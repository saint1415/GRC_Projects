# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | AC-2, AC-2(3), AC-3, AC-6, AC-6(5), AC-17, CA-9, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PE-2, PE-3, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| PCI DSS v4.0.1 | 7.2, 7.3, 8.2, 8.3, 8.4, 8.6, 9.2, 3.4.1 |
| Supporting standards | STD-06 Authenticator and privileged access; STD-10 Facility security |

## 1. Purpose
Make sure only the right people, with the right access, reach card data, guest data, lock systems, and the systems that run the hotels, and that every action can be traced to one person.

## 2. Scope
Every account on company systems (identity provider, SYS-01, POS, lock systems, cloud accounts, servers, network devices), company users of the franchisor's systems, vendor and contractor access, and physical access to server rooms and network closets at all 6 hotels and the corporate office.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Director | Owns this policy and STD-06; runs the identity provider and the privileged access broker |
| Hotel General Managers and department heads | Approve access for their staff; request and remove brand PMS accounts; take part in access reviews |
| HR Director | Sends hires, transfers, and terminations to the identity provider on the effective date |
| Security Manager | Approves vendor access; reviews privileged activity |
| Director of Loss Prevention and Safety | Physical access to server rooms and network closets |

## 4. Policy statements
4.1 Every user must have a unique ID. Shared, group, or generic accounts are prohibited unless the IT Director approves a documented exception with a way to know who used the account each time. Shared night-audit logins are not allowed. (IA-2; AC-2; PCI DSS 8.2.1, 8.2.2)
4.2 Access must be granted by job need with the least privilege. Permission to display full card numbers is limited to roles approved by the CFO, listed in STD-06. (AC-6; AC-3; PCI DSS 7.2, 3.4.1)
4.3 MFA is required for all access into the cardholder data environment, all remote network access, all administrator access, and all access to email and cloud services. (IA-2(1); IA-2(2); PCI DSS 8.4.1, 8.4.2, 8.4.3)
4.4 All user accounts and privileges must be reviewed at least every 6 months; privileged accounts every quarter. Department heads sign each review, and removals are completed within 5 business days of the review. (AC-2; PCI DSS 7.2.4)
4.5 Access must be removed on the termination date for company systems, and within 1 business day for franchisor systems (through the franchisor's process). Transfers remove the old role on the transfer date. (PS-4; AC-2; PCI DSS 8.2.5)
4.6 Accounts inactive for 90 days must be disabled. (AC-2(3); PCI DSS 8.2.6)
4.7 Administrator rights must be granted just in time through the privileged access broker and recorded. Standing domain or server administrator accounts are not allowed, apart from 2 sealed break-glass accounts per critical system, which are tested each quarter and alert the MSSP when used. (AC-6(5))
4.8 **Vendor access** must be enabled only when needed, through the privileged access broker, with named accounts, MFA, per-session approval by the system owner, recording, and automatic end of session. Always-on vendor remote tools are prohibited. (AC-17; MA-4; PCI DSS 8.2.7, 8.4.3)
4.9 Passwords and other authenticators must meet STD-06: at least 14 characters for passwords that are not paired with MFA, checks against known compromised passwords, and no vendor default passwords on any system. (IA-5; PCI DSS 2.2.2, 8.3.6)
4.10 System and interface accounts (for example POS to PMS and PMS to lock server) must be owned, kept in the credential vault, rotated at least annually and when anyone with knowledge leaves, and blocked from interactive sign-in. (IA-5; CA-9; PCI DSS 8.6)
4.11 Server rooms and network closets must be locked with badge access or a key log, and access lists reviewed each quarter. (PE-2; PE-3; PCI DSS 9.2)

## 5. Compliance and enforcement
P07 tests account lifecycle, MFA, vendor access, and privileged access each year. The GRC Analyst reports review completion to the COO each quarter. Violations are handled under POL-01 4.15.

## 6. Exceptions
Under POL-01 4.7. No exception may remove MFA from vendor remote access or allow shared accounts without accountability.

## 7. Related documents
POL-01; STD-06; STD-10; SSP (P02) sections 10 and 11; P07 POA&M items POAM-001, POAM-002, POAM-004
