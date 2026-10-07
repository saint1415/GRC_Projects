# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent insurance agency) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-agent |
| Effective date | 2026-09-15 (adopted 2026-09-14) |
| Review cycle | Every August with the risk assessment, and after a new system, a new vendor, a hire, a new insurer addendum, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-8, RA-2, RA-3, CA-2, SA-4, SA-9, AC-2, AC-3, AC-6, AC-11, AC-17, AC-19, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-8, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-8, SI-12, AT-2, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, GV.SC-06, GV.SC-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-07, ID.AM-08, ID.IM-02, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Legal and contract basis | Fla. Stat. 501.171(2)-(8); Fla. Stat. 626.561 and 626.748; Rule 69O-128, F.A.C.; the insurers' data security addenda. Elements follow 16 CFR 314.4 as a benchmark |

## 1. Purpose
Protect clients' personal information and the premium money that passes through the agency, and show the insurers and the State of Florida that the agency takes "reasonable measures" (Fla. Stat. 501.171(2)) in a way one person can actually run. This policy, together with the risk register (P01), the system profile (P02), and the incident runbook (P08), is the agency's **written information security program**, the document the insurers' addenda and questionnaires ask for. Each rule below is written so it can be checked (P07).

## 2. Scope
All agency information in any form (electronic, paper, spoken), including personal information (501.171(1)(g)) and nonpublic personal information (Rule 69O-128), on every system in the Agency Systems Profile (SYS-01 to SYS-08), on paper in the office and the garage, and at every vendor that handles it. It covers the premium trust account. It applies to the owner-agent and to any future employee or contractor. Vendors are bound through their contracts.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Information security coordinator (the addenda's "designated individual") | Owner-agent | Runs this policy; decides breach questions with counsel; keeps records |
| Risk acceptor | Owner-agent | Accepts or treats every risk (section 4.4) |
| On-call IT consultant | Contractor (security terms since 2026-07-27) | Technical help on request; owner-started sessions only |
| Bookkeeper | Contractor | Reconciliations with view-only banking access; reports anything unusual the same day |
| Vendors and insurers | AMS vendor, email suite vendor, insurers, others | Operate their safeguards; report incidents under their contracts |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The agency must maintain a written security program made up of this policy, the system profile (P02), the risk register (P01), and the incident runbook (P08). (PM-1; GV.PO-01; 501.171(2))
4.2 The owner-agent is designated in writing, by this policy, as the agency's information security coordinator. (PM-2; GV.RR-02; 16 CFR 314.4(a) benchmark)
4.3 A risk assessment must be completed every August and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. Any risk that can move premium money to the wrong account must be treated. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every August (P07). At least every second year, the evaluation must include review by someone outside the agency, such as the IT consultant. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. Each insurer questionnaire must be answered from this program, not from memory. (PL-1; GV.PO-02)

## 5. Sanctions and exceptions
5.1 **Sanctions.** Any future employee who breaks this policy must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination, documented and kept 5 years. (PS-8; GV.RR-04)
5.2 A contractor or vendor that breaks its contract or this policy must be dealt with under its contract, up to ending it. (SA-9)
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. The owner records any personal departure from this policy the same way. (PL-1)

## 6. Vendors and insurers
6.1 **No terms, no client data.** No vendor may receive or store client information until it has written confidentiality and security terms, including notice to the agency of any breach no later than 10 days after it determines one (501.171(6)(a)). This includes the bookkeeper, IT help, e-signature, rater, and AI tools. (SA-9; GV.SC-05)
6.2 The owner must keep a vendor list showing each vendor, the client information it holds, its terms, and the date last reviewed. (SA-9; ID.AM-07)
6.3 Before adopting any new service that will hold client information, the owner must complete the one-page vendor checklist (security terms, MFA, data location, export and deletion). (SA-4; GV.SC-06)
6.4 The AMS vendor's SOC 2 report must be reviewed every year, and the owner must operate the customer controls it lists. Other vendors are reviewed each August. (SA-9; GV.SC-07)
6.5 The owner must keep each insurer's data security addendum, notice contact, and notice deadline in the P08 notification matrix. (IR-6; RS.CO-02)
6.6 Remote support sessions must be started and watched by the owner. Unattended remote access must be off. (AC-17)

## 7. Access control
7.1 Every person must have their own account. Credentials and one-time codes must never be shared, including with the bookkeeper. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every service that holds client information or money and offers it. Email and online banking must use an authenticator app or security key, not text message codes. Where an insurer portal offers no MFA, the owner uses the AMS single sign-on if offered and asks the insurer in writing for MFA. (IA-2(1); IA-2(2); PR.AA-03; Carrier DSA)
7.3 Passwords must be unique passphrases of at least 14 characters, stored in a password manager, never in the browser. (IA-5)
7.4 The bookkeeper's banking access must be view-only. Only the owner may add payees, change bank details, or send money from the premium trust account. (AC-6; AC-2; PR.AA-05; 626.561(1))
7.5 Devices must lock after 5 minutes idle (the phone after 30 seconds). (AC-11)
7.6 **Emergency access.** AMS, email, and banking recovery codes and a one-page access sheet must be kept in a sealed envelope held by the owner's attorney, for use if the owner or the owner's phone is unavailable. (AC-2; CP-2)
7.7 On the first business day of each month, the owner must review email sign-ins, mailbox forwarding and inbox rules, connected apps, and the AMS activity log, and note the review in the security log. Forwarding to outside addresses must be blocked, and new-rule alerts must stay on. (AU-6; DE.AE-02)

## 8. Money movement and invoices
8.1 Premium trust account details must appear only on the AMS invoice template and in the client letter that says the agency **never changes bank details by email or text**. (SI-8; 626.561(1))
8.2 The owner must never change a client's or insurer's payment details, or send a client new payment instructions, because of an email or text. Any change must be confirmed by calling a number already on file, not one in the message. (IA-2; AT-2)
8.3 Bank alerts must be on for every outgoing transfer and every new payee. The bookkeeper must report any unexpected deposit, transfer, or return the same day. (AU-6; DE.AE-02)

## 9. Data handling
9.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Driver license and Social Security numbers, claim injury details, bank draft forms, credentials, the premium trust account | Approved systems only (9.2); encrypted; least necessary |
| **Confidential** | Applications, policies, loss runs, payroll reports, contracts, this policy set | Approved systems; owner only |
| **Public** | Office hours, website, marketing | No restriction |

9.2 Restricted and Confidential data may be kept only in the AMS, the business email and file suite, and the insurer and partner portals. It must not be kept in a personal account, a phone's camera roll or messages, or a consumer app. (AC-3; SA-9)
9.3 Clients must send documents through the AMS upload portal or a secure link, not as email attachments or texts. Documents the agency sends that contain Restricted data must go by the portal or a secure link. Texted ID photos received anyway must be uploaded to the AMS and deleted from the phone the same day. (SC-8; AC-19; PR.DS-02)
9.4 Every device that can hold Restricted data must use full-disk encryption. (SC-28; PR.DS-01)
9.5 Email and files must be backed up with 1-year retention, and a full AMS export must be taken each quarter and kept encrypted. (CP-9; PR.DS-11; 626.748)
9.6 **Retention.** Policy records are kept at least 5 years after policy expiration (626.748) and premium payment records at least 3 years after payment (626.561(2)); breach determinations are kept 5 years (501.171(4)(c)). Other client information is disposed of when no longer needed. The schedule is reviewed each August. (SI-12; ID.AM-08)
9.7 **Disposal.** Paper is cross-cut shredded. Devices and printer-scanner storage are wiped (or drives destroyed with a certificate) before disposal, reuse, or return, and each disposal is logged. (MP-6; ID.AM-08; 501.171(8))

## 10. Acceptable use, AI, and training
10.1 Agency devices are for agency work. Family members must not use them. (PL-4)
10.2 Agency devices must use the agency network or the phone hotspot, not the family guest network. The router admin password must be changed from the default and its firmware kept current. (SC-7; SI-2)
10.3 Automatic updates and the built-in antivirus must stay on. Software must come only from official app stores or the vendor's site. (SI-2; SI-3)
10.4 **AI tools.** Client information may go into an AI tool only after a written P10 assessment, written terms that bar training on agency data, and the owner's approval. Coverage comparisons and summaries an AI tool drafts must be checked against the policy forms before they reach a client; the licensed agent, not the tool, gives the advice. (PL-4; SA-9; Rule 69O-128)
10.5 The owner must complete a security awareness course every year, including business email compromise, and read monthly security reminders. Any future employee must be trained before getting access. (AT-2; PR.AT-01)

## 11. Incident response
11.1 The agency must keep an incident runbook (P08) with a printed contact list in the office and in the evacuation kit. (IR-8; RS.MA-01)
11.2 Every suspected incident (phishing click, strange mailbox rule, fake invoice, lost phone, vendor notice) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
11.3 The owner must decide with counsel whether a breach of personal information occurred, and must write and keep any determination that notice is not required for 5 years and give it to the Department of Legal Affairs within 30 days (501.171(4)(c)). (IR-4)
11.4 Notices to individuals, the Department of Legal Affairs, consumer reporting agencies, insurers, and the E&O insurer must meet the deadlines in the P08 notification matrix. (IR-6; RS.CO-02)
11.5 No ransom may be paid without counsel's advice and an OFAC sanctions check. (IR-4)
11.6 The runbook must be walked through every year and after any real incident; lessons learned recorded within 30 days of closing an incident. (IR-8; ID.IM-02)

## 12. Contingency
12.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
12.2 The owner must keep a written emergency servicing arrangement with another licensed agent, and give clients a contact card with each insurer's claims line. (CP-2)
12.3 When a hurricane watch is issued, the owner packs the evacuation kit (laptop, phone, chargers, printed contacts, fire-safe authenticator). (CP-2)

## 13. Compliance and enforcement
Compliance is checked in the annual control assessment (P07), the monthly review in 7.7, and each insurer questionnaire. Sanctions follow section 5.

## 14. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Devices and data locations
| Item | Restricted or Confidential data held | Protection required |
|---|---|---|
| Laptop | Synced files, downloads | 9.4, 7.3, 10.3 |
| Phone | Second factors; texted ID photos until uploaded | 9.3, 9.4, 7.6 |
| Printer-scanner | Scans on internal storage | 9.7 |
| Retired laptop | Old client files (to be wiped) | 9.7 |
| AMS | The agency's record | Contract; 7.2; 9.5 |
| Email and file suite | Correspondence, invoices, documents | 7.2; 7.7; 9.5 |
| Online banking | Premium trust account | 7.2; 7.4; 8.3 |
| Garage boxes (2014 to 2021) | Old applications and policies | 9.6; 9.7 |
