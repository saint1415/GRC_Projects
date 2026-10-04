# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (corner grocery with online and phone ordering) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner |
| Effective date | 2026-09-05 (adopted 2026-09-04) |
| Review cycle | Every August with the risk assessment and before each annual SAQ, and after a new system, a new vendor, a new helper, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PL-4, PS-3, PS-8, RA-2, RA-3, CA-2, SA-9, AC-2, AC-11, AC-17, AC-18, AU-6, CM-3, CM-6, CM-8, IA-2, IA-2(1), IA-5, SC-7, SC-8, SC-28, CP-2, CP-9, MP-4, MP-6, SI-2, SI-3, SI-12, PT-5, AT-2, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, GV.SC-07, GV.OC-03, ID.AM-01, ID.AM-07, ID.AM-08, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, PR.IR-01, PR.PS-01, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| PCI DSS v4.0.1 | Requirements 1 to 9, 11, and 12 as rated in P03 (12.1 information security policy; 12.2 acceptable use) |

## 1. Purpose
Protect customers' card data and personal information, and the store's own information, and meet PCI DSS, the FTC Act, and Florida law in a way that one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All store information in any form (electronic, paper, spoken), including card data and customer account and order data, on every part of the Store Sales Platform (SYS-01 to SYS-10), on paper in the store, and at every provider that handles it. It applies to the owner and to the family member who helps at the register, and to any future helper or employee. Providers are bound through their contracts and terms.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security and privacy lead; PCI DSS contact | Owner | Runs this policy; completes the SAQs; decides incident and notice questions; keeps records |
| Risk acceptor | Owner | Accepts or treats every risk (4.4) |
| Register helper | Family member (unpaid) | Follows sections 7.1, 7.8, 8.3, 8.4, and 9; reports anything odd to the owner the same day |
| Outside IT helper | Contractor | Technical help on request; no standing access |
| Providers | Processor, website builder, POS app vendor, accounting vendor, ISP | Operate their safeguards; report incidents under their terms |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The store must keep a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01; PCI 12.1)
4.2 The owner is designated in writing, by this policy, as the store's security and privacy lead and PCI DSS contact. (PM-2; GV.RR-02; PCI 12.1)
4.3 A risk assessment must be completed every August, before each annual SAQ, and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9; PCI 12.3)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. Any risk that exposes full card data is never accepted. (PM-9; GV.RM-01)
4.5 Security controls must be checked every August (P07), and the PCI DSS SAQs must be completed every year with the evidence for each answer kept. At least every second year the check must include review by someone outside the store, such as the outside IT helper. (CA-2; PCI 11.1)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02; PCI 12.1)
4.7 The owner must keep a one-page PCI scope note (how card data flows, which devices touch it, which SAQ applies and why) and confirm it every year before the SAQs. (PL-2; ID.AM-01; PCI 12.5)

## 5. Sanctions and exceptions
5.1 **Sanctions.** A helper or future employee who breaks this policy is retrained; a serious or repeated breach (for example, writing down card data or sharing a password) ends their access to the register and systems. Each case is written down and kept with the security records. (PS-8; GV.RR-04)
5.2 A provider that breaks its terms or this policy is dealt with under its contract, up to replacing it. (SA-9)
5.3 The owner must record any personal departure from this policy as an exception under 5.4, with the reason and the fix.
5.4 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. (PL-1)

## 6. Providers
6.1 Card data may be handled only by providers that show current PCI DSS compliance (an attestation of compliance or the PCI SSC listing). (SA-9; GV.SC-05; PCI 12.8)
6.2 The owner must keep a provider list showing each provider, the data it handles, what it is responsible for under PCI DSS, and the date of its latest AOC or SOC 2 report. (SA-9; GV.SC-05; PCI 12.8)
6.3 Every August, the owner must check the processor's AOC and the website builder's SOC 2 report, and operate the customer responsibilities those documents list. (SA-9; GV.SC-07; PCI 12.8)
6.4 Remote support sessions must be started and watched by the owner. Unattended remote access must be off. (AC-17)
6.5 No customer data may go to a service, including an AI tool, unless its business terms bar reuse and model training and allow deletion. (SA-9; PT-5)

## 7. Access, configuration, and the terminal
7.1 Every person must have their own account. Credentials must never be shared. The family member uses a separate cashier-level POS user that cannot issue refunds. (IA-2; AC-2; PR.AA-01; PCI 7.2, 8.2)
7.2 MFA must be on for every service that offers it: the online store, email, the merchant portal, and the accounting SaaS. (IA-2(1); PR.AA-03; PCI 8.4)
7.3 Passwords must be unique passphrases of at least 14 characters, stored in a password manager. Every vendor default password (router, terminal, Wi-Fi, apps) must be changed before first use. (IA-5; CM-6; PCI 2.2, 8.3)
7.4 Every quarter the owner must review the users and add-ons in the online store, the POS app, and the accounting SaaS, and remove what is not needed. The tax preparer's access is removed after each filing season. (AC-2; PR.AA-05; PCI 7.2, 8.6)
7.5 Laptop and tablet must lock after 5 and 2 minutes idle; the phone after 1 minute. (AC-11)
7.6 **Emergency access.** Recovery codes for email, the online store, and the merchant portal, with a one-page contact sheet, must be kept in a sealed envelope in the owner's home safe, with a copy held by a trusted relative. (AC-2; CP-2)
7.7 **Changes and monthly check.** Changes to online store checkout settings, add-ons, custom code, and router settings must be written in the change log before they are made. No add-on or custom code may run on checkout pages. On the first Monday of each month the owner checks the online store activity log, the email sign-in history, and the processor's refunds report, and notes the check. (CM-3; AU-6; DE.AE-02; PCI 6.5)
7.8 **Terminal.** The terminal's make, model, serial number, and location must be recorded. It must be inspected at opening each day for added parts, broken seals, or a changed serial number. Nobody may service or swap it without a call-back to the processor's published number. Cameras must not view the keypad. (CM-8; PE-3; ID.AM-01; PCI 9.5)
7.9 **Network.** Customers may use only the guest Wi-Fi. The terminal must be on a network separated from customers' devices, and from the laptop and cameras once the separate network is installed. The main Wi-Fi password must not be posted. Router firmware is checked every August. (SC-7; AC-18; PR.IR-01; PCI 1.3, 2.3)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Card data (number, expiration date, security code, PIN), customer accounts and order histories, passwords and recovery codes | Approved places only (8.2); never on paper; never in an AI tool |
| **Confidential** | Supplier invoices, processor statements, tax and bank records, this policy set | Encrypted storage; owner only |
| **Public** | Prices, store hours, online catalog | No restriction |

8.2 Restricted data may be kept only in: the processor's systems, the online store, and the POS app. Customer exports may be made only when needed and must be deleted within 30 days. (AC-3; SA-9; SI-12)
8.3 **Card data is never written down.** Phone-order card details are keyed into the terminal while the customer is on the line. The security code is never stored in any form. (MP-4; PR.DS-01; PCI 3.2, 3.3)
8.4 Card numbers must never be requested or accepted by email, text, or chat. If one arrives, the owner deletes it, asks the customer to call, and notes it in the security log. (SC-8; PR.DS-02; PCI 4.2)
8.5 Every device that can hold Restricted data must use full-disk encryption. (SC-28; PR.DS-01; Fla. Stat. 501.171(2))
8.6 Paper with customer details must be cross-cut shredded, not thrown in the trash. Old devices must be encrypted, then reset, before trade-in, or destroyed by a recycler that gives a certificate. (MP-6; ID.AM-08; PCI 9.4; Fla. Stat. 501.171(8))
8.7 Business files must be kept in a business file plan with version history, so they can be restored. (CP-9; PR.DS-11)
8.8 Security records (this policy, risk assessments, SAQs and evidence, assessments, incident records, and any written no-notice determination) must be kept at least 5 years. (SI-12)
8.9 The online privacy notice and any security statement must match actual practice, and must be checked whenever a provider or data use changes. (PT-5; GV.OC-03)

## 9. Acceptable use, claims, and training
9.1 Store devices are for store work. On the shared laptop, family members use their own standard account, and the owner does daily work from a standard account, not the administrator account. (PL-4; PCI 12.2)
9.2 Devices must never be left in the delivery vehicle or unattended outside the store or the owner's home. (PL-4)
9.3 Automatic updates and the built-in antivirus must stay on. Software must come only from official app stores or the vendor's site. (SI-2; SI-3; PCI 5.2, 6.3)
9.4 The laptop's firewall must stay on. Store administration on public Wi-Fi is allowed only over the phone's cellular data. (SC-7; PCI 1.5)
9.5 **AI tools.** No Restricted data may go into any AI tool. AI output (price suggestions, offer emails) is a draft: the owner reads every email before it is sent and checks every price change against the P10 rules (cost floor, weekly change cap, emergency freeze, same price for every tender) before it goes into the POS app. A new AI use needs a P10 assessment first. (PL-4; SA-9)
9.6 The owner must complete a card security course every year. The family member must be shown terminal inspection and phone and email scams before working the register, and every year after. (AT-2; PR.AT-01; PCI 12.6)
9.7 Before any new helper works the register, the owner checks a reference and the helper signs an acknowledgment of this policy. (PS-3; PCI 12.7)
9.8 Price and offer claims must be true. No comparative claim (for example "lowest prices") may be made without a dated price check kept on file. (PT-5; GV.OC-03; FTC Act Section 5)

## 10. Incident response
10.1 The store must keep the card data compromise runbook (P08) with a printed contact list at the store and at home. (IR-8; RS.MA-01; PCI 12.10)
10.2 Every suspected incident (an odd charge report, a changed terminal, a strange store setting, a phishing click, a lost phone) must be written in the incident log the same day, with the time it was noticed. (IR-5; IR-6; RS.MA-02)
10.3 The processor must be notified within 24 hours of suspecting a card data compromise, as the merchant agreement requires. (IR-6; RS.CO-02; PCI 12.10)
10.4 Notices to customers, the Florida Department of Legal Affairs, and others must meet the deadlines in the P08 notification matrix, confirmed by legal counsel. (IR-6; RS.CO-02; Fla. Stat. 501.171)
10.5 Evidence must not be deleted, and no ransom or extortion payment may be made without counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-4; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 If the terminal or internet is down, the store sells for cash only, using the printed price list and a paper tally. Card numbers are never written down to run later. (CP-2; PCI 3.3)
11.3 **Hurricanes and declared emergencies.** When a hurricane warning is issued, the laptop and tablet go home with the owner. During a declared state of emergency, no price may be raised above its level before the declaration unless the store's own costs rose, and AI price suggestions are not used (Fla. Stat. 501.160; P10). (CP-2)
11.4 The family member keeps a one-page open-and-close sheet that covers cash-only selling and how to pause online orders. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07), the annual SAQs, and the monthly check in 7.7. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Devices and data locations
| Item | Restricted data held | Protection required |
|---|---|---|
| Countertop terminal | Card data during each sale | 7.8, 7.9 |
| Online store | Customer accounts, orders | 7.2, 7.4, 7.7 |
| POS app and tablet | Sales totals | 7.1, 7.5 |
| Laptop | Customer exports (deleted within 30 days) | 8.5, 9.1, 9.3 |
| Phone | Portal second factor; store admin app; customer texts | 7.5, 7.6, 8.4 |
| Email and files | Order notices | 7.2, 8.7 |
| Phone-order pad | Order details only, never card data | 8.3, 8.6 |
