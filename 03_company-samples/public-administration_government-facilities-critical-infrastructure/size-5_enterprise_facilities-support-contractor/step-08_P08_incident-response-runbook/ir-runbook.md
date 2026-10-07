# Incident Response Runbook: Intrusion into Building Access Control and Automation Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded facilities support contractor operating government buildings in 8 states and DC) |
| Tier / Vertical | Enterprise / Government Services and Facilities |
| Incident type | Unauthorized access to the IBOP, its PACS or BAS tenants, or customer OT networks, for example through AQ-1's legacy remote-support tool, a stolen technician credential, or a default device password, leading to door unlocks, schedule or setpoint changes, or theft of cardholder data and face templates. Includes the SEC materiality assessment step, crisis management, and customer and multi-state notice workflows |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Building Manual-Mode Procedures |
| Runbook owner | Director of Security Operations, with the Director of OT Security for sections 3 to 5 and the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise ransomware tabletop 2025-11-13 (**IT scenario only; no OT or physical safety injects; before the AQ-2 acquisition**). Next: full tabletop of this scenario with the disclosure committee and one county customer on 2026-11-19 (POAM-013) |
| Notification matrix | `notification-matrix.csv` (30 obligations: 7 customer contract notices, 3 customer reporting duties that the company supports, 5 breach notice rows, 4 SEC, 3 FAR supply chain, 2 ransom rules, plus law enforcement, CIRCIA status, federal agency and FTI scope rows, inbound vendor notices, and the insurer) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| OT technical lead | Director of OT Security | OT security team lead on duty | SOC bridge |
| Building safety lead | Vice President, Remote Operations | ROC shift supervisor at the unaffected ROC | ROC hotline (separate carrier) |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | President of the most affected segment | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Risk Officer, Chief Compliance Officer, Vice President, Investor Relations; the president of the affected segment attends; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Customer notice owners | Segment notice owners (Federal, State and Local, Education, Security Integration); Site Managers for each building | Segment presidents | Contract obligations register (printed copy in the binder) |
| Privacy and breach decisions | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| FAR supply chain reports | Vice President, Government Contracts Compliance | Chief Compliance Officer | Direct mobile |
| Outside counsel and forensics (OT-capable) | Retained firms through counsel and the insurer panel | MSSP incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume the attacker can see company email, chat, and the IBOP console. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder at each ROC and site office. **Customer security staff are part of the response**: they control guards, lobbies, and lockdowns at their buildings.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at each ROC and site office: this runbook, contacts, the contract obligations register extract, manual-mode procedures, emergency revoke lists
- [ ] All remote access to customer OT through the OT remote access gateway. **Gap until POAM-001 closes: AQ-1 legacy tool at 142 sites**
- [ ] No default or shared device credentials. **Gap until POAM-003 and POAM-004 close**
- [ ] Known-good controller programs and door schedules in the repository, with hashes. **Gap until POAM-008 closes (AQ-2 programs)**
- [ ] SIEM receives IBOP, gateway, and edge gateway logs. **Gap until POAM-006 closes (AQ sources)**
- [ ] OT sensors at the buildings in scope. **Gap until POAM-005 closes (550 buildings without sensors)**
- [ ] Manual-mode procedures exercised for every IBOP building and federal building (PRC-03.4)
- [ ] Materiality playbook includes OT and physical-safety factors; disclosure committee roster current. **Gap until POAM-013 closes**
- [ ] Customer notice matrix covers AQ-1 and AQ-2 contracts. **Gap until POAM-014 closes**
- [ ] OT-capable forensics, counsel, and insurer contacts confirmed this quarter

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Doors unlocked outside schedule, or schedule changed with no FSP ticket | PACS alarms; atypical-use rules (AC-2(12)); customer security staff | ROC confirms with the Site Manager; if no approved change, declare |
| Setpoints, schedules, or programs changed with no ticket; repository hash mismatch | BAS alarms; nightly integrity comparison (SI-7) | OT lead checks the audit trail; if unexplained, declare |
| AQ-1 legacy agent active outside an approved service window | Weekly SOC agent inventory; edge firewall; site check | Disable the agent at the site; declare |
| Remote session nobody booked; gateway session from an unusual location | Gateway; identity platform; SIEM | Terminate the session; disable the account; declare |
| New BACnet device, anomalous writes, or scanning on a site OT network | OT sensors | Isolate the site tunnel if writes continue; declare |
| Bulk cardholder or face template export by an unknown user | PACS audit trail; database activity monitoring | Disable the account; preserve; declare |
| A customer or GSA reports suspicious activity | Customer IT or security; GSA IT | Declare and start the notice clocks |

**Declare a severity-1 incident when** any door, schedule, setpoint, program, or account change cannot be tied to an approved ticket at more than one building, at any public safety building or courthouse, or at any building where people may be at risk, or when an unknown remote session reached a site OT network.

**Record three times, separately:**
1. **Discovery time** (contracts): when the company first knew of the suspected incident. This starts the customer clocks (immediately for GSA, 1 hour for public safety customers, 24 hours for state, local, and education customers).
2. **Breach determination time** (state breach laws): when the Chief Privacy Officer determines that personal information was breached, or there is reason to believe it was. This starts the third-party agent clock (Florida worked example: 10 days under Fla. Stat. 501.171(6)(a)) and, for the company's own data, the state individual notice clocks.
3. **Materiality determination time** (SEC): recorded by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.

## 3. First hour: make the buildings safe, then contain (RS.MA, RS.MI)
**Safety comes before evidence** (POL-03 4.4). Wrong door states and HVAC settings affect people now.

| Step | Who | Done when |
|---|---|---|
| 1. Tell each affected customer's security staff and Site Manager what is happening; agree on door posture (lock exterior doors to scheduled state, post guards, lock down where the customer decides) | Site Managers; building safety lead | Customer security acknowledges at each building |
| 2. Put affected BAS equipment in local or manual mode per PRC-03.4; restore safe setpoints at the controller | Building engineers with the OT lead | Building conditions stable |
| 3. Cut remote paths: disable AQ-1 legacy agents at all 142 sites (not only affected ones), suspend subcontractor gateway accounts, and drop site tunnels to any IBOP tenant that may be compromised. Controllers keep running on their last programs and door controllers on cached credentials | Director of OT Security; IBOP Platform Manager | No remote session into any affected site |
| 4. Fail over alarm monitoring for affected tenants to an unaffected ROC so alarms are still watched | Vice President, Remote Operations | Alarms monitored |
| 5. In the PACS, disable unknown or suspect administrator accounts, force credential resets for company administrators of affected tenants, and export the audit trail | IBOP Platform Manager | Accounts disabled; audit export saved |
| 6. Send the immediate GSA report and the 1-hour public safety notices if any of their buildings or data may be involved | Federal Site Manager; State and Local notice owner | Notices logged with time |
| 7. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains OT-capable forensics under privilege; the insurer is notified | CISO; General Counsel | Engagement letters; claim number |
| 8. The Chief Operating Officer activates the crisis management team | Chief Operating Officer | Crisis team convened |
| 9. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open |

**Do not** reboot or re-download controllers, wipe IBOP servers, or restore backups yet. That destroys evidence and may push a tampered program to more devices.

## 4. Analysis (RS.AN)
1. **Scope:** which tenants, buildings, controllers, doors, and accounts were touched? Compare running door schedules and controller programs against the repository hashes. Check gateway recordings, PACS and BAS audit trails, OT sensor data, edge gateway logs, and cloud audit logs. For AQ-1 sites, collect the legacy tool vendor's relay logs through counsel, because they are not in the SIEM.
2. **Initial access:** the AQ-1 legacy tool, a technician or subcontractor credential, a default device password, an edge gateway vulnerability, or a customer network. Check the AQ-1 path first while POAM-001 is open.
3. **Evidence:** image affected engineering workstations and snapshot IBOP virtual machines; export logs before retention expires; keep chain of custody in the evidence register with hashes.
4. **Data theft:** were cardholder records, badge photos, **face templates**, student records, drawings, or GSA CUI exported? **This drives section 7.**
5. **Reach into GSA:** did the attacker use or obtain credentials of any PIV holder, or touch GSA CUI? If there is any chance, the immediate GSA report must already have been sent (BTTRG 1.6.1); GSA handles its own systems.
6. **Supply chain angle:** if the entry point was equipment or software, check it against FAR 52.204-25, 52.204-23, and FASCSA orders; those clocks start at identification (1 or 3 business days).
7. **Business impact:** Finance and the BIA owners estimate impact using P05 values (for example, about $1.9 million per day if ROC monitoring is lost broadly, and about $1.1 million per day for manual lockdown and guard posts). These estimates feed section 6.

## 5. Containment, eradication, and restoration of control (RS.MI)
1. Remove the AQ-1 legacy tool from every affected site permanently; reimage affected edge gateways and engineering workstations.
2. Rotate every credential the attacker could have seen: device passwords in the PAM vault, PACS and BAS administrator accounts, gateway accounts, subcontractor accounts, site tunnel keys.
3. Rebuild affected IBOP servers from clean images and restore databases from a backup dated before the first malicious action.
4. Restore controller programs and door schedules from the repository, **verifying hashes**, one building at a time, with the building engineer on site watching equipment behavior.
5. Have customer security staff walk every changed door and confirm the correct state.
6. Forensics confirms persistence is removed (scheduled tasks, new accounts, remote tools) before each site reconnects.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors. Note that 17 CFR 229.106(a) defines the registrant's information systems to include resources "owned or used by the registrant", which counsel considers when an incident involves customer-owned building systems the company operates.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.6) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives (POL-05 4.9) | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 3 to 5 | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date, time, and reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation, or security details customers treat as exempt records | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align timing and content of customer, employee, media, and investor communications with the filing; brief GSA and state customers before the filing becomes public where contracts require; brief the audit committee and risk committee chairs | Communications; Investor Relations; segment presidents | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist; OT and government-customer factors added under POAM-013):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost revenue, SLA credits, and performance deductions from P05 values; response and forensic costs; guard and overtime costs; expected notification and legal costs; insurance coverage and retention |
| Physical safety and security | Whether doors at courthouses, public safety buildings, schools, or universities were unlocked or controlled by the attacker; any injury, property damage, or unsafe building condition; how long buildings were in manual mode |
| Government customers and eligibility | Contract cure or default notices; effect on GSA, state, or university relationships; FAR reports filed (52.204-25(d)); any effect on federal or state eligibility; rebid risk on contracts up for renewal |
| Data | Number of cardholders and states; face templates, student records, or GSA CUI involved; whether data was published |
| Scale and systemic reach | Number of tenants and buildings affected; whether the intrusion shows a platform-wide weakness (for example, all AQ-1 sites) |
| Legal and regulatory | Customer reporting duties triggered (Florida example: 282.318 and 282.3185); state attorney general inquiries; litigation exposure |
| Reputation and strategy | National media; analyst or ratings action; effect on acquisitions and integration plans |

**Worked example of the clocks (fictional dates):** at 06:40 on Monday 2027-02-01 the ROC sees doors unlocked outside schedule at three county buildings serviced through the AQ-1 legacy tool, one of them a sheriff's administration building. The incident commander declares severity 1 at 07:05 (discovery time 06:40).
- **1 hour:** the public safety customer is notified by 07:40.
- **24 hours:** the county is notified by 06:40 on Tuesday 2027-02-02 (in practice at 08:15 on Monday). The county then has its own 48-hour report to the state (Florida example: Fla. Stat. 282.3185(5)(b)1.), so the company's notice must carry the facts the county needs.
- **SEC:** the disclosure committee convenes Tuesday 2027-02-02 and determines materiality on Wednesday 2027-02-03 at 15:00, because the same weakness exists at 142 sites and a sheriff's building was affected. The Form 8-K is due by Tuesday 2027-02-09 (4 business days: February 4, 5, 8, and 9).
- **Breach:** on Friday 2027-02-05 forensics confirms that cardholder records for the three buildings, including face templates at one pilot site, were exported. The Chief Privacy Officer records the breach determination that day. The third-party agent notice to the county is due no later than Monday 2027-02-15 under Fla. Stat. 501.171(6)(a), but the contract's 24-hour term means the county is told on 2027-02-05. The county decides on notices to individuals.
- **FAR:** if the investigation identifies covered video equipment at an affected site, the report to the contracting officer is due within 1 business day of identification.
Counsel must also decide whether "reason to believe" a breach arose earlier (for example, when the attacker's account ran an export on 2027-02-01), which would move the breach clocks forward.

## 7. Customer and multi-state notice workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation about personal information before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Build the list of affected customers, tenants, and buildings; pull each customer's notice terms from the contract obligations register | Segment notice owners | Customer notice list with clocks |
| 7.2 | Send customer notices on the shortest clock: GSA immediately; public safety customers within 1 hour; state, local, and education customers within 24 hours; FSP customers within 72 hours. Include the facts each customer needs for its own reports: summary, buildings, data types, last good backup, estimated impact | Segment notice owners; Site Managers | Notices logged with times |
| 7.3 | Breach determination for personal information: cardholder records, badge photos, face templates, student records, employee data. Treat face templates as biometric data even where the law is unsettled (Florida example: 501.171(1)(g)1.a.(VI) and 501.702; counsel to confirm) | Chief Privacy Officer | Signed determination |
| 7.4 | **Customer data:** the company acts as the customer's third-party agent. Send the formal breach notice with all information the customer needs (Florida example: within 10 days under 501.171(6)(a)), and support the customer's own notices. For university student records, follow each university's direction (34 CFR 99.33(a)) | Chief Privacy Officer; segment notice owners | Customer breach notices |
| 7.5 | **Company data (employees):** apply each state's law where affected employees reside, using counsel's state matrix. Florida example: individuals within 30 days of determination; Department of Legal Affairs within 30 days if 500 or more Floridians; consumer reporting agencies if more than 1,000 | Chief Privacy Officer; General Counsel | State deadline table; notices |
| 7.6 | **GSA CUI:** if CUI was accessed, report the non-compliance to the GSA contracting officer by the agency's method (32 CFR 2002.16(a)(6)(iii)) | Vice President, Government Contracts Compliance | GSA notice |
| 7.7 | **FAR supply chain:** report covered equipment (1 business day), Kaspersky articles (3 business days), or FASCSA articles (3 business days) found during the investigation, with further information within 10 business days | Vice President, Government Contracts Compliance | Contracting officer reports |
| 7.8 | **Plan to the shortest clock** across contracts, state laws, FAR, and the SEC. Publish one master calendar | Incident commander with the General Counsel | Master calendar |
| 7.9 | Honor any law enforcement delay request under the state laws that allow it; document it | General Counsel | Delay record |
| 7.10 | **Public records:** incident reports to government customers may become public records. Mark security details (door layouts, vulnerabilities) as exempt security records (Florida example: Fla. Stat. 119.071(3)(a)) and let the customer's custodian decide on requests | General Counsel | Marked reports |
| 7.11 | Provide input to customers' after-action reports (Florida example: within 1 week after remediation under 282.3185(6)) | Director of Security Operations | Input delivered |

**Ransom demands:** state agencies and local governments in Florida may not pay a ransom (Fla. Stat. 282.3186), and the company will never pay on a customer's behalf (POL-03 4.7). Any payment for the company's own systems requires the CEO, the General Counsel, the insurer, and an OFAC sanctions check. Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove any notice or disclosure duty.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Identity platform and break-glass access
2. ROC connectivity, SD-WAN, and carriers
3. Security tooling (EDR, SIEM, OT sensors) for validation
4. Alarm routing and ROC consoles for affected tenants (from the unaffected ROC first)
5. PACS administration for affected tenants; re-verify all door schedules and recent cardholder changes with customer security staff
6. Telephony and service desks
7. OT remote access gateway (rebuilt; the only remote path; AQ-1 sites stay on site visits until migrated)
8. BAS supervisory servers; bring buildings back from manual mode one at a time
9. FSP work order flow
10. Video management and evidence exports
11. Controller program repository (verified against offline copies)
12. ERP, payroll, billing, and analytics

**Validate before reconnecting each building:** credentials rotated, programs and schedules match the hashed known-good copies, door states walked by customer security, and the edge gateway allows management traffic only from the gateway. Tell each customer in writing when each building returns to normal operation (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, including each affected customer; written report within 30 days (POL-03 4.11).
- Update the risk register (P01: R-001, R-002, R-004, R-024, R-025), the POA&M (P07), the subcontractor and vendor terms, the materiality playbook, and this runbook.
- The disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including materiality minutes, breach determinations, and customer notices, for at least 3 years or longer where a contract or customer records schedule requires (POL-01 4.11).
