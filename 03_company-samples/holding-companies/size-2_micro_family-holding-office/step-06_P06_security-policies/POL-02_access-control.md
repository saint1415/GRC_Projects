# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Family Office Director (Qualified Individual) |
| Approved by | Principal, 2026-09-18 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, RA-5, PS-8, SA-9, CA-2, PM-28. Part B: AC-1, AC-2, AC-3, AC-5, AC-6, AC-11, AC-17, AC-19, AU-6, AU-11, SI-4, IA-2, IA-2(1), IA-5, PS-4, PS-7. Part C: PL-4, AT-2, AT-2(3) |
| CSF 2.0 | GV.OC-03, GV.RR-01, GV.RR-02, GV.RR-04, GV.RM-02, GV.PO-01, GV.PO-02, GV.SC-05, GV.SC-07, ID.RA-01, ID.RA-05, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.AT-02, DE.CM-03 |
| Regulation | 16 CFR 314.3(a); 314.4(a), (b), (c)(1), (c)(5), (c)(7), (c)(8), (d)(1), (e), (f), (g); Fla. Stat. 501.171(2); 17 CFR 275.202(a)(11)(G)-1(b) |

**Why this policy has three parts.** A 7-person office does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C. Together with POL-03, POL-04, and the SSP (P02), this policy is the office's written information security program under 16 CFR 314.3(a).

## 1. Purpose
Set up the office's security program, make sure only authorized people reach family, subsidiary, and office information and only as far as their job requires, protect the payments the office makes, and tell the workforce how to use office systems.

## 2. Scope
All workforce members of Cris Santos Company, LLC (employees, temporary staff, and interns), subsidiary staff with guest accounts, and family members with vault accounts, for the parts that apply to them. It covers every system in the Family Office Shared Services Platform and every copy of office information, including systems the MSP and vendors run for the office.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Principal | Approves policies and the security budget; accepts Moderate risks; decides sanctions with the Family Office Director |
| Board of Managers | Accepts or rejects treatment plans for High and Very High risks; receives the annual written security report |
| Family Office Director | Qualified Individual; runs this policy; approves access; reviews logs and accounts monthly |
| Office Manager | Creates and removes accounts and guest accounts; keeps the onboarding and offboarding checklists; coordinates the MSP |
| Controller | Owns the payment verification procedure (B.10) and bank entitlements |
| MSP | Operates device and server controls; uses named, MFA-protected accounts |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Qualified Individual.** The Family Office Director is the Qualified Individual responsible for overseeing, implementing, and enforcing the information security program. The Principal must record the designation in writing and update it within 30 days of any change. If the role is ever given to the MSP or a consultant, the office must keep responsibility, name a senior staff member to oversee that person, and require the provider to keep a program that protects the office. (PM-2; GV.RR-02; 16 CFR 314.4(a))

A.2 **Risk assessment.** The Family Office Director must update the written risk assessment every August, and after any major change such as restarting the AI assistant pilot, replacing SYS-11, adding a subsidiary, or a new vendor that holds family information, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-05; 16 CFR 314.4(b), (b)(2))

A.3 **Risk acceptance and appetite.** The Family Office Director may accept Low and Very Low risks. Only the Principal may accept a Moderate risk. High and Very High risks must not be accepted; the Board of Managers approves a dated treatment plan instead. The office has **no appetite** for (a) a payment to a new or changed bank account without a recorded callback, or (b) family members' identity documents reachable by anyone without a need to see them. (PM-9; GV.RM-02)

A.4 **Sanctions.** A workforce member who breaks a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Family Office Director must record each sanction, and the Principal must approve suspension or termination. Reporting a mistake in good faith, including clicking a phishing link, is never sanctioned. (PS-8; GV.RR-04)

A.5 **Service providers.** Before a vendor receives or can reach family or office information, the Family Office Director must check that it can protect it (security questions, SOC 2 report, or equivalent), and the contract must require it to maintain safeguards and to report security incidents. The Family Office Director keeps a service provider list and reviews each provider at least yearly, starting with those that hold the most sensitive information. (SA-9; GV.SC-05; 16 CFR 314.4(f)(1)-(3))

A.6 **Evaluation, testing, and adjustment.** Security controls must be assessed at least once a year by someone who does not operate them. The MSP must scan the office network and SYS-11 for vulnerabilities every month and fix critical and high findings within 14 days, or record an exception under A.9. The program must be adjusted after each assessment, each risk update, and any material change. (CA-2; RA-5; 16 CFR 314.4(d)(1), (g))

A.7 **Annual report.** The Family Office Director must give the Board of Managers a written report each September on the overall status of the program and material matters: risk decisions, service providers, test results, security events, and recommended changes. This follows 16 CFR 314.4(i), which the office adopts voluntarily. (PM-9; GV.RR-01)

A.8 **Policy review and access to policies.** The Family Office Director must review this policy set every August and after an incident or major change, and must keep the current version in the Office site where every workforce member can read it. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. An exception to MFA (B.3) or encryption (POL-04 4.2) must also be approved in writing by the Qualified Individual. (PL-1; 16 CFR 314.4(c)(3), (c)(5))

A.10 **Family clients only.** The office gives investment advice only to family clients as defined in 17 CFR 275.202(a)(11)(G)-1(d)(4). Before anyone new receives advice, co-invests alongside the family, or receives investment materials, the Investment Director must confirm eligibility in writing, and counsel must review any doubtful case. (PM-28; GV.OC-03)

### Part B. Access control
B.1 **Unique accounts.** Every workforce member, guest, MSP technician, and family vault user must have their own account. Shared or generic accounts are not allowed. The MSP's shared global administrator account must be replaced by named accounts by 2026-12-31. (IA-2; AC-2; PR.AA-01; 16 CFR 314.4(c)(1)(i))

B.2 **Least privilege and need to know.** Access must match the person's job. Family information is grouped by family branch, and staff are added only to the branches they serve. Tax returns, identity documents, estate plans, and medical bills are kept only in the vault (POL-04 4.3). Each subsidiary's guests see only their own subsidiary's folder. The Family Office Director approves access in writing on the onboarding checklist. (AC-3; AC-6; PR.AA-05; 16 CFR 314.4(c)(1)(ii))

B.3 **MFA.** MFA is required for every person accessing any office system, including guests, family vault users, and MSP technicians. Staff and administrators must use phishing-resistant security keys once issued (target 2026-12-31). SMS codes are not allowed for staff or administrators. SYS-11 may be reached only through the MSP's MFA-protected gateway. (IA-2(1); PR.AA-03; 16 CFR 314.4(c)(5))

B.4 **Administrator rights.** No more than two named people may hold standing global administrator rights in SYS-02 (the Office Manager and one named MSP technician); other administrator rights are granted only when needed and removed after use. (AC-6; AC-2)

B.5 **Offboarding.** On or before a workforce member's last day, the Office Manager must complete the offboarding checklist: disable the SYS-02 account (which ends single sign-on), remove bank and custodian entitlements and collect tokens, remove vault and bill pay access, remove MFA registrations, collect the laptop and keys, and remind the person in writing of their confidentiality duty. For an involuntary termination, access must be disabled before the person is told. Subsidiaries must tell the office within 1 business day when a guest leaves. (PS-4; AC-2; 16 CFR 314.4(c)(1)(i))

B.6 **Monthly reconciliation.** Each month the Office Manager must compare the user lists of SYS-01 to SYS-07 and SYS-11, and the bank and custodian entitlement reports, with the staff roster and the subsidiaries' guest list, and remove anything that does not match. Guest accounts expire after 180 days unless renewed. Each quarter the Family Office Director must confirm that each person's access still fits their job. (AC-2; AC-6; PR.AA-05)

B.7 **Locking.** Laptops must lock after 10 minutes idle. Personal phones that hold office email must use the office's app protection policy (PIN, no saving to the phone, remote wipe of office data) from 2026-11-30. (AC-11; AC-19)

B.8 **Vendor and MSP access.** MSP technicians and vendor support staff must use named accounts with MFA. The MSP must give the Family Office Director a current list of technicians with access every year and must not change firewall rules, SYS-02 security settings, or SYS-11 without approval recorded in the MSP ticket. (AC-17; PS-7; IA-2(1); 16 CFR 314.4(c)(7))

B.9 **Passwords.** Passwords must be at least 12 characters, unique to each system, and kept in the office password manager. The staff Wi-Fi password must be changed every year and whenever a workforce member leaves. (IA-5)

B.10 **Payment verification.** No one may change a payee's bank details, set up a new payee, or release a wire over $10,000 on the strength of an email, text, or call alone. The requester must be called back at a number already on file (never a number in the request), and the callback must be recorded in the payment log with the date, the number called, and who confirmed. A second staff member must check the log entry before release. Bank and bill pay dual approval must stay on. Family members and subsidiaries are told this rule in writing. (AC-5; AT-2(3); PR.AT-02)

B.11 **Log review and alerts.** The MSP must route SYS-02 alerts for risky sign-ins, new inbox rules, external forwarding, mass downloads, and administrator changes to the Family Office Director and the MSP help desk. Each month the Family Office Director must review sign-in, mailbox rule, and administrator activity with the log review checklist, record the review, and open an incident under POL-03 for anything unexplained. Audit logs must be kept for at least one year. (AU-6; AU-11; SI-4; DE.CM-03; 16 CFR 314.4(c)(8))

### Part C. Workforce use rules (essentials of POL-05)
C.1 Office systems are for office work. Workforce members must open only the family and subsidiary information their job needs. (PL-4; PR.AT-01)

C.2 Workforce members must not store or send office information with personal email, personal cloud storage, or messaging apps, and must not enter family, subsidiary, or office information into any AI tool that is not on the approved-tools list in POL-04 4.6. (PL-4)

C.3 Workforce members must lock their screen when stepping away and never share passwords, security keys, bank tokens, or MFA codes with anyone, including the MSP and family members. (AC-11; PL-4)

C.4 Workforce members must complete security training at hire and every year, including the payment-fraud module, and take part in phishing simulations. (AT-2; AT-2(3); 16 CFR 314.4(e)(1))

C.5 Workforce members must report suspected incidents at once under POL-03 section 4.2, including their own mistakes and any payment request that seems unusual. (IR-6)

C.6 **Public communications.** Workforce members must not describe the office in public profiles, speeches, or vendor references as offering investment advice or services to anyone outside the family. The Investment Director checks staff public profiles each year. (PL-4; 17 CFR 275.202(a)(11)(G)-1(b)(3))

C.7 Workforce members must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Family Office Director checks compliance through the monthly reconciliation (B.6), the monthly log review (B.11), the quarterly payment log review (B.10), and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and offboarding checklists; payment log; P01 risk register; P02 SSP control statements AC-2, AC-5, IA-2(1), PS-4
