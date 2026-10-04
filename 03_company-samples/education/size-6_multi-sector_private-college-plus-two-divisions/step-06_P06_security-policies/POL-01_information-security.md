# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Higher Education, Education Software, Student Health) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Division primary regulations | Higher Education: FTC Safeguards Rule, 16 CFR 314 (N61-R02) and FERPA (N61-R01). Education Software: COPPA, 16 CFR 312.8 and 312.10 (N61-R03). Student Health: HIPAA Security Rule, 45 CFR 164 Subpart C (N62-R01) |
| Division supplements | Higher Education (v2026); Education Software (v2025, change gate to be added by 2026-11-30); Student Health (v2023, re-issue due 2026-11-30). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects students', families', patients', and customers' information and the systems that hold it. For Cris Santos College this policy, the other group policies, the Higher Education supplement, and the P02 system security plans together form the written information security program required by 16 CFR 314.3(a). For Education Software they form the written children's information security program required by 16 CFR 312.8(b).

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, faculty, adjuncts, contractors, student workers, and volunteers), all systems and data the group owns or operates, and systems operated for the group by service providers, including one division acting for another. It covers customer information under the Safeguards Rule, education records and treatment records under FERPA, children's personal information under COPPA, PHI under HIPAA, and all other group information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber and AI risk; approves this policy; accepts Very High risks |
| College board of trustees | Receives the Qualified Individual's written report at least annually (314.4(i)) |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the group AI council |
| Group Chief Privacy Officer | Owns data classification, purpose limits, and cross-division data sharing rules |
| Group General Counsel | Owns intercompany agreements, customer and vendor contract terms, and the notification matrix |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Very Low and Low risks |
| College CISO | **Qualified Individual** for Cris Santos College (16 CFR 314.4(a)) |
| Education Software CISO | Coordinator of the children's information security program (16 CFR 312.8(b)(1)) |
| Student Health security and compliance lead; Student Health Privacy Officer | HIPAA Security Official and Privacy Official (45 CFR 164.308(a)(2); 164.530(a)) |
| University registrar | FERPA compliance officer for the college |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that meets each division's primary regulation: the Safeguards Rule for the college, the COPPA security program for Education Software, and the HIPAA Security Rule for Student Health. (PM-1; GV.PO-01; 314.3(a); 312.8(b); 164.316)

4.2 The Group CISO is accountable for the program. Each division must designate its regulator-facing roles in writing: the college's Qualified Individual, Education Software's COPPA program coordinator, and Student Health's HIPAA Security and Privacy Officials. (PM-2; GV.RR-02; 314.4(a); 312.8(b)(1); 164.308(a)(2))

4.3 Each division and corporate must complete a written risk analysis at least annually and after material changes, using NIST SP 800-30 Rev. 1. A new product feature, a new data flow between divisions, an acquisition, or a new AI use is a material change. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; 314.4(b); 312.8(b)(2); 164.308(a)(1)(ii)(A)-(B))

4.4 **Risk acceptance authority:** Very Low and Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Risks of harm to children, or to a student's access to education, rated High must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02; 164.316(b)(2)(iii))

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems that holds Restricted data (POL-04), which controls it inherits from corporate or from another division and which remain its own, and must confirm that documentation every year. (PL-2; CA-2; GV.RR-02; 164.308(a)(8))

4.7 **Sanctions.** Workforce members who violate security or privacy policies must be sanctioned in proportion to intent and harm, and HR must document every sanction. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))

4.8 **Service providers, including sister divisions.** No service provider may hold or process a division's Restricted data without a written agreement that requires safeguards, limits use to the division's purposes, sets an incident notice time (24 hours between group divisions; 72 hours or shorter for outside providers), and gives a right to assess. This applies when one division serves another: Education Software is a service provider and school official for the college, Student Health acts for the college and for contracting colleges, and corporate is a business associate of Student Health. Each division must assess its service providers before contract and at least annually, based on risk. (SA-4; SA-9; GV.SC-05; 314.4(f); 34 CFR 99.31(a)(1)(i)(B); 312.8(c); 164.308(b))

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. Each division must also regularly test or monitor its key controls, including annual penetration testing and vulnerability assessments at least every six months for systems holding customer information. (CA-2; CA-7; CA-8; RA-5; ID.IM-01; 314.4(d); 312.8(b)(4); 164.308(a)(8))

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1)

4.11 Security policies, procedures, risk analyses, assessments, and required actions must be retained for 6 years from creation or last effective date, whichever is later. (SI-12; 164.316(b)(2)(i))

4.12 **AI systems.** No AI system that uses Restricted data, that is offered to children, or that makes or supports decisions about applicants, students, patients, or customers' students may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.13 **Reporting to governing bodies.** The Qualified Individual must report in writing at least annually to the college board of trustees on the overall status of the college's program and its compliance with 16 CFR 314, and on material matters including risk assessment, risk decisions, service provider arrangements (including those with other group divisions), testing results, security events, and recommendations. The Group CISO reports to the board risk committee each quarter. (PM-9; CA-7; GV.OV-01; 314.4(i))

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, division access reviews, and, for the college, the annual Title IV compliance audit.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); 16 CFR Part 314; 34 CFR Part 99; 16 CFR Part 312; 45 CFR 164 Subpart C.
