# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Cris Santos Hydro, Cris Santos Constructors, Cris Santos Engineering) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board safety, risk, and reliability committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents. For Hydro, the CIP Senior Manager also reviews and approves the CIP policy topics at least every 15 calendar months (CIP-003-9 R1) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-7, PS-8, RA-3, SA-4, SA-9, CA-2, CA-3, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory drivers | C-DAMS-R01 (Security Program Rev. 3A 3.2; Table 9.3a coordination); C-DAMS-R03 (CIP-003-9 R1, R3, R4); N23-R03 and N23-R04 (DFARS 252.204-7012(b); SP 800-171 Rev. 2 3.12.4); SEC Reg S-K Item 106 |
| Division supplements | Hydro supplement (v2026); Constructors supplement (v2023, re-issue due 2026-11-30); Engineering supplement (v2025). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects the people who live below the group's dams, the reliability of the grid, the federal and client information the group holds, and the systems that hold it.

## 2. Scope
All workforce members of the group (employees, craft workers, contractors, and temporary staff), all systems and data the group owns or operates (IT and OT), and systems operated for the group by vendors and service providers. **Affiliates count as service providers to each other:** when one division provides a service to, or works inside the systems of, another division, the receiving division's vendor rules apply in full.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board safety, risk, and reliability committee | Oversees cyber and physical security risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Chief Compliance Officer | Second-line compliance across divisions (NERC, FERC dam security, federal contracts) |
| General Counsel | Owns intercompany agreements and the multi-regulator notification matrix; chairs the disclosure committee |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Senior Vice President, Hydro Operations | CIP Senior Manager (CIP-003-9 R3); approves CIP policy topics and delegations |
| Director, Hydro Security | FERC primary security contact for the Hydro fleet |
| Federal Programs Compliance Director | DFARS and CMMC compliance; CMMC Affirming Official |
| Group internal audit | Independently assesses common controls once and samples division controls |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0, using NIST SP 800-82 Rev. 3 for OT, that meets each division's regulatory and contractual obligations. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Hydro must keep a named CIP Senior Manager and a documented delegation process (CIP-003-9 R3, R4) and a FERC primary security contact with alternates (Security Program Rev. 3A 3.2). Constructors must keep a CMMC Affirming Official (32 CFR 170.22). (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board safety, risk, and reliability committee; Very High, that committee only. High risks to public safety (uncontrolled release of water, missed dam safety anomalies) and potential NERC noncompliance must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. Where a supplement conflicts with group policy, group policy governs. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which remain with the division, and confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm. HR must document every sanction. (PS-8; GV.RR-04)

4.8 **Affiliates are vendors.** No division may connect to, operate, or change another division's systems, or receive its BCSI, CEII, or CUI, without a written intercompany agreement that states the security terms. When Constructors or Engineering staff or devices work in Hydro OT, every Hydro vendor control applies: vendor remote access through the Intermediate Systems, transient device review, escort, training, and change approval. (SA-9; PS-7; CA-3; GV.SC-05; C-DAMS-R03 CIP-003-9 Att. 1 Sec. 5.2 and 6)

4.9 **Third parties.** Every vendor and service provider with system or data access must be tiered, assessed before access, and reassessed on its tier's cycle. Contracts for OT products and services must include the CIP-013 plan terms for Hydro's medium impact systems, and contracts involving covered defense information must flow down DFARS 252.204-7012. (SA-4; SA-9; GV.SC-05)

4.10 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. Regulator-facing statements (FERC certification letters, SPRS postings and CMMC affirmations, SEC disclosures) must be reviewed against evidence by a second person before submission. (CA-2; CA-7; ID.IM-01; GV.OV-01)

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. No exception may waive a regulatory requirement. (PL-1)

4.12 Security policies, plans, risk analyses, assessments, and required actions must be retained for at least 6 years, or longer where a regulation or contract requires (for example NERC evidence retention). (SI-12)

4.13 **AI systems.** No AI system that supports dam safety, grid operations, safety of workers or the public, or decisions about people may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, CIP compliance monitoring by the NERC Compliance Director, and CMMC assessments.

## 6. Exceptions
Exceptions follow section 4.11.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); FERC Security Program Rev. 3A; NERC CIP-003-9; DFARS 252.204-7012.
