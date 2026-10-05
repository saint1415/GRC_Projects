# SOC 2 Readiness Summary: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded independent crude oil producer) |
| Tier / Vertical | Enterprise / Mining, Quarrying, and Oil and Gas Extraction |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 owner and partner services (about 68,000 royalty owners and 1,400 non-operating partners); SL-2 produced water gathering and disposal services (about 35 third-party operators in the Permian) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and (new) Processing Integrity and Privacy. SL-2: Security, Availability, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (third annual report; Processing Integrity and Privacy added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's work is producing oil, which SOC 2 does not cover. Two service lines are different: the company **provides services to outside parties**, so it is a service organization for them, and they ask for a CPA's SOC 2 report.
- **SL-1 owner and partner services.** The company pays about 68,000 royalty owners and bills about 1,400 non-operating partners every month (about $520 million a month in distributions), through the owner and partner portal, monthly statements, and direct deposit. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) since 2025, with no exceptions in the 2025 report. Institutional owners and the larger partners' auditors now ask for **Processing Integrity**, because statement and payment accuracy is the core commitment, and owner groups ask for **Privacy**, because most owners are individuals whose taxpayer and bank data the company holds.
- **SL-2 water services.** About 35 third-party operators send produced water to company gathering lines and disposal wells and are invoiced on SCADA-measured volumes through the water services portal. Several larger customers' vendor programs now require a SOC 2 Type 2 report including **Processing Integrity**, because invoices depend on SCADA meter data.

**Alternatives considered:** the vertical has no sector assurance scheme for these services. A SOC 1 report would cover only the financial reporting effect for partners, not portal security or availability; ISO/IEC 27001 certification would not give customers the control-level testing their auditors ask for. SOC 2 with the added categories answers both groups with one assessment per service line.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04) support both service lines, so one set of evidence serves both reports, the SOX program, and the Internal Audit assessment (P07). The cloud providers, the hydrocarbon accounting software vendor (support only), the print and mail vendor, and the bank are subservice organizations presented with the carve-out method; their own SOC reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 owner and partner services | SL-2 water services |
|---|---|---|
| Services | Owner and partner portal; monthly revenue and joint interest billing statements; direct deposit payments; tax forms | Produced water gathering and disposal; SCADA-measured volume tickets; water services portal; monthly invoices |
| Infrastructure | Cloud provider A: portal, hydrocarbon accounting, volume integration (landing zone controls, P04) | Enterprise SCADA platform at the IOC with BCC standby (water facilities in the Permian); Cloud provider B: water services portal |
| Software | Company-built portal; commercial hydrocarbon accounting software (customer-managed) | Enterprise SCADA platform and historian; company-built portal |
| People | Owner Relations, revenue accounting, SOC, identity and cloud platform teams | Midstream and water operations, Production Controllers, measurement technicians, SOC, OT security |
| Data | Owner and partner names, addresses, taxpayer numbers, bank details, interests, statements | Customer volumes, tickets, invoices (business data; no personal information) |
| Procedures | P06 policy hierarchy; P08 runbook; owner relations procedures | P06; P08; measurement manual; OT change board |
| Subservice organizations (carved out) | Cloud provider A; print and mail vendor; bank | Cloud provider B; primary cellular carrier |

## 3. Readiness results
**SL-1 owner and partner services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 30 | 3 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | 14 | 4 | 0 | 0 |

**SL-2 water services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 25 | 8 | 0 | 0 |
| Availability (A1, 3) | 1 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 1 | 3 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready on its existing categories except three Security items being fixed now: CC3.3, CC6.6, CC9.2. The new categories have partially ready items: PI1.2 and PI1.3 (run ticket reason codes and automated LACT reconciliation, POAM-017) and P4.2, P5.1, P6.2, P7.1 (retention of owner exports, owner data requests, disclosure logging, state of residence). All close by 2027-03-31; the items that close after the period starts on 2027-01-01 have compensating controls today and would be described in the report if still open.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: PI1.3. Partially ready: CC2.3, CC3.1, CC6.3, CC7.1, CC7.2, CC7.5, CC9.1, CC9.2, A1.2, A1.3, PI1.1, PI1.2, PI1.4. The gaps are the same ones Internal Audit found in the FSPA (P07) where they touch the water facilities: OT account certification, field device inventory, OT monitoring coverage, failover time, carrier concentration, and vendor assurance, plus the newness of the SCADA-to-ticket reconciliation. Closing POAM-001, POAM-004, and POAM-016 and the reconciliation exception workflow by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01. Items due 2027-06-30 (CC7.1, CC7.2, CC9.1, A1.2) have compensating controls (patrols, trucking fallback, SOC monitoring of the IOC) and would be described in the report if still open.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC3.3, CC6.6, PI1.2, P7.1; SL-2 CC3.1, PI1.1, PI1.4 | Bank change controls; portal bot protection; run ticket reason codes; owner data clean-up; SL-2 service objectives and measurement specification; dispute log | Bank change verification records; reason code reports; dispute log |
| 2027 Q1 | SL-1 PI1.3, P4.2, P5.1, P6.2, CC9.2; SL-2 CC2.3, CC6.3, CC7.5, CC9.2, A1.3, PI1.2, PI1.3 | Automated reconciliation; privacy operations; contract amendments; OT domain certification; SCADA failover retest (2027-02-28); range checks; reconciliation exception workflow | Reconciliation reports; certification records; failover retest report |
| 2027 Q1 (March) | Readiness check by Internal Audit for both lines; SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | SL-2 CC7.1, CC7.2, CC9.1, A1.2 (due 2027-06-30) | Field device inventory; OT sensors at the remaining water facilities; second carrier at alarm-critical water facilities | Inventory reconciliation; sensor coverage report; carrier contract |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 11 collecting, 7 ready, 7 not started (each tied to a POA&M item, a P01 risk, or a 2026 Q4 action).

**Owner, partner, and customer communication:** SL-1 owners and partners who ask receive the 2025 report, a bridge letter, and a roadmap letter for the added categories; SL-2 customers receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11).
