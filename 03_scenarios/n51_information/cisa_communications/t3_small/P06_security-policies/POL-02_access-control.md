# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | COO |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes, incidents, or FCC rule changes |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-5, IA-8, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.IR-01 |
| FCC and CALEA rules | 64.2010(a)-(g); 1.20003 |

## 1. Purpose
Make sure only authorized people and processes can reach customer information, network elements, and the lawful-intercept system, only to the extent their job requires, and that customers are authenticated as the CPNI rules require.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at CO-1, CO-2, the warehouse and fleet yard, remote cabinets, and remote work locations, and the agents of vendors who access company systems, including the overflow call center. Covers all systems and data, including systems that vendors operate for the company. It applies to customer proprietary network information (CPNI), lawful-intercept information, subscriber personal information, network configuration and outage information, and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Department managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager | Provisions and removes workforce access; runs the identity provider and cloud IAM |
| Network Engineering Manager | Owns TACACS+ policy and network element accounts |
| Director of Customer Operations | Owns customer authentication procedures for phone, chat, and in-person channels; reconciles overflow vendor agent rosters monthly |
| Workforce and vendor agents | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including on network elements. Network element administration must use named TACACS+ accounts backed by the identity provider. Until migration is complete (POAM-003), shared device passwords must be vaulted and rotated whenever a holder leaves. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Bulk export of customer records from the BSS is limited to two billing roles. Service accounts must have only the rights their function needs (for example, read-only CDR collection). (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for email, single sign-on applications, VPN, cloud administration, and all network element administration. Cloud, identity, and network administrators must use phishing-resistant hardware keys. (IA-2(1); IA-2(2); PR.AA-03)
4.4 **Termination.** HR must open a termination ticket on or before the last day. IT must disable the user's access **the same business day**, or immediately for involuntary terminations, and any shared credential the person knew must be rotated within 1 business day. (PS-4; AC-2)
4.5 Managers must review their staff's BSS roles, OSS roles, and identity provider groups every quarter. The Director of Customer Operations must reconcile the overflow vendor's agent roster monthly. (AC-2; AC-6)
4.6 Workforce accounts lock after 10 failed sign-in attempts. Workstations lock after 15 minutes idle; BSS sessions end after 30 minutes idle. (AC-7; AC-11; AC-12)
4.7 **Management plane.** Network elements, element managers, TACACS+, and configuration backups may be reached only from the jump hosts. The corporate network must not route to the management network. The lawful-intercept system must have its own isolated management path, reachable only by the 3 CALEA-authorized employees. (AC-17; SC-7; PR.IR-01; 1.20003)
4.8 **Emergency access.** Sealed break-glass console credentials must exist at CO-1 and CO-2, be tested quarterly, and be used only when TACACS+ or the identity provider is unavailable. Any use is reviewed by the IT Manager within 1 business day. (AC-2)
4.9 Workforce passwords must be at least 14 characters and not on the banned-password list. Vendor default passwords and SNMP community strings must be changed before a device is connected. (IA-5)
4.10 **Customer authentication (CPNI).** (IA-8; 64.2010)
- **Phone:** call detail may be discussed on a customer-initiated call only after the customer gives the account password. Otherwise it is sent to the address of record or discussed on a call back to the telephone number of record. (64.2010(b))
- **Online (portal, app, chat):** access to CPNI requires authentication that does not use readily available biographical or account information (such as date of birth, SSN digits, account number, or ZIP code), and then a password. Password reset uses a one-time code sent to the telephone number or email address of record. (64.2010(c), (e))
- **In person:** a valid government-issued photo ID matching the account. (64.2010(d))
- **Notices:** customers must be notified immediately, by voicemail or text to the telephone number of record or by mail to the address of record, when a password, backup authentication answer, online account, or address of record is created or changed. The notice must not reveal the changed information. (64.2010(f))
- **Business customers:** enterprise contracts may set other authentication terms only where the 64.2010(g) conditions are met.
4.11 Vendor remote access must use named accounts with MFA through the VPN, be limited to approved systems, and be logged. (AC-17; MA-4)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (POL-01 section 4.8), which expressly covers misuse of CPNI (47 CFR 64.2009(b)). Sanctions range from retraining to termination, and for vendor agents, removal from company work. Compliance is checked through the annual control assessment (P07), the access reviews in POL-02, and the evidence gathered for the annual CPNI certification.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the Chief Executive Officer for High risk), and expire within 12 months. No exception may permit a practice the CPNI, CALEA, or outage rules prohibit.

## 7. Related documents
POL-01; POL-05; CPNI customer authentication procedure; P02 control statements AC-2, AC-6, IA-2(1), IA-8
