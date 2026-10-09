# Intake Report: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm, headquarters and 3 other Florida branches) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager (Information Security Lead), with the HR and Compliance Manager and the Payroll Manager |
| Approved | COO, 2026-08-31 |

## 1. Purpose and scope
Intake collected the firm's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that hold candidate, associate and client data, the suppliers that touch them, and the rules that may bind the firm. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, samples, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-010 | Identity provider; payroll platform (users, HR module, reports); IT ticketing; HR files; ATS admin console | 2024-03-01 to 2026-07-02 |
| Devices and network | EV-011 to EV-017 | Device management console; EDR console; IT asset records; managed IT provider documentation, scans and remote tool; productivity suite admin console | 2026-06-26 to 2026-07-02 |
| Cloud and backups | EV-018 to EV-023 | Cloud provider console; reporting database; document archive; backup service | 2026-06-30 to 2026-07-02 |
| Documents and records | EV-024 to EV-029 | Shared drive and document request; HR files; learning records; IT ticketing; COO's files | 2025-01-01 to 2026-07-06 |
| I-9, E-Verify and FCRA programs | EV-030 to EV-034 | HR and Compliance Manager's files; E-Verify; ATS onboarding package; screening provider portal; payroll vendor tax filings | 2023-06-01 to 2026-07-06 |
| Suppliers and contracts | EV-035 to EV-042 | Accounting system; contracts folder and vendor files; vendor portals; ATS marketplace; timekeeping admin portal; insurance policy; client files | 2026-01-01 to 2026-07-06 |
| Facilities and disposal | EV-043 to EV-045 | HQ badge system; Branch Managers' responses; shredding certificates | 2026-06-30 to 2026-07-07 |
| Business volume | EV-046 to EV-048 | Accounting system; payroll platform reports; ATS reporting and screening invoices | 2025-12-31 to 2026-06-30 |
| Career site and AI tools | EV-049, EV-050 | Career site; staff survey and identity provider app list | 2026-07-06 to 2026-07-07 |

## 3. Observations by area
**Users and access.** The identity provider has 60 active named staff accounts, each with number-matching push MFA. Its application list includes the productivity suite, ATS, cloud console, timekeeping admin portal and AI add-on admin page; the payroll platform and E-Verify are not in it (EV-001). Sign-in logs are kept 30 days (EV-002). The HR module lists 60 current staff and 16 terminations from January 2025 to June 2026, including 2 Onboarding and Compliance Specialists who left in 2025 (EV-003). Termination tickets record when SSO access was disabled and do not name the payroll platform or E-Verify (EV-004), and the HR checklist does not list those two systems either (EV-005). The payroll platform uses local accounts with SMS one-time codes. The Payroll Specialist role can both edit bank accounts and submit payroll, the vendor's bank-change confirmation email is off, and no alert rules are set (EV-006). The Controller's approval is recorded for each weekly payroll register, and the change report has no scheduled runs (EV-007). The ATS recruiter and account manager roles can view I-9 images and consumer report PDFs for all 4 branches (EV-008). The I-9 module has been in use since 2022 with electronic signatures, a per-form change history and E-Verify case numbers, and no retention or purge rule is configured (EV-009). The ATS audit history shows the AI add-on set to rank and auto-advance on 2026-03-02, with no change request or approval recorded (EV-010).

**Devices and network.** Device management lists 62 laptops and 34 smartphones. Laptops patch automatically, report full-disk encryption on all 62 and lock after 10 minutes; the kiosks, scanners and network gear are not enrolled (EV-011). EDR runs on all 62 laptops and on none of the 8 kiosks, and after-hours alerts were reviewed the next business day (EV-012). One kiosk PC retired in 2025 was discarded, and the IT Support Specialist states its drive was not wiped. The kiosks share one local account (EV-013). Lobby kiosks connect to the staff network at all 4 offices, and guest Wi-Fi is separate (EV-014). Quarterly external scans cover only the 4 office firewall addresses (EV-015). The managed IT provider's remote tool uses named accounts with MFA (EV-016). Email has no external-sender warning rule (EV-017).

**Cloud and backups.** The cloud tenant runs the integration service, reporting database, document archive and backup vault. Two administrators hold standing rights, including over the backup vault (EV-018). Integration API credentials were last rotated in 2024 (EV-019). Data-access logging is off for the archive and the reporting database, and the archive has no versioning or object lock (EV-020). The reporting database holds full SSN and bank account columns for about 31,000 current and former associates, every recruiter account can query it, and no report reads those columns (EV-021). The archive holds scanned Forms I-9 from 2014 to 2022 and consumer report PDFs, indexed by a spreadsheet, with no purge records (EV-022). Daily snapshots complete in the same account and region as production, immutability is off, and no restore has ever been run (EV-023).

**Documents and records.** The request for policies, a prior risk assessment, an incident response plan, a breach notification procedure, a BIA, a contingency plan, a manual payroll procedure, a retention schedule, an electronic I-9 system description and I-9 check records returned none (EV-024). The 2025 handbook has one page on computer use (EV-025). The IT Manager was designated Information Security Lead on 2026-07-01 (EV-026). Training records show an annual awareness video only, with no phishing exercises or payroll fraud module (EV-027). Eighteen security-related tickets in 12 months had no incident category or post-incident notes (EV-028).

**I-9, E-Verify and FCRA programs.** The firm signed the E-Verify MOU in 2023 as a direct employer, and 4 users on the current roster have tutorial records (EV-030). Each new hire from January to June 2026 has an E-Verify case (EV-031). The background check disclosure page also holds a release of liability and state notices (EV-032). The screening provider sends pre-adverse and adverse action letters at least 5 business days apart when triggered (EV-033). The 2026 first-quarter reemployment tax return carries the E-Verify certification (EV-034).

**Suppliers and contracts.** Payments go to the ATS, payroll, identity, productivity, cloud, timekeeping, screening, managed IT, shredding, insurance, ISP and phone suppliers, and the AI add-on is billed through the ATS marketplace (EV-035). Only the payroll services agreement has security and breach notice terms. The ATS terms have no data return clause and no stated recovery objectives, and the ATS SOC 2 report has not been received (EV-036). The payroll vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 and has no review notes (EV-037). The AI add-on was bought with click-through terms and no bias test or validation report is on file (EV-039). The timekeeping app keeps clock-in locations for the life of the account (EV-040). The cyber policy requires MFA on email and remote access (EV-041). Client agreements contain no business associate agreement or federal contract clauses, and two 2026 client questionnaires ask about SOC 2 (EV-042).

**Facilities and disposal.** HQ uses badge access (EV-043). Branches 2 to 4 use keyed locks with no key log presented, and every branch has locked shred bins (EV-044). Monthly certificates of destruction are on file (EV-045).

**Business volume.** 2025 receipts were $20.4 million across 255 business days, with gross margin of about $4.8 million (EV-046). About 450 associates are paid in an average week, about $270,000 per payroll (EV-047). The firm took about 16,000 applications and made about 2,000 associate hires in 2025, all for Florida worksites (EV-048).

**Career site and AI tools.** The applicant privacy notice does not mention an automated scoring tool, and the site has no accommodation contact (EV-049). Recruiters use the AI add-on and the ATS generative AI feature, and staff report using public chatbots. No approved-tools list was found (EV-050).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| ATS vendor's SOC 2 Type 2 report and stated recovery objectives | ATS vendor (through the COO) | 2026-06-30 | Not received; P04 and P05 treat the ATS rows as unconfirmed (POAM-010) |
| Number of staff using public chatbots, and what they paste | COO | 2026-07-08 | Not established at intake; P10 treats it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003), receipts, payroll and hiring volume (EV-046 to EV-048), backup schedule (EV-023), vendor recovery statements (EV-036, EV-037), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001, EV-002, EV-006 to EV-023 |
| P04 Cloud mapping | Cloud and SaaS components (EV-018 to EV-023, EV-035) and provider assurance (EV-037, EV-038) |
| P01 Risk register | Likelihood inputs from the ticket history (EV-028), configuration exports, contracts and the AI add-on records (EV-039) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The handbook (EV-025) and the empty document request (EV-024) |
| P07 Control assessment | Populations to sample from (EV-001, EV-003, EV-004, EV-006, EV-008) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the insurer's breach hotline (EV-041) |
| P09 SOC 2 | Client questionnaires (EV-042) and vendor assurance on file (EV-037, EV-038) |
| P10 AI governance | AI tools found (EV-035, EV-039, EV-050) |
