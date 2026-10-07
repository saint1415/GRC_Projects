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
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-2(8), IA-5, MA-4, PS-4, PS-5, SC-7, CM-8 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.IR-01 |
| PCI DSS v4.0.1 | Requirements 7 and 8; 1.4; 2.2 (N44-45-R01) |
| Supporting standards | STD-06 Authenticator and privileged access standard; STD-04 Store and POS device standard |

## 1. Purpose
Make sure only authorized people and systems can reach card data, customer data, and company systems, and only to the extent their job requires.

## 2. Scope
All workforce members, vendors (including the POS vendor, the marketing agency, and the refrigeration contractor), and service accounts with access to company systems at all sites and in all cloud and SaaS services, including registers, store POS servers, the virtual terminal, and the e-commerce admin console.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers and Store Managers | Request and approve access; complete access reviews for their staff |
| System owners (POS, e-commerce, ERP, cloud, loyalty) | Approve role design; review privileged and export rights quarterly |
| HR Director | Records hires, transfers, and terminations in the HR system on or before the effective date |
| IT Director | Runs the identity provider, POS account provisioning, and break-glass accounts |
| Security Manager | Runs privileged access management and the access broker; reviews privileged and vendor activity |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared, group, or generic accounts are prohibited, including POS vendor support accounts and virtual terminal accounts. Where a system cannot support named accounts, the exception must be documented with compensating controls and approved under POL-01 4.7. (IA-2; AC-2; PR.AA-01; PCI DSS 8.2.1, 8.2.2)
4.2 Access must be role-based, least-privilege, and approved by the user's manager and the system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05; PCI DSS 7.2)
4.3 MFA is required for all workforce and third-party access to company systems, and for all access into the CDE, including vendor remote access and e-commerce administration. Administrators must use phishing-resistant authenticators (security keys) by 2027-03-31. (IA-2(1); IA-2(2); IA-2(8); PR.AA-03; PCI DSS 8.4)
4.4 **Termination.** HR must record the termination on or before the last day. Identity provider and POS access must be disabled that day, or immediately for involuntary terminations. Badges, keys, and any local accounts must be recovered or disabled within 24 hours. (PS-4; AC-2; PCI DSS 8.2.5)
4.5 **Transfers.** Access from the prior role or store must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2)
4.6 **Access reviews.** System owners must review privileged, POS manager, refund approval, and export rights every quarter. Managers must review all other user accounts at least every 6 months. (AC-2; AC-6; PCI DSS 7.2.4)
4.7 **Privileged access.** Administrators must use a separate privileged account, elevated just in time through the privileged access management service, with sessions logged. Administrative access to registers, store POS servers, and the POS head-office application must go through the access broker with MFA. No vendor or service account may hold standing domain administrator rights. (AC-6(2); AC-6(5); AC-17)
4.8 Accounts lock after 10 failed sign-in attempts (6 for POS sign-ins). Workstations lock after 10 minutes idle, and registers, the e-commerce admin console, the merchant portal, and the virtual terminal end sessions after 15 minutes idle. (AC-7; AC-11; AC-12; PCI DSS 8.2.8)
4.9 **Emergency access.** Each critical system (identity provider, cloud organization, POS head office, e-commerce admin) must have break-glass accounts stored sealed and offline, tested quarterly, and used only when normal access fails. Every use must be reviewed by the IT Director within 1 business day. (AC-2)
4.10 Passwords must be at least 14 characters for identity provider accounts and must not be on the banned-password list; POS passwords must meet STD-06. Vendor default passwords must be changed before any device connects to a company network. Service, application, and vendor credentials must be vaulted and rotated at least annually and when anyone with knowledge of them leaves. (IA-5; PR.AA-03; PCI DSS 2.2.2, 8.3, 8.6)
4.11 **Vendor remote access** (POS vendor, refrigeration contractor, and others) must use named accounts with MFA through the company's access broker, be approved per session, be recorded, and be disabled when not in use. (AC-17; MA-4; PCI DSS 8.2.7)
4.12 **No unapproved connections.** No device, modem, or wireless access point may be connected to a store, DC, or cloud network without IT approval and an inventory entry. Vendors must not install their own network connections. (SC-7; CM-8; PR.IR-01; PCI DSS 1.4)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 4.8). Compliance is checked through the annual independent assessment (P07), the QSA's PCI DSS assessment, and the access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.7.

## 7. Related documents
POL-01; POL-05; STD-04; STD-06; P02 control statements AC-2, AC-6, AC-17, IA-2, IA-5; P07 findings for AC-2, AC-6, AC-17, IA-5, PS-4
