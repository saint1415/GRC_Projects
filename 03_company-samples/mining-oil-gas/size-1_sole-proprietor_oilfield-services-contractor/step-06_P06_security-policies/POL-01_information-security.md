# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated oilfield services contractor) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-operator |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, before each MSA renewal, and after a new system, a new customer connection, a hire, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-8, RA-2, RA-3, CA-2, CA-3, SA-9, AC-2, AC-6(2), AC-11, AC-17, AC-19, AU-6, IA-2(1), IA-2(2), IA-5, CM-3, CM-8, SC-7, SC-28, CP-2, CP-9, MP-6, MP-7, SI-2, SI-3, SI-12, AT-2, AT-3, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-06, GV.SC-10, ID.AM-07, ID.AM-08, ID.RA-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.AT-02, PR.DS-01, PR.DS-11, PR.PS-01, PR.IR-01, DE.CM-03, DE.CM-09, RS.MA-01, RS.CO-02, RC.RP-01 |
| Benchmark and duties | NIST CSF 2.0 with SP 800-82 Rev. 3 (N21-BM, voluntary); Customer A MSA security schedule items (1) to (8) (MSA-A); Fla. Stat. 501.171 |

## 1. Purpose
Protect customer information and customer field equipment that the business touches, and the business's own records, in a way one person can actually run on a laptop, a phone, and a truck. Meet Customer A's security schedule. Each rule is written so it can be checked (P07).

## 2. Scope
All business information in any form, including customer production data, control programs, setpoints, network details, and credentials, and the helpers' W-9 forms; every system in the Field Service Business Systems (SYS-01 to SYS-08); and every connection the owner makes to a customer system, by cable, USB drive, or remote session. It applies to the owner-operator and to any future employee. Day helpers do not use the systems; any future change to that must follow section 5.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead and risk acceptor | Owner-operator | Runs this policy; accepts or treats every risk; keeps records |
| Incident commander | Owner-operator | Runs the P08 runbook; gives customer and legal notices |
| On-call IT technician | Contractor | Technical help on request; no standing access |
| Customer change approver | Customer A production superintendent; Customer B operations manager | Approves logic and setpoint changes in writing |
| Customer incident contact | Customer A production superintendent; each customer's named contact | Receives incident notices (section 10) |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The owner-operator is designated, by this policy, as the security lead, risk acceptor, and incident commander. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every July, before each MSA renewal, and after any major change, using NIST SP 800-30 Rev. 1. Every risk must have a treatment and a due date. (RA-3; PM-9; ID.RA-01)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. A risk that could cause a release or unsafe condition at a customer site must not be accepted above Low. (PM-9; GV.RM-01)
4.5 Controls must be self-assessed every July (P07). At least every second year, the assessment must include review by someone outside the business, such as the IT technician or a customer's security staff. (CA-2; ID.IM-01)
4.6 This policy must be reviewed at least every year, before each MSA renewal, and after an incident. (PL-1; GV.PO-02)

## 5. Workforce, sanctions, and exceptions
5.1 Day helpers must not be given any account, password, device, or customer access. Any future employee must sign this policy and be trained (9.7) before getting access, and a breach of it must lead to retraining, a written warning, or termination, recorded and kept 6 years (8.8). (PS-8)
5.2 **Exceptions** to this policy must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. No exception may override a customer contract term. (PL-1)

## 6. Providers and customer connections
6.1 Customer data may be kept only in the services listed in Appendix A, and never in a personal account. (SA-9; GV.SC-05; MSA-A (1))
6.2 The owner must keep a contract requirements register listing each customer's security terms (notice times, change approval, data return) and read it before each renewal. (PM-9; GV.OC-03; MSA-A (1)-(8))
6.3 Before using any new service that will hold customer data, including any AI tool, the owner must read its terms and confirm: no use of the data for the provider's own purposes (such as model training), MFA available, and data deletion on request. If a customer's contract requires consent, written consent must be obtained first. (SA-9; GV.SC-06; MSA-A (5))
6.4 Each provider in Appendix A must be reviewed every July, including any SOC 2 report it publishes, and the owner must run the customer-side controls that report lists. (SA-9; GV.SC-07)
6.5 Remote access into a customer system is allowed only by the method the customer approves in writing. Shared logins and always-on unattended access must be reported to the customer as a risk, in writing, and each session must be recorded in the remote session log (date, customer, purpose, changes made). Passwords must never be saved in a remote client. (AC-17; CA-3; PR.AA-05; MSA-A (2))
6.6 The IT technician may reach the laptop only in a session the owner starts and watches. (AC-17)

## 7. Access control
7.1 Every account must be the owner's own. Credentials must not be shared, except a shared login the customer imposes, which is handled under 6.5. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every service that offers it: email and files, accounting, and the dynamometer service. Use an authenticator app, not text-message codes, where the service allows it. (IA-2(1); IA-2(2); PR.AA-03)
7.3 All passwords, including customer site and device passwords, must be unique passphrases of at least 14 characters (or the longest the device allows) and stored only in the password manager. No password lists in files, notes, or spreadsheets. Maker default passwords on devices the owner sets up must be changed, with the customer's approval. (IA-5; PR.AA-01; MSA-A (1))
7.4 The laptop must be used day to day from a standard account. The administrator account is used only to install or update software. (AC-6(2); PR.AA-05)
7.5 The laptop must lock after 5 minutes idle; the phone after 1 minute. (AC-11)
7.6 **Emergency access.** Account recovery codes, the laptop encryption recovery key, the password manager emergency kit, and a one-page sheet saying where the customer program copies are must be kept in a sealed envelope held by a trusted family member. (AC-2; CP-2)
7.7 On the first working day of each month, the owner must review the sign-in lists of the email and accounting services, check open POA&M items, and note both in the security log. Any sign-in the owner does not recognize is handled under section 10. (AU-6; DE.CM-03; GV.OV-03)

## 8. Data handling and control changes
8.1 Information is classified in three levels. Appendix A lists where each kind is kept. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer control programs and setpoints, network details, credentials, W-9 forms | Approved locations only (Appendix A); encrypted; password manager for credentials |
| **Confidential** | Customer production data (gauges, run tickets, dynamometer cards), MSAs, invoices | Business accounts only; shared with third parties only with customer consent (6.3) |
| **Public** | Business name, phone number, insurance certificates sent on request | No restriction |

8.2 Restricted data must not be pasted or uploaded into any AI tool or website not listed in Appendix A. (SA-9; MSA-A (5))
8.3 The laptop must keep full-disk encryption on. USB drives that carry customer programs must be encrypted. (SC-28; PR.DS-01)
8.4 **Control changes.** Before changing logic or setpoints on a customer device, the owner must have the customer approver's email approval (a text is acceptable in an emergency, followed by email the same day). Each change must be entered in the change log: date, device, reason, approver, before and after program versions. Hardwired safety shutdowns must never be bypassed or changed. (CM-3; ID.RA-07; PR.PS-01; MSA-A (4))
8.5 After each approved change, the owner must save the new program to the encrypted offline backup drive and send the customer its own copy. The offline drive is also updated monthly and a restore is tested every quarter. (CP-9; PR.DS-11)
8.6 W-9 forms must be entered in the accounting service and the scans deleted; paper originals are kept in a locked drawer. (SC-28; Fla. Stat. 501.171(2))
8.7 **Disposal and return.** When an MSA ends, the owner must return the customer's programs and data, delete all copies and credentials within 30 days, and confirm in writing. Old USB drives and laptops must be wiped (encrypted, then reset) or destroyed. Each disposal is recorded. (MP-6; ID.AM-08; GV.SC-10; MSA-A (6))
8.8 Security records (this policy, risk assessments, assessments, change logs, session logs, incident records) must be kept for 6 years. (SI-12)

## 9. Acceptable use and field rules
9.1 The laptop is for business use only. Family members must not use it. (PL-4)
9.2 The laptop must be kept out of sight in a locked truck at well sites and taken indoors overnight. (PL-4; PR.AA-06)
9.3 Automatic updates and the built-in antivirus must stay on. Software must come only from the maker's site or the official app store. Configuration software and firmware updates are checked every quarter. (SI-2; SI-3; PR.PS-02)
9.4 Only the two labeled program USB drives may be connected to customer equipment. Each must be scanned on the laptop immediately before each site use. A personal drive must never be connected to customer equipment. (MP-7; DE.CM-09; SP 800-82r3 6.2.1.2)
9.5 The laptop must not connect to a customer network or device if it shows any antivirus alert or unusual behavior. It must never bridge the home network or phone hotspot to a customer network. (SC-7; PR.IR-01)
9.6 **AI tools.** Only the AI tools listed in Appendix A may be used, under the conditions in the P10 assessment. AI output never changes a setpoint or program directly; the owner decides and the customer approves under 8.4. (PL-4; SA-9)
9.7 The owner must complete a basic security course every year and an OT security course once, and read monthly security alerts. (AT-2; AT-3; PR.AT-01; PR.AT-02)

## 10. Incident response
10.1 The business must keep the incident runbook (P08) with a printed contact sheet in the truck and the home office. (IR-8; RS.MA-01)
10.2 Every suspected incident (unknown sign-in, phishing click, lost phone or drive, antivirus alert, unexpected setpoint change, a weakness found in customer equipment) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6)
10.3 Customer A must be notified within 24 hours of discovering any suspected incident that could affect its data or systems, and any other customer whose systems the laptop reached in the last 30 days must be told the same day. (IR-6; RS.CO-02; MSA-A (3))
10.4 Florida notices for the helpers' personal information must meet the deadlines in the P08 notification matrix. (IR-6; Fla. Stat. 501.171(4))
10.5 No ransom may be paid without legal counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-3; ID.IM-03)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner must keep a written mutual coverage agreement with another contract pumper, approved by each customer, and a route sheet per customer in the truck and the home office. (CP-2)
11.3 When a hurricane watch is issued, the owner must confirm the shut-in and restart order with each customer, update the offline backup drive, and keep the laptop, drives, and paper gauge book indoors. (CP-2; PR.IR-02)

## 12. Compliance and enforcement
Compliance is checked in the annual self-assessment (P07) and the monthly review in 7.7. Customer A may check compliance through its questionnaire; answers must be accurate.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P09 SOC 2 self-check; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Approved locations, providers, and software
| Item | Data allowed | Protection required |
|---|---|---|
| Email and file account (SYS-01) | Confidential; Restricted program copies | 7.2 MFA; 7.7 review |
| Accounting service (SYS-02) | Invoices; helper 1099 and W-9 data | 7.2 MFA; 8.6 |
| Password manager | All credentials | 7.3; emergency kit under 7.6 |
| Field laptop (SYS-03) | Restricted and Confidential | 7.4, 7.5, 8.3, 9.1 to 9.5 |
| Smartphone (SYS-04) | Contacts; MFA app; gauge photos | 7.5; remote locate and wipe on |
| Encrypted offline backup drive and 2 labeled program drives (SYS-06) | Restricted program copies | 8.3, 8.5, 9.4 |
| Dynamometer analysis service (SYS-08) | Dynamometer cards by well code only, under P10 conditions | 6.3; 7.2 |
| Configuration software (PLC, RTU, flow meter, pump controller) | Not applicable | 9.3; listed with versions in the device and credential register |
