# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (specialty chemical distributor, broker) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Companion document | HSP-01 Hazmat Transportation Security Plan (required by 49 CFR 172.800; kept separate so it can be shown to DOT or DHS on request) |
| Owner and approver | Owner |
| Effective date | 2026-10-05 |
| Review cycle | Every September with the risk assessment and the HSP-01 review, and after a new product, supplier, carrier, system, hire, or incident (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, CA-2, RA-2, RA-3, SA-9, AC-2, AC-6(2), AC-17, AC-19, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, AT-2(3), AT-3, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-07, ID.AM-07, ID.AM-08, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.AT-02, PR.DS-01, PR.DS-11, PR.IR-01, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Regulations | 49 CFR 172.201, 172.202, 172.604, 172.704, 172.800-172.802, 107.620; Fla. Stat. 501.171; CFATS RBPS 27.230(a)(5), (a)(6), (a)(8) as a voluntary benchmark (C-CHEMICAL-R01) |

## 1. Purpose
Protect the information that sells, releases, describes, and pays for each chemical shipment, so that hazmat goes only to the right truck with the right papers, money goes only to the right account, and personal data stays private. Each rule is written so it can be checked (P07).

## 2. Scope
All business information in any form, on every system in the Brokerage Core SaaS Stack (SYS-01 to SYS-08), on paper in the home office, and at every vendor that handles it. It applies to the owner and to any future employee or contractor. Suppliers and carriers are bound through their own agreements and HSP-01.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security officer, privacy contact, risk acceptor, incident commander | Owner | Runs this policy and HSP-01; decides incidents and notices; keeps records |
| Senior management official for HSP-01 | Owner | 49 CFR 172.802(b)(1) |
| On-call IT technician | Contractor | Technical help on request; no standing access |
| ERI provider | Contractor | 24-hour emergency response line for the company's shipments |
| Suppliers' shipping offices and carriers | Business partners | Release, load, and move shipments under HSP-01 rules |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must keep a security program documented in this policy, HSP-01, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The owner is designated in writing, by this policy, as security officer and as the senior management official responsible for HSP-01. (PM-2; GV.RR-02; 172.802(b)(1))
4.3 A risk assessment must be done every September and after any major change, using NIST SP 800-30 Rev. 1. It also serves as the information part of the HSP-01 transportation security risk assessment. (RA-3; PM-9; 172.802(a))
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and are never accepted as they are. Any risk that could put hazmat in the wrong hands is treated. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every September (P07). At least every second year, someone outside the business, such as the IT technician or the hazmat training provider, must review the evaluation. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Exceptions
5.1 Any departure from this policy must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. No exception may be made to HSP-01 sections 4.2 to 4.4 for a bulk hydrogen peroxide load. (PL-1)
5.2 Any future employee or contractor who breaks this policy is dealt with in proportion to intent and harm, up to ending the engagement. (PL-4)

## 6. Vendors and partners
6.1 The owner must keep a vendor list showing each SaaS service, portal, and contractor, the data it holds, whether it offers MFA, and the date its terms or assurance report were last reviewed. (SA-9; ID.AM-07; GV.SC-07)
6.2 The email and file suite provider's SOC 2 report must be reviewed every year, and the owner must operate the customer controls it lists. (SA-9; GV.SC-07)
6.3 **New product rule.** Before the first shipment of any new product, the owner must check its description against the Hazardous Materials Table, add it to the product description sheet, and get written confirmation that the ERI provider has its information. (SA-9; 172.604(b)(2))
6.4 Remote support sessions must be started and watched by the owner. No remote-support tool may be left installed with unattended access. (AC-2; AC-17)

## 7. Access control
7.1 Every person must have their own account in every service. Credentials must never be shared. Family members must not use the business laptop. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every service that offers it, starting with email, accounting, and the bank. Email uses an authenticator app or a security key, not text messages. (IA-2(1); IA-2(2); PR.AA-03)
7.3 Passwords must be unique passphrases of at least 14 characters, kept in a password manager. Passwords must not be saved in the browser. (IA-5)
7.4 Daily work on the laptop must use a standard account. The administrator account is for installs and settings only. (AC-6(2))
7.5 The phone carrier account must have a PIN and a port-out lock. Recovery codes for email, accounting, and the bank must be kept in a sealed envelope held by the business attorney, for use if the owner or the phone is unavailable. (AC-19; CP-2)
7.6 On the first business day of each month, and after any suspicious message, the owner must review email sign-ins, email forwarding rules, and new bank payees, and note the review in the security log. (AU-6; DE.AE-02)
7.7 The owner must review the users in the accounting SaaS every quarter. (AC-2; PR.AA-05)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Pickup authorizations and pickup numbers, HSP-01, driver identity data, bank details, credentials, recovery codes | Approved systems only; MFA-protected; never in AI tools; shared only with the party that needs it |
| **Confidential** | BOLs, customer lists and prices, supplier terms, end-use statements, SDS library, training and registration records | MFA-protected systems; owner only; not in AI tools unless 9.4 allows |
| **Public** | Product brochures, published SDS | No restriction |

8.2 BOLs must be built only from the product description sheet, which lists each product's description as checked against the Hazardous Materials Table. (172.202; SI-12)
8.3 Every device that holds business data must use full-disk encryption. (SC-28; PR.DS-01)
8.4 Email and files must be backed up outside the suite at least monthly, and one month of BOLs must be test-restored each quarter. (CP-9; PR.DS-11; 172.201(e))
8.5 **Retention.** BOL copies, with the date the carrier accepted the load, are kept for 2 years after acceptance (172.201(e)). Registration statements and certificates are kept for 3 years from issuance (107.620(a)). Training records are kept for the current 3 years while the person does hazmat work, plus 90 days (172.704(d)). HSP-01 versions are kept while in effect. Driver identity data is kept for no more than 90 days after delivery. (SI-12; ID.AM-08)
8.6 Data past its retention period must be deleted. Paper is cross-cut shredded. Old laptops and phones must be wiped (encrypted, then reset) before reuse or trade-in, and each disposal recorded. (MP-6; Fla. Stat. 501.171(8))
8.7 Full driver license numbers are not collected. The supplier checks the license at the dock against the driver name and pickup number. (SI-12; Fla. Stat. 501.171(2))

## 9. Acceptable use, AI tools, and training
9.1 Business devices are for business work. (PL-4)
9.2 Automatic updates and the built-in antivirus must stay on. Software comes only from official app stores or the vendor's site. (SI-2; SI-3)
9.3 Business work at home must use a separate work network with a non-default router password. (SC-7; PR.IR-01)
9.4 **AI tools.** An AI tool may be used only after a written P10 assessment and only for the uses it approves. No Restricted data may go into any AI tool. Customer prices and supplier terms may go only into a tool whose terms bar the vendor from training on them. **No AI tool may be used to choose or draft a hazmat description, hazard class, or packing group.** (PL-4; SA-9; 172.202)
9.5 The owner must complete HMR training at least every 3 years (general awareness, function-specific, safety, and security awareness) with a test, plus in-depth security training on HSP-01 within 90 days of each revision. The owner must also complete a yearly module on phishing, lookalike domains, and payment fraud. (AT-2; AT-2(3); AT-3; PR.AT-01; PR.AT-02; 172.704)

## 10. Incident response
10.1 The business must keep an incident runbook (P08) with a printed contact list in the home office. (IR-8; RS.MA-01)
10.2 Every suspected incident or suspicious order (a lookalike domain, a change of ship-to or bank details that fails call-back, a lost phone, a vendor breach notice) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 A suspicious hydrogen peroxide order or pickup request must be reported to the producer's shipping office at once and to local law enforcement the same day. (IR-6; RS.CO-02; C-CHEMICAL-R01 27.230(a)(15)-(16))
10.4 Notices to individuals, regulators, customers, and suppliers must meet the deadlines in the P08 notification matrix, confirmed by counsel. (IR-6; RS.CO-02; Fla. Stat. 501.171)
10.5 No ransom or extortion payment may be made without counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year with one supplier's shipping office, and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 Each supplier's shipping office must have the owner's written instruction to hold every release if the owner cannot be reached by phone. (CP-2)
11.3 The owner must keep a reciprocal coverage arrangement with another independent distributor to answer customers and carriers when the owner is unavailable. The covering person gets a phone and the printed load list only, no system access. (CP-2)
11.4 When there are loads in transit, a printed list of them, with carrier dispatch numbers, must be updated each evening. (CP-2)

## 12. Compliance
Compliance is checked in the annual control assessment (P07) and the monthly review in 7.6.

## 13. Related documents
HSP-01 (this folder); P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Where Restricted data may be kept
| Location | Restricted data allowed | Protection required |
|---|---|---|
| Email and file suite | Pickup authorizations, HSP-01, recovery-code list (not the codes) | 7.2, 8.4 |
| Supplier and carrier portals | Pickup numbers | 7.3 |
| Accounting SaaS and bank | Bank details | 7.2 |
| Sealed envelope at the attorney's office | Recovery codes, laptop recovery key | Sealed; checked yearly |
| Phone | MFA app; driver texts (deleted after the BOL is filed) | 7.5, 8.3 |
| AI assistant | None | 9.4 |
