# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Electric Utility, Gas Production, Engineering Services) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, regulatory changes, or Severity 1 incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, SR-6, CA-2, CA-5, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory links | NERC CIP-003-9 R1, R3, R4 (the Electric Utility's CIP policies are separate documents approved by the CIP Senior Manager; this policy does not replace them); CIP-013-2; SEC Reg S-K Item 106 |
| Division supplements | Electric Utility supplement (v2026); Gas Production supplement (v2023, re-issue due 2026-11-30); Engineering Services supplement (v2025). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects the safety and reliability of the grid and of field operations, the information of customers, royalty owners, clients, and the workforce, and the systems that hold it.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and interns); all IT and OT systems and data the group owns or operates; and systems operated for the group by vendors, cloud providers, and affiliates. It covers the Electric Utility's BES Cyber Systems, the Distribution Operations Platform, Gas Production field SCADA, client information held by Engineering Services (including CEII and BES Cyber System Information), and all other group information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber and operational risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls (SYS-G1, SYS-G2, SYS-G4 through the Group OT security director); co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks |
| Group General Counsel | Owns contracts, the notification matrix, and coordination of regulatory filings |
| Group Chief Privacy Officer | Owns classification and handling of personal information; state breach determinations |
| Group OT security director | Owns the group OT security standard and SYS-G4 |
| CIP Senior Manager (Electric Utility) | Accountable for the Electric Utility's NERC CIP compliance; approves CIP policies, plans, and self-reports |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks; act as division OT security owner where no other owner is named |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0. OT systems must also follow the group OT security standard, based on NIST SP 800-82 Rev. 3. The Electric Utility must maintain a NERC CIP program for its BES Cyber Systems that meets every applicable Reliability Standard. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. The Electric Utility must identify a CIP Senior Manager by name and document any change within 30 calendar days, and document any delegation of authority (CIP-003-9 R3, R4). Each division must name a security and compliance lead and an OT security owner in writing. (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. High risks to public or crew safety must be treated, not accepted. A potential noncompliance with a Reliability Standard cannot be accepted as a risk; it follows 4.13. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter or division-specific requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. (PL-2; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm. HR must document every sanction. (PS-8; GV.RR-04)

4.8 **Vendors and affiliates.** No vendor, cloud provider, or affiliate may access OT systems, CEII, or BES Cyber System Information without contract security terms (the group OT security schedule: incident notice, notice when access should end, vulnerability disclosure, software integrity, remote access coordination) and a risk assessment. **A division that provides services to another division is treated as a vendor of that division**, with the same terms and assessment as a third party. (SA-4; SA-9; SR-6; GV.SC-05; CIP-013-2 R1 Part 1.2 for medium impact systems)

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Assessors must not assess controls they designed or operate. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01)

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. No exception may create a potential noncompliance with a Reliability Standard or a client contract. (PL-1)

4.11 **Retention.** Security policies, risk analyses, assessments, and incident records must be retained for 6 years. NERC CIP evidence must be retained for at least three calendar years, or longer if the Compliance Enforcement Authority directs or a noncompliance is open. (SI-12)

4.12 **AI systems.** No AI system that supports grid operations, power purchasing, field operations, or client deliverables, or that processes Restricted or client information, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.13 **Regulatory compliance.** Any workforce member who finds a potential noncompliance with a Reliability Standard must report it to the Electric Utility NERC compliance director within 2 business days. The CIP Senior Manager decides on self-reports to the Regional Entity, and mitigation is tracked in the POA&M. (CA-5; GV.OC-03)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, quarterly CIP internal controls reviews, and division access reviews.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); the Electric Utility's CIP-003-9 policies and low impact plan; the CIP-013-2 supply chain plan.
