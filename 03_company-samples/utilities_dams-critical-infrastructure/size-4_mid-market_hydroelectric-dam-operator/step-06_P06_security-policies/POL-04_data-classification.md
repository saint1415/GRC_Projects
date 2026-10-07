# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | GRC Manager with the Chief Dam Safety Engineer |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy, which was written mainly for IT) |
| Review cycle | Annually (next review by 2027-09-30); CIP-003-9 R1 topics within 15 calendar months; and after major changes or significant incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-6, AU-6, MP-3, SC-8, SC-28, SC-12, SA-9, AC-21, MP-6, PL-4, SI-12 |
| CSF 2.0 | ID.AM-05, PR.DS-01, ID.AM-07, GV.SC-05, PR.DS-11 |
| Regulatory drivers | C-DAMS-R01 (FERC Security Program Rev. 3A); C-DAMS-R02 (18 CFR 12.10); C-DAMS-R03 (NERC CIP-003-9, CIP-012-2, EOP-004-4) where cited below |
| Supporting standards | See `standards-index.md` |

## 1. Purpose
Protect information in proportion to the harm its disclosure, change, or loss could cause, with particular care for information that could help someone attack a dam.

## 2. Scope
All company and client information in any form, in corporate IT, OT, the cloud, SaaS, and paper.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Information owners | Classify and approve access |
| Chief Dam Safety Engineer | Owner of drawings, inundation maps, and instrument data |
| Corporate Security Manager | Owner of Security Program documents |
| Data Analytics Lead | Classification of cloud datasets |
| All workforce | Handle information according to its label |

## 4. Policy statements
Each statement ends with the SP 800-53 controls, CSF 2.0 subcategory, and regulatory driver it implements.

4.1 Restricted: CEII (specific engineering, vulnerability, or detailed design information about the projects), Security Program documents (VA, SAs, Security Plans, Section 9 determinations, certification letters), BES Cyber System Information, network diagrams, and OT credentials. Confidential: RMOS client data, employee personal information, contracts, financial data. Internal: other business data. Public: approved for release. (RA-2; ID.AM-05; CEII, 18 CFR 388.113(c)(2); C-DAMS-R01 (Rev. 3A 3.2 (OPSEC)))
4.2 Restricted information is stored only in the restricted library or approved OT systems, with named access approved by its owner and download alerts. It may not be stored in general file shares, personal storage, or email attachments to outside parties. (AC-3; AC-6; AU-6; PR.DS-01; CEII, 18 CFR 388.113(c)(2); C-DAMS-R01 (Form 1 Q22))
4.3 Security Program documents and certification letters are marked "Privileged - Security Sensitive Material". Information filed with FERC for CEII treatment carries the justification and CEII labels the rule requires. (MP-3; PR.DS-01; C-DAMS-R01 (Rev. 3A 8.0); CEII, 18 CFR 388.113(d)(1))
4.4 Confidential and Restricted data is encrypted in transit and at rest in cloud and SaaS services, with company-managed keys in the cloud. (SC-8; SC-28; SC-12; PR.DS-01; RMOS contracts; Fla. Stat. 501.171(2))
4.5 Every cloud dataset carries a classification tag; datasets containing CEII are kept in a separate storage location with named access. (RA-2; AC-3; ID.AM-07; CEII, 18 CFR 388.113(c)(2))
4.6 Restricted and Confidential information may be shared with vendors, clients, or agencies only under a contract or legal basis that requires equivalent protection, and only the minimum needed. (SA-9; AC-21; GV.SC-05; CEII, 18 CFR 388.113; RMOS contracts)
4.7 Media and equipment that held Restricted or Confidential data are sanitized or destroyed with a certificate before disposal or return. (MP-6; PR.DS-01; C-DAMS-R01 (Table 9.3a system lifecycle (secure disposal)))
4.8 Restricted and Confidential data may not be entered into AI tools unless the tool is approved for that level (STD-11). (PL-4; SA-9; PR.DS-01; CEII, 18 CFR 388.113)
4.9 Retention follows POL-01 4.12; permanent project records are kept as 18 CFR 12.12 requires. (SI-12; PR.DS-11; C-DAMS-R02 (related Part 12 duty: 12.12))

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), quarterly OT access reviews, NERC compliance evidence reviews by the NERC Compliance Manager, and metrics reported to the audit committee. Violations are handled under POL-01 4.14.

## 6. Exceptions
Exceptions must be requested in writing, risk-rated, approved under POL-01 4.4, recorded in the risk register, and limited to 12 months. No exception may waive a FERC or NERC requirement.

## 7. Related documents
POL-01; STD-10 CEII and information handling; STD-08 encryption; STD-11 AI use
