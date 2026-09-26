# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-17, IA-2, IA-2(1), IA-5, PS-4, PE-2 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, DE.CM-06 |
| Regulatory basis | 10 CFR 37.23(e)(5) and 37.43(d)(3), (6), (7) through the Florida license condition; NIST SP 800-82 Rev. 3 sec. 6.2.1 and 6.2.10 (voluntary) |

## 1. Purpose
Make sure only authorized people can reach company systems, OT, security systems, and data, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and temporary staff) at the Plant, in company vehicles, and at customer sites. Covers all company systems and data, including systems that vendors operate for the company, the plant OT network, and the physical security systems. It applies to Part 37 security-related information and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers | Request and approve access for their staff; complete quarterly access reviews |
| Radiation Safety Officer | Approves access to Part 37 security-related information and to the vault; keeps both approved lists |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager | Provisions and removes access; runs the identity provider |
| Maintenance and Controls Supervisor | Approves OT accounts and each vendor remote session |
| Workforce | Protect credentials and badges; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, with one documented exception: operator logins on HMI stations inside the processing building, which are physically controlled. (IA-2; AC-2)

4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)

4.3 **Security-related information.** Only people on the RSO's information access list may open the Part 37 security plan, implementing procedures, the approved-individuals list, or the DOT security plan. The RSO must evaluate need to know and complete a trustworthiness and reliability determination before adding anyone. (AC-3; 10 CFR 37.43(d)(3), (6))

4.4 MFA is required for all access to company systems, remote access, and cloud administration. Administrators and members of the Part 37 restricted library must use phishing-resistant hardware keys. (IA-2(1); PR.AA-03; 37.43(d)(7))

4.5 **Termination.** HR must open a termination ticket on or before the last day. The same business day, IT must disable all accounts and the RSO must remove the person from both Part 37 lists and the PACS. For involuntary terminations this must happen immediately. The regulatory limit is 7 working days (37.23(e)(5), 37.43(d)(6)); company policy is stricter. (PS-4; AC-2; PE-2)

4.6 Managers must review their staff's access every quarter. The RSO must reconcile the HR roster, both Part 37 lists, and the PACS badge list every month. (AC-2; AC-6)

4.7 Accounts must lock after 10 failed sign-in attempts. Workstations must lock after 10 minutes idle. (AC-7; AC-11)

4.8 **No default passwords.** Default passwords on any device, including cameras, door controllers, PLCs, HMIs, and network equipment, must be changed before the device is connected. Device credentials must be kept in the company password vault, not in files. (IA-5; PR.AA-01)

4.9 **Emergency access.** Two break-glass administrator accounts must exist, stored sealed and offline, tested quarterly, and used only when the identity provider is unavailable. The IT Manager must review any use. (AC-2)

4.10 **Vendor and MSP remote access.** It must use named accounts with MFA and be restricted to approved sources. OT remote access must be off by default and enabled per session by the Maintenance and Controls Supervisor. Each session must be recorded. (AC-17; IA-2(1); DE.CM-06)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the Part 37 program reviews, and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-04; POL-05; Part 37 access authorization procedure AAP-01 (restricted); SEC-10 Information Protection procedure (restricted, due 2026-09-30); P02 control statements AC-2, AC-3, IA-5
