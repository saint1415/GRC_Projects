# Incident Response Runbook: Ransomware Forcing EHR Downtime and Ambulance Diversion

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded for-profit hospital system: 8 hospitals, 1,970 beds; FL, GA, AL) |
| Tier / Vertical | Enterprise / Healthcare and Public Health |
| Incident type | Ransomware that encrypts systems at several hospitals, forces EHR downtime, and may require ambulance diversion, with PHI exfiltration (double extortion). Includes the SEC materiality assessment and a multi-state breach notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Hospital IT-Outage Diversion Procedure |
| Emergency plan link | This runbook is the cyber annex to the unified emergency preparedness plan (42 CFR 482.15(a)(2) and (f)(4)); diversion and community communications use that plan's incident command and coordinated communication plan (482.15(c)) |
| Runbook owner | Director of Security Operations (HIPAA Security Officer), with the General Counsel for sections 7 and 8 and the Vice President, Emergency Management for section 4 |
| Approved | Executive risk committee, 2026-08-24 |
| Last tested | Enterprise ransomware tabletop 2026-02-26 (H-01 and H-02 clinical leaders; **the disclosure committee and EMS did not take part**). Next: multi-hospital downtime and diversion exercise with the disclosure committee on 2026-11-18 (POAM-004; POAM-005) |
| Notification matrix | `notification-matrix.csv` (34 obligations: 8 HIPAA, 1 Part 2, 4 generic state, 5 Florida worked example, 5 SEC and disclosure, plus EMS and emergency management, OFAC, law enforcement, CIRCIA status, FTC HBNR screening, contractual, and FAR screening rows) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (technical) | Director of Security Operations | SOC manager on duty | SOC bridge on the out-of-band conferencing service |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| System incident command (all hospitals) | Chief Operating Officer | Chief Medical Officer | System command center at H-01; backup at H-02 |
| Hospital incident commander (each hospital) | Hospital president | House supervisor on duty | Hospital command center; EMS radio in the ED |
| Clinical downtime leads | Chief Nursing Officer; Chief Medical Information Officer | Hospital chief nursing officers | Crisis line |
| Diversion coordination | System Transfer and Command Center | Vice President, Emergency Management | Transfer center line; EMS radio |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, COO, CISO, Chief Privacy Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| Breach and privacy decisions | Chief Privacy Officer (HIPAA Privacy Officer) | Chief Compliance Officer | Direct mobile |
| ECIS recovery | EHR Technical Director | EHR vendor 24x7 support | Data center operations bridge |
| Outside breach counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | Managed security service provider incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| SL-1 practices and SL-2 partners | Vice President, Affiliate Services; Vice President, Virtual Care | Service desks | Contact rosters in the binder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, VoIP, the identity platform, and the file servers may be compromised. Use company mobile phones, the out-of-band conferencing service, EMS radio and analog lines in each ED, and the printed incident binder in every hospital command center.

## 1. Preparation checks (Identify / Protect)
- [ ] Immutable backups in a separate account, restore-tested in the last 90 days (CP-9, CP-4). **Cyber restore 41 h against a 24 h target until POAM-003 closes**
- [ ] Isolated recovery environment ready (**in build until POAM-003 closes**)
- [ ] EDR on all endpoints and servers, **including H-08 (gap until POAM-022 closes)**
- [ ] SIEM receives logs from all clinical systems, **except the H-08 EHR, device gateways, and OT (gap until POAM-007 closes)**
- [ ] All service accounts vaulted (**gap until POAM-001 closes**)
- [ ] Break-glass accounts sealed and tested this quarter (POL-02 4.11)
- [ ] BCA downtime computers checked this month at every hospital, with reports less than 2 hours old (POL-03 4.10)
- [ ] IT-outage diversion criteria agreed with county EMS at every hospital (**only H-01 until POAM-018 closes**)
- [ ] Analog lines, EMS radio, and cellular phones tested in every ED
- [ ] Materiality playbook, thresholds, and 8-K templates current; disclosure committee roster current (**gap until POAM-005 closes**)
- [ ] Outside counsel, forensics, and insurer contacts confirmed this quarter; state breach law matrix updated in the last 12 months
- [ ] Printed incident binder in every hospital command center: this runbook, contact lists, diversion script, downtime procedures, notification matrix

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renames or encryption | EDR, staff report, backup job failures | SOC opens a severity-1 case; isolate hosts through EDR; page the incident commander |
| Several workstations, ADCs, or analyzer middleware stop at once on one or more units | Nursing, pharmacy, laboratory | Charge nurse calls the service desk and starts unit downtime; SOC triages |
| Large or unusual outbound transfer (reporting database, analytics, cloud storage) | Egress monitoring, DLP, cloud threat detection | Block destination; preserve logs; open a case |
| Privileged account misuse, new admin accounts, or service account use from a workstation | PAM, identity platform, SIEM | Revoke sessions; disable the account; open a case |
| Suspicious activity from the H-08 network or legacy directory | Network detection, VPN logs, H-08 IT report | Treat as severity 1 until scoped; cut the H-08 VPN if activity reaches the integration engine |
| Extortion message or leak-site post naming the system | Email, threat intelligence, law enforcement, media | Declare; preserve; do not engage without counsel |
| A vendor reports a ransomware event affecting system PHI or connections | Vendor notice (BAA) | Open a vendor incident case; consider cutting the vendor's interfaces |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any production system, or an extortion claim names system data.

**Record two times, separately:**
1. **Discovery time** (HIPAA): the first day the breach was known, or by reasonable diligence would have been known, to any workforce member or agent (45 CFR 164.404(a)(2)). Night-shift reports at any hospital count. This starts the 60-day HIPAA clock.
2. **Materiality determination time** (SEC): recorded later by the disclosure committee (section 7). This starts the 4-business-day Form 8-K clock.

## 3. First 4 hours (RS.MA, RS.MI, and patient safety)
Three tracks start together: the **technical track** (incident commander), the **clinical track** (system incident command and each hospital incident commander), and the **executive track** (CISO and General Counsel).

| Step | Who | Done when |
|---|---|---|
| 1. Each affected hospital starts downtime procedures on every unit, the ED, pharmacy, laboratory, imaging, and registration; collect the latest BCA prints | Hospital incident commanders; charge nurses | Paper workflow running |
| 2. Isolate affected hosts through EDR; do not power them off (preserve memory) | SOC | Hosts network-contained |
| 3. Block attacker infrastructure; cut the H-08 VPN and any vendor interface involved; consider isolating DC-2 from DC-1 replication to protect the standby | SOC; Network Engineering; EHR Technical Director | Blocks and isolation confirmed |
| 4. Revoke sessions and rotate credentials for privileged and service accounts involved; use break-glass accounts if SSO is affected | Identity team | Revocations logged |
| 5. Confirm the backup vault is untouched (retention locks, no deletions, no policy changes) | Cloud Platform Engineering | Vault integrity confirmed |
| 6. Patient safety checks: pumps keep their last approved drug library; ADCs to override with nurse double check; critical results by phone | Chief Nursing Officer; pharmacy and laboratory leaders | Safety checks logged |
| 7. COO opens system incident command; each hospital assesses whether its ED can safely accept ambulances (section 4) | COO; hospital presidents | Decisions recorded with time |
| 8. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 9. Notify SL-2 partner hospitals within 15 minutes of any tele-critical care interruption; notify SL-1 practices of EHR downtime | Vice President, Virtual Care; Vice President, Affiliate Services | Notices logged |
| 10. Start the incident log (timeline, decisions, who, when) on paper and the evidence register | Incident commander | Log open |

## 4. Clinical operations and ambulance diversion (RS.MA, RC.RP)
**What the law allows.** EMTALA lets a hospital direct an ambulance that is **not yet on hospital property** to another facility when the hospital is in "diversionary status," that is, "it does not have the staff or facilities to accept any additional emergency patients" (42 CFR 489.24(b), definition of "comes to the emergency department"). If the ambulance comes onto hospital property anyway, the patient has come to the emergency department. Diversion never changes the duty to screen and stabilize anyone who arrives, by ambulance or on foot (489.24(a)). The system owns no ambulances, so the separate rules for hospital-owned ambulances do not apply. The freestanding EDs are dedicated emergency departments too.

**Decision rule (from the BIA, P05 section 5; STD-03.4).** Each hospital decides for itself. The hospital president (or delegate), the ED medical director, and the house supervisor decide together (POL-03 4.6). Consider diversion when any trigger is true and not expected to recover within the MTD:
| Trigger | Scope of diversion |
|---|---|
| CT cannot be read, or images cannot reach a radiologist (BP-05) | CT-dependent traffic: suspected stroke, major trauma |
| Laboratory cannot produce or report results, including critical values (BP-04) | Traffic needing stat laboratory work |
| ED cannot document, order, or give medications safely on paper (BP-01, BP-02, BP-06) | Full diversion |
| Phones, secure messaging, and radio fallback all unavailable (BP-08) | Full diversion |
| Operating room air handling or medical gas alarms unavailable (BP-09) | Trauma and surgical traffic |

**Multi-hospital coordination rule.** No more than one hospital in a county may go on full IT-outage diversion unless the System Transfer and Command Center has confirmed with county EMS and the receiving hospitals that they can absorb the load. If several system hospitals in one region are affected, system incident command decides which stay open for EMS (for example, keeping the trauma center at H-01 open with paper workflows and extra staff while H-02 diverts stroke traffic to it).

**Diversion steps:**
1. Notify county EMS dispatch by radio or analog line using the script in the binder: scope (full or CT-dependent only), reason ("IT systems outage"), and next update time. Do not say "cyberattack" on open radio.
2. Notify the System Transfer and Command Center, which informs receiving hospitals and county emergency management (482.15(c)(7) and (b)(7)).
3. Record every decision and status change with the time and the trigger that justified it.
4. Review diversion at least every 2 hours and end it as soon as the affected process is back within its RTO or a safe workaround is running.

**Patients already in the hospital.** Continue care on paper. Transfer patients who need services the hospital cannot provide without its systems, sending all available records with the patient (489.24(e)(2)(iii)) through the paper transfer packet and copy log (482.15(c)(4)). HIM tracks every paper record created (POL-04 4.6).

## 5. Analysis (RS.AN)
1. **Scope:** hosts, servers, data centers, cloud accounts, identities, and data stores affected. Check whether DC-2 and the shared directory are affected; this decides failover (section 9) versus a vault restore. For H-08, collect EHR logs from the legacy vendor, because they are not in the SIEM.
2. **Initial access:** phishing, stolen credentials, an edge device, an unvaulted service account, a vendor remote tool, an SL-1 practice connection, or the H-08 network. Check the H-08 VPN and service accounts first while POAM-006 and POAM-001 are open.
3. **Evidence:** forensics images hosts and exports logs before they roll over; chain of custody in the evidence register; hashes recorded for each artifact.
4. **Exfiltration:** determine what data left, from which systems, for which patients, workforce members, and SL-1 practices. Sources: egress logs, reporting database and analytics query logs, cloud storage logs, and the attacker's claims and samples. Check whether H-03 Part 2 records are involved (42 CFR 2.16(b)). **This drives section 8.**
5. **Integrity:** confirm no clinical data was altered (compare to backups; check audit trails; reconcile laboratory results). If integrity cannot be confirmed, laboratory directors decide whether to hold result release and issue corrected reports (42 CFR 493.1291(k)).
6. **Business impact:** Finance and the BIA owners estimate daily impact with P05 values: about $3.1 million a day if emergency care is disrupted system-wide, $5.6 million for inpatient care, $3.4 million for surgery, and about $10.5 million a day of deferred collections if claims stop. Diversion hours by hospital are tracked. These estimates feed section 7.

## 6. Containment and eradication (RS.MI)
1. Contain by segment: isolate affected hospitals, data center tiers, cloud accounts, or the H-08 network.
2. Disable compromised accounts; reset all privileged credentials and service account secrets; rotate interface and API keys (integration engine, clearinghouses, HIEs, SL-1 gateway, SL-2 platform).
3. Rebuild from known-good images in the isolated recovery environment; never decrypt and reuse encrypted hosts.
4. Patch the initial access path before reconnecting.
5. Forensics confirms persistence is removed in each zone before recovery starts there.

## 7. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 to 6. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 7.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 7.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision. The COO brings a status report from system incident command (hospitals in downtime, diversion hours, expected recovery) | General Counsel | Minutes started |
| 7.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 7.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 to 6 | Committee | Worksheet completed |
| 7.5 | **Materiality determination** recorded with the date and time and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 7.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 7.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 7.8 | Align timing and content of patient, partner, media, and investor communications with the filing; brief the audit committee and board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 7.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost or deferred revenue from P05 values; recovery and forensic costs; ransom demand; notification, credit monitoring, and legal costs; insurance coverage and retention; effect on liquidity and covenants. Thresholds updated for H-08 (POAM-005) |
| Operational | Hospitals in EHR downtime and for how long; diversion hours by hospital; cancelled surgeries; SL-1 and SL-2 service interruptions |
| Data | Number of patients and states; data types (PHI, Social Security numbers, Part 2 records); whether data was published |
| Patient safety | Any harm or near miss linked to the incident or to diversion |
| Legal and regulatory | Expected OCR, CMS or state survey, EMTALA, CLIA, or state attorney general inquiries; litigation; contract breaches with SL-1 practices and SL-2 partners |
| Reputation and strategy | Media coverage; community trust; effect on acquisitions and partner contracts |

**Worked example of the clocks (fictional dates):** ransomware is reported by night-shift staff at H-02 at 02:40 on Tuesday 2027-03-02 (HIPAA discovery date). Two hospitals go on CT-dependent diversion that morning. The committee convenes Wednesday 2027-03-03 and determines materiality on Thursday 2027-03-04 at 17:00. The Form 8-K is due by Wednesday 2027-03-10 (4 business days: March 5, 8, 9, and 10). Forensics confirms PHI was taken on Monday 2027-03-15; Florida's 30-day clocks (individuals and the Department of Legal Affairs) run from that determination to 2027-04-14. The HIPAA 60-day outer limit runs from discovery to 2027-05-01, so the Florida date comes first and sets the plan. Counsel must also decide whether a "reason to believe a breach occurred" arose earlier (for example, when the extortion message claimed data theft), which would move the Florida dates forward.

## 8. Multi-state breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 8.1 | Four-factor breach risk assessment (45 CFR 164.402): nature and extent of PHI, who received it, whether it was actually acquired or viewed, and mitigation. Ransomware with exfiltration is treated as a breach unless the assessment shows a low probability of compromise | Chief Privacy Officer | Signed assessment |
| 8.2 | Build the affected population from forensic results: each individual, data elements, and **state of residence**. Separate: (a) the system's own patients and workforce; (b) SL-1 practices' patients (the system is their business associate); (c) H-03 Part 2 patients | Chief Privacy Officer; data team | Affected-individual file with state counts |
| 8.3 | **Business associate duty (SL-1):** notify each affected practice within the hosting agreement term (10 days), and no later than 60 days after discovery (164.410), with the identity of each individual. Practices decide their own notices unless they delegate to the system | Vice President, Affiliate Services | Practice notices sent |
| 8.4 | Apply HIPAA (and 2.16(b) for Part 2 records): individual notices within 60 days of discovery; HHS contemporaneously if 500 or more; media in every state or jurisdiction with more than 500 affected residents; substitute notice where contact information is missing | Chief Privacy Officer | HIPAA notice plan |
| 8.5 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general notices, consumer reporting agency thresholds, content rules, and whether HIPAA-compliant notice satisfies the state law. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 8.6 | **Florida worked example:** individual notice within 30 days of determining the breach (15 more days only with written good cause to the Department, and only for individual notice); Department of Legal Affairs notice within 30 days if 500 or more Floridians; consumer reporting agencies if more than 1,000 are notified at once; HIPAA notice is deemed compliant if a copy is timely provided to the Department | General Counsel | Florida filings |
| 8.7 | **Plan to the shortest clock** across HIPAA, every state, and the SEC. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 8.8 | Honor any law enforcement delay request under 164.412 and the matching state provisions; document it | General Counsel | Delay record |
| 8.9 | Engage the mail vendor, call center (toll-free number for 90 days if substitute notice is used), and credit monitoring provider | Chief Privacy Officer | Vendors active |
| 8.10 | Notify contractual parties: SL-2 partners, payers and Medicaid managed care plans, and the insurer, per contract | Contract owners | Contract notices logged |
| 8.11 | Track inbound vendor notices (164.410; state third-party agent laws such as Fla. Stat. 501.171(6)) if the incident started at a vendor | Director of Third-Party Risk Management | Vendor notices logged |

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.7). Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove notification or disclosure duties and does not guarantee working decryption.

**CIRCIA:** not in effect as of 2026-10-06. If finalized as proposed, all 8 hospitals (100 or more beds) would have to report a covered incident to CISA within 72 hours and a ransom payment within 24 hours. Recheck the matrix whenever the rule changes.

## 9. Recovery (RC.RP, RC.CO)
**Choose the recovery path first.** If DC-2 and the directory are clean, fail the ECIS over to DC-2 (tested at 2.6 hours). If both data centers or the directory are compromised, rebuild from the immutable vault in the isolated recovery environment (target 24 hours; 41 hours in the last test, POAM-003). Keep hospitals on downtime and keep diversion decisions under review until each process meets its RTO.

Restore in BIA priority order (P05 section 8), in a clean environment first:
1. Clinical communications: analog lines, radio, cellular; then VoIP and secure messaging
2. Identity platform and break-glass access
3. Network core, SD-WAN, DNS, data center links
4. Building OT monitoring
5. Security tooling (EDR console, SIEM) for validation
6. Tele-critical care platform (tell SL-2 partners the status)
7. ECIS: database, application, integration engine (obtain the EHR vendor's support for validation)
8. Laboratory analyzer middleware and pharmacy ADC servers: laboratory directors validate results against controls before release
9. PACS and the radiology reading path
10. Patient portal, telehealth, and FHIR API (tell SL-1 practices the status)
11. H-08 legacy EHR (with the legacy vendor)
12. HIE, public health reporting, release of information; resend queued reportable results
13. ERP, payroll, supply chain
14. Clearinghouse connectivity and the claims backlog (fallback to the secondary clearinghouse and payer portals if the primary is affected)

**Validate before reconnecting:** EDR clean, credentials rotated, patched, logging to the SIEM. **Back-entry:** each unit enters its downtime records within 24 hours of recovery, starting with medication administration and results, with the author's authentication (POL-04 4.6; 42 CFR 482.24(c)(1)). End diversion and tell EMS, emergency management, staff, patients, partners, and the community when services return (RC.CO).

## 10. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- File the after-action report in the emergency preparedness binder. An actual emergency that activates the emergency plan exempts the hospitals from their next required full-scale or functional exercise, and the response must be analyzed and documented (42 CFR 482.15(d)(2)(i)(B) and (d)(2)(iii)).
- Update the risk register (P01: R-001, R-002, R-004, R-009, R-015), the POA&M (P07), this runbook, the diversion criteria, and the materiality playbook.
- The disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including diversion logs, materiality minutes, and breach assessments, for at least 6 years (POL-01 4.11).
