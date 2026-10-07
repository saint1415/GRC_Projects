# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (Security and Compliance Coordinator) |
| Approved by | President, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after a boundary change, a new contract requirement, or an incident |
| Implements (SP 800-53 Rev. 5) | Part A: PM-9, PL-2, RA-3, CA-2, CA-5, SA-9, PS-8, PL-1. Part B: AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, AC-18, AC-19, AC-20, IA-2, IA-2(1), IA-2(2), PS-4, PE-3, PE-8, MA-5, CM-8, SC-7, AU-6, SI-4. Part C: PL-4, AT-2 |
| CSF 2.0 | GV.RM-01, GV.RR-04, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01 |
| SP 800-171 Rev. 2 | 3.1.1 to 3.1.22, 3.2.1, 3.2.3, 3.3.5, 3.4.1, 3.5.1 to 3.5.3, 3.7.6, 3.9.2, 3.10.1 to 3.10.6, 3.11.1, 3.12.1 to 3.12.4, 3.13.1, 3.13.6, 3.14.7 |

**Why this policy has three parts.** A 7-person shop does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01) and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program for Controlled Unclassified Information (CUI), make sure only authorized people reach CUI and only as far as their job requires, and tell everyone how to use company systems.

## 2. Scope
All employees, temporary workers, and contractors of Cris Santos Company, and the MSP's technicians when they work on company systems. It covers every system and every copy of company information, on screen, on paper, or on media, including systems run for the company by the MSP and cloud providers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| President | Approves policies and the security budget; accepts risk; CMMC Affirming Official; ITAR Empowered Official |
| Office Manager | Security and Compliance Coordinator; runs this policy; requests and removes access; monthly checks; visitor log |
| CNC Programmer | Keeps job folders organized and permissions correct; follows Part C at the CAM workstation |
| Lead Machinist | Custody of printed drawings and USB drives on the floor; escorts service engineers |
| MSP | Creates and disables accounts on the Office Manager's request; operates device, network, and backup controls under the responsibility matrix |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Coordinator.** The Office Manager is the Security and Compliance Coordinator. The President must record the designation in writing and update it within 30 days of any change. (PL-1; GV.RR-02)

A.2 **Risk assessment.** The Coordinator must update the risk assessment every July, and after any boundary change (for example, a new system, a DNC link to the older machines, or enabling an AI feature), using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment. (RA-3; ID.RA-01; 3.11.1)

A.3 **Risk acceptance.** The Coordinator may accept Low and Very Low risks. Only the President may accept Moderate risk, in writing. High and Very High risks are not accepted; they need a dated treatment plan approved by the President. A gap in an SP 800-171 requirement is never accepted, only scheduled. (PM-9; GV.RM-01)

A.4 **Where CUI may live.** CUI may be stored, processed, or sent only on systems listed in the SSP as CUI Assets: the CUI suite (SYS-01), the CAM workstation, the quality PC, the two company laptops, the CNC machines and CMM, company-owned USB drives, and printed copies. No cloud service may hold CUI unless it meets FedRAMP Moderate-equivalent requirements under DFARS 252.204-7012(b)(2)(ii)(D) and is listed in the SSP. (SA-9; GV.SC-05; 3.1.20)

A.5 **Service providers.** Any MSP or other provider that administers company systems or handles CUI or security data must have a written responsibility matrix, named accounts with MFA for each technician, a 24-hour incident notice term, and technicians who are U.S. persons (22 CFR 120.62). The President reviews the MSP's SOC 2 report and responsibility matrix each year. (SA-9; GV.SC-05; 32 CFR 170.19(c)(2))

A.6 **SSP and SPRS accuracy.** The Coordinator keeps the SSP current and updates it within 30 days of a boundary change. The President must not post a score or sign an affirmation in SPRS unless the score is supported by a current self-assessment with evidence. (PL-2; 3.12.4; 32 CFR 170.22)

A.7 **Assessment and POA&M.** Controls must be assessed against the SP 800-171A objectives at least once a year by someone who does not operate them, or by the Coordinator with an independent reviewer. Every deficiency goes on the POA&M, which the Coordinator reviews with the President monthly. (CA-2; CA-5; 3.12.1 to 3.12.3)

A.8 **Records.** Security policies, the SSP, risk assessments, assessments, POA&Ms, incident records, training records, and visitor logs must be kept for at least 6 years. Audit logs must be kept for at least 1 year. (SI-12; GV.PO-02)

A.9 **Sanctions.** Breaking a rule in this policy set leads to coaching and retraining, a written warning, or termination, in proportion to intent and harm. The President decides. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.10 **Policy review and exceptions.** The Coordinator reviews this policy set every August. An exception must be requested in writing, rated on the risk scale, approved under A.3, recorded in the risk register, and limited to 12 months. (PL-1; GV.PO-02)

### Part B. Access control
B.1 **Unique accounts.** Every person must have their own account on every system that holds CUI, including the quality PC and the MSP's administrator access. Shared or generic accounts, including shared mailboxes that receive CUI, are not allowed. (IA-2; AC-2; 3.5.1)

B.2 **Least privilege.** Access must match the job. The Coordinator approves access in writing on the onboarding checklist before it is granted. ITAR job folders are limited to the President, the CNC Programmer, and the Quality Inspector. Nobody uses an administrator account for daily work; local administrator rights are not given to users. (AC-2; AC-3; AC-6; 3.1.2; 3.1.5)

B.3 **MFA.** MFA is required for the CUI suite, every computer that holds CUI, the firewall, the RMM console, the backup console, and every other administrator login, including those held by the MSP. (IA-2(1); IA-2(2); 3.5.3)

B.4 **Offboarding.** On or before a person's last day, the Coordinator completes the offboarding checklist: disable the CUI suite, commercial suite, ERP, and Prime A portal accounts; remove MFA registrations; collect keys, laptops, and USB drives; change the Wi-Fi key and alarm code. For an involuntary departure, access is disabled before the person is told. (PS-4; AC-2; 3.9.2)

B.5 **Monthly account check.** Each month the Coordinator compares every account list (CUI suite, commercial suite, ERP, Prime A portal, local accounts, MSP technicians) with the staff list and records the result. The President reviews the record quarterly. (AC-2; 3.1.1)

B.6 **Remote access.** Remote administration is allowed only through the MSP's RMM tool with MFA and session logging. The MSP may run only the remote privileged actions listed in its responsibility matrix. The Coordinator reviews the RMM session report monthly. (AC-17; 3.1.12; 3.1.15)

B.7 **Phones and mobile devices.** CUI suite access from a phone is allowed only through the suite's app with the company's app protection policy (PIN, no copy to personal apps, remote wipe of company data). Otherwise it is blocked. (AC-19; 3.1.18; 3.1.19)

B.8 **Wireless.** Enclave computers use wired connections. Staff Wi-Fi is for laptops and phones only, and its key is changed at least yearly and whenever someone leaves. Guest Wi-Fi stays separate. (AC-18; 3.1.16; 3.1.17)

B.9 **Screen lock.** Every computer locks after 10 minutes of inactivity, including the CAM workstation and quality PC. (AC-11; 3.1.10)

B.10 **Physical access and visitors.** Every non-employee who enters past the office signs the visitor log in and out and is escorted at all times. Before a visitor enters the shop or inspection room, staff ask whether the visitor is a U.S. person; for a foreign person, drawings in view are covered or removed. Machine and CMM service engineers stay with the Lead Machinist and may not connect their own media to company computers. The dock door is closed when unattended. Keys and the alarm code are recorded in a register. (PE-3; PE-8; MA-5; 3.10.1 to 3.10.5; 22 CFR 120.56)

B.11 **External systems.** The only external system approved for CUI is the Prime A supplier portal. Other customers must be asked to send CUI to the CUI suite. (AC-20; 3.1.20)

B.12 **Inventory.** The Coordinator keeps one inventory of every CUI Asset, Security Protection Asset, and Specialized Asset, with its CMMC category, owner, and where CUI is stored, and updates it within 30 days of any change. (CM-8; 3.4.1)

B.13 **Network separation.** Computers and machines that handle CUI sit on the enclave network segment, with traffic denied by default and allowed by exception. Office laptops, phones, and guest Wi-Fi stay off that segment. (SC-7; 3.13.1; 3.13.6)

B.14 **Log review.** Each month the Coordinator, with the MSP, reviews CUI suite sign-in and file activity, RMM sessions, and firewall alerts using the review checklist, and records the result. Alerts for mass download, new forwarding rules, and foreign sign-ins go to the Coordinator and the MSP. (AU-6; SI-4; 3.3.5; 3.14.7)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Use company systems for company work, and open only the jobs and files your work needs.

C.2 Never put CUI in personal email, personal cloud storage, text messages, messaging apps, the commercial suite, the ERP, or any public website or AI chatbot. Approved AI tools are listed in POL-04 4.6.

C.3 Lock your screen when you step away. Never share passwords or approve an MFA prompt you did not start.

C.4 Complete security awareness training at hire and every year, including CUI handling, phishing, insider threat indicators, and export control basics. Role-based training applies to CUI suite users. (AT-2; AT-3; 3.2.1 to 3.2.3)

C.5 Report a suspected incident, a lost device or drawing, a strange email, or an unescorted visitor to the Office Manager at once (POL-03 4.2).

C.6 When working from home, do not print CUI, keep screens out of view of others, and use only company laptops. (3.10.6)

C.7 Sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
The Coordinator checks compliance through the monthly account check, the visitor log, and the annual assessment (P07). Violations are handled under A.9.

## 6. Exceptions
See A.10. Open exceptions on 2026-09-01: none.

## 7. Related documents
POL-01 and POL-05 (pointer files), POL-03, POL-04, the SSP (P02), the risk register (P01), the gap analysis (P03), the onboarding and offboarding checklist, and the visitor log.
