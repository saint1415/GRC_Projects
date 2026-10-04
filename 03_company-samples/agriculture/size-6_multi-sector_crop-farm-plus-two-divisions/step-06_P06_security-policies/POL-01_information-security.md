# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Crop Farming, Food Processing, Farm Supply) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, RA-3, PM-9, PL-1, PL-2, CA-2, SA-4, SA-9, SR-6, CP-12, SI-17, CM-3, CA-7, SI-12, PS-8 |
| CSF 2.0 | GV.PO-01, GV.RR-02, ID.RA-01, GV.RM-01, GV.PO-02, GV.SC-06, GV.SC-05, PR.PS-01, ID.IM-01, PR.DS-11, GV.RR-04 |
| Division supplements | Crop Farming supplement (v2026-09, OT and seasonal workforce added); Food Processing supplement (v2026); Farm Supply supplement (v2025, portal change gate added 2026-09). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, covering IT and operational technology (OT), assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects the people, crops, food, and information the group is responsible for: workers and H-2A workers, consumers of packed product, growers and cooperatives, and the systems that run farms, plants, and branches.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, seasonal and H-2A workers, contractors, and integrators acting for the group), all IT and OT systems and data the group owns or operates (including irrigation, fertigation, plant process, refrigeration, and blending controls), and systems operated for the group by vendors and service providers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies, IT and OT; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks |
| Group Chief Privacy Officer; Group General Counsel | Personal information handling; contracts; the notification matrix |
| Group VP Food Safety and Quality | Group food safety and food defense standards, including cyber scenarios in food defense |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Division OT security managers (Crop Farming, Food Processing) | OT architecture, OT access, OT change control, and OT monitoring with the SOC |
| Group internal audit | Independently assesses common controls once and samples division controls, with an independent OT assessment firm |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents and unexpected equipment behavior immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that covers IT and OT in every division, with NIST SP 800-82 Rev. 3 as the OT guide. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Crop Farming and Food Processing must each name an OT security manager in writing. (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, including OT. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Worker-safety and food-safety risks rated High must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy, must be re-aligned within 90 days after a group policy changes, and must be attested by the division security and compliance lead every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems including OT, which controls it inherits and which responsibilities remain with the division, and confirm that documentation every year. (PL-2; CA-2; GV.RR-02)

4.7 **Acquisitions.** Any acquired farm, plant, or business must have an OT and IT security review before closing and must meet group remote access, identity, and monitoring requirements within 180 days after closing, or hold an approved exception. (RA-3; SA-4; GV.SC-06)

4.8 **Suppliers and integrators.** No vendor, integrator, or contractor may access group systems or OT, or handle Restricted data, without a contract that includes the group security schedule (named personnel, MFA, access only through group PAM, incident notice within 24 hours, return of programs and data at exit) and a risk-tiered security review. (SA-4; SA-9; SR-6; GV.SC-05)

4.9 **OT safety first.** Security measures on OT must not stop safety functions. Every OT system must have a documented safe state and manual operating procedure, and changes to safety interlocks, fertigation limits, or refrigeration controls require OT change control and, where a PSM process is involved, management of change. (CP-12; SI-17; CM-3; PR.PS-01)

4.10 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division, including OT, using an independent OT assessment firm where needed. (CA-2; CA-7; ID.IM-01)

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1; GV.PO-01)

4.12 Security policies, procedures, risk analyses, assessments, and incident records must be retained for at least 6 years. (SI-12; PR.DS-11)

4.13 **AI systems.** No AI system that supports decisions about people, controls physical equipment, feeds financial reporting, or is offered to customers may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; CM-3; GV.RM-01)

4.14 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm, with HR documenting each sanction. (PS-8; GV.RR-04)

## 5. Compliance and enforcement
Compliance is checked through the annual common control assessment and division samples (P07), quarterly access certifications, the annual supplement attestations, and OT change reviews. Violations are handled under POL-01 4.14.

## 6. Exceptions
Exceptions follow POL-01 4.11. OT exceptions also need the division OT security manager's written safety reasoning.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10).
