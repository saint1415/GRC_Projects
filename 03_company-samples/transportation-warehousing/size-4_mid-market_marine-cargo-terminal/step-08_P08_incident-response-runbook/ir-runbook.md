# Incident Response Runbook: Ransomware Disrupting the Terminal Operating System

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed marine cargo terminal operator: Terminal 1, Terminal 2 and an off-dock depot in Florida) |
| Tier / Vertical | Mid-Market / Transportation and Warehousing |
| Incident type | Ransomware that encrypts TOS application servers, gate servers and office systems and stops vessel, yard and gate operations at both terminals and the depot, with possible theft of data first (double extortion). Assumed entry: a phished administrator credential used with one of the standing domain administrator accounts (P01 R-009). Mobile harbor crane controllers at T2 are at risk because they share a flat network with the T2 gate servers (R-002) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy. This runbook and `ir-runbook-ot-vendor-access.md` form the core of the Cyber Incident Response Plan required by 33 CFR 101.650(g)(2) (full plan due 2026-12-31, POAM-014) |
| Companion documents | `ir-runbook-ot-vendor-access.md` (unauthorized access to crane controllers through vendor remote access); `notification-matrix.csv`; BIA recovery order (P05 section 8); both FSPs (SSI) |
| Runbook owner | Director of IT and Cybersecurity (CySO), incident commander |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. TOS failover test 2026-11-07 (POAM-010); cyber drill with key personnel 2026-11-18 (POAM-014, POAM-029); executive tabletop with outside counsel in 2027-Q1 |
| Handling | SSI once contacts and network details are added (POL-04 4.2) |

## 0. Governance, roles and contacts (Govern)
The response runs on three tiers, so that technical, operational and business or legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, CySO, Vice President Terminal Operations, Director of Port Security, Director of Commercial and Customer Service, HR Director, outside breach counsel | Business continuity across sites, terminal closure or reduced working, external statements, contract notices, the ransom decision (recommendation to the CEO), resources |
| **Incident response team (IRT)** | Incident commander: CySO. Security Manager (alternate CySO), security analysts (including the OT analyst), OT network engineer, TOS Application Manager, MSSP, forensic firm (through counsel), TOS vendor and cloud provider support | Containment, investigation, eradication, recovery sequence, Coast Guard reporting |
| **Terminal operations command** | Vice President Terminal Operations; T1 and T2 General Managers; Depot Manager; Director of Maintenance and Engineering; T1 and T2 FSOs; shift superintendents | Manual working, crane and yard equipment safety, gate procedures, hazardous cargo control, MTSA security measures |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander and Coast Guard reporting | Director of IT and Cybersecurity (CySO) | Security Manager (alternate CySO) | CySO line (24x7 rota), then the out-of-band group |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Legal, privilege and breach determinations | General Counsel | Outside breach counsel (insurer panel) | Out-of-band group; insurer hotline |
| Cyber insurer | Carrier breach hotline ($15M aggregate limit, $500K retention) | Broker | Policy card in each incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | Security analysts on call | MSSP hotline |
| Terminal operations | Vice President Terminal Operations | T1 General Manager | Radio channel 1 and cell |
| OT safety and crane OEMs | Director of Maintenance and Engineering | Senior crane electrician on duty | Cell; OEM 24x7 service lines |
| MTSA security, TWIC access and NRC reports | T1 FSO (Director of Port Security) at T1; T2 Security Lead at T2 | Security supervisor on duty | Security office radio and cell |
| Customer and partner communications | Director of Commercial and Customer Service | Vice President Terminal Operations | Printed partner contact sheet |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | Chief Operating Officer | Phone |
| Law enforcement | FBI field office | CISA | Numbers in the binder |

**Out-of-band first.** Assume email, chat and the identity provider may be compromised. The CMT, IRT and terminal command use a pre-provisioned messaging group on personal phones, terminal radios and the printed call trees in the incident binders at both security offices, both gate complexes, the depot office and the T1 operations building.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions. Do not speculate in email or chat. **Coast Guard reporting under 33 CFR 6.16-1 does not wait for counsel** (POL-03 4.4).

## 1. Preparation checks (Identify / Protect)
- [x] Write-once TOS database backups in the separate backup account, 35-day retention, separate administrator credentials (CP-9; P07 30 of 30 job days)
- [x] EDR on all Windows endpoints and servers with 24x7 MSSP (SI-3; P07 fully satisfied)
- [x] Warm standby TOS database replica in a second region (CP-7)
- [ ] Failover to the standby region tested, and a TOS restore demonstrated within the 4-hour RTO (CP-4). **Gap until POAM-010 closes** (first test 2026-11-07)
- [ ] Hourly isolated TOS snapshots, so a corrupted replica does not force a 24-hour loss (POAM-010, 2026-11-30)
- [ ] T2 gate server images and T2 PLC programs held by the company (CP-9). **Gap until POAM-011 closes**
- [ ] No standing domain administrator accounts (AC-6). **Gap until POAM-002 closes**
- [x] Break-glass accounts for the identity provider and cloud sealed in the T1 and T2 FSO safes (POL-02 4.9); [ ] TOS and gate server break-glass accounts (due 2027-01-31, R-034)
- [ ] Printed dangerous cargo location list at both security offices at every shift change, and manual gate kits with pre-printed interchange forms at all lanes (POAM-009, 2026-10-31)
- [x] Pre-imaged spare laptops: 10 at T1, 4 at T2 (P05)
- [x] Incident binders at both security offices, both gate complexes, the depot and the T1 operations building: this runbook, call trees, the notification matrix, manual gate and vessel forms
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-15
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file renaming or encryption on any server or workstation | EDR alert; staff report | MSSP isolates the host (automatic for high-confidence detections) and calls the Security Manager within 30 minutes; staff call the CySO line. **Do not power off** |
| Backup deletion attempts, or EDR or logging being disabled | Cloud audit logs; EDR tamper alert; guardrail alert | Treat as a ransomware precursor; declare |
| New domain administrator, or privileged sign-in outside hours | SIEM; directory audit | Disable the account; declare if unexplained |
| TOS unavailable, or the TOS database stops accepting transactions | Planners, gate clerks, TOS vendor | CySO checks the cloud console and TOS vendor status; declare if encryption or unknown administrator activity is seen |
| OCR portals, kiosks or gate servers fail on all lanes at once | Gate supervisor | Treat as possible ransomware until ruled out |
| A crane, RTG or mobile harbor crane behaves unexpectedly, or HMIs show changed settings | Operator; mechanic | **Stop the equipment in a safe state** (POL-03 4.8); switch to `ir-runbook-ot-vendor-access.md` section 3 for the OT steps |
| Large outbound transfer from TOS, file shares or gate servers | Cloud firewall flow logs; MSSP | Block the destination; declare |
| Extortion email or leak-site post naming the company | Email; insurer; FBI | Declare; preserve the message |

**Severity 1 (declare immediately):** confirmed ransomware execution on any system, confirmed data theft, or an extortion claim naming company data. The incident commander declares it and records the **date and time of discovery and declaration** in the incident log (POL-03 4.3).

**Clocks start at evidence, not certainty.** 33 CFR 6.16-1 requires evidence of an actual or threatened cyber incident to be reported **immediately**. Florida's 30-day clock for personal information starts when the breach is determined (Fla. Stat. 501.171).

## 3. First 4 hours (RS.MA, RS.MI, RS.CO)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | **Safety first.** Stop crane, RTG and mobile harbor crane moves that depend on TOS data; hold hazardous cargo moves; superintendents informed by radio | Terminal operations command | Equipment in a safe state |
| 0-30 min | Isolate affected hosts through EDR (network containment); keep them powered on for memory evidence | MSSP; security analysts | Hosts contained |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log | CySO | Log open |
| 0-60 min | **Report under 33 CFR 6.16-1:** call the Captain of the Port for each affected terminal, the FBI field office and CISA. Give what is known now; update later. This also meets the Subpart F NRC duty (101.620(b)(7)) | CySO (alternate CySO or the terminal FSO if unreachable) | Report times and reference numbers in the log |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | General Counsel | Claim number; counsel on the call |
| 0-60 min | Protect the backup account: confirm write-once retention is intact; suspend cross-account backup jobs; rotate backup administrator credentials out of band; **pause replication to the standby region** if the primary database is affected | CySO with the TOS Application Manager | Backup and replica integrity confirmed |
| 0-2 h | Isolate sites: drop SD-WAN tunnels from affected sites to the cloud hub; disconnect the T2 gate and yard switch from the T2 office network; **power off the T2 OEM cellular appliance**; confirm the T1 OT zone firewall allows only the TOS equipment interface, then block it until OT is checked | OT network engineer with the MSSP | Routes down or filtered; OT has no path to IT |
| 0-2 h | Revoke all identity provider sessions; reset privileged credentials from a clean device using break-glass accounts; disable all vendor remote access in the privileged remote access service | Security Manager | Sessions revoked; vendor access off |
| 0-2 h | Start manual working (P05): manual gate on 3 T1 lanes with the printed release list; T2 and depot gates on paper; radio dispatch; paper tally; printed dangerous cargo list to both security offices and the port fire departments; manual TWIC checks if PACS is affected | Terminal operations command; FSOs | Manual procedures running |
| 1-2 h | Convene the CMT; first situation report (scope, safety, vessels at berth, gate queues, decisions needed) | CMT chair | CMT meeting held |
| 1-2 h | Tell port partners that EDI and the gates are suspended and that messages received after the declaration time are not trusted until verified (both port authorities, carriers with vessels due, port community systems, customs data exchange, trucking companies by portal banner or email from a clean account) | Director of Commercial and Customer Service | Partners called from the printed list |
| 2-4 h | Staff and longshore briefing script: what happened, manual procedures, do not discuss externally, report anything unusual to the CySO line | HR Director with the terminal General Managers | Script read at shift briefings and sent by text |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Scope.** Which TOS servers, gate servers at each site, OCR servers, endpoints, cloud accounts and identities are affected? Use EDR telemetry, identity provider and directory logs, cloud control-plane logs in the locked log bucket, firewall flow logs and SD-WAN logs.
2. **Initial access and dwell time.** Identify the phished account, the first use of a domain administrator account, the first host reached and the date the attacker first got in. Check for other accounts used from the same source. Where T2 gate server logs are missing (they are local and deletable until POAM-005 closes), export what remains in the first hour.
3. **Preserve evidence.** Forensics images key hosts, takes memory captures and keeps cloud snapshots of affected disks, with chain of custody (who collected, when, hash, storage). Evidence is held by the forensic firm under counsel.
4. **OT check (both terminals).** With the OEMs, compare PLC programs and HMI settings with known-good copies: T1 from the offline copies in the Maintenance and Engineering safe; T2 from the OEM until the company holds its own copies (POAM-011). Look for new connections to controllers from the gate and yard networks. **No crane, RTG or mobile harbor crane returns to TOS-directed work until the Director of Maintenance and Engineering signs off this check.**
5. **Data taken?** Look for archive tools, staging directories, large outbound transfers and cloud storage access. Build an **affected data list**, because it drives every notice:
   - truck driver names and driver license numbers in the TOS gate module (Fla. Stat. 501.171);
   - employee records (HR SaaS exports, file shares);
   - SSI: FSP or FSA extracts, network maps, assessment findings (49 CFR 1520.9(c));
   - cargo, customs status and customer data (commercial harm; contract notices).
6. **Backups and replica.** Before restoring anything, confirm that the write-once copies (and the hourly snapshots, once live) are intact, check whether corruption replicated to the standby, and identify the **last clean restore point** before the attacker's first access.
7. **Security impact.** Each FSO decides whether an FSP security measure was circumvented (a breach of security) and whether the disruption could become a TSI (33 CFR 101.305).

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at site firewalls, SD-WAN and the cloud firewall.
2. Disable compromised accounts. Rotate every administrator, service, integration and vendor credential, including EDI partner credentials, port community system and customs data exchange API keys, the scheduling optimization API key, and the TOS vendor support account.
3. **No standing domain administrator rights after recovery.** Use the break-glass accounts until privileged access management is in place (POAM-002); record every use.
4. Rebuild affected endpoints, gate servers and OCR servers from clean images and patch them. **Do not decrypt and reuse compromised systems.** T2 gate servers have no images today: rebuild from vendor media with the TOS vendor (days of work; P05 finding 2).
5. Rebuild TOS application servers from clean images in an isolated recovery network. Restore the database to the last clean point.
6. Keep OT disconnected from IT until the OT check (4.4) is signed off and a temporary firewall rule allows only the TOS equipment interface. At T2, reconnect mobile harbor cranes only through a temporary firewall placed between the gate and crane segments.
7. Forensics confirms that persistence (scheduled tasks, remote tools, rogue accounts, group policy changes) is removed before reconnection.

## 6. Legal, regulatory and external communication (RS.CO)
**Follow `notification-matrix.csv`.** The General Counsel keeps the **decision log** (POL-03 4.5). Outside counsel confirms every notice except the Coast Guard report, which is made immediately.

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Was the 6.16-1 report made to the COTP for each affected terminal, the FBI and CISA? (If not, report to the NRC without delay) | CySO | Incident log with times and reference numbers |
| D2 | Was an FSP security measure circumvented (breach of security), or is this a TSI? | Terminal FSO with the terminal General Manager and the COTP | FSO records (105.225(b)(3)) |
| D3 | Was SSI released to unauthorized persons? If so, inform TSA or the Coast Guard promptly (1520.9(c)) | FSO with the CySO | Decision log |
| D4 | Is this a breach of personal information under Fla. Stat. 501.171? Date of determination (starts the 30-day clock) | General Counsel with outside counsel | Decision log |
| D5 | How many Florida residents are affected, and who lives in other states? (500 or more: Department of Legal Affairs; more than 1,000: consumer reporting agencies; other states: each state's law) | General Counsel | Affected individuals list by state |
| D6 | Has law enforcement asked in writing for a delay of individual notice? | General Counsel | Copy of the written request |
| D7 | Which contract notices are due (carrier alliance within 24 hours; leases; customers)? | General Counsel with the CFO | Contract register |
| D8 | Ransom decision | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Immediately (first hour) | 6.16-1 report to the COTPs, FBI and CISA | CySO |
| Without delay, if applicable | NRC report of a breach of security or suspicious activity; TSI report to the COTP per the FSP (101.305) | Terminal FSO |
| Hour 0-1 | Insurer hotline; counsel engaged | General Counsel |
| Within 24 hours | Carrier alliance notice under its agreement; daily updates while services are affected | Director of Commercial and Customer Service through counsel |
| Day 0, then twice daily | Port partner and trucking updates (portal banner, email from a clean account) | Director of Commercial and Customer Service |
| As facts develop | Updates to the COTPs and the FBI; answer COTP questions on terminal status and hazardous cargo | CySO; FSOs |
| Promptly | SSI disclosure report, if D3 is yes | Terminal FSO |
| As soon as scoped | Breach determination documented (D4) | General Counsel |
| No later than 30 days after determination | Florida individual notices (15 more days only with written good cause to the Department within the 30 days); Department of Legal Affairs notice if 500 or more Floridians | General Counsel with outside counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at once | Outside counsel |
| Each other state | Residents of other states: apply the law of each state where affected individuals reside | Outside counsel |
| Throughout; kept 2 years | Incident record (101.640; 105.225(b)(3)) | Terminal FSOs |

**Ransom decision (POL-03 4.7).** Needs the CEO after advice from counsel and the insurer, an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis), and notice to the audit committee chair. Paying does not remove any reporting or notice duty and does not guarantee deletion of stolen data. The default position, approved by the CEO, is not to pay while the write-once backups are intact.

**CIRCIA is not in effect** (final rule not published as of 2026-09-25), so there is no 72-hour or 24-hour CIRCIA report today. Recheck when the final rule is published. The company is privately held, so there is no Form 8-K duty.

**Communications.**
- Carriers and T2 customers: a direct call from the Vice President Terminal Operations or the T1 or T2 General Manager for every vessel due in the next 72 hours, with a revised berth plan.
- Trucking companies: portal banner and recorded gate hotline message within 2 hours of any gate stoppage; appointment rebooking rules.
- Media: holding statement approved by counsel; no technical details, ransom, attribution or security measure details (SSI).
- Staff and longshore labor: shift briefings and text updates through the out-of-band channel only.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 8). Each step is validated before the next begins: EDR clean, credentials rotated, patches applied, and forensics sign-off for the segment.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Identity provider and break-glass administrator access | 1 h | Sessions revoked; privileged credentials rotated |
| 2 | Firewalls, SD-WAN and core networks, with OT zones isolated | 2 h | Clean segments only; T2 temporary firewall between gate and crane segments |
| 3 | PACS and TWIC readers; printed dangerous cargo lists | 2 h | FSOs confirm access control; manual TWIC checks until then |
| 4 | TOS database and application servers (failover or restore from the last clean point) | 4 h target (6.5 h demonstrated in 2026-04) | TOS vendor integrity checks; test transactions |
| 5 | Clean operations endpoints and gate booth workstations | 4 h | Pre-imaged spares; EDR healthy |
| 6 | Crane and RTG controllers at T1, then mobile harbor cranes at T2, reconnected to the TOS | 4 h (T1); 1 to 3 days (T2 today) | Director of Maintenance and Engineering and OEM sign-off on program and settings comparison |
| 7 | Gate automation: T1 first, then T2 and the depot | 3 h (T1); 8 h (T2) | Gate test transactions; OCR accuracy check |
| 8 | EDI gateway and the customs data exchange feed | 8 h | Credentials rotated; test messages with each partner |
| 9 | Customer portal and truck appointments | 6 h | Web application firewall rules re-applied; test bookings |
| 10 | SIEM feeds and EDR console | 8 h | Monitoring confirmed before wider reconnection |
| 11 | Finance, payroll and billing | 48 to 72 h | Restore; permissions review |
| 12 | Scheduling optimization service (AI-001) | Not required | Reconnect last, with a new scoped API key, only after a security review (P10) |

**Validate before resuming normal operations:**
- **Reconcile the TOS with reality.** Compare the restored inventory with a physical yard check (2 shifts at T1), paper gate interchanges and carrier bay plans. Moves made during manual working must be keyed in before automated dispatch restarts.
- **Customs holds first.** Refresh release and hold status from the customs data exchange before any import container leaves by an automated gate (33 CFR 105.265(a)(7)).
- **Hazardous cargo.** Each FSO confirms that TOS dangerous cargo locations match the printed list and a yard check.
- **Clean systems only.** EDR clean, credentials rotated, systems patched, no standing administrator rights.

Tell staff, both COTPs, the carrier alliance and port partners when each service is back (RC.CO). Keep manual procedures running until each process is within its RTO (P05).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.13).
- Update the risk register (P01: R-001, R-002, R-004, R-009, R-017), the POA&M (P07), this runbook, the contingency plan and the Cybersecurity Plan (101.650(g)(3)).
- Record the incident and every report made, and keep the records for at least 2 years, protected against amendment (POL-01 4.11; 101.640). Keep the breach decision log for at least 5 years where a no-notice determination was made (Fla. Stat. 501.171(4)(c)).
- Add the incident to the next annual cyber training and the next drill or exercise (101.635).
