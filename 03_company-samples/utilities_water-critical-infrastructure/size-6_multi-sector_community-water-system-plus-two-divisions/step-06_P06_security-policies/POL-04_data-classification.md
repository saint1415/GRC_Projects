# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer, with the Group CISO |
| Approved by | Group CISO and Group Chief Privacy Officer under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-4, SC-8, SC-13, SC-28, CP-9, MP-6, MP-7, SI-12 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory drivers | C-WATER-R01 (300i-2(d)); N23-R03 (NIST SP 800-171 3.1.3, 3.8.7, 3.13.11, 3.13.16); N56-R07 (FAR 52.204-21(b)(1)(vii)); N56-R01 (16 CFR 682.3) |
| Division supplements | Water Utility: RRA, ERP, and SCADA design records. Construction: CUI marking and enclave-only handling. Environmental Services: client data and federal tenants |

## 1. Purpose
Classify group information by sensitivity and by whose it is, and set handling rules so that critical infrastructure details, covered defense information, client data, and personal information stay where they belong.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including OT configuration and controller logic.

## 3. Classes
| Class | Examples | Where it may live |
|---|---|---|
| **Restricted: regulated** | Covered defense information (CUI); FCI | CUI only in SYS-C2; FCI in systems that meet FAR 52.204-21 |
| **Restricted: critical infrastructure** | RRAs, ERPs, SCADA network diagrams, OT asset inventories, credentials, PLC logic | Restricted repositories and OT systems; offline backup media |
| **Confidential** | Customer and employee personal information, client compliance data, bid data | Approved systems with encryption and role-based access |
| **Internal** | Procedures, schedules | Group systems |
| **Public** | Published notices, consumer confidence reports | Anywhere |

## 4. Policy statements
4.1 Every dataset and repository must have an owner who assigns its class. (RA-2; ID.AM-07)

4.2 Covered defense information may be stored, processed, and transmitted only inside the CUI enclave (SYS-C2). It must never be copied to laptops, removable media, SYS-C1, or email outside the enclave. Transfers to subcontractors must use the enclave's transfer service, which uses FIPS-validated cryptography. (AC-4; MP-7; SC-13; NIST SP 800-171 3.1.3, 3.8.7, 3.13.11)

4.3 Restricted critical infrastructure records must be kept in restricted repositories with access limited to named roles, and shared outside the group only with the approval of the record owner. RRAs and ERPs must be retained for at least 5 years after each certification. (AC-3; SC-28; SI-12; 42 U.S.C. 300i-2(d))

4.4 Restricted and Confidential information must be encrypted at rest and in transit. (SC-8; SC-28; PR.DS-01; PR.DS-02)

4.5 FCI from federal remediation sites must be tagged by tenant on SYS-E1 so that FAR 52.204-21 controls can be shown per contract. (AC-3; FAR 52.204-21(b)(1)(i))

4.6 Client data on SYS-E1 may be used only to deliver that client's service, and must be returned or deleted within 60 days of contract end with a certificate. (AC-3; SI-12)

4.7 PLC logic, HMI projects, and OT server images must be backed up to encrypted offline media monthly and after every change, and verified against the running configuration. Cloud data must be backed up to the immutable vault. (CP-9; PR.DS-11)

4.8 Media must be sanitized or destroyed before disposal or reuse. Consumer reports from background checks must be disposed of by shredding or secure erasure (16 CFR 682.3). (MP-6; PR.DS-01)

4.9 Information must be retained according to the group records schedule and then destroyed. (SI-12; PR.DS-10)

## 5. Compliance and enforcement
Checked through P07 (AC-4, SC-13, CP-9) and the CUI discovery scans run each quarter. Violations are handled under POL-01 4.7.

## 6. Exceptions
Exceptions follow POL-01 4.10. No exception may permit covered defense information outside SYS-C2.

## 7. Related documents
POL-01; POL-02; POL-05; group records schedule; `division-supplements.md`.
