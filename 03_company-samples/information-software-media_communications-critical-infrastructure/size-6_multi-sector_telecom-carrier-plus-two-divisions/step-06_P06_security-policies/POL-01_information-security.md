# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Telecom Carrier, Network Engineering Services, Tower and Fiber Infrastructure) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee, 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory drivers | C-COMMUNICATIONS-R01 (47 CFR 64.2009(b), (e)); C-COMMUNICATIONS-R03 (47 CFR 1.20003(a)); C-COMMUNICATIONS-R06 (Reg S-K Item 106); N54-R04 (FAR 52.204-21(c)); 47 CFR 17.6 |
| Division supplements | Carrier (v2026); Engineering (v2026-03); Tower (v2023, re-issue due 2026-12-31). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects customers' CPNI and personal information, lawful-intercept information, the networks that carry 911 calls, the systems that monitor tower obstruction lighting, federal contract information, and landowners' and tenants' information.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and outsourced contact center agents), all systems and data the group owns or operates, including network elements and device fleets (SBCs, routers, OLTs, RMUs, smart locks), and systems operated for the group by vendors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group Chief Privacy Officer | Owns data classification and the rules for CPNI and personal information across divisions |
| Group General Counsel | Owns intercompany agreements and the notification matrix |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Carrier Senior Vice President, Regulatory and Compliance | CPNI compliance officer; signs the annual CPNI certifications |
| Carrier Vice President, Network Security and Lawful Intercept | CALEA senior officer for every Carrier operating company |
| Tower site operations director | Antenna structure lighting compliance |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that covers every division and corporate shared services. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. The Carrier must designate in writing a CPNI compliance officer and a CALEA senior officer for each operating company, and the Tower division must designate the owner of antenna structure lighting compliance. (PM-2; GV.RR-02; 47 CFR 1.20003(a); 47 CFR 17.6(a))

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services (including the service assurance platform), or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Risks to 911 call completion, tower obstruction lighting, or lawful-intercept confidentiality rated High must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. A division that hosts other divisions as tenants (such as the Carrier's service assurance platform) must have a written tenant agreement with each of them. (PL-2; CA-2; CA-3; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security or privacy policies must be sanctioned in proportion to intent and harm. The disciplinary process expressly covers misuse of CPNI, and HR must document every sanction. (PS-8; GV.RR-04; 47 CFR 64.2009(b))

4.8 **No agreement, no data.** No vendor, subcontractor, or affiliate may receive CPNI, customer or landowner personal information, lawful-intercept information, federal contract information, or customer network data without a written agreement (or intercompany agreement) with confidentiality, security, and incident notice terms (notice to the group within 24 hours), and a security review. Federal subcontracts must carry the FAR 52.204-21 flowdown when the subcontractor may hold FCI. (SA-9; SA-4; GV.SC-05; 47 CFR 64.2007(b); FAR 52.204-21(c))

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01)

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1)

4.11 **Retention.** Security policies, risk analyses, assessments, and incident records must be retained at least 6 years. Regulatory records must be kept at least as long as the rule requires: CPNI approval and notice records and campaign records 1 year, CPNI breach records 2 years, and antenna structure light outage records 2 years. (SI-12; 47 CFR 64.2007(a)(3); 64.2009(c); 64.2011(d); 17.49)

4.12 **AI systems.** No AI system that processes CPNI or personal information, takes account actions, or makes or supports decisions about customers, landowners, or network and structure safety may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.13 **Regulatory certifications.** Every signed regulatory certification or filing (the annual CPNI certification, CALEA SSI policies, and the covered equipment certification under 47 CFR 1.50007) must be supported by a documented evidence pack that the signing officer reviews, including open P07 findings. (CA-2; PM-1; GV.OV-01; 47 CFR 64.2009(e))

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, and division access reviews.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); 47 CFR 64.2001-64.2011.
