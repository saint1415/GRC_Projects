# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent utility engineering consultant) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-engineer |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new client, a new tool or vendor, a new subcontractor, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, RA-2, RA-3, CA-2, SA-9, PS-6, PS-7, AC-2, AC-3, AC-6, AC-11, AC-17, AC-19, AC-20, AC-21, AU-6, IA-2(1), IA-2(2), IA-5, SC-7, SC-8, SC-28, CM-8, CP-2, CP-9, MP-6, MP-7, SI-2, SI-3, SI-5, SI-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.OC-03, GV.SC-05, GV.SC-07, ID.AM-01, ID.AM-07, ID.AM-08, ID.RA-01, ID.IM-02, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-02, PR.IR-01, DE.AE-02, DE.CM-09, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Regulatory and contract basis | N22-R01 by contract: Client A SSA-A (1) to (8) and Client B VAA-B (1) to (5); FERC CEII NDA (18 CFR 388.113(h)(2)); Fla. Stat. 501.171; Client C confidentiality clause (P03) |

## 1. Purpose
Protect client security information and the business's access to client systems, and meet the security terms the clients pass down from the NERC CIP standards, in a way one person can actually run. Each rule is written so it can be checked (P07).

## 2. Scope
All business information in any form (electronic, paper, spoken), on every component of the Core Business Systems (SYS-01 to SYS-08), on paper in the home office, at every vendor that holds it, and the owner's accounts on client-operated systems (the Client A portal and the Client B gateway). It applies to the owner-engineer and to anyone who later works for the business. Subcontractors and the IT technician are bound through their contracts and access agreements.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead, incident commander, risk acceptor | Owner-engineer | Runs this policy; decides incident and notice questions; keeps records |
| On-call IT technician (NDA) | Contractor | Technical help on request; no standing access; no access to client folders |
| CAD drafting subcontractor | Contractor | Works from markups only; never receives client security information without written client approval (6.3) |
| Clients | Client A, Client B | Authorize named access and operate the portal and gateway controls on their side |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The owner-engineer is designated by this policy as the person accountable for security and for every client security term. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every July and after any major change (a new client, tool, vendor, or subcontractor, or an incident), using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9; ID.RA-01)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan. A risk that could put a client's protection system or BCSI at risk is never accepted at High. (PM-9; GV.RM-01)
4.5 Controls must be self-assessed every July (P07). At least every second year, someone outside the business (such as the IT technician under NDA, or a client's security reviewer) must review the results. (CA-2; ID.IM-02)
4.6 This policy must be reviewed every year and after a major change or incident. (PL-1; GV.PO-02)
4.7 The owner must keep a list of every client security term (SSA-A, VAA-B, the CEII NDA, and client confidentiality clauses) and check it against this policy when a contract is signed or renewed. (PL-1; GV.OC-03)

## 5. Exceptions and enforcement
5.1 Any departure from this policy must be written down as an exception with the reason, the risk level under 4.4, and an end date no more than 12 months away. An exception may never break a client term. (PL-1)
5.2 A subcontractor or vendor that breaks its agreement or this policy is dealt with under its contract, up to ending it, and the affected client is told as 10.2 requires. (PS-7; SA-9)

## 6. Clients, subcontractors, and vendors
6.1 **Client terms come first.** Where a client term is stricter than this policy, the client term applies to that client's information. (SA-9; GV.SC-05)
6.2 The owner must keep a vendor list showing each SaaS provider, subcontractor, and tool, the client information it may hold, and the date its terms were reviewed. No vendor may hold client information until its terms have been reviewed. (SA-9; ID.AM-07)
6.3 **No client security information to helpers without client approval.** No subcontractor, standby engineer, or helper may see Client A BCSI, Client B settings or event records, or CEII until (a) the client (or FERC, for CEII) has approved that person in writing and (b) the person has signed an access agreement that bars further sharing and requires return and deletion on request. Drawing markups for the drafter must contain no BCSI. (PS-6; AC-3; PR.AA-05)
6.4 When a person the client has authorized no longer needs access, the owner must tell the client within 24 hours (SSA-A (4)). (PS-7; AC-2)
6.5 The email and file suite provider's SOC 2 report must be reviewed every year (P09), and the owner must run the customer controls it lists. (SA-9; GV.SC-07)
6.6 IT technician sessions must be started and watched by the owner. The technician never opens client folders. (AC-17; PS-6)

## 7. Access control
7.1 Each person has their own account. Credentials, including client portal and gateway credentials, are never shared. (AC-2; PR.AA-01)
7.2 **MFA by authenticator app or security key** must be on for the email and file suite, the accounting SaaS, and any other service that holds client or financial information. SMS codes may be used only as a fallback. (IA-2(1); IA-2(2); PR.AA-03)
7.3 Passwords must be unique passphrases of at least 14 characters, kept in a password manager. Passwords must never be saved in a browser. (IA-5; PR.AA-01)
7.4 Daily work on the laptop must use a standard account. The administrator account is used only to install or update software. (AC-6; PR.AA-05)
7.5 The laptop must lock after 5 minutes idle and the phone after 30 seconds. (AC-11)
7.6 **Emergency access.** Recovery codes for the email suite, the accounting SaaS, and the password manager, plus a one-page emergency sheet (client contacts, insurer hotline), must be kept in a sealed envelope held by the owner's attorney. (AC-2; CP-2)
7.7 On the first business day of each month, the owner must review the email and file suite sign-in history and file sharing activity, and the security advisories of the settings and analysis software vendors, and record the review in the security log. (AU-6; SI-5; DE.AE-02)
7.8 Every quarter, the owner must review every file share and remove any not needed. Before answering a client's access verification, the owner must run the sharing report and attach it (SSA-A (3)). (AC-2; AC-3; PR.AA-05)
7.9 **Client remote access.** Connect to Client B only through Client B's gateway, only from the business laptop, and only for a session Client B has enabled. Never approve an MFA push the owner did not start; report it to Client B at once (10.3). (AC-17; PR.AA-05)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Client Restricted** | Client A BCSI (relay settings, network drawings, control house photos), Client B settings files and event records, FERC CEII, Client C load data | Approved locations only (8.2); encrypted; named people only (6.3) |
| **Confidential** | Contracts, invoices and bank details, the drafter's W-9, credentials, this policy set | Encrypted storage; owner only |
| **Public** | Business website, published papers | No restriction |

8.2 Client Restricted information may be kept only in: the Client A portal (Client A BCSI), the encrypted laptop, owner-only client folders in the business suite (not Client A BCSI), and the dedicated USB drives (8.6). It must never be kept in email, a personal or consumer account, a phone camera roll, or an AI tool without client consent. (AC-3; AC-20; PR.DS-01)
8.3 Every device that can hold Client Restricted information must use full-disk encryption. CEII stays in its own encrypted archive. (SC-28; PR.DS-01)
8.4 Client A BCSI moves only through the Client A portal; Client B files only through Client B's file exchange. No "anyone with the link" shares. (SC-8; AC-21; PR.DS-02)
8.5 Photos at a client site are taken only with the client's permission, uploaded to the client's portal or folder the same day, and deleted from the phone. Phone photo sync to a personal cloud stays off. (AC-19; PR.DS-01)
8.6 Only the two dedicated, labeled USB drives may carry settings files. They are scanned before every site use and at each client's kiosk where one exists, and never used for personal files. (MP-7; DE.CM-09)
8.7 The owner must keep a client information register: one row per client data set, its location, and its return or destroy date. Client information is returned or destroyed within 30 days after a project ends (or sooner if the contract says so), with written certification to the client. CEII is destroyed or returned to FERC on request. (CM-8; MP-6; ID.AM-01)
8.8 Paper is cross-cut shredded. Electronic copies are deleted and the deletion recorded. USB drives and devices are wiped (encrypted, then erased) before reuse or disposal, or destroyed by a recycler that gives a certificate. (MP-6; ID.AM-08)
8.9 Security records (this policy, risk assessments, assessments, incident logs, certifications, and client notices) are kept for 6 years. (SI-12)
8.10 Local settings databases and software license files on the laptop must be backed up daily to the owner-only folder in the business suite, and a restore tested every quarter. (CP-9; PR.DS-11)

## 9. Acceptable use and training
9.1 Business devices are for business work. Household members must not use them. (PL-4)
9.2 Once the dedicated field laptop is in place (P01 R-002), only it may connect to client relays or the Client B gateway, and it is never used for email or web browsing. Until then, the owner runs a full antivirus scan and installs updates before each site visit. (PL-4; AC-6)
9.3 Automatic updates and the built-in antivirus stay on. Settings and analysis software is updated before each project and each site visit. Software comes only from the vendor's site or an official app store. (SI-2; SI-3; PR.PS-02)
9.4 Business devices use a business network separate from household devices, with a changed router admin password. Until it exists, client gateway sessions use the phone hotspot. (SC-7; PR.IR-01)
9.5 **AI tools.** No client information goes into any AI tool without (a) a written P10 assessment, (b) terms that bar the provider from keeping or training on the data, and (c) the client's written consent. (PL-4; SA-9)
9.6 The owner must complete Client A's annual module and one general security course each year, including phishing. (AT-2; PR.AT-01)

## 10. Incident response
10.1 The business must keep the incident runbook (P08) and a printed contact sheet at the home office and in the field bag. (IR-8; RS.MA-01)
10.2 Every suspected incident (lost or stolen device, phishing click, unexpected MFA prompt, wrong share, vendor notice) must be written in the incident log the same day with the time it was discovered. If it may affect a client's information or systems, the client must be notified **within 24 hours of discovery** (SSA-A (5), VAA-B (5)). (IR-5; IR-6; RS.MA-02; RS.CO-02)
10.3 A suspected compromise of the Client B gateway credentials, or an MFA push the owner did not start, must be reported to Client B's operations desk immediately by phone (VAA-B (4)). (IR-6; RS.CO-02)
10.4 An unauthorized disclosure of CEII must be reported promptly to FERC (18 CFR 388.113(h)(2)). A breach of personal information must be assessed for notice under Fla. Stat. 501.171 (30 days). Deadlines are in the P08 notification matrix. (IR-6)
10.5 No ransom may be paid without the insurer's and counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident; lessons learned are recorded within 30 days of closing an incident. (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities: owner access and phone first, then client contact, then a clean device. (CP-2; RC.RP-01)
11.2 The owner must keep a written standby arrangement with another independent engineer, under NDA, for urgent Client B and Client C work. Client A work waits unless Client A has authorized that engineer by name (6.3). (CP-2)
11.3 Each client is given a second contact (the owner's attorney) who will tell them if the owner is unavailable. (CP-2)
11.4 When a hurricane watch is issued, the owner takes the laptop, phone, dedicated USB drives, and printed contact sheet. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07), the monthly review in 7.7, and the quarterly share review in 7.8. Departures are handled under section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P04 SaaS control map; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P09 SOC 2 self-check; P10 AI use assessment. Pointer files POL-02 to POL-05 show where each topic lives in this policy. `policy-control-map.csv` traces every statement.

## Appendix A. Where client information may live (8.2)
| Location | Client Restricted data allowed | Protection required |
|---|---|---|
| Client A portal | Client A BCSI (the only place for shared copies) | Client MFA; 7.1 |
| Engineering laptop | Working files for all clients; CEII archive | 8.3, 7.4, 7.5, 9.3 |
| Business suite, owner-only client folders | Client B, C, and D project files (no Client A BCSI) | 7.2, 7.8, 8.4 |
| Dedicated USB drives (2) | Settings files for site work | 8.6, 8.8 |
| Phone | MFA prompts only; site photos only until uploaded the same day | 8.5, 7.5 |
| Email | No Client Restricted attachments; links to the portal instead | 7.2, 7.7 |
| Paper in the home office | Markups during active projects | Shredded at close-out (8.8) |
