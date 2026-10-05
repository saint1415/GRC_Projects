# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight broker arranging truck and rail shipments) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner |
| Effective date | 2026-09-09 (adopted 2026-09-08) |
| Review cycle | Every August with the risk assessment, and after a new system, a new vendor, a new service line, a hire, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-8, RA-2, RA-3, CA-2, SA-9, SR-6, AC-2, AC-3, AC-11, AC-17, AC-19, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, AT-2(3), IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, GV.SC-06, GV.SC-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-11, PR.IR-01, PR.PS-02, ID.AM-07, ID.AM-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Rules served | Fla. Stat. 501.171(2), (3)-(6), (8); 49 CFR 371.3 and 371.7; 49 U.S.C. 13901(c) and 13904(g); 49 CFR 387.307(e); largest shipper's master agreement; railroad portal terms |

## 1. Purpose
Protect the confidentiality, integrity, and availability of carrier, driver, shipper, and business information; keep loads moving and carriers paid; and keep the business's FMCSA broker authority, in a way that one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All business information in any form (electronic, paper, spoken) on every system in the Freight Brokerage SaaS Stack (SYS-01 to SYS-09), in the railroad portals and FMCSA account the owner uses (SYS-10, SYS-11), on paper in the home office, and at every vendor that handles it. It applies to the owner and to any future employee or contractor. Contractors are bound through their contracts.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead | Owner | Runs this policy; decides breach questions; keeps records |
| Risk acceptor | Owner | Accepts or treats every risk (section 4.4) |
| Contract bookkeeper | Contractor | Uses an own accounting login; follows sections 7 and 8 |
| On-call IT consultant | Contractor | Technical help in sessions the owner starts; no standing accounts |
| Transportation attorney | Outside counsel | Backup responder for surety and FMCSA notices (11.3); breach advice |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must maintain a security program documented in this policy, the system security plan (P02), and the risk register (P01). (PM-1; GV.PO-01; Fla. Stat. 501.171(2))
4.2 The owner is designated in writing, by this policy, as the business's security lead. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every August and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every August (P07). At least every second year, the evaluation must include review by someone outside the business, such as the IT consultant or another broker's security lead. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Sanctions and exceptions
5.1 **Sanctions.** Any future employee who breaks this policy must be sanctioned in proportion to intent and harm: retraining, written warning, or termination. Each sanction must be documented. (PS-8; GV.RR-04)
5.2 A contractor or vendor that breaks its contract or this policy must be dealt with under its contract, up to ending it. (SA-9)
5.3 **Exceptions**, including the owner's own departures from this policy, must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. (PL-1)

## 6. Vendors, carriers, and payments
6.1 The owner must keep a vendor list showing each service, the data it holds, its breach notice terms, and its assurance (SOC 2 report or other). The TMS vendor's SOC 2 report must be reviewed every year, and the owner must operate the customer controls that report lists. A vendor that holds personal information for the business must commit to notify the business of a breach no later than 10 days after determining it (Fla. Stat. 501.171(6)). (SA-9; GV.SC-05; GV.SC-07)
6.2 **Carrier identity check.** Before a carrier's first load, the owner must confirm its authority and insurance through the monitoring service, confirm that its email domain and phone number match the contact on its FMCSA registration, and call the registered number to confirm the booking. If they do not match, the carrier is not booked. (SR-6; GV.SC-06)
6.3 **Bank detail changes.** A carrier's bank details may be changed only after a call-back to the phone number already in the carrier file, never a number given in the request. No payment goes to new bank details for 5 business days after a change. Each change and call-back is noted in the TMS. Shippers are told in writing that the business's bank details never change by email. (AT-2(3); SR-6)
6.4 Every truckload must be tracked. Rate confirmations must forbid re-brokering and name the driver and truck expected at pickup. (SR-6; GV.SC-07)
6.5 IT consultant sessions must be started and watched by the owner. Contractors must not hold standing administrator accounts in any service. (AC-17; AC-2)
6.6 The owner may use a railroad portal only with a user ID the railroad issued to the owner. Another person's credentials must never be used. (AC-2; IA-2)

## 7. Access control
7.1 Every person must have their own account. Credentials must never be shared. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every service that offers it. Email, the TMS, and the FMCSA account must use an authenticator app or a hardware security key, not text messages, as the main method. (IA-2(1); IA-2(2); PR.AA-03; Fla. Stat. 501.171(2))
7.3 Passwords must be unique passphrases of at least 14 characters, stored in a password manager. (IA-5)
7.4 Every quarter the owner must review the user and administrator accounts in each SaaS service and remove any that are not needed. (AC-2; PR.AA-05)
7.5 The laptop must lock after 5 minutes idle; the phone after 1 minute. (AC-11)
7.6 **Emergency access.** Recovery codes, a spare hardware security key, the in-transit list procedure, and a signed authorization for the attorney (11.3) must be kept in a sealed envelope held by the transportation attorney. (AC-2; CP-2)
7.7 On the first business day of each month, the owner must review the TMS audit log, the email sign-in history, and the bank's payee history, and before each weekly ACH batch must check the TMS log for bank detail changes. Each review is noted in the security log. (AU-6; DE.AE-02)
7.8 The mobile carrier account that receives MFA codes must have a port-out or account PIN. The FMCSA account must recover only to the business email. (IA-5; AC-19)

## 8. Data handling
8.1 Information is classified in three levels. Documents marked Sensitive Security Information must not be accepted; if one arrives, it must not be forwarded, and the sender is asked how to return it. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Carrier W-9s with Social Security numbers, driver license copies, bank details, driver location, credentials | Approved locations only (8.2); encrypted; least access |
| **Confidential** | Shipper rates and contracts, rail shipping instructions, 49 CFR 371.3 transaction records, this policy set | Approved SaaS services; named-recipient sharing |
| **Public** | Website, load board profile | No restriction |

8.2 Restricted data may be kept only in the TMS carrier file and the bank portal. It must not be kept in email attachments, a phone camera roll, a personal account, or a consumer app. (AC-3; SA-9)
8.3 Every device that can hold Restricted or Confidential data must use full-disk encryption. (SC-28; PR.DS-01)
8.4 Files must be shared only with named recipients. The file suite default must be named recipients only. (AC-3; PR.AA-05)
8.5 **Independent copies.** The owner must download the in-transit list at 7 a.m. and 2 p.m. each business day, export the TMS transaction records every quarter, and export the carrier and contract folders every month to an encrypted drive kept offline. (CP-9; PR.DS-11; 49 CFR 371.3(b))
8.6 Photos of BOLs, PODs, and carrier documents must be uploaded to the TMS the same day and then deleted from the phone. (SC-28; CP-9)
8.7 **Retention and disposal.** Transaction records are kept 3 years after the load (49 CFR 371.3(b)); carrier packets 3 years after the carrier's last load. Then paper is cross-cut shredded and electronic copies erased. Old laptops and phones are wiped (encrypted, then reset) or destroyed by a recycler that gives a certificate. Each disposal is recorded. (SI-12; MP-6; ID.AM-08; Fla. Stat. 501.171(8))
8.8 Security documentation (this policy, risk assessments, assessments, incident records, and any no-harm determination under Fla. Stat. 501.171(4)(c)) must be kept at least 5 years. (SI-12)

## 9. Acceptable use and training
9.1 Business devices are for business work. Family members must not use them. (PL-4)
9.2 Automatic updates and the built-in antivirus must stay on. Software must come only from official app stores or the vendor's site. (SI-2; SI-3; PR.PS-02)
9.3 Business devices must use their own network or the phone hotspot, not the shared household network. (SC-7; PR.IR-01)
9.4 **AI tools.** An AI tool or feature may process business data only after a written assessment (P10) and the owner's written approval, with model training on business data turned off. Restricted data must never go into a consumer AI tool. AI output must not approve a carrier payment or a shipper invoice without the owner's review. (PL-4; SA-9)
9.5 The owner must complete a security awareness course every year that covers phishing, payment change fraud, and carrier impersonation. Any future workforce member must be trained before getting access. (AT-2; AT-2(3); PR.AT-01)
9.6 Quotes, rate confirmations, email signatures, the website, and the load board profile must use the registered business name and MC number and state broker status. (PL-4; 49 CFR 371.7; 49 U.S.C. 13901(c))

## 10. Incident response
10.1 The business must keep an incident runbook (P08) with a printed contact list at the home office and in the laptop bag. (IR-8; RS.MA-01)
10.2 Every suspected incident (phishing click, strange sign-in alert, bank detail change request that fails the call-back, lost phone, vendor notice) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 For any incident involving personal information, the owner must decide with counsel whether it is a breach under Fla. Stat. 501.171 and the laws of other affected states. A decision that notice is not required must be written, kept 5 years, and sent to the Florida Department of Legal Affairs within 30 days (501.171(4)(c)). (IR-6)
10.4 Notices to shippers, individuals, and regulators must meet the deadlines in the P08 notification matrix, including the largest shipper's 72-hour notice and Florida's 30-day notice. (IR-6; RS.CO-02)
10.5 No ransom may be paid without legal counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-8; ID.IM-02)

## 11. Contingency and broker authority
11.1 Recovery follows the BIA (P05) priorities: owner access, in-transit loads, internet, TMS, railroad portals, email, accounting and bank. (CP-2; RC.RP-01)
11.2 The owner must keep a written backup broker agreement with a registered broker who will follow loads in transit if the owner cannot. (CP-2)
11.3 Surety claim notices and FMCSA notices must be answered within the 7-business-day windows in 49 CFR 387.307(e). The surety must have the business email on file, and the transportation attorney holds a signed authorization to respond if the owner cannot. (CP-2; IR-8)
11.4 The FMCSA registration record must be checked monthly and updated within 30 days of any change in address, phone, email, or process agent (49 U.S.C. 13904(g)). (PM-9; IA-5)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the monthly review in 7.7. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system security plan; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Where Restricted and Confidential data lives
| Location | Data held | Protection required |
|---|---|---|
| TMS (SYS-01) | Carrier file (W-9s, bank details), transaction records, BOL and POD images | 7.2, 8.2, 8.5 |
| Bank portal (SYS-04) | Carrier bank details for ACH | 6.3, hardware token |
| Email and file suite (SYS-02) | Shipper contracts, rail shipping instructions; no Restricted data after cleanup | 7.2, 8.4 |
| Accounting SaaS (SYS-03) | Payables ledger, 1099 data | 7.2 |
| Tracking app (SYS-06) | Driver names, phone numbers, location | 6.1 |
| Laptop (SYS-07) | Synced Confidential files | 8.3, 7.5, 9.2 |
| Phone (SYS-08) | MFA codes and app, document photos until uploaded | 8.3, 8.6, 7.8 |
| Offline encrypted drive | Monthly and quarterly exports | 8.3, 8.5 |
| Paper file at the home office | Signed agreements | Locked drawer; 8.7 |
