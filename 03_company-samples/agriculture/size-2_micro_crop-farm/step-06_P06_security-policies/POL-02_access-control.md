# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (Security Coordinator) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, SI-12, CA-2. Part B: AC-2, AC-3, AC-6, AC-11, AC-17, AC-18, IA-2, IA-2(1), IA-5, MA-4, CM-3, PS-4. Part C: PL-4, AT-2, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, GV.SC-06, ID.RA-01, ID.RA-07, ID.IM-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01 |
| Binding rules served | 21 CFR 112.161(a)(4) (records signed by the person who did the work); 20 CFR 655.122(j) (earnings records kept safe and accurate); Fla. Stat. 501.171(2) (reasonable security measures) |

**Why this policy has three parts.** A 7-person farm does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C. A one-page Spanish summary of Part C is given to every field worker.

## 1. Purpose
Set up the farm's security program, make sure only authorized people reach farm systems, irrigation controls, and worker records, and only as far as their job requires, and tell everyone how to use farm systems.

## 2. Scope
All workforce members of Cris Santos Company, including the Owner and General Manager, year-round and seasonal employees (including H-2A workers), and temporary help. It covers every system and every copy of farm information, including systems run for the farm by the MSP, the irrigation dealer, the equipment dealer, and SaaS vendors, and the irrigation equipment itself (pump station controller, gateway, and pivot panels).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner and General Manager | Approves policies and the security budget; accepts Moderate and higher risks; decides sanctions |
| Office Manager (Security Coordinator) | Runs this policy; grants and removes access; keeps the inventory, risk register, and supplier file; reviews accounts and logs |
| Irrigation and Equipment Technician | Approves every dealer session and every change to the pump station and pivots; administers SYS-01 irrigation settings |
| Field Supervisor | Makes sure crew members use their own SYS-01 accounts and sign paper forms during outages |
| MSP | Creates and disables productivity suite accounts on request; operates office computer, firewall, and backup controls |
| All workforce | Protect passwords and PINs; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security Coordinator.** The Office Manager is the designated Security Coordinator, with about 3 hours a week for the role. The Owner and General Manager must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The Security Coordinator must update the risk assessment every July, after the watermelon harvest, and after any major change such as new irrigation automation, a new SaaS system holding worker records, or connecting the yield model to farm decisions, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Security Coordinator may accept Low and Very Low risks. Only the Owner and General Manager may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner and General Manager. A risk that could injure a worker is never accepted at High. (PM-9; GV.RM-01)

A.4 **Sanctions.** A workforce member who breaks a security rule must be dealt with in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination, consistent with employment law and the H-2A work contract. The Security Coordinator records each sanction; the Owner and General Manager decides suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Suppliers.** Before any supplier gets access to farm systems, irrigation equipment, or Restricted information, the Security Coordinator must complete the one-page supplier checklist, and the agreement must include security terms: named accounts with MFA, access only when needed, notice of security incidents affecting the farm within 72 hours (24 hours for the MSP), return or deletion of farm data at the end, and, for the irrigation dealer, a copy of the current controller program held by the farm. This applies to trials, pilots, and free tools. The Security Coordinator reviews the FMIS vendor's SOC 2 report and the MSP each year. (SA-9; GV.SC-05; GV.SC-06; Fla. Stat. 501.171(6))

A.6 **Assessment.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2; ID.IM-01)

A.7 **Retention of security records.** Policies, risk assessments, assessments, incident records, training records, and sanction records must be kept for at least 3 years. A written Florida no-harm determination must be kept for at least 5 years (Fla. Stat. 501.171(4)(c)). (SI-12; GV.PO-02)

A.8 **Policy review and access to policies.** The Security Coordinator must review this policy set every August and after an incident or major change, and must keep the current version, with the Spanish summary of Part C, in the Office folder and in the printed binder in the shop. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated on the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

### Part B. Access control
B.1 **Named accounts only.** Every person who uses SYS-01, the productivity suite, the telematics portal, or any other farm system must have their own account. Shared or generic logins are not allowed. The shared field crew login must be retired by 2026-11-30; crew members then enter hours and Produce Safety records under their own SYS-01 accounts with a PIN on the managed field tablet, so that each record shows who did the work. (IA-2; AC-2; PR.AA-01; 21 CFR 112.161(a)(4); 20 CFR 655.122(j)(1))

B.2 **Least privilege.** Access must match the person's job, using the SYS-01 role list (manager, operator, crew). The Security Coordinator approves access in writing (the onboarding checklist) before it is granted. Only the Owner and General Manager and the Irrigation and Equipment Technician may hold SYS-01 roles that can start, stop, or schedule irrigation. The Office folder holding payroll and H-2A files is limited to the Office Manager and the Owner and General Manager. Nobody keeps local administrator rights on an office computer. (AC-2; AC-3; AC-6; PR.AA-05; Fla. Stat. 501.171(2))

B.3 **MFA.** MFA is required for every SYS-01 user (crew accounts use the managed tablet plus a PIN), every productivity suite mailbox, the backup console, the telematics portal, the AI vendor account, and every remote access path into the pump station, including the dealer's. (IA-2(1); PR.AA-03)

B.4 **Departures and season end.** On or before a workforce member's last day, the Security Coordinator must complete the departure checklist: disable SYS-01, suite, and portal accounts; remove MFA registrations; block mail forwarding; ask the MSP to remove device access; collect keys, phones, and tablets; and change any PIN or shared password the person knew. For an involuntary departure, access is disabled before the person is told. At the end of each H-2A season (by July 31), the Security Coordinator disables seasonal accounts and changes the field tablet PIN. (PS-4; AC-2; PR.AA-05)

B.5 **Monthly reconciliation.** Each month the Security Coordinator compares the user lists of SYS-01, the suite, the telematics portal, the backup console, and the AI vendor account with the staff list, removes anything that does not match, and checks for mail forwarding rules to outside addresses. (AC-2; AC-6; PR.AA-05)

B.6 **Locking.** Office computers lock after 15 minutes idle. Tablets and phones lock after 5 minutes and require a PIN. (AC-11)

B.7 **Emergency access.** A sealed copy of a SYS-01 administrator credential is kept by the Owner and General Manager for use when the Technician is unavailable. Any use must be reported to the Security Coordinator and the password changed afterwards. (AC-2)

B.8 **Remote and supplier access.** The irrigation dealer may reach the pump station only on request: the Technician approves each session, the gateway is enabled only for that session, the dealer uses a named account with MFA, and the Technician records the date, the technician's name, and the work done. Equipment dealer access to the telematics account is granted per service visit and removed afterwards. MSP technicians use named accounts with MFA, and the MSP gives the Security Coordinator a current list of technicians with access each year. (AC-17; MA-4; IA-2(1); SA-9; PR.AA-05)

B.9 **Passwords, PINs, and defaults.** Passwords must be at least 12 characters and never reused from personal accounts. Default passwords and PINs on any device, including the gateway, the pump station touchscreen, pivot modems, and the Wi-Fi, must be changed before use. The staff Wi-Fi password is changed every year and whenever a contractor or employee who knew it leaves; visitors and dealer technicians use a separate guest Wi-Fi. (IA-5; AC-18; PR.AA-01)

B.10 **Irrigation changes.** Any change to the pump station program, fertigation limits, pivot settings, or irrigation schedules made outside normal day-to-day operation must be approved by the Technician and recorded in the change log with the reason, and the prior program version kept. (CM-3; ID.RA-07)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Farm systems are for farm work. Workforce members may look only at the records their job needs. (PL-4; PR.AT-01)

C.2 Workforce members must not store or send Restricted information (POL-04) with personal email, personal cloud storage, personal messaging apps, or public AI chatbots. (PL-4; Fla. Stat. 501.171(2))

C.3 Workforce members must lock their screen when stepping away and must never share passwords, PINs, or MFA codes, including with the MSP or a dealer. (AC-11; PL-4)

C.4 Workforce members must complete security training at hire and every year, in English or Spanish, and must not open links or attachments that ask for a password or a payment change without checking with the Office Manager by phone. (AT-2; PR.AT-01)

C.5 Workforce members must report suspected incidents at once under POL-03 section 4.2, including their own mistakes, a lost phone or tablet, or a pump or pivot doing something nobody scheduled. (IR-6)

C.6 Workforce members must sign an acknowledgment of this Part C, in English or Spanish, at hire, at the start of each season, and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to action under A.4. The Security Coordinator checks compliance through the monthly reconciliation (B.5), the monthly log review, the change log (B.10), and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding, departure, and season-end checklists; supplier checklist; change log; P01 risk register; P02 SSP control statements AC-2, AC-17, IA-2(1), MA-4, PS-4
