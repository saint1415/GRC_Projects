# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Electric Cooperative, Inc. |
| Policy ID | POL-02 |
| Owner | Office and Finance Manager (Security Coordinator); Line Superintendent for SCADA and field devices |
| Approved by | General Manager, 2026-08-31; adopted by the Board of Trustees, 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Yearly (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, SI-12, CA-2. Part B: AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, IA-2, IA-2(1), IA-5, MA-4, PE-3, PS-4. Part C: PL-4, AT-2 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01 |
| Drivers | 7 CFR 1730.20, 1730.21(b), 1730.22(a), 1730.24, 1730.27; Fla. Stat. 501.171(2) and (6); NIST CSF 2.0 and SP 800-82 Rev. 3 (voluntary benchmark) |

**Why this policy has three parts.** A 7-person cooperative does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the cooperative's security program, make sure only authorized people can operate the grid or see member information, and only as far as their job requires, and tell staff how to use cooperative systems.

## 2. Scope
All employees, trustees using cooperative systems, contractors, and vendor staff. It covers every system and every copy of cooperative information: SCADA, the substation and field devices, the AMI head-end, the business suite, email and the shared drive, the backup vault, and all computers, tablets, and phones, including systems run for the cooperative by vendors and the MSP.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board of Trustees | Adopts this policy; approves High-risk treatment plans and the security budget; receives the yearly security report |
| General Manager | Accepts Moderate risk; approves sanctions with the Security Coordinator; approves payee bank changes (C.7) |
| Office and Finance Manager (Security Coordinator) | Runs this policy; grants and removes business suite, email, and AMI access; reviews accounts and logs; keeps vendor files |
| Line Superintendent (OT lead) | Grants and removes SCADA access; device passwords; vendor remote access; substation keys |
| Meter and Service Technician | Assigns AMI disconnect and load-control rights under B.2 |
| MSP | Creates and disables email and device accounts on the Security Coordinator's request; operates office device controls |
| All staff | Protect credentials and keys; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security Coordinator and OT lead.** The Office and Finance Manager is the Security Coordinator and the Line Superintendent is the OT lead. The General Manager must record both designations in writing (done 2026-08-31) and update them within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment and VRA.** The Security Coordinator and the OT lead must update the risk register every July, and after any major change such as a new SCADA or AMI system, a new vendor with remote access, or new field devices, using NIST SP 800-30 Rev. 1. Each update must be adopted into the Vulnerability and Risk Assessment record (7 CFR 1730.27). Every risk must have an owner and a treatment. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Security Coordinator may accept Low and Very Low risks. Only the General Manager may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Board of Trustees. A risk to public or crew safety rated High is never accepted. (PM-9; GV.RM-01)

A.4 **Sanctions.** A person who breaks a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Security Coordinator records each sanction, and the General Manager approves suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Vendor terms before access.** No vendor may receive remote access to SCADA, field devices, or the AMI head-end, or hold member personal information, until its contract includes: notice to the cooperative within 24 hours of an incident affecting SCADA or AMI commands and within 72 hours of any other incident affecting cooperative data; named accounts with MFA for its staff; access to OT only on request (B.6); return or deletion of data at exit; and no use of member data outside the service. Existing contracts must be amended at renewal, and no later than 2026-12-31. (SA-9; GV.SC-05; 7 CFR 1730.20; Fla. Stat. 501.171(6))

A.6 **Assessment.** Security controls must be assessed every year by someone who does not operate them, before the borrower analysis that RUS requires (7 CFR 1730.22(a)), and after major changes. (CA-2; ID.IM-01)

A.7 **Retention.** Security records (risk assessments, VRA updates, assessments, incident records, access reviews, training records, exercise records, and vendor reviews) must be kept for at least 5 years and in any case until the next RUS review has been completed and the related inspection or test has been repeated (7 CFR 1730.21(b)). (SI-12; GV.PO-02)

A.8 **Policy review and access to policies.** The Security Coordinator must review this policy set every August and after an incident or major change, and must keep the current version in the shared drive and in the ERP binder, where every employee can read it. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

A.10 **Board oversight.** The General Manager must report to the Board of Trustees each year on security risks, POA&M progress, incidents, and the state of the VRA and ERP, and after any incident reported to DOE. (PM-9; GV.OV-01; 7 CFR 1730.24)

### Part B. Access control
B.1 **Named accounts.** Every person must have their own account in SCADA, the AMI head-end, the business suite, email, and the backup vault. Shared or generic accounts are not allowed. The only exception is a view-only SCADA account for a wall alarm display, which cannot send commands. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** Access must match the person's job. SCADA control rights are limited to the 4 field staff; settings-change and administrator rights to the Line Superintendent and one backup. AMI remote disconnect and load-control rights are limited to the Meter and Service Technician and the Member Services Representative (disconnect only). A disconnect or load-control command reaching more than 5 meters needs a second person's approval, and every disconnect must be checked against the medical-needs flag first. (AC-2; AC-3; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for SCADA, the AMI head-end, the business suite, email, the backup vault, and every administrator login, including logins held by the MSP and by vendors. (IA-2(1); PR.AA-03)

B.4 **Termination.** On or before a person's last day, the Security Coordinator and the Line Superintendent must complete the termination checklist: disable SCADA, AMI, suite, email, and vault accounts; ask the MSP to remove device access; remove MFA registrations; collect keys, tablets, and phones; and change any shared secret the person knew (for example, a device password). For an involuntary termination, access must be disabled before the person is told. (PS-4; AC-2)

B.5 **Account reviews.** Each month the Security Coordinator must compare the SCADA, AMI, suite, and vault user lists with the staff roster and the vendor access list, and remove anything that does not match. Each quarter the Line Superintendent and the Meter and Service Technician must confirm that SCADA and AMI rights still fit each job. (AC-2; AC-6; PR.AA-05)

B.6 **Vendor and MSP remote access.** SCADA vendor support access to the SCADA tenant and the substation gateway must be enabled only when the Line Superintendent requests or approves it, for a set window, and must be recorded in the change log and disabled afterwards. MSP technicians must use named accounts with MFA, and the MSP must give the Security Coordinator a current technician list every year. (AC-17; MA-4; SA-9)

B.7 **Device passwords.** No field device, modem, gateway, or collector may keep a vendor default or installer-set password. Each device must have a unique password, stored in the cooperative's password manager and known only to the Line Superintendent and one backup. Device passwords must be changed when someone who knew them leaves. (IA-5; PR.AA-01)

B.8 **Locking and sessions.** Computers and tablets must lock after 15 minutes idle. No computer may sign in automatically to Windows or to SCADA. SCADA operator sessions must end after 30 minutes idle; the view-only alarm display may stay signed in. (AC-11; AC-12; PR.AA-03)

B.9 **Keys.** Substation 1, recloser cabinet, and control cabinet keys must be restricted keys, issued from a key log, and recovered under B.4. A lost key must be reported at once and the lock changed. (PE-3; PR.AA-06; 7 CFR 1730.21(c))

B.10 **Emergency access.** A sealed copy of a SCADA administrator credential must be kept by the General Manager for use when the Line Superintendent is unavailable. Any use must be reported to the Line Superintendent and the password changed afterwards. (AC-2; PR.AA-05)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Cooperative systems are for cooperative work. Staff must look up a member's account only for a work reason. (PL-4; PR.AT-01)

C.2 Staff must not store or send member personal information, SCADA screens, device settings, or network details with personal email, personal cloud storage, personal messaging apps, or public AI chatbots. POL-04 section 4.6 lists the approved tools. (PL-4)

C.3 Staff must lock their screen when stepping away and never share passwords or MFA codes with anyone, including callers who say they are from a vendor, the MSP, or the G&T. (AC-11; PL-4)

C.4 Staff must complete security training at hire and every year, with an OT module for field staff (SCADA, device passwords, what an attack on a recloser looks like), and must take part in phishing simulations. (AT-2; PR.AT-01)

C.5 Staff must report suspected incidents at once under POL-03 section 4.2, including their own mistakes. (IR-6)

C.6 Staff must sign an acknowledgment of this policy at hire and after each yearly update. (PL-4)

C.7 **Payment changes.** Any request to change a payee's bank details, or any unusual payment request, must be verified by calling the requester at a phone number already in the cooperative's records, never one given in the request. The General Manager must approve the change in writing before any payment goes to the new account. This applies to the G&T power bill above all. (AT-2; SI-8; IA-2(1))

C.8 Truck tablets and company phones must stay with the user or locked in the truck. A lost or stolen device must be reported at once so it can be wiped and its SCADA session ended. (PL-4; MP-5)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Security Coordinator checks compliance through the monthly account review (B.5), the vendor access log (B.6), and the yearly independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; key log; vendor access log; P01 risk register; P02 SSP control statements AC-2, AC-6, AC-17, IA-2(1), IA-5, PS-4; the ERP; the VRA
