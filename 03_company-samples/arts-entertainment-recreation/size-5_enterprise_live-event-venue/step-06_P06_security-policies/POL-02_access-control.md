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
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-2(12), AC-6, AC-6(9), AC-17, IA-2, IA-2(1), IA-2(2), IA-4, IA-5, IA-5(1), MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory basis | PCI DSS v4.0.1 Requirements 7 and 8 (N71-R04); FTC Act Section 5 reasonable security (N71-R05) |

## 1. Purpose
Make sure only authorized people, services, and clients reach company systems and data, with the least access they need, strong authentication, and prompt removal.

## 2. Scope
All Cris Santos Company workforce members (employees, part-time and seasonal event staff, contractors, and interns) at headquarters, all 36 venues in 8 states, the 3 festivals, and the two contact centers, including acquired venues from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, venue operational technology, and systems that service providers and other vendors operate for the company, and the services the company offers to business clients (SL-1 white-label ticketing and SL-2 venue management).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Policy owner; runs the identity platform and identity governance |
| System owners | Approve roles and certify access |
| Client administrators | Manage their organization's client console users under the client agreement |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events |
| Vice President, Integration Management Office | Brings acquired venues' identities under this policy |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every workforce member, client user, and service must have a unique identifier. Shared or generic accounts, including shared POS clerk and box office logins, are prohibited except where a documented exception exists. (IA-4; AC-2; PR.AA-01)
4.2 Access must be role-based and limited to what the job needs, approved by the system owner before it is granted. (AC-6; AC-2; PR.AA-05)
4.3 Phishing-resistant MFA is required for privileged access and all access into the cardholder data environment; MFA is required for all other workforce access to company systems and for all client users of the client console. (IA-2; IA-2(1); IA-2(2); PR.AA-03)
4.4 Access to the cardholder data environment and privileged access must be certified quarterly; all other access at least every 6 months. (AC-2; PR.AA-05)
4.5 Access must be removed the same business day a workforce member leaves, and seasonal event staff access must expire automatically at the end of each season. (PS-4; AC-2; PR.AA-05)
4.6 Workforce accounts inactive for 60 days and client user accounts inactive for 90 days must be disabled automatically. (AC-2(3); PR.AA-05)
4.7 Privileged access must use just-in-time elevation through PAM, with sessions recorded and logged to the SIEM. (AC-6(9); AC-6; PR.AA-05)
4.8 Service accounts and API keys must be inventoried, stored in the secrets vault, use workload identity or key-pair authentication where the platform supports it, be restricted by network policy, and be rotated at least every 12 months. (IA-5; AC-6; PR.AA-01)
4.9 Vendor and integrator remote access, including to venue operational technology, must go through PAM with MFA and session recording, and be enabled only when needed. (MA-4; AC-17; PR.AA-05)
4.10 Passwords must meet STD-02.2: at least 14 characters for the workforce and 12 for client users, screened against breached-password lists. (IA-5(1); PR.AA-03)
4.11 Break-glass accounts must be sealed, tested quarterly, and used for the cardholder data environment only with a second approver. (AC-2; AC-6; PR.AA-05)
4.12 Client and workforce accounts must be monitored for atypical use, such as bulk exports, refunds, fee changes, and sign-ins from new locations, with alerts to the SOC. (AC-2(12); AU-6; DE.CM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- STD-02.4 Client User and API Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the QSA's Reports on Compliance, and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 TVOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
