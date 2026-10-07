# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Medical Director (Privacy Officer) |
| Approved by | Practice Administrator |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-3, MP-6, SC-8, SC-28, SI-12, CP-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| HIPAA Security Rule | 164.310(d); 164.312(a)(2)(iv), (e); 164.308(a)(7)(ii)(A) |

## 1. Purpose
Classify practice information by sensitivity and set handling rules so protection matches the harm a disclosure would cause.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, students, and volunteers) at Clinic A and Clinic B. Covers all systems and data, including systems that business associates operate for the practice. It applies to electronic protected health information (ePHI) and all other practice information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Privacy Officer | Owns classification; approves new uses of Restricted data |
| IT Manager | Implements encryption, backup, and disposal controls |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | ePHI, patient records, X-ray images, Social Security numbers, credentials | Encrypted at rest and in transit; minimum necessary; approved systems only |
| **Confidential** | Payroll, contracts, security documents | Encrypted in transit; need-to-know |
| **Internal** | Schedules, procedures | Workforce only |
| **Public** | Website, brochures | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest on every device and service, including desktops, and encrypted in transit. External email containing PHI must use the practice's enforced encryption option. (SC-28; SC-8; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv); 164.312(e)(2)(ii))
4.3 Restricted data may be stored only in approved systems: the EHR, the imaging archive, the practice file share, and the backup vault. It must never be kept on personal devices or in personal cloud accounts. (AC-3)
4.4 The IT Manager must keep an inventory of where Restricted data is stored and which vendors receive it. (ID.AM-07; CM-8)
4.5 Media and devices holding Restricted data must be wiped (for reuse) or destroyed by a certified vendor that provides a certificate of destruction (for disposal). (MP-6; ID.AM-08; 164.310(d)(2)(i)-(ii))
4.6 Backups of Restricted data must be encrypted, stored apart from production (a separate account or location), protected from alteration, and restore-tested quarterly. (CP-9; PR.DS-11; 164.308(a)(7)(ii)(A))
4.7 Restricted data must not be entered into AI tools or other third-party services unless the tool is on the approved list and the vendor has a signed BAA (see P10 and POL-05). (SA-9)
4.8 Records are retained according to the medical records retention schedule. Security documentation is retained for 6 years (POL-01 4.10). (SI-12)

## 5. Compliance and enforcement
Violations are handled under the HIPAA sanctions procedure (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; P10 AI approved-tools list; medical records retention schedule
