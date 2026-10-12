# Intake Report: Cris Santos Company | Financial Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (merchant services provider, an ISO; one Florida office suite) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | Operations Manager (security lead), with the MSP lead technician for the MSP exports and the web developer for the hosting export |
| Approved | Owner, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that transmit card data or hold merchant owner information, the settings the company controls for its merchants, the suppliers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, tests) to the same register, so one list backs every deliverable.

A 7-person ISO has no HR system, CMDB or accounts payable vendor master. Its systems of record are the processor partner's gateway console and portal, the CRM, suite and phone admin consoles, the payroll service, the MSP's exports and monthly report, the contracts folders, the card statements, the ASV portal, and what can be seen in the office.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People | EV-001, EV-002 | Payroll service portal; agent roster and agreements | 2026-06-30 to 2026-07-01 |
| Gateway and processor partner portal | EV-003 to EV-009 | Gateway reseller console and reports; processor partner portal | 2026-06-30 to 2026-07-06 |
| SaaS tenants | EV-010 to EV-014 | CRM, productivity suite and phone system admin consoles and reports | 2026-06-30 to 2026-07-07 |
| Devices, network, backup, website and terminals | EV-015 to EV-024 | MSP device, policy, encryption and antivirus consoles; MSP monthly report and tickets; firewall documentation; backup console; hosting and storage consoles; terminal spreadsheet | 2026-06-30 to 2026-07-09 |
| Suppliers and contracts | EV-025 to EV-032 | Contracts folders; processor partner portal; CRM vendor portal; vendor websites; card statements and invoices | 2025-01-01 to 2026-07-09 |
| PCI DSS validation, documents and records | EV-033 to EV-041 | Owner's files; ASV portal; shared drive and document request; training and HR files; shredding receipts; state business registry; website terms and support inbox | 2025-10-15 to 2026-07-08 |
| Business volume | EV-042 | Outside accountant | 2025-12-31 |
| Office, people and AI | EV-043 to EV-046 | Interviews; walk-through and key list; staff survey; sales materials | 2026-07-07 to 2026-07-09 |

## 3. Observations by area
**People.** Payroll lists 7 active employees, one departure in 2025 and none from January to June 2026 (EV-001). There are 6 active outside sales agents; one agent contract ended on 2026-02-13. The agent agreements contain no security or privacy terms, no training requirement and no background check (EV-002).

**Gateway and processor partner portal.** The console has 6 company staff accounts. The Owner and the Operations Manager hold the administrator role; the other 4 hold the support role, which can log in as any merchant and issue sales and refunds. Outside agents hold a view-only sales role. MFA is optional and enrolled on 2 of the 6 staff accounts (EV-003). The console can also reset merchant passwords, edit hosted payment page settings including a custom header field that accepts HTML and script, and set fraud filter thresholds. Passwords need 8 characters, the audit log is kept 13 months, and no alert rules are set up (EV-004). About 420 merchants use the gateway (about 120 hosted payment pages, about 300 virtual terminals). Staff keyed about 1,900 transactions in the 12 months to June 2026, and reports show only the first six and last four digits (EV-005). The fraud filter defaults set in 2024 (decline at 80 and above, review from 60 to 79) are used by 104 of 120 e-commerce merchants and have not changed since 2024 (EV-006). The portal enforces MFA for every user (EV-007). Deposit account change requests are entered on the strength of a phone call or email; a March 2026 request for a salon merchant was stopped after the processor partner asked for a signed form (EV-008). About 850 merchants are active, about 92% of them in Florida; each brings about $1,300 a year in residuals; about 25 merchants are boarded and 40 disputes handled a month (EV-009).

**SaaS tenants.** The CRM enforces MFA for staff and agents, limits agents to their own merchants, and holds about 1,250 merchant files with owner Social Security numbers, IDs and voided checks. No retention rule is configured, and the vendor's AI writing assistant has been on by default since June 2026 (EV-010). The suite enforces push MFA with number matching off, keeps audit logs for less than 12 months, and has no rule to encrypt outbound mail or block attachments with Social Security numbers (EV-011). Agents send merchant applications as plain email attachments, mailboxes hold applications back to 2023, and a monthly CRM export sits in the shared drive (EV-012). The phone system has 5 seats and one shared administrator login with no second factor. It has recorded every support call since 2025-05-12 with no retention limit, and only inbound calls play an announcement (EV-013). The support queue takes about 15 merchant calls a day (EV-014).

**Devices, network, backup, website and terminals.** The MSP device list holds 9 laptops (7 assigned, 2 spares) and no network devices, phone system, website, terminals or SaaS services (EV-015). Staff have no local administrator rights and a 15-minute screen lock applies (EV-016). All 9 laptops report full-disk encryption (EV-017). The MSP patches monthly and runs antivirus; its services do not include endpoint detection and response or internal scanning (EV-018). Antivirus alerts reach the MSP in business hours and not the company (EV-019). The office has one flat staff network, a WPA2 staff Wi-Fi password set in 2023, a separate guest Wi-Fi, and one internet line (EV-020). The suite backup runs daily with 1 year of retention and one MSP administrator account, and has no restore jobs in its history (EV-021). Two laptops retired in 2025 have no wipe record (EV-022). The website form plugin is two major versions behind, the bucket holds about 610 files since 2023, bucket logging is off, and only the web developer holds the hosting login (EV-023). The terminal spreadsheet lists 44 spares, was last reconciled in 2025, and has no inspection field; terminals arrive key-injected (EV-024).

**Suppliers and contracts.** The ISO agreement requires the annual SAQ D for Service Providers and AOC, quarterly ASV scans, and notice of a suspected compromise within 24 hours. It gives the company no availability commitment and names no company service as a covered bank service (EV-025). The processor partner's AOC (Level 1, March 2026) covers its platform; its responsibility summary does not mention custom header content (EV-026). The MSP contract has no security incident notice, named technicians or MFA terms (EV-027). The contracts folder holds no phone vendor AOC, no service provider list and no responsibility matrix (EV-028). The CRM vendor's SOC 2 Type 2 report states an RTO of 8 hours and an RPO of 1 hour (EV-029). Vendors describe encryption at rest and in transit (EV-030). The card statements show 12 recurring suppliers and no AI tool charges (EV-031). A cyber policy with a breach hotline is on file (EV-032).

**PCI DSS validation, documents and records.** The 2025 SAQ D and AOC, signed on 2025-10-15, describe the scope as the gateway console only (EV-033). Four quarterly ASV scans of the office IP address passed (EV-034). The only policy is a 2022 PCI policy template. The request for acceptable use and classification rules, a retention schedule, an incident response plan, incident contacts, a written risk assessment, a penetration test report and a service provider list returned none (EV-035). All 7 employees watched the PCI awareness video; agents are not on the list (EV-036). Employees were background-checked before hire (EV-037). A shredding service collects the shred bin (EV-038). The company is a privately held Florida LLC with no financial license or charter and no SEC registration (EV-039). The merchant service terms do not mention keyed entry, and merchants' PCI DSS questions are answered one by one by email (EV-040). A merchant association questionnaire is due 2026-09-30 (EV-041).

**Business volume.** FY2025 receipts were about $1.1 million across 250 business days, about $4,400 per business day, and the cash reserve covers about 45 days of expenses (EV-042).

**Office, people and AI.** Accounts are created on verbal request and removed when remembered; nobody reviews logs; the shared phone login is used by three people; keyed entry happens at the office or at home; deposit changes have no call-back step; returned terminals are not inspected (EV-043). The walk-through found keyed suite entry with an after-hours alarm, keys held by two people, spare terminals in a locked cabinet, and a locked shred bin (EV-044). The staff survey found merchant statements pasted into public chatbots (EV-045). The sales brochure says the fraud filter stops 99% of fraud (EV-046).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they pasted | Operations Manager (staff survey follow-up) | 2026-07-09 | Not established at intake; P10 treats it as unknown |
| MSP technician list and evidence of MFA on the remote management tool | MSP lead technician | 2026-07-08 | Not provided; asked again in P07 (EV-SA-9) and carried into the P01 risk register (R-011) and POAM-011 |
| Processor partner and sponsor bank incident contacts | Owner | 2026-07-03 | Not on file at intake; to be recorded by 2026-09-15 (POAM-008) |
| Phone vendor PCI DSS AOC | Phone vendor | 2026-07-08 | Not received by P07 fieldwork end (EV-SA-9); carried into POAM-011 |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-043), receipts and cash (EV-042), merchant, call and dispute volumes (EV-005, EV-009, EV-014), backup schedule (EV-021), vendor recovery figures (EV-027, EV-029), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-003 to EV-024 |
| P04 Cloud mapping | SaaS components, the cloud workload and the MSP-operated backup (EV-003, EV-007, EV-010 to EV-013, EV-021, EV-023) and provider documentation (EV-026, EV-029, EV-030) |
| P01 Risk register | Likelihood inputs from the console, portal and MSP exports, the contracts folders, the document request (EV-035) and the intake interviews (EV-043) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with PCI DSS and the Safeguards Rule |
| P06 Policies | The 2022 policy template and the document request (EV-035) |
| P07 Control assessment | Populations to test from (EV-001, EV-002, EV-003, EV-005, EV-015, EV-024) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the ISO agreement (EV-025) and the cyber policy (EV-032) |
| P09 SOC 2 | Vendor assurance on file (EV-026, EV-029) and the merchant association questionnaire (EV-041) |
| P10 AI governance | AI tools found (EV-006, EV-010, EV-031, EV-045, EV-046) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a company-maintained inventory; POAM-006 plans a one-page inventory by 2026-09-30.
