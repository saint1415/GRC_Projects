# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group CISO, with the Director of Federal Contracts Compliance for FCI and CUI |
| Approved by | Group CISO, under authority of POL-01 |
| Effective date | 2026-10-01 (approved 2026-09-15) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, AC-20, AC-21, AC-22, CM-8, CM-12, MP-3, MP-6, SC-8, SC-28, CP-9, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory drivers | N23-R01 FAR 52.204-21(a), (b)(1)(iii), (vii); N23-R03 DFARS 252.204-7012(b)(2)(ii)(D); N23-R04 DFARS 252.204-7021(d)(2); NIST SP 800-171 R2 3.8.4 (marking); FAR 52.222-8 (certified payroll); N53-R04 PCI DSS Requirement 3 (Property stores no account data) |
| Division supplements | Construction: field access to CUI drawings; certified payroll intake. Property: tenant and badge holder data; cardholder data stays with the parking provider. A&E: CUI design production; digital twin client data |

## 1. Purpose
Classify group information by sensitivity and by the rules that come with it, and set handling rules so that FCI and CUI stay on systems with the required status and payment and personal information is protected.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including drawings, specifications, pay applications, certified payrolls, bid documents, and building system data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Federal Contracts Compliance | Identifies FCI and CUI on each federal contract from the contract and its CUI marking guidance; keeps the CUI project list |
| Federal practice leaders (Construction and A&E) | Make sure CUI on their projects stays in the enclave |
| Data owners | Classify their data and approve sharing |
| PDPP system owner | Enforces CUI upload blocking and project data tags in the PDPP |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as:
- **CUI** (for example, controlled technical information in facility drawings and specifications on DoD projects);
- **FCI** (information provided by or generated for the Government under a contract and not intended for public release; FAR 52.204-21(a));
- **Restricted** (Social Security numbers and other personal information, bank and remittance details, credentials and keys, client facility security details, cardholder data);
- **Confidential** (bid pricing, client designs, contract terms);
- **Internal**; or
- **Public**.
(RA-2; ID.AM-07)

4.2 **CUI lives only in the enclave (SYS-G6).** CUI must be created, stored, processed, and shared only in the enclave or another system with the required CMMC Level 2 status and FedRAMP Moderate authorization or equivalent. It must never be placed in the PDPP, commercial email or files, the AI estimating assistant, or any other commercial service. (AC-4; AC-20; CM-12; DFARS 252.204-7012(b)(2)(ii)(D); 252.204-7021(d)(2))

4.3 **Field access to CUI.** Superintendents, field engineers, and subcontractors who need CUI drawings must use enclave virtual desktops (including from jobsite trailers) or enclave guest accounts. Exporting CUI from the enclave to a commercial system is prohibited, with no exception. Plots of CUI drawings must be made from enclave desktops, marked, and kept in locked plan storage. (AC-4; MP-3; PE-17; SP 800-171 R2 3.1.3, 3.8.4)

4.4 **FCI** may be stored and processed only on systems inside the CMMC Level 1 scope (the PDPP, SYS-G4, SYS-G5, and managed endpoints) or on external systems approved under POL-01 4.8. (AC-20; FAR 52.204-21(b)(1)(iii))

4.5 **CUI spills.** CUI found outside the enclave is a reportable incident under POL-03 4.4. The copies must be restricted at once and purged with a record of each removal. (IR-6; MP-6)

4.6 Restricted information must be encrypted at rest and in transit with approved algorithms. In the enclave, cryptography must be FIPS-validated. (SC-28; SC-8; SC-13; PR.DS-01; PR.DS-02)

4.7 **Certified payrolls and Social Security numbers.** Subcontractor certified payrolls must be received through the PDPP payroll intake, which masks Social Security numbers for project staff. They must not be requested or accepted by email. (AC-3; SC-8; FAR 52.222-8)

4.8 **Client facility security details** (camera and badge reader layouts, tenant security floors, client system configurations) must be shared only with users the project executive or the Systems Integration Director has approved for that client. (AC-21; PR.DS-10)

4.9 **Cardholder data** must not be stored on Property systems. It stays with the parking technology service provider. (SC-28; PCI DSS Requirement 3)

4.10 Backups of CUI, FCI, and Restricted information must be held with a different provider or account from production, protected against deletion, and restore-tested at least quarterly for High-criticality systems. (CP-9; PR.DS-11)

4.11 Media holding CUI or Restricted information must be sanitized or destroyed with a record. (MP-6; ID.AM-08; FAR 52.204-21(b)(1)(vii))

4.12 Information must be retained per the group retention schedule. At federal contract closeout, project copies of FCI and any CUI must be returned or destroyed as the contract requires. (SI-12)

4.13 FCI, CUI, Restricted, and Confidential information must not be entered into any AI tool unless the tool is approved under the Group AI Standard for that class. No AI tool is approved for CUI. (SA-9; PL-4)

4.14 Information posted publicly (websites, social media, marketing, drone and progress photos) must be reviewed so that no FCI, CUI, or client facility security details are posted. Photos of federal sites need the federal practice leader's approval. (AC-22; FAR 52.204-21(b)(1)(iv))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-4, CM-8, CM-12, AC-20), CUI discovery scans (at least quarterly), and the CMMC self-assessments.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may allow CUI outside the enclave.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; PDPP SSP (P02); enclave SSP; P10 Group AI Standard.
