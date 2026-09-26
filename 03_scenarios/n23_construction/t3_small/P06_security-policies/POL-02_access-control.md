# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | CFO |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-17, AC-19, AC-22, IA-1, IA-2, IA-2(1), IA-2(2), IA-2(8), IA-3, IA-5, PE-2, PE-3, PE-8, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| Federal contract requirements | FAR 52.204-21(b)(1)(i), (ii), (iv), (v), (vi), (viii), (ix) (N23-R01) |

## 1. Purpose
Make sure only authorized people and devices can reach company and federal contract information, only to the extent their job requires, and that no single person can move money alone.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary staff, and interns) at the main office, the equipment yard, and every jobsite. Covers all company systems and data, including systems that vendors operate for the company, and company-issued devices wherever they are used. External subcontractor users of company systems are covered by statements 4.5 and 4.6.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Department heads and Project Managers | Request and approve access for their staff and their project's external users; complete quarterly reviews |
| Payroll and HR Specialist | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager | Provisions and removes access; runs the identity provider and device management |
| Accounting Manager | Maintains separation of duties in the ERP and bank portal |
| VP Operations and superintendents | Physical access at the yard and jobsites |
| Workforce | Protect credentials and badges; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including jobsite trailer accounts and commissioning laptops. Shared mailboxes must be reached by delegation from named accounts. (IA-2; AC-2; FAR 52.204-21(b)(1)(v))
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. (AC-2; AC-3; AC-6; PR.AA-05; FAR 52.204-21(b)(1)(i)-(ii))
4.3 **Separation of duties for payments.** No one person may both change vendor or employee bank details and release a payment. Every ACH batch and wire must be approved by two authorized people in the bank portal. (AC-5; PR.AA-05)
4.4 MFA is required for all access to email, single sign-on applications, cloud administration, the bank portal, and SAM. Phishing-resistant MFA (security keys or device-bound passkeys) is required for administrators, executives, Project Managers, and accounting staff. (IA-2(1); IA-2(2); IA-2(8); PR.AA-03)
4.5 **Termination and closeout.** HR must open a termination ticket on or before the last day. IT must disable access **the same business day**, or immediately for involuntary terminations, and collect the badge. Project Managers must remove external users from project systems within 5 business days of project closeout. (PS-4; AC-2; FAR 52.204-21(b)(1)(i))
4.6 Managers must review their staff's access every quarter, including external users on their projects. The CFO must review ERP and bank portal payment roles every quarter. (AC-2; AC-6)
4.7 **Emergency access.** Two break-glass administrator accounts must exist, protected by security keys stored in the CFO's safe, tested quarterly, and used only when the identity provider is unavailable. The IT Manager must review any use. (AC-2)
4.8 Passwords must be at least 14 characters and must not appear on the banned-password list. Default passwords must be changed before first use on every device the company uses or installs, including commissioning laptops, jobsite routers, and client security systems. (IA-5; FAR 52.204-21(b)(1)(vi))
4.9 Only company-managed devices may reach systems that hold FCI. Rugged tablets and commissioning laptops must be enrolled in device management with a passcode, encryption, and remote wipe. (AC-19; IA-3; FAR 52.204-21(b)(1)(i))
4.10 **Physical access.**
- The main office uses badges.
- Jobsite trailers must be locked whenever no company employee is inside.
- Visitors at the office and trailers must sign in and be escorted.
- Keys and badges must be inventoried.
- The yard gate combination must be changed at least annually and whenever a holder leaves.

(PE-2; PE-3; PE-8; FAR 52.204-21(b)(1)(viii)-(ix))
4.11 Only the two named website approvers may publish content. Nothing may be posted that shows the interior security features of a federal facility or a client's security systems. (AC-22; FAR 52.204-21(b)(1)(iv))
4.12 Vendor and MSP remote access must use named accounts with MFA and be restricted to approved source addresses. (AC-17; IA-2(1))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.14. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the CMMC self-assessment, and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; access review procedure; P02 control statements AC-2, AC-5, IA-2, IA-2(8), PE-3
