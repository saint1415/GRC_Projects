# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated CNC machine shop) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-machinist |
| Effective date | 2026-09-05 (adopted 2026-09-04) |
| Review cycle | Every August with the risk assessment and the CMMC Level 1 self-assessment, and after a new system, a new customer contract with security terms, a hire, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, RA-2, RA-3, CA-2, SA-9, SR-3, AC-2, AC-3, AC-6, AC-11, AC-17, AC-20, AC-22, AU-6, IA-2, IA-2(1), IA-5, CM-8, SC-7, SC-28, SI-2, SI-3, SI-7, CP-2, CP-9, MP-6, MP-7, PE-3, PE-8, SI-12, AT-2, IR-4, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.RM-01, GV.SC-05, ID.AM-01, ID.AM-02, ID.AM-08, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.DS-01, PR.DS-11, PR.IR-01, PR.PS-02, DE.CM-01, RS.MA-01, RS.CO-02, RC.RP-01 |
| Contract requirements | FAR 52.204-21(b)(1)(i)-(xv) and (c); CMMC Level 1 (Self) (32 CFR 170.15, 170.22; DFARS 252.204-7021); OEM supplier quality agreements and NDAs; aerospace PO notice terms |

## 1. Purpose
Protect customer drawings, CNC programs, quality records, and the shop's money, and meet the security terms in customer contracts, in a way one person can actually run. Each rule is written so it can be checked (P07). Rules tagged **[FAR]** carry a FAR 52.204-21 requirement and must be fully in place before the CMMC Level 1 affirmation, because Level 1 allows no plan of action.

## 2. Scope
All shop information in any form (electronic, paper, spoken), on every system in the Shop Business Systems (P02), on paper in the bay, and at every vendor or subcontractor that handles it. It applies to the owner-machinist and to any future employee, helper, or student. Contractors are bound through their contracts and NDAs.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead | Owner-machinist | Runs this policy; keeps records |
| CMMC affirming official (32 CFR 170.22) | Owner-machinist | Runs the Level 1 self-assessment and affirms in SPRS only when every requirement is MET |
| Risk acceptor | Owner-machinist | Accepts or treats every risk (4.4) |
| On-call IT technician | Contractor under NDA | Technical help on request; no standing access |
| Customers' contacts | OEM quality contacts; aerospace buyer | Receive notices under 10.4 |

One person writes, follows, and checks these rules, so independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The shop must keep a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 This policy designates the owner-machinist, in writing, as security lead and CMMC affirming official. (PM-2; GV.RR-02)
4.3 A risk assessment must be done every August and after any major change, using NIST SP 800-30 Rev. 1. Every risk must have a treatment and a due date. (RA-3; PM-9; ID.RA-01)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and are never accepted as they are. (PM-9; GV.RM-01)
4.5 Controls must be self-assessed every August (P07), together with the CMMC Level 1 self-assessment. At least every second year, someone outside the shop (such as the IT technician) must review the assessment. (CA-2)
4.6 **[FAR] CMMC.** The owner must not affirm in SPRS unless every one of the 15 requirements is MET on the SP 800-171A objectives. The self-assessment and affirmation must be repeated every year and after any change that affects a requirement. (CA-2; 32 CFR 170.15; 170.22)
4.7 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Exceptions and conduct
5.1 Any future employee or helper who breaks this policy must be dealt with in proportion to intent and harm: retraining, written warning, or ending the work. Each case is documented.
5.2 A contractor or vendor that breaks its NDA, flowdown, or this policy must be dealt with under its contract, up to ending it. (SA-9)
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. No exception is allowed for a **[FAR]** rule while the shop holds a CMMC status. (PL-1)

## 6. Customers, vendors, and subcontractors
6.1 The owner must keep a supplier list showing each vendor or subcontractor, what shop or customer information it receives, and its NDA or flowdown date. (SA-9; SR-3; ID.AM-02)
6.2 **[FAR]** Outside processors receive only the PO and the specification callout. If a processor must see an aerospace drawing, the owner must first flow down FAR 52.204-21 and the CMMC requirement and confirm the processor's Level 1 (Self) status in writing. (SA-9; GV.SC-05; 52.204-21(c); DFARS 252.204-7021(f))
6.3 OEM drawings are shared only with a processor or other shop that the OEM has approved and that has signed an NDA. (SA-9; OEM SQA)
6.4 The productivity suite provider's SOC 2 report must be reviewed every year, and the owner must run the customer controls it lists. (SA-9; GV.SC-07)
6.5 **[FAR]** Remote support sessions must be started and watched by the owner. Unattended remote access must be off. (AC-17; 52.204-21(b)(1)(i))

## 7. Access control
7.1 **[FAR]** Every person must have their own account. Credentials are never shared. (IA-2; AC-2; PR.AA-01; 52.204-21(b)(1)(v))
7.2 **[FAR]** Daily work on the laptop must use a standard user account. The administrator account is used only to install or change software. (AC-6; 52.204-21(b)(1)(ii))
7.3 MFA with an authenticator app must be on for every service that offers it: the productivity suite, the accounting SaaS, and the website builder. (IA-2(1); PR.AA-03)
7.4 **[FAR]** Passwords must be unique passphrases of at least 14 characters, kept in a password manager. Default passwords (router, machine share, new devices) must be changed before use. (IA-5; 52.204-21(b)(1)(vi))
7.5 The owner must approve the bookkeeper's and any other account in writing, remove it the day the work ends, and review account lists every quarter. (AC-2; PR.AA-05)
7.6 Laptop and phone must lock after 5 minutes idle. (AC-11)
7.7 **Emergency access.** Recovery codes, the laptop encryption recovery key, and a one-page access sheet must be kept sealed with the owner's designated emergency contact. (AC-2; CP-2)
7.8 On the first workday of each month the owner must review sign-in history for the productivity suite and the accounting SaaS, and the router's device list, and note the review in the security log. (AU-6; DE.CM-01)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Aerospace drawings (FCI), OEM drawings and models, CNC programs for customer parts, credentials | Approved locations only (8.2); named-person sharing; never in consumer apps |
| **Confidential** | Quotes, prices, quality records, contracts, tax and bank records | Shop systems only |
| **Public** | Website text, approved photos | Reviewed before posting (8.7) |

8.2 **[FAR]** Restricted data may be kept only in: the productivity suite (aerospace files in the one restricted Aerospace folder), the laptop, the customer portals, and paper in the bay. It must not go to a personal account, a consumer app, or an AI tool. (AC-3; AC-20; 52.204-21(b)(1)(iii))
8.3 **Intake screening.** Before downloading or quoting any drawing package, the owner must check it for CUI markings, DoD distribution statements, ITAR or EAR markings, and export classification notes. A marked package must not be downloaded or worked; the owner tells the customer the shop cannot accept it. (RA-2; ID.AM-05; 22 CFR 122.1; DFARS 252.204-7012)
8.4 **[FAR]** Sharing links must go to named people and expire within 30 days. "Anyone with the link" sharing is not allowed for Restricted data. (AC-3; 52.204-21(b)(1)(ii))
8.5 **Released programs.** Released programs for OEM parts must be kept in a read-only Released folder with a file hash. Before each OEM run, the program in the controller must be compared with the released copy. Any edit made at the controller must be saved back, recorded on the traveler, and approved by the OEM before the part ships if it changes the released process. (SI-7; PR.DS-01; OEM SQA)
8.6 The Jobs and records folders must be backed up at least weekly to a copy the laptop cannot overwrite (a drive kept disconnected between backups, plus a second cloud backup service), and a test restore done every quarter. (CP-9; PR.DS-11)
8.7 **[FAR]** Only the owner may post to the website or social media. Every photo must be checked before posting for part numbers, drawings, and customer names, and the website must be reviewed every quarter. (AC-22; 52.204-21(b)(1)(iv))
8.8 **[FAR]** Paper with Restricted data goes in the locked cabinet and is shredded when no longer needed. Old laptops, phones, drives, and USB sticks must be wiped (encrypted, then reset) or destroyed by a recycler that gives a certificate. Each disposal is recorded. (MP-6; ID.AM-08; 52.204-21(b)(1)(vii))
8.9 Security records (this policy, risk assessments, self-assessments and CMMC evidence, incident records, contracts) must be kept at least six years; quality records as long as each SQA requires (10 years today). (SI-12; 32 CFR 170.15(c)(2); OEM SQA)

## 9. Acceptable use, shop floor, and training
9.1 Shop devices are for shop work. Family members must not use them. (PL-4)
9.2 **[FAR]** Automatic updates and the built-in antivirus must stay on. The owner checks CAM software and router firmware for updates on the first workday of each month. Software comes only from the vendor or the official app store. (SI-2; SI-3; 52.204-21(b)(1)(xii)-(xv))
9.3 **[FAR]** The laptop and VMC must be on their own wired segment. Visitors, the alarm panel, and personal devices use the guest Wi-Fi. The VMC share must require a password. (SC-7; PR.IR-01; 52.204-21(b)(1)(i), (x))
9.4 **[FAR]** Only shop-labeled USB sticks may carry programs to the machines. The service technician's laptop or media may connect to a machine only after the owner scans it, or the technician uses a shop stick. (MP-7; SI-3; 52.204-21(b)(1)(xv))
9.5 **[FAR]** Visitors sign the visitor log (kept one year), stay in the office corner unless escorted, and drawings are covered or put away while they are in the bay. The owner keeps a list of who holds keys. (PE-3; PE-8; PR.AA-06; 52.204-21(b)(1)(viii)-(ix))
9.6 **AI tools.** No customer information may be entered into any AI tool unless the tool is approved in writing after a P10 assessment and its terms protect confidentiality and bar training on shop data. AI-written G-code must be simulated in CAM and dry-run before any cut, and never used in a released OEM program without OEM approval. (PL-4; AC-20; SA-9)
9.7 The owner must complete a small-business security course every year and read monthly security reminders. Any future helper must be trained before getting access. (AT-2; PR.AT-01)

## 10. Incident response
10.1 The shop must keep an incident runbook (P08) with a printed contact list in the office and at home. (IR-8; RS.MA-01)
10.2 Every suspected incident (ransom note, strange sign-in, phishing click, lost device, misdirected drawing, a program that does not match its released copy) must be written in the incident log the same day, with the time it was discovered. (IR-6; IR-4)
10.3 If a drawing package turns out to contain CUI or ITAR data after download, the owner must stop work, isolate the files, and tell the customer the same day. (IR-6; 8.3)
10.4 Customer notices must meet the P08 notification matrix: the aerospace customer within 72 hours of an incident affecting its information, and each OEM within 5 business days of unauthorized access to its confidential information. (IR-6; RS.CO-02; Aerospace PO terms; OEM SQA)
10.5 No ransom may be paid without legal advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident; lessons learned recorded within 30 days of closing an incident. (IR-8; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. Restored programs are compared with released hashes before use. (CP-2; RC.RP-01)
11.2 The owner must keep a written overflow arrangement with a nearby shop for urgent repeat jobs, used only with each customer's approval (6.2, 6.3). (CP-2)
11.3 Before a hurricane, follow the storm checklist in P01 R-011. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual self-assessment (P07), the CMMC Level 1 self-assessment, and the monthly review in 7.8. Section 5 covers breaches of this policy.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 show where each topic lives in this policy.

## Appendix A. Devices and data locations
| Item | Restricted data held | Protection required |
|---|---|---|
| Laptop | Drawings, models, CAM files, programs | 7.2, 7.6, 9.2, 9.3; disk encryption |
| Phone | Email; setup photos | 7.3, 7.6 |
| Productivity suite | Drawings, programs, records | 7.3, 8.4, 8.6 |
| VMC and turning center controllers | Programs in memory | 8.5, 9.3, 9.4 (specialized assets) |
| Router | Traffic | 7.4, 9.3 |
| USB sticks (shop-labeled) | Programs | 8.8, 9.4 |
| Paper cabinet in the bay | Travelers, inspection records | Locked; 8.8 |
