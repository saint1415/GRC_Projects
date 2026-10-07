# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent recruiter, sole proprietorship) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-recruiter |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new system, a new vendor or AI tool, a first hire, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-28, PL-1, PL-4, PS-8, CM-3, RA-2, RA-3, CA-2, SA-9, AC-2, AC-3, AC-11, AC-17, AC-19, AU-6, IA-2, IA-2(1), IA-5, SC-7, SC-8, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-06, GV.SC-10, ID.AM-07, ID.AM-08, ID.RA-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, DE.CM-03, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Binding rules served | Fla. Stat. 501.171(2) reasonable measures, (3)-(6) notice, (8) disposal; 16 CFR 682.3 (N56-R01); Title VII 703(b) and 703(k) and ADA 12112(b)(6) for screening (section 9.5) |

## 1. Purpose
Protect the personal information that candidates, contractors, and clients trust the business with, keep searches and contractor starts running, and screen candidates fairly, in a way that one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All business information in any form (electronic, paper, spoken) on every system in the Recruiting and Placement Systems Profile (SYS-01 to SYS-10), on paper in the home office, and at every vendor that handles it. It applies to the owner-recruiter and to any future employee or assistant. The outside bookkeeper and the IT support technician are bound through their engagement letter and confidentiality agreement.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead and privacy contact | Owner-recruiter | Runs this policy; decides breach questions; keeps records |
| Risk acceptor | Owner-recruiter | Accepts or treats every risk (4.4) |
| On-call IT support technician | Contractor | Technical help on request; no standing access |
| Outside bookkeeper | Contractor | Accounting SaaS only |
| Back-office partner and SaaS vendors | Service providers | Operate their safeguards; report incidents under their terms (section 6) |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01; Fla. Stat. 501.171(2))
4.2 The owner-recruiter is designated in writing, by this policy, as the security lead and privacy contact. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every July and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. A risk of unlawful discrimination against candidates is never accepted. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every July (P07). At least every second year, someone outside the business, such as the IT support technician, must review the evaluation. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)
4.7 **Change rule.** Before turning on a new tool, a new vendor, or any AI setting that affects candidates (for example, automatic rejection), the owner must write a short risk check in the security log, and for AI, complete a P10 assessment. (CM-3; ID.RA-07)
4.8 Legal and contract duties are tracked in the P03 workbook and reviewed each July. (GV.OC-03)

## 5. Sanctions and exceptions
5.1 Any future employee or assistant who breaks this policy must be sanctioned in proportion to intent and harm: retraining, written warning, or termination, documented and kept 4 years. (PS-8)
5.2 A contractor or vendor that breaks its terms or this policy must be dealt with under its contract, up to ending it. (SA-9)
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. (PL-1)

## 6. Vendors, the back-office partner, and remote support
6.1 Restricted data (8.1) may go only to a vendor whose terms bind it to protect the data, not to use it for its own purposes (including training AI models), and to report a breach. (SA-9; GV.SC-05; Fla. Stat. 501.171(2))
6.2 The owner must keep a vendor list showing each vendor, the data it holds, its criticality, a security contact, and its breach notice terms. (SA-9; GV.SC-04; ID.AM-04)
6.3 Before signing up for a vendor or tool that will hold Restricted or Confidential data, the owner must check: its security page or SOC 2 report, MFA, data use and training terms, deletion on exit, and breach notice. The partner's and the ATS vendor's SOC 2 reports must be reviewed every year. (SA-9; GV.SC-06; GV.SC-07)
6.4 **Exit.** Before ending any service, export the data and confirm deletion in writing. A full ATS export must be saved to the file storage every month, because the ATS vendor deletes data 30 days after a subscription ends. (SA-9; CP-9; GV.SC-10)
6.5 Remote support sessions must be started and watched by the owner. Unattended remote access must not be installed. (AC-17)
6.6 **Bank changes.** The owner must never forward, request, or relay a contractor's bank account change. Contractors are sent to the partner's self-service. Any bank-change request that reaches the owner by email or text is treated as suspected fraud and reported to the partner by phone the same day. (SA-9; IR-6)

## 7. Access control
7.1 Every person must have their own account. Credentials must never be shared, including with the IT technician. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every service that offers it. Where a service offers an authenticator app or a security key, SMS codes must not be used. Email, the ATS, and the partner portal must use the strongest MFA they offer. (IA-2(1); PR.AA-03; Fla. Stat. 501.171(2))
7.3 Passwords must be unique passphrases of at least 14 characters, stored in a password manager, not the browser. Default passwords on devices such as the router must be changed before use. (IA-5)
7.4 The owner must review the account list every quarter, close unused accounts (for example, old job board accounts), and keep the bookkeeper's access to the accounting SaaS only. (AC-2; PR.AA-05)
7.5 The laptop must lock after 5 minutes idle and the phone after 30 seconds. (AC-11)
7.6 **Emergency access.** Recovery codes for email, the ATS, and the partner portal, the laptop disk encryption recovery key, and the location of the continuity sheet must be kept in a sealed envelope held by the owner's attorney. (AC-2; CP-2)
7.7 New-sign-in alerts must be on for email and the ATS. On the first business day of each month the owner must review the email sign-in history and forwarding rules and the ATS export log, and note the review in the security log. (AU-6; DE.CM-03)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | SSNs; dates of birth with names; driver license, passport, and other ID numbers and images; consumer reports and clearance results; bank details; passwords and recovery codes | Approved locations only (8.2); never by email; delete when no longer needed (8.6) |
| **Confidential** | Resumes, candidate notes, compensation, AI scores, client job orders, fee agreements, contractor rates | Business systems only; shared only with the client or partner who needs it |
| **Public** | Job ads, the website | No restriction |

8.2 Restricted data may be kept only in the partner portal (SSNs and dates of birth entered for start requests) and the sealed envelope (recovery codes). It must not be kept in email, the laptop downloads folder, the phone camera roll, the ATS, or any AI tool. (AC-3; SI-12; PR.DS-01)
8.3 SSNs and dates of birth must be entered only in the partner portal or read to the partner by phone. They must never be emailed or texted. Candidates who send ID images or SSNs unprompted get a reply asking them not to, and the item is deleted the same day. (SC-8; PR.DS-02)
8.4 Collect only what the step needs: no SSN, date of birth, or ID at the submittal stage. (SI-12; ID.AM-07)
8.5 Every device that can hold business data must use full-disk encryption. Encrypted data is outside the Florida definition of personal information (Fla. Stat. 501.171(1)(g)2.). (SC-28; PR.DS-01)
8.6 **Retention schedule.** (SI-12; ID.AM-08; Fla. Stat. 501.171(8))

| Record | Keep | Then |
|---|---|---|
| Start forms, SSNs, dates of birth | Not kept after the partner confirms the start request | Delete from all places and empty deleted items |
| Candidate ID images | Not kept | Delete on receipt |
| Consumer reports or clearance details sent by anyone | Not kept | Delete on receipt; record the disposal (8.7) |
| Candidate records in the ATS | 3 years after last activity | Delete |
| AI screening records (scores, settings, rejection lists) | 3 years | Delete |
| Fee agreements, invoices, tax records | 7 years | Shred or delete |

No recordkeeping subpart of 29 CFR Part 1602 is addressed to employment agencies (checked on eCFR 2026-09-23). The 3-year periods are a business choice so the owner can answer a client question or a discrimination charge.
8.7 Paper must be cross-cut shredded. Old laptops and phones must be encrypted, then reset, and the reset recorded before trade-in, or destroyed by a recycler that gives a certificate. Every disposal of consumer information or a device is recorded in the security log. (MP-6; N56-R01 16 CFR 682.3; Fla. Stat. 501.171(8))
8.8 Security documentation (this policy, risk assessments, assessments, incident records) must be kept for at least 5 years. (SI-12)

## 9. Acceptable use and training
9.1 Business devices are for business work. Family members must not use the laptop. (PL-4)
9.2 Devices must never be left in a vehicle or unattended in a public place. (PL-4)
9.3 Automatic updates and the built-in antivirus must stay on. Software must come only from the official app stores or the vendor's site. (SI-2; SI-3)
9.4 Work devices must use the separate work network at home (once set up) or the phone hotspot, not public Wi-Fi without the hotspot. (SC-7)
9.5 **AI tools and fair screening.** (PL-4; SA-9; Title VII 703(b), 703(k); ADA 12112(b)(6))
- An AI tool may process candidate data only after a P10 assessment and with terms that bar training on that data.
- AI scores may sort applicants but must never reject an applicant on their own. Every applicant who meets the job order's minimum requirements gets a human review.
- Job ads must say that software helps sort applications and how to ask for a person to review an application or for an accommodation.
- A client request that refers to a protected trait (for example, age, sex, national origin, or disability) is refused in writing.
- No personal data may be entered into a consumer AI chatbot.
9.6 The owner must complete a security course every year (including payment-fraud and AI-in-hiring topics) and read monthly security alerts. Any future employee or assistant is trained before getting access. (AT-2; PR.AT-01)

## 10. Incident response
10.1 The business must keep an incident runbook (P08) with a printed contact list at home and in the laptop bag. (IR-8; RS.MA-01)
10.2 Every suspected incident (phishing click, unexpected sign-in alert, lost phone, misdirected email, vendor notice, bank-change request) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 For any incident that may involve personal information, the owner must count the people and the data elements involved against the Fla. Stat. 501.171(1)(g) list and record the determination date. (IR-4; RS.AN-08)
10.4 Notices to individuals, the Florida Department of Legal Affairs, consumer reporting agencies, other states, clients, and the partner must meet the deadlines in the P08 notification matrix, confirmed by breach counsel. (IR-6; RS.CO-02; Fla. Stat. 501.171(3)-(5))
10.5 No extortion payment may be made without counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner must keep a one-page continuity sheet (open searches, contractors on assignment, client and partner contacts), updated every Friday, in the file storage and on paper. (CP-2)
11.3 The owner must keep a written arrangement with the partner's account manager to contact clients and contractors if the owner is unavailable for more than 2 business days. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the monthly review in 7.7. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P04 SaaS control map; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P09 SOC 2 self-check and partner report review; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Devices, accounts, and data locations
| Item | Data held | Required settings |
|---|---|---|
| Laptop | Email cache; documents (no Restricted data after the purge) | 8.5 encryption; 7.5 lock; 9.3 updates and antivirus |
| Phone | Email and ATS apps; candidate texts | Passcode; 7.5 lock; no ID photos (8.2); remote erase tested |
| Email and files | Correspondence, resumes, continuity sheet, ATS exports | 7.2 authenticator-app MFA; 7.7 alerts and review |
| ATS with AI match add-on | Candidate records, AI scores | 7.2 MFA; 6.4 monthly export; 9.5 AI settings; training opt-out on |
| Partner portal | Start requests with SSNs and dates of birth | 7.2 strongest available MFA; 6.6 bank-change rule |
| Accounting SaaS | Invoices, bank feed | Vendor-enforced MFA; 7.4 bookkeeper access only |
| Home router | None | 7.3 changed admin password; 9.4 separate work network |
| Paper drawer | Current fee agreements; printed runbook and continuity sheet | Locked; 8.7 shredding |
