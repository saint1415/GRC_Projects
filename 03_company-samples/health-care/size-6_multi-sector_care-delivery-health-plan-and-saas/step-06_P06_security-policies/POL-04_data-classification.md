# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, PT-2, PT-3, AC-4, AC-21, CM-8, SC-8, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| HIPAA | Security Rule 164.310(d); 164.312(a)(2)(iv), (e); 164.308(a)(7)(ii)(A). Privacy Rule 164.502(a)(3), (b); 164.506(c); 164.514(b), (d) |
| Division supplements | Care Delivery: clinical images and device data. Health Plan: member NPI and MA enrollee records (42 CFR 422.118). SaaS: customer PHI and de-identification rules |

## 1. Purpose
Classify group information by sensitivity and by whose data it is, and set handling rules so that each covered entity's PHI and each customer's PHI is used only for its permitted purpose.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including on shared platforms such as the Group Data Platform.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes, the purpose catalog, and minimum-necessary protocols |
| Data owners | Classify and tag datasets; approve feeds and access |
| Group data platform director | Enforces tags and purposes in the platform |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (PHI, customer PHI, member nonpublic personal information, credentials, and keys), **Confidential**, **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest and in transit with approved algorithms and group-managed keys. (SC-28; SC-8; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv); 164.312(e)(2)(ii))

4.3 **Tagging.** Every dataset holding PHI on a shared platform must carry tags for the covered entity (or customer) it belongs to and its permitted purpose (treatment, payment, health care operations, or de-identified). Untagged datasets must not be queryable after 2027-01-31. (PT-2; PT-3; CM-8; ID.AM-07; 42 CFR 422.118(a))

4.4 **Between covered entities.** One covered entity's PHI may be disclosed to the other only under a documented permission (for example 164.506(c)) and, for routine and recurring feeds, a written minimum-necessary protocol approved by both Privacy Officers. (AC-21; PT-3; PR.DS-10; 164.502(b); 164.514(d)(3))

4.5 **De-identification** must use the expert determination or safe harbor method (164.514(b)). SaaS customer PHI may be de-identified only where the customer's BAA permits it, and must be de-identified inside SYS-D3 before it leaves the SaaS. (PT-2; AC-4; 164.502(a)(3))

4.6 Backups of Restricted information must be immutable, held with a different provider or account from production, and restore-tested at least quarterly for High-criticality systems. (CP-9; PR.DS-11; 164.308(a)(7)(ii)(A))

4.7 Media holding Restricted information must be sanitized or destroyed with a certificate. (MP-6; ID.AM-08; 164.310(d)(2)(i))

4.8 Information must be retained per the group retention schedule. Copies in staging areas must be purged within 7 days. (SI-12)

4.9 Restricted information must not be entered into any AI tool unless the tool is approved under the Group AI Standard and covered by a BAA (or subcontractor agreement) that prohibits training on group or customer data. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-3, AC-4, PT-3, CM-8) and platform tag coverage reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP for the Group Data Platform; P10 Group AI Standard.
