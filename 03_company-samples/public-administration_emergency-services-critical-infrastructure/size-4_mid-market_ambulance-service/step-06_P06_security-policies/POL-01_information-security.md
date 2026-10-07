# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-16 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, significant incidents, or exercises |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, CA-2, CA-5, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07 |
| HIPAA Security Rule and other rules | 164.308(a)(1), (a)(1)(ii)(A)-(C), (a)(2), (a)(8), (b)(1); 164.314(a); 164.316 |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of patient, caller, and client information and keeps ambulances moving during an incident.

## 2. Scope
All workforce members (employees, contractors, students, and volunteers) at headquarters, both communications centers, 13 stations, and in all vehicles. It covers all systems and data, including systems that business associates and other vendors operate for the company, and the PHI the company handles as a business associate for its billing services clients.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, incidents, and SOC 2 progress |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and DPCP system owner; approves POL-02 to POL-05; accepts Moderate risks |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| Director of IT (HIPAA Security Officer) | Runs the program day to day (45 CFR 164.308(a)(2)); owns the SSP and contingency planning |
| Security Manager and security analysts | Security operations, vulnerability management, MSSP oversight, GRC and standards |
| Compliance and Privacy Officer | HIPAA Privacy Officer; breach determinations; BAAs in both directions; sanctions with HR |
| Medical Director | Clinical safety decisions for dispatch, downtime, and AI |
| Directors (Communications, Field Operations, Clinical Services, Revenue Cycle, Government Contracts) | Apply policies in their units; approve access; own downtime procedures |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program that meets the HIPAA Security Rule, both as a covered entity and as a business associate, and is documented in this policy set, the supporting standards, and the System Security Plan. (PM-1; GV.PO-01; 164.316(a))
4.2 The Director of IT is the designated HIPAA Security Officer. The designation must be in writing and reaffirmed each year. (PM-2; GV.RR-02; 164.308(a)(2))
4.3 An enterprise risk analysis must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01; 164.308(a)(1)(ii)(A)-(B))
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks that could delay an emergency response may not be accepted above Low. (PM-9; GV.RM-01; 164.308(a)(1)(ii)(B))
4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, incidents, SOC 2 readiness, and progress against the program roadmap. (CA-5; GV.OV-01; 164.308(a)(1))
4.6 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02; 164.316(b)(2)(iii))
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1; GV.PO-01; 164.316(a))
4.8 **Sanctions.** Workforce members who fail to comply with security or privacy policies must be sanctioned in proportion to intent and harm, from retraining to termination. The Compliance and Privacy Officer and HR must document each sanction. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))
4.9 **No BAA, no PHI.** Before any vendor creates, receives, maintains, or transmits PHI for the company, including client PHI held under the billing services BAAs, it must sign a business associate agreement, pass a security review scaled to its tier, and be approved by the Compliance and Privacy Officer. Purchasing must not issue a purchase order to such a vendor without that approval. Turning on a new feature that sends PHI to a vendor (for example an AI feature) counts as a new PHI flow. (SA-9; GV.SC-05; 164.308(b)(1); 164.314(a)(2)(iii))
4.10 Tier 1 vendors (those with PHI at scale, privileged access, or support for a High-criticality process) must be reassessed each year, including a review of their SOC 2 report or equivalent (STD-03; P09). (SR-6; GV.SC-07; 164.308(b)(1))
4.11 Security controls must be independently evaluated at least annually (P07) and after major changes. (CA-2; ID.IM-01; 164.308(a)(8))
4.12 Security policies, procedures, risk analyses, assessments, and incident records must be retained for 6 years from creation or last effective date, whichever is later. (SI-12; GV.PO-02; 164.316(b)(2)(i))
4.13 AI tools and AI features that process PHI or caller information, or that support dispatch, clinical, or billing decisions, must be approved through the AI governance gate before use (STD-05; P10). (PM-9; SA-9; GV.RM-01; 164.308(a)(1)(ii)(B))

## 5. Compliance and enforcement
Violations are handled under the HIPAA sanctions procedure (section 4.8). Compliance is checked through the annual independent assessment (P07), quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); HIPAA Security Rule, 45 CFR 164 Subpart C; client BAAs
