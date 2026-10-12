# Intake Report: Cris Santos Company | Educational Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (private, for-profit career college, one Florida campus and online programs) |
| Intake window | 2026-06-22 to 2026-07-02 |
| Collected by | IT Director (Qualified Individual), with the Registrar and the Director of Financial Aid |
| Approved | Campus President, 2026-08-21 |

## 1. Purpose and scope
Intake collected the college's own records before any assessment work began on 2026-07-06. It covers the organization, the systems that hold customer information (16 CFR 314.2(d)) and education records, the suppliers that touch them, and the rules that may bind the college. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, reviews, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-010 | Identity provider; HR system; IT ticketing; SIS, FAMS and LMS admin consoles; integration documentation | 2024-08-01 to 2026-06-30 |
| Devices and network | EV-011 to EV-014 | Device management console; antivirus console; firewall management; campus walk-through | 2026-06-23 to 2026-06-30 |
| Cloud, data handling and logging | EV-015 to EV-019 | Cloud provider console; backup service; file server; productivity suite; audit log settings | 2026-06-24 to 2026-06-30 |
| Documents and records | EV-020 to EV-031 | Shared drive; Campus President's files; IT ticketing; HR learning records and files; Board records; Registrar's office | 2022-07-01 to 2026-06-30 |
| Suppliers and contracts | EV-032 to EV-037 | Accounting system; contracts folder; vendor file; provider portals and trust pages; insurance policy | 2026-01-01 to 2026-06-30 |
| Title IV and business volume | EV-038 to EV-042 | Director of Financial Aid's files; compliance audit report; accounting system; SIS reporting; FAMS and SIS aid records | 2025-12-15 to 2026-06-30 |
| Student records (FERPA) | EV-043 to EV-045 | College catalog; Registrar's FERPA records; LMS course setup | 2026-01-05 to 2026-06-30 |
| AI tools | EV-046, EV-047 | SIS analytics module configuration; CRM admin console | 2026-06-26 |

## 3. Observations by area
**Users and access.** All 60 staff have named identity provider accounts with MFA registered; MFA is optional for students, and staff MFA uses push approval without number matching (EV-001, EV-002). HR recorded 5 staff terminations and 9 adjunct contract ends from January to June 2026 (EV-003), and IT has 5 staff termination tickets, each with an open and a closed date (EV-004). The exit checklist covers a confidentiality reminder and return of the laptop and badge (EV-005). In the SIS, admissions representative and advisor roles can view every student's full record, including aid holds. Aid awarding and disbursing roles are held by different staff (EV-006). The financial aid servicer holds 6 local FAMS administrator accounts that sign in with a password and have no MFA setting (EV-007). Adjunct faculty use local LMS accounts (EV-008). Students can change refund bank details in the portal without MFA or an out-of-band confirmation (EV-009). The integration server uses one service account with read-write rights to all SIS and FAMS objects, its secret sits in a configuration file unchanged since installation, and ISIR fields are mapped into the reporting database (EV-010).

**Devices and network.** Device management lists 70 staff endpoints and 150 lab PCs, with full-disk encryption reported on 70 of 70 staff endpoints, a 10-minute screen lock and automatic OS patching (EV-011). Signature antivirus runs on staff endpoints and lab PCs, with alerts sent to a shared mailbox and no endpoint detection and response agent (EV-012). Staff, lab and student and guest Wi-Fi are on separate segments. Lab-to-staff firewall rules were last modified in 2023, outbound traffic has no transfer alerting, the campus has one internet provider, and the firmware record shows no update schedule (EV-013). At the walk-through, the Lab Coordinator stated that one local administrator password is set on all 150 lab PCs and that IT students use a shared lab administrator account. The records room key is held by 9 staff with no key log presented, and the 2 SAIG workstations are also used for email and web browsing (EV-014).

**Cloud, data handling and logging.** The cloud tenant holds the integration server, reporting database, file server and backup vault in one account and region, and the 3 IT staff administer both production and backups (EV-015). Daily backups completed from April to June 2026. Vault immutability is off, and no restore jobs were run (EV-016). The financial aid export folder holds ISIR and award spreadsheets readable by 14 staff, with no file-level encryption (EV-017). Email transport encryption is opportunistic, and no rule enforces message encryption or detects SSNs. Financial aid staff email aid spreadsheets to the business office and the servicer (EV-018). The SIS, FAMS, identity provider and cloud tenant log sign-ins and administrative changes. No alert rules are configured, and no log review records were provided (EV-019).

**Documents and records.** The document request returned no change management procedure, contingency plan, retention and disposal schedule for customer information, penetration test report, access review records, Board reports from the Qualified Individual, or written approvals of alternatives to encryption or MFA (EV-020). The WISP dates from 2023 with no later revision (EV-021). The IT Director was designated Qualified Individual on 2024-03-04 (EV-022). The last risk assessment is dated June 2024 and does not mention the online IT programs, the current LMS or the early-alert pilot (EV-023). The incident response document is a two-page contact list from 2023 (EV-024). The ticket history shows 2 phishing events in 2026, handled by the IT Director with no lessons-learned notes (EV-025). The only scan report is a 2025 scan run with a trial tool (EV-026). Annual security awareness and FERPA training reached 96% of staff, with content dated 2023 and no IT-specific course (EV-027). The handbook has a general discipline section (EV-028). Board minutes from 2024 to June 2026 record no written report from the Qualified Individual (EV-029). The records policy covers academic records only (EV-030). Paper is shredded by a vendor with certificates, and retired drives are wiped in-house with no record (EV-031).

**Suppliers and contracts.** Payments went to 14 suppliers (EV-032). The SIS, LMS and FAMS contracts carry security, confidentiality and FERPA school-official clauses. The SIS contract does not address vendor use of college records to improve its models, and the servicer contract has general confidentiality language only (EV-033). No security questionnaires or SOC 2 reports were on file for the SIS, LMS or FAMS vendors or the servicer (EV-034). The cloud provider's SOC 2 report and shared responsibility documentation were downloaded from its portal (EV-035). SaaS vendors state encryption at rest and in transit, vendor backups and denial-of-service protection (EV-036). A cyber insurance policy provides a breach hotline and a panel of breach counsel and forensic firms (EV-037).

**Title IV and business volume.** The PPA includes the agreement to comply with 16 CFR Part 314, and the SAIG Enrollment Agreement covers the SAIG mailbox on 2 dedicated workstations (EV-038). An independent auditor performs the annual Title IV compliance audit (EV-039). FY2025 receipts were $20.7 million, about 80% from Title IV aid, with no E-Rate discounts and no health plan billing (EV-040). About 900 students are enrolled, about 600 in healthcare programs and about 300 online, all adult learners, with start dates every 6 weeks (EV-041). The FAMS and SIS aid records cover about 6,400 consumers (EV-042).

**Student records (FERPA).** The 2026 catalog carries the annual FERPA notice (EV-043). The Registrar keeps a request log, a consent form, a redisclosure notice and a paper disclosure log, which has no entries from financial aid or career services (EV-044). Program directors collect immunization and background check documents as LMS assignments (EV-045).

**AI tools.** The SIS early-alert pilot covers 214 students in 2 programs since the May 2026 term, with inputs that include home ZIP code, Pell eligibility and first-generation status. The request for fairness test results, a student notice and a written human review rule returned none (EV-046). The CRM's applicant scoring feature is available and turned off (EV-047).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| FAMS vendor SOC 2 report | Director of Financial Aid | 2026-06-29 | None on file at intake; requested from the vendor in 2026-08 and tracked in POAM-002 |
| Financial aid servicer's security assurance (SOC 2 report or questionnaire) | Director of Financial Aid | 2026-06-29 | None on file; carried into the P01 risk register (R-009) and POAM-002 |
| Staff use of general-purpose AI tools with student data | Campus President | 2026-06-30 | Not established at intake; the P10 inventory covers the 2 vendor features found (EV-046, EV-047) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003), receipts and Title IV share (EV-040), enrollment and start dates (EV-041), backup schedule (EV-016), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-019 |
| P04 Cloud mapping | Cloud and SaaS components (EV-015, EV-032) and provider assurance (EV-035, EV-036) |
| P01 Risk register | Likelihood inputs from the ticket history (EV-025), the scan report (EV-026), configuration exports and the walk-through |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The 2023 WISP (EV-021), the contact list (EV-024) and the records policy (EV-030) |
| P07 Control assessment | Populations to sample from (EV-001, EV-003, EV-004, EV-007, EV-008, EV-011) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register and the insurance policy (EV-037) |
| P09 SOC 2 | Vendor assurance on file (EV-034, EV-035) |
| P10 AI governance | AI features found (EV-046, EV-047) and the ISIR field mapping (EV-010) |
