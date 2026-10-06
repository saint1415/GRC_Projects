# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, PT-2, PT-3, AC-4, AC-21, CM-12, SC-8, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory anchors | 8 CFR 274a.2(b)(2), (b)(4), (g); 16 CFR 682.3; 29 CFR 1630.14(b)(1); Fla. Stat. 501.171(2), (8); HIPAA 164.502(b), 164.514(d), 164.310(d), 164.312(a)(2)(iv), (e); 42 CFR 484.110(c)-(d); FAR 52.204-21(b)(1)(vii) |
| Division supplements | Staffing: client submittals and MSP program data. Consulting: client PHI and federal contract information. Home Health: patient data outside the EHR |

## 1. Purpose
Classify group information by sensitivity and by whose data it is, and set handling rules so that each kind of record is used only for its purpose and destroyed when no longer needed.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including on the Group Workforce Platform and in client and agency systems that group workforce members use.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes, the processing register, the retention schedule, and minimum-necessary protocols |
| Data owners | Classify data; approve feeds and access |
| Group workforce platform director | Enforces classes and retention in the GWP |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted**, **Confidential**, **Internal**, or **Public**. Restricted includes SSNs, bank account numbers, Form I-9 records and document images, E-Verify case data, consumer reports, medical screening files, PHI (Home Health's and clients'), federal contract information, credentials, and keys. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest and in transit with approved algorithms and group-managed keys. SSNs and bank account numbers must be tokenized in the payroll engine and masked in user interfaces. (SC-28; SC-8; PR.DS-01; PR.DS-02; Fla. Stat. 501.171(2); 164.312(a)(2)(iv))

4.3 **Data map.** Every system that stores Restricted information must be on the GWP or division data map with its location, owner, and purpose. (CM-12; PT-3; ID.AM-07)

4.4 **Purpose and minimum necessary.** Restricted information may be shared between divisions or with corporate only for a purpose recorded in the processing register. Patient data must not leave Home Health systems except as HIPAA permits and only the minimum necessary; a routine feed needs a written protocol approved by the Home Health HIPAA Privacy Officer. Payroll must receive visit records that identify the visit, not the patient. (AC-4; AC-21; PT-2; PT-3; 164.502(b); 164.514(d)(3))

4.5 **Use limits by record type.** Form I-9 information may be used only for the purposes 8 CFR 274a.2(b)(4) allows. E-Verify information may be used only to confirm employment eligibility (MOU Art. II.A.15). Medical screening files must be kept separate from other personnel files (29 CFR 1630.14(b)(1)). Client PHI may be used only as the client's BAA permits. Federal contract information stays in the Federal Solutions enclave. (PT-3; AC-3)

4.6 Backups of Restricted information must be immutable, held with a different provider or account from production, and restore-tested at least once a year for High-criticality systems. (CP-9; PR.DS-11; 8 CFR 274a.2(g)(1)(ii); 164.308(a)(7)(ii)(A))

4.7 Media holding Restricted information must be sanitized or destroyed with a certificate. Consumer report information must be disposed of by shredding, erasing, or destroying it so it cannot be read or reconstructed. (MP-6; ID.AM-08; 16 CFR 682.3; Fla. Stat. 501.171(8); FAR 52.204-21(b)(1)(vii))

4.8 **Retention.** Records must be kept per the group retention schedule (for example: Form I-9 for 3 years after hire or 1 year after employment ends, whichever is later; Home Health clinical records 5 years after discharge unless state law requires longer) and deleted automatically when the period ends. Candidate profiles inactive for 4 years must be deleted unless the law requires longer. (SI-12; 8 CFR 274a.2(b)(2); 42 CFR 484.110(c))

4.9 Restricted information must not be entered into any AI tool unless the tool is approved under the Group AI Standard, and for PHI, covered by a BAA or subcontractor agreement that prohibits training on group or client data. (SA-9; PL-4)

4.10 Consulting must label and purge client PHI in the engagement repository at engagement close, or return it, as the BAA requires. (SI-12; 164.504(e)(2)(ii)(J))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-4, PT-3, CM-12) and data discovery scans.

## 6. Exceptions
Exceptions follow POL-01 section 4.11.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP for the Group Workforce Platform; P10 Group AI Standard.
