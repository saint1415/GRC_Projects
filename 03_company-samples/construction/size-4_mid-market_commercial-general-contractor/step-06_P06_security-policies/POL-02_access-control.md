# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-6(2), AC-17, AC-19, AC-20(1), IA-1, IA-2, IA-2(1), IA-2(2), IA-2(8), IA-3, IA-5, PE-2, PE-3, PE-8, PS-4, PS-5, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| Federal contract requirements | FAR 52.204-21(b)(1)(i), (ii), (v), (vi), (viii), (ix) (N23-R01); SP 800-171 Rev. 2 families 3.1, 3.5, 3.9, 3.10 for the CPE (N23-R03) |
| Supporting standards | STD-06 Authenticator and privileged access; STD-10 Facility and jobsite security |

## 1. Purpose
Make sure only authorized people and devices can reach company, federal contract, and client information, only to the extent their job requires; that no single person can move money alone; and that access ends when the need ends.

## 2. Scope
All workforce members and every company system, including the CUI Project Enclave (CPE), SaaS tenants, the cloud landing zone, the MBSS platform, jobsite devices, and physical sites (offices, yard, trailers). External users (subcontractors, design teams, A&E guests, vendor technicians) are covered by statements 4.6, 4.7, and 4.13.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Department heads and Project Managers | Request and approve access for their staff and their project's external users; complete quarterly reviews |
| FC-4 Project Executive | Approves every CPE account, including A&E guests; reconciles the A&E roster monthly |
| HR Director | Opens onboarding, transfer, and termination records the same day |
| Superintendents | Enter field terminations in the time-clock system on the last day; control trailer access |
| IT Director | Provisions and removes access; runs both identity tenants and device management |
| Controller | Maintains separation of duties in the ERP and bank portal |
| Director of Technology and Security Systems | Controls MBSS remote access to client sites |
| Workforce | Protect credentials, security keys, and badges; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including jobsite trailer, commissioning laptop, and MBSS technician accounts. Shared mailboxes are reached only by delegation from named accounts. (IA-2; AC-2; FAR 52.204-21(b)(1)(v))
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Company-administrator rights in SaaS platforms are limited to IT staff; Project Managers receive project-level administration only. (AC-2; AC-3; AC-6; PR.AA-05; FAR 52.204-21(b)(1)(i)-(ii))
4.3 **Separation of duties for payments.** No one person may both change vendor, owner, or employee bank details and release a payment. Every ACH batch and wire must be approved by two authorized people in the bank portal. The same rule applies to the company's SAM EFT data (POL-01 4.8). (AC-5; PR.AA-05)
4.4 **MFA.** MFA is required for all access to email, single sign-on applications, the CPE, cloud administration, the bank portal, payroll self-service, and SAM. Phishing-resistant authenticators (FIDO2 security keys or device-bound passkeys) are required for all CPE users, administrators, executives, Project Managers, billing and accounts payable staff, and the Controller (by 2026-12-31). Help desk MFA resets for these roles require video or in-person verification. (IA-2(1); IA-2(2); IA-2(8); PR.AA-03)
4.5 **Terminations and transfers.** HR must enter a termination on or before the last day; superintendents must enter field terminations through the time-clock system the same day. IT must disable access **the same business day**, or immediately for involuntary terminations, and collect badges, keys, and security keys. A transfer off a project removes that project's access within 5 business days; a transfer off FC-4 removes CPE access the same day. (PS-4; PS-5; AC-2; SP 800-171 Rev. 2 3.9.2)
4.6 **External users.** Project Managers must remove external users from project systems within 5 business days of project closeout. A&E guest accounts in the CPE expire after 30 days unless renewed, and the A&E firm must report departures within 1 business day (subcontract term). (AC-2; PS-7; FAR 52.204-21(b)(1)(i))
4.7 **Access reviews.** Managers must review their staff's access, including external users on their projects, every quarter. The FC-4 Project Executive must review all CPE accounts monthly. The CFO must review ERP and bank portal payment roles every quarter. (AC-2; AC-6)
4.8 **Privileged access.** Administrators must use separate administrative accounts with FIDO2 for privileged work. Cloud and server administration goes through the privileged access broker with session recording. Two break-glass accounts per critical tenant must be tested quarterly and stored in the headquarters safe. (AC-6(2); AC-2)
4.9 Passwords must be at least 14 characters and must not appear on the banned-password list. Default passwords must be changed before first use on every device the company uses or installs, including jobsite routers, commissioning laptops, and client security systems. (IA-5; FAR 52.204-21(b)(1)(vi))
4.10 **Devices.** Only company-managed devices may reach systems that hold FCI. CUI may be reached only from enclave laptops or from managed tablets configured as virtual desktop clients that store no CUI. Rugged tablets must be enrolled in device management with a passcode, encryption, and remote wipe before first use. (AC-19; IA-3; SP 800-171 Rev. 2 3.1.18, 3.1.19)
4.11 **Remote access.** Remote access to company systems must use the VPN, single sign-on, or the CPE virtual desktop gateway, with MFA. Jobsite routers must not expose remote administration to the internet. (AC-17; FAR 52.204-21(b)(1)(x))
4.12 **Physical access.**
- Offices, the yard, and the MBSS monitoring room use badges; badges are reviewed quarterly.
- Jobsite trailers must be locked whenever no company employee is inside.
- Printed CUI is kept only in a badge-locked CUI room or locked cabinet with an authorized-access list.
- Visitors at offices, trailers, and the CUI room must sign in and be escorted; trailer visitor logs are reconciled weekly with gate records on federal installations.
- Keys, badges, and gate combinations must be inventoried and changed when a holder leaves.

(PE-2; PE-3; PE-8; FAR 52.204-21(b)(1)(viii)-(ix); SP 800-171 Rev. 2 3.10.1, 3.10.3 to 3.10.5)
4.13 **Vendor and MBSS remote access.** Vendor support and MBSS technician access to client sites must use named accounts with MFA through the company's gateway, with session recording. Client-owned remote tools may be used only with the client's written approval and named accounts. (AC-17; IA-2(1); AC-20(1))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.18. Compliance is checked through the annual control assessment (P07), the SP 800-171 self-assessment, and the access reviews in this policy.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved under POL-01 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-04; POL-05; STD-06; STD-10; P02 control statements AC-2, AC-5, AC-19, IA-2(8), PE-3
