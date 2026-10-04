# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO (Qualified Individual) |
| Approved by | President and Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2023 policy; the WISP is now this policy set plus the standards index) |
| Review cycle | Annually (next review 2027-09-30), and after material changes, new campuses, new AI uses, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, CA-5, SA-4, SA-9, SR-6, SI-12, PT-3 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07 |
| Safeguards Rule and other rules | 16 CFR 314.3(a); 314.4(a), (b), (d)(1), (e)(2), (f), (g), (i); 34 CFR 99.31(a)(1)(i)(B); 34 CFR 668.16(c); HEA section 483 |
| Supporting standards | See `standards-index.md` (STD-01 to STD-11) |

## 1. Purpose
Establish the college's information security program (the written information security program required by 16 CFR 314.3(a)), assign accountability, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of student, financial aid, and college information, and supports safe campuses.

## 2. Scope
All employees (staff, full-time and adjunct faculty), student workers, contractors, and volunteers at Campuses 1-3, in the online division, and working remotely. It covers all systems and data, including systems that vendors, the third-party servicer, and the MSSP operate for the college, and any campus or program the college opens or acquires from the date it connects to college systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board of directors | Receives the Qualified Individual's written report at least annually (314.4(i)); approves the risk appetite |
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, and incidents |
| President and Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Information Officer | Executive sponsor and SILP system owner; senior member who directs and oversees the Qualified Individual (314.4(a)(2)); approves POL-02 to POL-05; accepts Moderate risks |
| vCISO (Qualified Individual) | Oversees, implements, and enforces the program (314.4(a)); owns this policy; writes the annual board report |
| Information Security Manager and security analysts | Security operations, vulnerability management, MSSP oversight, GRC and standards |
| Chief Compliance Officer | Title IV and FERPA compliance; breach determinations with counsel; vendor contract terms; fraud referrals |
| Registrar | FERPA compliance officer; education records data owner |
| Director of Financial Aid | Financial aid data owner; SAIG; third-party servicer oversight; FAFSA data use limits |
| Provost and Chief Academic Officer | Chairs the AI review group (P10) |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All employees | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The college must maintain a written information security program that meets the FTC Safeguards Rule, as applied to Title IV institutions, and FERPA's access and authentication requirements. It is documented in this policy set, the supporting standards, and the System Security Plan. (PM-1; GV.PO-01; 314.3(a))
4.2 The college must designate a Qualified Individual in writing and reaffirm the designation each year. Because the Qualified Individual is employed by a service provider, the college retains responsibility for compliance, the CIO directs and oversees the Qualified Individual in monthly documented meetings, and the provider's contract requires it to maintain an information security program that protects the college. (PM-2; GV.RR-02; 314.4(a)(1)-(3))
4.3 A written risk assessment must be performed at least annually and **whenever a material change occurs**, including a new campus, a new system that holds customer information or education records, and any new AI use. It must use NIST SP 800-30 Rev. 1 and meet 314.4(b)(1)(i)-(iii). Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01; 314.4(b))
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The CIO may accept Moderate risks. The President and CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks that could delay a Clery emergency notification or disable physical security may not be accepted above Low. (PM-9; GV.RM-01; 314.4(b)(1)(iii))
4.5 The Qualified Individual must report in writing to the board at least annually on the overall status of the program and compliance with 16 CFR Part 314, and on material matters: risk assessment, risk management and control decisions, service provider arrangements, testing results, security events and management's responses, and recommended changes. The vCISO also reports to the audit committee each quarter. (PM-9; GV.OV-01; 314.4(i))
4.6 Security policies must be reviewed at least annually and after material changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02; 314.4(g))
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. Exceptions to MFA or encryption also require the Qualified Individual's written approval of the compensating or equivalent controls (314.4(c)(3), (c)(5)). (PL-1)
4.8 **Sanctions.** Employees who fail to comply with security or FERPA policies must be sanctioned in proportion to intent and harm, from retraining to termination. HR and the Chief Compliance Officer must document each sanction. (PS-8; GV.RR-04)
4.9 **No contract, no student data.** Before any vendor receives, maintains, or processes customer information or education records, it must sign a contract with security safeguards, FERPA school-official terms (direct control, use only for the outsourced function, no redisclosure), incident notice within 72 hours, and return or deletion of data at the end of the contract, and pass a security review scaled to its tier. Purchasing and card holders must not buy such a service without the Chief Compliance Officer's approval. (SA-9; SA-4; GV.SC-05; 314.4(f)(1)-(2); 34 CFR 99.31(a)(1)(i)(B))
4.10 Tier 1 vendors (those holding customer information or education records at scale, with privileged access, or supporting a High-criticality process) must be reassessed each year, including a review of their SOC 2 report or equivalent (STD-03; P09). (SR-6; GV.SC-07; 314.4(f)(3))
4.11 Security controls must be independently assessed at least annually (P07) and after material changes, and the program adjusted for the results. (CA-2; CA-5; 314.4(d)(1); 314.4(g))
4.12 **FAFSA data use.** FAFSA and ISIR data, and anything derived from them, may be used only for the application, award, and administration of student aid, unless the Director of Financial Aid confirms in writing that another use is permitted. They must not be copied into the data warehouse, analytics, marketing, or AI models without that confirmation. (PT-3; HEA section 483)
4.13 AI tools that process customer information or education records, or that influence decisions about applicants or students, must be approved through the AI governance process before use (STD-05; P10). (PM-9; GV.RM-01)
4.14 Customer information must be disposed of under the retention and disposal standard (STD-11) no later than 2 years after its last use, unless a longer period is required by law (for example, 34 CFR 668.24) or needed for a documented business purpose. Security records (risk assessments, assessments, incident records, decision logs) are kept for 6 years. (SI-12; 314.4(c)(6))

## 5. Compliance and enforcement
Violations are handled under section 4.8. Compliance is checked through the annual independent assessment (P07), the annual Title IV compliance audit, semiannual access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); risk register and appetite statements (P01); gap analysis (P03); 16 CFR Part 314; 34 CFR Part 99; FSA Electronic Announcement GENERAL-23-09
