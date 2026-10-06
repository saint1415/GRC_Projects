# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (residential real estate brokerage) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Broker-owner |
| Effective date | 2026-09-15 (adopted 2026-09-15) |
| Review cycle | Every August with the risk assessment, and after a new system, a new contractor, a first hire or affiliated sales associate, a new line of service, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, CA-2, RA-2, RA-3, SA-9, AC-2, AC-3, AC-11, AC-19, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, CM-3, SC-7, SC-8, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, AT-2(3), IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-07, ID.AM-01, ID.AM-07, ID.AM-08, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, PR.PS-01, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Rules served | Fla. Stat. 501.171(2), (6), (8); Fla. Stat. 475.25(1)(k) and (1)(d)1.; Fla. Admin. Code ch. 61J2-14; Fla. Stat. 475.5015; 15 U.S.C. 45(a); 15 U.S.C. 1681m(a); 16 CFR 682.3. 16 CFR 314.3-314.4 used as the benchmark (P03) |

## 1. Purpose
Protect clients' money and personal information, keep the brokerage's escrow duties, and do it in a way one broker can actually run. Every rule below is written so it can be checked (P07). This policy is the brokerage's written security program (benchmark 16 CFR 314.3(a)).

## 2. Scope
All brokerage information in any form (electronic, paper, spoken), including client personal information, payment and wire instructions, and consumer reports, on every system in the TMCC (SYS-01 to SYS-09), in the external services SYS-10 and SYS-11, in paper files in the home office, and at every contractor and vendor that handles it. It applies to the broker-owner and to any future employee or affiliated sales associate. Contractors are bound through their written terms (section 6).

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead (benchmark Qualified Individual) and privacy contact | Broker-owner | Runs this policy; decides breach and notice questions; keeps records |
| Broker and escrow signatory | Broker-owner | Escrow duties under Fla. Stat. 475.25 and ch. 61J2-14 |
| Risk acceptor | Broker-owner | Accepts or treats every risk (4.4) |
| Freelance transaction coordinator | Contractor | Follows sections 7 to 9 under the engagement terms in 6.2 |
| Outside bookkeeper | Contractor | Prepares the escrow reconciliation; follows 6.2 |
| On-call IT technician | Contractor | Technical help on request; settings review every second year (4.5) |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The brokerage must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01; 501.171(2))
4.2 The broker-owner is designated in writing, by this policy, as the brokerage's security lead (the benchmark "Qualified Individual") and privacy contact. (PM-2; GV.RR-02; benchmark 314.4(a))
4.3 A risk assessment must be completed every August and after any change listed in the review cycle, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9; benchmark 314.4(b))
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. A risk to client funds rated High is never accepted. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every August (P07). At least every second year, the IT technician must check the settings independently. (CA-2; benchmark 314.4(d)(1))
4.6 This policy must be reviewed at least every year and after major changes or incidents. The website security statement must be checked at the same time so it stays accurate. (PL-1; GV.PO-02; 15 U.S.C. 45(a); benchmark 314.4(g))

## 5. Sanctions and exceptions
5.1 A contractor that breaks this policy or its engagement terms is dealt with under those terms, up to ending the engagement. Any future employee or affiliated sales associate who breaks it receives retraining, a written warning, or termination of the relationship, in proportion to intent and harm, documented and kept for 5 years. (PL-4; SA-9)
5.2 The owner must record any personal departure from this policy as an exception under 5.3, with the reason and the fix.
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. No exception is allowed to rule 8.4. (PL-1)

## 6. Contractors and vendors
6.1 No contractor or vendor may handle client personal information until it has written terms covering safeguards, confidentiality, and breach notice. (SA-9; GV.SC-05; 501.171(6)(a))
6.2 **Engagement terms** with the coordinator and the bookkeeper must require: their own logins with MFA; no copies of client files on their own devices beyond what the work needs; notice to the owner of any breach as soon as possible and no later than 10 days after determination; and return or deletion of all data when the engagement ends. (SA-9; GV.SC-05; 501.171(6)(a))
6.3 Before adopting any new tool that will hold client data, the owner answers five questions in writing: what data, where stored, who can access it, does it offer MFA, and what happens to the data when the account closes. The transaction platform vendor's SOC 2 report must be reviewed every year, and the owner must operate the customer controls that report lists. The tenant screening service is reviewed with the P10 assessment. (SA-9; GV.SC-07; benchmark 314.4(c)(4), (f)(3))
6.4 Remote support sessions must be started and watched by the owner. No remote access tool may be left with unattended access. (AC-2)

## 7. Access control
7.1 Every person must have their own login. **Credentials and sign-in codes must never be shared.** The coordinator works through delegated access to a transactions mailbox, not through the owner's account. (IA-2; AC-2; PR.AA-01; benchmark 314.4(c)(1)(i))
7.2 MFA must be on for every account that offers it. Email, the transaction platform, and online banking must use a security key or an authenticator app with number matching; text-message codes are not accepted for those three after 2026-09-30. (IA-2(1); IA-2(2); PR.AA-03; benchmark 314.4(c)(5))
7.3 Passwords must be unique passphrases of at least 14 characters, stored in a password manager, never in the browser. (IA-5)
7.4 Contractor accounts are limited to the files they work on, removed on the day an engagement ends, and reviewed every quarter. (AC-2; PR.AA-05; benchmark 314.4(c)(1)(ii))
7.5 The laptop must lock after 5 minutes idle and the phone after 30 seconds. (AC-11)
7.6 **Emergency access.** Recovery codes for email, the platform, and banking, the laptop encryption recovery key, and a one-page access sheet must be kept in a sealed envelope held by the owner's attorney, for use if the owner or the owner's phone is unavailable. (AC-2; CP-2)
7.7 Every Monday the owner must review the email sign-in history, mailbox and forwarding rules, and the platform access log, and act on provider alerts for new forwarding rules and unusual sign-ins the same day. External auto-forwarding must be blocked. Each review is noted in the security log. (AU-6; DE.AE-02; benchmark 314.4(c)(8))
7.8 Every change to account security, sharing, forwarding, or network settings must be noted in the security log with the date and reason. (CM-3; PR.PS-01; benchmark 314.4(c)(7))

## 8. Data handling and money instructions
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Wire and payment instructions, bank account details, identity documents, Social Security numbers, consumer reports, credentials | Approved systems only (8.2); never by ordinary email attachment or text; kept only as long as 8.7 allows |
| **Confidential** | Contracts, offers, client budgets, escrow ledger, this policy set | Approved systems; shared only with parties to the transaction |
| **Public** | Listing details released to the MLS, website content | No restriction |

8.2 Restricted data may be kept only in the transaction platform, the business email and file account, online banking, the screening service, and the locked file drawer. It must not be kept in text messages, the phone camera roll, a personal account, or an AI tool. (AC-3; SA-9)
8.3 The laptop and phone must use full-disk encryption. (SC-28; PR.DS-01)
8.4 **No money moves on an emailed instruction alone.** Before any outgoing escrow payment, and before telling any client where to send money, the owner must confirm the instruction by calling a number taken from the contract, the payee's own website, or the owner's own records, never from the email that carried the instruction. The callback is recorded on the escrow ledger. Escrow wire instructions are given to clients only through the platform's secure document sharing and repeated by phone. Every buyer receives and signs a wire safety notice at contract saying the brokerage will never change wire instructions by email. (IA-8; AT-2(3); PR.DS-10; Fla. Stat. 475.25(1)(k))
8.5 Identity documents and bank statements must be collected through the platform's secure document sharing, not by email or text. Anything that still arrives by text is uploaded and then deleted from the phone the same day. (SC-8; PR.DS-02; benchmark 314.4(c)(3))
8.6 Files that are not in the platform must be kept in the business file account, with an independent backup of mail and files. (CP-9; PR.DS-11)
8.7 **Retention and disposal.** One complete file per transaction or lease is kept for 5 years from the later of the receipt of entrusted funds or the signing of the agreement (Fla. Stat. 475.5015), then destroyed. Extra copies of identity documents, bank statements, and screening reports in email, downloads, and the phone are deleted within 30 days after closing or the rental decision. Paper is cross-cut shredded. Devices are wiped (encrypted, then reset) or destroyed before they leave the owner's control, and each disposal is recorded. (SI-12; MP-6; ID.AM-08; 501.171(8); 16 CFR 682.3)
8.8 Security documentation (this policy, risk assessments, assessments, incident records, any no-harm determination) must be kept for at least 5 years. (SI-12; 501.171(4)(c))

## 9. Acceptable use and training
9.1 The laptop is for brokerage work. Family members may use it only through their own standard account, never the owner's. (PL-4)
9.2 Devices must never be left in a vehicle or unattended at a showing or open house. Losing the phone is reported at once to the lockbox provider and handled under P08. (PL-4; AC-19)
9.3 Automatic updates and the built-in antivirus must stay on, and the router firmware must be kept current. Software comes only from official app stores or the vendor's site. (SI-2; SI-3)
9.4 Work devices use a home network separate from family and smart-home devices, with a changed router admin password, or the phone hotspot. Public Wi-Fi is never used for banking. (SC-7; PR.IR-01)
9.5 **AI tools.** No Restricted or Confidential client information may be entered into a generative AI tool. Any AI-drafted listing description or advertisement must be checked before publishing for any statement of preference based on a protected class (42 U.S.C. 3604(c)). Any automated scoring or recommendation about a person (such as the tenant screening recommendation) is used only as the P10 assessment allows. (PL-4; SA-9; 15 U.S.C. 45(a))
9.6 The owner and the coordinator must complete a short security course every year that covers business email compromise, fake sign-in pages, and how to report them, and the owner must read monthly security reminders. (AT-2; AT-2(3); PR.AT-01; benchmark 314.4(e))

## 10. Incident response
10.1 The brokerage must keep an incident runbook (P08) with a printed contact list, including the escrow bank's fraud desk, in the home office and in the car. (IR-8; RS.MA-01; benchmark 314.4(h))
10.2 Every suspected incident (a client asking about changed wire instructions, a strange sign-in alert, a lost phone, a misdirected email) must be written in the incident log the same day, with the time of discovery. (IR-5; IR-6; RS.MA-02)
10.3 If money may have been sent to the wrong account, the first call is to the sending bank, within minutes, before anything else. (IR-4)
10.4 Notices to clients, the Florida Department of Legal Affairs, and the Florida Real Estate Commission must meet the deadlines in the P08 notification matrix, confirmed by legal counsel. (IR-6; RS.CO-02; 501.171(3)-(4); r. 61J2-10.032(1))
10.5 The runbook must be walked through every year and after any real incident or near miss. Lessons learned must be recorded within 30 days of closing an incident. (IR-8; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities: owner identity and phone, the verified phone channel, banking, email, then the platform. (CP-2; RC.RP-01)
11.2 The owner must keep a written backup arrangement with a trusted broker at another firm to step in on open transactions, with the clients' consent, if the owner is unavailable. (CP-2)
11.3 A printed list of open transactions (parties, title company, phone numbers from the contracts, deadlines, deposit holder) must be updated every week. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and in the weekly review in 7.7. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Systems and data locations (benchmark 314.4(c)(2))
| Item | Restricted data held | Protection required |
|---|---|---|
| Transaction platform (SYS-01) | Contracts, identity documents, wire instructions | 7.1, 7.2, 8.5 |
| Email and files (SYS-02) | Correspondence, escrow ledger spreadsheet, security records | 7.1, 7.2, 7.7, 8.6 |
| Online banking (SYS-05) | Escrow and operating accounts | 7.2, 8.4 |
| Screening service (SYS-10) | Consumer reports | 6.3, 8.7, 9.5 |
| Laptop (SYS-07) | Downloads, synced files | 8.3, 7.5, 9.1 |
| Phone (SYS-08) | Sign-in factor; texts until uploaded | 8.3, 8.5, 7.5, 9.2 |
| Locked file drawer | Signed paper originals, reconciliations | 8.7 |
