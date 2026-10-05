# SOC 2 Readiness Summary: Cris Santos Company Holdings | Construction | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Construction |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criteria are listed by ID with short topic labels in the author's own words |
| Scoping | Per division (section 1). Two readiness reports: the TSSI managed service in Construction (`soc2-readiness.csv`) and the A&E digital twin facility data service (`soc2-readiness-digital-twin.csv`). Construction general contracting and Property leasing are out of scope |
| Categories in scope | Security, Availability, and Confidentiality for both services |
| Target reports | Both services: Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 |
| Prepared | 2026-09-15 by the Group Chief Risk Officer's assurance team with the Systems Integration Director and the A&E digital services director, using P02, P06, and P07 evidence |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service as part of their own control environment. The question for each division is whether it provides a service that other organizations build their own controls on.

| Division | Service line | Service organization? | Decision | Report |
|---|---|---|---|---|
| Construction | **TSSI managed service**: remote monitoring and maintenance of video, access control, and BAS for 140 clients | **Yes.** Clients (hospitals, universities, offices, 11 federal sites) rely on TSSI's remote access and credential controls to protect their own facilities, and they ask for a SOC 2 Type 2 report | **In scope.** First readiness assessment | Type 1, then Type 2 |
| Construction | General contracting, construction management, design-build | **No.** Owners buy construction services under contracts. They do not run their own controls on Construction's systems; owner portal users are covered by contract terms and the PDPP vendor's own report | **Out of scope** (reasons below) | n/a |
| Construction | TSSI installation and commissioning | No. Installed systems are handed over to the client, who operates them | Out of scope | n/a |
| A&E | **Digital twin facility data service** for 52 owner clients, hosted on the group cloud | **Yes.** Clients rely on it for facility operations and ask for a SOC 2 report | **In scope.** First readiness assessment | Type 1, then Type 2 |
| A&E | Architecture and engineering design services | No. Professional services, not an outsourced system | Out of scope | n/a |
| Property | Commercial leasing and building operations | **No.** Tenants lease space; they do not rely on Property systems as part of their own control environment | **Out of scope** (reasons below) | n/a |
| Property | Parking card payments | Not a SOC 2 matter. The parking technology service provider gives Property a PCI DSS attestation of compliance, and Property's own PCI DSS duties are in P03 | Out of scope | n/a |

**Why Construction general contracting is out of scope:**
1. **No user entities in the SOC 2 sense.** Owners pay for a building, not for an outsourced system. Owner and subcontractor users of the PDPP rely on the project management SaaS vendor's own SOC 2 report and the group's complementary controls, which P07 tested (SA-9).
2. **Federal customers use a different assurance path.** For FAR and DFARS contracts, the assurance is the CMMC status in SPRS and the affirmations (P03), not a SOC 2 report. A SOC 2 report would not satisfy DFARS 252.204-7021.
3. **Owner questionnaires** are answered with the group security program description and the P03 and P07 results.
4. **Revisit trigger:** if Construction starts operating systems for owners after handover (for example, hosting a client's building management system), assess whether that service line needs a SOC 2 report.

**Why Property leasing is out of scope:** tenants buy space and services in a building, not an outsourced system. Federal tenants rely on lease security terms (P03 PRP-G16), and commercial tenants on lease terms. **Revisit trigger:** if Property sells managed building technology services to tenants (for example, tenant access control as a service), assess that service line.

**Other assurance options considered.** The vertical overlay names no standard assurance mechanism for construction other than federal CMMC statuses. Two federal TSSI clients asked for the group's Section 889 procedures; these are given directly (POL-01 4.14 and the approved-manufacturer list), not through SOC 2.

**Group services carved in.** Both reports carve in group identity (SYS-G1), the SOC (SYS-G2), and the group cloud and network (SYS-G3) as internal shared services. Cloud providers are carved out as subservice organizations.

## 2. System descriptions (scope)
### 2.1 TSSI managed service (Construction)
- **Services:** remote monitoring, alarm response support, firmware and configuration maintenance, and user administration for client video, access control, and BAS installations.
- **Infrastructure and software:** the remote access platform (SYS-D2) in the group cloud on provider A; the configuration repository; the client credential vault; group identity and SOC carved in.
- **Subservice organizations (carve-out):** cloud provider A; the remote access platform vendor.
- **People:** about 160 TSSI service technicians and engineers, the Systems Integration Director, and group SOC and identity teams.
- **Data:** client facility security details (device layouts, configurations, credentials). No CUI is allowed in the service; federal-site details that are CUI stay in the enclave.
- **Complementary user entity controls:** clients approve work orders, manage their own end users and badge holders, and tell TSSI about staff changes on their side.

### 2.2 A&E digital twin facility data service
- **Services:** hosting of building information models and facility data (equipment, maintenance, space) for 52 owner clients after handover.
- **Infrastructure and software:** a tenant-per-client application in the group cloud on provider A; group identity and SOC carved in.
- **Subservice organizations (carve-out):** cloud provider A.
- **Data:** client facility data, classified Confidential. **No CUI is allowed in the service.**
- **Complementary user entity controls:** clients manage and review their own users and decide what data to upload.

## 3. Readiness results
### 3.1 TSSI managed service (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 26 | 6 | 1 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC2.3 (no system description and no standard written commitments across 140 different service agreements) and A1.3 (the remote access platform's recovery has never been tested).
**Partially ready:** CC6.1, CC6.2, CC6.3 (the client credential vault is not partitioned, credential release is not tied to work orders, and shared client accounts are not changed when technicians leave; P07 IA-5 findings, POAM-032), CC7.2 (session logs not in the SIEM), CC8.1 (12 of 40 sampled configuration changes without a work order), CC9.2 (platform vendor not reviewed; private-label devices not traced, POAM-018), C1.1 (repository not restricted per client), and C1.2 (no offboarding procedure).

**Why so many Ready criteria for a first-time report:** control environment, risk assessment, monitoring, network, malware, and incident response criteria are met by group common controls that P07 assessed once (126 of 136 common statements satisfied). The gaps are specific to how TSSI handles client credentials and changes, which is also the High risk CON-015 in P01.

### 3.2 A&E digital twin service (`soc2-readiness-digital-twin.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 29 | 4 | 0 | 0 |
| Availability (A1, 3) | 1 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Partially ready:** CC2.3 (the service description promises backups that do not cover system documentation, P03 AE-G19, POAM-027), CC6.3 (client user reviews not described as a complementary user entity control), CC8.1 (tenant isolation tests not in every release, P01 AE-008), CC9.2 (provider A's complementary controls not mapped), A1.2 (system documentation not backed up), A1.3 (no full recovery test against the 99.5% commitment), and C1.1 (12 of 52 client agreements not mapped; no check that CUI is never uploaded).

The digital twin service is closer to ready than TSSI because it was built in 2025 on the group cloud with group logging and identity from the start. Its gaps are mostly documentation and testing.

## 4. Remediation plan and evidence calendar
| Quarter | Service | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | TSSI | CC6.1, CC9.2 | Per-client vault partitions; parent-manufacturer check records; platform vendor report review |
| 2026 Q4 | Digital twin | CC2.3, A1.2 | Corrected service description; backups including system documentation |
| 2027 Q1 | TSSI | CC2.3, CC6.2, CC6.3, CC7.2, CC8.1, A1.3, C1.1, C1.2 | System description and standard commitments; work-order-linked credential release; rotation records; SIEM alerts for sessions; platform recovery test; repository permissions; offboarding procedure |
| 2027 Q1 | Digital twin | CC6.3, CC8.1, CC9.2, A1.3, C1.1 | Complementary user entity controls in the description; isolation tests in releases; provider control mapping; full recovery test; mapped client agreements and CUI upload scan |
| 2027-03-31 | Both | All in-scope criteria | Type 1 reports as of 2027-03-31 |
| 2027 Q2 to Q3 | Both | All in-scope criteria | Operating evidence for the first Type 2 period (2027-04-01 to 2027-09-30) |

**Communication:** the Systems Integration Director sends the 140 TSSI clients a readiness letter with the 2027 timeline and the Section 889 procedures for the federal clients that asked. The A&E digital services director sends the 52 digital twin clients the corrected service description and the same timeline.
