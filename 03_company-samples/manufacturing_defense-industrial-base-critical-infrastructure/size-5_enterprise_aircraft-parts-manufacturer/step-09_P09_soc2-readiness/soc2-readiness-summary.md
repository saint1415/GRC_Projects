# SOC 2 Readiness Summary: Cris Santos Company | Defense Industrial Base | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded tier-1 aerostructures and aircraft components manufacturer) |
| Tier / Vertical | Enterprise / Defense Industrial Base |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 MRO customer portal (about 140 airline, lessor, and repair station customers); SL-2 aircraft health monitoring analytics (19 airline operators) |
| Categories in scope | SL-1: Security, Availability, Confidentiality. SL-2: Security, Availability, Confidentiality, Processing Integrity. Privacy is out of scope for both, with reasons in the CSV |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (second annual report). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Primary assurance for defense work | CMMC (Final Level 2 (C3PAO) since 2026-03-20; Level 3 planned for Program H). SOC 2 does not replace it |
| Files | `soc2-readiness.csv` (all 61 criteria for each service line: 122 rows); `soc2-evidence-map.csv` (24 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's revenue comes from making parts, which SOC 2 does not cover, and its defense customers rely on CMMC status in SPRS and the DFARS clauses, not SOC 2. Two commercial service lines are different: the company **provides services that run on its systems for other businesses**, so it is a service organization for them, and their vendor programs ask for a CPA's SOC 2 report.
- **SL-1 MRO customer portal.** Airlines, lessors, and repair stations track component repairs at FL-3, approve quotes, and download release records. SL-1 issued its first SOC 2 Type 2 report (Security, Availability) for 2025, with no exceptions. Customers now ask for Confidentiality because the portal holds their maintenance records and commercial terms.
- **SL-2 aircraft health monitoring analytics.** Operators send sensor data; the platform runs models and returns maintenance alerts. Operators' safety and reliability programs rely on the results, so their vendor programs require **Processing Integrity** in addition to Security, Availability, and Confidentiality.

**Alternatives considered:**
- **CMMC:** required for CUI; it does not cover commercial service commitments, and SL-1 and SL-2 hold no CUI (P04 finding 5).
- **ISO/IEC 27001 certification:** some operators accept it, but the largest customers ask for SOC 2, and running both would duplicate effort.
- **Customer questionnaires only:** no longer accepted by the largest operators.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines and CMMC, so one evidence set serves SOC 2, CMMC, and SOX. Cloud provider A and the notification messaging service are subservice organizations presented with the carve-out method; their own SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 MRO customer portal | SL-2 aircraft health monitoring analytics |
|---|---|---|
| Services | Repair order tracking, quote approval, release record download | Sensor data ingestion, model runs, maintenance alerts and reports |
| Infrastructure | Cloud provider A managed containers in two regions, landing zone controls (P04) | Cloud provider A data platform in one region (second region planned) |
| Software | Company-built portal integrated with ERP and the quality system | Company-built pipelines and models (AI-006 in P10) |
| People | Aftermarket digital team; SOC; identity and cloud platform teams | Digital Services data engineers and data scientists; SOC |
| Data | Customer repair records, commercial terms, customer staff contacts (EAR99 or not subject to the EAR) | Operator sensor data and alerts (EAR99 or not subject to the EAR) |
| Procedures | P06 policy hierarchy; P08 runbook; portal support procedures | P06; P08; model validation procedures (planned) |
| Subservice organizations (carved out) | Cloud provider A; notification messaging service | Cloud provider A; 3 third-party data feed providers |

## 3. Readiness results
**SL-1 MRO customer portal**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 32 | 1 |  |  |
| Availability (A1, 3) | 3 |  |  |  |
| Confidentiality (C1, 2) | 1 | 1 |  |  |
| Processing Integrity (PI1, 5) |  |  |  | 5 |
| Privacy (P1-P8, 18) |  |  |  | 18 |

**SL-2 aircraft health monitoring analytics**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 23 | 9 | 1 |  |
| Availability (A1, 3) | 1 | 1 | 1 |  |
| Confidentiality (C1, 2) | 1 | 1 |  |  |
| Processing Integrity (PI1, 5) | 1 | 3 | 1 |  |
| Privacy (P1-P8, 18) |  |  |  | 18 |

**SL-1** is ready for its next Type 2, including the new Confidentiality category, once two items close: CC9.2, C1.2 (subservice organization review and automated deletion at contract end).

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC8.1, A1.3, PI1.3. Partially ready: CC1.3, CC2.3, CC3.2, CC6.1, CC6.2, CC6.7, CC7.2, CC7.5, CC9.2, A1.2, C1.2, PI1.1, PI1.2, PI1.4. The gaps come from a young service line: model changes outside the change process, no model registry or drift monitoring, single-region design with no tested recovery, shared feed keys, and incomplete specifications. Closing them by 2027-03-31 lets the SL-2 period start on 2027-04-01.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC9.2; SL-2 CC1.3, CC3.2, CC6.1, CC7.2, PI1.1 | Subservice report review; SL-2 RACI; SL-2 risks in P01; per-operator keys; SIEM onboarding; product specifications | Vendor review; RACI; register entries; key rotation logs; SIEM source list |
| 2027 Q1 | SL-1 C1.2; SL-2 CC2.3, CC6.2, CC6.7, CC7.5, CC8.1, CC9.2, A1.2, A1.3, C1.2, PI1.2, PI1.3, PI1.4 | Deletion automation; system description; self-service administration; TLS feeds; second-region standby and recovery test; model change gates and registry; feed provider reviews; range checks; output reconciliation | Deletion certificates; system description; provisioning tickets; recovery test report; model deployment approvals; reconciliation reports |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines); SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 to Q4 | Operate and collect | Monthly evidence reviews by the GRC team | All evidence map items |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports and for CMMC. Status: 13 collecting, 6 ready, 5 not started (each tied to a 2026 Q4 or 2027 Q1 action).

**Customer communication:** SL-1 customers receive the 2025 report, a bridge letter, and notice that Confidentiality is added for 2027. SL-2 operators receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11).
