# Incident Response Runbook: Ransomware on Building Automation Systems Across Regions

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded office and retail REIT; 140 properties in FL, TX, GA, NC, AZ, and CA) |
| Tier / Vertical | Enterprise / Commercial Facilities |
| Incident type | Ransomware on building automation systems (BAS), entering through Integrator C's remote-support tool at the acquired properties and spreading to Platform B site servers, with possible reach into the access control and video platform console PCs and corporate systems; includes the SEC materiality assessment and a multi-state notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Tenant and Contractual Notice Procedure; STD-03.4 OT Incident and Degraded-Mode Operations Standard |
| Runbook owner | Director of Security Operations, with the Senior Vice President, Engineering for building safety (sections 3 and 8) and the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise tabletop 2026-03-19 (data breach scenario; **no building outage, and engineering and the disclosure committee did not take part**). Next: building-outage tabletop with the disclosure committee and engineering on 2026-11-17 (POAM-012) |
| Notification matrix | `notification-matrix.csv` (26 obligations: 5 SEC and disclosure, 4 generic state, 6 Florida worked example, 6 contractual, plus OFAC, voluntary CISA and FBI reporting, CIRCIA status, insurance, and FAR status) |

**Safety comes first.** The company's product is safe, cooled, and secure space. In this incident the buildings keep running on their own: BAS field controllers keep their last programs and schedules, door controllers cache credentials for up to 72 hours, and life-safety systems (fire alarm, elevators, emergency voice) are on separate networks with only read-only relays into the BAS. Nothing in this runbook touches life-safety systems.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | Cyber Defense Center manager on duty | Incident bridge on the out-of-band conferencing service |
| OT safety lead | Senior Vice President, Engineering | Building Technology Director for the affected region | Company mobile; engineering radio at each property |
| OT technical lead | Director of OT Security | OT security engineer on call | Company mobile |
| Physical security lead | Vice President, Corporate Security | RSOC supervisor on duty | RSOC line (24x7) |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Executive Vice President, Property Operations | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Chief Accounting Officer, CISO, Chief Privacy Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Breach and privacy decisions | Chief Privacy Officer | Deputy General Counsel | Direct mobile |
| Outside breach counsel and forensics (OT-capable) | Retained firms engaged through counsel and the insurer panel | MSSP incident team | Retainer hotline |
| Cyber insurer | Primary carrier breach hotline | Broker | Policy card in the incident binder |
| BAS vendor support | Integrator A and B1 to B4 clean technicians, verified by call-back; **Integrator C treated as possibly compromised** | Equipment manufacturers' service lines | Numbers in the incident binder, **not** from email |
| Tenant, owner, and client communications | Vice President, Corporate Communications with the Executive Vice President, Property Operations (tenants), the President of the TRS (SL-1 owners), and the Vice President, Digital Products (SL-2 clients) | Property Managers | Printed contact lists |
| Investor communications | Vice President, Investor Relations | CFO | Direct mobile |
| Law enforcement and government | FBI field office or IC3; CISA | n/a | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, the identity platform, and the integrators' own systems may be compromised. Coordinate on company mobile phones, the out-of-band conferencing service, engineering radios, and the printed incident binder at each property and RSOC.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at each property and RSOC: this runbook, contacts, the notification matrix, tenant contact lists, the lease 72-hour clause list, and degraded-mode procedures. **Clause list and contact refresh: gap until POAM-025 closes**
- [ ] Degraded-mode procedures at every property (CP-2). **Gap at 30 properties until POAM-013 closes (2026-12-31)**
- [ ] Always-on vendor tools removed; all integrators only through the OT remote access gateway (AC-17, MA-4). **Gap for Integrator C until POAM-003 closes (2026-11-30)**
- [ ] OT zones with deny-by-default conduits (SC-7). **Gap at the 19 acquired properties until POAM-004 closes**
- [ ] Immutable backups of Platform A and B and company-held controller programs, restore-tested in the last 90 days (CP-9, CP-4). **Gap for Platform C and 9 Platform B properties until POAM-008 closes**
- [ ] OT logs in the SIEM and passive OT monitoring (AU-6, SI-4). **Gap for Platform B, Platform C, and 86 properties until POAM-005 closes**
- [ ] Break-glass accounts sealed and tested this quarter (POL-02 4.11)
- [ ] Materiality worksheet includes the P05 building-outage values; disclosure committee roster current (**gap until POAM-012 closes**)
- [ ] Outside counsel, OT-capable forensics, and insurer contacts confirmed this quarter
- [ ] State breach law matrix from outside counsel updated in the last 12 months

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note or unreadable graphics on a BAS server or engineering workstation | Chief engineer, engineering staff, EDR | Call the Cyber Defense Center and the OT safety lead. **Do not power off** the server. Unplug the workstation's network cable |
| BAS graphics show setpoints, schedules, or equipment states nobody changed; alarms stop arriving at the RSOC | Chief engineer; RSOC | Check equipment locally; if confirmed, treat as a BAS compromise |
| Remote-support session nobody approved (Integrator C tool console) or a gateway session outside its approval window | Property staff; OT gateway alerts | Call the integrator on a known number; if not confirmed, disconnect the server's network and declare |
| Mass file changes, new administrator accounts, or EDR ransomware detection on Platform A or B hosts, console PCs, or corporate endpoints | EDR; SIEM; identity platform | Cyber Defense Center isolates hosts and opens a severity-1 case |
| Door controllers offline, badges failing, or unexplained door unlocks across properties | RSOC; access control platform alerts | Physical security lead posts officers; check the platform console |
| Extortion message or leak-site post naming the company, its tenants, or SL-2 clients | Email, threat intelligence, law enforcement, media | Declare; preserve the message; do not engage without counsel |
| A vendor or integrator reports a ransomware event | Vendor notice | Open a vendor incident case; treat that vendor's access as hostile until cleared |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any BAACS or production IT system, or an extortion claim names company, tenant, or client data.

**Record three times, separately:**
1. **Discovery time:** when the incident was first known. It starts the planning clock for lease 72-hour clauses (counsel decides the exact start for each lease) and the SL-1 2-business-day notice.
2. **Breach determination time (each state):** when the company determined, or had reason to believe, that personal information was accessed. It starts state clocks such as Florida's 30 days (Fla. Stat. 501.171(4)(a)).
3. **Materiality determination time (SEC):** recorded later by the disclosure committee (section 6). It starts the 4-business-day Form 8-K clock.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Make the buildings safe.** At every affected property, chief engineers check chillers, air handlers, and tenant data rooms locally, switch plant equipment to local hand control where the BAS is not trusted, and start hourly rounds. Regional engineering directors move staff between properties | OT safety lead; chief engineers | Each affected property reports stable cooling and equipment status to the incident bridge |
| 2. **Cut the entry path.** Block all traffic from the seller site VPN at the shared services hub; stop Integrator C's remote tool by disconnecting the 19 Platform C servers' network at the property edge; suspend all integrator accounts on the OT gateway except named clean technicians | OT technical lead; Network Engineering | No traffic from the acquired properties to the hub; gateway sessions only by approval |
| 3. **Stop spread.** Close conduits between OT zones and corporate networks at every property (pre-built "isolate" rule set); isolate Platform B site servers showing activity; keep Platform A clusters running but block inbound connections from Platform B and C | Network Engineering; OT technical lead | Isolation rule set applied; Platform A healthy |
| 4. **Secure the doors.** Confirm door controllers still work on cached credentials; set perimeter doors to scheduled lock; post officers at main entrances with printed tenant lists; move affected RSOC consoles to clean spare PCs or to another RSOC | Physical security lead | Entrances staffed; door status confirmed |
| 5. Revoke sessions and rotate credentials for administrators, service accounts, and integrator accounts involved; use break-glass accounts if single sign-on is affected | Director of Identity and Access Management | Revocations logged |
| 6. Confirm backup accounts are untouched (write-once locks, no recent deletions) | Director of Cloud Platform Engineering | Backup integrity confirmed |
| 7. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains OT-capable forensics under privilege; the insurer is notified through the hotline | CISO; General Counsel | Claim number and engagement letters |
| 8. COO activates the crisis management team; Property Managers send service notices to tenants at affected properties (lease service clauses) | COO; Executive Vice President, Property Operations | Crisis team active; first tenant notices sent |
| 9. Start the incident log (timeline, decisions, who, when) and the evidence register with chain of custody | Incident commander | Log open |

**Do not** power off field controllers, door controllers, or NVRs, and do not reset controllers to factory settings. For Platform C and 9 Platform B properties, the company does not yet hold copies of the controller programs (POAM-008).

## 4. Analysis (RS.AN)
1. **Scope:** which systems are affected: Platform C servers, Platform B site servers, Platform A clusters, engineering workstations, console PCs, NVRs, the legacy PACS, the OT remote access gateway, cloud workloads, corporate endpoints. Use EDR, SIEM, gateway records, cloud audit logs, and passive OT sensors. For Platform C, Platform B, and the legacy PACS, collect logs locally, because they are not in the SIEM (POAM-005).
2. **Field devices:** with clean integrator technicians, compare controller programs at a sample of devices at each affected platform against the last company-held copies. Look for changed setpoints, disabled alarms, or new logic.
3. **Initial access:** confirm the path (Integrator C credentials on the remote tool, or a compromise at Integrator C itself). **Ask Integrator C whether other customers are affected.** Treat all of its access as hostile until it proves otherwise.
4. **Evidence:** forensics images affected hosts and exports logs before they roll over; chain of custody is kept in the evidence register; hashes are recorded for each artifact.
5. **Personal information:** determine whether the attacker reached any system holding personal information: visitor ID scans (SYS-11, including the legacy kiosks at the 6 acquired towers), the access control platform console from a console PC (tenant employee records and access history), the legacy PACS database, HR and payroll (SYS-12), or file storage. Look for archive and transfer tools and large outbound transfers. **This drives section 7.**
6. **Business impact:** Finance and the BIA owners estimate impact using P05 values (about $520,000 a day for Platform A manual operation and $230,000 a day for Platform B; office rent at risk of about $4.5 million a day from day 4 on the 2023 template; about $14.4 million for a 5-business-day outage of Platforms A and B). These estimates feed section 6.

## 5. Containment and eradication (RS.MI)
1. Contain by zone and property: keep affected properties isolated; reconnect nothing until section 8 validation passes.
2. Remove Integrator C's remote tool permanently; integrator access resumes only through the OT gateway with named accounts, MFA, and per-session approval (POL-02 4.9).
3. Rotate all OT local passwords, gateway and platform administrator credentials, service accounts, and data platform connection credentials. Change any remaining default passwords.
4. Rebuild engineering workstations and console PCs from the standard images. **Do not decrypt and reuse them.**
5. Rebuild Platform B site servers from clean images and restore the BAS database from a verified backup; Platform C servers are rebuilt on Platform B hardware where the migration design allows, using programs recovered from field controllers or escrow.
6. Reload any field controller whose program was changed, from a verified company-held copy.
7. Forensics confirms persistence is removed before any system reconnects to an OT zone.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.5) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 and 5 and the BIA values | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date, time, and reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align timing and content of tenant, owner, client, employee, media, and investor communications with the filing; brief the audit committee and board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Manual operation costs and rent at risk from P05 (rent abatement after 3 business days for office leases on the 2023 template, after 5 for retail); tenant claims; SL-1 fee credits; recovery, forensic, legal, and notification costs; insurance recovery and retention ($5 million); effect on liquidity and loan covenants |
| Operational | Number of properties and regions without supervisory control; days in degraded mode; access control and RSOC impact; effect on SL-1 and SL-2 clients |
| Occupant safety | Any injury, heat stress event, or unsecured building linked to the incident |
| Data | Number of individuals and states; data types (visitor ID numbers, employee Social Security numbers, credential records, face templates); whether data was published |
| Legal and regulatory | Expected state attorney general inquiries; CPPA interest in California data; lease disputes; JV partner, owner, and lender claims |
| Reputation and strategy | Media coverage; tenant renewals at risk; JV partner confidence; effect on the acquisition program |

**Worked example of the clocks (fictional dates):** ransomware is discovered on Monday 2027-03-08 at 06:40 at an acquired property and found on Platform B site servers in two regions by noon. The committee convenes Tuesday 2027-03-09. By Thursday 2027-03-11 at 15:00, 41 properties have been in degraded mode for 3 days, abatement exposure has started at 9 office properties, and the committee determines the incident is material. The Form 8-K is due by **Wednesday 2027-03-17** (4 business days: March 12, 15, 16, and 17). On Friday 2027-03-19, forensics confirms that visitor ID scans from the legacy kiosks at 2 acquired towers (Texas) and access control records viewed from a compromised console PC in Florida were taken: the Chief Privacy Officer records the breach determination that day. Florida's 30-day clocks (individuals and, if 500 or more Floridians, the Department of Legal Affairs) run to Sunday 2027-04-18, so notices are planned for Friday 2027-04-16. Texas and any other states follow counsel's state matrix. The lease 72-hour clauses were planned from the first sign of possible access to tenant employee data (Wednesday 2027-03-10 at 14:00, when a compromised console PC was found), because counsel had not yet decided each clause's start, so those tenant notices went out by Saturday 2027-03-13. Counsel must also decide whether a "reason to believe" a breach occurred arose earlier (for example, when the extortion note claimed data theft), which would move the state dates forward.

## 7. Notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each legal notice before it goes out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Decide, with counsel, whether personal information was accessed and when that determination was made; record it for each state | Chief Privacy Officer | Determination memo |
| 7.2 | Build the affected population from forensic results: each individual, data elements, and **state of residence** (from visitor ID addresses, credential records, and HR records). Separate groups: (a) visitors; (b) tenant employees; (c) company employees; (d) SL-2 client users; (e) individuals at SL-1 managed properties (owner notice decisions) | Chief Privacy Officer; data team | Affected-individual file with state counts |
| 7.3 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, and content rules. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 7.4 | **Florida worked example:** individual notice within 30 days of the determination; Department of Legal Affairs notice within 30 days if 500 or more Floridians (individual notice may get 15 more days on written good cause); consumer reporting agencies if more than 1,000 are notified at once; a written no-harm determination only if counsel supports it | General Counsel | Florida filings |
| 7.5 | **Contractual notices:** tenants with 72-hour clauses (about 1,100 leases); SL-1 owners and JV partners within 2 business days; SL-2 clients within 72 hours of confirmation; lenders as each agreement requires; service interruption notices to tenants at affected properties | Vice President, Leasing; President of the TRS; Vice President, Digital Products; Treasurer | Notice log |
| 7.6 | **Plan to the shortest clock** across states, contracts, and the SEC. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 7.7 | Honor any law enforcement delay request (for example Fla. Stat. 501.171(4)(b)) and document it | General Counsel | Delay record |
| 7.8 | Engage the mail vendor, call center, and credit monitoring provider through the insurer panel | Chief Privacy Officer | Vendors active |
| 7.9 | Voluntary report to CISA and the FBI within 24 hours of declaration (CPG 5.B); record it for OFAC mitigation | CISO | Report confirmations |
| 7.10 | Track inbound vendor notices (state third-party agent laws such as Fla. Stat. 501.171(6)) if the incident started at Integrator C or another vendor | Director of Third-Party Risk Management | Vendor notices logged |

**Two separate questions.** Ransomware that stays on BAS servers encrypts operational data and drawings, which are not personal information under state breach laws. State notice duties start only if the attacker reached personal information. Lease, owner, client, and lender notices are contractual and have their own triggers and clocks. The SEC question is separate from both: a building outage with no data theft can still be material.

**Ransom decision:** requires the CEO, the CFO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.8). Paying does not remove notification or disclosure duties, and it does not restore controller programs that were changed.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Identity platform and break-glass access
2. SD-WAN core, property firewalls, and OT zone rules, rebuilt deny-by-default before any OT device reconnects
3. Security tooling (EDR console, SIEM, passive OT sensors) for validation
4. Access control platform administration from clean console PCs; re-verify door schedules and administrator accounts
5. Tenant notification channels
6. RSOC consoles and video
7. Tenant experience platform and mobile credentials (tell SL-2 clients the restoration status)
8. Clean engineering workstations and tablets (pre-imaged spares first)
9. Platform A clusters: reconnect property by property, then check each plant system with the chief engineer before leaving hand control (RTO 6 hours)
10. Platform C site servers and the legacy PACS: rebuild or migrate (RTO 8 hours is a target only; no backups today)
11. Productivity suite and visitor management (paper logs until restored)
12. Platform B site servers: restore from the backup account (RTO 12 hours; the 2026 test took 14)
13. Parking interfaces, property management and ERP, treasury, payroll, card terminals, and the data platform, as affected

**Validate before reconnecting:** EDR clean, credentials rotated, patched, logging to the SIEM, and the chief engineer confirms equipment runs correctly under BAS control. Keep manual rounds until each property has run 24 hours under BAS control without unexplained alarms. Tell tenants, owners, and clients when services are back to normal (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the integrators involved; written report within 30 days (POL-03 4.12).
- Update the risk register (P01: R-001, R-003, R-011, R-017), the POA&M (P07), the degraded-mode procedures, this runbook, and the materiality playbook.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Review Integrator C's relationship: contract terms, remote access design, and whether the security addendum was met (POL-01 4.8).
- Retain all records, including the materiality determination minutes, breach determinations, and evidence logs, for at least 7 years (POL-01 4.11).
