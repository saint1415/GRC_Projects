# Incident Response Runbook: Intrusion into Distribution Control Systems (OT)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded investor-owned electric utility; NERC DP, TO, TOP; Florida and south Georgia) |
| Tier / Vertical | Enterprise / Utilities |
| Incident type | Intrusion into the distribution control systems (ADMS and OMS) through a compromised vendor support path or stolen engineer credentials, with unauthorized feeder breaker operations and probing toward the EMS, including the **SEC materiality assessment** and the NERC, DOE, and state reporting workflows |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); NIST SP 800-82 Rev. 3 for OT response |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 DOE-417 and EOP-004 Filing Procedure; the CIP-008 incident response plan v9 (for any EMS, EACMS, or substation BES Cyber System involvement) |
| Runbook owner | Director, Security Operations (enterprise incident commander), with the Director, Distribution Control Center for grid operations and the General Counsel for section 6 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | OT tabletop 2026-02-24 (also the CIP-008-6 R2.1 test; **the disclosure committee did not take part**). Next: disclosure committee tabletop with an OT scenario on 2026-11-18 (POAM-011) |
| Notification matrix | `notification-matrix.csv` (34 obligations: 10 NERC CIP, DOE-417, and EOP-004 reporting rows plus RC coordination; 5 SEC and disclosure; 3 generic state and 5 Florida worked example; 3 contractual; OFAC; law enforcement; and not-applicable rows for CIRCIA, TSA, NRC, and FAR) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Enterprise incident commander (cyber) | Director, Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Operational incident commander (grid) | Director, Distribution Control Center | DCC shift supervisor | DCC hotline; radio |
| Transmission operations | Director, Transmission Operations | TCC shift supervisor | TCC hotline |
| CIP determinations (Reportable incident, attempt to compromise) | CIP Senior Manager's delegate on duty | Director, NERC Compliance | Duty phone |
| Executive incident lead | CISO | Director, OT Security | Out-of-band group on company phones |
| Crisis management team chair | Chief Operating Officer | SVP, Transmission and System Operations | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Risk Officer, Chief Compliance Officer, SVP Transmission and System Operations, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| NERC, DOE, and E-ISAC filings | Director, NERC Compliance | NERC compliance analyst on call | Duty phone |
| Breach and privacy decisions | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Outside counsel, OT forensics | Panel firms engaged through counsel and the insurer | ADMS vendor incident team (only after its path is ruled out as the source) | Retainer hotline |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement and government | FBI field office; CISA; DOE CESER | E-ISAC | Numbers in the incident binder |

**Out-of-band first.** Assume the corporate network, email, and chat may be watched. Use company mobile phones, the out-of-band conferencing service, and the printed binders at the DCC, TCC, backup sites, and SOC.

## 1. Preparation checks (Identify / Protect)
- [ ] All vendor remote access paths into OT pass through jump hosts or Intermediate Systems with MFA and recording (**ADMS vendor appliance disabled 2026-08-13; redesign due 2026-11-30, POAM-001**)
- [ ] Vendor remote access is off by default, and the DCC can disable all vendor sessions with one action (PAM kill switch tested this quarter)
- [ ] Offline ADMS and EMS backups at OCN verified this month; golden images for consoles and servers current (CP-9)
- [ ] Manual-mode procedures, paper switching order books, and radio checks current at the DCC and backup DCC (P05 BP-02)
- [ ] OT sensors at the DCC, backup DCC, TCC, and medium impact substations feeding the SOC; **distribution substation coverage 41% (POAM-004)**
- [ ] DCC and TCC checklists list DOE-417 criteria 1 to 26, **including criterion 14 (due 2026-10-31)**, and the CIP-008 determination steps
- [ ] Materiality worksheet includes BIA outage costs (**due 2026-10-31, POAM-011**); disclosure committee roster current
- [ ] Insurer, OT forensics, and outside counsel contacts confirmed this quarter

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Breaker, recloser, or switch operations nobody in the DCC commanded | ADMS alarms; operator report; AMI outage events without a field cause | DCC supervisor checks for switching orders and FLISR actions; if none, calls the SOC and declares a suspected OT incident |
| Remote session outside an approved window, or from an unknown path | OT PAM; jump host logs; OT sensors | SOC kills the session through PAM; opens a severity-1 case |
| New device, scanning, or unusual protocol traffic in the ADMS zone or toward the EMS Electronic Access Point | OT sensors; EAP IDS; SIEM | SOC opens a case; notifies OT Security and the CIP delegate |
| Changes to ADMS displays, points, or settings without a change record | File integrity monitoring; drift reports | Freeze changes; open a case |
| Vendor reports a compromise of its support systems or credentials | Vendor notice (contract clause) | Disable that vendor's access everywhere; open a vendor incident case |
| Extortion message or public claim about the company grid | Email; threat intelligence; media | Declare; preserve; do not engage without counsel |

**Declare a severity-1 OT incident when** any unauthorized control action is confirmed, or an unauthorized person is confirmed to have interactive access to the ADMS, OMS, EMS, or substation systems.

**Record these times separately in the incident log.** Each starts a different clock:
1. **Incident time** (DOE-417): when the event occurred or began. The 1-hour Emergency Alert clock runs from here.
2. **Recognition time** (EOP-004-4 and DOE-417 System Report): when staff recognized that an event met a threshold.
3. **CIP determination time** (CIP-008-6 R4): when the CIP delegate determined a Reportable Cyber Security Incident (1-hour clock) or an attempt to compromise (end of the next calendar day).
4. **Materiality determination time** (SEC): recorded later by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.
5. **Breach determination time** (state laws): when the company determined that personal information was breached, or had reason to believe it was. This starts the Florida 30-day clocks.

## 3. First hour (RS.MA, RS.MI)
**Grid safety comes first (POL-03 4.7).** The DCC does not wait for forensics to protect people and equipment.

| Step | Who | Done when |
|---|---|---|
| 1. Put affected feeders under manual control; confirm crews and clearances are safe; issue a hold on remote switching for affected substations; dispatch crews to staff key substations | Director, Distribution Control Center | Holds logged; crews confirmed safe |
| 2. Disable all vendor remote access to OT through the PAM kill switch; disconnect the ADMS DMZ from the corporate network if activity crosses it | SOC; OT Security (with DCC approval) | Vendor sessions at zero; DMZ isolation confirmed |
| 3. Tell the TCC; the TCC checks EMS and Electronic Access Point logs and informs the Reliability Coordinator under its procedures | Director, Transmission Operations | RC informed |
| 4. CIP delegate evaluates whether any high or medium impact BES Cyber System or EACMS is involved and records a determination (or "not yet determined") with the time | CIP Senior Manager's delegate | Determination logged |
| 5. **DOE-417 Emergency Alert within 1 hour of the incident** if criterion 2, 3, 6, or 7 applies (phone the DOE Operations Center first if filing would distract from operations) | DCC shift supervisor with the NERC compliance analyst | Confirmation number logged |
| 6. CISO briefs the CEO and the General Counsel; counsel engages outside counsel and OT forensics under privilege; insurer notified through the hotline | CISO; General Counsel | Engagement letters; claim number |
| 7. COO activates the crisis management team; Corporate Communications prepares outage messages that do not speculate on cause | Chief Operating Officer | Crisis team convened |
| 8. Start the incident log (timeline, decisions, who, when) and the evidence register | Enterprise incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** which consoles, servers, jump hosts, accounts, field devices, and substations were touched. Sources: OT PAM recordings, jump host logs, ADMS command logs (every command is tied to a user), OT sensor captures, EDR on ADMS hosts, firewall logs.
2. **Initial access:** vendor support path, stolen engineer or vendor credentials, the corporate-to-historian rules (until POAM-002 closes), a field gateway, or a transient device. Check vendor paths first.
3. **Control actions:** list every unauthorized command with the device, time, and result; compare device settings (relays at distribution substations, recloser and capacitor controls) against the OT CMDB baselines. Assume settings may have been changed even where no command was seen.
4. **EMS and BES Cyber Systems:** OT Security and the TCC confirm whether the attacker reached or probed the EMS Electronic Access Point, an Intermediate System, or a medium impact substation. Any such activity goes to the CIP delegate for the CIP-008 determination.
5. **Data:** check OMS and GIS access for customer data (names, addresses, phone numbers, medical-priority flags, premise locations), and any path to the CIS. This drives section 7.
6. **Evidence:** preserve memory and disk images of Windows hosts before rebuild (CIP-009-6 R1.5 style, per Cyber Asset capability); export controller and gateway logs; keep chain of custody in the evidence register; never power-cycle a field device until its logs are pulled, unless safety requires it.
7. **Business impact:** Finance and the BIA owners estimate impact with P05 values (for example, about $3.6 million per day if remote switching is lost during normal weather, far more in a storm; restoration cost, customer credits, and regulatory exposure). These estimates feed section 6.

## 5. Containment and eradication (RS.MI)
1. Keep the grid in a safe, manually operated state until containment is confirmed; return feeders to service by field switching where needed.
2. Remove the attacker's access path: disable the vendor account and path, rotate all ADMS domain, jump host, PAM, and service account credentials, and revoke certificates issued to affected hosts.
3. Rebuild affected consoles and servers from golden images; restore ADMS configuration from the last verified offline backup; never reuse a compromised host.
4. Verify settings on every field device the attacker could reach against the baseline; reset any default credentials found (POAM-013).
5. Re-enable remote switching substation by substation, starting with the highest load, after OT Security and the DCC director sign off each one.
6. Forensics confirms persistence is removed before the ADMS returns to full remote operation; vendor access stays off until the vendor's path is rebuilt through the jump hosts.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.5) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 and 5 | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date, time, and reasoning, whether material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay. For a grid attack, counsel considers early contact with the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align timing and content of customer, client, media, regulator, and investor communications with the filing; brief the audit committee and risk and reliability committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | P05 BIA outage costs (restoration, overtime, customer credits); forensic and rebuild costs; capital acceleration (for example, legacy gateway replacement); lost sales; expected penalties; insurance coverage and the $10 million retention; effect on rate recovery |
| Operational | Customers out and for how long; whether remote control was lost; whether the attacker could repeat the attack; storm season timing |
| Safety | Any harm or near miss to workers or the public; medical-priority customers affected |
| Reliability and regulatory | Whether BES Cyber Systems were reached; DOE-417 and EOP-004 filings; possible NERC violations; state commission inquiries; FERC or DOE attention |
| Data | Customer data accessed; states of residence; Utility Services clients affected |
| Reputation and strategy | National media; rating agency comment; effect on rate cases and the service lines |

**Worked example of the clocks (fictional dates):**
- **Tuesday 2027-01-12, 06:40:** 31 feeder breakers at 9 substations open without operator command during the winter morning peak; about 142,000 customers and about 420 MW are interrupted. 06:52: the DCC confirms no switching orders and declares a severity-1 OT incident.
- **DOE-417 Emergency Alert by 07:40** (1 hour from the incident): criterion 3 (cyber event causing interruption of electrical system operations) and criterion 6 (uncontrolled loss of 300 MW or more of firm load for more than 15 minutes). The DCC supervisor phones the DOE Operations Center at 07:25 and the written form follows.
- **EOP-004-4:** the same load loss meets the uncontrolled loss of firm load threshold for an entity with a prior-year peak of 3,000 MW or more. The DOE-417 form is submitted with sharing to NERC selected, so it also serves as the EOP-004 report (otherwise due by 4 p.m. on Wednesday 2027-01-13, the end of the next business day).
- **09:15:** the SOC finds scans from a compromised ADMS DMZ host against the TCC Electronic Access Point. **11:30:** the CIP delegate determines this was an attempt to compromise an EACMS of a high impact BES Cyber System. **CIP-008-6 R4 notice to the E-ISAC and CISA by 23:59 on Wednesday 2027-01-13**, with the three attributes. A DOE-417 update records the new cyber information.
- **Thursday 2027-01-14, 16:00:** the disclosure committee determines the incident is material (loss of remote control at scale, repeat risk, safety and reliability implications). **Form 8-K due Thursday 2027-01-21:** 4 business days are January 15, 19, 20, and 21, because Monday 2027-01-18 is a federal holiday (Martin Luther King Jr. Day), when the SEC is closed.
- **Monday 2027-02-01:** forensics confirms the attacker exported OMS records for about 61,000 Florida customers, including medical-priority flags. Counsel determines on that date that a breach of personal information occurred. **Florida 30-day clocks** (individuals and the Department of Legal Affairs) run to Wednesday 2027-03-03. Counsel must also decide whether a "reason to believe" arose earlier, which would move the dates forward. Georgia residents are handled under Georgia law through counsel's state matrix.

## 7. Regulatory and breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** The Director, NERC Compliance owns the NERC and DOE rows; the Chief Privacy Officer owns the state rows; the General Counsel owns the SEC rows.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | DOE-417: file the Emergency Alert, Normal Report, Attempted Cyber Compromise, or System Report as the criteria require; select sharing with NERC, the E-ISAC, and CISA on line W; file updates and the 72-hour final report | Director, NERC Compliance | Filing confirmations |
| 7.2 | CIP-008-6 R4: notify the E-ISAC and CISA within 1 hour of a Reportable determination or by the end of the next calendar day for an attempt to compromise; updates within 7 calendar days of new attribute information | Director, NERC Compliance | Notices with the three attributes |
| 7.3 | EOP-004-4: report Attachment 1 events through the DOE-417 form or the EOP-004 Attachment 2 form | Director, NERC Compliance | Submission |
| 7.4 | Decide whether any NERC requirement was violated during the incident and, if so, self-report to SERC | Director, NERC Compliance | Self-report decision record |
| 7.5 | Build the affected-person file from forensics: each individual, data elements, and **state of residence**; separate company customers from SL-1 client utilities' customers | Chief Privacy Officer | Affected-individual file with state counts |
| 7.6 | **SL-1 clients:** the company is their third-party agent; notify each affected client utility within 24 hours (contract) and no later than 10 days after determination (Fla. Stat. 501.171(6) worked example); clients decide their own notices | Vice President, Utility Services | Client notices sent |
| 7.7 | Apply **each state's law** for every state with affected residents, using counsel's state matrix; record the earliest deadline per state | Outside counsel; General Counsel | State deadline table |
| 7.8 | **Florida worked example:** individual notice within 30 days of determination (15 more days only for individual notice, on good cause); Department of Legal Affairs within 30 days if 500 or more Floridians; consumer reporting agencies if more than 1,000 are notified at once | Chief Privacy Officer | Florida filings |
| 7.9 | **Plan to the shortest clock** across DOE, NERC, SEC, every state, and the contracts; publish one master calendar | Chief Privacy Officer; Director, NERC Compliance | Master calendar |
| 7.10 | Honor any law enforcement delay request where the state law allows it; document it | General Counsel | Delay record |
| 7.11 | Tell the state public service commissions through Regulatory Affairs under their outage and incident rules (outside the scope of this sample) | Regulatory Affairs | Commission notices |

**Extortion or ransom:** any payment needs the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.9). Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying never removes reporting or disclosure duties.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a validated state first:
1. EMS at the TCC or backup TCC (only if affected; under the CIP-009 recovery plan)
2. OT identity domains, OT PAM, and sealed emergency accounts (new credentials)
3. ADMS at the DCC or backup DCC from verified offline backups and golden images (2-hour target; 5 h 20 min demonstrated, POAM-005)
4. OMS and mobile dispatch
5. Contact center, IVR, and the direct DCC hazard line
6. Storm command tools
7. Physical access control and alarm monitoring
8. Substation and field communications, substation by substation, after settings are verified
9. Enterprise identity, network core, and security tooling (if affected)
10. Fleet charging management, load forecasting, portal and app, AMI connects, Utility Services, payments, billing, ERP (only if affected)

**Validate before reconnecting:** clean EDR scans, credentials rotated, device settings matched to baselines, logging to the SIEM, OT sensors watching the restored segment. Keep manual-mode procedures until each process meets its RTO. Tell customers, clients, regulators, and staff when remote operation returns (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days; the CIP-008 plan and this runbook updated and roles notified within 90 days (POL-03 4.12).
- Update the risk register (P01: R-001, R-002, R-006, R-016), the POA&M (P07), and the materiality playbook.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including determination minutes, filings, and breach assessments, for at least 7 years (POL-01 4.12).
