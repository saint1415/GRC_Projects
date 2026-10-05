# Information Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Compliance Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions. CIP-003-9 R1 content is also approved by the CIP Senior Manager at least once every 15 calendar months |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-6, AC-21, MP-3, MP-6, SC-8, SC-28, PL-4 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10 |
| Regulatory basis | CIP-011-3; CIP-004-7 R6; CIP-012-2; 18 CFR 388.113; FERC Security Program 3.2, 3.4.3.4, 8.0; Form 1 Q22; Fla. Stat. 501.171 (worked example) |

## 1. Purpose
Classify the company's information and set handling rules, so that information useful for planning an attack on a dam or the grid (CEII, BCSI, FERC security documents) stays with people who need it, and personal and client information is protected.

## 2. Scope
All Cris Santos Company workforce members (employees, seasonal staff, contractors, and interns) at the headquarters, 14 offices, two Hydro Operations Centers, the Contract Operations Center, and all 46 developments in Georgia, Alabama, North Carolina, South Carolina, Tennessee, and Virginia, including the Piedmont developments from their acquisition date. Covers all systems and data: IT, OT (fleet SCADA, plant control, spillway and gate control, dam safety instrumentation and warning), cloud, colocation, SaaS, and systems that vendors operate for the company, and the services the company offers to external clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Compliance Officer | Owns this policy and STD-04.4 |
| Director, NERC Compliance | BCSI program (CIP-011-3) |
| Vice President, Corporate Security | FERC security documents |
| Vice President, Dam Safety | Dam safety records and inundation maps |
| Information owners | Classify and authorize access |
| All workforce | Handle information by its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategories. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as Restricted (CEII, BCSI, and FERC security documents), Confidential (personal information, client data including client CEII, financial data), Internal, or Public. (RA-2; ID.RA-04; ID.RA-05)
4.2 Restricted information must be stored only in approved repositories with named access. Access to BCSI must be authorized under CIP-004-7 R6 and verified at least every 15 calendar months. (AC-3; AC-6; PR.AA-05; PR.IR-01)
4.3 Restricted information may be shared outside the company only with the information owner's authorization and a signed handling agreement, and never through general file shares or folders shared with contractors. (AC-21; PR.AA-05)
4.4 FERC security documents and certification letters must be marked "Privileged - Security Sensitive Material"; filings with FERC that contain CEII must include a CEII request and justification. (MP-3; PR.DS-01)
4.5 Restricted and Confidential information must be encrypted at rest and in transit; real-time data between Control Centers must be protected under CIP-012-2. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.6 Storage media must be sanitized or destroyed before reuse or disposal, with records kept. (MP-6; PR.DS-01)
4.7 Client data from SL-1 and SL-2 must be kept separate per client and used only for that client's service. (AC-3; PR.AA-05; PR.IR-01)
4.8 Restricted or Confidential information must not be entered into any AI tool unless the AI council has approved that tool for that class. (PL-4; SA-9; GV.PO-01; GV.SC-04; GV.SC-05)
4.9 Data loss prevention scans for BCSI and CEII must run monthly across file shares and collaboration sites, and findings must be fixed within 10 business days. (AU-6; SI-4; PR.PS-04; DE.AE-02; DE.CM-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup and Logic Copy Standard
- STD-04.4 CEII and BCSI Handling Standard
- PRC-04.1 Restricted Information Access Authorization Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the NERC internal controls program, the annual Internal Audit assessment (P07), and access verifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. An exception cannot excuse a NERC CIP requirement.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 HFCDMS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
