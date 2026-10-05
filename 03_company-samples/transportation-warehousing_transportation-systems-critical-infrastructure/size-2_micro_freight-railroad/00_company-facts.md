# Scenario facts: Cris Santos Company | Transportation Systems | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given. Regulatory text was read on eCFR (point in time 2026-09-23, and 2026-10-01 for the FRA part 225 amendments effective 2026-09-30) and in the Federal Register on 2026-10-05.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; the owner also serves as General Manager) |
| Business | Short line freight railroad (NAICS 482112 Short Line Railroads). A Class III carrier under the Surface Transportation Board revenue classes (49 CFR part 1201, General Instructions 1-1) |
| Network | 16 route miles of company-owned main track in a rural north Florida county, from the interchange at Junction (mile 0) to an industrial park and a lumber mill at the end of the line. Non-signaled ("dark") territory, FRA Class 1 track (10 mph), run under track warrant control from one dispatch desk. Plus a daily interchange move of **2.5 miles over a Class I railroad's PTC-equipped, freight-only main line** to the Class I's yard, under the Class I dispatcher's authority. The Class I does not operate on company track |
| Facilities | One building at Junction: office, dispatch desk, and a two-track enginehouse (locomotive and car shop). One leased radio tower site at mile 8 with the company's repeater. 6 public highway-rail grade crossings with active warning devices (standalone circuits, not networked; inspected and tested by a contract signal maintainer) and 9 passive crossings |
| Equipment | 3 locomotives (2 in service, 1 spare); none carries onboard positive train control (PTC) apparatus. 1 hi-rail truck (camera kit for the P10 pilot) |
| Traffic | About 2,400 carloads a year from 6 customers: lumber and wood chips (lumber mill), dry fertilizer (not regulated as hazardous), crushed stone, plastic pellets (transload), feed grain, and **about 110 tank cars a year of liquefied petroleum gas (propane, Division 2.1)** for a propane distributor. No material poisonous by inhalation (PIH), no Division 1.1 to 1.3 explosives, no radioactive material. One interchange turn a day, 5 days a week (about 250 operating days a year); one shift, 07:00 to 15:30 |
| Location | Florida only. The whole line and the interchange move lie outside every Florida high threat urban area (HTUA) listed in Appendix A to 49 CFR part 1580. Map check by the General Manager on 2026-07-14 |
| Workforce | 7 employees: Owner and General Manager, Office Manager, Roadmaster, Track Maintainer, Locomotive Engineer, Conductor, Mechanic |
| Revenue | About $1.1 million a year (fictional), about $4,400 per operating day. SBA-small: the SBA standard for NAICS 482112 is 1,500 employees (13 CFR 121.201) |
| Customers | 6 shippers and receivers on line; the connecting Class I for all interchange traffic |
| TSA status | A freight railroad carrier that "operates rolling equipment on track that is part of the general railroad system of transportation" (49 CFR 1580.1(a)(1)). So **49 CFR 1570.201 (Security Coordinator) and 1570.203 (reporting significant security concerns, including "Cyber Attack" in Appendix A to part 1570) apply**, and the company is a covered person for Sensitive Security Information (SSI) under 49 CFR 1520.7(n). **Part 1580 subpart C does not apply**: it covers carriers that transport rail security-sensitive materials (RSSM) (1580.201(1)), and propane is not RSSM under 1580.3. **Part 1580 subpart B does not apply** (1580.101: not Class I, no RSSM in an HTUA, not a host to a covered railroad) |
| TSA cyber directives | **Not covered.** SD 1580-21-01E and SD 1580/82-2022-01E apply to railroads in 49 CFR 1580.101 and railroads TSA designates. TSA has never notified the company (confirmed 2026-07-14 by the General Manager; no TSA letter in the correspondence file). Details in P03 |
| FRA status | Subject to FRA safety rules, including accident/incident reporting (49 CFR part 225, 225.3) and track safety standards as a track owner (part 213). **No PTC duty:** 49 CFR 236.1005(b)(1) places the installation duty on Class I railroads and railroads that provide or host intercity or commuter passenger service. The interchange move runs unequipped on the Class I's PTC line under the exception for Class II and III trains in 236.1006(b)(4): the segment has no regularly scheduled passenger traffic, the company runs no more than 4 unequipped trains a day on it (its one daily turn counts as two), and each movement is under 20 miles |
| Hazmat security | Transports a large bulk quantity of Division 2.1 material (propane in tank cars), so it must have a hazmat transportation security plan (49 CFR 172.800(b)(3); components in 172.802) and give its hazmat employees security awareness and in-depth security training (172.704(a)(4)-(5)). Crews inspect hazmat cars at acceptance (174.9) |
| Not in scope | Passenger service (none). SEC disclosure (private company). FAR and CMMC clauses (no federal contracts). Payment cards (customers pay by invoice and ACH). HIPAA (no health plan or provider functions). CIRCIA and the TSA surface cyber NPRM are proposed only and are tracked, not treated as obligations |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification for employee personal information, Fla. Stat. 501.171) |

**Regulatory driver IDs used in this folder.** The vertical's `requirements.csv` lists C-TRANSPORTATION-R01 to R07. Of these, R01 (TSA rail cyber directives) does not apply and is used only for readiness rows; R06 (TSA surface cyber NPRM) and R07 (CIRCIA) are proposed rules, tracked only; R02 to R05 (pipeline, aviation, maritime) do not apply to a railroad. The binding rules that do apply are not in the registry, so this sample adds **scenario-level driver IDs**. They are defined here and nowhere else.

| ID | Requirement | Citation | Status for this company |
|---|---|---|---|
| C-TRANSPORTATION-S01 | TSA Security Coordinator and reporting of significant security concerns | 49 CFR 1570.201; 1570.203 and Appendix A to part 1570; 1570.105 | Applies (1580.1(a)(1) freight railroad) |
| C-TRANSPORTATION-S02 | TSA rail security-sensitive materials (RSSM) operations | 49 CFR part 1580 subpart C (1580.201, 1580.203, 1580.205) | Does not apply today (no RSSM carried). Would apply if a customer ships PIH, explosives, or highway route-controlled radioactive material |
| C-TRANSPORTATION-S03 | Protection of Sensitive Security Information (SSI) | 49 CFR part 1520 (1520.7(n), 1520.9) | Applies |
| C-TRANSPORTATION-S04 | FRA positive train control | 49 CFR part 236 subpart I (236.1005(b)(1); 236.1006(b)(4)) | No installation duty; the interchange move relies on the 236.1006(b)(4) exception |
| C-TRANSPORTATION-S05 | FRA accident/incident reporting | 49 CFR part 225 (225.9, 225.11) | Applies |
| C-TRANSPORTATION-S06 | Hazmat transportation security plan, security training, and rail car security inspection | 49 CFR 172.800, 172.802; 172.704(a)(4)-(5); 174.9 | Applies (propane, Division 2.1) |
| C-TRANSPORTATION-S07 | Florida breach notification | Fla. Stat. 501.171 | Applies to employee personal information |
| C-TRANSPORTATION-S08 | FRA track inspection duties | 49 CFR 213.7; 213.233 | Applies (track owner); relevant to the AI pilot in P10 |
| C-TRANSPORTATION-BM | NIST CSF 2.0 | Voluntary benchmark | Chosen because no binding cyber control rule applies |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Owner and General Manager | Accepts risk; approves policies and spending. **Primary TSA Security Coordinator** (1570.201). Senior management official for the hazmat security plan (172.802(b)(1)). Primary train dispatcher. Makes FRA part 225 reports |
| Office Manager | **Security Lead**: runs security day to day and directs the MSP (designated in writing in POL-02, 2026-08-31). Car accounting, waybills and interchange EDI, billing, payroll, and HR records. Coordinates Florida breach notices |
| Roadmaster | Designated qualified track inspector and supervisor (49 CFR 213.7). Relief train dispatcher. **Alternate TSA Security Coordinator**. Business owner of the AI pilot (P10) |
| Track Maintainer | Track maintenance; drives the hi-rail truck |
| Locomotive Engineer | Certified locomotive engineer; crew tablet user |
| Conductor | Certified conductor; hazmat car acceptance inspections (174.9) and shipping papers |
| Mechanic | Locomotive and car inspections; locomotive telematics; relief conductor |
| Managed service provider (MSP) | IT support, patching, antivirus, firewall, Wi-Fi, and backup administration. 4-business-hour response time; no recovery time commitment; no security terms in the contract |
| Operations SaaS vendor | Hosts the short line operations system (SYS-01); SOC 2 Type 2 report reviewed in P09 |
| Contract signal maintainer | Inspects and tests the grade crossing warning systems (not connected to any network) |

**Overlap.** The General Manager is risk acceptor, Security Coordinator, dispatcher, and policy approver. The Office Manager runs security and is also the person most of the controls depend on. The compensating checks are the MSP (which operates most technical controls and must report on them), an independent consultant for the control assessment (P07), and the operations SaaS vendor's SOC 2 report (P09).

## 3. Systems

| ID | System | Hosting | Operations-critical? | Notes |
|---|---|---|---|---|
| SYS-01 | Short line operations system: track warrants and track-and-time authorities with conflict checking, train sheets, slow orders and bulletins, car inventory and switch lists, waybills and interchange EDI with the Class I, hazmat car list, demurrage and invoicing | Vendor SaaS | Yes | System of record for movement authority. MFA enforced on the 2 administrator accounts (General Manager, Office Manager). The 3 crew tablets share one "crew" login without MFA |
| SYS-02 | Productivity suite: email and shared drive | SaaS | Yes | MFA on all 7 accounts. The shared drive holds the timetable and special instructions, track charts, the hazmat security plan, TSA correspondence (including 2 SSI-marked documents), employee files, and customer contracts. Synced to the desktops |
| SYS-03 | Endpoints: 3 desktops (dispatch desk, office, shop), 2 laptops (General Manager, Office Manager), 3 rugged crew tablets (engineer, conductor, Roadmaster) | MSP-managed | Dispatch desktop and tablets: yes | Laptops encrypted; desktops not. Tablets have a passcode and built-in encryption. The dispatch desktop runs the radio console software on an operating system version past end of vendor support (since October 2025) |
| SYS-04 | Office network: small-business firewall, office and enginehouse Wi-Fi, one business internet line | On premises | Yes | MSP-managed. No failover line |
| SYS-05 | Cloud backup of the productivity suite (shared drive and mailboxes) | SaaS | No | Set up by the MSP; nightly; 30 days of versions; never restore-tested |
| SYS-06 | Radio dispatch system: base station and desktop console at the dispatch desk, repeater at the mile 8 tower, locomotive and handheld radios | On premises and wayside (OT) | Yes | Radio carries every movement authority. The console software runs on the dispatch desktop (SYS-03). The repeater is linked by radio, not by IP |
| SYS-07 | Locomotive telematics: cellular units on the 2 road locomotives report location, fuel, and engine faults to a vendor portal | Onboard units (OT) plus vendor SaaS | No | Monitoring only; no remote control of the locomotive |
| SYS-08 | Accounting, payroll, and HR | SaaS | No | Employee personal information, including certification and drug and alcohol testing records |
| SYS-09 | Track defect detection (computer vision) pilot: camera kit on the hi-rail truck; video uploaded to the vendor's service, which flags suspected defects | Vendor SaaS | No (pilot) | Pilot since 2026-05-04 (see P10) |

**SSP system (P02):** the *Train Dispatch and Operations Back Office (TDOB)*: SYS-01 to SYS-07, with interfaces to SYS-08 and to the Class I's interchange EDI and dispatcher.

## 4. Current security posture: early to partial

**In place today:**
- Primary (General Manager) and alternate (Roadmaster) TSA Security Coordinators designated at the corporate level and reported to TSA (1570.201); reachable 24/7 by cell phone
- Hazmat transportation security plan for propane (172.800(b)(3)); hazmat training, including security awareness and in-depth security training, current for the 4 hazmat employees (172.704)
- Ground-level security inspection of hazmat cars at acceptance (174.9)
- FRA accident/incident reporting by the General Manager (part 225)
- MFA on email and on the operations system administrator accounts
- MSP patching, antivirus, and firewall
- Laptop encryption
- Paper track warrant forms and a printed timetable kept at the dispatch desk
- Locked office and enginehouse with an alarm
- Background checks at hire for positions that handle hazmat (172.802(a)(1))

**Missing:**
1. Cyber attacks are not treated as TSA-reportable events. There is no procedure to report to TSA within 24 hours (1570.203; Appendix A to part 1570, "Cyber Attack"). A 2025 mailbox compromise was not reported.
2. No incident response plan. Paper dispatch is a habit, not a written and exercised procedure.
3. The 3 crew tablets share one operations system login with no MFA. Its password was not changed when a conductor left in 2026-02.
4. The productivity suite backup has never been restore-tested. There is no company-held copy of operations system data.
5. No adopted security policies.
6. The MSP contract has no security terms, incident notice, or recovery commitment. No evidence that the MSP's remote tool requires MFA.
7. The dispatch desktop runs an operating system version past end of vendor support, kept for radio console compatibility.
8. Two TSA-marked SSI documents sit in the general shared drive, which every employee and the MSP can open. No SSI handling rules (1520.9).
9. No inventory of devices, SaaS accounts, or operations technology (radio, telematics).
10. No log review and no behavior-based malware detection (EDR).
11. The hazmat security plan's annual review is overdue (last reviewed 2025-03-18; 172.802(c)).
12. No cyber training or phishing awareness; only hazmat security training.
13. The AI defect detection pilot started without a contract review or an approved-tools list.
14. One internet line; dispatch depends on a SaaS system.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| Registry defaults adapted | **Primary system:** the registry default is "Train dispatching and positive train control back office". This railroad has no PTC system to back up (no installation duty under 236.1005(b)(1); its interchange move runs under the 236.1006(b)(4) exception), so the SSP system is the train dispatch and operations back office. **P08 incident:** adapted the same way, to ransomware on the dispatch and office back-office systems. **P10:** the registry default (track and equipment defect detection, computer vision) is kept, as a vendor SaaS pilot on the hi-rail truck |
| P03 regulation | The named primary regulation (TSA SD 1580/82-2022-01E) **does not apply**. P03 analyzes the binding TSA rules that do apply (49 CFR 1570.105, 1570.201, 1570.203, and SSI protection in 1520.9), the hazmat security plan and security training rules (49 CFR 172.800, 172.802, 172.704, 174.9), the FRA PTC applicability rows, and a short NIST CSF 2.0 benchmark. The SD rows are kept as a readiness reference |
| P08 incident | Ransomware on the dispatch and office back-office systems, starting from a phishing email; the MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | The railroad is not a service organization. Security plus Availability readiness self-assessment, used to answer the connecting Class I's cybersecurity questionnaire for connected short lines; plus a review of the operations SaaS vendor's SOC 2 Type 2 report |
| P10 AI | Track defect detection (computer vision) pilot on the hi-rail truck |
| Cloud | SaaS plus one cloud workload: the SaaS backup of the productivity suite, operated by the MSP. Vendor-agnostic |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk analysis and gap analysis with the MSP (applicability confirmed 2026-07-14) |
| 2026-08-04 to 2026-08-06 | Control assessment (independent consultant; on site 2026-08-05) |
| 2026-08-31 | Deliverables approved by the Owner and General Manager |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Business processes | 8 business processes, BP-01 to BP-08 (BP-07 is the TSA, FRA, and hazmat security obligations process) | P05, P01, P08 |
| Dispatch | The General Manager dispatches from the desk in the office; the Roadmaster relieves. The crew acknowledges each track warrant by radio and on the tablet. Roadway work on the main track is protected by track-and-time authority from the same system | P05, P02, P08 |
| Former conductor | Left on 2026-02-27. The shared crew password (last changed 2023-05) was found unchanged on 2026-07-15 during the risk analysis and changed on 2026-07-16. The vendor's 90-day sign-in history showed the crew login used only from the 3 company tablets | P01, P03, P07 |
| 2025 mailbox compromise | On 2025-10-14 a phishing email captured the Office Manager's password and an MFA approval. The attacker sent a fake bank-change invoice to one shipper, who called to check. No money was lost. It was not reported to TSA | P01, P03 |
| SSI documents | Two TSA documents marked SSI (received by email in 2024 and 2025) are stored in the general shared drive folder "TSA" | P01, P03, P06 |
| Dispatch desktop | The radio console vendor expects a version certified for the current operating system in 2026-11. The MSP excluded the dispatch desktop from operating system upgrades at the radio vendor's request | P01, P02, P07 |
| Cyber insurance | A cyber liability policy with a 24x7 breach hotline and panel vendors (breach counsel, forensics). The policy requires prompt notice and use of panel vendors | P08 |
| MSP contract | Covers help desk, patching, antivirus, firewall, Wi-Fi, and backup administration, with a 4-business-hour response time. Renewal 2026-12-31 | P05, P07 |
| Internet | One business internet line; the General Manager's phone hotspot is the informal fallback | P01, P05 |
| Assessor | The P07 assessor is an independent cybersecurity consultant with rail operations experience, not involved in the risk analysis or gap analysis and operating no control | P07 |
| Telematics portal | P07 testing found that the telematics portal (SYS-07) uses one shared administrator login, with the password set at installation in 2024 and no MFA | P01, P07 |
| Class I questionnaire | On 2026-07-20 the connecting Class I sent its connected short lines a cybersecurity questionnaire covering security and availability of interchange data. Response due 2026-10-30 | P09 |
| Operations SaaS vendor report | SOC 2 Type 2, Security and Availability, 12 months ending 2026-03-31, unqualified, one exception (late removal of 2 of 20 departed vendor staff, remediated). States RTO 4 hours and RPO 1 hour. Reviewed 2026-08-19 | P09, P05 |
| Budget | Approved by the Owner and General Manager on 2026-08-31: about $7,300 one-time and $4,040 a year | P01, P07 |
| AI pilot results | 12 weekly inspection runs (2026-05-04 to 2026-07-24). The Roadmaster recorded 23 defects; the model flagged 19 of them (83%). The model raised 141 flags, of which 31 were confirmed as defects (22%). On sections with heavy vegetation, the model found 4 of 7 recorded defects (57%) | P10 |
| Personal information held | About 40 current and former employees' records in SYS-08 and the shared drive; no customer consumer data | P08 |
