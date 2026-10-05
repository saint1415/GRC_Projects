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
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-6(3), AC-17, IA-1, IA-2, IA-2(1), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.IR-01 |
| Regulatory basis | 47 CFR 64.2010(a)-(g); 47 CFR 1.20003 |

## 1. Purpose
Make sure only authorized people and processes reach company systems and customer information, only to the extent their role requires; that customers are authenticated as the CPNI rules require before CPNI is disclosed; and that access ends promptly when it is no longer needed.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) and the agents of care vendors and other third parties who use company systems, in all four states, including acquired carriers from their closing date. Covers all systems and data, including the carrier network and its management plane, the lawful-intercept platform, cloud, data centers, SaaS, and systems that vendors operate for the company, and the services offered to business customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-05) and identity governance |
| Director of Network Security Engineering | TACACS+, jump hosts, and network element accounts |
| Chief Customer Officer | Customer authentication procedures for care, retail, portal, and chatbot |
| Managers and system owners | Approve access; complete quarterly certifications |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events |
| Director of Outsourced Care | Vendor agent rosters and access |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user, service, and network administrator must have a unique identity. Shared accounts are prohibited for workforce and vendor agents. Network elements must authenticate administrators with named accounts through TACACS+ wherever the element supports it; device and service accounts must be vaulted in PAM. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. Bulk CPNI export rights need approval by the Vice President, OSS/BSS Platforms. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Duties that could let one person change rating tables and release a bill run, or activate a lawful intercept alone, must be separated in role design; intercept activation needs dual control. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all access to systems holding CPNI, all cloud and administrative access, and all customer-facing administrator portals. Privileged users and network administrators must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)
4.5 Privileged commands on network elements may be issued only from management plane jump hosts. Elements that cannot support named accounts must be reachable only from jump hosts. (AC-6(3); AC-17; PR.IR-01)
4.6 Access must be disabled the same business day as a termination, and immediately for involuntary terminations, including vendor agents removed from a roster. (PS-4; AC-2; PR.AA-05)
4.7 Workforce and vendor accounts inactive for 60 days must be disabled automatically. (AC-2(3); PR.AA-05)
4.8 Managers must certify their staff's access every quarter; vendor managers must certify vendor agent access every quarter. (AC-2; PR.AA-05)
4.9 Customers must be authenticated before CPNI is disclosed: call detail on a customer-initiated call only after the customer gives a password not prompted by readily available biographical or account information, otherwise by sending it to the address of record or calling the telephone number of record; online access only after authentication without such information; in-store access only with valid photo ID. Business customers may use contract terms only where they have a dedicated account representative and a contract that addresses CPNI protection. (IA-8; IA-5; PR.AA-03)
4.10 Customers must be notified immediately, at the telephone number or address of record, when a password, backup authentication answer, online account, or address of record is created or changed, without revealing the changed data. (IA-5; AU-12; PR.AA-03)
4.11 Vendor and remote maintenance access must go through the zero-trust or PAM gateway with approval and session recording. Standing vendor access is prohibited, including transition services providers at acquired carriers. (AC-17; MA-4; PR.AA-05)
4.12 Default passwords and SNMP community strings must be changed before any device or system is connected to the network. (IA-5; CM-6; PR.AA-01)
4.13 Access to the lawful-intercept enclave is limited to employees authorized by the CALEA senior officer and is reviewed every quarter. (AC-3; AC-6; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- STD-02.4 Customer Authentication Standard (CPNI)
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure
- PRC-02.5 Care Authentication Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CPNI certification evidence package. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or of a vendor agent's access, in proportion to intent and harm. Misuse of CPNI is always a sanctionable violation.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 OSS/BSS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
