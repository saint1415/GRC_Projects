# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operator of one mixed-use commercial building) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new building system, a new contractor with system access, a hire, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, RA-3, CA-2, SA-9, AC-2, AC-3, AC-6, AC-17, AC-19, AU-6, CM-3, CM-7, CM-8, IA-2, IA-2(1), IA-5, SC-7, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, IR-4, IR-5, IR-6, IR-8, PE-3, PT-5 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-07, ID.AM-01, ID.AM-07, ID.AM-08, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-11, PR.IR-01, PR.PS-02, DE.AE-02, RS.MA-01, RS.CO-02, RC.RP-01 |
| Benchmark and law | CISA CPG 2.0 (voluntary); Fla. Stat. 501.171(2) and (8); 16 CFR 682.3(a); FTC Act Section 5 |

## 1. Purpose
Protect the building, the people in it, and the personal information the business holds, in a way one person can actually run. The rules are written so each can be checked (P07). They also set out the "reasonable measures" Florida law requires for personal information (Fla. Stat. 501.171(2)).

## 2. Scope
All business information in any form (electronic, paper, spoken) and every system in the Property Systems Profile: the access control, video, and thermostat services and their devices (SYS-01 to SYS-03), the building network (SYS-04), the property management, email and file, and screening services (SYS-05, SYS-06, SYS-09), and the laptop and phone (SYS-07, SYS-08). It applies to the owner and any future employee. Contractors are bound through the security terms in section 6.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security and privacy lead, administrator of every system | Owner | Runs this policy; issues and removes all access; decides breach questions; keeps records |
| Risk acceptor | Owner | Accepts or treats every risk (section 4.4) |
| On-call IT consultant | Contractor | Technical help on request; no standing access |
| Installer and HVAC contractor | Contractors | Service building devices under section 6; no standing administrator access |
| Vendors | Access control, video, thermostat, property management, email, and screening vendors | Operate their platform safeguards |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must keep a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The owner is designated in writing, by this policy, as the security and privacy lead and the only system administrator. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every July and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9; ID.RA-01)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every July (P07). At least every second year the evaluation must include an outside reviewer, such as the IT consultant working from the POA&M rather than the owner's own answers. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. Exceptions must be written, risk-rated under 4.4, recorded in the risk register, and expire within 12 months. (PL-1; GV.PO-02)

## 5. Building systems (access control, video, thermostats, network)
5.1 **No new device, app, or vendor feature without approval.** The owner must approve, in the security log, any new device on the building network, any new app with access to a building system, and any optional vendor feature (analytics, face recognition, audio, integrations) before it is turned on. AI features also need a written P10 assessment. (CM-7; CM-3; PR.PS-02)
5.2 Entrance and lobby cameras must not record audio. Face recognition must not be used. (CM-7; PT-5; Fla. Stat. 934.03)
5.3 Building devices (door controllers, cameras, thermostats) must be on their own network, separate from the free lobby Wi-Fi, which must have guest isolation on. No building device or router admin page may be reachable from the internet. (SC-7; PR.IR-01; CPG 3.I, 3.S)
5.4 Default passwords must be changed before a device is connected. The router administrator password must be a unique passphrase. (IA-5; CPG 3.A)
5.5 Automatic firmware updates must stay on in every building platform. The router firmware must be checked each quarter. (SI-2; PR.PS-02)
5.6 The owner must keep a one-page device list (type, location, serial number, firmware) and a network sketch, updated after every installer or HVAC visit. (CM-8; ID.AM-01)
5.7 Life safety comes first. Egress hardware, the fire alarm, and the elevator must never depend on the building network or any cloud service, and no cyber response step may lock an exit.

## 6. Contractors and vendors
6.1 Each contractor with building credentials or system access (installer, HVAC contractor, IT consultant, janitorial contractor) must sign one-page security terms: named accounts only, no sharing, MFA where offered, notice to the owner within 72 hours of any incident that could affect the building or its data, and return or deletion of access at the end of the work. (SA-9; GV.SC-05; CPG 1.D)
6.2 Contractors must not hold standing administrator accounts. The owner grants a named, time-limited account with MFA for each service visit and removes it afterward. (AC-2; AC-6; AC-17; CPG 1.E)
6.3 The owner must keep a vendor list showing each vendor, the data or systems it touches, and its contract terms. (SA-9; ID.AM-07)
6.4 The access control vendor's SOC 2 report must be reviewed every year, and the owner must operate the customer controls that report lists. (SA-9; GV.SC-07)

## 7. Access control
7.1 Every person must have their own account. Credentials must never be shared, including with contractors. (IA-2; AC-2; PR.AA-01; CPG 3.C)
7.2 MFA by authenticator app (or a security key) must be on for every account that offers it, starting with the access control, video, thermostat, property management, and email accounts. Text-message codes are not enough for those accounts. (IA-2(1); PR.AA-03; CPG 3.F)
7.3 Passwords must be unique passphrases of at least 16 characters, kept in a password manager. Passwords must not be saved in the web browser. (IA-5; CPG 3.B)
7.4 **Building credentials.** Each credential is issued only on a tenant's or contractor's written request and must name the person. Leases and contractor terms require notice of departures within 1 business day, and the owner disables the credential the same day. On the first business day of each month the owner reviews the credential list and disables credentials unused for 60 days. Each July every tenant confirms its list in writing. (AC-2; PE-3; PR.AA-05; CPG 3.D)
7.5 Files with Restricted data may be shared only with named people. "Anyone with the link" sharing is not allowed. (AC-3; PR.AA-05)
7.6 Daily work on the laptop must use a standard account; the administrator account is used only to install software. (AC-6; CPG 3.G)
7.7 The laptop must lock after 5 minutes idle and the phone after 1 minute. The phone must have remote wipe turned on. (AC-19)
7.8 On the first business day of each month the owner must review administrator changes and after-hours door events in the access control portal, new sign-ins in email, and the router's connected-device list, and note the review in the security log. (AU-6; DE.AE-02)

## 8. Data handling
8.1 Information is classified in three levels. (ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Guarantor and applicant Social Security numbers, license copies, credit reports, personal financial statements; tenant bank details; portal passwords and recovery codes | Approved locations only (8.2); named sharing; MFA; kept only as long as 8.6 allows |
| **Confidential** | Door access history, video, credential lists, leases, contracts, this policy set | Owner and named contractors only |
| **Public** | Vacancy listings, building hours | No restriction |

8.2 Restricted data may be kept only in the property management service, one restricted folder in the business file plan, and the locked home-office cabinet. It must not stay in email attachments, the laptop's downloads folder, or the phone. (AC-3; PR.DS-01)
8.3 The laptop must use full-disk encryption; the phone must use a passcode. (SC-28; PR.DS-01)
8.4 Email and files must have a backup the owner controls, with version history. The access control configuration (schedules, access groups, credential list) must be exported monthly and after any change. The laptop must be backed up to an encrypted drive. A restore must be tested each July. (CP-9; PR.DS-11; CPG 3.O)
8.5 Tenants must be told that bank details for rent never change by email, and any request to change a payment destination must be confirmed by calling a known number. (AT-2)
8.6 **Retention and disposal.** Applicant and guarantor files and credit reports: kept for the lease term plus 3 years for signed leases, and 90 days for applications that did not lead to a lease, then destroyed. Video: 30 days (vendor setting). Door access history: 1 year. Paper must be cross-cut shredded; electronic copies deleted and the trash emptied; old devices wiped (encrypted, then reset) or destroyed by a recycler that gives a certificate. Each disposal is recorded. (MP-6; SI-12; ID.AM-08; Fla. Stat. 501.171(8); 16 CFR 682.3)
8.7 Security records (this policy, risk assessments, assessments, incident records, disposal records) must be kept for at least 5 years. (SI-12)

## 9. Acceptable use and training
9.1 The laptop is for business work. Family members must not use it. (PL-4)
9.2 Software must come only from official app stores or the vendor's site. Automatic updates and the built-in antivirus must stay on. Unknown USB devices must not be connected. (SI-2; SI-3; CPG 3.R)
9.3 **AI tools.** An AI tool or feature may process video, images of people, or Restricted data only after a written P10 assessment and the owner's written approval. (PL-4; CM-7)
9.4 Lobby and parking signs must say that cameras record video, and that no audio is recorded. (PT-5)
9.5 The owner must complete a short small-business security course every year and read CISA alerts. Any future employee must be trained before getting access. (AT-2; PR.AT-01; CPG 3.J)

## 10. Incident response
10.1 The business must keep an incident runbook (P08) with a printed contact list in the home office and in the management closet. (IR-8; RS.MA-01)
10.2 Every suspected incident (a door unlocked out of schedule, a new administrator nobody added, a changed thermostat schedule, a phishing click, a lost phone, a vendor notice) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6)
10.3 If personal information may have been accessed, the owner must record the date of "determination of the breach or reason to believe a breach occurred" and meet the deadlines in the P08 notification matrix, confirmed by counsel. (IR-6; RS.CO-02; Fla. Stat. 501.171(3) to (6))
10.4 No ransom may be paid without counsel's advice and an OFAC sanctions check. (IR-4)
10.5 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident.

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner must keep one-page manual procedures for locking and unlocking the entrances with mechanical keys and for setting each thermostat at the wall, plus a sealed envelope (recovery codes, spare keys, access sheet) at the attorney's office, and written fallback arrangements with the HVAC contractor and installer. (CP-2; CPG 6.A)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the monthly review in 7.8. A contractor that breaks section 6 is dealt with under its contract, up to ending it. Any future employee who breaks this policy is sanctioned in proportion to intent and harm, and the sanction is recorded.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Where Restricted and Confidential data live
| Location | Data held | Protection required |
|---|---|---|
| Property management service (SYS-05) | Leases, ledgers, tenant bank details | 7.2; vendor backups |
| Restricted folder in the business file plan (SYS-06) | Guarantor and applicant files, credit reports | 7.2, 7.5, 8.4, 8.6 |
| Access control and video services (SYS-01, SYS-02) | Credential list, door history, video | 7.2, 7.4, 8.4 |
| Laptop (SYS-07) | Working copies only | 8.3, 7.7, 9.2 |
| Phone (SYS-08) | Second factors; admin apps | 7.7; recovery codes kept off the phone |
| Home-office cabinet | Signed leases, guaranties | Locked; 8.6 |
