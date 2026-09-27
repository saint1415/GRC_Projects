# Scenario facts: Cris Santos Company | Manufacturing | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute or regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; diversified industrial group) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate wholly owned subsidiary |
| Division 1: Medical Devices (NAICS 334510), **focus of this scenario** | Designs, manufactures, and services connected electromedical devices: infusion systems, patient monitors, and point-of-care ultrasound. Runs a device cloud for hospital customers. About 24,000 employees. A registered device manufacturer under FDA's QMSR (21 CFR Part 820) |
| Division 2: Medical Supply Distribution (NAICS 423450, sector 42 Wholesale Trade) | Distributes medical and surgical supplies and equipment from about 1,500 suppliers (including Division 1) to about 21,000 customer sites. About 13,000 employees. A **device distributor** under 21 CFR 803.3, and an **initial importer** for product lines of 6 foreign manufacturers. Holds federal contracts with the Department of Veterans Affairs and the Department of Defense |
| Division 3: Engineering and Product Testing Services (NAICS 541380, sector 54 Professional, Scientific, and Technical Services) | Independent testing laboratories for device makers: electrical safety, electromagnetic compatibility, wireless coexistence, software verification, and cybersecurity testing (penetration testing and fuzzing). About 3,500 employees in 9 laboratories. About 950 client companies, many of them competitors of Division 1 |
| Corporate shared services | Identity, network, cloud platform, security operations, finance, HR, legal, trade compliance, internal audit. About 4,500 employees |
| Location | Headquartered in Florida. Medical Devices: 5 plants (2 in Florida, 3 in other states). Distribution: 24 distribution centers in 16 states. Testing: 9 laboratories in 6 states. Devices are installed at hospitals in all 50 states. **State law handled generically**, with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| SEC status | Publicly traded. Form 8-K Item 1.05 and Regulation S-K Item 106 (17 CFR 229.106) apply at group level |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber and product security risk oversight; accepts Very High risks |
| Board audit committee | Oversees group internal audit and SEC disclosure controls |
| Group CISO | Group security program, group policies, common controls (SYS-G1 to SYS-G3); co-accepts High risks |
| Group Chief Risk Officer | Group risk register and ERM roll-up (NIST IR 8286 Rev. 1); chairs the Group AI council; co-accepts High risks |
| Group Chief Privacy Officer | Privacy program, data classification, HIPAA business associate oversight |
| Group General Counsel | Contracts (BAAs, NDAs, federal contracts), notification matrix, SEC counsel liaison |
| Group trade compliance director | Export controls (EAR) and restricted-party screening for all divisions |
| Division presidents (3) | Accept Moderate risks for their divisions |
| Division security and compliance leads (3) | Division supplements and registers; accept Low risks |
| Medical Devices: VP Quality and Regulatory Affairs (VP QA/RA) | FDA submissions, complaint handling (21 CFR 820.35), medical device reporting (21 CFR 803), corrections and removals (21 CFR 806); owns section 524B compliance |
| Medical Devices: Chief Product Security Officer (CPSO) | Product security incident response team (PSIRT, 14 staff), coordinated vulnerability disclosure (CVD), SBOM program, ISAO liaison |
| Medical Devices: VP Engineering; VP Manufacturing Operations; device cloud operations director | Device and cloud engineering and build pipeline; plants, MES, and test stations; device cloud operations |
| Medical Devices: HIPAA security official and privacy officer for the device cloud | Designated in writing for the device cloud's business associate duties (45 CFR 164.308(a)(2)) |
| Distribution: VP Quality and Regulatory (distribution) | Device complaint files (21 CFR 803.18(d)), importer reports (803.40), recall and hold execution |
| Distribution: federal contracts compliance director | FAR and DFARS clause compliance, CMMC status, contracting officer notices |
| Testing: laboratory quality director | Laboratory accreditation, client confidentiality, test report integrity |
| Testing: cybersecurity testing practice lead | Penetration testing and fuzzing services; the findings vault |
| Group internal audit | Independent assessor. Reports to the board audit committee. Assesses common controls once; samples division controls |
| Disclosure committee | SEC materiality decisions |

## 3. Systems
| ID | System | Owner |
|---|---|---|
| SYS-G1 | Group identity platform (SSO, MFA, PAM, identity governance) | Corporate |
| SYS-G2 | Group SOC, SIEM, and EDR | Corporate |
| SYS-G3 | Group cloud platform (provider A primary; provider B for disaster recovery and the immutable backup vault), wide-area network, and a group colocation data center | Corporate |
| SYS-G4 | Group ERP, procurement, and HR and payroll services (SaaS) | Corporate |
| SYS-D1 | Device Engineering and Manufacturing System (DEMS): product lifecycle management (PLM), source repositories, CI/CD build pipeline and HSM-backed code-signing service, and the MES and production test stations at the 5 plants | Medical Devices |
| SYS-D2 | Device Connectivity Cloud (DCC): telemetry, remote viewing and secondary alarm notification, drug library and firmware distribution, hospital EHR interfaces | Medical Devices |
| SYS-D3 | Device electronic quality management system (eQMS): complaints, CAPA, MDR, and correction and removal records. Distribution keeps its device complaint files in a separate eQMS module | Medical Devices |
| SYS-D4 | Distribution order-to-cash platform: distribution ERP (colocation data center), warehouse management at 24 distribution centers, transportation management, EDI gateway, and the customer ordering portal. Holds federal order data | Distribution |
| SYS-D5 | Distribution center automation (conveyors, sortation, automated storage; operational technology) | Distribution |
| SYS-D6 | Testing laboratory information management system (LIMS), client portal, the findings vault, and laboratory test networks (including the isolated cybersecurity test range) | Testing |
| SYS-D7 | Fielded devices at customer sites (IX-4 and IX-3 infusion pumps, PM-7 monitors, US-2 ultrasound) | Medical Devices (installed at hospitals) |

**SSP system (P02):** the *Device Engineering and Manufacturing System (DEMS)*: SYS-D1, the Medical Devices division's PLM, source repositories, CI/CD build pipeline and HSM-backed code-signing service, and the MES and production test stations at its 5 plants; it inherits common controls from SYS-G1 to SYS-G3 and interconnects with the DCC update service (SYS-D2) and the eQMS (SYS-D3).

## 4. Current security posture: mature group program; maturity varies by division
**In place today:**
- Group policies aligned to CSF 2.0 (2026) with division supplements
- A common control catalog for SYS-G1 to SYS-G3
- 24x7 group SOC; EDR on IT endpoints and servers
- PAM with just-in-time elevation; quarterly access certification for IT systems
- Immutable backups for IT and cloud workloads
- SEC Item 106 disclosure in the annual report
- Medical Devices: QMSR quality system with design controls; a secure product development framework (SPDF) procedure since 2023; a PSIRT with a published CVD policy; active membership in a health sector ISAO since 2023
- Medical Devices: automated machine-readable SBOMs for IX-4, PM-7, US-2, and the DCC; HSM-backed code signing with two-person approval at Plants A to C; quarterly security maintenance releases for IX-4 and PM-7
- Medical Devices: DCC SOC 2 Type 2 report (Security, Availability) issued annually; BAAs with every hospital customer of the DCC
- Distribution: federal contract clauses accepted; device complaint files kept; importer MDR procedure
- Testing: laboratory accreditation to ISO/IEC 17025; NDAs with every client; client data separated by project in the LIMS

**Gaps:**
1. **Legacy IX-3 infusion pumps.** About 42,000 IX-3 pumps (cleared in 2018, before section 524B) remain in service. There is no SBOM for IX-3. Its embedded operating system component reaches end of support in June 2027. Security updates install only by USB through field service or hospital biomedical staff, and 58% of units run the latest security release. IX-3 firmware is still signed on a build server at Plant D with a software key outside the group HSM.
2. **OT at acquired plants.** Plants D and E (acquired in 2024) have flat networks between the MES, test stations, and office networks, shared operator logins at test stations, and no MES logs in the SIEM.
3. **Common control inheritance.** It is documented for Medical Devices but not for Distribution. Four laboratories acquired in 2025 run a local directory that is not federated to SYS-G1.
4. **Federal contract safeguarding.** Distribution has never assessed itself against the 15 FAR 52.204-21 requirements, has no CMMC Level 1 self-assessment or SPRS affirmation, and has not defined which systems hold Federal contract information. The next option on the DoD contract is due 2027-03-31.
5. **Testing information barrier.** The Testing division holds competitors' confidential design data and unpublished vulnerability findings. The barrier between Testing and Medical Devices is written in policy but not enforced technically: 212 Medical Devices engineers can reach a shared collaboration space used by Testing staff. Testing also ran Medical Devices' own premarket penetration tests without a documented independence statement.
6. **PHI in test submissions.** Client contracts prohibit PHI, but device logs submitted for testing contained patient identifiers 3 times in 2026. There is no intake scanning and no BAA framework.
7. **Shared incident notification.** A device incident can trigger FDA reports (803, 806), hospital BAA notices, Distribution's customer, recall, and federal contract duties, state breach laws, and SEC disclosure at once. The single notification matrix has not been exercised across divisions.
8. **AI governance.** A Group AI Standard was adopted in 2026-03. The AI-enabled ultrasound image analysis function (AI-001) is in development with open bias findings, and Testing uses a generative AI report drafting tool on client confidential data without client consent terms.
9. **Supplier software transparency.** For 31% of third-party software components in DEMS-built firmware, the supplier has not provided an SBOM entry or a support end date. Contract manufacturers' access to PLM has not been reviewed since 2024.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 | The Device Engineering and Manufacturing System (DEMS, SYS-D1), a division system that inherits group common controls; a group common control catalog |
| P03 | Medical Devices: FD&C Act section 524B (primary) with 21 CFR 803, 806, 820 and FDA guidance, plus the HIPAA Security Rule for the DCC as a business associate. Distribution: FAR 52.204-21 (the CMMC Level 1 requirement set) plus FDA distributor and importer duties. Testing: no binding cybersecurity rule applies, so NIST CSF 2.0 is the benchmark. Group: SEC and state breach laws. A regulation-by-division matrix |
| P08 | An exploited vulnerability in fielded IX-3 infusion pumps, touching all three divisions: a multi-regulator notification matrix and SEC materiality |
| P09 | SOC 2 scoped per division: the DCC (Medical Devices) is in scope; the Testing client portal and LIMS are in scope for a first report; Distribution is out of scope, with reasons |
| P10 | Group AI governance program: group standards, division use cases, and the regulator-specific rules; focus use case AI-001, an AI-enabled device software function (ultrasound image analysis) |
| Cloud | Shared corporate platform plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division risk analyses and regulatory gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples; DEMS plant and lab testing 2026-08-11 to 2026-08-14 |
| 2026-08-27 | Group AI council risk assessment |
| 2026-09-01 | SOC 2 readiness self-assessments completed |
| 2026-09-15 | Results to the board risk committee; deliverables approved |

## 7. Detailed facts used by the deliverables
These facts add detail to sections 1 to 6. They do not change them.

| Topic | Fact |
|---|---|
| Medical Devices products | **IX-4** infusion system (current; class II; 510(k) submitted and cleared in 2024, after section 524B took effect; about 95,000 pumps at about 1,100 hospitals; per-device certificates, signed firmware with secure boot, drug library and firmware updates through the DCC). **IX-3** infusion pump (legacy; cleared 2018; sales ended 2025; supported until 2028-12-31; about 42,000 pumps at about 700 hospitals; drug libraries loaded from an on-premises server at the hospital; embedded web server for biomedical maintenance). **PM-7** patient monitoring platform (class II; 510(k) cleared 2025; about 60,000 monitors; primary alarms always sound at the bedside). **US-2** point-of-care ultrasound (class II; cleared 2025; about 18,000 units). **AI-001** ultrasound image analysis function for US-2 (in development; marketing submission planned 2027 Q2; see P10) |
| Plants | Plant A (Florida; IX-4, PM-7), Plant B (Florida; disposables and infusion sets), Plant C (PM-7 subassemblies), Plant D (acquired 2024; IX-3 service and spare-part production), Plant E (acquired 2024; US-2). 61 MES-connected test stations in total, 19 of them at Plants D and E |
| DCC | Multi-tenant device cloud on provider A with disaster recovery on provider B. Business associate for about 1,300 hospital customers; PHI of about 9 million patients (24-month rolling retention set by BAAs). Standard BAA: breach notice within 15 calendar days of discovery and security incident reports within 5 business days; 64 health systems negotiated 5-day breach notice. SOC 2 Type 2 (Security, Availability) for the 12 months ending June 30 |
| Device cloud HIPAA status | Medical Devices is a business associate for the DCC only (45 CFR 160.103). It is not a covered entity. Fielded devices store data under the hospital's control |
| Export controls | Medical Devices exports to about 40 countries. Group trade compliance classifies items under the EAR (N31-33-R04) and screens foreign-national access to technology (deemed exports). No division makes defense articles, so ITAR (N31-33-R03) does not apply |
| Distribution federal contracts | A VA Federal Supply Schedule contract and a DoD medical-surgical distribution contract (awarded 2024-03; base period to 2027-03-31, then options). Both include FAR 52.204-21 and 52.204-25. The DoD contract includes DFARS 252.204-7012, but DoD has marked or provided no covered defense information; order, delivery, and facility data are Federal contract information. The contract covers distribution services, not only COTS items. About 380 federal facilities are served |
| Distribution FDA status | Distributor for most products (803.3); initial importer for 6 foreign manufacturers' product lines (registered under 21 CFR 807.20(a)(5)). It does not repackage or relabel devices. A 2026 private-label proposal is on hold pending regulatory review, because relabeling would make the division a manufacturer (803.3). It distributes no prescription drugs |
| Distribution scale | About 21,000 customer sites (hospitals, ambulatory surgery centers, physician offices, long-term care); about 140,000 SKUs; 24 distribution centers, 9 of them with automated sortation (SYS-D5). No direct-to-patient delivery; no PHI except incidental data on returns |
| Testing scale | 9 laboratories; 5 federated to SYS-G1 and 4 acquired in 2025 on a local directory (migration due 2027-03-31). About 950 client companies. About 11% of laboratory hours are for Medical Devices. No federal contracts and no CUI (decision confirmed by Group General Counsel on 2026-06-30). A generative AI report drafting tool was piloted from 2026-02 |
| Cloud | Provider A hosts the corporate landing zone, the DCC, and the Testing client portal. Provider B hosts the DCC disaster recovery environment and the immutable backup vault. PLM and the eQMS are SaaS. SYS-D4 distribution ERP runs in the group colocation data center; warehouse management runs at each distribution center with a central database in the colocation data center |
| Revenue split (fictional) | Medical Devices about $10.8 billion; Distribution about $6.3 billion; Testing about $0.9 billion. Total about $18.0 billion |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Patient-safety risks rated High must be treated, not accepted |
| Out of scope by fact | No division makes defense articles (ITAR) or holds covered defense information (DFARS 252.204-7012 obligations not triggered). No division is a HIPAA covered entity. No division distributes prescription drugs. CIRCIA reporting is proposed only (not in effect) |
