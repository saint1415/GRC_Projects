# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (Privacy Officer and Security Officer) |
| Approved by | Owner physician, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, SI-12, CA-2. Part B: AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, IA-2, IA-2(1), IA-5, PS-4. Part C: PL-4, AT-2 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01 |
| HIPAA Security Rule | 164.308(a)(1), (a)(1)(ii)(A)-(C), (a)(2), (a)(3), (a)(4), (a)(5), (a)(8), (b)(1); 164.310(b), (c); 164.312(a), (d); 164.316 |

**Why this policy has three parts.** A 7-person office does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the practice's security program, make sure only authorized people reach patient and practice information and only as far as their job requires, and tell the workforce how to use practice systems.

## 2. Scope
All workforce members of Cris Santos Company: both physicians, employees, temporary staff, students, and volunteers. It covers every system and every copy of practice information, including systems run for the practice by the MSP and SaaS vendors. It applies to ePHI and all other practice information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner physician | Approves policies and the security budget; accepts Moderate risk; decides sanctions with the Office Manager |
| Office Manager | Privacy Officer and Security Officer; runs this policy; grants and removes access; reviews logs and accounts |
| MSP | Creates and disables suite and device accounts on the Office Manager's request; operates device controls |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security and Privacy Officer.** The Office Manager is the designated HIPAA Security Officer and Privacy Officer. The owner physician must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02; 164.308(a)(2))

A.2 **Risk analysis.** The Office Manager must update the risk analysis every July, and after any major change such as a new EHR, a new vendor handling ePHI, or expanding the AI scribe, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01; 164.308(a)(1)(ii)(A)-(B))

A.3 **Risk acceptance.** The Office Manager may accept Low and Very Low risks. Only the owner physician may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the owner physician. (PM-9; GV.RM-01)

A.4 **Sanctions.** A workforce member who breaks a security or privacy rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Office Manager must record each sanction, and the owner physician must approve suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))

A.5 **No BAA, no ePHI.** No vendor may create, receive, maintain, or transmit ePHI for the practice until a business associate agreement is signed or accepted. That includes trials, pilots, and free tools. The Office Manager keeps every BAA in the BAA folder and checks each year that the MSP holds BAAs with its own subcontractors. (SA-9; GV.SC-05; 164.308(b)(1); 164.314(a))

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2; 164.308(a)(8))

A.7 **Retention.** Security policies, procedures, risk analyses, assessments, incident records, BAAs, training records, and sanction records must be kept for 6 years from the date created or the date last in effect, whichever is later. (SI-12; GV.PO-02; 164.316(b)(2)(i))

A.8 **Policy review and access to policies.** The Office Manager must review this policy set every August and after an incident or major change, and must keep the current version in the shared drive where every workforce member can read it. (PL-1; GV.PO-02; 164.316(b)(2)(ii)-(iii))

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

### Part B. Access control
B.1 **Unique accounts.** Every workforce member must have their own account in the EHR, the productivity suite, and the fax portal. Shared or generic accounts are not allowed. (IA-2; AC-2; PR.AA-01; 164.312(a)(2)(i))

B.2 **Least privilege.** Access must match the person's job, using the EHR role list. The Office Manager must approve access in writing (the onboarding checklist) before it is granted. EHR administrator roles are limited to the Office Manager and one physician as backup. (AC-2; AC-3; AC-6; PR.AA-05; 164.308(a)(4)(ii)(B)-(C))

B.3 **MFA.** MFA is required for the EHR, the productivity suite, the fax portal where offered, and every administrator login, including logins held by the MSP (backup console, firewall, remote management). (IA-2(1); PR.AA-03; 164.312(d))

B.4 **Termination.** On or before a workforce member's last day, the Office Manager must complete the termination checklist: disable EHR, suite, and fax accounts; ask the MSP to remove device access; remove MFA registrations; collect keys and devices; and remind the person in writing of their confidentiality duty. For an involuntary termination, access must be disabled before the person is told. (PS-4; AC-2; 164.308(a)(3)(ii)(C))

B.5 **Monthly reconciliation.** Each month the Office Manager must compare the user lists of the EHR, suite, fax portal, and backup console with the staff roster, and remove anything that does not match. Every quarter the Office Manager must confirm each person's EHR role still fits their job. (AC-2; AC-6; PR.AA-05; 164.308(a)(4)(ii)(C))

B.6 **Locking.** Computers and tablets must lock after 10 minutes idle, and the EHR must end sessions after 15 minutes idle. No computer is exempt; where a screen must stay visible, it is placed out of patients' view. (AC-11; AC-12; 164.310(c); 164.312(a)(2)(iii))

B.7 **Emergency access.** A sealed copy of an EHR administrator credential must be kept by the owner physician for use when the Office Manager is unavailable. Any use must be reported to the Office Manager and the password changed afterwards. (AC-2; 164.312(a)(2)(ii))

B.8 **Vendor and MSP access.** MSP technicians and vendor support staff must use named accounts with MFA. The MSP must give the Office Manager a current list of technicians with access every year. (AC-17; IA-2(1); SA-9)

B.9 **Passwords and shared secrets.** Passwords must be at least 12 characters and never reused from personal accounts. The staff Wi-Fi password must be changed every year and whenever a workforce member leaves. (IA-5; 164.308(a)(5)(ii)(D))

### Part C. Workforce use rules (essentials of POL-05)
C.1 Practice systems are for practice work. Workforce members must access only the patient information they need for their job, and never their own, family members', or neighbors' records unless they are treating them. (PL-4; PR.AT-01; 164.310(b))

C.2 Workforce members must not store or send ePHI with personal email, personal cloud storage, personal messaging apps, or public AI chatbots. POL-04 section 4.6 lists the approved tools. (PL-4; 164.310(b))

C.3 Workforce members must lock their screen when stepping away, keep screens out of patients' view, and never share passwords or MFA codes, including with the MSP. (AC-11; PL-4; 164.310(b)-(c))

C.4 Workforce members must complete security and privacy training at hire and every year, and must take part in phishing simulations. (AT-2; PR.AT-01; 164.308(a)(5))

C.5 Workforce members must report suspected incidents at once under POL-03 section 4.2, including their own mistakes. (IR-6)

C.6 Workforce members must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Office Manager checks compliance through the monthly reconciliation (B.5), the monthly log review, and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; P01 risk register; P02 SSP control statements AC-2, IA-2(1), PS-4, PS-8
