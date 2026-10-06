# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, new partner integrations, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PT-2, PL-1, PS-8, RA-1, RA-3, CA-2, CA-5, SA-4, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07 |
| Legal and contractual basis | FTC Act Section 5 (15 U.S.C. 45); Fla. Stat. 501.171(2), (6); PCI DSS v4.0.1 12.1 and 12.8 (SAQ P2PE); Manufacturer A agreement; Partner agreements |
| Supporting standards | See `standards-index.md` (STD-01 to STD-11) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects customer devices and the data on them while they are in the company's care, customer and partner claim records, payment activity, and company systems.

## 2. Scope
All workforce members (employees, managers, agency temporary staff, and contractors) at the 34 stores, the Depot, the contact center, and the corporate office. It covers all company systems and data, customer devices and recovered data in the company's custody, data the company processes for Partners P1 and P2, and systems that vendors operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and STPP system owner; approves POL-02 to POL-05; accepts Moderate risks |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| IT Director (Information Security Officer) | Runs the program day to day; owns the SSP and contingency planning |
| Security Manager, security analyst, and GRC Analyst | Security operations, MSSP oversight, vulnerability management, risk register, POA&M, vendor reviews, standards |
| General Counsel and Privacy and Compliance Manager | Breach determinations, privacy notices, retention, contract terms |
| Chief Financial Officer | Merchant agreement, SAQ attestations, cyber insurance, vendor contracts |
| Business unit leaders (Director of Retail Operations, Depot Director, Director of Partner Programs, Director of Customer Experience, Digital Engineering Manager) | Apply policies in their units; approve access; own downtime procedures and their standards |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program documented in this policy set, the supporting standards, and the System Security Plan, using NIST CSF 2.0 as its benchmark. (PM-1; PL-1; GV.PO-01)
4.2 The IT Director is the designated Information Security Officer. The designation must be in writing and reaffirmed each year. (PM-2; GV.RR-02; PCI DSS 12.1.3)
4.3 An enterprise risk assessment must be performed at least annually and after major changes (a new region, an acquisition, a new partner integration, or a new AI use), using NIST SP 800-30 Rev. 1. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. A risk of workforce access to customer device content beyond the repair need may not be accepted above Low once its controls are in place. (PM-9; GV.RM-01)
4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, incidents, and progress against the program roadmap. (GV.OV-01; CA-5)
4.6 Security policies must be reviewed at least annually and after major changes or incidents, and published to all workforce. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02; PCI DSS 12.1.1, 12.1.2)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.8 **Sanctions.** Workforce members who break security or privacy policies must be sanctioned in proportion to intent and harm, from retraining to termination. Viewing, copying, keeping, or sharing a customer's personal data without a repair need is serious misconduct and grounds for termination. HR and the business unit leader must document each sanction. (PS-8; GV.RR-04)
4.9 **No terms, no data.** Before any vendor receives, stores, or processes customer, claimant, or card-related data, or supports a High-criticality process, it must pass a security review scaled to its tier and sign terms covering security, data use (including no training of AI models on company data), retention and deletion, and breach notice to the company within 72 hours or less. Purchasing must not issue a purchase order to such a vendor without the GRC Analyst's approval. (SA-4; SA-9; GV.SC-05; Fla. Stat. 501.171(6); PCI DSS 12.8.1 to 12.8.3)
4.10 Tier 1 vendors (those with customer data at scale, payment functions, or support for a High-criticality process) must be reassessed each year, including a review of their SOC 2 report or PCI DSS attestation and the controls the company must run for them (STD-03; P09). (SR-6; GV.SC-07; PCI DSS 12.8.4)
4.11 **Data received as an agent.** Claim data received from protection plan partners may be used only to perform the repair and report outcomes. It must not be used for marketing or analytics beyond the partner's service. (PT-2; Partner agreements)
4.12 Security controls must be independently assessed at least annually (P07) and after major changes. (CA-2; ID.IM-01)
4.13 Security documentation (policies, risk assessments, control assessments, and risk decisions) must be kept for at least 3 years. Incident records and any written no-notice determination under Fla. Stat. 501.171(4)(c) must be kept for at least 5 years. (SI-12)
4.14 AI tools that process customer, claimant, applicant, or employee data, or that influence prices, repairs, or decisions about people, must be approved through the AI governance process before use (STD-05; P10). (PM-9; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in section 4.8. Compliance is checked through the annual independent assessment (P07), the quarterly access reviews (POL-02), the log reviews (POL-03), and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); Manufacturer A and B program agreements; Partner P1 and P2 agreements; merchant agreement
