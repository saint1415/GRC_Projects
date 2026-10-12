# Scenario facts: Cris Santos Company | Educational Services | Micro

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (operates a K-12 tutoring and learning center) |
| Business | Educational support and tutoring company (NAICS 611710): one-to-one and small-group tutoring in reading, writing, and math for grades K-12, plus SAT and ACT test preparation. Sessions are held in person at the learning center and live online through a vendor tutoring platform |
| Location | Florida. One learning center in a retail plaza (front desk, office, 6 tutoring rooms, 1 open study area). Online sessions are offered only to families with a Florida home address (a scenario choice that keeps state law to Florida) |
| Workforce | 7 employees: the Owner (Executive Director), 1 Center Director, 1 Director of Tutoring, 1 Enrollment and Billing Coordinator, 3 full-time Lead Tutors. Plus 14 part-time **contractor tutors** (independent contractors, not employees), who teach mostly online sessions from home |
| Students | About 420 students in the last 12 months: about 330 private-pay students from about 290 families, and 90 students in a school district after-school program. About **250 of the 420 are children under 13** (all 90 district students, grades 3 to 5, and about 160 private-pay students in grades K-6). The tutoring platform also holds records of about **1,900 former students** going back to 2019 (EV-016) |
| Volume | About 300 tutoring sessions a week (about 60 percent in person, 40 percent online). Open Monday to Friday 2:30 pm to 8:00 pm and Saturday 9:00 am to 2:00 pm (EV-018) |
| Revenue | About $1.1 million a year (fictional): about $920,000 from families (about $3,700 billed per operating day) and about $180,000 from the district contract. SBA-small (standard $24.0 million for NAICS 611710) (EV-034) |
| School district contract | A Florida public school district pays the company to run after-school tutoring at 2 elementary schools (Tuesday and Thursday, 3:00 pm to 4:30 pm) for about 90 students. The contract and its **data privacy agreement** designate the company a "school official" under FERPA (34 CFR 99.31(a)(1)(i)(B)) for the program. The district sends a roster with student names, grade, teacher, reading and math assessment scores, and accommodation notes. Contract terms: use the data only for the program; no redisclosure; reasonable safeguards; notify the district within **48 hours** of discovering unauthorized access; delete district data within 60 days after the contract ends and certify deletion; district may audit. The contract states it is paid from the district's general operating funds. The district sends an annual vendor security questionnaire (due 2026-09-30) (EV-027; EV-032) |
| Regulatory status | Determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv). **COPPA operator** (16 CFR 312.2; N61-R03): the tutoring platform is an online service directed to children, and the company collects children's personal information through it (names, user names, voice and video in online sessions and recordings, work samples) (EV-016; EV-004). **Not a FERPA institution** (34 CFR 99.1): it receives no funds under a Department of Education program. FERPA reaches it only through the district contract (99.31(a)(1)(i)(B); 99.33(a)) (EV-027; EV-034). **Not subject to the GLBA Safeguards Rule**: it is not a Title IV participant and offers no financing or payment plans (families pay monthly in advance by card) (EV-018). Florida covered entity under Fla. Stat. 501.171 |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): GLBA and FSA requirements; HIPAA (not a covered entity; evaluation reports that parents share are held as tutoring records); CIPA (not an E-Rate recipient); CIRCIA (proposed only; the company would also fall below the proposed size criterion); payment cards (card data is entered in the scheduling and billing platform's hosted payment fields and processed by its payment processor; the company stores no card numbers (EV-023). Noted only) |
| State law approach | Florida law cited only where unavoidable (breach notice and disposal, Fla. Stat. 501.171) |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Owner (Executive Director) | Accepts risk; approves policies and spending; signs the district contract; decision maker in incidents |
| Center Director | **Information Security Coordinator** under 16 CFR 312.8(b)(1) and privacy contact for parents (designated in writing on 2026-07-13, the first day of fieldwork; EV-037). Runs daily operations, staff and contractor onboarding and offboarding, and the MSP relationship |
| Director of Tutoring | Academic lead and district program coordinator. Administers the tutoring platform (SYS-01): tutor accounts, course setup, and the AI progress insights module (AI-001 business owner) |
| Enrollment and Billing Coordinator | Runs the scheduling and billing platform (SYS-02): family accounts, enrollment agreements and consent records, invoices |
| Lead Tutors (3) | Tutoring in person and online; supervise contractor tutors' session notes |
| Contractor tutors (14) | Independent contractors; teach mostly online sessions from home on their own computers (SYS-07) |
| Managed service provider (MSP) | IT support, laptop patching, antivirus, firewall and Wi-Fi, productivity suite administration, backup administration. Contract: help desk with a 4-business-hour response time; no recovery time commitment (EV-025) |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds children's personal information? | Notes |
|---|---|---|---|---|
| SYS-01 | Tutoring and learning platform: student portal (practice exercises, work samples), live online classroom with session recording, tutor session notes, assessment results, progress reports, tutor-parent messaging, AI progress insights module | Vendor SaaS | Yes (system of record) | Vendor provides a SOC 2 Type 2 report (never requested before this engagement) (EV-028; EV-038). MFA available but **not enforced** (EV-004). Session recordings kept indefinitely (default setting) (EV-004; EV-016) |
| SYS-02 | Scheduling, enrollment, and billing platform with parent portal: family accounts, enrollment agreements with a privacy check box, invoices, card payments through the integrated processor | Vendor SaaS | Yes (child's name, age, grade, school; parent contact details) | Administrator login (Enrollment and Billing Coordinator) has **no MFA** (EV-005) |
| SYS-03 | Business productivity suite: email, shared drive, calendar, chat | SaaS | Yes | MFA enforced for staff. Shared drive "Student files" folder holds intake forms and **evaluation reports and IEP or 504 plan excerpts that parents provide** for about 260 students, plus the district roster spreadsheets (EV-006; EV-007) |
| SYS-04 | Endpoints: 7 company laptops (4 staff, 3 Lead Tutors), 1 front-desk desktop, 10 student tablets in kiosk mode | MSP-managed | Cached (laptops and desktop) | Laptops encrypted; **front-desk desktop not encrypted** (EV-010). Tablets hold no student data (platform runs in the browser) (EV-009) |
| SYS-05 | Center network: small-business firewall, one internet line, staff Wi-Fi, and a "student and guest" Wi-Fi | On-premises | In transit | MSP-managed. **Both Wi-Fi networks are on the same network segment**; the guest password is posted at the front desk (EV-013; EV-036) |
| SYS-06 | SaaS-to-SaaS backup of the productivity suite (email and shared drive) | SaaS, operated by the MSP | Yes | Nightly; 30 days of versions; one MSP administrator account **without MFA**; never restore-tested (EV-014) |
| SYS-07 | Contractor tutors' personal computers | Not managed (bring your own device) | Yes (session notes; district roster spreadsheets received by email) | No device requirements in the contractor agreement (EV-026) |
| SYS-08 | Public website with inquiry and free-assessment sign-up form, and the online privacy notice | Website builder SaaS | No (collects parent contact details only) | Privacy notice is a generic template (EV-019) |

**SSP system (P02):** the *Tutoring Operations Platform (TOP)*: SYS-01 to SYS-06 and SYS-08, with SYS-07 (contractor tutors' personal computers) treated as external systems that connect to it.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). For a 7-person tutoring company the systems of record are the vendor admin consoles (tutoring platform, scheduling platform, productivity suite, website builder), the payroll service, the MSP's exports and monthly report, the contracts and vendor folders, the card and bank statements, the Center Director's mailbox and roster, and a walk-through of the center. Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the COPPA Rule and the FERPA conditions in the district contract** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Registry defaults adapted | Primary system kept as the core business SaaS stack, named the Tutoring Operations Platform. Incident kept (ransomware with student record exposure). AI use case changed from "AI admissions and student-success risk scoring" to **student-progress risk scoring in the tutoring platform**: a tutoring company has no admissions decisions, but it does score students' progress |
| P03 regulation | **COPPA Rule, 16 CFR Part 312** (N61-R03) instead of the vertical default (GLBA Safeguards Rule): the company is not a Title IV institution or a financial institution, and COPPA is the federal rule that governs its core service. FERPA duties that flow down through the district contract are added as a short secondary section |
| P08 incident | Ransomware with student record exposure: a phishing email to the Enrollment and Billing Coordinator leads to theft of the "Student files" folder and encryption of center computers. The MSP and the cyber insurer's panel are in the notification chain; the district must be told within 48 hours |
| P09 SOC 2 | Security plus Confidentiality. Used to answer the district's vendor security questionnaire (due 2026-09-30). Includes a review of the tutoring platform vendor's SOC 2 Type 2 report |
| P10 AI | AI-001: student-progress risk scoring (AI progress insights module in SYS-01), used by the Director of Tutoring for district program placement and session recommendations to parents |
| Cloud | SaaS plus one cloud workload: the SaaS-to-SaaS backup of the suite (SYS-06), operated by the MSP. Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, exports from the vendor consoles, the payroll service and the MSP, the contracts and vendor folders, the card and bank statements, intake interviews, a walk-through of the center, inventories, obligations register |
| 2026-07-13 to 2026-07-24 | BIA interviews, risk assessment and gap analysis with the MSP |
| 2026-07-27 to 2026-07-31 | Policies drafted from the gaps |
| 2026-08-03 to 2026-08-05 | Control assessment (independent consultant): operating tests of controls already in place; design review of the draft policies |
| 2026-08-28 | Deliverables and policies approved by the Owner |
| 2026-09-08 | District after-school program restarts for the new school year |
| 2026-09-30 | District vendor security questionnaire due |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6. Facts drawn from the company's records cite the evidence register ID they rest on.

| Topic | Added fact | Used in |
|---|---|---|
| Finances and payroll | A cash reserve covers about 45 days of expenses; payroll and contractor payments run every two weeks through an outside payroll service (EV-034; EV-001) | P01, P05 |
| Platform vendor report | SOC 2 Type 2 (Security, Availability, Confidentiality), 12 months ending 2026-04-30; states RTO 8 hours, RPO 1 hour, and customer notice within 72 hours of confirming an incident. Reviewed 2026-08-18 by the Center Director with the independent consultant (EV-038) | P02, P05, P09 |
| Scheduling platform vendor | No SOC 2 report; standard terms state daily backups and no recovery objectives (EV-023) | P05, P09 |
| AI module | Released by the vendor in May 2026 and on by default; used by the Director of Tutoring from 2026-05-18; about 210 students scored; flags drove 34 of 36 district placement changes; 31 parent progress reports in June and July carried an AI-based session recommendation and 12 families added sessions (EV-033; EV-050). Turned off 2026-08-28 | P01, P03, P10 |
| Former users | Three former contractor tutors kept platform access for 2 to 7 months after their last session (disabled 2026-07-15; no sign-ins after leaving). A former temporary front-desk worker's scheduling account was found and disabled 2026-08-04. A former Enrollment and Billing Coordinator's website login was removed 2026-07-16 (EV-041; EV-AC-2) | P01, P04, P07 |
| Consent practices | About 35 trial accounts for prospective students were created in 2026 before consent. About 20 families pay by bank debit with only the check box as consent (EV-045; EV-018; EV-017) | P03, P07 |
| Parent requests | Two parent requests in 2026; one came from an email address not on the family account and was answered (EV-020) | P03 |
| Network | The firewall management page was reachable from the internet with a password only (found 2026-08-04; turned off 2026-08-06). Firewall logs are kept 7 days. The staff Wi-Fi password has not changed since 2023 (EV-SC-7; EV-049; EV-013) | P01, P04, P07, P08 |
| Front-desk desktop | Uses one shared login whose password has not changed since 2024; no screen lock (EV-009; EV-AC-2) | P02, P07 |
| Devices | Two laptops retired in 2025 have no wipe record. Younger children sign in to the student portal on center tablets with a picture password (EV-015; EV-004) | P02, P09 |
| Contractor computers | During P07, 2 of the 3 contractor tutors interviewed still had district roster spreadsheets in their downloads folders (deleted on screen) (EV-AC-20) | P07 |
| Platform settings | Idle tutor sessions end after 30 minutes; the platform shows the top two factors behind each AI flag (EV-004; EV-033) | P02, P10 |
| Assessor | The P07 assessor is an independent security consultant, not involved in the risk assessment or gap analysis and operating no control | P07 |
| Child safety | The company has a child-safety code of conduct and a child-safety reporting procedure, separate from POL-03 (EV-031) | P06, P09 |
