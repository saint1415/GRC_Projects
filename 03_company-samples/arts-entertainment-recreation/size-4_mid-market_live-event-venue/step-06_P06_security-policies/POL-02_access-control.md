# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| PCI DSS v4.0.1 (N71-R04) | 7.1 to 7.3; 8.1 to 8.6; 2.2.2 |
| Supporting standards | STD-06 Authenticator and privileged access standard |

## 1. Purpose
Make sure only authorized people and systems can reach card data, patron data, payment pages, and company systems, and only to the extent their job requires.

## 2. Scope
All workforce members, agencies, vendors, and service accounts with access to company systems at all sites and in all cloud and SaaS services, including the ticketing tenant, the tag manager, the website CMS, the payment partner portal, the identity provider, network devices, and physical security systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers | Request and approve access; complete quarterly access reviews for their staff |
| System owners (ticketing, website and tag manager, CRM, cloud, finance) | Approve role design; review privileged, publishing, and export rights quarterly |
| HR Director | Records hires, transfers, and terminations in the HR system on or before the effective date |
| Vice President of Marketing and Digital | Sponsors agency accounts and sets their end dates |
| IT Director | Runs the identity provider and provisioning; owns break-glass accounts |
| Security Manager | Runs privileged access management and third-party remote access; reviews privileged activity |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited. The only exception is a sealed break-glass account for a critical system, whose use is logged and reviewed within 1 business day. (IA-2; AC-2; PCI 8.2.1; 8.2.2)
4.2 Access must be role-based, least-privilege, and approved by the user's manager and the system owner before it is granted. The ticketing tenant may have no more than 6 administrators. (AC-2; AC-3; AC-6; PR.AA-05; PCI 7.2.1; 7.2.2)
4.3 **Single sign-on and MFA.** Every workforce, agency, and vendor account on a company system, and every account that can change content on pages that embed the payment form, must sign in through the identity provider with MFA. Where a system cannot use SSO, the account requires an approved exception and the system's own app-based MFA. (IA-2(1); IA-2(2); PR.AA-03; PCI 8.4.1; 8.4.2)
4.4 **Termination.** HR must record the termination on or before the last day. Identity provider access must be disabled automatically that day, or immediately for involuntary terminations. Local accounts, agency accounts, and badges must be disabled within 24 hours. Agency and vendor accounts must carry an end date no more than 12 months out. (PS-4; AC-2; PCI 8.2.5)
4.5 **Transfers.** Access from the prior role must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2)
4.6 **Access reviews.** Managers must review their staff's access to the ticketing tenant, identity provider groups, CRM, and cloud accounts every quarter. System owners must review administrator, tag manager publishing, and export rights every quarter. (AC-2; AC-6; PCI 7.2.4)
4.7 **Privileged access.** Administrators must use a separate privileged account for administration, elevated just in time through the privileged access broker, with sessions logged. Administrators of the identity provider, the ticketing tenant, and the cloud must use phishing-resistant security keys by 2027-03-31. (AC-6(2); AC-6(5); PCI 7.2.2)
4.8 Accounts lock after 10 failed sign-in attempts for at least 30 minutes or until reset. Laptops lock after 15 minutes idle (5 minutes for box office and call center PCs), and sessions end after 15 minutes idle in the ticketing tenant. (AC-7; AC-11; AC-12; PCI 8.3.4; 8.2.8)
4.9 Passwords must be at least 14 characters through the identity provider and at least 12 characters on any approved local account, and must not be on the banned-password list. API keys and service account credentials must be scoped to the minimum needed, stored in the secrets service, never hard-coded, and rotated at least annually. Default credentials must be changed before any device or system connects to a company network. (IA-5; PCI 8.3.6; 8.6.2; 8.6.3; 2.2.2)
4.10 **Third-party remote access** (integrator, web agency, vendor support) must use named accounts with MFA through the privileged access broker, be approved per session, be recorded, and end when the work is complete. (AC-17; MA-4; PCI 8.4.3; 8.2.7)
4.11 Accounts inactive for 45 days must be disabled automatically in the identity provider and within 90 days on any approved local account. (AC-2(3); PCI 8.2.6)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.10. Compliance is checked through the quarterly access reviews, the annual independent assessment (P07), and the PCI DSS ROC.

## 6. Exceptions
Exceptions follow POL-01 section 4.7.

## 7. Related documents
POL-01; POL-05; STD-06; P02 control statements AC-2, AC-6, IA-2, IA-5; P07 findings for AC-2, AC-6, IA-2, IA-2(1), IA-5, PS-4
