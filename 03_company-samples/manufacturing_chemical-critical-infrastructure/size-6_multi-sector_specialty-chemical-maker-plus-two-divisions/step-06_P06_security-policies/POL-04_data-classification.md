# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group CISO, with the Group General Counsel for SSI and legacy CVI |
| Approved by | Group CISO, after board risk committee review |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-2, MP-4, MP-6, AC-3, AC-21, SC-28, SI-12 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10 |
| Regulatory basis | 49 CFR Part 1520 (SSI); 33 CFR 101.630(b) and 105.225(c); 6 CFR 27.400 (legacy CVI, precaution); FMCSA 49 CFR 382.405; state breach laws |

## 1. Purpose
Classify group information by the harm its disclosure, alteration, or loss could cause, and set handling rules for each class, including the security information that federal rules protect.

## 2. Scope
All information the group creates, receives, or holds, in any form, including OT configuration data and information held by service providers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Data owners (division leaders) | Classify their data and approve access |
| Terminal T1 Facility Security Officer | Controls SSI for Terminal T1 |
| Group General Counsel | Decides SSI and legacy CVI questions |
| All workforce | Label and handle information by class |

## 4. Policy statements
**Classes used across the group:**

| Class | Examples | Handling |
|---|---|---|
| **Restricted-Security** | Terminal T1 Facility Security Plan, Cybersecurity Plan, and TWIC reader records (SSI); legacy CVI; hazmat security plans; OT network diagrams, conduit registers, firewall rules, SIS logic, vulnerability reports | Need-to-know only; encrypted at rest and in transit; never in email to external parties; SSI marked and handled under 49 CFR Part 1520 |
| **Restricted-Formulation** | Master recipes and formulations (about 2,300 at Plant C1), process safety information with trade-secret content | Need-to-know groups per recipe family; query logging; no use in AI tools except approved projects (4.6) |
| **Restricted-Personal** | Employee and driver personal information, driver qualification files, drug and alcohol testing records | Least privilege; testing records released only as 49 CFR 382.405 allows; breach handling under POL-03 |
| **Confidential** | Contracts, pricing, customer tank data, production plans | Internal sharing by role; encrypted in transit |
| **Internal** | Policies, procedures, training | Workforce only |
| **Public** | SDS, marketing, published RMP executive summaries | No restriction |

4.1 Every dataset and system must have an owner and a class recorded in the asset inventory. (RA-2; ID.AM-05)

4.2 SSI (the Facility Security Plan, the Cybersecurity Plan, and TWIC reader records) must be protected under 49 CFR Part 1520 and disclosed only to covered persons with a need to know. (AC-3; MP-4; 33 CFR 101.630(b); 105.225(c))

4.3 Legacy CVI from the CFATS era is kept in a restricted repository and handled as Restricted-Security as a precaution while CFATS is lapsed. (AC-3; MP-4)

4.4 Restricted data must be encrypted at rest and in transit wherever technically feasible. Where OT protocols cannot be encrypted, the conduit must be segmented and monitored instead. (SC-28; SC-8; PR.DS-01)

4.5 OT configuration copies and recipes must be kept offline in at least one copy, with integrity verified before use. (CP-9; SI-7)

4.6 Restricted data must not be entered into any AI tool unless the tool and the project are approved under the Group AI Standard with no-training and retention terms. Public AI services are allowed only for Public data. (AC-21; PR.DS-10)

4.7 Media holding Restricted data must be sanitized before reuse or disposal, with certificates. (MP-6)

4.8 Records are retained per POL-01 4.11 and destroyed securely at the end of their retention period unless on legal hold. (SI-12)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through access reviews, data loss prevention reports, and the P07 assessment.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may permit disclosure of SSI to a person who is not a covered person with a need to know.

## 7. Related documents
POL-01; POL-02; POL-05; 49 CFR Part 1520; group records schedule; Group AI Standard (P10).
