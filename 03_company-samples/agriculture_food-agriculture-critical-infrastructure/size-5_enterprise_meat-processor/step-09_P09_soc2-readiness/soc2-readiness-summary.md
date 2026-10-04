# SOC 2 Readiness Summary: Cris Santos Company | Food and Agriculture | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded further processor of meat products) |
| Tier / Vertical | Enterprise / Food and Agriculture |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 cold storage and logistics services (about 40 food company customers, DC-01 to DC-04); SL-2 co-manufacturing and private label (about 25 customers, PLT-01, PLT-03, PLT-04, PLT-07) |
| Categories in scope | Both service lines: Security, Availability, Confidentiality, and Processing Integrity. Privacy was evaluated and is out of scope for both (section 1) |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (follows the 2025 Type 1 for Security and Availability; adds Confidentiality and Processing Integrity). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (24 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's business is selling food, which SOC 2 does not cover; food safety assurance comes from FSIS inspection, the HACCP plans, FDA oversight at PLT-07, and customers' supplier approval programs. Two service lines are different: the company **performs services for other businesses whose own controls depend on it**, so it is a service organization for them.
- **SL-1 cold storage and logistics.** About 40 food companies store and ship refrigerated and frozen product through DC-01 to DC-04 and see inventory, temperature history, and lot data in the SL-1 portal. Their own HACCP and recall programs rely on the company's temperature records and inventory accuracy. SL-1 received a SOC 2 Type 1 report (Security, Availability) as of 2025-12-31. Customers now ask for a Type 2 report and for Processing Integrity, because temperature records and inventory are what they rely on, and Confidentiality, because the portal holds their volumes and pricing.
- **SL-2 co-manufacturing and private label.** About 25 retailers and brands have the company make products to their specifications, and receive CCP record packages and certificates of analysis through the SL-2 portal. Two national retail customers require a SOC 2 Type 2 report including **Confidentiality** (their specifications are trade secrets) and **Processing Integrity** (record packages must show the product was made to specification) by the end of 2027.

**Privacy is out of scope for both.** Neither service line collects or processes personal information on behalf of customers' consumers. Driver and employee data belong to the company's own operations and are covered by the enterprise privacy program.

**Alternatives considered:** GFSI-benchmarked food safety certifications and customer supplier audits address food safety, not the IT controls behind temperature records, portals, and specifications, so they complement SOC 2 rather than replace it. Customer security questionnaires were the status quo; SOC 2 replaces most of them with one report per service line.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the SOX program, and the P07 assessment. The cloud providers, the cold-chain monitoring vendor (SL-1), and the WMS vendor (SL-1) are subservice organizations presented with the carve-out method; their own SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 cold storage and logistics | SL-2 co-manufacturing and private label |
|---|---|---|
| Services | Refrigerated and frozen storage, handling, transport, and the customer portal | Production to customer specifications; record packages and certificates of analysis; customer portal |
| Infrastructure | DC-01 to DC-04, refrigeration controls, cold-chain monitoring, Cloud provider B portal with standby, landing zone controls (P04) | PLT-01, PLT-03, PLT-04, PLT-07 plant OT (all on the OT DMZ standard), central MES and records platform on Cloud provider A, Cloud provider B portal |
| Software | WMS and TMS (SaaS), SL-1 portal, cold-chain SaaS | Central MES, records platform, SL-2 portal |
| People | DC staff, SL-1 customer service, SOC, OT Security | Plant production and FSQA staff, SL-2 account managers, engineering, SOC |
| Data | Customer inventory, temperature history, lot data, pricing | Customer specifications and formulations (Restricted), CCP record packages, certificates of analysis |
| Procedures | P06 policy hierarchy; P08 runbook; SL-1 service manual | P06; P08; HACCP plans; PRC-01.3 OT change procedure |
| Subservice organizations (carved out) | Cloud provider B; cold-chain monitoring vendor; WMS and TMS vendors | Cloud providers A and B; records platform software vendor (remote support) |

PLT-05 and PLT-08 are outside both service lines, which keeps the two non-conforming plants (P07 section 6) out of the SL-2 boundary.

## 3. Readiness results
**SL-1 cold storage and logistics**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 29 | 4 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 co-manufacturing and private label**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 23 | 8 | 2 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 2 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

Across both service lines: 65 Ready, 18 Partially ready, 3 Not ready, 36 N/A (122 rows).

**SL-1** is close to ready for its first Type 2 period. Partially ready: CC3.1 (the system description must add the new categories), CC6.6 and CC7.1 (the DC-03 default password showed refrigeration controllers were outside configuration checks), CC9.2 (the cold-chain vendor's missing recovery commitment and SOC 2 exception), A1.2 (manual temperature logs exercised at 1 of 4 DCs), and PI1.3 (manual inventory adjustments unreviewed; temperature record gaps during outages). All close by 2027-01-31, before the period starts.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC3.1 (no system description), CC8.1 (OT change records), PI1.3 (HMI overrides are not recorded centrally or compared with the released recipe, so a record package cannot prove the product was made to the customer's specification). Partially ready: CC2.3, CC3.4, CC6.1, CC6.8, CC7.1, CC7.4, CC7.5, CC9.2, A1.3, C1.1, PI1.1, PI1.4. The gaps are the same ones Internal Audit found in the PPCM (P07): setpoint overrides, OT change control, MES recovery, vendor assurance, and default passwords at PLT-04. Closing POAM-005, POAM-010, POAM-012, POAM-017, and POAM-019 by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01. CC6.8 and CC7.1 depend partly on HMI replacement (POAM-004, through 2027-12-31); allowlisting is the compensating control and would be described in the report if still open.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC3.1, CC6.6, CC7.1, CC9.2; SL-2 CC3.1, CC3.4, CC7.4, CC8.1, C1.1, PI1.1 | System descriptions; credential sweep; cold-chain contract amendment; AI change gate; FSQA decision field; change workflow and reconciliation; specification access reviews; record package definitions | Updated descriptions; sweep report; amended contract; change reconciliations; access reviews |
| 2027 Q1 | SL-1 A1.2, PI1.3; SL-2 CC6.1, CC7.5, A1.3, PI1.3, PI1.4, CC9.2, CC2.3 | Manual log exercises at DCs; WMS adjustment reviews; second-badge overrides and setpoint comparison; MES failover retest; package completeness check; vendor backlog; agreement updates | Exercise records; override logs; DR retest report; package checks |
| 2026-12 and 2027-03 | Readiness checks by Internal Audit (SL-1 in December, SL-2 in March) | Mock walkthroughs with the service auditor | Walkthrough results |
| 2027 Q2 to Q4 | SL-2 CC6.8, CC7.1 (HMI replacement) | Replacement at SL-2 plants first | Replacement records |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 14 collecting, 4 ready, 6 not started (each tied to a POA&M item or a 2026 Q4 or 2027 Q1 action).

**Customer communication:** SL-1 customers receive the 2025 Type 1 report, a bridge letter, and the Type 2 timeline; SL-2 customers receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11).
