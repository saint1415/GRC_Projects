# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after significant changes, acquisitions, platform migrations, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CA-7, CM-8, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.OC-02, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07 |
| PCI DSS v4.0.1 | 12.1, 12.3.1, 12.4.1, 12.4.2, 12.4.2.1, 12.5.2.1, 12.5.3, 12.8, 12.9 |
| FTC Safeguards Rule | 16 CFR 314.4(a), (b), (d), (f), (g), (i) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects cardholder data, merchant information, and the processing, settlement, and funding services that merchants, ISV partners, and both sponsor banks depend on.

## 2. Scope
All workforce members (employees and contractors) in every business unit, including Integrated Payments. It covers all company systems and data: both cardholder data environments (the core platform in Cloud A and the Integrated Payments gateway in Cloud B), the settlement environment in the colocation cages, the systems connected to them, systems that service providers operate for the company, and any business the company acquires from the date of closing.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports and the Qualified Individual's annual written report |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks; designates the Qualified Individual |
| Chief Operating Officer | Executive sponsor; holds PCI DSS executive responsibility (12.4.1); approves POL-02 to POL-05 and the standards; accepts Moderate risks |
| vCISO | Owns this policy and the program strategy; prepares the quarterly board reporting |
| Director of Information Security | **Qualified Individual** (16 CFR 314.4(a)); runs the program day to day; maintains the risk register, the SSP, and PCI DSS scope |
| Chief Risk and Compliance Officer | Service provider oversight; sponsor bank and card brand compliance; model risk; notice decisions with the General Counsel |
| CTO, VP Platform Engineering, Director of Integrated Payments Engineering | Secure engineering, change management, and operations for their platforms |
| Co-sourced internal audit firm | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The company must maintain a written information security program that meets PCI DSS v4.0.1 for service providers and the FTC Safeguards Rule. The program is documented in this policy set, the supporting standards, the System Security Plan (P02), and the risk register (P01). (PM-1; GV.PO-01; 16 CFR 314.4)

4.2 The Director of Information Security is the designated Qualified Individual. The CEO must make the designation in writing and reaffirm it each year. The COO directs and oversees the Qualified Individual. (PM-2; GV.RR-02; 16 CFR 314.4(a))

4.3 **Executive responsibility for PCI DSS.** The COO is accountable for protecting cardholder data and for PCI DSS compliance on every platform. A written charter, approved by the CEO, defines that accountability and how the COO reports to the CEO and the audit committee. Every PCI DSS requirement must have a named responsible role for each platform, recorded in the PCI DSS responsibility matrix. (PM-2; GV.RR-01; PCI DSS 12.1.3, 12.4.1)

4.4 A written risk assessment must be performed at least annually and after any significant change, using NIST SP 800-30 Rev. 1 and the criteria in P01 section 1. A targeted risk analysis must be documented for each PCI DSS requirement that lets the company choose how often it is performed, on every platform. (RA-3; PM-9; GV.RM-01; 16 CFR 314.4(b); PCI DSS 12.3.1)

4.5 **Risk acceptance authority.**
- Risk owners (director level or above) may accept Low and Very Low risks.
- The COO may accept Moderate risks.
- The CEO may accept High risks for up to 12 months with a dated treatment plan, and must report them to the audit committee each quarter.
- Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair.
- No one may accept a risk that would leave a PCI DSS requirement not in place at the annual ROC.

(PM-9; GV.RM-01)

4.6 **PCI DSS scope** must be documented and confirmed at least every six months and after any significant change. Significant changes include acquisitions, new hosting or interconnections, new card data flows, new service providers, and reorganizations. Each significant organizational change must trigger a documented review of its effect on scope and on control ownership, reported to the COO and the audit committee. (CM-8; PL-2; ID.AM-01; PCI DSS 12.5.2.1, 12.5.3; 16 CFR 314.4(g))

4.7 At least every three months, the Director of Information Security must review whether staff on every platform perform the required security tasks: daily log reviews, network rule reviews, configuration checks, alert response, and change management. Each review must be documented with results, remediation actions, and COO sign-off. (CA-7; GV.OV-01; PCI DSS 12.4.2, 12.4.2.1)

4.8 **Service providers.** Before a service provider stores, processes, or transmits account data or can affect the security of a CDE, it must pass due diligence scaled to its tier, sign a written agreement with security obligations, provide a current AOC or agree to be included in the company's ROC, and agree a responsibility matrix. Tier 1 providers must be reviewed each year, including their AOC or SOC 2 report (STD-07; P09). (SA-9; SR-6; GV.SC-05; GV.SC-07; PCI DSS 12.8; 16 CFR 314.4(f))

4.9 **Merchants and ISV partners.** Merchant and ISV agreements must acknowledge the company's responsibility for the account data it handles. The company must give merchants and ISVs its current AOC and a responsibility matrix for the services they use on request. (PL-2; GV.OC-02; PCI DSS 12.9.1, 12.9.2)

4.10 The Qualified Individual must report in writing at least annually to the board audit committee on the overall status of the program and compliance with the Safeguards Rule, and on material matters: risk assessment, risk management and control decisions, service provider arrangements, test results, security events and management's responses, and recommended changes. The vCISO reports to the audit committee each quarter on the top risks and POA&M status. (PM-9; GV.OV-01; 16 CFR 314.4(i))

4.11 Security controls must be independently tested each year: the co-sourced internal audit assessment (P07) and the QSA's ROC. The program must be adjusted after tests, material changes, and risk assessments. (CA-2; ID.IM-01; 16 CFR 314.4(d), (g))

4.12 Security policies must be reviewed at least annually and after significant changes or incidents. Supporting standards must be reviewed at least annually by their owners. Updated policies must be communicated to all affected staff. (PL-1; GV.PO-02; PCI DSS 12.1.2)

4.13 **Exceptions** to any security policy or standard must be requested in writing, risk-rated, approved under 4.5, recorded in the risk register, and time-limited to 12 months or less. (PL-1)

4.14 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction. (PS-8; GV.RR-04)

4.15 Security policies, risk assessments, assessment results, and incident records must be kept for at least 3 years. Longer periods apply where a contract, a card brand, or law requires. (SI-12; GV.PO-02)

4.16 **Acquisitions and new platforms.** Before an acquired environment is connected to a CDE or brought into a sponsor bank program, the Director of Information Security must complete a security due diligence review and an integration plan. Within 90 days of closing, the environment must send logs to the SIEM, use the company identity provider and PAM for administrative access, and be in the PCI DSS scope document, or hold an approved exception under 4.13. (CA-7; CM-8; GV.OV-02; PCI DSS 12.5.3)

4.17 **AI and models.** AI tools and models that process company or customer data, or support decisions about merchants, cardholders, or transactions, must be approved through the AI and model risk process before use (STD-10; P10). (PM-9; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under section 4.14. Compliance is checked through the quarterly reviews (4.7), the annual independent assessment (P07), the QSA's ROC, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.13. They must be written, risk-rated, approved by the right authority under section 4.5, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); PCI DSS responsibility matrix and charter; FTC Safeguards Rule, 16 CFR Part 314; 12 CFR 53.4 and 304.24
