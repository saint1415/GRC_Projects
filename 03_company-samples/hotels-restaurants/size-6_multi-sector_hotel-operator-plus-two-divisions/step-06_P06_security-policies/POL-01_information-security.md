# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Hotels, Attractions and Entertainment, Resort Real Estate and Vacation Ownership, including Cris Santos Vacation Finance, LLC) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee (2026-09-10); adopted by the finance subsidiary board for its information security program (16 CFR 314.3(a)) the same day |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory drivers | PCI DSS v4.0.1 Requirements 12.1, 12.3, 12.4, 12.8, 12.9 (N72-R01, N71-R04, N53-R04); 16 CFR 314.3-314.4 (N53-R01); 16 CFR 312.8(b) (N71-R06); 15 U.S.C. 45(a) (N72-R02); Reg S-K Item 106 (N53-R05) |
| Division supplements | Hotels supplement (v2026); Attractions supplement (v2025, update due 2026-12-31); Vacation Ownership supplement (re-issue due 2026-11-30, replacing the division's 2023 standards). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects guests', visitors', children's, owners', and borrowers' information, card data, and the systems that run hotels, parks, rides, and resorts.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, seasonal staff, contractors, and staff of managed hotels employed by the group), all systems and data the group owns or operates, systems the Hotels division operates for owners of managed hotels, and systems operated for the group by service providers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Board audit committee | Oversees group internal audit and the assessment program |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G4; co-accepts High risks; executive responsible for the Hotels service provider PCI DSS program (Requirement 12.4.1) |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); chairs the Group AI council; co-accepts High risks |
| Group Chief Privacy Officer | Owns data classification, purpose rules for SYS-G5, and retention |
| Group General Counsel | Owns management agreements, intercompany agreements, and the notification matrix; chairs the disclosure committee |
| Group Director of Payments and PCI Compliance | Runs one PCI DSS program across three merchant validations and the Hotels service provider validation |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Qualified Individual (Vacation Ownership security and compliance lead) | Oversees, implements, and enforces the finance subsidiary's program (16 CFR 314.4(a)); reports in writing at least annually to the finance subsidiary board (314.4(i)) |
| Finance subsidiary president | Senior officer who directs and oversees the Qualified Individual, who is employed by an affiliate (314.4(a)(2)) |
| Attractions digital products director | Coordinates the children's information security program (16 CFR 312.8(b)(1)) |
| Group internal audit | Independently assesses common controls once and samples division controls |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0. It must meet PCI DSS v4.0.1 for each merchant and service provider validation, the FTC Safeguards Rule for the finance subsidiary, and the COPPA Rule for the kids' club, and must provide reasonable security under FTC Act Section 5 and state law. (PM-1; GV.PO-01; N72-R01 Req 12.1; N53-R01 314.3(a))

4.2 The Group CISO is accountable for the program. The finance subsidiary board must designate a Qualified Individual in writing, and Attractions must designate in writing the employee who coordinates the children's information security program. (PM-2; GV.RR-02; 314.4(a); 312.8(b)(1))

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. The analysis must also meet PCI DSS Requirement 12.3 (including targeted risk analyses), 16 CFR 314.4(b), and 16 CFR 312.8(b)(2). (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Safety risks to guests, visitors, or riders and known card data exposures rated High must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. An acquired business must adopt group policy, or a supplement aligned to it, within 6 months of closing. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year and at each migration milestone. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm. HR must document every sanction. (PS-8; GV.RR-04)

4.8 **Service providers and written assurances.** No service provider may store, process, or transmit card data, customer information, children's information, biometric data, or guest profiles for the group until it has passed a risk-based security review and signed contract terms that require safeguards and incident notice to the group. Before any provider collects or receives children's information, Attractions must also obtain written assurances (312.8(c)). Each provider must be reassessed on a schedule set by its risk tier, and at least annually for providers holding card data or customer information. (SA-9; SA-4; GV.SC-05; Req 12.8; 314.4(f))

4.9 **Managed hotel owners.** For each managed hotel, the Hotels division must give the owner a written acknowledgment of its responsibility for the account data it handles and a responsibility matrix showing which PCI DSS requirements the division meets and which the owner meets. Management agreements must assign security responsibilities and incident notice duties. (SA-9; GV.SC-05; Req 12.9.1, 12.9.2; N72-R02)

4.10 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. The Qualified Individual must use the results in the annual report to the finance subsidiary board. (CA-2; CA-7; ID.IM-01; 314.4(d)(1), (g), (i))

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. An exception from MFA for the finance subsidiary requires the Qualified Individual's written approval of a reasonably equivalent control (314.4(c)(5)); an exception from encryption of customer information requires the Qualified Individual's approval of compensating controls (314.4(c)(3)). (PL-1)

4.12 Security policies, risk analyses, assessments, and required actions must be retained for at least 3 years after they are superseded, and longer where a division supplement or law requires. (SI-12)

4.13 **AI systems.** No AI system that sets prices, talks to guests, makes or supports decisions about credit, employment, or access, or processes Restricted data may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), PCI DSS validations, the annual supplement attestations, and quarterly access reviews.

## 6. Exceptions
Exceptions follow section 4.11.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); regulatory gap analyses (P03); Group AI Standard (P10).
