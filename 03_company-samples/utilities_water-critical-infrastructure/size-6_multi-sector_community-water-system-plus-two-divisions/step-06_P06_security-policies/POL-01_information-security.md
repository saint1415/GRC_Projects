# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Water Utility, Infrastructure Construction, Environmental Services) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, SR-6, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory drivers | C-WATER-R01 (42 U.S.C. 300i-2(a)-(d)); N23-R03 (DFARS 252.204-7012(b)); N23-R04 (32 CFR 170.16, 170.22); N56-R07 (FAR 52.204-21); N56-R09 (49 CFR 172.802(b)); SEC Reg S-K Item 106 |
| Division supplements | Water Utility supplement (v2025); Construction supplement (v2023, re-alignment due 2026-11-30); Environmental Services supplement (first issue due 2026-11-30). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, covering business IT and operational technology (OT), assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects safe drinking water for about 3.37 million people, the covered defense information the group holds for DoD, its clients' compliance data, and the personal information of customers and employees.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and temporary staff); all systems and data the group owns or operates, including SCADA, PLCs, RTUs, and other OT at water plants, liquid waste facilities, and client sites; and systems operated for the group by suppliers, including other group divisions acting as suppliers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber and OT risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G4; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and the enterprise risk roll-up (NIST IR 8286 Rev. 1); co-accepts High risks |
| Group OT Security Director | Owns the group OT security standard and the OT remote access gateway (SYS-G4); approves OT exceptions |
| Group General Counsel | Owns intercompany and supplier agreements and the notification matrix |
| Division presidents | Accept Moderate risks; the Construction president is the CMMC Affirming Official |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Water Utility Emergency Management Director | Manages the RRA and ERP program for the 42 covered water systems |
| Environmental Services hazmat compliance manager | Maintains the hazardous materials security plan with the named senior official |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that covers IT and OT and meets the security obligations of every division's regulators and contracts. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Each division must name a security and compliance lead in writing. The Water Utility must name an RRA and ERP program manager; Construction must name its CMMC Affirming Official (32 CFR 170.22(a)(1)); Environmental Services must name, by job title, the senior official responsible for the hazardous materials security plan (49 CFR 172.802(b)(1)). (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. The cyber element of every covered water system's RRA must draw on that system's OT asset inventory and the Water Utility register, not on a generic checklist. (RA-3; PM-9; ID.RA-01; 42 U.S.C. 300i-2(a)(1)(A)(ii))

4.4 **Risk acceptance authority:** Very Low and Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Risks to public health or worker safety rated High must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter or division-specific requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm, through group HR. (PS-8; GV.RR-04)

4.8 **Suppliers, including sister divisions.** No supplier may access a division's OT, covered defense information, FCI, or client data without a written agreement that sets security requirements (incident notice to the asset owner, remote access rules, personnel screening, and return or destruction of data) and a security review. A division that provides services to another division is a supplier under this statement, and the intercompany contract must carry the same security terms. (SA-4; SA-9; SR-6; GV.SC-05)

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. No self-assessment may be submitted to a government system (for example SPRS) and no compliance affirmation may be made until group internal audit or counsel has reviewed its scope and evidence. (CA-2; CA-7; ID.IM-01; 32 CFR 170.16, 170.22)

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. Any exception that affects OT remote access or another division's systems also needs the Group OT Security Director's approval. (PL-1)

4.11 Security policies, procedures, risk analyses, assessments, and required actions must be retained for at least 6 years from creation or last effective date. Each RRA and ERP, including revisions, must be retained for at least 5 years after its certification to EPA (42 U.S.C. 300i-2(d)). (SI-12)

4.12 **AI systems.** No AI system that supports operational decisions (treatment, pumping, compliance data), client deliverables, or decisions about workers may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, and division access reviews.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); group OT security standard; RRAs and ERPs of the covered water systems.
