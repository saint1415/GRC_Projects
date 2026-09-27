# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or product launches |
| Implements (SP 800-53 Rev. 5) | SC-1, MP-1, RA-2, SC-8, SC-28, SC-13, AC-3, SI-12, AC-21, SA-9, RA-5(11), SI-7, CM-14, CP-9, CP-9(1), MP-6, PM-5(1) |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory basis | HIPAA 164.312(a)(2)(iv), (c), (e) (N62-R01); 16 CFR 318 (N62-R06); FD&C Act 524B(b)(2) (N31-33-R05); Fla. Stat. 501.171(8) |

## 1. Purpose
Classify company, customer, patient, and consumer information so each class gets the right protection, and set handling rules for the data types specific to a device maker: PHI held for customers, consumer health data, source code, SBOMs and vulnerability data, and signing keys.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at every site: headquarters, the FL-1, MN-1, and TX-1 plants, the R&D centers, the RCM monitoring centers, and remote work, including the acquired infusion business from its acquisition date. Covers all systems and data, including cloud, colocation, SaaS, plant OT, the Device Software Factory, and systems that business associates, contract manufacturers, and other vendors operate for the company, and the products and services the company provides to customers and consumers (fielded devices, the DDC, the RCM service, and the consumer companion app).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns the classification scheme; PHI and consumer health data rules |
| VP Product Security | Vulnerability data and embargoed information |
| Director of Build and Release Engineering | Key material and released artifacts |
| Data owners | Classify and approve access |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 All information must be classified as Restricted, Confidential, Internal, or Public. Restricted includes PHI held for customers, consumer health data, signing and PKI keys, and embargoed vulnerability details. (RA-2; ID.AM-05)
4.2 Restricted and Confidential data must be encrypted in transit with TLS 1.2 or higher and at rest with company-managed keys. New products must not use weaker protocols. (SC-8; SC-28; SC-13; PR.DS-01)
4.3 PHI may be used only for the services in the customer's BAA, and retained only as long as the BAA allows (24-month rolling retention for the DDC unless the BAA states otherwise). (AC-3; SI-12; PR.DS-01)
4.4 Consumer health data may be shared with a third party only at the user's direction or with a processor under contract that is told of the company's status under 16 CFR Part 318. Third-party software kits in the app must be approved under STD-04.4 before release. (AC-21; SA-9; GV.SC-05)
4.5 Vulnerability details must be kept Restricted until the agreed disclosure date; SBOMs are Confidential and shared with customers under the customer security guide terms. (AC-3; RA-5(11); PR.DS-01)
4.6 Released firmware and software must be integrity-protected by signature from build to device, and signatures must be verified before installation at every station and device. (SI-7; CM-14; PR.DS-10)
4.7 Backups of Restricted data must be encrypted, immutable, and restore-tested at least quarterly for tier-1 systems. (CP-9; CP-9(1); PR.DS-11)
4.8 Media containing Restricted or Confidential data must be sanitized or destroyed with certificates; HSMs must be zeroized under dual control. (MP-6; PR.DS-01)
4.9 Data used for analytics or AI training must be de-identified or approved by the AI governance committee and registered under PRC-04.1; PHI and consumer data must not be used to train models without a documented legal basis and customer or user permission. (AC-3; PM-5(1); ID.AM-07)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Consumer Health Data Standard
- PRC-04.1 Data Set Registration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 DSF-MES SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.
