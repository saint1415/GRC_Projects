# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-8, PS-8, RA-3, CA-2, CA-3, CA-5, SA-4, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, ID.IM-01 |
| CISA CPG 2.0 (voluntary baseline) | 1.A, 1.B, 1.D, 1.E, 2.C, 3.I, 3.P |
| Supporting standards | See `standards-index.md` (STD-01 to STD-11) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects tenants, visitors, employees, and the buildings themselves: the confidentiality of personal and business information, and the integrity and availability of the building systems that keep 14 properties secure, cooled, and occupied.

## 2. Scope
All employees, contractors, integrators, and other vendors who use or support company systems at the 14 properties and the corporate office. It covers IT systems, the building automation, access control, and video systems (OT), the cloud landing zone, SaaS services, and any property the company acquires, from the date it connects to company networks.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor; BAACS system owner; approves POL-02 to POL-05; accepts Moderate risks |
| vCISO | Owns this policy and the program strategy; reports to the audit committee; chairs the AI review group |
| IT Director (information security officer) | Runs the program day to day; owns network, cloud, and backup controls |
| Security Manager and security analysts | Security operations, vulnerability management, MSSP oversight, OT monitoring |
| GRC Analyst | Risk register, POA&M, policies and standards, evidence, vendor reviews |
| Vice President of Engineering and Building Technology Manager | Security of the building automation systems and integrator access |
| Director of Security Operations | Security of access control, video, visitor management, and the SCC |
| General Counsel | Breach determinations, contract security terms, lease notice obligations |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All employees and contractors | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program, documented in this policy set, the supporting standards, and the System Security Plan, that uses the CISA Cross-Sector Cybersecurity Performance Goals (CPG 2.0) as its baseline and NIST SP 800-82 Rev. 3 for operational technology. (PM-1; GV.PO-01; CPG 1.B)
4.2 The IT Director is the designated information security officer. The VP of Engineering and the Director of Security Operations are accountable for the security of the building systems they own. IT, engineering, and security operations must meet monthly on security. Designations must be in writing and reaffirmed each year. (PM-2; GV.RR-02; CPG 1.A)
4.3 An enterprise risk assessment must be performed at least annually and after major changes, including acquisitions, using NIST SP 800-30 Rev. 1. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks that could plausibly harm occupants may not be accepted above Low. (PM-9; GV.RM-01)
4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, incidents, and progress against the program roadmap. (GV.OV-01; CA-5)
4.6 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.8 **Vendor security terms.** Before any vendor receives system access, remote access to building systems, or company, tenant, visitor, or employee data, it must sign the security addendum in STD-05. At minimum the addendum requires: notice to the company within 72 hours of a suspected incident affecting company systems or data; named accounts and MFA; no standing remote access to OT; a named contact; and the company's right to review its controls. Purchasing must not issue a purchase order without the GRC Analyst's approval. (SA-4; SA-9; GV.SC-05; CPG 1.D, 1.E; Fla. Stat. 501.171(6))
4.9 Tier 1 vendors (those with privileged or remote access to building systems, personal information at scale, or support for a High-criticality process) must be reassessed each year, including a review of their SOC 2 report or equivalent (STD-05; P09). (SR-6; GV.SC-07)
4.10 **New AI and platform features.** No AI use case, and no new analytics, biometric, or automation feature in an existing platform, may be enabled until it is approved through the AI review process (STD-06; P10). Features that make or drive decisions about entry to a building, use biometric data, or write to building systems need COO approval after a full assessment. (PM-9; GV.RM-01; CPG 3.P)
4.11 Security controls must be independently assessed at least annually (P07), and the IT perimeter must be penetration-tested each year. OT must be assessed with passive methods unless the system owner approves active testing in writing. (CA-2; ID.IM-01; CPG 2.C)
4.12 **Life-safety separation.** Fire alarm, elevator, and emergency voice systems must stay on separate networks. Building automation may read life-safety status only through hardwired, read-only points, and egress door releases must stay hardwired to the fire alarm. No change may create a network path from any company system to a life-safety system. (PL-8; PR.IR-01; CPG 3.I)
4.13 **Acquisitions.** Before closing on a property, the security team must complete the due diligence checklist in STD-02 (OT inventory, remote access, vendor contracts). Acquired networks must stay isolated from company networks until assessed and brought to STD-02. (RA-3; CA-3)
4.14 Security policies, risk assessments, assessment results, incident records, breach decision logs, and any written no-harm determination must be retained for at least 5 years. (SI-12; Fla. Stat. 501.171(4)(c))
4.15 **Sanctions.** Employees and contractors who fail to comply with security policies must be sanctioned in proportion to intent and harm, from retraining to termination of employment or contract. HR and the General Counsel must document each sanction. (PS-8; GV.RR-04)

## 5. Compliance and enforcement
Violations are handled under section 4.15. Compliance is checked through the annual independent assessment (P07), quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); CISA CPG 2.0; NIST SP 800-82 Rev. 3; Fla. Stat. 501.171
