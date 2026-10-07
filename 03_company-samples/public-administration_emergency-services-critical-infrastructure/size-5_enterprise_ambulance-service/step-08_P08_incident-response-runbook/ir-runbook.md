# Incident Response Runbook: CAD Outage from Ransomware

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded private ambulance provider; FL, GA, AL, SC, TN) |
| Tier / Vertical | Enterprise / Emergency Services |
| Incident type | Ransomware encrypts the enterprise CAD application tier and dispatch consoles at two communications centers, forcing manual dispatch across several counties, with possible theft of CAD data and call recordings. Includes the SEC materiality assessment, county notifications, and a multi-state breach notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 County Notification Procedure; STD-03.4 Manual Dispatch and Center Failover Standard |
| Runbook owner | Director of Security Operations (HIPAA Security Officer), with the Vice President, Communications Centers for Track A and the General Counsel for sections 7 and 8 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise tabletop 2026-03-24 (technical response and manual dispatch; **the disclosure committee did not take part and the scenario was a data breach, not a dispatch outage**). Quarterly manual dispatch drills at RCC-1 to RCC-3. Next: full tabletop with the disclosure committee using this scenario on 2026-11-18 (POAM-014) |
| Notification matrix | `notification-matrix.csv` (36 obligations: 9 HIPAA, 4 generic state, 6 Florida worked example, 4 SEC, plus county, service line, insider trading blackout, OFAC, law enforcement, CIRCIA status, insurance, and not-applicable rows) |

**Two tracks run at once.** Track A keeps ambulances moving (dispatch continuity). Track B handles the security incident. **Track A never waits for Track B**, and no one on Track B may take an action that stops dispatch without the dispatch supervisor's agreement.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Dispatch continuity (Track A lead) at each affected center | On-duty dispatch supervisor | Communications center manager | Dispatch floor; supervisor cell; company radio talkgroup |
| Dispatch continuity (enterprise) | Vice President, Communications Centers | Director of CAD and Dispatch Systems | Crisis line |
| Incident commander (Track B lead) | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Chief Medical Officer | Crisis line |
| Clinical safety | Chief Medical Officer, with the Medical Director for Communications | Regional medical directors | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Chief Operating Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Breach and privacy decisions | Chief Privacy Officer (HIPAA Privacy Officer) | Chief Compliance Officer | Direct mobile |
| County liaison | Vice President, Government Relations and County Contracts | Regional operations directors | County contact sheet in the incident binder |
| Service line clients | Vice President, EMS Billing Services (SL-1); President, Managed Transportation (SL-2) | Client account managers | Client contact lists |
| Outside breach counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | MSSP incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (for investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, the identity platform, and anything on the console network may be compromised. Use company mobile phones, the out-of-band conferencing service, company radio talkgroups, and the printed incident binder at every communications center and regional office.

## 1. Preparation checks (Identify / Protect)
- [ ] Manual dispatch kits at every center: paper incident cards, unit status boards, run cards by zone, radio procedures, county PSAP numbers (STD-03.4)
- [ ] Manual dispatch drilled in the last 90 days at every center, **including RCC-4 (gap until POAM-007 closes)**
- [ ] Center-to-center failover tested for every center, **including RCC-3 (gap until POAM-011 closes)**
- [ ] Immutable CAD database snapshots in a separate backup account, restore-tested in the last 90 days (CP-9, CP-4)
- [ ] Standby region images current and the regional failover runbook rehearsed; **automated interface cutover not yet built (POAM-011)**
- [ ] EDR on all consoles, CAD servers, and MDCs, **except AQ-01 workstations (gap until POAM-023 closes)**; SIEM receives logs from all dispatch systems **except the AQ-01 legacy CAD (gap until POAM-005 closes)**
- [ ] 20 pre-imaged spare consoles kept offline at each of RCC-1 to RCC-3
- [ ] Break-glass accounts sealed and tested this quarter (POL-02 4.11)
- [ ] Materiality playbook and 8-K templates current, including operational-outage factors; disclosure committee roster current (**gap until POAM-014 closes**)
- [ ] Outside counsel, forensics, and insurer contacts confirmed this quarter; state breach law matrix updated in the last 12 months

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| CAD client freezes or errors on several consoles at once | Dispatchers | Supervisor starts Track A (manual mode) at once; calls the SOC |
| Ransom note on a console, or files renamed with an unknown extension | Dispatcher, EDR alert | **Do not power off.** Isolate through EDR or unplug the network cable. Start Track A. SOC opens a severity-1 case |
| CAD servers or database unreachable; mass changes or deletions in the cloud account | SOC, cloud threat detection | SOC opens a case; incident commander paged |
| MDCs lose CAD but radio works | Crews | Crews switch to radio status reports; dispatch confirms manual mode |
| Suspicious activity from the AQ-01 network or legacy directory | Network detection, VPN logs, local IT firm | Treat as severity 1 until scoped; cut the AQ-01 site VPN if activity reaches the integration hub |
| Extortion message or leak-site post naming the company | Email, threat intelligence, law enforcement, media | Declare; preserve; do not engage without counsel |
| A vendor (CAD vendor, ePCR vendor, telephony vendor) reports ransomware affecting company data or services | Vendor notice (BAA) | Open a vendor incident case; start the third-party track in section 8 |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any production dispatch system, or an extortion claim names company data.

**Record two times, separately:**
1. **Discovery time** (HIPAA): the first day the breach was known, or by reasonable diligence would have been known, to any workforce member or agent (45 CFR 164.404(a)(2)). This starts the 60-day HIPAA clock. The Florida clock starts at determination of the breach or reason to believe one occurred (Fla. Stat. 501.171(4)).
2. **Materiality determination time** (SEC): recorded later by the disclosure committee (section 7). This starts the 4-business-day Form 8-K clock.

## 3. Track A: keep dispatching (RC.RP; CP-2, CP-7)
| Step | Who | Done when |
|---|---|---|
| A1. Announce "manual dispatch" on every affected talkgroup. Units report location and status by radio | On-duty dispatch supervisor | All staffed units acknowledged |
| A2. Call each affected county PSAP supervisor: CAD-to-CAD is down; ask the PSAP to voice-announce new calls on the radio system and transfer callers by phone (PRC-03.4) | On-duty dispatch supervisor | Every affected PSAP confirms |
| A3. Paper incident cards and unit status boards; one call-taker, one radio dispatcher, and one unit tracker per zone; the supervisor assigns | Dispatchers | Board matches the radio roll call |
| A4. Decide whether to move positions to an unaffected center (RCC-3, or RCC-1 or RCC-2 if unaffected). Do not fail over to a center that shares the affected network segment until the SOC clears it | Vice President, Communications Centers with the incident commander | Positions moved or decision logged |
| A5. Forward request lines and transferred-caller lines to unaffected centers or supervisor phones if console phones are affected | Communications center manager | Test call answered |
| A6. Defer scheduled non-urgent interfacility trips; tell hospitals and facilities the expected delay | Vice President, Field Operations | Facility call list done |
| A7. Crews switch to paper patient care records if tablets cannot sync | Vice President, Field Operations | Crews confirm |
| A8. **At 2 hours in manual mode (P05 MTD)**, or sooner if the Chief Medical Officer judges it unsafe, ask the county to activate mutual aid for new 911 calls in the most affected zones | Chief Operating Officer with the Chief Medical Officer | County confirms |
| A9. Log every Track A decision with the time; the Medical Director for Communications reviews delayed calls in real time | Dispatch supervisor; Medical Director for Communications | Log kept |

## 4. Track B: first 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| B1. Isolate affected consoles and servers through EDR; do not power them off (preserve memory) | SOC | Hosts network-contained |
| B2. Block attacker infrastructure; if activity crosses from AQ-01, cut the AQ-01 site VPN; block vendor remote tools until cleared | SOC; Network Engineering | Blocks confirmed |
| B3. Revoke sessions and rotate credentials for privileged and service accounts involved; use break-glass accounts if SSO is affected | Identity team | Revocations logged |
| B4. Confirm the backup account and the standby region are untouched (immutability locks, no recent deletions, replication paused if the primary database is affected) | Cloud Platform Engineering | Backup integrity confirmed |
| B5. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| B6. COO activates the crisis management team | COO | Team convened |
| B7. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open |

## 5. Analysis (RS.AN)
1. **Scope:** which consoles, CAD servers, cloud accounts, identities, and centers are affected. Use EDR, SIEM, cloud audit logs, PAM records, and network detection. For AQ-01, collect legacy CAD and directory logs locally, because they are not in the SIEM.
2. **Initial access:** phishing, stolen credentials, an edge device, a vendor remote tool (check the radio console gateway tool while POAM-004 is open), a vehicle router, or the AQ-01 network. Check the AQ-01 VPN path first while POAM-016 is open.
3. **Evidence:** forensics images hosts and exports logs before they roll over; chain of custody is kept in the evidence register; hashes recorded for each artifact.
4. **Exfiltration:** determine whether CAD incident records (names, addresses, chief complaints), call recordings, ePCR extracts, or SL-2 member data left the environment, and for which people. Sources: egress logs, object storage access logs, database query logs, the attacker's claims and samples. **This drives section 8.**
5. **Integrity:** confirm no incident, unit, or response plan data was altered before restoring (compare to snapshots; check CAD audit trails). The Medical Director for Communications must approve response plans before CAD returns to live use.
6. **Business impact:** Finance and the BIA owners estimate daily impact using P05 values (for example, about $2.4 million per day if 911 dispatch at RCC-1 to RCC-3 runs manually, about $1.2 million per day if interfacility scheduling stops, and county late-response penalties). These estimates feed section 7.

## 6. Containment and eradication (RS.MI)
1. Contain by segment: isolate affected centers, accounts, or the AQ-01 network.
2. Disable compromised accounts; reset all privileged credentials and service account secrets; rotate CAD-to-CAD certificates, integration keys, and mobile gateway credentials (tell each county PSAP before rotating its certificate).
3. Rebuild consoles from the standard image or deploy the offline spares; rebuild CAD servers from clean images in the standby region. **Never decrypt and reuse encrypted hosts.**
4. Patch the initial access path before reconnecting.
5. Forensics confirms persistence is removed before recovery starts in each zone.

## 7. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 5 and 6. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors. **A dispatch outage can be material even if no data is taken.**

| Step | What happens | Who | Done when |
|---|---|---|---|
| 7.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 7.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 7.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 7.4 | Committee reviews the materiality worksheet (below) with facts from sections 3 to 6 | Committee | Worksheet completed |
| 7.5 | **Materiality determination** made and recorded with the date and time, and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 7.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 7.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay. The company may ask, through outside counsel to the Department of Justice, if disclosure would pose a substantial public safety risk (for example, by revealing an unremediated weakness in dispatch systems); it cannot decide this itself | General Counsel | Filing confirmation |
| 7.8 | Align timing and content of county, patient, client, media, and investor communications with the filing; brief the audit committee and the board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 7.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost or deferred revenue from P05 values; county late-response penalties; recovery, overtime, mutual aid, and forensic costs; ransom demand; notification and legal costs; insurance coverage and retention; effect on liquidity and covenants |
| Operational | Counties and centers in manual dispatch and for how long; interfacility trips deferred; SL-1 and SL-2 services affected |
| Public safety | Delayed responses linked to the incident; Chief Medical Officer's review of delayed calls |
| Contract | County agreement default or termination rights; state Medicaid broker contract remedies; SL-1 client service credits |
| Data | Number of patients, members, and states; data types (PHI, call recordings, Medicaid IDs); whether data was published |
| Legal and regulatory | Expected OCR, state EMS regulator, or attorney general inquiries; litigation exposure |
| Reputation and strategy | Media coverage; county procurement processes; effect on acquisitions |

**Worked example of the clocks (fictional dates):** ransomware encrypts consoles at RCC-1 and RCC-2 at 03:40 on Monday 2027-02-01; manual dispatch starts at 03:42 and RCC-3 takes part of the load by 05:15 (Track A). The SOC sees CAD database export activity the same morning, so discovery for HIPAA purposes is 2027-02-01. The committee convenes Tuesday 2027-02-02 and determines on Wednesday 2027-02-03 at 17:00 that the incident is material because 11 counties ran on manual dispatch for more than 30 hours and county penalties and contract risk are significant. The Form 8-K is due by Tuesday 2027-02-09 (4 business days: February 4, 5, 8, and 9). Forensics confirms on Friday 2027-02-12 that call recordings and CAD records were taken; Florida's 30-day clocks (individuals and the Department of Legal Affairs) run from that determination to 2027-03-14. The HIPAA 60-day outer limit runs from discovery to 2027-04-02, so the Florida date comes first and sets the plan. Counsel must also decide whether a "reason to believe a breach occurred" arose earlier (for example, on 2027-02-01 when the export activity was seen), which would move the Florida dates forward.

## 8. Notification workflow: counties, clients, and multi-state breach (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each legal obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 8.1 | **Counties first:** every affected PSAP was told at A2; written notice to each county contract manager per its agreement (standard term: verbal within 1 hour, written within 24 hours) | Vice President, Government Relations and County Contracts | County notice log |
| 8.2 | Four-factor breach risk assessment (45 CFR 164.402): nature and extent of PHI, who received it, whether it was actually acquired or viewed, and mitigation. Ransomware with exfiltration is treated as a breach unless the assessment shows a low probability of compromise | Chief Privacy Officer | Signed assessment |
| 8.3 | Build the affected population from forensic results: each individual, data elements, and **state of residence** (from the incident address or billing address). Separate three groups: (a) the company's own patients and callers; (b) SL-1 agencies' patients (the company is their business associate); (c) SL-2 members (the company is the Medicaid programs' and plans' business associate) | Chief Privacy Officer; data team | Affected-individual file with state counts |
| 8.4 | **Business associate duties:** notify each affected SL-1 agency and SL-2 program or plan within the BAA term, and no later than 60 days after discovery (164.410), with the identity of each individual. Clients decide their own notices unless they delegate to the company | Vice President, EMS Billing Services; President, Managed Transportation | Client notices sent |
| 8.5 | Apply HIPAA for the company's own patients: individual notices within 60 days of discovery; HHS contemporaneously if 500 or more; media in every state or jurisdiction with more than 500 affected residents; substitute notice where contact information is missing (common for 911 callers) | Chief Privacy Officer | HIPAA notice plan |
| 8.6 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, content rules, and whether HIPAA-compliant notice satisfies the state law. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 8.7 | **Florida worked example:** individual notice within 30 days of determining the breach; Department of Legal Affairs notice within 30 days if 500 or more Floridians (only the individual notice may get 15 more days on written good cause); consumer reporting agencies if more than 1,000 are notified at once; HIPAA notice is deemed compliant if a copy is timely provided to the Department | General Counsel | Florida filings |
| 8.8 | **Plan to the shortest clock** across HIPAA, every state, the SEC, and the contracts. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 8.9 | Honor any law enforcement delay request under 164.412 and the matching state provisions; document it | General Counsel | Delay record |
| 8.10 | Engage the mail vendor, call center (toll-free number for 90 days if substitute notice is used), and credit monitoring provider | Chief Privacy Officer | Vendors active |
| 8.11 | Track inbound vendor notices (164.410; state third-party agent laws such as Fla. Stat. 501.171(6)) if the incident started at a vendor | Director of Third-Party Risk Management | Vendor notices logged |

**CIRCIA is not yet in force.** If the final rule is published and matches the proposal, this incident would also need a CISA report within 72 hours and a ransom payment report within 24 hours. A voluntary report to CISA or the FBI is made on day 0 to 2 in any case.

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.7). Manual dispatch, center failover, and county mutual aid must be sustained while the decision is made. Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove notification or disclosure duties.

## 9. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first. Items 1 to 4 are already running from Track A:
1. Manual dispatch and county radio
2. Telephony and call routing (forwarded if needed)
3. Identity platform and break-glass access
4. Network core, SD-WAN, and communications center connectivity
5. Security tooling (EDR console, SIEM) for validation
6. Enterprise CAD in the standby region from a clean image, database restored to a point before the compromise; the Medical Director for Communications approves response plans; then CAD-to-CAD links one county at a time, testing each with the PSAP
7. Clean consoles (offline spares first), then vehicle routers, MDCs, and AVL
8. AQ-01 legacy CAD (if affected) or the RCC-4 manual mode
9. 12-lead ECG relay, ePCR sync, and back-entry of paper patient care records within 48 hours
10. Managed transportation platform and SL-1 billing services (tell clients the restoration status)
11. Revenue cycle, ERP, payroll, and reporting

**Validate before leaving manual mode:** EDR shows clean hosts, credentials are rotated, systems are patched, logs reach the SIEM, and a test incident runs end to end (entry, unit recommendation, MDC, CAD-to-CAD). **The dispatch supervisor, not IT, decides when each center switches back**, and announces it on the radio and to each county PSAP (RC.CO). Reconcile the paper incident cards into CAD so response-time reports, county reports, and state data are complete.

## 10. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.10), including the affected county PSAPs.
- The Chief Medical Officer reviews every call handled in manual mode for delays that affected patients.
- Update the risk register (P01: R-001, R-002, R-003, R-005, R-017), the POA&M (P07), the BIA's MTD assumptions, this runbook, and the materiality playbook.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including the materiality determination minutes and breach assessments, for at least 6 years (POL-01 4.11).
