# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group CISO, with the Vice President, Rail Security for SSI |
| Approved by | Group CISO |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | AC-3, AC-21, MP-3, MP-6, SC-8, SC-28, SI-12 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10 |
| TSA and other | 49 CFR 1520.9(a), 1520.7(k); SD 1580/82-2022-01E IV.B; FAR 52.204-21(b)(1)(vii); Fla. Stat. 501.171(2), (8) |

## 1. Purpose
Classify group information so that each kind gets the protection the law, the directives, and contracts require.

## 2. Scope
All information the group creates or holds, in any form, in every division.

## 3. Classification levels
| Level | Examples | Minimum handling |
|---|---|---|
| **SSI** (Sensitive Security Information) | CIP, CAP and its results, reports to TSA and CISA, vulnerability assessments, hazmat security plans, security-relevant rail drawings | Marked; only covered persons with a need to know; stored in the restricted SSI library; never in general file shares or email to outsiders; disposed of as part 1520 requires |
| **Restricted** | Employee medical and certification records, guarantor financial statements, driver records, PTC keys, FCI | Named-role access; encrypted at rest and in transit; logged access |
| **Confidential** | Contracts, pricing, network diagrams that are not SSI, customer data | Need-to-know access; encrypted in transit |
| **Internal** | Policies, procedures, routine operational data | Workforce only |
| **Public** | Published tariffs, website content | Approved for release |

## 4. Policy statements
4.1 Every dataset and document repository must have an owner who classifies it. (ID.AM-05; RA-2)

4.2 **SSI** may be disclosed only to covered persons with a need to know. Group employees and contractors who handle railroad SSI are covered persons (49 CFR 1520.7(k)) wherever they sit in the group. SSI must be stored in the restricted SSI library, which only the roles named by the Vice President, Rail Security can open. Plans, reports, and assessment results under the directives must be stored and transmitted as part 1520 requires (SD IV.B). (AC-3; AC-21; MP-3; PR.DS-01)

4.3 Documents shared outside the group (right-of-way licensees, vendors, customers) must be screened for SSI before release using the rail security checklist. (AC-21; PR.DS-01)

4.4 Restricted information must be encrypted at rest and in transit and accessed by named roles only. (SC-8; SC-28; PR.DS-01; PR.DS-02)

4.5 FCI must be kept in the federal contracts workspace and the ERP; media holding FCI must be sanitized or destroyed before disposal or reuse, with a record. (MP-6; FAR 52.204-21(b)(1)(vii))

4.6 Integration and transfer platforms are not storage. Files with personal information passed through SYS-G5 must be deleted from the transfer store within 7 days of successful delivery. (SI-12; PR.DS-10)

4.7 Records with personal information must be disposed of when no longer retained, by shredding, erasing, or otherwise making them unreadable (Fla. Stat. 501.171(8) worked example). (SI-12; MP-6)

4.8 Guarantor financial statements and employee medical records must not be kept in email or shared mailboxes. (AC-3; PR.DS-01)

## 5. Compliance and enforcement
Checked through the P07 assessment (AC-21) and access reviews of the SSI library.

## 6. Exceptions
Exceptions follow POL-01 section 4.12. No exception may permit SSI disclosure that part 1520 does not allow.

## 7. Related documents
POL-01; POL-02; 49 CFR part 1520; P08 notification matrix.
