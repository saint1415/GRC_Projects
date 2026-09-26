# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | COO |
| Approved by | COO; majority owner and CEO (budget and risk acceptance sections) |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after significant changes or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CA-7, CM-8, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.OC-02, GV.SC-05, GV.SC-07 |
| PCI DSS v4.0.1 | 12.1, 12.3.1, 12.4.1, 12.4.2, 12.5.2.1, 12.5.3, 12.8, 12.9 |
| FTC Safeguards Rule | 16 CFR 314.4(a), (b), (d), (f), (g), (i) |

## 1. Purpose
Set up the Cris Santos Company information security program, assign who is accountable, and give every other security policy its authority. The program protects cardholder data, merchant information, and the processing services that merchants and the sponsor bank depend on.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors). Covers all company systems and data, including the cardholder data environment (CDE), the systems connected to it, and systems that service providers operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Majority owner and CEO | Approves the security budget; accepts High and Very High risks; receives the annual Qualified Individual report |
| COO | Program owner and executive accountable for PCI DSS compliance; approves policies; accepts Moderate risks |
| IT Manager (Information Security Lead) | Qualified Individual under 16 CFR 314.4(a); runs the program day to day; maintains the risk register, SSP, and PCI DSS scope |
| Compliance and Risk Manager | Service provider oversight; sponsor bank and card brand compliance; notice decisions with counsel |
| CTO and Platform Engineering Lead | Secure engineering, change management, and cloud operations |
| All workforce | Follow these policies; report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The company must maintain a written information security program that meets PCI DSS v4.0.1 for service providers and the FTC Safeguards Rule. The program is documented in this policy set, the System Security Plan (P02), and the risk register (P01). (PM-1; GV.PO-01)

4.2 The IT Manager is the designated Qualified Individual. The CEO must make the designation in writing, and the COO directs and oversees the Qualified Individual. (PM-2; GV.RR-02; 16 CFR 314.4(a))

4.3 **Executive responsibility for PCI DSS.** The COO is accountable for protecting cardholder data and for PCI DSS compliance. A written charter, approved by the CEO, must define that accountability and how the COO reports to the CEO. Every PCI DSS requirement must have a named responsible role, recorded in the PCI DSS responsibility matrix. (PM-2; GV.RR-01; PCI DSS 12.1.3, 12.4.1)

4.4 A written risk assessment must be performed at least annually and after any significant change, using NIST SP 800-30 Rev. 1. It must include the evaluation criteria in P01 section 1. A targeted risk analysis must be documented for each PCI DSS requirement that lets the company choose how often it is performed. (RA-3; PM-9; GV.RM-01; 16 CFR 314.4(b); PCI DSS 12.3.1)

4.5 **Risk acceptance authority:**
- The IT Manager may accept Low and Very Low risks.
- The COO may accept Moderate risks.
- Only the majority owner and CEO may accept High and Very High risks, and only with a dated treatment plan.
- No one may accept a risk that would leave a PCI DSS requirement not in place at the annual ROC.

(PM-9; GV.RM-01)

4.6 **PCI DSS scope** must be documented and confirmed at least every six months and after any significant change to the environment. Every significant organizational change must trigger a documented review of its effect on scope and on control ownership. Significant changes include new hosting, new card data flows, new service providers, and reorganizations. (CM-8; PL-2; ID.AM-01; PCI DSS 12.5.2.1, 12.5.3; 16 CFR 314.4(g))

4.7 At least every three months, the IT Manager must review whether staff are performing the required security tasks: daily log reviews, network rule reviews, configuration checks, alert response, and change management. Each review must be documented with its results, remediation actions, and COO sign-off. (CA-7; GV.OV-01; PCI DSS 12.4.2, 12.4.2.1)

4.8 **Service providers.** Before a service provider stores, processes, or transmits account data, or can affect CDE security, it must meet four conditions:
- pass due diligence
- sign a written agreement that includes security obligations
- provide a current AOC, or agree to be included in the company's ROC
- agree a responsibility matrix

Providers must be reviewed at least annually, including their AOC or SOC 2 report (P09). (SA-9; SR-6; GV.SC-05; GV.SC-07; PCI DSS 12.8; 16 CFR 314.4(f))

4.9 **Merchants and partners.** Merchant agreements must acknowledge the company's responsibility for the account data it handles. The company must give merchants its current AOC and a PCI DSS responsibility matrix on request. (PL-2; GV.OC-02; PCI DSS 12.9.1, 12.9.2)

4.10 The Qualified Individual must report in writing at least annually to the CEO and COO. The report must cover the program's overall status, compliance with the Safeguards Rule, and material matters: risk decisions, service providers, test results, security events, and recommended changes. The company has no board, so the CEO and COO are the senior officers who receive it. (PM-9; GV.OV-01; 16 CFR 314.4(i))

4.11 Security controls must be tested every year: an internal control assessment (P07) and the QSA's ROC. The program must be adjusted after tests, material changes, and risk assessments. (CA-2; ID.IM-01; 16 CFR 314.4(d), (g))

4.12 Security policies must be reviewed at least annually and updated after significant changes or incidents. Updated policies must be communicated to all affected staff. (PL-1; GV.PO-02; PCI DSS 12.1.2)

4.13 **Exceptions** to any security policy must be requested in writing, risk-rated, approved under 4.5, recorded in the risk register, and time-limited to 12 months or less. (PL-1)

4.14 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction. (PS-8; GV.RR-04)

4.15 Security policies, risk assessments, assessment results, and incident records must be kept for at least 3 years. Longer periods apply where a contract or law requires. (SI-12; GV.PO-02)

## 5. Compliance and enforcement
Violations are handled under section 4.14. Compliance is checked through the quarterly reviews (4.7), the annual control assessment (P07), and the QSA's ROC.

## 6. Exceptions
Exceptions follow section 4.13. They must be written, risk-rated, approved by the policy owner (or by the majority owner and CEO for High risk), and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); PCI DSS responsibility matrix; FTC Safeguards Rule, 16 CFR Part 314
