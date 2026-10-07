# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Director of IT (HIPAA Security Officer) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-16 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, significant incidents, or exercises |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-12, AC-17, AC-19, AC-19(5), CP-2, IA-2, IA-2(1), IA-2(2), IA-2(8), IA-5, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| HIPAA Security Rule and other rules | 164.308(a)(3), (a)(4), (a)(5)(ii)(D); 164.312(a), (d) |
| Supporting standards | STD-06 Authenticator and privileged access standard; STD-04 Fleet and station device standard |

## 1. Purpose
Make sure only authorized people and systems can reach patient, caller, and client information, and only to the extent their job requires, without slowing an emergency response.

## 2. Scope
All workforce members, vendors, and service accounts with access to company systems at all sites, in all vehicles, and in all cloud and SaaS services, including communications center consoles, MDCs, station alerting controllers, and vendor remote support.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers and directors | Request and approve access; complete quarterly access reviews for their staff |
| System owners (CAD, ePCR, billing, cloud) | Approve role design; review privileged and export rights quarterly |
| HR Director | Records hires, transfers, and terminations in the HR system on or before the effective date |
| Director of IT | Runs the identity provider and provisioning; owns break-glass accounts |
| Security Manager | Runs the vendor access broker; reviews privileged activity |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including per-vehicle accounts on MDCs once named crew sign-in is deployed (target 2027-03-31). Until then the per-vehicle accounts are a documented exception with compensating controls (device management, VPN certificates, read-only mobile role). (IA-2; AC-2; PR.AA-01; 164.312(a)(2)(i))
4.2 Access must be role-based, least-privilege, and approved by the user's manager and the system owner before it is granted. Billing services staff are assigned to client teams and see only their assigned client workspaces. (AC-2; AC-3; AC-6; PR.AA-05; 164.308(a)(4)(ii)(B)-(C))
4.3 MFA is required for all workforce access to company systems. Administrators must use phishing-resistant authenticators (security keys) by 2027-03-31. (IA-2(1); IA-2(2); IA-2(8); PR.AA-03; 164.312(d))
4.4 **Termination.** HR must record the termination on or before the last day. Identity provider access must be disabled automatically that day, or immediately for involuntary terminations. ePCR, scheduling, CAD, badge, and station door access must be removed within 24 hours. (PS-4; AC-2; PR.AA-05; 164.308(a)(3)(ii)(C))
4.5 **Transfers.** Access from the prior role (for example field to communications) must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2; PR.AA-05; 164.308(a)(4)(ii)(C))
4.6 **Access reviews.** Managers must review their staff's access to CAD, the ePCR, the billing platform, identity provider groups, and cloud accounts every quarter. System owners must review privileged, configuration, and export rights every quarter. (AC-2; AC-6; PR.AA-05; 164.308(a)(4)(ii)(C))
4.7 **Privileged access.** Administrators must use a separate privileged account. CAD administration is limited to the IT team and 2 named communications staff with a CAD configuration role. Cloud administrator rights must be elevated just in time from 2027-03-31. (AC-6(2); AC-6(5); AC-6; PR.AA-05; 164.308(a)(4)(ii)(B))
4.8 Accounts lock after 10 failed sign-in attempts. Office devices lock after 10 minutes idle, and ePCR and billing sessions end after 15 minutes idle. Communications center consoles stay unlocked during a shift because live calls must be visible; the badge-controlled center rooms are the documented equivalent measure. (AC-7; AC-11; AC-12; PR.AA-05; 164.312(a)(2)(iii))
4.9 **Emergency access.** The identity provider, CAD administration, and the cloud organization must each have break-glass accounts stored sealed and offline, tested quarterly, and used only when normal access fails. Every use must be reviewed by the Security Officer within 1 business day. (AC-2; CP-2; PR.AA-05; 164.312(a)(2)(ii))
4.10 Passwords must be at least 14 characters and must not be on the banned-password list. Device and service credentials (routers, station alerting controllers, monitors, service accounts) must be stored in the password vault, rotated at least annually, and changed from the manufacturer default before the device connects to any network. (IA-5; PR.AA-03; 164.308(a)(5)(ii)(D))
4.11 **Vendor remote access** (including the CAD vendor and the station alerting vendor) must use named accounts with MFA through the company's access broker, be approved per session by the system owner, be recorded, and end when the work is complete. (AC-17; MA-4; PR.AA-05; 164.308(a)(3)(ii)(A))
4.12 Laptops, tablets, and MDCs must be enrolled in device management with full-device encryption and remote wipe before they receive access. (AC-19; AC-19(5); PR.DS-01; 164.312(a)(2)(iv))

## 5. Compliance and enforcement
Violations are handled under the HIPAA sanctions procedure (POL-01 section 4.8). Compliance is checked through the annual independent assessment (P07) and the quarterly access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. The per-vehicle MDC accounts (4.1) are the only standing exception and expire on 2027-03-31.

## 7. Related documents
POL-01; POL-05; STD-04; STD-06; P02 control statements AC-2, AC-6, IA-2, IA-5; P07 findings for AC-02, AC-06, IA-05, PS-04
