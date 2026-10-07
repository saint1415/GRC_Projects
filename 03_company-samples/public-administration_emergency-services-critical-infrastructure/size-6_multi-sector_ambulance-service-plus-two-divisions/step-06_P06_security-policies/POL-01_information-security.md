# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Ambulance Services, Urgent Care, Billing and Dispatch Services) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| HIPAA Security Rule | 164.308(a)(1), (a)(1)(ii)(A)-(C), (a)(2), (a)(8), (b)(1)-(2); 164.316 |
| Division supplements | Ambulance Services supplement (v2026); Urgent Care supplement (v2024, re-alignment due 2026-11-30); BDS supplement (v2025). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects patients, callers, and clients' information, and the dispatch and clinical systems that emergency response depends on.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, students, and volunteers), all systems and data the group owns or operates (including communications centers and vehicle systems), and systems operated for the group by business associates, subcontractors, and other service providers. It covers the ePHI of both covered-entity divisions, PHI that BDS and corporate hold as business associates for internal divisions and external clients, card data, and all other group information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); chairs the Group AI council; co-accepts High risks |
| Group Chief Privacy Officer | Owns data classification and minimum-necessary rules across divisions |
| Group General Counsel | Owns BAAs, client and county agreements, and the notification matrix |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Division HIPAA Security and Privacy Officers | Ambulance Services and Urgent Care each designate their own (45 CFR 164.308(a)(2)); BDS designates officials as a business associate |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that meets the HIPAA Security Rule for every covered entity and business associate in the group. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Each covered-entity division must designate its own HIPAA Security Official and Privacy Official in writing, and BDS must designate its own security and privacy officials. (PM-2; GV.RR-02; 164.308(a)(2))

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; 164.308(a)(1)(ii)(A)-(B))

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Risks rated High that could delay an emergency response or harm a patient must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02; 164.316(b)(2)(iii))

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems that holds ePHI or supports dispatch, including vehicle and communications center systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security or privacy policies must be sanctioned in proportion to intent and harm. Each covered entity's Privacy Officer and HR must document every sanction. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))

4.8 **No BAA, no PHI.** No vendor, subcontractor, or intercompany service provider may create, receive, maintain, or transmit PHI for a division without a business associate agreement (or subcontractor agreement) and a security review. BDS must not route an external client's PHI to a new subcontractor or a new feature of an existing subcontractor (for example, an AI service) until legal has checked the change against that client's BAA and contract. (SA-9; SA-4; GV.SC-05; 164.308(b)(1)-(2); 164.314(a))

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01; 164.308(a)(8))

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1)

4.11 Security policies, procedures, risk analyses, assessments, and required actions must be retained for 6 years from creation or last effective date, whichever is later. (SI-12; 164.316(b)(2)(i))

4.12 **AI systems.** No AI system that processes PHI or caller audio, or that makes or supports decisions about patients, callers, response priority, or claims, may be deployed, moved to a new mode (for example, from shadow to advisory), or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.13 **Data received from public safety partners.** Before any interface carries data from a law enforcement agency or PSAP beyond EMS incident data, the Group General Counsel and the BDS security and compliance lead must confirm whether the data is criminal justice information and, if so, that an agreement and the required controls are in place. (AC-21; CA-3; GV.OC-03)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, and division access reviews.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); HIPAA Security Rule, 45 CFR 164 Subpart C.
