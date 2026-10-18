# Intake Report: Cris Santos Company | Professional, Scientific, and Technical Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm, 7 employees, one Florida office suite) |
| Intake window | 2026-06-22 to 2026-07-02 |
| Collected by | Office Manager, with the MSP lead technician for the MSP exports |
| Approved | Owner CPA, 2026-08-31 |

## 1. Purpose and scope
Intake collected the firm's own records before any assessment work began on 2026-07-06. It covers the organization, the systems that hold client tax return information and customer information, the suppliers that touch them, and the rules that may bind the firm. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, tests) to the same register, so one list backs every deliverable.

A 7-person firm has no HR system, CMDB or accounts payable vendor master. Its systems of record are the vendor admin consoles (tax software, client portal, productivity suite, payroll platform, practice management), the outside payroll service, the MSP's exports and monthly report, the contracts folder, the firm's card statements and general ledger, the IRS PTIN and e-file accounts, the insurer's policy and application, and what can be seen in the office.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-005, EV-009, EV-010 | Outside payroll service; tax software, suite, portal and payroll platform admin consoles | 2026-06-24 to 2026-06-30 |
| Data and email | EV-006 to EV-008 | Productivity suite admin console and cloud storage | 2026-06-25 |
| Business volume | EV-011 to EV-013 | Tax software reporting; practice management; general ledger | 2025-12-31 to 2026-06-26 |
| Devices, network and backup | EV-014 to EV-021 | MSP device, policy, encryption and antivirus consoles; MSP monthly report; firewall documentation; backup console; MSP tickets | 2026-06-29 to 2026-06-30 |
| Suppliers and contracts | EV-022 to EV-031 | Contracts folder; card statements and invoices; vendor portals and websites; AI assistant admin console; office files | 2026-03-31 to 2026-06-30 |
| Documents and records | EV-032 to EV-040 | Office files; document request; HR files; IRS PTIN and e-file accounts; consent folder; engagement letters; email inbox | 2024-02-15 to 2026-06-30 |
| Office and people | EV-041 to EV-044 | Walk-through; key list; Office Manager and Owner CPA interviews | 2026-06-30 to 2026-07-01 |
| Late answer | EV-045 | Office files (designation memo) | 2026-07-06 |

## 3. Observations by area
**People and access.** The payroll service lists 7 active employees and one temporary seasonal data-entry assistant whose last working day was 2026-04-17 (EV-001). The tax software has 8 active named accounts in 4 roles; the vendor enforces MFA for every user, sessions time out, and the audit trail records bank account changes on returns (EV-002). The productivity suite has a named account for each employee and for the seasonal assistant; the Owner CPA and the Office Manager hold the global administrator role on their everyday accounts (EV-003). Suite MFA uses push approval with number matching off, automatic external forwarding is allowed, no alert policies are on, and audit logs are kept for less than one year (EV-004). Every client folder, including payroll folders, is shared with all staff and syncs to the 4 desktops (EV-005). The portal has 5 staff accounts with MFA; client MFA is optional and about 30% of individual clients use it (EV-009). The payroll platform holds about 420 employees of 38 client companies, reached by the Bookkeeper and the Owner CPA (EV-010). The Office Manager adds and removes accounts when remembered and accounts are never reviewed (EV-043). The lists were compared with each other during the risk assessment (EV-048).

**Data and email.** Client folders hold scans, workpapers, prior returns and signed Forms 8879 from 2016 on, for current and former clients alike (EV-006). The suite mail app runs on 7 staff-owned phones with no device policy (EV-007). Mail is protected by TLS between servers; no rule encrypts or blocks outbound attachments that contain SSNs (EV-008). Returns and source documents are emailed to clients as attachments when they ask (EV-043).

**Business volume.** The firm prepares about 880 individual returns (about 1,400 individuals) and about 170 business returns a year under one EFIN; about 6% of individual clients live outside Florida for part or all of the year (EV-011). Every active client has a signed engagement letter, and card payments go through the vendor-hosted payment page (EV-012). Receipts were about $1.1 million across about 250 business days, about $4,400 per business day, with about 60% billed from February to April (about $10,500 per business day in season); cash covers about 45 days of expenses (EV-012, EV-013).

**Devices, network and backup.** The MSP device list shows 4 desktops and 4 laptops; it has no MFP, network devices, phones or SaaS services (EV-014). Staff have no local administrator rights; the 10-minute screen lock covers the laptops and excludes the reception and seasonal desktops (EV-015). The 4 laptops report full-disk encryption; the 4 desktops do not (EV-016). The MSP patches monthly, updates firewall firmware quarterly and runs antivirus on all 8 computers; its services do not include vulnerability scanning, endpoint detection and response, or the MFP (EV-017). Antivirus alerts go to the MSP help desk in business hours only (EV-018). The firewall exposes no services, guest Wi-Fi is separate, and the staff Wi-Fi password was last changed in 2021 (EV-019). The suite backup runs daily with 1 year of retention, one shared MSP administrator account without MFA, single-file restores only, and no immutable retention setting shown (EV-020). MSP tickets show setting changes with no approval recorded and 2 desktops replaced in 2024 with no wipe record (EV-021).

**Suppliers and contracts.** The MSP contract covers IT operations and backup administration with a 4-business-hour response time and no recovery time, security, breach notice or IRC 7216 terms (EV-022). The card statements show 12 recurring suppliers plus a 3-seat generative AI assistant charged to the Owner CPA's card since 2026-03-02 (EV-023). The tax software vendor transmits returns as an Authorized IRS e-file Provider (EV-024). Its SOC 2 Type 2 report covers the 12 months ending 2026-03-31, with an unmodified opinion, an RTO of 4 hours and an RPO of 1 hour, and U.S. data centers (EV-025). The other SaaS vendors describe encryption at rest and in transit; the portal and payroll terms state no breach notice timeframe, and the portal terms do not say where data is stored (EV-026). The AI assistant's business terms exclude training on inputs by default, keep inputs up to 30 days, and do not commit to U.S.-only processing (EV-027). The leased MFP stores scanned images on its drive, and the lease (ending 2027-03-31) does not include drive wiping unless requested (EV-028). There is one internet line and no failover (EV-029). A cyber policy with a breach hotline and panel vendors has been held since 2025 (EV-030). A shredding vendor empties a locked bin and issues certificates (EV-031).

**Documents and records.** The 2024 WISP was filled in from the IRS Pub. 5708 template, with no later revision, approval or distribution record (EV-032). The request for an incident response plan, a risk assessment, a contingency plan, a retention schedule, an asset inventory, a change log, access reviews, a vendor inventory, log reviews, an incident log and restore tests returned none (EV-033). Training records show one security video in 2024 (EV-034). Confidentiality agreements are signed at hire and do not mention IRC 7216 or 6713 (EV-035). The Office Manager completed an online FTC Safeguards Rule course in June 2026 (EV-036). The 4 PTIN holders answered Yes to the Form W-12 WISP question at the 2026 renewal; the firm is an ERO with the Owner CPA as Responsible Official (EV-037). The IRC 7216 consent template comes from a 2018 practice guide, and 12 lender releases in 2026 have signed consents on file (EV-038). Payroll engagement letters promise breach notice to the client without unreasonable delay (EV-039). The largest bookkeeping and payroll client sent a security questionnaire in June 2026, due 2026-09-30 (EV-040). The Qualified Individual designation memo, asked for at intake, was signed on 2026-07-06 (EV-045).

**Office and people.** The walk-through counted 4 desktops, 4 laptops and the MFP, and found a locked network closet, keyed entry with an alarm, a locked shred bin and locked cabinets (EV-041). Two people hold keys (EV-042). A misdirected email with a return in 2025 was handled informally with no record, and MSP technicians have never received a written IRC 6713 and 7216 notice (EV-043). Three staff use the AI assistant to draft letters and notice responses; its terms were not reviewed before purchase, and the firm has no health care bookkeeping clients, federal contracts or attest engagements (EV-044).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Written designation of the person who coordinates the information security program | Owner CPA | 2026-06-29 | Received 2026-07-06 (EV-045) |
| What client content has been entered into the AI assistant and any other AI tool | Owner CPA | 2026-07-01 | Not established at intake; answered in the P03 interviews (EV-050) and the P10 review (EV-056) |
| MSP technician list and evidence of MFA on the remote management platform | MSP lead technician | 2026-07-01 | Not provided; asked again in P07 on 2026-07-27 (EV-SA-9) and carried into POAM-012 |
| Backup subcontractor terms and immutable retention setting | MSP lead technician | 2026-07-01 | Not provided; asked again in P07 (EV-SA-9, EV-CP-9) and carried into POAM-008 and POAM-012 |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-043), revenue, season split and cash (EV-012, EV-013), backup schedule (EV-020), vendor recovery figures (EV-022, EV-025), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-002 to EV-009 and EV-014 to EV-021 |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-002 to EV-009, EV-020, EV-023) and provider documentation (EV-025, EV-026) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the contracts folder, the walk-through (EV-041) and the intake interviews (EV-043, EV-044) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The 2024 WISP (EV-032), the document request response (EV-033) and the designation memo (EV-045) |
| P07 Control assessment | Populations to test from (EV-001, EV-002, EV-003, EV-009, EV-014) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the cyber policy (EV-030) and payroll engagement letters (EV-039) |
| P09 SOC 2 | Vendor assurance on file (EV-025, EV-026) and the payroll client's questionnaire (EV-040) |
| P10 AI governance | AI tools found (EV-002, EV-023, EV-027, EV-044) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a firm-maintained inventory; the SSP (CM-8) plans one by 2026-10-31.
