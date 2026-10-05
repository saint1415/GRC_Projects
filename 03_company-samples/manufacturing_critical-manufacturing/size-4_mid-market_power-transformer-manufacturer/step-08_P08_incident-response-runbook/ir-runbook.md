# Incident Response Runbook 1: Ransomware Disrupting Production of Grid Equipment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed power and distribution transformer manufacturer, Florida) |
| Tier / Vertical | Mid-Market / Critical Manufacturing |
| Incident type | Ransomware, with possible data theft, that encrypts office systems and the ERP and spreads to a plant (most likely Plant 2, through its flat network, dual-homed MES, and domain trust), stopping transformer production during hurricane season |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions, with OT response guidance from NIST SP 800-82 Rev. 3 section 6.4 |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-product-compromise.md` (compromise of products or services supplied to utilities); `notification-matrix.csv`; BIA (P05); risk register (P01 R-001, R-002, R-006, R-051) |
| Runbook owner | Security Manager (incident commander), with the OT Security Engineer and the Director of Manufacturing Engineering for the OT sections |
| Approved | 2026-09-15 by the Chief Operating Officer; effective 2026-10-01 |
| Last tested | Not yet. Crisis management tabletop with outside counsel 2026-11-12; Plant 2 OT tabletop 2026-11-19 (POAM-011) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so that technical, plant, and business and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: COO. CEO, CFO, General Counsel, vCISO, Security Manager, IT Director, Director of Manufacturing Engineering, Director of Digital Services, VP Sales, Director of Marketing and Communications, HR Director; outside breach counsel | Business continuity, customer and storm-order commitments, external statements, the ransom recommendation to the CEO, spending |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director (recovery lead), OT Security Engineer (OT lead), security analysts, MSSP, forensic firm and OT-capable response firm (through counsel), cloud and ERP vendor contacts | Containment, investigation, eradication, recovery sequence |
| **Plant command** | Director of Manufacturing Engineering; Plant 1 and Plant 2 Managers; both Controls Leads; Director of Quality | Safe state, manual operations, restart approvals, test data integrity |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on personal phones; printed call tree |
| OT incident lead | OT Security Engineer | Director of Manufacturing Engineering | Out-of-band group; plant radio |
| Safe-state decisions | Plant Manager at the affected plant | Shift supervisor on duty | Plant radio; cell |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Legal and notices | General Counsel | Outside breach counsel (insurer panel) | Out-of-band group |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card in the incident binder |
| Forensics and OT response | Panel forensic firm and panel OT-capable response firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Customer communications | VP Sales (utilities and developers); Director of Digital Services (FMS subscribers) | COO | Cell |
| Utility notices | General Counsel; Contracts and Trade Compliance Manager prepares | Director of Field Service (access notices) | Cell |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume email, chat, VoIP, and the identity provider may be compromised. The CMT and IRT use a pre-provisioned messaging group on personal phones and printed call trees kept in the incident binders at HQ, Plant 1, Plant 2, and with the OT Security Engineer.

**Legal privilege protocol.** Outside counsel engages the forensic and OT firms and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel." Keep facts (timeline, logs) separate from legal conclusions. Do not speculate in email or chat.

## 1. Preparation checks (Identify / Protect)
- [x] Immutable ERP, FMS, and PLM backups in the backup account, second region, 35-day write-once retention, separate credentials (CP-9; P07)
- [x] EDR on all IT endpoints and servers with 24x7 MSSP (SI-3; P07)
- [x] Plant 1 OT DMZ, documented isolation point at the Plant 1 IT/OT firewall, nightly controller backups with weekly offline copies
- [ ] Plant 2 isolation points documented and labeled (unplug the MES office interface; block the Plant 2 site firewall uplink). **Gap until 2026-11-30 (POAM-001)**
- [ ] Verified offline copies of Plant 2 PLC, HMI, and CNC programs and recipes. **Gap: hand copies from 2026-04 (POAM-006; P01 R-006)**
- [ ] Full ERP restore tested within the last 90 days. **Gap: first full test 2026-10-27 (POAM-005)**
- [ ] Break-glass accounts sealed and tested for the identity provider, cloud organization, and corporate directory (POL-02 4.11). **First quarterly test 2026-10-15**
- [ ] Plant 2 domain trust one-way (POAM-002, due 2026-10-31)
- [x] Incident binders at HQ, Plant 1, and Plant 2: this runbook, call tree, notification matrix, the 31 utility security contacts, paper traveler kits, oven safe-state procedures
- [x] Insurer panel counsel, forensic firm, and OT-capable firm confirmed 2026-08-20
- [x] Printed 5-day production schedule per plant refreshed daily during storm season (P05 BP-01)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renaming or encryption on any server or PC | EDR alert; staff report | MSSP isolates the host (automatic for high-confidence detections) and calls the incident commander within 30 minutes. **Do not power off** |
| HMI locked, showing a ransom note, or behaving on its own (setpoints or recipes changing) | Operator; shift supervisor | Operator steps back and calls the shift supervisor, who calls the Controls Lead and the Plant Manager. **Do not touch the controls** |
| Kiosks or the MES stop responding across a bay | Shift supervisor | Call the incident line; switch to paper travelers |
| New Domain Admins members, use of the Plant 2 MES service account, or Kerberos anomalies across the trust | SIEM; MSSP | Disable the account; cut the trust; declare if unexplained |
| Backup deletion attempts, disabling of EDR or logging, or new cloud administrator roles | Cloud audit logs; EDR tamper alert | Treat as a ransomware precursor; declare |
| Large outbound transfers from the PLM vault, file servers, or the ERP account | Cloud hub egress alerts; firewall logs | Block the destination; declare |
| Extortion email or leak-site post naming the company | Email; threat intelligence; FBI | Declare; preserve the message |

**Severity 1 (declare immediately):** confirmed ransomware execution on any server or plant system, any unauthorized change on a plant controller or HMI, confirmed data theft, or an extortion claim naming company data. The Security Manager declares for IT; the OT Security Engineer declares for OT (POL-03 4.3).

**Record the time of declaration in the incident log.** Several clocks can start from decisions made in the first days:
- utility addendum notices run from **confirmation** that the incident relates to products or services supplied (24 or 48 hours; decision D2);
- FMS subscriber notice runs from confirmation of an incident affecting subscriber data (72 hours);
- the Florida 30-day notice runs from **determination** of a breach of employee or applicant personal information (decision D3).

## 3. First 4 hours: safety, isolation, and calls (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | **Safe state.** At each affected plant the Plant Manager decides per area. *Drying ovens:* if the local PLC runs normally, let the cycle finish under operator watch at the panel; otherwise follow the oven safe-shutdown procedure. *Oil processing:* stop. *Test bay:* stop tests and de-energize. *Winders, core lines, cranes:* stop at the end of the current operation | Plant Manager; Controls Lead; oven operators | Every area in a known safe state, logged with times |
| 0-30 min | **Isolate the plants.** Plant 1: block all rules at the IT/OT firewall (the OT DMZ keeps plant zones apart). Plant 2: unplug the MES office interface and block the Plant 2 site firewall uplink; power off the 4 OEM routers; disconnect the 2 unmanaged access points | OT Security Engineer; Controls Leads | No path from office or internet to plant zones |
| 0-30 min | **Isolate IT and the cloud.** MSSP contains affected hosts (keep them powered on for memory evidence). Cut the Plant 2 domain trust. Sever SD-WAN routes from affected sites to the cloud hub. Disconnect the integration platform from both MES instances | Security Manager; IT Director; MSSP | Spread stopped; ERP account reachable only from clean admin workstations |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages the forensic and OT-capable firms | Chief Financial Officer | Claim number; counsel on the call |
| 0-60 min | **Protect the backup account:** confirm write-once retention is intact; suspend cross-account copy jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-2 h | Revoke all identity provider sessions; reset privileged credentials with the break-glass accounts; rotate the Plant 2 MES service account and integration credentials; disable vendor remote access | Security Manager | Sessions revoked; credentials rotated |
| 0-2 h | **Go manual.** Paper travelers and printed schedules at both plants; hold new work order release | Production Planning Manager; shift supervisors | Paper workflow running |
| 1-2 h | Convene the CMT; first situation report (scope, safety, plants down, storm orders at risk, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Staff briefing by shift: what happened, manual procedures, report anything unusual, do not post online | Plant Managers with HR | Briefing given at each shift |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Scope.** Which servers, PCs, HMIs, controllers, kiosks, cloud workloads, and identities are affected? Sources: EDR, identity provider and directory logs, cloud control-plane logs in the locked archive, firewall and SD-WAN logs, the Plant 1 OT sensor, and a walk-down of every Plant 2 HMI and engineering workstation (no Plant 2 logs exist centrally until POAM-007 closes).
2. **Controllers.** Did the attacker reach PLCs or only HMIs? Controls Leads compare controller programs and recipes with the verified copies (Plant 1 OT backup server; Plant 2 laptop copy until POAM-006 closes). The OT-capable firm assists. **No controller is trusted until checked.**
3. **Initial access and dwell time.** Check phishing, VPN, OEM routers, the Plant 2 domain trust, the integration platform, the AI-002 connector, and MSSP and vendor tools.
4. **Preserve evidence** before any wipe (POL-03 4.11): memory and disk images of key servers, HMI images, controller program uploads, and firewall, VPN, router, and cloud logs, with chain of custody (who collected, when, hash, storage). Evidence is held by the forensic firm under counsel.
5. **Exfiltration.** Were designs, customer substation drawings, FCI, FMS data, or employee and applicant personal information taken? Check egress logs, archive tools, staging folders, and leak-site samples. Build the **affected data list** by type, customer, and (for personal information) state of residence.
6. **Products and services.** Were the TMU configuration software, signing key, firmware library, field laptops, saved utility credentials, or the FMS touched? **This decides whether the incident is "related to products or services supplied" under the addenda (decision D2).** If yes, also run `ir-runbook-product-compromise.md`.
7. **Backups.** Confirm the restore points in the backup account predate the attacker's first access.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at site firewalls, SD-WAN, and the cloud hub.
2. Disable compromised accounts. Rotate service account, integration, EDI, and vendor credentials. Rotate every shared HMI, supervisor, and test PC password (POAM-004).
3. **Rebuild, do not decrypt and reuse.**
   - Office PCs and servers: rebuild from standard images.
   - Cloud workloads: rebuild from templates in a clean recovery account, then restore data from the backup account.
   - Plant 2 MES: rebuild single-homed on the plant side; no office interface.
4. **HMIs and engineering workstations:** reimage from OEM media with OEM help, then load verified project files. Unsupported operating systems (19 at Plant 2) may need OEM media or replacement units (P01 R-009).
5. Retire the Plant 2 domain trust permanently if it was used.
6. The forensic and OT firms confirm that persistence is removed from IT, cloud, and OT before recovery starts.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel reviews every external notice before it goes out. The General Counsel keeps the **decision log** (POL-03 4.6).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Severity and whether to convene the CMT | Incident commander; CMT chair | Incident log |
| D2 | Is the incident related to products or services supplied to a utility (configuration software, firmware, field access, FMS)? If yes, which of the 31 addendum utilities, and does each have a 24- or 48-hour term? | General Counsel with the VP Engineering and the Director of Digital Services | Decision log with the time of confirmation |
| D3 | Was personal information of employees or applicants accessed (Florida and other states)? Date of determination | General Counsel with counsel | Decision log; affected list by state |
| D4 | Are FMS subscriber data affected (72-hour contract notice)? | Director of Digital Services with the General Counsel | Decision log |
| D5 | Do any federal deliveries slip? Was covered equipment or a covered article found during rebuild (FAR 52.204-25, -23, -30)? | Contracts and Trade Compliance Manager | Decision log |
| D6 | Has law enforcement asked for a delay? | Counsel | Decision log |
| D7 | Ransom decision | CEO, on the CMT's recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel and response firms engaged | CFO |
| Hour 0-24 | Audit committee chair and PE sponsor informed | CEO |
| Day 0-1 | Voluntary report to the FBI (IC3 or field office) and CISA. Supports OFAC mitigation and is the path CIRCIA would formalize | Security Manager through counsel |
| **Within 24 hours of confirmation (9 utilities) or 48 hours (22 utilities)** | Incident notice to each affected addendum utility if D2 is yes. If in doubt, counsel decides early; the deadlines are contract terms | General Counsel |
| Within 1 business day | Access-revocation notice to each utility where an exposed field technician credential exists | Director of Field Service |
| Within 72 hours of confirmation | FMS subscriber notice if D4 is yes | Director of Digital Services |
| Day 1-3, then daily | Delivery-impact updates to utilities with storm-restoration orders and other affected customers; delivery update to the federal contracting officers | VP Sales; Contracts and Trade Compliance Manager |
| Within 1 business day / 3 business days | FAR 52.204-25(d) report if covered equipment is identified; FAR 52.204-23(c) or 52.204-30(c)(3) report if a covered article is identified | Contracts and Trade Compliance Manager |
| Within 30 days of determination | Florida notice to affected individuals; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000; other states per their laws | HR Director and General Counsel |
| Within 30 days of knowing | Disclosure to addendum utilities of any vulnerability found in supplied software or firmware | VP Engineering |

**Not required:**
- **No CIRCIA report is required.** The rule is proposed only; report voluntarily instead.
- **No DFARS report.** The company has no DoD work.
- **No FAR 52.204-21 incident report.** The clause has no reporting paragraph.
- **No SEC filing.** The company is privately held.

**Ransom decision (POL-03 4.10).** Needs the CEO, counsel, and the insurer, an **OFAC sanctions check** on the threat actor and any wallet, and a report to law enforcement. Paying does not remove any notice duty and does not guarantee deletion of stolen data. The default position, approved by the CEO, is not to pay while backups are intact and the plants can run manually.

**Storm season.** If a hurricane watch covers a utility customer's service area during the incident, the VP Sales tells that utility the realistic ship dates for its reserved storm units within 24 hours. This is a business commitment, not a legal deadline.

**Communications.**
- Utilities and developers: direct calls from the VP Sales or the COO, then written updates.
- FMS subscribers: status page and direct contact from the Director of Digital Services.
- Media: holding statement approved by counsel; no technical details, ransom, or attribution comments.
- Staff: shift briefings and the out-of-band channel only.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7). **No plant equipment restarts until the Controls Lead has verified its programs and settings and the Plant Manager approves (POL-03 4.4).** Each step is validated before the next: EDR or allowlisting healthy, credentials rotated, patches applied, and forensic and OT firm sign-off for the segment.

| Order | Resource | Target (BIA) | Validation |
|---|---|---|---|
| 1 | Drying ovens and oil processing at both plants (BP-03, BP-06) | 12 h | PLC programs and recipes match verified copies; HMI restored; Plant Manager approves restart |
| 2 | Identity provider, corporate directory, administrator access (break-glass if needed); Plant 2 trust stays off | 2 h | Sessions revoked; privileged credentials rotated |
| 3 | SD-WAN, site firewalls, cloud hub; IT/OT firewalls rebuilt deny-by-default | 4 h | Only flows needed now are open |
| 4 | FMS (BP-14), in its own account | 8 h | Restored from pre-compromise backup; subscribers told when alerting resumes |
| 5 | SIEM feeds and EDR console | 8 h | Monitoring confirmed before wider reconnection |
| 6 | Test systems (BP-04, BP-07) | 12 h (Plant 1), 24 h (Plant 2) | Unique accounts; the Director of Quality checks raw data against printouts before signing any certified test report; retest where in doubt |
| 7 | Field laptops and contact lists (BP-13) | 12 h | Reimaged; utility credentials not saved |
| 8 | ERP and APS (BP-01) | 24 h | Restored from the backup account into a clean account; orders, receipts, and shipments made on paper reconciled |
| 9 | MES (Plant 1 from its OT DMZ backup; Plant 2 rebuilt single-homed) | 24 h | Paper traveler confirmations re-entered |
| 10 | Integration platform | 24 h | Reconnected to each MES only through the restricted path |
| 11 | Core and winding HMIs (BP-02, BP-05) | 24 h (Plant 1), 48 h (Plant 2) | Manual recipe entry with an engineering double-check until then |
| 12 | Firmware library and configuration software (BP-10) | 48 h | Rebuilt from the verified offline copy; every hash re-verified before any firmware is loaded at final test |
| 13 | PLM vault (BP-09) | 48 h | Design files verified against release records |
| 14 | EDI (BP-11, BP-12) | 48 h | Credentials rotated; test transactions accepted |
| 15 | Tank fabrication (BP-08), finance (BP-16), payroll and HR (BP-17) | 72 h | Restore; permissions review |

**Communicate restoration (RC.CO):** tell staff by shift; tell utilities, FMS subscribers, and the contracting officers when production, deliveries, and alerting resume.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.13).
- Update the risk register (P01: R-001, R-002, R-006, R-051), the POA&M (P07), this runbook, and the contingency plan.
- Declare the end of recovery when every High-criticality process is back within its RTO and monitoring is restored (RC.RP-06).
- Retain the incident log, decision log, notices, and evidence for at least 5 years, or longer if counsel or a contract requires.
