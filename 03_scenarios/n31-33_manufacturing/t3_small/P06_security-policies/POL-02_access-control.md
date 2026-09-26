# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | COO |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-3, IA-5, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory basis | HIPAA Security Rule for the device cloud, 164.308(a)(3), (a)(4), (a)(5)(ii)(D); 164.312(a), (d) (N62-R01); FD&C Act 524B(b)(2) for device credentials and code signing (N31-33-R05) |

## 1. Purpose
Make sure only authorized people, services, and devices can reach company systems, the device cloud, and PHI, and only to the extent their job or function requires.

## 2. Scope
All workforce members, contractors, and service accounts. Covers corporate IT, engineering systems (repository, build and signing server, PLM), the device cloud (including the access of clinicians at hospital customers), the MES and test stations, and the credentials built into PM-2 and PM-1 monitors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager | Provisions and removes workforce access; runs the identity provider |
| Cloud Operations Lead | Approves and reviews device cloud production access |
| VP Engineering | Approves signing of release firmware; owns device credential design |
| Hospital administrators | Manage their own clinicians' portal access (under the BAA) |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited. **Exception on record:** MES and test stations use shared operator logins until named accounts with badge-plus-PIN login are live (due 2027-01-31, P01 R-019). Until then, supervisors sign off each lot and Line 2 must be segmented from the office network. (IA-2; AC-2; 164.312(a)(2)(i))
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. (AC-2; AC-3; AC-6; PR.AA-05; 164.308(a)(4)(ii)(B)-(C))
4.3 **Production access to PHI.** Standing access to device cloud production data is prohibited. Engineers must request time-limited access through a ticket approved by the Cloud Operations Lead, and each session must be logged. Company support staff see hospital data read-only unless a hospital ticket requires more. (AC-6; AC-2; 164.308(a)(4))
4.4 MFA is required for all workforce access to email, the identity provider, the repository, PLM, ERP, eQMS, VPN, and the cloud console. Privileged cloud and production roles must use phishing-resistant hardware keys. (IA-2(1); PR.AA-03; 164.312(d))
4.5 **Termination.** HR must open a termination ticket on or before the last day. IT must disable access **the same business day**, or immediately for involuntary terminations. Local accounts outside single sign-on must be listed and removed in the same ticket. (PS-4; AC-2; 164.308(a)(3)(ii)(C))
4.6 Managers must review their staff's access every quarter. The Cloud Operations Lead must review device cloud production roles every quarter, and the VP Engineering must review build server and signing rights every quarter. (AC-2; AC-6)
4.7 **Separation of duties.** Nobody may both approve and perform a release signing. Release firmware must be signed only after two authorized people approve. Backup administration must be held by roles separate from production administration. (AC-5)
4.8 **Device credentials.** Devices must not ship with default, hardcoded, or shared passwords or keys. Each device must authenticate with a unique credential. Legacy PM-1 shared keys must be rotated at least yearly and limited to the minimum scope until PM-1 is retired. (IA-3; IA-5; FD&C Act 524B(b)(2))
4.9 Accounts lock after 10 failed sign-in attempts. Laptops lock after 10 minutes idle, and portal sessions end after 15 minutes idle. (AC-7; AC-11; AC-12; 164.312(a)(2)(iii))
4.10 Passwords must be at least 14 characters and must not appear on the banned-password list. Service secrets must be kept in the secrets manager and rotated at least every 90 days. (IA-5; 164.308(a)(5)(ii)(D))
4.11 Remote administrative access to the device cloud must go through the identity provider and the managed bastion. Vendor remote access must use named accounts with MFA. (AC-17; IA-2(1))

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.8. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the quarterly access reviews in 4.6.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved at the level set in POL-01 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-04; POL-05; access review procedure; code-signing procedure; P02 control statements AC-2, AC-5, AC-6, IA-3, IA-5
