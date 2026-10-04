# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (IT hardware reseller) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every August with the risk assessment and the CMMC Level 1 self-assessment, and after a new system, a new supplier type, a hire, a CUI request, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-9, PL-1, PL-4, PS-8, RA-2, RA-3, CA-2, SA-9, SR-3, SR-5, SR-11, AC-2, AC-3, AC-6, AC-11, AC-17, AC-20, AC-22, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-28, CP-2, CP-9, MP-6, PE-3, PE-8, SI-2, SI-3, SI-12, AT-2, IR-4, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-06, GV.SC-07, ID.RA-09, ID.AM-04, ID.AM-08, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.DS-01, PR.DS-11, PR.IR-01, PR.PS-02, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Contract and legal basis | FAR 52.204-21(b)(1)(i)-(xv); 32 CFR 170.15 and 170.22 (CMMC Level 1); FAR 52.204-25; FAR 52.204-23; FTC Act Section 5; Fla. Stat. 501.171 |

## 1. Purpose
Protect the business's information, its customers' networks, and the prime's Federal Contract Information (FCI), and meet FAR 52.204-21 and CMMC Level 1 in a way that one person can actually run. Each rule is written so it can be checked (P07).

## 2. Scope
All business information in any form (electronic, paper, spoken), on every system in the Reseller Order Desk (SYS-01 to SYS-10), on paper in the home office and garage, and at every supplier and service provider that handles it. It applies to the owner and to any future employee or helper. Contractors are bound through their agreements.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead and risk acceptor | Owner | Runs this policy; accepts or treats every risk (4.3) |
| CMMC Affirming Official | Owner | Affirms Level 1 compliance in SPRS only when 4.6 is satisfied |
| On-call IT consultant | Contractor (confidentiality agreement) | Technical help on request; no standing access |
| Bookkeeper | Contractor | Read-only financial access |

Because one person writes, follows, and checks these rules, independence is limited. Rule 4.5 adds an outside check every year.

## 4. Governance and risk
4.1 The business must keep a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 A risk assessment must be done every August and after any major change, using NIST SP 800-30 Rev. 1. Every risk must have a treatment and a due date. (RA-3; PM-9)
4.3 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan. A risk that could put counterfeit or covered equipment on a DoD delivery is never accepted. (PM-9; GV.RM-01)
4.4 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)
4.5 The CMMC Level 1 self-assessment must be done every year against all 15 FAR 52.204-21 requirements, with the IT consultant checking the evidence on screen. (CA-2; 32 CFR 170.15(a)(1))
4.6 **Affirm only what is true.** The owner must not enter a Level 1 result or affirmation in SPRS unless every requirement is MET with evidence in the evidence folder. If a requirement stops being met, the owner fixes it at once or tells the prime. (CA-2; PM-9; 32 CFR 170.22)

## 5. Exceptions and sanctions
5.1 **Exceptions** must be written, risk-rated under 4.3, recorded in the risk register, and must expire within 12 months. No exception may be made to a FAR 52.204-21 requirement while the business holds a Level 1 status. (PL-1)
5.2 Any future employee or helper who breaks this policy must be sanctioned in proportion to intent and harm, from retraining to ending the engagement. Contractors are handled under their agreements. (PS-8)

## 6. Suppliers and supply chain (scaled from NIST SP 800-161 Rev. 1)
6.1 **Sourcing rule.** Items for DoD orders, and any switch, router, firewall, access point, or optic for any customer, must be bought from the OEM or an authorized distributor. A marketplace seller or broker may be used only for other items or when no authorized source has stock, and then only under 6.2 and 6.3. (SR-5; GV.SC-06)
6.2 A marketplace seller or broker must be checked before the first purchase: business registration, time in business, return terms, and reviews, recorded in the supplier list. A seller with a failed authenticity check is removed. (SR-3; SR-5; GV.SC-07)
6.3 **Receiving checks.** Every item from a non-authorized source must be inspected on arrival: serial number checked in the OEM partner portal, seals and packaging inspected and photographed, and, for devices with firmware, the firmware version and hash compared with the OEM's published values before the item is sold. Failures go to the quarantine shelf and the P08 runbook. (SR-11; ID.RA-09)
6.4 **Section 889 check.** Before quoting any item for a DoD order, the owner must confirm the true manufacturer, including for white-label or rebranded products, is not a covered manufacturer under FAR 52.204-25, and record the check on the quote. DoD-bound purchase orders must carry the substance of FAR 52.204-25. (SR-5; GV.SC-05)
6.5 **Payments.** A first payment to a new account, or any change of bank details, must be confirmed by a call to a phone number already on file, never one in the message. Marketplace sellers are paid only through the marketplace. (SR-3; AT-2)
6.6 The owner must keep a supplier and service provider list showing what data each holds and its assurance (for example a SOC 2 report). The accounting SaaS vendor's SOC 2 report is reviewed every year, and the owner operates the customer controls it lists. (SA-9; GV.SC-07)
6.7 Remote support sessions must be started and watched by the owner. Unattended remote access must be off. (SA-9; AC-17)

## 7. Access control
7.1 Every person must have their own account. Credentials must never be shared. (IA-2; AC-2; PR.AA-01; 52.204-21(b)(1)(v))
7.2 MFA with an authenticator app must be on for every service that offers it, starting with the accounting SaaS, email, distributor portals, and the bank. (IA-2(1); IA-2(2); PR.AA-03)
7.3 Passwords must be unique passphrases of at least 14 characters stored in a password manager. Default passwords on routers and other devices must be changed before use. (IA-5; 52.204-21(b)(1)(vi))
7.4 The owner must review every account list (SYS-01, SYS-02, SYS-03) each quarter and remove accounts that are no longer needed the same day. (AC-2; PR.AA-05; 52.204-21(b)(1)(i))
7.5 Daily work on the laptop must use a standard account. The administrator account is used only to install software or change settings. (AC-6; 52.204-21(b)(1)(ii))
7.6 The laptop must lock after 5 minutes idle and the phone after 1 minute. (AC-11)
7.7 **Emergency access.** Recovery codes for email, the accounting SaaS, and the bank, and a one-page emergency sheet, must be kept in a sealed envelope held by the owner's attorney. (AC-2; CP-2)
7.8 On the first business day of each month the owner must review the sign-in history of SYS-01 and email, mail forwarding rules, and any payment-detail changes, and note the review in the security log. (AU-6; DE.AE-02)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-08)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | FCI (asset tag lists, serial-to-tag spreadsheets, delivery schedules), customer device passwords, credentials, bank details | Approved locations only (8.2); named-people sharing; never in AI tools |
| **Confidential** | Pricing, quotes, customer lists, supplier terms, this policy set | Approved locations; shared only with the customer or supplier concerned |
| **Public** | Website, product catalog | No restriction |

8.2 Restricted data may be kept only in SYS-01, SYS-02 (named-people sharing), the password manager vault, the laptop, and paper in the locked cabinet. (AC-20; AC-3; 52.204-21(b)(1)(iii))
8.3 **CUI stop rule.** If the prime or anyone sends a file marked CUI or Controlled, the owner must not open or save it, must tell the sender and ask for its return or deletion instructions, and must re-scope before accepting any such work. (AC-20; 32 CFR 170.23(a)(2))
8.4 Files must be shared with named people only. Links to Restricted files must expire within 30 days. (AC-3; PR.DS-01)
8.5 Staging spreadsheets must be saved only in cloud storage. The laptop and cloud files must be backed up with version history. (CP-9; PR.DS-11)
8.6 Security and CMMC evidence (assessments, screenshots, SPRS entries, incident records, disposal records) must be kept for 6 years from the CMMC Status Date or creation, whichever is later. (SI-12; 32 CFR 170.15(c)(2))
8.7 Before disposal, trade-in, resale, or reuse, every laptop and phone must be encrypted and then reset, or destroyed by a recycler that gives a certificate. Every returned network device must be factory reset and checked for leftover configuration before resale. Each wipe is recorded (device, serial, method, date). (MP-6; ID.AM-08; 52.204-21(b)(1)(vii))

## 9. Acceptable use, network, physical, and training
9.1 Business devices are for business work. Household members must not use them. (PL-4)
9.2 The laptop must use the business-only Wi-Fi network at home. Household devices stay on the household network. Router settings are checked every quarter and firmware is kept current. (SC-7; SI-2; 52.204-21(b)(1)(x), (xii))
9.3 Automatic updates and the built-in antivirus must stay on. Software comes only from official stores or the vendor's site. The owner relies on the vendors' testing for automatic laptop and phone updates; firmware for staged devices is tested on the bench test switch before use. (SI-2; SI-3; PR.PS-02)
9.4 **Posting.** Nothing about DoD orders, the prime, or the installation may be posted on the website or social media. Every product photo is checked for labels, asset tags, and customer names before posting. (AC-22; 52.204-21(b)(1)(iv))
9.5 **AI tools.** Only the approved AI tool in P10 may be used, with model training off. No Restricted data may be entered. DoD order lines and customer names are removed before any sales history is uploaded. An AI suggestion never overrides the sourcing rule in 6.1. (PL-4; AC-20; SA-9)
9.6 **Garage and cabinet.** Staged DoD equipment and stock are kept in the locked cabinet when the owner is not at the bench. The cabinet key is kept in a lockbox only the owner can open. The garage keypad code is changed every year and whenever someone no longer needs it. Anyone else who enters the garage is accompanied by the owner and written in the entry log. Keys and codes are listed in the security log. (PE-3; PE-8; PR.AA-06; 52.204-21(b)(1)(viii)-(ix))
9.7 The owner must complete a security awareness course and an anti-counterfeit course every year, and review phishing and payment fraud examples each quarter. (AT-2; PR.AT-01)

## 10. Incident response
10.1 The business must keep an incident runbook (P08) and a printed contact sheet in the home office. (IR-8; RS.MA-01)
10.2 Every suspected incident (failed serial check, suspicious payment request, phishing click, lost device, customer report of an odd device) must be written in the incident log the same day, with the time it was discovered or identified. (IR-6; RS.MA-02)
10.3 Report clocks: covered telecommunications equipment found during performance must be reported within 1 business day of identification (FAR 52.204-25(d)); a Kaspersky covered article within 3 business days (FAR 52.204-23(c)); a suspected counterfeit or nonconforming item delivered on the prime's orders within 2 business days (BPA term). Reports go to the prime's subcontracts manager as the BPA states. (IR-6; RS.CO-02)
10.4 If personal information may be involved, Florida notice duties are checked with counsel (Fla. Stat. 501.171). (IR-6)
10.5 No extortion or ransom payment may be made without legal counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned are recorded within 30 days of closing an incident. (IR-8)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner keeps the emergency sheet (7.7) and a written agreement that the prime may source open orders elsewhere if the owner is unavailable for more than 3 business days. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07), the CMMC Level 1 self-assessment (4.5), and the monthly review in 7.8.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P09 self-check; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Devices and data locations
| Item | Restricted data held | Protection required |
|---|---|---|
| Laptop | Staging work, downloads | 7.5, 7.6, 8.5, 9.2, 9.3 |
| Phone | Email; second factors | 7.2, 7.6 |
| SYS-01 accounting and inventory SaaS | Orders, DoD order notes | 7.2, 7.4, 7.8 |
| SYS-02 email and files | FCI spreadsheets, quotes | 7.2, 8.4, 8.5 |
| Password manager vault | Customer device passwords, credentials | 7.2, 7.3 |
| Locked cabinet | Staged DoD equipment, paper tag sheets | 9.6 |
