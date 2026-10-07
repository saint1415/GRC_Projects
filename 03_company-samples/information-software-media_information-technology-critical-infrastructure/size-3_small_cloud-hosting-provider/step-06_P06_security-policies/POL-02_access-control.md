# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-25 |
| Review cycle | Annually (next review 2027-09-24), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(9), AC-3, AC-5, AC-6, AC-7, AC-11, AC-12, AC-17, IA-1, IA-2, IA-2(1), IA-5, IA-8, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.IR-01 |
| Regulatory drivers | C-IT-R01 (FedRAMP Rev5 Class C readiness: AC and IA families); MSA confidentiality clause |

## 1. Purpose
Make sure only authorized people can reach company systems, the management plane, and customer environments, and only to the extent their job requires. The company's administrative tools reach every customer, so this policy treats them as the most sensitive systems it runs.

## 2. Scope
All workforce members and contractors, and every system in the HCP boundary. That includes the identity provider, public cloud tenant, code repository, RMM tool, hypervisor managers, BMCs, network devices, bastion host, SIEM, and laptops. Section 4.10 covers customer accounts in the portal.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager | Provisions and removes workforce access; runs the identity provider; keeps the vault |
| System owners (Director of Platform Engineering, Engineering Manager (Control Plane), Managed Services Lead) | Define roles for their systems; remove local accounts; review privileged access |
| Workforce | Protect credentials and security keys; never share accounts |

## 4. Policy statements
4.1 **Unique accounts.** Every user must have a unique, named account. Shared or generic accounts are prohibited, including RMM technician accounts, hypervisor manager accounts, and BMC accounts. Root and vendor default credentials may be used only through a vault checkout that is approved, logged, and followed by rotation. (IA-2; AC-2; AC-2(9); PR.AA-01)

4.2 **Least privilege.** Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Privileged roles are cloud administrator, backup administrator, platform administrator, RMM technician, and repository administrator. Each is assigned separately. No one may hold both production administration and backup deletion rights. (AC-3; AC-5; AC-6; PR.AA-05)

4.3 **MFA.** Phishing-resistant MFA (company-issued hardware security keys) is required for all workforce access. Every administrative interface must be reached through identity-provider single sign-on or through the bastion host with MFA. This includes hypervisor managers, BMCs, network devices, the cloud console, and the RMM console. (IA-2(1); IA-2(2); AC-17; PR.AA-03)

4.4 **Termination and transfer.**
- HR must open a termination ticket on or before the last day.
- IT must disable all access **the same business day**, or immediately for involuntary terminations.
- The checklist covers the identity provider, RMM, hypervisor and BMC accounts, cloud tenant, code repository, domain registrar, and vault.
- Access changes for transfers must be completed within 5 business days.
(PS-4; PS-5; AC-2)

4.5 **Access reviews.** System owners must review privileged access every quarter in the identity provider, cloud tenant, RMM tool, hypervisor managers, and code repository. Other access must be reviewed at least annually. Unneeded access must be removed within 5 business days of the review. (AC-2; AC-6; PR.AA-05)

4.6 **Lockout and timeouts.**
- Accounts lock after 10 failed sign-in attempts.
- Laptops and NOC workstations lock after 10 minutes idle.
- Portal sessions end after 30 minutes idle and bastion sessions after 15 minutes.
(AC-7; AC-11; AC-12)

4.7 **Emergency access.** Two break-glass accounts must exist for each critical system (identity provider, cloud tenant, hypervisor managers). They must be sealed and stored offline at two sites and tested quarterly. They may be used only when normal sign-in is unavailable. The Information Security Officer must review every use within one business day. (AC-2; PR.AA-05)

4.8 **Secrets and authenticators.**
- Passwords must be at least 14 characters and must not appear on the banned-password list.
- Service credentials must be short-lived and scoped to one purpose. Secrets must never be stored in code.
- Vendor default accounts must be disabled or changed before a device goes into production.
- Code and VM template signing keys must be kept in a hardware security module.
(IA-5; IA-5(7); SC-12)

4.9 **Remote and vendor access.**
- The RMM console must accept connections only from company egress addresses.
- A script that targets more than one customer requires a second approver.
- Vendor maintenance sessions must go through the bastion and be recorded.
(AC-17; MA-4; PR.IR-01)

4.10 **Customer accounts.**
- The portal must require MFA for customer administrator roles from 2027-01-31.
- Support staff must never ask a customer for a password.
- Staff may share VM snapshots between tenants only through the portal workflow, with the owning customer's authorization.
(IA-8; IA-2(1); AC-3)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the right authority, and expire within 12 months.

## 7. Related documents
POL-01; POL-05; access review and termination procedures (due 2026-12-31); P02 control statements AC-2, AC-6, AC-17, IA-2, IA-5; P07 POAM-001 to POAM-005
