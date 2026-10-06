# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (and Cris Santos Assurance, LLP) |
| Policy ID | POL-04 |
| Owner | Privacy Officer |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | AC-21, CM-8, CP-9, MP-1, MP-6, SC-8, SC-12, SC-28, SI-12, SA-9(5) |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.OC-03 |
| FTC Safeguards Rule | 16 CFR 314.4(c)(2), (c)(3), (c)(6) |
| Other | 26 CFR 301.7216-2 and -3; 45 CFR 164.312(a)(2)(iv), (e)(1); Fla. Stat. 501.171(8); IRS Pub. 1345 (Form 8879 retention) |
| Supporting standards | STD-04 Data handling, IRC 7216 disclosure, and retention standard; STD-08 Encryption and key management standard; STD-11 Offshore preparation program security standard |

## 1. Purpose
Classify Company and client information, and set the handling, disclosure, retention, and disposal rules for each class, so that tax return information, customer information, PHI, and client funds data get the strongest protection.

## 2. Scope
All information the Company and the Attest Firm create, receive, or hold, in any form (electronic, paper, or images on scanners and printers), in every system and with every service provider.

## 3. Classes
| Class | Examples | Minimum handling |
|---|---|---|
| **Restricted** | Tax return information (26 CFR 301.7216-1(b)(3)), SSNs, bank and account numbers, client payroll data, PHI from health care engagements, identity documents | Encrypted at rest and in transit; need-to-know access; disclosure only as 4.5 allows; no plain email |
| **Confidential** | Client financial statements and ledgers, SOC engagement evidence, engagement letters, Company financial data | Encrypted at rest; engagement-team access; shared only through the portal or approved services |
| **Internal** | Policies, procedures, staff directories | Company systems only |
| **Public** | Website content, published articles | No restriction |

## 4. Policy statements
4.1 Every information owner must classify the data they create or receive. Unlabeled client data is treated as Restricted. (RA-2; GV.OC-03)

4.2 Restricted data must be encrypted at rest and in transit over external networks. It must not be sent as a plain email attachment; staff must use the portal or the enforced-encryption option. Where encryption is infeasible, the Qualified Individual must approve compensating controls in writing. (SC-8; SC-28; SC-12; PR.DS-01; PR.DS-02; 314.4(c)(3); 164.312(e)(1))

4.3 PHI received from health care clients must be stored only in the restricted data enclave, accessible only to the engagement team, from 2027-03-31. Until then it must be stored only in folders marked for PHI. (AC-3; 164.308(a)(4))

4.4 The Company must keep an inventory of where Restricted data is stored and which service providers and sub-processors (including AI sub-processors) receive it, updated by the new technology gate (POL-01 4.9). (CM-8; ID.AM-07; 314.4(c)(2))

4.5 **IRC 7216 disclosures.** Tax return information may be disclosed or used only as 26 CFR 301.7216-2 permits or with the taxpayer's prior written, knowing, and voluntary consent under 301.7216-3. The consent must be signed before the disclosure, must identify the recipient and purpose, and is tracked for expiry (one year if no duration is stated, 301.7216-3(b)(5)). The taxpayer receives a copy at signing. (AC-21; GV.OC-03)

4.6 **Offshore disclosures.** No tax return information may be routed to the offshore preparation program before the consent is signed. SSNs of Form 1040 series filers must be redacted or masked in every document and screen the offshore preparer can see, unless counsel approves an IRS-defined adequate data protection safeguard (301.7216-3(b)(4)). (SA-9(5); AC-21)

4.7 **Retention and disposal.** Records must be kept as the retention schedule in STD-04 sets: 7 years for tax files unless law or a client agreement requires longer, at least 3 years for Forms 8878 and 8879 as IRS Pub. 1345 requires, and 6 years for HIPAA-related documentation. Customer information must be disposed of no later than two years after the last date it was used to provide a service to the customer, unless the schedule, a legal requirement, or a legitimate business need requires longer, or targeted disposal is not feasible because of how the data is kept (314.4(c)(6)(i)). A disposal run must be performed each year, with legal hold checks. (SI-12; ID.AM-08; 314.4(c)(6))

4.8 Paper must be shredded by the contracted vendor with certificates of destruction. Drives, scanners, and multifunction printers must be wiped or destroyed, with a certificate, before reuse, disposal, or return to a lessor. (MP-6; Fla. Stat. 501.171(8))

4.9 Backups of Company-managed data must be encrypted, immutable for at least 35 days, stored in a separate account and region, and restore-tested at least quarterly for the DMS and workpaper application. (CP-9; PR.DS-11)

4.10 Restricted or Confidential data may be entered into an AI tool only if the tool is on the approved list for that data class and the use has a documented IRC 7216 basis (STD-05; P10). Public AI chatbots must never receive client data. (SA-9; AC-21)

4.11 Legal holds set by the General Counsel suspend disposal for the records they cover. (SI-12)

## 5. Compliance and enforcement
Violations are handled under POL-01 4.14. Compliance is checked through the annual independent assessment (P07), consent sampling by the Privacy Officer, and the annual disposal run report.

## 6. Exceptions
Exceptions follow POL-01 4.8. No exception may permit a disclosure that IRC 7216 does not allow.

## 7. Related documents
POL-01; POL-05; STD-04; STD-08; STD-11; 16 CFR 314.4(c); 26 CFR 301.7216-2 and -3; IRS Pub. 1345; Fla. Stat. 501.171(8)
