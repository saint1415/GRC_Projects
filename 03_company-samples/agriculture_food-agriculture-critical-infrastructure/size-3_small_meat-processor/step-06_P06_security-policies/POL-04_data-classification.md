# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | FSQA Manager |
| Approved by | General Manager |
| Effective date | 2026-09-07 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-6, AU-9, AU-11, SC-8, SC-28, SI-12, CP-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| Regulatory basis | 21 CFR 121.305, 121.315, 121.325; 9 CFR 417.5; 21 CFR 123.9; Fla. Stat. 501.171 |

## 1. Purpose
Classify company information by the harm its disclosure or alteration would cause, and set handling rules. For a food plant, **alteration** can be worse than disclosure: a changed formulation or falsified CCP record can hurt consumers.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary and agency workers, and contractors) at the Florida plant and outlet store. Covers all systems and data, including process control systems, cloud and SaaS services, and systems that vendors operate or maintain for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| FSQA Manager | Owns classification; approves access to Restricted food defense and formulation data |
| IT Manager | Implements encryption, access restriction, backup, logging, and disposal controls |
| Controls Engineer | Protects OT configuration data (PLC programs, setpoints, recipes) |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Food defense plan and vulnerability assessment; formulations and cure specifications; PLC programs and network diagrams; employee Social Security numbers and bank data; credentials | Named-person access only; encrypted at rest and in transit; access logged; never on personal devices or public AI tools |
| **Confidential** | HACCP and seafood HACCP records; food defense monitoring records; customer pricing and contracts; online customer accounts | Encrypted in transit; need-to-know; integrity protected |
| **Internal** | Production schedules, procedures, training materials | Workforce only |
| **Public** | Website, product labels, brochures | No restriction |

(RA-2; ID.AM-07)
4.2 The food defense plan and vulnerability assessment must be kept in a restricted library limited to the General Manager, FSQA Manager, IT Manager, Controls Engineer, and Maintenance and Refrigeration Manager, with a controlled printed copy in the FSQA office safe so the plan stays available onsite during IT outages. (AC-3; 21 CFR 121.315(c))
4.3 **Record integrity.** Electronic CCP, seafood HACCP, and food defense records must be created under named accounts at the time of the activity, must keep an audit trail of every change, and must be locked after sign-off. Corrections must be made by a new entry that keeps the original. (AU-9; PR.DS-10; 9 CFR 417.5(b), (d); 21 CFR 123.9(f); 21 CFR 121.305(c)-(d))
4.4 Restricted and Confidential data must be encrypted in transit. Restricted data must be encrypted at rest on every device and service. (SC-8; SC-28; PR.DS-01; PR.DS-02)
4.5 **Retention.** HACCP monitoring records must be kept at least 1 year for refrigerated products and 2 years for frozen, preserved, or shelf-stable products (9 CFR 417.5(e)); seafood HACCP records on the same schedule (21 CFR 123.9(b)); food defense records at least 2 years after preparation and the food defense plan at least 2 years after its use is discontinued (21 CFR 121.315). For simplicity the company keeps every such record for 3 years after preparation, and each version of the food defense plan for 3 years after it is replaced. (SI-12; AU-11)
4.6 Backups of Restricted and Confidential data, including PLC programs and recipe databases, must be encrypted, stored apart from production (a separate account or offline), protected from alteration, and restore-tested quarterly. (CP-9; PR.DS-11)
4.7 Media and devices holding Restricted data must be wiped for reuse or destroyed by a certified vendor that provides a certificate of destruction. This includes replaced HMIs and engineering laptops. (MP-6; ID.AM-08)
4.8 Restricted data must not be entered into AI tools or other third-party services unless the tool is on the approved list (POL-05 4.8). (SA-9)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.9). Compliance is checked through the annual control assessment (P07) and food defense verification.

## 6. Exceptions
Exceptions follow POL-01 section 4.8. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; records retention schedule; food defense plan; P10 AI approved-tools list
