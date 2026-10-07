# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (applies also to Cris Santos Assurance, LLP under the administrative services agreement) |
| Policy ID | POL-01 |
| Owner | Director of Information Security (Qualified Individual) |
| Approved by | Chief Executive Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after material changes, acquisitions, or security events |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, RA-3, CA-2, CA-5, CA-8, RA-5, SA-4, SA-9, SA-9(5), SR-6, PS-6, PS-7, PS-8, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-04, GV.OV-01, GV.OC-03, GV.SC-05, GV.SC-07 |
| FTC Safeguards Rule | 16 CFR 314.3(a); 314.4(a), (b), (d), (e)(2)-(4), (f), (g), (i) |
| Other | 26 CFR 301.7216-2(d)(2) and 301.7216-3(b)(4); 45 CFR 164.308(a)(1)-(2), 164.316; IRS Pubs. 4557 and 5708 |
| Supporting standards | STD-03 Vendor risk management; STD-05 AI use; STD-09 Vulnerability and patch management; STD-11 Offshore preparation program security (see `standards-index.md`) |

## 1. Purpose
Set up the Company's written information security program (WISP), assign who is accountable, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of client tax return information, customer information, ePHI held as a business associate, and Company information.

## 2. Scope
All workforce members of the Company and the Attest Firm (principals, partners, employees, seasonal staff, interns, and contractors), at every office and when working remotely. It covers all systems and data, including systems that service providers operate for the Company and the offshore preparation program. It applies to customer information (16 CFR 314.2(d)), tax return information (26 CFR 301.7216-1(b)(3)), ePHI, and all other Company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board of directors | Governing body; receives the Qualified Individual's written report at least annually |
| Audit committee | Quarterly cyber risk reporting; oversees the co-sourced internal audit firm |
| Chief Executive Officer | Approves this policy and the risk appetite; accepts High risks; oversees the Qualified Individual |
| Chief Operating Officer | Executive sponsor; approves the other policies and standards; accepts Moderate risks |
| Director of Information Security | **Qualified Individual** (16 CFR 314.4(a)) and HIPAA Security Officer; maintains the WISP, risk register, SSP, and POA&M |
| GRC Manager | Risk register, vendor reviews, policy register, evidence |
| General Counsel and Privacy Officer | IRC 7216 program, contracts, BAAs, breach determinations |
| Practice leaders and the Director of Tax Operations | Apply the program in their practices; own their systems' risks |
| All workforce | Follow these policies; report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The Company must maintain a written information security program made up of this policy set, the standards index, the System Security Plan (P02), the risk register (P01), and the incident response plan (POL-03 and P08). The Qualified Individual must keep an index of these parts where every workforce member can reach it. (PM-1; PL-2; GV.PO-01; 314.3(a))

4.2 The Director of Information Security is the Qualified Individual and the HIPAA Security Officer. The designation must be in writing and signed by the Chief Executive Officer. A deputy must be named in writing to act when the Qualified Individual is unavailable. (PM-2; GV.RR-02; 314.4(a); 164.308(a)(2))

4.3 A written risk assessment must be performed at least annually (each July) using NIST SP 800-30 Rev. 1. It must also be updated within 90 days after any material change, including an acquisition of another firm, an expansion of the offshore program, or the adoption of a new AI tool or feature that handles client data. It must state the criteria for rating risks, for assessing confidentiality, integrity, and availability, and for mitigating or accepting each risk. (RA-3; PM-9; 314.4(b); 164.308(a)(1)(ii)(A))

4.4 Risk acceptance authority: the risk owner may accept Low and Very Low risks; the Chief Operating Officer, Moderate; the Chief Executive Officer, High, temporarily and with a dated treatment plan. Very High risks may not be accepted, except for a 90-day exception after notice to the audit committee chair. The risk appetite statements in P01 bind every decision. (PM-9; GV.RM-04)

4.5 Security controls must be assessed at least annually by an assessor independent of their operation (the co-sourced internal audit firm). Unless continuous monitoring as defined in 314.2 is in place, an annual penetration test must be performed with a scope set from the risk assessment, and vulnerability assessments must be performed at least every six months, after every material change, and when circumstances may materially affect the program. (CA-2; CA-8; RA-5; ID.IM-02; 314.4(d))

4.6 The Qualified Individual must report in writing to the board at least annually on the program's overall status and compliance with 16 CFR Part 314, and on material matters: the risk assessment, risk decisions, service provider arrangements, test results, security events and management's responses, and recommended changes. A summary goes to the audit committee each quarter. (PM-9; GV.OV-01; 314.4(i))

4.7 Policies say what must happen; standards set measurable minimums; procedures say how. A standard may not weaken its parent policy. Policies and standards must be reviewed at least annually and after material changes, test results, or security events. (PL-1; GV.PO-02; 314.4(g))

4.8 Exceptions to any policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and limited to 12 months. An exception to encryption or MFA also needs the Qualified Individual's written approval of the compensating controls (314.4(c)(3) and (c)(5)). No exception may extend a legal notification deadline. (PL-1)

4.9 **New technology gate.** No new SaaS service, new AI tool, new AI feature in an existing tool, or new data flow of customer information may go live until it passes security and privacy review, including a documented IRC 7216 basis for any disclosure of tax return information (STD-05; P10). Purchasing and card spend may not pay for SaaS that has not passed the gate. (SA-4; SA-9; CM-3; 314.4(c)(4); 314.4(c)(7))

4.10 **Service providers.** Before a service provider receives customer information, tax return information, or ePHI, the GRC Manager must confirm it can protect the data and assign a tier under STD-03. The contract must require it to maintain safeguards, notify the Company of security events within the contract term (no later than 10 days for Florida personal information under Fla. Stat. 501.171(6)), and, for ePHI, sign a business associate agreement. Tier 1 providers are reviewed annually and Tier 2 every two years. (SA-9; SR-6; RA-3(1); GV.SC-05; GV.SC-07; 314.4(f); 164.308(b)(2))

4.11 **IRC 7216 notice to contractors.** Every contractor individual who may see tax return information while servicing the Company's software or equipment must receive written notice of 26 U.S.C. 6713 and 7216 before access, as 26 CFR 301.7216-2(d)(2) requires, and acknowledge it each year. (PS-6; SA-9)

4.12 **Offshore preparation program.** Tax return information may go to a preparer outside the United States only through the Company-hosted virtual desktops in U.S. regions, only after the taxpayer has signed the consent required by 26 CFR 301.7216-3, and only with SSNs of Form 1040 series filers redacted or masked in every document the offshore preparer can see, unless counsel has approved use of an IRS-defined adequate data protection safeguard (301.7216-3(b)(4)). The Director of Tax Operations owns the program under STD-11. (SA-9(5); PS-7; AC-21)

4.13 Program records (risk assessments, test results, incident records and decision logs, reports to the board, policy versions, and HIPAA-required documentation) must be kept for at least 6 years. (SI-12; 164.316(b)(2)(i))

4.14 **Sanctions.** Workforce members who break security or confidentiality rules must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR and the General Counsel document each sanction. Knowing or reckless misuse of tax return information is also a federal offense (26 U.S.C. 7216). (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))

4.15 The Company must employ or contract qualified security personnel sufficient to manage its risks, including filing-season surges, and must verify each year that they keep current on threats and countermeasures. (314.4(e)(2)-(4))

## 5. Compliance and enforcement
Violations are handled under 4.14. Compliance is checked through the annual independent assessment (P07), the access reviews in POL-02, vendor reviews (P09), and the Qualified Individual's annual report.

## 6. Exceptions
Exceptions follow 4.8.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); risk register (P01); 16 CFR Part 314; 26 CFR 301.7216-1 to -3; 45 CFR Part 164 Subpart C; IRS Pubs. 4557, 5708, and 1345
