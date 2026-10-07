# Incident Response Runbook: Cyber Attack on a Plant Business Network with Attempted Pivot Toward CDAs

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded nuclear generation company; four stations, seven units; FL, GA, SC, AL) |
| Tier / Vertical | Enterprise / Nuclear Reactors, Materials, and Waste |
| Incident type | Ransomware and data theft on a station's plant business network during a refueling outage, with an attempted pivot toward critical digital assets (CDAs). Includes the 10 CFR 73.77 decision points, the SEC materiality assessment and Form 8-K Item 1.05 step, and multi-state breach notification for contractor personal data |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; STD-03.2 Regulatory Notification Standard |
| Relationship to the CSP | This runbook covers the business side. Anything on the CDA side is handled by the station's cyber security incident response procedures under its NRC-approved cyber security plan (CSP), led by the Site Cyber Security Program Manager. This runbook hands off to those procedures and never directs actions on CDAs |
| Runbook owner | Director, Security Operations, with the General Counsel for sections 6 and 7 and the Director, Nuclear Cyber Security for section 5 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise technical tabletop 2026-04-22 (SOC, Station 2 cyber team, WMS team; **the disclosure committee did not take part, and the SOC-to-station notification step was missing**). GDC plan tested 2026-04-14 under CIP-008-6. Next: full tabletop with the disclosure committee on 2026-11-19 using this scenario (POAM-013) |
| Notification matrix | `notification-matrix.csv` (37 obligations: 10 under 10 CFR 73.77; 5 under 50.72 and 73.1200; 4 NERC CIP-008 and DOE-417; 4 SEC; 6 state law, with Florida as the worked example; and 8 others: OFAC, law enforcement, CIRCIA status, insurer, contractor and client contracts, and two FAR clauses) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (business IT) | Director, Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Station decision maker for NRC notifications | Shift manager of the affected station | Site Vice President | Control room (station phone tree in the sealed binder) |
| Station cyber lead (CDA side) | Site Cyber Security Program Manager | Station cyber security team lead | Station cyber pager |
| Fleet nuclear cyber coordination | Director, Nuclear Cyber Security | Site Cyber Security Program Manager at an unaffected station | Direct mobile |
| Crisis management team chair | Chief Nuclear Officer | Senior Vice President, Nuclear Engineering | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Nuclear Officer, Chief Compliance Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Breach and privacy decisions | Chief Compliance Officer | Deputy Chief Compliance Officer | Direct mobile |
| Physical security and access authorization | Director, Nuclear Security | Station security manager | Security operations line |
| NERC CIP (if the GDC is involved) | Director, NERC Compliance | CIP Senior Manager (Vice President, Generation Dispatch and Energy Marketing) | GDC desk |
| Outage | Vice President, Outage Management; station outage manager | Plant Manager | Outage control center |
| Outside counsel, forensics, insurer | Retained firms (engaged through counsel and the insurer panel) | MSSP incident team | Retainer hotline |
| Communications | Vice President, Corporate Communications (coordinates with station public affairs and the NRC public affairs process) | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3; CISA | Station local law enforcement agency (LLEA) liaison | Numbers in the binder. **The SOC calls only after the stations are told (section 3, step 7)** |

**Out-of-band first.** Assume email, chat, and the identity platform may be compromised. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder at each station and at the fleet support center. **Never discuss Safeguards Information (SGI) on these channels**; SGI goes only through the station's secure communications (73.77(c)(3)).

## 1. Preparation checks (Identify / Protect)
- [ ] Immutable backups in separate cloud accounts and DC-2, restore-tested within the last 90 days for tier-1 business systems (CP-9, CP-4)
- [ ] EDR on all business endpoints and servers, **including Station 4 (gap until POAM-004 closes)**
- [ ] SIEM receives logs from every station business network, **except Station 4 (gap until POAM-004 closes)**
- [ ] WMS edge servers at Stations 1 to 3 hold a current read-only copy of the clearance index and surveillance schedule; printed outage schedules and paper clearance forms are staged in each outage control center (P05 BP-06, BP-07)
- [ ] WMS outage-mode recovery tested against the 4-hour RTO (**gap until POAM-010 closes**)
- [ ] Portable media kiosks working at every protected area entry and every warehouse (**Station 3 warehouse gap until POAM-015 closes**)
- [ ] SOC external reporting procedure includes the station notification step (**gap until POAM-013 closes**; until then the SOC manager calls the Director, Nuclear Cyber Security before any external report)
- [ ] Break-glass accounts sealed and tested this quarter (POL-02 4.11)
- [ ] Materiality playbook, 8-K templates, and disclosure committee roster current
- [ ] State breach law matrix from outside counsel updated in the last 12 months
- [ ] Outside counsel, forensics, and insurer contacts confirmed this quarter

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file renames, or encryption on a station business system | EDR, staff report, backup job failures | SOC opens a severity-1 case; isolates hosts through EDR; pages the incident commander **and the Site Cyber Security Program Manager** |
| Malware or suspicious files on maintenance and test equipment, a portable media kiosk, or media bound for the protected area | Kiosk alert, station cyber team | Station cyber team takes the lead under the CSP procedures; SOC supports; shift manager informed at once (73.77 decision in section 3) |
| Attempted connection to a one-way data transfer device, a historian replica, or a boundary device | Network detection, historian replica logs, station cyber team | Treat as an attempted pivot; shift manager informed at once |
| Searches or downloads of CSP references, CDA inventories, network diagrams, or security procedures | DLP, file share audit logs, SIEM | Preserve; shift manager informed (possible 73.77(a)(3)) |
| Plant-themed phishing or calls asking about outage schedules, security, or plant systems | Users (POL-05 4.4), email security | Screen with the station against the shared criteria (POAM-013); possible 73.77(a)(3) |
| Suspicious activity from an outage contractor account, device, or trailer | Identity platform, network detection, contractor segment logs | Disable the account; isolate the device; tell the access authorization program (possible 73.77(a)(2)(ii)) |
| Extortion message or leak-site post naming the company | Email, threat intelligence, law enforcement, media | Declare; preserve; do not engage without counsel |

**Declare a severity-1 incident when** encryption or a ransom note is confirmed on any production business system, an extortion claim names company data, or any activity reaches toward the CDA boundary.

**Record four times, separately:**
1. **Discovery of the cyberattack at the station** (NRC 73.77 clocks of 1, 4, and 8 hours). The shift manager records it in the control room log.
2. **Any notification to another agency** (FBI, CISA, state, or local). This can start the 73.77(a)(2)(iii) 4-hour clock.
3. **Determination of the breach or reason to believe a breach occurred** (state breach clocks; Florida 30 days).
4. **Materiality determination** (SEC 4-business-day clock), recorded later by the disclosure committee (section 6).

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Isolate affected business hosts through EDR; do not power them off (preserve memory). Do nothing on the CDA side | SOC | Hosts network-contained |
| 2. Tell the shift manager and the Site Cyber Security Program Manager of the affected station, and the Director, Nuclear Cyber Security | Incident commander | Logged in the SOC case and the control room log |
| 3. Station cyber team checks the CDA boundary under the CSP: one-way devices passing outward only, kiosks, maintenance and test equipment, recent portable media transfers. The shift manager decides whether plant procedures need to be entered | Site Cyber Security Program Manager; shift manager | Boundary status reported to the bridge |
| 4. Revoke sessions and rotate credentials for privileged, service, and contractor accounts involved; use break-glass accounts if SSO is affected | Identity team | Revocations logged |
| 5. Confirm backups are untouched (immutability locks, no recent deletions) | Cloud Platform Engineering | Backup integrity confirmed |
| 6. If the WMS or edge server is affected during an outage: the outage manager switches to printed schedules and paper clearances with independent verification; surveillance coordinators confirm due dates from the edge copy or printed look-ahead | Station outage manager; Plant Manager | Outage work control on paper |
| 7. **Before any call to the FBI, CISA, or another agency, the SOC tells every affected station** (POL-03 4.2). The shift manager then knows the 73.77(a)(2)(iii) clock will start if no other 73.77 notification applies | Incident commander | Station acknowledgment logged before the call |
| 8. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 9. The Chief Nuclear Officer activates the crisis management team. If emergency plan criteria are met, the shift manager declares under the emergency plan (50.72(a)) | Chief Nuclear Officer; shift manager | Crisis team active |
| 10. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open |

### 3.1 NRC notification decision points (station shift manager)
The shift manager decides, advised by the Site Cyber Security Program Manager and station Licensing. The SOC and corporate staff supply facts but never make the NRC call. Each decision is recorded with its time and basis.

| # | Question | If yes | Clock |
|---|---|---|---|
| D1 | Did a cyberattack adversely impact safety-related or important-to-safety, security, or emergency preparedness functions (including offsite communications), or compromise support systems with such an impact, within the scope of 73.54? | ENS notification under 73.77(a)(1); the NRC may ask for an open line (73.77(c)(4)) | 1 hour after discovery |
| D2 | Could the attack have caused such an impact (for example, malware on maintenance and test equipment or portable media bound for CDAs, or an attempt against a boundary device)? | ENS notification under 73.77(a)(2)(i) | 4 hours after discovery |
| D3 | Was it initiated, or is it suspected to be initiated, by someone with physical or electronic access to 73.54-scope systems (for example, an outage contractor with unescorted access)? | ENS notification under 73.77(a)(2)(ii); access authorization program reviews the individual | 4 hours after discovery |
| D4 | Has the company told a local, State, or other Federal agency about an event related to the cyber program for 73.54-scope systems, and no other 73.77(a) notification applies? | ENS notification under 73.77(a)(2)(iii) | 4 hours after the other agency was told |
| D5 | Is there information that may show intelligence gathering or pre-operational planning (for example, searches for CDA inventories or network diagrams)? | ENS notification under 73.77(a)(3) | 8 hours after the information was received or collected |
| D6 | Are emergency assessment, offsite response, or offsite communications capabilities majorly lost? | 50.72(b)(3)(xiii), indicating the 73.77 criteria (73.77(c)(7)) | 8 hours |
| D7 | Are security systems affected without timely compensatory measures, or is law enforcement responding on site in a way likely to draw media inquiries? | 73.1200(g)(1)(i) or (e)(3)(i) | 8 hours or 4 hours after discovery |
| D8 | Any cyber program weakness found, or any notification made? | Corrective action program entries under 73.77(b)(1) and (b)(2) | 24 hours |

**Notes for the shift manager:**
- A business-network-only event that never reached toward 73.54-scope systems may need no 73.77(a) call. Record the basis. It still needs CAP entries for any program weakness found.
- If the notification would include SGI, call the commercial number, ask for a secure line, and if none is available, report without SGI and say so (73.77(c)(3)).
- A call that turns out not to meet a threshold is retracted by telephone with the basis (73.77(c)(5)).
- Written follow-up reports are due within 60 days on NRC Form 366 after (a)(1), (a)(2)(i), or (a)(2)(ii) calls; none is required after (a)(2)(iii) or (a)(3) calls (73.77(d)).
- **NRC event notification reports are public.** Tell Corporate Communications, Investor Relations, and the General Counsel as soon as any ENS call is made, because the report can become public before the company has made a materiality determination.
- **Pending rule:** the NRC proposed rule of 2026-06-26 (91 FR 38928) would fold 73.77 into the 50.72 and 73.1200 processes. It is not final. Use the current 73.77 criteria until a final rule takes effect (P03 section 6).

## 4. Analysis (RS.AN)
1. **Scope:** hosts, accounts, file shares, cloud accounts, and stations affected. Use EDR, SIEM, network detection, PAM records, cloud audit logs, and contractor segment logs. For Station 4, collect logs locally because they are not in the SIEM (POAM-004).
2. **Initial access:** phishing of an outage contractor, a contractor laptop on the contractor segment, a vendor remote path, a stolen credential, or an edge device exploit. Check the Station 4 vendor VPN while POAM-009 is open, and any device with its own cellular link (POAM-018).
3. **Boundary:** with the station cyber team, establish whether the attacker touched anything that crosses toward CDAs: portable media staging, maintenance and test equipment, historian replicas, one-way device management interfaces. The station cyber team owns the CDA-side analysis and its records.
4. **Evidence:** forensics images hosts and exports logs before they roll over; chain of custody is kept in the evidence register; hashes recorded for each artifact. Evidence that contains SGI or security-related information stays in the station program.
5. **Exfiltration:** determine what data left, from which systems, and for whom: outage contractor rosters, employee data, access authorization data (73.56(m)), export-controlled work packages (Part 810), security-related information. **This drives sections 3.1 (D5) and 7.**
6. **Integrity:** for the WMS, confirm that no clearance record or surveillance date was changed (compare to the edge server copy, backups, and the WMS audit trail). If integrity cannot be confirmed, the Plant Manager orders a field re-verification of active clearances and a manual check of surveillance due dates before work resumes.
7. **Business impact:** Finance and the BIA owners estimate impact using P05 values: about $3.2 million per day of refueling outage extension (BP-07), about $2.3 million per day for a unit offline, and up to $15.8 million per day in a fleet-wide worst case (BP-01). These estimates feed section 6.

## 5. Containment and eradication (RS.MI)
1. Contain by segment: isolate affected accounts, file servers, the outage trailer and contractor segments, or the whole station business network from DC-1 if needed. The one-way devices need no action; they cannot pass traffic inward.
2. Disable compromised accounts; reset privileged credentials and service account secrets; rotate WMS integration keys.
3. **Freeze transfers toward CDAs.** The station suspends non-essential portable media and maintenance and test equipment transfers into the protected area until the station cyber team clears them under the CSP. Any equipment that was on the business network during the attack is quarantined and examined before use with CDAs.
4. Rebuild from known-good images; never decrypt and reuse encrypted hosts.
5. Patch or close the initial access path before reconnecting.
6. Forensics confirms persistence is removed before recovery starts in each zone.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 3 to 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery (Instruction 1 to Item 1.05), from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4), and at once if an ENS call has been made | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 3 to 5, including any NRC notifications and whether the NRC event notification report is already public | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date and time and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations (Item 1.05(a)). Do not include technical details that would impede response or remediation (Instruction 4), and never include SGI or security-related information | General Counsel; CFO; outside securities counsel; Director, Nuclear Cyber Security reviews for security-related content | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (substantial risk to national security or public safety) allows delay (Item 1.05(c)); any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | If any required information was not determined or was unavailable, say so in the filing and file an 8-K/A within 4 business days after it is determined or becomes available (Instruction 2) | General Counsel | Amendment tracker open |
| 6.9 | Align timing and content of contractor, employee, client, media, and investor communications with the filing and with the public NRC event report; brief the audit committee, the board risk committee, and the nuclear safety oversight committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.10 | Keep reassessing as facts change. Carry lessons into the next Item 106 disclosure (17 CFR 229.106) | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Outage extension days at about $3.2 million each; lost generation if a unit is taken offline (about $2.3 million per unit-day); replacement power to meet PPA delivery; recovery and forensic costs; notification and credit monitoring costs; insurance coverage and retention; effect on liquidity and covenants |
| Operational | Business systems down and for how long; WMS on paper; stations affected; whether any unit's power was reduced |
| Nuclear safety and regulatory | Any 73.77, 50.72, or 73.1200 notification; whether any CDA or plant function was affected; expected NRC inspection or enforcement; NERC implications if the GDC is involved |
| Data | Number of people and states; data types (Social Security numbers, access authorization data, export-controlled technology, security-related information); whether data was published |
| Legal | State attorney general inquiries; litigation exposure; contract claims from outage contractors, PPA counterparties, and SL-1 and SL-2 clients |
| Reputation and strategy | National media attention to an attack on a nuclear company; public NRC event reports; analyst and rating agency reaction; effect on license renewal, acquisitions, or service line sales |

**Worked example of the clocks (fictional dates).** Station 2 is 12 days into a planned refueling outage of Unit 2.
- **Tuesday 2027-03-09, 04:20:** the SOC declares severity 1 after ransomware encrypts Station 2 business file servers and the WMS edge server. Initial access was a phished outage contractor account.
- **04:50:** checking the boundary (section 3, step 3), the station cyber team finds malware on a maintenance and test equipment laptop that had been connected to the business network for updates. The laptop is used with CDAs under the CSP. The shift manager records **04:50 as the discovery time** for D2.
- **08:50:** ENS call under **73.77(a)(2)(i)** (due by 08:50, 4 hours after discovery). The laptop never connected to a CDA during the attack, so D1 is "no."
- **10:00:** forensics shows the attacker searched file shares for "CDA inventory" and "network diagram." The 11:20 follow-up ENS call reports this under **73.77(a)(3)** (due by 18:00).
- **11:45:** after telling Station 2, the SOC reports to the FBI and CISA. Because 73.77(a) notifications were already made for this event, D4 does not require a separate (a)(2)(iii) call; the shift manager records that basis and gives the NRC the update.
- **By 2027-03-10, 04:50:** CAP entries for the notifications and the weaknesses found (73.77(b)).
- **Wednesday 2027-03-10:** the disclosure committee convenes. The NRC event notification report for Station 2 is now public. An extortion message claims theft of contractor data.
- **Friday 2027-03-12, 16:00:** forensics confirms the outage contractor roster (1,350 people in 23 states, including 230 Florida residents, with Social Security numbers) was taken. The committee determines the incident is **material**: the outage is now expected to run 6 days late (about $19 million), and the public NRC report and media attention make it qualitatively significant. **The Form 8-K is due by Thursday 2027-03-18** (4 business days: March 15, 16, 17, and 18).
- **Florida:** individual notice is due no later than 30 days after the 2027-03-12 determination, which is Sunday 2027-04-11; the plan sends notices by Friday 2027-04-09. 230 Floridians is below the 500 threshold, so no Department of Legal Affairs notice, and below 1,000, so no Florida consumer reporting agency notice. Counsel must also decide whether "reason to believe a breach occurred" arose on 2027-03-10, when the extortion message claimed data theft, which would move the Florida date to 2027-04-09 at the latest.
- **NRC written follow-up report** for the 73.77(a)(2)(i) call: due within 60 days, by 2027-05-08. None is required for the (a)(3) call.

## 7. Multi-state breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out. HIPAA does not apply (P03 G-114).

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Breach determination for personal information: what data elements, whose, whether acquired, and the risk of harm | Chief Compliance Officer | Signed determination with date (starts state clocks) |
| 7.2 | Build the affected population from forensic results: each individual, data elements, and **state of residence**. Separate groups: (a) employees; (b) outage contractor workers (data held by the company); (c) access authorization and fitness-for-duty data (73.56(m) and 26.37); (d) SL-2 client workers' dose records, if the dosimetry systems were involved | Chief Compliance Officer; data team | Affected-individual file with state counts |
| 7.3 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, content rules, and any law enforcement delay. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 7.4 | **Florida worked example:** individual notice within 30 days of the determination or reason to believe (501.171(4)(a)), with up to 15 more days only on written good cause to the Department (501.171(3)(a)); Department of Legal Affairs notice within 30 days if 500 or more Floridians (no extension for this notice); consumer reporting agencies if more than 1,000 are notified at one time (501.171(5)); notice content under 501.171(4)(e) | General Counsel | Florida filings |
| 7.5 | **Plan to the shortest clock** across every state and the SEC filing. Publish one master calendar | Chief Compliance Officer | Master calendar |
| 7.6 | Honor any written law enforcement delay request (Florida: 501.171(4)(b)) and the matching rules of other states; document it | General Counsel | Delay record |
| 7.7 | Engage the mail vendor, call center, and credit monitoring provider | Chief Compliance Officer | Vendors active |
| 7.8 | Notify the outage contractor companies whose workers were affected (contract terms, within 24 hours of confirmation) and coordinate their own employee communications | Vice President, Outage Management | Contractor notices logged |
| 7.9 | If access authorization or fitness-for-duty information was taken: the Director, Nuclear Security records it in the CAP, reviews the 73.56(m) and 26.37 controls, and considers whether the shared industry personnel access database operator must be told | Director, Nuclear Security | CAP entry; review record |
| 7.10 | If export-controlled reactor technology was taken: the Export Compliance Officer assesses whether an unauthorized transfer occurred under Part 810 and advises on any report to DOE | Export Compliance Officer | Export control assessment |
| 7.11 | Track inbound vendor notices (Fla. Stat. 501.171(6)(a) and other states' third-party rules) if the incident started at a vendor | Director of Third-Party Risk Management | Vendor notices logged |

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.6). Report to the FBI or CISA after the stations are told; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove any NRC, SEC, or state notification duty.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first. CDA-supported plant functions, physical security systems, and emergency preparedness systems (priorities 1 to 3) are restored under the station procedures and the CSP, not by this runbook.
1. Identity platform and break-glass access
2. Network core, station business networks, DNS
3. Security tooling (EDR console, SIEM) for clean-room validation
4. Radiation protection business systems (electronic dosimetry servers, permits)
5. WMS and edge servers. Before releasing work: reconcile WMS clearance and surveillance records with the paper records kept during the outage, and the Plant Manager confirms active clearances in the field
6. Access authorization and badging systems (outage badging resumes)
7. Energy scheduling and settlement platform (if affected)
8. EDMS and engineering systems
9. M&D platform and dosimetry systems (tell SL-1 and SL-2 clients the restoration status)
10. ERP, payroll, and supply chain
11. Financial close and fuel management systems

**Validate before reconnecting:** EDR clean, credentials rotated, patched, logging to the SIEM. **Before any equipment returns to use with CDAs,** the station cyber team clears it under the CSP. Keep paper work control until the WMS meets its RTO and the reconciliation is complete. Tell employees, contractors, and clients when services return (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.10).
- CAP entries closed out; NRC written follow-up reports filed on time; retractions made where a threshold was not met.
- Update the risk register (P01: R-001, R-002, R-013, R-014, R-055), the POA&M (P07), this runbook, and the materiality playbook.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain records: CSP-related records until license termination (73.54(h)); NRC written follow-up reports for 3 years from the report date or until the license is terminated, whichever comes first (73.77(d)(12)); Florida no-harm determinations for 5 years (501.171(4)(c)); all other incident records at least 6 years (POL-01 4.11).
