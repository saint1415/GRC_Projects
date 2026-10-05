# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (Security Lead) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, SI-12, CA-2. Part B: AC-2, AC-3, AC-6, AC-11, AC-17, MA-4, IA-2, IA-2(1), IA-5, PS-4. Part C: PL-4, AT-2 |
| CSF 2.0 | GV.OC-03, GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, ID.IM-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01 |
| Regulatory drivers | C-TRANSPORTATION-S01 (49 CFR 1570.105(b), 1570.201); C-TRANSPORTATION-BM |

**Why this policy has three parts.** A 7-person railroad does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the railroad's security program, make sure only authorized people reach company systems and information and only as far as their job requires, and tell employees how to use company systems.

## 2. Scope
All employees of Cris Santos Company, temporary staff, and contractors with access to company systems. It covers every system and every copy of company information, including systems run for the company by the MSP and SaaS vendors, the radio system, and the crew tablets.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner and General Manager | Approves policies and the security budget; accepts Moderate and higher risk; primary TSA Security Coordinator; decides sanctions with the Office Manager |
| Office Manager | Security Lead; runs this policy; grants and removes access; reviews logs and accounts; directs the MSP |
| Roadmaster | Alternate TSA Security Coordinator; relief dispatcher |
| MSP | Creates and disables suite and device accounts on the Office Manager's request; operates device controls |
| All employees | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security roles.** The Office Manager is the Security Lead. The Owner and General Manager is the primary TSA Security Coordinator and the Roadmaster the alternate. The General Manager must send TSA the Security Coordinators' details within 37 calendar days of any change, and at least one Security Coordinator must be reachable at all times through the registered number, which rings both of them. (PM-2; GV.RR-02; 49 CFR 1570.201(e)-(f))

A.2 **Risk assessment.** The Office Manager must update the risk assessment every July, and after any major change such as a new operations system, a new vendor holding company data, a new commodity, or expanding the AI pilot, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Office Manager may accept Low and Very Low risks. Only the Owner and General Manager may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner and General Manager. A risk to train or roadway worker safety is never accepted at High. (PM-9; GV.RM-01)

A.4 **Sanctions.** An employee who breaks a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Office Manager records each sanction, and the Owner and General Manager approves suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Vendors.** No vendor may hold company data or have remote access to company systems until the Office Manager has reviewed its terms for security, incident notice, and data return and deletion. Contracts signed or renewed after 2026-09-01 must require notice of a security incident affecting company data or systems within 24 hours. The Office Manager reviews the operations SaaS vendor's SOC 2 report and the MSP's security evidence every year. (SA-9; GV.SC-05)

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2; ID.IM-01)

A.7 **Retention.** Security policies, risk assessments, assessments, incident records, TSA reports, training records, and sanction records must be kept for at least 3 years. The hazmat security plan is kept as long as it is in effect, with all copies kept current (49 CFR 172.802(c)). (SI-12; GV.PO-02)

A.8 **Policy review and access to policies.** The Office Manager must review this policy set every August and after an incident or major change, and keep the current version in the shared drive where every employee can read it. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated with the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

A.10 **Changes that bring new duties.** Before the railroad accepts a new customer or commodity, changes a route, or adds an interchange movement, the General Manager must check whether the change brings TSA duties (part 1580 subparts B or C, including RSSM such as anhydrous ammonia), hazmat security plan changes, or PTC duties (more than 4 unequipped trains a day or a move of 20 miles or more on the Class I's PTC line), and notify TSA where 49 CFR 1570.105(b) requires. (PM-9; GV.OC-03)

### Part B. Access control
B.1 **Unique accounts.** Every employee must have their own account in the operations system, the productivity suite, the telematics portal, and the payroll system. Shared or generic accounts are not allowed. The shared crew login must be replaced by named crew accounts by 2026-11-30; until then its password must be changed every 90 days and whenever a crew member leaves. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** Access must match the person's job. Only employees qualified as dispatchers (today the General Manager and the Roadmaster) may hold the dispatcher role that issues authorities in the operations system. Administrator accounts are used only for administration; each administrator also has a daily-use account. The Office Manager approves access in writing (the onboarding checklist) before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for the operations system, the productivity suite, the payroll system, the telematics portal, and every administrator login, including logins held by the MSP (backup console, firewall, remote management). Push approvals must use number matching. (IA-2(1); PR.AA-03)

B.4 **Termination.** On or before an employee's last day, the Office Manager must complete the termination checklist: disable the operations system, suite, telematics, and payroll accounts; change any shared secret the person knew; remove MFA registrations; collect keys, the tablet, and the handheld radio; and ask the MSP to remove device access. For an involuntary termination, access must be disabled before the person is told. (PS-4; AC-2; PR.AA-05)

B.5 **Monthly reconciliation.** Each month the Office Manager must compare the user lists of the operations system, suite, telematics portal, payroll system, and backup console with the employee roster, and remove anything that does not match. Every quarter the Office Manager must confirm each person's role still fits their job. (AC-2; AC-6; PR.AA-05)

B.6 **Locking.** Computers and tablets must lock after 10 minutes idle. The dispatch desktop may stay unlocked only while a dispatcher is at the desk; the dispatcher locks it when leaving. (AC-11; PR.AA-03)

B.7 **Emergency access.** A sealed copy of an operations system administrator credential is kept in the General Manager's office safe for use when neither manager can sign in. Any use must be reported to the Office Manager and the password changed afterwards. (AC-2)

B.8 **MSP and vendor remote access.** MSP technicians and vendor support staff must use named accounts with MFA. The MSP must give the Office Manager a current list of technicians with access every year. Remote work on the dispatch desktop during operating hours needs the dispatcher's approval at the time. (AC-17; MA-4; IA-2(1); SA-9)

B.9 **Passwords and shared secrets.** Passwords must be at least 12 characters and never reused from personal accounts. The Wi-Fi password must be changed every year and whenever an employee leaves. Installation or default passwords must be changed before a device or service goes into use. (IA-5; PR.AA-01)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. (PL-4; PR.AT-01)

C.2 Employees must not store or send company Restricted information (POL-04) with personal email, personal cloud storage, personal messaging apps, or public AI chatbots. POL-04 section 4.7 lists the approved AI tools. (PL-4)

C.3 Employees must lock their screen when stepping away, never share passwords or MFA codes (including with the MSP), and never approve an MFA prompt they did not start. (AC-11; PL-4)

C.4 Employees must complete security awareness training at hire and every year, and take part in phishing simulations. (AT-2; PR.AT-01)

C.5 Employees must report suspected incidents at once under POL-03 section 4.2, including their own mistakes. (IR-6)

C.6 Any request to change payment or bank details, from a customer, vendor, or employee, must be confirmed by phone using a number already on file, never one given in the request. (AT-2; PL-4)

C.7 Employees must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Office Manager checks compliance through the monthly reconciliation (B.5), the monthly log review, and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; P01 risk register; P02 SSP control statements AC-2, IA-2, IA-2(1), PS-4, PM-2
