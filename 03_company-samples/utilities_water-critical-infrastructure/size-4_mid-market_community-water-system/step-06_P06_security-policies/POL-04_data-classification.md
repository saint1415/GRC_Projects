# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | IT Director (security officer) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-21, SC-8, SC-28, MP-4, MP-6, SI-12, PL-4, SA-9 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10, GV.PO-02 |
| Regulatory drivers | 42 U.S.C. 300i-2(d) (C-WATER-R01); 40 CFR 141.33(e), 141.405(b); Fla. Stat. 501.171(2), (4)(c), (8) |
| Supporting standards | STD-05 Media sanitization and disposal; STD-10 AI use |

## 1. Purpose
Classify company information by the harm its loss or misuse would cause, and set handling rules for each class.

## 2. Scope
All information the company creates, receives, or holds, in any form, including client data held for Utility Services.

## 3. Classes
| Class | Examples | Handling summary |
|---|---|---|
| **Restricted** | RRA and ERP contents; SCADA configurations, PLC logic, network diagrams and IP plans; credentials and vault contents; critical asset locations in the GIS; customer bank account numbers and online account credentials | Need to know; restricted libraries only; encrypted at rest and in transit; never in unapproved tools; external sharing only with approval and a written confidentiality agreement |
| **Confidential** | Customer names, addresses, and usage; client customer data; employee personal data; contracts; security assessment results | Role-based access; encrypted at rest and in transit; external sharing under contract |
| **Internal** | Procedures, schedules, internal memos | Workforce only |
| **Public** | Water quality reports, public notices, rates | No restrictions after approval |

## 4. Policy statements
4.1 Every information system and data set must have an owner who assigns its class. OT process data and configurations are Restricted by default. (RA-2; ID.AM-05)
4.2 RRA and ERP contents, SCADA drawings, and critical asset maps must be stored only in the restricted libraries, with access limited to named groups and reviewed every quarter. (AC-3; PR.DS-01; 42 U.S.C. 300i-2(d))
4.3 Restricted and Confidential data must be encrypted at rest and in transit with methods approved in STD-03. Card numbers must never be stored or entered in company systems; card payments use the processor's hosted page and phone line only. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.4 RRA and ERP contents may be shared outside the company only with the approval of the Emergency Management and Resilience Manager and the General Counsel, under a written confidentiality agreement. EPA certifications contain only the content the statute permits. (AC-21; PR.DS-01; 42 U.S.C. 300i-2(a)(4))
4.5 **Retention.** RRAs and ERPs: at least 5 years after each certification. Public notices and certifications: at least 3 years. Ground Water Rule residual records: as 40 CFR 141.405(b) requires (5 or 10 years by record type). Florida breach no-notice determinations: at least 5 years. Security records: under POL-01 statement 4.14. (SI-12; GV.PO-02; 40 CFR 141.33(e); 141.405(b); Fla. Stat. 501.171(4)(c))
4.6 Media and records containing Restricted or Confidential data must be sanitized or destroyed under STD-05 when no longer retained, with a certificate for each batch. (MP-6; PR.DS-10; Fla. Stat. 501.171(8))
4.7 Restricted and Confidential data must not be entered in any AI tool or external service that is not on the approved list, and approved AI tools must have contract terms that prohibit training on company data (STD-10). (PL-4; SA-9)
4.8 Client customer data held for Utility Services must be kept separate by client in the CIS and used only for that client's services. (AC-3; PR.DS-10)
4.9 Removable media may carry Restricted OT data (for example offline PLC backups) only if encrypted and logged, and must be stored in a locked location. (MP-4; PR.DS-01)

## 5. Compliance and enforcement
Checked through quarterly reviews of restricted libraries, disposal certificates, and the annual assessment (P07).

## 6. Exceptions
Under POL-01 statement 4.7.

## 7. Related documents
POL-01; POL-05; STD-05; STD-10; RRA library index
