# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Aircraft Parts, Engineering Services, Defense Software and Data Services) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board audit and risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, CMMC assessments, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, SR-3, SR-6, CA-2, CA-5, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, GV.SC-06, ID.RA-01, ID.IM-01 |
| SP 800-171 Rev. 2 | 3.11.1, 3.12.1 to 3.12.4 (policy basis for all families) |
| Division supplements | Aircraft Parts supplement (v2026); Engineering Services supplement (v2024, re-alignment due 2026-11-30); Defense Software supplement (v2025). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects the CUI, FCI, export-controlled data, and Government data the group holds for DoD, prime contractors, and customers, and the systems that hold it.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, interns, and consultants), all systems and data the group owns or operates, systems operated for the group by suppliers and service providers, and services one division provides to another. Classified systems at the cleared Engineering Services centers follow 32 CFR Part 117 and the DCSA authorizations; this policy applies to them only where it does not conflict.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit and risk committee | Oversees cyber risk; approves this policy; accepts Very High risks; receives internal audit results |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks |
| Group CMMC program director | Owns CMMC scopes, SSP set, SPRS submissions, and C3PAO and DIBCAC coordination |
| Group General Counsel | Owns contract flowdowns, the notification matrix, and disclosure support |
| Group export compliance director | Owns the ITAR and EAR program; supervises division Empowered Officials |
| Division presidents | Accept Moderate risks; serve as CMMC Affirming Officials for their CAGE codes (32 CFR 170.22) |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Group ITPSO and facility security officers | Insider threat program and NISPOM duties at cleared centers |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that implements NIST SP 800-171 Rev. 2 on every system that processes, stores, or transmits CUI, as DFARS 252.204-7012(b)(2) requires. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Each division president must designate in writing a division security and compliance lead and, for CMMC, accept the Affirming Official role for the division's CAGE codes. (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk assessment at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; 3.11.1)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board audit and risk committee; Very High, the board audit and risk committee only. High risks that could put a nonconforming part on an aircraft, or that involve unauthorized export of ITAR or EAR technical data, must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls and SSPs.** Corporate control providers must maintain the common control catalog. Every system that holds CUI must have an SSP (or an annex to one) that describes its boundary, environment, connections, and implementation, and that states which controls it inherits and which remain with the division. Inheritance must be confirmed every year and before any CMMC assessment. (PL-2; PM-10; CA-2; GV.RR-02; 3.12.4)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm. HR must document every sanction; cases involving CUI or export-controlled data must also go to the Group ITPSO and the Empowered Official. (PS-8; GV.RR-04)

4.8 **No flowdown, no CUI.** No supplier, subcontractor, consultant, or service provider may receive CUI until the contract includes DFARS 252.204-7012 (and 252.204-7021 where the prime contract requires CMMC) and the supplier's SPRS assessment and CMMC status have been checked at the level the work needs. (SA-4; SR-3; SR-6; GV.SC-05; GV.SC-06; 252.204-7012(m)(1); 252.204-7020(g)(2); 252.204-7021(f)(2))

4.9 **Intercompany services are external services.** When one division provides a service that holds another division's CUI, the providing division must meet the same requirements as an outside provider. A cloud service that holds CUI must meet the FedRAMP requirements in DFARS 252.204-7012 (security equivalent to the FedRAMP Moderate baseline and paragraphs (c) to (g)), and its customer responsibility matrix must be referenced in the user division's SSP. (SA-9; GV.SC-05; 252.204-7012(b)(2)(ii)(D); 32 CFR 170.19(c)(2))

4.10 **Evaluation.** Group internal audit must assess common controls at least annually against SP 800-171A objectives and sample each division's controls. Results feed the POA&M and the risk registers. A POA&M must be reviewed monthly; before a CMMC assessment it may hold only requirements that 32 CFR 170.21 permits. (CA-2; CA-5; CA-7; ID.IM-01; 3.12.1; 3.12.2)

4.11 **SPRS accuracy.** SP 800-171 assessment scores and CMMC affirmations must be submitted only after the Group CMMC program director confirms them against current evidence. The Affirming Official must not affirm a status the evidence does not support. (CA-5; GV.OV-01; 252.204-7019; 32 CFR 170.22)

4.12 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. Exceptions cannot waive a contract clause or a legal duty. (PL-1)

4.13 Security policies, procedures, risk assessments, assessments, and incident records must be retained for at least 6 years, and longer when a contract or DoD request requires. (SI-12)

4.14 **AI systems.** No AI system that processes CUI, export-controlled data, or Government data, or that supports decisions about people, aircraft maintenance, or product conformance, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.15 **Acquisitions.** An acquired site or business must stay isolated from group CUI systems until it passes a cyber due diligence review and an integration plan is approved by the Group CISO. CUI held at the acquired site remains subject to DFARS 252.204-7012 from day one. (CA-2; PL-2; GV.SC-05)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, and quarterly access certifications.

## 6. Exceptions
Exceptions follow section 4.12.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog and GCEE SSP (P02); group and division risk registers (P01); Group AI Standard (P10); DFARS 252.204-7012; 32 CFR Part 170.
