# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, incidents, or changes to payment design |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-5, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| PCI DSS v4.0.1 | Requirements 7, 8, and 2.2.2 |

## 1. Purpose
Make sure only authorized people can reach card data, guest records, and hotel systems, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and staff supplied by the staffing company) at the hotel, its restaurant, and its bars. Covers all systems and data, including services that vendors operate for the hotel (PMS, payment services, booking engine, channel manager, cloud tenant, chatbot, and pricing system). It applies to payment card data, guest personal information, and all other hotel information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Front Office Manager, Food and Beverage Director, Chief Engineer | Request and approve access for their staff; complete access reviews every 6 months |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager | Provisions and removes access; runs the identity provider; approves vendor remote sessions |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including at the front desk and for night audit. Documented exceptions for system accounts must have compensating controls. (IA-2; AC-2; PCI 8.2.1, 8.2.2)
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. **The PMS permission to display full card numbers is limited to named users who charge virtual cards, and is removed once the PMS charge-without-display feature is in use.** (AC-2; AC-3; AC-6; PR.AA-05; PCI 7.2, 3.4.1)
4.3 MFA is required for all access to the PMS, email, the identity provider, the cloud console, and any remote access, including vendor remote access. (IA-2(1); PR.AA-03; PCI 8.4)
4.4 **Termination and transfer.** HR must open a termination ticket on or before the last day. IT must disable all access **the same day**, or immediately for involuntary terminations. Transfers must trigger a review of the user's roles. (PS-4; AC-2; PCI 8.2.5)
4.5 Managers must review their staff's PMS roles and identity provider access at least every 6 months. (AC-2; AC-6; PCI 7.2.4)
4.6 Accounts lock after 10 failed sign-in attempts. Screens lock after 15 minutes idle; front desk PCs use fast user switching so agents never share a session. (AC-7; AC-11; PCI 8.2.8, 8.3.4)
4.7 Passwords must meet the length and complexity that PCI DSS requires and must not appear on the banned-password list. **Vendor default passwords must be changed before a system is connected to the network.** Interface and system account credentials must be inventoried and changed at least annually or when someone who knows them leaves. (IA-5; CM-6; PCI 2.2.2, 8.3, 8.6)
4.8 **Vendor remote access** (MSP, lock vendor, POS vendor) must use named accounts with MFA, be enabled only when the IT Manager approves a session, be restricted to approved sources, and be logged. Always-on remote tools are prohibited. (AC-17; MA-4; PCI 8.2.7, 8.4.3)
4.9 Two break-glass administrator accounts for the identity provider must exist, stored sealed and offline, tested quarterly, and used only when single sign-on is unavailable. Any use is reviewed by the Information Security Lead. (AC-2)

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.8. Sanctions range from retraining to termination, depending on intent and harm. For contracted staff, the staffing company is asked to remove the person from the hotel assignment. Compliance is checked through the annual control assessment (P07), the PCI DSS self-assessment, and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months. No exception may allow storage of card security codes after authorization.

## 7. Related documents
POL-01; POL-05; access review procedure; P02 control statements AC-2, AC-6, AC-17, IA-2, IA-5
