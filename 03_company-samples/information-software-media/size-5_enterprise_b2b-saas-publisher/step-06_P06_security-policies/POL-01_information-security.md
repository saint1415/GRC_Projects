# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Cybersecurity and risk committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, SA-9, SI-12, PT-5 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| Regulatory drivers | FTC Act Section 5 (N51-R01); SEC Item 106 (N51-R08); CCPA cybersecurity audit (N51-R03); Fla. Stat. 501.171(2) |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of customer, consumer, and company information, keeps the company's security, privacy, and AI statements true, and supports its FTC, SEC, CCPA, FedRAMP, and contractual obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and vendor agents with company accounts) in every office and remote location, including acquired companies from their acquisition date. Covers all systems and data, including the Operations Cloud, Data Cloud, Government Edition, AQ-01, cloud accounts, SaaS, endpoints, and systems that sub-processors and other vendors operate for the company. Where the Government Edition's FedRAMP package sets a stricter requirement, the stricter requirement applies inside its boundary.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Cybersecurity and risk committee of the board | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106(c)(1)) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Chief Privacy Officer | Privacy program; DPA terms; CCPA cybersecurity audit certification |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO must be designated in writing as the executive accountable for the security program, and the Chief Privacy Officer as accountable for the privacy program. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Tenant isolation and regulatory risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security or privacy policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor may receive customer data until it is tiered, assessed under STD-01.3, contracted with security and service provider terms, and, for sub-processors, announced to customers with 30 days' notice. Vendors with access to customer data must be screened annually for access by countries of concern or covered persons (28 CFR Part 202). (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation; the CCPA cybersecurity audit must use an auditor that meets Cal. Code Regs. tit. 11, 7122. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence before closing and a funded integration plan that brings identity, cloud guardrails, logging, secrets, and data-use terms to enterprise standards within 12 months of closing. (RA-3; SA-9; GV.OC-01)
4.11 Security documentation, including risk analyses, assessments, and required actions, must be retained for at least 7 years. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity risk to the cybersecurity and risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OV-01)
4.13 Every public or contractual statement about security, privacy, or AI (trust page, DPA, product pages, questionnaire answers, system descriptions) must be reviewed against evidence before publication and every quarter by the Director of Trust and Assurance and the General Counsel's delegate; a statement that is not true must be corrected within 5 business days. (PT-5; PL-4; GV.OC-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party and Sub-processor Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Public Statement Review Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the quarterly public statement review. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a tenant isolation or regulatory risk at High or above are refused unless a dated treatment plan exists. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 OCP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
