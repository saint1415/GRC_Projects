# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director (information security officer) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-17, AU-6, IA-2, IA-2(1), IA-2(2), IA-2(8), IA-5, MA-4, PE-2, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06 |
| CISA CPG 2.0 (voluntary baseline) | 1.E, 3.A, 3.B, 3.C, 3.D, 3.E, 3.F, 3.G, 3.H |
| Supporting standards | STD-07 Authenticator and privileged access standard; STD-02 OT security standard |

## 1. Purpose
Make sure only authorized people and systems can reach company systems, building systems, and the buildings themselves, and only to the extent their role requires.

## 2. Scope
All employees, contractors, integrators, vendors, and service accounts with access to company IT systems, the building automation platforms, the access control and video platform, and the cloud landing zone; and all physical credentials (cards and mobile credentials) issued to tenant employees, staff, and contractors at the 14 properties.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers | Request and approve access for their staff; complete quarterly access reviews |
| System owners (VP of Engineering for the BAS, Director of Security Operations for access control and video, IT Director for IT and cloud) | Approve role design; review privileged rights quarterly |
| Chief Engineers | Approve each integrator remote session at their property |
| Tenant designated contacts | Authorize and revoke credentials for their employees; recertify their lists quarterly |
| HR Director | Records hires, transfers, and terminations on or before the effective date |
| IT Director | Runs the identity provider, the remote access gateway, and break-glass accounts |
| Director of Security Operations | Runs credential issuance and revocation, door groups, and video access |
| Everyone | Protect credentials; never share accounts or badges |

## 4. Policy statements
4.1 Every user must have a unique account, including on building systems wherever the product supports named accounts. Where it does not, the exception must be documented with compensating controls (access only through the remote access gateway and physical control of the console). (IA-2; AC-2; CPG 3.C)
4.2 Access must be role-based, least-privilege, and approved by the user's manager and the system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for all access to company systems, and for all remote access to building systems, including by vendors. Administrators of the identity provider, cloud, and access control platform must use phishing-resistant security keys. (IA-2(1); IA-2(2); IA-2(8); PR.AA-03; CPG 3.F)
4.4 **Termination.** HR must record the termination on or before the last day. Identity provider access must be disabled automatically that day, or immediately for involuntary terminations. Local building system accounts, console accounts, and badges must be disabled within 24 hours. (PS-4; AC-2; CPG 3.D)
4.5 **Transfers.** Access from the prior role, including badge groups and building system rights, must be removed within 5 business days unless the new manager approves keeping it. (PS-5; AC-2)
4.6 **Access reviews.** Managers must review their staff's access each quarter. System owners must review privileged rights each quarter. The access control platform may have no more than 6 full administrators. (AC-2; AC-6; CPG 3.H)
4.7 **Tenant credentials.** Credentials may be issued only on written authorization from the tenant's designated contact. Credentials not used for 90 days must be suspended automatically. Each tenant must recertify its credential list every quarter, and credentials not recertified must be suspended. (AC-2; AC-2(3); PE-2; CPG 3.D)
4.8 **Privileged access.** Administrators must use a separate privileged account for administration. Each critical administration plane (identity provider, cloud organization, access control platform, BAS Platform A) must have two break-glass accounts sealed offline, tested quarterly, and reviewed within 1 business day of any use. (AC-6(2); AC-6(5); CPG 3.G)
4.9 **Integrator and vendor remote access.** Remote access to building systems must go only through the company's remote access gateway, with named accounts, MFA, per-session approval by the chief engineer on duty, and session recording. Always-on remote-support tools are prohibited. (AC-17; MA-4; CPG 1.E)
4.10 Passwords must be at least 16 characters where the system allows and must not be on the banned-password list. Default passwords must be changed before any device connects to a company network, and integrators must confirm this on the commissioning checklist. (IA-5; CPG 3.A, 3.B)
4.11 Accounts lock after 10 failed sign-in attempts, and repeated failures alert the MSSP. Workstations and console PCs lock after 10 minutes idle, except video wall PCs behind badge-controlled doors (documented exception). (AC-7; AC-11; CPG 3.E)
4.12 **Video access.** Only named investigators approved by the Director of Security Operations may export video. Video access and exports are logged and reviewed every quarter. (AC-6; AU-6)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.15. Compliance is checked through the annual independent assessment (P07), the quarterly access reviews, and the tenant recertification reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.7.

## 7. Related documents
POL-01; POL-05; STD-02; STD-07; P02 control statements AC-2, AC-6, AC-17, IA-2, IA-5, MA-4; P07 findings for AC-02, AC-06, AC-17, IA-05, MA-04, PS-04
