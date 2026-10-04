# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (Security Coordinator), with the Field Superintendent for OT |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, SI-12, CA-2. Part B: AC-1, AC-2, AC-3, AC-4, AC-6, AC-11, AC-17, IA-2, IA-2(1), IA-5, MA-4, PE-3, PS-4, SC-7. Part C: PL-4, AT-2, MP-7 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-01, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.IR-01, PR.AT-01 |
| Benchmark (N21-BM) | SP 800-82 Rev. 3 sections 3.3.1 (governance), 5.2.3 (network security), 6.2.1 (identity and access), 6.2.10 (remote access) |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people and devices reach company systems and the SCADA system, and only as far as their job requires, and tell staff how to use company systems.

## 2. Scope
All Cris Santos Company workforce members (the Owner, employees, temporary workers) and every contractor or vendor with access, including the MSP, the SCADA integrator, and the SCADA vendor. Covers both offices, the tank battery, the SWD facility, every well site, all business IT and OT systems, and systems that vendors run for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves policies and the security budget; accepts Moderate risk; decides sanctions with the Office Manager |
| Office Manager (Security Coordinator) | Runs this policy; requests and removes access in SaaS; directs the MSP; reviews accounts and logs |
| Field Superintendent (OT lead) | Approves SCADA access and every vendor session; owns the field office network and the IT/OT boundary |
| Field Technician | Creates and removes SCADA host and mobile viewer accounts on the Field Superintendent's approval |
| Production Accountant | Creates and removes production accounting accounts on the Office Manager's request |
| MSP | Creates and disables suite and device accounts on request; operates device controls |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security roles.** The Office Manager is the Security Coordinator and the Field Superintendent is the OT lead. The Owner must record both designations in writing and update them within 30 days of any change. (PM-2; GV.RR-02; SP 800-82r3 3.3.1)

A.2 **Risk analysis.** The Security Coordinator must update the risk analysis every July, and after any major change such as a new SCADA host, a new vendor with access to SCADA or owner data, or a change to the predictive maintenance add-on, using NIST SP 800-30 Rev. 1 with the OT threat sources in SP 800-82 Rev. 3 Appendix C. Every risk must have an owner and a treatment. (RA-3; ID.RA-01; GV.RM-01)

A.3 **Risk acceptance.** The Office Manager may accept Low and Very Low risks (the Field Superintendent for field-only items). Only the Owner may accept a Moderate risk, with the Field Superintendent's agreement if it affects field operations. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. No risk with a plausible injury, H2S exposure, or release may be accepted at High. (PM-9; GV.RM-01)

A.4 **Sanctions.** A workforce member who breaks a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Office Manager records each sanction; the Owner approves suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **No terms, no access.** No vendor may receive Restricted data (POL-04) or remote access to any company system until the Security Coordinator has completed the one-page vendor checklist and the contract includes security terms: named accounts with MFA, incident notice, notice before feature or setting changes that affect field equipment, limits on data use, and data return or deletion at the end. Existing vendors get these terms at renewal. (SA-9; GV.SC-01; GV.SC-05)

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2; ID.IM-01)

A.7 **Retention.** Policies, risk analyses, assessments, incident records, vendor reviews, training records, and sanction records must be kept for at least 5 years. (SI-12; GV.PO-02)

A.8 **Policy review and access to policies.** The Security Coordinator must review this policy set every August and after an incident or major change, and keep the current version in the shared drive where every workforce member can read it. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

### Part B. Access control
B.1 **Unique accounts.** Every person must have their own account in the suite, production accounting, the bank portal, the SCADA mobile viewer, and any vendor remote session. Shared accounts are not allowed, with one exception: the HMI operator login on the SCADA host may be shared by Lease Operators only while the field office stays locked when unattended, a sign-in sheet is kept at the HMI, and the operator log is reviewed monthly, consistent with the SP 800-82 Rev. 3 OT overlay discussion of IA-2. The Field Technician and the integrator must use named SCADA accounts. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** Access must match the person's job and be approved before it is granted: by the Office Manager for SaaS, by the Field Superintendent for SCADA. Only the Field Technician and named integrator staff may change controller programs. Staff use standard accounts on computers, including the engineering laptop. (AC-2; AC-3; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for the suite, production accounting, the bank portal, the SCADA mobile viewer, the cloud backup console, every administrator login, and every remote access path into the field office network. (IA-2(1); PR.AA-03)

B.4 **Vendor and remote access to SCADA.** Vendors may reach the SCADA host only through the company's remote session tool, with a named account and MFA. The Field Superintendent (or the Field Technician, if the Field Superintendent is unreachable) enables each session, the session is logged, and it ends when the work ends. Always-on remote access tools and port forwards to the SCADA host are prohibited. (AC-17; MA-4; PR.AA-05)

B.5 **Termination.** On or before a person's last day, the Office Manager must complete the last-day checklist: disable suite, production accounting, bank, mobile viewer, and SCADA accounts; ask the MSP to remove device access and wipe company phones; collect keys and devices; and have the Field Superintendent change the HMI operator password, the field Wi-Fi password, and the gate code. For an involuntary termination, access is removed before the person is told. Vendor access ends on the contract end date. (PS-4; AC-2)

B.6 **Quarterly review.** Each quarter the Office Manager compares every system's user list with the staff and vendor list, and the Field Superintendent reviews SCADA and mobile viewer accounts. Anything that does not match is removed. (AC-2; AC-6; PR.AA-05)

B.7 **Locking.** Computers and phones lock after 10 minutes idle. The SCADA host HMI is exempt so alarms stay visible, on condition that the field office is locked whenever nobody is there. (AC-11)

B.8 **Emergency access.** The SCADA host administrator password and one production accounting administrator credential must be kept sealed in the main-office safe for use when the normal holder is unavailable. Any use is reported to the Office Manager and the password changed afterwards. (AC-2)

B.9 **Passwords and defaults.** Passwords must be at least 12 characters and never reused from personal accounts. Default passwords on any device (router, radio, modem, controller, firewall) must be changed before the device is connected. Shared passwords (HMI operator, field Wi-Fi) are changed at least yearly and whenever someone who knows them leaves. (IA-5; PR.AA-01)

B.10 **IT/OT boundary and cloud.** The SCADA host and radio base must sit behind a firewall that separates them from the field office PCs and Wi-Fi, with rules approved by the Field Superintendent. No device may connect to both sides. Nothing on the SCADA host may be reachable from the internet. **No cloud service may send commands or setpoints to field controllers;** the SCADA vendor connector stays send-only unless a new AI and risk review approves a change. (SC-7; AC-4; PR.IR-01)

B.11 **Physical access.** The field office is locked when unattended; the tank battery and SWD facility stay fenced and locked; controller cabinets stay padlocked. The gate code is changed every quarter and after any departure, and keys are logged. (PE-3; PR.AA-06)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Staff may look only at the owner, employee, and seismic data their job needs. (PL-4; PR.AT-01)

C.2 Staff must not store or send Restricted data (POL-04) with personal email, personal cloud storage, personal messaging apps, or public AI chatbots. POL-04 4.6 lists the approved AI tools. (PL-4)

C.3 Staff must not plug personal phones, USB drives, or visiting laptops into the SCADA host or the SCADA side of the network. Only the company USB drive, scanned first on an MSP-managed computer, may be used on the SCADA host. (MP-7; PL-4)

C.4 Staff must lock their screen when stepping away and never share passwords or MFA codes, including with the MSP, the integrator, or anyone calling about the bank. (AC-11; PL-4)

C.5 Staff must complete security training at hire and every year (with a field module for field staff), and take part in phishing exercises. (AT-2; PR.AT-01)

C.6 Staff must report suspected incidents at once under POL-03 4.2, including their own mistakes and any HMI behavior they cannot explain. (IR-6)

C.7 Staff must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Security Coordinator checks compliance through the quarterly review (B.6), the monthly log review, and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; last-day checklist; vendor checklist; P01 risk register; P02 SSP control statements AC-2, AC-17, IA-2, PS-4, SC-7
