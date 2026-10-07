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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(9), AC-17, IA-1, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Other requirements | PCI DSS v4.0.1 Requirements 7 and 8; HIPAA 164.308(a)(3), (a)(4), 164.312(a), (d) for SL-2 |

## 1. Purpose
Make sure only authorized people, services, and devices reach company systems, customer records, and payment systems, with no more access than their role needs, and that the people who pick up customers' devices are who they say they are.

## 2. Scope
All workforce, contractor, vendor, client (SL-1 and SL-2), and customer accounts on company systems, including the STPP, manufacturer portals used on the company's behalf, store POS and PIN pad administration, cloud consoles, and the AC legacy stack until it is retired.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Policy owner; runs the identity platform and identity governance |
| System owners | Approve role templates and certify access |
| Store managers | Enter HR events the same day; verify customer identity at release |
| Vice President, Integration Management Office | Brings AC accounts under this policy |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user must have a unique account. Shared accounts are prohibited, including on POS systems, the ticketing system, and manufacturer portals. (AC-2; IA-2; PR.AA-01)
4.2 Access must be granted by approved role templates on least privilege. The restricted passcode field may be viewed only by the technician assigned to the open ticket. (AC-3; AC-6; PR.AA-05)
4.3 MFA is required for all workforce access to company systems, all remote and administrative access, and all access into the cardholder data environment. Privileged access requires phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)
4.4 Access must be removed the same business day as termination. Managers must enter terminations in the HR system the same day. (AC-2; PS-4; PR.AA-01)
4.5 Access to the STPP, the cardholder data environment, and privileged roles must be certified quarterly; other access annually. (AC-2; PR.AA-05)
4.6 Privileged access must use PAM with just-in-time elevation and session recording. (AC-6(9); AC-6; PR.AA-05)
4.7 Vendor and remote support access must go through PAM. Unmanaged remote support tools are prohibited. (AC-17; MA-4; PR.AA-05)
4.8 Vendor default passwords must be changed before any device or application is used, including POS PCs, PIN pad administration menus, and sanitization stations. (IA-5; CM-6; PR.AA-01)
4.9 A device may be released only after the customer shows photo ID matching the ticket or gives the one-time code sent to the phone on file. (IA-8; PR.AA-02)
4.10 Break-glass accounts must be sealed, monitored, and tested quarterly. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, access certifications, the annual Internal Audit assessment (P07), and the annual PCI DSS ROC. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions to this policy follow the process in POL-01 section 7 and `policy-hierarchy.md` section 5: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, limited to 12 months, and recorded in the exception register with compensating controls.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 STPP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
