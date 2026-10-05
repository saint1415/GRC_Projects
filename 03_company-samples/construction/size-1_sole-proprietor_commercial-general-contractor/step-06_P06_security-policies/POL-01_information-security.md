# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (commercial and institutional building general contractor) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new federal contract or subcontract, a new system or vendor, a hire, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-8, RA-2, RA-3, CA-2, SA-4, SA-9, SR-5, CM-8, MP-3, AC-2, AC-3, AC-20, AC-22, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-28, CP-2, CP-9, MP-6, PE-3, PE-8, SI-2, SI-3, SI-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.DS-01, PR.DS-11, PR.IR-01, PR.PS-02, ID.AM-01, ID.AM-07, ID.AM-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| FAR and CMMC | FAR 52.204-21(b)(1)(i)-(xv), (b)(2), (c); FAR 52.204-25(b), (d), (e); 32 CFR 170.15, 170.22, 170.23 |

## 1. Purpose
Protect the company's money, its clients' drawings, and federal contract information (FCI), and meet FAR 52.204-21 and CMMC Level 1 in a way one person can actually run. Each rule below is written so it can be checked (P07) and, for CMMC, shown with evidence.

## 2. Scope
All company information in any form (electronic, paper, spoken), including FCI, on every system in the Project Management and Payment Application System (SYS-01 to SYS-06), in the external services it uses (SYS-07 to SYS-09), on paper in the home office, truck, and storage unit, and at every vendor and subcontractor that handles it. It applies to the owner and to any future employee. Contractors and subcontractors are bound through their contracts.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead and risk acceptor | Owner | Runs this policy; accepts or treats every risk (4.4); keeps records |
| CMMC Affirming Official | Owner | Affirms Level 1 compliance in SPRS after each self-assessment and every year (4.2) |
| SAM Entity Administrator | Owner | Keeps SAM registration, EFT details, and representations accurate |
| On-call IT technician | Contractor | Technical help on request; outside reader of the yearly assessment (4.5) |
| Outside bookkeeper | Contractor | Works only in a separate accountant-role account (7.1) |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The company must maintain a security program documented in this policy, the system security plan (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The owner is designated in writing, by this policy, as the security lead and as the **CMMC Affirming Official** under 32 CFR 170.22(a)(1). The owner must not affirm in SPRS or sign a SAM representation without the evidence folder that supports it. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every July and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. A risk that could send a payment to the wrong account is always treated. (PM-9; GV.RM-01)
4.5 Controls must be evaluated every July (P07). Before each CMMC self-assessment, the IT technician or another outside person must read the evidence and challenge each Met result. (CA-2; 32 CFR 170.15(c)(1))
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Sanctions and exceptions
5.1 **Sanctions.** Any future employee who breaks this policy must be sanctioned in proportion to intent and harm: retraining, written warning, or termination. Each sanction must be documented. (PS-8; GV.RR-04)
5.2 A contractor, vendor, or subcontractor that breaks its contract or this policy must be dealt with under its contract, up to ending it. (SA-9)
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. No exception may be used to claim a CMMC requirement is Met. (PL-1)

## 6. Vendors, subcontractors, and purchasing
6.1 No vendor may hold FCI unless its terms bar using company data to train or improve its products and allow deletion on request. (SA-9; GV.SC-05; 52.204-21(b)(1)(iii))
6.2 The owner must keep a vendor list showing each vendor, the data it holds, and the date its terms were checked. (SA-9; ID.AM-07)
6.3 The project management vendor's SOC 2 report must be reviewed every year, and the owner must run the customer controls that report lists. (SA-9)
6.4 **Section 889 check.** Before buying or using any phone, hotspot, router, camera, recorder, or other network device, and before approving any such item in a subcontractor submittal for federal work, the owner must confirm the producer is not named in FAR 52.204-25(a) and record the check in the inventory. A documented reasonable inquiry must be completed before each SAM renewal. (SR-5; CM-8; 52.204-25(b); 52.204-26)
6.5 Every subcontract on federal work must include the federal rider with the substance of FAR 52.204-21 and 52.204-25. (SA-4; 52.204-21(c); 52.204-25(e))
6.6 On DoD work, a lower-tier subcontractor gets FCI only if it holds a current CMMC Level 1 (Self) status confirmed in SPRS before award. Otherwise the owner gives the crew only the printed sheets it needs on site and keeps the rest. (SA-4; 32 CFR 170.23(a)(1); DFARS 252.204-7021(f))

## 7. Accounts, passwords, and payments
7.1 Every person must have their own account. Credentials must never be shared. The bookkeeper uses a separate accountant-role account, and family members use a separate standard laptop account. (IA-2; AC-2; PR.AA-01; 52.204-21(b)(1)(i), (v))
7.2 MFA must be on for every service that offers it: email (security key), the project management SaaS (including subcontractor users), the accounting SaaS, the bank, and the government sign-in service. (IA-2(1); IA-2(2); PR.AA-03)
7.3 Passwords must be unique passphrases of at least 14 characters, stored in a password manager. **Default passwords on any device (router, hotspot, printer) must be changed before first use**, and remote administration must stay off. (IA-5; 52.204-21(b)(1)(vi))
7.4 The owner must remove project management users at each job closeout and review all user lists every quarter. Daily laptop work uses a standard account, not the administrator account. (AC-2; AC-3; PR.AA-05; 52.204-21(b)(1)(i)-(ii))
7.5 **Emergency access.** Recovery codes and a one-page access sheet must be kept in a sealed envelope held by the owner's attorney, for use if the owner or the phone is unavailable. (AC-2; CP-2)
7.6 **Bank-detail changes.** A request to change a subcontractor's, supplier's, or client's bank details must be confirmed by calling the number in the signed contract, never a number in the request. The owner then waits 5 business days and confirms a $1 test deposit by phone before sending a full payment to the new account. (AC-3; AT-2)
7.7 Every contract and every pay app cover sheet must state: "We will never change our bank details by email. Call us at the number in this contract before paying to any new account." (AT-2)
7.8 On the first business day of each month, and before sending each pay app, the owner must check email sign-in history and mailbox forwarding and inbox rules, and note the check in the security log. (AU-6; DE.AE-02)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | FCI (federal drawings, submittals, daily logs, pay apps), W-9 forms, bank details, credentials, client security details | Approved locations only (8.2); encrypted; shared only with those who need it |
| **Confidential** | Bids and pricing, private clients' drawings, contracts, tax records | Approved locations; not posted or shared outside the job |
| **Public** | Marketing photos cleared under 9.4, license and insurance certificates | No restriction |

8.2 **Approved locations for Restricted data:** SYS-01, SYS-02, SYS-03, the laptop, and the phone's work apps. Not a personal cloud account, a free file-transfer link, a personal email account, or any AI tool without terms that meet 6.1. Subcontractors must upload to SYS-01. (AC-20; SA-9; 52.204-21(b)(1)(iii); DFARS 252.204-7021(d)(2))
8.3 Every device that can hold Restricted data must use full-disk encryption. (SC-28; PR.DS-01)
8.4 The company does not accept CUI. Every incoming federal document must be checked for CUI markings; if any arrive, the owner stops, does not copy or forward them, and calls the prime contractor or Contracting Officer. (MP-3; 52.204-21(b)(2))
8.5 Laptop work files must be kept in the business file storage with version history on. A quarterly export of SYS-01 pay apps, lien waivers, and daily logs must be saved there. (CP-9; PR.DS-11)
8.6 Before any device is reused, sold, traded in, or thrown away, it must be wiped (encrypted, then factory reset) or destroyed by a recycler that gives a certificate, and the disposal recorded in the disposal log. Paper with Restricted data must be shredded. (MP-6; ID.AM-08; 52.204-21(b)(1)(vii))
8.7 Security records (this policy, risk assessments, CMMC self-assessment evidence, incident records, Section 889 inquiries) must be kept for 6 years. (SI-12; 32 CFR 170.15(c)(2))

## 9. Physical security and acceptable use
9.1 Company devices are for company work. Family members use their own devices or the separate family account. (PL-4; 52.204-21(b)(1)(i))
9.2 The home office door must be locked when the owner is away. Non-household visitors to the home office must be escorted at all times and signed in on the paper visitor log, kept 1 year. Keys and codes (office, storage unit, jobsite lockboxes) must be listed, and changed when a key is lost or a person who held one leaves the job. (PE-3; PE-8; PR.AA-06; 52.204-21(b)(1)(viii)-(ix))
9.3 Automatic updates and the built-in antivirus must stay on. The router firmware must be checked every quarter. Software must come only from official app stores or the vendor's site. (SI-2; SI-3; PR.PS-02; 52.204-21(b)(1)(xii)-(xv))
9.4 Before posting any photo from a federal job, the owner must check that no drawing, floor plan, badge, or security feature is visible. Past posts are reviewed each quarter. (AC-22; 52.204-21(b)(1)(iv))
9.5 Work devices use the separate work network at home and phone tethering at jobsites. Family and smart-home devices stay on the guest network. Public Wi-Fi is not used for banking or SAM. (SC-7; PR.IR-01; 52.204-21(b)(1)(x))
9.6 **AI tools.** An AI tool may receive Restricted or Confidential data only after a written assessment (P10) and terms that meet 6.1. Its output is a draft: the owner checks every quantity and price before it goes into a bid. (PL-4; SA-9)
9.7 The owner must complete a basic cybersecurity course and a payment fraud module every year. Any future employee must be trained before getting access. (AT-2; PR.AT-01)
9.8 Plan sets and the laptop must not be left visible in the truck; plan sets go in the locked truck box. (PE-3)

## 10. Incident response
10.1 The company must keep an incident runbook (P08) with a printed contact card in the truck and the home office. (IR-8; RS.MA-01)
10.2 Every suspected incident (a strange sign-in alert, a bank-change request that fails call-back, a lost phone, a payment that did not arrive) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 **Money first.** If a payment may have gone to the wrong account, the owner must call the bank's fraud line to request a recall before doing anything else. (IR-4)
10.4 If covered telecommunications or video surveillance equipment is found during federal contract performance, the owner must report to the Contracting Officer (DoD: dibnet.dod.mil) within 1 business day and send mitigation details within 10 business days. (IR-6; RS.CO-02; 52.204-25(d))
10.5 Notices to individuals, the Florida Department of Legal Affairs, clients, and federal contacts must meet the deadlines in the P08 notification matrix, confirmed by counsel. (IR-6; RS.CO-02)
10.6 No ransom may be paid without counsel's advice and an OFAC sanctions check. (IR-4)
10.7 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner must keep a written standby agreement with another small general contractor to supervise active jobsites for up to 2 weeks if the owner is unavailable. (CP-2)
11.3 Current plan sets for each active job must be kept printed in the truck. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the yearly control assessment (P07), the CMMC Level 1 self-assessment, and the monthly check in 7.8. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system security plan; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Devices and data locations
| Item | Restricted data held | Protection required |
|---|---|---|
| Laptop | Estimates, pay app drafts, scanned lien waivers, W-9 forms | 7.1, 8.3, 8.5, 9.3 |
| Phone | Email, photos, every second factor | 7.5, 8.2, 8.3 |
| SYS-01 project management | FCI and private drawings | 7.2, 7.4 |
| SYS-02 accounting | Vendor bank details, W-9 forms | 7.1, 7.2, 7.6 |
| SYS-03 email and files | Pay apps, correspondence, backups (8.5) | 7.2, 7.8 |
| Home office file cabinet and truck box | Signed subcontracts, certified payroll copies, plan sets | 9.2, 9.8, 8.6 |
