# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer, with the Group General Counsel for client and contract data |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, AC-21, CM-8, SC-8, SC-12, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory basis | HIPAA 164.312(a)(2)(iv), (e); 164.308(a)(7)(ii)(A) for the DCC (N62-R01); 48 CFR 52.204-21(b)(1)(i), (vii) (N42-R04); EAR (N31-33-R04); 524B(b)(2) for signing keys |
| Division supplements | Medical Devices: signing material and PSIRT embargo data. Distribution: Federal contract information enclave. Testing: client data, findings, and intake scanning |

## 1. Purpose
Classify group information by sensitivity and by whose information it is, and set handling rules so that PHI, client data, federal contract information, and signing material are each handled as their owners and the law require.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including on plant, warehouse, and laboratory systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes and handling rules |
| Data owners | Classify and label datasets; approve sharing |
| Chief Product Security Officer | Owns handling of embargoed vulnerability data and signing material |
| Testing laboratory quality director | Owns client data handling and intake checks |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (PHI; signing keys and credentials; unpublished vulnerability details, including Testing findings; testing client confidential data; export-controlled technology), **Confidential** (designs, source code, Federal contract information, business plans), **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest and in transit with approved algorithms and group-managed keys. Signing keys must be generated and held in HSMs; software keys are prohibited for production signing after 2027-03-31. (SC-28; SC-8; SC-12; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv); 164.312(e)(2)(ii))

4.3 **Testing client data** must be stored only in the LIMS, the client portal, or the findings vault, separated by client, and never copied to collaboration spaces reachable by other divisions. (AC-4; AC-21; PR.DS-10)

4.4 **Intake checks.** Files submitted to Testing must be scanned for PHI and for export control markings before release to engineers. PHI found must be quarantined and returned or destroyed, and the client told. (RA-2; SI-12; ID.AM-07)

4.5 **Federal contract information** must be held only in the Distribution FCI enclave (ERP federal module and the labeled FCI library) and shared only with subcontractors whose agreements include the FAR 52.204-21 flowdown. (AC-3; AC-21; 52.204-21(b)(1)(i), (c))

4.6 **Embargoed vulnerability details** may be shared only with people who need them to fix, verify, or coordinate disclosure, until the agreed disclosure date. (AC-21; PR.DS-10)

4.7 Backups of Restricted information must be immutable, held with a different provider or account from production, and restore-tested at least quarterly for High-criticality systems. Plant MES backups are included. (CP-9; PR.DS-11; 164.308(a)(7)(ii)(A))

4.8 Media holding Restricted or Confidential information must be sanitized or destroyed with a certificate. (MP-6; ID.AM-08; 164.310(d)(2)(i); 52.204-21(b)(1)(vii))

4.9 Information must be retained per the group retention schedule; QMS records follow the QMS schedule. (SI-12)

4.10 Restricted or Confidential information must not be entered into any AI tool unless the tool is approved under the Group AI Standard, the contract prohibits training on group data, and, for Testing client data, the client has agreed in writing. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.14. Compliance is checked through the P07 assessment (AC-3, AC-4, SC-12, SC-28, CP-9) and intake scanning reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP for DEMS; P10 Group AI Standard.
