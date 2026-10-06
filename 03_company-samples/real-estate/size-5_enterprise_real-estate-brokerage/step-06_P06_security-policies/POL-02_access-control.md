# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc., adopted by Cris Santos Title and Escrow, LLC and Cris Santos Relocation, LLC |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-2, AC-6, PS-4, PS-7, AC-2(3), IA-2(1), IA-2(2), IA-8, AC-6(1), AC-6(5), AC-20, AC-17, AC-5, IA-5, IA-2 |
| CSF 2.0 | PR.AA-05, PR.AA-01, PR.AA-03 |
| Regulatory drivers | See `policy-control-map.csv` (N53-R01 Safeguards Rule citations for each statement) |

## 1. Purpose
Make sure only authorized people, with the access their role needs, can reach company systems and customer information, including the 38,000 contractor agents who work from their own devices and the external parties who use the Closing Communications Hub.

## 2. Scope
All Cris Santos Company, Inc. employees, the about 38,000 contractor sales associates who use company systems, contractors, and temporary staff, in all 9 states, and the employees of Cris Santos Title and Escrow, LLC and Cris Santos Relocation, LLC, which adopted this hierarchy by resolution. Acquired firms are covered from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, contractor agents' own devices when they access company systems, and systems that vendors operate for the company, and the services offered to business clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Owns this policy and the identity platform (SYS-05) |
| System owners | Approve role templates; run quarterly certifications |
| Executive Vice President, Brokerage Operations | Owns contractor agent onboarding and departures |
| Managing brokers | Report agent departures the same day; certify office access |
| Title and Escrow client services | Verify and create external professional Hub accounts |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Access must be granted only through identity governance using role templates approved by the system owner, and only to the information the role needs. (AC-2; AC-6; PR.AA-05)
4.2 Employee access must be disabled the same business day as termination, and contractor agent access within 1 business day after the agent leaves the company or the agent's license is no longer active with the company. (AC-2; PS-4; PS-7; PR.AA-01)
4.3 Workforce accounts inactive for 45 days and external Hub accounts inactive for 90 days must be disabled automatically. (AC-2(3); PR.AA-01)
4.4 Every person who accesses a company information system must use MFA. Privileged users, Title and Escrow staff who handle funds, and (by 2027-03-31) contractor agents must use phishing-resistant authenticators under STD-02.2. Any equivalent control must be approved in writing by the Qualified Individual. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.5 Privileged access must be granted just in time through PAM with a ticket reference, and standing administrator rights are not allowed. (AC-6(1); AC-6(5); PR.AA-05)
4.6 Access to sensitive systems must be certified quarterly by managers for employees and monthly by managing brokers for contractor agents. (AC-2; PR.AA-05)
4.7 Contractor agents may use their own devices only through the browser under conditional access, with no download of closing documents to unmanaged devices, under STD-02.3. (AC-20; AC-17; PR.AA-05)
4.8 The person who enters or changes a payee must not approve the disbursement; every trust account wire must have a second approver in a different role, and engineers must not hold approval roles. (AC-5; PR.AA-05)
4.9 Service, API, and bank channel credentials must be stored only in the enterprise secrets vault and rotated at least every 12 months or when a holder leaves. (IA-5; PR.AA-01)
4.10 Shared logins are not allowed. Agents' assistants must have their own accounts in the assistant role. (AC-2; IA-2; PR.AA-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard (employees, contractor agents, external Hub accounts)
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote, Vendor, and Personal Device Access Standard
- PRC-02.1 Access Provisioning and Agent Onboarding and Departure Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or of the agent agreement, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 TMCC SSP; P03 gap analysis; P08 BEC runbook and notification matrix; P10 AI governance.
