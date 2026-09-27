# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | Vice President of Operations (2026-08-31) |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, incidents, or assessment findings |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-17, AC-20, IA-2, IA-2(1), IA-2(2), IA-5(1), PS-3, PS-4, PE-3 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| SP 800-171 Rev. 2 and contract clauses | 3.1.x, 3.5.x, 3.9.x, 3.10.x; DFARS 252.204-7012(b)(2)(i); ITAR 22 CFR 120.56 |

## 1. Purpose
Make sure only authorized U.S. persons with a business need can reach CUI and export-controlled technical data, in systems and on the shop floor, and only to the extent their job requires. This policy replaces the 2024 access control policy.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary workers, and contractors) at the Florida plant and working remotely. Covers all company systems and data, with added rules for the CUI Engineering Enclave (CEE) defined in the SSP (P02), printed CUI on the shop floor, and systems that service providers operate for the company. It applies to controlled unclassified information (CUI), including controlled technical information and export-controlled technical data, federal contract information (FCI), and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Engineering and department managers | Request and approve enclave access; complete quarterly access reviews |
| Contracts Manager | Confirms U.S.-person status or export authorization before enclave access |
| HR Manager | Sends onboarding, transfer, and termination notices the same day |
| IT Manager and Systems Administrators | Provision and remove access; run the identity provider |
| Manufacturing Systems Engineer | Manages MES and DNC accounts |
| Facilities and Security Coordinator and Plant Manager | Badges, visitor log, and escorts |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account, including on MES terminals and DNC. Shared or generic accounts are prohibited. Service accounts must be named, owned, and not used for interactive sign-in. (IA-2; AC-2; 3.5.1; 3.5.2)
4.2 Enclave access requires a manager's approval, a completed background check, and the Contracts Manager's confirmation that the person is a U.S. person or covered by an export authorization. (AC-2; PS-3; 3.9.1; 22 CFR 120.56)
4.3 Access must be role-based and least-privilege. Engineers do not hold local administrator rights, and machine operators may view but not edit NC programs. (AC-3; AC-6; PR.AA-05; 3.1.2; 3.1.5)
4.4 MFA is required for every enclave account, including MES sign-in and all administrator accounts. Administrators must use hardware security keys, and all enclave users will move to phishing-resistant authenticators by 2027-01-31. (IA-2(1); IA-2(2); PR.AA-03; 3.5.3)
4.5 **Termination and transfer.** HR must notify IT on or before the last day. IT must disable enclave access **the same business day**, or immediately for involuntary terminations. Transfers out of engineering, quality, or program roles are reviewed within 5 business days. Accounts inactive for 45 days are disabled automatically. (PS-4; AC-2; 3.9.2; 3.5.6)
4.6 Managers must review their staff's enclave, PLM, and MES access every quarter. (AC-2; AC-6)
4.7 Accounts lock after 10 failed sign-in attempts. Enclave endpoints and MES terminals lock after 15 minutes idle. Virtual desktop sessions end after 30 minutes idle. (AC-7; AC-11; 3.1.8; 3.1.10; 3.1.11)
4.8 Passwords must be at least 14 characters and must not appear on the banned-password list. Service credentials must be stored in the key vault, never in files. (IA-5(1); 3.5.7; 3.5.10)
4.9 Remote access to the enclave is allowed only through the virtual desktop gateway with MFA and a compliant device. Vendor remote support uses a watched guest session opened on request. (AC-17; 3.1.12 to 3.1.15; 3.7.5)
4.10 Personal devices and external systems may not be used to process, store, or transmit CUI. Public AI services and public file-sharing sites are blocked from the enclave. (AC-20; 3.1.20)
4.11 **Physical access.** The engineering wing and server room are limited to badge groups. Every visitor on the shop floor or in the engineering wing must sign the visitor log and be escorted at all times. Visits by foreign persons require the Contracts Manager's approval in advance, and drawings on the visit route must be covered or removed. (PE-3; 3.10.1 to 3.10.5; 22 CFR 120.56)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.8. Sanctions range from retraining to termination, depending on intent and harm. A suspected unauthorized release of ITAR or EAR technical data is also referred to the Contracts Manager (Empowered Official) for a voluntary disclosure decision. Compliance is checked through the annual self-assessment against SP 800-171A objectives, the control assessment (P07), and the reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), recorded in the risk register, and expire within 12 months. An exception never removes a DFARS 252.204-7012 duty or permits an unauthorized export.

## 7. Related documents
POL-01; POL-04; POL-05; access review procedure (due 2026-11-30); P02 control statements AC-2, IA-2, PE-3
