# Scenario facts: Cris Santos Company | Other Services | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about acquirers, manufacturers, the protection plan administrator, customers, contracts, and vendors are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; a consumer technology services group) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate legal subsidiary under common ownership: Cris Santos Repair, LLC (Device Repair), Cris Santos Electronics, LLC (Electronics Retail), and Cris Santos Tech Services, LLC (IT Support Services) |
| Division 1: Device Repair (NAICS 811210), **focus of this scenario** | A national electronics and device repair chain: **1,120 repair stores**, **260 repair counters inside the group's electronics stores** (staffed and run by Device Repair), and **5 regional repair depots** (mail-in repair, board-level repair, manufacturer warranty repair, enterprise depot repair, trade-in sanitization and refurbishment; 2 of them house the **data recovery labs**). Manufacturer-authorized service provider for **Manufacturer A** (all stores and depots) and warranty depot for **Manufacturer B** (3 depots). Repair network for the **third-party administrator (TPA)** of the device protection plans that Electronics Retail sells. Free device recycling drop-off at every store. About 17,500 employees |
| Division 2: Electronics Retail (NAICS 449210, sector 44-45 Retail Trade) | **260 consumer electronics stores**, a website and mobile app (home delivery, store pickup, and installation, shipped only to addresses in the group's 26 states), a **trade-in program** (used phones, tablets, and laptops bought for store credit and sent to Device Repair depots for sanitization and resale), sale of device protection plans as an agent of the TPA, and sale of IT Support subscriptions. About 21,500 employees and about 8.4 million loyalty members (members must be 18 or older) |
| Division 3: IT Support Services (NAICS 541519, sector 54 Professional, Scientific, and Technical Services) | (a) **Consumer tech support** subscriptions (remote and in-home) for about 1.3 million subscribers; (b) **managed IT services** for about 4,200 small and mid-sized business customers (about 310,000 managed endpoints), including 610 medical and dental practices, 380 accounting and tax firms, and 520 retail and restaurant businesses whose point-of-sale networks it manages. Issues an annual **SOC 2 Type 2** report. About 4,500 employees |
| Corporate shared services | Identity, network, cloud platform, two colocation data centers, security operations, customer engagement platform, ERP and finance, HR, legal, and internal audit. About 1,500 employees |
| Location | Headquartered in Florida. All stores, depots, employees, and customers are in **26 states** in the Southeast, Mid-Atlantic, Midwest, and Texas. The group has **no stores, employees, customers, shipments, or mail-in service in California, Colorado, or New York** (a standing group decision, reviewed by counsel each year). **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about **$18.0 billion** annual revenue (fictional): Device Repair about $3.9 billion, Electronics Retail about $12.6 billion, IT Support Services about $1.5 billion |
| Why this combination | A consumer technology services group: Retail sells the devices, plans, and support subscriptions; Device Repair fixes, sanitizes, and refurbishes the devices; IT Support supports the people and businesses that use them |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber, privacy, and AI risk oversight; accepts Very High risks |
| Board audit committee | Oversees group internal audit and SEC reporting |
| Group CISO; Group Chief Risk Officer; Group Chief Privacy Officer; Group General Counsel | Group standards, group risk register, common controls, notification matrix |
| Division presidents (3) | Accept Moderate risks for their division |
| Device Repair CISO | Division security and compliance lead; owns the repair merchant's PCI DSS program and Report on Compliance (ROC), the STPP security plan, and the manufacturer program security terms |
| Device Repair chief operating officer | Owns repair operations, technician standards, depots, data recovery labs, and sanitization |
| Electronics Retail CISO | Division security and compliance lead; owns the retail merchant's PCI DSS program and ROC |
| IT Support security and compliance lead | Division security and compliance lead; **HIPAA Security Official** for the division's business associate services; owns the SOC 2 program |
| IT Support Privacy Official | HIPAA privacy duties for the division's business associate services; customer contract privacy terms |
| Group AI council | Approves High-tier AI use cases under the Group AI Standard (P10) |
| Group internal audit | Independent of the teams it assesses (reports to the board audit committee). Assesses common controls once and samples division controls (P07) |
| Disclosure committee | SEC materiality determinations (Form 8-K Item 1.05) |
| External assurance | PCI Qualified Security Assessor (QSA) firm for both merchants' ROCs; SOC 2 service auditor (independent CPA firm) for IT Support |

## 3. Systems
| ID | System | Owner |
|---|---|---|
| SYS-G1 | Group identity platform (workforce single sign-on, MFA, privileged access management (PAM), identity governance) | Corporate |
| SYS-G2 | Group SOC, SIEM, and endpoint detection and response (EDR) | Corporate |
| SYS-G3 | Group cloud platform and data centers: landing zones in two public cloud providers (provider A and provider B, vendor-agnostic) and two group colocation data centers | Corporate |
| SYS-G4 | Group customer engagement platform: one customer account and sign-in across the three divisions, CRM and customer data platform, contact center, and the **group customer chatbot** | Corporate (group digital) |
| SYS-G5 | Group ERP, HR, and payroll, with the background check vendor integration | Corporate |
| SYS-D1 | **Service Ticketing and Point-of-Sale Platform (STPP)**: intake and consent, tickets, customer and device records, parts, invoicing, payment integration with the P2PE terminals, customer status pages, and the interfaces to the TPA, Manufacturer A and B portals, and the AI-assisted diagnostics service | Device Repair |
| SYS-D2 | Repair bench and depot technology: about 6,900 technician bench workstations, about 40 third-party diagnostic, flashing, and data transfer tools, the **AI-assisted diagnostics** service, depot data recovery labs, and sanitization stations | Device Repair |
| SYS-D3 | Retail commerce and payments: store point-of-sale (POS) lanes, payment switch, website and app back end, order management, trade-in system, and loyalty | Electronics Retail |
| SYS-D4 | Retail store infrastructure: store networks and Wi-Fi, CCTV, electronic shelf labels | Electronics Retail |
| SYS-D5 | IT Support service delivery platform: remote monitoring and management (RMM), professional services automation (PSA) ticketing, remote support tool, customer credential vault, documentation, and the managed backup service | IT Support Services |

**SSP system (P02):** the *Service Ticketing and Point-of-Sale Platform (STPP)*: the Device Repair division's ticketing, customer, payment, and parts platform (SYS-D1) plus the repair bench environment that connects customer devices to it (SYS-D2 bench workstations and diagnostic tools), used at 1,120 repair stores, 260 in-store repair counters, and 5 depots and by IT Support in-home technicians, inheriting group common controls from SYS-G1 to SYS-G4.

## 4. Current security posture: a defined group program, mature in retail and managed services, uneven in the repair estate
**In place today:**
- Group policies aligned to NIST CSF 2.0, with division supplements, and a common control catalog
- 24x7 group SOC, SIEM, and EDR; single sign-on with MFA for all workforce users; PAM with just-in-time elevation for administrators
- PCI DSS validated every year by a QSA Report on Compliance for the retail merchant (since 2014) and for the repair merchant (since 2023)
- A **PCI-listed validated P2PE solution** from the processor on all payment terminals at repair stores and depots
- Quarterly access certification for group applications; immutable backups in the second cloud provider
- A **passcode vault** in the STPP (restricted field, purged 7 days after device release) live at 680 of 1,120 repair stores
- Background checks for all technicians before hire (a Manufacturer A program term)
- A device sanitization standard (2019) with per-device certificates for trade-in devices
- IT Support SOC 2 Type 2 report (Security, Availability, Confidentiality) issued every year since 2024
- Board risk committee oversight; SEC Reg S-K Item 106 disclosure in the annual report

**Missing or weak, found in the 2026 assessments:**
1. **Passcodes and account credentials.** Outside the 680 stores with the passcode vault, staff still type device passcodes, and sometimes customers' account email and password, into free-text ticket notes visible to every STPP user in the region. A July 2026 search found about 2.1 million tickets with passcodes and about 96,000 with account passwords in notes. Notes are never purged.
2. **Technician access to device contents.** The 260 in-store repair counters still use **shared bench logins**. USB storage is blocked and bench sessions are logged only at the depots and data recovery labs. Customers filed 37 complaints in 2025-2026 alleging that technicians viewed or copied personal content.
3. **Shared networks at in-store repair counters.** Bench workstations and customer devices under repair at the 260 in-store counters connect to the retail store network. The 2026 retail pre-ROC segmentation test found the bench network reachable from the POS lane network at 112 stores.
4. **Sanitization.** The 2019 sanitization standard is based on NIST SP 800-88 Rev. 1 and has not been updated to Rev. 2 (September 2025). Recycling drop-off devices at stores (about 640,000 a year) have no per-device record, and verification sampling is not done at 2 of 5 depots.
5. **Third-party bench tools.** About 40 diagnostic, flashing, and data transfer tools on bench workstations update themselves from vendor sites, run with local administrator rights, and were never reviewed as a software supply chain risk.
6. **IT Support remote tools.** The RMM and remote support tools can push scripts to about 310,000 customer endpoints. 14 technicians held standing global administrator rights in the RMM, and RMM console MFA is not phishing-resistant.
7. **AI.** The AI-assisted diagnostics service (live at all stores since 2025) recommends repairs and flags liquid damage that voids warranty coverage, with no accuracy measurement by device model; marketing calls it "AI-verified diagnostics" without substantiation. The group customer chatbot shared by all three divisions records passcodes that customers paste into chats. IT Support is piloting an AI agent that runs remediation scripts on customer endpoints.
8. **Cross-division notification.** Two merchant agreements, the TPA agreement, the Manufacturer A and B agreements, enterprise repair contracts, IT Support's business associate agreements and managed services contracts, state breach laws, and SEC disclosure all apply to one incident. The group matrix lists them but has never been exercised.
9. **Common control inheritance.** It is documented for the retail cardholder data environment (PCI responsibility matrix) and for IT Support (SOC 2 system description). It was never documented for Device Repair before this SSP, and it is still not documented for the depots and data recovery labs.
10. **Division supplement drift.** The Device Repair supplement was last aligned to group policy in 2024. The in-store repair counters follow retail store procedures where the two conflict.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 | Registry default kept: the Service Ticketing and Point-of-Sale Platform (STPP), the focus division's system of record, used by all three divisions and inheriting group common controls |
| P03 | Each division's primary rule set. Device Repair: the vertical's NIST CSF 2.0 benchmark (all 106 subcategories), the binding legal baseline (FTC Act Section 5; state breach, data security, and disposal law with Fla. Stat. 501.171 as the worked example; FTC Disposal Rule), and PCI DSS v4.0.1 (Level 1 merchant, validated P2PE). Electronics Retail: PCI DSS v4.0.1 (Level 1 merchant) with FTC Act Section 5, FACTA truncation, and applicability screens. IT Support: an applicability finding that its vertical's primary rule (FTC Safeguards Rule) does not bind it directly, the HIPAA Security Rule as a business associate, PCI DSS service provider duties, SOC 2 commitments, and the FTC Act. A regulation-by-division matrix ties them together |
| P08 | Registry default kept and widened: a compromised update of a third-party bench diagnostic tool exposes customer device data at repair benches (Device Repair stores, in-store counters, and depots, and IT Support in-home visits) and reaches retail POS lanes through the in-store counter network (the point-of-sale compromise). It needs a multi-regulator notification matrix and an SEC materiality decision |
| P09 | SOC 2 scoped per division: IT Support managed services in scope (a true service organization; existing Type 2); Device Repair enterprise depot repair and protection plan fulfillment in scope for a first readiness assessment; Electronics Retail out of scope, with reasons and the assurance it relies on instead (PCI ROC) |
| P10 | Registry default kept as the priority use cases: AI-assisted diagnostics (Device Repair) and the group customer chatbot, assessed inside a group AI governance program with the other divisions' use cases |
| Cloud | Shared corporate platform (two providers, vendor-agnostic) plus two colocation data centers and division workloads |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-01 to 2026-07-31 | Group and division risk analyses; internal PCI DSS pre-assessments of both cardholder data environments |
| 2026-07-01 to 2026-08-31 | Common control assessment (group internal audit) plus division samples |
| 2026-08-17 to 2026-08-28 | Group AI council assessment of priority AI use cases |
| 2026-08-28 | IT Support 2026 SOC 2 Type 2 report issued (period 2025-07-01 to 2026-06-30) |
| 2026-09-10 | Results to the board risk committee; deliverables approved |
| 2026-10-19 to 2026-11-20 | QSA fieldwork for the 2026 retail ROC (planned) |
| 2026-11 | Manufacturer A annual program audit (Device Repair) |
| 2026-12-15 | 2026 retail ROC and AOC due to the acquirer |
| 2027-01-11 to 2027-02-12 | QSA fieldwork for the repair ROC (planned) |
| 2027-03-31 | Repair ROC and AOC due to the acquirer |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only |
