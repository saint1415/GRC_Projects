# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-5, MA-4, PE-2, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| CISA CPG 2.0 (voluntary) | 3.A, 3.B, 3.C, 3.D, 3.E, 3.F, 3.G, 3.H |

## 1. Purpose
Make sure only authorized people can reach company systems, building systems, and tenant spaces, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors), integrators, the MSP, and the guard contractor. Covers every logical account (corporate SaaS, cloud, BAS, access control platform, video, network devices) and every physical credential (employee, contractor, and tenant badges).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Department heads | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding and termination tickets the same day |
| IT Manager | Provisions and removes logical access; runs the identity provider |
| Director of Engineering | Approves BAS accounts and integrator sessions (delegated to chief engineers) |
| Security Manager | Issues and revokes badges; runs the tenant roster attestation |
| Tenant designated contacts | Approve badges for their own employees; confirm the roster each quarter |
| Workforce | Protect credentials and badges; never share accounts |

## 4. Policy statements
4.1 **Unique accounts.** Every user must have a unique account. Shared or generic accounts are prohibited, including on BAS servers and workstations, NVRs, and vendor remote access. Where a device cannot support named accounts, the exception must be documented (POL-01 4.6) with a compensating control, such as access only through the remote access gateway with MFA. (IA-2; AC-2; CPG 3.C)
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Administrator rights on the access control platform are limited to 2 named administrators; console operators use operator roles. Administrators must use a separate administrator account for privileged tasks. (AC-2; AC-3; AC-6; PR.AA-05; CPG 3.G; 3.H)
4.3 **MFA** is required for email, the property management system, the identity provider, cloud administration, the access control platform, and all remote access. Administrators must use phishing-resistant hardware keys. (IA-2(1); PR.AA-03; CPG 3.F)
4.4 **Termination.** HR must open a termination ticket on or before the last day. IT must disable the user's accounts **the same business day**, or immediately for involuntary terminations, and the Security Manager must deactivate the badge at the same time. (PS-4; AC-2; CPG 3.D)
4.5 **Reviews.** Department heads must review their staff's access every quarter. The Security Manager must review access control platform administrators and BAS accounts every quarter. (AC-2; AC-6)
4.6 **Tenant badges.** Each tenant's designated contact must approve every badge and confirm the tenant's badge roster every quarter. Badges not used for 60 days must be suspended automatically, and suspended badges not reactivated within 30 days must be deleted. (PE-2; AC-2; CPG 3.D)
4.7 **Emergency access.** Two break-glass administrator accounts must exist for the identity provider and the cloud tenant, stored sealed and offline, tested quarterly, and used only when normal administrator access is unavailable. Any use is reviewed by the IT Manager and reported to the COO. (AC-2)
4.8 **Passwords.** Passwords must be at least 16 characters and must not appear on the banned-password list. Default passwords must be changed before any device is connected, and at commissioning of every BAS controller, door controller, camera, and NVR. OT local passwords must be unique per device and stored in the company password manager, never in spreadsheets. (IA-5; CPG 3.A; 3.B)
4.9 **Vendor and remote access.** Integrators and the MSP must use named accounts with MFA through the company's remote access gateway. Each integrator session must be approved by a chief engineer (BAS) or the Security Manager (access control and video), limited in time, and recorded. Always-on vendor remote-support tools are prohibited. (AC-17; MA-4; IA-2(1); CPG 1.E; 3.F)
4.10 Accounts lock after 10 failed sign-in attempts. Workstations lock after 10 minutes idle. Security console PCs are exempt from the idle lock because they are staffed 24x7 in a badge-controlled room. Failed sign-ins to administrator accounts and OT systems must be logged and reviewed (POL-03). (AC-7; AC-11; CPG 3.E)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; access review procedure; BAS commissioning checklist; P02 control statements AC-2, AC-6, AC-17, IA-2, IA-5, MA-4
