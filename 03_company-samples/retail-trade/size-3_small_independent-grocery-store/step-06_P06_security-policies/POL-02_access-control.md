# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-12, AC-17, AC-18, IA-2, IA-2(1), IA-2(2), IA-5, PS-4, SC-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.IR-01 |
| PCI DSS v4.0.1 (N44-45-R01) | 7.1-7.3, 8.1-8.6 |
| Law (N44-45-R02) | FTC Act Section 5, 15 U.S.C. 45(n) (reasonable security) |

## 1. Purpose
Make sure only authorized people can reach company systems and customer data, and only to the extent their job requires. Pay special attention to anything that can change the checkout page or the POS settings that keep card data inside the P2PE solution.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and temporary staff) and contractors with access to company systems, including the marketing contractor. Covers the store, online ordering, and all systems and data, including systems that service providers operate for the company (storefront, payment processor, POS vendor, cloud provider, pricing engine vendor). It applies to cardholder data wherever it could appear, customer and loyalty member data, workforce data, and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Department managers (Store Manager, E-commerce and Marketing Manager, Controller) | Request and approve access for their staff and contractors; complete quarterly access reviews |
| HR and Payroll Specialist | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager | Provisions and removes access; runs the identity provider; keeps break-glass accounts |
| Store Manager | Approves each vendor remote access session to the POS back office and building controls |
| Workforce and contractors | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including on the POS back office and the storefront admin console. POS vendor technicians and contractors must each have a named account. (IA-2; AC-2; PR.AA-01; PCI DSS 8.2)
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Contractors must not hold rights to add scripts, edit theme code, or install apps unless a change is approved under POL-01 4.13. (AC-2; AC-3; AC-6; PR.AA-05; PCI DSS 7.2)
4.3 MFA is required for all administrator access, all remote access, and all access to email, the storefront admin console, the cloud console, the merchant portal, and the back office system. (IA-2(1); IA-2(2); PR.AA-03; PCI DSS 8.4)
4.4 Employees and contractors must sign in to the storefront admin console only through the identity provider. Local storefront accounts are prohibited, except one sealed break-glass account (4.10). (AC-2; IA-2)
4.5 **Termination.** HR must open a termination ticket on or before the last day. IT must remove access to every system, including the storefront and the POS back office, **the same business day**, or immediately for involuntary terminations. Any shared secret the person knew (for example the corporate Wi-Fi passphrase) must be changed. (PS-4; AC-2; PR.AA-05; PCI DSS 8.2)
4.6 Every quarter, managers must review storefront administrators and installed apps, cloud administrators, merchant portal users, and POS back office accounts, and remove anything not needed. (AC-2; AC-6; PR.AA-05; PCI DSS 7.2)
4.7 Accounts must lock after no more than 10 failed sign-in attempts. Administrator PCs must lock after 10 minutes idle, and storefront admin sessions must end after 30 minutes idle. (AC-7; AC-11; AC-12; PCI DSS 8.2; 8.3)
4.8 Passwords must be at least 14 characters and must not appear on the banned-password list. A password known to more than one person must be changed at once when anyone who knows it leaves. (IA-5; PR.AA-01; PCI DSS 8.3)
4.9 API keys, app tokens, and other system credentials must be stored in the cloud secrets store or the identity provider, never in email or documents, and rotated at least every 90 days or when a person with access leaves. (IA-5; PCI DSS 8.6)
4.10 **Emergency access.** Two break-glass administrator accounts (identity provider and storefront) must exist, stored sealed and offline, tested quarterly, and used only when single sign-on is unavailable. Any use must be reviewed by the IT Manager. (AC-2)
4.11 Vendor remote access (POS vendor, refrigeration and building controls contractor) must be enabled only on request, approved by the Store Manager, use a named account with MFA, and be turned off after the session. (AC-17; IA-2(1); PCI DSS 8.4)
4.12 **Network separation.** Refrigeration and building controls, the POS back office, office PCs, and guest Wi-Fi must be on separate network segments with deny-by-default rules between them. Guest Wi-Fi must reach the internet only. (SC-7; AC-18; PR.IR-01)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.10. Sanctions range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the quarterly access reviews (POL-02 4.6), and the PCI DSS self-assessment each year.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), recorded in the risk register, and expire within 12 months. No exception may allow card numbers to be entered or stored outside the P2PE devices and the processor's payment form.

## 7. Related documents
POL-01; POL-05; access review procedure (due 2026-11-30); P02 control statements AC-2, AC-6, IA-2, IA-2(1); P01 R-002, R-006, R-009, R-022
