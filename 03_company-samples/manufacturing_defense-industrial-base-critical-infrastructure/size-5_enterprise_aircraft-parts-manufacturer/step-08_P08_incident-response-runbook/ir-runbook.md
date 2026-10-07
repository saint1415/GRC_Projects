# Incident Response Runbook: Exfiltration of Controlled Unclassified Information (CUI)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded tier-1 aerostructures and aircraft components manufacturer; 8 sites in 6 states) |
| Tier / Vertical | Enterprise / Defense Industrial Base |
| Incident type | Exfiltration of CUI: a state-sponsored actor exploits a zero-day vulnerability in the managed file transfer software used for the CEE's CUI exchange gateway and for the separate corporate instance, and takes CUI (drawings, models, specifications for DoD and prime programs) and employee personal information (payroll files). Includes the DoD 72-hour report, export control decisions, an **SEC materiality assessment and Form 8-K Item 1.05** step, and multi-state breach notification for employees |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure |
| Contract and regulatory basis | DFARS 252.204-7012(c) to (g) and (m)(2); 32 CFR 117.8; 22 CFR 127.12; 15 CFR 764.5; Form 8-K Item 1.05; state breach laws (Florida worked example). Text checked on eCFR (version date 2026-09-23) |
| Runbook owner | Director of Security Operations (incident commander), with the Vice President, Contracts for section 6 and the General Counsel for sections 7 and 9 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | DIBNet reporting drill 2026-04-15 (met targets); materiality tabletop 2026-04-22 (ransomware scenario only). Next: tabletop with this scenario and the disclosure committee on 2026-11-19 (POAM-019) |
| Notification matrix | `notification-matrix.csv` (31 obligations: 8 DFARS, 3 NISPOM, 2 export control, 4 SEC, 3 generic state, 4 Florida worked example, 3 contractual, and 4 others: OFAC, law enforcement, FAR 52.204-25, and CIRCIA status) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO | Chief Information Officer | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Vice President, Manufacturing Operations | Crisis line |
| DoD reporting and prime notices | Vice President, Contracts | Contracts managers (2 certificate holders); Director of Security Operations (certificate holder) | Direct mobile |
| Export control decisions | Vice President, Trade Compliance (Senior Empowered Official) | Outside export counsel | Direct mobile |
| CUI data owner (what was taken) | Vice President, Engineering | PLM Platform Manager | Direct mobile |
| NISPOM reporting | Corporate Facility Security Officer; ISSM | Assistant FSO | Direct mobile |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Risk Officer, Vice President, Contracts, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| Employee notifications | Chief Human Resources Officer | Vice President, Corporate Communications | Direct mobile |
| Outside counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | Cloud provider security team | Retainer hotlines |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read email and chat on any system it reached. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder at FL-1, TX-1, and DC-2.

**Need-to-know.** Incident details include CUI and possibly classified program associations. Keep the bridge to people with a role above; brief cleared staff on Program K matters only through the FSO.

## 1. Preparation checks (Identify / Protect)
- [ ] Four DoD-approved medium assurance certificates current, usable from clean laptops (252.204-7012(c)(3))
- [ ] DIBNet report fields gathered in advance: CAGE codes, contract and subcontract numbers, prime security contacts, facility clearance status, points of contact
- [ ] Gateway staging folders purged within 72 hours (target; 14 days today until R-001 treatment closes)
- [ ] Web application firewall virtual patching rules ready for the gateway; vendor advisory subscription active
- [ ] Logs retained 1 year online and 6 years in archive; write-once settings verified (AU-9, AU-11)
- [ ] Forensic retainer with cloud imaging capability; snapshot procedure for gateway VMs
- [ ] Materiality playbook with a data-theft scenario, content review step, and Attorney General delay path (**gap until POAM-019 closes, 2026-11-30**)
- [ ] Outside counsel's state breach matrix updated in the last 12 months
- [ ] Payroll and benefits files on the corporate instance encrypted at the file level and purged after pickup

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Vendor or government advisory about an actively exploited file transfer vulnerability | Threat intelligence; vendor; DoD or CISA advisory | Treat as severity 1 until scoped: apply virtual patching, block management interfaces, start a compromise hunt on both instances |
| Unusual outbound volume or new download patterns from the gateway | SIEM transfer anomaly use case; egress monitoring | Open a case; snapshot the gateway VMs before any change |
| New web shell, unexpected process, or new admin account on a gateway server | EDR; file integrity monitoring | Isolate the server from the network with EDR (do not power off) |
| Supplier or prime reports receiving unexpected files or a data leak | Supplier notice; prime security contact | Open a case; confirm what data was shared with them |
| Extortion message or leak-site post naming the company or its programs | Email; threat intelligence; law enforcement; media | Declare at once; preserve; do not engage without counsel |

**Declare a CUI exfiltration incident when** any evidence shows unauthorized access to the CUI exchange gateway or its stored files, or CUI appears outside company control. **Do not wait for proof that CUI was taken:** a cyber incident includes any compromise, including possible copying of information to unauthorized media (252.204-7012(a)).

**Record three times, separately:**
1. **Discovery time** (DoD): starts the 72-hour DIBNet clock (252.204-7012(c)).
2. **Materiality determination time** (SEC): recorded later by the disclosure committee (section 7). Starts the 4-business-day Form 8-K clock.
3. **Breach determination time** (states): when the company determines, or has reason to believe, that employee personal information was breached (section 9). Starts the state clocks, such as Florida's 30 days.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Snapshot both gateway instances and capture memory before any change; then isolate them from the internet (prime portals stay available from virtual desktops) | SOC; Director of Cloud Platform Engineering | Hashes recorded; chain of custody started |
| 2. Apply the vendor mitigation or virtual patch; block attacker infrastructure at the web application firewall and egress proxies | SOC; Network Engineering | Blocks confirmed |
| 3. Rotate gateway service accounts, supplier account secrets, and keys used by the gateway; revoke admin sessions | Identity team | Rotations logged |
| 4. Start the 72-hour clock in the incident log; the Vice President, Contracts starts the DIBNet draft | Incident commander; Vice President, Contracts | Discovery time agreed and written down |
| 5. CISO briefs the CEO, COO, and General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 6. COO activates the crisis management team: CUI exchange moves to prime portals and approved exceptions (P05 BP-08); buyers told not to use email workarounds | COO; Vice President, Supply Chain | Instructions issued |
| 7. FSO checks whether any Program K data or cleared staff are involved | Corporate Facility Security Officer | Determination logged |

## 4. Analysis (RS.AN)
1. **Review for compromise** (252.204-7012(c)(1)(i)): which servers, accounts, folders, and files were reached; whether the attacker moved from the gateway into PLM, the suite, or virtual desktops; whether the corporate instance was reached by the same actor.
2. **Exact file list:** from gateway transfer logs, web application firewall logs, and storage access logs, list every file the attacker read or downloaded, with path, time, and destination. The staging folders hold up to 14 days of transfers, which bounds the exposure (P01 R-001).
3. **What the files are:** the Vice President, Engineering maps each CUI file to part number, program, customer (DoD, Prime A to Prime D, or commercial), and distribution statement. The Vice President, Trade Compliance marks each as ITAR, EAR, or not controlled. Human Resources maps each corporate file to the employees in it and their states of residence.
4. **Where the data went:** attacker infrastructure, hosting locations, and any sign of a foreign actor. This feeds the export decision, the law enforcement report, and the materiality assessment.
5. **Malware:** isolate web shells and loaders for DC3 (section 6).
6. **Business impact:** Finance and the BIA owners estimate impact using P05 values (for example, outside processing slows if the gateway stays down past its 12-hour RTO; about $2.2 million per day of expediting and delay). These estimates feed section 7.

## 5. Containment and eradication (RS.MI)
1. Keep both gateway instances isolated until rebuilt from known-good images on patched software. Never clean and reuse a compromised gateway server.
2. Remove attacker persistence (web shells, scheduled tasks, accounts); reset all gateway, supplier, and integration credentials.
3. Purge staging folders after evidence is captured; set the 72-hour purge rule before reopening.
4. Confirm with forensics that no persistence remains in PLM, the suite, or virtual desktops.
5. **Preservation (252.204-7012(e)):** keep images of all known affected systems and all relevant monitoring and packet capture data for **at least 90 days from submission of the DIBNet report**; extend log retention for affected tables. Ask the cloud provider to preserve its own logs.

## 6. DoD reporting and partner notices (RS.CO)
**Follow `notification-matrix.csv`.** Counsel reviews external notices, but the DoD report is never delayed for counsel review.

| When | Action | Owner |
|---|---|---|
| Hour 0 | Discovery time recorded; clock started | Incident commander |
| **Within 72 hours of discovery** | **DIBNet report** from a clean laptop with a medium assurance certificate. Report what is known; mark unknowns; update as analysis continues | Vice President, Contracts |
| As soon as practicable after the report | Give the DoD incident report number to each prime whose CUI was affected (252.204-7012(m)(2)(ii)); notify DoD contracting officers under contract terms | Vice President, Contracts |
| When malware is isolated | Submit to **DC3** as DC3 or the contracting officer instructs; never to the contracting officer (252.204-7012(d)) | Director of Security Operations |
| On request | Give DoD access for forensic analysis; provide damage assessment information if the contracting officer asks (252.204-7012(f), (g)) | Vice President, Contracts |
| Days 1 to 5 | Notify affected suppliers that their uploads were exposed; ask them to check their own systems and report under their flowdowns | Vice President, Supply Chain |
| Days 1 to 5 | Voluntary report to the FBI and CISA | CISO |

## 7. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 to 6. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors. A theft with no outage can still be material.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 7.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 7.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 7.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 7.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 to 6 | Committee | Worksheet completed |
| 7.5 | **Materiality determination** made and recorded with the date and time and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 7.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 7.7 | **Content review (company step):** the Vice President, Trade Compliance, the Vice President, Contracts, and the FSO confirm the draft contains no CUI, export-controlled technical data, or classified information, and that customer program names may be disclosed under the contracts. The review must fit inside the 4-business-day window | Vice President, Trade Compliance; Vice President, Contracts; FSO | Review signed |
| 7.8 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice, with input from the DoD customer where counsel advises | General Counsel | Filing confirmation |
| 7.9 | Align timing and content of prime, supplier, employee, media, and investor communications with the filing; brief the audit committee and the risk and technology committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 7.10 | Keep reassessing as facts change; counsel decides whether an amended filing is needed (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Response, forensic, legal, and notification costs; delivery delays from the gateway outage (P05); insurance coverage and retention; effect on guidance |
| Programs and customers | Which DoD and prime programs' data was taken; customer reaction; risk to future awards, CMMC status, or source approvals; remedies under contracts |
| Data | Volume and sensitivity of CUI and export-controlled data; number of employees and states for personal information |
| Legal and regulatory | DoD inquiries; export control exposure; state attorney general inquiries; litigation |
| National security | Whether disclosure could harm a program (raises the Attorney General delay question in step 7.8) |
| Reputation and strategy | Media coverage; analyst reaction; effect on the Program H bid |

**Worked example of the clocks (fictional dates):** the vendor publishes an advisory and the SOC sees anomalous gateway downloads on Tuesday 2027-02-02; discovery is recorded at 07:15. The **DIBNet report is due by Friday 2027-02-05 at 07:15** (72 hours). The disclosure committee convenes on Wednesday 2027-02-03 and determines materiality on Tuesday 2027-02-09 at 17:00. The **Form 8-K is due by Tuesday 2027-02-16** (4 business days: February 10, 11, 12, and 16, because Monday 2027-02-15 is a federal holiday). Forensics confirms on Friday 2027-02-12 that payroll files on the corporate instance were taken, covering about 7,800 employees, about 4,100 of them Florida residents. Florida's 30-day clocks for individuals and the Department of Legal Affairs run from that determination to Sunday 2027-03-14, so the plan targets Friday 2027-03-12. Counsel must also decide whether a "reason to believe a breach occurred" arose earlier (for example, when the vendor advisory named the corporate instance's version), which would move the state dates forward.

## 8. Export control and NISPOM decisions
| Decision | What happens | Owner |
|---|---|---|
| Was there an unauthorized export or release? | The Senior Empowered Official reviews the file list (section 4) with export counsel. Theft by an outside actor may not be a company violation, but release paths through the company (for example, files staged longer than needed, or access by a foreign person) are examined. Record the reasoning either way | Vice President, Trade Compliance |
| DDTC voluntary disclosure | If warranted: initial notification immediately after discovery, full disclosure within 60 calendar days of the notification unless extended (22 CFR 127.12(c)) | Vice President, Trade Compliance |
| BIS voluntary self-disclosure | If EAR technology from commercial programs was involved and a violation may have occurred (15 CFR 764.5) | Vice President, Trade Compliance |
| NISPOM | If the classified system is affected: report immediately to the DoD cognizant security office (32 CFR 117.8(f)(1)). If cleared employees were targeted: suspicious contact report (32 CFR 117.8(c)). Unclassified systems: the DIBNet report satisfies 117.8(f)(2) | Corporate Facility Security Officer; ISSM |

## 9. Multi-state breach notification workflow (employees) (RS.CO)
| Step | Action | Owner | Output |
|---|---|---|---|
| 9.1 | Confirm which payroll and benefits files were taken and which data elements they hold (names, Social Security numbers, bank account numbers) | Chief Human Resources Officer; forensics | Data element list |
| 9.2 | Build the affected population with **state of residence** from HR records, including remote employees and former employees in the files | Chief Human Resources Officer | Affected-individual file with state counts |
| 9.3 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, and content rules. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 9.4 | **Florida worked example:** individual notice within 30 days of determination; Department of Legal Affairs notice within 30 days if 500 or more Floridians (individual notice may get 15 more days on written good cause); consumer reporting agencies if more than 1,000 are notified at once | General Counsel | Florida filings |
| 9.5 | **Plan to the shortest clock** across all states and the SEC filing; publish one master calendar with the DoD and SEC dates | General Counsel | Master calendar |
| 9.6 | Honor any law enforcement delay request under each state's provisions (Florida 501.171(4)(b)); document it | General Counsel | Delay record |
| 9.7 | Engage the mail vendor, call center, and credit monitoring provider | Chief Human Resources Officer | Vendors active |
| 9.8 | Brief employees before notices arrive, in coordination with the 8-K timing | Chief Human Resources Officer; Communications | Employee message |

**Extortion.** If the actor demands payment, no payment may be made without the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.7). Report to the FBI or CISA. Paying does not remove any DoD, SEC, export, or state duty.

## 10. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. DoD reporting capability (clean laptop, certificate, contacts)
2. Identity platform: gateway and admin credentials rotated
3. Networks and egress controls: attacker blocks in place
4. Security tooling confirms no persistence in PLM, the suite, and virtual desktops
5. CUI exchange gateway rebuilt from known-good images on patched software, with the 72-hour purge rule, then supplier accounts re-enabled in waves
6. Corporate file transfer instance rebuilt; payroll files moved to the payroll SaaS direct integration
7. Confirm released engineering data in PLM was not altered (checksum comparison) before resuming releases to suppliers

**Validate before reconnecting:** EDR clean, patched, credentials rotated, logging to the SIEM, and the evidence set complete. Tell primes and suppliers when exchange resumes (RC.CO).

## 11. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of containment; written report within 30 days (POL-03 4.11).
- Update the risk register (P01: R-001, R-033, R-050, R-055), the POA&M (P07), this runbook, and the materiality playbook.
- Check whether the incident changes compliance with any CMMC requirement in the certified scope before the next affirmation (32 CFR 170.22), and whether the SSP or SPRS entries need updating.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including the materiality determination minutes and export decisions, for at least 6 years (POL-01 4.11), and the 252.204-7012(e) evidence for at least 90 days from the report or longer if DoD asks.
