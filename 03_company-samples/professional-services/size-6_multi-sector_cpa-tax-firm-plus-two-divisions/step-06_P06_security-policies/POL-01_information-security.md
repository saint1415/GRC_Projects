# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (CPA and Tax Services, Wealth Management, Practice Management Software) and corporate shared services; adopted by Cris Santos CPA Partners, LLP under the administrative services agreement |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee; adopted by the Tax and Advisory board of managers, the Wealth board of managers, the Practice Cloud board, and the CPA Partners managing partner |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-6, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory basis | FTC Safeguards Rule 16 CFR 314.3 and 314.4(a), (b), (d), (f), (g), (i) (Tax and Advisory); 17 CFR 248.30(a) and 275.206(4)-7 (Wealth); 45 CFR 164.308 and 164.316 (CPA Partners as business associate); IRC 7216 |
| Division supplements | Tax and Advisory supplement (v2026); CPA Partners supplement (v2023, re-alignment due 2026-12-31); Wealth supplement (v2025); Practice Cloud supplement (v2025). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects taxpayers', clients', and customer firms' information and the systems that hold it. For Tax and Advisory, this policy with POL-02 to POL-05, the Tax and Advisory supplement, the TPCP system security plan, and the risk assessment form the written information security program required by 16 CFR 314.3(a).

## 2. Scope
All workforce members of the group and its divisions (employees, seasonal staff, contractors, and interns), the professionals leased to CPA Partners, all systems and data the group owns or operates, and systems operated for the group by service providers and affiliates. It covers tax return information, GLBA customer information, Wealth customer information, Practice Cloud customer data, PHI that CPA Partners holds as a business associate, and all other group information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls (SYS-G1 to SYS-G4); serves as Tax and Advisory's Qualified Individual (16 CFR 314.4(a)); co-accepts High risks |
| Tax division president | Senior member of Tax and Advisory who directs and oversees the Qualified Individual (314.4(a)(2)) |
| Tax and Advisory board of managers | Receives the Qualified Individual's annual written report (314.4(i)) |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group Chief Privacy Officer | Owns data classification, the purpose register, and the design of the IRC 7216 consent program |
| Chief Tax Officer | Owns the IRC 7216 consent process and the IRS e-file program for Tax and Advisory |
| Wealth Chief Compliance Officer | Administers Wealth's compliance program, Regulation S-P program, and Identity Theft Prevention Program |
| Practice Cloud CISO | Leads Practice Cloud security and its SOC 2 control environment |
| CPA Partners risk and quality partner | Security liaison for the attest practice; business associate duties |
| Group General Counsel | Owns intercompany agreements, customer contracts, and the notification matrix |
| Division presidents and the CPA Partners managing partner | Accept Moderate risks for their units |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that meets the FTC Safeguards Rule for Tax and Advisory, Regulation S-P and the Advisers Act compliance rule for Wealth, the HIPAA Security Rule for CPA Partners' business associate work, and Practice Cloud's customer commitments. (PM-1; GV.PO-01; 314.3(a); 248.30(a)(1))

4.2 The Group CISO is accountable for the program and is Tax and Advisory's Qualified Individual. Because the Group CISO is employed by the holding company, Tax and Advisory retains responsibility for its compliance, its board of managers names a senior member to direct and oversee the Qualified Individual, and the holding company must maintain a program that protects Tax and Advisory under Part 314. (PM-2; GV.RR-02; 314.4(a)(1)-(3))

4.3 Each division, CPA Partners, and corporate must complete a written risk assessment at least annually and after material changes, using NIST SP 800-30 Rev. 1 and the criteria in the P01 report. Risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; 314.4(b))

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president (for CPA Partners, its managing partner); High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Risks of direct financial loss to clients rated High must be treated, not accepted. (PM-9; GV.RM-01; 314.4(b)(1)(iii))

4.5 **Division supplements.** A division or CPA Partners may add stricter requirements in a written supplement. A supplement must not weaken group policy, must be re-aligned within 90 days after a group policy changes, and must be attested by the division security and compliance lead every year. (PL-1; GV.PO-02; 164.316(b)(2)(iii))

4.6 **Common controls and affiliates.** Corporate control providers must maintain the common control catalog. Each division and CPA Partners must document, for each system that holds regulated data, which controls it inherits and which remain its own, and confirm that every year. Every service one group entity provides to another that involves regulated data must be covered by a written intercompany agreement with security, notice, and (where applicable) Regulation S-P service provider and HIPAA subcontractor terms. (PL-2; PM-10; SA-4; 314.4(a)(3); 248.30(a)(5); 164.308(b)(2))

4.7 **IRC 7216.** No workforce member may disclose or use tax return information except as section 7216 and 26 CFR 301.7216-2 permit or as the taxpayer has consented in writing under 301.7216-3. Disclosure from Tax and Advisory to any other group entity, including Wealth, is a disclosure to a separate person and needs a permission or a compliant consent obtained before the disclosure. (PT-2; PT-4; GV.OC-03; 301.7216-2(c)(2); 301.7216-3)

4.8 **Sanctions.** Workforce members who violate security or privacy policies, including misuse of tax return information, must be sanctioned in proportion to intent and harm, and each sanction documented. (PS-8; GV.RR-04)

4.9 **Service providers.** No service provider may receive, maintain, process, or access regulated data without a security review before contract, contract terms requiring safeguards and incident notice, and periodic assessment based on risk (at least annually for tier 1). Contractors who maintain tax software or equipment must receive the written notice of IRC 6713 and 7216 before access. Practice Cloud must not add a sub-processor that handles customer data until legal has checked the change against customer contracts and SOC 2 commitments. (SA-9; SA-4; GV.SC-05; 314.4(f); 301.7216-2(d)(2); 248.30(a)(5))

4.10 **Evaluation and reporting.** Group internal audit must assess common controls at least annually and sample each division's controls. The Qualified Individual must report in writing to the Tax and Advisory board of managers at least annually on program status, compliance with Part 314, and material matters. (CA-2; CA-7; ID.IM-01; 314.4(d)(1), (g), (i))

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. An exception from MFA for Tax and Advisory systems also needs the Qualified Individual's written approval of equivalent controls. (PL-1; 314.4(c)(5))

4.12 Security policies, procedures, risk assessments, assessments, and incident records must be retained for at least 6 years, and longer where a division rule requires it. (SI-12; 164.316(b)(2)(i); 275.204-2)

4.13 **AI systems.** No AI system that processes tax return information, customer information, customer firms' data, or PHI, or that supports decisions about clients, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under 4.8. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, quarterly access reviews, and the Qualified Individual's annual report.

## 6. Exceptions
Exceptions follow section 4.11.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); 16 CFR Part 314; 26 CFR 301.7216-1 to -3; 17 CFR 248.30.
