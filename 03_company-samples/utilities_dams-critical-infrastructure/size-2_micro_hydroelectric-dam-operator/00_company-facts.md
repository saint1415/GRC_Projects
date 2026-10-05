# Scenario facts: Cris Santos Company | Dams | Micro

All 10 deliverables in this folder use the facts below. The company, the hydroelectric project, the river, and the downstream community are fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or a FERC program document, the citation is given. Regulatory text was checked against eCFR (version date 2026-09-23) for 18 CFR Part 12 and 18 CFR 388.113, the FERC *Security Program for Hydropower Projects* Revision 3A PDF on ferc.gov, and the NERC Bulk Electric System Definition Reference Document (version 3, April 30, 2026).

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held by Cris Santos) |
| Business | Owner and operator of one small run-of-river hydroelectric project with a FERC-regulated dam (NAICS 221111, Hydroelectric Power Generation) |
| The project | **Bramble Shoals Hydroelectric Project** (fictional), a FERC-licensed project on the fictional Bramble River in north Florida. Hydropower is rare in Florida; this project is invented for the sample and does not describe any real dam |
| Project works | A concrete gravity dam about 420 feet long and 26 feet high above streambed (to the top of the gates), with a 180-foot uncontrolled overflow section and 2 motor-operated vertical lift spillway gates; an intake and powerhouse at the left abutment with 2 Kaplan units of 2.2 MW each (4.4 MW total; about 2.4 MVA per unit); a headpond of about 260 acres with gross storage of about 1,700 acre-feet; a small substation stepping up to 12.47 kV. No black start capability |
| Location | Florida. One site: the powerhouse with the control room, a two-room office on high ground above the powerhouse, the gate hoist house on the dam, a maintenance shop, and the license-required public recreation facilities (a portage trail, a canoe launch below the dam, and a bank-fishing area) |
| License history (fictional) | Dam built in 1928 for a mill; redeveloped for power and first licensed in 1987; acquired by Cris Santos Company in 2012 with FERC approval of the license transfer; current license issued in 2018 |
| Hazard potential | **Significant** (18 CFR 12.3(b)(13)(ii)): failure or misoperation would probably not cause loss of life but could damage a county road bridge 1.5 miles downstream, a canoe outfitter, and several riverside properties. Recreation users near the tailrace and at the canoe launch can be exposed to sudden flow changes, so the company keeps an Emergency Action Plan (EAP) and has no exemption under 18 CFR 12.21 |
| Part 12 Subpart D | **Does not apply** (18 CFR 12.30): the dam is not more than 32.8 feet high, gross storage is not more than 2,000 acre-feet, no project work is High hazard, and the Regional Engineer has not required independent consultant inspections |
| FERC Security Group | **Security Group 3**, per FERC's January 2010 regrouping letter to the prior licensee, confirmed by the FERC engineer at the 2025-11-04 dam safety inspection. Group 3 dams have no required security documents; a Security Assessment and Security Plan are "highly recommended" (Security Program Rev. 3A, 3.3.3 and Table 3.3.8) |
| FERC Section 9 (cyber/SCADA) | **Not subject.** Only Group 3 dams interconnected to operational or critical cyber assets of Group 1 or 2 dams are subject to Section 9 (Rev. 3A, 9.1 note); this plant is not interconnected to any other dam. The company ran the Section 9 screen voluntarily on 2026-07-16 and adopts the Table 9.3a baseline measures as its benchmark (see section 7) |
| Offtaker | A local electric cooperative buys all energy under a long-term power purchase agreement. The cooperative owns the revenue meter and the recloser at the point of interconnection and reads them through its own metering system |
| Grid status | Interconnected at 12.47 kV (distribution). Not part of the Bulk Electric System under NERC Inclusion I2 (units are not over 20 MVA, the plant is not over 75 MVA, and the connection is below 100 kV) and not a blackstart resource. Not on the NERC Compliance Registry, so NERC CIP does not apply |
| Workforce | **7 employees:** Owner and General Manager, Plant Superintendent, Controls and Electrical Technician, 3 Operator-Mechanics, and an Office and Compliance Administrator |
| Operations | The plant is staffed 07:00 to 17:30 every day by a rotation of operator-mechanics, with the Plant Superintendent and the Controls and Electrical Technician on site on weekdays. Overnight the plant is unattended: the gate PLC holds the headpond level automatically, and alarms call out the on-call operator-mechanic, who can view and operate the HMI remotely. Night drive-in time is about 30 minutes |
| Revenue | About $1.1 million a year (fictional): energy sales about $1.0 million, renewable energy credits about $80,000, and about $20,000 of other income (a land lease). Under the SBA size standard of 750 employees for NAICS 221111 (13 CFR 121.201), the company is SBA-small |
| Federal contracts | None. FAR 52.204-21 and 52.204-25 do not apply |
| Sensitive data | Design drawings, EAP inundation maps, and control system details. These are critical energy infrastructure information (CEII) as defined in 18 CFR 388.113(c)(2) and are treated as CEII internally; the 388.113 designation procedures apply to information submitted to or generated by the Commission (388.113(a), (d)). Any security information supplied to FERC is marked "Privileged - Security Sensitive Material" (Rev. 3A 3.4.3.4). Dam safety instrumentation data. Employee personal information for 7 employees (Florida breach law applies). The recreation facilities are free, so the company takes no card payments. No PCII has been submitted. No BES Cyber System Information exists |
| Not in scope | NERC CIP (not BES, not registered). FERC Section 9 as an obligation (Group 3, not interconnected). Part 12 Subpart D and the ODSP external audit in 12.65 (not High hazard). HIPAA, PCI DSS, CMMC (no such data or contracts). CIRCIA reporting: the final rule is not published (proposed only), and the company is far below the SBA size standard used in the proposed scope |
| State law approach | Florida law is cited only where unavoidable (breach notice for employee personal information, Fla. Stat. 501.171). Otherwise the samples stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Owner and General Manager | Accepts Moderate, High, and Very High risks; approves policies, this deliverable set, and spending; **FERC primary security contact** (Rev. 3A 3.2); signs the Owner's Dam Safety Program (18 CFR 12.62(b)) and FERC correspondence; holds the cyber insurance policy |
| Plant Superintendent | System owner of the Hydro Plant Control and Dam Monitoring System (P02); **Chief Dam Safety Coordinator** designated in the Owner's Dam Safety Program (ODSP) (18 CFR 12.61(b), 12.62(a); a Coordinator is allowed because no project work is High hazard); EAP lead; makes 18 CFR 12.10 reports; alternate FERC security contact; incident commander for control system incidents; business owner of the AI anomaly detection trial (P10) |
| Controls and Electrical Technician | Day-to-day administrator of the control system (HMI accounts, PLC and HMI backups, control network, firewall change requests); OT technical lead in incidents; works with the controls integrator |
| Operator-Mechanics (3) | Operate gates and units; daily dam walk-down and instrument readings; rotate the on-call week |
| Office and Compliance Administrator | **Security program coordinator** (combined with license compliance, accounting, and payroll): keeps the risk register, policies, training records, incident log, and vendor folder; prepares FERC filings with the Plant Superintendent; MSP contact |
| Managed service provider (MSP) | Office IT only: productivity suite administration, 6 office endpoints, office firewall and Wi-Fi, cloud backup. No access to the control network |
| Controls integrator | Designed the 2015 controls upgrade; holds the PLC and HMI project files; remote support under a time-and-materials service agreement through an always-on cellular VPN and the remote desktop tool |
| Remote monitoring service vendor | SaaS alarm callout and trending service; offers the AI anomaly add-on (P10) |
| Consulting dam safety engineer | Licensed professional engineer under contract; supports the ODSP annual review, EAP updates, instrument trigger points, and a quarterly instrument trend review. Not a Part 12D independent consultant (Subpart D does not apply) |
| Independent assessor | OT security consultant contracted for the P07 control assessment; did not design or operate any control |

**Where roles overlap and how that is compensated.** The Plant Superintendent is system owner, dam safety coordinator, and incident commander, and the Owner is both FERC security contact and risk acceptor. The Office and Compliance Administrator keeps the security program but is not technical. Independent checks come from the outside assessor (P07), the consulting dam safety engineer (ODSP and instrument reviews), the FERC dam safety inspection, and the monitoring vendor's SOC 2 report (P09).

## 3. Systems

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | HMI workstation: 1 HMI PC in the control room running the SCADA/HMI software, plus the Controls and Electrical Technician's engineering laptop with PLC programming software | On-premises OT (control room) | **The HMI PC's operating system has been out of vendor support since October 2025.** One shared "operator" sign-in. Staff also browse weather radar websites on it. The engineering laptop moves between the office Wi-Fi and the control network |
| SYS-02 | Spillway gate control: 1 gate PLC, 2 local gate control panels in the hoist house, gate position encoders, portable standby diesel generator with a manual transfer switch | On-premises OT (hoist house) | Automatic headpond level control. Gates can be run from the HMI (local or remote) or from the local panels. Annual gate operation and standby power load tests are done (18 CFR 12.54) |
| SYS-03 | Unit control: 2 unit PLCs, 2 digital governors, 2 static exciters, generator protective relays, local unit control panels | On-premises OT (powerhouse) | Governor and exciter settings are kept by the integrator |
| SYS-04 | Dam safety instrumentation and public warning: headwater and tailwater level sensors, 4 automated uplift piezometers, 1 automated seepage weir, a data logger in the hoist house; 1 manual seepage weir and 6 survey monuments; tailrace warning horn and strobes that the PLC sounds before a gate opens or a unit starts | On-premises OT plus field devices | The data logger keeps 60 days of readings locally. Warning devices are part of the public safety measures under 18 CFR 12.52 |
| SYS-05 | Control network: unmanaged switches, an industrial firewall between the control network and the office network (integrator-managed, 2015), the integrator's cellular router, and a cellular data gateway that sends readings to SYS-07 | On-premises OT | One flat control network for the dam and powerhouse. **The firewall allows any office device to reach the HMI PC (remote desktop and file sharing); the cellular router bypasses the firewall** |
| SYS-06 | Remote access paths | Remote desktop tool (vendor cloud relay); cellular VPN | (a) A commercial remote desktop tool on the HMI PC with unattended access and **one shared password, no MFA**, used by 5 staff and 2 integrator engineers since 2021; (b) the integrator's **always-on cellular VPN** to the control network for PLC programming |
| SYS-07 | Remote monitoring and alarm service | Vendor SaaS | Receives readings one way from the SYS-05 gateway every minute; trends, alarm callouts by text and voice, mobile app. A remote setpoint-write feature exists in the product but is disabled for this site. **AI anomaly add-on in a free trial since 2026-05-04** (P10). The vendor has a SOC 2 Type 2 report (P09) |
| SYS-08 | Office IT: 3 desktops and 3 laptops, office firewall and Wi-Fi, printer | On-premises, MSP-managed | MSP patching and antivirus on the 6 office endpoints; laptops encrypted. The engineering laptop (SYS-01) is not MSP-managed |
| SYS-09 | Productivity suite (email, files, calendar) | SaaS | MFA enforced for all 7 users. Holds the EAP, ODSP, drawings, FERC filings, HR files. **CEII-type documents sit in a folder open to all staff and are shared with the integrator and consulting engineer by "anyone with the link"** |
| SYS-10 | Cloud backup of the productivity suite | Cloud workload operated by the MSP | Nightly, 30 days of versions; one restore test in 2025 (a single file). Does not cover the HMI PC, PLC logic, or HMI project |
| SYS-11 | Business SaaS: accounting, outside payroll service | Vendor SaaS | Payroll every two weeks |
| SYS-12 | Physical security: fence and locked gates at the powerhouse and substation, locked hoist house, 4 IP cameras recording to a network video recorder (NVR) in the control room, viewable through a phone app over the camera vendor's cloud relay | On-premises plus vendor relay | Cameras cover the spillway, powerhouse door, intake, and substation |
| SYS-13 | Revenue meter and recloser | Owned and read by the cooperative | Outside the company's boundary |

**SSP system (P02):** the *Hydro Plant Control and Dam Monitoring System (HPCDMS)*: SYS-01 to SYS-06, with their interfaces to SYS-07, SYS-08, and SYS-12, plus the control room, hoist house, powerhouse, and instrument locations that house them.

## 4. Current security posture: informal, with basic hygiene and big gaps

**In place today:**
- EAP filed with the Regional Engineer, posted in the control room, reviewed every year, with an annual readiness test of key staff (18 CFR 12.24(d), 12.25); last test 2026-02-17, a call-down drill with county emergency management
- ODSP filed in 2023 and reviewed every year, naming the Plant Superintendent as Chief Dam Safety Coordinator (18 CFR 12.60 to 12.64)
- Annual spillway gate operation and standby generator load test, with verified statements (18 CFR 12.54)
- Permanent project records kept in a fire-resistant cabinet in the office on high ground, with scanned copies in the productivity suite (18 CFR 12.12)
- 18 CFR 12.10 reporting used for physical conditions: a gate hoist motor failure in 2024 and a kayaker rescue below the dam in 2025
- Tailrace warning horn and strobes, warning signs, and a boat barrier above the dam (18 CFR 12.52)
- Fence and locked gates at the powerhouse and substation; locked hoist house; 4 cameras; law enforcement and county emergency management numbers posted; sheriff's deputies patrol the recreation area
- MSP patching and antivirus on office endpoints; MFA on the productivity suite; nightly cloud backup of the suite
- An industrial firewall between the office and control networks (with weak rules)
- A cyber insurance policy since 2025-06-01 with a 24x7 breach hotline

**Missing or weak, found in the 2026 assessments:**
1. No Security Assessment, Security Plan, or cyber security plan. For Group 3 these are highly recommended, not required (Rev. 3A 3.3.3). The only document is a 2011 one-page physical security checklist from the prior owner. At the 2025-11-04 inspection the FERC engineer recommended a cyber security plan that covers the remote control capability.
2. The remote desktop tool on the HMI PC allows unattended access with one shared password and no MFA, used by 7 people including 2 integrator engineers. The password was last changed in February 2023. A former operator-mechanic who left on 2024-11-15 knew it.
3. The integrator's cellular router gives an always-on VPN into the control network that bypasses the firewall. The company cannot see or log its use.
4. The firewall lets any office device reach the HMI PC; the engineering laptop moves between office Wi-Fi and the control network; the HMI PC is used to browse websites.
5. The HMI PC operating system has been out of vendor support since October 2025; there is no OT patching process; antivirus signatures on the HMI PC were last updated in 2024.
6. The company holds no copies of PLC logic, the HMI project, or governor and exciter settings. The integrator's copies date from May 2023 and have never been restore-tested. There is no OT recovery procedure.
7. No OT asset inventory; only the integrator's 2015 network drawing.
8. No incident response plan. The EAP and ODSP do not mention cyber events, and staff do not know that "security incidents (physical and/or cyber)" are conditions reportable under 18 CFR 12.10 (12.3(b)(4)(xi)).
9. No security training except one MSP phishing email campaign for office staff in 2025 (Rev. 3A 3.2 calls for annual training on security, physical and cyber).
10. No account management: no termination checklist. The former operator-mechanic's suite account was disabled, but the shared OT passwords were not changed.
11. CEII-type documents (drawings, inundation maps, the control network drawing) are in a suite folder open to all staff and shared by "anyone with the link".
12. No security terms in the integrator, monitoring service, or MSP contracts; the monitoring vendor's SOC 2 report had never been reviewed.
13. The AI anomaly add-on was switched on as a free trial on 2026-05-04 without review; the vendor's standard terms allow use of customer data to improve its models.
14. No logging or review of HMI, firewall, or remote access activity. The remote desktop tool keeps a 30-day connection log at the vendor that nobody reviews.
15. Manufacturer default passwords on the camera NVR administrator account and the cellular data gateway web page (found in P07 testing, 2026-08-11).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | FERC Security Program for Hydropower Projects, Revision 3A (March 30, 2016), as applied to a **Security Group 3** dam: the general licensee duties apply; the Group 1 and 2 documents do not; Section 9 is used as a voluntary benchmark. Secondary and binding: 18 CFR Part 12 (12.10 reporting, EAP, gate testing, records, warning devices, ODSP). NERC CIP recorded as not applicable |
| P08 incident | Unauthorized access to spillway and turbine control systems through the shared remote desktop password or the integrator's always-on cellular VPN. Kept from the registry default because it is the most likely serious incident at this plant |
| P09 SOC 2 | The company is not a service organization. Part A is a Security plus Availability self-assessment used to answer the cooperative's generator security questionnaire (due 2026-09-30) and the cyber insurance renewal application (due 2026-11-01). Part B reviews the remote monitoring vendor's SOC 2 Type 2 report |
| P10 AI | AI-001: dam-safety sensor anomaly detection, the remote monitoring vendor's AI add-on (trial). Kept from the registry default; at this size it is a vendor add-on, not a separate platform. AI-002: staff use of public generative AI chatbots |
| Primary system | Kept from the registry default (*Hydro Plant Control and Dam Monitoring System*); at this size it is one HMI PC, three PLCs, and a data logger, supported by an outside integrator |
| Cloud | SaaS (productivity suite, monitoring service, accounting, payroll) plus one cloud workload, the MSP-operated cloud backup. Vendor-agnostic |

## 6. Assessment calendar (fictional unless a regulation is cited)

| Date | Event |
|---|---|
| 2012 | Cris Santos Company acquires the project (FERC approves the license transfer) |
| 2015 | Controls upgrade by the integrator: PLCs, HMI, industrial firewall |
| 2021-03 | Remote desktop tool installed for integrator support and on-call operation |
| 2023 | ODSP filed with the Regional Engineer |
| 2024-03-12 | Gate hoist motor failure reported under 18 CFR 12.10 |
| 2024-11-15 | An operator-mechanic leaves the company |
| 2025-06-01 | Cyber insurance policy starts |
| 2025-11-04 | FERC dam safety inspection; security discussed; the FERC engineer recommends a cyber security plan covering remote control |
| 2026-02-17 | Annual EAP readiness test (call-down drill with county emergency management) |
| 2026-05-04 | AI anomaly add-on trial switched on |
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork, including the voluntary Section 9 screen on 2026-07-16 |
| 2026-08-10 to 2026-08-12 | Control assessment by the independent assessor (on site 2026-08-11) |
| 2026-08-31 | Deliverables approved by the Owner and General Manager |
| 2026-09-30 | Response due on the cooperative's generator security questionnaire |
| 2026-11-01 | Cyber insurance renewal application due |
| 2027 (autumn) | Next FERC dam safety inspection (date set by the Regional Office) |

## 7. Facts added while completing the deliverables (fictional)

| Fact | Used in |
|---|---|
| About $3,000 of revenue per day ($1.1 million over 365 days); generation about $2,750 per day at average output; a cash reserve covers about 45 days of expenses | P05, P01 |
| Voluntary Section 9 screen on 2026-07-16: Form 3 Q1 to Q3 Yes, Q4 No. Table 9.1c values at or below every threshold (population at risk within 3 miles about 40 on a peak summer weekend; within 60 miles and in total about 150; damages far below $300 million; no municipal-wide disruption); generation under 100 MW is Non-critical (Table 9.1c note 3). Had Section 9 applied, the plant would sit at the baseline level (9.1.1.2) | P02, P03 |
| The only other water control structure on the river is a county-owned low-head weir 6 miles downstream; no contact procedure exists | P03, P08 |
| Sheriff's office orientation visit to the project on 2025-03-20 | P03 |
| Instrument trigger points set by the consulting engineer in the 2023 ODSP instrumentation plan | P03, P10 |
| Remote desktop tool connection log (2026-07-12 to 2026-08-10): 64 sessions; 61 matched to the on-call rota or integrator work orders; 3 could not be matched until the integrator confirmed on 2026-08-13 that they came from an engineer's home computer during an unlogged support call | P07, P01 |
| Interim controls: shared remote desktop password changed on 2026-08-12 and given only to the 5 staff; from 2026-09-15 the integrator's cellular router stays powered off except during sessions a staff member starts and watches | P01, P02, P07, P08 |
| The integrator's newest PLC and HMI copies are dated 2023-05-18; governor and exciter settings were never copied | P05, P07 |
| The old HMI PC replaced in 2019 is in the shop storeroom, not wiped | P03 |
| Remediation budget: about $21,000 one-time and about $3,100 a year, approved by the Owner on 2026-08-31 | P01, P07 |
| Monitoring vendor SOC 2 Type 2: 12 months ending 2026-03-31, Security and Availability, unqualified, 1 exception; RTO 12 hours, RPO 15 minutes; the AI add-on is outside the system description | P09, P10 |
| AI-001 trial results: vendor back-test on 9 documented events (2019-2026) found 7; 57 alerts from 2026-05-04 to 2026-08-15, 3 confirmed as real conditions (none past a trigger point); about 0.4 alerts a day in May and 0.6 a day from June to mid-August | P10 |
| The cooperative's questionnaire asks about remote access to generator controls, MFA, and incident notice | P09 |
