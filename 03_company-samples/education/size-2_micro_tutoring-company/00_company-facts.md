# Scenario facts: Cris Santos Company | Educational Services | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (operates a K-12 tutoring and learning center) |
| Business | Educational support and tutoring company (NAICS 611710): one-to-one and small-group tutoring in reading, writing, and math for grades K-12, plus SAT and ACT test preparation. Sessions are held in person at the learning center and live online through a vendor tutoring platform |
| Location | Florida. One learning center in a retail plaza (front desk, office, 6 tutoring rooms, 1 open study area). Online sessions are offered only to families with a Florida home address (a scenario choice that keeps state law to Florida) |
| Workforce | 7 employees: the Owner (Executive Director), 1 Center Director, 1 Director of Tutoring, 1 Enrollment and Billing Coordinator, 3 full-time Lead Tutors. Plus 14 part-time **contractor tutors** (independent contractors, not employees), who teach mostly online sessions from home |
| Students | About 420 students in the last 12 months: about 330 private-pay students from about 290 families, and 90 students in a school district after-school program. About **250 of the 420 are children under 13** (all 90 district students, grades 3 to 5, and about 160 private-pay students in grades K-6). The tutoring platform also holds records of about **1,900 former students** going back to 2019 |
| Volume | About 300 tutoring sessions a week (about 60 percent in person, 40 percent online). Open Monday to Friday 2:30 pm to 8:00 pm and Saturday 9:00 am to 2:00 pm |
| Revenue | About $1.1 million a year (fictional): about $920,000 from families (about $3,700 billed per operating day) and about $180,000 from the district contract. SBA-small (standard $24.0 million for NAICS 611710) |
| School district contract | A Florida public school district pays the company to run after-school tutoring at 2 elementary schools (Tuesday and Thursday, 3:00 pm to 4:30 pm) for about 90 students. The contract and its **data privacy agreement** designate the company a "school official" under FERPA (34 CFR 99.31(a)(1)(i)(B)) for the program. The district sends a roster with student names, grade, teacher, reading and math assessment scores, and accommodation notes. Contract terms: use the data only for the program; no redisclosure; reasonable safeguards; notify the district within **48 hours** of discovering unauthorized access; delete district data within 60 days after the contract ends and certify deletion; district may audit. The contract states it is paid from the district's general operating funds. The district sends an annual vendor security questionnaire (due 2026-09-30) |
| Regulatory status | **COPPA operator** (16 CFR 312.2): the tutoring platform is an online service directed to children, and the company collects children's personal information through it (names, user names, voice and video in online sessions and recordings, work samples). **Not a FERPA institution** (34 CFR 99.1): it receives no funds under a Department of Education program. FERPA reaches it only through the district contract (99.31(a)(1)(i)(B); 99.33(a)). **Not subject to the GLBA Safeguards Rule**: it is not a Title IV participant and offers no financing or payment plans (families pay monthly in advance by card). Florida covered entity under Fla. Stat. 501.171 |
| Not in scope | GLBA and FSA requirements; HIPAA (not a covered entity; evaluation reports that parents share are held as tutoring records); CIPA (not an E-Rate recipient); CIRCIA (proposed only; the company would also fall below the proposed size criterion); payment cards (card data is entered in the scheduling and billing platform's hosted payment fields and processed by its payment processor; the company stores no card numbers. Noted only) |
| State law approach | Florida law cited only where unavoidable (breach notice and disposal, Fla. Stat. 501.171) |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Owner (Executive Director) | Accepts risk; approves policies and spending; signs the district contract; decision maker in incidents |
| Center Director | **Information Security Coordinator** under 16 CFR 312.8(b)(1) and privacy contact for parents (designated in writing on 2026-07-13, the first day of this engagement). Runs daily operations, staff and contractor onboarding and offboarding, and the MSP relationship |
| Director of Tutoring | Academic lead and district program coordinator. Administers the tutoring platform (SYS-01): tutor accounts, course setup, and the AI progress insights module (AI-001 business owner) |
| Enrollment and Billing Coordinator | Runs the scheduling and billing platform (SYS-02): family accounts, enrollment agreements and consent records, invoices |
| Lead Tutors (3) | Tutoring in person and online; supervise contractor tutors' session notes |
| Contractor tutors (14) | Independent contractors; teach mostly online sessions from home on their own computers (SYS-07) |
| Managed service provider (MSP) | IT support, laptop patching, antivirus, firewall and Wi-Fi, productivity suite administration, backup administration. Contract: help desk with a 4-business-hour response time; no recovery time commitment |

## 3. Systems
| ID | System | Hosting | Holds children's personal information? | Notes |
|---|---|---|---|---|
| SYS-01 | Tutoring and learning platform: student portal (practice exercises, work samples), live online classroom with session recording, tutor session notes, assessment results, progress reports, tutor-parent messaging, AI progress insights module | Vendor SaaS | Yes (system of record) | Vendor provides a SOC 2 Type 2 report (never requested before this engagement). MFA available but **not enforced**. Session recordings kept indefinitely (default setting) |
| SYS-02 | Scheduling, enrollment, and billing platform with parent portal: family accounts, enrollment agreements with a privacy check box, invoices, card payments through the integrated processor | Vendor SaaS | Yes (child's name, age, grade, school; parent contact details) | Administrator login (Enrollment and Billing Coordinator) has **no MFA** |
| SYS-03 | Business productivity suite: email, shared drive, calendar, chat | SaaS | Yes | MFA enforced for staff. Shared drive "Student files" folder holds intake forms and **evaluation reports and IEP or 504 plan excerpts that parents provide** for about 260 students, plus the district roster spreadsheets |
| SYS-04 | Endpoints: 7 company laptops (4 staff, 3 Lead Tutors), 1 front-desk desktop, 10 student tablets in kiosk mode | MSP-managed | Cached (laptops and desktop) | Laptops encrypted; **front-desk desktop not encrypted**. Tablets hold no student data (platform runs in the browser) |
| SYS-05 | Center network: small-business firewall, one internet line, staff Wi-Fi, and a "student and guest" Wi-Fi | On-premises | In transit | MSP-managed. **Both Wi-Fi networks are on the same network segment**; the guest password is posted at the front desk |
| SYS-06 | SaaS-to-SaaS backup of the productivity suite (email and shared drive) | SaaS, operated by the MSP | Yes | Nightly; 30 days of versions; one MSP administrator account **without MFA**; never restore-tested |
| SYS-07 | Contractor tutors' personal computers | Not managed (bring your own device) | Yes (session notes; district roster spreadsheets received by email) | No device requirements in the contractor agreement |
| SYS-08 | Public website with inquiry and free-assessment sign-up form, and the online privacy notice | Website builder SaaS | No (collects parent contact details only) | Privacy notice is a generic template |

**SSP system (P02):** the *Tutoring Operations Platform (TOP)*: SYS-01 to SYS-06 and SYS-08, with SYS-07 (contractor tutors' personal computers) treated as external systems that connect to it.

## 4. Current security posture: early to partial
**In place today:**
- MFA on the productivity suite for all staff
- MSP patching, antivirus, and firewall management for company devices
- Unique accounts for staff and contractor tutors in the tutoring platform and the scheduling platform
- Full-disk encryption on the 7 company laptops
- Background screening and child-safety training for every tutor before they work with students
- No card numbers stored by the company (hosted payment fields)
- Signed data privacy agreement with the school district
- A cyber liability policy with a 24x7 breach hotline and panel vendors (breach counsel, forensics)

**Missing:**
1. No written information security program, although COPPA 312.8(b) requires one (compliance date April 22, 2026).
2. No risk assessment has ever been done.
3. The online privacy notice is a generic template. It does not meet 16 CFR 312.4(d): no list of third parties, no retention policy, no description of parents' rights.
4. Parental consent is a check box in the online enrollment agreement. The direct notice does not contain what 312.4(c)(1) requires, and no separate consent is asked for disclosures that are not integral to the service (312.5(a)(2)).
5. No written data retention policy (312.10). Former students' records and online session recordings are kept indefinitely.
6. Contractor tutors use personal computers, receive district roster spreadsheets by email, and sign a contractor agreement with no confidentiality or security terms.
7. MFA is not enforced in the tutoring platform or on the scheduling platform's administrator login.
8. Staff laptops and student and guest devices share one network segment.
9. The suite backup has never been restore-tested, and the tutoring platform's data has never been exported.
10. No incident response plan; nobody knows the district's 48-hour notice term or the Florida deadlines.
11. Contractor tutor offboarding is ad hoc. Three former contractor tutors still had tutoring platform accounts (found 2026-07-15).
12. No vendor oversight: the platform vendor's SOC 2 report was never requested, and the AI progress insights module was switched on by the vendor with terms that allow use of de-identified data to improve its models.
13. No security awareness training (child-safety training only).
14. Parents' requests to review or delete their child's information are handled by email with no check that the requester is the parent (312.6(a)(3)(i)).

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
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis with the MSP |
| 2026-08-03 to 2026-08-05 | Control assessment (independent consultant) |
| 2026-08-28 | Deliverables approved by the Owner |
| 2026-09-08 | District after-school program restarts for the new school year |
| 2026-09-30 | District vendor security questionnaire due |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Finances and payroll | A cash reserve covers about 45 days of expenses; payroll and contractor payments run every two weeks through an outside payroll service | P01, P05 |
| Platform vendor report | SOC 2 Type 2 (Security, Availability, Confidentiality), 12 months ending 2026-04-30; states RTO 8 hours, RPO 1 hour, and customer notice within 72 hours of confirming an incident. Reviewed 2026-08-18 by the Center Director with the independent consultant | P02, P05, P09 |
| Scheduling platform vendor | No SOC 2 report; standard terms state daily backups and no recovery objectives | P05, P09 |
| AI module | Released by the vendor in May 2026 and on by default; used by the Director of Tutoring from 2026-05-18; about 210 students scored; flags drove 34 of 36 district placement changes; 31 parent progress reports in June and July carried an AI-based session recommendation and 12 families added sessions. Turned off 2026-08-28 | P01, P03, P10 |
| Former users | Three former contractor tutors kept platform access for 2 to 7 months after their last session (disabled 2026-07-15; no sign-ins after leaving). A former temporary front-desk worker's scheduling account was found and disabled 2026-08-04. A former Enrollment and Billing Coordinator's website login was removed 2026-07-16 | P01, P04, P07 |
| Consent practices | About 35 trial accounts for prospective students were created in 2026 before consent. About 20 families pay by bank debit with only the check box as consent | P03, P07 |
| Parent requests | Two parent requests in 2026; one came from an email address not on the family account and was answered | P03 |
| Network | The firewall management page was reachable from the internet with a password only (found 2026-08-04; turned off 2026-08-06). Firewall logs are kept 7 days. The staff Wi-Fi password has not changed since 2023 | P01, P04, P07, P08 |
| Front-desk desktop | Uses one shared login whose password has not changed since 2024; no screen lock | P02, P07 |
| Devices | Two laptops retired in 2025 have no wipe record. Younger children sign in to the student portal on center tablets with a picture password | P02, P09 |
| Contractor computers | During P07, 2 of the 3 contractor tutors interviewed still had district roster spreadsheets in their downloads folders (deleted on screen) | P07 |
| Platform settings | Idle tutor sessions end after 30 minutes; the platform shows the top two factors behind each AI flag | P02, P10 |
| Assessor | The P07 assessor is an independent security consultant, not involved in the risk assessment or gap analysis and operating no control | P07 |
| Child safety | The company has a child-safety code of conduct and a child-safety reporting procedure, separate from POL-03 | P06, P09 |
