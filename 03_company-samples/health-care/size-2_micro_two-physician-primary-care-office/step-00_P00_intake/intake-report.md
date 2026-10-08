# Intake Report: Cris Santos Company | Health Care and Social Assistance | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (primary care office, two physicians, one Florida office suite) |
| Intake window | 2026-07-06 to 2026-07-17 |
| Collected by | Office Manager (Privacy and Security Officer), with the MSP lead technician for the MSP exports |
| Approved | Owner physician, 2026-08-31 |

## 1. Purpose and scope
Intake collected the practice's own records before any assessment work began on 2026-07-20. It covers the organization, the systems that create, receive, maintain or transmit ePHI, the suppliers that touch them, and the rules that may bind the practice. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, tests) to the same register, so one list backs every deliverable.

A 7-person office has no HR system, CMDB or accounts payable vendor master. Its systems of record are the vendor admin consoles (EHR, productivity suite, cloud fax), the payroll service, the MSP's exports and monthly report, the paper contracts folder, the card statements, and what can be seen in the office.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-005, EV-008 | Payroll service; EHR, productivity suite and cloud fax admin consoles | 2026-06-30 to 2026-07-08 |
| Data and email | EV-006, EV-007 | Productivity suite admin console | 2026-07-07 |
| Devices, network and backup | EV-009 to EV-016 | MSP device, policy, encryption and antivirus consoles; MSP monthly report; firewall documentation; backup console; MSP tickets | 2026-06-30 to 2026-07-08 |
| Suppliers and contracts | EV-017 to EV-023 | Contracts folder; payer files; EHR vendor portal; card statements and invoices; AI scribe vendor emails | 2024-03-01 to 2026-07-10 |
| Documents and records | EV-024 to EV-029 | Template binder and document request; office files; HR files; contracts folder; email inbox | 2019-06-01 to 2026-07-09 |
| Business volume | EV-030, EV-031 | Outside accountant; EHR/PM reporting | 2025-12-31 to 2026-06-30 |
| Office and people | EV-032 to EV-037 | Service agreements; walk-through; key list; Office Manager interview; staff survey; notice of privacy practices | 2024-01-01 to 2026-07-15 |
| Vendor documentation and AI | EV-038, EV-039 | Vendor websites and portals; EHR admin console | 2026-07-07 to 2026-07-10 |

## 3. Observations by area
**People and access.** Payroll lists 7 active employees and 1 termination from January to June 2026, a medical assistant who left in April 2026 (EV-001). The EHR has 8 active named accounts in 5 roles; the Office Manager and both physicians hold the administrator role, and there are no shared accounts (EV-002). The EHR requires MFA for every user, ends idle sessions after 15 minutes, and records an audit trail; its access report has no runs in 2025 or 2026 (EV-003). The productivity suite has 8 named accounts with MFA enforced by push approval, number matching off, audit logs kept for less than one year, and automatic external forwarding allowed (EV-004). The suite's BAA is offered in the admin console and shows as not accepted (EV-005). The fax portal has 5 named accounts (EV-008). The Office Manager adds and removes accounts when remembered, with verbal approvals and no checklist (EV-035). The lists were compared with each other during the risk analysis (EV-042).

**Data and email.** The shared drive is synced to the 6 desktops and holds forms, scanned outside records awaiting import, billing worksheets and HR files; the billing folder is limited to 2 users (EV-006). Outside email is encrypted end to end only when the sender types a keyword in the subject line (EV-007). The Office Manager names the EHR, email, the shared drive, the fax portal and the procedure-room workstation as the places ePHI is held (EV-035).

**Devices, network and backup.** The MSP device list shows 6 desktops and 4 laptops; the 2 tablets appear only in the MSP's mobile device settings, and the list has no network devices, medical devices or SaaS services (EV-009). Staff have no local administrator rights. The 10-minute screen lock excludes the 2 front-desk desktops and the procedure-room workstation (EV-010). The 4 laptops and 2 tablets report encryption; the 6 desktops do not (EV-011). The MSP reports monthly patching, quarterly firewall firmware updates and antivirus on all 10 computers; its services do not include vulnerability scanning or endpoint detection and response (EV-012). Antivirus alerts go to the MSP help desk queue in business hours and not to the practice (EV-013). The firewall exposes no inbound services, and guest Wi-Fi is separate from staff Wi-Fi (EV-014). The backup copies the shared drive nightly with 30 days of versions, immutable retention off, one MSP administrator account, and no restore jobs in its history (EV-015). MSP tickets show 2 desktops retired in 2025 with no wipe or destruction record, and no restore tests (EV-016).

**Suppliers and contracts.** BAAs are signed with the EHR vendor, the MSP and the cloud fax vendor. The MSP BAA requires subcontractor BAAs, and no backup vendor BAA or subcontractor list is in the folder. The AI scribe BAA is an unsigned draft (EV-017). The MSP contract has a 4-business-hour response time and no recovery time commitment (EV-018). Claims and eligibility go electronically through the EHR vendor's clearinghouse subcontractor (EV-019). The practice is enrolled with Medicare and Florida Medicaid (EV-020). The EHR vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 and states an RTO of 4 hours and an RPO of 15 minutes (EV-021). The card statements show 8 recurring suppliers and no AI tool charges (EV-022). The associate physician opened an AI scribe trial on 2026-06-01; the vendor's standard terms allow use of de-identified data to improve its models (EV-023).

**Documents and records.** The policy set is a purchased template binder with no adoption date, approval or review record. The request for an incident response plan, a contingency plan, downtime procedures, a retention schedule and an incident log returned none (EV-024). The last risk analysis is a 2019 consultant checklist with no likelihood or impact ratings (EV-025). The Office Manager was designated Privacy Officer and Security Officer in writing (EV-026). Training records show the new-hire HIPAA video only (EV-027). A cyber liability policy with panel vendors is on file (EV-028). A referral network questionnaire arrived in July 2026, due 2026-09-30 (EV-029).

**Business volume.** Revenue was about $1.1 million across 250 clinic days in FY2025, about $4,400 per clinic day, and cash on hand covers about 30 days of expenses (EV-030). There are about 3,500 active patients, about 40 visits per clinic day, and about $21,000 billed per week (EV-031).

**Office and people.** There is one internet line and no failover (EV-032). The walk-through counted 6 desktops, 4 laptops and 2 tablets, and found the ECG machine and spirometer connected by USB to the procedure-room workstation, a locked network closet, and keyed entry with an alarm (EV-033). Three people hold keys (EV-034). A lost staff phone in 2025 and a misdirected fax were handled informally with no record (EV-035). The staff survey found the AI scribe pilot and mentions of public chatbots used to draft letters (EV-036). The notice of privacy practices is posted (EV-037).

**Vendor documentation and AI.** The suite, fax and backup vendors describe encryption at rest and TLS in transit (EV-038). The EHR's rule-based decision support reminders use age, sex, problem list and medications (EV-039).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they enter | Office Manager (staff survey follow-up) | 2026-07-16 | Not established at intake; P10 treats it as unknown |
| MSP technician list and evidence of MFA on the remote management platform | MSP lead technician | 2026-07-09 | Not provided; asked again in P07 (EV-SA-9) and carried into the P01 risk register (R-013) and POAM-009 |
| MSP subcontractor list and confirmation of the backup vendor BAA | MSP lead technician | 2026-07-09 | Not provided; asked again in P07 and carried into POAM-009 |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-035), revenue, cash and visit volume (EV-030, EV-031), backup schedule (EV-015), vendor recovery figures (EV-018, EV-021), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-002 to EV-016 |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-004 to EV-008, EV-015, EV-022) and provider documentation (EV-021, EV-038) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the contracts folder, the walk-through (EV-033) and the Office Manager interview (EV-035) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The template binder (EV-024) and the designation letter (EV-026) |
| P07 Control assessment | Populations to test from (EV-001, EV-002, EV-004, EV-008, EV-009) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the cyber policy (EV-028) |
| P09 SOC 2 | Vendor assurance on file (EV-021, EV-038) and the referral network questionnaire (EV-029) |
| P10 AI governance | AI tools found (EV-022, EV-023, EV-036, EV-039) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a practice-maintained inventory; the SSP (CM-8) plans one by 2026-10-31.
