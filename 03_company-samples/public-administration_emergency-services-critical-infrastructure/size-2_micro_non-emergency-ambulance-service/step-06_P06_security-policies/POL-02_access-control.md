# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (Privacy Officer and Security Officer) |
| Approved by | Owner, 2026-09-04 |
| Effective date | 2026-09-08 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, SI-12, CA-2. Part B: AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, IA-2, IA-2(1), IA-5, PS-4, AU-6. Part C: PL-4, AT-2, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, DE.CM-03 |
| HIPAA Security Rule (C-EMERGENCY-R04) | 164.308(a)(1), (a)(1)(ii)(A)-(D), (a)(2), (a)(3), (a)(4), (a)(5), (a)(8), (b)(1); 164.310(b), (c); 164.312(a), (d); 164.316 |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people reach patient and company information and only as far as their job requires, and tell the workforce how to use company systems and devices, in the office and in the ambulances.

## 2. Scope
All workforce members of Cris Santos Company: the Owner, employees, part-time and per diem crew members, students on ride-alongs, and the contracted Medical Director when using company systems. It covers every system and every copy of company information, including systems run for the company by the MSP and SaaS vendors, the facility request portal, and the devices in the ambulances. It applies to ePHI and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves policies and the security budget; accepts Moderate risk; decides sanctions with the Office Manager |
| Office Manager | Privacy Officer and Security Officer; runs this policy; grants and removes access, including facility portal accounts; reviews logs and accounts |
| Scheduler-Dispatcher | Uses the dispatch board under a named account; reports access problems; keeps the dispatch desk rules in C.3 |
| MSP | Creates and disables suite and device accounts on the Office Manager's request; operates device controls |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security and Privacy Officer.** The Office Manager is the designated HIPAA Security Officer and Privacy Officer. The Owner must keep the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02; 164.308(a)(2))

A.2 **Risk analysis.** The Office Manager must update the risk analysis every August, and after any major change such as a new operations platform, a new vendor handling ePHI, a 911 zone from the county, or wider use of the AI intake assistant, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01; 164.308(a)(1)(ii)(A)-(B))

A.3 **Risk acceptance.** The Office Manager may accept Low and Very Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. A risk that could cause a missed dialysis session or a missed 911 redirect must not be accepted at Moderate or above without treatment. (PM-9; GV.RM-01)

A.4 **Sanctions.** A workforce member who breaks a security or privacy rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Office Manager must record each sanction, and the Owner must approve suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))

A.5 **No BAA, no ePHI.** No vendor may create, receive, maintain, or transmit ePHI for the company until a business associate agreement is signed or accepted, and the agreement must cover the specific feature in use. That includes trials, pilots, free features, and AI features added to an existing service. The Office Manager keeps every BAA in the security folder and checks each year that the MSP and the platform vendor hold BAAs with their own subcontractors. (SA-9; GV.SC-05; 164.308(b)(1); 164.314(a))

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2; 164.308(a)(8))

A.7 **Retention of security records.** Security policies, procedures, risk analyses, assessments, incident records, BAAs, training records, and sanction records must be kept for 6 years from the date created or the date last in effect, whichever is later. (SI-12; GV.PO-02; 164.316(b)(2)(i))

A.8 **Policy review and access to policies.** The Office Manager must review this policy set every August and after an incident or major change, and must keep the current version in the shared drive and in the dispatch binder, where every workforce member can read it. (PL-1; GV.PO-02; 164.316(b)(2)(ii)-(iii))

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

### Part B. Access control
B.1 **Named accounts only.** Every workforce member must have their own account in the operations platform (dispatch board and ePCR), the productivity suite, and the phone system. Shared or generic accounts are not allowed. The shared "dispatch" account must be retired by 2026-10-31; until then its password was changed on 2026-09-08 and its use is limited to the dispatch desktop and the on-call phone. (IA-2; AC-2; PR.AA-01; 164.312(a)(2)(i))

B.2 **Least privilege.** Access must match the person's job, using the platform's role list (dispatcher, crew, billing, administrator). The Office Manager must approve access in writing on the onboarding checklist before it is granted. Platform administrator roles are limited to the Office Manager and the Owner as backup. Facility portal accounts are created only on a written request from the facility and must see only that facility's trips. (AC-2; AC-3; AC-6; PR.AA-05; 164.308(a)(4)(ii)(B)-(C))

B.3 **MFA.** MFA is required for the operations platform (every user, including crews and administrators), the productivity suite, the billing portal, and every administrator login, including logins held by the MSP (backup console, firewall, remote management). (IA-2(1); PR.AA-03; 164.312(d))

B.4 **Termination.** On or before a workforce member's last day or last shift, the Office Manager must complete the termination checklist: disable platform, suite, and phone accounts; remove MFA registrations; ask the MSP to remove device access; collect keys, phones, and tablets; change any code or password the person knew; and remind the person in writing of their confidentiality duty. For a per diem crew member who has not worked for 60 days, the account must be disabled until the next shift is scheduled. For an involuntary termination, access must be disabled before the person is told. (PS-4; AC-2; 164.308(a)(3)(ii)(C))

B.5 **Monthly reconciliation.** Each month the Office Manager must compare the user lists of the platform (including facility portal users), suite, phone system, and backup console with the staff roster, and remove anything that does not match. Every quarter the Office Manager must confirm each person's platform role still fits their job. Each year the Office Manager must ask each facility to confirm its portal users. (AC-2; AC-6; PR.AA-05; 164.308(a)(4)(ii)(C))

B.6 **Log review.** Each week the Office Manager must check the platform's export log for exports nobody expected. Each month the Office Manager must review the platform access report, the suite sign-in alerts, and the MSP report using the review checklist, and report findings to the Owner. (AU-6; DE.CM-03; 164.308(a)(1)(ii)(D))

B.7 **Locking.** Tablets and phones must lock after 2 minutes idle, and computers after 10 minutes. The dispatch desktop is the only exception: it may keep the board on screen, but the screen must face away from the door, carry a privacy filter, and require the dispatcher's quick re-sign-in after 10 minutes idle once named accounts are in place. (AC-11; 164.310(c); 164.312(a)(2)(iii))

B.8 **Emergency access.** A sealed copy of a platform administrator credential, with its MFA recovery code, must be kept in the Owner's safe for use when neither the Office Manager nor the Owner can sign in. Any use must be reported to the Office Manager, and the password changed afterwards. (AC-2; 164.312(a)(2)(ii))

B.9 **Vendor and MSP access.** MSP technicians and vendor support staff must use named accounts with MFA. No remote access tool may be installed on a company device except the MSP's managed tool. The MSP must give the Office Manager a current list of technicians with access every year. (AC-17; IA-2(1); SA-9)

B.10 **Passwords and shared secrets.** Passwords must be at least 12 characters and never reused from personal accounts. The office Wi-Fi password and the alarm codes must be changed every year and whenever a workforce member who knew them leaves. (IA-5; 164.308(a)(5)(ii)(D))

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Workforce members must access only the patient information they need for the trip in front of them, and never look up their own, family members', or neighbors' records. (PL-4; PR.AT-01; 164.310(b))

C.2 Workforce members must not store or send patient information with personal email, personal cloud storage, personal messaging apps, personal phones, or public AI chatbots. Photos of face sheets, wristbands, or monitors must never be taken on a personal phone. POL-04 section 4.6 lists the approved tools. (PL-4; 164.310(b))

C.3 Workforce members must lock their screen or tablet when stepping away, keep tablets in the ambulance cab or with the crew, keep the dispatch screen out of visitors' view, and never share passwords or MFA codes, including with the MSP or vendor support. (AC-11; PL-4; 164.310(b)-(c))

C.4 Workforce members must complete security and privacy training at hire and every year, and must take part in phishing simulations. The Scheduler-Dispatcher must also complete the recording announcement and AI intake training before using those features. (AT-2; PR.AT-01; 164.308(a)(5))

C.5 Workforce members must report suspected incidents at once under POL-03 section 4.2, including their own mistakes and lost devices. (IR-6)

C.6 Workforce members must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Office Manager checks compliance through the weekly export check and monthly reconciliation (B.5, B.6) and the MSP report. The annual independent assessment (P07) tests it.

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; log review checklist; P01 risk register; P02 SSP control statements AC-2, IA-2, IA-2(1), PS-4, PS-8
