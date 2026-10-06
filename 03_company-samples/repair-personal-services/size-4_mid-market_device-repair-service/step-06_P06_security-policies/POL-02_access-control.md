# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director (Information Security Officer) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(1), AC-3, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Legal and contractual basis | Fla. Stat. 501.171(2); FTC Act Section 5; Manufacturer A agreement (named MFA accounts); PCI DSS v4.0.1 12.1.3 |
| Supporting standards | STD-06 Authenticator and privileged access standard; STD-08 Customer data access and bench standard |

## 1. Purpose
Make sure only authorized people and systems can reach customer, claimant, and company information, and only to the extent their job requires.

## 2. Scope
All workforce members, vendors, partners' systems, and service accounts with access to company systems at all sites and in all cloud and SaaS services, including the manufacturer portals, the contact center platform, bench workstations, and the lab.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers and business unit leaders | Request and approve access; complete quarterly access reviews for their staff |
| System owners (SYS-01, cloud, manufacturer portals, contact center, lab) | Approve role design; review privileged and export rights quarterly |
| HR Director | Records hires, transfers, and terminations in the HR system on or before the effective date |
| IT Director | Runs the identity provider and provisioning; owns break-glass accounts |
| Security Manager | Privileged access, vendor remote access, and review of privileged activity |
| Director of Partner Programs | Named accounts on the manufacturer portals for program compliance |
| Workforce | Protect credentials; never share accounts or badges |

## 4. Policy statements
4.1 Every user must have a unique account, including on manufacturer portals, the contact center platform, bench workstations, and counter tablets (badge plus PIN). Shared or generic accounts are prohibited. (IA-2; AC-2; Manufacturer A agreement)
4.2 Access must be role-based, least-privilege, and approved by the user's manager and the system owner before it is granted. SYS-01 roles must not give any role access to restricted passcode fields except the assigned technician. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for all workforce access to company systems and to vendor platforms that hold customer data, including manufacturer portals. Administrators must use phishing-resistant authenticators (security keys) by 2027-06-30. (IA-2(1); IA-2(2); PR.AA-03)
4.4 **Termination.** HR must record the termination on or before the last day. Identity provider access must be disabled automatically that day, or immediately for involuntary terminations. Accounts outside the identity provider (manufacturer portals, contact center platform, lab systems) and badges must be disabled within 1 business day through the termination checklist ticket. (PS-4; AC-2)
4.5 **Transfers.** Access from the prior role or store must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2)
4.6 **Access reviews.** Managers must review their staff's access to SYS-01, identity provider groups, manufacturer portals, and the contact center platform every quarter. System owners must review administrator, export, and refund rights every quarter. Accounts outside the identity provider must also be reconciled against the HR system each month. (AC-2; AC-6)
4.7 **Privileged access.** Administrators must use a separate privileged account, elevated just in time where the platform supports it. No everyday account may hold SYS-01 administrator functions. (AC-6(2); AC-6(5))
4.8 **Customer devices.** Technicians may open and use a customer device only as STD-08 allows for the repair type and only under the customer's consent recorded on the ticket. Access to customer devices is by the assigned technician on a bench workstation with session recording. (AC-6; AC-3; FTC Act Section 5)
4.9 Accounts lock after 10 failed sign-in attempts. Office endpoints lock after 10 minutes idle; counter tablets after 2 minutes; SYS-01 sessions end after 30 minutes idle. (AC-7; AC-11; AC-12)
4.10 **Emergency access.** Two break-glass accounts for the identity provider and the cloud organization must be stored sealed and offline, tested quarterly, and used only when normal access fails. Every use must be reviewed by the Information Security Officer within 1 business day. (AC-2)
4.11 Passwords must be at least 14 characters and must not be on the banned-password list. Default credentials must be changed before any device (including CCTV recorders, network equipment, and storage arrays) is connected. Service and pipeline secrets must be kept in the secrets service and rotated at least annually. (IA-5)
4.12 **Vendor remote access** (SYS-01 vendor support, lab storage vendor, and others) must use named accounts with MFA through the company's recorded remote access tool, approved per session, and must end when the work is complete. (AC-17; MA-4)
4.13 **Customer access.** Customers reach the status portal and recovered-data links only with a one-time code sent to the phone or email on file; links expire after 14 days. Devices are released only on photo ID or the one-time code. (IA-8; AC-3)

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.8. Compliance is checked through the annual independent assessment (P07) and the quarterly access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may allow a shared account on a manufacturer portal.

## 7. Related documents
POL-01; POL-04; POL-05; STD-06; STD-08; P02 control statements AC-2, AC-6, IA-2, IA-5; P07 findings for AC-2, AC-6, AC-17, IA-5, PS-4
