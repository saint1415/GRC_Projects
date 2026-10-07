# Scenario facts: Cris Santos Company | Emergency Services | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant) |
| Business | Private ambulance (EMS) provider (NAICS 621910 Ambulance Services) with three business lines: (1) ground ambulance operations: advanced life support (ALS) and basic life support (BLS) 911 emergency response under county and municipal agreements, plus interfacility and non-emergency transport; (2) a managed transportation division that arranges Medicaid non-emergency medical transportation (NEMT) as a broker for state Medicaid programs and managed care plans; (3) EMS billing services for public EMS agencies |
| Location | Headquartered in Florida. Operations in Florida, Georgia, Alabama, South Carolina, and Tennessee: 210 stations and posts, 4 regional communications centers (RCC-1 to RCC-4), 12 fleet maintenance hubs, 3 managed transportation contact centers, 1 billing center, and headquarters (231 sites). **State laws are handled generically:** notify and keep records under the law of each state where affected individuals reside or where the company operates, with Florida as the worked example |
| Workforce | 12,000 employees: about 8,200 field clinicians (EMTs and paramedics), 850 dispatchers and call-takers, 1,050 managed transportation contact center and network staff, 700 billing and revenue cycle staff, 600 fleet and logistics staff, and 600 corporate, IT, security, and administrative staff |
| Volume | About 2.5 million responses and 1.9 million ground transports a year (about 5,200 transports a day). 911 service under 27 county and municipal agreements covering about 9.8 million residents; interfacility service for about 300 hospitals and 1,900 nursing and other facilities. The managed transportation division arranges about 7.2 million trips a year |
| Fleet | About 1,450 ground ambulances (about 980 ALS and 470 BLS), including 160 from the acquired Tennessee operation (AQ-01). No air medical service |
| Revenue | About $4.8 billion a year (fictional): ground ambulance transport about $2.1 billion; county and municipal contract fees about $0.3 billion; managed transportation about $2.25 billion (mostly capitated payments passed through to network transportation providers); EMS billing services about $0.15 billion. Not small under the SBA standard for NAICS 621910 ($22.5 million; 13 CFR 121.201) |
| Payers | Medicare Part B (ambulance supplier), Medicaid in 5 states, Medicaid managed care plans, commercial plans, facility contracts, and county subsidies. Medicaid is federal financial assistance, so Section 1557 of the Affordable Care Act applies (45 CFR Part 92) |
| Licenses and county authority | An EMS service license in each of the 5 states. Florida worked example: state license for ALS and BLS transport (Fla. Stat. 401.25; Chapter 64J-1, F.A.C.), a certificate of public convenience and necessity from each Florida county served (Fla. Stat. 401.25(2)(d)), and a medical director for each licensed service (Fla. Stat. 401.265(1)) |
| HIPAA status | **Covered entity:** a health care provider that transmits claims electronically in HIPAA standard transactions (45 CFR 160.103). Also a **business associate** for two service lines: EMS billing services for 46 public EMS agencies (SL-1), and managed transportation for 3 state Medicaid programs and 6 managed care plans (SL-2), each under a business associate agreement |
| County 911 relationship | County public safety answering points (PSAPs) answer 911 calls and send EMS incidents to the company's CAD over CAD-to-CAD interfaces (30 PSAP interfaces: 26 on the enterprise CAD, 4 on the AQ-01 legacy CAD), or transfer callers to company dispatchers. The company has **no access** to state or national criminal justice databases or law enforcement records systems. The CAD-to-CAD hub drops law enforcement fields by design, and the 3 county PSAPs that asked to share premise hazard notes confirmed in writing in 2026 that the notes sent contain no criminal justice information |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); SOX IT general controls; multi-state operations; growth by acquisition (AQ-01, a Tennessee ambulance provider acquired 2025-11; AQ-02, a billing services firm acquired 2026-03); two service lines offered to external clients |
| Not in scope | FBI CJIS Security Policy and 28 CFR 20.21 and Part 23: no criminal justice information (P03 section 1). 42 CFR Part 2: not a federally assisted substance use disorder program. FCC EAS rules: not an EAS participant. Payment cards: patients and members pay through a payment processor's hosted page, outside company systems. The employee group health plan is a separate covered entity handled by the benefits program |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board (audit committee plus a risk committee) | Cyber oversight (Item 106 disclosure) |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk; materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Program owner; HIPAA **Security Officer** is the Director of Security Operations, reporting to the CISO |
| Chief Privacy Officer | HIPAA **Privacy Officer** |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Medical Officer | Enterprise medical director; clinical oversight of dispatch protocols, patient care protocols, and clinical AI |
| GRC team (7), Security Operations Center (24x7, in-house plus MSSP overflow), Internal Audit (in-house) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | Enterprise computer-aided dispatch (CAD): call entry, unit recommendation, automatic vehicle location (AVL), mobile data, and the CAD-to-CAD hub | Vendor-licensed CAD software, customer-managed on Cloud provider A, active in one region with a warm standby in a second region. Serves RCC-1 to RCC-3 and the enterprise fleet. Named accounts through SSO with MFA |
| SYS-02 | Electronic patient care reporting (ePCR) with hospital record delivery and state data exports | Vendor SaaS (business associate, SOC 2 Type 2). About 3,900 rugged tablets work offline and sync. AQ-01 moved onto it in 2026-05 |
| SYS-03 | Revenue cycle platform with two clearinghouses | Vendor SaaS (business associate). Used for the company's own claims and for the SL-1 billing services clients |
| SYS-04 | Identity platform (SSO, MFA, privileged access management, identity governance) | AQ-01 identities are still in a legacy directory |
| SYS-05 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 1 colocation data center | Cloud provider A: CAD, integration hub, call recording archive, data platform. Cloud provider B: managed transportation platform (SL-2), member app, AI services. Colocation DC-1 (Georgia): network core, telephony gateways, offline backup copies |
| SYS-06 | Regional communications centers RCC-1 to RCC-4 | About 260 dispatch positions (230 at RCC-1 to RCC-3; 30 at RCC-4), radio console gateways to county P25 systems, UPS and generators. RCC-4 is AQ-01's center |
| SYS-07 | Fleet mobile systems | Per ambulance: a cellular vehicle router with GPS, a mobile data computer (MDC), 2 to 3 ePCR tablets, and a cardiac monitor that sends 12-lead ECGs through the monitor vendor's cloud relay (business associate) |
| SYS-08 | Enterprise network (SD-WAN with dual carriers at communications centers) | 14 AQ-01 sites remain on legacy firewalls and a flat network |
| SYS-09 | Endpoints | About 4,100 workstations and laptops (including dispatch consoles), 3,900 tablets, and 1,450 MDCs, with EDR and device management |
| SYS-10 | ERP, payroll, and crew scheduling (SOX-relevant) | SOX IT general controls tested annually |
| SYS-11 | Telephony and contact center platform with call recording (SaaS) | Request lines, transferred 911 callers, and the managed transportation contact centers |
| SYS-12 | AQ-01 legacy estate | On-premises CAD on an unsupported server operating system with shared console logins, a legacy directory, and no SIEM feed. Migration to SYS-01 due 2027-03-31 |
| SYS-13 | About 650 vendors (190 with PHI) and about 1,400 managed transportation network providers | Tiered third-party risk program |
| SYS-14 | AI portfolio (9 use cases) | Governed by an AI governance committee formed in 2025 |

**SSP system (P02):** the *Enterprise Dispatch and Patient Care Platform (EDPCP)*: the enterprise CAD (SYS-01) with AVL, mobile data, and the CAD-to-CAD hub; dispatch consoles at RCC-1 to RCC-3; fleet mobile systems for the enterprise fleet (SYS-07); and the company's ePCR tenant (SYS-02) with its CAD-to-ePCR and hospital delivery interfaces. It is High for availability and inherits common controls from the enterprise platform.

## 4. Current security posture: mostly compliant, with targeted gaps
**In place today:**
- A mature program aligned to CSF 2.0
- Annual risk analysis tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC
- PAM
- Quarterly access certification
- Immutable backups
- Enterprise CAD with a warm standby region, and center-to-center failover between RCC-1, RCC-2, and RCC-3
- Quarterly manual dispatch drills at RCC-1 to RCC-3
- Annual DR tests for tier-1 systems
- Tiered vendor reviews
- Annual SOC 2 Type 2 report for SL-1 billing services (Security and Confidentiality) since 2025
- SEC Item 106 disclosure in its 10-K

**Targeted gaps:**
1. **Acquisition integration.** AQ-01 (1,150 employees, 160 ambulances, RCC-4, 4 Tennessee county agreements) still runs its own on-premises CAD on an unsupported server operating system, with shared console logins, a legacy directory, a flat network, and no SIEM feed.
2. **Dispatch recovery time.** The 2026-05-14 regional failover test brought the enterprise CAD back in 1 hour 25 minutes against a 1-hour RTO, and center-to-center failover has been tested for RCC-1 and RCC-2 but not RCC-3.
3. **Fleet edge devices.** About 160 of 1,450 vehicle routers run end-of-support firmware, and MDCs in the AQ-01 fleet and in 15% of the enterprise fleet still use shared vehicle logins.
4. **Managed transportation network providers.** About 1,400 network providers reach trip manifests with PHI through the broker portal. 38% have not completed the annual security attestation, and MFA is enforced for only 62% of provider portal accounts.
5. **AI.** 9 AI use cases, but only 5 have completed committee review. AI call triage runs in shadow mode at RCC-1 and RCC-2 and under-triages Spanish-language calls.
6. **Materiality.** The materiality playbook was written for data breaches. It has never been exercised for a dispatch outage, its worksheet leaves out county contract penalties, and two disclosure committee members are new since 2026.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 | Computer-aided dispatch outage from ransomware (registry default): ransomware encrypts the enterprise CAD application tier and dispatch consoles at two communications centers, forcing manual dispatch across several counties, with possible theft of CAD data and call recordings. Includes an **SEC materiality assessment and 8-K Item 1.05** step, county notifications, and a multi-state breach-notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to external clients: SL-1 EMS billing services (Security, Availability, Confidentiality, Processing Integrity) and SL-2 managed transportation (Security, Availability, Confidentiality, Privacy) |
| P10 | Enterprise AI portfolio (9 use cases), with the committee operating model and a full assessment of AI-001, AI-assisted emergency call triage (registry default) |
| Cloud | Multi-cloud (vendor-agnostic) with common controls |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line) |
| 2026-09-10 | Results to the risk committee of the board |
