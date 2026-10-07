# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Assistant Manager (Security and Privacy Lead) |
| Approved by | Owner-Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Yearly (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, SI-12, CA-2. Part B: AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, IA-2, IA-2(1), IA-5, PS-4. Part C: PL-4, AT-2, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01 |
| PCI DSS v4.0.1 (N72-R01) | Requirement groups 2.2, 7.2, 8.2, 8.3, 8.4, 12.1, 12.2, 12.3, 12.5, 12.6, 12.8 |

**Why this policy has three parts.** A 7-person motel does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the motel's security program, make sure only authorized people reach guest, card, and business information and only as far as their job requires, and tell the workforce how to use motel systems.

## 2. Scope
All employees of Cris Santos Company, the contracted bookkeeper and handyman, and any temporary staff. It covers every system and every copy of motel information, including systems run for the motel by the MSP, the PMS vendor, the payment gateway, and the lock vendor.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner-Manager | Approves policies and the security budget; accepts Moderate risk; decides sanctions with the Assistant Manager; holds emergency credentials |
| Assistant Manager | Security and Privacy Lead; runs this policy; grants and removes access; reviews logs and accounts; starts vendor remote sessions |
| MSP | Creates and disables Windows accounts on the Assistant Manager's request; operates device and network controls |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security and Privacy Lead.** The Assistant Manager is the designated Security and Privacy Lead and PCI DSS contact. The Owner-Manager must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02; PCI DSS 12.1)

A.2 **Risk assessment.** The Assistant Manager must update the risk assessment every July, and after any major change such as a new PMS or payment design, a franchise decision, or switching on a new AI feature, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01; PCI DSS 12.3)

A.3 **Risk acceptance.** The Assistant Manager may accept Low and Very Low risks. Only the Owner-Manager may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner-Manager. (PM-9; GV.RM-01)

A.4 **Sanctions.** A workforce member who breaks a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Assistant Manager records each sanction, and the Owner-Manager approves suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Service providers.** No vendor may store, process, or transmit card data or guest personal information for the motel, or have remote access to motel systems, until (a) written terms cover security, remote access, and incident notice, (b) a vendor that touches card data provides a current PCI DSS attestation of compliance, and (c) it is on the provider list with its responsibilities recorded. The Assistant Manager checks every AOC each year. (SA-9; GV.SC-05; PCI DSS 12.8)

A.6 **Assessment, scope, and validation.** Security controls must be assessed at least once a year by someone who does not operate them. The Assistant Manager must confirm the PCI DSS scope (what stores, processes, or transmits card data) at least every 12 months and after any change to how payments are taken, before the Owner-Manager signs the SAQ. Nobody may sign an SAQ answer as "In Place" without evidence. (CA-2; PL-2; PCI DSS 12.5)

A.7 **Retention of security records.** Policies, risk assessments, assessments, SAQs and attestations, incident records, and sanction records must be kept for at least 3 years, and longer where a law or POL-03 requires (for example, a Florida no-harm determination is kept at least 5 years). (SI-12; GV.PO-02)

A.8 **Policy review and access to policies.** The Assistant Manager must review this policy set every August and after an incident or major change, and must keep the current version where every workforce member can read it. (PL-1; GV.PO-02; PCI DSS 12.1)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

### Part B. Access control
B.1 **Named accounts.** Every workforce member must have their own account on the front desk PC, in the PMS, and in email. Shared or generic logins are not allowed. The front desk inbox is reached through each person's own mailbox (delegated access), not a shared password. (IA-2; AC-2; PR.AA-01; PCI DSS 8.2)

B.2 **Least privilege.** Access must match the person's job, using the PMS role list. The Assistant Manager must approve access in writing (the onboarding checklist) before it is granted. The "view full card number" permission is limited to the Owner-Manager until virtual cards are charged without display, and then removed from everyone. (AC-2; AC-3; AC-6; PR.AA-05; PCI DSS 7.2)

B.3 **MFA.** MFA is required for every PMS user, every mailbox, the gateway merchant portal, the website-builder account, and every administrator or remote login, including logins held by the MSP (firewall, backup console, remote management). (IA-2(1); PR.AA-03; PCI DSS 8.4)

B.4 **Termination.** On or before a workforce member's last day, the Assistant Manager must complete the termination checklist: disable PMS, email, gateway portal, and lock system access; ask the MSP to remove the Windows account; remove MFA registrations; collect keys and staff key cards; change any shared secret the person knew (staff Wi-Fi passphrase and any shared door or safe code). For an involuntary termination, access is disabled before the person is told. (PS-4; AC-2; PCI DSS 8.2)

B.5 **Monthly reconciliation.** Each month the Assistant Manager must compare the user lists of the PMS, the suite, the gateway portal, and the lock system with the staff roster, and remove anything that does not match. Every 6 months the Assistant Manager must confirm each person's PMS role still fits their job. (AC-2; AC-6; PR.AA-05; PCI DSS 7.2)

B.6 **Locking.** Computers must lock after 15 minutes idle at most. The front desk PC must not sign in automatically; staff switch to their own account at shift change. (AC-11; PR.AA-03; PCI DSS 8.2)

B.7 **Vendor remote access.** Vendor remote support tools (including the lock vendor's) must be off by default. The Assistant Manager turns a tool on for one session at a time, after confirming the request by calling the vendor at a known number; the session uses MFA or a one-time code, is noted in the remote access log, and is turned off afterwards. MSP technicians use named accounts with MFA, and the MSP gives the Assistant Manager a current technician list every year. (AC-17; IA-2(1); SA-9; PCI DSS 8.2, 8.4)

B.8 **Passwords and defaults.** Passwords must be at least 12 characters and never reused from personal accounts. No device may keep a vendor default password (firewall, CCTV recorder, terminals' admin functions, Wi-Fi). The staff Wi-Fi passphrase must be changed every year and whenever a workforce member leaves. (IA-5; PR.AA-01; PCI DSS 2.2, 8.3)

B.9 **Emergency access.** The Owner-Manager keeps a sealed PMS administrator credential and a sealed set of emergency key cards for use when the Assistant Manager is unavailable or the lock system is down. Any use must be reported to the Assistant Manager and the credential changed afterwards. (AC-2; PR.AA-05)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Motel systems are for motel work. The front desk PC is used only for the PMS, email, and approved websites; no personal browsing, downloads, or software. (PL-4; PR.AT-01; PCI DSS 12.2)

C.2 Workforce members must not store or send guest or card information with personal email, personal phones, messaging apps, or public AI chatbots. POL-04 lists the approved tools. (PL-4; PCI DSS 12.2)

C.3 Workforce members must lock or switch accounts when stepping away, and never share passwords or MFA codes, including with a caller who says they are from a vendor, the MSP, an OTA, or the bank. (AC-11; PL-4)

C.4 **Callers and visitors.** Never give out a room number, guest details, or card details by phone. Call vendors back at the number on file before acting on any request. Issue a key card only after checking the guest's ID or the registered guest's approval. (AT-2; PL-4; PCI DSS 12.6)

C.5 Workforce members must complete security training at hire and every year, including the front desk module on card handling, phishing, and callers. (AT-2; PR.AT-01; PCI DSS 12.6)

C.6 Workforce members must report suspected incidents within 1 hour under POL-03 section 4.2, including their own mistakes. (IR-6)

C.7 Workforce members must sign an acknowledgment of this policy at hire and after each yearly update. (PL-4; PCI DSS 12.2)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Assistant Manager checks compliance through the monthly reconciliation (B.5), the weekly log review (POL-04 4.10), and the yearly independent assessment (P07). The Owner-Manager reviews progress monthly.

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; remote access log; P01 risk register; P02 SSP control statements AC-2, AC-17, IA-2(1), PS-4
