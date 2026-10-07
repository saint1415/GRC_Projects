# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Transformer Manufacturing, Electric Utility, Grid Engineering) and corporate shared services |
| Policy ID | POL-01 |
| Version | v2026.1 (v2026 approved 2026-03-24; revised after the 2026 risk, gap, and control assessments) |
| Owner | Group CISO |
| Approved by | Board risk committee, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, SR-1, SR-5, CA-2, CA-3, CA-7, CM-3, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-02, GV.SC-05, ID.RA-01, ID.IM-01, PR.PS-01 |
| Regulatory and contract drivers | NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary benchmark); N22-R01 NERC CIP-003-9 (Electric Utility); Utility Supplier Cyber Security Addenda (CIP-013-2 R1 Part 1.2 flow-down); N54-R04 FAR 52.204-21; C-CRITICAL-MFG-R03 EAR (15 CFR 762.6); Regulation S-K Item 106 |
| Division supplements | Transformer Manufacturing (v2026, P8 and AI sections added in this revision); Electric Utility (v2026, maps group policy to the CIP program); Grid Engineering (2023 standards, **drifted**, re-issue due 2026-12-31). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects the group's ability to build safe grid equipment, keep the lights on for the Electric Utility's customers, deliver engineering work its clients trust, and meet its duties to customers, regulators, and investors.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and temporary staff); all systems and data the group owns or operates, including plant operational technology (OT), the TMU product and the Fleet Monitoring Service, and the Electric Utility's control centers and substations; and systems operated for the group by suppliers and cloud providers. Where the Electric Utility's NERC CIP program sets a stricter or more specific rule for a BES Cyber System, the CIP program governs for that system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber and operational risk (Reg S-K Item 106(c)(1)); approves this policy and POL-03; accepts Very High risks |
| Board audit committee | Oversees group internal audit and disclosure controls |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group General Counsel | Owns intercompany agreements, the customer security terms register, and the notification matrix |
| Group OT security director | Owns the group OT security standard and OT monitoring for plants and the utility |
| Electric Utility CIP Senior Manager | The senior vice president of transmission and distribution operations, designated under CIP-003-9 R3. Approves CIP policies and CIP exceptions. Group roles support, but never override, CIP Senior Manager decisions |
| Chief product security officer (Manufacturing) | Owns TMU product security, firmware signing, and the PSIRT |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks; attest supplement alignment every year |
| Group internal audit | Independently assesses common controls once and samples division controls (P07) |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0, using NIST SP 800-82 Rev. 3 for OT, that also meets every binding duty in the regulation-by-division matrix (P03): NERC CIP for the Electric Utility, customer and client contract terms, FAR clauses, EAR recordkeeping, and SEC disclosure. (PM-1; GV.PO-01; GV.OC-03)

4.2 The Group CISO is accountable for the program. The Electric Utility must keep a CIP Senior Manager designated in writing, and changes to that designation must be documented within 30 days as CIP-003-9 R3 requires. (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Very Low and Low, the division security and compliance lead; Moderate, the division president, with a treatment plan or a documented reason; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee, temporary only and with a dated plan; Very High, the board risk committee only. Risks rated High that could harm workers, crews, or the public (plant process safety, unsafe units on the grid, prolonged outages) must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter or division-specific requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog (P02). Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. The Electric Utility may use group controls as CIP evidence only for systems outside its Electronic Security Perimeters. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm, and HR must document every sanction. (PS-8; GV.RR-04)

4.8 **Suppliers, customers, and affiliates.**
- No supplier may receive system access, company data, or product components until it passes the group supplier review and its contract carries the group security terms. (SR-5; SA-4; SA-9; GV.SC-05)
- When one division supplies products or services to another, the intercompany agreement must carry a security schedule at least as strong as the one a third-party vendor would sign. Where the Electric Utility is the buyer, the schedule must cover the CIP-013-2 R1 Part 1.2 topics. (SR-1; SA-4; GV.SC-05)
- Every security term the group accepts from customers and clients (utility addenda, client CIP flow-down terms, FAR clauses, SOC 2 commitments) must be recorded in the customer security terms register, with its deadline, its contact, and an owner. (SA-4; GV.SC-02; GV.OC-03)

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Where the assessor helped design a control (for example, the group OT standard), the test must be co-sourced with an independent party. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01)

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. No exception may waive a NERC CIP requirement, a contract term, or a legal duty. CIP exceptions follow the Electric Utility's CIP exception process, approved by the CIP Senior Manager. (PL-1)

4.11 Security policies, procedures, risk analyses, assessments, and required actions must be kept for the period in the group retention schedule, which is never less than 3 years. Longer periods apply where a NERC standard, contract, or law requires them (for example, export records for 5 years under 15 CFR 762.6(a)). (SI-12)

4.12 **AI systems.** No AI model that steers production, allocation of storm-reserve slots or spare units, maintenance of plant equipment, grid operations, or engineering deliverables may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; CM-3; GV.RM-01)

4.13 **Operational technology safety.** A security change to plant control systems or Electric Utility operational systems must not reduce process or public safety. OT changes must follow the site's management-of-change process and need approval from plant or operations engineering as well as security. (CM-3; PR.PS-01)

4.14 **Acquisitions.** An acquired site must stay isolated from group networks until it passes a security integration review: a covered telecommunications equipment check (FAR 52.204-25), an asset inventory, removal of directory trusts, and a dated integration plan approved within 90 days of closing. A site already connected when this policy takes effect (P8) must meet the plan dates in the POA&M. (CA-3; SA-9; GV.SC-04)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, quarterly access certifications, and the Electric Utility's CIP internal controls.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); regulation-by-division matrix (P03); notification matrix (P08); Group AI Standard (P10); group OT security standard; Electric Utility CIP-003-9 cyber security policies.
