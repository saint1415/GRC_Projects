# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Risk and Quality Partner |
| Approved by | Firm Administrator |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after material changes or security events |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-6, SC-8, SC-28, SI-12, CP-9, CM-8 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| FTC Safeguards Rule | 16 CFR 314.4(c)(2), (c)(3), (c)(6) |
| Other | 26 CFR 301.7216-2 and -3; Fla. Stat. 501.171(8) |

## 1. Purpose
Classify firm information by sensitivity and set handling rules so protection matches the harm a disclosure would cause, including the legal limits on disclosing tax return information.

## 2. Scope
All Cris Santos Company workforce members (partners, employees, seasonal preparers, interns, and contractors), all firm systems, paper records, and data, including data held by service providers for the firm.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Risk and Quality Partner | Owns classification and the retention schedule; approves new uses of Restricted data |
| Tax Partner | Approves any disclosure of tax return information that needs taxpayer consent |
| IT Manager | Implements encryption, backup, inventory, and disposal controls |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Tax return information, SSNs and ITINs, bank and account numbers, identity documents, client financial statements and workpapers, credentials | Encrypted at rest and in transit; approved systems only; disclosed only as IRC 7216 permits |
| **Confidential** | Engagement letters, fee data, payroll, security documents | Encrypted in transit; need-to-know |
| **Internal** | Procedures, calendars | Workforce only |
| **Public** | Website, newsletters | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest on every device and service, including desktops and printer-scanner storage, and encrypted in transit over external networks. Returns and source documents must be sent to clients only through the client portal or the firm's encrypted email option, never as plain attachments. (SC-28; SC-8; PR.DS-01; PR.DS-02; 314.4(c)(3))
4.3 Restricted data may be stored only in approved systems: the tax software, the client portal, the DMS, the workpaper application, and the backup vault. It must never be kept on personal devices, personal email, or personal cloud accounts. (AC-3)
4.4 The IT Manager must keep an inventory of where Restricted data is stored and which service providers receive it, including sub-processors such as AI services. (ID.AM-07; CM-8; 314.4(c)(2))
4.5 **Disclosure of tax return information.** Tax return information may be shared outside the firm only when 26 CFR 301.7216-2 permits it (for example, to the IRS, to another U.S. preparer or e-file provider for non-substantive processing, or to a contractor who has received the written section 6713 and 7216 notice) or when the taxpayer has signed a consent that meets 301.7216-3 before the disclosure. It may not be shared with anyone outside the United States without consent, and SSNs of Form 1040 filers may not be sent outside the United States. (AC-21; PT-4)
4.6 **Retention and disposal.** Customer information must be disposed of securely no later than two years after the last date it was used to serve the client, unless the retention schedule requires it longer for business or legal reasons (for example, Forms 8879 for at least three years under IRS Pub. 1345, and engagement workpapers under professional standards). The retention schedule must be reviewed each year. (SI-12; ID.AM-08; 314.4(c)(6))
4.7 Paper must be shredded by a vendor that provides certificates of destruction. Drives must be wiped or destroyed with a record kept, and printer-scanner drives must be wiped with a certificate before a leased device leaves the firm. (MP-6; ID.AM-08; Fla. Stat. 501.171(8))
4.8 Backups of Restricted data must be encrypted, immutable, stored apart from production, and restore-tested quarterly. (CP-9; PR.DS-11)
4.9 Restricted data must not be entered into AI tools unless the tool is on the approved list and the Tax Partner has confirmed the IRC 7216 basis for that use (see P10 and POL-05). (SA-9)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.11. Compliance is checked through the annual control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.8. They must be written, risk-rated, approved by the policy owner (or by the Managing Partner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; retention schedule; P10 approved AI tools list; IRC 7216 consent templates
