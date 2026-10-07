# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Meat Processing, Food Distribution, Grocery Retail) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, CM-3, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory drivers | 21 CFR 121.130, 121.157 (Plant 6); 9 CFR 417.4(a)(3), 417.5 (all plants); 21 CFR 117.206 (DCs); PCI DSS Req. 12.1, 12.3, 12.8 (Grocery Retail); SEC Reg S-K Item 106 |
| Division supplements | Meat Processing supplement (v2025); Food Distribution standards (v2023, re-issue due 2026-12-31); Grocery Retail supplement (v2026). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects the food the group makes, moves, and sells, the people who eat it, and the customer, cardholder, and employee information the group holds.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, agency temporary workers, contractors), all IT and OT systems and data the group owns or operates (including plant control systems, DC automation, store systems, and the cold-chain platform), and systems operated for the group by service providers, integrators, and contractors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber and food safety risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G5; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group Chief Food Safety and Quality Officer | Decides product holds, recalls, and food regulator notices that cross divisions; approves food safety sign-off rules for OT changes |
| Group OT security director | Owns the group OT security standard, SYS-G5, and the OT reference architecture |
| Group General Counsel | Owns contracts, the notification matrix, and approval of external notices |
| Group Chief Privacy Officer | Owns data classification and personal information handling |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements, registers, and inheritance matrices; accept Low risks |
| Plant managers and plant FSQA managers | Sign HACCP plans (9 CFR 417.2(d)); at Plant 6, sign and maintain the food defense plan (21 CFR 121.310) |
| Grocery Retail payments security manager | Owns the PCI DSS program |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0, covering IT and OT, that supports each division's food safety, food defense, and payment card obligations. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. The Group OT security director leads OT security. Each division must name a security and compliance lead in writing. (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. Risk analyses for plants must feed the food defense vulnerability assessment where Part 121 applies. (RA-3; PM-9; ID.RA-01; 21 CFR 121.130)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Risks that could put adulterated product into commerce must be treated, not accepted, at High or Very High. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document which controls it inherits and which responsibilities remain with the division, and confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm, and HR must document every sanction. (PS-8; GV.RR-04)

4.8 **No security terms, no access.** No integrator, contractor, cloud or SaaS provider, or payment service provider may connect to group OT, hold group data, or handle cardholder data without written security terms and a security review proportionate to its access. Assurance (for example, a SOC 2 report or PCI DSS attestation) must be obtained and reviewed at least annually for critical suppliers. (SA-9; SA-4; GV.SC-05; PCI DSS Req. 12.8)

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01)

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1)

4.11 Security policies, risk analyses, assessments, and incident records must be retained for at least 6 years. Food safety records follow the longer of this period or the rule that requires them (for example, 9 CFR 417.5(e), 21 CFR 121.315, 21 CFR 1.912). (SI-12)

4.12 **AI systems.** No AI system that can affect food safety, critical infrastructure operations, or decisions about people may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.13 **OT changes and food safety.** Every change to a control system, recipe, or monitoring system that can affect product must pass change control with an FSQA sign-off that records the HACCP reassessment decision (9 CFR 417.4(a)(3)) and, at Plant 6, the food defense reanalysis decision (21 CFR 121.157(b)-(c)). (CM-3; GV.OC-03)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, the PCI DSS ROC, and FSQA verification records.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); Plant 6 food defense plan; plant HACCP plans.
