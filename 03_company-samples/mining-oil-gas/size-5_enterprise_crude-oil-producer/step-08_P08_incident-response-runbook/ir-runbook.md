# Incident Response Runbook: Ransomware Spreading from Business IT toward Field SCADA

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded independent crude oil producer; Permian, Mid-Continent, and Florida) |
| Tier / Vertical | Enterprise / Mining, Quarrying, and Oil and Gas Extraction |
| Incident type | Ransomware that starts in business IT and spreads toward the OT DMZ and field SCADA, with possible theft of royalty owner and employee data (double extortion). Includes the SEC materiality assessment, release reporting if a loss of containment follows, and a multi-state breach notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); NIST SP 800-82 Rev. 3 for OT response and recovery |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Regulatory Release Reporting Procedure |
| Runbook owner | Director of Security Operations, with the Director of OT Security for sections 3 to 5 and 9, and the General Counsel for sections 6 and 8 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise tabletop 2026-03-19 (IT ransomware; **no OT scenario, and the disclosure committee did not take part**). Next: full tabletop with an OT scenario and the disclosure committee on 2026-11-19 (POAM-012) |
| Notification matrix | `notification-matrix.csv` (30 obligations: 5 SEC disclosure, 9 state breach including 5 Florida worked-example rows, 5 release reporting, 5 government and screening rows, 1 ransom, 5 contractual) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| OT incident lead | Director of OT Security | OT security engineer on call | OT bridge; IOC shift supervisor line |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Field operations lead (manual operations, shut-in) | Chief Operating Officer | Vice Presidents of Permian, Mid-Continent, and Florida Operations | Crisis line; IOC shift supervisor |
| IOC and BCC control | IOC shift supervisor (Production Controller lead) | BCC shift supervisor | Hardwired control room phones; licensed radio |
| Crisis management team chair | Chief Operating Officer | Vice President, Operations Technology and Automation | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Risk Officer, COO, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Breach and privacy decisions | Privacy Counsel (Legal) | Chief Compliance Officer | Direct mobile |
| Release reporting (EPA, PHMSA, state) | Vice President, Health, Safety, and Environment; Pipeline Compliance Manager | Regional HSE managers | HSE on-call line |
| Outside counsel, forensics with OT capability | Retained firms (engaged through counsel and the insurer panel) | MSSP incident team | Retainer hotline |
| SCADA Integrator A; AQ-MC Integrator B | Integrator emergency lines | Vendor account managers | Numbers in the incident binder |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (for investor messages) | Direct mobile |
| Law enforcement and government | FBI field office or IC3; CISA | Sector ISAC | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and the corporate identity platform may be compromised. Use company mobile phones, the out-of-band conferencing service, control room hardwired phones and licensed radio, and the printed incident binder at the IOC, the BCC, the Florida control room, and each field office.

## 1. Preparation checks (Identify / Protect)
- [ ] Immutable backups of cloud and data center workloads in separate accounts, restore-tested within the last 90 days for tier-1 systems (CP-9, CP-4)
- [ ] Offline SCADA images and controller program backups current for the IOC and BCC; **Florida and AQ-MC program backups and restore tests are gaps until POAM-005 closes**
- [ ] IT/OT boundary isolation ("pull the plug") procedure tested at the IOC and BCC; **Florida has no OT DMZ, so isolation there means cutting its single IT/OT firewall (POAM-003)**
- [ ] Regional manual operations procedures, patrol route sheets, and shut-in criteria printed at each field office (P05 BP-01, BP-02)
- [ ] OT identity domain break-glass accounts sealed and tested this quarter (POL-02 4.12)
- [ ] EDR on corporate endpoints and servers (97% coverage); SIEM receives IOC and BCC OT logs; **Florida and AQ-MC logs missing until POAM-011 closes**
- [ ] Materiality playbook, production-loss worksheet, and 8-K templates current; disclosure committee roster current (**worksheet gap until POAM-012 closes**)
- [ ] Manual PHMSA release estimate method available (**gap until POAM-021 closes**)
- [ ] Outside counsel, OT-capable forensics, integrators, and insurer contacts confirmed this quarter
- [ ] State breach law matrix from outside counsel updated in the last 12 months

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renames or encryption on corporate systems | EDR, staff report, backup job failures | SOC opens a severity-1 case; isolate hosts through EDR; page the incident commander and the OT incident lead |
| Activity from an infected IT segment toward the OT DMZ (jump hosts, historian feed, patch staging) | OT DMZ firewall, OT monitoring, PAM | Treat as severity 1; OT incident lead decides on boundary isolation (section 3, step 2) |
| Unusual traffic or logins on SCADA servers, HMIs, or engineering workstations; unexpected logic downloads | Passive OT monitoring (IOC, BCC, Permian), SCADA event logs, Production Controller report | Severity 1; Production Controllers verify field status by radio and patrols |
| Suspicious activity from the AQ-MC network or VPN | VPN logs, enterprise network detection, local IT report | Cut the AQ-MC site-to-site VPN if activity reaches enterprise systems; keep AQ-MC on local control |
| Large or unusual outbound transfer (owner data, cloud storage, file shares) | Egress monitoring, DLP, cloud threat detection | Block destination; preserve logs; start the breach track (section 8) |
| Extortion message or leak-site post naming the company | Email, threat intelligence, law enforcement, media | Declare; preserve; do not engage without counsel |
| Vendor reports an incident affecting company systems or data (Integrator A or B, ESP vendor, payroll, print and mail) | Vendor notice | Open a vendor incident case; cut the vendor's remote access at the gateway |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any production system, attacker activity reaches the OT DMZ or any OT asset, or an extortion claim names company data.

**Record three times, separately:**
1. **Discovery time:** when the incident was first known to the SOC. State breach clocks that run from discovery or determination are tracked from the breach determination in section 8.
2. **Materiality determination time** (SEC): recorded later by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.
3. **Release discovery time** (EPA and PHMSA), if a loss of containment occurs: knowledge of an oil discharge (40 CFR 110.6) and confirmed discovery of a gathering line release (49 CFR 195.52). These clocks are measured in hours, not days (section 7).

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Isolate affected corporate hosts through EDR; do not power them off (preserve memory) | SOC | Hosts network-contained |
| 2. **IT/OT boundary decision.** If there is any sign of attacker activity at the OT DMZ, or the infection spreads faster than the SOC can contain it, isolate the IT/OT boundary at the IOC and BCC (block the historian feed, jump hosts, and patch staging) and cut the Florida IT/OT firewall and the AQ-MC VPN. Production Controllers may do this on the OT incident lead's call without executive approval (POL-03 4.4). SCADA keeps running inside the boundary | OT incident lead; IOC shift supervisor | Boundary isolated; time logged |
| 3. **Field safety check.** Production Controllers confirm by SCADA (if trusted) and by radio that safety shutdowns, tank levels, and gathering line pressures are normal. If SCADA integrity is in doubt, each region moves to manual operations: patrols within 2 hours, local control, and shut-in of sites that cannot be watched (P05 BP-01, BP-02). Safety shutdowns are never bypassed | COO; regional Vice Presidents of Operations | Manual operations running where needed; shut-in list logged |
| 4. **SPCC alarm sites.** For the 31 tank batteries that rely on the SCADA high-level alarm (40 CFR 112.9(c)(4)(iv)), start patrols or pump-down at once if alarm delivery to the IOC cannot be trusted | Vice President, HSE; field superintendents | Patrol or pump-down confirmed for all 31 |
| 5. Block attacker infrastructure; revoke sessions and rotate credentials for privileged and service accounts involved; use OT break-glass accounts if the OT identity domain is affected | SOC; Identity team; OT security | Revocations logged |
| 6. Disable vendor remote access at the gateway; confirm the ESP vendor cloud has no setpoint write path (POAM-002) | Director of OT Security | Vendor paths closed |
| 7. Confirm backup accounts and offline SCADA images are untouched | Cloud Platform Engineering; Vice President, Operations Technology and Automation | Backup integrity confirmed |
| 8. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains OT-capable forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 9. COO activates the crisis management team; purchasers and gas gatherers are told of nomination changes as needed | COO; Vice President, Midstream and Water | Crisis team running |
| 10. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** corporate hosts, cloud accounts, identities, OT DMZ hosts, SCADA servers, HMIs, engineering workstations, and controllers affected. Use EDR, SIEM, cloud audit logs, PAM records, and passive OT monitoring. For Florida and AQ-MC, collect logs locally before they roll over (30 days), because they are not in the SIEM.
2. **Initial access:** phishing, stolen credentials, edge device exploit, vendor remote tool, or the AQ-MC network. Check the AQ-MC VPN path and vendor sessions first while POAM-002 and POAM-003 are open.
3. **OT integrity:** compare controller programs and setpoints with the program repository (Permian) or the last known-good backup (other regions); review logic download events since the earliest attacker activity. If integrity cannot be confirmed for a site, it stays on local control or shut in until verified.
4. **Evidence:** forensics images hosts and exports logs; OT evidence is collected read-only and only with the OT incident lead's approval; chain of custody is kept in the evidence register.
5. **Exfiltration:** determine what data left, from which systems, for which owners, partners, and employees. Sources: egress logs, cloud storage access logs, hydrocarbon accounting database activity, file share logs, the attacker's claims and samples. **This drives section 8.**
6. **Business impact:** Production and Revenue Accounting and the BIA owners estimate production deferred and other costs using the production-loss worksheet in section 6. These estimates feed the materiality assessment.
7. **CIRCIA readiness (not a current duty):** the SOC drafts the facts a 72-hour covered cyber incident report would need under the proposed rule, so the company could report quickly if a final rule takes effect. Voluntary reporting to CISA and the FBI happens now (matrix).

## 5. Containment and eradication (RS.MI)
1. Contain by zone: corporate segments, cloud accounts, OT DMZ, each control center, AQ-MC.
2. Disable compromised accounts; reset privileged credentials, OT domain credentials, and service account secrets; rotate API keys for the historian feed, volume integration, and purchaser ticket exchanges.
3. Rebuild corporate and OT DMZ hosts from known-good images; never decrypt and reuse encrypted hosts. Rebuild SCADA servers and HMIs from offline images, then restore configuration from verified backups.
4. Re-verify controller programs against known-good copies before any site returns to remote control.
5. Patch or close the initial access path before reconnecting anything across the IT/OT boundary.
6. Forensics confirms persistence is removed before recovery starts in each zone.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.5) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 3 to 5, including the production-loss estimate | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date and time, and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer (for example shut-ins extending past 48 hours, confirmed owner data theft, or a release) | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation (for example, unpatched OT weaknesses) | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align timing and content of owner, partner, customer, purchaser, media, and investor communications with the filing; brief the audit committee and the board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Production-loss worksheet (company playbook, built from P05):**
| Input | Source | Example values |
|---|---|---|
| Barrels of oil equivalent deferred per day, by operating area | IOC shut-in list; regional Vice Presidents | Permian-wide shut-in: about 74% of production |
| Revenue deferred per day | P05 BP-01 and BP-02 values; current strip prices from Marketing | Permian-wide shut-in: about $9.8 million per day; whole company: about $13.2 million per day |
| Expected days to restore remote control | Section 9 recovery order; demonstrated failover time (9 hours) and RTOs | 4 to 12 hours for the IOC with a clean BCC; days if SCADA must be rebuilt |
| Deferred versus lost production | Reservoir engineering | Most short shut-ins defer rather than lose reserves; water handling outages can force longer shut-ins |
| Other costs | Finance | Patrol overtime and contract crews (about $600,000 per day), forensics and counsel, owner notification and credit monitoring, insurance retention |

**Materiality worksheet (qualitative factors):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Production-loss worksheet; recovery costs; ransom demand; notification and legal costs; insurance coverage and retention; effect on liquidity and credit agreement covenants |
| Operational | Operating areas on manual operations and for how long; shut-in volumes; SL-2 water service disruption; payment run delays |
| Safety and environment | Any release, injury, or near miss linked to the incident; regulator notices made |
| Data | Number of owners, partners, and employees affected; states of residence; data types (taxpayer numbers, bank accounts); whether data was published |
| Legal and regulatory | Expected PHMSA, EPA, state regulator, or attorney general inquiries; litigation exposure; contract breaches with purchasers or SL-2 customers |
| Reputation and strategy | Media coverage; analyst reaction; effect on acquisitions and the AQ-MC integration |

**Worked example of the clocks (fictional dates):** ransomware is discovered on corporate file servers on Tuesday 2027-02-02 at 08:10 and the IT/OT boundary is isolated at 09:30. The Permian moves to manual operations and about 20% of Permian production is shut in by evening. The committee convenes Wednesday 2027-02-03 and determines materiality on Thursday 2027-02-04 at 16:00. The Form 8-K is due by Wednesday 2027-02-10 (4 business days: February 5, 8, 9, and 10). Forensics confirms royalty owner data was taken on Friday 2027-02-19; Florida's 30-day clocks (individuals and the Department of Legal Affairs) run from that determination to Sunday 2027-03-21, so notices are planned for Friday 2027-03-19. Other states' deadlines come from counsel's matrix, and the earliest one sets the plan. Counsel must also decide whether a "reason to believe a breach occurred" arose earlier (for example, when the extortion message claimed data theft on 2027-02-05), which would move the Florida dates forward.

## 7. Release reporting if a loss of containment follows (RS.CO)
A cyber incident that removes visibility or control can lead to a tank overflow or a gathering line release even though safety shutdowns work. Release clocks are short and do not wait for the cyber investigation. Follow PRC-03.4.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Field staff confirm the release and stop it; HSE on-call records the time of knowledge or confirmed discovery | Field superintendent; HSE on-call | Release record opened |
| 7.2 | **Oil discharge that may be harmful** (for example a sheen on water): notify the National Response Center **immediately** (40 CFR 110.6) | Vice President, HSE | NRC report number |
| 7.3 | **Release from one of the 44 regulated rural gathering miles** meeting 195.52(a): call the National Response Center at the earliest practicable moment, **no later than one hour after confirmed discovery**, with an initial estimate of product released. If SCADA and historian data are unavailable, use the manual estimate method (tank gauges, pump run times, line pack); **this method is a gap until POAM-021 closes** | Pipeline Compliance Manager | NRC report number; estimate worksheet |
| 7.4 | Revise or confirm the PHMSA notice within 48 hours (195.52(d)) | Pipeline Compliance Manager | Follow-up record |
| 7.5 | File DOT Form 7000-1 within 30 days for any 195.50 accident on any company crude gathering line (195.54) | Pipeline Compliance Manager | Filed report |
| 7.6 | Make state oil and gas regulator reports per the HSE state reporting matrix | Vice President, HSE | State report numbers |
| 7.7 | Tell the disclosure committee about any release; it is a qualitative materiality factor | Vice President, HSE | Committee briefed |

## 8. Multi-state breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 8.1 | Determine whether a breach of personal information occurred under each affected state's definition (royalty owners: names with taxpayer numbers, bank account numbers; employees: Social Security, driver license and commercial driver license numbers, health plan identifiers, vehicle geolocation) | Privacy Counsel (Legal) | Signed breach determination with date |
| 8.2 | Build the affected population from forensic results: each individual, data elements, and **state of residence** (from owner and HR records). Separate (a) royalty owners, (b) non-operating partners that are individuals, (c) employees and former employees. Records without a state (about 6% of owner records until POAM-023 closes) are traced through the last mailing address | Privacy Counsel; Owner Relations; HR | Affected-individual file with state counts |
| 8.3 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, and content rules. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 8.4 | **Florida worked example:** individual notice within 30 days of determining the breach (15 more days only for individual notice, on written good cause to the department within the 30 days); Department of Legal Affairs notice within 30 days if 500 or more Floridians; consumer reporting agencies if more than 1,000 are notified at once; a no-notice determination only in writing, sent to the department within 30 days and kept 5 years | Privacy Counsel | Florida filings |
| 8.5 | **Plan to the shortest clock** across every state and the SEC filing. Publish one master calendar | Privacy Counsel | Master calendar |
| 8.6 | Honor any written law enforcement delay request under the state laws and document it | General Counsel | Delay record |
| 8.7 | Engage the mail vendor, call center, and credit monitoring provider; prepare owner portal and statement inserts | Director, Owner Relations | Vendors active |
| 8.8 | Notify contractual parties per the matrix: SL-2 customers, partners under joint operating agreements, purchasers, lenders, and the insurer | Contract owners | Contract notices logged |
| 8.9 | Track inbound vendor notices (Fla. Stat. 501.171(6) and other states' third-party agent rules) if the incident started at a vendor | Director of Third-Party Risk Management | Vendor notices logged |

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.9). Report to the FBI and CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove notification, release reporting, or disclosure duties, and a decryptor is never run on OT systems; they are rebuilt.

## 9. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Safety alarm call-out (HSE paging, roving patrols) and the SPCC alarm sites
2. OT identity domain, SCADA break-glass accounts, and OT DMZ jump hosts, rebuilt clean
3. Enterprise SCADA at the IOC or BCC and historians, from verified offline images; controller programs verified before remote control resumes (target 4 hours; 9 hours demonstrated, POAM-004)
4. Field communications (private LTE, radio, cellular)
5. Water handling and disposal facility control; then compressor station control
6. Gathering line and LACT control and ticketing
7. AQ-MC legacy SCADA (untested recovery) and Florida regional SCADA (no standby)
8. Corporate identity platform, EDR console, and SIEM (in parallel with steps 2 to 4)
9. Crude marketing and nominations
10. Field data capture, volume integration, hydrocarbon accounting (prior month payment run as fallback)
11. SL-1 owner and partner portal and SL-2 water services portal (tell owners, partners, and customers the restoration status)
12. ERP, payroll, drilling data, data platform, geoscience

**Validate before reconnecting the IT/OT boundary:** OT DMZ hosts rebuilt, credentials rotated, initial access closed, monitoring restored, and the OT incident lead and the Vice President, Operations Technology and Automation agree in writing. Each region returns from manual to remote operation only after Production Controllers verify field status point by point for its critical sites. Tell staff, owners, partners, customers, and purchasers when services return (RC.CO).

## 10. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- Update the risk register (P01: R-001, R-002, R-005, R-007, R-008), the POA&M (P07), this runbook, the materiality playbook, and the FSPA contingency plan.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including the materiality determination minutes, release reports, and breach determinations, for at least 6 years (POL-01 4.11).
