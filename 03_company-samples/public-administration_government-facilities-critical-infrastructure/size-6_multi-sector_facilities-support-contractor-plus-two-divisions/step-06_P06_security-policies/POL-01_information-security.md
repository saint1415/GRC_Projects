# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Government Facilities Support, Construction and Renovation, Janitorial and Security Services) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, SR-3, SR-5, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory drivers | State agency contract exhibits (SP 800-53 Rev. 5 Moderate); C-GOVERNMENT-R08 (GovRAMP); FAR 52.204-21(c), 52.204-25, 52.204-30; N23-R03 (DFARS 252.204-7012(m)); N23-R04 (32 CFR Part 170); N56-R01 to N56-R03 |
| Division supplements | Facilities Support (v2026); Construction (v2025, CUI standard due 2026-11-30); Janitorial and Security (2022 legacy set, re-issue due 2026-12-31). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects the buildings and people the group serves, the information customers and government agencies entrust to it, and the group's own workforce data.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its subsidiaries (employees, temporary staff, and contractors), all systems and information the group owns or operates, including the Integrated Building Operations Platform (IBOP) and the customer building systems it administers, and systems operated for the group by vendors, integrators, and subcontractors. Acquired businesses are in scope from the closing date.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program, group policies, and the common control catalog; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and the roll-up to enterprise risk management (NIST IR 8286 Rev. 1); chairs the Group AI council; co-accepts High risks |
| Group General Counsel | Owns customer and subcontract security terms, the notification matrix, and public records decisions |
| Group building technology director | System owner of the IBOP |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks; manage division regulators and customer security terms |
| Construction CUI program manager | Runs the DFARS 252.204-7012 and CMMC program for the Construction division |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0, using the NIST SP 800-53 Rev. 5 Moderate baseline as the group control set. Divisions with stricter customer or regulatory requirements (for example SP 800-171 for CUI) add them in their supplements. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Each division must name a security and compliance lead in writing, and the Construction division must also name a CUI program manager. (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Life-safety and physical-security risks rated High at a customer building must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems that holds customer, government, or workforce data, which controls it inherits and which responsibilities remain with the division, including in any system security plan it gives a customer or assessor (for example the Construction CMMC system security plan). Inheritance must be confirmed every year. (PL-2; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm, and HR must document every sanction. (PS-8; GV.RR-04)

4.8 **Third parties.** No vendor, integrator, or subcontractor may receive customer or government information, or access a customer building system, without a security review and contract terms that include: the security requirements of the customer contract, FAR 52.204-21(c) and DFARS 252.204-7012(m) flow-downs where they apply, incident notice to the group within 24 hours, and the right to audit. (SA-9; SA-4; GV.SC-05)

4.9 **Supply chain screening.** No division may buy, install, or use telecommunications or video surveillance equipment or services without screening against FAR 52.204-25, 52.204-23, and FASCSA orders (52.204-30). Acquired businesses must be brought into screening within 90 days of closing. (SR-3; SR-5; GV.SC-05)

4.10 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01)

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1)

4.12 Security policies, procedures, risk analyses, assessments, and incident records must be retained for 6 years, or longer where a contract or a public customer's records schedule requires. (SI-12; GV.PO-02)

4.13 **AI systems.** No AI system that controls building equipment or physical access, processes biometric, workforce, customer, or government data, or supports decisions about people may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.14 **Acquisitions.** An acquired business must adopt group policy, join group identity and monitoring, and retire remote access paths that bypass the group jump service within 180 days of closing. Until then, its risks are recorded in the acquiring division's register with an interim acceptance under 4.4. (PL-1; RA-3; GV.OC-03)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, and quarterly access certifications.

## 6. Exceptions
Exceptions follow section 4.11.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); NIST SP 800-53 Rev. 5 and SP 800-53B.
