# Scenario facts: Cris Santos Company | Healthcare and Public Health | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes and of the Health Care (NAICS 62) samples. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; a holding company with three operating divisions) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate legal subsidiary |
| Division 1: Hospital System (NAICS 622110), **focus of this scenario** | 9 acute-care hospitals with 3,620 licensed beds: a 960-bed tertiary teaching hospital with a Level I trauma center (the flagship) and 8 community hospitals of 140 to 420 beds. 9 emergency departments (about 610,000 visits a year), about 186,000 inpatient admissions a year, and 46 hospital outpatient sites (imaging, infusion, wound care, clinics). About 29,000 employees. A HIPAA covered entity (health care provider that bills electronically, 45 CFR 160.103). Every hospital participates in Medicare and Medicaid |
| Division 2: Health Plan (NAICS 524114, sector 52 Finance and Insurance) | Medicare Advantage and commercial health plans; about 620,000 members. About 8,000 employees. A HIPAA covered entity (health plan). State insurance regulation applies in each state where it is licensed (handled generically) |
| Division 3: College of Nursing and Health Sciences (NAICS 611310, sector 61 Educational Services) | A proprietary (for-profit) institution of higher education, acquired by the group in 2023. Nursing (associate, bachelor's, RN-to-BSN, and online master's) and allied health programs (surgical technology, radiologic technology, respiratory therapy, medical laboratory technology). 4 campuses plus online programs; about 9,600 enrolled students. About 2,000 employees (faculty and staff). Participates in the federal student aid programs under Title IV of the Higher Education Act, so FERPA (34 CFR Part 99) applies and it agreed to comply with the GLBA Safeguards Rule (16 CFR Part 314) in its Program Participation Agreement. **Not** a HIPAA covered entity |
| Corporate shared services | Identity, data centers, network, cloud, security operations, ERP, HR, finance, legal, and internal audit. About 6,000 employees |
| Location | Headquartered in Florida. The hospitals are in 3 southeastern states (6 in Florida, 3 in two neighboring states); the Health Plan is licensed in 5 southeastern states; the College has 4 campuses in 2 states and online students in many states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| Why these three divisions | A health system with its own insurance and education arms: the Health Plan pays for much of the care the hospitals deliver, and the College trains the nurses and technologists the hospitals hire |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber and enterprise risk oversight; accepts Very High risks; approves group policy |
| Board audit committee | Receives group internal audit reports |
| Group CISO | Group security program, group policies, common controls (SYS-G1 to SYS-G3) |
| Group Chief Risk Officer | Group risk register and enterprise risk management roll-up; chairs the Group AI council |
| Group Chief Privacy Officer | Data classification, minimum necessary between covered entities, FERPA and HIPAA interplay |
| Group General Counsel | Business associate and intercompany agreements, the notification matrix |
| Group CIO, with the group identity, infrastructure (data centers and cloud), and SOC directors | Operate the corporate common control providers |
| Division security and compliance leads (3) | Division registers and supplements. The Hospital System lead is the hospital covered entity's HIPAA Security Official; the Health Plan lead is the Health Plan's Security Official; the College IT director is the College's Qualified Individual (16 CFR 314.4(a)) |
| Division privacy officers | Hospital System Privacy Officer and Health Plan Privacy Officer (each covered entity designates its own); the College Registrar is the FERPA compliance lead |
| Hospital System leadership | Division president; system chief medical information officer (CMIO); system chief nursing officer (CNO); system emergency management director (coordinator of the unified emergency preparedness program); clinical engineering director (medical devices); each hospital's chief executive and its incident command |
| Health Plan leadership | Division president; medical director (leads the utilization management committee, 42 CFR 422.137(a)) |
| College leadership | College president; dean of nursing; clinical placement director; financial aid director |
| Group internal audit | Reports to the board audit committee. Assesses common controls once and samples division controls; neither designs nor operates them |
| Disclosure committee | SEC materiality of cybersecurity incidents |
| Group AI council | Approves High-tier AI use cases (P10) |

## 3. Systems
| ID | System | Owner |
|---|---|---|
| SYS-G1 | Group identity platform (single sign-on, MFA, privileged access management, identity governance) and the group directory forest | Corporate |
| SYS-G2 | Group SOC, SIEM, and endpoint detection and response (EDR) | Corporate |
| SYS-G3 | Group infrastructure: two group data centers (DC1 primary in Florida; DC2 secondary in a neighboring state), the wide-area network, voice, the group file and collaboration services, and the group cloud platform (provider A primary; provider B for the immutable backup vault), vendor-agnostic | Corporate |
| SYS-G4 | Group ERP, HR, and payroll (SaaS) | Corporate |
| SYS-H1 | Enterprise EHR: one instance for all 9 hospitals, their outpatient sites, and 64 community-connect practices (ED, inpatient, perioperative, pharmacy, eMAR with barcode administration, patient access, revenue cycle, patient portal), including the EHR vendor's sepsis prediction model. Runs in DC1 with a replicated copy in DC2 | Hospital System |
| SYS-H2 | Ancillary clinical systems: laboratory information system and blood bank, PACS with a vendor-neutral archive, cardiology systems, pharmacy automation and dispensing cabinets, and the clinical interface engine | Hospital System |
| SYS-H3 | Medical devices (about 52,000 networked devices) on clinical device networks, and building and clinical operational technology (nurse call, building automation, medical gas alarms) | Hospital System (clinical engineering and facilities) |
| SYS-P1 | Health Plan administration: claims core (DC1), enrollment, utilization management platform, and member and broker portals (cloud provider A) | Health Plan |
| SYS-E1 | College academic systems (all SaaS): student information system with financial aid, learning management system, clinical placement and compliance tracking, an academic EHR training platform (synthetic patients only), and online exam proctoring | College |
| SYS-E2 | College campus IT: 4 campus networks, simulation labs, and the College's own directory (not yet on SYS-G1) | College |

**SSP system (P02):** the *Hospital Clinical Information System (HCIS)*: SYS-H1 (the enterprise EHR, including its downtime business continuity workstations) and the parts of SYS-H2 that exchange data with it (interface engine, laboratory and blood bank, PACS and archive, pharmacy automation), hosted in DC1 and DC2 and inheriting common controls from SYS-G1 to SYS-G3.

## 4. Current security posture: varies by division
**In place today:**
- Group policies aligned to CSF 2.0 and a common control catalog
- A 24x7 group SOC with EDR on servers and workstations in the Hospital System, Health Plan, and corporate
- SYS-G1 single sign-on and MFA for email and remote access for the Hospital System, Health Plan, and corporate workforce; privileged access management for administrators; quarterly access certification for the Hospital System and Health Plan
- Immutable backups of data center and cloud workloads in a vault at cloud provider B
- EHR replication from DC1 to DC2, with a failover test each year
- Downtime business continuity workstations on every nursing unit and in every ED
- A unified and integrated emergency preparedness program for the 9 hospitals under 42 CFR 482.15(f), with hurricane, surge, and mass-casualty plans and two exercises per hospital per year (482.15(d)(2))
- The Hospital System and the Health Plan act as separate covered entities, each with its own security and privacy officials
- The Health Plan's SOC 1 Type 2 report on claims administration for self-funded employers
- SEC Reg S-K Item 106 disclosure

**Missing or weak, found in the 2026 assessments:**
1. **Ransomware resilience of the shared data centers.** The EHR's production copy (DC1) and its replica (DC2) are joined to the same group directory forest, so one compromise can reach both. A full EHR restore from the immutable vault has never been tested; the estimated rebuild time is 5 to 7 days against an 8-hour recovery time objective. The Health Plan claims core and the College's administrative file shares sit in the same data center.
2. **Emergency preparedness for a cyber event.** The unified emergency plan and its risk assessments (482.15(a)(1), (f)(4)) are built around hurricanes and surge. They do not cover a system-wide IT outage that puts all 9 hospitals on downtime at once, and there are no system-level criteria for ambulance diversion and patient transfers during an IT outage. Downtime workstations at 3 community hospitals have not been tested in the last 12 months.
3. **Medical devices and clinical OT.** The device inventory is about 81% complete; about 6,900 devices (13%) run unsupported operating systems; device network segmentation is complete at 5 of 9 hospitals; 37 of 140 vendor remote support connections bypass group privileged access management.
4. **Student and trainee access.** About 4,500 nursing and allied health students a year rotate through the hospitals (about 3,100 from the College and 1,400 from 22 outside schools). Their EHR accounts are created from emailed rosters outside identity governance, sign in with a password only, and have no end dates. Students are workforce under HIPAA (160.103, "trainees"), but the hospitals rely on the schools for training records.
5. **The College lags group standards.** It runs its own directory and is not on SYS-G1. MFA is enforced for email but not for the student information and financial aid systems. Its written GLBA risk assessment dates from 2022, before the acquisition, and its Qualified Individual has not given the board a written annual report since 2023 (16 CFR 314.4(b), (c)(5), (i)).
6. **Sepsis prediction model.** The EHR vendor's sepsis model went live at all 9 hospitals in 2025 at the vendor's default threshold. Local validation was done only at the flagship, and the identification and mitigation steps of 45 CFR 92.210(b)-(c) were not documented.
7. **PHI exchanged between the two covered entities.** About 140,000 Health Plan members were hospital patients in the last 12 months. Routine feeds between the Hospital System and the Health Plan (admission notices, care management extracts) have no written minimum-necessary protocols (164.514(d)(3)).
8. **Multi-regulator incident notification.** One incident could trigger HIPAA notices from two covered entities, state attorney general and insurance commissioner notices, a Federal Student Aid breach report and an FTC Safeguards Rule notice for the College, county EMS coordination, and an SEC materiality decision. The group notification matrix has not been exercised, and the College's 2022 incident response plan is not part of the group plan.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 | The Hospital Clinical Information System (HCIS), the focus division's primary system (registry default "Hospital EHR and clinical systems"), with a common control catalog for the corporate controls it inherits |
| P03 | Each division's primary regulation: HIPAA Security Rule and the hospital emergency preparedness condition of participation (42 CFR 482.15) for the Hospital System; HIPAA, Medicare Advantage rules, and state insurance law for the Health Plan; the GLBA Safeguards Rule (16 CFR 314.4) and FERPA for the College. Group-wide obligations in a regulation-by-division matrix |
| P08 | Ransomware forcing EHR downtime and ambulance diversion (registry default), spreading from the shared data center so that it affects all three divisions: a multi-regulator notification matrix and an SEC materiality step |
| P09 | SOC 2 scoped per division: the Hospital System's community-connect EHR service for 64 practices is in scope; the Health Plan relies on its SOC 1 report; the College is out of scope, with reasons |
| P10 | Group AI governance program, with the sepsis prediction model (registry default) as the priority use case and division use cases under their own regulator rules |
| Cloud | Shared corporate cloud platform plus division workloads, vendor-agnostic. Most clinical systems run in the two group data centers |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division risk analyses, BIA, and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment by group internal audit, plus division samples |
| 2026-08-10 to 2026-08-21 | Sepsis model validation at all 9 hospitals and AI council review (P10) |
| 2026-09-15 | Results to the board risk committee; approvals |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Legal entities and HIPAA roles | The Hospital System and the Health Plan are legally separate subsidiaries under common ownership. They have **not** designated themselves an affiliated covered entity (45 CFR 164.105(b)), so each is a separate covered entity. Corporate shared services sits in the parent and is a business associate of both under intercompany BAAs (Hospital System BAA signed 2021; Health Plan BAA signed 2022). Corporate is a service provider of the College under a 2025 intercompany services agreement |
| Revenue split (fictional) | Hospital System about $10.5 billion (about $28.8 million a day); Health Plan about $7.1 billion in premiums and fees (about $19.5 million a day); College about $0.4 billion (about $1.1 million a day). Total about $18.0 billion, as in section 1 |
| Workforce split | Hospital System 29,000; Health Plan 8,000; College 2,000; corporate 6,000. Total 45,000 |
| Hospital System scale | About 3.4 million patients with an encounter in the last 3 years. No hospital has a transplant program (482.15(g) does not apply). No hospital holds itself out as providing substance use disorder diagnosis, treatment, or referral as a specialized program, so none is a 42 CFR Part 2 program; Part 2 records received from outside programs are flagged in the EHR and handled by the Privacy Officer case by case. All 9 hospitals have 100 or more beds |
| Community-connect EHR service | The Hospital System extends its EHR instance (SYS-H1) to 64 independent physician practices (about 1,100 users). For these practices it is a business associate. The practices asked for a SOC 2 Type 2 report by the end of 2027 |
| Health Plan scale | About 365,000 Medicare Advantage members, 170,000 fully insured commercial members, and 85,000 members of 40 self-funded employer plans it administers (administrative services only, ASO). For the ASO plans it is a business associate of each group health plan. Licensed as an HMO and insurer in 5 southeastern states (including Florida); **not licensed in New York**. Its SOC 1 Type 2 report covers ASO claims administration for the 12 months ending June 30 |
| Health Plan UM | The Health Plan uses rule-based prior authorization criteria and is piloting an AI prior authorization triage model (no production decisions; it has not yet been presented to the utilization management committee) |
| College scale | About 9,600 enrolled students and records for about 31,000 former students. About 80% of enrolled students receive Title IV aid. In 2025 the College's administrative file shares (registrar, financial aid, HR) moved to the group file service in DC1 (SYS-G3). The College operates no health clinic, so it is not a HIPAA covered entity; immunization and health clearance records it collects for clinical placements are education records under FERPA and are excluded from PHI (160.103, "protected health information", paragraph (2)(i)) |
| Students at the hospitals | College students on rotation sign a FERPA consent (34 CFR 99.30) that allows the College to send their placement and clearance information to the hospitals. In the hospitals they are trainees, so they are hospital workforce under HIPAA (160.103) |
| Prior incidents | No reportable breach in the last 3 years. A 2025 phishing incident at the College compromised 3 staff mailboxes; no customer information was found to be acquired |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Patient-safety risks rated High must be treated, not accepted |
| Other role titles used | HCIS system owner: the Hospital System clinical applications director. Hospital System: system chief medical officer, system chief pharmacy officer, system laboratory, imaging, quality, facilities, revenue cycle, transfer center, and health information management directors, the digital health director, the community-connect director, and the Section 1557 Coordinator (45 CFR 92.7). Health Plan: compliance officer and the claims operations, enrollment, member services, care management, and ASO operations directors. College: registrar, financial aid, admissions, and clinical placement directors and the dean of nursing. Corporate: group identity, SOC, infrastructure, and network directors, Group HR director, group chief financial officer, chief audit executive, and group communications lead |
| Data centers and recovery | DC2 is about 300 miles from DC1, in a colocation facility whose operator controls the building perimeter. EHR storage replication gives a 15-minute RPO; the vault at provider B keeps daily immutable copies for 35 days under a separate backup identity. The 2026-04 failover test brought the EHR back at DC2 in 1 hour 40 minutes. A clean recovery environment at provider B is planned for 2027-03-31 |
| HCIS details | About 34,000 workforce users plus about 4,500 students and trainees a year; about 1,900 EHR security templates; about 640 downtime workstations whose reports refresh every 2 hours; an active-passive clinical interface engine across DC1 and DC2; imaging archive tier at provider A. Clinical workstations unlock with badge tap and PIN; remote access uses MFA with number matching. An external penetration test of the data centers and EHR web services ran in 2026-03 |
| HCIS weaknesses found | 63 interface and service accounts with static passwords older than 1 year (9 stored in plain text, found during P07 testing); 11 ancillary servers on an unsupported operating system; median 47 days to apply critical patches on ancillary servers (target 30); interfaced devices not linked in the inventory; 412 student accounts active after their rotations ended (July 2026 sample); 37 of 140 device vendor connections outside PAM using shared vendor credentials |
| Students from outside schools | Affiliation agreements with 22 outside schools; they do not require the schools to report withdrawals or schedule changes. Hospitals rely on the schools' training attestations. Employee training completion is 98%, with monthly phishing exercises |
| Data shared between the covered entities | Routine admission-notice (ADT) feed from the Hospital System to Health Plan care management under a 2023 intercompany data sharing addendum, relying on 164.506(c)(4); it sends full ADT segments |
| Agreements | The 2021 Hospital System intercompany BAA does not expressly cover community-connect practices' PHI that corporate hosts; the 2022 Health Plan intercompany BAA covers the ASO plans' PHI. The 2025 College intercompany services agreement requires same-day phone notice to the College of an incident affecting its data, then written notice; it does not state the FERPA 99.33(a) redisclosure limits. Community-connect practices federate their own identity providers with MFA required by contract (attested, not technically verified) |
| Emergency preparedness | The unified plan was reviewed 2025-06; hazard analyses cover each hospital and the community; the plan was activated for a 2024 hurricane; the 2025 additional exercise was a mass-casualty drill. Hospitals belong to regional health care coalitions. Transfer arrangements point mostly to other group hospitals. Staff mass notification uses group email and SMS through SYS-G1. Diversion criteria and a system coordination rule for IT outages are in the P08 runbook, to be adopted as the cyber annex; the first cross-division tabletop is set for 2026-12-15 |
| Health Plan details | UM committee composition meets 42 CFR 422.137(c); internal coverage criteria are published with evidence summaries; a June 2026 audit of 60 UM cases found every expected adverse decision had physician review. About 85% of claims staff can work remotely. The claims core was restore-tested in 2026-02; its recovery runbooks are kept only on the claims file share. Brokers may still use SMS codes. Delegated UM and pharmacy benefit vendors are reviewed once a year |
| College details | The College IT director was designated Qualified Individual in 2023. The College adopted group policies in 2024 but has no division supplement; its 2022 IT standards, 2022 risk assessment, and 2022 incident response plan are still in use. College employees moved to group HR and payroll in 2024; EDR reached College servers in 2025. MFA covers email only. Its 2025 Title IV compliance audit reported a finding on the outdated risk assessment. Semiannual vulnerability scans of campus networks; last penetration test 2023. File shares moved to DC1 with their old permission groups. Students in clinical programs sign a FERPA consent naming the clinical sites (40 files sampled) |
| AI program | Group AI Standard and Group AI council adopted in 2026; 10 use cases in the inventory (P10), including the sepsis model at 9 hospitals since 2025, an inpatient deterioration index, a CT intracranial hemorrhage triage tool at the flagship, an ED AI scribe pilot (60 physicians), a proposed portal reply drafting feature, the Health Plan's prior authorization triage model in shadow mode and its fraud, waste, and abuse model, the College's online proctoring and AI tutoring assistant, and an enterprise generative AI assistant (pilot, about 3,000 users) |
| Sepsis model validation (2026-01-01 to 2026-06-30) | About 190,000 scored adult encounters; 1,412 confirmed sepsis cases, 974 caught (69.0%); 7,560 alerted encounters (PPV 12.9%); 58% of alerts screened within 1 hour; subgroup and hospital results as in P10 section 4.1 |
| P08 exercise scenario (illustrative counts) | Entry through a device vendor connection at a community hospital; about 1.1 million patients (including about 40,000 patients of 12 community-connect practices), about 260,000 members (including members of 22 ASO plans), about 70,000 people in both sets, and about 14,000 current and former students affected |
