# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Center Director (Information Security Coordinator) |
| Approved by | Owner, 2026-08-28 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after material changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PL-2, RA-3, PM-9, PS-8, SA-9, CA-2, PL-1. Part B: AC-2, AC-3, AC-6, AC-11, AC-17, AC-18, AC-20, IA-2, IA-2(1), IA-5, PS-4, SC-7. Part C: PL-4, PS-7, AT-2, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, ID.IM-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.IR-01 |
| COPPA Rule | 16 CFR 312.8(a), (b)(1)-(5), (c) |
| District contract | Data privacy agreement terms flowing from 34 CFR 99.31(a)(1)(i)(B) and 99.33(a) |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C. Together with POL-03, POL-04, and the SSP (P02), this policy is the company's **written information security program** under 16 CFR 312.8(b).

## 1. Purpose
Set up the company's security program, make sure only authorized people reach students' and families' information and only as far as their work requires, and tell staff and contractor tutors how to use company systems.

## 2. Scope
All workforce members of Cris Santos Company: employees, the 14 contractor tutors, temporary staff, and volunteers. "Workforce" in this policy always includes contractor tutors. It covers every system and every copy of company information, including systems run for the company by the MSP and SaaS vendors and contractor tutors' own computers when used for company work.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves policies and the security budget; accepts Moderate risk; decides sanctions with the Center Director |
| Center Director | Information Security Coordinator; runs this policy; grants and removes access in the suite and through the MSP; reviews accounts and logs |
| Director of Tutoring | Grants and removes tutoring platform access; assigns students to tutors |
| Enrollment and Billing Coordinator | Grants and removes scheduling platform access |
| MSP | Creates and disables suite and device accounts on the Center Director's request; operates device and network controls |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Information Security Coordinator.** The Center Director is the employee designated to coordinate the information security program. The Owner must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02; 312.8(b)(1))

A.2 **Written program.** The written information security program consists of the SSP (P02), this policy, POL-03, and POL-04. Its safeguards must fit the sensitivity of children's information and the company's size. (PL-2; GV.PO-01; 312.8(b))

A.3 **Risk assessment.** The Center Director must update the risk assessment every July, and after any material change such as a new platform, a new vendor that receives children's information, a new district contract, or turning on an AI feature, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01; 312.8(b)(2)-(3))

A.4 **Risk acceptance.** The Center Director may accept Low and Very Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. A risk to a child's safety is never accepted above Low. (PM-9; GV.RM-01)

A.5 **Sanctions.** A workforce member who breaks a security or privacy rule must face consequences in proportion to intent and harm: coaching and retraining, a written warning, suspension, termination, or, for a contractor tutor, ending the contract. The Center Director must record each sanction, and the Owner must approve suspension, termination, or ending a contract. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.6 **No written assurances, no children's data.** Before any vendor, contractor, or other third party collects, keeps, or receives children's information for the company, the Center Director must check that it can protect the information and must get its written commitment to do so (a contract term, data processing addendum, or signed agreement). That includes trials, pilots, free tools, and new features a vendor switches on. The Center Director keeps these in the vendor folder and reviews the tutoring platform vendor's SOC 2 report every year. (SA-9; GV.SC-05; 312.8(c))

A.7 **Assessment.** Security controls must be assessed at least once a year by someone who does not operate them, and after material changes. (CA-2; ID.IM-01; 312.8(b)(4))

A.8 **Program evaluation and policy review.** Every August, after the July risk assessment, the Center Director must evaluate the program against the risk assessment, test results, and any material changes, update the policies, and keep the current versions in the shared drive where every workforce member can read them. (PL-1; GV.PO-02; 312.8(b)(5))

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.4, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

### Part B. Access control
B.1 **Unique accounts.** Every workforce member must have their own account in the tutoring platform, the scheduling platform, and the suite. Shared or generic staff accounts are not allowed. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** Access must match the person's work. Tutors see only the students assigned to them in the platform. The "Student files" folder is limited to the Center Director and the Director of Tutoring. Platform administrator roles are limited to the Director of Tutoring and one backup. The Center Director approves access in writing (the onboarding checklist) before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for the suite, for every tutor and administrator account in the tutoring platform, for the scheduling platform administrator, and for every administrator login held by the MSP (backup console, firewall, remote management). Children's student portal accounts are exempt (see SSP section 11). (IA-2(1); PR.AA-03; 312.8(b)(3))

B.4 **Offboarding.** On or before a workforce member's last day, or a contractor tutor's last session, the Center Director must complete the offboarding checklist: disable platform, scheduling, and suite accounts; ask the MSP to remove device access; remove MFA registrations; collect keys and devices; and, for contractor tutors, get written confirmation that any student information on their own computers has been deleted. For an involuntary departure, access must be disabled before the person is told. (PS-4; AC-2; PR.AA-01)

B.5 **Monthly reconciliation.** Each month the Center Director must compare the user lists of the platform, the scheduling platform, the suite, the website, and the backup console with the staff and contractor roster, and remove anything that does not match. Every quarter the Director of Tutoring must confirm each tutor's student assignments still fit. (AC-2; AC-6; PR.AA-05)

B.6 **Locking.** Company computers must lock after 10 minutes idle. The front-desk desktop must use individual sign-ins. Student tablets stay in kiosk mode with no student data stored. (AC-11; PR.AA-03)

B.7 **MSP and vendor access.** MSP technicians and vendor support staff must use named accounts with MFA. The MSP must give the Center Director a current list of technicians with access every year. (AC-17; IA-2(1); SA-9)

B.8 **Passwords and networks.** Passwords must be at least 12 characters and never reused from personal accounts. Student and guest devices must be on a network separated from staff devices. The staff Wi-Fi password must be changed every year and whenever a workforce member leaves. (IA-5; SC-7; AC-18; PR.IR-01)

B.9 **Contractor tutors' own computers.** A contractor tutor may use a personal computer for company work only if it runs a supported operating system with automatic updates, has a screen lock and built-in device encryption turned on, and is not shared with other household members while signed in. Student information must stay in the platform: contractor tutors must not download, print, or email student records, and the company does not send rosters by email. Each contractor tutor signs an attestation at the start of each school year. (AC-20; ID.AM-02; 312.8(b)(3); district DPA)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Workforce members must access only the information of students they work with, and only for tutoring. (PL-4; PR.AT-01)

C.2 Workforce members must not store or send students' information with personal email, personal cloud storage, personal messaging apps, or public AI chatbots. POL-04 section 4.6 lists the approved tools. (PL-4)

C.3 Workforce members must lock their screen when stepping away and never share passwords or MFA codes, including with the MSP. (AC-11; PL-4)

C.4 Workforce members must complete security and privacy training when they start and every year, and must take part in phishing simulations. (AT-2; PR.AT-01)

C.5 Workforce members must report suspected incidents at once under POL-03 section 4.2, including their own mistakes. (IR-6)

C.6 Employees must sign an acknowledgment of this policy when they start and after each annual update. Contractor tutors accept these rules as part of their contractor agreement, which also includes confidentiality, the device rules in B.9, and the reporting rule in C.5. (PL-4; PS-7)

C.7 Tutors must communicate with students only through the tutoring platform or in person at the center or a program site. They must never contact a student through personal phone numbers, personal email, or social media, and must never record or photograph a student outside the platform. (PL-4; PS-7; GV.RR-04)

## 5. Compliance and enforcement
Breaking this policy leads to consequences under A.5. The Center Director checks compliance through the monthly reconciliation (B.5), the monthly log review, Lead Tutors' monthly spot review of messages and recordings, and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and offboarding checklist; contractor tutor agreement and attestation; P01 risk register; P02 SSP control statements AC-2, AC-20, IA-2(1), PS-4, PS-7
