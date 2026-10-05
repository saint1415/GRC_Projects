# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated industrial equipment repair service) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-technician |
| Effective date | 2026-09-11 (adopted 2026-09-11) |
| Review cycle | Every August with the risk assessment, and after a new customer contract, a new system or supplier, a helper or subcontractor, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-8, RA-2, RA-3, RA-5, CA-2, SA-9, AC-2, AC-3, AC-6, AC-11, AC-17, AC-19, AC-20, AU-6, CM-2, CM-7, CM-8, IA-2, IA-2(1), IA-5, SC-7, SC-28, CP-2, CP-9, CP-10, MP-6, MP-7, SI-2, SI-3, SI-5, SI-7, SI-12, AT-2, IR-4, IR-5, IR-6, IR-8, MA-4, PE-3 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-02, GV.SC-05, GV.SC-07, GV.OC-04, ID.AM-01, ID.AM-02, ID.AM-07, ID.AM-08, ID.RA-02, ID.RA-09, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.DS-01, PR.DS-11, PR.PS-01, PR.IR-01, DE.AE-02, DE.AE-08, DE.CM-06, DE.CM-09, RS.MA-01, RS.CO-02, RC.RP-03, RC.RP-05 |
| Contract terms | Customer A exhibit S1 to S8; Customer B and C NDAs (Appendix B) |

## 1. Purpose
Protect customers' machine programs, drawings, and passwords, keep customers' production lines safe when the owner connects to them, and meet every security term in the owner's customer contracts, in a way that one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All business information in any form (electronic, paper, spoken), on every system in the Field Service Business Systems (SYS-01 to SYS-06, SYS-08, SYS-09), on the old laptop until it is wiped, in the van and the home office, and at every supplier that handles it. It covers every connection the owner makes to a customer machine, plant network, or substation cabinet. It applies to the owner-technician and to any future helper or subcontractor.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead, contract compliance, incident lead | Owner-technician | Runs this policy; keeps the obligations list; decides incident and notice questions; keeps records |
| Risk acceptor | Owner-technician | Accepts or treats every risk (4.4) |
| On-call IT consultant (NDA) | Contractor | Technical help on request in owner-watched sessions; helps with the annual evaluation |
| Outside bookkeeper | CPA firm | Uses its own MFA login to the accounting SaaS |
| Customer A plant controls engineer | Customer | Approves gateway sessions; runs the media scanning station; receives exhibit S4 notices |

The owner-technician is designated in writing, by this policy, as the person responsible for information security. Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must keep a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The owner must keep the contract obligations list in Appendix B current and review it whenever a customer contract, purchase order, or NDA is signed or changed. (PM-9; GV.OC-03)
4.3 A risk assessment must be completed every August and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. A risk that could affect safety at a customer plant, or that breaks a contract term, is never accepted at High. (PM-9; GV.RM-02)
4.5 Security controls must be evaluated every August (P07). At least every second year, the evaluation must include review by someone outside the business, such as the IT consultant under NDA. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Exceptions, helpers, and sanctions
5.1 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. The owner records any personal departure from this policy as an exception, with the reason and the fix. (PL-1)
5.2 No helper or subcontractor may handle customer information or connect to customer equipment until they sign an NDA and read this policy. Before using one at a utility site, the owner must add them to the access notice step in 7.6. (PS-8; SA-9)
5.3 A helper or subcontractor who breaks this policy must be dealt with under their contract, up to ending it. (PS-8; GV.RR-04)

## 6. Customer obligations and suppliers
6.1 **No customer data to third parties without consent.** Customer A information must not go to any third party, including cloud and AI services other than the business email and file storage, without Customer A's written consent (exhibit S1). Customers B and C information is used only for their services (NDAs). (SA-9; GV.SC-05)
6.2 The owner must keep a supplier list (Appendix A) showing each supplier, the customer data it holds, and the terms that cover it. (SA-9; ID.AM-02)
6.3 Each August the owner must review each supplier: the productivity suite provider's SOC 2 report (and the customer controls it lists), and for the others their security page, MFA support, and data use terms. (SA-9; GV.SC-07)
6.4 Remote support sessions on the laptop must be started and watched by the owner. Unattended remote access must be off. (MA-4; DE.CM-06)

## 7. Working on customer equipment
7.1 The laptop connects to a customer machine network only at the customer's request and only to the machine the job needs. While cabled to a machine network: use the standard account, turn Wi-Fi off, and keep the legacy virtual machine on host-only networking unless it is the tool for that machine. (AC-20; SC-7; CM-7; PR.IR-01)
7.2 **Scanning.** At Customer A, the laptop and every USB stick must go through the plant's media scanning station before connecting to plant equipment, every time, including night calls. If the station is unavailable, call the plant controls engineer and wait (exhibit S3). At other sites, every stick must be scanned on the laptop before it is plugged into a machine. A stick of unknown origin must never be used. (MP-7; SI-3; DE.CM-09)
7.3 **Remote access.** Remote work for Customer A goes only through its gateway (exhibit S2). The owner must not install or keep any remote access device at a customer site without the plant management's written approval, MFA on its management account, and the customer's approval for each session. (AC-17; PR.AA-05)
7.4 **Integrity before loading.** Before loading any firmware or software onto Customer A or utility equipment, the owner must check the hash value Customer A provides and record the check on the job ticket. If the hash does not match, do not load it; tell Customer A the same day (exhibit S5). For other customers, the owner must compare the file with the library copy and its hash before loading. (SI-7; ID.RA-09)
7.5 After every visit, the owner must save each changed program to the library with the date and a hash value, update the library index, and give the customer an encrypted copy of its current programs. (CM-8; CP-9; ID.AM-07)
7.6 **Utility sites.** Follow the utility's access rules, work escorted, and use only utility-controlled remote access. Tell Customer A within 1 business day when anyone working for the business should no longer have utility site access (exhibit S6). (AC-17; PR.AA-06)
7.7 After reloading a program, the owner must compare the program on the controller with the library copy using the engineering software's compare function and record the result. (CP-10; RC.RP-05)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer programs, recipes, firmware, drawings, network lists, machine passwords, vibration data from customer machines | Approved locations only (8.2); encrypted; shared only under 6.1 |
| **Confidential** | Quotes, invoices, remittance details, tax records, contracts, this policy set | Approved locations; owner and bookkeeper only |
| **Public** | Business name, services offered, published manuals | No restriction |

8.2 Restricted data may be kept only on the encrypted laptop, in the business file plan, on encrypted per-customer USB sticks, on the offline backup drives, and (for passwords) in the password manager. It must not be kept in a personal account, the phone's camera roll, a personal photo cloud, or a consumer app. Equipment photos go to the job folder in the business file plan the same day. (AC-3; SC-28; PR.DS-01)
8.3 Every laptop, phone, USB stick, and backup drive that holds Restricted data must be encrypted. (SC-28; PR.DS-01)
8.4 Customer machine passwords must be kept only in the password manager, in a separate vault per customer. (IA-5; PR.AA-01)
8.5 Files are shared only with named people, with links that expire. "Anyone with the link" sharing is not allowed for Restricted data. (AC-3; PR.DS-02)
8.6 Program files may be sent to an OEM support desk only with the customer's consent. If the desk is outside the United States, the owner must first ask the customer whether the files are export-controlled. (SA-9; GV.OC-03)
8.7 **Backups.** Every week the library and business records must be backed up, encrypted, to one of two external drives that are disconnected after the backup; one drive is kept off site. A test restore must be done every quarter, and restored files must be checked against the library index hashes. (CP-9; PR.DS-11; RC.RP-03)
8.8 **Disposal.** USB sticks must be wiped before use for another customer. Old laptops and drives must be wiped (encrypted, then reset) or destroyed by a recycler that gives a certificate, with a record. When work for a customer ends, or on request, its data must be returned or deleted and the deletion recorded (exhibit S7). (MP-6; ID.AM-08)
8.9 Security records (this policy, risk assessments, assessments, incident and job-ticket records, deletion records) must be kept for at least 3 years, or longer if a contract requires it. (SI-12)

## 9. Access control and devices
9.1 Every person must have their own account. Credentials must never be shared. (IA-2; AC-2; PR.AA-01)
9.2 MFA must be on for every service that offers it: the productivity suite, the accounting SaaS, the router portal while the router exists, and any new service. (IA-2(1); PR.AA-03)
9.3 Passwords must be unique passphrases of at least 14 characters, stored in the password manager. Default passwords on any device the owner installs must be changed before use. (IA-5)
9.4 Daily work on the laptop must use a standard account. The separate administrator account is used only to install or update software. (AC-6; PR.AA-05)
9.5 Every quarter the owner must review the accounts in each service (including the bookkeeper's) and remove any that are no longer needed. (AC-2)
9.6 **Emergency access.** Recovery codes for the suite and the accounting SaaS and a one-page emergency access sheet must be kept in a sealed envelope held by the owner's attorney. (AC-2; CP-2)
9.7 On the first working day of each month, the owner must review sign-in history for the suite, the accounting SaaS, and the router portal, and note the review in the security log. (AU-6; DE.AE-02)
9.8 The laptop must lock after 5 minutes idle; the phone after 1 minute. (AC-11)
9.9 The van must be locked and alarmed. The laptop, backup drive, and USB sticks must not be left in the van overnight. The home office file cabinet must be locked when the owner is away. (PE-3; PR.AA-06)
9.10 The laptop must use the separate business Wi-Fi at home. Household devices use the guest network. (SC-7; PR.IR-01)

## 10. Incident response
10.1 The business must keep an incident runbook (P08) with a printed contact list in the van and at home. (IR-8; RS.MA-01)
10.2 **Incident criteria.** Any of these is an incident: a ransom note, renamed or unreadable files, or an antivirus detection on the laptop or a stick; a sign-in the owner did not make; a lost or stolen laptop, phone, stick, or backup drive; a hash mismatch; customer data sent to the wrong place; a customer or supplier reporting a breach that involves the owner's data or devices. (IR-4; DE.AE-08)
10.3 Every suspected incident must be written in the incident log the same day, with the date and time it was discovered. (IR-5; IR-6)
10.4 Customer A must be notified within 24 hours of discovering a cyber incident that affects or could affect its systems or information, or a device used on its equipment, and the owner must coordinate the response with Customer A (exhibit S4). Customers B and C must be given prompt written notice of any unauthorized disclosure of their information (NDAs). Other notices follow the P08 notification matrix. (IR-6; RS.CO-02)
10.5 No ransom may be paid without legal counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-8; ID.IM-04)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; ID.IM-04)
11.2 The owner must keep a written referral arrangement with another independent controls technician for breakdown calls when the owner is unavailable. (CP-2)
11.3 Each grid-equipment customer must hold an encrypted copy of its own current programs (7.5). (CP-9; GV.OC-04)
11.4 The owner must keep a list of engineering software, licenses, installers, and the virtual machine image location (Appendix A), so a replacement laptop can be built in one day. (CM-8; ID.AM-02)

## 12. Acceptable use, training, and AI
12.1 Business devices are for business work. Family members must not use them. (PL-4)
12.2 Software must come only from the maker's official site or app store. Automatic updates and the built-in antivirus must stay on. (SI-2; SI-3)
12.3 The owner must subscribe to CISA ICS advisories and the automation makers' security notices, check them monthly, and pass relevant ones to the affected customer. (SI-5; RA-5; ID.RA-02)
12.4 **AI tools.** No Restricted data may go into any AI tool until a P10 assessment is done, the supplier's terms bar using the data to train or improve its models, and (for Customer A) Customer A has consented in writing. Consumer AI assistants may be used only for Public information. A person must check every AI output before it is used for a maintenance decision, a quote, or a customer document. (PL-4; SA-9)
12.5 The owner must complete a security awareness course every year and a free online industrial control system security course from a government training portal by 2026-12-31. (AT-2; PR.AT-01)

## 13. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the monthly review in 9.7. Exceptions follow section 5.

## 14. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Assets, software, and suppliers
| Item | Restricted data held | Protection required |
|---|---|---|
| Service laptop and legacy virtual machine | Library, drawings | 8.3, 9.4, 7.1, 12.2 |
| Phone | MFA app; photos until moved | 8.2, 9.8 |
| USB sticks (to be replaced by 10 encrypted sticks, one per customer) | Programs for one customer | 7.2, 8.3, 8.8 |
| Two offline backup drives | Library and records | 8.7 |
| Router at Customer B (until replaced or removed) | None; reaches the oven PLC and HMI | 7.3, 9.2 |
| Old laptop (to be wiped) | Old library copy | 8.8 |
| Engineering software from 5 automation makers; licenses; installers; VM image location | n/a | 11.4 |
| Productivity suite provider | Library sync, email, drawings | SOC 2 review (6.3); MFA |
| Accounting SaaS provider | Invoices, payments | MFA; account review |
| Router maker (cloud portal) | Router management | MFA |
| Vibration analytics vendor (AI-001) | Vibration data; machine names | P10 decision; no Customer A data without consent |
| IT consultant | Watched sessions only | NDA; 6.4 |

## Appendix B. Contract obligations list
| Term | Duty | Where it is met |
|---|---|---|
| Customer A exhibit S1 | Use only for the services; no third-party disclosure without written consent | 6.1, 8.6, 12.4 |
| Exhibit S2 | Remote access only through Customer A's gateway; no contractor devices | 7.3 |
| Exhibit S3 | Media scanning station before connecting | 7.2 |
| Exhibit S4 (CIP-013-2 R1.2.1, 1.2.2 flow-down) | Notice within 24 hours; coordinate response | 10.4; P08 |
| Exhibit S5 (R1.2.5 flow-down) | Verify Customer A's hash before loading | 7.4 |
| Exhibit S6 (R1.2.6, 1.2.3 flow-down) | Utility access rules; utility-controlled remote access; 1-business-day access notice | 7.6 |
| Exhibit S7 | Return or securely delete | 8.8 |
| Exhibit S8 | Cyber liability insurance of at least $1 million from 2027-09-30 | P01 R-014 |
| Customer B and C NDAs | Reasonable care; use only for the services; prompt notice of unauthorized disclosure | 8.2 to 8.5; 10.4 |

## Appendix C. Laptop baseline
Standard daily account and a separate administrator account; full-disk encryption on; built-in antivirus and firewall on; automatic updates on; 5-minute lock; legacy virtual machine on host-only networking with no internet; Wi-Fi off when cabled to a machine network; remote-support tool with unattended access off.
