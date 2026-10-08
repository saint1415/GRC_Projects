# Scenario facts: Cris Santos Company | Healthcare and Public Health | Mid-Market

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes and of the Health Care (NAICS 62) samples. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (private; private equity-backed; board with an audit committee; licensed operator of one community acute-care hospital and its off-campus outpatient center) |
| Business | **Community acute-care hospital**, NAICS 622110 General Medical and Surgical Hospitals. 112 licensed acute beds: 80 medical-surgical and telemetry, 12 intensive care, and 20 women's services (labor, delivery, recovery, postpartum), plus a newborn nursery. A 32-bed emergency department (ED), 6 operating rooms, 2 endoscopy suites, 1 cardiac catheterization lab, laboratory with a blood bank, imaging (CT, MRI, X-ray, ultrasound), pharmacy, respiratory therapy, and rehabilitation. The hospital is a primary stroke center and receives ST-elevation heart attack (STEMI) patients for the catheterization lab |
| Location | Florida only. A main campus in a suburban Central Florida county (hospital, attached medical office building, on-premises data center) and an off-campus outpatient center 9 miles away (CT, MRI, X-ray, mammography, laboratory draw station, physical therapy). Two other hospitals are within 15 miles: a 400-bed regional medical center (11 miles) and a 180-bed hospital (14 miles) |
| Workforce | 600 employees: 305 nursing (registered nurses, licensed practical nurses, nursing assistants), 115 clinical ancillary (laboratory, imaging, pharmacy, respiratory therapy, rehabilitation), 68 facilities, environmental services, food services, and biomedical engineering, 62 patient access, health information management (HIM), and revenue cycle, 20 IT and information security, and 30 leadership, administration, finance, HR, quality, and compliance |
| Contracted clinicians and other users (not employees) | Contracted groups staff the ED (24x7), hospitalist service, anesthesia, radiology (on site by day, overnight teleradiology), and pathology. About 280 independent physicians hold medical staff privileges. Travel and agency nurses fill about 25 full-time positions. About 240 users at 18 independent physician practices use the hospital's EHR through the affiliated practice program (section 5) |
| Patients | About 42,000 ED visits a year (about 115 a day), 7,800 inpatient admissions, an average daily census of 74, 950 births, 6,200 surgical and endoscopy cases, and about 150,000 outpatient encounters. The EHR holds records for about 310,000 individuals (EV-054) |
| Revenue | $100.0 million a year (fictional), about $274,000 a day (EV-053). Above the SBA standard of $47.0 million for NAICS 622110 (13 CFR 121.201), so not small |
| Payers | Medicare (about 44% of revenue), Florida Medicaid (about 18%), commercial and other plans. Medicare and Medicaid are federal financial assistance, so Section 1557 of the Affordable Care Act applies (45 CFR Part 92) |
| HIPAA status | **Covered entity**, determined in the intake obligations register (C-HPH-R01): the clearinghouse agreement covers standard electronic claims and eligibility transactions (EV-047). For the affiliated practice program, the hospital is also a **business associate** of the 18 practices (C-HPH-R01-BA; EV-041, EV-045) |
| Other federal status | Medicare-participating hospital (EV-047), so the hospital conditions of participation apply (42 CFR Part 482), including emergency preparedness (**42 CFR 482.15**) and medical record services (42 CFR 482.24); EMTALA (42 CFR 489.24); the Medicare Promoting Interoperability Program (42 CFR 495.24); and FDA medical device reporting as a device user facility (21 CFR 803.3, 803.30). Each is decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): 42 CFR Part 2 (the hospital is not a Part 2 program; HIM flags Part 2 records received from outside programs for the Privacy Officer, EV-047, EV-056), the FTC Health Breach Notification Rule, group health plan requirements (the plan is fully insured, and the hospital as plan sponsor receives only summary health and enrollment information, confirmed in P03, EV-069) and the Florida Digital Bill of Rights do not apply. **Payment cards**: patient payments use a validated point-to-point encryption service outside the clinical systems (noted, not assessed) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171; recording consent, Fla. Stat. 934.03). Seasonal residents and visitors from other states are treated generically: apply the law of each state where affected individuals reside |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Board of directors and its audit committee | Quarterly cyber risk reporting; only body that may approve a temporary exception for a Very High risk |
| Chief Executive Officer (CEO) | Accepts High risk; approves POL-01, the risk appetite, and the security budget; hospital incident commander for a hospital-wide emergency (Hospital Incident Command System) |
| Chief Operating Officer (COO) | Executive sponsor of the security program and **system owner** of the SSP system; accepts Moderate risk; chairs the cyber crisis management team |
| Chief Financial Officer (CFO) | Contracts and BAAs with the Privacy Officer; cyber insurance; revenue cycle oversight |
| Chief Nursing Officer (CNO) | Clinical downtime lead for nursing; with the ED Medical Director and the administrator on call, decides ambulance diversion |
| Chief Medical Officer (CMO) | Medical staff liaison; chairs the Clinical Decision Support Committee (clinical AI oversight, P10) |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board and audit committee reporting |
| IT Director | HIPAA **Security Officer** (45 CFR 164.308(a)(2)); leads 16 IT staff |
| Information Security Manager plus 2 security analysts (one focused on GRC) | Security operations, MSSP oversight, vulnerability management, GRC |
| Compliance and Privacy Officer | HIPAA **Privacy Officer**; **Section 1557 Coordinator** (45 CFR 92.7); breach determinations |
| Director of Emergency Management | **Emergency preparedness coordinator** for the 42 CFR 482.15 program; Hospital Incident Command System planning |
| Director of Biomedical Engineering | Medical device inventory, maintenance, and device security with IT |
| Director of Facilities | Building and clinical operational technology (OT) |
| Business and clinical leaders | ED Director; Director of Surgical Services; Director of Women's Services; Pharmacy Director; Laboratory Director; Imaging Director; HIM Director; Director of Revenue Cycle; Director of Physician Services; Outpatient Center Manager; HR Director; Director of Marketing and Communications; Quality Director |
| Internal audit (co-sourced firm) | Annual IT audit; performs the P07 assessment |
| Managed security service provider (MSSP) | 24x7 monitoring of EDR and the SIEM. A business associate |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in [`step-00_P00_intake/vendor-register.csv`](step-00_P00_intake/vendor-register.csv).

| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Hospital EHR: ED, inpatient and nursing documentation, computerized order entry, eMAR with barcode medication administration, pharmacy, surgery and anesthesia, labor and delivery, patient accounting, HIM, patient portal, and an ambulatory module used by the affiliated practices | EHR vendor-hosted (SaaS) | Yes | System of record; certified health IT. The vendor is a business associate with a SOC 2 Type 2 report. Includes the vendor's sepsis prediction model (AI-001) |
| SYS-02 | Identity provider (single sign-on, MFA, conditional access) synchronized with the on-premises directory | SaaS | No (identities only) | Clinical workstations use badge-tap single sign-on with a password |
| SYS-03 | Imaging archive (PACS) and radiology information system (RIS) | Vendor-managed software in the hospital's cloud workloads account | Yes | Includes the FDA-cleared stroke and hemorrhage triage software (AI-002) |
| SYS-04 | Cloud landing zone: 5 accounts (management, security and log archive, shared services, workloads, backup) | Public cloud provider (vendor-agnostic) | Yes | Interface engine, PACS and RIS, data warehouse, file services, and the backup vault |
| SYS-05 | On-premises data center (main campus) | On-premises | Yes | 3-host virtualization cluster: directory, file and print, laboratory information system with blood bank module (LIS), automated dispensing cabinet server, infusion pump server, physiologic monitoring gateway, fetal monitoring surveillance server, cardiology information system (ECG and catheterization lab hemodynamics), nurse call server, and the downtime extract server. A backup appliance replicates to the cloud backup account (EV-012, EV-021) |
| SYS-06 | Networks | On-premises | Yes (in transit) | Campus core and Wi-Fi; the outpatient center connects over SD-WAN with two carriers; two internet carriers at the main campus; site-to-cloud VPN. Infusion pumps and imaging modalities are on their own VLANs; other devices share the clinical workstation VLAN (EV-014) |
| SYS-07 | Endpoints | On-premises | Yes (cached) | 960 workstations and laptops (including 260 workstations on wheels and 12 downtime workstations), 380 clinical smartphones, 120 handheld barcode scanners (EV-010) |
| SYS-08 | Medical devices: about 1,650 networked | On-premises | Yes | 290 wireless infusion pumps, about 176 patient monitors and central stations, 22 fetal monitors, 24 networked ventilators, 8 anesthesia machines, 2 CT, 2 MRI, X-ray and ultrasound, 1 catheterization lab system, 42 laboratory analyzers, 36 automated dispensing cabinets, and other devices (EV-013) |
| SYS-09 | Building and clinical OT | On-premises | Limited (nurse call and infant protection show names and rooms) | Building automation (HVAC, isolation rooms, pharmacy and blood bank temperatures), nurse call, infant protection, medical gas alarms, pneumatic tube, generator and transfer switch monitoring, badge access, video. Owned by the Director of Facilities (EV-016) |
| SYS-10 | Security operations | SaaS and MSSP | Yes (log fragments) | SIEM operated by the MSSP; EDR on servers and workstations; email security gateway |
| SYS-11 | Clinical communications | On-premises and SaaS | Yes (secure messages) | VoIP phones, clinical smartphones with secure messaging, overhead paging, mass notification, analog lines in the ED and house supervisor office, and the county EMS radio in the ED |
| SYS-12 | External connections and vendors | Vendors | Yes | Clearinghouse, health information exchange (HIE), reference laboratory, overnight teleradiology group, telestroke neurology service, public health feeds (electronic laboratory reporting, syndromic surveillance, immunization). About 210 vendors have PHI access (EV-041) |
| SYS-13 | AI tools | Vendors | Yes | Sepsis prediction model (AI-001), imaging triage (AI-002), ED ambient AI scribe pilot (AI-003), rule-based decision support (AI-004), coding assistance (AI-005); staff use of public generative AI sites (AI-006) found at intake (EV-055) |

**SSP system (P02):** the *Hospital EHR and Clinical Systems (HECS)*: the hospital's configuration and use of SYS-01 (including AI-001), SYS-02, SYS-03 (including AI-002), SYS-04, SYS-05, SYS-06, SYS-07, SYS-08, and SYS-10, with their interfaces to SYS-12. SYS-09 building OT and SYS-11 communications share the campus network and are covered in P01, P04, P05, and P08, but they are separate systems owned by the Director of Facilities and the IT Director.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the HIPAA Security Rule, the Breach Notification Rule, 42 CFR 482.15 and the other rules analyzed** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulations | All applicable regulations for the primary business line: HIPAA Security Rule (primary), HIPAA Breach Notification Rule, the hospital emergency preparedness condition of participation (42 CFR 482.15, cyber-relevant parts), Section 1557 decision support duties (45 CFR 92.210), medical record confidentiality (42 CFR 482.24(b)), EMTALA diversion (42 CFR 489.24(b)), the Promoting Interoperability security risk analysis measure (42 CFR 495.24), and device user facility reporting (21 CFR 803.30). The voluntary HHS HPH Cybersecurity Performance Goals are used as a self-benchmark (`cpg-benchmark.csv`) |
| P08 incidents | **Two incident types.** (1) Ransomware forcing EHR downtime and ambulance diversion (`ir-runbook.md`). (2) Insider unauthorized access to a high-profile patient's record (`ir-runbook-insider-access.md`). Both are integrated with the Hospital Incident Command System, the crisis management team, and outside counsel |
| P09 SOC 2 | The **affiliated practice program** makes the hospital a service organization: it provides EHR access, user administration, help desk, and interfaces to 18 independent practices. The two largest practices and the regional accountable care organization they belong to asked for a SOC 2 Type 2 report (Security, Availability, Confidentiality). Plus a vendor SOC 2 review program |
| P10 AI | AI use-case portfolio of 6 use cases, led by the registry default: the EHR vendor's **sepsis prediction model** (AI-001) |
| Cloud | Vendor-agnostic 5-account landing zone. AWS, Azure, and Google Cloud names appear only in an equivalents table |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-01 to 2026-06-19 | Intake: evidence requests, exports, inventories, obligations register |
| 2026-06-22 to 2026-07-17 | Security risk analysis, BIA interviews, and gap analysis fieldwork (walk-throughs 2026-07-07 to 2026-07-09) |
| 2026-07-20 to 2026-07-24 | 2026 policy revisions (POL-01 to POL-05), new standards, and the P08 runbooks drafted from the gaps |
| 2026-07-27 to 2026-08-14 | Control assessment by the co-sourced internal audit firm: operating tests of controls already in place; design review of the draft policies and runbooks (after-hours device testing 2026-08-05) |
| 2026-08-17 to 2026-08-28 | AI portfolio review (P10) and vendor SOC 2 report reviews (P09) |
| 2026-09-17 | Results to the audit committee; deliverables, policies, and runbooks approved by the COO and the CEO |
| 2026-10-01 | 2026 policies take effect |
| 2027-03 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies and standards introduced, after at least one quarter of operation |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Registry defaults | The registry defaults fit this business and were kept: the primary system is the hospital EHR and clinical systems (named HECS in P02), the P08 incident is ransomware forcing EHR downtime and ambulance diversion, and the P10 lead use case is the sepsis prediction model. A second incident type (insider access) and five more AI use cases were added because the Mid-Market tier calls for two incident types and a use-case portfolio |
| Revenue split | Inpatient care about $52 million, emergency care about $14 million, outpatient surgery and endoscopy about $12 million, outpatient imaging and laboratory about $14 million (of which the outpatient center about $9 million), other about $8 million. Per calendar day: inpatient about $142,000, ED about $38,000, imaging and laboratory about $38,000; outpatient surgery about $48,000 per operating day (250 operating days) (EV-053) |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics. The policy requires a call to the carrier hotline before incident vendors are engaged (EV-046) |
| EHR vendor recovery commitments | The EHR vendor's SOC 2 system description states RTO 12 hours and RPO 15 minutes. The 12 downtime workstations (ED 3, each nursing unit 1, ICU 1, women's services 1, pharmacy 1, laboratory 1, house supervisor 1, surgery 1) receive an hourly read-only extract (EV-043; EV-029) |
| Workforce activity | Employee terminations and transfers, non-employee departures, the last access review and phishing results are recorded from the systems of record in the evidence register (EV-006, EV-038, EV-060), not stated here |
| Backups | The backup design is recorded from the backup service and appliance (EV-021) and the P03 fieldwork review (EV-064), not stated here |
| MSSP | The MSSP's contract terms and the SIEM's log sources are recorded in EV-022, not stated here |
| Diversion | The county EMS communications center receives diversion status from hospitals under the county EMS protocol (fictional). Stroke and STEMI patients diverted from this hospital go to the regional medical center 11 miles away. The CNO, the ED Medical Director, and the administrator on call decide diversion together (EV-030; EV-057) |
| Affiliated practice program | 18 independent physician practices (about 240 users) use the EHR's ambulatory module under the hospital's license. The hospital provides accounts, role assignment, help desk, training, and the lab and imaging interfaces under a services agreement and a BAA with each practice. Service fees are about $1.1 million a year (EV-005; EV-041; EV-045) |
| AI tools | AI-001 sepsis prediction model live since 2025-11-03 for adult ED and inpatient encounters. AI-002 FDA-cleared triage flags suspected large vessel occlusion and intracranial hemorrhage on head CT. AI-003 ambient scribe pilot with 12 ED physicians since 2026-05. AI-004 is the EHR's rule-based library (186 active rules, including a nursing early warning score). AI-005 coding assistance suggests codes for ED and outpatient encounters since 2026-01. AI-006: web proxy logs showed 214 staff using public generative AI sites in July 2026 (EV-055; EV-070) |
| Terminology | "Hospital EHR and Clinical Systems (HECS)" is the SSP system in P02, identifier CSC-HECS-01 |
| Additional role titles | Administrator on call (rotating senior leaders); House Supervisor; ED Medical Director (contracted group); Director of Materials Management; Medical Staff Office Manager; Infection Prevention Manager; Director of Security (hospital security officers); patient experience manager |
| Other operating details | The EHR role catalog has 64 roles (EV-008). 15 of the 210 PHI vendors are Tier 1 and about 80 are Tier 2 under the P09 tiering approach. The employee health plan's broker confirmed on 2026-07-08 that the hospital receives only summary health and enrollment information (EV-069). About 40 of the 115 daily ED visits arrive by ambulance. The hospital has 18 airborne infection isolation rooms and about 14 pharmacists (EV-054). Patient access keeps a pre-assigned block of 500 downtime registration numbers (EV-029). IT keeps 20 pre-imaged spare laptops (EV-010) |
| BIA recovery assumptions | About 40% of diverted ambulance patients would have been admitted and do not return; about 50% of cancelled elective cases are rescheduled; about 60% of deferred outpatient studies are rebooked (EV-057) |
| Emergency preparedness program | Hazard vulnerability analysis and plan last reviewed in 2025. Annual county full-scale exercise (hurricane, 2026-05) and an annual mass-casualty tabletop. The ransomware and 72-hour EHR downtime tabletop on 2026-11-10 is the next additional exercise; the IT outage annex is due 2026-12-15. The hospital command center is main campus conference room 2. Transfer agreements exist with the regional medical center and the 180-bed hospital (EV-030; EV-031) |
| Affiliated practice agreement terms | The services agreement commits to restoring practice access within 8 hours of EHR availability and to initial notice within 5 business days of confirming a security incident affecting practice data. The two largest practices and their regional accountable care organization asked for the SOC 2 Type 2 report (EV-045; EV-049) |
| Infrastructure details found in fieldwork | Recorded as P03 fieldwork evidence, not stated here: the facility walk-throughs (EV-063), the backup, server and network connection review (EV-064), and the access rights review of the interface test environment, the data warehouse, and secure messaging (EV-065) |
| Security operations metrics | Recorded from the systems of record, not stated here: incidents (EV-036), privacy incident files and breaches (EV-037), sanctions (EV-039), training, acknowledgments and phishing (EV-038), Critical vulnerability findings (EV-018), reference laboratory patient-matching errors (EV-025), device returns (EV-051), and the 2025 risk analysis actions (EV-032) |
| Assessment populations | Taken from intake exports: privileged accounts (EV-007), servers (EV-012), accounts payable vendors (EV-040), and the workforce population refreshed to 2026-06-30 (EV-060) |
| P07 new finding | On 2026-08-05 testers found that the infusion pump server and the dispensing cabinet server shared one vendor default local administrator password, and that 4 of 20 sampled device classes accepted default credentials (EV-IA-5). Logged as P01 R-054 on 2026-08-07; the server password was changed with the manufacturers on 2026-09-30 |
| Budget | FY2027 security plan approved 2026-09-17: $1.45 million one-time and $620,000 a year. Unsupported device replacement is in the 2027-2029 capital plan (about $1.2 million) |
| AI portfolio details | AI-002 has been in production since 2025-03 and reads about 38 head CTs a day. 14 coders use AI-005 (EV-055). AI-001 validation for 2025-11-03 to 2026-07-31: about 29,000 scored encounters, 410 confirmed sepsis cases, 2,900 alerted encounters. The Clinical Decision Support Committee's charter was extended to all AI tools on 2026-09-17; its first AI review meeting is 2026-10-08. A sample of 25 public AI sessions found 3 pastes of patient details (EV-070) |
