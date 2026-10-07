# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, AC-21, CM-8, SC-8, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| HIPAA | Security Rule 164.310(d); 164.312(a)(2)(iv), (e); 164.308(a)(7)(ii)(A). Privacy Rule 164.502(a)(3), (b); 164.504(e) |
| Division supplements | Ambulance Services: patient care records and state records rules. Urgent Care: clinical images and lab data. BDS: client partitions, call recordings, and card data |

## 1. Purpose
Classify group information by sensitivity and by whose data it is, and set handling rules so that each covered entity's and each client's PHI is used only as permitted.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including call audio, recordings, CAD incident data, and paper run tickets.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes and handling rules |
| Data owners | Classify data and approve interfaces and access |
| System owners | Enforce classes, retention, and partitions in their systems |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (PHI, client PHI, call audio and recordings, card data, credentials, and keys), **Confidential**, **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest and in transit with approved algorithms and group-managed keys. (SC-28; SC-8; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv); 164.312(e)(2)(ii))

4.3 **Client data.** Each external client's PHI must be kept in that client's partition and used only as its BAA and contract permit. Client data must not be sent to a new subcontractor or feature without the check in POL-01 4.8. (AC-21; PR.DS-10; 164.502(a)(3); 164.504(e))

4.4 **Interfaces.** Every interface that brings data into or out of the CAD or revenue cycle platform must be in the interface register with a list of permitted fields. Fields outside the list must be filtered. (AC-4; CA-3; PR.DS-10)

4.5 **Card data.** Card numbers must not be spoken to, written down by, or stored in recordings by contact center agents once tone-masked keypad entry is live (target 2027-03-31). Until then, recordings must be paused during payment and checked monthly for card numbers. (SC-28; AU-9; PR.DS-01)

4.6 Backups of Restricted information must be immutable, held with a different provider or account from production, and restore-tested at least quarterly for High-criticality systems. (CP-9; PR.DS-11; 164.308(a)(7)(ii)(A))

4.7 Media holding Restricted information, including retired tablets, MDC drives, and router storage, must be sanitized or destroyed with a certificate. (MP-6; ID.AM-08; 164.310(d)(2)(i))

4.8 Information must be retained per the group records schedule: CAD incident records 7 years; patient care records at least as long as each state's EMS rules require (Florida worked example: 5 years, Rule 64J-1.014, F.A.C.) and 7 years for Medicare documentation (42 CFR 424.516(f)); revenue cycle file transfer copies no longer than 14 days. (SI-12)

4.9 Restricted information must not be entered into any AI tool unless the tool is approved under the Group AI Standard and covered by a BAA (or subcontractor agreement) that prohibits training on group or client data. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-4, AC-21, CA-3, CM-8) and monthly recording checks.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP; P10 Group AI Standard.
