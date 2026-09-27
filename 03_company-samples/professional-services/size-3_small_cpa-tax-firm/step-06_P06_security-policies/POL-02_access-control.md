# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | Firm Administrator |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after material changes or security events |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| FTC Safeguards Rule | 16 CFR 314.4(c)(1), (c)(5) |

## 1. Purpose
Make sure only authorized people can reach client tax return information and firm systems, and only to the extent their work requires.

## 2. Scope
All Cris Santos Company workforce members (partners, employees, seasonal preparers, interns, and contractors) at the Main and Branch offices and when working remotely. Covers all systems and data, including systems that service providers operate for the firm, and client accounts on the client portal.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Partners and team managers | Request and approve access for their staff; complete quarterly access reviews |
| HR and Payroll Specialist | Opens onboarding, transfer, and termination tickets the same day; sets end dates for seasonal staff |
| IT Manager and IT Support Technician | Provision and remove access; run the identity provider |
| Client Services Supervisor | Administers client portal accounts and settings |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic sign-ins are prohibited. Shared mailboxes must be accessed only through delegated permissions from named accounts. (IA-2; AC-2; 314.4(c)(1)(i))
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Tax staff get access to client folders for their team only; wider access needs partner approval. (AC-3; AC-6; PR.AA-05; 314.4(c)(1)(ii))
4.3 **MFA for everyone.** Multi-factor authentication is required for every individual who accesses any firm information system, including email, the tax software, the DMS, the VPN, and cloud administration. Push approvals must show a number to match. Administrators must use phishing-resistant hardware keys. Legacy protocols that bypass MFA must be blocked. Any exception needs the Qualified Individual's written approval of equivalent controls. (IA-2(1); IA-2(2); PR.AA-03; 314.4(c)(5))
4.4 **Client accounts.** Clients must use MFA on the client portal. Client service staff must verify a client's identity by calling the phone number on file before resetting a client's portal MFA or changing the contact email. (IA-8; 314.4(c)(1)(i); 314.4(c)(5))
4.5 **Termination.** HR must open a termination ticket on or before the last day. IT must disable access the same business day, or immediately for involuntary terminations. Seasonal accounts must be created with an end date no later than April 30. (PS-4; AC-2)
4.6 Managers must review their staff's access to the tax software, the DMS, and the productivity suite every quarter. The IT Manager reviews all administrator rights monthly. (AC-2; AC-6)
4.7 **Administrator rights.** Administrator rights must be held only by separate administrator accounts used for administration, never by everyday accounts. Two break-glass accounts must be stored sealed and offline, tested quarterly, and used only when the identity provider is unavailable. (AC-6; AC-2)
4.8 Accounts lock after 10 failed sign-in attempts. Workstations lock after 10 minutes idle, including seasonal stations. (AC-7; AC-11)
4.9 Passwords must be at least 14 characters and must not appear on the banned-password list. Local administrator passwords must be unique per device and managed by the IT tool. Default passwords on devices must be changed before use. (IA-5)
4.10 **Remote access.** Remote access to firm systems must use the firm VPN or SSO with MFA. Service provider remote access (including the MSP's management tool) must use named accounts with MFA and be restricted to approved sources. Access to firm systems from outside the United States requires the Tax Partner's prior approval, because tax return information may be disclosed outside the United States only with the taxpayer's consent (26 CFR 301.7216-2(c)(2)). (AC-17; IA-2(1))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.11. Compliance is checked through the annual control assessment (P07) and the quarterly access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.8. They must be written, risk-rated, approved by the policy owner (or by the Managing Partner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; access review procedure; P02 control statements AC-2, AC-6, IA-2
