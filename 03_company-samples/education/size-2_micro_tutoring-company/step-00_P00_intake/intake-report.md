# Intake Report: Cris Santos Company | Educational Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (K-12 tutoring and learning center, one Florida location) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | Center Director, with the MSP lead technician for the MSP exports |
| Approved | Owner, 2026-08-28 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that collect, store or send students' and families' information, the suppliers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

A 7-person tutoring company has no HR system, CMDB or accounts payable vendor master. Its systems of record are the vendor admin consoles (tutoring platform, scheduling platform, productivity suite, website builder), the payroll service, the Center Director's staff and contractor roster, the MSP's exports and monthly report, the contracts and vendor folders, the card and bank statements, the Center Director's mailbox, and what can be seen at the center.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the regulatory analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-008 | Payroll service; staff and contractor roster; tutoring platform, scheduling platform, suite and website builder admin consoles | 2026-06-30 to 2026-07-08 |
| Devices, network and backup | EV-009 to EV-015 | MSP device, encryption and antivirus consoles; MSP monthly report; firewall documentation; backup console; MSP tickets | 2026-06-30 to 2026-07-08 |
| Students, families and consent | EV-016 to EV-020 | Tutoring platform and scheduling platform reporting; enrollment agreement; website; Center Director's mailbox | 2026-06-30 to 2026-07-09 |
| Suppliers and contracts | EV-021 to EV-029 | Card and bank statements; vendor terms and documentation; contracts folder; vendor folder | 2026-06-30 to 2026-07-09 |
| Documents and records | EV-030 to EV-032 | Document request list; HR files; Center Director's mailbox | 2026-07-02 to 2026-07-09 |
| AI tools | EV-033 | Tutoring platform admin console; vendor release note | 2026-07-07 |
| Business volume | EV-034 | Outside accountant | 2025-12-31 |
| Interviews and walk-through | EV-035, EV-036 | Intake interviews; walk-through of the center | 2026-07-09 |
| Received after the intake window | EV-037, EV-038 | Owner's files; tutoring platform vendor | 2026-04-30 to 2026-07-13 |

## 3. Observations by area
**People and access.** Payroll lists 7 employees and 14 contractor tutors paid every two weeks, and 2 employee separations in the 12 months, the former Enrollment and Billing Coordinator and a temporary front-desk worker (EV-001). The Center Director's roster records screening and child-safety training dates before each person's first session, marks former contractor tutors inactive, and has no column for account set-up or removal (EV-002). The tutoring platform has 24 active staff and tutor accounts, each named to one person; the Director of Tutoring and the 3 Lead Tutors hold the administrator role, and about 35 trial student accounts were created in 2026 (EV-003). Platform MFA is available and not enforced; idle tutor sessions end after 30 minutes; retention is at the default, with no end date; recordings can be shared by link; and the export history shows no exports (EV-004). The scheduling platform administrator signs in with a password only, and its MFA option is off (EV-005). The suite has 7 staff accounts with MFA enforced and no alert rules configured (EV-006). The "Student files" folder is open to all 7 staff and holds evaluation reports and IEP or 504 plan excerpts for about 260 students and the district rosters (EV-007). The website builder has a login in the name of the former Enrollment and Billing Coordinator (EV-008).

**Devices, network and backup.** The MSP manages 7 laptops and 1 front-desk desktop, each with its remote management agent; the 10 student tablets run in kiosk mode with no stored student data. The front-desk desktop uses one shared login, last changed in 2024, and has no screen lock (EV-009). The 7 laptops are encrypted and the desktop is not (EV-010). The MSP patches monthly, updates firewall firmware quarterly, and runs signature antivirus; its services do not include endpoint detection and response or log monitoring (EV-011). Antivirus alerts go to an MSP mailbox checked in business hours (EV-012). Staff and student and guest Wi-Fi share one network segment; the staff Wi-Fi password was last changed in 2023; firewall logs are kept for 7 days (EV-013). The suite backup runs nightly with 30 days of versions, immutable retention off, one MSP administrator account with no second factor, and no restore jobs (EV-014). Two laptops retired in 2025 have no wipe record (EV-015).

**Students, families and consent.** About 420 students were active in the last 12 months, about 250 of them under 13; the platform also holds records of about 1,900 former students and every recording since 2019 (EV-016). Consent is a check box in the online enrollment agreement, which lists name, grade and school and offers no separate choice about disclosures to third parties (EV-017). About 300 sessions run a week; about $77,000 is billed each month; about 20 families pay by bank debit (EV-018). The website privacy notice is a generic template with no list of third parties, retention period or parents' rights (EV-019). Two parent requests in 2026 were answered by email, one from an address not on the family account, with no identity check recorded (EV-020).

**Suppliers and contracts.** The statements show recurring payments to 9 suppliers and no separate charges from AI tool vendors (EV-021). The platform terms allow de-identified customer data to be used to improve the vendor's products, including AI features, and the offered data processing addendum is not signed (EV-022). The scheduling platform vendor states daily backups, gives no recovery objectives and offers no SOC 2 report; card numbers go into the processor's hosted fields (EV-023). The suite, backup and website vendors describe encryption and TLS (EV-024). The MSP contract has a 4-business-hour response time, no recovery time commitment, and no security, incident notice or subcontractor terms (EV-025). The contractor tutor agreement has no confidentiality, security, device, incident reporting or deletion terms (EV-026). The district contract and data privacy agreement set a 48-hour notice term, deletion within 60 days after the contract ends, and a district audit right (EV-027). No vendor assurance documents are on file; the platform vendor's SOC 2 report was first requested on 2026-07-07 (EV-028). A cyber liability policy with a breach hotline and panel vendors is on file (EV-029).

**Documents and records.** The document request returned no written security program, policies, risk assessment, incident response plan, contingency procedures, retention policy, inventory, or written designation of a security coordinator (EV-030). The employee handbook has a short confidentiality clause, and a child-safety code of conduct and reporting procedure exist (EV-031). The district's annual vendor security questionnaire is due 2026-09-30 (EV-032).

**AI tools.** The vendor turned on the AI progress insights module by default in its May 2026 release; the Director of Tutoring has used it since 2026-05-18, and about 210 students have been scored. The platform's homework helper chatbot is listed and off (EV-033).

**Business volume.** Revenue was about $1.1 million in FY2025: about $920,000 from families, about $3,700 billed per operating day, and about $180,000 from the district contract. Cash on hand covers about 45 days of expenses (EV-034).

**Interviews and walk-through.** Accounts are added and removed when remembered, with no checklist. District rosters are emailed to program contractor tutors at personal addresses. The AI flags are used for district placement and progress report recommendations with no written review rule. Tutors use public chatbots to make worksheets. No interviewee named the district's 48-hour notice term or a Florida deadline (EV-035). The walk-through counted 7 laptops, 1 desktop and 10 tablets, found the network closet locked, and found the student and guest Wi-Fi password posted at the front desk (EV-036).

**Received after the intake window.** The Owner signed the Center Director's designation as Information Security Coordinator on 2026-07-13 (EV-037). The platform vendor's SOC 2 Type 2 report arrived on 2026-07-16; it covers the 12 months ending 2026-04-30, states an RTO of 8 hours and an RPO of 1 hour, and does not cover the AI module (EV-038).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Tutoring platform vendor SOC 2 report | Platform vendor | 2026-07-07 | Received 2026-07-16 (EV-038, Intake follow-up) |
| Written designation of a security coordinator | Owner | 2026-07-09 | Signed 2026-07-13 (EV-037, Intake follow-up) |
| Number of tutors using public chatbots, and what they enter | Director of Tutoring | 2026-07-10 | Not established at intake; carried into P01 (R-022) and P10 (AI-002) |
| MSP technician list and evidence of MFA on the remote management platform | MSP lead technician | 2026-07-08 | Not provided; asked again for P07 on 2026-07-27 and carried into the P01 risk register (R-013) and POAM-007 |
| Name of the backup subcontractor and its security terms | MSP lead technician | 2026-07-08 | Not provided; asked again for P07 on 2026-07-27 and carried into POAM-007 |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-035), revenue, cash and session volume (EV-034, EV-018), district contract terms (EV-027), backup schedule (EV-014), vendor recovery figures (EV-023, EV-025, EV-038), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-003 to EV-015 and EV-017 |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-003 to EV-008, EV-014, EV-021) and provider documentation (EV-022 to EV-024, EV-038) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the roster and payroll records, the contracts folder, the walk-through (EV-036) and the intake interviews (EV-035) |
| P03 Regulatory analysis | The obligations register (which rules apply) and every observation above, compared with the COPPA Rule and the FERPA conditions in the district contract |
| P06 Policies | The document request response (EV-030), the handbook and child-safety documents (EV-031), and the designation letter (EV-037) |
| P07 Control assessment | Populations to test from (EV-001, EV-002, EV-003, EV-005, EV-006, EV-008) |
| P08 IR runbook | Notification duties from the obligations register and the district contract (EV-027); contacts from the vendor register; the cyber policy (EV-029) |
| P09 SOC 2 | The district questionnaire (EV-032) and vendor assurance (EV-038) |
| P10 AI governance | AI tools found (EV-021, EV-033, EV-035) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a company-maintained inventory; the SSP (CM-8) plans one by 2026-10-31.
