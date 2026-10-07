# Scenario facts: Cris Santos Company | Water and Wastewater Systems | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held community water system) |
| Business | Community water system (NAICS 221310): groundwater supply, treatment, storage, and distribution of drinking water for a rural residential community. No wastewater service (homes use septic systems; the few commercial customers on sewer are served by the county) |
| Location | Florida. One service area with one **plant site**: Wells 1 and 2, a tray aerator, the chlorine feed room, a 300,000-gallon ground storage tank, 3 high-service pumps, a standby generator, and a small building with the office and the plant control room. **Well 3** is about 2 miles away. A 150,000-gallon **elevated tank** is about 1.5 miles away |
| Source and treatment | 3 groundwater wells. Aeration (hydrogen sulfide removal) and disinfection with sodium hypochlorite. Design capacity 0.65 million gallons per day (MGD); average day demand 0.23 MGD; maximum day 0.42 MGD. About 38 miles of mains |
| Customers | **Population served: 2,850 persons** (1,190 connections: 1,140 residential and 50 commercial, including one elementary school). This is the population the company reports to the state drinking water primacy agency |
| Workforce | 7 employees: Owner and General Manager, Office Manager, Chief Operator, 2 Operators, Utility Field Technician, Customer Service and Billing Clerk |
| Plant staffing | Staffed 7:00 to 15:30 on weekdays, with weekend and holiday rounds. Nights and weekends are covered by an on-call licensed operator (rotation of the Chief Operator and the 2 Operators) |
| Revenue | About $1.1 million a year (fictional): water rates, service fees, and connection charges. Under the SBA standard of $41.0 million for NAICS 221310 (13 CFR 121.201), so SBA-small |
| Rate regulation | Rates are set by the state or county utility regulator. Rate filings are outside the scope of these deliverables |
| SDWA section 1433 status | **Not covered.** The company is a community water system (40 CFR 141.2: at least 15 service connections used by year-round residents), but it serves 2,850 persons, which is not "greater than 3,300 persons" (42 U.S.C. 300i-2(a)(1)). It has no federal risk and resilience assessment (RRA) or emergency response plan (ERP) certification duty. EPA must provide guidance and technical assistance to systems serving fewer than 3,300 persons (300i-2(e)) |
| Growth watch item | A 240-lot subdivision was approved in 2026 for service starting in 2027. At about 2.4 persons per home it would add roughly 580 persons, which would take the population served above 3,300 by about 2029. How and when a system that newly exceeds 3,300 must certify under section 1433 was **not verified**; the Owner will ask EPA before the subdivision connects |
| Ground Water Rule status | The company provides 4-log treatment of viruses by chlorination and does compliance monitoring under 40 CFR 141.403(b). It chose to **monitor the residual disinfectant continuously** at the entry point, the alternative open to systems serving 3,300 or fewer (141.403(b)(3)(i)(B)), so the rules for continuous monitoring in 141.403(b)(3)(i)(A) apply: record the lowest residual each day; grab samples every 4 hours if the analyzer fails; resume continuous monitoring within 14 days. The SCADA trend is therefore compliance data |
| Sanitary survey | Last state sanitary survey 2025-03-18: no significant deficiencies. One recommendation: update the emergency plan contact list. States must survey community water systems every 3 years, with exceptions in 40 CFR 142.16(o)(2)(iii); next survey expected by March 2028 |
| Not in scope | Wastewater (POTW) requirements: the company runs no wastewater system. Federal contracts: none. HIPAA: not a covered entity. Card data: customers pay by card on the payment processor's hosted page, so card numbers never touch company systems |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (customer data breach notice, Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and resilience duties |
|---|---|
| Owner and General Manager | Accepts Moderate, High, and Very High risks; approves policies, the security budget, and contracts; decides on public notices with the Chief Operator; calls the cyber insurer |
| Office Manager | Part-time **security and compliance coordinator** (designated in writing 2026-08-31); manages the MSP; requests and removes business system accounts; keeps the policies, risk register, and incident log; HR and payroll; may accept Low and Very Low risks |
| Chief Operator | Operator in responsible charge of the plant under the state operator license; **owns the SCADA system and the treatment process**; holds the HMI and PLC administrator credentials; compliance sampling and monthly operating reports; leads the Tier 1 public notice decision; business owner of the anomaly detection trial (P10) |
| Operators (2) | Plant rounds and daily checks; on-call rotation; manual operation |
| Utility Field Technician | Distribution system, meters (drive-by meter reading), flushing, line repairs, checks at Well 3 and the elevated tank |
| Customer Service and Billing Clerk | Billing system, payments, customer calls, the customer contact list for notices |
| Managed service provider (MSP), contractor | Business IT: office computers and phones, office firewall and Wi-Fi, productivity suite administration, office backup, patching, antivirus. **The MSP contract excludes "plant control systems"** (see gaps) |
| SCADA integrator, contractor | Designed and installed the SCADA system in 2018; PLC programming and HMI changes; remote support through a remote desktop tool. Time-and-materials contract with no security terms |
| Remote monitoring vendor | SaaS remote monitoring, alarm call-out, mobile app, and two-year trend history; anomaly detection feature on trial (P10) |
| Contract certified laboratory | Bacteriological and chemical compliance analyses |
| Cyber insurer | Cyber liability policy since 2025-11-01, with a 24x7 breach hotline and panel vendors (breach counsel, forensics). The policy requires prompt notice and use of panel vendors |

## 3. Systems

| ID | System | Hosting | Holds sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | SCADA HMI computer: one desktop in the plant control room running the HMI and SCADA software, a local historian, alarm handling, and the PLC programming software (it is also the engineering workstation) | On-premises, plant control room | Yes (process data, HMI project, a copy of the PLC program) | Commissioned 2018. Supported operating system, but operating system and SCADA software updates have not been applied since May 2024, on the integrator's advice |
| SYS-02 | Plant PLC and 2 RTUs: the PLC runs Wells 1 and 2, the aerator blower, hypochlorite pump pacing, ground tank level, and the high-service pumps; RTUs at Well 3 and the elevated tank | On-premises, plant and remote sites | Yes (control logic) | Hypochlorite metering pump: the PLC sets pump speed; the pump's mechanical stroke-length setting caps its maximum output. Hand-off-auto switches on wells, pumps, and the chemical feed |
| SYS-03 | Telemetry: cellular modems at Well 3 and the elevated tank (carrier's standard business data plan with public addresses) | Carrier network | No | The tank modem's web administration was reachable from the internet with the default password (found in P07) |
| SYS-04 | Remote access: a commercial remote desktop tool (vendor cloud relay) installed on SYS-01 by the integrator in 2018 in unattended-access mode | Vendor cloud relay | No | One shared access password, no MFA. Used by integrator technicians and by the 3 licensed operators from personal phones and home computers when on call. **The P08 incident path** |
| SYS-05 | Remote monitoring service: an edge gateway at the plant reads PLC values and sends them outbound to the vendor's service; alarm call-out to phones; mobile app; two-year trend history; anomaly detection feature (trial since 2026-06-15) | Vendor SaaS on a public cloud; edge gateway on-premises | Yes (process data) | 5 named users, MFA available but not turned on. The service can write setpoints back to the PLC; that feature is turned off in the account settings |
| SYS-06 | Productivity suite (email, files, chat) | SaaS, administered by the MSP | Yes (emergency plan, 2018 SCADA drawings, customer notice templates, HR files, a password spreadsheet) | MFA enforced for all 7 users since October 2025 (insurer requirement) |
| SYS-07 | Utility billing system with customer portal | Vendor SaaS | Yes (customer PII, bank draft details for 410 autopay customers, portal credentials) | 1,190 accounts. MFA enforced for the 3 staff users. Card payments on the processor's hosted page |
| SYS-08 | Accounting and payroll | Vendor SaaS | Yes (payroll, bank details) | Owner and Office Manager only; MFA on |
| SYS-09 | Office and plant network and endpoints: one small-business firewall and router, one Wi-Fi access point, 6 computers, 3 company smartphones, 1 meter-reading handheld | On-premises, MSP-managed | Yes (cached) | **Flat network:** SYS-01, the plant PLC, and the SYS-05 gateway connect to the same switch as the office computers. The Wi-Fi password is shared with visitors and contractors |
| SYS-10 | Office backup: nightly cloud backup of the productivity suite and 2 office desktops | SaaS, operated by the MSP | Yes | Never restore-tested |
| SYS-11 | Physical security: fence and locked gate at the plant; keyed doors; intrusion alarm on the plant building monitored by an alarm company; fenced and padlocked Well 3 and tank sites | On-premises | No | No cameras |
| SYS-12 | Alarm dialer: a standalone cellular autodialer at the plant, wired to the chlorine analyzer's high and low relay contacts, ground tank low level, power failure, and building intrusion; it calls the on-call phone | On-premises | No | Independent of SCADA, the office network, and the internet |

**SSP system (P02):** the *Water Treatment SCADA System (WTSS)*: SYS-01, SYS-02, SYS-03, SYS-04, and SYS-12, the plant network segment they share with the office (part of SYS-09), and the SCADA data feed and remote alarm functions provided by SYS-05.

## 4. Current security posture: informal, basic hygiene, big gaps

**In place today:**
- Licensed operators can run the wells, chemical feed, and high-service pumps by hand at the panels. They did so for 2 days during a hurricane power outage in October 2024. There is no written procedure
- The hypochlorite pump's mechanical stroke-length setting caps the dose at about 2.5 times the normal rate, and the chlorine analyzer's own high and low alarm relays call the on-call phone through the alarm dialer, independent of SCADA
- Standby generator with automatic transfer at the plant; portable generator hookup at Well 3; fuel delivery contract
- A hand-operated emergency interconnect with the adjacent county utility (about 0.15 MGD)
- A 2023 emergency plan (hurricanes and power loss) and a boil water notice template
- The MSP patches office computers, runs antivirus, and manages the office firewall
- MFA on email for all users, and on the billing and accounting systems
- Cyber insurance since 2025-11-01
- Fence, locks, and an alarmed plant building
- 2025 sanitary survey with no significant deficiencies
- Daily operator logs and monthly operating reports to the primacy agency

**Missing or weak, found in the 2026 assessments:**
1. No cybersecurity risk assessment has ever been done. The 2023 emergency plan covers hurricanes and power loss; its only cyber line is "call the SCADA integrator".
2. The remote desktop tool on the HMI computer is always on, uses one shared password with no MFA, and is used from personal phones and home computers by operators and integrator staff. Nobody reviews its connection log.
3. A former operator who left in March 2026 still knew the shared remote desktop password, which had not been changed since 2023. The Chief Operator changed it on 2026-07-22, after the risk interviews; there is still no rule for changing it when someone leaves.
4. The HMI uses one shared "operator" login. HMI administrator and PLC passwords are unchanged since 2018. The PLC has no program password, and its key switch is in the remote-program position.
5. The network is flat: the HMI computer, the plant PLC, and the office computers share one network, and the Wi-Fi password is shared with visitors and contractors.
6. There is no OT asset inventory or current network diagram. The latest drawings are the integrator's 2018 as-builts.
7. Operating system and SCADA software updates on the HMI computer have not been applied since May 2024. The MSP contract excludes plant control systems, so no one manages patching or malware protection for the HMI computer.
8. The HMI project and PLC program are not backed up by the company. The only copies are on the HMI computer and the integrator's laptop.
9. There is no incident response plan or cyber procedure, and none has been exercised. The manual-operation steps are not written down.
10. The contracts with the SCADA integrator, the remote monitoring vendor, and the MSP have no security terms (incident notice, remote access rules).
11. No one has had security awareness training or a phishing exercise.
12. The customer contact list for emergency notices exists only in the billing system. The last printed copy is from October 2024.
13. The office backup has never been restore-tested.
14. The Chief Operator turned on the anomaly detection feature of the remote monitoring service in June 2026 during a free trial, with no review. The monitoring service accounts do not use MFA.
15. The elevated tank's cellular modem had web administration reachable from the internet with the default password (found during P07 testing on 2026-08-11).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | **Applicability first.** SDWA section 1433 (C-WATER-R01) does not apply at 2,850 persons served; it is kept as a readiness reference because of the growth watch item. Binding rules analyzed: the SDWA public notification rule (40 CFR Part 141 Subpart Q, Tier 1 notice) with the related reporting and record rules (141.31, 141.33), and the Ground Water Rule duties that depend on SCADA (141.401, 141.403). Cyber benchmark: NIST CSF 2.0 with NIST SP 800-82 Rev. 3 |
| P08 incident | Remote-access compromise of the plant HMI through the shared remote desktop tool, with an attacker raising the hypochlorite pump speed and silencing the HMI high-chlorine alarm. The MSP, the integrator, and the insurer are in the notification chain |
| P09 SOC 2 | The company is not a service organization. (a) Security plus Availability readiness self-assessment, used to answer the cyber insurer's renewal questionnaire; (b) review of the remote monitoring vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| P10 AI | The anomaly detection feature of the remote monitoring service (SYS-05), on trial. The registry default "water-quality anomaly detection" is kept, adapted to this size: the company does not build or host a model; it configures a vendor feature |
| Cloud | SaaS plus one cloud workload: the remote monitoring service and its plant edge gateway. Vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |
| Registry defaults | Primary system "Water treatment SCADA" kept (as the WTSS). Incident "Remote-access compromise of treatment-plant HMI" kept. AI use case adapted as described above |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2025-03-18 | Last state sanitary survey (no significant deficiencies) |
| 2025-11-01 | Cyber insurance policy starts |
| 2026-07-13 to 2026-07-24 | BIA, risk assessment, and gap analysis (Office Manager and Chief Operator with the MSP lead technician; SCADA integrator interviewed 2026-07-21) |
| 2026-08-10 to 2026-08-12 | Control assessment by an independent OT security consultant (site visit to the plant, Well 3, and the elevated tank on 2026-08-11) |
| 2026-08-31 | Deliverables approved by the Owner and General Manager |
| 2026-10-01 | Cyber insurer's renewal questionnaire due |
| 2026-11-01 | Cyber insurance renewal |
| 2027-07 | Next annual risk review |
| By 2028-03 | Next state sanitary survey expected |

## 7. Facts added while building the deliverables
These facts were added while the deliverables were built because they needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Endpoints | SYS-09 computers: Owner laptop, Office Manager desktop, Billing Clerk desktop, Chief Operator laptop, operator desk desktop in the control room (email and lab reports), and the Utility Field Technician's laptop (meter-reading software). Company smartphones: the on-call phone, the Chief Operator's phone, and the Utility Field Technician's phone | P02, P04, P07 |
| Internet | One business broadband line at the plant site; no failover. The alarm dialer and the cellular modems do not depend on it | P01, P05 |
| Remote desktop tool | Unattended access with one shared password set in 2023; connection history kept by the tool vendor for 90 days and visible in its web console, which the Chief Operator can open but never has | P01, P07, P08 |
| Password spreadsheet | The HMI, PLC, modem, and remote desktop passwords are kept in a spreadsheet in the productivity suite's shared folder, which all 7 staff can open | P01, P03, P07 |
| Chlorine dose | Normal hypochlorite feed holds about 1.2 mg/L free chlorine leaving the plant. The state-determined minimum residual for 4-log treatment is a value set in the company's operating permit. The mechanical stroke setting caps the pump at about 2.5 times the normal rate | P01, P08 |
| Cash reserve | A cash reserve covers about 45 days of expenses; payroll runs biweekly through the payroll SaaS | P01, P05 |
| Assessor | The P07 assessor is an independent OT security consultant, not involved in the risk or gap analysis and independent of the SCADA integrator and the MSP | P07 |
| Tank modem fix | The SCADA integrator turned off web administration and changed the tank modem password on 2026-08-12, the day after the consultant reported it | P01, P07 |
| Shared password change | The Chief Operator changed the remote desktop password on 2026-07-22, the day after the risk interviews found the former operator still knew it. The tool remains password-only and always on | P01, P03, P07 |
| Remote monitoring vendor report | The vendor provided its SOC 2 Type 2 report on 2026-08-14 | P09 |
| Tank modem history | The elevated tank modem was replaced after a 2022 lightning strike and kept its default web administration password; the Well 3 modem's password had been changed at commissioning. The remote desktop password set in 2023 was 9 characters | P07 |
| Edge gateway | The remote monitoring edge gateway was installed in mid-2024, when the company subscribed to the service; the 2018 as-builts do not show it | P07 |
| P07 evidence | Evidence was requested from the MSP on 2026-08-03; the MSP technician list was not received by the end of fieldwork. The insurer's free online training portal has never been used | P07, P09 |
| Worst-case dose | With the stroke cap at about 2.5 times the normal rate, the Chief Operator estimates the worst-case plant outlet free chlorine at roughly 3 mg/L | P08 |
| Remote monitoring vendor report | SOC 2 Type 2, Security and Availability, 12 months ending 2026-03-31, unqualified, one change-approval exception; stated recovery time 8 hours and recovery point 1 hour; cloud hosting and call-out providers carved out. The anomaly detection feature launched after the report period. The subscription terms allow use of de-identified customer data to improve the vendor's analytics; customers are notified within 72 hours of a confirmed incident | P09, P10 |
| Insurer questionnaire | The renewal questionnaire asks about MFA on remote access, backups and restore tests, separation of control systems, patching, training, vendor access, and an incident response plan; the insurer accepts a self-assessment | P09 |
| Anomaly detection trial | The vendor extended the free trial to 2026-10-31. Inputs: entry point chlorine, well flows and status, hypochlorite pump speed, tank levels, high-service pump status, and pressure at the elevated tank. From 2026-06-15 to 2026-08-16 it sent 41 alerts; 4 of the 6 events in the operator logs were flagged. The elevated tank holds pressure for the far end of the system, which includes the elementary school | P10 |
| Other AI use | Office staff occasionally use public chatbots to draft customer letters; the productivity suite includes machine learning email filtering | P10 |
