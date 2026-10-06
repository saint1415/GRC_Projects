# Scenario facts: Cris Santos Company | Healthcare and Public Health | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes and of the Health Care (NAICS 62) samples. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (private; private equity-backed; board with an audit committee; licensed operator of one community acute-care hospital and its off-campus outpatient center) |
| Business | **Community acute-care hospital**, NAICS 622110 General Medical and Surgical Hospitals. 112 licensed acute beds: 80 medical-surgical and telemetry, 12 intensive care, and 20 women's services (labor, delivery, recovery, postpartum), plus a newborn nursery. A 32-bed emergency department (ED), 6 operating rooms, 2 endoscopy suites, 1 cardiac catheterization lab, laboratory with a blood bank, imaging (CT, MRI, X-ray, ultrasound), pharmacy, respiratory therapy, and rehabilitation. The hospital is a primary stroke center and receives ST-elevation heart attack (STEMI) patients for the catheterization lab |
| Location | Florida only. A main campus in a suburban Central Florida county (hospital, attached medical office building, on-premises data center) and an off-campus outpatient center 9 miles away (CT, MRI, X-ray, mammography, laboratory draw station, physical therapy). Two other hospitals are within 15 miles: a 400-bed regional medical center (11 miles) and a 180-bed hospital (14 miles) |
| Workforce | 600 employees: 305 nursing (registered nurses, licensed practical nurses, nursing assistants), 115 clinical ancillary (laboratory, imaging, pharmacy, respiratory therapy, rehabilitation), 68 facilities, environmental services, food services, and biomedical engineering, 62 patient access, health information management (HIM), and revenue cycle, 20 IT and information security, and 30 leadership, administration, finance, HR, quality, and compliance |
| Contracted clinicians and other users (not employees) | Contracted groups staff the ED (24x7), hospitalist service, anesthesia, radiology (on site by day, overnight teleradiology), and pathology. About 280 independent physicians hold medical staff privileges. Travel and agency nurses fill about 25 full-time positions. About 240 users at 18 independent physician practices use the hospital's EHR through the affiliated practice program (section 5) |
| Patients | About 42,000 ED visits a year (about 115 a day), 7,800 inpatient admissions, an average daily census of 74, 950 births, 6,200 surgical and endoscopy cases, and about 150,000 outpatient encounters. The EHR holds records for about 310,000 individuals |
| Revenue | $100.0 million a year (fictional), about $274,000 a day. Above the SBA standard of $47.0 million for NAICS 622110 (13 CFR 121.201), so not small |
| Payers | Medicare (about 44% of revenue), Florida Medicaid (about 18%), commercial and other plans. Medicare and Medicaid are federal financial assistance, so Section 1557 of the Affordable Care Act applies (45 CFR Part 92) |
| HIPAA status | **Covered entity.** A health care provider that transmits claims and eligibility transactions electronically through a clearinghouse (45 CFR 160.103). For the affiliated practice program, the hospital is also a **business associate** of the 18 practices |
| Other federal status | Medicare-participating hospital: the hospital conditions of participation apply (42 CFR Part 482), including emergency preparedness (**42 CFR 482.15**) and medical record services (42 CFR 482.24). EMTALA applies (42 CFR 489.24). The hospital uses certified EHR technology in the Medicare Promoting Interoperability Program (42 CFR 495.24). As a hospital it is a device user facility for FDA medical device reporting (21 CFR 803.3, 803.30) |
| Not in scope | **42 CFR Part 2** (screened as not applicable): the hospital has no unit or staff that holds itself out as providing substance use disorder diagnosis, treatment, or referral, so it is not a Part 2 program; ED and inpatient withdrawal management are general medical care. Part 2 records received from outside programs are flagged by HIM and handled case by case by the Privacy Officer. **FTC Health Breach Notification Rule**: does not apply to HIPAA covered entities or business associates acting as such (16 CFR 318.1). **Group health plan** requirements (164.314(b)): the employee health plan is fully insured, and the hospital as plan sponsor receives only summary health information and enrollment information. **Payment cards**: patient payments use a validated point-to-point encryption service outside the clinical systems (noted, not assessed) |
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

| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Hospital EHR: ED, inpatient and nursing documentation, computerized order entry, eMAR with barcode medication administration, pharmacy, surgery and anesthesia, labor and delivery, patient accounting, HIM, patient portal, and an ambulatory module used by the affiliated practices | EHR vendor-hosted (SaaS) | Yes | System of record; certified health IT. The vendor is a business associate with a SOC 2 Type 2 report. Includes the vendor's sepsis prediction model (AI-001) |
| SYS-02 | Identity provider (single sign-on, MFA, conditional access) synchronized with the on-premises directory | SaaS | No (identities only) | Clinical workstations use badge-tap single sign-on with a password |
| SYS-03 | Imaging archive (PACS) and radiology information system (RIS) | Vendor-managed software in the hospital's cloud workloads account | Yes | Includes the FDA-cleared stroke and hemorrhage triage software (AI-002) |
| SYS-04 | Cloud landing zone: 5 accounts (management, security and log archive, shared services, workloads, backup) | Public cloud provider (vendor-agnostic) | Yes | Interface engine, PACS and RIS, data warehouse, file services, and the backup vault |
| SYS-05 | On-premises data center (main campus) | On-premises | Yes | 3-host virtualization cluster: directory, file and print, laboratory information system with blood bank module (LIS), automated dispensing cabinet server, infusion pump server, physiologic monitoring gateway, fetal monitoring surveillance server, cardiology information system (ECG and catheterization lab hemodynamics), nurse call server, and the downtime extract server. A backup appliance replicates to the cloud backup account |
| SYS-06 | Networks | On-premises | Yes (in transit) | Campus core and Wi-Fi; the outpatient center connects over SD-WAN with two carriers; two internet carriers at the main campus; site-to-cloud VPN. Infusion pumps and imaging modalities are on their own VLANs; other devices are not (gap 1) |
| SYS-07 | Endpoints | On-premises | Yes (cached) | 960 workstations and laptops (including 260 workstations on wheels and 12 downtime workstations), 380 clinical smartphones, 120 handheld barcode scanners |
| SYS-08 | Medical devices: about 1,650 networked | On-premises | Yes | 290 wireless infusion pumps, about 176 patient monitors and central stations, 22 fetal monitors, 24 networked ventilators, 8 anesthesia machines, 2 CT, 2 MRI, X-ray and ultrasound, 1 catheterization lab system, 42 laboratory analyzers, 36 automated dispensing cabinets, and other devices |
| SYS-09 | Building and clinical OT | On-premises | Limited (nurse call and infant protection show names and rooms) | Building automation (HVAC, isolation rooms, pharmacy and blood bank temperatures), nurse call, infant protection, medical gas alarms, pneumatic tube, generator and transfer switch monitoring, badge access, video. Owned by the Director of Facilities |
| SYS-10 | Security operations | SaaS and MSSP | Yes (log fragments) | SIEM operated by the MSSP; EDR on servers and workstations; email security gateway |
| SYS-11 | Clinical communications | On-premises and SaaS | Yes (secure messages) | VoIP phones, clinical smartphones with secure messaging, overhead paging, mass notification, analog lines in the ED and house supervisor office, and the county EMS radio in the ED |
| SYS-12 | External connections and vendors | Vendors | Yes | Clearinghouse, health information exchange (HIE), reference laboratory, overnight teleradiology group, telestroke neurology service, public health feeds (electronic laboratory reporting, syndromic surveillance, immunization). About 210 vendors have PHI access |
| SYS-13 | AI tools | Vendors | Yes | Sepsis prediction model (AI-001), imaging triage (AI-002), ED ambient AI scribe pilot (AI-003), rule-based decision support (AI-004), coding assistance (AI-005); unapproved public generative AI use found (AI-006) |

**SSP system (P02):** the *Hospital EHR and Clinical Systems (HECS)*: the hospital's configuration and use of SYS-01 (including AI-001), SYS-02, SYS-03 (including AI-002), SYS-04, SYS-05, SYS-06, SYS-07, SYS-08, and SYS-10, with their interfaces to SYS-12. SYS-09 building OT and SYS-11 communications share the campus network and are covered in P01, P04, P05, and P08, but they are separate systems owned by the Director of Facilities and the IT Director.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- MFA for email, remote access, VPN, the cloud console, and any EHR access from outside the hospital network; badge-tap single sign-on with a password on clinical workstations
- EDR on servers and workstations, monitored 24x7 by the MSSP
- SIEM receiving EHR audit, identity provider, firewall, EDR, and cloud logs
- Annual security risk analysis (last done June 2025 by a consultant), used for the Promoting Interoperability attestation
- Security policies adopted in 2023
- Quarterly vulnerability scanning of IT assets
- Write-once backups in a separate cloud backup account (35-day retention) for cloud workloads, and for on-premises servers through the backup appliance
- EHR disaster recovery tested by the vendor each year
- An emergency preparedness program under 42 CFR 482.15, built for hurricanes and mass casualties, with the Hospital Incident Command System, an annual community full-scale exercise with the county, and a second annual exercise
- Annual training and quarterly phishing simulations
- Annual internal IT audit by a co-sourced firm
- Infusion pumps and imaging modalities on their own network segments
- 12 downtime workstations that print census, medication administration records, allergies, and active orders from an hourly extract

**Gaps (numbered; every deliverable cites these):**
1. **Medical device security.** The security inventory covers about 1,150 of 1,650 networked devices (70%). 210 devices run unsupported operating systems. Patient monitors, fetal monitoring, the catheterization lab system, laboratory analyzers, and dispensing cabinets share the clinical workstation VLAN. Manufacturer disclosure statements (MDS2) are on file for 35% of models.
2. **Emergency plan silent on cyber.** The 482.15 hazard vulnerability analysis lists "IT outage" as a short, low-ranked event. There are no criteria for diversion caused by an IT outage, downtime procedures have never been exercised beyond 4 hours, and no exercise has simulated a multi-day EHR loss.
3. **On-premises recovery unproven.** There is no IT disaster recovery plan. The LIS, dispensing cabinet server, pump server, monitoring gateway, fetal surveillance server, and cardiology system have never been restore-tested. The EHR vendor's recovery time (12 hours) exceeds the ED's need.
4. **Privileged access.** Privileged access management covers only the cloud. There are 31 domain administrator accounts, including 12 vendor service accounts. Access reviews are annual, not quarterly.
5. **Vendor remote access.** 46 device and application vendors have remote access. 32 use the vendor access platform; 14 use persistent VPN accounts without MFA.
6. **Third-party risk.** About 210 vendors have PHI access, with 168 BAAs on file (42 missing). Vendors are reviewed only at onboarding.
7. **Monitoring gaps.** Medical devices, OT, the LIS, and the other on-premises clinical servers do not send logs to the SIEM. EHR access monitoring covers only VIP records and employees' own records.
8. **Non-employee accounts.** Contracted clinicians, agency nurses, and affiliated practice users are not removed on time. 19 active accounts belonged to people who had left (July 2026).
9. **No AI governance.** No AI inventory or review process. The sepsis prediction model went live in November 2025 without local validation or a Section 1557 review (45 CFR 92.210); ED physicians are piloting an AI scribe; staff use public generative AI tools.
10. **Thin standards.** Policies exist, but supporting standards (configuration, logging, vendor, medical device, AI) are missing or thin.
11. **PHI in test.** The interface engine test environment uses copies of production PHI.
12. **Email impersonation.** DMARC is in monitoring mode only (p=none), and external sender tagging is off.
13. **Building OT.** At the main campus, building OT shares the IT network. The building automation vendor reaches it through a cloud portal with shared credentials.

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
| 2026-06-22 to 2026-07-17 | Security risk analysis, BIA interviews, and gap analysis fieldwork |
| 2026-07-27 to 2026-08-14 | Control assessment by the co-sourced internal audit firm (after-hours device testing 2026-08-05) |
| 2026-08-17 to 2026-08-28 | AI portfolio review (P10) and vendor SOC 2 report reviews (P09) |
| 2026-09-17 | Results to the audit committee; deliverables approved by the COO and the CEO |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Registry defaults | The registry defaults fit this business and were kept: the primary system is the hospital EHR and clinical systems (named HECS in P02), the P08 incident is ransomware forcing EHR downtime and ambulance diversion, and the P10 lead use case is the sepsis prediction model. A second incident type (insider access) and five more AI use cases were added because the Mid-Market tier calls for two incident types and a use-case portfolio |
| Revenue split | Inpatient care about $52 million, emergency care about $14 million, outpatient surgery and endoscopy about $12 million, outpatient imaging and laboratory about $14 million (of which the outpatient center about $9 million), other about $8 million. Per calendar day: inpatient about $142,000, ED about $38,000, imaging and laboratory about $38,000; outpatient surgery about $48,000 per operating day (250 operating days) |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics. The policy requires a call to the carrier hotline before incident vendors are engaged |
| EHR vendor recovery commitments | The EHR vendor's SOC 2 system description states RTO 12 hours and RPO 15 minutes. The 12 downtime workstations (ED 3, each nursing unit 1, ICU 1, women's services 1, pharmacy 1, laboratory 1, house supervisor 1, surgery 1) receive an hourly read-only extract |
| Workforce activity | In the 12 months to 2026-06-30: 142 employee terminations, 88 internal transfers, and about 210 departures of contracted clinicians, agency nurses, and affiliated practice users. The last access review was completed in February 2026. The June 2026 phishing simulation click rate was 6.9% |
| Backups | Daily backups of cloud workloads and nightly backups of on-premises servers to the backup appliance, replicated to the backup account with 35-day write-once retention and separate administrator credentials. The backup appliance itself is joined to the hospital directory |
| MSSP | Contract requires a call to the Information Security Manager within 30 minutes of a high-severity alert. Medical devices, OT, the LIS, and the on-premises clinical servers do not send logs to the SIEM |
| Diversion | The county EMS communications center receives diversion status from hospitals under the county EMS protocol (fictional). Stroke and STEMI patients diverted from this hospital go to the regional medical center 11 miles away. The CNO, the ED Medical Director, and the administrator on call decide diversion together |
| Affiliated practice program | 18 independent physician practices (about 240 users) use the EHR's ambulatory module under the hospital's license. The hospital provides accounts, role assignment, help desk, training, and the lab and imaging interfaces under a services agreement and a BAA with each practice. Service fees are about $1.1 million a year |
| AI tools | AI-001 sepsis prediction model live since 2025-11-03 for adult ED and inpatient encounters. AI-002 FDA-cleared triage flags suspected large vessel occlusion and intracranial hemorrhage on head CT. AI-003 ambient scribe pilot with 12 ED physicians since 2026-05. AI-004 is the EHR's rule-based library (186 active rules, including a nursing early warning score). AI-005 coding assistance suggests codes for ED and outpatient encounters since 2026-01. AI-006: web proxy logs showed 214 staff using public generative AI sites in July 2026 |
| Terminology | "Hospital EHR and Clinical Systems (HECS)" is the SSP system in P02, identifier CSC-HECS-01 |
| Additional role titles | Administrator on call (rotating senior leaders); House Supervisor; ED Medical Director (contracted group); Director of Materials Management; Medical Staff Office Manager; Infection Prevention Manager |
| Other operating details | The EHR role catalog has 64 roles. 15 of the 210 PHI vendors are Tier 1 under the P09 tiering approach. The employee health plan's broker confirmed on 2026-07-08 that the hospital receives only summary health and enrollment information |
