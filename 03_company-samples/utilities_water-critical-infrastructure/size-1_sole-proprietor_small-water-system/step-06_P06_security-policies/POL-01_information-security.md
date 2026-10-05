# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (small community water system) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-operator |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a change to the panel or portal, a new vendor, a hire, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-8, RA-2, RA-3, CA-2, SA-4, SA-9, AC-2, AC-6(2), AC-17, AC-19, AU-6, IA-2, IA-2(1), IA-5, MA-4, CM-6, CM-8, SC-7, SC-28, CP-2, CP-9, CP-10, MP-6, SI-2, SI-3, SI-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, GV.SC-07, ID.AM-01, ID.AM-07, ID.AM-08, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.DS-01, PR.DS-11, PR.PS-01, PR.PS-02, PR.IR-01, PR.IR-03, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Regulatory basis | 40 CFR 141.202-141.205, 141.31, 141.33, 141.403(b)(3), 141.404(c), 141.405; Fla. Stat. 501.171; SDWA section 1433 elements as a voluntary benchmark (C-WATER-R01) |

## 1. Purpose
Keep the water system safe to drink and the business running by protecting the control panel, the remote access path, and customer and compliance information, in a way one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All systems in the Water System Operations Profile (SYS-01 to SYS-08), the well house, paper records, and every contractor or vendor that can reach the panel or hold business information. It applies to the owner-operator, the relief operator while covering, and any future employee. Contractors are bound through their agreements.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead and risk acceptor | Owner-operator | Runs this policy; decides incident and notice questions; keeps records |
| Licensed operator of record | Owner-operator | Treatment decisions, compliance monitoring, notices |
| Relief operator | Contractor | Follows sections 7, 9, 10, and 11 while covering |
| Controls integrator | Contractor | Remote and on-site panel support only as section 6 allows |
| On-call IT technician | Contractor | Technical help on request; no standing access |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The owner-operator is designated in writing, by this policy, as the security lead for both the control panel and the business systems. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every July and after any major change, using NIST SP 800-30 Rev. 1, and must cover the 300i-2(a)(1)(A) elements as a voluntary checklist. Every risk must have a treatment and a due date. (RA-3; PM-9; ID.RA-01)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan. A risk that could leave customers with under-disinfected water is never accepted at High. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every July (P07). At least every second year the evaluation must include an outside reviewer, such as the IT technician or an EPA-sponsored assessment if one is available to a system this size. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Sanctions and exceptions
5.1 **Sanctions.** A future employee who breaks this policy must be sanctioned in proportion to intent and harm, from retraining to termination, with a written record. (PS-8; GV.RR-04)
5.2 A contractor that breaks this policy or its agreement must be dealt with under its contract, up to ending it. A contractor that makes an unapproved remote connection to the panel loses remote access until the owner restores it in writing. (SA-9)
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. (PL-1)

## 6. Vendors and remote access to the panel
6.1 The cloud remote access portal is the only allowed remote path to the panel. No other remote tool, modem, or port may be added without a P01 risk review. (AC-17; PR.AA-05)
6.2 **Integrator access.** The integrator's portal account must stay disabled. The owner enables it only for a session the owner has approved, for a stated purpose and time window, and disables it when the work ends. Each session is written in the maintenance log (date, purpose, changes made). (MA-4; AC-17; AC-2)
6.3 Any PLC program or HMI change, remote or on site, must be followed the same day by a new owner-held copy (8.4) and a check of the dose and pump settings against the manual-operation sheet. (CM-6; CP-9)
6.4 Agreements with anyone who can reach the panel must require MFA, approved sessions only, notice to the owner within 24 hours of any security incident affecting the business, and delivery of current program copies. (SA-4; SA-9; GV.SC-05)
6.5 The owner keeps a vendor list (vendor, what it can reach or hold, contract date, assurance report date) and reviews the portal vendor's SOC 2 report every year, operating the customer controls it lists. (SA-9; GV.SC-07; ID.AM-07)

## 7. Access control
7.1 Every person has their own account. Credentials are never shared, including with the relief operator. (IA-2; AC-2; PR.AA-01)
7.2 MFA with an authenticator app must be on for every portal account, the billing SaaS, and email. (IA-2(1); PR.AA-03)
7.3 Passwords are unique passphrases of at least 14 characters, stored in a password manager. Default passwords on the router, PLC, HMI, and any new device must be changed before or at installation. Passwords must not be saved in the portal app. (IA-5; PR.AA-01)
7.4 The owner reviews the portal, billing, and email account lists every quarter and removes any account not needed. (AC-2; PR.AA-05)
7.5 Daily work on the laptop is done in a standard account; the administrator account is for installs only. (AC-6(2))
7.6 **Emergency access.** Recovery codes and a one-page access sheet are kept in a sealed envelope held by the owner's attorney, for use if the owner is unavailable. (AC-2; CP-2)
7.7 On the first of each month, and after any alarm without a known cause, the owner reviews portal sign-ins and setpoint changes and notes the review in the operating log. (AU-6; DE.AE-02)

## 8. Data and records handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Panel and router credentials, PLC program and HMI project, network details, customer portal data, recovery codes | Approved locations only (8.2); encrypted; never emailed to anyone outside the vendor list |
| **Confidential** | Customer lists and exports, compliance records, contracts, this policy set | Encrypted storage; owner and relief operator only |
| **Public** | Water quality reports, rates, public notices | No restriction |

8.2 Restricted data may be kept only in: the password manager, the file account, the encrypted USB drive in the home fire safe, and the sealed envelope. (AC-3; SC-28)
8.3 Every device that holds Confidential or Restricted data must use full-disk encryption. (SC-28; PR.DS-01)
8.4 The current PLC program and HMI project are kept in two owner-held copies (encrypted USB drive and file account) and refreshed after every change. (CP-9; PR.DS-11)
8.5 Compliance records are kept for at least the periods in 40 CFR 141.33 and 141.405(b): notices and certifications 3 years, microbiological results 5 years, chemical results 10 years, lowest daily residual and residual failures 5 years, the state-specified minimum residual 10 years. The residual spreadsheet is kept in the file account, and the paper log is scanned monthly. (SI-12; CP-9; ID.AM-08)
8.6 Paper with customer information is shredded. Old devices are wiped (encrypted, then reset) or destroyed by a recycler that gives a certificate, and each disposal is recorded (Fla. Stat. 501.171(8)). (MP-6; ID.AM-08)
8.7 Billing exports are deleted from the laptop once used. A printed customer contact list for notices is refreshed monthly and kept in the well house binder in a locked box. (SC-28; CP-9)

## 9. Acceptable use and training
9.1 Business devices are for business use. Family members do not use the laptop or sign in to the portal app. (PL-4)
9.2 Software comes only from official app stores or vendor sites. Automatic updates and the built-in antivirus stay on. (SI-2; SI-3; PR.PS-02)
9.3 The router and HMI firmware are checked against vendor and CISA advisories each quarter and updated with the integrator. Panel components are listed with model and firmware in the inventory. (SI-2; CM-8; ID.AM-01)
9.4 The cellular router allows only its outbound connection to the portal relay. Remote web administration stays off. (CM-6; SC-7; PR.IR-01)
9.5 **AI tools.** An AI tool may be used only after a written P10 assessment. No customer data, credentials, or panel details go into a consumer AI tool. AI output never replaces the daily grab sample or a site visit. Public notices are written only from the primacy agency's templates. (PL-4; SA-9)
9.6 The owner completes a cybersecurity course each year and reads CISA advisories. The relief operator is briefed on this policy and the P08 runbook before covering. (AT-2; PR.AT-01)

## 10. Incident response and notices
10.1 The business keeps an incident runbook (P08) with a printed contact sheet in the well house binder and at home. (IR-8; RS.MA-01)
10.2 Every suspected incident (unexpected setpoint change, unknown sign-in, vendor notice, lost phone) is written in the operating log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 **Treat the water first.** When disinfection may have been interrupted, the operator goes to the well house, runs the feed by hand, takes grab samples every 4 hours until the residual is restored, and records the times. (IR-4; CP-2; 40 CFR 141.403(b)(3)(i)(B); 141.404(c))
10.4 The operator consults the primacy agency within 24 hours whenever a key treatment process was interrupted, and issues any required notice by the deadlines in the P08 notification matrix (Tier 1 within 24 hours; state notice by the end of the next business day if the residual was not restored within 4 hours; Tier 2 within 30 days). (IR-6; RS.CO-02; 141.202; 141.405(a)(1); 141.203)
10.5 No ransom is paid without legal advice and an OFAC sanctions check. (IR-4)
10.6 The runbook is walked through every year with the relief operator and after any real incident. Lessons learned are recorded within 30 days of closing an incident. (IR-3)

## 11. Contingency and manual operation
11.1 Recovery follows the BIA (P05) priorities: operator on site, disinfection by hand, supply and pressure, notices, clean remote access, then program verification. (CP-2; RC.RP-01)
11.2 A one-page manual-operation sheet (dose table by well flow, pump settings, how to unplug the cellular router) is kept in the well house and reviewed after every panel change. (CP-2; PR.IR-03)
11.3 The relief agreement covers emergencies as well as planned days off, and the relief operator runs the plant by hand with the owner at least once a year. (CP-2)
11.4 Restore steps for the PLC program and setpoints, written with the integrator, are kept with the program copies. (CP-10; RC.RP-01)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07), the monthly review in 7.7, and the quarterly checks in 7.4 and 9.3. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 show where each topic lives in this policy.

## Appendix A. Where Restricted and Confidential data live
| Item | Data held | Protection required |
|---|---|---|
| Control panel (well house) | PLC program, setpoints | 7.3, 6.2, 6.3 |
| Remote access portal | Remote control, audit log | 7.1, 7.2, 7.7 |
| Laptop | Exports, spreadsheet cache | 8.3, 7.5, 8.7 |
| Phone | Portal app, authenticator | 8.3, 7.3 |
| File account | Program copy, residual spreadsheet, records | 7.2, 8.4, 8.5 |
| Encrypted USB drive (home fire safe) | Program copy | 8.2, 8.4 |
| Well house binder (locked box) | Manual-operation sheet, contact list, templates | 8.7, 11.2 |
