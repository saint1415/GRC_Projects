# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or CMMC scope changes |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-4, AC-5, AC-6, AC-17, AC-20, IA-1, IA-2, IA-2(1), IA-2(2), IA-3, IA-5, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| SP 800-171, CMMC, and other drivers | SP 800-171 Rev. 2 3.1.x, 3.5.x, 3.7.5, 3.9.2; ITAR 22 CFR 120.56; EAR 15 CFR 734.13(a)(2) |

## 1. Purpose
Make sure only authorized people, processes, and devices reach company information, only to the extent their role and export authorization allow, and that access ends promptly when it is no longer needed.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, temporary workers, and interns) at all 8 sites in Florida, Georgia, Alabama, Texas, Kansas, and Arizona and at the 2 data centers, including acquired operations from their acquisition date. Covers all company systems and data, including the government-community and commercial clouds, SaaS, plant OT, and systems that suppliers and service providers operate for the company, with added rules for the CUI Engineering Enclave (CEE) and the Manufacturing Operations Zone (MOZ). The classified information system at FL-1 also follows NISPOM and DCSA requirements, which prevail where stricter.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-01) and identity governance |
| Managers and system owners | Approve access; complete quarterly certifications |
| Vice President, Trade Compliance | Sets export attributes and approves any foreign-person access to controlled technology |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events |
| Vice President, Supply Chain | Contractor and supplier account sponsorship and separations |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user, service, and device must have a unique identity. Shared accounts are prohibited; shared shop-floor terminals must use badge plus PIN with individual sign-in. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. CEE access also requires U.S.-person verification or a documented export authorization. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Access to ITAR and EAR controlled technical data must be enforced by export attributes on every PLM folder, file share, and suite site. A migration must not go live until attributes are verified. (AC-3; AC-4; PR.AA-05)
4.4 Duties that would let one person both change and release engineering data, or both administer and review logs, must be separated in role design. (AC-5; PR.AA-05)
4.5 Phishing-resistant MFA is required for all CEE access and all privileged access; MFA is required for all other remote, cloud, and supplier access. (IA-2(1); IA-2(2); PR.AA-03)
4.6 Access must be disabled the same business day as a separation, including contractor separations, and immediately for involuntary separations. (PS-4; AC-2; PR.AA-05)
4.7 Accounts inactive for 45 days must be disabled automatically. (AC-2(3); PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and suspended when role-based training is 30 days overdue. (AC-6; AT-3; PR.AA-05)
4.9 Remote and vendor maintenance access, including equipment manufacturers, must go through the PAM vendor gateway with company MFA, approval, and session recording. Manufacturer remote tools outside PAM are prohibited. (AC-17; MA-4; PR.AA-05)
4.10 Only managed devices with valid certificates may connect to CEE and MOZ networks; unknown devices must be blocked or quarantined. (IA-3; CM-8(3); PR.AA-01)
4.11 CEE access is allowed only from company-owned, managed devices; connections to external systems are limited to the approved register. (AC-20; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Export Attribute Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CMMC readiness checks before each affirmation. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. A suspected unauthorized release of ITAR or EAR technical data is also referred to the Vice President, Trade Compliance for a voluntary disclosure decision.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 CEE SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
