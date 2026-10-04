# Incident Response Runbook: Ransomware on Farm-Management and Irrigation Control Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed diversified precision-agriculture crop farm with a central packinghouse and a Grower Services unit) |
| Tier / Vertical | Mid-Market / Agriculture, Forestry, Fishing and Hunting |
| Incident type | Ransomware on the Farm Management and Irrigation Control Platform (FMICP), entering through the SCADA integrator's remote access, with theft of HR, H-2A, and grower data (double extortion) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions; OT steps follow NIST SP 800-82 Rev. 3 sections 6.4 and 6.5 |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-ot-integrity.md` (unauthorized change to fertigation, irrigation, ripening, or cold-chain controls); `notification-matrix.csv`; BIA (P05); food safety recall plan; Farm 2 freeze-night procedure (STD-07) |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-15 by the Chief Operating Officer; effective 2026-10-01 |
| Last tested | Not yet. Executive and operations tabletop with outside counsel, the SCADA integrator, and the FMIS vendor scheduled 2026-11-10 (POAM-014) |

**Scenario used to write this runbook.** A Tuesday in late March, at the peak of tomato and strawberry harvest, in a dry week. At 04:50 the IOC night operator finds a ransom note on 2 HMIs. The SCADA servers will not open, and the historian has stopped. Pumps keep running on the PLCs' last schedules. By 06:00 office laptops at headquarters and the Farm 1 office are encrypted, the farm data hub will not start, and the grower portal returns errors on settlement day. An email to the CEO claims the attackers hold "your workers' passports and your growers' bank files." Forensics later finds the attacker used the SCADA integrator's always-on remote tool and shared account (P01 R-002), moved from the SCADA server to the office network, and copied the personnel share and settlement exports before encrypting (R-001, R-003).

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so that technical, operational, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, vCISO, Director of Food Safety and Quality, HR Director, Vice President of Grower Services, Director of Sales, Communications Manager, outside breach counsel | Business continuity, product holds with food safety, external statements, contract notices, ransom recommendation to the CEO, spending |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director (IT recovery lead), 2 security analysts, MSSP, panel forensic firm (through counsel), FMIS vendor, cloud and identity vendor contacts | Containment, investigation, eradication, IT recovery sequence |
| **Operations command** | Director of Irrigation and Water Resources (chair), Packinghouse Manager, 3 Farm Managers, Director of Food Safety and Quality, SCADA integrator field engineer (on site only) | Manual irrigation, freeze protection, packing and cold chain, harvest on paper, safe return to automatic control |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Operations command chair | Director of Irrigation and Water Resources | Farm Manager (Farm 2) | Irrigation radio channel and cell |
| Breach decisions (workers) | HR Director with outside breach counsel | vCISO | Out-of-band group |
| Breach decisions (growers, customers) | Vice President of Grower Services and Director of Sales with counsel | Controller | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel) | Company's outside general counsel | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($10 million limit, $250,000 retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Communications | Communications Manager | Outside crisis PR (through counsel) | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume email, chat, VoIP, and the integrator's remote tool are compromised. The CMT, IRT, and operations command use a pre-provisioned messaging group on personal phones, the irrigation radios, and printed call trees kept in incident binders at headquarters, the IOC, the packinghouse, and each farm office.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel." Keep facts (timeline, logs) separate from legal conclusions, and do not speculate in email or chat.

## 1. Preparation checks (Identify / Protect)
- [x] Write-once backups of the operations and Grower Services accounts in a separate backup account, 35 days, separate credentials; July 2026 restore test passed (CP-9; P07)
- [x] EDR on all laptops and desktops with 24x7 MSSP monitoring and 30-minute escalation (SI-3, IR-4; P07)
- [ ] Offline, verified copies of all 68 PLC and HMI programs and both SCADA server images (CP-9). **Gap until POAM-010 closes (2026-12-31)**
- [ ] Integrator remote tool removed; vendor access only through the broker (AC-17). **Gap until POAM-003 closes (2026-12-31)**
- [ ] Restore test of SCADA, the farm data hub, and the grower portal within the last 90 days (CP-4). **Gap: first test 2026-10-21 (POAM-011)**
- [ ] Freeze-night manual start procedure written and drilled (POAM-012, due 2026-11-30)
- [ ] Break-glass accounts sealed and tested for the identity provider, cloud, SYS-01, and SCADA (POL-02 4.12)
- [x] Incident binders at every site: this runbook, the OT integrity runbook, call trees, paper tally cards (English and Spanish), paper pesticide application and Produce Safety forms, pre-printed lot labels, manual irrigation schedules, and the notification matrix
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-15
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renaming or encryption, on any laptop, server, HMI, or line PC | EDR alert; staff report; IOC operator | MSSP isolates IT hosts (automatic for high-confidence detections) and calls the incident commander within 30 minutes. **IOC operators do not power off HMIs or SCADA servers**; they unplug the network uplink and call the incident phone |
| A pump, pivot, valve, or injection skid starts, stops, or changes rate when nobody scheduled it | IOC operator; Irrigation Technician; SYS-01 irrigation alerts | Put the equipment in Hand at its panel; follow `ir-runbook-ot-integrity.md` in parallel |
| Integrator remote tool session that nobody requested | IOC operator; SCADA server | End the session; disable the tool; declare |
| Backup deletion attempts, or disabling of EDR or logging | Cloud audit logs; EDR tamper alert | Treat as a ransomware precursor; declare |
| Large outbound transfer from the personnel share, the settlement database, or the imagery data lake | Cloud firewall flow logs (egress alerts due 2027-01-31, POAM-020) | Block the destination; declare |
| Extortion email or leak-site post naming the company, workers, or growers | Email; threat intelligence; FBI | Declare; preserve the message |
| Grower portal, ERP, or EDI unavailable across sites | Staff and grower reports | IT triage; declare if malicious |

**Severity 1 (declare immediately):** any confirmed ransomware execution, confirmed theft of worker or grower personal data, an extortion claim naming company data, or any unexplained OT command (POL-03 4.4).

**Record two times in the incident log** (POL-03 4.3): when the incident was discovered, and, later, when the company determined (or had reason to believe) that personal information was accessed. Florida's 30-day notice clocks run from the determination (Fla. Stat. 501.171(3)-(4)), and retail customer notice runs 24 hours from awareness (contract).

## 3. First 4 hours (RS.MA, RS.MI): safety and crops first
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | **Put irrigation and fertigation in a safe state.** Switch each running well pump, injection skid, and pivot to Hand or Off at its panel per the manual schedule; **stop all fertigation injection and close injection valves**; confirm pressures and flows at the meter faces. Farm 3 pivots: switch to local control at the pivot panel | Director of Irrigation with Irrigation Technicians | All pumps and pivots under local control; injection off |
| 0-30 min | **Packinghouse and cold chain.** Switch cooling tunnels, cold rooms, and ripening rooms to local controller operation at the last known-good setpoints; start hourly manual temperature rounds on paper; hold ripening room ethylene cycles until setpoints are verified | Packinghouse Manager | Rooms on local control; first round logged |
| 0-30 min | Isolate affected IT hosts through EDR; unplug HMIs and SCADA servers from the network but **keep them powered on** for memory evidence; open the headquarters and packinghouse IT/OT firewalls to deny all | MSSP; IT Director | Hosts contained; OT isolated |
| 0-30 min | Disable the integrator's remote tool account and tell the integrator by phone: **no remote connections until further notice**; suspend pivot manufacturer support access | Security Manager | Vendor access off; integrator acknowledged |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log | Incident commander | Log open |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | Chief Operating Officer | Claim number; counsel on the call |
| 0-60 min | Protect the backup account: confirm write-once retention is intact; suspend cross-account backup jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-2 h | Revoke all identity provider sessions; reset privileged credentials from a clean device using break-glass accounts; rotate SYS-01 integration keys and the grower portal's bank file credentials | Security Manager | Sessions revoked; keys rotated |
| 0-2 h | **Paper operations.** Tally cards to crew leads; paper pesticide application forms (display within 24 hours still applies); pre-printed lot labels and paper receiving logs at the packinghouse; phone and email orders from the top 10 customers | Farm Managers; Food Safety Coordinators; Packinghouse Manager; Director of Sales | Paper workflows running |
| 1-2 h | Convene the CMT; first situation report (scope, crop and product risk, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Staff briefing in English and Spanish: what happened, paper procedures, whom to call, do not discuss outside the company | Communications Manager with HR and the Farm Managers | Script read at each site and sent by text |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

**Freeze season (December to February).** If the incident starts in freeze season, the Farm 2 Farm Manager staffs the freeze-night crew on site each night and starts the 14 Farm 2 pumps by hand from the standalone thermometer alarm (STD-07 freeze procedure). SCADA automation and the alarm dialer are not trusted until section 7 step 6 is complete. The BIA MTD for freeze protection is 2 hours (P05 BP-02).

## 4. Analysis (RS.AN)
1. **Scope.** Which endpoints, SCADA servers, HMIs, cloud accounts, SaaS tenants, and identities are affected? Use EDR telemetry, identity provider sign-in logs, cloud control-plane logs in the locked log archive, firewall flow logs, and the remote tool's history on the SCADA servers. **Export SCADA and historian logs now**: they are kept only 90 days on the server.
2. **Initial access and dwell time.** Confirm the entry point (the integrator tool, a phished credential, or an exposed appliance), the first compromised host, and the date the attacker first got in.
3. **OT integrity.** Did the attacker change PLC logic, setpoints, schedules, fertigation recipes, ripening programs, or cold storage setpoints? Compare PLC programs with the company-held approved copies by hash (where POAM-010 copies exist) and ask the integrator for its copies of the other programs. **If any fertigation, ripening, or cold-chain setting may have changed, run `ir-runbook-ot-integrity.md` sections 4 and 6 for the affected blocks, rooms, and lots.**
4. **Exfiltration.** Determine what was taken: personnel and H-2A files (Social Security, passport, and visa numbers, home-country addresses), biometric templates, payroll exports, grower bank details and settlement data, online customer accounts. Look for archive tools, staging folders, cloud storage access, egress volume, and leak-site samples. Build the **affected individuals list** by data element and state or country of residence. **This drives every breach notice.**
5. **Records.** Confirm with the FMIS vendor that the SYS-01 tenant (Produce Safety, pesticide, tally, and traceability records) was not accessed or altered, and get the vendor's written statement.
6. **Backups.** Confirm the backup account and the FMIS vendor's copies are intact before any restore. Identify the last backup taken before the attacker's first access.
7. **Preserve evidence.** Forensics images key hosts (including one SCADA server) and exports logs, with chain of custody (who collected, when, hash, storage). Evidence is held by the forensic firm under counsel.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at the site firewalls, SD-WAN, and the cloud firewall.
2. Remove the integrator's remote tool from both SCADA servers permanently. Any vendor support during recovery is **on site**, or through the access broker once POAM-003 closes.
3. Disable compromised accounts. Rotate all SCADA, HMI, PLC programming, modem, gateway, and service credentials, the SYS-01 and ERP integration keys, and the bank file transfer keys; store them in the vault.
4. **Rebuild SCADA servers and HMIs** from clean media with the integrator on site, then load verified HMI projects. **Reload PLC programs** from approved copies wherever the integrity check in section 4 step 3 fails or cannot be done. Record each program version and hash.
5. Rebuild affected laptops, line PCs, and cloud workloads from clean images in the isolated recovery network. Restore data from backups taken before the attacker's first access. **Do not decrypt and reuse compromised systems.**
6. Forensics confirms that persistence (scheduled tasks, remote tools, rogue accounts) is removed before any segment reconnects.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every notice before it goes out. The HR Director (workers) and the Vice President of Grower Services (growers) keep the **decision log** (POL-03 4.6).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is this a breach of security under Fla. Stat. 501.171(1)(a) (unauthorized access of electronic personal information), and under the law of each other state where affected individuals reside? | Counsel with the HR Director and the Vice President of Grower Services | Decision log |
| D2 | Date of determination (starts the Florida 30-day clocks) | Counsel | Decision log |
| D3 | How many affected, by state (Florida thresholds: 500 for the Department of Legal Affairs; more than 1,000 at once for consumer reporting agencies)? How many workers now live abroad? | HR Director; Vice President of Grower Services | Affected individuals list |
| D4 | Has law enforcement asked in writing to delay notice (501.171(4)(b))? Is a written no-harm determination appropriate (501.171(4)(c))? The company will not rely on a no-harm determination when government identifiers or bank account numbers were taken with names | Counsel | Decision log |
| D5 | Could product safety, traceability, or committed volumes be affected (retail 24-hour notice)? Are settlement dates or grower data affected (grower notice)? Do the credit agreement or sponsor governance require notice? | Director of Food Safety and Quality; Director of Sales; Vice President of Grower Services; CFO | Contract register |
| D6 | Ransom decision | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | COO |
| Within 24 hours of awareness | Retail customers: notice of any event that could affect product safety, traceability, or committed volumes (supplier agreements), with the expected shipping impact | Director of Sales with the Director of Food Safety and Quality |
| Day 0-1 | Contract growers: notice that the portal and settlement are affected and the payment plan; within 72 hours if grower data may be involved (marketing agreements) | Vice President of Grower Services |
| Day 0-1 | Lender and PE sponsor notice per the credit agreement and sponsor governance | CFO; CEO |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA. It supports the investigation and is a mitigating factor if a payment is ever considered (OFAC advisory) | Security Manager through counsel |
| Each payday | H-2A earnings statements issued on or before payday from paper tally and the payroll provider (20 CFR 655.122(k)) | HR Director |
| Within 24 hours of each application | Pesticide application and hazard information displayed from paper forms (40 CFR 170.311(b)(5)) | Food Safety Coordinators |
| On request | Produce Safety records to FDA (paper forms and the latest monthly export; 21 CFR 112.166(a)); H-2A records to DOL within 72 hours when kept centrally (655.122(j)(2)) | Director of Food Safety and Quality; HR Director |
| As soon as scoped | Breach determination documented (D1, D2) | Counsel |
| Within 30 days of determination | Florida individual notices by mail or email, in English and Spanish (501.171(4)); Department of Legal Affairs notice if 500 or more Floridians (501.171(3)). The 15-day good-cause extension applies only to the individual notice | HR Director; Vice President of Grower Services; counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at once (501.171(5)) | Counsel |
| Each other state | Residents of other states (online customers; former workers): apply each state's law. H-2A workers at home-country addresses: notified by company policy in Spanish, by mail, email, and through the H-2A filing agent | Counsel; HR Director |

**Why the Florida clock matters.** Florida's 30 days run from the **determination** of a breach, not from the end of the investigation. Counsel should set and record the determination date early. If the payroll provider or another third-party agent was the source, the agent must notify the company within 10 days of its own determination (501.171(6)), and the company's clocks then run.

**Not triggered for this company (reasons in the matrix):** the Reportable Food Registry (the company registers no food facility), CIRCIA reporting (not final as of 2026-09-25; as proposed the company would be covered, so the Security Manager rechecks at each exercise), SEC disclosure (privately held), and FAR 52.204-25 and 52.204-23 (no federal contracts).

**Ransom decision (POL-03 4.9).** Needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis); and a report to law enforcement. Paying does not remove notice duties if data was taken, and it does not make SCADA, PLCs, or HMIs trustworthy again. The default position, approved by the CEO, is not to pay while backups are intact and irrigation can run by hand.

**Communications.**
- Workers: briefings at each site in English and Spanish; a hotline through the insurer's notification vendor once notices go out.
- Growers: a direct call from the Vice President of Grower Services; written updates every 2 days while the portal is down.
- Retail customers: account managers call the top 10 customers; written notice through the supplier portals.
- Media: holding statement approved by counsel; no technical details, ransom, or attribution comments.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7). Each step is validated before the next begins: EDR clean, credentials rotated, patches applied, and forensics sign-off for the segment.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Farm 2 freeze protection and weather alarms (in freeze season) | 1 h, by hand | Standalone alarm and freeze crew on site; automation not used |
| 2 | Cold-chain sensors and alarm service | 1 h, manual rounds | Alarm service confirmed clean by the vendor; rounds continue until verified |
| 3 | Packinghouse controls on a clean, isolated OT network | 2 h, local operation | Ripening and cooling setpoints checked against the approved programs |
| 4 | Identity provider and administrator access (break-glass if needed) | 2 h | Sessions revoked; privileged credentials rotated |
| 5 | Site networks and SD-WAN, OT segments first | 4 h | Deny-by-default rules re-applied; integrator tool absent |
| 6 | SCADA servers and HMIs rebuilt; PLC programs verified | 8 h | Program hashes match approved copies; return to automatic control **one pump and one pivot at a time** with an Irrigation Technician watching a full cycle; **fertigation returns last**, after a supervised test at low rate |
| 7 | SYS-01 access and crew tablets | 4 h | Vendor statement that the tenant is clean; named crew accounts |
| 8 | ERP and EDI | 8 h | Restore; reconcile orders taken by phone |
| 9 | Farm data hub and integrations | 8 h | Restore from pre-compromise backup; re-sync historian data |
| 10 | Grower portal (alerts) | 8 h | Restore; portal credentials reset for all grower users |
| 11 | SIEM feeds and EDR console | 8 h | Monitoring confirmed before wider reconnection |
| 12 | Telematics and RTK | 24 h | Dealer access on request only |
| 13 | Payroll and timekeeping | 48 h | Repeat prior payroll if needed, then correct from paper tally |
| 14 | Settlement service | 48 h | Controller reconciles the spreadsheet settlement to the restored service before the next run |
| 15 | Retail sales and imagery | 24 to 72 h | Restore |

Key in paper tally, pesticide forms, and lot logs within 72 hours of restoration, and keep the paper originals with the records (21 CFR 112.161(a)(2)). Keep paper procedures until each process is back within its RTO. Tell staff, growers, and retail customers when services are restored (RC.CO).

**End of recovery** is declared by the incident commander and the operations command chair when BP-01 to BP-06 have run on automation for 72 hours without anomalies, the paper records for the incident period have been keyed and reviewed, and the settlement for the affected week has been reconciled.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- Update the risk register (P01: R-001, R-002, R-003, R-007, R-021), the POA&M (P07), the contingency plan (STD-07), and both runbooks.
- Keep all incident documentation, including the decision log and notices, for at least 3 years (POL-01 4.12), and any Florida no-harm determination for at least 5 years (Fla. Stat. 501.171(4)(c)).
