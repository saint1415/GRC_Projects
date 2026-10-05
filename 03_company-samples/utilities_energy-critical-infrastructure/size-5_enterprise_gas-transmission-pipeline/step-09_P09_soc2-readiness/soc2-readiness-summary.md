# SOC 2 Readiness Summary: Cris Santos Company | Energy | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded interstate natural gas transmission company) |
| Tier / Vertical | Enterprise / Energy (natural gas pipeline) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs are listed with short topic labels in our own words |
| Service lines | SL-1 shipper services platform (nominations, scheduling, confirmations, capacity release, postings, invoicing; about 380 shippers and interconnecting pipelines). SL-2 contract operations of the JV-1, JV-2, and JV-3 pipelines for their owners (gas control from GCC-1 with GCC-2 standby, field operations, measurement, and monthly operating statements) |
| Categories in scope | SL-1: Security, Availability, and (new) Confidentiality. SL-2: Security, Availability, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (third annual report; Confidentiality added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (22 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's assurance work faces regulators: TSA reviews the Cybersecurity Implementation Plan and assessment results, PHMSA inspects control room management, and the SOX program tests financial controls. None of these produces a report that customers can rely on. Two service lines make the company a **service organization** for other businesses:
- **SL-1 shipper services platform.** Shippers and interconnecting pipelines enter nominations and receive confirmations, scheduled quantities, and invoices through the platform. Its availability at nomination deadlines and the confidentiality of each shipper's positions matter to them. SL-1 has issued a SOC 2 Type 2 report (Security and Availability) since 2025; the 2025 report had no exceptions. Several large shippers asked for Confidentiality in 2026.
- **SL-2 contract operations.** The company operates JV-1 to JV-3 for owner groups that include other pipeline companies. Their auditors and boards ask for independent assurance over gas control, access to the shared SCADA platform, and the accuracy of the monthly measurement and operating statements that drive their revenue allocations, so Processing Integrity is in scope.

**Alternatives considered:**
- **TSA security directive compliance reviews** (the vertical's assurance alternative for designated pipelines): they cover the company's own Critical Cyber Systems, but their results are SSI and cannot be shared with shippers or JV owners, and they do not address processing integrity of statements.
- **Operating agreement audit rights:** each JV owner could audit separately; one SOC 2 report replaces three overlapping audits.
SOC 2 complements the TSA and PHMSA programs; it does not replace them.

**Relationship to other assurance:** enterprise common controls (P02 section 10.3; P04 section 5) serve both service lines, so one set of evidence supports both reports, the TSA Cybersecurity Assessment Plan, and SOX. The cloud providers, the colocation provider, and the payroll SaaS are subservice organizations presented with the carve-out method; their SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 shipper services platform | SL-2 contract operations for JV owners |
|---|---|---|
| Services | Nominations, scheduling, confirmations, capacity release, informational postings, invoicing | Gas control of JV-1 to JV-3, field operations and maintenance, measurement, monthly operating and measurement statements, owner portal |
| Infrastructure | Cloud provider A managed containers and databases in two zones with a second-region standby; landing zone controls (P04) | PSGCS at GCC-1 and GCC-2 (P02): shared SCADA platform, 9 JV compressor stations, JV field devices and telemetry; measurement system and JV owner portal on Cloud provider A |
| Software | Company-built platform and APIs | Commercial SCADA platform; station controls; measurement and allocation software; owner portal |
| People | Commercial applications team; scheduling desk; SOC; identity and cloud platform teams | Gas controllers; field operations; measurement; contract operations; SCADA engineering; OT security; SOC |
| Data | Shipper nominations, positions, contracts, and invoices (Confidential) | Real-time process data; measurement data; owner statements (Confidential) |
| Procedures | P06 policy hierarchy; P08 runbook; tariff procedures | P06; P08; control room management procedures; measurement manual |
| Subservice organizations (carved out) | Cloud provider A; email delivery service | Cloud provider A; telecommunications carriers; SCADA vendor (remote support through the gateway) |

**Boundary note for SL-2:** the SL-2 system shares the SCADA platform, OT domain, and gas control centers with PS-1 and PS-2. Findings in the shared platform (P07) therefore count for SL-2 even when the affected component sits on an owned pipeline system.

## 3. Readiness results
**SL-1 shipper services platform**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 32 | 1 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 contract operations for JV owners**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 22 | 10 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready for its 2027 Type 2. Two items are partially ready: shipper user MFA enrollment (CC6.1, due 2026-12-31) and labels and data loss prevention on bulk exports for the new Confidentiality category (C1.1, due 2027-01-31).

**SL-2** is not yet ready for its first period. Not ready: CC6.6 (the 7 always-on vendor modems on the shared SCADA platform, POAM-004, due 2026-12-15). Partially ready: CC2.3, CC3.1, CC6.1, CC6.3, CC7.1, CC7.2, CC7.5, CC8.1, CC9.1, CC9.2, A1.3, C1.1, and PI1.3. These are the same gaps Internal Audit found in the PSGCS (P07), plus SL-2's missing system description, commitments register, and allocation review. Closing POAM-001, POAM-002, POAM-004, POAM-005, POAM-008, POAM-009, POAM-011, and POAM-012 by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01. CC9.2 (POAM-014, due 2027-06-30) has compensating controls today (annual supplier review and soak testing of SCADA releases) and would be described in the report if still open.

Privacy is N/A for both lines because they process business contact data only; employee data is outside both systems.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-2 CC6.1, CC6.3, CC6.6, CC8.1, C1.1; SL-1 CC6.1 | Shared password automation (POAM-001); transfer trigger (POAM-008); modem removal (POAM-004); point-to-point workflow block (POAM-009); owner-group access review; shipper MFA enforcement | Gateway session records; OT access workflow records; change records; MFA enrollment reports |
| 2027 Q1 | SL-2 CC2.3, CC3.1, CC7.1, CC7.2, CC7.5, CC9.1, A1.3, PI1.3; SL-1 C1.1 | SL-2 system description and commitments register; KEV backlog cleared (POAM-002); JV meter and valve monitoring pilot (POAM-005); GCC-2 isolation exercise (POAM-012); platform-wide SCADA scenario drill (POAM-011); allocation second review; SL-1 export labels | Exercise reports; coverage reports; allocation review records |
| 2027 Q1 (March) | Readiness check by Internal Audit for SL-2; mock walkthrough with the service auditor | Walkthrough of CC6, CC7, CC8, and PI1 controls | Walkthrough results |
| 2027-04-01 | SL-2 Type 2 period starts (to 2027-09-30) | | All SL-2 evidence items collecting |
| 2027 Q2 | SL-2 CC9.2 | Supplier contract amendments and software bills of materials (POAM-014, due 2027-06-30) | Amended contracts; SBOM register |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 12 collecting, 5 ready, 5 not started (all SL-2 items tied to a POA&M item or a 2027 Q1 action).

**User entity communication:** shippers receive the 2025 SL-1 report, a bridge letter, and notice that Confidentiality is added in 2027. JV owners receive this summary at the next operating committee meetings, with the expected SL-2 report date (2027-11). Neither communication includes SSI.
