# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office and Compliance Administrator (security program coordinator); Plant Superintendent for the OT rules in Part B |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Every July with the risk register (next review 2027-07-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PS-8, SA-9, CA-2, SI-12, PL-1, RA-3, CM-3. Part B: AC-2, AC-3, AC-6, AC-17, MA-4, IA-2, IA-2(1), IA-5, SC-7, CM-7, PS-4, AU-6, PE-3. Part C: PL-4, AT-2, MP-7 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, ID.IM-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.IR-01, PR.PS-05, PR.AT-01, DE.CM-06 |
| FERC and Part 12 | Security Program Rev. 3A 3.2 and 3.3.3 (Group 3); Table 9.3a baseline measures for access control, segregation, coordination, and system lifecycle (voluntary benchmark); Appendix A Form 1 Q4 to Q9, Q22 |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01) and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people can reach the Hydro Plant Control and Dam Monitoring System (HPCDMS) and company information, and only as far as their job requires, and tell staff how to use company systems. The overriding goal is that **nobody can move a spillway gate or a unit without authority**.

## 2. Scope
All workforce members of Cris Santos Company and every outside party with access: the controls integrator, the MSP, the remote monitoring service vendor, the consulting dam safety engineer, and the independent assessor. It covers the HPCDMS (SYS-01 to SYS-06), the monitoring service (SYS-07), office IT and SaaS (SYS-08 to SYS-11), cameras and locks (SYS-12), and the project works.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner and General Manager | Approves policies, spending, and exceptions; accepts Moderate and higher risk; FERC primary security contact |
| Plant Superintendent | System owner of the HPCDMS and OT security lead; approves OT access, remote sessions, and changes; alternate FERC security contact; Chief Dam Safety Coordinator |
| Controls and Electrical Technician | Creates and removes HMI and remote access accounts; keeps OT passwords, copies, and the inventory; runs the weekly session review |
| Office and Compliance Administrator | Security program coordinator; requests suite account changes from the MSP; keeps the termination checklist, key inventory, training records, and vendor folder |
| Controls integrator and MSP | Follow this policy when they connect; use named accounts with MFA |
| All workforce | Protect passwords and keys; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security roles.** The Owner and General Manager is the FERC primary security contact and the Plant Superintendent the alternate. The Office and Compliance Administrator is the security program coordinator, and the Plant Superintendent is the OT security lead. The Owner must record these designations in writing, tell the FERC Regional Office of any change in the contacts, and update the record within 30 days. (PM-2; GV.RR-02; Rev. 3A 3.2)

A.2 **Risk assessment.** The Office and Compliance Administrator and the Plant Superintendent must update the risk assessment every July using NIST SP 800-30 Rev. 1, and after any major change: a new remote access path, the HMI replacement, a new vendor connection, or any proposal to let the monitoring service or an AI tool send commands. The assessment also serves as the Security Assessment that FERC highly recommends for Group 3 dams. (RA-3; ID.RA-01; Rev. 3A 3.3.3)

A.3 **Risk acceptance.** The Plant Superintendent or the Office and Compliance Administrator may accept Low and Very Low risks. Only the Owner may accept Moderate, High, or Very High risk, and High and Very High risks only temporarily with a dated treatment plan. **A risk that could cause an uncontrolled gate movement may not be accepted at High; it must be reduced.** (PM-9; GV.RM-01)

A.4 **Discipline.** A workforce member who breaks a security rule is dealt with in proportion to intent and harm: coaching, a written warning, or dismissal, decided by the Owner. Reporting a mistake or a suspected incident in good faith is never punished. (PS-8; GV.RR-04)

A.5 **Vendors.** Every vendor that connects to the HPCDMS or holds company data (the integrator, the MSP, the monitoring vendor, the remote access tool vendor, the camera vendor) must have written security terms by its next renewal: named accounts with MFA, incident notice to the company within 24 hours, no use of company data for other customers, and return or deletion of data at the end. The Office and Compliance Administrator reviews the monitoring vendor's SOC 2 report every year and keeps a one-page record for each other vendor. (SA-9; GV.SC-05; Table 9.3a coordination)

A.6 **Independent assessment.** Security controls must be assessed every year by someone who does not operate them, and after major changes. Results go to the Owner and are kept available for the FERC engineer. (CA-2; ID.IM-01; Rev. 3A 3.2)

A.7 **Retention.** Policies, risk assessments, assessments, training records, session reviews, and incident records must be kept for at least 5 years from the date they were last in effect. Reports of conditions affecting the safety of the project, including security incidents, are permanent project records under 18 CFR 12.12(a)(1)(iii)(B). (SI-12; GV.PO-02)

A.8 **Annual review.** Every July the Office and Compliance Administrator and the Plant Superintendent must review this policy set, the OT procedures, the criticality of OT assets, and the voluntary Section 9 screen, together with the risk register. They also review after an incident or a major change. Current policies are kept in the suite where every workforce member can read them. (PL-1; GV.PO-02; Table 9.3a general measures)

A.9 **Exceptions.** An exception must be requested in writing, rated on the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. The shared local HMI sign-in (B.1) is a recorded exception until the HMI PC is replaced. (PL-1; GV.PO-01)

A.10 **Change control.** No device, software, remote tool, firewall rule, firmware version, or SaaS feature may be added to or changed in the HPCDMS without a change form approved by the Plant Superintendent. The form asks what connects to what, who can use it, and whether it adds a way to move gates or units. A change that adds any remote path or command path also needs the Owner's approval and a risk assessment update (A.2). (CM-3; PR.PS-01; Table 9.3a system lifecycle)

### Part B. Access control
B.1 **Named accounts.** Every person must have their own account in the remote access tool, the suite, the monitoring portal, the camera app, and the accounting and payroll services. Shared accounts are not allowed, except the local HMI operator sign-in used inside the locked control room, which is a recorded exception (A.9) until the replacement HMI supports named accounts (due 2027-03-31). (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** Access must match the job. Remote access is **view-only by default**. Remote gate or unit commands are allowed only for the on-call operator-mechanic answering an alarm, or with the Plant Superintendent's approval. Engineer-level HMI rights and PLC programming are limited to the Controls and Electrical Technician and named integrator engineers. Nobody uses Windows administrator rights for routine HMI work. (AC-3; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for all remote access to the HPCDMS, the suite, the monitoring portal, accounting and payroll, and every administrator login, including the industrial firewall (held by the integrator) and MSP tools. (IA-2(1); PR.AA-03)

B.4 **Remote access.** Only one approved remote access path may reach the HPCDMS: the remote access tool with named accounts and MFA. No vendor may keep an always-on connection. Integrator sessions must be requested in advance, approved by the Plant Superintendent or the Controls and Electrical Technician, started and watched by a staff member, and ended when the work is done, with the integrator's cellular router powered off afterwards until it is removed. Every remote session start sends an alert to the on-call phone. (AC-17; MA-4; DE.CM-06; Table 9.3a remote and third-party access)

B.5 **Network separation.** No office device may connect to the control network, and the firewall must allow no traffic from the office network into it. The engineering laptop is used only on the control network and never joins office or public Wi-Fi. The HMI PC is used only to operate the plant: no web browsing and no email. (SC-7; CM-7; PR.IR-01; Table 9.3a segregation)

B.6 **Leavers.** On or before a workforce member's last day, the Office and Compliance Administrator must complete the termination checklist: disable the suite, remote access tool, monitoring portal, camera app, and payroll accounts; have the Controls and Electrical Technician change every shared OT password and panel code the person knew; and collect keys, gate codes, and company devices. For an involuntary departure, access is removed before the person is told. A vendor engineer's access is removed the same day the vendor reports the person has left. (PS-4; AC-2; IA-5)

B.7 **Reviews.** Every week the Controls and Electrical Technician must compare remote sessions with the on-call rota and integrator work orders, and record any session nobody can explain as a suspected incident (POL-03). Every quarter the Office and Compliance Administrator must compare every account list with the staff and vendor list and remove anything that does not match. (AU-6; AC-2; DE.CM-03)

B.8 **Physical access.** The control room, hoist house, gate and unit panels, and the data logger cabinet must be locked when unattended. Keys are issued by the Plant Superintendent, listed in a key inventory checked every July, and a lock must be changed when a key is not returned. (PE-3; PR.AA-06; Form 1 Q4 to Q9)

B.9 **Passwords.** Passwords must be at least 14 characters, unique to the system, and never reused from personal accounts. They must not be written down at the control desk or in panels. Manufacturer default passwords must be changed before any device is connected, and the change form (A.10) confirms it. Shared OT passwords that remain (B.1) are changed every 6 months and whenever someone who knew them leaves. (IA-5; PR.AA-01; Form 1 Q9)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. The HMI PC and the engineering laptop are used only for plant operation and maintenance. (PL-4; PR.AT-01)

C.2 Workforce members must not keep or send company information in personal email, personal cloud storage, or personal messaging apps, and must never enter drawings, inundation maps, control system details, passwords, or employee personal information into public AI chatbots (POL-04 4.6). (PL-4)

C.3 **Operational security.** Do not discuss security measures, control system details, remote access, or gate operating plans with people outside the company. Report anyone asking unusual questions about the dam, photographing the gates or hoist house, or flying drones near the project, as POL-03 requires. (PL-4; Rev. 3A 3.2)

C.4 Only the company's OT USB drive may be connected to the HMI PC or the engineering laptop (POL-04 4.7). Personal phones must not be charged from OT equipment. (MP-7; PR.PS-05)

C.5 Workforce members must complete security training at hire and every year, covering physical and cyber security, CEII handling, remote access rules, and what to report. (AT-2; PR.AT-01; Rev. 3A 3.2)

C.6 Workforce members must report suspected incidents at once under POL-03 4.3, including their own mistakes. (IR-6)

C.7 Workforce members must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy is handled under A.4. The Plant Superintendent checks compliance through the weekly session review (B.7), the change forms (A.10), and the daily walk-down security checks. The annual independent assessment (P07) tests the key rules.

## 6. Exceptions
Exceptions follow A.9. No exception may allow an always-on vendor connection or remote gate control without MFA.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; termination checklist; key inventory; change form; P01 risk register; P02 SSP control statements AC-2, AC-17, IA-2(1), MA-4, SC-7, PS-4
