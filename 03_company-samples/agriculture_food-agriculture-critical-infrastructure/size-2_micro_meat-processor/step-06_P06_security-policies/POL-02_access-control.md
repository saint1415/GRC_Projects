# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (security and compliance lead) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, SI-12, CA-2. Part B: AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, IA-2, IA-2(1), IA-5, PS-4, MA-4, CM-3. Part C: PL-4, AT-2 |
| CSF 2.0 | GV.RR-02, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.PS-01, PR.AT-01 |
| FSIS rules supported | 9 CFR 416.16(a)-(b); 417.4(a)(3); 417.5(b)-(d); 417.2(d); 416.12(b) |

**Why this policy has three parts.** A 7-person plant does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people reach company systems, plant machines, and records, and only as far as their job requires, and tell everyone how to use company systems.

## 2. Scope
All employees, temporary workers, and anyone working for the company. It covers every system and copy of company information, including the plant machines (smokehouse controller, line controls, label printer), the floor tablets, the SaaS services, and systems run for the company by the MSP and equipment vendors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner and General Manager | Approves policies and the security budget; accepts Moderate risk; decides sanctions with the Office Manager |
| Office Manager | Security and compliance lead; runs this policy; grants and removes access; keeps the account and vendor lists; reviews logs |
| Production Supervisor | Approves changes to cook cycles, formulations, and label templates; decides whether a change needs a HACCP reassessment |
| Maintenance and Sanitation Technician | Turns vendor remote sessions on and off and supervises them; keeps machine baselines |
| MSP | Creates and disables suite and PC accounts on the Office Manager's request; operates PC and network controls |
| Everyone | Protect passwords and PINs; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security lead.** The Office Manager is the designated security and compliance lead. The owner must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The Office Manager must update the risk register every July, and after any major change such as a new machine with remote support, a new SaaS service that holds food safety records, or the AI camera leaving its pilot, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Office Manager may accept Low and Very Low risks. Only the owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the owner. A risk that could put unsafe or misbranded food into commerce is never accepted. (PM-9; GV.RM-01)

A.4 **Sanctions.** Anyone who breaks a security rule must be dealt with in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The owner decides suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8)

A.5 **Vendors.** No vendor may connect to a plant machine, hold company records, or receive Restricted information (POL-04) until the Office Manager has recorded it on the vendor list with its access method and contact. New contracts and renewals with the MSP, equipment vendors, and SaaS vendors must include security incident notice and named-account terms. (SA-9; GV.SC-05)

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2)

A.7 **Retention.** Security documents (policies, risk register, assessments, incident records, vendor list, training records) must be kept at least 3 years. Food safety records follow the FSIS retention periods (9 CFR 416.16(c); 417.5(e)). (SI-12; GV.PO-02)

A.8 **Policy review and access.** The Office Manager must review this policy set every August and after an incident or major change, and keep the current version where every employee can read it, with a printed copy in the production office. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated on the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

### Part B. Access control
B.1 **Named accounts.** Every person must have their own account in the productivity suite, the records app, the accounting service, the cold-chain dashboard, and on the labeling PC. Shared or generic accounts are not allowed, except the smokehouse operator PIN until the controller supports named users; that PIN is changed every 90 days and whenever someone leaves. Records app entries are made under the person's own account; typed initials under someone else's account are not allowed. (IA-2; AC-2; PR.AA-01; 9 CFR 416.16(a); 417.5(b))

B.2 **Least privilege.** Access must match the person's job. The Office Manager approves access in writing on the joiner checklist before it is granted. Administrator rights in the records app, suite, and labeling PC are limited to two named people, never a vendor default account. (AC-2; AC-3; AC-6; PR.AA-05; 9 CFR 417.5(d))

B.3 **MFA.** MFA is required for the productivity suite, the accounting service, the payroll service, the records app administrator, the cold-chain dashboard where offered, the smokehouse manufacturer portal, and every administrator login, including logins held by the MSP (firewall, backup console, remote management). (IA-2(1); PR.AA-03)

B.4 **Leavers.** On or before a person's last day, the Office Manager must complete the leaver checklist: disable all accounts, ask the MSP to remove PC access, change the smokehouse PIN and any password the person knew, collect keys, and remind the person in writing of their confidentiality duty. For an involuntary departure, access is removed before the person is told. (PS-4; AC-2)

B.5 **Monthly reconciliation.** Each month the Office Manager must compare the user lists of the suite, records app, accounting service, cold-chain dashboard, smokehouse portal, and backup console with the staff roster and the vendor list, and remove anything that does not match. (AC-2; AC-6; PR.AA-05)

B.6 **Locking.** Office computers lock after 10 minutes idle. The labeling PC and floor tablets may stay unlocked during the production shift because gloved workers use them, but each entry is made under the person's own account (B.1) and they lock at the end of the shift. (AC-11)

B.7 **Emergency access.** A sealed envelope in the owner's office safe holds the records app administrator, firewall, and smokehouse controller administrator credentials. Any use must be logged and the password changed afterwards. (AC-2)

B.8 **Vendor remote access.** Vendor remote connections to plant machines and the labeling PC are off by default. The Maintenance and Sanitation Technician turns a connection on only for a requested job, watches the session when practical, turns it off afterwards, and records it in the maintenance log (vendor, person, time, what was changed). Vendors must use named accounts with MFA where the service offers it. No unattended remote access tools may be installed without the Office Manager's approval. (AC-17; MA-4; IA-2(1); PR.AA-05)

B.9 **Passwords.** Passwords must be at least 12 characters, unique to the company, and never written on equipment. The staff Wi-Fi password changes every year and whenever someone leaves. (IA-5)

B.10 **Changes to food safety settings.** Changes to smokehouse cycles, formulations, line settings, and label templates must be recorded in the change log, checked by a second person, and approved by the Production Supervisor before use. For each change, the Production Supervisor records whether it requires a HACCP reassessment or an SSOP update, and the owner signs and dates any modified plan or SSOP. A copy of the approved setting is kept offline. (CM-3; PR.PS-01; 9 CFR 417.4(a)(3); 417.2(d); 416.12(b); 416.14)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems and machines are for company work. Only change machine settings you are trained and approved to change. (PL-4; PR.AT-01)

C.2 Do not put Restricted information (POL-04) in personal email, personal cloud storage, messaging apps, or public AI chatbots. (PL-4)

C.3 Never share passwords, PINs, or MFA codes, including with vendors or the MSP. Never write them on equipment. (IA-5; PL-4)

C.4 Complete security training at hire and every year, and take part in phishing simulations if you use company email. (AT-2; PR.AT-01)

C.5 Report suspected incidents at once under POL-03 section 4.2, including your own mistakes and anything odd on a machine screen. (IR-6)

C.6 Sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Office Manager checks compliance through the monthly reconciliation (B.5), the change log review, and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9. The smokehouse operator PIN in B.1 is a recorded exception (expires 2027-08-31).

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; joiner and leaver checklists; change log; maintenance log; vendor list; P01 risk register; P02 SSP control statements AC-2, AC-17, IA-2, CM-3, MA-4
