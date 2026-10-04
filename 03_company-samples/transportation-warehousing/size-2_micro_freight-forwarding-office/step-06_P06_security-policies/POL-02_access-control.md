# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office and Compliance Manager (Security Coordinator) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, CA-2, SI-12. Part B: AC-1, AC-2, AC-3, AC-5, AC-6, AC-11, AC-17, AC-19, IA-2, IA-2(1), IA-5, PS-4, AU-6, SI-4, SI-8. Part C: PL-4, AT-2 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, DE.AE-02 |
| Customs broker rules | 19 CFR 111.2(a)(2)(ii)(B), 111.24, 111.28(a), 111.28(b)(3), 111.29(a) |

**Why this policy has three parts.** A 7-person office does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people reach client records, money, and CBP systems and only as far as their job requires, and tell employees how to use company systems.

## 2. Scope
All employees and anyone else who works for Cris Santos Company. It covers every system and every copy of company information, including systems run for the company by the MSP and SaaS vendors, carrier and terminal portal accounts, CBP portal accounts, and company mail and files on personal phones.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves policies and the security budget; accepts Moderate and higher risk; decides sanctions; approves high-value wires |
| Office and Compliance Manager | Security Coordinator; runs this policy; grants and removes access; files CBP employee list updates; reviews accounts and logs |
| Licensed Customs Broker (Entry Supervisor) | Approves customs platform roles for customs staff; records entry reviews |
| MSP | Creates and disables suite and device accounts on the Office and Compliance Manager's request; operates device controls |
| All employees | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security Coordinator.** The Office and Compliance Manager is the Security Coordinator. The owner must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The Security Coordinator must update the risk assessment every July, and after any major change such as a new customs platform, a new vendor that holds client records, or a new AI feature, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Security Coordinator may accept Low and Very Low risks. Only the owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the owner. (PM-9; GV.RM-01)

A.4 **Sanctions.** An employee who breaks a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Security Coordinator records each sanction; the owner approves suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Vendors and client confidentiality.** No vendor or tool may receive client records until the Security Coordinator has confirmed that its contract protects confidentiality, says where the data is stored (within the United States for customs records, 19 CFR 111.23(a)), and is covered by the client authorization in the company's client terms (111.24). That includes trials, pilots, and features a vendor switches on. (SA-9; GV.SC-05)

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2)

A.7 **Retention of security records.** Policies, risk assessments, assessments, incident records, training records, sanction records, and CBP notices must be kept for at least 5 years. (SI-12)

A.8 **Policy review and access to policies.** The Security Coordinator must review this policy set every August and after an incident or major change, and keep the current version where every employee can read it. (PL-1; GV.PO-01; 111.28(a)(2))

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

### Part B. Access control
B.1 **Named accounts only.** Every employee must have their own account in the customs platform, the suite, the accounting SaaS, the bank portal (if they need it), and CBP portals. Shared or generic accounts are not allowed. The entries@ address must be a shared mailbox reached through named accounts. Where a carrier or terminal portal offers named users, each user gets one; where it does not, the shared password is kept only in the company password manager. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** Access must match the person's job, using the role list for each system. The Security Coordinator, and for customs platform roles the Entry Supervisor, must approve access in writing on the onboarding checklist before it is granted. Customs platform administrator roles are limited to the Security Coordinator and the owner as backup. (AC-2; AC-3; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for the customs platform, the suite, the accounting SaaS, the bank portal, CBP portals where offered, and every administrator login, including logins held by the MSP (backup console, firewall, remote management tool). MFA push approvals must use number matching. (IA-2(1); PR.AA-03)

B.4 **Termination.** On or before an employee's last day, the Security Coordinator must complete the termination checklist: disable the customs platform, suite, accounting, bank, and CBP portal accounts; ask the MSP to remove device access; remove MFA registrations; change every shared portal password the person knew; collect keys and the laptop; notify the processing Center that any customs signing authority is withdrawn (111.2(a)(2)(ii)(B)); and send CBP the terminated-employee update within 10 days, well inside the 30-day limit (111.28(b)(3)). For an involuntary termination, access must be disabled before the person is told. (PS-4; AC-2)

B.5 **Monthly reconciliation.** Each month the Security Coordinator must compare the user lists of the customs platform, suite, accounting SaaS, bank portal, and backup console with the staff roster, and remove anything that does not match. Every quarter the Entry Supervisor must confirm each person's customs platform role still fits their job. (AC-2; AC-6; PR.AA-05)

B.6 **Locking.** Computers must lock after 10 minutes idle. (AC-11)

B.7 **MSP and vendor access.** MSP technicians and vendor support staff must use named accounts with MFA. The MSP must give the Security Coordinator a current list of technicians with access every year. (AC-17; IA-2(1); SA-9)

B.8 **Passwords.** Passwords must be at least 14 characters, unique to the company, and never reused from personal accounts. Shared portal passwords live only in the company password manager, never in spreadsheets or email. Default passwords on any device (printer, firewall, Wi-Fi) must be changed before use. (IA-5)

B.9 **Phones.** Company mail and files may be used on a personal phone only through the suite apps with the company's app protection rules (PIN, no copying to personal apps, selective wipe). (AC-19)

B.10 **Payments.** Before any payment to a new beneficiary or to changed bank details, the Accounting Specialist must call the payee at a phone number already on file or from an independent source (never one given in the request) and record the call. Every wire to a new or changed beneficiary needs a second approver in the bank portal (the owner, or the Office and Compliance Manager when the owner is away). Requests to change bank details by email alone are refused. (AC-5; PR.AA-05; 111.29(a))

B.11 **Monthly log review and mail protection.** Each month the Security Coordinator must review, with a checklist, the suite's risky sign-in and new forwarding rule alerts, mass download alerts, and the customs platform's user access and export reports, and report findings to the owner. The suite must tag external email, warn on look-alike domains, and protect the owner's and the Accounting Specialist's names from impersonation. (AU-6; SI-4; SI-8; DE.AE-02)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Employees may access only the client records they need for their job. Client records are confidential: they may be shared only with the client, its surety, CBP and other authorized U.S. officials, or as the client has authorized in writing (111.24). (PL-4; PR.AT-01)

C.2 Employees must not store or send client records with personal email, personal cloud storage, personal messaging apps, or public AI chatbots. Overseas agents and clients send documents to company mailboxes, not to personal phones. POL-04 section 4.6 lists the approved tools. (PL-4)

C.3 Employees must lock their screen when stepping away and never share passwords or MFA codes, including with the MSP or someone claiming to be from a carrier, bank, or CBP. (AC-11; PL-4)

C.4 Employees must complete security training at hire and every year, including payment fraud, phishing, client confidentiality, and the 72-hour CBP breach notice, and must take part in phishing simulations. (AT-2; PR.AT-01; 111.28(a)(1))

C.5 Employees must report suspected incidents at once under POL-03 section 4.2, including their own mistakes and any odd payment request. (IR-6)

C.6 Employees must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Security Coordinator checks compliance through the monthly reconciliation (B.5), the monthly log review, and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9. No exception may allow a shared account without MFA on the customs platform or the bank portal, or a payment change without a call-back.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; P01 risk register; P02 SSP control statements AC-2, AC-5, IA-2(1), PS-4
