# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Staffing, Professional Services and Consulting, Home Health) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, RA-8, SA-4, SA-9, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, GV.SC-06, ID.RA-01, ID.IM-01 |
| Regulatory anchors | NIST CSF 2.0 (group benchmark); HIPAA 164.308(a)(1), (a)(2), (a)(8), (b)(1)-(2) and 164.316 for Home Health, Consulting, and corporate; 8 CFR 274a.2(g) and the E-Verify MOU for every employing entity; FAR 52.204-21 for Federal Solutions; Reg S-K Item 106 |
| Division supplements | Staffing supplement (v2026); Consulting supplement (v2026); Home Health supplement (v2023, re-alignment due 2026-11-30). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects the people whose data the group holds (candidates, associates, consultants, caregivers, patients, and clients' data) and the systems that hold it.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (internal employees, temporary associates when they use group systems, contractors, and subcontractors), all systems and data the group owns or operates, and systems operated for the group by vendors and other service providers. It covers worker and candidate personal information, Form I-9 and E-Verify records, consumer reports, clinician medical screening files, Home Health PHI, client PHI that Consulting holds as a business associate, federal contract information, and all other group information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group Chief Privacy Officer | Owns data classification, the processing register, privacy impact assessments, and minimum-necessary rules across divisions |
| Group General Counsel | Owns BAAs, intercompany agreements, vendor terms, and the notification matrix; chairs the disclosure committee |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Home Health HIPAA Privacy Officer and Security Officer | Designated by the covered entity (45 CFR 164.308(a)(2); 164.530(a)) |
| Consulting HIPAA compliance officer | Runs the business associate program |
| Staffing Vice President, Employment Compliance | Owns Form I-9, E-Verify, and FCRA procedures for every employing entity |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that also meets the binding rules each division is subject to (HIPAA for Home Health and for Consulting and corporate as business associates, FAR 52.204-21 for Federal Solutions, and the employment record rules for every employing entity). (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Home Health must designate its own HIPAA Security Official and Privacy Official in writing. Consulting must designate a HIPAA compliance officer for its business associate program. (PM-2; GV.RR-02; 164.308(a)(2))

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; 164.308(a)(1)(ii)(A)-(B))

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Patient-safety risks and risks that would leave workers unpaid, when rated High, must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02; 164.316(b)(2)(iii))

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems that holds personal information, PHI, or federal contract information, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security or privacy policies must be sanctioned in proportion to intent and harm. HR and, for PHI, the relevant privacy official must document every sanction. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))

4.8 **No contract, no data.** No vendor, subcontractor, or intercompany service provider may receive personal information, PHI, or federal contract information without a written agreement with security and breach notice terms and a security review. For PHI, that agreement must be a business associate or subcontractor agreement that covers the specific service. Intercompany BAAs must be reviewed whenever corporate adds or changes a service that touches a division's PHI. Add-ons enabled through a SaaS marketplace count as new vendors. (SA-9; SA-4; GV.SC-05; GV.SC-06; 164.308(b)(1)-(2); 164.314(a))

4.9 **New processing needs a privacy review.** Any new interface, data feed, or feature that moves personal information or PHI between divisions, to corporate, or to a vendor must have a privacy impact assessment approved by the Group Chief Privacy Officer (and, for PHI, by the owning privacy official) before go-live. (RA-8; PT-2; PT-3)

4.10 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01; 164.308(a)(8))

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1)

4.12 Security policies, procedures, risk analyses, assessments, and required actions must be retained for 6 years from creation or last effective date, whichever is later. Records with their own legal retention periods (Forms I-9, E-Verify documentation, payroll and tax records, Home Health clinical records) follow the group retention schedule. (SI-12; 164.316(b)(2)(i); 8 CFR 274a.2(b)(2); 42 CFR 484.110(c))

4.13 **AI systems.** No AI system that ranks, screens, or makes or supports decisions about candidates, workers, patients, or clients' patients may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, and quarterly access reviews.

## 6. Exceptions
Exceptions follow section 4.11.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); notification matrix (P08).
