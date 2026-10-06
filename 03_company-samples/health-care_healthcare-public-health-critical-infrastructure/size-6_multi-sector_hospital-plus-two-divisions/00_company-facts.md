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
