# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director (workforce identity) with the Director of Network Engineering (network elements) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-2(8), IA-5, IA-8, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| FCC rules | 47 CFR 64.2010(a)-(g) (customer authentication and account-change notices); 1.20000 and 1.20003 (lawful-intercept access) |
| Supporting standards | STD-06 Authenticator and privileged access standard; STD-04 Network element security standard |

## 1. Purpose
Make sure only authorized people and systems can reach customer information, network elements, and lawful-intercept systems, and only to the extent their job requires; and make sure customers are authenticated as the CPNI rules require before CPNI is disclosed.

## 2. Scope
All workforce members, vendor agents, vendor support staff, and service accounts with access to company systems, including network elements (routers, OLTs, DSLAMs, cabinet switches, SBCs, softswitches), the management plane, cloud and SaaS services, SYS-18, and the lawful-intercept system. Section 4.11 to 4.13 cover customers (non-organizational users) of the portal, app, chatbot, care center, and stores.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers and business unit leaders | Request and approve access; complete quarterly access reviews for their staff |
| System owners (BSS, OSS, cloud, SYS-18, network elements) | Approve role design; review privileged and export rights quarterly |
| HR Director | Records hires, transfers, and terminations in the HR system on or before the effective date |
| IT Director | Runs the identity provider and provisioning; owns break-glass accounts for IdP and cloud |
| Director of Network Engineering | Runs TACACS+ and element accounts; owns break-glass console credentials |
| Security Manager | Runs privileged access management and the vendor access broker; reviews privileged activity |
| Director of Customer Operations | Owns customer authentication procedures for care, retail, chatbot, and portal |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including on network elements and SYS-18. Where a device cannot support named accounts through TACACS+ or RADIUS, the exception must be documented with compensating controls (jump-host-only access, session recording, password rotation after each use). (IA-2; AC-2)
4.2 Access must be role-based, least-privilege, and approved by the user's manager and the system owner before it is granted. TACACS+ command authorization must limit configuration commands to the roles that need them. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for all workforce access to company systems, including every network element through TACACS+ or the jump hosts. Administrators of the IdP, cloud, network elements, and SYS-10 must use phishing-resistant authenticators (security keys) by 2027-03-31. (IA-2(1); IA-2(2); IA-2(8); PR.AA-03)
4.4 **Termination.** HR must record the termination on or before the last day. Identity provider access must be disabled automatically that day, or immediately for involuntary terminations. Badges, SYS-18 accounts, and any remaining local accounts must be disabled within 24 hours, and any shared credential the person knew must be rotated within 5 business days. (PS-4; AC-2)
4.5 **Transfers.** Access from the prior role must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2)
4.6 **Access reviews.** Managers must review their staff's access to the BSS, OSS, identity provider groups, SYS-18, and cloud accounts every quarter. System owners must review privileged rights, TACACS+ role assignments, and BSS export rights every quarter. (AC-2; AC-6)
4.7 **Privileged access.** Administrators must use a separate privileged account, elevated just in time through the privileged access management service or TACACS+, with sessions logged. Network elements may be administered only from the jump hosts. No standing administrator rights are allowed for vendor or service accounts. (AC-6(2); AC-6(5); AU-2)
4.8 Accounts lock after 10 failed sign-in attempts; workstations lock after 10 minutes idle; BSS sessions end after 30 minutes idle. (AC-7; AC-11; AC-12)
4.9 **Emergency access.** The IdP, cloud organization, and network elements must have break-glass credentials stored sealed at CO-1 and CO-4, tested quarterly, and used only when normal access fails. Every use must be reviewed by the Security Manager within 1 business day, and the credential rotated. (AC-2)
4.10 Passwords must be at least 14 characters and not on the banned-password list. Service account and TACACS+ shared secrets must be vaulted and rotated at least annually. Default credentials and SNMP community strings must be changed before any device connects to the network; SNMPv3 is required for new deployments. (IA-5)
4.11 **Customer authentication: telephone and stores.** Call detail may be discussed on a customer-initiated call only after the customer gives the account password, which must not be prompted by readily available biographical or account information. Otherwise call detail is sent to the address of record or the customer is called back at the telephone number of record. In stores, CPNI is disclosed only after a valid photo ID matching the account. Overflow vendor agents do not have call detail screens. (IA-8; 64.2010(b), (d))
4.12 **Customer authentication: online and chatbot.** Online access to CPNI, including through the chatbot, requires authentication without readily available biographical or account information, then a password. Passwords and backup authentication must be set without such information; a customer who fails must set a new password the same way. The chatbot shows account data only to customers signed in to the portal or app. (IA-8; IA-5; 64.2010(c), (e))
4.13 **Account-change notices.** Customers must be notified immediately by voicemail or text to the telephone number of record, or by mail to the address of record, when a password, backup authentication answer, online account, or address of record is created or changed. The notice must not reveal the changed data or go to the new contact information. This applies to SYS-18 accounts until migration. (AU-12; 64.2010(f))
4.14 **Business customer exemption.** Different authentication terms may be used only for business customers with a dedicated account representative and a contract that specifically addresses CPNI protection. (IA-8; 64.2010(g))
4.15 **Vendor remote access** (network equipment, hosted voice, SYS-18 vendors) must use named accounts with MFA through the access broker, be approved per session, be recorded, and end when the work is complete. Shared vendor accounts are prohibited. (AC-17; MA-4)
4.16 **Lawful intercept.** Only the employees named in the CALEA SSI policies may access SYS-10 or intercept records, and interceptions may be activated only with lawful authorization and the affirmative intervention of one of them. (AC-3; 1.20000; 1.20003)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the annual independent assessment (P07), the quarterly access reviews, and monthly sampling of care calls (25 in-house and 25 overflow).

## 6. Exceptions
Exceptions follow POL-01 section 6. No exception may permit a customer authentication practice that 47 CFR 64.2010 prohibits.

## 7. Related documents
POL-01; POL-05; STD-04; STD-06; CPNI operating procedures; CALEA SSI policies; P02 control statements AC-2, AC-6, IA-2, IA-5, IA-8; P07 findings for AC-02, AC-06, AC-17, IA-05, IA-08, MA-04, PS-04
