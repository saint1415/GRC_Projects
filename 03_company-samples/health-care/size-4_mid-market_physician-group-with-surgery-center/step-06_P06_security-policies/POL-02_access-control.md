# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director (HIPAA Security Officer) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(8), IA-5, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| HIPAA Security Rule | 164.308(a)(3), (a)(4), (a)(5)(ii)(C)-(D); 164.312(a), (d) |
| Supporting standards | STD-06 Authenticator and privileged access standard; STD-04 Medical device security standard |

## 1. Purpose
Make sure only authorized people and systems can reach patient and company information, and only to the extent their job requires.

## 2. Scope
All workforce members, vendors, and service accounts with access to company systems at all sites and in all cloud and SaaS services, including medical device consoles and vendor remote support.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers and business unit leaders | Request and approve access; complete quarterly access reviews for their staff |
| System owners (EHR, PACS, cloud, CBO systems) | Approve role design; review privileged and export rights quarterly |
| HR Director | Records hires, transfers, and terminations in the HR system on or before the effective date |
| IT Director | Runs the identity provider and provisioning; owns break-glass accounts |
| Security Manager | Runs privileged access management and vendor access; reviews privileged activity |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including on medical device consoles where the vendor supports named accounts. Where it does not, the exception must be documented with compensating controls (restricted network access and physical control). (IA-2; AC-2; 164.312(a)(2)(i))
4.2 Access must be role-based, least-privilege, and approved by the user's manager and the system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05; 164.308(a)(4)(ii)(B)-(C))
4.3 MFA is required for all workforce access to company systems. Administrators must use phishing-resistant authenticators (security keys) by 2027-03-31. (IA-2(1); IA-2(2); IA-2(8); PR.AA-03; 164.312(d))
4.4 **Termination.** HR must record the termination on or before the last day. Identity provider access must be disabled automatically that day, or immediately for involuntary terminations. Badges and any local accounts must be disabled within 24 hours. (PS-4; AC-2; 164.308(a)(3)(ii)(C))
4.5 **Transfers.** Access from the prior role must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2)
4.6 **Access reviews.** Managers must review their staff's access to the EHR, identity provider groups, PACS, file shares, and cloud accounts every quarter. System owners must review privileged, report-writer, and export rights every quarter. (AC-2; AC-6; 164.308(a)(4)(ii)(C))
4.7 **Privileged access.** Administrators must use a separate privileged account for administration, elevated just in time through the privileged access management service, with sessions logged. No standing domain administrator rights are allowed for vendor or service accounts. (AC-6(2); AC-6(5); AU-2)
4.8 Accounts lock after 10 failed sign-in attempts. Workstations lock after 10 minutes idle (tap-badge re-authentication in clinical areas), and EHR sessions end after 15 minutes idle. (AC-7; AC-11; AC-12; 164.312(a)(2)(iii))
4.9 **Emergency access.** Each critical system (identity provider, EHR administration, cloud organization, PACS) must have break-glass accounts stored sealed and offline, tested quarterly, and used only when normal access fails. Every use must be reviewed by the Security Officer within 1 business day. (AC-2; 164.312(a)(2)(ii))
4.10 Passwords must be at least 14 characters and must not be on the banned-password list. Service account credentials must be vaulted and rotated at least annually, and default credentials must be changed before any device connects to the network. (IA-5; 164.308(a)(5)(ii)(D))
4.11 **Vendor remote access** (including PACS and modality vendors) must use named accounts with MFA through the company's access broker, be approved per session, be recorded, and end when the work is complete. (AC-17; MA-4)

## 5. Compliance and enforcement
Violations are handled under the HIPAA sanctions procedure (POL-01 section 4.8). Compliance is checked through the annual independent assessment (P07) and the quarterly access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.7.

## 7. Related documents
POL-01; POL-05; STD-04; STD-06; P02 control statements AC-2, AC-6, IA-2, IA-5; P07 findings for AC-02, AC-06, IA-05, PS-04
