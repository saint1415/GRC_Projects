# SOC 2 Readiness Summary: Cris Santos Company | Chemical | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded specialty chemical formulator and packager) |
| Tier / Vertical | Enterprise / Chemical |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Service lines | SL-1 tank telemetry and vendor-managed inventory (about 2,900 customers; about 41,000 sensors at about 6,800 sites); SL-2 toll manufacturing and contract formulation (about 85 customers; batch systems at PLT-01, PLT-03, PLT-06, and PLT-09) |
| Categories in scope | SL-1: Security and Availability (unchanged). SL-2: Security, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (third annual report). SL-2: first Type 2, period 2027-04-01 to 2027-12-31 (9 months), report expected 2028-02 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-24 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's revenue comes from selling chemicals, which SOC 2 does not cover. Two service lines are different: the company **provides services to other businesses** that depend on its systems, so it is a service organization for them.
- **SL-1 tank telemetry and VMI.** Customers rely on the company's cloud platform to watch their tank levels and reorder automatically, and about 1,900 municipal water utilities are among the customer base. SL-1 has issued an annual SOC 2 Type 2 report (Security and Availability) since 2025. Customers have not asked for more categories; the 2026 report period is in progress.
- **SL-2 toll manufacturing and contract formulation.** Customers send their own formulations, which run in the company's plant batch systems, and receive batch records and certificates of analysis through a customer portal. Two large customers require a SOC 2 Type 2 report with **Confidentiality** (their recipes are trade secrets) and **Processing Integrity** (batches must follow the approved recipe) by 2027.

**Alternatives considered:**
- **ISO/IEC 27001 certification:** some international customers would accept it, but the two customers that asked named SOC 2 with Processing Integrity, and the enterprise already runs a SOC 2 program for SL-1.
- **Customer audits under the toll agreements:** about 20 site audits a year today. A SOC 2 report is expected to replace most of them.
- **The vertical registry lists no assurance alternative for chemical companies**, and the CFATS and MTSA programs are regulatory, not assurance for customers. They support the same controls but do not give customers a CPA's opinion.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the MTSA Cybersecurity Plan audit at PLT-01, and the SOX program. Cloud provider A, Cloud provider B, and the cellular carrier are subservice organizations presented with the carve-out method; their own reports are reviewed under CC9.2. SL-2 is the first SOC 2 scope in the company that includes **plant OT** (the batch systems), so the P07 findings on change control and recovery bear directly on it.

## 2. System description (scope)
| Element | SL-1 tank telemetry and VMI | SL-2 toll manufacturing and contract formulation |
|---|---|---|
| Services | Remote tank level monitoring; automatic replenishment orders; customer portal | Formulation and batch production from customer recipes; batch records and certificates of analysis |
| Infrastructure | Cloud provider B managed containers and IoT device connectivity, second-region standby, landing zone controls (P04); cellular network | PLT-01, PLT-03, PLT-06, PLT-09 batch systems behind OT DMZs; central remote access gateway and OT backup vault (CCP-03); SL-2 portal and LIMS on Cloud provider A |
| Software | Company-built telemetry platform and portal | DCS and batch management software (commercial); LIMS; company-built SL-2 portal |
| People | Digital services team; SOC; identity and cloud platform teams | Toll manufacturing account team; plant operators and controls engineers; QC laboratories; SOC; OT Center of Excellence |
| Data | Tank levels, site and contact data, replenishment orders | Customer recipes, batch records, certificates of analysis |
| Procedures | P06 policy hierarchy; P08 runbook; SL-1 support procedures | P06; P08; MOC; recipe intake; quality release |
| Subservice organizations (carved out) | Cloud provider B; cellular carrier | Cloud provider A; DCS vendor (remote support) |

## 3. Readiness results
**SL-1 tank telemetry and VMI**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 32 | 1 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 toll manufacturing and contract formulation**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 22 | 10 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 1 | 2 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready for its next Type 2 period. The one partially ready item (CC9.1) is the cellular carrier concentration: about 80% of sensors use one carrier, and the only fallback is customers phoning in orders. Dual-SIM sensors are rolled out at contract renewal (P01 R-047).

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC8.1, PI1.3, PI1.5. Partially ready: CC2.3, CC3.1, CC6.1, CC6.2, CC6.3, CC6.8, CC7.1, CC7.2, CC7.5, CC9.2, C1.2, PI1.1. Most gaps are the same ones Internal Audit found in the GC-PCBMS (P07): recipe and control changes outside MOC, no recipe integrity check, shared integrator accounts, OT leaver accounts, KEVs, and unproven OT restores. Closing POAM-001, POAM-002, POAM-003, POAM-005, POAM-016, POAM-022, and POAM-023 by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01. The items that close later (CC6.8 through POAM-020, due 2027-06-30) have compensating controls today and would be described in the report if still open.

**Why Processing Integrity is hard here.** For a software service, processing integrity is about code and data. For toll manufacturing it also means proving that every batch ran the customer's approved recipe version on a control system whose changes are all approved. Until the DCS change log is reconciled to MOC and executed recipe versions are reconciled to approved versions (POAM-001), the company cannot show that, which is why PI1.3 is Not ready.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-2 CC6.1, CC6.2, CC6.3, CC7.1, CC7.2 | Named integrator accounts (POAM-005); OT leaver automation (POAM-023); KEV compensating controls (POAM-002); OT detections (POAM-022) | Gateway account reviews; leaver reconciliations; KEV register; SIEM use case tests |
| 2027 Q1 | SL-2 CC2.3, CC3.1, CC7.5, CC8.1, CC9.2, C1.2, PI1.1, PI1.3, PI1.5 | SL-2 system description, commitments register, and processing exhibit; MOC reconciliation and recipe version reconciliation (POAM-001); recipe vault (POAM-016); restore tests at the SL-2 plants (POAM-003); supplier clauses (POAM-010); contract-end deletion procedure | Reconciliation reports; vault hash reports; restore test reports; amended agreements |
| 2027 Q1 (March) | Readiness check by Internal Audit (SL-2); SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor at PLT-01 | Walkthrough results |
| 2027 Q2 | SL-2 CC6.8; SL-1 CC9.1 | Blend Hall 1 console upgrade (POAM-020); dual-SIM rollout starts with water utilities | Upgrade records; rollout status |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 13 collecting, 6 ready, 6 not started (each tied to a POA&M item or a 2027 Q1 action).

**Customer communication:** SL-1 customers receive the 2025 report and a bridge letter. SL-2 customers, including the two that asked for the report, receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2028-02). Until then, toll customers may continue their site audits.
