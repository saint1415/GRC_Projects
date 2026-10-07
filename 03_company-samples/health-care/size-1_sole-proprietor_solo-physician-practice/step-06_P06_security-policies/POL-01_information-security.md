# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (solo primary care physician practice) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Physician-owner |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk analysis, and after a new system, a new vendor, a hire, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-8, RA-2, RA-3, CA-2, SA-9, AC-2, AC-3, AC-11, AC-17, AC-19, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-8, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-07, ID.AM-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| HIPAA Security Rule | 164.308(a)(1)-(8), 164.308(b)(1); 164.310; 164.312; 164.314(a); 164.316 |

## 1. Purpose
Protect the confidentiality, integrity, and availability of patient information and practice information, and meet the HIPAA Security Rule in a way that one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All practice information in any form (electronic, paper, spoken), including electronic protected health information (ePHI), on every system in the Practice Systems Profile (SYS-01 to SYS-07), on paper in the exam suite, and at every vendor that handles it. It applies to the physician-owner and to any future employee, student, or volunteer. Contractors are bound through their contracts and BAAs.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security Officer and Privacy Officer | Physician-owner | Runs this policy; decides breach questions; keeps records |
| Risk acceptor | Physician-owner | Accepts or treats every risk (section 4.4) |
| On-call IT consultant (BA) | Contractor | Technical help on request; no standing access |
| Vendors with a BAA | EHR vendor, billing company, cloud fax vendor, IT consultant | Operate their safeguards; report incidents under the BAA |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The practice must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01; 164.316(a))
4.2 The physician-owner is designated in writing, by this policy, as the practice's Security Officer and Privacy Officer. (PM-2; GV.RR-02; 164.308(a)(2))
4.3 A risk analysis must be completed every July and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9; 164.308(a)(1)(ii)(A)-(B))
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every July (P07). At least every second year, the evaluation must include review by someone outside the practice, such as the IT consultant under BAA. (CA-2; 164.308(a)(8))
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02; 164.316(b)(2)(iii))

## 5. Sanctions and exceptions
5.1 **Sanctions.** Any future employee, student, or volunteer who breaks this policy must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. Each sanction must be documented and kept for 6 years. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))
5.2 A contractor or vendor that breaks its BAA or this policy must be dealt with under its contract, up to ending the contract. (SA-9)
5.3 The owner must record any personal departure from this policy as an exception under 5.4, with the reason and the fix.
5.4 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. (PL-1)

## 6. Vendors and business associates
6.1 **No BAA, no PHI.** No vendor may create, receive, maintain, or transmit PHI for the practice until a BAA is signed. This includes email, file storage, answering, IT support, and AI tools. (SA-9; GV.SC-05; 164.308(b)(1); 164.314(a))
6.2 The owner must keep a vendor list showing each vendor, the PHI it handles, and the BAA date. (SA-9; ID.AM-07)
6.3 The EHR vendor's SOC 2 report must be reviewed every year, and the owner must operate the customer controls that report lists. (SA-9; GV.SC-07)
6.4 Remote support sessions must be started and watched by the owner. Unattended remote access must be off. (AC-17; 164.308(a)(3)(ii)(A))

## 7. Access control
7.1 Every person must have their own account. Credentials must never be shared. (IA-2; AC-2; PR.AA-01; 164.312(a)(2)(i))
7.2 MFA must be on for every service that holds PHI and offers it: the EHR, email and files, and the cloud fax portal. (IA-2(1); IA-2(2); PR.AA-03; 164.312(d))
7.3 Passwords must be unique passphrases of at least 14 characters, stored in a password manager. (IA-5; 164.308(a)(5)(ii)(D))
7.4 The owner must approve each billing company account in writing, remove it the same day the billing company reports a departure, and review the EHR user list every quarter. (AC-2; PR.AA-05; 164.308(a)(4)(ii)(B)-(C); 164.308(a)(3)(ii)(C))
7.5 Laptop and tablet must lock after 5 minutes idle; the phone after 1 minute. (AC-11; 164.312(a)(2)(iii))
7.6 **Emergency access.** EHR and email recovery codes and a one-page access sheet must be kept in a sealed envelope held by the owner's attorney, for use if the owner or the owner's phone is unavailable. (AC-2; 164.312(a)(2)(ii))
7.7 On the first clinic day of each month, the owner must review the EHR audit log and the email sign-in history and note the review in the security log. (AU-6; DE.AE-02; 164.308(a)(1)(ii)(D); 164.308(a)(5)(ii)(C))

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | PHI, clinical photos, visit audio, credentials | Approved systems only (8.2); encrypted; minimum necessary |
| **Confidential** | Contracts, tax and bank records, this policy set | Encrypted storage; owner only |
| **Public** | Office hours, website | No restriction |

8.2 Restricted data may be kept only in: the EHR, the business-grade file plan covered by a BAA, and the cloud fax account. It must not be kept in a personal account, a phone camera roll, or a consumer app. (AC-3; SA-9)
8.3 Every device that can hold Restricted data must use full-disk encryption. (SC-28; PR.DS-01; 164.312(a)(2)(iv))
8.4 Patients must not be sent PHI by ordinary text message. Use the EHR portal. Appointment reminders with no clinical content are allowed. (SC-8; PR.DS-02; 164.312(e)(1))
8.5 Clinical photos must be taken with the EHR mobile app or uploaded to the chart the same day and then deleted from the phone. (SC-28; CP-9; 164.308(a)(7)(ii)(A))
8.6 Files that are not in the EHR must be kept in the business file plan with version history on, so they can be restored. (CP-9; PR.DS-11; 164.310(d)(2)(iv))
8.7 Paper with PHI must go in the locked building shredding bin. Old devices must be wiped (encrypted, then reset) before reuse or trade-in, or destroyed by a recycler that gives a certificate. Each disposal is recorded. (MP-6; ID.AM-08; 164.310(d)(2)(i)-(ii))
8.8 Security documentation (this policy, risk analyses, assessments, incident records, BAAs) must be kept for 6 years from creation or last effective date, whichever is later. (SI-12; 164.316(b)(2)(i))

## 9. Acceptable use and training
9.1 Practice devices are for practice work. Family members must not use them. (PL-4; 164.310(b))
9.2 Devices must never be left in a vehicle or unattended outside the locked suite or the owner's home. (PL-4; 164.310(c))
9.3 Automatic updates and the built-in antivirus must stay on. Software must come only from the official app stores or the vendor's site. (SI-2; SI-3; 164.308(a)(5)(ii)(B))
9.4 Practice work in the suite must use the practice's own network or the phone hotspot, not the shared building network. (SC-7; 164.312(e)(1))
9.5 **AI tools.** An AI tool may process PHI only after a written assessment (P10), a signed BAA, and the owner's written approval. A visit may be recorded only with every party's prior consent (Fla. Stat. 934.03), documented in the chart. (PL-4; SA-9; 164.308(b)(1))
9.6 The owner must complete a HIPAA security course every year and read monthly security reminders. Any future workforce member must be trained before getting access. (AT-2; PR.AT-01; 164.308(a)(5))

## 10. Incident response
10.1 The practice must keep an incident runbook (P08) with a printed contact list in the suite and at home. (IR-8; RS.MA-01; 164.308(a)(6))
10.2 Every suspected incident (lost device, phishing click, misdirected fax, vendor notice) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02; 164.308(a)(6)(ii))
10.3 For any incident involving PHI, the owner must complete and keep the four-factor breach risk assessment in 45 CFR 164.402. (IR-6)
10.4 Notices to patients, HHS, the media, and the Florida Department of Legal Affairs must meet the deadlines in the P08 notification matrix, confirmed by legal counsel. (IR-6; RS.CO-02; 164.404-164.408)
10.5 No ransom may be paid without legal counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01; 164.308(a)(7)(ii)(E))
11.2 The owner must keep a written coverage arrangement with a nearby physician for urgent patient needs and refills when the owner is unavailable. (CP-2; 164.308(a)(7)(ii)(C))
11.3 The next clinic day's schedule must be printed each evening, and paper visit-note forms kept in the suite for EHR outages. (CP-2; 164.308(a)(7)(ii)(C))

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the monthly review in 7.7. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Devices and data locations (164.310(d)(2)(iii))
| Item | Restricted data held | Protection required |
|---|---|---|
| Laptop | EHR downloads, documents | 8.3, 7.5, 9.3 |
| Tablet | EHR session cache | 8.3, 7.5 |
| Phone | EHR second factor; photos until uploaded | 8.3, 8.5, 7.5 |
| EHR/PM | The medical record | BAA; 7.2 |
| Business file plan (replacing the consumer account) | Documents | BAA; 7.2; 8.6 |
| Cloud fax | Faxes | BAA; 7.2 |
| Paper cabinet in the suite | Signed forms | Locked; 8.7 |
