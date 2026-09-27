# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. |
| Policy ID | POL-02 |
| Owner | Chief Information Officer, with the ISO |
| Approved by | Board Risk Committee, 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(1), AC-3, AC-5, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, IA-12, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, GV.RR-04 |
| Interagency Guidelines (12 CFR 30 App. B) | II.B.3; III.C.1.a; III.C.1.e; 12 CFR 41.90(d)(2) |
| Supporting standards | STD-04 Payments and account maintenance security; STD-07 Authenticator and privileged access |

## 1. Purpose
Make sure only authorized people can reach customer information and move funds, and only to the extent their job requires. This includes controls that stop employees from giving customer information or funds to people who try to obtain them through fraudulent means (III.C.1.a), and controls that detect and answer identity theft Red Flags such as unverified changes to customer contact information (12 CFR 41.90).

## 2. Scope
All workforce members, contractors, and vendor support staff with access to bank systems; all customer and respondent users of online banking and the correspondent portal. Covers the core, online banking, the payments hub and correspondent portal, the cloud landing zone, the identity provider, and all other systems that hold customer information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers and Branch Managers | Request and approve access for their staff; complete quarterly access reviews against role templates |
| HR Director | Opens onboarding, transfer, and termination tickets the same day |
| Chief Information Officer | Provisions and removes access; owns core role templates and PAM |
| Information Security Officer | Reviews privileged and core security administrator access each quarter |
| Director of Payments Operations | Owns payments hub roles, limits, and callback settings |
| Treasury Management Director | Owns customer online banking authentication settings, limits, and business user entitlements |
| Correspondent Services Director | Owns respondent user access to the correspondent portal |
| Retail Banking Director and Contact Center Director | Own verification of customer contact-information changes |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account in every system, including the core, the admin console, the payments hub, and the correspondent portal. Shared, generic, and vendor default accounts are prohibited; any found must be disabled the same day and recorded as an incident. (IA-2; AC-2; III.C.1.a)
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Core access must follow a role template for each job; any entitlement outside the template needs ISO approval and expires after 12 months. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 **Workforce MFA** is required for every system that holds customer information and for all remote access. Administrators must use phishing-resistant hardware keys. Push approvals must use number matching. (IA-2(1); IA-2(2); PR.AA-03)
4.4 **Privileged access.** Administrators of the directory, identity provider, cloud accounts, core security module, payments hub, and correspondent portal must use separate privileged accounts managed in PAM with just-in-time elevation. Core security administrators must not also process customer account maintenance. (AC-6(2); AC-6(5); III.C.1.e)
4.5 **Customer authentication.** All business online banking users must use app-based push with number matching or passkeys by 2027-03-31; SMS codes are allowed only as a fallback with a risk review. Consumers must be offered app-based or passkey MFA, with step-up before adding an external transfer recipient. Every new wire or ACH beneficiary added in online banking must be confirmed out of band before the first payment. (IA-8; PR.AA-03; II.B.3)
4.6 **Contact-information changes.** A change to a customer's phone number, email address, mailing address, or authorized signer must be verified out of band (a call to the phone number already on file, a one-time passcode to the app or the prior number, or in-branch identification) before it is made. The bank must alert the customer at both the old and the new contact points. For 10 days after a change, non-face-to-face wire requests from that customer need a second verification. (IA-12; PR.AA-02; III.C.1.a; 12 CFR 41.90)
4.7 **Termination.** HR must open a termination ticket on or before the last day. IT must disable all access the same business day, including core logons, or immediately for involuntary terminations. (PS-4; AC-2)
4.8 **Transfers.** Prior roles must be removed within 5 business days of a transfer unless the new manager re-approves them. (PS-5; AC-2)
4.9 **Quarterly access reviews.** Managers must review their staff's access to the core, the admin console, the payments hub, the correspondent portal, and the LOS against the role templates each quarter, within 30 days of quarter end. The ISO reviews privileged accounts each quarter. (AC-2; AC-6; PR.AA-05)
4.10 **Separation of duties.** Every outgoing wire must be keyed by one person and approved by another. Wire approvers must not maintain beneficiary templates. Changes to payments hub limits, approval rules, or callback settings need a second administrator's approval and a change record (STD-04). (AC-5; GV.RR-04; III.C.1.e)
4.11 **Wire callback.** Any wire request received by email, fax, or phone must be verified by a callback to a phone number already on file, never a number in the request, before it is keyed. The callback is recorded in the required field in the payments hub. (AC-3; III.C.1.a)
4.12 Workforce accounts lock after 10 failed sign-in attempts; customer logons after 5. Teller and payments workstations lock after 5 minutes idle and other endpoints after 10. Admin console, payments hub, and correspondent portal sessions end after 15 minutes idle. (AC-7; AC-11; AC-12)
4.13 **Emergency access.** Sealed break-glass accounts must exist for the identity provider, the cloud management account, the payments hub, and the admin console. They are tested quarterly and used only when normal access is unavailable. The ISO reviews any use. (AC-2)
4.14 Workforce passwords must be at least 14 characters and must not appear on the banned-password list; where a system cannot enforce this (the core allows 8), the gap is recorded as an exception with compensating MFA. (IA-5)
4.15 **Vendor access.** Vendor and MSSP remote access must use named accounts with MFA through PAM, with per-session approval and session recording. Standing vendor VPNs are not allowed after 2027-03-31. The payments workstations must not be reachable remotely. (AC-17; MA-4)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (POL-01 section 4.8). Compliance is checked through the annual independent assessment (P07), the quarterly access reviews, and monthly sampling of contact-information changes and wire callbacks.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may remove maker-checker, the wire callback, or contact-change verification.

## 7. Related documents
POL-01; POL-05; STD-04; STD-07; access review procedure; wire transfer and callback procedure; Identity Theft Prevention Program; P02 control statements AC-2, AC-5, AC-6(5), IA-8, IA-12
