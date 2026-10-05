# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (security and compliance lead) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, RA-3, RA-5, SI-2, PS-8, SA-9, CA-2, SI-12, PL-1. Part B: AC-1, AC-2, AC-6, AC-11, AC-17, SC-7, IA-2, IA-2(1), IA-5, IA-8, PS-4, AU-6. Part C: PL-4, AT-2, AT-3, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.AT-02, PR.PS-02, PR.IR-01, DE.AE-02 |
| Regulatory drivers | C-COMMUNICATIONS-R01: 47 CFR 64.2009(b), (c), (e); 64.2010(a)-(f). C-COMMUNICATIONS-R03: 47 CFR 1.20003(a) |

**Why this policy has three parts.** A 7-person carrier does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security and CPNI program, make sure only authorized people reach customer, network, and lawful-intercept information and only as far as their job requires, make sure customers are properly authenticated before CPNI is released, and tell the workforce how to use company systems.

## 2. Scope
All workforce members of Cris Santos Company, and the network engineering consultant, the MSP, and any vendor staff who sign in to company systems. It covers every system in the SSP (P02), the AI assistant, the network hut, and every copy of company information. Part B section B.9 to B.12 covers customers' access to their own CPNI by phone, online, and in person.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner and General Manager | Approves policies and the security budget; accepts Moderate and higher risks; signs the CPNI certification; CALEA senior officer; decides sanctions with the Office Manager |
| Office Manager | Security and compliance lead and CPNI compliance coordinator; runs this policy; grants and removes access to the BSS; reviews accounts and logs; keeps CPNI records |
| Network Operations Lead | Grants and removes network and voice platform access; manages network credentials; reviews network logs |
| MSP | Creates and disables productivity suite and device accounts on the Office Manager's request |
| Network engineering consultant | Uses only a named login, only for scheduled work |
| All workforce | Protect credentials; authenticate customers as Part B requires; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Named leads.** The Office Manager is the security and compliance lead and the CPNI compliance coordinator. The Owner and General Manager is the officer who signs the annual CPNI certification and the CALEA senior officer. Each designation must be in writing and updated within 30 days of any change, and a change of CALEA senior officer must also be reflected in the SSI policies filed with the FCC (POL-03 4.6). (PM-2; GV.RR-02; 64.2009(e); 1.20003(a))

A.2 **Risk assessment.** The Office Manager must update the risk assessment every July, and after any major change (a new voice platform, a new middle-mile circuit, a new AI feature), using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Office Manager may accept Low and Very Low risks. Only the Owner and General Manager may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner and General Manager. Risks to 911 calling rated High are never accepted. (PM-9; GV.RM-01)

A.4 **Sanctions, including CPNI.** A workforce member who breaks a security rule or uses or releases CPNI without authorization must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. Looking up call detail without a customer request or a work reason is a violation. The Office Manager must record each sanction; the Owner and General Manager must approve suspension or termination. Reporting a mistake in good faith is never sanctioned. This is the company's express disciplinary process under 47 CFR 64.2009(b). (PS-8; GV.RR-04)

A.5 **No CPNI terms, no CPNI.** No vendor may receive or reach CPNI or customer PII until the Office Manager has approved it and the contract includes confidentiality, use limited to serving the company, incident notice within 24 hours, and deletion at the end of service. Contracts in place before 2026-09-01 must be amended at renewal. The Office Manager keeps a register of every third party allowed access to CPNI, kept for at least one year after access ends. (SA-9; GV.SC-05; 64.2009(c))

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2; ID.IM-01)

A.7 **Evidence for the CPNI certification.** By February 1 each year, the Office Manager must give the Owner and General Manager a file that supports the certification statement: training records, the result of a 10-call sample of call detail requests, the account change notice settings, the CPNI complaint log, and any breaches. The statement must describe what the company actually does. (CA-2; GV.OV-01; 64.2009(e))

A.8 **Retention.** CPNI third-party access records: at least 1 year. CPNI breach records: at least 2 years (POL-03 4.3). Lawful-intercept records: as the CALEA SSI policies state. Security policies, risk assessments, assessments, and training and sanction records: at least 3 years. (SI-12; GV.PO-02; 64.2009(c); 64.2011(d))

A.9 **Vulnerability and patch management.** The Network Operations Lead must review security advisories for the router, OLTs, switches, and hut servers each month and record the result. Critical fixes must be applied within 14 days, or a dated exception approved under A.10. The MSP does the same for office IT under its contract. (RA-5; SI-2; ID.RA-01; PR.PS-02)

A.10 **Policy review and exceptions.** The Office Manager must review this policy set every August and after an incident or major change, and keep the current version where every workforce member can read it. An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. No exception may relax a CPNI authentication rule in Part B. (PL-1; GV.PO-01; GV.PO-02)

### Part B. Access control
B.1 **Named accounts everywhere.** Every person must have their own account in the BSS, the voice platform, the productivity suite, the router VPN, the EMS, and on network devices. Shared or generic accounts are not allowed. Until named network accounts are in place (target 2026-12-31), the shared network login is an approved exception under A.10, changed whenever anyone who knows it leaves. (AC-2; IA-2; PR.AA-01)

B.2 **Least privilege.** Access must match the job. Only the Office Manager and the Network Operations Lead may export call detail records or the full customer list. API keys must have only the rights their integration needs. The Office Manager approves BSS access, and the Network Operations Lead approves network and voice platform access, in writing before it is granted. (AC-2; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for the BSS, the voice platform, the productivity suite, the router VPN, the cloud backup console, and every administrator login, including logins held by the MSP and the consultant. (IA-2(1); PR.AA-03)

B.4 **Termination.** On or before a person's last day, the Office Manager must complete the termination checklist: disable BSS, suite, voice platform, VPN, and EMS accounts; ask the MSP to remove device access; change any shared secret the person knew; collect keys, tablets, and hut access; and remind the person in writing of their CPNI confidentiality duty. For an involuntary termination, access is removed before the person is told. (PS-4; AC-2)

B.5 **Monthly reconciliation and log review.** Each month the Office Manager must compare the BSS, suite, voice platform, and backup user lists with the staff list, and the Network Operations Lead must do the same for VPN and network accounts; anything that does not match is removed. In the same session they must review: BSS reports of call detail views without a matching ticket, voice platform exports and sign-ins, and VPN logins. Results go on the review checklist. (AC-2; AU-6; DE.AE-02)

B.6 **Remote and management access.** Network devices and hut servers may be administered only from the hut or through the router VPN with a named MFA login. Management interfaces must never be reachable from the internet. The consultant's login is enabled only for scheduled work and disabled afterward. (AC-17; SC-7; PR.IR-01)

B.7 **Passwords and secrets.** Passwords must be at least 12 characters and never reused from personal accounts. Shared secrets, device passwords, API keys, and SNMP strings must be kept in the company password manager, never in text files, notes apps, or email. Default passwords and community strings must be changed before a device goes into service. (IA-5; PR.AA-01)

B.8 **Locking.** Computers must lock after 10 minutes idle and tablets after 2 minutes, with a 6-digit passcode or better. A screen that must stay visible (the outage map at the counter) must run under a display-only account with no access to the BSS. (AC-11)

B.9 **Customer authentication by phone.** Call detail may be released on a customer-initiated call only after the caller gives the account PIN, and the PIN prompt must not hint at biographical or account information. If the caller has no PIN or cannot give it, the representative must offer to mail the information to the address of record or call back the telephone number of record, and nothing else. Recognizing the caller's voice is not authentication. Before discussing any other account information (services, bills, balance), the representative must authenticate the caller with the PIN or by calling back the telephone number of record. General help that reveals no account information (outage status, prices, troubleshooting) needs no authentication. (IA-8; PR.AA-03; 64.2010(a), (b))

B.10 **Customer authentication online.** Online access to CPNI requires a portal password. Passwords and any backup authentication must be set up and reset without readily available biographical or account information, using a one-time code sent to the telephone number or email of record. The AI assistant must not show account information to anyone who has not signed in to the portal. (IA-8; IA-5; 64.2010(c), (e))

B.11 **Customer authentication in person.** CPNI may be released at the counter only after the customer shows a valid photo ID that matches the account. (IA-8; 64.2010(d))

B.12 **Change notices.** The BSS must notify the customer immediately when a password, PIN, online account, or address of record is created or changed, by a message to the telephone number or address of record (never to new contact information) that does not reveal the changed data. (IA-8; DE.CM-03; 64.2010(f))

B.13 **Emergency network access.** A sealed copy of a break-glass network administrator credential is kept in the General Manager's safe for use when the Network Operations Lead and the consultant are unavailable. Any use must be logged and the credential changed afterward. (AC-2)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Workforce members must look up only the accounts they are serving, and never their own, a family member's, or a neighbor's call detail. (PL-4; PR.AT-01; 64.2009(b))

C.2 Workforce members must not store or send CPNI, customer PII, network configurations, or lawful-intercept information with personal email, personal cloud storage, messaging apps, or public AI chatbots. POL-04 4.7 lists the approved AI tools. (PL-4)

C.3 Workforce members must lock their screen when stepping away and never share passwords or MFA codes, including with the MSP, the consultant, or a caller claiming to be from a vendor. (AC-11; PL-4)

C.4 Workforce members must complete security awareness training at hire and every year, take part in phishing simulations, and complete CPNI and customer authentication training before handling customer accounts and every year after. Training records are kept under A.8. (AT-2; AT-3; PR.AT-01; PR.AT-02; 64.2009(b))

C.5 Workforce members must report suspected incidents at once under POL-03 4.2, including a caller pressing for call detail without a PIN, and their own mistakes. (IR-6)

C.6 Workforce members must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. Compliance is checked through the monthly reconciliation and log review (B.5), the annual CPNI evidence file (A.7), and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.10.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; P01 risk register; P02 SSP control statements AC-2, IA-2(1), IA-8, PS-4, PS-8; P03 rows G-016 to G-026
