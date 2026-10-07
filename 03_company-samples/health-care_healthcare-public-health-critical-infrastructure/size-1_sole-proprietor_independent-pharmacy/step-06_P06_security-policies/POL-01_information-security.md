# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent community pharmacy) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Pharmacist-owner |
| Effective date | 2026-09-08 (adopted 2026-09-04) |
| Review cycle | Every August with the risk analysis, and after a new system or vendor, a change of PMS, a hire, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-3, PS-4, PS-6, PS-8, RA-2, RA-3, CA-2, SA-4, SA-9, AC-2, AC-3, AC-6, AC-11, AC-17, AC-19, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-8, SC-12, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, GV.SC-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, PR.IR-01, PR.PS-02, ID.AM-07, ID.AM-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| HIPAA Security Rule | 164.308(a)(1)-(8), 164.308(b)(1); 164.310; 164.312; 164.314(a); 164.316 |
| DEA | 21 CFR 1311.200, 1311.215(c), 1311.305; 21 CFR 1311.30 (CSOS) |

## 1. Purpose
Protect the confidentiality, integrity, and availability of patient information, prescription records, and controlled substance records, and meet the HIPAA Security Rule and the DEA electronic prescription and ordering rules in a way that one pharmacist can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All pharmacy information in any form (electronic, paper, spoken), including electronic protected health information (ePHI) and controlled substance records, on every system in the Pharmacy Core SaaS Stack (SYS-01 to SYS-08), on paper in the store, and at every vendor that handles it. It applies to the pharmacist-owner and the relief pharmacist (a workforce member), and to any future employee. Vendors are bound through their contracts and BAAs.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security Officer and Privacy Officer | Pharmacist-owner | Runs this policy; decides breach and DEA reporting questions; keeps records |
| Risk acceptor | Pharmacist-owner | Accepts or treats every risk (section 4.4) |
| PMS administrator and CSOS certificate holder | Pharmacist-owner | Sets PMS roles and access; the only person who uses the CSOS key |
| Relief pharmacist | Independent contractor (workforce member) | Follows this policy on relief days; reports incidents to the owner the same day |
| On-call IT consultant (BA) | Contractor | Technical help on request; no standing access |
| Vendors with a BAA | PMS vendor, cloud fax vendor, IT consultant, and the email and file suite vendor once its BAA is accepted | Operate their safeguards; report incidents under the BAA |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The pharmacy must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01; 164.316(a))
4.2 The pharmacist-owner is designated in writing, by this policy, as the pharmacy's Security Officer and Privacy Officer. (PM-2; GV.RR-02; 164.308(a)(2))
4.3 A risk analysis must be completed every August and after any major change (including a new PMS or a new vendor that handles PHI), using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9; 164.308(a)(1)(ii)(A)-(B))
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. A risk to patient safety must not be accepted above Low. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every August (P07). At least every second year, the evaluation must include review by someone outside the pharmacy, such as the IT consultant under BAA. (CA-2; 164.308(a)(8))
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02; 164.316(b)(2)(iii))

## 5. Sanctions and exceptions
5.1 **Sanctions.** A workforce member (the relief pharmacist or any future employee) who breaks this policy must be sanctioned in proportion to intent and harm: retraining, written warning, ending the engagement, or a report to the licensing board where the law requires it. Each sanction must be documented and kept for 6 years. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))
5.2 The relief pharmacist's contract must include a confidentiality and security clause that points to this policy. (PS-6)
5.3 A vendor that breaks its BAA or this policy must be dealt with under its contract, up to ending the contract. (SA-9)
5.4 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. The owner must record any personal departure from this policy the same way. (PL-1)

## 6. Vendors and business associates
6.1 **No BAA, no PHI.** No vendor may create, receive, maintain, or transmit PHI for the pharmacy until a BAA is in effect. This includes email, file storage, fax, IT support, and AI tools. (SA-9; GV.SC-05; 164.308(b)(1); 164.314(a))
6.2 The owner must keep a vendor list showing each vendor, the PHI it handles, and the BAA date. (SA-9; ID.AM-07)
6.3 Every year the owner must review the PMS vendor's SOC 2 report and operate the customer controls it lists. (SA-9; GV.SC-07)
6.4 **EPCS certification.** The owner must keep the PMS vendor's current EPCS third-party audit or certification report, read each new one, and confirm it finds the application compliant before relying on it. (SA-4; 21 CFR 1311.200(a)-(b))
6.5 If the PMS vendor says the application is no longer EPCS-compliant, the pharmacy must stop processing controlled substance prescriptions in it at once and resume only when the vendor confirms compliance and the updates are installed. (SA-9; 21 CFR 1311.200(c)-(d))
6.6 **Vendor remote support** must be in attended mode: the owner accepts each session, watches it, and records it in the security log. Unattended access must stay off. (AC-17; 164.308(a)(3)(ii)(A))

## 7. Access control
7.1 Every person must have their own account on the PMS, the desktop, and every other system. Credentials must never be shared or written down at the counter. (IA-2; AC-2; PR.AA-01; 164.312(a)(2)(i); 21 CFR 1311.205(b)(10))
7.2 MFA must be on for every service that holds PHI and offers it, including the PMS administrator role at every location, the email and file suite, and the cloud fax portal. (IA-2(1); IA-2(2); PR.AA-03; 164.312(d))
7.3 Passwords must be unique passphrases of at least 14 characters, stored in a password manager. (IA-5; 164.308(a)(5)(ii)(D))
7.4 **Who may dispense and annotate controlled substance prescriptions:** the pharmacist-owner and the relief pharmacist, each under their own account with the PMS pharmacist role. Only the owner holds the administrator role, and uses it only to change settings. The owner must create an account only after recording a license check, remove it the day an engagement ends, and review the PMS user list every quarter. (AC-2; AC-6; PR.AA-05; 164.308(a)(3)(ii)(B)-(C); 164.308(a)(4)(ii)(B)-(C); 21 CFR 1311.200(e))
7.5 The desktop and laptop must lock after 3 minutes idle (desktop) or 5 minutes (laptop), and the phone after 1 minute. The PMS session must time out after 15 minutes. (AC-11; 164.312(a)(2)(iii))
7.6 **Emergency access.** Recovery codes and a one-page emergency access sheet must be kept in a sealed envelope held by the owner's attorney, for use if the owner or the owner's phone is unavailable. (AC-2; 164.312(a)(2)(ii))
7.7 **Reviews.** Each business morning, the pharmacist on duty must read the PMS's daily EPCS audit report and decide whether any listed event is a security incident (10.4). On the first business day of each month, the owner must review the PMS sign-in report and the email sign-in history. Each review is noted in the security log. (AU-6; DE.AE-02; 164.308(a)(1)(ii)(D); 164.308(a)(5)(ii)(C); 21 CFR 1311.215(c))
7.8 **CSOS key.** Only the owner may use the CSOS private key, which must be kept only under the owner's own desktop account and never copied. (SC-12; 21 CFR 1311.30(a)-(d))

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | PHI, prescriptions, controlled substance records, compounding records with patient names, credentials, the CSOS key | Approved systems only (8.2); encrypted; minimum necessary |
| **Confidential** | Contracts, PBM agreements, tax and bank records, this policy set | Encrypted storage; owner only |
| **Public** | Store hours, price list, website | No restriction |

8.2 Restricted data may be kept only in: the PMS, the email and file suite once its BAA is in effect, and the cloud fax account. It must not be kept in a personal account, a phone camera roll, or a consumer app. (AC-3; SA-9)
8.3 Every device that can hold Restricted data must use full-disk encryption. (SC-28; PR.DS-01; 164.312(a)(2)(iv))
8.4 Patients must not be sent PHI by ordinary text message or email. Refill reminders may say only that a prescription is ready. (SC-8; PR.DS-02; 164.312(e)(1))
8.5 Reports downloaded from the PMS must be deleted from the desktop when no longer needed, and patient list exports must not be kept on any device. (SC-28; MP-6)
8.6 Before a device is moved, repaired, or replaced, any local data that is not in the PMS or the file suite must be copied to the file suite. Master formulation records must also be kept as a printed binder at the compounding bench. (CP-9; PR.DS-11; 164.310(d)(2)(iv))
8.7 Paper with PHI must be cross-cut shredded. Old devices must be wiped (encrypted, then reset) before reuse or trade-in, or destroyed by a recycler that gives a certificate. Each disposal is recorded. (MP-6; ID.AM-08; 164.310(d)(2)(i)-(ii))
8.8 Security documentation (this policy, risk analyses, assessments, incident records, BAAs, review logs) must be kept for 6 years from creation or last effective date, whichever is later. Controlled substance records are kept as DEA and Florida law require, at least 2 years (21 CFR 1311.305; Fla. Stat. 893.07). (SI-12; 164.316(b)(2)(i))

## 9. Acceptable use and training
9.1 Pharmacy devices are for pharmacy work. No personal browsing or personal accounts on the counter desktop. (PL-4; 164.310(b))
9.2 The desktop screen must face away from the counter. Devices must never be left in a vehicle or unattended outside the locked store or the owner's home. (PL-4; 164.310(c))
9.3 Automatic updates and the built-in antivirus must stay on. Daily work uses standard (non-administrator) desktop accounts. Software must come only from the official stores or the vendor's site. (SI-2; SI-3; AC-6; 164.308(a)(5)(ii)(B))
9.4 The pharmacy network must be separate from customer Wi-Fi and from the camera recorder. The Wi-Fi password for the pharmacy network must not be shared or posted. (SC-7; 164.312(e)(1))
9.5 **AI tools.** No PHI or patient details may be entered into any AI tool unless a written assessment (P10), a BAA, and the owner's written approval are in place. No AI tool may be used to perform or check compounding calculations, doses, or formulations; those are checked against the master formulation record and a standard reference. AI may be used for general drafting with no patient information, and every output is reviewed before use. (PL-4; SA-9; 164.308(b)(1))
9.6 Both pharmacists must complete a HIPAA security course every year, and the owner must read monthly security reminders. Any future workforce member must be trained before getting access. (AT-2; PR.AT-01; 164.308(a)(5))

## 10. Incident response
10.1 The pharmacy must keep an incident runbook (P08) with a printed contact list in the store and at home. (IR-8; RS.MA-01; 164.308(a)(6))
10.2 Every suspected incident (vendor outage notice, lost device, phishing click, misdirected fax, unexpected remote session, odd EPCS audit event) must be written in the incident log the same day, with the time it was discovered. The relief pharmacist must report it to the owner the same day. (IR-5; IR-6; RS.MA-02; 164.308(a)(6)(ii))
10.3 For any incident involving PHI, the owner must complete and keep the four-factor breach risk assessment in 45 CFR 164.402. (IR-6)
10.4 **DEA EPCS report.** When the pharmacy determines that an event could have compromised the integrity of controlled substance prescription records, it must report to the PMS vendor and DEA within one business day (21 CFR 1311.215(c)). (IR-6; RS.CO-02)
10.5 **CSOS key.** Loss, theft, or compromise of the CSOS key or its password must be reported to the certificate authority by a revocation request within 24 hours of substantiation (21 CFR 1311.30(e)). (IR-6; SC-12)
10.6 Notices to patients, HHS, the media, the Florida Department of Legal Affairs, and others must meet the deadlines in the P08 notification matrix, confirmed by legal counsel. (IR-6; RS.CO-02; 164.404-164.408)
10.7 No ransom may be paid without legal counsel's advice and an OFAC sanctions check. The runbook must be walked through every year and after any real incident, and lessons learned recorded within 30 days of closing an incident. (IR-3; IR-4; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01; 164.308(a)(7)(ii)(E))
11.2 **Downtime kit.** The pharmacy must keep a paper downtime kit in the locked prescription cabinet: an active-patient medication list printed every Friday, blank labels and a label template, paper dispensing and controlled substance logs, and the printed contact list. (CP-2; 164.308(a)(7)(ii)(C))
11.3 The owner must keep a written arrangement with a nearby pharmacy to take patient transfers when the store must close, and a written plan for the relief pharmacist to cover if the owner is unavailable. (CP-2; 164.308(a)(7)(ii)(C))
11.4 During a PMS outage, controlled substances are dispensed only as P08 allows, every dispensing is logged on paper, PDMP reports are kept current by the close of the next business day or an extension is requested, and duplicate electronic prescriptions are checked when the PMS returns. (CP-2; 21 CFR 1311.200(g); Fla. Stat. 893.055(3)(a))

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and in the reviews in 7.7. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P09 SOC 2 self-check and vendor review; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Devices, data locations, and facility protection (164.310(a)(2)(ii); 164.310(d)(2)(iii))
| Item | Restricted data held | Protection required |
|---|---|---|
| Counter desktop | PMS sessions; scanned prescriptions until filed; CSOS key (owner's account only) | 8.3, 7.5, 7.8, 9.3 |
| Laptop | PMS web access; email; downloads | 8.3, 7.5 |
| Phone | Second factor; email | 8.3, 7.5 |
| PMS | Prescriptions, profiles, controlled substance records, claims | BAA; 7.1, 7.2, 7.4 |
| Email and file suite | Fax copies; compounding records | BAA (accept); 7.2; 8.6 |
| Cloud fax | Faxes | BAA; 7.2 |
| Locked cabinets in the prescription department | Paper prescriptions; controlled substances; downtime kit | Locked; keys and alarm codes held only by the two pharmacists |
| Store | All of the above | Locked and alarmed after hours; camera; public kept out of the prescription department |
