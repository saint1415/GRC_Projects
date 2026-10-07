# Incident Response Runbook: Network Intrusion Exposing CPNI

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded regional broadband and wired telecommunications carrier; FL, GA, SC, NC) |
| Tier / Vertical | Enterprise / Communications |
| Incident type | Network intrusion exposing customer proprietary network information (CPNI): exploitation of an internet-facing edge device or an unsupported SBC, movement through the network management plane with shared or stolen credentials, and theft of call detail records from the CDR store, with possible reach toward lawful-intercept systems. Includes the **SEC materiality assessment and Form 8-K Item 1.05** step, the **Item 1.05(d)** CPNI delay, and a multi-state notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 PSAP, 988, and NORS Notification Procedure; PRC-03.5 CALEA Compromise Reporting Procedure |
| Runbook owner | Director of Security Operations, with the General Counsel for sections 6 and 7 and the Vice President, Network Operations Center for service protection |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise tabletop 2026-03-24 (technical response and NOC coordination; **the disclosure committee did not take part and the 64.2011 hold was not exercised**). Next: full tabletop with the disclosure committee on 2026-11-12 (POAM-013) |
| Notification matrix | `notification-matrix.csv` (35 obligations: 7 CPNI, 1 CALEA, 6 outage reporting, 6 SEC, 2 generic state, 5 Florida worked example, plus OFAC, CIRCIA status, 3 FAR, and 3 contractual rows) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | Out-of-band conferencing on company mobile phones |
| Service protection and outage notices | Vice President, Network Operations Center (24x7 NOC shift lead) | NOC-2 shift lead | NOC hotline; out-of-band bridge |
| Management plane containment | Director of Network Security Engineering | Network engineering on-call | Out-of-band bridge |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Chief Network Officer | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Chief Accounting Officer, CISO, Chief Privacy Officer, Chief Compliance Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| CPNI breach determination and law enforcement notice | Chief Privacy Officer | Chief Compliance Officer | Direct mobile; reporting facility accounts held by 3 trained staff |
| CALEA compromise reports | Director, Lawful Intercept Compliance (and each subsidiary's designee) | General Counsel | Direct mobile; agency contacts in the SSI appendices |
| Outside counsel and forensics | Telecommunications regulatory counsel; breach counsel and forensics through the insurer panel | n/a | Retainer hotlines |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | FBI field office; USSS (through the FCC reporting facility for CPNI breaches) | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read email, chat, and the management network. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder at NOC-1, NOC-2, DC-1, and DC-2. No incident details in tickets until the incident commander clears the ticketing system.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder current at both NOCs and both data centers: this runbook, the notification matrix, PSAP and 988 contact lists, the business-day calendar, and the disclosure committee roster
- [ ] FCC CPNI breach reporting facility access tested this quarter for the 3 trained staff
- [ ] Network element logs and flows in the SIEM (**58% coverage until POAM-004 closes**; export element logs on day 0 where they are only local)
- [ ] Object-level read logging on the CDR store confirmed (needed to scope which customers' call detail was read)
- [ ] Sealed break-glass console credentials for management plane jump hosts at DC-1 and DC-2
- [ ] Shared local passwords on legacy elements rotated after every administrator departure (**gap until POAM-002 closes**)
- [ ] Materiality playbook with the joint CPNI and SEC clock and the Item 1.05(d) EDGAR correspondence template (**gap until POAM-013 closes**)
- [ ] Outside counsel, forensics, and insurer contacts confirmed this quarter; state breach law matrix updated within 12 months
- [ ] PSAP contacts confirmed within 12 months (**37 AQ records open until POAM-021 closes**)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Login to a network element or adapter host from a source that is not a jump host | TACACS+ accounting; element logs in the SIEM | SOC opens a security case; NOC confirms whether a change window exists |
| Configuration change, new local account, or reboot on an SBC, edge router, or OLT outside a maintenance window | NOC configuration-diff report; element managers | NOC opens a case and calls the SOC |
| OSS adapter or rating service account reading the CDR store at unusual volume or from a new source | Cloud audit and object access logs | Disable the key; open a case |
| Large outbound transfer from DC-1, DC-2, or a cloud account to an unknown destination | Edge firewall; cloud flow logs | Block the destination; preserve logs |
| Vendor, CISA, FBI, or FCC advisory naming an exploited flaw in company equipment | Threat intelligence | Treat as possible compromise; hunt on matching devices |
| Law enforcement contact about the company's network, intercepts, or data | FBI, USSS, or another agency | Route at once to the General Counsel, Chief Privacy Officer, and Director, Lawful Intercept Compliance |
| Extortion message or data-leak post naming company customers | Email; threat intelligence; media | Declare; preserve; do not engage without counsel |

**Declare a severity-1 CPNI intrusion when** an unauthorized actor is confirmed on a voice core, management plane, adapter, or CDR store component, or evidence shows call detail or other CPNI may have left the company.

**Record three times, separately:**
1. **Discovery time:** when anyone at the company first knew of the suspected intrusion. This starts outage clocks if service is affected and the SEC "without unreasonable delay" expectation for the materiality determination.
2. **Reasonable determination of a CPNI breach** (Chief Privacy Officer with counsel): a person intentionally gained access to, used, or disclosed CPNI without or beyond authorization (47 CFR 64.2011(e)). This starts the 7-business-day law enforcement clock and, where Florida-defined personal information is involved, Florida's 30-day clock. Do not wait for forensics to finish; evidence that the CDR store was read by an unauthorized account is enough.
3. **Materiality determination time** (disclosure committee, section 6). This starts the 4-business-day Form 8-K clock.

## 3. First 2 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the out-of-band bridge; start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open |
| 2. **Check service impact first:** will containment affect voice, 911, broadband, SS7, or SL-2? Any service-affecting action needs joint approval by the incident commander and the NOC shift lead (POL-03 4.5) | NOC shift lead | Decision logged |
| 3. If any 911 or 988 special facility is potentially affected: PSAP and 988 notices within 30 minutes; NORS notification within 120 minutes (wireline and SS7) or 240 minutes (VoIP, facility affected) | Vice President, Network Operations Center | Notices sent; NORS receipt |
| 4. Isolate the exploited edge device or SBC management interface; fail voice to the geo-redundant SBC cluster | Director of Network Security Engineering with the NOC | Isolation confirmed; calls completing |
| 5. Cut AQ-02 and AQ-03 site VPN routes to the management plane if activity crosses from an AQ network (POAM-003 open) | Network engineering | Routes removed |
| 6. Disable compromised adapter and service accounts; rotate keys; force administration through clean jump hosts with break-glass credentials | Identity team; Network Security Engineering | Revocations logged |
| 7. **Preserve evidence before it rolls over:** element logs held locally, TACACS+ accounting, jump host logs, cloud object access logs, VPN logs, configuration snapshots; write-once storage with hashes | SOC; NOC | Exports hashed and stored |
| 8. CISO briefs the CEO and General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Engagement letters; claim number |
| 9. Ask: could the lawful-intercept enclave, an AQ intercept function, or intercept records have been reached? If it cannot be ruled out, the Director, Lawful Intercept Compliance, starts the CALEA track (section 7.3). Forensics may not view intercept content | Director, Lawful Intercept Compliance | Decision logged |
| 10. COO activates the crisis management team if service, many customers, or public safety is affected | COO | Crisis team convened |

## 4. Analysis (RS.AN)
1. **Initial access:** the device and flaw used, the time of first access, and other devices on the same advisory. Check AQ-02 SBCs and edge routers first while POAM-008 is open.
2. **Movement:** trace from the entry device through the management plane: TACACS+ accounting, jump host sessions, shared local account use on legacy elements (POAM-002), element login histories, and OSS adapter sessions.
3. **What CPNI was taken:** which CDRs (date range, lines, carrier subsidiary) were read or copied from the CDR store, and whether the BSS, portal, or data platform was reached. Use object access logs. **If object-level evidence is missing for any period, treat all call detail in that period as exposed** (up to 36 months for about 1.15 million lines).
4. **Personal information for state law:** whether state-defined personal information was involved (for example, portal credentials, SSNs, or financial account data). Call detail with names and numbers alone may not meet some state definitions; counsel decides per state.
5. **Lawful intercept:** through the authorized employees only, whether any intercept function, its management path, or intercept records were accessed.
6. **Persistence:** new accounts, changed configurations, implants on SBCs and routers, altered TACACS+ or SNMP settings, and tampered firmware. Where firmware integrity cannot be verified, plan device replacement.
7. **Business impact for section 6:** Finance and the BIA owners estimate impact using P05 values (for example, about $9.4 million per day if broadband is disrupted enterprise-wide; about $2.6 million per day for voice), plus forensic, notification, credit monitoring, legal, and contract costs.

## 5. Containment and eradication (RS.MI)
1. Replace or rebuild compromised SBCs and edge devices on supported releases; never return a suspect unit to service.
2. Rotate every shared element password, SNMP community, TACACS+ key, VPN pre-shared key, adapter credential, and service account secret. Assume all were exposed.
3. Rebuild adapter hosts and mediation collectors from known-good images; restore the CDR store only from backups that predate first access and pass integrity checks.
4. Restrict adapter accounts to the commands and elements they need before reconnecting.
5. Forensics confirms persistence is removed in each zone before recovery starts there.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. The materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.7) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives (POL-05 4.10) | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 and 5 | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date, time, and reasoning, whether material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | **Joint clock check (CPNI and SEC).** If the incident is also a CPNI breach, 64.2011(a) and (b)(1) bar public disclosure until 7 full business days after the USSS and FBI notice. Item 1.05(d) lets the company delay the 8-K for that period, in no event more than seven business days after the law enforcement notice, **only if** it sends EDGAR correspondence to the SEC no later than the date the 8-K was otherwise due. Counsel sets the exact filing date and time so both texts are met | General Counsel; outside securities and telecommunications counsel | Joint clock entered in the master calendar |
| 6.7 | If material: draft the Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.8 | **File within 4 business days after the determination**, or by the Item 1.05(d) date if step 6.6 applies and the correspondence was filed on time. If the investigating agency directs a longer customer-notice delay under 64.2011(b)(3), Item 1.05(d) does not cover it; any further SEC delay needs a written Attorney General determination under Item 1.05(c), requested through outside counsel and the Department of Justice | General Counsel | Filing confirmation |
| 6.9 | Align timing and content of customer, business customer, media, and investor communications with the filing and the CPNI hold; brief the audit committee and the risk and technology committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.10 | Keep reassessing as facts change; file an amendment within 4 business days after information that was not available becomes available (Instruction 2 to Item 1.05). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Credits and lost revenue from P05 values; forensic, rebuild, and device replacement costs; notification, call center, and credit monitoring costs; insurance coverage and retention; effect on liquidity and covenants |
| Operational | Services affected (voice, 911, broadband, SS7, SL-1, SL-2) and for how long; number of states and customers |
| Data | Number of customers and lines; date range of call detail; whether intercept-related data or government customers' CPNI is involved; whether data was published |
| Public safety and national security | 911 outages; lawful-intercept exposure; government customers affected |
| Legal and regulatory | FCC enforcement exposure (CPNI, CALEA, outage rules); state attorney general inquiries; contract breaches with enterprise, federal, wholesale, SL-1, and SL-2 customers; litigation |
| Reputation and strategy | Media coverage; customer churn; effect on pending acquisitions and the AQ integrations |

**Worked example of the clocks (fictional dates, no holidays in the period):** suspicious logins discovered Monday 2027-03-01 at 09:30. The disclosure committee convenes Tuesday 2027-03-02. CDR store reads by a compromised adapter account are confirmed, and the Chief Privacy Officer records the reasonable determination of a CPNI breach on Wednesday 2027-03-03. The committee determines the incident is material on Thursday 2027-03-04 at 16:00, so the 8-K is otherwise due Wednesday 2027-03-10 (4 business days: March 5, 8, 9, and 10). The USSS and FBI notice goes in through the reporting facility on Friday 2027-03-05 (business day 2; the legal limit would be Friday 2027-03-12). The CPNI hold runs 7 full business days after that notice, through Tuesday 2027-03-16. The company sends the Item 1.05(d) EDGAR correspondence by 2027-03-10. Counsel then sets the exact 8-K filing date and time so that both texts are met: the FCC hold (no public disclosure until 7 full business days have passed after the notice) and the SEC cap (no more than seven business days after the notice). The playbook flags this day as a counsel decision rather than fixing it in advance. Customer notices go out from Wednesday 2027-03-17. Florida's 30-day clock (individuals, and the Department if 500 or more Floridians) runs from the 2027-03-03 determination to Friday 2027-04-02, so Florida is met. If the FBI or USSS directs a longer delay under 64.2011(b)(3), get the direction in writing: Florida also allows delay on a law enforcement agency's written request (501.171(4)(b)), but the SEC delay then needs the Attorney General path.

## 7. Notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms each obligation before notices go out. The current 47 CFR 64.2011 is in force; the 2023 amendments are not yet effective (P03 section 1.3). Recheck the Federal Register for an FCC effective-date notice at the start of every incident.

### 7.1 Service and outage notices (from minute 0)
| When | Action | Owner | Citation |
|---|---|---|---|
| Within 30 minutes of discovering an outage that potentially affects a PSAP or 988 facility | Telephone and electronic notice to designated contacts; first follow-up within 2 hours | Vice President, Network Operations Center | 47 CFR 4.9(h), (i) |
| Within 120 minutes (wireline, SS7) or 240 minutes or 24 hours (VoIP) of discovering a qualifying outage | NORS notification; initial report within 72 hours (wireline and SS7); final report within 30 days | Vice President, Network Operations Center; Chief Network Officer approves | 47 CFR 4.9(b), (d), (f), (g); 4.11 |
| Daily, if DIRS is activated | DIRS reports | Vice President, Network Operations Center | 47 CFR 4.18 |

### 7.2 CPNI breach (from the reasonable determination)
| Step | Action | Owner | Output |
|---|---|---|---|
| 7.2.1 | Document the reasonable determination with date and basis, by carrier subsidiary | Chief Privacy Officer with counsel | Determination memo |
| 7.2.2 | **Internal target 2 business days; legal limit 7 business days:** electronic notice to the USSS and FBI through the FCC reporting facility. Flag any extraordinarily urgent need for earlier customer notice | Chief Privacy Officer | Reporting facility receipt |
| 7.2.3 | **Hold:** no customer or public disclosure until 7 full business days after that notice, notwithstanding contrary state law, unless the investigating agency agrees or directs otherwise. Staff, vendor, and media scripts say only "we are investigating a network security issue" | General Counsel; Vice President, Corporate Communications | Holding statements approved |
| 7.2.4 | After the hold: notice to each customer whose CPNI was breached; enterprise and government accounts through their account representatives | Chief Privacy Officer; Chief Customer Officer | Notices sent |
| 7.2.5 | Breach record (dates, CPNI description, circumstances) kept at least 2 years | Chief Privacy Officer | Breach register entry |
| 7.2.6 | If BSS approval flags were altered so customers cannot opt out: written FCC notice within 5 business days | Vice President, Regulatory Affairs | FCC letter |
| 7.2.7 | Next annual certification: accurate operating-procedures statement and complaint summary | Chief Compliance Officer | Certification evidence package |

### 7.3 CALEA (if lawful intercept may be involved)
The Director, Lawful Intercept Compliance (or the subsidiary designee), reports any compromise of a lawful interception or of call-identifying information, and any unlawful electronic surveillance on company premises, to the affected law enforcement agencies within a reasonable time upon discovery (47 CFR 1.20003(c)), using the SSI appendix contacts. **AQ-03's appendix is out of date until POAM-020 closes; use the enterprise LI compliance team's contacts.** Details stay in the restricted CALEA record, not in the incident log.

### 7.4 State notices (multi-state)
| Step | Action | Owner | Output |
|---|---|---|---|
| 7.4.1 | Build the affected-customer file from forensic results: each customer, data elements, carrier subsidiary, and **state of residence** (service and billing addresses) | Chief Privacy Officer; data team | Affected-customer file with state counts |
| 7.4.2 | Apply **each state's law** using counsel's matrix: whether the data meets the state's definition, individual timelines, regulator and attorney general notices, consumer reporting agency thresholds, and whether a federal-regulator notice satisfies the state. Record the earliest deadline per state | Outside counsel; General Counsel | State deadline table |
| 7.4.3 | **Florida worked example:** individual notice within 30 days of determination; Department of Legal Affairs notice within 30 days if 500 or more Floridians; consumer reporting agencies if more than 1,000 are notified at once; a timely copy of notice given under the primary or functional federal regulator's rules is deemed compliant (counsel decides whether the FCC CPNI notice qualifies); a no-harm determination must be written, kept 5 years, and sent to the Department within 30 days | General Counsel | Florida filings |
| 7.4.4 | **Plan to the shortest clock** across the CPNI hold, every state, the SEC, and contracts. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 7.4.5 | Engage the mail vendor, call center, and credit monitoring provider (if personal information is involved) | Chief Privacy Officer | Vendors active |
| 7.4.6 | Track inbound vendor notices if the incident started at a vendor (Florida third-party agent duty: 10 days; company contracts: 24 hours) | Director of Third-Party Risk Management | Vendor notices logged |

### 7.5 Federal contracts and other parties
- If covered telecommunications equipment is identified (for example, in an acquired network during rebuild), report to the contracting officer within 1 business day under FAR 52.204-25(d); a Kaspersky covered article within 3 business days under FAR 52.204-23(c); a FASCSA covered article within 3 business days under FAR 52.204-30. Each has a further report within 10 business days.
- Enterprise, federal, wholesale, SS7, SL-1, and SL-2 customers: per contract, after the CPNI hold for CPNI-related content.
- CIRCIA is not in effect; make a voluntary report to CISA and the FBI on day 0 to 2.

**Extortion or ransom demand:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.10). Paying does not remove any notification or disclosure duty.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Voice core and 911 trunks (geo-redundant SBC cluster; replacement SBCs)
2. Management plane: clean jump hosts, TACACS+ with rotated keys, configuration archive verified against offline copies
3. Identity platform and break-glass access
4. STP pairs, backhaul, and SL-2 voice
5. Security tooling for validation; network element logging onboarded for rebuilt devices
6. Broadband gateways, DNS and DHCP, business transport
7. SL-1 orchestration (tell SL-1 customers the status)
8. BSS and CCaaS (care), with the chatbot in outage-message mode until its API client is re-scoped
9. Lawful-intercept platform, re-provisioned from mediation order records by authorized employees
10. AQ-02 and AQ-03 legacy systems behind enterprise jump hosts
11. Portal, app, OSS dispatch and activation
12. Mediation and the CDR store: back within 72 hours, before switch CDR buffers overflow (P05 BP-12)

**Validate before reconnecting:** credentials rotated, devices patched or replaced, logging to the SIEM. Tell customers, PSAPs, and business customers when service is fully restored (RC.CO), and file the final NORS report within 30 days.

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.13).
- Update the risk register (P01: R-001, R-003, R-007, R-008, R-009, R-012, R-014), the POA&M (P07), this runbook, and the materiality playbook.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Keep the CPNI breach record at least 2 years (64.2011(d)) and all incident documentation, including materiality minutes and the EDGAR correspondence, at least 6 years (POL-01 4.11).
