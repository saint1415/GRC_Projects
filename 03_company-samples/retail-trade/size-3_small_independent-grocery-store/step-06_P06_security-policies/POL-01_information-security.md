# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | General Manager |
| Approved by | General Manager |
| Effective date | 2026-09-04 (replaces the 2023 one-page "PCI policy") |
| Review cycle | Annually (next review 2027-09-04), and after major changes such as a new payment channel, or after incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CM-3, CM-7, CM-8, SI-7, SI-4, SA-9, SR-6, SI-12, PT-5 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.OV-01, GV.OC-03, GV.RM-01, GV.SC-05, GV.SC-07, ID.RA-01, ID.AM-03, PR.PS-01 |
| PCI DSS v4.0.1 (N44-45-R01) | 12.1, 12.3, 12.5, 12.8; 6.4.3, 6.5, 11.6.1 |
| Law (N44-45-R02) | FTC Act Section 5, 15 U.S.C. 45(a) and 45(n) |

## 1. Purpose
Set up the Cris Santos Company information security program, assign who is accountable, and give every other security policy its authority. The program protects customers' card data, loyalty and online account data, and the systems the store needs to sell and to keep food safe.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and temporary staff) and contractors with access to company systems, including the marketing contractor. Covers the store, online ordering, and all systems and data, including systems that service providers operate for the company (storefront, payment processor, POS vendor, cloud provider, pricing engine vendor). It applies to cardholder data wherever it could appear, customer and loyalty member data, workforce data, and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Majority owner | Approves the security budget; accepts High and Very High risks; signs the PCI DSS attestations after reviewing the evidence |
| General Manager | Program owner; approves policies; accepts Moderate risks |
| IT Manager (Information Security Lead) | Runs the program day to day; PCI DSS contact; maintains the risk register, SSP, and PCI scope document |
| Controller | Merchant agreement, acquirer contact, SAQ submissions, service provider contracts, cyber insurance |
| E-commerce and Marketing Manager | Storefront, checkout page, loyalty program, pricing engine; approves marketing and privacy claims with the IT Manager |
| Store Manager | PIN pad inspections, POS back office, physical security, contractor site access |
| All workforce and contractors | Follow these policies; report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The company must maintain an information security program documented in this policy set, the System Security Plan (P02), and the PCI DSS scope document. (PM-1; GV.PO-01; PCI DSS 12.1)
4.2 The IT Manager is the designated Information Security Lead and PCI DSS contact. The designation must be in writing and include the authority to stop a change that puts card data at risk. (PM-2; GV.RR-02; PCI DSS 12.1)
4.3 A risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Where PCI DSS lets the company set how often a control runs, the frequency must be set by a written targeted risk analysis. (RA-3; PM-9; ID.RA-01; PCI DSS 12.3)
4.4 Risk acceptance authority: the IT Manager may accept Low risks; the General Manager, Moderate; the majority owner, High and Very High. A High risk to card data or food safety may not be accepted without a dated treatment plan. (PM-9; GV.RM-01)
4.5 The PCI DSS scope (card data flows, in-scope components, the P2PE and embedded-form basis, and service providers) must be documented and confirmed at least every 12 months and before each SAQ is signed. **Every SAQ answer must be supported by evidence kept in the SAQ file, including the SAQ A eligibility criterion on script attacks.** (CA-2; PL-2; ID.AM-03; PCI DSS 12.5)
4.6 Security policies must be reviewed at least annually and updated after major changes or incidents. (PL-1; GV.PO-02; PCI DSS 12.1)
4.7 Exceptions to any security policy must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1; GV.RM-01)
4.8 **Service providers.** Before a service provider receives customer data, card data, or access that could affect the checkout page or store systems, the company must have a written agreement with security, data use, deletion, and incident notice terms. The Controller must keep a list of service providers and a matrix of which PCI DSS requirements each one manages, and must check each provider's AOC or SOC 2 report at least annually. (SA-9; SR-6; GV.SC-05; GV.SC-07; PCI DSS 12.8)
4.9 Security controls must be assessed at least annually (P07) and after major changes. (CA-2; ID.IM-02)
4.10 **Sanctions.** Workforce members and contractors who break security or privacy policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, termination, or contract termination. HR must document each sanction. (PS-8; GV.RR-04)
4.11 Security policies, risk assessments, SAQs and their evidence, and incident records must be kept for at least 3 years. (SI-12)
4.12 Privacy notices and marketing claims about security, data sharing, savings, and prices must be reviewed by the E-commerce and Marketing Manager and the IT Manager before publication, and must match actual practice. (PT-5; GV.OC-03; FTC Act 45(a))
4.13 **Changes to the checkout page.** Changes to the storefront theme, checkout template, tags, and installed apps must be requested, reviewed for security impact, approved by the E-commerce and Marketing Manager, and recorded before they go live. (CM-3; PR.PS-01; PCI DSS 6.5)
4.14 **Payment page scripts.** Every script that runs on the checkout page must be listed in an inventory with a written business reason, authorized by the E-commerce and Marketing Manager and the IT Manager, and protected by an integrity check. Changes to the page's scripts and security headers must be detected and alerted as the customer's browser receives them, at the frequency set by the targeted risk analysis. (CM-7; CM-8; SI-7; SI-4; PCI DSS 6.4.3; 11.6.1)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.10. Sanctions range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the quarterly access reviews (POL-02 4.6), and the PCI DSS self-assessment each year.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), recorded in the risk register, and expire within 12 months. No exception may allow card numbers to be entered or stored outside the P2PE devices and the processor's payment form.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); PCI DSS scope document (due 2026-11-30, P03 row G-060); service provider list and responsibility matrix (P03 row G-063); PCI DSS v4.0.1; FTC Act Section 5
