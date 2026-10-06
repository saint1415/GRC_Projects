# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CA-2(1), CM-7(5), CM-8, SA-9, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| Regulatory basis | PCI DSS v4.0.1 Requirements 12.1, 12.3, 12.4, 12.5, 12.8, 6.4.3 (N71-R04); FTC Act Section 5 and 16 CFR Part 464 (N71-R05); SEC Item 106 |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of patron, client, card, and company information, and supports the company's PCI DSS obligations as a merchant and a service provider, its FTC Act and fee rule obligations, and its SEC disclosure duties.

## 2. Scope
All Cris Santos Company workforce members (employees, part-time and seasonal event staff, contractors, and interns) at headquarters, all 36 venues in 8 states, the 3 festivals, and the two contact centers, including acquired venues from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, venue operational technology, and systems that service providers and other vendors operate for the company, and the services the company offers to business clients (SL-1 white-label ticketing and SL-2 venue management).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, PCI DSS validation status, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; the CFO holds executive responsibility for PCI DSS (Requirement 12.4.1); both take part in materiality determinations |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Director of Payments and PCI Compliance | PCI DSS program owner; scope, targeted risk analyses, QSA and acquirer liaison |
| Chief Privacy Officer | Privacy program; breach determinations |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 that meets PCI DSS v4.0.1 as a merchant and a service provider and other applicable requirements, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO must own the security program, the Director of Payments and PCI Compliance must own the PCI DSS program, and the CFO must hold executive responsibility for PCI DSS compliance, each designated in writing. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. Targeted risk analyses must be documented for every PCI DSS requirement that allows the company to set the frequency. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Safety and card data risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security or privacy policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor may store, process, or transmit card or patron data, or affect the security of a payment page, until it is tiered and assessed under STD-01.3 and has a contract with security terms and, for PCI DSS service providers, a responsibility matrix. Service provider PCI DSS status must be checked at least annually. (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation, and the merchant and service provider Reports on Compliance must be completed by a QSA each year. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence before closing and a funded integration plan that brings identity, network, logging, endpoint, and card acceptance controls to enterprise standards within 12 months of closing. Acquired card acceptance enters PCI DSS scope on the day of closing. (RA-3; SA-9; GV.OC-01)
4.11 Security documentation, including risk analyses, assessments, and required actions, must be retained for at least 3 years, or longer where law, contract, or a legal hold requires. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, PCI DSS validation status, and material incidents. (PM-9; GV.OV-01)
4.13 PCI DSS scope must be documented and confirmed at least annually and after significant change, and every 6 months for the service provider cardholder data environment. (CM-8; PL-2; ID.AM-03)
4.14 No script may run on any checkout or payment page, on the company's own brand or on a client template, unless it is inventoried, authorized, justified, and integrity-checked under STD-01.8, and every payment page must be monitored for unauthorized changes. (CM-7(5); SI-7; PR.PS-01)
4.15 Every ticket price the company offers, displays, or advertises, including on client templates it renders, must be the total price, shown more prominently than other pricing information, and changes to pricing or bot defense rules must go through change control with business owner approval (STD-01.9). (CM-3; PL-4; GV.OC-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard (including targeted risk analyses)
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Payment Page and Checkout Template Standard
- STD-01.9 Pricing and Fee Display Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 PCI DSS Scope Confirmation Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the QSA's Reports on Compliance, and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a safety or card data risk at High or above are refused unless a dated treatment plan exists. A PCI DSS requirement that cannot be met as written needs a compensating control that the QSA accepts; a policy exception alone does not change the Report on Compliance. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 TVOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
