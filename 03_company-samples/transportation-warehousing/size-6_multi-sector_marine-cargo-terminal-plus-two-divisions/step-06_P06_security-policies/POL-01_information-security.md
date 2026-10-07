# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Marine Terminals, Freight Trading, Port Real Estate) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory drivers | N48-49-R01 (33 CFR 101.620, 101.625, 101.630, 101.640, 101.650(e)-(f)); N42-R02 and N42-R04 (32 CFR 170.15, 170.19, 170.22; FAR 52.204-21); N48-49-R08 (Reg S-K Item 106); 46 U.S.C. 41106(2) |
| Division supplements | Marine Terminals supplement MT-S1 (v2026); Freight Trading supplement FT-S1 (v2025, updated 2026-09); Port Real Estate supplement RE-S1 (v2023, re-alignment due 2026-12-31). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects the terminals' operations and the safety of the people who work in them, customers' cargo data, the group's federal contract information, tenants' information, and the systems that hold them.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors and temporary staff), registered longshore workers and vendor technicians whenever they use group IT or OT, all systems and data the group owns or operates (including crane, yard equipment and building OT), and systems operated for the group by service providers and integrators.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G4; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); chairs the Group AI council; co-accepts High risks |
| Group General Counsel | Owns intercompany agreements, the affiliate data-sharing standard and the notification matrix |
| Division presidents | Accept Moderate risks for their divisions; approve division supplements |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Division Cybersecurity Officer (Marine Terminals) | Subpart F duties for all 9 facilities (33 CFR 101.625) |
| Facility Security Officers | Facility security under each FSP; physical security of OT and related IT |
| Freight Trading federal contracts compliance manager | CMMC scope, SPRS entries and DoD clause compliance |
| Group internal audit | Independently assesses common controls once and samples division controls; audits Cybersecurity Plans independently (101.630(f)(4)) |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that meets the cybersecurity obligations of each division, including Subpart F at every regulated facility and the security clauses in the group's federal contracts. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Each division must name a security and compliance lead. Marine Terminals must designate in writing a Cybersecurity Officer for every facility, and an alternate with 24x7 contact details for each facility. (PM-2; GV.RR-02; 101.620(b)(3); 101.625)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services or need a group decision must roll up to the group register. For Marine Terminals the analysis must feed each facility's Cybersecurity Assessment. (RA-3; PM-9; ID.RA-01; 101.650(e)(1))

4.4 **Risk acceptance authority:** Very Low and Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Safety risks (crane, ASC and hazardous cargo) rated High must be treated, not accepted. A Subpart F vulnerability left unresolved by risk acceptance must be documented in the Cybersecurity Plan (101.630(c)(12)). (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter or division-specific requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its critical systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Affiliate separation.** No division may receive another division's customers' confidential data, or preferential treatment through group systems, unless the Group General Counsel has approved it under the affiliate data-sharing standard. In particular, Freight Trading is a cargo owner like any other at the group's terminals: its users may see only their own shipments, and terminal appointment rules must apply equally to all truckers. (AC-21; GV.OC-03; 46 U.S.C. 41106(2))

4.8 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm. For longshore workers and vendor technicians, the group may withdraw system access and refer the matter to the hiring hall or the vendor. (PS-8; GV.RR-04)

4.9 **Third parties.** No vendor, integrator or service provider may connect to group IT or OT, or handle confidential or regulated data, without a security review, contract terms that require it to notify the group of vulnerabilities and incidents without delay, and remote access only through the group jump host. Cybersecurity capability must be an evaluation criterion in every IT and OT procurement. (SA-4; SA-9; GV.SC-05; 101.650(f)(1)-(3))

4.10 **Federal contract information.** Any system that processes, stores or transmits FCI must be inside the CMMC Level 1 assessment scope before it is used for that purpose. CUI may be accepted only into an environment approved by the Group CISO as meeting NIST SP 800-171; until one exists, Freight Trading must decline or quarantine CUI. (PL-2; CA-2; 32 CFR 170.19(b); 252.204-7012(b)(2))

4.11 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. Auditors of a Cybersecurity Plan must not have regular cybersecurity duties at that facility. (CA-2; CA-7; ID.IM-01; 101.630(f)(4))

4.12 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. Where a Subpart F measure is not feasible, the compensating control must be documented for the Cybersecurity Plan. (PL-1)

4.13 Security policies, procedures, risk analyses, assessments and required actions must be retained for at least 6 years; Subpart F and facility security records for at least 2 years under 33 CFR 105.225; CMMC assessment artifacts for 6 years from the status date. (SI-12; 101.640; 32 CFR 170.15(c)(2))

4.14 **AI systems.** No AI system that makes or supports operational, safety, commercial or legal decisions, or that processes confidential or regulated data, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). An AI system that can move equipment needs a safety case. (RA-3; PL-2; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under 4.8. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, each facility's Cybersecurity Plan audit, and the annual CMMC Level 1 self-assessment.

## 6. Exceptions
Exceptions follow section 4.12.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); 33 CFR Part 101 Subpart F; 32 CFR Part 170; FAR 52.204-21; DFARS 252.204-7012.
