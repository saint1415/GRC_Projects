# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (electronics and device repair service) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-technician |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new system, a new contractor or hire, a new service line, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-6, PT-5, RA-2, RA-3, CA-2, SA-9, AC-2, AC-3, AC-6, AC-11, AC-18, AC-19, AU-6, IA-2, IA-2(1), IA-5, CM-7, SC-7, SC-28, CP-2, CP-9, MP-6, PE-3, SI-2, SI-3, SI-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-04, GV.SC-05, GV.SC-06, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.DS-01, PR.DS-10, PR.PS-05, PR.IR-01, ID.AM-07, ID.AM-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Laws and contracts | FTC Act Section 5 (15 U.S.C. 45(a)(1), 45(n)); Fla. Stat. 501.171(2)-(6), (8); PCI DSS v4.0.1 SAQ P2PE (merchant agreement) |

## 1. Purpose
Protect customers' devices and data, the shop's own records, and card payments, in a way one person can actually run. Customers hand over their phones and their passcodes; this policy says what the shop does with them and what it never does. Each rule is written so it can be checked (P07).

## 2. Scope
All information the shop handles in any form (electronic, paper, spoken), including customer devices while they are in the shop's custody and any data copied from them, on every system in the Service Ticketing and Point-of-Sale System (SYS-01 to SYS-12). It applies to the owner-technician, the fill-in technician, and any future employee. Other contractors and vendors are bound through their contracts.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security and privacy lead, incident lead | Owner-technician | Runs this policy; decides breach questions; keeps records |
| Risk acceptor | Owner-technician | Accepts or treats every risk (4.4) |
| Fill-in technician | Independent contractor | Follows sections 7 to 10 while covering the shop; signs an acknowledgment of this policy |
| Independent security consultant | Contractor | Outside check at the annual review when engaged (4.5) |
| Vendors | Ticketing and POS vendor, payment processor, SaaS providers, recycler | Operate their safeguards; give breach notice under their terms and Fla. Stat. 501.171(6) |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The shop must keep a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The owner-technician is designated in writing, by this policy, as the security and privacy lead and incident lead. (PM-2; GV.RR-02)
4.3 A risk assessment must be done every July and after any major change, using NIST SP 800-30 Rev. 1. Every risk is recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-01)
4.5 Controls must be self-assessed every July (P07). At least every second year the assessment must include someone outside the shop, such as the independent security consultant. (CA-2)
4.6 This policy must be reviewed at least every 12 months and after major changes or incidents. (PL-1; GV.PO-02; PCI DSS 12.1.2)

## 5. Contractors and exceptions
5.1 The fill-in technician and any future worker must sign an acknowledgment of this policy and a confidentiality agreement before getting access to customer devices or SYS-01. (PS-6; GV.RR-04; PCI DSS 12.1.3)
5.2 A contractor who breaks this policy or the agreement is dealt with under the agreement, up to ending it, and any breach question is handled under section 10.
5.3 The owner must record any personal departure from this policy as an exception under 5.4, with the reason and the fix.
5.4 **Exceptions and changes** are recorded in the security log with a risk rating under 4.4 and must expire within 12 months. Adding a new SaaS service, tool, or AI feature is a change and is logged. (PL-1; ID.RA-07)

## 6. Vendors and contractors
6.1 **No terms, no customer data.** No vendor or contractor may receive customer data until its terms cover confidentiality, use only for the shop's purpose, no training of AI models on the shop's data, deletion at the end, and breach notice to the shop. (SA-9; GV.SC-05; Fla. Stat. 501.171(6))
6.2 The owner must keep a vendor list showing each vendor, the data it holds, its breach notice term, and whether it handles card data. The payment processor is the only provider that handles account data. (SA-9; GV.SC-04; PCI DSS 12.8.1, 12.8.5)
6.3 Before using a new service, the owner checks its terms (training, retention, MFA, breach notice) and, for a payment provider, its PCI DSS status. Each year the owner reads the ticketing vendor's SOC 2 report and checks that the P2PE solution is still on the PCI SSC list. (SA-9; GV.SC-06; GV.SC-07; PCI DSS 12.8.3, 12.8.4)
6.4 When a vendor or contractor relationship ends, the owner removes its access, asks for deletion of shop data, and keeps the reply. (SA-9; GV.SC-10)

## 7. Access control
7.1 Every person has their own account. **No shared logins.** The fill-in technician uses a named SYS-01 account that is disabled at the end of each cover period. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every service that holds customer data or money and offers it: SYS-01, the productivity suite, accounting, bank, processor portal, and camera app. (IA-2(1); PR.AA-03)
7.3 Passwords are unique passphrases of at least 14 characters kept in the password manager. Default passwords (router, new devices) are changed before use. (IA-5)
7.4 The fill-in account has no export, settings, or report rights. The owner reviews SYS-01 users and active sessions each quarter and ends any session that is not expected. (AC-2; AC-6; PR.AA-05)
7.5 The laptop and bench PC lock after 5 minutes; the tablet after 2 minutes; the phone after 1 minute. (AC-11)
7.6 **Emergency access.** Recovery codes for SYS-01, email, and the processor portal, and a one-page device-return procedure, are kept in a sealed envelope held by the owner's designated emergency contact. (AC-2; CP-2)
7.7 On the first Tuesday of each month the owner reviews SYS-01 sign-ins and exports, the email and processor sign-in histories, and the router's connected-device list, and notes the review in the security log. SYS-01 sign-in alerts go to the owner's phone. (AU-6; DE.AE-02)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Device passcodes, account passwords, customer device content and copies, card numbers | Collected only when the repair needs it; kept only as long as 8.5 to 8.8 allow; encrypted |
| **Confidential** | Customer contact details and repair history, intake photos, contracts, tax and bank records | Approved systems only (Appendix A); MFA; owner and fill-in technician only |
| **Public** | Prices, hours, website | No restriction |

8.2 Restricted and Confidential data may be kept only in the systems listed in Appendix A. Never in a personal account, a consumer app, or the phone's camera roll after the day of intake. (AC-3; SA-9)
8.3 **Passcodes and passwords.** Device passcodes go only in the SYS-01 restricted passcode field, which is cleared at release, never in free-text notes or on paper tags. The shop does not ask for account passwords; when an account sign-in is needed, the customer enters it in person. (SI-12; PR.DS-01)
8.4 **Customer device access rules.** A technician may open on a customer device only what the repair or the requested transfer needs (for example the camera app to test a new camera, or a test call). A technician must never browse, read, copy, photograph, or keep customer content, and must not connect a customer device to any personal account. Data transfers copy whole data sets with the transfer tool; the technician does not open the files. Breaking this rule is a possible breach under Fla. Stat. 501.171(1)(a) and is handled under section 10. (AC-3; PR.DS-10; 15 U.S.C. 45(n))
8.5 **Transfer and recovery copies** are kept only on encrypted storage (the bench PC and hardware-encrypted drives) and are deleted 14 days after the customer confirms delivery, or 30 days after the job closes if the customer does not answer. Each deletion is logged by ticket number. (SI-12; SC-28; Fla. Stat. 501.171(8))
8.6 **Sanitization method.** Storage that held customer data is sanitized using NIST SP 800-88 Rev. 2: the clear method (3.1.1) for normal reuse of the shop's own drives, the purge method (3.1.2), such as cryptographic erase, where the device supports it, and destruction (3.1.3) through the certified recycler for devices that cannot be sanitized. Each sanitization is verified (4.5.1). (MP-6; ID.AM-08)
8.7 **Recycling drop-off devices** get a per-device record (serial number, method, verification, date) modeled on the SP 800-88 Rev. 2 Appendix C certificate, before they go into the recycler's bin. Devices that cannot be sanitized are marked "destroy" for the recycler. (MP-6; Fla. Stat. 501.171(8))
8.8 **Card data.** Card numbers are entered only into the P2PE terminal. Phone payments are keyed while the caller waits. Card numbers and security codes are never written down, typed into SYS-01, or sent by text or email. Any paper with card data found in the shop is cross-cut shredded the same day. (PCI DSS 3.1.1, 3.2.1, 3.3.1.2, 9.4.6; SAQ P2PE eligibility)
8.9 Paper intake forms are kept one year in the locked cabinet and then cross-cut shredded. Security records (this policy, risk assessments, incident and deletion logs) are kept at least 5 years. (SI-12; Fla. Stat. 501.171(4)(c))

## 9. Acceptable use and training
9.1 Shop devices are for shop work. Family members and customers must not use them. (PL-4)
9.2 **Bench rules.** The bench screen faces away from the counter. The bench camera shows hands and the bench, not device screens. Customer drives are scanned with the antivirus before any file is opened. Daily bench work uses a standard (non-administrator) account. (PL-4; PR.DS-10)
9.3 Automatic updates and antivirus stay on. Software comes only from the publisher or the parts supplier, never from forum links. The approved bench tool list is in Appendix A. (SI-2; SI-3; CM-7; PR.PS-05)
9.4 **Payment terminal.** The terminal is listed in Appendix A, inspected each Tuesday at opening using the PIM checks, logged, and locked in the cabinet overnight. Anyone claiming to service the terminal is verified with the processor first. (PE-3; PCI DSS 9.5.1, 9.5.1.1, 9.5.1.2, 9.5.1.3)
9.5 **Network.** Customers use the guest Wi-Fi. Customer devices under repair use the separate bench network. Shop devices and the terminal stay on the main network. (SC-7; AC-18; PR.IR-01)
9.6 The owner completes a small-business security course and a phishing refresher every year and reads the PIM. The fill-in technician is briefed on this policy before each cover period. Supplier bank-detail changes are confirmed by phone at a known number. (AT-2; PR.AT-01; PCI DSS 12.6.1)
9.7 **AI tools.** An AI tool may be used for shop work only after a written assessment (P10) and only on terms with no model training on the shop's data. No customer names, contact details, passcodes, account details, or photos showing personal content may be entered into any AI tool. A technician confirms every AI diagnostic suggestion before quoting. (PL-4; SA-9)
9.8 Customer-facing statements about privacy, wiping, or AI must be true and supported by records. The intake notice says what access a repair needs and what never happens. (PT-5; 15 U.S.C. 45(a)(1))

## 10. Incident response
10.1 The shop keeps an incident runbook (P08) with a printed contact list at the counter and at home. (IR-8; RS.MA-01; PCI DSS 12.10.1)
10.2 Every suspected incident (unexpected sign-in, lost drive, customer complaint about data, tampered terminal, phishing click) is written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 The processor is told within 24 hours of suspecting a card data compromise (merchant agreement term). (IR-6; RS.CO-02)
10.4 Notices to customers and the Florida Department of Legal Affairs must meet the deadlines in the P08 notification matrix, confirmed by counsel. Customers in other states are notified under their own states' laws. (IR-6; RS.CO-02; Fla. Stat. 501.171(3)-(5))
10.5 No ransom or extortion payment may be made without counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook is walked through every year and after any real incident. Lessons are recorded within 30 days of closing an incident. (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The fill-in technician is the backup for releasing devices, using the device-return procedure in the sealed envelope. The custody list is printed every Saturday evening. (CP-2)
11.3 **Storm procedure.** When a hurricane watch is issued, the owner texts customers to collect finished devices, moves the rest into the cabinet off the floor, and takes the laptop and encrypted drives home. (CP-2; PR.IR-02)
11.4 SYS-01 customer data is exported monthly to the productivity suite, and open recovery jobs get a second encrypted copy that is deleted with the job (8.5). (CP-9; PR.DS-11)

## 12. Compliance
Compliance is checked in the annual self-assessment (P07) and the monthly review in 7.7. Contractor breaches follow section 5.

## 13. Related documents and obligations
P01 risk register; P02 system profile; P03 gap analysis (obligations: FTC Act Section 5, Fla. Stat. 501.171, PCI DSS v4.0.1 SAQ P2PE, merchant agreement); P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Devices, data locations, and approved tools
| Item | Data held | Protection required |
|---|---|---|
| SYS-01 ticketing and POS | Customer records; passcodes in the restricted field until release | 7.1, 7.2, 8.3 |
| P2PE terminal (make, model, and serial number recorded on the printed copy kept in the cabinet) | Card data, encrypted | 8.8, 9.4 |
| Productivity suite | Email, files, monthly SYS-01 export | 7.2; version history |
| Accounting SaaS and bank | Invoices and payments | 7.2 |
| Owner laptop | Cached email and files | Encryption; 7.5 |
| Bench PC and 2 hardware-encrypted transfer drives | Transfer and recovery copies | Encryption; 7.5; 8.5 |
| Counter tablet and owner phone | Cached tickets; intake photos for one day | Passcode; 7.5; 8.2 |
| Camera cloud | Video, 30 days | 7.2; 9.2 |
| Website builder | Booking requests, deleted after 90 days | 7.2 |
| Approved bench tools | Device makers' own transfer and diagnostic tools; tools bought from the parts supplier; the operating system's disk and encryption tools | 9.3 |
