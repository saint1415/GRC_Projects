# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Compliance Manager (Privacy Officer) for PHI; VP Engineering for product data |
| Approved by | COO |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-6, SC-8, SC-12, SC-28, SI-12, CP-9, CM-8 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| Regulatory basis | HIPAA Security Rule for the device cloud, 164.310(d); 164.312(a)(2)(iv), (e); 164.308(a)(7)(ii)(A) (N62-R01); FD&C Act 524B(b)(2)-(3) for signing keys and SBOMs (N31-33-R05) |

## 1. Purpose
Classify company and customer information by sensitivity and set handling rules, so protection matches the harm a disclosure or alteration would cause.

## 2. Scope
All workforce members and all information the company creates or receives, in any system, including PHI the device cloud holds for hospitals, device design data, source code, and cryptographic keys.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Compliance Manager (Privacy Officer) | Owns the classification of PHI; approves new uses of PHI |
| VP Engineering | Owns the classification of source code, design files, signing keys, and SBOMs |
| IT Manager and Cloud Operations Lead | Implement encryption, backup, and disposal controls |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | PHI in the device cloud; firmware code-signing keys; device certificate authority keys; production credentials | Encrypted at rest and in transit; minimum necessary; approved systems only; keys in hardware or managed key services |
| **Confidential** | Source code; design history files; unfixed vulnerability details; SBOMs; complaint records; contracts | Encrypted in transit; need-to-know; not shared outside the company without an NDA or BAA |
| **Internal** | Procedures; production schedules; training | Workforce only |
| **Public** | Published CVD policy; customer security guide; published advisories | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted data must be encrypted at rest and in transit. External transfers of PHI must use TLS 1.2 or higher or an approved secure transfer. (SC-28; SC-8; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv); 164.312(e)(2)(ii))
4.3 **Signing keys.** Firmware code-signing private keys must be generated and held in a hardware security module or a managed key service with non-exportable keys. Backup key shares must be held by two officers. Keys must never be stored as files on build servers or workstations. (SC-12; FD&C Act 524B(b)(2))
4.4 PHI may be stored only in the device cloud database and object storage and in approved vendor services with a subcontractor BAA. PHI must be masked or removed before logs leave the device cloud. PHI must never be kept on laptops, in email, or in personal accounts, except incidental identifiers in eQMS complaints and support tickets. (AC-3; 164.308(b)(1))
4.5 Unfixed vulnerability details are Confidential until the coordinated public disclosure date. (RA-5(11))
4.6 The IT Manager must keep an inventory of where Restricted data is stored and which vendors receive it. Engineering must keep a machine-readable SBOM for each device and device cloud release. (CM-8; ID.AM-07)
4.7 Media and devices holding Restricted or Confidential data must be wiped (for reuse) or destroyed by a certified vendor that provides a certificate of destruction (for disposal). Returned monitors must have their local trend buffer erased before refurbishment. (MP-6; ID.AM-08; 164.310(d)(2)(i)-(ii))
4.8 Backups of Restricted data must be encrypted, stored apart from production administrators (a separate account with separate roles), protected from alteration, and restore-tested at least quarterly. (CP-9; PR.DS-11; 164.308(a)(7)(ii)(A))
4.9 Restricted and Confidential data must not be entered into AI tools unless the tool is on the approved list (P10 and POL-05). PHI requires a BAA with the AI vendor as well. (SA-9)
4.10 PHI is deleted after the 24-month retention period set in the BAAs. Security documentation is retained for 6 years (POL-01 4.11). QMS records follow QMS retention. (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.8. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved at the level set in POL-01 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-02; POL-05; P10 approved AI tools list; BAAs; code-signing procedure; QMS record retention procedure
