# Incident Response Runbook: Ransomware with Student Record Exposure

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded postsecondary education company operating a private, for-profit college; 23 campuses in six states; online students in all 50 states and DC) |
| Tier / Vertical | Enterprise / Educational Services |
| Incident type | Ransomware with exfiltration of SIS extracts and scanned financial aid documents (double extortion), including the SEC materiality assessment, the FSA breach report, the FTC notice, and a multi-state breach notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Refund Fraud Response Procedure. Together they are the written incident response plan required by 16 CFR 314.4(h) |
| Runbook owner | Director of Security Operations, with the General Counsel for sections 6 and 7 and the Vice President, Financial Aid for the FSA steps |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise tabletop 2026-03-26 (technical and academic continuity; **the disclosure committee did not take part and the FSA and FTC steps were not exercised**). Next: full tabletop with the disclosure committee on 2026-11-12 (POAM-011) |
| Notification matrix | `notification-matrix.csv` (27 obligations: 5 federal education and Safeguards Rule, 4 generic state, 5 Florida worked example, 4 SEC, plus insider trading, OFAC, law enforcement, CIRCIA status, 3 contractual, and 2 checked and not applicable) |

**Where this plan meets 16 CFR 314.4(h):**
| Element | Where |
|---|---|
| (h)(1) Goals | POL-03 section 1 |
| (h)(2) Internal response processes | Sections 2 to 5 and 8 below |
| (h)(3) Roles, responsibilities, decision authority | POL-03 section 3; section 0 below |
| (h)(4) External and internal communications | Sections 6 and 7 and `notification-matrix.csv` |
| (h)(5) Remediation of weaknesses | Section 9 (feeds the POA&M) |
| (h)(6) Documentation and reporting | Section 3 step 7 (incident log); sections 6 and 7 |
| (h)(7) Evaluation and revision | Section 9 |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO (Qualified Individual) | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Provost and Chief Academic Officer | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Chief Compliance Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Notification event and breach decisions | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| FSA reporting and Department system access | Vice President, Financial Aid | Associate Vice President, Financial Aid Operations | Direct mobile |
| Education records and FERPA disclosure records | University Registrar | Associate Registrar | Direct mobile |
| Refunds and student funds | Vice President, Student Finance | Bursar | Direct mobile |
| Academic continuity (LMS, online and campus classes) | Provost and Chief Academic Officer | Deans; Director of Academic Technology | Crisis line |
| Campus safety and emergency notification | Vice President, Campus Operations | Campus safety directors | Crisis line |
| SL-1 and SL-2 clients | Vice President, Workforce Education Services; Vice President, Online Program Services | Client services leads | Direct mobile |
| Outside breach counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | MSSP incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (for investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, the student portal, and the identity platform may be compromised. Use company mobile phones, the out-of-band conferencing service, the emergency notification service (for students and staff), and the printed incident binders at headquarters and each student support center.

## 1. Preparation checks (Identify / Protect)
- [ ] Immutable backups in separate accounts, restore-tested within the last 90 days for tier-1 systems (CP-9, CP-4)
- [ ] EDR on all endpoints and servers, including the legacy imaging system (in place; the system itself is unsupported until POAM-008 closes)
- [ ] SIEM receives logs from all systems with customer information, **except the SAIG transmission software and the imaging system (gap until POAM-009 closes)**; logs retained 1 year online and 7 years in the archive (AU-11)
- [ ] Break-glass accounts sealed and tested this quarter
- [ ] Weekly read-only course packets published for online courses (**gap until POAM-007 closes**)
- [ ] Offline export of student and parent mailing and email addresses and emergency notification contact lists, refreshed weekly (**gap until POAM-024 closes**)
- [ ] Materiality playbook and 8-K templates current; disclosure committee roster current (**gap until POAM-011 closes**)
- [ ] FSA Cybersecurity Breach Intake instructions and the College's OPEID in the incident binder
- [ ] Outside counsel, forensics, and insurer contacts confirmed this quarter; state breach law matrix from outside counsel updated in the last 12 months
- [ ] Vendor contracts require incident notice within 72 hours (**legacy contracts and the Title IV servicer until POAM-005 and POAM-020 close**)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renames or encryption | EDR, staff report, backup job failures | SOC opens a severity-1 case; isolate hosts through EDR; page the incident commander |
| Large or unusual SIS report export, or a large outbound transfer from the data platform or file shares | Database activity monitoring, egress alerting, DLP (bulk-export detection until POAM-015 closes is limited) | Suspend the account; block the destination; preserve logs; open a case |
| MFA reset followed by sign-ins from a new device or location, or new privileged accounts | Identity platform, PAM, SIEM | Revoke sessions; disable the account; confirm with the user and manager by phone |
| Activity on the legacy imaging system or the SAIG servers that does not match their normal pattern | EDR; local logs reviewed weekly (until POAM-009 closes) | Treat as severity 1 until scoped; stop SAIG transmissions if Department access may be involved |
| Spike in student refund bank-detail changes | Daily bank-change reconciliation; student finance fraud review | Hold refund files; start PRC-03.4 |
| Extortion message to executives, staff, or students, or a leak-site post naming the College | Email, threat intelligence, law enforcement, media, FSA | Declare; preserve; do not engage without counsel |
| Vendor or Title IV servicer reports an incident affecting company data | Vendor notice | Open a vendor incident case with the vendor incident template; start the third-party track in section 7 |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any production system, or an extortion claim names company or student data.

**Record these times separately. They start different clocks:**
1. **Suspected breach (FSA):** report immediately. Do not wait for confirmation.
2. **Discovery (FTC):** the first day the event is known to any employee, officer, or other agent of the company other than the person committing the breach (16 CFR 314.4(j)(2)). This starts the 30-day FTC clock.
3. **Determination (states):** the day the company determined a breach occurred, or had reason to believe one occurred (Florida: Fla. Stat. 501.171(3)-(4)). Other states use their own triggers.
4. **Materiality determination (SEC):** recorded later by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Isolate affected hosts through EDR; do not power them off (preserve memory) | SOC | Hosts network-contained |
| 2. Block attacker infrastructure; cut the private link to the colocation data center if the imaging system or telephony core is affected; stop SAIG transmissions if Department access may be involved | SOC; Network Engineering; Vice President, Financial Aid | Blocks confirmed |
| 3. Revoke sessions and rotate credentials for privileged accounts, the integration service accounts, and the SAIG server accounts; use break-glass accounts if SSO is affected; freeze help desk MFA resets except by video verification | Identity team | Revocations logged |
| 4. Confirm backup accounts are untouched (immutability locks, no recent deletions) | Cloud Platform Engineering | Backup integrity confirmed |
| 5. Hold outgoing refund files and freeze student bank-detail changes until their integrity is confirmed | Vice President, Student Finance | No refund file released |
| 6. CISO briefs the CEO, the General Counsel, and the board risk committee chair; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 7. The Vice President, Financial Aid files the FSA Cybersecurity Breach Intake report and emails CPSSAIG@ed.gov | Vice President, Financial Aid | Submission confirmation |
| 8. COO activates the crisis management team; the Provost activates academic continuity (deadline extensions, course packets); campuses switch to downtime procedures | COO; Provost | Continuity running |
| 9. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open (POL-03 4.3) |

## 4. Analysis (RS.AN)
1. **Scope:** hosts, cloud accounts, identities, SaaS tenants, and data stores affected. Use EDR, SIEM, cloud audit logs, PAM records, and SIS audit trails. For the imaging system and SAIG software, collect logs locally, because they are not in the SIEM.
2. **Initial access:** help desk MFA reset, phishing, an edge device exploit, a vendor connection, or a stolen student or adjunct credential. Check help desk reset records and the legacy campus VPN concentrators first while POAM-013 and the R-048 treatment are open.
3. **Evidence:** forensics images hosts and exports logs before they roll over; chain of custody is kept in the evidence register; hashes recorded for each artifact.
4. **Exfiltration:** determine what data left, from which systems, for which people. Check the SIS report exports, the data platform, and the imaging system first; they hold the most concentrated customer information. Sources: egress logs, cloud storage access logs, warehouse query logs, the attacker's claims and samples. **This drives sections 6 and 7.**
5. **Who and what is affected.** Build the affected-person file from the data taken. For each person, record: type (student, former student, parent borrower, SL-2 partner student, employee); data elements (SSN, ISIR data, bank details, grades, disability or health records); state of residence; whether the data was encrypted and whether the key was also taken; and whether the record belongs to the College or to an SL-2 partner. This file drives every count: 500 consumers for the FTC, 500 Floridians for the Department, more than 1,000 for the consumer reporting agencies, and each other state's thresholds.
6. **Integrity:** confirm no grades, enrollment status, awards, or refund bank details were altered (compare to backups; check SIS audit trails; reconcile disbursements with Department records). If integrity cannot be confirmed, the University Registrar and the Vice President, Financial Aid decide what to hold.
7. **Determinations:** the Qualified Individual and counsel document whether a notification event occurred under 16 CFR 314.2 (unauthorized access to unencrypted customer information is presumed to be acquisition unless reliable evidence shows otherwise) and the discovery date; the Chief Privacy Officer documents state law breach determinations by state.
8. **Business impact:** Finance and the BIA owners estimate impact using P05 values (for example, about $5.9 million per day if online instruction stops, about $2.4 million per day if registration stops, and about $8.8 million of Title IV cash deferred per day if aid processing stops). These estimates feed section 6.

## 5. Containment and eradication (RS.MI)
1. Contain by segment: isolate affected accounts, cloud accounts, campuses, or the colocation link.
2. Disable compromised accounts; reset all privileged credentials and service account secrets; rotate integration, LMS, CRM, bank file, and partner feed keys.
3. Follow FSA's instructions for resetting SAIG and Department system credentials if they may be involved.
4. Rebuild from known-good images; never decrypt and reuse encrypted hosts.
5. Patch the initial access path before reconnecting.
6. Have the Title IV third-party servicer and any affected vendor confirm in writing that their access is reset and protected by MFA before reconnecting.
7. Forensics confirms persistence is removed before recovery starts in each zone.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.6) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 and 5 | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date and time and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align timing and content of student, partner, employer, media, and investor communications with the filing; brief the audit committee and the board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost or deferred receipts from P05 values; tuition credits and withdrawals; deferred Title IV cash; recovery, forensic, notification, credit monitoring, and legal costs; ransom demand; insurance coverage and retention |
| Operational | Instruction stopped (online, campus, SL-2 partners) and for how long; registration, aid processing, and refunds stopped; session start dates affected |
| Data | Number of students, former students, parent borrowers, and partner students; states involved; data types (SSNs, ISIR data, bank details, grades); whether data was published |
| Title IV and accreditation (added in 2026, POAM-011) | Likely FSA follow-up (a corrective action plan, a program review, or an administrative capability finding); effect on the next compliance audit; accreditor inquiry; state authorization inquiries |
| Legal and regulatory | Expected FTC, state attorney general, or Department inquiries; litigation exposure; breach of SL-1 and SL-2 contracts |
| Reputation and strategy | Media coverage; enrollment effect for upcoming start dates; partner or employer loss |

**Worked example of the clocks (fictional dates):** ransomware discovered Tuesday 2027-02-02 at 08:10 (FTC discovery); the FSA intake report is filed the same morning. An extortion email claiming data theft arrives Wednesday 2027-02-03. The committee convenes 2027-02-03 and determines materiality on Thursday 2027-02-04 at 16:00, so the Form 8-K is due by Wednesday 2027-02-10 (4 business days: February 5, 8, 9, and 10). Forensics confirms that SIS extracts with SSNs were taken on Friday 2027-02-19. The FTC notice is due no later than **2027-03-04** (30 days after discovery). Florida's 30-day clocks run from determination: 2027-03-21 if the determination is the forensic confirmation, but **2027-03-05** if counsel concludes that the extortion email on 2027-02-03 gave reason to believe a breach occurred. Plan to the earliest date: the FTC deadline of 2027-03-04 comes first, and other states may be earlier still.

## 7. Breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | FSA: initial intake report immediately (section 3 step 7); updates as scope, records affected, and remediation status change | Vice President, Financial Aid | Intake confirmations |
| 7.2 | Build the affected-person file (section 4 step 5) and separate four groups: (a) the College's students, former students, and parent borrowers; (b) SL-2 partner students; (c) SL-1 employer data; (d) employees | Chief Privacy Officer; data team | Affected-person file with state counts |
| 7.3 | **FTC:** if the notification event involves 500 or more consumers, file on the ftc.gov form as soon as possible and no later than 30 days after discovery. A law enforcement delay determination does not remove this notice; include it in the filing | Chief Privacy Officer with the Qualified Individual | FTC filing |
| 7.4 | **SL-2 partners:** notify each affected partner within the 72-hour contract term with the facts and the list of its students. Each partner is the institution for its own students and decides its own FERPA, state law, and FSA steps; the company supports them | Vice President, Online Program Services | Partner notices |
| 7.5 | **SL-1 employers:** notify affected employer clients within the 72-hour contract term | Vice President, Workforce Education Services | Client notices |
| 7.6 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, and content rules. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 7.7 | **Florida worked example:** individual notice within 30 days of determination (15 more days only on written good cause to the Department); Department of Legal Affairs notice within 30 days if 500 or more Floridians; consumer reporting agencies without unreasonable delay if more than 1,000 are notified at once. The deemed-compliance path in 501.171(4)(g) is not available, because no federal rule requires the College to notify individuals | General Counsel | Florida filings |
| 7.8 | **Plan to the shortest clock** across FSA, the FTC, every state, and the SEC. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 7.9 | Honor any law enforcement delay request under each state's provisions (for Florida, 501.171(4)(b)); document it | General Counsel | Delay record |
| 7.10 | Engage the mail vendor, call center, and credit monitoring provider; prepare the student portal and text message notices | Chief Privacy Officer | Vendors active |
| 7.11 | **FERPA:** within 14 days of the individual notices, record the unauthorized disclosure in each affected student's disclosure record (34 CFR 99.32(a)) | University Registrar | Disclosure records updated |
| 7.12 | Track inbound vendor notices (state third-party agent laws such as Fla. Stat. 501.171(6)(a); vendor contracts) if the incident started at a vendor | Director of Third-Party Risk Management | Vendor notices logged |
| 7.13 | Include the event and the response in the Qualified Individual's next annual written report (314.4(i)(2)) | CISO | Report section drafted |

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.9). Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove any notification or disclosure duty.

**Not in effect:** CIRCIA reporting to CISA (72 hours, or 24 hours after a ransom payment) is only proposed. It would cover every Title IV institution once final; until then reporting is voluntary.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Emergency notification service and campus safety systems (SaaS; confirm they were not affected)
2. Identity platform and break-glass access
3. Network core, SD-WAN, DNS, and cloud connectivity
4. Security tooling (EDR console, SIEM) for validation
5. Telephony and the student support center (overflow vendor until restored)
6. SIS and integration services in the standby region; the University Registrar and the Vice President, Financial Aid validate enrollment status, grades, and awards before release
7. LMS access for the College and SL-2 partner tenants (vendor recovery; obtain the vendor's integrity statement)
8. Student portal and mobile app; required MFA and bank-change controls stay on
9. Admissions CRM
10. SL-1 employer portal (tell SL-1 and SL-2 clients the restoration status)
11. SAIG transmission servers, coordinated with FSA, and financial aid processing
12. Online proctoring
13. Refund processing: before releasing held refunds, the Vice President, Student Finance confirms every bank-detail change made during the incident window with the student by phone. Title IV credit balances must still be paid no later than 14 days after they occur (34 CFR 668.164(h)(2)); use paper checks if the bank file is not ready
14. ERP and payroll
15. Transcripts, billing, and payment plans
16. Data and analytics platform (rebuild **without** ISIR-derived fields, POAM-004)
17. Legacy imaging system: **do not restore** to the old platform; recover documents into the cloud content service under POAM-008, or re-request documents from students

**Validate before reconnecting:** EDR clean, credentials rotated, patched, logging to the SIEM. Keep academic continuity and downtime procedures until each process meets its RTO. Tell students, partners, employers, and staff when services return (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- **Remediation (314.4(h)(5)):** record every weakness the incident exposed as a POA&M item with an owner and date (P07). Update the risk register (P01: R-001, R-002, R-003, R-013).
- **Evaluate and revise (314.4(h)(7)):** update this runbook, POL-03, the materiality playbook, and the notification matrix.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including the materiality determination minutes, notification event determinations, and notices, for at least 7 years (POL-01 4.11); this also covers the 5-year retention of any Florida no-harm determination (501.171(4)(c)).
