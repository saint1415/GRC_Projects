# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Operations Manager (Security and Privacy Lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, CA-2, CM-3. Part B: AC-2, AC-3, AC-6, AC-11, AC-17, IA-2, IA-2(1), IA-5, PS-4. Part C: PL-4, AT-2, AT-3, AC-19 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-02, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, ID.RA-07, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AT-01, PR.AT-02 |
| Legal and contractual drivers | Fla. Stat. 501.171(2); 8 CFR 274a.2(b)(4) and (g)(1); E-Verify MOU Art. II.A.3, II.A.5, II.A.15; 15 U.S.C. 1681b(b)(3) |

**Why this policy has three parts.** A 7-person firm does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01) and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the firm's security program, make sure only authorized people reach worker, candidate, and client information and only as far as their job requires, and tell staff how to use firm systems.

## 2. Scope
All staff of Cris Santos Company, including the Owner, and any contractor with access to firm systems (the MSP and the outside CPA firm). It covers every system and every copy of firm information: the ATS, the payroll service, the productivity suite, E-Verify, the screening portal, the accounting SaaS, laptops, the applicant tablet, the scanner, personal phones used for work, and paper records. Temporary associates working at client sites do not use firm systems except their own payroll self-service account.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves policies and the security budget; accepts Moderate and higher risk; decides sanctions with the Operations Manager; reviews the payroll bank-change report monthly |
| Operations Manager | Security and Privacy Lead; runs this policy; grants and removes access in the payroll service and E-Verify; reviews accounts and logs |
| Senior Recruiter | ATS administrator: creates and removes ATS users on the Operations Manager's approval; manages ATS and AI settings under A.10 |
| MSP | Creates and disables suite and laptop accounts on the Operations Manager's request; operates laptop controls |
| All staff | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security and Privacy Lead.** The Operations Manager is the designated Security and Privacy Lead. The Owner must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The Operations Manager must update the risk assessment every July, and after any major change such as a new payroll service, a new vendor holding worker data, turning on any AI feature, or accepting job orders outside Florida, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Operations Manager may accept Low and Very Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. (PM-9; GV.RM-02)

A.4 **Sanctions.** A staff member who breaks a security or privacy rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Operations Manager must record each sanction, and the Owner must approve suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Vendors.** No vendor, app, or AI feature may receive worker or candidate personal information until the Operations Manager has checked it with the vendor checklist and recorded it in the vendor file with a breach contact. At each renewal the Owner must seek security terms, breach notice within 72 hours, and return or deletion of data at exit. Critical vendors (payroll service, ATS, MSP) must provide a SOC 2 report or a completed questionnaire each year. (SA-9; GV.SC-05)

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2)

A.7 **Retention of security records.** Policies, risk assessments, assessments, incident records, vendor reviews, training records, and sanction records must be kept for at least 5 years. (SI-12; GV.PO-02)

A.8 **Policy review and access to policies.** The Operations Manager must review this policy set every August and after an incident or major change, and keep the current version in the shared drive where every staff member can read it. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated with the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

A.10 **Changes that need approval.** The Owner must approve, in the change log, any change to: payroll bank-change rules or alerts, payroll administrator rights, ATS user roles, and any AI feature setting (turning a feature on, changing a filter or threshold). (CM-3; ID.RA-07)

### Part B. Access control
B.1 **Unique accounts.** Every staff member must have their own account in the ATS, the payroll service, the suite, and E-Verify. Shared or generic accounts are not allowed. (IA-2; AC-2; PR.AA-01; E-Verify MOU Art. II.A.15)

B.2 **Least privilege.** Access must match the job:

| Data or function | Who may access |
|---|---|
| Payroll administration, bank changes, census and tax reports | Operations Manager and Coordinator; Owner as backup approver |
| Onboarding packets (SSNs, bank forms), Form I-9 files, E-Verify | Operations Manager and Coordinator |
| Background check results | Operations Manager and Coordinator; recruiters see only "cleared" or "in review" |
| Applicant records, job orders, client contacts | All recruiters, the Account Manager, the Operations Manager, and the Owner |
| ATS administration | Senior Recruiter; Operations Manager as backup |

The Operations Manager must approve access in writing (the onboarding checklist) before it is granted. (AC-2; AC-3; AC-6; PR.AA-05; 8 CFR 274a.2(b)(4); 15 U.S.C. 1681b(b)(3))

B.3 **MFA.** MFA is required on every firm system that offers it. Payroll administrators must use an authenticator app, not SMS codes. MFA is required on every administrator login held by the MSP (backup console, firewall, remote management). Push approvals must use number matching. (IA-2(1); PR.AA-03)

B.4 **Bank-account changes.** Staff must never change an associate's or staff member's bank account on the strength of an email, text, or voicemail. A staff-entered change requires a call-back to the phone number already on file, recorded in the payroll notes. The first payroll after any bank change, including one made in self-service, is checked by the Operations Manager before payroll is submitted. (IA-2; PR.AA-02)

B.5 **Termination.** On or before a staff member's last day, the Operations Manager must complete the termination checklist: disable ATS, payroll, suite, E-Verify, screening portal, and accounting accounts; ask the MSP to remove laptop access; remove MFA registrations; sign the person's phone out of firm apps; collect keys and the laptop; and remind the person in writing of their confidentiality duty. For an involuntary termination, access must be disabled before the person is told. (PS-4; AC-2; E-Verify MOU Art. II.A.3)

B.6 **Monthly reconciliation.** Each month the Operations Manager must compare the user lists of the ATS, payroll service, suite, E-Verify, screening portal, backup console, and accounting SaaS with the staff roster, and remove anything that does not match. Every quarter the Operations Manager must confirm each person's access still fits B.2. (AC-2; AC-6; PR.AA-05)

B.7 **Locking.** Laptops must lock after 10 minutes idle. No laptop is exempt. Applicants fill in forms only on the lobby tablet or the ATS career site. (AC-11)

B.8 **Vendor and MSP access.** MSP technicians and vendor support staff must use named accounts with MFA. The MSP must give the Operations Manager a current list of technicians with access every year. (AC-17; IA-2(1); SA-9)

B.9 **Passwords.** Passwords must be at least 12 characters, kept in the firm's password manager, and never reused from personal accounts or written down. The staff Wi-Fi password must be changed every year and whenever someone leaves. (IA-5; E-Verify MOU Art. II.A.15)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Firm systems are for firm work. Staff must open only the worker, candidate, and client records their job needs. (PL-4; PR.AT-01)

C.2 **Personal phones.** A personal phone may be used for firm email, the ATS app, and texting candidates only if it has a passcode, built-in encryption, automatic updates, and lost-device location turned on. Staff must not keep photos of identity documents, SSNs, or bank details on a phone: candidates are sent the ATS upload link instead, and any such photo received must be deleted after it is uploaded. A lost phone must be reported within 1 hour. (AC-19; PL-4; Fla. Stat. 501.171(2))

C.3 Staff must not store or send worker or candidate personal information with personal email, personal cloud storage, or public AI chatbots. POL-04 4.6 lists approved AI tools. (PL-4)

C.4 Staff must lock their screen when stepping away and never share passwords or MFA codes, including with the MSP or a caller claiming to be from a vendor. (AC-11; PL-4)

C.5 Staff must complete security and privacy training at hire and every year, and take part in phishing simulations. The Operations Manager, the Coordinator, and the Owner also complete payroll fraud training; E-Verify users complete the E-Verify tutorial before creating cases. (AT-2; AT-3; PR.AT-01; PR.AT-02; E-Verify MOU Art. II.A.5)

C.6 Staff must report suspected incidents at once under POL-03 4.2, including their own mistakes. (IR-6)

C.7 Staff must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Operations Manager checks compliance through the monthly reconciliation (B.6), the monthly log review, and the annual independent assessment (P07). The Owner checks B.4 through the monthly bank-change report.

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; change log; vendor file; P01 risk register; P02 SSP control statements AC-2, AC-3, IA-2(1), PS-4, PS-8
