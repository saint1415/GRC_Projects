# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and Cris Santos Title and Closing, LLC |
| Policy ID | POL-02 |
| Owner | IT Director |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-29 |
| Effective date | 2026-10-15 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-17, AC-19, AC-20, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4, PS-5, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06 |
| FTC Safeguards Rule (N53-R01) | 16 CFR 314.4(c)(1)(i)-(ii), (c)(5) |
| Supporting standards | STD-06 Authenticator and privileged access standard |

## 1. Purpose
Make sure only authorized people and systems can reach customer, client, and company information, and only to the extent their work requires. Contractor agents are the largest user group and the main target of email takeover, so this policy applies to them in full.

## 2. Scope
All employees, contractor agents, service providers, developers, and service accounts with access to company systems, including SaaS tenants, the cloud landing zone, the Closing Communications Portal, and the banking platforms.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers and managing brokers | Request and approve access; report departures the same day; complete quarterly access reviews |
| System owners (SYS-01, SYS-02, SYS-10, portal) | Approve role design; review privileged and export rights quarterly |
| HR Director | Records hires, transfers, and terminations on or before the effective date |
| Director of Agent Services | Keeps the contractor agent roster current; matches it to state license transfer records weekly |
| IT Director | Runs the identity provider and provisioning; owns break-glass accounts |
| Security Manager (Qualified Individual) | Runs privileged access and vendor access; reviews privileged activity |
| Users | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, except closing-room kiosk logins that can open only signing sessions, which the Security Manager must approve and list. (IA-2; AC-2; 314.4(c)(1)(i))

4.2 Access must be role-based, least-privilege, and approved by the user's manager and the system owner before it is granted. In SYS-01, agents may see only their own transactions plus those they are assigned to. Export rights in SYS-02 and SYS-01 are limited to named roles. (AC-2; AC-3; AC-6; PR.AA-05; 314.4(c)(1)(ii))

4.3 **MFA for every individual.** MFA is required for every person who accesses any company information system, including every contractor agent, developer, and service provider. No written equivalent will be approved without the notice in POL-01 section 6. Administrators and staff who prepare, approve, or release payments must use phishing-resistant authenticators (security keys). (IA-2(1); IA-2(2); PR.AA-03; 314.4(c)(5))

4.4 **Employee termination.** HR must record the termination on or before the last day. Identity provider access must be disabled automatically that day, or immediately for involuntary terminations; bank platform tokens must be revoked the same day. (PS-4; AC-2; 314.4(c)(1)(i))

4.5 **Contractor agent departure.** A managing broker must report an agent's departure the same business day. Agent Services must also match the roster to state license transfer records weekly. Access must be disabled within 1 business day of either signal. Agent accounts with no sign-in for 90 days must be disabled. (PS-7; AC-2(3); PR.AA-01; 314.4(c)(1)(i))

4.6 **Transfers.** Access from the prior role must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2)

4.7 **Access reviews.** Managers must review their staff's access each quarter; managing brokers must review their agents' access each quarter; system owners must review privileged, export, and payee-change rights each quarter. (AC-2; AC-6; 314.4(c)(1))

4.8 **Privileged access.** Administrators must use a separate privileged account for administration, elevated just in time with sessions logged. No more than 4 standing global administrators are allowed across the identity provider and productivity suite. (AC-6(2); AC-6(5))

4.9 Accounts lock after 10 failed sign-in attempts. Company devices lock after 10 minutes idle (5 minutes for closing-room PCs). (AC-7; AC-11)

4.10 **Emergency access.** The identity provider, cloud organization, and SYS-02 must each have break-glass accounts stored sealed and offline, tested quarterly, and used only when normal access fails. Every use must be reviewed by the Security Manager within 1 business day. (AC-2)

4.11 Passwords must be at least 14 characters and must not be on the banned-password list. Service account secrets must be stored in the key vault service and rotated at least annually. (IA-5)

4.12 **Personal devices.** Contractor agents may use personal devices only through the browser for SYS-01 and SYS-04 on laptops, and only through the managed mail and document apps on phones and tablets. Downloads to unmanaged laptops are blocked. (AC-17; AC-19; AC-20; 314.4(c)(1)(i))

4.13 **Vendor and developer access.** Vendors and the contract development firm must use named accounts with MFA. Production deployments of the Closing Communications Portal need an approval by a company employee in the pipeline. Shared developer credentials are prohibited. (MA-4; AC-6; 314.4(c)(1)(i))

4.14 **Portal users.** Buyers and sellers use the portal with a one-time code sent to the phone number verified at contract. Any change to that phone number must be confirmed by a callback to the number in the contract file. (IA-8; 314.4(c)(1)(i))

## 5. Compliance and enforcement
Violations by employees are handled under POL-01 section 4.8; violations by contractor agents are handled by the Broker of Record. Compliance is checked through the annual independent assessment (P07) and the quarterly access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.7.

## 7. Related documents
POL-01; POL-05; STD-06; P02 control statements AC-2, AC-6, IA-2(2), IA-5, IA-8; P07 findings for AC-2, AC-6, IA-2(2), IA-5, PS-4
