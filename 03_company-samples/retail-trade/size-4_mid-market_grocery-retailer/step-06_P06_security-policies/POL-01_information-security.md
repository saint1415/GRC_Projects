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
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CA-5, CM-8, SA-9, SR-6, SI-12, PT-5 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, ID.AM-03 |
| PCI DSS v4.0.1 | Requirements 12.1, 12.3, 12.5, 12.8 (N44-45-R01) |
| Other rules | FTC Act Section 5, 15 U.S.C. 45(a), (n) (N44-45-R02); Fla. Stat. 501.171(2) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects payment card data, customer and loyalty data, supplier data, and the systems that keep the stores, the distribution center, and online ordering running.

## 2. Scope
All workforce members (employees, temporary staff, and contractors) at the 5 stores, the distribution center, and the support center. It covers all systems and data, including systems that third-party service providers and other vendors operate for the company, and any store acquired by the company from the date it connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk and PCI DSS compliance; receives quarterly reports on top risks, POA&M status, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and EPP system owner; approves POL-02 to POL-05; accepts Moderate risks |
| Chief Financial Officer | Owns the merchant agreement and acquirer relationship; signs the PCI DSS attestation of compliance |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| IT Director | Information security officer and PCI DSS program owner; runs the program day to day |
| Security Manager and security analysts | Security operations, vulnerability management, MSSP oversight, GRC, standards, and TPSP tracking |
| General Counsel and Privacy and Compliance Manager | Privacy notice, data sharing reviews, claims review, breach determinations, vendor contract terms |
| Business leaders (Director of E-commerce and Marketing, Director of Store Operations, Distribution Center Director, Director of Fresh Departments) | Apply policies in their units; approve access; own downtime procedures and the checkout page content |
| Co-sourced internal audit and the QSA firm | Independent assessments (P07; annual PCI DSS assessment) |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program documented in this policy set, the supporting standards, and the System Security Plan. (PM-1; GV.PO-01; PCI DSS 12.1)
4.2 The IT Director is the designated information security officer and PCI DSS program owner. The Chief Financial Officer signs the PCI DSS attestation of compliance after reviewing the QSA's findings. Both designations must be in writing and reaffirmed each year. (PM-2; GV.RR-02; PCI DSS 12.1.3)
4.3 An enterprise risk assessment must be performed at least annually and after major changes (including acquisitions and payment technology changes), using NIST SP 800-30 Rev. 1. Targeted risk analyses must be documented for every PCI DSS requirement that lets the company set its own frequency. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01; PCI DSS 12.3)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks of card data compromise or of unsafe food reaching customers may not be accepted above Low once treatment is complete. (PM-9; GV.RM-01)
4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, PCI DSS validation status, incidents, and progress against the program roadmap. (GV.OV-01; CA-5)
4.6 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02; PCI DSS 12.1.2)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. No exception may waive a PCI DSS requirement without a documented compensating control reviewed by the QSA. (PL-1)
4.8 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm, from retraining to termination. HR must document each sanction. (PS-8; GV.RR-04)
4.9 **PCI DSS scope.** The IT Director must keep a PCI DSS scope document, data flow diagrams, and an inventory of in-scope system components, and must confirm scope at least every 12 months and after any significant change, such as a new payment channel, a system move, or a store acquisition. (PL-2; CM-8; ID.AM-03; PCI DSS 12.5)
4.10 **Third-party service providers and vendors.** No third party may store, process, or transmit card data, or affect the security of the CDE, without a written agreement that acknowledges its PCI DSS responsibilities, a current AOC, and an entry in the responsibility matrix. No vendor may receive customer or loyalty data without contract terms on security, permitted use, breach notice, and deletion. The Privacy and Compliance Manager must check each TPSP's compliance status at least annually. Purchasing must not issue a purchase order to such a vendor without that approval. (SA-9; SR-6; GV.SC-05; GV.SC-07; PCI DSS 12.8)
4.11 Security controls must be independently evaluated at least annually (P07) and after major changes. The firm that assesses PCI DSS compliance must not be the firm that performs the internal control assessment. (CA-2)
4.12 Security policies, risk assessments, assessments, scope documents, and incident records must be retained for at least 3 years, or longer where a contract, law, or POL-03 requires. (SI-12)
4.13 AI tools that use customer, employee, or supplier data, or that affect prices, offers, hiring, or customers, must be approved through the AI governance process before use (STD-05; P10). (PM-9; GV.RM-01)
4.14 **Claims review.** Privacy, security, savings, and pricing claims in the privacy notice, website, app, ads, and in-store signs must be reviewed by the Privacy and Compliance Manager before publication, and must be kept accurate when practices change. (PT-5; GV.OC-03; FTC Act Section 5)
4.15 **Data sharing review.** Any new use or sharing of customer or loyalty data, including supplier data programs, must pass a privacy review that checks it against the privacy notice before it starts. (PT-5; GV.OC-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (4.8). Compliance is checked through the annual independent assessment (P07), the QSA's PCI DSS assessment, quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); PCI DSS v4.0.1; FTC Act Section 5; Fla. Stat. 501.171
