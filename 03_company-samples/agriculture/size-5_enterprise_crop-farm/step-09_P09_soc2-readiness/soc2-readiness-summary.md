# SOC 2 Readiness Summary: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded diversified precision-agriculture crop farm) |
| Tier / Vertical | Enterprise / Agriculture, Forestry, Fishing and Hunting |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Service lines | SL-1 grower data platform (licensed to about 420 contract and independent growers); SL-2 grower packing, cooling, and traceability services at the 3 regional hubs (about 160 contract growers) |
| Categories in scope | SL-1: Security, Availability, Confidentiality. SL-2: Security, Availability, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (third annual report). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's work is growing, packing, and selling its own crops, which SOC 2 does not cover. Two service lines are different: the company **provides services to other farms**, so it is a service organization for them, and their buyers and lenders ask for a CPA's SOC 2 report.
- **SL-1 grower data platform.** Contract and independent growers license agronomy analytics, irrigation scheduling recommendations, and yield reporting on Cloud provider A. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2025. Growers rely on the platform's availability in planting and irrigation season and on the confidentiality of their yields and field data.
- **SL-2 grower packing, cooling, and traceability services.** About 160 contract growers deliver produce to the 3 hubs, where the company cools and packs it, assigns traceability lot codes, and sends lot and shipping data to the growers' buyers. Retail buyers now ask growers to show that the packer's lot codes and traceability data are accurate and complete, which is a **Processing Integrity** commitment. SL-2 has no SOC report yet.

**Alternatives considered:** third-party food safety audits (all 17 packing sites passed in 2026) address food safety practices, not IT controls over lot data, so they complement SOC 2 rather than replace it. An agreed-upon procedures report on lot code accuracy was cheaper but gives buyers no opinion on control design and operation over a period. ISO/IEC 27001 certification was set aside because SL-1 clients already accept SOC 2 and one framework per service line is cheaper to run.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports and the SOX and internal audit programs. Cloud provider A, the FMIS vendor, the EDI network provider, and the cold-chain monitoring SaaS are subservice organizations presented with the carve-out method; their own SOC reports are reviewed under CC9.2, which is where SL-2's gap sits.

**Effect on farm status:** SL-2 growth is limited by the hub farm-status condition (P03 G-145): if third-party produce passes a majority at a hub, that hub would need FDA registration. The SL-2 system description will state the hub capacity offered to growers, which the Chief Food Safety and Quality Officer sets each season.

## 2. System description (scope)
| Element | SL-1 grower data platform | SL-2 grower packing, cooling, and traceability services |
|---|---|---|
| Services | Agronomy analytics, irrigation scheduling recommendations (AI-002), yield reporting for growers' own fields | Receiving, cooling, packing, lot code assignment, traceability records, and lot and shipping data delivery for growers' produce |
| Infrastructure | Cloud provider A managed containers in a dedicated workload account; second-region warm standby; landing zone controls (P04) | Hub packing line servers and controllers, optical graders, refrigeration controllers, label printers (SYS-07); traceability data service on Cloud provider A; replicas at DC-2 |
| Software | Company-built platform and APIs; AI-002 recommendation model | Packing line management software (vendor); traceability data service (company-built); EDI |
| People | Digital agronomy team; SOC; identity and cloud platform teams | Hub managers, receiving clerks, and packing staff; Traceability Program Manager; SOC; OT security |
| Data | Growers' field boundaries, soil and moisture data, yields, irrigation plans (Confidential) | Growers' receiving data, lot codes, cooling records, packed volumes, pricing (Confidential) |
| Procedures | P06 policy hierarchy; P08 runbook; SL-1 support and release procedures | P06; P08; receiving, lot code, and traceability procedures; packing site downtime procedures |
| Subservice organizations (carved out) | Cloud provider A; weather data service; mapping service | Cloud provider A; packing line software vendor (remote support); EDI network provider; cold-chain monitoring SaaS |

## 3. Readiness results
**SL-1 grower data platform**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 32 | 1 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 grower packing, cooling, and traceability services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 26 | 6 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready for its next Type 2 period. The one partially ready item is CC6.2: 12% of grower administrators did not return the Q2 2026 attestation, so departed grower staff accounts can stay active. An automatic 60-day inactivity rule is due 2026-12-31, before the period starts.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC9.2 (the cold-chain monitoring SaaS that carries the hub cooler alarms has no SOC report, questionnaire, or security terms). Partially ready: CC2.3, CC3.2, CC6.6, CC6.8, CC7.2, CC8.1, A1.3, PI1.1, PI1.2, PI1.4. The gaps match what Internal Audit and the gap analysis found (P07 MA-4 and SA-9; P03 traceability rows): packing vendor remote sessions, change control for packing line and label template changes, cooler alarm vendor assurance, and traceability outputs. Closing POAM-004 and POAM-015 by 2026-12-31 and the 2027-03-31 items (system description, risk matrix, change control, hub restore test, processing specification) makes SL-2 ready to start its period on 2027-04-01. Items that close later (CC6.8, CC7.2, PI1.2, PI1.4, due 2027-06-30) have compensating controls today (network segmentation, daily lot reconciliation, receiving checks) and would be described in the report as open items if still open.

**Privacy** is out of scope for both lines: neither service commits to growers about personal information beyond grower staff contact and login details, which the Security criteria cover. **Processing Integrity** is out of scope for SL-1 because its analytics and recommendations are advisory.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-2 CC9.2, CC6.6; SL-1 CC6.2 | Cold-chain vendor questionnaire and terms (POAM-015); packing line vendors onto the gateway (POAM-004); SL-1 grower account inactivity rule; grower notice tested in the 2026-11-17 tabletop | Signed vendor terms; gateway session records; inactivity job reports |
| 2027 Q1 | SL-2 CC2.3, CC3.1, CC3.2, CC8.1, A1.3, PI1.1 | SL-2 system description and grower commitments; SL-2 risk and commitment matrix; packing OT and label template change control; hub restore test; processing specification | Approved description; change records; restore test report |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines); SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | Remaining SL-2 partially ready items (CC6.8, CC7.2, PI1.2, PI1.4), due 2027-06-30 | Packing line allowlisting; OT sensors at the hubs; electronic receiving at Hub 3; lot code source in EDI outputs | Allowlisting reports; sensor coverage; receiving and EDI samples |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 13 collecting, 6 ready, 6 not started (each tied to a POA&M item or a 2027 Q1 action).

**Client communication:** SL-1 growers receive the most recent SL-1 report and a bridge letter; SL-2 growers and the buyers who asked receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11).
