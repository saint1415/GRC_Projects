# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Chief Information Officer |
| Approved by | Chief Information Officer, with the vCISO's concurrence |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after material changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-2(8), IA-5, IA-8, IA-11, IA-12, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Safeguards Rule and other rules | 16 CFR 314.4(c)(1), (c)(5); 34 CFR 99.31(a)(1)(ii), 99.31(c); 34 CFR 668.16(c)(2), (g)(1); 34 CFR 668.164(h) |
| Supporting standards | STD-04 Student identity and account recovery standard; STD-06 Authenticator and privileged access standard |

## 1. Purpose
Make sure only authorized people reach student, financial aid, and college information, only to the extent their duties or legitimate educational interest require, and that the college can trust who is on the other end of every sign-in, refund change, and record request.

## 2. Scope
All employees, students, applicants, the third-party servicer, employer partner users, clinical preceptors, guest instructors, vendors, and service accounts with access to college systems, at all campuses, online, and in all cloud and SaaS services, including campus safety consoles and vendor remote support.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers and deans | Request and approve access; complete semiannual access reviews for their staff and faculty |
| Data owners (Registrar, Director of Financial Aid, Bursar, Dean of Online Learning) | Approve role design; review privileged, export, and report-writer rights quarterly |
| HR Director | Records hires, transfers, terminations, and adjunct contract end dates in the ERP on or before the effective date |
| Chief Information Officer | Runs the identity provider and provisioning; owns break-glass accounts |
| Information Security Manager | Runs privileged access management and vendor access; reviews privileged activity |
| Vice President of Enrollment Management | Applicant identity proofing (STD-04) |
| Everyone with an account | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account in the identity provider. Shared or generic accounts are prohibited, including in teaching labs. Local accounts in SaaS applications are allowed only for break-glass use or where the application cannot federate, and then only with an expiry date and quarterly review. (IA-2; AC-2; 314.4(c)(1)(i))
4.2 Access must be role-based, least-privilege, and approved by the manager and the data owner before it is granted. School officials may reach only the education records in which they have a legitimate educational interest; advisors see only their assigned students. No user may hold both aid-awarding and disbursing roles. (AC-2; AC-3; AC-5; AC-6; PR.AA-05; 314.4(c)(1)(ii); 34 CFR 99.31(a)(1)(ii); 34 CFR 668.16(c)(2))
4.3 **MFA is required for every individual who accesses a college information system that holds customer information or education records**: employees, students, the third-party servicer, employer partner users, and vendors. Any exception requires the Qualified Individual's written approval of reasonably equivalent or more secure controls, with an end date. Administrators must use phishing-resistant authenticators (security keys) by 2027-03-31. (IA-2(1); IA-2(2); IA-2(8); IA-8; PR.AA-03; 314.4(c)(5))
4.4 **Sensitive changes need step-up authentication.** Changing refund bank details, contact details used for account recovery, or MFA methods requires re-authentication with MFA and triggers a confirmation message to the prior contact. Refunds to a newly changed bank account are held for 3 business days unless the student confirms by phone through a number on file. (IA-11; 34 CFR 668.164(h); 34 CFR 99.31(c))
4.5 **Account recovery.** The service desk may reset a student's password or MFA only after identity proofing under STD-04 (for example a video check against the ID on file). Security questions or date of birth alone are never enough. (IA-5; IA-12; 34 CFR 99.31(c))
4.6 **Applicants.** Online applicants must be identity-proofed under STD-04 before aid is packaged. Credible indications of a false identity go to the Chief Compliance Officer for an Office of Inspector General referral decision. (IA-12; 34 CFR 668.16(g)(1))
4.7 **Termination.** HR must record each termination and each adjunct contract end date on or before the last day. Identity provider access must be disabled automatically that day, or immediately for involuntary terminations. Local accounts and badges must be disabled within 24 hours. (PS-4; AC-2; AC-2(3))
4.8 **Transfers.** Access from the prior role must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2)
4.9 **Access reviews.** Managers must review their staff's and faculty's access every 6 months. Data owners must review privileged, export, and report-writer rights, data warehouse grants, and all local and third-party accounts every quarter. (AC-2; AC-6; 314.4(c)(1))
4.10 **Privileged access.** Administrators must use a separate privileged account, elevated just in time through the privileged access management service, with sessions logged. Each critical system (identity provider, SIS, LMS, FAMS, cloud organization, emergency notification console) must have break-glass accounts stored sealed and offline, tested quarterly, and reviewed within 1 business day of any use. (AC-6(2); AC-6(5); AU-2)
4.11 Accounts lock after 10 failed sign-in attempts. Staff workstations lock after 10 minutes idle; SIS and FAMS sessions end after 30 minutes idle. (AC-7; AC-11; AC-12)
4.12 Passwords must be at least 14 characters for staff and 12 for students and must not be on the banned-password list. Lab computers must use unique local administrator passwords managed by a password solution. Service account credentials must be vaulted and rotated at least annually. (IA-5)
4.13 **Vendor remote access** (including the access control vendor and integration vendors) must use named accounts with MFA through the college's access broker, be approved per session, be recorded, and end when the work is complete. Always-on vendor remote tools are prohibited. (AC-17; MA-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the annual independent assessment (P07), semiannual and quarterly access reviews, and monthly reports of refund bank changes and account recoveries.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. MFA exceptions also need the Qualified Individual's written approval (4.3).

## 7. Related documents
POL-01; POL-05; STD-04; STD-06; P02 control statements AC-2, AC-6, IA-2(2), IA-11, IA-12; P07 findings for AC-02, IA-02(02), IA-11, IA-12, PS-04
