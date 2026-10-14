# Scenario facts: Cris Santos Company | Manufacturing | Enterprise

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or FDA guidance, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; connected medical device manufacturer) |
| Business | Designs, builds, and services connected medical devices (NAICS 334510, Electromedical and Electrotherapeutic Apparatus Manufacturing). Runs the **Device Data Cloud (DDC)** for hospital customers, a **Remote Cardiac Monitoring (RCM) service** for hospitals and physician practices, and a **consumer companion app** for its home blood pressure monitor |
| Location | Headquartered in Florida. Three U.S. plants: **FL-1** (Florida: patient monitors and hospital device gateways), **MN-1** (Minnesota: infusion pumps; acquired in 2024 with the infusion pump business), and **TX-1** (Texas: wearable ECG patches, home blood pressure monitors, and the national distribution center). R&D centers in Florida and Massachusetts. Two RCM monitoring centers (Florida and Texas). Two colocation data centers (DC-1 Florida, DC-2 Texas). Customers in all 50 states. **All operations and all law in these samples are U.S. only.** International distribution and export classification are handled by a separate trade compliance program outside these samples. **State breach laws are handled generically:** the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: 2,600 R&D (about 1,100 device software and firmware, 450 cloud and data), 5,200 manufacturing and supply chain, 900 quality and regulatory, 1,300 field service and customer support, 700 RCM service staff (certified cardiac technicians and support), 800 commercial, 500 general and administrative |
| Revenue | About $4.8 billion a year (fictional); about $13.2 million per calendar day and $19.2 million per business day |
| SEC status | Publicly traded; not a smaller reporting company. Form 8-K Item 1.05 and Regulation S-K Item 106 (17 CFR 229.106) apply. SOX IT general controls are tested annually over ERP and financial systems |
| Products (all class II) | **VM-700** bedside and transport patient monitor (current; 510(k) cleared 2024, after section 524B took effect; about 77,000 units in the field). **VM-500** patient monitor (legacy; cleared 2019; sales ended 2025; supported until 2028; about 41,000 units). **DG-10** hospital device gateway (on-premises appliance that connects monitors and pumps to the DDC; about 3,100 units at about 2,300 hospitals; cleared as part of the VM-700 system in 2024). **IV-300** large-volume infusion pump with wireless drug library (acquired 2024; cleared 2021, before 524B; the second-generation wireless module was a 2025 510(k) submission, cleared 2026-01, so 524B applied to it; about 210,000 pumps, 62,000 still on the first-generation module). **CR-100** wearable ECG patch with a phone gateway app (cleared 2023-09, after 524B; about 420,000 monitoring studies a year). **US-20** handheld ultrasound probe with a tablet app (cleared 2022, before 524B; about 35,000 probes). **HB-40** home blood pressure monitor sold over the counter, Bluetooth to the consumer companion app (cleared 2024 with 524B content; about 1.1 million sold). **AI-001** left ventricular ejection fraction (LVEF) estimation function for the US-20 (in development; 510(k) planned 2027 Q2; see P10) |
| Device Data Cloud (DDC) | Multi-tenant platform on Cloud provider A (vendor-agnostic). Receives telemetry from monitors and pumps through DG-10 gateways; gives clinicians remote viewing and secondary alarm notifications; distributes pump drug libraries and signed firmware updates (the update service); archives US-20 images for hospital users; sends results to hospital EHRs. Primary alarms always sound at the bedside device |
| Remote Cardiac Monitoring (RCM) service | CR-100 patches stream ECG data through the patient's phone gateway app to the RCM platform on Cloud provider A. An FDA-cleared arrhythmia detection algorithm (AI-002) flags events; cardiac technicians in the two monitoring centers review them 24x7 and send reports to the prescribing physician, calling urgent findings by phone. Hospitals and practices bill payers; the company bills its customers, not payers |
| Consumer companion app | Offered directly to consumers who buy the HB-40. Stores blood pressure and pulse readings, weight and medications the user enters, and data the user imports from the phone's health platform, on the Consumer Health Platform (Cloud provider B). The user controls sharing (for example, a PDF report to a doctor). About 900,000 active users. Not offered on behalf of any HIPAA covered entity |
| Customers | About 2,300 hospitals and health systems (DDC, devices) and about 5,200 physician practices (RCM). About 3,400 business associate agreements (BAAs), because health systems sign one BAA for many hospitals |
| HIPAA status | **Business associate, not a covered entity**, determined in the intake obligations register (N62-R01; EV-006). The company does not bill payers or conduct HIPAA standard transactions, so it is not a covered health care provider (45 CFR 160.103). It creates, receives, maintains, and transmits PHI on behalf of hospitals and practices through the **DDC and the RCM service**, so it is their business associate: the Security Rule applies to those services (45 CFR 164.302), BAA terms follow 164.314(a), and breach notice to customers follows 164.410. About 62 subcontractors handle PHI for the company and need subcontractor BAAs (164.308(b)(1), 164.314(a)(2)(iii)). The company's employee group health plan is a separate covered entity run by the benefits program and is outside these samples |
| FTC Health Breach Notification Rule | **Applies to the consumer companion app**, determined in the intake obligations register (N62-R06; EV-012). The app is a personal health record: it draws information from multiple sources (the HB-40, the user, and the phone's health platform) and is managed by and for the individual. The company offers it outside any HIPAA relationship, so for the app it is a vendor of personal health records under 16 CFR 318.2, and 16 CFR 318.1 does not exclude it. The rule does **not** apply to the DDC or RCM, where the company acts as a business associate (318.1(a)) |
| FDA status | Registered device manufacturer at all three plants. Quality management system under the QMSR (21 CFR Part 820, which incorporates ISO 13485 by reference; in effect since 2026-02-02). Section 524B of the FD&C Act (21 U.S.C. 360n-2) applies to every premarket submission for a cyber device made on or after 2023-03-29. Medical device reporting (21 CFR Part 803) and corrections and removals (21 CFR Part 806) apply to every marketed device |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): DFARS 252.204-7012, CMMC, and ITAR (N31-33-R01 to R03): no defense contracts and no defense articles. EAR (N31-33-R04): export classification is handled by the trade compliance program outside these samples. FAR 52.204-25: the company holds no federal prime contracts or subcontracts. CIRCIA: proposed rule only (not in effect) |
| Regulatory driver IDs | N31-33-R05 (FD&C Act 524B) is the primary driver. For the business associate services, this folder cites the Health Care vertical's verified IDs: **N62-R01** (HIPAA Security Rule), **N62-R03** (HIPAA Breach Notification Rule), and **N62-R06** (FTC Health Breach Notification Rule, for the consumer app). FDA regulations (21 CFR 803, 806, 820) and SEC rules are cited directly |
| Added at this size | SEC cybersecurity disclosure; SOX IT general controls; three plants with OT networks; an acquired business (infusion pumps, MN-1) still being integrated; about 2,400 suppliers including 2 contract manufacturers |

## 2. People (role titles only)
| Role | Security, product security, and compliance duties |
|---|---|
| Board of directors (audit committee; risk and technology committee) | The risk and technology committee oversees cybersecurity and product security risk (Item 106 disclosure); the audit committee oversees Internal Audit, SOX, and disclosure controls |
| Chief Executive Officer (CEO); Chief Financial Officer (CFO) | Accept Very High risks jointly; take part in materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Enterprise security program owner; chairs the policy governance committee |
| Vice President, Product Security (VP Product Security) | Product security program and the Product Security Incident Response Team (PSIRT, 14 staff); coordinated vulnerability disclosure (CVD); reports to the Chief Technology Officer with a dotted line to the CISO |
| Chief Technology Officer (CTO) | R&D and device software engineering; owner of the Device Software Factory |
| Chief Quality and Regulatory Officer (CQRO) | FDA submissions and correspondence; complaint handling; MDR (21 CFR 803); corrections and removals (21 CFR 806); owns section 524B compliance |
| Chief Privacy Officer | HIPAA privacy duties as a business associate; breach risk assessments; FTC Health Breach Notification Rule for the consumer app |
| Director of Security Operations | Designated HIPAA security official for the business associate services (45 CFR 164.308(a)(2)); runs the 24x7 SOC (in-house, with an MSSP for overflow) |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee; leads the P07 assessment |
| General Counsel | Chairs the disclosure committee |
| GRC team (10, second line), SOC, PSIRT, OT security team (6), Internal Audit (in-house IT audit group) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems
The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Notes |
|---|---|---|
| SYS-01 | Device Data Cloud (DDC), Cloud provider A | Holds PHI for hospitals (about 14 million patient records, 24-month rolling retention set by BAAs). Update service distributes signed firmware and drug libraries. SOC 2 Type 2 (Security, Availability, Confidentiality) since 2023 (EV-013) |
| SYS-02 | RCM platform, Cloud provider A | Holds PHI for practices and hospitals (about 1.6 million patients). Arrhythmia algorithm (AI-002); technician workstations in two monitoring centers. Disaster recovery test 2026-04-18 recovered in 3.5 hours against a 2-hour RTO (EV-049) |
| SYS-03 | Consumer Health Platform, Cloud provider B | Companion app back end (about 900,000 active users); PHR identifiable health information under 16 CFR Part 318 |
| SYS-04 | Device Software Factory (DSF) | Source repositories (SaaS), CI/CD build farm (on-premises build cluster at DC-1 and cloud runners on Cloud provider B), code-signing service on hardware security modules (HSMs) at DC-1 and DC-2, artifact repository, SBOM service. **Legacy IV-300 1.x firmware is still signed on a standalone offline signing workstation outside the HSM service** (EV-043) |
| SYS-05 | Product lifecycle management (PLM) and electronic quality management system (eQMS), both SaaS | Design history files, risk management files, release approvals; complaints, CAPA, MDR and correction/removal records |
| SYS-06 | Manufacturing execution systems (MES) and plant OT at FL-1, MN-1, TX-1 | About 420 test and programming stations load signed firmware and device identity certificates from the manufacturing PKI. FL-1 and TX-1 OT networks are segmented; **MN-1 is flat with its office network, runs MES servers on an unsupported OS, and uses shared operator logins on a legacy directory** (EV-034, EV-036, EV-029) |
| SYS-07 | Enterprise resource planning (ERP) | SOX-relevant; orders, UDI and serial-number traceability for corrections and removals |
| SYS-08 | Identity platform (SSO, MFA, privileged access management, identity governance) | All workforce except the MN-1 legacy directory (about 900 users) (EV-025, EV-029) |
| SYS-09 | Enterprise estate | About 16,000 endpoints; SD-WAN to all sites; DC-1 and DC-2; Cloud providers A and B; about 700 applications |
| SYS-10 | Third parties | About 2,400 suppliers; about 180 software and cloud vendors with company data; 62 subcontractors handle PHI; 2 contract manufacturers (CMO-1 and CMO-2) build subassemblies; third-party firmware modules (wireless, battery management) (EV-066, EV-068) |
| SYS-11 | Fielded device fleet | VM-700, VM-500, DG-10, IV-300, CR-100 (with the phone gateway app), US-20, HB-40 (see section 1) |
| SYS-12 | AI portfolio | 11 use cases; AI governance committee formed in 2025 (EV-077) |

**SSP system (P02):** the *Device Software Factory and Manufacturing Execution System (DSF-MES)*: the code-to-release pipeline in SYS-04 (source repositories, CI/CD build farm, HSM code-signing service, artifact repository, SBOM service), the PLM release records in SYS-05, and the MES servers and firmware and key-provisioning stations in SYS-06 at FL-1, MN-1, and TX-1; the DDC update service, the eQMS, and the ERP are interconnected systems outside the boundary.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. At this size the sources are enterprise systems of record across the business units and plants, the Device Software Factory, PLM and the eQMS, prior Internal Audit and SOX workpapers, regulatory files, and board and committee records.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv), reviewed by the General Counsel's office.
- **Gaps against section 524B, the FDA regulations, the HIPAA Security Rule and the other applicable rules** are judged in the gap analysis (P03), and **whether controls work** is tested by Internal Audit in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 SSP | Device Software Factory and Manufacturing Execution System (DSF-MES), Moderate baseline with integrity supplements |
| P03 regulation | Primary: FD&C Act section 524B, with 21 CFR 803, 806, and 820 and FDA's premarket (2026-02-03) and postmarket (December 2016) cybersecurity guidance. Also: HIPAA Security Rule and breach notice as a business associate; FTC Health Breach Notification Rule for the consumer app; SEC Item 1.05 and Item 106; state breach laws (Florida worked example) |
| P04 cloud | Multi-cloud (Cloud providers A and B, vendor-agnostic) with platform, landing zone, workload, and SaaS layers and common controls; two colocation data centers |
| P05 BIA | Enterprise-wide, with quantified impact, a dependency map, and third parties |
| P07 assessment | Internal Audit, independent; 40+ controls on DSF-MES with statistical sampling; MN-1 plant testing on 2026-08-11 |
| P08 incident | Exploited vulnerability in a fielded connected device (worked example: the DG-10 hospital device gateway), with an **SEC materiality assessment and 8-K Item 1.05** step, FDA reporting, business associate notice to hospitals, and the disclosure committee |
| P09 SOC 2 | Type 2 readiness across two service lines: SL-1 DDC hospital services and SL-2 RCM service |
| P10 AI | Enterprise AI portfolio (11 use cases) with the AI governance committee, and a full assessment of AI-001 (image analysis) |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-04-20 to 2026-05-15 | Intake: evidence requests, exports from enterprise systems of record, inventories, obligations register (reviewed by the General Counsel's office); the 2026-05-16 DR exercise reports followed on 2026-05-22; intake approved 2026-05-29 |
| 2026-05-18 to 2026-06-26 | Enterprise BIA interviews |
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (evidence sampling completed 2026-08-14) |
| 2026-06-22 to 2026-07-10 | 2026 annual revision of POL-01 to POL-05 drafted from the intake evidence and early risk and gap results |
| 2026-07-13 to 2026-08-28 | Control assessment by Internal Audit (MN-1 plant testing 2026-08-11): operating tests of controls in force under the 2025 policy set; design review of the draft 2026 revisions |
| 2026-08-24 | SOC 2 readiness self-assessment completed |
| 2026-08-26 | AI governance committee portfolio review |
| 2026-09-08 | Executive risk committee approvals |
| 2026-09-10 | Results to the risk and technology committee of the board; 2026 policy revisions approved (effective 2026-10-01) |
| 2027-03 (planned) | Internal Audit follow-up: operating effectiveness of the controls the 2026 revisions and POA&M items introduced, after at least one quarter of operation |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Information Officer (CIO) | Enterprise IT; owns the enterprise platform (common control provider) |
| Chief Operating Officer (COO) | Plants, supply chain, and service; authorizing official for DSF-MES (P02) |
| Chief Medical Officer | Clinical safety; chairs the AI governance committee |
| Chief Compliance Officer | Regulatory compliance program; second line with the GRC team |
| Chief Accounting Officer | SOX program owner; disclosure committee member |
| Vice President, Manufacturing Systems | MES and plant OT at all three plants (system owner for the MES part of DSF-MES) |
| Director of Build and Release Engineering | CI/CD, artifact repository, SBOM service, and the signing service operations |
| Plant directors (FL-1, MN-1, TX-1) | Plant operations and plant OT change approval |
| Vice President, Digital Health | DDC (SL-1) service line owner |
| Vice President, Remote Monitoring Services | RCM service (SL-2) owner; monitoring centers |
| Vice President, Consumer Health | Consumer companion app and Consumer Health Platform |
| Vice President, Integration Management Office | Integration of the acquired infusion business (MN-1, IV-300) |
| Vice President, Supply Chain | Suppliers and contract manufacturers |
| Director of Identity and Access Management | Identity platform (SYS-08) |
| Director of Cloud Platform Engineering | Landing zones in both clouds (common control provider) |
| Director of Network Engineering | SD-WAN, data center, and plant network segmentation (common control provider) |
| Director of Endpoint Engineering | Workstations, EDR, and endpoint baselines (common control provider) |
| Director of OT Security | OT security team; plant OT monitoring and segmentation standards |
| Director of Third-Party Risk Management | Vendor tiering, BAAs, SOC report reviews, supplier security (in the GRC team) |
| Chief Human Resources Officer | Onboarding, terminations, and training records |
| Vice President, Facilities | Physical security of plants, R&D centers, and monitoring centers |
| Vice President, Corporate Communications | Media and customer communications during incidents |
| Vice President, Investor Relations | Investor communications; disclosure committee member |
| Vice President, Field Service | Field service and technical support; USB updates for legacy devices; update adoption outreach |
| Vice President, Regulatory Affairs | FDA submissions under the CQRO; backup for FDA reporting decisions |

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Chief Accounting Officer, CISO, VP Product Security, CQRO, Chief Privacy Officer, Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel. The VP Product Security, the CQRO, and the Chief Risk Officer joined in 2026 (EV-020).

**Service lines offered to business customers (P09).** SL-1: DDC hospital services (remote viewing, secondary alarms, EHR interfaces, drug library and firmware distribution, image archive) for about 2,300 hospitals, with an annual SOC 2 Type 2 report since 2023. SL-2: RCM service for about 5,200 practices and hospitals (no SOC 2 report yet; two large health systems require one by 2027) (EV-005, EV-013).

**Revenue by segment (fictional, used for BIA values).** Patient monitoring and gateways about $1.7 billion; infusion about $1.2 billion; RCM service about $0.9 billion; ultrasound about $0.4 billion; consumer about $0.25 billion; service contracts and DDC subscriptions about $0.35 billion. About 16,000 patients are on RCM monitoring at any time (EV-001, EV-056).

**Acquired infusion business.** Acquired 2024-03. It brought MN-1, the IV-300 product line, about 900 workforce members on a legacy directory (EV-029), and 5 PHI subcontractors whose contracts are still being replaced (EV-068). Integration is due 2027-06-30.
