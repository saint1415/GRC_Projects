# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Gas Transmission, Gathering and Production, Integrity Services) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee, 2026-09-22 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after a major change, an acquisition, a TSA directive revision, or a Severity 1 incident |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-2(1), CA-7, CM-3, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory drivers | C-ENERGY-R02 (SD 01G II.B); C-ENERGY-R03 (SD 02G II.A.3, II.A.4, II.B, III.G, VI); C-ENERGY-R04 (192.631(f)); N55-R01 (Reg S-K Item 106) |
| Division supplements | Gas Transmission supplement (v2026); Gathering and Production supplement (v2023, re-issue due 2026-11-30); Integrity Services supplement (v2025, SSI annex due 2026-12-31). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects pipeline and field operations, the people who live and work along our pipelines, the information clients and regulators entrust to us, and the business services the pipelines depend on.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and authorized representatives), all IT and OT systems and data the group owns or operates, and systems operated for the group by service providers. It covers Sensitive Security Information (SSI), critical energy infrastructure information (CEII), client data, royalty owner and employee personal information, and all other group information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy, POL-03, and the Group AI Standard; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group OT Security Director | Owns OT security architecture, the OT remote access gateway, and OT monitoring for all divisions |
| Group Chief Risk Officer | Owns the group risk register and the ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group General Counsel | Owns intercompany and client agreements, the notification matrix, and regulator notices |
| Director of Pipeline Cybersecurity (Gas Transmission) | Primary TSA Cybersecurity Coordinator; owns the TSA Cybersecurity Implementation Plan and Cybersecurity Assessment Plan |
| Division presidents | Accept Moderate risks; Gas Transmission president retains responsibility for TSA plan measures that corporate performs |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Group internal audit | Independently assesses common controls once a year and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0, with NIST SP 800-82 Rev. 3 as the guide for OT. For every pipeline system TSA has designated as critical, the program must meet the TSA security directives and the TSA-approved plans. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Every division that TSA designates must name a primary and at least one alternate Cybersecurity Coordinator at the corporate level, at least one of them a U.S. citizen eligible for a security clearance, available to TSA and CISA 24 hours a day, and must keep their contact details current with TSA within 7 days of a change. (PM-2; GV.RR-02; SD 01G II.B)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Very Low and Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Pipeline safety and environmental risks rated High must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter or regulator-specific requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. For a TSA-designated division the inheritance record is part of the implementation plan, because corporate performs plan measures but the division retains sole responsibility for them. (PL-2; PM-10; CA-2; GV.RR-02; SD 02G II.A.3)

4.7 **TSA plan discipline.** No measure in a TSA-approved implementation plan may be changed, delayed, or replaced without the Cybersecurity Coordinator's approval. Any slip against a plan schedule must be reported to the Coordinator within 5 business days. Any permanent change (one intended to last 45 or more calendar days) requires an amendment request filed with TSA no later than 50 calendar days after the change takes effect. If a division cannot implement an SD 01G measure in the required timeframe, the Coordinator must notify TSA immediately. (PL-2; CA-5; SD 02G II.B.2, VI.B to VI.D; SD 01G III.C)

4.8 **Operational change control.** Any change to SCADA, station or field control logic, displays, alarm setpoints, OT network rules, or analytics shown to controllers (including AI model releases and threshold changes) must go through the division's control room management of change, with control room participation in planning before the change is made. (CM-3; PR.PS-01; 192.631(f))

4.9 **Evaluation and independence.** Group internal audit must assess common controls at least annually and sample each division's controls. The cybersecurity architecture design review required by a TSA assessment plan must be performed by a reviewer independent of the group; the Integrity Services OT Assessment Practice must not assess another group division. (CA-2; CA-2(1); CA-7; ID.IM-01; SD 02G III.G.2.b)

4.10 **Third parties and authorized representatives.** No vendor, integrator, or service provider may access group OT or Restricted information without security terms and a security review. Where a third party performs measures under a TSA directive for a group division, or where Integrity Services performs measures for a client, the contract must name the measures, the evidence to be kept, and SSI handling, because both parties are liable for an authorized representative's non-compliance. (SA-4; SA-9; GV.SC-05; SD 02G II.A.4)

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. An exception may not change a TSA-approved measure without 4.7. (PL-1)

4.12 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm, and HR must document every sanction. (PS-8; GV.RR-04)

4.13 **AI systems.** No AI system that informs controllers, field staff, integrity decisions, or client deliverables, or that processes Restricted information, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.14 Security policies, plans, assessments, and records needed to show compliance with TSA directives must be retained for at least 3 years and kept available for TSA inspection, with SSI protected under POL-04. (SI-12; SD 02G IV.C)

## 5. Compliance and enforcement
Violations are handled under 4.12. Compliance is checked through the annual common control assessment and division samples (P07), the TSA Cybersecurity Assessment Plan, annual supplement attestations, and quarterly access certifications.

## 6. Exceptions
Exceptions follow section 4.11.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); regulation-by-division matrix (P03); Group AI Standard (P10); TSA implementation, incident response, and assessment plans (SSI, held by the Director of Pipeline Cybersecurity).
