# Intake Report: Cris Santos Company | Healthcare and Public Health | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent community pharmacy, one Florida storefront) |
| Intake window | 2026-07-01 to 2026-07-10 |
| Collected by | Store Manager (designated Privacy and Security Officer on 2026-07-10), with the MSP lead technician for the MSP exports |
| Approved | Pharmacist-owner, 2026-08-28 |

## 1. Purpose and scope
Intake collected the pharmacy's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that create, receive, maintain or transmit ePHI and controlled substance records, the suppliers that touch them, and the rules that may bind the pharmacy. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, tests) to the same register, so one list backs every deliverable.

A 7-person pharmacy has no HR system, CMDB or accounts payable vendor master. Its systems of record are the vendor admin consoles (PMS, productivity suite, cloud fax, delivery app), the payroll service, the MSP's exports and monthly report, the paper BAA and contracts folder, the card statements and invoices, the store's license and registration files, and what can be seen in the store.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-009 | Payroll service; PMS, productivity suite, cloud fax and delivery app consoles | 2026-06-30 to 2026-07-02 |
| Data and email | EV-010, EV-011 | Productivity suite admin console | 2026-07-01 |
| Devices, network and backup | EV-012 to EV-020 | MSP device, policy, encryption and antivirus consoles; MSP monthly report; MSP network documentation; backup console; MSP tickets; packaging workstation | 2026-06-30 to 2026-07-09 |
| Suppliers and contracts | EV-021 to EV-037 | BAA and contracts folder; PMS vendor portal; email inbox; card statements and invoices; payer files; license and registration files; vendor websites | 2026-03-31 to 2026-07-07 |
| Documents and records | EV-038 to EV-043 | Policy binder and document request; office and HR files | 2022-06-01 to 2026-07-10 |
| Business volume | EV-044, EV-045 | Accounting SaaS; PMS reporting | 2025-12-31 to 2026-06-30 |
| Store and people | EV-046 to EV-049 | Key and alarm code list; walk-through; Store Manager interview; staff survey | 2026-07-08 to 2026-07-09 |

## 3. Observations by area
**People and access.** Payroll lists 7 active employees and 1 termination from January to June 2026, a pharmacy technician who left in late April 2026 (EV-001). The PMS has 8 active named accounts in 4 roles; only the pharmacist role can verify prescriptions; the Store Manager is the administrator and the pharmacist-owner the backup administrator (EV-002). PMS sign-in requires MFA only from outside the store; the store network is a trusted location, the idle timeout is 60 minutes (raised from 15 in 2019), and the password rule is 8 characters (EV-003). A pharmacist must verify every technician entry, and the daily EPCS audit report is generated each business day; all 90 retained reports are marked unopened (EV-004). The PMS sent the PDMP file each night in June 2026 (EV-005). The productivity suite has 8 named accounts with MFA by push approval, number matching off, audit logs kept less than one year, and automatic external forwarding allowed (EV-006); its BAA shows as accepted in 2024 (EV-007). The fax portal has named accounts for the pharmacists, technicians and Store Manager (EV-008). The delivery app is on the free tier with one driver account and no BAA in its terms (EV-009). The Store Manager adds and removes accounts when remembered, with no checklist or access review, and uses the PMS administrator account for daily work (EV-048). The lists were compared with each other during the risk analysis (EV-052).

**Data and email.** The shared drive holds delivery log exports since 2021, ALF order sheets and medication lists, packaging schedules, controlled substance inventory spreadsheets, invoices and HR files, and is synced to the store desktops (EV-010). Outside email is encrypted end to end only when the sender chooses the encrypt option (EV-011). The Store Manager names the PMS, email and shared drive, the fax portal, the delivery app, the packaging workstation and the counter desktops' download folders as places ePHI is held (EV-048).

**Devices, network and backup.** The MSP device list shows 5 desktops and 2 laptops; the packaging workstation appears only as a patching and antivirus exclusion, with an operating system past its support end date, and the delivery phone only in the mobile device settings (EV-012). The 3 counter desktops sign in automatically to one shared account and are excluded from the screen lock (EV-013). The 2 laptops and the delivery phone report encryption; the 5 desktops and the packaging workstation do not (EV-014). The MSP reports monthly patching and antivirus on the 7 managed computers; its services do not include vulnerability scanning or endpoint detection and response (EV-015). Antivirus alerts go to the MSP help desk in business hours and not to the pharmacy (EV-016). The firewall exposes no inbound services; the desktops, packaging workstation, VoIP phones and camera recorder share one staff network; guest Wi-Fi is separate; the staff Wi-Fi password was last changed in 2021 (EV-017). The backup copies the shared drive and images two computers nightly with 30 days of versions, immutable retention off, one MSP administrator account, and no restore jobs in its history (EV-018). MSP tickets show a desktop retired in 2024 with no wipe or destruction record, and no restore tests (EV-019). The equipment vendor's remote-support tool accepts unattended connections at any time with one shared vendor password, and the packaging software uses one shared login (EV-020).

**Suppliers and contracts.** BAAs are on file with the PMS vendor, the MSP and the cloud fax vendor, plus the suite's online acceptance. None is on file for the packaging equipment vendor or the delivery app vendor; no MSP subcontractor list or backup vendor BAA is in the folder; the folder is paper only (EV-021). The PMS agreement covers hosting, backups and the claims switch, e-prescribing and PDMP connections, with no recovery figures (EV-022). The PMS vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 and states an RTO of 4 hours and an RPO of 30 minutes (EV-023). The vendor states that an EPCS third-party audit exists; the report itself was not on file (EV-024). The May 2026 release notes, which announce a controlled substance risk score on by default for all roles, are unread (EV-025); the score's documentation lists age, sex and payment type among its inputs (EV-026). The DUR alerts are rule-based (EV-027). The MSP contract has a 4-business-hour response time and no recovery time commitment (EV-028). The packaging equipment contract gives next-business-day on-site support and has no business associate terms (EV-029). The card statements show 12 recurring suppliers and no charges from the delivery app vendor, AI tool vendors or a training vendor (EV-030). There is one internet line and no failover (EV-031). The ALF management company has a supply agreement and sent a questionnaire due 2026-09-30 (EV-032, EV-033). The pharmacy is an enrolled Florida Medicaid provider and submits claims to PBMs in real time (EV-034). The permit, the DEA registration for Schedules II to V and the single CSOS certificate are on file (EV-035). A cyber liability policy with a breach hotline is in force (EV-036). The suite, fax and backup vendors describe encryption at rest and in transit (EV-037).

**Documents and records.** The policy set is a purchased 2019 binder with no adoption, approval or review record. The request for a risk analysis, an incident procedure, an EPCS reporting procedure, a contingency plan, downtime procedures, a contact list, a retention schedule and an incident log returned none (EV-038). The only earlier risk document is a 2022 yes/no checklist from the PMS vendor (EV-039). The Store Manager was designated Privacy Officer and Security Officer in writing on 2026-07-10 (EV-040). Training records show the 2019 privacy video at hire only (EV-041). The handbook has no sanctions rule (EV-042). An independent assessment is engaged for August 2026 (EV-043).

**Business volume.** Sales were about $1.1 million across about 306 business days in FY2025, about $3,600 per business day, and the cash reserve covers about 3 weeks (EV-044). There are about 3,100 active patients, about 55 prescriptions a business day (about 12% controlled substances), about 70 adherence pack patients, about 25 deliveries a day, and records for about 11,500 individuals (EV-045).

**Store and people.** Keys and alarm codes are held by 3 people (EV-046). The walk-through counted 5 desktops, 2 laptops, the delivery phone and the packaging system, and found a locked Schedule II safe, cameras over the counter and safe, an alarm keypad, no backup generator and a standalone card terminal (EV-047). The staff survey found the risk score flag visible to all staff and mentions of public chatbots used to draft letters (EV-049).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they enter | Store Manager (staff survey follow-up) | 2026-07-09 | Not established at intake; P10 treats it as unknown |
| MSP technician list and evidence of MFA on the remote management platform | MSP lead technician | 2026-07-03 | Not provided; asked again on 2026-07-28 for P07 (EV-SA-9) and carried into the P01 risk register (R-013) and POAM-010 |
| MSP subcontractor list and confirmation of the backup vendor BAA | MSP lead technician | 2026-07-03 | Not provided; asked again on 2026-07-28 for P07 (EV-SA-9) and carried into POAM-010 |
| Data retention period for the proof-of-delivery app | Delivery app vendor (support form) | 2026-07-02 | No answer; P01 R-012 treats retention as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-048), sales, cash and volume (EV-044, EV-045), backup schedule (EV-018), vendor recovery figures (EV-023, EV-028, EV-029), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-002 to EV-020 |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-002 to EV-011, EV-018, EV-030) and provider documentation (EV-023, EV-037) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the contracts folder, the walk-through (EV-047) and the Store Manager interview (EV-048) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the HIPAA and DEA requirements |
| P06 Policies | The 2019 binder (EV-038), the handbook (EV-042) and the designation letter (EV-040) |
| P07 Control assessment | Populations to test from (EV-001, EV-002, EV-006, EV-008, EV-009, EV-012) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the cyber policy (EV-036) |
| P09 SOC 2 | Vendor assurance on file (EV-023, EV-037) and the ALF questionnaire (EV-033) |
| P10 AI governance | AI tools found (EV-025, EV-026, EV-027, EV-049) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a pharmacy-maintained inventory; the SSP (CM-8) plans one by 2026-10-31.
