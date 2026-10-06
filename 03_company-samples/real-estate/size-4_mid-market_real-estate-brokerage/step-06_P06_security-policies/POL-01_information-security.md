# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and Cris Santos Title and Closing, LLC |
| Policy ID | POL-01 |
| Owner | Security Manager (Qualified Individual) |
| Approved by | Chief Executive Officer (noted by the board audit committee); adopted for Title and Closing by its board of managers |
| Approval date | 2026-09-29 |
| Effective date | 2026-10-15 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-14, PL-1, PS-8, RA-3, CA-2, CA-5, CA-8, RA-5, AT-2, AT-3, SA-9, SR-6, SA-15, CM-3, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, PR.AT-01, PR.PS-06 |
| FTC Safeguards Rule (N53-R01) | 16 CFR 314.3; 314.4(a), (a)(1)-(3), (b), (c)(4), (c)(7), (d), (e), (f), (g), (i) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-11) |

## 1. Purpose
Establish one information security program for Cris Santos Company, Inc. and its subsidiary Cris Santos Title and Closing, LLC ("Title and Closing"), assign accountability, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of customer, client, tenant, and company information, and above all the integrity of the instructions that move client money.

## 2. Scope
- All employees of both entities.
- All licensed sales associates affiliated with the company as independent contractors ("contractor agents") when they use company systems or handle company client information.
- All systems and data, including systems that service providers operate for the company, and any business acquired by the company from the date it connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports and the Qualified Individual's annual report |
| Title and Closing board of managers | Governing body of the financial institution under 16 CFR 314.4(i); receives the annual written report |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and TMCC system owner; approves POL-02 to POL-05; accepts Moderate risks |
| President, Title and Closing | Senior member who directs and oversees the Qualified Individual for Title and Closing (314.4(a)(2)); co-signs risk decisions that affect its customer information |
| Security Manager (Qualified Individual) | Oversees, implements, and enforces the program (314.4(a)); owns this policy and the SSP |
| vCISO | Program strategy; supports board reporting; security reviewer for AI use cases |
| IT Director | Infrastructure, cloud, recovery, and the technical side of access management |
| General Counsel | Contracts, notification decisions, retention schedule, RESPA and fair housing compliance |
| Broker of Record and managing brokers | Supervise contractor agents and enforce agent obligations under the agent agreement |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All employees and contractor agents | Follow the policies and report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The company must maintain one written information security program for both entities that meets the FTC Safeguards Rule. It is documented in this policy set, the supporting standards, and the System Security Plan. (PM-1; GV.PO-01; 314.3(a))

4.2 **Qualified Individual.** The Qualified Individual must be designated in writing by the CEO and by Title and Closing's board of managers, and reaffirmed each year. Because the Qualified Individual is employed by the parent, an affiliate of Title and Closing, Title and Closing retains responsibility for compliance, and its President directs and oversees the Qualified Individual, meeting at least quarterly with minutes. (PM-2; GV.RR-02; 314.4(a), (a)(1)-(2))

4.3 **Intercompany protection.** The intercompany services agreement must require the parent to maintain an information security program that protects Title and Closing in accordance with 16 CFR Part 314, to report on it annually, to give notice of security events, and to allow audit. (SA-9; GV.SC-05; 314.4(a)(3))

4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan; for risks to Title and Closing's customer information, the President of Title and Closing must co-sign. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. No risk of diverting client funds may be accepted above Moderate. (PM-9; GV.RM-01; 314.4(b)(1)(iii))

4.5 An enterprise risk assessment must be written and performed at least annually and after major changes (including acquisitions, new affiliates, and new lines of business), using NIST SP 800-30 Rev. 1. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01; 314.4(b), (b)(2), (g))

4.6 **Annual report.** The Qualified Individual must report in writing at least annually to Title and Closing's board of managers and to the audit committee on the overall status of the program and compliance with 16 CFR Part 314, and on material matters: risk assessment, risk management and control decisions, service provider arrangements, testing results, security events and management's responses, and recommended changes. The vCISO and the Qualified Individual must also report to the audit committee each quarter. (PM-9; GV.OV-01; 314.4(i), (i)(1)-(2))

4.7 Security policies must be reviewed at least annually and after major changes or incidents. Exceptions must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1; GV.PO-02)

4.8 **Sanctions.** Employees who violate security policies are sanctioned in proportion to intent and harm, from retraining to termination, through HR. Contractor agents are sanctioned by the Broker of Record under the agent agreement, up to loss of system access and termination of affiliation. (PS-8; GV.RR-04)

4.9 **Service providers.** No service provider may receive, maintain, process, or access customer information until it has passed a security review scaled to its tier and signed a contract that requires it to implement and maintain appropriate safeguards and to give notice of breaches. Tier 1 service providers must be reassessed each year (STD-03; P09). (SA-9; SR-6; GV.SC-05; GV.SC-07; 314.4(f)(1)-(3))

4.10 **Training.** Employees must complete security awareness training at hire and each year, plus quarterly phishing simulations. Contractor agents must complete annual training as a condition of system access and are included in phishing simulations. Staff who prepare, verify, or release payments must complete role-based payment fraud training each year. Training content must be updated from the risk assessment. (AT-2; AT-3; PR.AT-01; PR.AT-02; 314.4(e)(1))

4.11 **Testing.** Security controls must be independently assessed at least annually (P07). Unless the Qualified Individual documents effective continuous monitoring, the company must perform penetration testing at least annually, scoped each year from the risk assessment, and vulnerability assessments at least every six months, after material changes to operations or business arrangements, and whenever circumstances may materially affect the program. (CA-2; CA-8; RA-5; ID.IM-02; 314.4(d)(1)-(2))

4.12 Security policies, risk assessments, assessment results, and incident records must be retained for at least 5 years. (SI-12)

4.13 **In-house applications and change.** Applications the company owns that transmit, access, or store customer information (today the Closing Communications Portal) must follow the secure development standard (STD-04), whoever writes the code. Changes to production systems and to SaaS security settings must follow change management with a recorded approval. (SA-15; CM-3; PR.PS-06; 314.4(c)(4), (c)(7))

4.14 AI tools that process customer or consumer information, or that support decisions about housing, access to brokerage services, or closings, must be approved through the AI governance process before use (STD-11; P10). (PM-9; GV.RM-01)

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), quarterly access reviews, the payee verification sample tests in STD-05, and the metrics reported to the audit committee and the board of managers.

## 6. Exceptions
Exceptions follow section 4.7. The Qualified Individual will not approve a written equivalent to MFA for any user group under 16 CFR 314.4(c)(5) without notice to the President of Title and Closing and the COO.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); gap analysis (P03); 16 CFR Part 314; Fla. Stat. 475.25, 626.8473, 501.171
