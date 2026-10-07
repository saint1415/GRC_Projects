# SOC 2 Readiness Summary: Cris Santos Company Holdings | Nuclear Reactors, Materials, and Waste | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Nuclear Reactors, Materials, and Waste |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division and service line (section 1). Two readiness reports: the Engineering and Radiation Services **dosimetry service** (`soc2-readiness.csv`) and the Radioactive Waste Management **waste customer portal** (`soc2-readiness-waste-portal.csv`). Nuclear Generation is out of scope |
| Categories in scope | Dosimetry service: Security, Availability, Confidentiality, Processing Integrity. Waste customer portal: Security, Availability |
| Target reports | Dosimetry service: Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30. Waste customer portal: Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| Prepared | 2026-09-17 by the Group Chief Risk Officer's assurance team with the Engineering and Radiation Services and Radioactive Waste Management security and compliance leads |

## 1. Scoping decisions per division
A SOC 2 report covers controls at a **service organization** that matter to the **user entities** relying on its service. The question for each service line is whether outside organizations rely on its controls as part of their own.

| Division | Service line | Service organization? | Decision | Categories |
|---|---|---|---|---|
| Engineering and Radiation Services | Personnel dosimetry processing and the customer portal (SYS-E3) for about 2,100 customer licensees | **Yes.** Customers rely on the service for 10 CFR 20.1501(d) processing and to hold their 20.2106 records. Three large customers asked for a SOC 2 report (scenario gap 6) | **In scope.** First readiness assessment | Security, Availability, Confidentiality, Processing Integrity |
| Engineering and Radiation Services | Engineering services; contractor/vendor access authorization program | Partly, but clients get assurance another way: licensees audit the access authorization program directly under 73.56(n), and engineering work is controlled by clients' quality assurance programs | Out of scope | n/a |
| Radioactive Waste Management | Waste customer portal (SYS-W1): manifests, shipment status, and certificates of disposal for generators | **Yes, for this service line.** Generators rely on the portal records for their own regulatory recordkeeping, and several asked for assurance in 2026 renewals | **In scope.** First readiness assessment | Security, Availability |
| Radioactive Waste Management | Waste processing, transport, and remediation | Assurance comes from Agreement State, DOT, and EPA-authorized state inspections and from DOE contract oversight | Out of scope | n/a |
| Nuclear Generation | Electricity generation and wholesale sales | **No** (reasons below) | **Out of scope** | n/a |

**Why Nuclear Generation is out of scope:**
1. **No user entities.** Wholesale buyers and grid operators buy energy and capacity. They do not rely on Nuclear Generation's systems as part of their own control environment, which is what a SOC 2 report is for.
2. **Assurance comes from regulators instead.** The NRC inspects each station's cyber security program against its approved CSP, Nuclear Oversight reviews it every 24 months (73.55(m)), and the NERC Regional Entity audits the CIP program for the fleet operations center (P03 regulation-by-division matrix).
3. **A SOC 2 system description would be a security risk.** A useful description of station systems would contain CDA, defensive architecture, and security details that the group protects as cyber security sensitive, and in part as SGI (73.22(a)). Distributing it to report users would work against the CSP.
4. **Revisit trigger:** if Nuclear Generation begins offering operating or work management services to other plant owners, assess whether a SOC 1 or SOC 2 report is needed for that service.

Nuclear Generation still benefits from this work: the group common controls that both in-scope reports carve in are the same ones the PBN-WMS inherits (P02), and the P07 results on them are shared evidence.

**Other assurance options considered.** The vertical overlay names no standard assurance alternative for these services. For the dosimetry service, NVLAP accreditation already gives customers assurance about measurement quality; it does not cover information security or availability, which is what the three customers asked about. ISO/IEC 27001 certification was considered and set aside because customer contracts and questionnaires ask for SOC 2.

## 2. System descriptions (scope)
### 2.1 Dosimetry service (Engineering and Radiation Services)
- **Services:** receipt and processing of personnel dosimeters, dose calculation and reporting, the customer portal for dose reports and records, and record hosting for customer licensees.
- **Infrastructure and software:** the laboratory information system and customer portal (SYS-E3) on cloud provider A in the group landing zone; laboratory readers and processors on the laboratory network; group identity (SYS-G1), SOC (SYS-G2), and cloud platform (SYS-G3) carved in as internal shared services.
- **Subservice organizations (carve-out):** cloud providers A and B; the customer identity service vendor.
- **People:** laboratory staff and the division's application team, plus group SOC, identity, and cloud teams.
- **Data:** dose records and personal information (names, dates of birth, identification numbers, Social Security numbers for about 61% of individuals) for about 310,000 monitored individuals; about 5,800 customer portal users.
- **Complementary user entity controls:** customers provision and remove their portal users, protect their own copies of reports, and tell the service promptly about changes in monitored individuals.

### 2.2 Waste customer portal (Radioactive Waste Management)
- **Services:** waste profiles, shipment scheduling and status, manifests and the e-Manifest interface, and certificates of disposal for generator customers.
- **Infrastructure and software:** a vendor SaaS waste tracking platform (SYS-W1) configured by the division; group identity for workforce users.
- **Subservice organizations (carve-out):** the waste tracking SaaS vendor and its hosting provider.
- **Data:** waste profiles, manifests, shipment records, and customer contacts.
- **Complementary user entity controls:** customers provision their users, review certificates on receipt, and report discrepancies.

## 3. Readiness results
### 3.1 Dosimetry service (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 27 | 5 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first report:** control environment, risk assessment, monitoring, identity, network, and SOC criteria are met by group common controls that group internal audit assessed in P07.
**Not ready:** CC2.3. There is no system description and no written statement of service commitments (turnaround, accuracy, confidentiality, incident notice).
**Partially ready:** CC6.1 (password-only customer administrators, POAM-013), CC6.6 (laboratory network not segmented), CC7.4 (72-hour customer notice and third-party agent duty not in the group matrix, POAM-011), CC7.5 (2026 restore test not yet done), CC8.1 (algorithm change validation not linked to change records), A1.3 (no recovery test against the 24-hour RTO), C1.2 (manual destruction at contract end), and PI1.3 (NVLAP evidence not mapped to processing integrity criteria).

**Why Processing Integrity is in scope.** Customers rely on the dose results themselves, not only on the service being secure and available. The NVLAP quality system already produces most of the evidence (proficiency testing, calibration, report review). The work is to map it to the criteria.

### 3.2 Waste customer portal (`soc2-readiness-waste-portal.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 25 | 6 | 2 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC2.3 (no system description or service commitments), CC4.1 (the division's inherited controls have never been assessed and there is no inheritance matrix, POAM-016), and A1.3 (rebuilding manifests and certificates from the monthly export has never been tested).
**Partially ready:** CC5.3 (2024 supplement, POAM-017), CC6.1 (customer MFA optional), CC6.2 (no review of customer administrators), CC7.4 (own severity scale; not in the group matrix), CC8.1 (configuration changes not ticketed), CC9.2 (vendor complementary controls not mapped), and A1.2 (no completeness check of the export).

The portal is less ready than the dosimetry service for the same reason the division's other results are weaker: its common control inheritance and policy alignment were never done (scenario gap 9). Fixing those also moves this report forward.

## 4. Remediation plan and evidence calendar
| Quarter | Service line | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | Dosimetry | CC6.1, CC7.4, CC7.5 | Customer administrator MFA enforced; matrix rows and customer notice procedure; 2026 restore test |
| 2026 Q4 | Waste portal | CC5.3, CC7.4 | Re-issued supplement; group severity scale adopted |
| 2027 Q1 | Dosimetry | CC2.3, CC6.6, CC8.1, A1.3, C1.2, PI1.3 | System description; laboratory segment; change linkage; recovery test; deletion certificates; NVLAP mapping. **Type 1 as of 2027-03-31** |
| 2027 Q1 | Waste portal | CC2.3, CC4.1, CC6.1, CC6.2, CC8.1, A1.2, A1.3 | System description; inheritance matrix and assessment; customer MFA; customer administrator reviews; change tickets; export check; recovery test |
| 2027 Q2 | Waste portal | CC9.2 | Vendor complementary control mapping and monitoring. **Type 1 as of 2027-06-30** |
| 2027 Q2 to Q4 | Both | All in-scope criteria | Operating evidence for the dosimetry Type 2 period (2027-04-01 to 2027-09-30) and the portal Type 2 period (2027-07-01 to 2027-12-31) |

**Communication:** the dosimetry laboratory director sends the three requesting customers a readiness letter with this timeline. The Radioactive Waste Management president tells generator customers at 2027 renewals when the first portal report will be available.
