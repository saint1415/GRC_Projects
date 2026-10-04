# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (precision-agriculture crop farm; sole proprietorship) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-operator |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, every November before freeze season (sections 7 and 11 only), and after a new system, a new vendor, the first hire, or an incident (next full review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, RA-3, CA-2, SA-4, SA-9, AC-2, AC-6, AC-11, AC-17, AC-18, AU-6, IA-2, IA-2(1), IA-5, CM-3, CM-6, CM-8, SC-7, SC-8, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-02, GV.SC-05, GV.SC-10, ID.AM-01, ID.AM-07, ID.AM-08, ID.RA-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-11, PR.PS-02, PR.IR-01, PR.IR-03, DE.CM-03, DE.AE-02, RS.MA-01, RS.CO-02, RC.RP-01 |
| Binding rules | 21 CFR 112.6(b), 112.7, 112.164, 112.166; Fla. Stat. 501.171(2), (3)-(6), (8) |

## 1. Purpose
Protect the farm's crops, records, and the personal information it holds, by keeping control of the systems that run the irrigation and the accounts that hold the records. Each rule below is written so it can be checked (P07). The benchmark is NIST CSF 2.0, with NIST SP 800-82 Rev. 3 for the irrigation equipment.

## 2. Scope
All farm information in any form, every system in the Farm Management and Irrigation Control Platform (SYS-01 to SYS-10), the irrigation equipment at the Home Farm and River Field, paper program documents, and every vendor that holds farm data or can control farm equipment. It applies to the owner-operator, to family members who use farm devices, and to any future employee. Contractors and vendors are bound through their contracts.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead and risk acceptor | Owner-operator | Runs this policy; decides every risk; keeps the records |
| Incident lead and breach decision-maker | Owner-operator, with counsel when personal information may be involved | Runs the P08 runbook; decides notices |
| Mutual-aid neighbor | Neighboring grower (written arrangement) | Starts freeze protection by hand when the owner cannot (section 11) |
| On-call IT technician | Contractor | Technical help on request; no standing access |
| Irrigation dealer | Contractor | Services the pump and pivot; uses SYS-01 only in service windows (6.3) |
| Vendors | FMIS, booking, accounting, AI yield, card processor | Operate their safeguards; report incidents under their terms and Fla. Stat. 501.171(6) |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The farm must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 This policy designates the owner-operator in writing as the farm's security lead. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every July and after any major change, using NIST SP 800-30 Rev. 1. Every risk must have a treatment and a due date. (RA-3; PM-9; ID.RA-05)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. A risk that can cost a crop must be treated before freeze season. (PM-9; GV.RM-02)
4.5 Security controls must be self-assessed every July (P07). At least every second year, the assessment must include a review by someone outside the farm, such as the IT technician or an extension or industry cyber program. (CA-2; ID.IM-01)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)
4.7 Exceptions must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. (PL-1)

## 5. Family members and future workforce
5.1 Family members may use the laptop only through their own standard (non-administrator) account. They must not use the owner's farm account or install software on it. (AC-6; PL-4)
5.2 Before the first hire, the owner must add hiring, training, account, and departure steps to this policy. Until then GV.RR-04 is not applicable. (PL-1)

## 6. Vendors, the irrigation dealer, and AI tools
6.1 **Check before connecting.** Before a new SaaS, connected device, or AI tool holds farm data or can control equipment, the owner must read its data and security terms, confirm it offers MFA, and record the decision in the vendor list. (SA-4; SA-9; GV.SC-06)
6.2 The owner must keep a vendor list (Appendix A) showing each vendor, what data or control it has, whether it holds personal information as a third-party agent, and the farm security contact registered with it. (SA-9; GV.SC-04; Fla. Stat. 501.171(6))
6.3 **Dealer access.** The irrigation dealer's SYS-01 account must have the viewer role, except during a service window the owner opens for a named job and closes when the job ends. Dealer changes to pump, pivot, or alarm settings must be recorded in the change log (7.8). At renewal the dealer agreement must name the technicians, require MFA, require notice of changes, and require prompt notice of any security incident. (AC-6; AC-17; SA-9; GV.SC-05; SP 800-82r3 6.2.10)
6.4 The FMIS vendor's SOC 2 report must be reviewed every year (P09), and the owner must run the customer controls it lists. (SA-9; GV.SC-07)
6.5 When a vendor or dealer relationship ends, its access must be removed the same day and farm data returned or deleted in writing. (AC-2; GV.SC-10)
6.6 **AI tools.** An AI tool may receive farm imagery or data only after a written P10 assessment and the owner's approval. Terms must not allow the vendor to use farm data for its own models unless the owner opts in. No AI tool may control irrigation or set crop insurance or program figures. (PL-4; SA-9)

## 7. Access control
7.1 Every person has their own account; credentials must never be shared. (IA-2; AC-2; PR.AA-01)
7.2 **MFA** with an authenticator app must be on for SYS-01, the booking platform, email, the accounting SaaS, and online banking. Recovery codes go in the sealed envelope (7.6). (IA-2(1); PR.AA-03)
7.3 Passwords must be unique passphrases of at least 14 characters, kept in a password manager, never saved in a shared browser. (IA-5; PR.AA-01)
7.4 **No default passwords.** Every device with a login (router, access point, pump controller, pivot panel, drone controller) must have its factory password changed before use or at the next service visit, recorded in the password manager. (IA-5; CM-6; SP 800-82r3 6.2.1)
7.5 The owner must review the SYS-01 user list and roles every July and every November before freeze season, and remove any account not needed. (AC-2; PR.AA-05)
7.6 **Emergency access.** Recovery codes for SYS-01, email, banking, and the booking platform, and a one-page emergency access sheet, must be kept in a sealed envelope held by the owner's attorney. (AC-2; CP-2)
7.7 On the first Monday of each month, and every Monday from December through February, the owner must review the SYS-01 activity log (sign-ins and irrigation commands) and the email and booking sign-in history, and note the review in the security log. (AU-6; DE.CM-03; DE.AE-02)
7.8 Changes to irrigation schedules, setpoints, fertigation rates, and freeze-alarm thresholds must be recorded in a change log with the date, who made the change, and why. (CM-3; ID.RA-07; SP 800-82r3 6.2.4)
7.9 The laptop locks after 5 minutes idle; the phone and tablet after 1 minute. (AC-11)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | W-9 data, bank details, account credentials and recovery codes, irrigation control access | Approved systems only (8.2); MFA; encrypted |
| **Confidential** | Qualified exemption sales records, field and program records, customer lists, yield data, drone imagery, contracts | Approved systems; backed up (8.4); shared only with the owner's approval |
| **Public** | U-pick hours, prices, the farm name and address | No restriction |

8.2 Restricted data may be kept only in the accounting SaaS, online banking, and the password manager. W-9 scans must be deleted once the data is entered in the accounting SaaS. (AC-3; SC-28; Fla. Stat. 501.171(2))
8.3 Every device that can hold farm data must use full-disk or device encryption. (SC-28; PR.DS-01)
8.4 **Farm-held copy.** On the first Monday of each month the owner must export SYS-01 records, booking sales, and accounting reports in spreadsheet or PDF form, save them in the business file plan with version history on, and copy them to an encrypted backup drive kept away from the laptop. A test restore of one file from each source must be done every quarter. (CP-9; PR.DS-11; 21 CFR 112.7(b); 21 CFR 112.166(b))
8.5 **Qualified exemption.** Each January the owner must complete, date, and sign a written annual review and verification of qualified exemption eligibility from the exported sales records, and keep it with the records. The farm name and complete business address must appear at the farm stand, the U-pick check-in, and on every booking and pre-order web page. (21 CFR 112.6(b)(2)-(3); 21 CFR 112.7(b); 21 CFR 112.161(b))
8.6 **Retention and disposal.** Qualified exemption records and other Produce Safety records are kept at least 4 years (covering the 3-year look-back plus the current year, and at least the 2 years in 112.164(a)). Customer exports are deleted after 12 months; W-9 data is kept as the tax preparer advises. Records no longer needed are deleted from every location, and old devices are wiped or destroyed by a recycler that gives a certificate. (SI-12; MP-6; ID.AM-08; 21 CFR 112.164(a); Fla. Stat. 501.171(8))

## 9. Acceptable use and training
9.1 The laptop's farm account is for farm work. Personal browsing and games use a separate account. (PL-4)
9.2 Devices must not be left unattended outside the home office, the locked pump house, or the owner's vehicle while the owner is with it. The pump house and pivot panel cabinet stay locked. (PL-4; PE-3)
9.3 Automatic updates and the built-in antivirus must stay on. Software comes only from official app stores or the vendor's site. Every USB stick or memory card from the tractor display or the drone must be scanned before files are opened. (SI-2; SI-3; PR.PS-02)
9.4 **Networks.** Customer Wi-Fi must be a guest network isolated from farm devices. The pump house must be on its own network. Farm accounts must never be used over the customer Wi-Fi. The router firmware must be updated when the provider releases it, and OT firmware checked with the dealer every November. (SC-7; AC-18; SI-2; PR.IR-01; SP 800-82r3 5.2.3)
9.5 **Payments.** Before changing any payee's bank details, the owner must call the payee on a number already on file, not one given in the request. (IA-2(1); PR.AT-01)
9.6 The owner must complete a free small-business cybersecurity course every year, read monthly security reminders, and brief family members on the laptop rules. (AT-2; PR.AT-01)
9.7 **Drone.** The drone is flown only under 14 CFR Part 107 by the certificated owner, and imagery of people at the U-pick is deleted unless needed. (PL-4)

## 10. Incident response
10.1 The farm must keep an incident runbook (P08) with a printed contact list in the home office and the pump house. (IR-8; RS.MA-01)
10.2 Every suspected incident (unknown sign-in, changed irrigation setting, ransom note, vendor breach notice, lost phone) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6)
10.3 **Crop first.** If irrigation control may be compromised, the owner must switch the pump controller and pivot panel to local and run them by hand before anything else. (IR-4; RS.MI-01; SP 800-82r3 6.4.4)
10.4 Notices to individuals, the Florida Department of Legal Affairs, and consumer reporting agencies must meet the deadlines in the P08 notification matrix, confirmed by counsel. (IR-6; RS.CO-02; Fla. Stat. 501.171(3)-(5))
10.5 No ransom may be paid without counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every November and after any real incident. Lessons learned are recorded within 30 days of closing an incident. (IR-8; ID.IM-02)

## 11. Contingency and freeze protection
11.1 Recovery follows the BIA (P05) priorities: manual irrigation first. (CP-2; RC.RP-01)
11.2 A one-page freeze-night procedure (how to switch to local and Hand, start the freeze zone, and check the field thermometer) must be posted inside the pump house and rehearsed every November. (CP-2; ID.IM-04; SP 800-82r3 6.5.1)
11.3 A standalone cellular freeze alarm, independent of SYS-01 and the home internet, must call both the owner and the mutual-aid neighbor. (CP-2; PR.IR-03)
11.4 The owner must keep a written mutual-aid arrangement with a neighboring grower to start freeze protection when the owner cannot. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual self-assessment (P07), the November freeze-season check, and the monthly review in 7.7. A personal departure from this policy is recorded as an exception under 4.7.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P04 SaaS control map; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Devices, data locations, and vendors (ID.AM-01, ID.AM-07, GV.SC-04)
| Item | Data or control held | Protection required |
|---|---|---|
| SYS-01 FMIS and irrigation module | Field records; remote control of pump and pivot; alarms | 7.2; 6.3; 7.7; 8.4 |
| Booking platform (third-party agent) | About 1,800 customer accounts; sales records | 7.2; 8.4; 8.5; breach contact registered |
| Accounting SaaS (third-party agent) and bank | W-9 data; payments | 7.2; 8.2; 9.5 |
| Email and business file plan | Correspondence; exports; program documents | 7.2; 8.4 |
| AI yield vendor | Drone imagery; block yields | 6.6 |
| Laptop | Farm account; downloads | 5.1; 8.3; 9.3 |
| Phone and tablet | SYS-01 app; alarms; card reader; drone app | 7.9; 8.3 |
| Router, access point, customer Wi-Fi | Network | 7.4; 9.4 |
| Pump controller, pivot panel, probes, freeze sensor | Irrigation control | 7.4; 7.8; 9.2; 9.4 |
| Encrypted backup drive | Monthly exports | 8.4; kept away from the laptop |
