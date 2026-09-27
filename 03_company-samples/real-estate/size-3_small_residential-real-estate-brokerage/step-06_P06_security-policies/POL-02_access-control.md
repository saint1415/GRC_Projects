# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | COO |
| Effective date | 2026-09-21 |
| Review cycle | Annually (next review 2027-09-21), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-7, AC-17, AC-19, AC-20, IA-2, IA-2(1), IA-2(2), IA-5, PS-4, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| FTC Safeguards Rule (16 CFR 314) | 314.4(c)(1), (c)(5) |

## 1. Purpose
Make sure only authorized people reach customer information and client funds, and only to the extent their work requires.

## 2. Scope
All Cris Santos Company workforce members: owners, employees, and the affiliated sales associates who work under the Broker of Record's license as independent contractors. Covers all company systems, including SaaS applications, the cloud tenant, online banking for the escrow accounts, and personal devices used to reach company email or the transaction platform.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| HR Manager | Opens onboarding, transfer, and termination tickets for employees the same day |
| Sales Managers | Request contractor access at affiliation; notify IT the same day an agent leaves; review their agents' access quarterly |
| Department managers | Approve and review access for their staff every quarter |
| Controller and Closing Services Manager | Set online banking entitlements and approval rules with each bank |
| IT Manager | Provisions and removes access; runs the identity provider |
| All workforce members | Protect credentials and devices; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique, named account. Shared or generic accounts are prohibited, including on the network storage device and for MSP technicians. (IA-2; AC-2; 314.4(c)(1)(i))
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Contractor sales associates see only their own and their team's transactions in the transaction platform. Only Closing Services staff and the Controller may use the closing software. (AC-2; AC-3; AC-6; PR.AA-05; 314.4(c)(1)(ii))
4.3 **MFA is required for every person who accesses any company information system**, including every contractor sales associate on email and the transaction platform. Administrators, Closing Services staff, and the Controller must use phishing-resistant authenticators. Legacy authentication protocols that bypass MFA must be disabled. Any exception requires the Qualified Individual's written approval of an equivalent control (POL-01 4.6). (IA-2(1); IA-2(2); PR.AA-03; 314.4(c)(5))
4.4 **Termination and departure.** HR must open a termination ticket on or before an employee's last day. A Sales Manager must notify IT the same day a contractor sales associate ends the affiliation or transfers the license. IT must disable access **the same business day**, or immediately for an involuntary departure. The Sales Managers reconcile active contractor accounts against the brokerage's license roster every week. (PS-4; PS-7; AC-2)
4.5 Managers must review their staff's and agents' access every quarter. The Controller must also review online banking users and approval rules every quarter. (AC-2; AC-6)
4.6 **Money movement.** Every outgoing wire from any escrow account (sales escrow, property management escrow, and title escrow trust) requires a preparer and a different approver, using the bank's approval rules and hardware tokens. No one may approve a wire they prepared. (AC-5; PR.AA-05; Fla. Admin. Code r. 61J2-14.010(1); Fla. Stat. 626.8473(4))
4.7 Accounts lock after 10 failed sign-in attempts. Company devices lock after 10 minutes idle. (AC-7; AC-11)
4.8 Passwords must be at least 14 characters and must not appear on the banned-password list. This applies to contractor accounts too. (IA-5)
4.9 **Personal devices.** Contractor sales associates and employees may reach company email and the transaction platform from a personal device only through the approved mobile apps under mobile application management, which keeps company data in the app and allows it to be wiped. Personal devices use guest Wi-Fi only in the offices. (AC-19; AC-20; 314.4(c)(3))
4.10 Vendor and MSP remote access must use named accounts with MFA and be restricted to approved source addresses. (AC-17; IA-2(1); 314.4(f)(2))
4.11 Paper files with customer information must be kept in locked rooms or cabinets, with a key log at each office. (PE-3; MP-4; 314.4(c)(1)(i))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 4.7. Compliance is checked through the annual control assessment (P07) and the quarterly access reviews in 4.5.

## 6. Exceptions
Exceptions follow POL-01 4.6. They must be written, risk-rated, approved under POL-01 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-04; POL-05; independent contractor agreement for sales associates; P02 control statements AC-2, AC-5, IA-2(2)
