# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent event promoter with one leased room) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new system, a new contractor with access, a change in how cards are taken, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, RA-2, RA-3, CA-2, CA-5, SA-9, AC-2, AC-3, AC-6, AC-11, AC-17, AC-18, AU-6, CM-3, CM-7, IA-2, IA-2(1), IA-5, SC-7, SC-8, SC-28, CP-2, MP-6, PE-3, SI-2, SI-3, SI-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.DS-01, PR.DS-02, PR.PS-01, PR.PS-02, PR.IR-01, ID.AM-07, ID.AM-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| PCI DSS v4.0.1 (N71-R04) | Requirement 12.1 (policy), and the groups cited in each section |
| Other rules | FTC Act Section 5 and 16 CFR Part 464 (N71-R05); Fla. Stat. 501.171(2), (4), (8) |

## 1. Purpose
Protect patrons' personal and payment information, the business's accounts and money, and the ability to run every show, in a way one person can actually keep up. Each rule below is written so it can be checked (P07).

## 2. Scope
All business information in any form, on every system in the Ticketing and Venue Operations Platform (SYS-01 to SYS-08), and at every vendor and contractor that handles it. It applies to the owner. Contractors (the marketing assistant, the door and security contractor's staff, the sound engineer, the IT consultant, the bookkeeper) are bound through their written terms and acknowledgments (section 6).

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security and privacy lead, PCI DSS contact | Owner | Runs this policy; signs the SAQ; decides incident and breach questions; keeps records |
| Risk acceptor | Owner | Accepts or treats every risk (4.4) |
| Contractors with access | Marketing assistant; door contractor's staff | Follow section 9; use only their own named accounts; report anything suspicious to the owner the same day |
| On-call IT consultant | Contractor | Technical help on request; no standing access; helps with the annual review (4.5) |
| Service providers | Ticketing vendor, payment processor, website builder, other SaaS | Operate their safeguards under their terms and AOCs |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01; PCI DSS 12.1)
4.2 The owner is designated in writing, by this policy, as the security and privacy lead and the PCI DSS contact. (PM-2; GV.RR-02; PCI DSS 12.1)
4.3 A risk assessment must be completed every July and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9; PCI DSS 12.3)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. No risk to card data is accepted above Low. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every July (P07). At least every second year, someone outside the business, such as the IT consultant, must review the evaluation. (CA-2; CA-5)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)
4.7 **PCI DSS scope and attestation.** The owner must keep a one-page PCI DSS scope description (card channels, systems, providers) and must sign an SAQ only when every eligibility criterion is true and each answer has evidence in the PCI folder. If any criterion is not true, the owner asks the processor which questionnaire applies. (PL-2; PCI DSS 12.5)

## 5. Contractors and exceptions
5.1 A contractor who breaks this policy is dealt with under its terms, up to ending the engagement and removing all access the same day. (SA-9; PL-4)
5.2 The owner must record any personal departure from this policy as an exception under 5.3, with the reason and the fix.
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. No exception may allow card data to be accepted or kept. (PL-1)

## 6. Vendors and contractors
6.1 The owner must keep a list of service providers showing what each does, the data it handles, and which PCI DSS requirements it is responsible for. Each July the owner downloads the ticketing vendor's and processor's current PCI DSS AOCs and reviews the ticketing vendor's SOC 2 report. (SA-9; GV.SC-07; PCI DSS 12.8)
6.2 Every contractor with access to business systems or patron data must have written terms covering confidentiality, use of data only for the business, return or deletion at the end, and notice to the owner of any suspected incident within 24 hours. (SA-9; GV.SC-05)
6.3 Contractors must acknowledge section 9 in writing before getting access. (PL-4; PCI DSS 12.2)
6.4 Remote support sessions on the laptop must be started and watched by the owner, and remote tools removed after use. (AC-17)

## 7. Access control
7.1 Every person must have their own named account. Credentials must never be shared, including with the marketing assistant or door staff. (IA-2; AC-2; PR.AA-01; PCI DSS 8.2)
7.2 MFA must be on for every account that offers it, starting with email (the reset route for every other account), the ticketing platform, the website builder, the processor portal, and accounting. (IA-2(1); PR.AA-03; PCI DSS 8.4)
7.3 Passwords must be unique passphrases of at least 14 characters, stored in a password manager. Default passwords must be changed before first use. (IA-5; PCI DSS 2.2; 8.3)
7.4 Contractors get the least access their work needs: the marketing assistant gets a marketing role (event pages, no exports, no payouts); door staff get a scan-only role without order search. Access is removed the day a contractor leaves. Every quarter the owner reviews the users and connected apps on SYS-01, the website, email marketing, and social accounts. (AC-2; AC-6; PR.AA-05; PCI DSS 7.2; 8.6)
7.5 The laptop must lock after 5 minutes idle; phones after 1 minute. (AC-11)
7.6 **Emergency access.** Recovery codes for every account with MFA and a one-page emergency access sheet must be kept in a sealed envelope held by the owner's attorney. (AC-2; CP-2)
7.7 On the first Monday of each month, and after every on-sale, the owner must review the SYS-01 activity log (new users, exports, payout changes, setting changes), the website change history, and email sign-ins, check that antivirus and updates are on, and note the review in the security log. (AU-6; DE.AE-02; PCI DSS 10.4)
7.8 **Changes and scripts.** Changes to website scripts and plugins, checkout settings, payout details, ticket limits, and pricing modes must be written in the change log with the date and reason. Only scripts on the approved script list may run on pages that embed the checkout, and the owner checks those pages monthly against the list. (CM-3; CM-7; PR.PS-01; PCI DSS 6.5; SAQ A script eligibility criterion)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Card data (never kept), credentials and recovery codes, patron records and exports | Approved systems only (8.2); MFA; minimum necessary |
| **Confidential** | Artist contracts, settlements, bank and tax records, this policy set | Owner and named contractors only |
| **Public** | Show listings, website content | No restriction, but prices follow 9.6 |

8.2 Patron records may be kept only in SYS-01, the email marketing service, and the business cloud storage. They must not be kept in personal accounts, consumer apps, or AI tools. (AC-3; SA-9)
8.3 **Card data.** The business must never accept, write down, key in, or keep card data. Phone orders are handled by sending the caller a payment link from SYS-01. Card details that arrive by email, text, or social message must not be used; the owner replies with a payment link and deletes the message from every folder, including trash, the same day. (SI-12; PCI DSS 3.2; 3.3; 9.4; Fla. Stat. 501.171(8))
8.4 Card data and patron exports must never be sent by email, text, or chat. Exports are shared only with named accounts; public or "anyone with the link" sharing is not allowed for patron data. (SC-8; AC-3; PR.DS-02; PCI DSS 4.2)
8.5 Every device that can hold Restricted data must use full-disk encryption and a passcode. (SC-28; PR.DS-01)
8.6 **Retention and disposal.** Keep only the latest monthly patron export and delete it after the email marketing upload. Delete Restricted data by erasing it, including from trash. Old phones and laptops must be encrypted, then reset, before reuse or recycling, and each disposal is recorded. (SI-12; MP-6; ID.AM-08; Fla. Stat. 501.171(8))
8.7 Security records (this policy, risk assessments, assessments, SAQs and evidence, incident records) must be kept for at least 3 years, and any written breach determination for at least 5 years. (SI-12; Fla. Stat. 501.171(4)(c))

## 9. Acceptable use, network, pricing, and training
9.1 Business accounts and devices are for business use. Family members and crews must not use them. (PL-4; PCI DSS 12.2)
9.2 The laptop and scanning phones must never be left unattended outside the locked office or the owner's home. The door lead signs the scanning phones out and back each show night. (PE-3; PCI DSS 9.2)
9.3 Automatic updates and antivirus must stay on. New devices and accounts are set up with the one-page setup checklist (change defaults, MFA, encryption, lock). Software comes only from official app stores or the vendor's site. (SI-2; SI-3; CM-6; PCI DSS 2.2; 5.3; 6.3)
9.4 **Network.** Business devices use the business Wi-Fi network only. Touring crews, artists, and the sound engineer use a separate guest network. The business network password is never posted. Away from the Room, use the phone hotspot rather than public Wi-Fi. (SC-7; AC-18; PR.IR-01; PCI DSS 1.3; 2.3)
9.5 **AI tools.** An AI tool may be used with business data only after a written P10 assessment and the owner's approval. Patron data, card data, and credentials must never be entered into a consumer AI tool. Smart pricing runs in suggest-only mode with floors, ceilings (artist caps), and accessible seating kept at or below same-section prices (28 CFR 36.302(f)(3)). (PL-4; SA-9)
9.6 **Prices and promises.** Every ticket price in a post, email, flyer, or listing must be the total price, shown more prominently than any other price (16 CFR 464.2). Posted ticket limits must match how they are enforced, and the privacy notice must match the tools actually used. (PL-4; FTC Act Section 5)
9.7 The owner must complete a security course every year (phishing, payment fraud, card data handling). Contractors with access receive a one-page briefing before access. (AT-2; PR.AT-01; PCI DSS 12.6)

## 10. Incident response
10.1 The business must keep an incident runbook (P08) with a printed contact list in the office and at home. (IR-8; RS.MA-01; PCI DSS 12.10)
10.2 Every suspected incident (unknown sign-in, changed payout details, unknown script, phishing click, lost device, vendor notice) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 On any suspicion that card data was compromised, the owner must notify the processor's risk team immediately and no later than 24 hours (merchant agreement), and must not delete or change evidence until counsel and the processor agree. (IR-6; RS.CO-02; PCI DSS 12.10)
10.4 Notices to patrons, the Florida Department of Legal Affairs, other states, and consumer reporting agencies must meet the deadlines in the P08 notification matrix, confirmed by legal counsel. (IR-6; Fla. Stat. 501.171(3)-(5))
10.5 No ransom or extortion payment may be made without legal counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-3; ID.IM-02)

## 11. Continuity
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 Before doors open, the attendee list must be downloaded to the scanning phones and printed. (CP-2)
11.3 The owner keeps a show-night card for the door lead and a written arrangement with a trusted fellow promoter to run settlement and refunds if the owner is unavailable. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the monthly review in 7.7. Contractor breaches follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Systems and data locations
| Item | Restricted data held | Protection required |
|---|---|---|
| Ticketing platform (SYS-01) | Patron records; settings that control the checkout and payouts | 7.1, 7.2, 7.4, 7.7, 7.8 |
| Website (SYS-03) | Pages that embed the checkout | 7.2, 7.8 |
| Email and files (SYS-04) | Latest patron export; contracts | 7.2, 8.4, 8.6 |
| Email marketing (SYS-05) | Subscriber list | 7.1, 7.2, 8.2 |
| Laptop | Working copies only | 8.5, 7.5, 9.3 |
| Owner's phone | Authenticator app; email | 8.5, 7.5, 7.6 |
| Scanning phones | Attendee list in the scanner app | 7.4, 7.5, 9.2 |
| Any message with card data | Must not exist | 8.3 |
