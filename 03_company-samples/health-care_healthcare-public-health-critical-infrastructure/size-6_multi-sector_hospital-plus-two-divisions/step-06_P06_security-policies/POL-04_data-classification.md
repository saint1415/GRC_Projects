# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, PT-2, PT-3, AC-4, AC-21, CA-3, SC-8, SC-28, CP-9, CP-4, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| HIPAA | Security Rule 164.310(d); 164.312(a)(2)(iv), (e); 164.308(a)(7)(ii)(A). Privacy Rule 164.502(b); 164.506(c); 164.514(d) |
| Other drivers | 16 CFR 314.4(c)(3), (c)(6) (College); 34 CFR 99.30 (FERPA consent); 42 CFR 422.118(a) (MA enrollee records); 42 CFR 482.15(b)(5) (medical documentation in emergencies) |
| Division supplements | Hospital System: clinical images, device data, and paper downtime records. Health Plan: member NPI and MA enrollee records. College: education records and customer information |

## 1. Purpose
Classify group information by sensitivity and by whose data it is, and set handling rules so that each covered entity's PHI, each member's information, and each student's records are used only for their permitted purpose.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including on shared services such as the group file service and on paper during downtime.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes and the minimum-necessary protocols between covered entities |
| Data owners | Classify data and approve feeds and access |
| Health information management (each hospital) | Custody of paper downtime records |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (PHI, member nonpublic personal information, student education records and customer information, credentials, and keys), **Confidential**, **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest and in transit over external networks with approved algorithms and group-managed keys. Restricted information must not be sent by unencrypted email. (SC-28; SC-8; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv); 164.312(e)(2)(ii); 16 CFR 314.4(c)(3))

4.3 **Between covered entities.** PHI may move between the Hospital System and the Health Plan only under a documented permission (for example, 164.506(c)(4)) and, for routine and recurring feeds, a written minimum-necessary protocol approved by both Privacy Officers that names the purpose and the data elements. The Health Plan must document the purposes for which it uses enrollee information it receives. (AC-21; CA-3; PT-3; PR.DS-10; 164.502(b); 164.514(d)(3)-(4); 42 CFR 422.118(a))

4.4 **Education records.** The College may disclose personally identifiable information from education records only with the student's signed and dated written consent or under a FERPA exception. Placement rosters and clearance information must reach hospitals through the secure roster feed, never as email attachments. (PT-2; AC-4; 34 CFR 99.30; 99.31)

4.5 **Backups** of Restricted information must be immutable, held with a different provider or account from production, and restore-tested at least quarterly for High-criticality systems. Each High-criticality clinical system must have a full restore test from the vault at least once a year. (CP-9; CP-4; PR.DS-11; 164.308(a)(7)(ii)(A), (D))

4.6 Media holding Restricted information must be sanitized or destroyed with a certificate. (MP-6; ID.AM-08; 164.310(d)(2)(i))

4.7 Information must be retained per the group retention schedule. College customer information must be disposed of no later than 2 years after its last use for the student unless needed for business operations or required by law, and the schedule must be reviewed every year. (SI-12; 16 CFR 314.4(c)(6))

4.8 **Paper downtime records** are Restricted. Each hospital's health information management team must track them, enter or scan them into the EHR within 24 hours of recovery (or on a documented schedule for outages longer than 24 hours), and destroy the copies securely. (MP-6; 482.15(b)(5); 164.310(d))

4.9 Restricted information must not be entered into any AI tool unless the tool is approved under the Group AI Standard and covered by a contract that prohibits training on group data. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-21, PT-3, CP-9) and data flow reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP (HCIS information exchanges); P10 Group AI Standard.
