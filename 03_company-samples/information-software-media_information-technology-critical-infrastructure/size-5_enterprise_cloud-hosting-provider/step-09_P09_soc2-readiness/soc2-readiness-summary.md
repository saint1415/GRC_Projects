# SOC 2 Readiness Summary: Cris Santos Company | Information Technology | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded public cloud and managed infrastructure provider) |
| Tier / Vertical | Enterprise / Information Technology |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Service lines | SL-1 Commercial Cloud; SL-2 Government Cloud; SL-3 Managed Infrastructure Services |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and (new) Processing Integrity for metering and invoicing. SL-2: Security, Availability, Confidentiality. SL-3: Security, Availability, Confidentiality, Processing Integrity. Privacy: assessed for all three and kept out of scope (section 1) |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (seventh annual report; Processing Integrity added). SL-2: Type 2, period 2027-01-01 to 2027-12-31 (fifth annual report). SL-3: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 183 rows); `soc2-evidence-map.csv` (27 evidence items) |
| Prepared | 2026-08-31 to 2026-09-04 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
The company is a service organization for about 41,000 customers. Customers, their auditors, and their regulators rely on a CPA's SOC 2 report to assess the company's controls over their workloads.
- **SL-1 Commercial Cloud** has issued an annual SOC 2 Type 2 report (Security, Availability, Confidentiality) since 2021. Large customers, including the 210 banking organizations and health care customers, ask for Processing Integrity over usage metering and invoicing because their bills depend on it.
- **SL-2 Government Cloud** has issued an annual Type 2 report since 2023. Agencies and DIB customers use it alongside FR-2.
- **SL-3 Managed Infrastructure Services** has no report yet. Bank customers' vendor programs now require one, and AQ-1's former customers had none. The first report needs the AQ-1 migration to finish, because the legacy RMM tool cannot meet the access, monitoring, and change criteria.

**Why Privacy is out of scope.** The company processes customers' personal information as a service provider. Its commitments for that data (use only to provide the service, confidentiality, deletion at contract end, breach notice) are covered by Confidentiality and the customer data processing terms. No service line makes privacy notice or consent commitments to data subjects, which is what the Privacy criteria test. The decision is reviewed each year with the service line owners and the Chief Privacy Officer.

**Alternatives considered:** FedRAMP certifications (FR-1, FR-2) serve federal customers but not commercial customers' auditors; ISO/IEC 27001 certification is held for SL-1 and SL-2 and is offered as a complement, not a replacement, because bank and health care customers' programs ask for SOC 2 reports.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support all three service lines, so one evidence set serves the three reports, FedRAMP, and SOX. Subservice organizations are presented with the carve-out method: colocation providers for edge PoPs, Cloud provider X (status page and recovery vault), and, until migration, the legacy RMM vendor for SL-3.

## 2. System description (scope)
| Element | SL-1 Commercial Cloud | SL-2 Government Cloud | SL-3 Managed Infrastructure Services |
|---|---|---|---|
| Services | IaaS and PaaS in regions R1 to R6 | IaaS and PaaS in region G1 | Patching, monitoring, backup, and operations of customer servers |
| Infrastructure | 18 data centers; 41 PoPs; control planes; key management | G1-A and G1-B; HCP-G (P02) | Fleet automation (SYS-09); legacy RMM tool (SYS-10) until 2027-03-31 |
| Software | Company-built control plane, console, and API; hypervisor; guest agent | Same, G1 instances | Fleet automation jobs; RMM scripts (AQ-1) |
| People | Platform, control plane, network, data center, SOC, support | U.S.-person G1 operations staff | Managed services engineers; AQ-1 technicians |
| Data | Customer content (classified Customer Content); metering data | Federal data and CUI; customer content | Customer server configuration, patch, and backup data |
| Procedures | P06 policy hierarchy; P08 runbooks; release procedures | Same, with FedRAMP rules | Same, with customer maintenance windows |
| Subservice organizations (carved out) | Colocation providers (PoPs); Cloud provider X | Cloud provider X (encrypted recovery copy, status page) | Legacy RMM vendor (until migration); Cloud provider X |

## 3. Readiness results
**SL-1 Commercial Cloud**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 29 | 4 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 Government Cloud**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 26 | 7 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-3 Managed Infrastructure Services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 22 | 7 | 4 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready to continue its annual report. Partially ready: CC6.8, CC7.2, CC8.1, CC9.2 (the release approval weakness, AI triage auto-close, and overdue vendor reviews), and PI1.1 and PI1.3 for the new Processing Integrity scope. POAM-001 (2026-12-15) and POAM-013 (2026-11-30) close before the period starts; if POAM-006 is still open on 2027-01-01, the exception would be described in the report.

**SL-2** is ready to continue its annual report once the same release and monitoring items close. Partially ready: CC6.1, CC6.3, CC6.8, CC7.1, CC7.2, CC8.1, CC9.2, A1.3. These match the Internal Audit findings for HCP-G (P07). A1.3 (G1 recovery time, POAM-009) and CC6.1 (cryptographic modules, POAM-004) close in 2027-01 and 2027-02, after the period starts, so the SL-2 report would describe them if the auditor tests them before they close.

**SL-3** is not yet ready to start a period. Not ready: CC6.1, CC7.2, CC8.1, CC9.2, A1.3. Partially ready: CC2.3, CC3.4, CC6.2, CC6.3, CC6.8, CC7.4, CC7.5, A1.2, C1.1, PI1.3, PI1.4. Almost every gap is the AQ-1 legacy RMM tool and directory. The AQ-1 migration (POAM-022, due 2027-03-31) is the gating item, which is why the SL-3 period starts on 2027-04-01.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | All lines CC6.8, CC8.1, CC7.2, CC9.2; SL-2 CC6.3, CC7.1; SL-3 CC9.2, CC3.4, CC7.2 | Two-person signed release approvals (POAM-001); human approval for automated actions (POAM-013); vendor review backlog (POAM-006); standing grants (POAM-002); vulnerability timeframes (POAM-007); RMM vendor addendum and real-time logs (POAM-022) | Release approval records; daily auto-close samples; vendor reviews; weekly grant checks |
| 2027 Q1 | SL-1 PI1.1, PI1.3; SL-2 A1.3, CC6.1; SL-3 CC6.1, CC6.2, CC6.3, CC8.1, CC7.4, CC7.5, A1.2, A1.3, C1.1, PI1.3, PI1.4, CC2.3 | Metering commitments and daily reconciliation; G1 failover retest (POAM-009); validated modules (POAM-004); AQ-1 identity migration and server migration (POAM-022); SL-3 recovery test; RMM section in the runbook | Reconciliation reports; DR retest; migration records; SL-3 recovery test |
| 2027 Q1 (March) | Readiness check by Internal Audit for SL-3; SL-3 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 and later | Maintain | Evidence collected through the periods | Per `soc2-evidence-map.csv` |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "All three" are enterprise common controls collected once and used for every report. Status: 15 collecting, 5 ready, 7 not started (each tied to a POA&M item or a 2027 Q1 action).

**Customer communication:** SL-1 and SL-2 customers receive the 2026 reports and a bridge letter describing the release approval remediation; SL-3 customers, including the 140 former AQ-1 customers, receive this summary and the expected first report date (2027-11).
