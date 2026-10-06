# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all subsidiaries |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the Group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(2), AC-3, AC-5, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, CA-3, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, IA-11, IA-12, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| Regulatory drivers | N55-R03 (ITGC: logical access); N52-R07 (Model #668 sec. 4D(2)(a), (g)); N62-R01 (164.308(a)(3)-(5); 164.312(a), (d)); N62-R02 (164.514(d)(2)); N55-R06 (164.504(f)(2)(iii)) |
| Division supplements | Insurance: surge adjuster onboarding, call center caller verification, agent and policyholder authentication. Health Care Services: EHR break-glass, front-desk accounts, cross-division EHR access |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, only to the extent their job and the data's permitted purpose require, and that the shared identity platform cannot be used to cross from one division into another without authorization.

## 2. Scope
All workforce identities, service accounts, and administrator accounts in every division and in corporate shared services, the help desks that support them, and the external identities (policyholders, agents, employer clients, patients, and bank users) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control; owns the identity recovery procedure |
| Division help desks | Reset passwords and MFA only within the limits of 4.4 |
| Data owners | Approve access to their data; a division's data owner approves any access from another division |
| Managers | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers in SYS-G5 the same day |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited, including front-desk accounts in clinic systems. (IA-2; AC-2; PR.AA-01; 164.312(a)(2)(i))

4.2 Access must be role-based and least privilege. **Access by one division to another division's regulated data must be approved by the owning division's data owner, name the legal basis and purpose, and be limited to the records that purpose needs.** For workers' compensation, insurer staff may receive only the work-injury records that workers' compensation law requires (164.512(l)), through reports rather than direct system access once available. (AC-3; AC-6; PR.AA-05; 164.514(d)(2))

4.3 MFA is required for all workforce access. Administrators and users who release payments, change payroll or bank templates, or hold ERP privileged roles must use phishing-resistant authenticators. Treasury must require step-up reauthentication to release a payment or change a bank template. (IA-2(1); IA-2(2); IA-11; PR.AA-03; Model #668 sec. 4D(2)(g))

4.4 **Identity recovery.** An MFA reset or re-registration must verify identity at least as strongly as the authenticator being replaced: a live video check against the HR photo and government ID, plus confirmation from the manager through a channel on file. Division help desks may reset only non-privileged users of their own division. Resets for administrators, payment and payroll roles, and executives are done only by the group identity team. Every reset is logged and reviewed by the SOC. (IA-5; IA-12; PR.AA-02)

4.5 **Administration boundaries.** Group-wide identity administration rights are limited to the group identity team. Division administrators receive rights scoped to their division. No more than 12 standing group-wide identity administrators may exist; all other privileged access is just in time. (AC-6; AC-6(5); PR.AA-05)

4.6 **Privileged access.** All privileged access, including ERP superuser and vendor support access, must be granted just in time through PAM with approval and session recording. Emergency ERP access must be reviewed within 2 business days after use. (AC-6(5); AC-6(7); MA-4; N55-R03)

4.7 **Separation of duties.** Vendor master changes, invoice entry, payment proposal, and payment release must be separated in the ERP and treasury. Superuser access must not be used to bypass these separations. (AC-5; N55-R03)

4.8 **Service accounts** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, rotate any static key at least every 90 days, and be certified each quarter. (AC-2; IA-5; PR.AA-01)

4.9 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Contractor and surge adjuster accounts must expire automatically at the assignment end date. (PS-4; AC-2(2); 164.308(a)(3)(ii)(C))

4.10 Managers and data owners must certify access every quarter, including privileged, service, and cross-division accounts. (AC-2; AC-6(7); 164.308(a)(4)(ii)(C))

4.11 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle. Application sessions must end after no more than 15 minutes idle for SCSP applications and 30 minutes for other systems. (AC-7; AC-11; AC-12; 164.312(a)(2)(iii))

4.12 **Directory trusts and system interconnections** require an interconnection agreement, a risk assessment, and approval by the Group CISO before they are created, and must be reviewed each year. (CA-3; PR.AA-05)

4.13 **External identities.** Agent, employer client, and bank user accounts must use MFA. Policyholder and patient portals must offer MFA and require step-up verification before payment method or contact changes. Changes to a claimant's or vendor's bank details requested by phone or email must be verified through contact data already on file before they take effect. (IA-8; PR.AA-03; Model #668 sec. 4D(2)(a))

4.14 **Plan sponsor separation.** Group health plan PHI may be accessed only by the plan administration unit named in the plan documents. (AC-3; N55-R06 (164.504(f)(2)(iii)))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, SOX testing, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.12. No exception may permit shared accounts for systems holding PHI or payment authority.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; SCSP SSP (P02).
