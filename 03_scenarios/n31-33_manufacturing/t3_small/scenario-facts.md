# Scenario facts: Cris Santos Company | Manufacturing | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a statute, regulation, or FDA guidance, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (connected medical device manufacturer) |
| Business | Designs, builds, and services a wireless patient-monitoring device (NAICS 334510, Electromedical and Electrotherapeutic Apparatus Manufacturing), and runs a companion **device cloud** service for hospital customers |
| Location | Florida. One facility: offices, the engineering lab, and a factory floor with three production lines (Line 1 board test, Line 2 final assembly and final test, Line 3 service and refurbishment) |
| Workforce | 250 employees: 72 engineering (34 device firmware and software, 14 cloud and DevOps, 12 hardware, 12 verification and test), 98 manufacturing operations, 18 quality and regulatory, 22 customer support and field service, 16 sales and marketing, 24 general and administrative (finance, HR, IT, legal) |
| Revenue | $58 million a year (fictional). The SBA size standard for NAICS 334510 is 1,250 employees (13 CFR 121.201), so the company is SBA-small |
| Products | **PM-2** wireless patient monitor (current model; class II; 510(k) submitted in 2024, after section 524B took effect, and cleared; about 6,800 units in the field). **PM-1** (legacy model; cleared in 2019, before section 524B; sales ended in 2024; supported until 2028; about 2,100 units in the field). **AI-001 skin-image analysis function** (in development; marketing submission planned for 2027 Q3; see P10) |
| Device cloud | Multi-tenant service on a public cloud (vendor-agnostic). Receives telemetry from fielded monitors, gives clinicians remote viewing and secondary alarm notifications, sends results to hospital EHRs, and distributes signed PM-2 firmware updates. Primary alarms always sound at the bedside monitor |
| Customers | 40 hospitals, all in Florida. Each has a business associate agreement (BAA) with the company |
| HIPAA status | **Business associate for the device cloud only.** The device cloud creates, receives, maintains, and transmits PHI on behalf of the hospitals (45 CFR 160.103), so the HIPAA Security Rule applies to it (45 CFR 164.302) and breach notice to hospitals follows 45 CFR 164.410. The company is not a covered entity. HIPAA analysis is limited to the device cloud service |
| PHI in the device cloud | Patient name, medical record number, date of birth, bed location, vital-sign trends, and alarm history for about 380,000 patients (24-month rolling retention set by the BAAs) |
| FDA status | Registered device manufacturer. Quality management system operated under the QMSR (21 CFR Part 820, which incorporates ISO 13485 by reference; effective 2026-02-02). Section 524B of the FD&C Act (21 U.S.C. 360n-2) applies to every premarket submission for a cyber device made on or after 2023-03-29 |
| Not in scope | DFARS 252.204-7012, CMMC, ITAR (N31-33-R01 to R03): the company holds no defense contracts and makes no defense articles. EAR (N31-33-R04): the company sells only to U.S. customers; export classification is outside these samples. SEC disclosure rules: privately held. FAR 52.204-25: no federal contracts. CIRCIA: proposed rule only (not in effect) |
| Regulatory driver IDs | N31-33-R05 (FD&C Act 524B) is the primary driver. For the device cloud's HIPAA scope, this folder cites the Health Care vertical's verified IDs: **N62-R01** (HIPAA Security Rule) and **N62-R03** (Breach Notification Rule). FDA regulations are cited directly (21 CFR 803, 806, 820) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: the third-party agent notice duty in Fla. Stat. 501.171(6). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security, product security, and compliance duties |
|---|---|
| Majority owner and Chief Executive Officer (CEO) | Approves the security budget; accepts High and Very High risks |
| Chief Operating Officer (COO) | Executive owner of the security program; accepts Moderate risks; signs policies |
| VP Quality and Regulatory Affairs (VP QA/RA) | FDA submissions and correspondence; complaint handling; medical device reporting (21 CFR 803); corrections and removals (21 CFR 806); owns section 524B compliance |
| VP Engineering | Device and cloud engineering; secure product development; SBOM; code signing; AI-001 development |
| IT Manager | Security Officer for corporate IT and designated HIPAA security official for the device cloud (45 CFR 164.308(a)(2)). Part-time security and compliance duties; runs the identity provider, endpoints, and networks |
| Product Security Lead | Senior firmware engineer with half-time product security duties: threat models, vulnerability monitoring, coordinated vulnerability disclosure (CVD) intake |
| Cloud Operations Lead | Runs device cloud production, backups, and monitoring |
| Director of Manufacturing Operations | Owns MES, test stations, and the production lines |
| Compliance Manager (Privacy Officer) | BAAs, HIPAA privacy duties, breach risk assessments; reports to the VP QA/RA |
| Customer Support Manager | Hospital customer communications; complaint intake |
| HR Manager | Onboarding, transfers, terminations |
| Clinical Affairs Manager (registered nurse) | Clinical input to risk management; AI-001 clinical validation |
| Contracted physician medical advisor | Clinical oversight of AI-001 |

## 3. Systems

| ID | System | Hosting | Holds PHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Device cloud service (DCS) | Public cloud tenant (IaaS/PaaS), vendor-agnostic | Yes | Device ingestion gateway, container platform (ingestion, processing, clinician portal, HL7 interface, update service), managed database, object storage, key management, logging |
| SYS-02 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects email, PLM, source repository, ERP, eQMS, VPN, and the cloud console. **MES stations are not integrated** |
| SYS-03 | Product lifecycle management (PLM) | SaaS | No | Design history files, requirements, risk management files |
| SYS-04 | Source code repository and CI/CD build pipeline | Repository: SaaS. Build server: on premises (engineering server room) | No | The **firmware code-signing private key is a file on the build server; no HSM** |
| SYS-05 | Manufacturing execution system (MES) and test stations (OT) | On premises, factory floor | No | MES server and 14 test stations (Line 1: 5, Line 2: 5, Line 3: 4). Test stations load signed firmware and device identity certificates. **Line 2 shares a flat network with the office** |
| SYS-06 | Enterprise resource planning (ERP) | SaaS | No | Orders, shipping, UDI and serial-number traceability |
| SYS-07 | Electronic quality management system (eQMS) | SaaS | Incidental | Complaints, CAPA, MDR and correction/removal records. Hospital complaints sometimes include patient identifiers |
| SYS-08 | Engineering and office endpoints | On premises and remote | Incidental (support staff) | 205 laptops and 30 desktops with EDR and full-disk encryption |
| SYS-09 | Productivity suite (email, files, chat) | SaaS | Incidental | |
| SYS-10 | Log analytics service | SaaS | Yes | Receives device cloud application logs, which contain patient names and MRNs. **No subcontractor BAA** |
| SYS-11 | Fielded devices | At hospital customers | Yes (local 72-hour trend buffer, under hospital control) | PM-2 uses per-device certificates (mutual TLS) and signed firmware with secure boot. PM-1 uses a per-hospital shared API key, checksum-only firmware checks, and field-service USB updates |
| SYS-12 | Customer support ticketing | SaaS | Incidental | Subcontractor BAA in place |

**SSP system (P02):** the *Device Cloud Service (DCS)*: SYS-01 and the components that administer it (the SYS-02 identity provider tenant, the SYS-10 log analytics service, and the support and DevOps endpoints in SYS-08), plus its interfaces to fielded devices (SYS-11) and hospital EHRs; the build and signing pipeline (SYS-04) is an interconnected system outside the boundary.

## 4. Current security posture: partially compliant

**In place today:**
- An ISO 13485-based quality management system under the QMSR, with design controls and risk management
- The PM-2 510(k) included cybersecurity documentation: a threat model, a security risk assessment, a third-party penetration test (2023), a manually generated SBOM, and a postmarket cybersecurity management plan section
- Signed PM-2 firmware, verified at boot and before any update is installed
- MFA through the identity provider for every workforce system except MES stations
- EDR and full-disk encryption on all laptops and desktops
- Device cloud: TLS 1.2 or higher on every external interface; mutual TLS with per-device certificates for PM-2; provider-managed encryption at rest; tenant separation enforced in the application and database
- Dependency and container image scanning in the CI pipeline for cloud code; monthly authenticated vulnerability scans of cloud workloads
- Daily database backups with point-in-time recovery, copied to a second region
- BAAs with all 40 hospitals; subcontractor BAAs with the cloud provider and the support ticketing vendor
- A SOC 2 Type 1 report (Security category) for the device cloud, as of 2026-03-31
- Annual security awareness training; same-day account disablement at termination
- Complaint handling, MDR, and correction and removal procedures in the eQMS (not written with cybersecurity in mind)
- A security@ mailbox listed on the company website

**Missing or weak, found in the 2026 assessments:**
1. The SBOM was generated manually, for PM-2 only (June 2024), and has not been updated for the three firmware releases since. PM-1 and the device cloud have no SBOM. Support level and end-of-support dates are not recorded.
2. No formal coordinated vulnerability disclosure policy: nothing is published, there is no intake time commitment, the security@ mailbox is checked ad hoc, there is no ISAO membership, and there is no customer advisory template.
3. No continuous monitoring of device software components against vulnerability sources, including CISA's Known Exploited Vulnerabilities (KEV) catalog.
4. No defined regular patch cycle for fielded devices and no out-of-cycle procedure. The last PM-2 firmware release was 11 months ago. Field update adoption is not measured.
5. The firmware code-signing private key is a password-protected file on the build server, with no HSM. Six build engineers have administrator rights on that server, and signing needs no second approval.
6. The Line 2 MES and test-station network is flat with the office network (Lines 1 and 3 are segmented).
7. MES and test stations use shared operator logins and no MFA. MFA is otherwise universal.
8. The device cloud has a SOC 2 Type 1 report (Security) only. Hospital customers now ask for Type 2 with Availability and Confidentiality.
9. The incident response plan covers corporate IT only. There is no product security incident procedure linking vulnerability handling to complaint handling, MDR, corrections and removals, customer advisories, and HIPAA business associate notice.
10. Device cloud audit and application logs are kept 30 days and nobody reviews them.
11. The log analytics service (SYS-10) receives logs with patient names and MRNs but has no subcontractor BAA.
12. Fourteen cloud support and DevOps engineers have standing production access to every tenant's PHI. There is no quarterly access review.
13. PM-1 authenticates to the device cloud with a per-hospital shared API key, and its embedded operating system component reaches end of support in June 2027.
14. The device cloud has never had an independent penetration test. The 2023 PM-2 test predates the current firmware.
15. No restore or failover test of the device cloud has ever been run.
16. The PM-2 threat model and security risk assessment have not been updated since clearance. The device cloud threat model is incomplete.
17. The customer security guide and manufacturer disclosure statement were last updated in 2024 and do not list end-of-support dates.
18. No AI governance: no approved AI tools list, some engineers paste proprietary code into public generative AI assistants, and AI-001 has no documented bias testing plan.
19. The PM-2 maintenance web interface accepts one service password that is the same on every unit (found during P07 testing on 2026-08-12).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P02 SSP | Device Cloud Service (DCS) |
| P03 regulation | Primary: FD&C Act section 524B, with the FDA regulations and guidance that implement it (21 CFR 803, 806, 820; FDA premarket cybersecurity guidance issued 2026-02-03; FDA postmarket cybersecurity guidance, December 2016). Secondary: HIPAA Security Rule for the device cloud as a business associate |
| P04 cloud | The device cloud on a public cloud tenant plus the SaaS services that support it. Vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |
| P08 incident | Exploited vulnerability in a fielded PM-2 monitor, with coordinated disclosure, hospital and FDA communications, and HIPAA business associate duties if PHI in the device cloud is affected |
| P09 SOC 2 | (a) SOC 2 Type 2 readiness for the device cloud (Security, Availability, Confidentiality), requested by hospital customers; (b) review of the cloud provider's SOC 2 Type 2 report (subservice organization) |
| P10 AI | AI-001 skin-image analysis function (in development); AI-002 generative AI coding assistants used by engineers |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork |
| 2026-08-10 to 2026-08-14 | Control assessment fieldwork (PM-2 lab testing on 2026-08-12) |
| 2026-08-24 | SOC 2 readiness self-assessment completed |
| 2026-08-26 | AI risk assessment completed |
| 2026-09-04 | Deliverables approved by the COO (Moderate and below) and the CEO (High) |
