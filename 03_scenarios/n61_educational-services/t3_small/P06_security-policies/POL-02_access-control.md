# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (private career college) |
| Policy ID | POL-02 |
| Owner | IT Director (Qualified Individual) |
| Approved by | Campus President |
| Approved / effective | Approved 2026-08-21; effective 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-7, AC-11, AC-17, IA-1, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, PS-4, PE-3 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory basis | 16 CFR 314.4(c)(1), (c)(5) (N61-R02); 34 CFR 99.31(a)(1)(i)(A) and (a)(1)(ii) (N61-R01); 34 CFR 668.16(c)(2) |

## 1. Purpose
Make sure only authorized people reach student and financial aid information, and only the records their job requires. For education records, this policy is the college's "reasonable methods" under FERPA (34 CFR 99.31(a)(1)(ii)): school officials may reach only records in which they have a legitimate educational interest.

## 2. Scope
All Cris Santos Company workforce members: employees, full-time and adjunct faculty, contractors, and student workers. It also covers the financial aid servicer and any vendor with an account in a college system, and students using the student portal, LMS, and financial aid portal. It covers every system in the SSP boundary (P02) and the connected LMS, CRM, email, and lab systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Data owners (Registrar for the SIS, Director of Financial Aid for the FAMS and SAIG, Dean of Academic Affairs for the LMS, Director of Admissions for the CRM) | Define roles; approve access requests; complete access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets, including adjunct contract end dates |
| IT Director and IT technicians | Provision and remove access; run the identity provider; manage privileged and service accounts |
| Director of Financial Aid | Approves every servicer account before it is created |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique, named account. Shared or generic accounts are prohibited, including servicer accounts and lab administrator accounts. The only exception is a student practice account inside the isolated practice lab (POL-05 4.10), which holds no college data. (IA-2; AC-2; PR.AA-01; 314.4(c)(1)(i))

4.2 Access must be role-based, least-privilege, and approved by the data owner before it is granted. Access to education records must match a legitimate educational interest:
- admissions representatives see applicants, not enrolled students' records;
- advisors see the students assigned to them;
- only financial aid staff see ISIR, tax, and verification data.

(AC-3; AC-6; PR.AA-05; 314.4(c)(1)(ii); 34 CFR 99.31(a)(1)(i)(A), (a)(1)(ii))

4.3 **MFA.** Multi-factor authentication is required for any individual accessing any college information system. This covers:
- all staff and faculty, including adjuncts;
- the financial aid servicer and any vendor account;
- students before they view aid information or change refund or bank details;
- administrators, who must use phishing-resistant authenticators.

The only alternative is reasonably equivalent or stronger controls that the Qualified Individual approves in writing (POL-01 4.7). (IA-2(1); IA-2(2); IA-8; PR.AA-03; 314.4(c)(5))

4.4 **Termination.** HR must open a termination ticket on or before the last day of work or the end of an adjunct contract. IT must disable all access **the same business day**, or immediately for involuntary terminations. Accounts outside the identity provider must be disabled at the same time. (PS-4; AC-2; PR.AA-05)

4.5 **Access reviews.** Data owners must review user access to their systems every six months. Privileged accounts, servicer accounts, and service accounts must be reviewed every quarter. The LMS account list must be reconciled against HR records every month. (AC-2; AC-6; PR.AA-05; 314.4(c)(1))

4.6 Accounts must lock after 10 failed sign-in attempts. Staff workstations must lock after 10 minutes idle. (AC-7; AC-11)

4.7 **Emergency access.** Two break-glass administrator accounts for the identity provider and cloud tenant must exist. Their credentials must be stored sealed and offline, and they must be tested quarterly and used only when normal administrator access is unavailable. The Qualified Individual must review every use. (AC-2; PR.AA-05)

4.8 **Authenticators.**
- Passwords must be at least 14 characters and must not appear on the banned-password list.
- Local administrator passwords must be unique per device and managed by the IT tool, including on lab computers.
- Service account secrets must be stored in the cloud key management service and rotated at least quarterly.

(IA-5; PR.AA-01; 314.4(c)(1)(i))

4.9 **Remote and vendor access.** Remote access to campus systems must use the VPN with MFA. Vendor and servicer access must use named accounts that the college approves and can disable, federated through the college identity provider where the system supports it. (AC-17; IA-2(1); PR.AA-03)

4.10 **Refund safeguards.** A student's change to refund or bank details must require MFA and trigger email and text confirmation, with a 3-business-day hold before the next refund is paid to the new account. (IA-8; AC-2; 314.4(c)(1)(i))

4.11 **Separation of duties.** No user may hold both the financial aid awarding role in the FAMS and the disbursement or refund role in the SIS. (AC-5; 34 CFR 668.16(c)(2))

4.12 **Physical access.** The server closet and the records room holding paper financial aid files must be locked, with access limited to named staff and logged (badge reader or key log). Locks must be rekeyed when a key holder leaves. (PE-3; PR.AA-06; 314.4(c)(1))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.10). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved at the level in POL-01 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-05; access request and review procedure (due 2026-11-30); P02 control statements AC-2, AC-6, IA-2, IA-8; FERPA annual notice (school official and legitimate educational interest criteria, 34 CFR 99.7(a)(3)(iii))
