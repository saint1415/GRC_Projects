# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (pipeline integrity engineering consultant) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Engineer-owner |
| Effective date | 2026-09-14 (adopted 2026-09-11) |
| Review cycle | Every August with the risk assessment, and after a new client, a new service, a subcontractor change, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, RA-2, RA-3, CA-2, SA-9, PS-7, AC-2, AC-3, AC-17, AC-6, AC-11, AC-21, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-8, SC-28, MP-3, MP-4, MP-6, CP-2, CP-9, SI-2, SI-3, SI-12, AT-2, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, PR.IR-01, PR.PS-02, ID.AM-07, ID.AM-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Rules it carries out | 49 CFR 1520.9, 1520.11, 1520.13, 1520.19 (SSI); Client A supplier addendum s.2 to s.14; Fla. Stat. 501.171(2) |

## 1. Purpose
Protect client pipeline data, Client A's Sensitive Security Information (SSI), and the business's own records, and meet the SSI rules and client contracts in a way that one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All information the business holds in any form (electronic, paper, spoken): client data, SSI, deliverables, and business and subcontractor records. It covers every system in the Core Business SaaS Stack (SYS-01 to SYS-05, SYS-07, SYS-08), paper in the home office, and every service or person the business shares data with. It applies to the engineer-owner and to any future employee. Subcontractors are bound through their written terms (6.2).

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead and SSI custodian | Engineer-owner | Runs this policy; keeps the SSI register; decides incident and notice questions; keeps records |
| Risk acceptor | Engineer-owner | Accepts or treats every risk (4.4) |
| Subcontractors | GIS and field subcontractors | Follow their security terms; report incidents to the owner within 24 hours |
| On-call IT support contractor | Contractor under NDA | Technical help on request; no standing access; never given SSI |

Because one person writes, follows, and checks these rules, independence is limited. Rule 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The engineer-owner is designated by this policy as the security lead and the custodian of all SSI the business holds. SSI duties under 49 CFR Part 1520 continue after an engagement ends (1520.7(k)). (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every August and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every August (P07). At least every second year, the evaluation must include review by someone outside the business, such as the IT support contractor under NDA. (CA-2)
4.6 This policy must be reviewed every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Exceptions and enforcement
5.1 Any future employee must be trained before getting access and is subject to discipline, up to termination, for breaking this policy.
5.2 A subcontractor or service that breaks its terms must be dealt with under its contract, up to ending it. The owner must tell the affected client when the breach involves its data.
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. No exception may allow SSI to be shared without a need to know or allow client data into a service the client has not approved. (PL-1)

## 6. Clients, subcontractors, and services
6.1 **Approved services only.** Client data may be stored or processed only in services listed in the approved-services list for that client. Client A data requires Client A's written approval of each service, including any AI tool. Today's list: the productivity suite, the engineering software on the laptop, and each client's own portal. (SA-9; GV.SC-05; Client A addendum s.4)
6.2 **Subcontractors.** A subcontractor may receive client data only after (a) the client approves the subcontractor in writing where the contract requires it, and (b) the subcontractor signs short security terms: MFA on the account used for client data, an encrypted device, no forwarding, deletion at task end, and incident notice to the owner within 24 hours. Subcontractors never receive SSI. (SA-9; PS-7; Client A addendum s.5)
6.3 The owner must keep a vendor list showing each service, the data it holds, and its agreement, and must review the productivity suite provider's SOC 2 report every year. (SA-9; GV.SC-07; ID.AM-07)
6.4 Remote IT support sessions must be started and watched by the owner. No remote support tool may stay installed with unattended access. (AC-17)
6.5 Answers to client security questionnaires must be supported by a document or setting the owner can show. (Client A addendum s.11)

## 7. Access control
7.1 Every account must belong to one person. Credentials must never be shared. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every account that holds client data, SSI, or personal information: the productivity suite, the accounting SaaS, the password manager, and any approved service. (IA-2(1); IA-2(2); PR.AA-03; Client A addendum s.2)
7.3 Passwords must be unique passphrases of at least 16 characters, stored in a password manager. (IA-5)
7.4 **Sharing.** Anonymous ("anyone with the link") sharing must stay off. Files go to named external accounts that must sign in, only the extract the task needs, and the share is removed when the task ends. (AC-3; AC-21; PR.AA-05)
7.5 Daily work must use a standard laptop account and a standard suite account. Administrator accounts are used only to change settings or install software. (AC-6)
7.6 The laptop must lock after 5 minutes idle and the phone after 1 minute. (AC-11)
7.7 **Emergency access.** Recovery codes for the suite, the accounting SaaS, and the password manager, plus a one-page emergency sheet, must be kept in a sealed envelope held by the owner's attorney. A second MFA method (hardware key) must be registered for the suite and the password manager. (AC-2; CP-2)
7.8 On the first working day of each month, the owner must review suite sign-ins, external shares, and access to the SSI folder, and record the review. (AU-6; DE.AE-02)

## 8. Data handling and SSI
8.1 Information is classified in four levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **SSI** | Client A plan excerpt, zone drawing, any draft that quotes them | Rules 8.2, 8.3, 8.6, 8.7, 8.8 |
| **Client Confidential** | ILI results, GIS, historian exports, integrity records, deliverables | Approved services only (6.1); encrypted; returned or destroyed at project end (8.8) |
| **Business Confidential** | W-9s, bank details, contracts, security records | Accounting SaaS or the suite only; encrypted; MFA |
| **Public** | Published reports, website | No restriction |

8.2 **SSI storage.** SSI must be kept only in the dedicated SSI folder in the suite, shared with no one, and on the encrypted laptop. SSI must never go on removable media, into an AI tool, to a personal email address, or to a subcontractor. Every SSI record and copy must be listed in the SSI register. (AC-3; MP-4; 1520.9(a)(1)-(2))
8.3 **Marking.** SSI must carry the protective marking and the distribution limitation statement of 49 CFR 1520.13, including any draft or note that quotes SSI. If unmarked SSI arrives, the owner must mark it and tell the sender the same day. (MP-3; 1520.9(a)(4); 1520.9(b))
8.4 Client data must move only through named suite shares or the client's own portal or file transfer site. Client data must not be sent as an attachment to a personal email address. (SC-8; PR.DS-02)
8.5 Every device and every removable drive that can hold client data must be encrypted. (SC-28; PR.DS-01; Client A addendum s.3)
8.6 Paper SSI must be printed only when needed and kept in the locking file cabinet when not in the owner's hands. (MP-4; PR.AA-06; 1520.9(a)(1))
8.7 Any request for SSI from anyone other than Client A must be referred to Client A's security contact and to TSA. Nothing is released. (1520.9(a)(3))
8.8 **Project close-out.** Within 30 days after a project ends, the owner must return or destroy the client's source data and, where the contract requires it, send a destruction certificate. SSI must be destroyed completely: cross-cut shredding for paper; deletion with the suite recycle bin and version history purged for files. Each step is recorded. Sealed deliverables are kept as professional records. (SI-12; MP-6; ID.AM-08; 1520.19(b); Client A addendum s.7)
8.9 **Backups.** Local working files must be copied weekly to a hardware-encrypted drive that is disconnected after each copy and kept in the locked cabinet. A restore of one project folder must be tested every quarter. SSI is excluded from this drive (8.2). (CP-9; PR.DS-11; Client A addendum s.13)
8.10 W-9 forms must be kept only in the accounting SaaS and deleted when tax records no longer require them. Security records (this policy, risk assessments, assessments, incident records, certificates) must be kept at least 5 years. (SI-12; Fla. Stat. 501.171(2))

## 9. Acceptable use and training
9.1 Work devices are for work only. Household members must not use them. (PL-4)
9.2 Household devices must use the router's guest network. The router must have a unique admin password and current firmware. (SC-7; PR.IR-01)
9.3 Automatic updates and the built-in antivirus must stay on. Software must come only from official app stores or the vendor's site. (SI-2; SI-3; PR.PS-02)
9.4 Work devices must never be left in a vehicle or unattended at a client site.
9.5 **AI tools.** An AI tool may process client data only after a written P10 assessment, the client's written approval (6.1), and business terms that bar training on the data. SSI and personal information must never go into an AI tool. AI outputs are advisory: the owner checks every finding against the source data and signs every deliverable. (PL-4; SA-9)
9.6 The owner must complete a security course and an SSI awareness module every year. (AT-2; PR.AT-01; Client A addendum s.12)

## 10. Incident response
10.1 The business must keep an incident runbook (P08) with a printed contact list in the home office and the contacts in the phone. (IR-8; RS.MA-01)
10.2 Every suspected incident (lost device, phishing click, wrong recipient, odd sign-in, subcontractor report) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 Client A must be notified within 24 hours and Client B within 72 hours after discovery of any suspected incident affecting their data or access. Client C is told without delay. (IR-6; RS.CO-02; Client A addendum s.6)
10.4 If SSI may have been released to anyone without a need to know, the owner must promptly inform TSA, coordinated with Client A. (IR-6; 1520.9(c))
10.5 Notices to individuals and the Florida Department of Legal Affairs must meet the deadlines in the P08 notification matrix, confirmed by counsel. (IR-6; Fla. Stat. 501.171)
10.6 The insurer's breach hotline must be called before hiring any outside firm. No ransom may be paid without counsel's advice and an OFAC sanctions check. (IR-4)
10.7 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-8; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner must keep a written arrangement with a peer pipeline integrity engineer to take urgent client calls if the owner is unavailable. Client data is shared with the peer only after the client approves in writing. (CP-2)
11.3 Each client's integrity engineer must have the escalation path for urgent findings (P05 BP-01).
11.4 When a hurricane watch is issued, the laptop, the encrypted backup drive, and the SSI cabinet contents (or their destruction) must be dealt with before leaving the home office.

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the monthly review in 7.8.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Data locations
| Item | Data held | Protection required |
|---|---|---|
| Laptop | Working client files, SSI working copies | 7.5, 7.6, 8.5, 9.3 |
| Phone | MFA prompts, field photos until uploaded | 7.6, 8.5 |
| Productivity suite | Client files, SSI folder, email | 7.2, 7.4, 8.2 |
| Accounting SaaS | Invoices, W-9s | 7.2, 8.10 |
| Encrypted backup drive | Weekly copy of non-SSI working files | 8.5, 8.9 |
| Locking file cabinet and fire safe | Paper SSI and the encrypted backup drive (cabinet); ILI vendor drives until returned (fire safe) | 8.6, 8.9 |
