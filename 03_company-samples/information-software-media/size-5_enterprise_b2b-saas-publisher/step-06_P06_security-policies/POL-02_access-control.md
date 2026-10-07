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
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-6(9), AC-17, IA-1, IA-2, IA-2(1), IA-5, IA-5(7), IA-8, PS-4, AU-10 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Regulatory drivers | FTC Act Section 5 (N51-R01); customer DPA; CCPA cybersecurity audit components (Cal. Code Regs. tit. 11, 7123(c)(1)) |

## 1. Purpose
Make sure only authorized people and software reach the company's and its customers' information, only to the extent their role requires, and that access ends promptly when it is no longer needed. Workforce access to customer tenants is treated as the most sensitive access the company grants.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and vendor agents with company accounts) in every office and remote location, including acquired companies from their acquisition date. Covers all systems and data, including the Operations Cloud, Data Cloud, Government Edition, AQ-01, cloud accounts, SaaS, endpoints, and systems that sub-processors and other vendors operate for the company. Where the Government Edition's FedRAMP package sets a stricter requirement, the stricter requirement applies inside its boundary.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-04) and identity governance |
| Managers and system owners | Approve access; complete quarterly certifications |
| Vice President, Customer Support | Owns the tenant access tool rules and session review |
| Chief People Officer | Timely joiner, mover, and leaver events, including contractor end dates |
| Vice President, Integration Management Office | Brings acquired-company identities onto the identity platform |
| Customer administrators | Manage their own users under the MSA |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every person and every service must have a unique identity. Shared workforce accounts are prohibited; every non-human identity must have a named human owner. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Engineers must not approve or promote their own changes to production, and tenant access approvers must not approve their own sessions. (AC-5; PR.AA-05)
4.4 All workforce sign-ins must use phishing-resistant MFA. Customer administrator roles must use MFA. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.5 Access must be disabled the same business day as a termination or contract end date, and immediately for involuntary terminations. (PS-4; AC-2; PR.AA-05)
4.6 Workforce accounts inactive for 45 days must be disabled automatically; non-human identities unused for 90 days must be disabled or removed. (AC-2(3); PR.AA-05)
4.7 Managers must certify their staff's access every quarter, and owners must certify their non-human identities every quarter. (AC-2; PR.AA-05)
4.8 Privileged access to production must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.9 Workforce access to customer tenant data must go only through the tenant access tool, must be linked to a customer ticket, must be recorded, and, from 2027-01-31, must have customer approval for Enterprise tenants unless the customer has given standing approval in writing. (AC-3; AU-10; PR.AA-05)
4.10 Long-lived static cloud access keys are prohibited for pipelines and services; secrets must be stored in the secrets manager and must never be committed to source repositories. A secret found in a repository must be revoked within 24 hours. (IA-5; IA-5(7); PR.AA-01)
4.11 Two sealed break-glass accounts per cloud organization must exist, be tested quarterly, and have every use reviewed by the Director of Security Operations. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account and Non-Human Identity Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Tenant Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Tenant Access Procedure
- PRC-02.5 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the quarterly public statement review. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 OCP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
