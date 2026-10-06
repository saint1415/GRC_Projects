# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent GovTech consultant) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-consultant |
| Effective date | 2026-09-16 (adopted 2026-09-15) |
| Review cycle | Every August with the risk assessment, and after a new agency client, a new system or AI tool, a new CJIS Security Policy version, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PL-1, PL-4, PL-4(1), PM-9, RA-2, RA-3, CA-2, CA-7, PS-3, PS-6, PS-7, SA-3, SA-4, SA-9, SA-10, AC-2, AC-3, AC-6, AC-11, AC-12, AC-17, AC-18, AC-20, AC-22, AU-6, AU-11, IA-2, IA-2(1), IA-2(2), IA-5, CM-7, CM-12, SC-7, SC-28, CP-2, CP-9, MP-4, MP-6, MP-7, MA-2, MA-4, PE-2, PE-17, SI-2, SI-3, SI-12, SR-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.SC-07, ID.AM-07, ID.AM-08, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-11, PR.PS-02, PR.IR-01, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Contract and legal basis | County contract (SP 800-53 Rev. 5 Moderate clause); CJIS Security Addendum sec. 3.01 (N92-R02, CJISSECPOL v6.1); Fla. Stat. 501.171(2) and (6)(a) |

## 1. Purpose
Protect agency data the owner touches, keep the owner's access from becoming a path into agency systems, and meet each agency's contract and the CJIS Security Policy in a way one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All information the business handles in any form, and especially agency data (county extracts, city applications, CJI seen in the sheriff's virtual desktop), on every part of the Consulting Delivery Environment (SYS-01 to SYS-04, SYS-06 to SYS-09) and in the owner's use of agency accounts (SYS-05). It applies to the owner-consultant and to anyone the owner ever hires or subcontracts. The on-call IT technician is bound through the NDA and section 6.4.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security officer, privacy contact, incident handler | Owner-consultant | Runs this policy; reports to agencies; keeps records |
| Risk acceptor | Owner-consultant | Accepts or treats every risk (4.4) |
| On-call IT technician | Contractor under NDA | Technical help on request; no standing access |
| Agency security contacts | County IT security officer, city IT director, sheriff's LASO | Grant and remove the owner's agency access; receive reports (10.2) |

One person writes, follows, and checks these rules, so independence is limited. Rule 4.5 adds an outside check every second year.

## 4. Governance and risk
4.1 The owner must keep a security program documented in this policy, the system profile (P02), and the risk register (P01). For the sheriff work, this is the "security program consistent with ... the CJIS Security Policy" that Security Addendum sec. 3.01 requires. (PL-1; GV.PO-01)
4.2 The owner is the designated security officer and privacy contact for every agency contract. (GV.RR-02)
4.3 A risk assessment must be completed every August and after any major change, using NIST SP 800-30 Rev. 1. Every risk gets a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan, never accepted as they are. Any risk that could expose CJI is treated whatever its level. (PM-9; GV.RM-01)
4.5 Controls must be self-assessed every August (P07). At least every second year, someone outside the business (the IT technician or a peer consultant) reviews the assessment. (CA-2; CA-7)
4.6 This policy is reviewed every year and after the events in the review cycle above. Every change to a security setting is noted in the security log with the date. (PL-1; GV.PO-02)

## 5. People, agreements, and exceptions
5.1 Before getting access to an agency's data, the owner signs whatever access agreement the agency requires (county acceptable use agreement, city confidentiality terms, CJIS Security Addendum certification) and completes any screening it requires. (PS-6; PS-3)
5.2 Anyone else who may see agency data (the IT technician, any future hire or subcontractor) must sign an NDA first, and must never see CJI unless the sheriff has screened and approved them. (PS-7)
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and expire within 12 months. No exception may allow CJI outside the sheriff's virtual desktop. (PL-1)

## 6. Agency access and providers
6.1 **No agreement, no agency data.** No service may hold, process, or see agency data unless it is on the approved list in Appendix A and, where the agency asks for one, the agency has approved it in writing. This includes AI tools. (SA-9; GV.SC-05)
6.2 Agency systems are reached only through the path each agency provides: county single sign-on, the city's 311 sign-in, and the sheriff's virtual desktop with its hardware token. No saved agency passwords in the browser. (AC-17)
6.3 The owner keeps a provider list (P04) showing what each provider holds, its security and breach notice terms, and when it was last reviewed. Each provider that may hold agency data is reviewed every August; the productivity suite's SOC 2 report is read every year (P09). Before buying any new service that may hold agency data, the owner checks data use, data location, breach notice, and MFA. (SA-4; SA-9; GV.SC-07)
6.4 Remote support sessions are started and watched by the owner and closed when the work ends. Before any repair or remote session, agency data is moved off the laptop or the session stays out of agency folders. (MA-4; PS-7)

## 7. Access control
7.1 One named account per person per service. Credentials are never shared. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every service that offers it, including the website builder. The owner asks every agency that does not offer contractor MFA to add it. (IA-2(1); IA-2(2); PR.AA-03)
7.3 Daily work on the laptop uses a standard account. The administrator account is used only to install or change software. (AC-6; PR.AA-05)
7.4 Passwords are unique, generated by the password manager, and at least 16 characters for the password manager's master passphrase and the laptop. Default passwords (router, new devices) are changed on day one. (IA-5)
7.5 The laptop locks after 10 minutes idle and the phone after 1 minute. The owner locks the laptop before walking away from it anywhere outside the home office. This is inside the CJIS 30-minute maximum. (AC-11)
7.6 The owner signs out of each agency system at the end of each work session, and the browser clears agency site sessions on close. (AC-12)
7.7 On the first working day of each month, the owner reviews the productivity suite sign-in history and sharing report, the password manager alerts, and the account list, and notes the review in the security log. After any incident, the review is weekly for 3 months. (AU-6; AC-2; DE.AE-02)
7.8 **Emergency access.** Recovery codes for the productivity suite, password manager, and accounting service, the laptop disk recovery key, and the printed agency contact sheet are kept in a sealed envelope held by the owner's attorney. The attorney gets no access to agency systems or data. (AC-2; CP-2)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Agency Restricted** | CJI, county extracts, city applications, anything with Social Security or driver license numbers | Only where 8.2 allows; encrypted; deleted on the contract date |
| **Confidential** | Contracts, invoices, credentials, this policy set | Business cloud storage or password manager; owner only |
| **Public** | Website, service descriptions | No restriction |

8.2 **Where agency data may live.** County and city data: only the laptop's agency folder, the matching folder in business cloud storage, and the agency's own systems. **CJI: only inside the sheriff's virtual desktop. Never copied, printed, photographed, or saved anywhere else.** (AC-20; AC-3; CJISSECPOL v6.1 AC-20, SC-28)
8.3 Every device that can hold agency data uses full-disk encryption. The only removable drive allowed with the laptop is the owner's encrypted backup drive, which never leaves the home office and is kept in the locked file box. (SC-28; MP-4; MP-7; PR.DS-01)
8.4 The owner keeps a data location log for each agency: what was received, when, where it is stored, and when it was deleted. Every quarter the owner searches the laptop and cloud storage for agency data that is not in the log. (CM-12; ID.AM-07)
8.5 Agency data is kept only as long as the contract allows (county: 30 days after each phase is accepted). Deletion covers the laptop, the cloud folder and recycle bin, and the backup drive, and ends with a written deletion certificate to the agency. (SI-12; MP-6; ID.AM-08)
8.6 Before a device is repaired, sold, or disposed of, agency data is removed and the device is wiped. A device that ever held CJI is sanitized to the CJIS standard (overwrite at least three times, or destroyed if inoperable) with the LASO told first. Paper with agency data is cross-cut shredded. Each disposal is recorded. (MP-6; MA-2; SR-12)
8.7 Security records (this policy, risk assessments, assessments, incident logs, deletion certificates, monthly review notes) are kept for at least 3 years, or longer where a contract requires it. (SI-12; AU-11)

## 9. Acceptable use and training
9.1 Work devices are for work only. Family members do not use them. (PL-4)
9.2 Agency work is done only in the home office or at a client office, never on public Wi-Fi (use the phone hotspot). The home office door is locked when the owner is away. Work devices use a separate work Wi-Fi network, never the family network. (PE-17; PE-2; SC-7; AC-18)
9.3 Automatic updates and the built-in antivirus stay on. Software comes only from official stores or the vendor's site. Unused software and browser extensions are removed each quarter. Router firmware is checked each quarter. (SI-2; SI-3; CM-7)
9.4 Scripts and report logic are developed and tested with test data or inside the agency's own test environment, reviewed before handover, and kept under version control with an off-device copy. (SA-3; SA-10; CP-9)
9.5 **AI tools.** No agency data, of any level, goes into any AI tool unless the tool is on the Appendix A list for that agency, the agency has approved it in writing, and a P10 assessment is done. No AI tool may decide or recommend who is eligible for a public benefit. (PL-4; SA-9; AC-20)
9.6 The owner completes a security course every year (with phishing practice and administrator topics) and reads monthly reminders. The sheriff's CJIS training is completed before access, every year, and within 30 days after any incident the owner is involved in (CJISSECPOL v6.1 AT-2). (AT-2; PR.AT-01)
9.7 No agency data, screenshots, or details that identify an agency's internal systems are posted on the website or social media. (PL-4(1); AC-22)

## 10. Incident response
10.1 The owner keeps the P08 runbook and the printed agency contact sheet in the locked file box and with the attorney. (IR-8; RS.MA-01)
10.2 **Reporting clocks.** Every suspected incident is written in the incident log the same day with the time it was found, and reported:
- to the sheriff's LASO **within 1 hour** if it could involve CJI or the sheriff's access (CJISSECPOL v6.1 IR-6; Security Addendum);
- to the county IT security officer **within 24 hours** if it could involve county data or access (county contract);
- to the city IT director **the same business day** if it could involve city data or access (city contract: "promptly");
- and, once a breach of personal information is determined, to the affected agency with all the facts it needs **no later than 10 days** after the determination (Fla. Stat. 501.171(6)(a)). Earlier contract clocks always win. (IR-6; IR-5; RS.MA-02; RS.CO-02)
10.3 The owner does not decide whether an agency must notify individuals; the agency does. The owner gives the agency what it needs, including counts and states of residence where known. (IR-6)
10.4 No ransom is paid without counsel, the insurer, an OFAC sanctions check, and the agreement of every affected agency. The county and city may not pay a ransom (Fla. Stat. 282.3186). (IR-4)
10.5 The runbook is walked through every year and after any real incident. Lessons learned are recorded within 30 days of closing an incident and fed into training (9.6). (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 Project folders and the scripts repository are backed up automatically and encrypted, with a copy away from the home office, and one folder is test-restored each quarter. (CP-9; PR.DS-11)
11.3 The owner keeps a one-page laptop build checklist and a peer backup agreement for non-CJI work (P05). (CP-2)

## 12. Rules for CJIS work
12.1 CJI is seen only inside the sheriff's virtual desktop (8.2). Test output with CJI stays there.
12.2 The hardware token is kept on the owner's key ring, never with the laptop; a lost token is reported to the LASO within 1 hour.
12.3 A new laptop, a reinstall, or a lost device is reported to the LASO before the next sign-in.
12.4 Every quarter the owner checks the FBI CJIS file repository for a new CJIS Security Policy version, and reviews any changes within 60 days (Security Addendum sec. 3.01).

## 13. Compliance and enforcement
Compliance is checked in the yearly self-assessment (P07) and the monthly review in 7.7. A break of an agency's rules is reported under 10.2 and may end the contract; a break of this policy alone is recorded as an exception under 5.3 with its fix.

## 14. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P04 SaaS control map; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 say where each topic lives in this policy.

## Appendix A. Approved services and data locations
| Service or location | Agency data allowed | Conditions |
|---|---|---|
| Laptop agency folders | County and city data (no CJI) | 8.3, 8.4, 8.5 |
| Business cloud storage agency folders | County and city data (no CJI) | MFA; named sharing links that expire after 30 days; 8.5 |
| Encrypted backup drive | Copies of the above | 8.3; locked file box |
| Sheriff's virtual desktop | CJI | Sheriff's terms; 12.1 to 12.3 |
| Password manager | Credentials only | MFA |
| Accounting service, website builder | None | MFA |
| Generative AI assistant | **None** | 9.5; model-improvement setting off |
| Personal accounts, family devices, public computers | **None** | 9.1 |
