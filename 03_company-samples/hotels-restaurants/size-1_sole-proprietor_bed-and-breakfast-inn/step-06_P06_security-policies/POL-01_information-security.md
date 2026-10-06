# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (six-room bed-and-breakfast inn) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-innkeeper |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new system or vendor, a change in how payments are taken, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, RA-3, CA-2, SA-9, AC-2, AC-3, AC-11, AC-17, AU-6, IA-2, IA-2(1), IA-5, CM-6, CM-8, SC-7, SC-8, SC-28, CP-2, CP-9, MP-6, PE-3, SI-2, SI-3, SI-12, AT-2, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-07, GV.OC-03, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, PR.IR-01, PR.PS-01, PR.PS-02, ID.AM-07, ID.AM-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| PCI DSS v4.0.1 (N72-R01) | Requirement 12.1 (this policy) and the requirement groups cited in each rule |

## 1. Purpose
Protect guests' card and personal data, keep guests safe in their rooms, and meet PCI DSS, the FTC Act, and Florida law in a way that one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All inn information in any form (electronic, paper, spoken), including card data and guest personal information, on every system in the Inn Business Systems Profile (SYS-01 to SYS-11), on paper in the house, and at every vendor that handles it. It applies to the owner-innkeeper and the relief innkeeper. Contractors (cleaning service, bookkeeper, IT consultant) are bound through their agreements.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security and privacy lead; PCI DSS contact | Owner-innkeeper | Runs this policy; deals with the payment facilitator; decides breach questions; keeps records |
| Risk acceptor and incident commander | Owner-innkeeper | Accepts or treats every risk (4.4); leads incidents (section 10) |
| Relief innkeeper | Unpaid family member | Follows sections 7 to 10 when covering; reports anything unusual to the owner the same day |
| On-call IT consultant | Contractor (confidentiality agreement) | Technical help on request; no standing access |
| Vendors | Innkeeping software vendor, payment facilitator, OTAs, lock vendor | Operate their safeguards under their terms and AOCs |

Because one person writes, follows, and checks these rules, independence is limited. Rule 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The inn must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01; Req 12.1)
4.2 The owner-innkeeper is designated, by this policy, as the inn's security and privacy lead and PCI DSS contact. (PM-2; GV.RR-02; Req 12.1)
4.3 A risk assessment must be completed every July and after any major change, using NIST SP 800-30 Rev. 1. Every risk must have a treatment and a due date. (RA-3; PM-9; Req 12.3)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every July (P07). At least every second year the evaluation must include review by someone outside the inn, such as the IT consultant. (CA-2)
4.6 **PCI DSS scope and validation.** Every year, and before any change in how cards are taken, the owner must confirm in writing where card data flows (P04 diagram) and complete the SAQs the payment facilitator requires. The owner must not attest to a control that is not in place. (CM-8; Req 12.5)
4.7 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02; Req 12.1)

## 5. Sanctions and exceptions
5.1 Anyone who breaks this policy while helping at the inn loses system access until retrained; repeated or deliberate breaches end their access permanently. (PL-4)
5.2 A contractor or vendor that breaks its agreement or this policy must be dealt with under its contract, up to ending it. (SA-9)
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. The owner records any personal departure from this policy as an exception. (PL-1)

## 6. Vendors
6.1 The owner must keep the provider list in Appendix A, showing what each provider does with card or guest data and its PCI DSS role. (SA-9; GV.SC-05; Req 12.8)
6.2 Every year the owner must obtain the current AOC from each provider that handles card data and review the innkeeping vendor's SOC 2 report, then operate the customer controls those documents list. (SA-9; GV.SC-07; Req 12.8)
6.3 No new vendor or new feature may receive card or guest data until the owner has read its terms on data use, retention, and breach notice. (SA-9; Req 12.8)
6.4 Remote support sessions must be started and watched by the owner. Unattended remote access must be off. (AC-17)
6.5 Accounts in cloud-managed device apps (door locks, router) must be reviewed every quarter with the SaaS user lists in 7.4. (AC-2)

## 7. Access control and monitoring
7.1 Every person must have their own account. Credentials must never be shared, including with the relief innkeeper. (IA-2; AC-2; PR.AA-01; Req 8.2)
7.2 MFA must be on for every service that offers it: the innkeeping software, email and files, both OTA portals, the payment facilitator portal, and the accounting SaaS. (IA-2(1); PR.AA-03; Req 8.4)
7.3 Passwords must be unique passphrases of at least 14 characters, kept in a password manager. Passwords must not be saved in a web browser. Default passwords on any device must be changed before use. (IA-5; Req 8.3; Req 2.2)
7.4 Daily work in the innkeeping software must use a front desk role without permission to display full card numbers. The owner must review the users of the innkeeping software, OTA portals, and lock app every quarter and remove anyone who no longer needs access the same day. (AC-2; AC-3; PR.AA-05; Req 7.2)
7.5 The laptop must lock after 5 minutes idle and the phone after 30 seconds. (AC-11; Req 8.2)
7.6 **Emergency access.** Recovery codes for the innkeeping software, email, OTA portals, and payment facilitator, and a one-page access sheet, must be kept in a sealed envelope held by the owner's attorney. (AC-2; CP-2)
7.7 On the first Monday of each month the owner must review the innkeeping activity log, the email sign-in history, the OTA sign-in history, and the lock app access log, and note the review in the security log. (AU-6; DE.AE-02; Req 10.4)
7.8 Each month the owner must check that the website's booking link still points to the innkeeping vendor's hosted payment page and that every price shown is the total price. (SA-9; Req 6.4; 16 CFR 464.2)
7.9 The house master door code must be changed every quarter and whenever a cleaner or helper stops working at the inn. (IA-5; PE-3)

## 8. Card and guest data handling
8.1 Information is classified in three levels. (SI-12; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Card numbers, security codes, ID numbers and ID images, passwords, door codes | Never written down or stored by the inn (8.2); approved systems only |
| **Confidential** | Guest profiles and stay history, contracts, tax and bank records, this policy set | Approved systems; owner and relief innkeeper only |
| **Public** | Rates (total price), policies, website | Must be accurate (9.7) |

8.2 **Card data rules.** (SI-12; SC-8; Req 3.2; Req 3.3.1; Req 4.2)
- Card numbers must never be written on paper or accepted, sent, or kept by email, text, or chat.
- Security codes must never be recorded.
- Phone bookings and third-party payers must pay through the payment facilitator's pay-by-link or the booking engine.
- OTA virtual cards must be charged by token in the innkeeping software, without displaying the full number.
- Card-present payments must use only the P2PE reader.
8.3 Restricted and Confidential data may be kept only in the innkeeping software, the payment facilitator, the OTA portals, the accounting SaaS, and the business file plan. They must not be kept in a personal account, a phone camera roll, or a consumer app. (AC-3; SA-9)
8.4 The laptop must use full-disk encryption, and the phone must keep its passcode and encryption on. (SC-28; PR.DS-01; Req 3.5)
8.5 The owner's office is owner-only and must be locked when the owner is not in it. The P2PE reader must be kept there and checked for tampering each week, as the P2PE Instruction Manual directs. (PE-3; CM-8; PR.AA-06; Req 9.2; Req 9.5)
8.6 **Retention schedule.** (SI-12; ID.AM-08; Fla. Stat. 509.101(2); Fla. Stat. 501.171(8))

| Record | Keep | Then |
|---|---|---|
| Card data and security codes | Not at all after authorization | Never stored |
| Guest ID | Checked visually at check-in; the ID type is noted in the register, no image taken | No image to dispose of |
| Guest register (dates and rates) | At least 2 years | Kept in the innkeeping software |
| Inactive guest profiles | 3 years after the last stay | Deleted in the innkeeping software |
| Guest emails and messages | 3 years | Deleted |
| Security and incident records | 5 years | Shredded or deleted |

8.7 Paper with Restricted or Confidential data must be cross-cut shredded. Old phones and laptops must be encrypted and reset before reuse, or destroyed by a recycler that gives a certificate. Each disposal is recorded in the security log. (MP-6; ID.AM-08; Req 9.4; Fla. Stat. 501.171(8))
8.8 Files that are not in a vendor system must be kept in the business file plan with version history on, and future reservations must be exported from the innkeeping software each month. (CP-9; PR.DS-11)

## 9. Acceptable use and training
9.1 The laptop and phone are for inn work and the owner's own use. Family members must not use the laptop. (PL-4; Req 12.2)
9.2 Devices must not be left unattended outside the locked office or the owner's apartment. (PL-4)
9.3 Automatic updates and the built-in antivirus must stay on. Software must come only from official app stores or the vendor's site. Router firmware must be kept current. (SI-2; SI-3; PR.PS-02; Req 5.2; Req 6.3)
9.4 Guests must use only the guest network. The owner's devices must use only the owner network, whose password is never given to guests. (SC-7; CM-6; PR.IR-01; Req 1.3)
9.5 **AI tools.** No card numbers, ID numbers, or passwords may be entered into any AI tool. The innkeeping AI add-on may run only under the conditions in the P10 assessment, and any new AI feature needs a new assessment first. (PL-4; SA-9)
9.6 The owner must complete a security awareness course every year covering phishing, fake OTA and payment messages, and social engineering. The relief innkeeper must read a one-page briefing before covering and each year. (AT-2; PR.AT-01; Req 12.6; Req 5.4)
9.7 Prices and privacy statements must be accurate. Every price shown or quoted, by any channel, must lead with the total price including mandatory fees. The privacy statement must describe what the inn and its providers actually do with card and guest data. (PM-9; GV.OC-03; 16 CFR 464.2; 15 U.S.C. 45(a))

## 10. Incident response
10.1 The inn must keep an incident runbook (P08) with a printed contact list in the office and in the owner's apartment. (IR-8; RS.MA-01; Req 12.10)
10.2 Every suspected incident (strange message to guests, unexpected sign-in alert, lost phone, fraud complaint from a guest) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 A suspected card data compromise must be reported to the payment facilitator within 24 hours of suspicion, as the sub-merchant agreement requires. (IR-6; Req 12.10)
10.4 Notices to guests, the Florida Department of Legal Affairs, consumer reporting agencies, and other states must meet the deadlines in the P08 notification matrix, confirmed by legal counsel. (IR-6; RS.CO-02; Fla. Stat. 501.171)
10.5 No ransom may be paid without legal counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-8)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The relief innkeeper must have a named account (7.1) so the inn can run without the owner. The owner must keep a written arrangement with a nearby inn to take relocated guests. (CP-2)
11.3 A 14-day arrivals list must be printed each week, and the mechanical override keys must stay in the lockbox. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07), the monthly reviews in 7.7 and 7.8, and the annual PCI DSS validation (4.6). Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P04 control map and data-flow diagram; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Providers, devices, and data locations
| Item | Data held | PCI DSS role | Protection required |
|---|---|---|---|
| Innkeeping software vendor (SYS-01, SYS-11) | Guest profiles, register, card tokens, virtual cards in its vault | Service provider (AOC on file) | 6.2; 7.2; 7.4 |
| Payment facilitator (SYS-02) | Card payments and vault | Service provider (AOC on file); sets the inn's validation | 6.2; 7.2 |
| OTA-1 and OTA-2 (SYS-03) | Reservations, guest messages, virtual cards | Card data source; no card data stored by the inn | 7.2; 7.4 |
| Email and file provider (SYS-04, moving to a business plan) | Guest correspondence | Must hold no card data (8.2) | 7.2; 8.6 |
| Accounting SaaS (SYS-05) | Books and payouts | None | 7.2 |
| Website builder (SYS-06) | Public pages | None; links to the hosted payment page | 7.8 |
| Smart lock vendor (SYS-10) | Guest names, room codes | None | 6.5; 7.9 |
| Laptop (SYS-07) | No card data after the redesign | Out of card data flow | 8.4; 7.5; 9.1; 9.3 |
| Phone and P2PE reader (SYS-08, SYS-02) | Payment app; no ID images | Reader in a validated P2PE solution | 8.4; 8.5; 7.5 |
| Router (SYS-09) | None | Out of card data flow after the redesign | 9.4; Appendix B |

## Appendix B. Device settings checklist
| Device | Setting |
|---|---|
| Router | Unique administrator password; remote management off; separate guest network; WPA2 or stronger; firmware current |
| Laptop | Full-disk encryption; 5-minute lock; antivirus and updates on; no saved browser passwords; no family user profile |
| Phone | Passcode; 30-second lock; photo backup off for documents; updates on |
| Door locks | Installer and old accounts removed; master code changed quarterly; codes expire at checkout |
