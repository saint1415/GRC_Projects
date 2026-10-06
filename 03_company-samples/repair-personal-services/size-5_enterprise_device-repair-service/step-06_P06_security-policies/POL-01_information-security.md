# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk and technology committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, SA-9, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| Other requirements | PCI DSS v4.0.1 12.1, 12.4, 12.8; HIPAA 164.308(a)(1), (a)(2), (b)(1) and 164.316 for SL-2 |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of customer, card, client, and company information, and the devices customers leave in the company's custody, and supports the company's FTC Act, state law, PCI DSS, SEC, CCPA, manufacturer, and client obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at all 1,120 stores, the three depots, the data recovery lab, the contact center, and headquarters, including the acquired chain from its acquisition date. Covers all systems and data, including cloud, colocation, SaaS, store technology, customer devices in custody, and the services the company offers to clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Risk and technology committee of the board | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, PCI DSS status, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations; the CFO signs the PCI DSS AOC |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Director of Security Operations | Runs the SOC; incident commander; HIPAA security official for SL-2 (45 CFR 164.308(a)(2)) |
| Chief Privacy Officer | Privacy program; breach determinations with counsel |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 that meets PCI DSS, applicable state and federal law, SEC disclosure rules, and contractual requirements, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO must be designated in writing as security program owner, the Director of Security Operations as HIPAA security official for SL-2, and the Chief Privacy Officer as privacy program owner. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Risks to customer data or card data (ER-02, ER-03) at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security or privacy policies must be sanctioned under PRC-01.1 in proportion to intent and harm. A substantiated case of accessing or copying customer device content without a repair need leads to termination and to manufacturer notice where a program agreement requires it. (PS-8; GV.RR-04)
4.8 No vendor may receive customer, card, or client data until it is tiered and assessed under STD-01.3 and its contract includes security requirements, breach notice to the company within 10 days or less, and data-use terms (including no model training on company data). Third-party service providers with PCI DSS responsibilities must provide an AOC and a responsibility matrix every year. (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation, and the PCI DSS scope must be assessed annually by a QSA. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence before closing and a funded integration plan that brings identity, network, logging, endpoint, and payment controls to company standards within 12 months of closing. An acquired business that takes cards must have interim card data controls (segmentation, EDR, unique credentials) within 90 days of closing. (RA-3; SA-9; GV.RM-03)
4.11 Security documentation, including risk analyses, assessments, exceptions, and incident records, must be retained for at least 6 years from creation or last effective date, whichever is later. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity risk to the risk and technology committee at least quarterly, including Very High and High risks, risks outside tolerance, PCI DSS status, and significant incidents. (PM-9; GV.OV-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration, Network, and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Acquisition Integration Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, access certifications, the annual Internal Audit assessment (P07), and the annual PCI DSS ROC. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method (Tables G-5 and I-2), approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a risk to customer data or card data (ER-02, ER-03) at High or above are refused unless a dated treatment plan exists. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 STPP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
