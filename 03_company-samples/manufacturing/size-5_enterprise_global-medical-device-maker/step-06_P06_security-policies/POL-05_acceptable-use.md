# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-05 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Human Resources Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or product launches |
| Implements (SP 800-53 Rev. 5) | AT-1, PL-4, AT-2, AT-3, MP-7, CM-7, AC-19, AC-20, CM-11, SA-9, IR-6 |
| CSF 2.0 | PR.AT-01, PR.AT-02, PR.AA-05, PR.PS-05 |
| Regulatory basis | HIPAA 164.308(a)(5), 164.310(b) (N62-R01); FD&C Act 524B(b)(2) (N31-33-R05) |

## 1. Purpose
Set the rules every workforce member follows when using company systems, plant equipment, and data, including generative AI tools.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at every site: headquarters, the FL-1, MN-1, and TX-1 plants, the R&D centers, the RCM monitoring centers, and remote work, including the acquired infusion business from its acquisition date. Covers all systems and data, including cloud, colocation, SaaS, plant OT, the Device Software Factory, and systems that business associates, contract manufacturers, and other vendors operate for the company, and the products and services the company provides to customers and consumers (fielded devices, the DDC, the RCM service, and the consumer companion app).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Owns this policy; attestations and training records |
| CISO | Technical enforcement |
| Plant directors | Plant floor rules for stations and removable media |
| All workforce | Follow the rules and report concerns |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Company systems and data may be used only for authorized business purposes; users have no expectation of privacy on company systems. (PL-4; PR.AT-01)
4.2 Every workforce member must acknowledge this policy and complete security awareness training at hire and annually; role-based training is required for developers, signing custodians, plant engineers, and RCM staff. (AT-2; AT-3; PL-4; PR.AT-01; PR.AT-02)
4.3 Removable media must not be connected to programming stations or plant OT systems, except company-issued, scanned media for USB field updates under the service procedure. (MP-7; CM-7; PR.PS-01)
4.4 Only company-managed devices may access Restricted data, source code, or plant systems; personal devices are limited to email and collaboration under STD-05.2. (AC-19; AC-20; PR.AA-05)
4.5 Users must not install unapproved software on company devices or stations. (CM-11; PR.PS-05)
4.6 Only AI tools on the approved AI tools list (STD-05.3) may be used for company work. Source code, vulnerability details, signing material, PHI, and consumer data must never be entered into unapproved AI tools, and any new AI feature must be registered before use. (PL-4; SA-9; GV.RR-04)
4.7 Users must report lost devices, suspected phishing, and suspected incidents within 1 hour (POL-03 4.2). (IR-6; RS.MA-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 External Systems and Personal Devices Standard
- STD-05.3 Approved AI Tools List

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 DSF-MES SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.
