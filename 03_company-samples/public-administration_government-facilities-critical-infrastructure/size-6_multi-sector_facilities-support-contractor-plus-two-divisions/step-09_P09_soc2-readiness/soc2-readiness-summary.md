# SOC 2 Readiness Summary: Cris Santos Company Holdings | Government Services and Facilities | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Government Services and Facilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). Two readiness reports: the Facilities Support managed building technology service (`soc2-readiness.csv`) and the Janitorial and Security remote monitoring service (`soc2-readiness-remote-monitoring.csv`). Construction and the janitorial and guard services are out of scope |
| Categories in scope | Security, Availability, and Confidentiality for both service lines |
| Target reports | Facilities Support: Type 2 for 2026-01-01 to 2026-12-31 (Type 1 issued as of 2025-12-31). Janitorial and Security: Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| Prepared | 2026-09-10 by the Group Chief Risk Officer's assurance team with the Facilities Support and Janitorial and Security security and compliance leads, using P02, P06, and P07 evidence |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it runs a system that customers rely on as part of their own controls.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Government Facilities Support | Managed building technology service: remote operation of building automation and access control from the IBOP and the ROCs for 296 state, local, and education sites | **Yes.** Customers rely on the group's platform and staff for door control, revocations, and alarm response | **In scope.** Type 1 issued; first Type 2 period under way | Security, Availability, Confidentiality | Type 2, 2026-01-01 to 2026-12-31 |
| Government Facilities Support | On-site operations and maintenance at 46 federal buildings | No. Staff operate agency systems inside agency boundaries; GSA assesses its own systems | Out of scope | n/a | n/a |
| Janitorial and Security | Remote video and alarm monitoring from the central monitoring station for 640 sites | **Yes.** 34 commercial customers and 2 county customers asked for a report in 2026 | **In scope.** First readiness assessment | Security, Availability, Confidentiality | Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| Janitorial and Security | Custodial services and security officers at customer posts | **No.** These are labor services performed under the customer's direction; customers do not build their own system controls on a division system | **Out of scope** | n/a | n/a |
| Construction and Renovation | Design-build and general contracting | **No** (reasons below) | **Out of scope** | n/a | n/a |

**Why Construction is out of scope:**
1. **No user entities.** Building owners buy a building, not an ongoing system service. They rely on contract performance, bonding, and inspections, not on Construction's information systems.
2. **Assurance comes from other programs.** DoD customers rely on DFARS 252.204-7012, SPRS assessments, and CMMC (32 CFR Part 170). Its Level 2 C3PAO assessment (POAM-020) is the assurance those customers need.
3. **Revisit trigger:** if Construction starts operating buildings after turnover (for example a commissioning-as-a-service offering on the IBOP), that work joins the Facilities Support service description.

**Why the janitorial and guard services are out of scope:** the customer directs the work at its own site, and the controls that matter (screening, training, credential return) are personnel controls that customers check through contract terms and site audits. The group answers those questions with this sample's P03 and P07 results. Customers at FTI and criminal justice buildings apply their own agency rules through the contract (IRS Pub. 1075; CJIS Security Policy).

**Other assurance options considered:**
- **GovRAMP:** one state customer requires GovRAMP verification of the IBOP by 2027-07-01. GovRAMP is built on SP 800-53, so it will reuse the SSP and P07 evidence (POAM-030). It does not replace SOC 2 for the county and education customers who ask for SOC 2.
- **FedRAMP:** not applicable. No group system operates on behalf of a federal agency.
- **CMMC:** applies to Construction only (above).

## 2. System descriptions (scope)
### 2.1 Facilities Support managed building technology service
- **Services:** 24x7 alarm monitoring and dispatch from ROC-1 and ROC-2; building automation supervision for 296 sites; access control administration for 188 sites (badges, revocations within 4 hours, door schedules).
- **Infrastructure and software:** the IBOP (P02): supervisory services and the jump service in provider A, the DR replica and backup vault in provider B, site edge gateways, ROC consoles. Group identity (SYS-G1), SOC (SYS-G2), and cloud platform (SYS-G3) are carved in as internal shared services.
- **Subservice organizations (carve-out):** cloud providers A and B; the access control SaaS vendor; the video SaaS vendor.
- **People:** about 2,400 IBOP workforce users plus integrators under subcontract.
- **Data:** cardholder records for about 212,000 people (including about 38,000 university students), door schedules and security layouts, alarm and trend data.
- **Complementary user entity controls:** customers approve badge requests, report separations of their own staff, keep security staff on site, and enable MFA for their badging users.
- **Description issue:** the 2025 Type 1 description listed the 37 acquired sites as "in transition to the jump service." For the 2026 Type 2 period the control did not operate at those sites, so management will either describe the exception or carve the sites out with disclosure. The group chose to describe it, because the affected customers already know.

### 2.2 Janitorial and Security remote monitoring service
- **Services:** video and intrusion alarm monitoring for 640 sites; guard dispatch; police notification; video analytics (AI-003).
- **Infrastructure and software:** the IBOP monitoring module (video SaaS tenants, alarm receivers, consoles at ROC-2), inherited group controls, a backup monitoring partner under contract.
- **Subservice organizations (carve-out):** the video SaaS vendor; the analytics vendor; the backup monitoring partner; cloud provider A.
- **People:** about 1,400 monitoring, installation, and branch staff, of whom about 220 work in the central monitoring station.
- **Data:** live and recorded video, alarm events, site contact lists.
- **Complementary user entity controls:** customers keep contact lists current, test their alarm panels, and control who may request video.

## 3. Readiness results
### 3.1 Facilities Support managed building technology service (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 19 | 12 | 2 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC6.1 (legacy remote access and 22 integrator accounts without MFA at the 37 acquired sites) and CC6.3 (the standing cross-tenant global administrator role). **Expect the service auditor to report exceptions for both** in the 2026 Type 2 report, because the fixes land on 2026-12-15 and 2027-03-31.
**Partially ready:** CC1.4, CC2.1, CC2.3, CC3.4, CC6.2, CC6.6, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.2, A1.3, and C1.2. They are the same gaps as the P07 findings (POAM-001 to POAM-018), seen through the TSC.

**What this means for customers.** Most of the control environment, risk, monitoring, physical, and backup criteria are Ready because group common controls carry them. The exceptions concentrate where the IBOP meets acquired sites and integrators, which is also where P01 rates the top group risk (GR-01). The Facilities Support president will brief the state and county customers before the report is issued, with the POA&M dates.

### 3.2 Janitorial and Security remote monitoring service (`soc2-readiness-remote-monitoring.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 15 | 15 | 3 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first-time report:** identity, network, encryption, scanning, and SOC criteria are met by group common controls already evidenced for the Facilities Support report.
**Not ready:** CC2.3 (no system description or written service commitments), CC5.3 (the 2022 policy set), CC7.4 (the incident response plan does not cover the service), and A1.3 (switchover never tested).
**Partially ready:** CC1.3, CC1.4, CC2.1, CC2.2, CC3.1, CC3.4, CC4.1, CC6.3, CC6.5, CC6.8, CC7.2, CC7.5, CC8.1, CC9.1, CC9.2, A1.2, C1.1, and C1.2. Most are division documentation gaps or come from the acquisition (the NVRs and installed equipment).

## 4. Remediation plan and evidence calendar
| Quarter | Service line | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | Facilities Support | CC6.1, CC6.2, CC8.1 | Jump service logs for all 37 sites; integrator accounts in identity governance; change tickets at acquired sites (POAM-001, -003, -009, -010) |
| 2026 Q4 | Both | CC2.3, CC7.4, A1.3, CC9.1 | Completed notice inventory and tabletop report (POAM-005); monitoring failover and switchover test reports (POAM-014) |
| 2026 Q4 | Janitorial and Security | CC1.3, CC2.2, CC5.3, CC6.8, CC6.3, CC7.2 | Re-issued supplement (POAM-027); NVR confirmation (POAM-022); mask approval and suppression alerts |
| 2027 Q1 | Facilities Support | CC6.3, CC6.6, CC7.1, CC7.2, CC7.5, CC2.1 | Per-customer roles (POAM-011); segmentation (POAM-013); OT monitoring and inventory (POAM-004, -006, -012, -015) |
| 2027 Q1 | Janitorial and Security | CC3.1, CC3.4, CC8.1, CC9.2, C1.1, C1.2, CC6.5 | System description draft; analytics change records and vendor review (P10 AI-003); export labeling; deletion certificates |
| 2027 Q2 | Janitorial and Security | All in-scope criteria | Type 1 as of 2027-06-30 |
| 2027 Q3 to Q4 | Both | All in-scope criteria | Operating evidence for the Facilities Support 2027 period and the monitoring service's first Type 2 period (2027-07-01 to 2027-12-31) |

**Communication:** the Janitorial and Security president sends the 36 customers who asked for a report a readiness letter with the 2027 timeline. Until then, the division answers questionnaires with the group security program description and the relevant P07 results.
