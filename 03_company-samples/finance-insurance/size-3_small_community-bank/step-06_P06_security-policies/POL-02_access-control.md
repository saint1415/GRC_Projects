# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. |
| Policy ID | POL-02 |
| Owner | IT Manager (Information Security Officer) |
| Approved by | Audit and Risk Committee of the Board of Directors, 2026-08-27 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, GV.RR-04 |
| Interagency Guidelines (12 CFR 30 App. B) | II.B.3; III.C.1.a; III.C.1.e |

## 1. Purpose
Make sure only authorized people can reach customer information and move funds, and only to the extent their job requires. This includes controls that stop employees from giving customer information or funds to people who obtain it through fraudulent means (III.C.1.a).

## 2. Scope
All Cris Santos Bank workforce members (directors, officers, employees, contractors, and temporary staff) at the six branches and the operations center. Covers all systems and data, including systems that service providers operate for the bank. It applies to customer information and all other bank information, and to customer access to online and mobile banking.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Department and Branch Managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Director | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager (ISO) | Provisions and removes access in the identity provider and the core; reviews core super user roles |
| Deposit Operations Manager | Owns wire platform roles and beneficiary templates |
| Treasury Management Officer | Owns customer online banking settings, limits, and business user entitlements |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account in every system, including the core, the admin console, and the wire platform. Shared or generic accounts are prohibited. (IA-2; AC-2; III.C.1.a)
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Core super user and admin console administrator roles are limited to named people approved by the COO. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 **Workforce MFA** is required for email, remote access, cloud administration, the online banking admin console, the wire platform, and the loan origination system. Administrators must use phishing-resistant hardware keys. Push approvals must use number matching. (IA-2(1); IA-2(2); PR.AA-03)
4.4 **Customer authentication.** MFA is required for every business online banking user by 2026-12-31 and every consumer user by 2027-03-31. Adding a wire or ACH beneficiary, or raising a limit, requires out-of-band confirmation with the customer. Until MFA is required, the Treasury Management Officer reviews the new-beneficiary report every business day. (IA-8; PR.AA-03; III.C.1.a)
4.5 **Termination.** HR must open a termination ticket on or before the last day. IT must disable all access, including core logons, **the same business day**, or immediately for involuntary terminations. (PS-4; AC-2)
4.6 **Quarterly access reviews.** Managers must review their staff's access to the core, the admin console, the wire platform, and the loan origination system every quarter, and finish within 30 days of quarter end. The ISO reviews core super user and administrator roles each quarter. (AC-2; AC-6; PR.AA-05)
4.7 **Separation of duties.** Every outgoing wire must be keyed by one person and approved by another (maker-checker). Wire approvers must not create or edit beneficiary templates. Changes to customer limits and dual-approval thresholds in the admin console need a second person's approval and a change record. (AC-5; GV.RR-04; III.C.1.e)
4.8 **Wire callback.** Any wire request received by email, fax, or phone must be verified by a callback to a phone number already on file, never a number in the request, before it is keyed. The callback is recorded in a required field in the wire platform. (AC-3; III.C.1.a)
4.9 Workforce accounts lock after 10 failed sign-in attempts. Customer logons lock after 5. Teller and payments workstations lock after 5 minutes idle and other endpoints after 10. Admin console and wire platform sessions end after 15 minutes idle. (AC-7; AC-11; AC-12)
4.10 **Emergency access.** Sealed break-glass administrator accounts must exist for the identity provider, the cloud tenant, the admin console, and the wire platform. They are tested quarterly and used only when normal access is unavailable. The ISO reviews any use. (AC-2)
4.11 Workforce passwords must be at least 14 characters and must not appear on the banned-password list. Customer password resets must be verified out of band (a call to the phone number on file or an in-branch visit), not by knowledge questions. (IA-5)
4.12 Vendor and MSSP remote access must use named accounts with MFA and be restricted to approved sources. The payments workstations must not be reachable remotely. (AC-17; IA-2(1))

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved at the level in POL-01 section 4.4, and expire within 12 months. No exception may remove maker-checker or the wire callback.

## 7. Related documents
POL-01; POL-05; access review procedure; wire transfer and callback procedure; P02 control statements AC-2, AC-5, IA-2, IA-8
