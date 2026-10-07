# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | General Manager (2026-08-31) |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-17, AC-18, IA-2, IA-2(1), IA-2(2), IA-4, IA-5, PS-4, PS-7, SC-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.IR-01 |
| PCI DSS v4.0.1 (N71-R04) | 1.3, 2.2, 2.3, 7.2, 8.2, 8.3, 8.4, 8.6 |
| Law (N71-R05) | FTC Act Section 5, 15 U.S.C. 45(n) |

## 1. Purpose
Make sure only authorized people and services can reach card data, patron data, and the settings that control ticket sales, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company employees, owners, and temporary staff, and every contractor with access to company systems. Covers every account on company systems and on the company's tenants in vendor services: the ticketing platform, identity provider, cloud tenant, POS back office, network devices, CCTV, and door access systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Ticketing | Approves and reviews ticketing platform access, including agency accounts |
| Department heads | Request and approve access for their staff; complete quarterly reviews |
| HR and Payroll Specialist | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager | Runs the identity provider, cloud IAM, network, and remote access |
| Workforce and contractors | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique, named account. Shared or generic accounts (for example "boxoffice" or a bar login) must not be used on the ticketing platform, box office PCs, or administrative consoles. (IA-2; IA-4; AC-2; PR.AA-01; PCI 8.2)
4.2 Access must be limited to what the job requires. The ticketing platform may have no more than 3 administrators. Marketing accounts must not have checkout or payment settings rights. (AC-6; AC-3; PR.AA-05; PCI 7.2)
4.3 **MFA** is required for every user of the ticketing platform, the identity provider, the cloud console, email, and any remote access tool, and for all administrator accounts. (IA-2(1); IA-2(2); PR.AA-03; PCI 8.4)
4.4 Passwords must meet the length and lockout settings in the IT standard, which follow PCI DSS 8.3. Vendor default passwords must be changed before any device or service goes live. (IA-5; AC-7; PR.AA-03; PCI 2.2; 8.3)
4.5 Access must be removed the same day a person leaves or a contract ends. Contractor accounts must carry an end date. (PS-4; PS-7; AC-2; PR.AA-05; PCI 8.2)
4.6 Department heads must review all ticketing, cloud, and administrative access every quarter and remove what is not needed. (AC-2; AC-6; PR.AA-05; PCI 7.2)
4.7 Service accounts and API keys must have the least scope needed, be stored in the key vault, never in code or settings, and be rotated at least annually or at once if exposed. (IA-5; AC-6; PR.AA-01; PCI 8.6)
4.8 Vendor remote access must be turned on only when needed, use a named account with MFA, and be logged. (AC-17; IA-2(1); PR.AA-03; PCI 8.4)
4.9 Any device that handles card data must be separated from the rest of the network or replaced by a standalone validated P2PE device. Production, CCTV and door access, POS, and guest networks must stay separated from the corporate segment. (SC-7; AC-18; PR.IR-01; PCI 1.3; 2.3)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.10. Compliance is checked through the annual control assessment (P07) and the quarterly access reviews in this policy.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-04; System Security Plan (P02); PCI DSS v4.0.1 Requirements 7 and 8
