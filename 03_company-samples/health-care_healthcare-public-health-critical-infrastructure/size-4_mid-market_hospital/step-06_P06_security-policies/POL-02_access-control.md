# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director (HIPAA Security Officer) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-6, AC-6(2), AC-6(5), AC-11, AC-17, AC-20, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PS-4, PS-5, PS-7, AU-6 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, DE.CM-03 |
| HIPAA Security Rule | 164.308(a)(3), (a)(4), (a)(5)(ii)(C)-(D); 164.312(a), (a)(2)(i)-(iii), (d) |
| Other rules | 42 CFR 482.24(b)(3) (unauthorized individuals cannot gain access to or alter records) |
| Supporting standards | STD-03 (vendor remote access), STD-06 (authenticators and privileged access) |

## 1. Purpose
Ensure that only authorized people, with a work reason, can reach patient information and hospital systems, and that access ends when the reason ends.

## 2. Scope
Every account on hospital systems and on the EHR the hospital provides to affiliated practices: employees, contracted clinicians, independent physicians, agency staff, students, affiliated practice users, vendors, and service accounts.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Director | Owns this policy and the identity lifecycle |
| HR Director | Source of truth for employee hires, transfers, and terminations |
| Medical Staff Office Manager | Source of truth for physician privileges and departures |
| Sponsors (department leaders, agency coordinators, practice managers) | Request and justify non-employee access; confirm departures within 1 business day |
| Compliance and Privacy Officer | EHR access monitoring and investigation |
| Information Security Manager | Privileged access management, vendor access platform, quarterly reviews |

## 4. Policy statements
4.1 Every user must have a unique account. Generic or shared accounts are prohibited except for view-only display kiosks with no patient search, approved by the Security Officer and listed in the exception register. (IA-2; AC-2; 164.312(a)(2)(i))

4.2 Access must be granted by role, based on least privilege, and approved by the user's department leader or sponsor. Data warehouse export rights and EHR super-user roles need Security Officer approval. (AC-3; AC-6; 164.308(a)(4)(ii)(B))

4.3 **MFA.** MFA is required for remote access, email, VPN, cloud consoles, the identity provider, any EHR access from outside the hospital network, and all administrator access, on campus or off. On campus, clinical workstations use badge tap plus password. Administrators must use phishing-resistant authenticators by 2027-03-31. (IA-2(1); IA-2(2); 164.312(d))

4.4 **Non-employee accounts.** Every account for a contracted clinician, agency nurse, student, affiliated practice user, or vendor must have a named sponsor and an end date no more than 12 months out (90 days for agency staff). Sponsors must report departures within 1 business day. IT reconciles agency and practice rosters monthly. (AC-2; PS-7; 164.308(a)(3)(ii)(C))

4.5 Access must be removed the same day for employee terminations and within 1 business day of notice for non-employees, including badges, local device accounts, and any shared credentials the person knew, which must be changed. (PS-4; AC-2; 164.308(a)(3)(ii)(C))

4.6 Transfers must remove the prior department's roles automatically; any carry-over needs written approval for up to 30 days. (PS-5; AC-2; 164.308(a)(4)(ii)(C))

4.7 **Access reviews.** Department leaders review user access each quarter; the Security Officer reviews privileged access each quarter; practice managers confirm their users each quarter. (AC-2; 164.308(a)(4)(ii)(C))

4.8 **Privileged access.** Administrators must use separate administrator accounts, reached through the privileged access management system with just-in-time elevation and session logging. Standing domain administrator rights are limited to 2 break-glass accounts. (AC-6(2); AC-6(5); 164.308(a)(4)(ii)(C))

4.9 **Vendor remote access.** Vendors may connect only through the vendor access platform with named accounts, MFA, per-session approval by the system owner, and session recording. Persistent VPN accounts for vendors are prohibited after 2026-12-31. (AC-17; MA-4; 164.308(a)(3)(ii)(A))

4.10 **Service and vendor passwords.** Service account and vendor credentials must be stored in the password vault, rotated at least yearly and whenever someone who knew them leaves, and never left at the manufacturer default. Default credentials must be changed before any device or server connects to the network. (IA-5; 164.308(a)(5)(ii)(D))

4.11 **Break-glass.** Each critical system (identity provider, directory, EHR administration, PACS, cloud) must have 2 sealed break-glass accounts, tested quarterly, whose use triggers an alert and a review. (AC-2; 164.312(a)(2)(ii))

4.12 Workstations must lock after 10 minutes in clinical areas and 15 minutes elsewhere; the EHR must end sessions after 30 minutes of inactivity. (AC-11; AC-12; 164.312(a)(2)(iii))

4.13 **EHR access monitoring.** The Compliance and Privacy Officer must run behavior-based access analytics on the EHR audit trail and review alerts monthly, in addition to VIP and employee-record alerts. Records of public figures are flagged as VIP at registration. (AU-6; DE.CM-03; 164.308(a)(1)(ii)(D); 482.24(b)(3))

4.14 Affiliated practice users may see only patients of their practice and patients referred to or shared with it, and must meet the device requirements in the services agreement. (AC-3; AC-20)

## 5. Compliance and enforcement
Compliance is checked by quarterly access reviews, monthly roster reconciliation, EHR access analytics, and the P07 assessment. Violations are handled under POL-01 4.8.

## 6. Exceptions
Under POL-01 4.7. Generic kiosk accounts and any vendor connection outside the platform must be listed in the exception register with an end date.

## 7. Related documents
POL-01; POL-03; STD-03; STD-06; P02 control statements AC-2, AC-6, AC-17, IA-2, IA-5; P08 insider-access runbook
