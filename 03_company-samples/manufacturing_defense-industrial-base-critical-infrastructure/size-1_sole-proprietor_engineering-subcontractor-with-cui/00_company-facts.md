# Scenario facts: Cris Santos Company | Defense Industrial Base | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23) and the Federal Register on 2026-10-04.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner, a licensed mechanical engineer, files Schedule C) |
| Business | Engineering subcontractor (NAICS 541330, Engineering Services): 3D CAD models made from legacy 2D drawings, tooling and fixture design, and tolerance stack-up analysis for aerospace and industrial manufacturers |
| Location | Florida. A home office in the owner's single-family house: a spare bedroom with a lockable door. The owner also attends design reviews at Prime A's site about once a month |
| Workforce | The owner only (0 employees). Uses contracted services instead of staff (section 2) |
| Revenue | About $180,000 a year (fictional). About 70% from Prime A (defense) and 30% from commercial customers. SBA-small (standard $25.5 million for NAICS 541330, 13 CFR 121.201) |
| Defense customer | **Prime A**, a large defense aerospace prime contractor. The owner is a first-tier subcontractor under a master purchase order awarded 2025-06-02 (two-year term) and issues about 14 task orders a year. The owner holds no prime DoD contract |
| Commercial customers | Industrial machinery and commercial aerospace firms. Their drawings are proprietary (under nondisclosure agreements), not CUI. Some commercial aerospace data may be EAR-controlled technology |
| CUI handled | Controlled technical information (CTI) as defined in DFARS 252.204-7012(a): Prime A drawings and 3D models marked CUI with a distribution statement, plus the models, drawings, and analysis reports the owner creates from them. It is covered defense information (CDI). Some Prime A drawings carry an ITAR export-control warning, so they are ITAR technical data. About 320 CUI files are held today |
| FCI handled | Federal contract information (FAR 52.204-21): task orders, statements of work, and invoices that reference the Prime A subcontract |
| Contract clauses in the current subcontract | DFARS 252.204-7012 (MAY 2024), 252.204-7019 and 252.204-7020 (NOV 2023), FAR 52.204-21 (NOV 2021), FAR 52.204-25. The subcontract was awarded before 2025-11-10 and does not include DFARS 252.204-7021 |
| CMMC requirement | On 2026-06-15 Prime A notified suppliers that the follow-on subcontract (solicitation expected 2026-12, award targeted 2027-02) will flow down DFARS 252.204-7021 (NOV 2025) at **CMMC Level 2 (Self)**, the minimum for a subcontractor that handles CUI (32 CFR 170.23(a)(2)). Prime A added that if its prime contract later moves to Level 2 (C3PAO), the subcontract will too (32 CFR 170.23(a)(3)). The DoD (Department of War) CIO memorandum of 2026-07-13 suspends CMMC Phase 2, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self) (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)). Prime A's Level 2 (Self) requirement fits within that, and NIST SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies |
| SPRS and identifiers | The owner registered in SAM.gov and holds a CAGE code (2025-04). A Basic Assessment score of **110** was posted in SPRS on 2025-05-20, before the 2025 award (see section 4) |
| Export controls | The owner is a U.S. citizen and the only person who handles the technical data. Not registered with DDTC: the business is confined to producing unclassified technical data (22 CFR 122.1(b)(2)) and furnishes no defense services, which require assistance to foreign persons (22 CFR 120.32). ITAR release and export rules still apply to the data (22 CFR 120.50, 120.56) |
| Not in scope | Classified information (no facility clearance, so NISPOM, 32 CFR Part 117, does not apply). CIRCIA (final rule not published). Health, payment card, and consumer data. The owner holds no personal information of others beyond business contact details |
| State law approach | Florida law is cited only where unavoidable (breach notice, Fla. Stat. 501.171, which is unlikely to be triggered because the business holds no personal information of others). Otherwise the samples stay federal |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner | Every role: system owner, security lead, CUI and export compliance lead, incident handler, risk acceptor, and **CMMC Affirming Official** (32 CFR 170.22) |
| On-call IT consultant | Hourly help with the laptop, router, and printer. U.S. person. Works on site with the owner present. No standing or remote access. Created a local "setup" administrator account on the laptop in 2025-05 that was never removed (found in P03) |
| Independent CMMC consultant | Hourly. Reviewed the self-assessment by video on 2026-07-22 and 2026-07-23 using screenshots and documents with no CUI. Did not operate any control. This is the outside check on the owner's self-assessment |
| Household members | Spouse and two teenagers. Not authorized users. Their devices share the home network. A cleaning service visits every two weeks |
| Prime A | Customer. Operates the supplier file-exchange portal (SYS-06) and the subcontract. Receives the DoD incident report number if the owner reports a cyber incident (252.204-7012(m)(2)(ii)) |
| Accountant | Prepares the owner's taxes from year-end reports. No system access |

## 3. Systems
| ID | System | Hosting | CUI? | CMMC asset category today (32 CFR 170.19(c)) | Notes |
|---|---|---|---|---|---|
| SYS-01 | Commercial productivity suite, business plan, 1 user (email, cloud file storage and sync, calendar) | Commercial SaaS | **Yes (today)** | CUI Asset (non-compliant: the offering is not FedRAMP Moderate authorized or equivalent) | MFA with an authenticator app. Prime A engineers email drawings here; the CUI project folder syncs to the laptop. A password spreadsheet and the laptop disk recovery key are stored here |
| SYS-02 | Engineering laptop (workstation class, business use only) | Owner device | Yes | CUI Asset | Desktop CAD and analysis software with node-locked licenses. Built-in full-disk encryption on (FIPS validation of the module not confirmed). Built-in antivirus and automatic OS updates. The owner works daily in an administrator account |
| SYS-03 | Mobile phone (personal) | Owner device | Yes (email attachments can be opened) | CUI Asset (to become a Security Protection Asset only) | Holds the authenticator app (MFA for SYS-01 and SYS-05). Passcode and biometric lock. Business email app installed |
| SYS-04 | Home network: internet service provider router with Wi-Fi | Home | Yes (in transit) | Security Protection Asset | WPA2 with one shared passphrase. Family devices, guests, and a smart TV share the network with the laptop and printer |
| SYS-05 | Accounting and invoicing SaaS | Commercial SaaS | No CUI; holds FCI | Outside the CUI boundary; scoping position open under DFARS 252.204-7021(d) | Client and billing records, task orders, invoices. Password only (MFA available, not turned on) |
| SYS-06 | Prime A supplier file-exchange portal | Prime A system | Yes | Not the owner's asset (Prime A's system; the owner is a user) | The owner downloads and uploads CUI here. Prime A enforces MFA |
| SYS-07 | External USB backup drive | Owner device | Yes | CUI Asset | Weekly manual backup of the laptop. **Not encrypted.** Kept in an unlocked desk drawer |
| SYS-08 | Home office multifunction printer and scanner | Home office | Yes (print and scan jobs) | CUI Asset | On the home Wi-Fi. Prints drawings for markup. A cross-cut shredder is next to it |
| SYS-09 | Commercial generative AI chatbot, individual paid plan | Commercial SaaS | Yes (CUI text was pasted) | Not permitted for CUI | Used for report drafting and engineering questions. The owner pasted CUI specification excerpts on several occasions (found in the P03 self-review). See P10 |
| SYS-10 | Government-community cloud productivity suite tenant (email and file storage), offering FedRAMP authorized at Moderate or higher, bought through an authorized reseller | Government-community cloud SaaS (planned) | Yes (planned) | CUI Asset (planned) | Ordered 2026-08-31; target go-live and CUI migration 2026-11-30. Customer responsibility matrix (CRM) to be referenced in the SSP (32 CFR 170.16(c)(2)(iii)) |

**SSP system (P02):** the *Engineering Office Systems (EOS)*: the owner's core SaaS stack (SYS-01 email and files, SYS-05 client and billing records) together with SYS-02, SYS-03, SYS-04, SYS-07, SYS-08, and the planned SYS-10, plus the owner, the home office room, and printed CUI. SYS-06 belongs to Prime A, and SYS-09 is outside the boundary because it is prohibited for CUI.

**Why the registry defaults were adapted.** The default primary system ("core business SaaS stack: email, files, client and billing records") was kept as the core of the boundary, but extended to the laptop, phone, home network, backup drive, and printer, because CUI is processed locally in desktop CAD and 32 CFR 170.19(c) puts every asset that processes, stores, or transmits CUI in the assessment scope. The default incident (exfiltration of CUI) and AI use case (generative AI assistant used with CUI engineering documents) fit this business and were kept.

## 4. Current security posture: early (few formal controls)
**In place today:**
- MFA (authenticator app) on the commercial productivity suite (SYS-01); Prime A enforces MFA on its portal (SYS-06)
- Built-in full-disk encryption on the laptop (FIPS validation not confirmed)
- Built-in antivirus with real-time scanning, and automatic OS updates, on the laptop and phone
- A cross-cut shredder for printed CUI; a lockable home office door
- The owner is a U.S. citizen and the only user of every system
- SAM registration, a CAGE code, and a SPRS Basic Assessment score posted 2025-05-20
- A generic SSP template downloaded in 2025-05

**Missing or weak (found in the 2026 self-assessment):**
1. CUI is stored in a commercial productivity suite whose offering is not FedRAMP Moderate authorized or equivalent (DFARS 252.204-7012(b)(2)(ii)(D); 32 CFR 170.16(c)(2)).
2. The SPRS score of 110 (2025-05-20) was self-reported in one evening from a template, without evidence. The 2026 recalculation under 32 CFR 170.24 is far lower (P03).
3. The SSP is a generic 2025 template that does not describe the real systems (SP 800-171 3.12.4).
4. No incident response plan, no DoD-approved medium assurance certificate, and no way to preserve images (252.204-7012(c) to (e); 3.6.1 to 3.6.3).
5. Family devices, guests, and a smart TV share the home network with the laptop and printer (3.13.1, 3.1.16).
6. The owner works daily in an administrator account, and the IT consultant's 2025 "setup" administrator account is still enabled (3.1.5, 3.1.6, 3.5.6, 3.9.2).
7. The USB backup drive holds CUI unencrypted in an unlocked drawer (3.8.9, 3.13.16).
8. Logs are left at default settings and never reviewed (3.3.1 to 3.3.5).
9. No CUI handling, insider threat, or role-based training (3.2.1 to 3.2.3).
10. CUI text was pasted into a commercial generative AI chatbot (3.1.20; see P10).
11. CUI attachments can be opened on the personal phone through the email app (3.1.18).
12. No vulnerability scanning; CAD software and router firmware are out of date (3.11.2, 3.14.1).
13. FIPS-validated cryptography is not confirmed for the laptop, email, or file sync (3.13.11).
14. The accounting SaaS holds FCI with a password only, and its CMMC scoping position is open (252.204-7021(d)(2); FAR 52.204-21).
15. Household visitors, including the cleaning service, enter the home office unescorted and are not logged (3.10.3, 3.10.4).
16. Passwords are kept in an unencrypted spreadsheet in the commercial cloud folder (3.5.10).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 incident | Exfiltration of CUI: an adversary-in-the-middle phishing page posing as a Prime A portal notice steals the owner's SYS-01 password and session token, and the attacker syncs the CUI project folder. CUI has not yet moved to SYS-10 |
| P09 SOC 2 | Security criteria only. A readiness self-check prepared because a commercial customer sent a security questionnaire. CMMC is the primary assurance mechanism for defense work; no SOC 2 report is pursued. Part B reviews the assurance evidence of the planned government-community cloud tenant (SYS-10) |
| P10 AI | The commercial generative AI chatbot (SYS-09) used with CUI engineering documents |
| Cloud | SaaS only. No IaaS. Vendor-agnostic: services are described by category |

## 6. Assessment calendar (fictional unless a regulation is cited)
| Date | Event |
|---|---|
| 2025-05-20 | SPRS Basic Assessment score of 110 posted (self-assessment from a template) |
| 2025-06-02 | Prime A master purchase order awarded |
| 2026-06-15 | Prime A notice: follow-on subcontract will require CMMC Level 2 (Self) |
| 2026-07-13 to 2026-07-24 | Self-assessment fieldwork: BIA, SSP, risk assessment, gap analysis (owner; CMMC consultant review 2026-07-22 and 2026-07-23) |
| 2026-08-03 to 2026-08-07 | Control assessment tests (owner; IT consultant on site 2026-08-05) |
| 2026-08-31 | Deliverables adopted by the owner; SYS-10 ordered |
| 2026-09-15 | Corrected SPRS Basic Assessment score due |
| 2026-11-10 | Planned start of CMMC Phase 2 (32 CFR 170.3(e)(2): one calendar year after Phase 1, which began when the DFARS rule took effect on 2025-11-10, 90 FR 43560); suspended by the DoD (Department of War) CIO memorandum of 2026-07-13 (DoD Class Deviation 2026-O0025, Revision 3) |
| 2026-11-30 | CUI migrated to SYS-10; CUI removed from SYS-01 |
| 2027-01-15 | Target date to post a CMMC Level 2 self-assessment and affirmation in SPRS (32 CFR 170.16(b)) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Revenue rhythm | About $720 of revenue per working day; Prime A pays invoices on 30-day terms | P05 |
| CAD licenses | Node-locked to the laptop; moving them to a replacement takes the vendor 1 to 2 business days | P05 |
| SYS-01 settings | Audit records kept 180 days; 30-day file version history; browser sessions stay signed in for 90 days | P02, P03, P04 |
| Credentials | Laptop password was 8 characters; passwords for 14 accounts and the laptop disk recovery key were in an unencrypted spreadsheet in SYS-01 | P02, P03, P07 |
| Laptop contents | Two unused trial programs and a game installed by a family member in 2025; CAD software two releases behind | P03 |
| Home office | Monitored house alarm; spare office key kept in the kitchen; laptop replaced in 2025 still in a closet, not sanitized; the owner sometimes worked at the public library | P02, P03 |
| Router and printer | Router firmware not updated since 2024; UPnP on; printer web sharing on and stored jobs never cleared | P03, P04 |
| Public website | Portfolio website hosted by a web host; checked 2026-07-15 and found to hold no CUI | P03 |
| Prime A onboarding | Prime A verified the owner's U.S. citizenship at onboarding in 2025 | P03 |
| P07 tests (2026-08-05) | Router administrator password was the factory default (changed that day); IT consultant's setup account disabled; a household tablet could read the printer's job list; the backup drive opened with no password (last backup 2026-08-02); laptop FIPS policy setting off; DIBNet access attempt failed (no certificate) | P01 R-015, P07 |
| AI chatbot use | CUI excerpts from two Prime A specifications (one ITAR-marked) pasted on 6 occasions between 2026-03 and 2026-07; no drawings uploaded; chat history deleted and model training turned off 2026-07-17; Prime A's subcontract administrator and counsel informed 2026-07-17 | P01 R-007, P04, P10 |
| SYS-10 evidence | Offering listed on the FedRAMP Marketplace at the High baseline; U.S. data centers and U.S.-person support; SOC 2 Type 2 (Security and Availability) for the period ending 2026-06-30; reviewed by the owner 2026-08-24 with the CMMC consultant's comments 2026-08-26 | P04, P09 |
| Budget | About $3,600 in the first year (fictional), including SYS-10 licenses of about $1,800 a year | P01, P07 |
| Insurance | No standalone cyber insurance; professional liability policy coverage for cyber events unconfirmed | P08 |
| Commercial questionnaire | A commercial customer sent a security questionnaire in July 2026 | P09 |
| Forensics | On-call terms with a digital forensics firm to be agreed by 2026-10-31 | P08 |
