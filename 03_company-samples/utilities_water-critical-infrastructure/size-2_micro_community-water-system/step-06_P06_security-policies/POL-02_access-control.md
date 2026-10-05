# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (community water system, 2,850 population served) |
| Policy ID | POL-02 |
| Owner | Office Manager (security and compliance coordinator), with the Chief Operator for every rule that touches the plant |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Every August (next review 2027-08-31), and after a major change or an incident |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, RA-3, PS-8, SA-9, CA-2, SI-12, PL-1, SC-24, CM-3. Part B: AC-1, AC-2, AC-3, AC-6, AC-17, AC-18, AU-6, CM-5, IA-2, IA-2(1), IA-5, MA-4, PS-4. Part C: PL-4, AT-2, AT-3, CM-7, MP-7, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, ID.IM-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.AT-02, PR.PS-01, PR.PS-04, PR.IR-01, PR.IR-03 |
| Regulatory basis | No federal rule requires these controls at 2,850 persons served (P03). Written to the NIST CSF 2.0 and SP 800-82 Rev. 3 benchmark, and as readiness for SDWA section 1433 automated-systems security (42 U.S.C. 300i-2(a)(1)(A)(ii)) if the population served passes 3,300 |

**Why this policy has three parts.** A 7-person water system does not need five separate policies. This policy carries the program rules that would otherwise be in an Information Security Policy (POL-01, Part A) and the staff use rules that would otherwise be in an Acceptable Use Policy (POL-05, Part C). POL-01 and POL-05 are short pointer files.

## 1. Purpose
Set up the company's security program, make sure only authorized people reach the plant control system and company information, and only as far as their job requires, and tell staff and contractors how to use company systems.

## 2. Scope
All 7 employees and every contractor or vendor who uses or supports company systems: the SCADA integrator, the managed service provider (MSP), and the remote monitoring vendor. It covers the Water Treatment SCADA System (WTSS: the HMI computer, the plant PLC, the RTUs, the cellular modems, the remote desktop tool, the alarm dialer, and the remote monitoring gateway), the office network, company phones, and the SaaS systems (productivity suite, billing, accounting and payroll, remote monitoring service).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner and General Manager | Approves policies, contracts, and the security budget; accepts Moderate risk; decides sanctions with the Office Manager |
| Office Manager | Security and compliance coordinator; runs this policy; requests and removes business accounts through the MSP; keeps the risk register, policies, and records |
| Chief Operator | Owns the WTSS; approves and removes HMI, remote desktop, and remote monitoring access; approves every integrator session; holds the HMI and PLC administrator credentials |
| Operators and Utility Field Technician | Use only their own accounts; follow Part C; report problems at once |
| MSP | Creates and disables business accounts and manages the office firewall and Wi-Fi on the Office Manager's request |
| SCADA integrator | Works on the WTSS only under B.7 |

**Overlapping roles.** The Chief Operator both runs the WTSS and approves access to it. The Office Manager's quarterly check of the Chief Operator's reviews (B.6), the independent assessment (A.6), and the Owner's monthly POA&M meeting are the compensating checks.

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Coordinator.** The Office Manager is the security and compliance coordinator, and the Chief Operator makes OT security decisions. The Owner must record both designations in writing (done 2026-08-31) and update them within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The Office Manager and Chief Operator must update the risk register every July using NIST SP 800-30 Rev. 1, and sooner when the new subdivision is connected, the HMI computer is replaced, the anomaly detection feature moves beyond advisory use, or after a cyber incident. Each risk needs an owner and a treatment. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Office Manager or Chief Operator may accept Low and Very Low risks. Only the Owner may accept a Moderate risk, with a treatment plan or a written reason. High and Very High risks must not be accepted; the Owner approves a dated treatment plan instead. **A risk that could affect public health through chemical feed or treatment must never be accepted above Low.** (PM-9; GV.RM-01)

A.4 **Sanctions.** Anyone who breaks a security rule is sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. Contractors may lose access or their contract. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Security terms before access.** No contractor or vendor may get remote access to the WTSS, or hold company OT files or customer data, unless its contract or an addendum covers: named technicians, notice to the company of any security incident affecting company systems or data within 24 hours, remote sessions only under B.7, and return or deletion of company files at the end of the contract. Existing contracts must be amended by 2026-12-31. (SA-9; GV.SC-05)

A.6 **Assessment.** An independent assessor who does not operate the controls must assess the WTSS controls at least every 2 years, and the Office Manager and Chief Operator must do a self-review in each year between. (CA-2; ID.IM-01)

A.7 **Records.** Security records (policies, risk register, assessments, incident logs, access reviews, training records) must be kept for at least 5 years. Drinking water records follow 40 CFR 141.33 and POL-04 4.7. (SI-12; GV.PO-02)

A.8 **Policy review and access.** The Office Manager reviews this policy set every August and after an incident or major change, and keeps the current version where all staff can read it. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated on the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

A.10 **Safeguards come first.** No security change may disable or bypass the hypochlorite pump's mechanical stroke limit, the chlorine analyzer's alarm relays, the alarm dialer, or the hand-off-auto switches, or make hand operation harder. Every OT change plan must say how it keeps them. (SC-24; CM-3; PR.IR-03)

### Part B. Access control
B.1 **Named accounts.** Everyone must use their own account in the productivity suite, billing, accounting, the remote monitoring service, and the remote desktop tool. The shared HMI "operator" login must be replaced with named HMI accounts by 2026-12-31. Until then, the shared HMI login may be used only inside the locked control room, and operators must record remote changes in the daily log. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** Access must match the job. HMI roles are view, operate, and administer; only the Chief Operator holds administer, with a sealed copy of the administrator password kept by the Owner for emergencies. The Chief Operator approves OT access in writing; the Office Manager approves business access. (AC-2; AC-3; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for email and the productivity suite, billing, accounting and payroll, the remote desktop tool, the remote monitoring service, and every administrator login, including the MSP-held firewall login. The remote desktop tool and remote monitoring service must have MFA by 2026-09-30. (IA-2(1); PR.AA-03)

B.4 **Remote access to the HMI.** Remote access to the HMI computer is allowed only through the remote desktop tool, with a named account and MFA, from a device the Chief Operator has approved and recorded. Unattended (always-on) access is prohibited from 2026-09-30. No other remote access tool may be installed on the HMI computer. (AC-17; PR.AA-05)

B.5 **Leavers.** On or before a person's last day, the Office Manager completes the termination checklist: business accounts disabled through the MSP; HMI, remote desktop, and remote monitoring accounts disabled by the Chief Operator; keys, phones, and the meter-reading handheld collected; and **every shared password or code the person knew changed the same day** (Wi-Fi, alarm codes, any remaining shared device password). For an involuntary termination, access is removed before the person is told. (PS-4; AC-2; IA-5)

B.6 **Reviews.** Each month the Office Manager compares business system user lists with the staff list. Each quarter the Chief Operator reviews HMI, remote desktop, and remote monitoring users, and the Office Manager checks that the review was done. (AC-2; AC-6; PR.AA-05)

B.7 **Integrator and vendor access.** Integrator technicians must be named in the contract and use their own remote desktop accounts with MFA. Each session must be requested in advance, approved by the Chief Operator, and watched by a licensed operator, who ends it when the work is done. The integrator must not keep copies of company files beyond what the contract allows. MSP technicians must use named accounts with MFA, and the MSP must send a current technician list each year. (AC-17; MA-4; SA-9; PR.AA-05)

B.8 **Log review.** Each week the Chief Operator reviews the remote desktop connection history and the remote monitoring sign-ins. Each month the Chief Operator reviews HMI setpoint and alarm-limit changes against the daily logs. Anything unexplained is reported under POL-03. (AU-6; PR.PS-04)

B.9 **Passwords and device credentials.** Passwords must be at least 14 characters and never reused from personal accounts. Default and commissioning passwords on any PLC, RTU, modem, gateway, or network device must be changed before it is connected, and when a person who knew them leaves (B.5). Device credentials are kept only in the company password manager, which only the Owner, Office Manager, and Chief Operator can open; the password spreadsheet must be deleted by 2026-09-30. Visitors and contractors use a separate guest Wi-Fi that cannot reach the plant network. (IA-5; AC-18; PR.AA-01)

B.10 **PLC program mode.** The PLC key switch must stay in RUN. It may be moved to program mode only for approved integrator work (B.7), recorded in the daily log, and returned to RUN when the work ends. The PLC must have a program password by 2026-10-31. (CM-5; PR.PS-01)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Customer information may be looked up only to do your job. (PL-4; PR.AT-01)

C.2 Never store or send Restricted information (POL-04 4.1), such as SCADA drawings, device passwords, the PLC program, or customer bank details, through personal email, personal cloud storage, messaging apps, or public AI chatbots. (PL-4)

C.3 Do not connect personal phones, personal computers, or USB drives to the HMI computer or the plant network. Do not browse the web or read email on the HMI computer. Only the Chief Operator may connect the encrypted backup drives (POL-04 4.5). (CM-7; MP-7; PR.PS-01)

C.4 Complete security awareness training at hire and every year, and take part in phishing simulations. Licensed operators and the Chief Operator also complete OT security training for water systems each year. (AT-2; AT-3; PR.AT-01; PR.AT-02)

C.5 Report any suspected incident at once under POL-03 4.2, including your own mistakes. (IR-6)

C.6 Sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Office Manager checks compliance through the monthly reconciliation and quarterly review (B.6), the weekly log review (B.8), and the independent assessment (A.6, P07).

## 6. Exceptions
Exceptions follow A.9. No exception may allow unattended remote access to the HMI computer or a change that weakens A.10.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; termination checklist (due 2026-09-30); OT account procedure (due 2026-10-31); P01 risk register; P02 control statements AC-2, AC-17, IA-2(1), IA-5, MA-4, PS-4; P07 POA&M
