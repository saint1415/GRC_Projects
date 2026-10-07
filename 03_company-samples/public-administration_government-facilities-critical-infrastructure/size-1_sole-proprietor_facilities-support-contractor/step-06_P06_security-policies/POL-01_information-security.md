# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (facilities support contractor operating government buildings) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner |
| Effective date | 2026-09-05 (adopted 2026-09-04) |
| Review cycle | Every August with the risk assessment, and after a new contract, a new system or service, a hire or subcontractor, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PL-4, PS-3, PS-6, RA-2, RA-3, CA-2, CA-7, SA-4, SA-9, SR-1, SR-3, SR-5, AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, AC-19, AC-20, AC-21, AC-22, AU-6, IA-2, IA-2(1), IA-5, MA-4, MA-5, MP-3, MP-4, MP-5, MP-6, MP-7, CM-7, CM-11, CM-12, SC-7, SC-28, SI-2, SI-3, SI-12, AT-2, AT-3, IR-4, IR-5, IR-6, IR-8, CP-2, CP-9 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-07, ID.AM-07, ID.AM-08, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-02, PR.IR-01, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Contract and legal basis | City security exhibit (CT-C, SP 800-53 Rev. 5 Moderate); FAR 52.204-21, -23, -25, -30, -9 (CT-F); 32 CFR Part 2002; GSA BTTRG v3.0 section 1.6.1; Fla. Stat. 119.0701(2)(b), 119.071(3), 501.171 |

## 1. Purpose
Protect the customers' buildings, the people in them, and the customers' information that the owner holds, and meet the security terms of the city contract and the federal subcontract in a way one person can actually run. Each numbered rule is written so it can be checked (P07).

## 2. Scope
All business and customer information in any form (electronic, paper, spoken), including city drawings, BAS programs, cardholder exports, door schedules, federal contract information (FCI), and GSA drawings marked CUI. It covers every component of the Building Systems Support Environment (SYS-01 to SYS-07), **every account the owner holds in a customer system** (SYS-08), the van, the home office, and the owner's conduct on GSA systems (SYS-09). It applies to the owner and to any future employee or subcontractor. The on-call IT technician is bound through the NDA.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security officer, records contact named in the contracts, CUI handler, incident handler | Owner | Runs this policy; keeps the records; makes every report |
| Risk acceptor | Owner | Accepts or treats every risk (4.4) |
| On-call IT technician | Contractor (NDA 2026-08-03) | Technical help on request; no standing access |
| City IT manager; prime contractor's security officer | Customer roles | Receive incident notices; own their systems and logs |

The owner is designated in writing, by this policy, to all the roles above (PM-2). Because one person writes, follows, and checks these rules, independence is limited; rule 4.5 adds an outside check.

## 4. Governance and risk
4.1 The business must keep a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; PL-2; GV.PO-01)
4.2 A risk assessment must be completed every August and after any change listed in the review cycle, using NIST SP 800-30 Rev. 1. Every risk must have a treatment, a due date, and a status. (RA-3; PM-9; ID.RA-01)
4.3 Information is categorized at Moderate for confidentiality, integrity, and availability (P02 section 6). A new type of customer data needs a new categorization before it is accepted. (RA-2)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and are never accepted as they are. Any risk to the safety of building occupants is told to the city facilities manager. (PM-9; GV.RM-01)
4.5 Controls must be self-assessed every August (P07). At least every second year, someone outside the business must review the assessment. (CA-2; CA-7)
4.6 This policy must be reviewed at least every August and after an incident. Exceptions must be written, risk-rated under 4.4, and expire within 12 months. (PL-1; GV.PO-02)

## 5. Contracts and customer rules come first
5.1 Where a customer contract or GSA rule is stricter than this policy, the customer rule wins. The owner keeps a one-page summary of each contract's security terms in the security folder. (PL-1)
5.2 The owner must not subcontract any administration of city building systems without the city's written approval (city contract), and must flow down FAR 52.204-21 to any subcontractor whose systems would hold FCI (52.204-21(c)). (SA-9; PS-7)
5.3 The owner must complete the city's annual basic cybersecurity training and GSA's annual IT security awareness training on time, and keep the certificates. (AT-2)

## 6. Services, suppliers, and parts
6.1 **Approved services.** Customer data may be kept or processed only in the services listed in Appendix A. A new service needs the provider checklist in 6.2 first. (SA-9; GV.SC-05)
6.2 Before using a new service, the owner records the provider, the data it will hold, MFA availability, where the data is stored, incident notice terms, and any SOC 2 or similar report. (SA-4; SA-9)
6.3 The productivity suite provider's SOC 2 report must be reviewed every year, and the owner must run the customer controls it lists (P09). (SA-9; GV.SC-07)
6.4 **Parts for the federal building.** Before buying any part for CT-F, the owner must: buy only from the controls distributor or the manufacturer; check the manufacturer against FAR 52.204-25 covered telecommunications equipment and confirm it is not a Kaspersky product (52.204-23); and search SAM.gov for "FASCSA order" (52.204-30(b)(2)). The SAM.gov search is also repeated every quarter. Results go in the parts log. (SR-1; SR-3; SR-5)
6.5 Remote support sessions on the owner's devices must be started and watched by the owner. Unattended access is not allowed on any device. (MA-4; MA-5)

## 7. Access control
7.1 Every account must be personal. If a customer system only offers a shared account, the owner must ask the customer in writing for a named account and keep the shared password only in the password manager. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every service and customer system that offers it. (IA-2(1); PR.AA-03)
7.3 Passwords must be unique passphrases of at least 14 characters, kept in a password manager. Default passwords must be changed before first use. Notes apps, paper, and email are not password stores. (IA-5)
7.4 **Remote access to customer building systems is allowed only through the path the customer's IT owner approves** (for the city: the city VPN with city MFA). No remote-desktop agents, modems, or other paths may be installed on customer equipment. (AC-17; MA-4; PR.AA-05)
7.5 Daily work on the laptop must use a standard account. The administrator account is used only to install or change software. (AC-6; CM-11)
7.6 **Emergency access.** Recovery codes for the suite, the password manager, and the laptop disk recovery key, plus a one-page emergency access sheet, must be kept in a sealed envelope held by the owner's attorney, for use if the owner or the phone is unavailable. A second authenticator method must be registered where offered. (CP-2; IA-5)
7.7 On the first business day of each month, the owner must review: the access control tenant's administrator changes and after-hours door unlocks; the BAS supervisory audit log (when the city gives access); the remote-desktop session log (until removed); and the suite's sign-in and sharing history. The review and any finding are noted in the security log; anything unexplained is reported under section 10. (AU-6; DE.AE-02)
7.8 The owner must keep a list of every account the owner holds in customer systems and give the city IT manager the current list at least every quarter and on any change, so the city can disable the owner's access if the owner is unavailable. (AC-2; PR.AA-05)
7.9 A lost or stolen PIV card must be reported to the prime contractor immediately. The card is carried only on federal building days and handed to the prime when the subcontract ends. (FAR 52.204-9(b); IA-4)
7.10 Laptop locks after 5 minutes idle; phone after 1 minute. (AC-11)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | GSA drawings marked CUI; cardholder exports; door schedules; security system diagrams; BAS passwords | Approved locations only (Appendix A); encrypted; named people only; never on the phone except the access control app |
| **Confidential** | City building drawings and BAS programs (exempt under Fla. Stat. 119.071(3)(b)); work orders and point lists (FCI); contracts | Approved locations only; encrypted; shared only with the customer's named people |
| **Public** | Business name and phone number | No restriction |

8.2 Every device that can hold Restricted or Confidential data must use full-disk encryption. (SC-28; PR.DS-01)
8.3 **Sharing.** CUI may go only to the prime contractor and GSA. Exempt city records may go only to people the city names. Files are shared by named-person links from the restricted folder, never "anyone with the link" and never as email attachments to new recipients. (AC-21; MP-5; PR.DS-02)
8.4 **CUI.** CUI is kept only in the restricted CUI folder (not synced to the phone) and the locked van cabinet. Excerpts, screenshots, and notes taken from CUI must be marked CUI. Copies outside these places must be deleted. (MP-3; MP-4; 32 CFR 2002.14(c))
8.5 Controller programs and door schedule exports must be saved after every change to the engineering folder, which is backed up nightly to the cloud backup folder and monthly to an encrypted external drive kept in the home office. A comparison of backup copies with running programs is done every quarter. (CP-9; PR.DS-11)
8.6 **Retention.** Keep only the two most recent cardholder exports. Keep city records the city needs until the contract ends; then transfer them to the city and destroy exempt duplicates (Fla. Stat. 119.0701(2)(b)4.). Keep security records (this policy, risk assessments, assessments, incident records) for 3 years after the contract they relate to ends. (SI-12)
8.7 Paper is cross-cut shredded. Old devices and drives are wiped (encrypted, then reset to factory settings) or destroyed by a recycler that gives a certificate. Each disposal is recorded. CUI destruction must make it unreadable and irrecoverable (32 CFR 2002.14(f)). (MP-6; ID.AM-08)
8.8 Requests from the public for city records are sent to the city's custodian of public records; the owner does not answer them directly (Fla. Stat. 119.0701(3)(a)). (SI-12)

## 9. Acceptable use and training
9.1 Business devices are for business work. Family members must not use them. (PL-4)
9.2 **Devices and work sites.** The laptop must not be left in the van overnight or unattended at a customer site. It must never be connected to a GSA network, and connects to a city network only through the city VPN or as the city IT manager approves. The phone may hold the access control mobile app and the authenticator app, with remote wipe on. (PL-4; AC-19; AC-20)
9.3 Software comes only from the vendor or the operating system's store. Automatic updates and the built-in antivirus stay on. Removable drives must be owner-owned and encrypted, and are not plugged into customer equipment without the customer's approval. (SI-2; SI-3; MP-7; CM-7)
9.4 Customer data must not be put into any service that is not in Appendix A, including free web tools, file converters, and chat services. (AC-20; SA-9)
9.5 Photos or details of customer buildings, systems, or people must not be posted anywhere public. (AC-22; PL-4)
9.6 **AI tools.** No customer data (point lists, drawings, schedules, cardholder data, photos of panels) may be entered into any AI tool. Configuring an AI feature in a customer system requires a written assessment (P10) and the customer's written decision first. (PL-4; SA-9)
9.7 Work traffic at home uses the separate work network on the owner-owned router once installed (2026-11-30); until then, the phone hotspot is used for city VPN sessions. (SC-7; PR.IR-01)
9.8 Besides the customer courses in 5.3, the owner completes a CUI awareness course accepted by the prime and the access control vendor's administrator course, and reads monthly security reminders. (AT-2; AT-3; PR.AT-01)

## 10. Incident response
10.1 The business keeps an incident runbook (P08) with a printed contact sheet in the van and the home office. (IR-8; RS.MA-01)
10.2 Every suspected incident (unexplained change in a customer system, lost device or PIV card, phishing click, misdirected file, provider notice) is written in the incident log the same day, with the time it was discovered. (IR-5; RS.MA-02)
10.3 **Notice clocks** (P08 notification matrix): the city IT manager within 24 hours of discovering a suspected incident; the prime immediately for anything touching GSA systems, GSA data, or GSA credentials; covered telecommunications equipment within 1 business day and Kaspersky or FASCSA items within 3 business days (through the prime); the city within 10 days of determining a breach of personal information the owner maintains (Fla. Stat. 501.171(6)(a)), which the 24-hour contract notice already covers. (IR-6; RS.CO-02)
10.4 **Building safety comes first.** In an incident affecting a building system, the owner first agrees safe door and equipment states with the city facilities manager, then contains. (IR-4)
10.5 No ransom is paid for any customer system. The city may not pay one (Fla. Stat. 282.3186). Any payment for the owner's own systems needs counsel's advice and an OFAC sanctions check first. (IR-4)
10.6 The runbook is walked through every year and after any real incident; lessons learned are recorded within 30 days. (IR-3)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner keeps a written arrangement with a backup controls firm, approved in writing by the city, for alarms and urgent work when the owner is unavailable, with a way for the city to give that firm temporary credentials. (CP-2)
11.3 The owner keeps a one-page manual operation sheet for each city building, with a copy in each building's mechanical room, and walks the city maintenance worker through it once a year. (CP-2; CP-3)
11.4 Before a named storm, the owner saves every running controller program and charges the laptop and hotspot. (CP-9)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the monthly review in 7.7. A future employee or subcontractor who breaks this policy is dealt with in proportion to intent and harm, up to ending the arrangement, and the action is recorded. (PS-8)

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P04 SaaS control map; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P09 SOC 2 self-check; P10 AI use assessment. Pointer files POL-02 to POL-05 show where each topic lives in this policy.

## Appendix A. Approved locations for customer data (CM-12)
| Location | Data allowed | Protection required |
|---|---|---|
| Laptop (engineering folder, restricted CUI folder, city records folder) | All levels | 8.2, 7.5, 9.3 |
| Productivity suite (same folder structure, synced to the laptop only) | All levels | 7.2, 8.3, 8.4 |
| Cloud backup folder and encrypted external drive | Controller programs, door schedule exports | 8.5 |
| Phone | Access control app session, MFA, alarm texts only; no files | 9.2 |
| Accounting service | Invoices and contract numbers only | 7.2 |
| Locked van cabinet and home office | Paper drawings, including CUI sets | 8.4 |
| **Not approved** | Consumer AI chatbot, remote-desktop service (being cancelled), personal email, any other service | 9.4, 9.6 |
