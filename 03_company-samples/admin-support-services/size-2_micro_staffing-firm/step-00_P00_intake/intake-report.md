# Intake Report: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm, one Central Florida office suite) |
| Intake window | 2026-07-06 to 2026-07-17 |
| Collected by | Operations Manager (Security and Privacy Lead), with the MSP lead technician for the MSP exports and the Senior Recruiter for the ATS |
| Approved | Owner, 2026-08-31 |

## 1. Purpose and scope
Intake collected the firm's own records before any assessment work began on 2026-07-20. It covers the organization, the systems that hold worker, candidate and client data (the PATS and the accounting SaaS), the suppliers that touch them, the paper Form I-9 files, and the rules that may bind the firm. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, samples, tests) to the same register, so one list backs every deliverable.

A 7-person staffing firm has no HR system, CMDB or accounts payable vendor master. Its systems of record are the vendor admin consoles and reports (the ATS, the payroll and timekeeping service, the productivity suite, the accounting SaaS), the E-Verify file, the MSP's exports, the paper contracts and HR files, the card statements, and what can be seen in the office.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and payroll | EV-001 to EV-006 | Payroll and timekeeping service portal, reports and tax filings; contracts folder | 2026-04-30 to 2026-07-08 |
| Applicant tracking and AI | EV-007 to EV-010 | ATS admin console, terms and reports | 2026-06-30 to 2026-07-08 |
| Email and shared drive | EV-011, EV-012 | Productivity suite admin console (exported by the MSP) | 2026-07-07 |
| Onboarding services | EV-013, EV-014 | E-Verify file; screening services agreement and portal | 2026-07-09 |
| Finance and spending | EV-015 to EV-017 | Accounting SaaS; CPA year-end report; card statements and invoices | 2025-12-31 to 2026-07-08 |
| MSP, devices, network and backup | EV-018 to EV-023 | MSP contract; MSP device, encryption, antivirus and patch reports; backup console; firewall management; MSP tickets | 2026-06-30 to 2026-07-14 |
| Contracts and office files | EV-024 to EV-026 | Facility files; cyber policy; client agreements and the largest client's questionnaire | 2026-07-09 |
| Documents and records | EV-027 to EV-032 | Handbook and HR files; designation letter; document request; Owner's files; shredding certificates | 2023-01-01 to 2026-07-10 |
| Office and people | EV-033 to EV-036 | Office walk-through; intake interviews; staff AI tool question | 2026-07-13 to 2026-07-15 |
| Public pages and vendor documentation | EV-037, EV-038 | Firm website and career site; vendor websites and help centers | 2026-07-10 |

## 3. Observations by area
**People and payroll.** Payroll lists 7 active staff and 3 staff departures in 2025-2026: an Account Manager in 2025, the previous Coordinator on 2025-12-12, and a recruiter on 2026-05-15 (EV-001). 96 different associates were paid in 2025, about 22 are on assignment in an average week, and associate gross payroll was about $700,000, about $13,500 a week (EV-002). The 3 payroll administrators sign in with a password and an SMS code; alerts for bank-account changes and report exports are available and off; associates change their own bank account in self-service with a password only (EV-003). The census report lists about 318 people with SSNs and bank accounts, about 301 of them with Florida addresses, and was downloaded 6 times in 2026 (EV-004). Payroll is due Wednesday 5 p.m. for Friday deposit, and the vendor can freeze bank changes and recall deposits on request (EV-005). Neither reemployment tax return includes the voluntary E-Verify certification (EV-006).

**Applicant tracking and AI.** The ATS has named accounts in 3 roles. The Owner, the Operations Manager and the Senior Recruiter are administrators, and all 3 recruiter accounts also hold the onboarding role that opens SSNs, bank forms and full background check results. MFA by authenticator app is enforced for every user (EV-007). The AI match feature was turned on 2026-03-16 by the Senior Recruiter, with a smart filter that hides Light Industrial applicants scoring under 50; the model-improvement opt-out is off, and the generative writer is in use (EV-008). The ATS terms delete customer data 30 days after a subscription ends; the AI feature terms allow model improvement use unless the customer opts out and have no breach notice or deletion term; the trust page states a SOC 2 Type 2 report, and none is on file (EV-009). The ATS holds about 9,800 candidate records, and every job order is in the Central Florida metro area (EV-010).

**Email and shared drive.** Suite MFA by push approval has been enforced for all users since 2025-06, with number matching off; logs are kept 90 days, and alerts for new forwarding rules and mass downloads are off (EV-011). The whole shared drive, including the Onboarding folder with Form I-9 scans, consumer report PDFs and onboarding exports, is shared with all 7 staff accounts, with 30 days of versions (EV-012).

**Onboarding services.** The E-Verify MOU was signed 2024-03-04; the firm's E-Verify file names 2 users, both with tutorial records (EV-013). The screening agreement (2021) carries the FCRA end-user certification and no breach notice term; the provider hosts the disclosure and authorization and mails the adverse action letters with a 5-business-day wait; recruiters see report results through the ATS integration (EV-014).

**Finance and spending.** The accounting SaaS has 3 users with vendor-enforced MFA (EV-015). FY2025 receipts were about $1.1 million, about $19,400 of billings a week; clients pay by ACH or check; the line of credit covers about 3 weeks of payroll; security spending appears as laptops, MSP fees and the insurance premium (EV-016). The card statements and invoices show the recurring suppliers and no AI tool vendor other than the ATS vendor (EV-017).

**MSP, devices, network and backup.** The MSP contract covers help desk, patching, antivirus, firewall, Wi-Fi, suite administration on request and the suite backup, with a 4-business-hour response time and no recovery commitment, security terms or incident notice clause (EV-018). The MSP device list shows 8 laptops with its remote management agent; the tablet, scanner and phones are not on it; the interview-room laptop is exempt from the 10-minute screen lock (EV-019). All 8 laptops report full-disk encryption, signature antivirus and current patches; antivirus alerts reach the MSP in business hours only (EV-020). The suite backup runs daily with 30 days of versions, immutable retention off, one MSP administrator login, and no restore jobs in its history (EV-021). The firewall blocks unsolicited inbound traffic, guest Wi-Fi is separate, and the office has one internet line (EV-022). MSP tickets close the retirement of 2 laptops in 2025 with no wipe record and show no restore tests (EV-023).

**Contracts and office files.** The previous copier was returned at lease end in 2024 with no wipe record in the lease file (EV-024). The cyber policy has a breach hotline and panel vendors and requires MFA on email and remote access (EV-025). Two Light Industrial clients require E-Verify; the largest client's agreement requires "prompt" incident notice, and its security questionnaire is due 2026-09-30 (EV-026).

**Documents and records.** The 2023 handbook has one page on computer use, signed at hire by all 7 staff; no other training is recorded (EV-027). Departure records show laptops and keys collected, with no account removal step (EV-028). The Operations Manager was designated Security and Privacy Lead on 2026-07-01 (EV-029). The request for a risk assessment, security policies, an incident response plan, a contingency plan, a retention schedule, an inventory, vendor reviews, review records, a change log and a description of the scanning process returned none (EV-030). The 2026 business plan states the mission, and the 2026 assessments were engaged on 2026-07-06 (EV-031). Monthly shredding certificates are on file for paper (EV-032).

**Office and people.** The walk-through counted 8 laptops, the kiosk-mode applicant tablet on guest Wi-Fi and the scanner, and found keyed entry with an alarm and a locked records room with the locked Form I-9 cabinet (EV-033). The Operations Manager states that accounts are removed when someone remembers, and that all 7 staff use personal phones for email, the ATS app and texting candidates, with no mobile management (EV-034). The Coordinator completes Forms I-9 on paper, scans them to the Onboarding folder since 2024-03, writes the E-Verify case number on the form, and enters bank changes requested by phone, email or text without a call-back (EV-035). The staff AI question found the ATS AI features and mentions of public chatbots (EV-036).

**Public pages and vendor documentation.** The career site's privacy statement does not mention automated scoring or how to ask for human review; the website has no security contact (EV-037). The ATS, payroll, suite and backup vendors describe encryption and sign-in lockout (EV-038).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they enter | Operations Manager (staff questionnaire follow-up) | 2026-07-16 | Not established at intake; P10 treats it as unknown |
| Payroll vendor SOC 2 Type 2 report | Payroll vendor | 2026-08-03 | Received 2026-08-14 under a nondisclosure agreement (EV-049); reviewed in P09 |
| ATS vendor SOC 2 Type 2 report | ATS vendor | 2026-08-03 | Not received by 2026-08-31; carried into the P01 risk register (R-017) |
| MSP technician list and evidence of MFA on the remote management platform | MSP lead technician | 2026-08-03 | Not received by P07 fieldwork end (EV-SA-9); carried into R-013 and POAM-012 |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Staff and associate volumes (EV-001, EV-002), payroll timing (EV-005), billings and the line of credit (EV-016), ATS volumes (EV-010), backup schedule (EV-021), vendor terms (EV-009, EV-018), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-003, EV-007, EV-011, EV-012, EV-019 to EV-022 |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-003, EV-007, EV-011, EV-021) and vendor documentation and terms (EV-009, EV-018, EV-038) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the contracts and HR files, the walk-through (EV-033) and the intake interviews (EV-034, EV-035) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the CSF 2.0 benchmark and the binding record rules |
| P06 Policies | The handbook (EV-027), the document request (EV-030) and the designation letter (EV-029) |
| P07 Control assessment | Populations to test from (EV-001, EV-007, EV-011, EV-013, EV-019, EV-028) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the census counts (EV-004), the cyber policy (EV-025) and the largest client's notice term (EV-026) |
| P09 SOC 2 | The largest client's questionnaire (EV-026) and vendor documentation (EV-038) |
| P10 AI governance | AI tools found (EV-008, EV-009, EV-017, EV-036) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a firm-maintained inventory; the SSP (CM-8) plans one by 2026-10-31.
