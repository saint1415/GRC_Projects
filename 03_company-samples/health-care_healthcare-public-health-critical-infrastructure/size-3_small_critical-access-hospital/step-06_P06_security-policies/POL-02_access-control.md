# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | CEO |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PS-4, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| HIPAA Security Rule | 164.308(a)(3), (a)(4), (a)(5)(ii)(C)-(D); 164.312(a), (d) |

## 1. Purpose
Make sure only authorized people can reach patient and hospital information and systems, only to the extent their job requires, and that every action can be traced to a person.

## 2. Scope
All workforce members of Cris Santos Company, LLC: employees, contracted clinicians, agency staff, students, volunteers, and vendor and MSP personnel with access. Covers all systems and data, including medical devices, building OT, and systems that business associates operate for the hospital.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Department managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day; tracks agency start and end dates |
| Medical staff office | Requests and ends access for contracted clinicians and medical staff |
| IT Manager | Provisions and removes access; runs the identity provider; approves vendor remote access |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including at nursing stations and on analyzer and device workstations. Display-only screens (such as the ED tracking board) must run as view-only kiosks. Documented exceptions must have compensating controls. (IA-2; AC-2; 164.312(a)(2)(i))
4.2 Access must be role-based, least-privilege, and approved by the user's manager (or the medical staff office for clinicians) before it is granted. (AC-2; AC-3; AC-6; PR.AA-05; 164.308(a)(4)(ii)(B)-(C))
4.3 MFA is required for email, remote access, the identity provider, cloud administration, and any vendor or MSP access. Administrators must use phishing-resistant hardware keys. On-site EHR sign-in must move to a second factor that works at the bedside (for example badge-tap plus PIN) by 2026-12-31. (IA-2(1); IA-2(2); PR.AA-03; 164.312(d))
4.4 **Termination and end of assignment.** HR or the medical staff office must open a termination ticket on or before the last day. IT must disable access **the same business day**, or immediately for involuntary terminations. Every contracted and agency account must carry an end date and expire automatically; agencies must report early departures within 1 business day. (PS-4; PS-7; AC-2; 164.308(a)(3)(ii)(C))
4.5 Managers must review their staff's EHR roles and identity provider access every quarter. The IT Manager must reconcile contracted and agency accounts with each agency's roster every month. (AC-2; AC-6)
4.6 Accounts lock after 10 failed sign-in attempts. Workstations lock after 10 minutes idle, and EHR sessions end after 15 minutes idle. Clinical workstations that cannot lock must use badge-tap fast user switching instead of an exemption. (AC-7; AC-11; AC-12; 164.312(a)(2)(iii))
4.7 **Emergency access.** Two break-glass administrator accounts must exist, stored sealed and offline, tested quarterly, and used only when the identity provider is unavailable. EHR emergency access to restricted records must record a reason and is reviewed monthly by the Privacy Officer. (AC-2; 164.312(a)(2)(ii))
4.8 Passwords must be at least 14 characters and must not appear on the banned-password list. Local administrator passwords must be unique per device and managed by the IT tool. Default passwords on devices, including medical devices and OT, must be changed before the device joins the network. (IA-5; 164.308(a)(5)(ii)(D))
4.9 **Vendor and MSP remote access.** Vendors and MSP technicians must use named accounts through the identity provider with MFA, limited to the systems they support, enabled only for approved support windows, and logged. Shared vendor accounts are prohibited. (AC-17; MA-4; IA-2(2))
4.10 Medical device and OT accounts must be named where the device supports it. Where it does not, the IT Manager must document the limitation and compensating controls (network segment, physical control, sign-in log). (IA-2; AC-2)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 4.8). Sanctions range from retraining to termination or removal from the schedule, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the governing body for High and Very High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; access review procedure; P02 control statements AC-2, AC-17, IA-2, IA-5
