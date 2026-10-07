# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, AC-4, AC-21, PT-2, PT-3, SC-8, SC-28, SI-12, MP-6 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02 |
| Regulatory basis | 16 CFR 314.4(c)(2), (c)(3), (c)(6); 34 CFR 99.3, 99.31, 99.33; HEA sec. 483; 16 CFR 312.10; 45 CFR 164.502, 164.514(d) |

## 1. Purpose
Tell every workforce member how sensitive each kind of data is, who owns it, what law governs it, and how it must be handled, stored, shared between divisions, and destroyed.

## 2. Scope
All data the group creates, receives, maintains, or transmits, in any form, in every division and in shared services.

## 3. Classes
| Class | Examples | Core handling |
|---|---|---|
| **Restricted** | Customer information under 16 CFR 314.2 (SSNs, bank details, aid and loan data); FAFSA and ISIR data and federal tax information-derived data; PHI of nonstudent patients; student treatment and counseling records; children's personal information on the District Platform; authentication secrets | Encrypt at rest and in transit; access by named role only; no transfer outside approved systems; logged access |
| **Confidential** | Education records generally (grades, enrollment, advising notes); employee records; customer contract data; non-public financials | Encrypt in transit; role-based access; share only with a legal basis |
| **Internal** | Policies, procedures, internal communications | Workforce only |
| **Public** | Catalogs, published notices, marketing | Approved for release |

## 4. Policy statements
4.1 Every data set in a shared platform must have a named data owner, a class, a governing law (FERPA, Safeguards Rule, HEA sec. 483, COPPA, HIPAA, contract), and a permitted purpose recorded in the catalog. Untagged data is handled as Restricted. (RA-2; CM-8; PT-3; ID.AM-07; 314.4(c)(2))

4.2 Data owners are: the university registrar (education records), the executive director of financial aid and the college chief financial officer (aid and student financial data), each customer institution (its tenant data, with Education Software as its contractor), the Student Health Privacy Officer (clinic records), and the Group HR director (employee data). (PM-2; GV.RR-02)

4.3 Restricted and Confidential data must be encrypted in transit over external networks, and Restricted data must be encrypted at rest. Any exception for the college's customer information needs compensating controls approved in writing by the Qualified Individual. (SC-8; SC-28; PR.DS-01; PR.DS-02; 314.4(c)(3))

4.4 **Data sharing between divisions.** Moving data from one division to another is a disclosure, not an internal use. Every recurring flow between divisions needs a written data-sharing approval signed by both data owners that states the legal basis (for example a FERPA exception under 34 CFR 99.31, a HIPAA permission under 164.502, or a contract), the minimum fields needed, retention, and recipients. Flows involving clinic data also need the Student Health Privacy Officer's sign-off. The change board must reject any interface without this approval. (AC-4; AC-21; PT-2; 34 CFR 99.31(a)(1); 99.33(a); 164.502(a); 164.514(d))

4.5 **Treatment records** (student clinic and counseling records) must stay within Student Health and be disclosed only to people providing treatment or with the student's written consent or another FERPA exception. Records of students of contracting colleges must never leave Student Health except as that college directs. (AC-21; PT-3; 34 CFR 99.3; 99.33(a))

4.6 **FAFSA and federal tax information-derived data** may be used only for the application, award, and administration of student aid. It must not be used as an input to admissions, student-success, or marketing models, and access outside the financial aid role is prohibited. (PT-3; AC-3; HEA sec. 483)

4.7 **Children's personal information** on the District Platform may be collected only under district authorization for the school's educational purpose or with verifiable parental consent, used only for that purpose, and deleted within 90 days after a district contract ends, as the published retention policy states. Material changes, such as new AI processing, need fresh authorization. (PT-3; SI-12; 312.5(a)(1); 312.10)

4.8 **Retention and disposal.** Each data set follows the group records schedule. The college's customer information must be disposed of no later than 2 years after its last use in providing a service to the student, unless it is needed for business operations or required by law (for example, Title IV record retention), and the schedule must be reviewed every year. Media must be sanitized under NIST SP 800-88 Rev. 2. (SI-12; MP-6; ID.AM-08; 314.4(c)(6))

4.9 **Clinic record status.** Student Health must record for every patient record whether it is PHI or a FERPA record and, for students, which institution it belongs to, so that access reviews and breach scoping apply the right law. (CM-8; PT-2; 164.404; 34 CFR 99.3)

4.10 Restricted data may be entered into an AI tool only if the tool is on the approved list, the vendor is contractually barred from training on it, and the use is registered under POL-01 4.12. (PT-3; SA-9)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through catalog coverage reports, interface approvals, and the P07 assessment (PT-3, CM-8, AC-4, SI-12).

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may permit a disclosure the law does not allow.

## 7. Related documents
POL-01; POL-02; POL-05; group records schedule; `division-supplements.md`; P02 SSP section 8.
