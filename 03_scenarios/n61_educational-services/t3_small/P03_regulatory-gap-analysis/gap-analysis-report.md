# Regulatory Gap Analysis: Cris Santos Company | Educational Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (private career college) |
| Tier / Vertical | Small / Educational Services |
| Primary regulation | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314, as applied to Title IV institutions and enforced by Federal Student Aid (FSA). Text checked on eCFR as of 2026-09-23 (last amended 88 FR 77508, Nov. 13, 2023) |
| Secondary regulation | FERPA, 34 CFR Part 99, plus three closely related Title IV requirements |
| Assessment dates | 2026-07-06 to 2026-07-17 |
| Assessor | IT Director (Qualified Individual) with the Registrar and the Director of Financial Aid |

## 1. Applicability
**The Safeguards Rule applies.** Each institution that participates in Title IV has agreed in its Program Participation Agreement to comply with 16 CFR Part 314. FSA reviews compliance in the annual compliance audit and treats information security safeguards as part of administrative capability under 34 CFR 668.16(c) (FSA Electronic Announcement GENERAL-23-09, Feb. 9, 2023). For GLBA purposes FSA defines customer information as information obtained as a result of providing a financial service to a student, past or present, such as administering Title IV aid.

**The small-institution exception does not apply.** 16 CFR 314.6 exempts institutions that maintain customer information on fewer than five thousand consumers from 314.4(b)(1), (d)(2), (h), and (i). The college's FAMS and SIS aid records cover about **6,400 consumers**: current aid recipients, former students within the Title IV record retention period, and parent borrowers. So every element of 314.4 applies, including the written risk assessment, penetration testing and vulnerability assessments, the written incident response plan, and the annual written report to the Board.

**Not applicable, with reasons:**
- **314.4(a)(1)-(3):** these apply only when the Qualified Individual works for a service provider or affiliate. The IT Director is a college employee.
- **314.4(c)(4), secure development:** the college builds no applications that handle customer information. The second half of (c)(4), evaluating externally developed applications, does apply and is a gap.

**Secondary regulation (Small tier: primary plus the most relevant secondary).**
- **FERPA** applies because the college receives funds under Department of Education programs. FERPA is disclosure-oriented. Its security-relevant duty is 99.31(a)(1)(ii): use "reasonable methods" so school officials reach only the records they have a legitimate educational interest in. Eight FERPA requirements were assessed.
- **FERPA has no breach notification clock.** The Department's Student Privacy Policy Office guidance says FERPA does not require an institution to notify students that information from their education records was stolen or otherwise subject to an unauthorized release, but it does require the institution to keep a record of each disclosure (34 CFR 99.32(a)(1)). Breach notice duties come from the FTC (314.4(j)), the SAIG Enrollment Agreement, and Florida law (see P08).
- **Title IV requirements** closely tied to the Safeguards Rule were added: the SAIG Enrollment Agreement breach notice, 34 CFR 668.16(c)(1) internal controls, and the HEA limits on use of FAFSA data and federal tax information.

## 2. Method
1. **Requirements.** Each row is a paragraph of 16 CFR 314.3 or 314.4, or of 34 CFR Part 99, at the most granular level the regulation uses (for example, 314.4(h)(1) to (h)(7)). Summaries paraphrase public-domain regulatory text.
2. **Requirement type.** The Safeguards Rule has no required/addressable split. Its elements are mandatory ("shall"), with two built-in alternatives: encryption may be replaced by compensating controls the Qualified Individual reviews and approves (314.4(c)(3)), and MFA may be replaced by equivalent controls the Qualified Individual approves in writing (314.4(c)(5)). Neither alternative has been approved today.
3. **Crosswalk.** Each row was mapped to CSF 2.0 and SP 800-53 Rev. 5. These are **author mappings**; no official NIST mapping for 16 CFR Part 314 was used.
4. **Evidence.** Interviews (Campus President, IT Director, Director of Financial Aid, Registrar, Business Office Manager, Dean of Academic Affairs), document review (WISP, contracts, Board minutes, training records), and configuration exports.
5. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork (2026-07-17). Remediation that has since been completed (for example, POL-03 and the P08 runbook, approved 2026-08-21) is shown in the remediation columns, not as a changed status.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 314.3(a) Written program | 0 | 1 | 0 | 0 |
| 314.4(a) Qualified Individual | 1 | 0 | 0 | 3 |
| 314.4(b) Risk assessment | 3 | 2 | 0 | 0 |
| 314.4(c) Safeguards | 0 | 6 | 5 | 0 |
| 314.4(d) Testing and monitoring | 0 | 1 | 3 | 0 |
| 314.4(e) Personnel | 0 | 2 | 2 | 0 |
| 314.4(f) Service providers | 0 | 2 | 1 | 0 |
| 314.4(g) Evaluate and adjust | 0 | 0 | 1 | 0 |
| 314.4(h) Incident response plan | 0 | 2 | 6 | 0 |
| 314.4(i) Report to the Board | 0 | 0 | 3 | 0 |
| 314.4(j) FTC notification | 0 | 0 | 2 | 0 |
| 314.6 Exception | 0 | 0 | 0 | 1 |
| **Safeguards Rule subtotal (47)** | **4** | **16** | **23** | **4** |
| FERPA, 34 CFR Part 99 (8) | 3 | 5 | 0 | 0 |
| Title IV requirements (3) | 0 | 2 | 1 | 0 |
| **Total (58)** | **7** | **23** | **24** | **4** |

Of the 47 rows that are unmet or partially met, 4 are rated **High**, 33 **Moderate**, and 10 **Low**.

**What is working:** a Qualified Individual is designated in writing, the 2026 risk assessment now meets the 314.4(b)(1) content requirements, staff MFA is in place, separation of duties between awarding and disbursing aid is enforced, and FERPA consent and access requests are handled well.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Servicer administrators of the student aid portal have no MFA | 314.4(c)(5) | High | Contract amendment requiring MFA or federation | Director of Financial Aid | 2026-10-31 |
| Servicer contract lacks specific safeguards | 314.4(f)(2) | High | Amendment: MFA, encryption, 72-hour incident notice, right to assess | Director of Financial Aid | 2026-10-31 |
| Unencrypted aid spreadsheets at rest and in email | 314.4(c)(3) | High | Restricted FAMS report role; encrypt required exports; message encryption | Director of Financial Aid | 2026-11-30 |
| No penetration testing or scheduled vulnerability assessments | 314.4(d)(2) | High | Scans every six months; annual external penetration test | IT Director | 2026-12-31 |
| No written report to the Board | 314.4(i) | Moderate | First report at the 2026-10-15 Board meeting | IT Director | 2026-10-15 |
| Risk assessment 2 years old | 314.4(b)(2) | Moderate | 2026 assessment done (P01); annual cycle | IT Director | 2027-07-31 |
| No written incident response plan; no FTC or FSA notice procedure | 314.4(h), (j); SAIG agreement | Moderate | POL-03 and P08 approved 2026-08-21; tabletop | IT Director | 2026-11-30 |
| Vendor oversight limited to contracts | 314.4(f)(3) | Moderate | Annual SOC 2 review (SIS and LMS done in P09) | IT Director | 2026-11-30 |
| No user activity monitoring | 314.4(c)(8) | Moderate | Weekly and monthly log reviews; EDR alerting | IT Director | 2026-10-31 |
| Broad SIS access for admissions and advisors | 314.4(c)(1)(ii); 34 CFR 99.31(a)(1)(ii) | Moderate | Role redesign; semiannual access review | Registrar | 2026-12-31 |
| No change management | 314.4(c)(7) | Moderate | Change procedure and log | IT Director | 2026-11-30 |
| No disposal schedule | 314.4(c)(6) | Moderate | Retention schedule; annual disposal | Director of Financial Aid | 2027-03-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The Board report on 2026-10-15 will present this table as the compliance status required by 314.4(i)(1).

## 5. Pending regulatory changes
- **16 CFR Part 314:** no pending FTC amendment was identified. The most recent change added the 314.4(j) FTC notice, effective May 13, 2024 (314.5).
- **CIRCIA (N61-R06)** is **still proposed**. The proposed rule (89 FR 23644, Apr. 4, 2024) would cover every institution of higher education that participates in Title IV, with no size floor, and would require reports to CISA within 72 hours of a covered cyber incident and within 24 hours of a ransom payment. It is flagged in the `pending_rule_change` column of the two notification rows and is **not** treated as a current obligation.
- **FSA and NIST SP 800-171:** FSA has encouraged institutions to adopt NIST SP 800-171 (Electronic Announcements of Dec. 18, 2020 and GENERAL-23-09), but has said the current requirement is the Safeguards Rule. It is tracked as guidance, not a requirement.
