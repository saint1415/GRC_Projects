# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (engineering subcontractor handling CUI drawings) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new system, a new contract clause, a hire or helper, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PL-4, PS-4, RA-2, RA-3, RA-5, CA-2, CA-5, SA-9, AC-2, AC-3, AC-6, AC-6(2), AC-7, AC-8, AC-11, AC-19, AC-20, AC-22, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-8, SC-13, SC-28(1), CP-2, CP-9, MP-3, MP-4, MP-6, MP-7, PE-3, PE-8, PE-17, CM-2, CM-6, CM-7, CM-11, MA-2, SI-2, SI-3, SI-5, SI-12, AT-2, AT-3, IR-3, IR-4, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-07, ID.AM-01, ID.AM-07, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.AT-02, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-01, PR.PS-02, PR.IR-01, DE.AE-02, RS.MA-01, RS.CO-02, RC.RP-01 |
| Contract and regulatory basis | DFARS 252.204-7012 (NIST SP 800-171 Rev. 2); DFARS 252.204-7019, 252.204-7020, 252.204-7021; 32 CFR Part 170; FAR 52.204-21; ITAR (22 CFR 120.50, 120.54, 120.56) |

## 1. Purpose
Protect Controlled Unclassified Information (CUI), federal contract information (FCI), and customer data, and meet NIST SP 800-171 Rev. 2 as the Prime A subcontract requires, in a way one person working from home can run. Each rule is written so it can be checked (P07). Where a rule closes an SP 800-171 requirement, the requirement number is given in brackets.

## 2. Scope
All business information in any form (electronic, paper, spoken) on every system in the Engineering Office Systems (SYS-01 to SYS-08 and SYS-10), on paper in the home office, and at every provider that handles it. It applies to the owner and to anyone the owner ever lets help with the business. Household members are not users and are treated as visitors.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead, CUI and export compliance lead, incident handler | Owner | Runs this policy; decides incident and reporting questions; keeps records |
| Risk acceptor and CMMC Affirming Official | Owner | Accepts or treats every risk (4.4); signs SPRS entries and affirmations only with evidence (4.7) |
| IT consultant | Contractor | Hands-on help on site with the owner present; no account left behind (6.4) |
| CMMC consultant | Contractor | Outside review of the self-assessment and SPRS entries; sees no CUI |
| Providers | SYS-10 provider, accounting SaaS vendor, internet service provider | Operate their safeguards as listed in their terms or CRM |

Because one person writes, follows, and checks these rules, independence is limited. Rule 4.5 adds an outside check.

## 4. Governance and risk
4.1 The business must keep a security program documented in this policy, the SSP (P02), and the risk register (P01), covering every system that processes, stores, or transmits CUI or FCI. (PM-1; GV.PO-01) [3.12.4]
4.2 The owner is designated by this policy as security lead, CUI and export compliance lead, and Affirming Official. (PM-2; GV.RR-02)
4.3 CUI may be processed, stored, or transmitted only on the systems listed in Appendix A. The SSP must be updated **before** any system, service, or location is added or changed. (PL-2; CM-2) [3.12.4; 3.4.1]
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; RA-3; GV.RM-01) [3.11.1]
4.5 A self-assessment against NIST SP 800-171A must be done every year and before each SPRS entry or CMMC affirmation. The CMMC consultant must review it before it is posted. (CA-2; ID.RA-01) [3.12.1]
4.6 Every requirement not met must be on the POA&M with a date; the POA&M is reviewed monthly. (CA-5) [3.12.2; 3.12.3]
4.7 **Honest reporting.** No SPRS score, date-to-110, or CMMC affirmation may be submitted unless the evidence supports it. If the business cannot meet a contract requirement by a deadline, the owner tells Prime A in writing instead. (CA-2; GV.PO-01)
4.8 One person holds every duty, so duties cannot be separated. This is an enduring exception recorded in the SSP; the compensating measure is the outside review in 4.5. (PL-1) [3.1.4]
4.9 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Exceptions and consequences
5.1 Any departure from this policy must be written down with the reason, the risk level under 4.4, the compensating measure, and an end date within 12 months, and recorded in the risk register. (PL-1)
5.2 A helper or provider that breaks this policy or its contract loses access the same day, and the contract may be ended. (SA-9; PS-4)
5.3 Exception records and all records required by this policy must be kept 6 years from creation (the same period 32 CFR 170.16(c)(4) requires for assessment artifacts). (SI-12)

## 6. Providers and external systems
6.1 **Only approved external systems may hold CUI:** the Prime A portal and SYS-10. Any cloud service that would store, process, or transmit CUI must be FedRAMP authorized at Moderate or higher, or meet equivalent requirements, and its customer responsibility matrix must be referenced in the SSP. (SA-9; AC-20; GV.SC-05) [3.1.20; DFARS 252.204-7012(b)(2)(ii)(D)]
6.2 The owner must keep a provider list showing each provider, what data it holds (CUI, FCI, other), and its assurance evidence, and review it every July. (SA-9; GV.SC-07)
6.3 No CUI may be sent to anyone other than Prime A without a written flowdown of DFARS 252.204-7012 and Prime A's approval. (SA-9) [DFARS 252.204-7012(m)(1)]
6.4 Helpers work on site with the owner present. No remote-support tool may be installed. Any account created for a helper must be removed the day the work ends. (AC-2; MA-2; PS-4) [3.7.2; 3.7.6; 3.9.2]
6.5 Nothing may be posted on the public website or social media about Prime A work without checking it against the CUI markings and Prime A's written approval. (AC-22) [3.1.22]

## 7. Access control
7.1 Only the owner is an authorized user. Authorized users and devices are listed in the SSP. Credentials are never shared with household members. (AC-2; IA-2; PR.AA-01) [3.1.1; 3.5.1]
7.2 Daily work must be done in a standard user account. The administrator account is used only to install approved software or change settings. (AC-6; AC-6(2); PR.AA-05) [3.1.5; 3.1.6; 3.13.3]
7.3 MFA is required for every service that holds CUI or FCI and for administrator sign-in on the laptop. SYS-10 uses hardware security keys, with a spare key in the home safe. (IA-2(1); IA-2(2); PR.AA-03) [3.5.3]
7.4 Passwords must be unique passphrases of at least 14 characters, kept only in the password manager. Passwords must never be stored in files, notes, or spreadsheets. Default passwords on any device must be changed before first use. (IA-5) [3.5.7; 3.5.8; 3.5.10]
7.5 The laptop locks after 5 minutes idle and after 10 failed sign-in attempts; the phone locks after 1 minute. The laptop shows a CUI notice at sign-in. (AC-11; AC-7; AC-8) [3.1.8; 3.1.9; 3.1.10]
7.6 CUI may be opened only on the laptop. The phone may hold the MFA app and non-CUI email only. (AC-19; PR.AA-05) [3.1.18; 3.1.19]
7.7 On the first working day of each month the owner reviews SYS-10 (until migration, SYS-01) sign-ins and downloads, the laptop security log, and the router log, and records the review on the monthly checklist. (AU-6; DE.AE-02) [3.3.5; 3.14.7; 3.12.3]
7.8 Accounts not used for 90 days are disabled; accounts are checked every quarter. (AC-2) [3.5.6]

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **CUI** | Prime A drawings and models; the owner's derived work; ITAR-marked data | Appendix A systems only; encrypted; marked; never to foreign persons |
| **Confidential** | FCI (task orders, invoices); commercial customer data under NDA; credentials | Encrypted storage; MFA; owner only |
| **Public** | Website, published brochures | No restriction |

8.2 Files derived from CUI and every medium holding CUI (including the backup drive and printouts) must carry the markings Prime A instructs. (MP-3) [3.8.4]
8.3 Every device or medium that can hold CUI must use FIPS-validated encryption in an approved mode. Recovery keys are kept in the home safe, never with the data. (SC-13; SC-28(1); PR.DS-01) [3.13.11; 3.13.16; 3.13.10; 3.8.6]
8.4 CUI moves only through the Prime A portal or SYS-10, never by ordinary email, text, or consumer file-sharing. (SC-8; PR.DS-02) [3.13.8; 3.1.3]
8.5 The only removable medium allowed is the owner's encrypted backup drive. It is connected only to the laptop and kept in the home safe between backups. (MP-4; MP-7) [3.8.7; 3.8.9; 3.1.21]
8.6 A full backup is made weekly and a restore is tested every quarter. Project files are kept in SYS-10 with version history. (CP-9; PR.DS-11)
8.7 Paper CUI is kept in a locked cabinet when not in use and destroyed in the cross-cut shredder. Devices and media are sanitized under NIST SP 800-88 Rev. 2 before disposal or reuse, or destroyed by a recycler that gives a certificate. Printer storage is cleared before the printer leaves the house. Each disposal is recorded. (MP-6; ID.AM-08) [3.8.3]
8.8 **Export control.** ITAR-marked or EAR-controlled technical data must never be shown, sent, or described to a foreign person, and must be stored only where the conditions of 22 CFR 120.54(a)(5) or 15 CFR 734.18(a)(5) are met or the data never leaves U.S.-person control. (AC-3; SC-13)

## 9. Acceptable use, physical security, and training
9.1 The laptop is for business work only. Family members must not use it. Software comes only from the approved list, installed from the vendor's site or app store. (PL-4; CM-11) [3.4.9]
9.2 CUI work is done only in the home office or at Prime A. Never in public places, and the laptop is never left in a vehicle. During a storm evacuation the laptop stays with the owner. (PE-17) [3.10.6; 3.8.5]
9.3 The home office is locked whenever anyone other than the owner is in the house. The only keys are the owner's and one in the home safe. (PE-3; PR.AA-06) [3.10.1; 3.10.2; 3.10.5]
9.4 Every visitor to the office, including household members, the cleaning service, and the IT consultant, is escorted by the owner after CUI is locked away, and recorded in the visitor log (name, date, time in and out, purpose). The log is kept one year and reviewed monthly. (PE-8) [3.10.3; 3.10.4]
9.5 The laptop and printer use the business network only. Household devices and guests use their own network. UPnP and remote administration are off on the router. (SC-7; CM-7; PR.IR-01) [3.13.1; 3.1.16; 3.4.7]
9.6 **AI tools.** CUI, FCI, and customer data under NDA must never be entered into a commercial AI tool. An AI tool may be used with CUI only if it runs inside an approved system under 6.1, has a written P10 assessment, and is approved by the owner in writing. AI output is never the source for a dimension, tolerance, or material callout. (PL-4; AC-20; SA-9) [3.1.20]
9.7 Automatic updates and antivirus stay on. Security updates are installed within 30 days (critical ones within 7). The owner subscribes to security alerts from CISA and from the CAD, router, and printer vendors, and scans the laptop for vulnerabilities monthly. (SI-2; SI-3; SI-5; RA-5; PR.PS-02) [3.14.1; 3.14.3; 3.11.2; 3.11.3]
9.8 The owner completes security awareness, CUI handling, and insider threat training every year and keeps the certificates. (AT-2; AT-3; PR.AT-01; PR.AT-02) [3.2.1; 3.2.2; 3.2.3]
9.9 Each device follows a one-page baseline of settings kept with the SSP; any change is entered in the change log first. (CM-2; CM-6; PR.PS-01) [3.4.1 to 3.4.4]

## 10. Incident response
10.1 The business keeps an incident runbook (P08) with a printed contact list in the home office and in the home safe. (IR-8; RS.MA-01) [3.6.1]
10.2 Every suspected incident (phishing click, unusual sign-in alert, lost device, CUI sent to the wrong place, CUI entered into an unapproved service) must be entered in the incident log the same day, with the time it was discovered. (IR-6; RS.MA-02) [3.6.2]
10.3 If a cyber incident may affect CUI or a covered system, the owner must review it for compromise and report it to DoD at https://dibnet.dod.mil **within 72 hours of discovery**, using the medium assurance certificate, then give the incident report number to Prime A as soon as practicable. (IR-6; RS.CO-02) [DFARS 252.204-7012(c), (m)(2)(ii)]
10.4 Images of affected systems and relevant logs must be preserved for at least 90 days from the report, and malware is sent only to DC3. (IR-4) [DFARS 252.204-7012(d), (e)]
10.5 A possible release of ITAR or EAR data to a foreign person is referred to export counsel the same day to decide on a voluntary disclosure (22 CFR 127.12; 15 CFR 764.5). (IR-6)
10.6 No ransom or extortion payment may be made without legal counsel's advice and an OFAC sanctions check. (IR-4)
10.7 The runbook is walked through every year and after any real incident. Lessons learned are recorded within 30 days of closing an incident. (IR-3; ID.IM-02) [3.6.3]

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner keeps a written continuity arrangement with Prime A for pausing or reassigning task orders, and sealed MFA recovery codes and an emergency sheet in the home safe. (CP-2)

## 12. Compliance
Compliance is checked by the monthly checklist (7.7), the annual self-assessment (4.5), and P07. Exceptions follow section 5.

## 13. Related documents
P01 risk register; P02 SSP; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Approved locations for CUI
| Location | CUI allowed | Protection required |
|---|---|---|
| Engineering laptop (SYS-02) | Yes | 7.2, 7.3, 7.5, 8.3, 9.1 |
| Government-community cloud suite (SYS-10), from go-live | Yes | 6.1, 7.3, 8.4 |
| Prime A portal (SYS-06) | Yes (Prime A's system) | 7.3 |
| Encrypted backup drive | Yes | 8.3, 8.5 |
| Printer and scanner (SYS-08), business network | Print and scan jobs only | 8.7, 9.5 |
| Locked cabinet in the home office | Paper CUI | 8.7, 9.3 |
| Commercial productivity suite (SYS-01) | **No** after 2026-11-30 (until then, transition only) | 6.1 |
| Phone (SYS-03), AI chatbot (SYS-09), any personal account | **No** | 7.6, 9.6 |
