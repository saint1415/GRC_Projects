# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Freight Railroad, Transload and Wholesale, Railside Industrial Real Estate) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board safety, security, and risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, directive renewals, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| TSA and other | SD 1580/82-2022-01E II.A.2-3, II.B, III.F, VI; SD 1580-21-01E II.B, II.E; 49 CFR 1570.105, 1570.201; FAR 52.204-21; 17 CFR 229.106 |
| Division supplements | Freight Railroad supplement (v2026, aligned to the CIP); Transload and Wholesale supplement (v2026, first issue due 2026-12-31); Real Estate supplement (v2026, first issue due 2026-12-31). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects train movement, terminal and building operations, Sensitive Security Information (SSI), Federal Contract Information (FCI), and the personal information of employees, drivers, and guarantors.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its subsidiaries (employees, contractors, and temporary staff), all systems and data the group owns or operates, including operational technology (OT) in dispatch, signaling, PTC, terminals, and buildings, and systems operated for the group by vendors, managed service providers, and authorized representatives.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board safety, security, and risk committee | Oversees cyber risk; approves this policy and POL-03; accepts Very High risks |
| Board audit committee | Oversees group internal audit and disclosure controls |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G5; primary TSA Cybersecurity Coordinator for the Covered Railroads; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks |
| Group General Counsel | Owns intercompany agreements, the group notification matrix, and legal review of TSA-facing submissions |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Vice President, Rail Security | Primary TSA Security Coordinator for all 72 railroads; SSI program owner |
| Chief Audit Executive | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0, with NIST SP 800-82 Rev. 3 for OT, that meets the TSA directives for the Covered Railroads and the other binding rules in each division. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. TSA Security Coordinators (49 CFR 1570.201) and Cybersecurity Coordinators (SD 1580-21-01E II.B) must be designated in writing at the corporate level, with at least one U.S. citizen Cybersecurity Coordinator, and their details sent to TSA within the required times (37 calendar days and 7 days). (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board safety, security, and risk committee; Very High, the board committee only. Risks to train movement safety, hosted passenger trains, or hazmat loading rated High must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. Every division with OT (dispatch, signaling, terminals, or buildings) must have a supplement that sets its OT standards. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm, with HR documenting every sanction. (PS-8; GV.RR-04)

4.8 **Third parties.** No vendor, managed service provider, or authorized representative may access group systems or data without a contract with security terms and a risk-tiered review. Contracts for OT and PTC vendors must set patch certification timelines and incident notice terms. The group remains responsible for TSA directive measures delegated to a managed security service provider (SD 1580/82-2022-01E II.A.2). (SA-9; SA-4; GV.SC-05)

4.9 **Changes touching Critical Cyber Systems.** Any change that adds a system, interface, or capability connected to a Critical Cyber System must go through the Freight Railroad change board, which decides whether a CIP amendment request is required. A permanent change (45 days or more) requires a request within 50 days (SD 1580/82-2022-01E VI.B-D). This applies to corporate and other divisions, not only to the railroads. (PL-2; CA-3; GV.OC-03)

4.10 **Acquisitions.** Every acquisition must pass the security baseline gate in the integration playbook, and any rail acquisition, new RSSM traffic in an HTUA, or new hosting of passenger service must be assessed for TSA applicability at least 90 days before operations start (49 CFR 1570.105(b)). (RA-3; GV.OC-03)

4.11 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls, on a schedule that covers at least one-third of CIP measures each year and all of them over three years (SD 1580/82-2022-01E III.F.2.d). Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01)

4.12 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. An exception may not change a measure in the TSA-approved CIP without a CIP amendment. (PL-1)

4.13 Security policies, plans, risk analyses, assessments, and required actions must be retained for at least 6 years, or longer where a regulation or contract requires. (SI-12)

4.14 **AI systems.** No AI system that supports safety inspections, pricing, credit, employment, or lease decisions, or that processes SSI or personal information, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, and the TSA Cybersecurity Assessment Plan.

## 6. Exceptions
Exceptions follow section 4.12.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); the TSA-approved CIP and CAP (SSI, held by the Vice President, Rail Cybersecurity).
