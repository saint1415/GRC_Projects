# Incident Response Runbook: Ransomware Halting Processing Lines and Cold-Chain Monitoring

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded further processor of meat products: 8 plants, 4 distribution centers; FL, GA, AL, NC, TN, TX) |
| Tier / Vertical | Enterprise / Food and Agriculture |
| Incident type | Ransomware that starts on the corporate network (or at PLT-08), reaches plant OT and the central MES, stops processing lines at several plants, and cuts cold-chain monitoring, with possible theft of employee and customer data. Includes the **SEC materiality assessment and Form 8-K Item 1.05** step, food safety decisions and FSIS and FDA notices, release reporting if refrigeration is affected, and multi-state breach notification |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Product Hold and Regulatory Notification Procedure; PRC-03.4 Multi-State Breach Notification Procedure |
| Runbook owner | Director of Security Operations, with the Director of OT Security (OT), the SVP FSQA (food safety), and the General Counsel (sections 7 and 8) |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Technical OT tabletop 2026-03-19 with PLT-01 and PLT-04 (**the disclosure committee did not take part**). Next: full tabletop with a multi-plant production-halt scenario and the disclosure committee on 2026-11-18 (POAM-014) |
| Notification matrix | `notification-matrix.csv` (27 obligations: FSIS, FDA, EPA and EPCRA release reporting, 4 SEC, 4 generic state, 5 Florida worked example, OFAC, law enforcement, CIRCIA status, MTSA and FAR (not applicable), insurer, and 3 customer contract rows) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| OT lead (safe state, containment, recovery) | Director of OT Security, with the Vice President, Engineering | Plant controls engineers | Plant radios and company phones |
| Food safety lead (product holds, FSIS and FDA notices) | Senior Vice President, Food Safety and Quality Assurance | Plant FSQA managers; PLT-07 FSQA Manager for FDA products | Direct mobile |
| Refrigeration and ammonia safety | Director of Refrigeration and Process Safety | Site refrigeration leads; refrigeration contractors on site | PSM emergency response plans |
| Crisis management team chair | Chief Operating Officer | Plant Managers | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Risk Officer, SVP FSQA, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Personal information decisions | Deputy General Counsel, Privacy | Chief Compliance Officer | Direct mobile |
| Outside breach counsel and OT-capable forensics | Retained firms (engaged through counsel and the insurer panel) | MSSP incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Customers | Vice President, Distribution and Transportation (SL-1); Vice President, Co-Manufacturing and Private Label (SL-2); SVP FSQA (recalls) | Account managers | Customer contact lists in the binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (for investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and the identity platform may be compromised. Use company mobile phones, plant radios, the out-of-band conferencing service, and the printed incident binders in each plant's FSQA office, engine room, and shipping office.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binders at every plant and DC: this runbook, contacts, the notification matrix, manual CCP forms, the manual temperature log, and signed formulation masters
- [ ] Controlled printed copy of the PLT-07 food defense plan and food safety plan onsite (21 CFR 121.315(c); 117.315(c))
- [ ] Immutable cloud backups and plant OT offline copies restore-tested within the last 90 days for tier-1 systems (CP-9, CP-4). **Gap: plant restores proven at 4 of 8 plants; PLT-08 has no offline copy (POAM-010, POAM-001)**
- [ ] OT DMZ in place at every plant (SC-7). **Gap at PLT-05 and PLT-08 (POAM-001, POAM-003)**
- [ ] OT monitoring with alerts on PLC downloads and recipe releases (SI-4). **Gap at PLT-08 and the PLT-05 engine room (POAM-011)**
- [ ] Manual cold storage temperature log exercised at every site. **Gap: 3 of 12 sites (POAM-008)**
- [ ] Break-glass accounts sealed and tested this quarter (POL-02)
- [ ] Materiality playbook with a product loss and recall cost method, and a current committee roster. **Gap until POAM-014 closes**
- [ ] FSIS District Office contacts for each plant and FDA Reportable Food Registry portal access holders at PLT-07 current
- [ ] LEPC and SERC contacts in each site's emergency response plan current
- [ ] Outside counsel, OT-capable forensics, and insurer contacts confirmed this quarter; state breach law matrix from outside counsel updated in the last 12 months

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note or mass file encryption on an office PC, SCADA server, historian, MES edge server, or the central MES | EDR, staff report, backup job failures | SOC opens a severity-1 case; isolate hosts through EDR where installed; **do not power off** OT servers; page the incident commander and OT lead |
| HMIs show "communication lost," or the MES will not release recipes or print labels | Operators, line supervisors | Supervisor calls the plant controls engineer and the SOC |
| Cold-chain dashboard stops updating at one or more sites, or no alerts arrive during a known excursion | DC and plant shift leads | Start the manual temperature log at once; call the SOC |
| Unapproved setpoint, formulation, or recipe release | Operators, QA, FSQA review, MES release alert | Treat as possible tampering: stop the affected step, call the plant FSQA manager and the SOC (POL-03 4.5) |
| Activity from PLT-08's network or its integrator VPN reaching enterprise systems | Network detection, VPN logs, local IT report | Treat as severity 1 until scoped; cut the PLT-08 site VPN if activity reaches enterprise systems |
| Extortion message or leak-site post naming the company | Email, threat intelligence, law enforcement, media | Declare; preserve; do not engage without counsel |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any production system, when HMIs, SCADA, or the MES lose function with signs of malicious activity at more than one line, or when an extortion claim names company data.

**Record these times separately**, because each one starts a different clock:
1. **Discovery time** of the incident (starts the materiality process and many state clocks).
2. **Product-affecting times** at each plant: last trusted CCP reading, start of manual monitoring, and any unexplained setpoint change (drive product decisions).
3. **Determinations** later in the incident: that product in commerce is adulterated (FSIS 24-hour clock), that a PLT-07 product is a reportable food (FDA 24-hour clock), that a reportable ammonia release occurred (immediate), that the incident is material (SEC 4-business-day clock), and that a breach of personal information occurred (state clocks; Florida 30 days).

## 3. First 4 hours: make the plants safe (RS.MA, RS.MI)
**Order matters.** Protect people, then product in process, then evidence and systems.

| Step | Who | Done when |
|---|---|---|
| 1. At every affected site, confirm refrigeration is running on local controllers and ammonia detection is normal. If a refrigeration controller shows signs of tampering, switch to manual operation under the PSM procedures. If a release is suspected, follow the site emergency response plan and section 6 release reporting | Director of Refrigeration and Process Safety; site refrigeration leads | Engine rooms report stable; no ammonia alarm |
| 2. Start manual temperature logging for every cooler, freezer, dock, and loaded trailer at affected sites, at least hourly | Plant and DC shift leads | First manual log entries recorded |
| 3. Put lines in a safe state: let smokehouse and oven cycles finish on local controllers where the cycle is intact, or abort and hold the product; stop brine injection and cure dosing; close CIP valves manually | Plant Managers with plant controls engineers | Every affected line stopped or finishing a verified cycle |
| 4. **Hold all product** made, cooked, chilled, or stored since the last trusted CCP record, plus anything dosed since the last verified recipe release | Plant FSQA managers | Hold tags on product; hold list started per plant |
| 5. Isolate: disconnect each plant's OT DMZ link to the cloud, stop MES releases centrally, cut the PLT-08 site VPN and integrator VPN, power off the PLT-05 refrigeration modem. Leave affected hosts powered on for memory evidence | OT lead; Network Engineering | Links down; photos of cable positions taken |
| 6. Revoke sessions and rotate credentials for privileged, MES, and service accounts involved; use break-glass accounts if SSO is affected | Identity team | Revocations logged |
| 7. Confirm immutable backups and plant offline copies are untouched | Cloud Platform Engineering; plant controls engineers | Backup integrity confirmed |
| 8. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains OT-capable forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 9. COO activates the crisis management team; plant managers brief the FSIS inspection program personnel on site that electronic CCP monitoring is down and manual monitoring and holds are in place | COO; Plant Managers; plant FSQA managers | Briefing times recorded per plant |
| 10. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** which office hosts, OT servers, HMIs, plants, cloud accounts, and identities are affected? Use EDR, SIEM, OT monitoring, cloud audit logs, PAM and gateway records. For PLT-08 and the PLT-05 engine room, collect logs locally, because they are not in the SIEM.
2. **Initial access:** phishing, stolen credentials, an edge device exploit, a vendor path, or PLT-08. Check the PLT-08 integrator VPN and the PLT-05 modem first while POAM-002 and POAM-003 are open.
3. **Did the attacker touch the process?** With plant controls engineers, compare PLC programs with the OT repository, active HMI setpoints and smokehouse cycles with the released recipes, and every formulation in the central MES with the signed masters. Check CIP valve logic and the dosing skids. **Any unexplained difference is treated as possible intentional adulteration** (POL-03 4.5): stop the affected step, hold product, and at PLT-07 start the food defense corrective action procedure (21 CFR 121.145).
4. **Evidence:** forensics images affected servers and exports logs before they roll over; chain of custody in the evidence register; hashes recorded for each artifact.
5. **Exfiltration:** did the attacker take HR and payroll data, online customer accounts, formulations, SL-2 customer specifications, or the PLT-07 food defense plan? Sources: egress logs, SaaS export logs, file share audit logs, the attacker's claims. **This drives sections 7 and 8**, the food defense reanalysis decision, and SL-2 customer notices.
6. **Business impact:** Finance and the BIA owners estimate daily impact with P05 values: about $18.8 million of production per day if all plants stop (BP-04), about $9.5 million of product at risk per day if cold storage monitoring fails across sites (BP-01), and about $15 million of shipments held per day if pre-shipment review stops (BP-06). These feed section 7.

## 5. Containment and eradication (RS.MI)
1. Contain by zone: isolate affected plants, cloud accounts, and identities. Keep unaffected plants running on their edge recipe caches (72 hours) only if the central MES is confirmed clean or disconnected.
2. Disable compromised accounts; reset all privileged credentials, MES and service account secrets, gateway vendor accounts, and API keys between the MES, ERP, WMS, and cloud.
3. Rebuild affected Windows hosts (office endpoints, SCADA, historians, MES edge servers, engineering workstations) from known-good images; **never decrypt and reuse** encrypted hosts.
4. Reload PLC programs from the OT repository if any comparison in section 4 step 3 failed or could not be completed.
5. Keep the PLT-08 integrator VPN and the PLT-05 modem disconnected; vendors work on site under escort until the OT gateway is live there.
6. Forensics confirms persistence is removed before recovery starts in each zone.

## 6. Food safety decisions and regulatory notices (RS.CO)
**Food safety decisions come first, and they belong to FSQA.** Follow `notification-matrix.csv`.

**Product on hold.** For each held lot, the plant FSQA manager documents the review required for unforeseen deviations (9 CFR 417.3(b)): segregate and hold, determine acceptability using manual records, chart recorders, and product testing where needed, dispose of anything that cannot be shown safe, and reassess the HACCP plan. Product may not ship until its records are complete (9 CFR 417.5(c)). The decision is recorded in the incident case before the case can close (POL-03 4.4).

| When | Action | Owner |
|---|---|---|
| Hour 0-24 | Decide whether any **already-shipped** meat product may be adulterated or misbranded (for example, shipped after monitoring stopped or after an unexplained setpoint change). If so, notify the FSIS District Office for that plant **within 24 hours** of that determination (9 CFR 418.2) and start the recall procedure (9 CFR 418.3) | SVP FSQA with plant FSQA managers |
| Hour 0-24 | Same question for shipped **PLT-07 FDA-regulated products**. If one is a reportable food, report to FDA's Reportable Food Registry **within 24 hours** of the determination (21 U.S.C. 350f(d)), unless the 350f(d)(2) conditions apply | PLT-07 FSQA Manager |
| Immediately on knowledge | If an ammonia release of 100 lb or more in 24 hours occurred, notify the National Response Center (40 CFR 302.6(a)) and the LEPC and SERC (40 CFR 355.40, 355.42), then send the written follow-up | Director of Refrigeration and Process Safety |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA; supports OFAC mitigation if payment is considered | CISO |
| Day 0-2 | Customer notices under SL-1, SL-2, and supply agreements (delivery impact, temperature record gaps, any recall) | Customer owners in section 0 |
| After containment | PLT-07: food defense corrective action record and reanalysis decision if tampering was found or cannot be ruled out (21 CFR 121.145; 121.157(b)(3)). Other plants: functional food defense plan review | PLT-07 FSQA Manager; SVP FSQA |

**Plan to the shortest clock.** The FSIS and FDA 24-hour clocks start at *determination*, not discovery, but the determination must be made with reasonable speed. Do not delay the product question while IT recovery continues.

**CIRCIA:** not in effect. As proposed, the company would be covered by the size criterion; recheck when the final rule is published (P03 section 6).

## 7. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 to 6. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 7.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.6) | CISO | Brief logged |
| 7.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 7.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 7.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 to 6, including the SVP FSQA's product hold and recall picture | Committee | Worksheet completed |
| 7.5 | **Materiality determination** made and recorded with the date, time, and reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer (for example, a recall decision or an outage passing 3 days) | Committee (General Counsel records) | Determination minute signed |
| 7.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 7.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 7.8 | Align timing and content of customer, employee, media, and investor communications with the filing; brief the audit committee and board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 7.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost production from P05 (about $18.8 million per day if all plants stop); product held, destroyed, or recalled (P05 BP-01 and BP-06 values, plus recall costs: retrieval, destruction, customer credits); customer chargebacks and lost shelf space; recovery and forensic costs; ransom demand; notification and credit monitoring costs; insurance coverage and retention |
| Operational | Plants, lines, and DCs down and for how long; cold storage at risk; SL-1 and SL-2 customer impact |
| Food safety | Product in commerce that may be adulterated; recalls and public health alerts; any illness reports |
| Data | Number of employees and customers affected and their states; data types (Social Security numbers, bank data, formulations, SL-2 customer specifications) |
| Legal and regulatory | Expected FSIS, FDA, EPA, or state inquiries; litigation exposure; customer contract breaches |
| Reputation and strategy | Media coverage; loss of a national customer; effect on the PLT-08 integration or future acquisitions |

**Worked example of the clocks (fictional dates):** ransomware is discovered Tuesday 2027-02-02 at 08:10 at PLT-02 and PLT-05; the central MES stops releases and 5 plants halt. On Wednesday 2027-02-03 at 11:00 the SVP FSQA determines that 3 lots of smoked sausage shipped from PLT-02 overnight lack lethality records and cannot be shown safe, so the FSIS District Office must be notified by Thursday 2027-02-04 at 11:00. The disclosure committee convenes Wednesday 2027-02-03 and determines materiality on Thursday 2027-02-04 at 16:00 (multi-day multi-plant halt plus a recall). The Form 8-K is due by Wednesday 2027-02-10 (4 business days: February 5, 8, 9, and 10). Forensics confirms on Friday 2027-02-19 that HR files for about 12,000 employees were taken; Florida's 30-day clocks (individuals, and the Department of Legal Affairs because more than 500 Floridians are affected) run from that determination to 2027-03-21, and every other affected employee's state law applies too. Counsel must also decide whether a "reason to believe a breach occurred" arose earlier (for example, when the extortion message claimed data theft), which would move the Florida dates forward.

## 8. Multi-state breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 8.1 | Decide whether personal information was accessed or acquired (employee data in ERP, payroll, and HR files; online customer accounts) | Deputy General Counsel, Privacy | Breach determination record |
| 8.2 | Build the affected population from forensic results: each individual, data elements, and **state of residence** (employees from HR records; customers from shipping addresses) | Deputy General Counsel, Privacy; data team | Affected-individual file with state counts |
| 8.3 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, and content rules. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 8.4 | **Florida worked example:** individual notice within 30 days of determining the breach (a 15-day extension is available for individual notice only, on good cause given in writing to the Department within 30 days); Department of Legal Affairs notice within 30 days if 500 or more Floridians; consumer reporting agencies if more than 1,000 are notified at one time | General Counsel | Florida filings |
| 8.5 | **Plan to the shortest clock** across every state, the SEC filing, and customer contracts. Publish one master calendar | Deputy General Counsel, Privacy | Master calendar |
| 8.6 | Honor any law enforcement delay request under the matching state provisions; document it | General Counsel | Delay record |
| 8.7 | Engage the mail vendor, call center, and credit monitoring provider | Deputy General Counsel, Privacy | Vendors active |
| 8.8 | Track inbound vendor notices if the incident started at a vendor (state third-party agent laws such as Fla. Stat. 501.171(6)) | Director of Third-Party Risk Management | Vendor notices logged |

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.9). Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not make held product safe or remove any notification or disclosure duty.

## 9. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Refrigeration running and temperatures recorded at every site (manual logs until cold-chain gateways are back on clean networks)
2. Safe state for in-process product; held product evaluated plant by plant
3. Identity platform and break-glass access
4. Network core, SD-WAN, OT DMZ, and security tooling (EDR, SIEM, OT monitoring) for validation
5. Plant SCADA and historians from verified clean backups; historian gaps covered by manual records
6. Central MES restored, then **every formulation compared with the signed master** before any release (POL-03 4.10)
7. Packaging, labeling, and lot coding (manual labels with second-person check until the MES is back)
8. Traceability platform (needed first if a recall is under way)
9. Food safety records platform; enter manual records
10. ERP order management, EDI, WMS, and TMS
11. SL-1 and SL-2 customer portals (tell customers the restoration status)
12. PLT-08 legacy systems
13. Payroll, financial close, online store

**Validate before restart:** each line restarts only after the plant controls engineer confirms PLC programs and setpoints match the approved versions, the plant FSQA manager signs a restart checklist, and the first batch on each line is verified against critical limits. Keep manual procedures until each process meets its RTO. Tell staff, customers, and the FSIS personnel on site when normal monitoring resumes (RC.CO).

## 10. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with plant FSQA managers and controls engineers; written report within 30 days (POL-03 4.12).
- Update the risk register (P01, especially R-001, R-002, R-003, R-004, R-005, R-008, R-010, R-014), the POA&M (P07), this runbook, the materiality playbook, the HACCP plans (reassessment under 9 CFR 417.3(b)(4) where the deviation was unforeseen), and the PLT-07 food defense plan if tampering was found or suspected.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain incident records, materiality minutes, product hold and disposition records, and breach determinations for at least 3 years (POL-01 4.13), and longer where a specific law requires it (for example, 5 years for a Florida no-notice determination).
