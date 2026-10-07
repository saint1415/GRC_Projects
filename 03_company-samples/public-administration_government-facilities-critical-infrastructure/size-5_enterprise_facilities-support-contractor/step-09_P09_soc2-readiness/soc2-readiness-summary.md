# SOC 2 Readiness Summary: Cris Santos Company | Government Services and Facilities | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded facilities support contractor operating government buildings) |
| Tier / Vertical | Enterprise / Government Services and Facilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 Managed Building Operations and Security (ROC monitoring, PACS administration, BAS supervision, and video management on the IBOP for 64 state, local, and education customers); SL-2 Facility Services Portal (work order and service request SaaS for about 180 customer organizations) |
| Categories in scope | SL-1: all five categories (Security, Availability, Confidentiality, Processing Integrity, Privacy). SL-2: Security, Availability, Confidentiality, and (new) Processing Integrity |
| Target reports | SL-1: first Type 2, period 2027-07-01 to 2027-12-31. SL-2: third annual Type 2, period 2027-01-01 to 2027-12-31 (Security, Availability, Confidentiality); Processing Integrity added from the 2028 period |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-28 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's revenue is facility operations, which SOC 2 does not describe. Two service lines are different: **the company operates systems that its customers' own security depends on**, so it is a service organization for them, and customers ask for a CPA's report.
- **SL-1 Managed Building Operations and Security.** The company runs its customers' access control administration, alarm monitoring, building automation supervision, and video management on its own platform (the IBOP) and holds about 585,000 cardholder records for them. Three state customers and the nine universities have asked for a SOC 2 Type 2 report. The universities asked for **Privacy** because the company holds student cardholder records and runs face verification pilots; two state customers asked for **Processing Integrity** because badge revocations and door schedule changes must be applied completely, accurately, and on time.
- **SL-2 Facility Services Portal.** Customers submit service requests and track work orders in the FSP. It has had a SOC 2 Type 2 report (Security, Availability, Confidentiality) since 2025; the 2025 report had one exception (a late access removal), since remediated. Customers now compute contract performance deductions from FSP timestamps, so they ask for **Processing Integrity**.

**Alternatives considered:**
- **GovRAMP:** two state customers' procurement policies require GovRAMP verification for the FSP (P03 G-223; POAM-022). GovRAMP verifies cloud services to state and local governments; it complements SOC 2 for those two customers but does not replace it for the others, and it does not cover the ROC operations in SL-1.
- **The state exhibits' annual independent assessment:** the P07 Internal Audit assessment meets the exhibits for 2026. A SOC 2 report can be mapped to the same SP 800-53 controls, so one external audit can serve both in later years.
- **FedRAMP:** not applicable. The company provides no cloud service to federal agencies; GSA's building systems run under GSA's own authorization.
- **CMMC:** not applicable. The company has no DoD contracts.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the state assessments, and SOX. The cloud providers, the PACS and BAS software vendors, and the colocation providers are subservice organizations presented with the carve-out method; their own SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 Managed Building Operations and Security | SL-2 Facility Services Portal |
|---|---|---|
| Services | 24x7 alarm monitoring and dispatch; badge enrollment and revocation; door schedules; BAS supervision; video management and exports | Service requests, work orders, asset records, SLA reporting |
| Infrastructure | IBOP on Cloud provider A (two regions); OT remote access gateway; about 1,480 site edge gateways; 3 ROCs (P02, P04) | Cloud provider B managed containers and database, second-region standby, landing zone controls (P04) |
| Software | Commercial PACS, video, alarm, and BAS supervisory software (company-hosted); company-built customer console and integrations | Company-built multi-tenant application and APIs |
| People | 210 ROC operators; controls and security technicians; IBOP engineers; SOC and OT security teams | FSP product and engineering team; SOC; segment dispatchers |
| Data | Cardholder records, access history, face templates (pilots), video, door schedules, controller programs, security layouts | Work orders, asset data, requester contact details, SLA timestamps |
| Procedures | P06 policy hierarchy; PRC-02.5 badge procedure; PRC-03.4 manual-mode procedures; P08 runbook | P06; P08; FSP support procedures |
| Excluded | Customer-owned field devices and site networks (customer responsibility); GSA systems at federal buildings; AQ-2 legacy BAS instances until migrated | Federal Facilities segment internal use (no federal customer users) |
| Subservice organizations (carved out) | Cloud provider A; PACS, video, and BAS software vendors (remote support); colocation providers | Cloud provider B; messaging and notification service |

## 3. Readiness results
**SL-1 Managed Building Operations and Security**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 22 | 9 | 2 | 0 |
| Availability (A1, 3) | 1 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | 12 | 6 | 0 | 0 |

**SL-2 Facility Services Portal**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 32 | 1 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 2 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is not yet ready for a Type 2 period to start. Not ready: CC6.1 and CC6.6, both driven by AQ-1's legacy remote-support tool and flat customer networks (the same gaps behind P01 R-001 and R-002). Partially ready: CC2.3, CC6.2, CC6.3, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC9.2, A1.2, A1.3, C1.2, PI1.4, PI1.5, P1.1, P2.1, P3.2, P4.2, P4.3, P6.4. These are the weaknesses Internal Audit found in the IBOP (P07) plus the face verification consent gaps from P10. Closing POAM-001, POAM-002, POAM-003, POAM-007, POAM-014, POAM-017, and POAM-021 by 2027-01-31 and the 2027 Q1 items makes SL-1 ready for a Type 1 readiness check in April 2027. Items that close on 2027-06-30 (POAM-005 OT sensors, POAM-016 unsupported workstations, POAM-018 segmentation, POAM-025 ROC absorption) set the start of the Type 2 period at 2027-07-01.

**SL-2** is ready for its next Type 2 on Security, Availability, and Confidentiality. CC6.3 is partially ready only until AQ-1 identities are federated (POAM-002, 2026-12-15). Processing Integrity is not ready to be audited for 2027: timestamp edits need a second approval and a monthly reconciliation (PI1.2, PI1.3, PI1.4; P01 R-016), due 2027-03-31, so it is added from the 2028 period.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC2.3, CC6.2, CC6.3, CC7.1, CC7.4, P1.1, P2.1, P3.2; SL-2 CC6.3 | Notice matrix for AQ contracts; console account clean-up and attestations; AQ-1 federation; credential sweep; AQ incidents to the SOC; face verification notices and consent | Attestations; federation records; sweep reports; consent forms |
| 2027 Q1 | SL-1 CC6.1, CC7.5, CC9.2, A1.3, C1.2, PI1.4, PI1.5, P4.2, P4.3, P6.4; SL-2 PI1.2, PI1.3, PI1.4 | AQ-1 tool removed (2027-01-31); PACS failover retest; subcontract addenda; retention jobs; AQ-2 migration and repository import; FSP timestamp approvals and reconciliation | Gateway session samples; retest report; retention reports; reconciliation reports |
| 2027 Q2 (April) | Readiness check by Internal Audit and a mock walkthrough with the service auditor (SL-1 Type 1 style review) | Walkthrough of every criterion | Walkthrough results |
| 2027 Q2 | SL-1 CC6.6, CC6.8, CC7.2, A1.2 | OT sensors at 95% of buildings; segmentation of the 214 flat-network buildings; unsupported workstations replaced or isolated; ROC 24-hour absorption | Sensor coverage; segmentation records; exercise report |
| 2027-07-01 | SL-1 Type 2 period starts (6 months) | Evidence collection per `soc2-evidence-map.csv` | All SL-1 items |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 11 collecting, 6 ready, 8 not started (each tied to a POA&M item or a 2027 action).

**Customer communication:** SL-2 customers receive the 2025 report, a bridge letter, and a Processing Integrity roadmap letter. SL-1 customers receive this summary, the P07 conclusion, and the expected SL-1 report date (2028-02). The two state customers that require GovRAMP also receive the GovRAMP status for the FSP (POAM-022).
