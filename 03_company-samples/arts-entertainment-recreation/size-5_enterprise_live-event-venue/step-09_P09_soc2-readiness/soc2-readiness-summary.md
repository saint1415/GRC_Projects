# SOC 2 Readiness Summary: Cris Santos Company | Arts, Entertainment, and Recreation | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded live entertainment company) |
| Tier / Vertical | Enterprise / Arts, Entertainment, and Recreation |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs are listed with short topic labels written for this summary; the AICPA text is not reproduced |
| Service lines | SL-1 white-label ticketing (about 340 client venues and promoters); SL-2 venue management services (8 publicly owned venues) |
| Categories in scope | SL-1: Security, Availability, Confidentiality (in the 2025 and 2026 reports), plus Processing Integrity and Privacy (new for 2027). SL-2: Security, Availability, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (third annual report; Processing Integrity and Privacy added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-28 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's revenue comes from its own events, which SOC 2 does not cover, and its card payments are assured through PCI DSS (P03). Two service lines are different: the company **provides services to other businesses**, so it is a service organization for them, and their auditors and procurement teams ask for a CPA's SOC 2 report.
- **SL-1 white-label ticketing.** Client venues and promoters sell tickets on client-branded sites run by the platform. The company is a PCI DSS service provider for them, but the PCI DSS AOC covers only card data. Clients also rely on the company for availability during on-sales, the confidentiality of their event and patron data, the accuracy of orders, fees, and settlement reports, and the handling of their patrons' personal information. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) since 2025; the 2025 report had no exceptions. Larger clients now ask for Processing Integrity (settlement accuracy) and Privacy.
- **SL-2 venue management.** The company operates 8 venues owned by cities, counties, and a state university. Owners rely on its systems for monthly reporting and settlement statements, and their auditors have asked for a SOC 2 Type 2 report that includes Processing Integrity.

**Alternatives considered:** PCI DSS AOCs (already provided to SL-1 clients, but limited to card data); a SOC 1 report for SL-2 settlement (owners' financial auditors may still ask for one; it would reuse the Processing Integrity evidence); ISO/IEC 27001 certification (clients in the United States ask for SOC 2 first).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the PCI DSS ROCs, and the SOX program. Cloud provider A, cloud provider B, the edge provider, the tokenization provider, and the processors are subservice organizations presented with the carve-out method; their SOC 2 reports and AOCs are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 white-label ticketing | SL-2 venue management services |
|---|---|---|
| Services | Ticket sales, box office, and gate entry for client events; client console; client reports and settlement files | Venue operations, box office and stand sales, settlement statements, and the owner portal for 8 managed venues |
| Infrastructure | Cloud provider A (two regions), edge provider, landing zone controls (P04) | Cloud provider B (settlement application and owner portal); venue networks and OT at the 8 venues; the TVOP for ticketing |
| Software | Company-built ticketing platform and payment service; client templates | Settlement application; cloud POS; building management systems |
| People | Platform and payments engineering; client success; SOC; identity and cloud platform teams | Venue management staff; venue finance; venue IT; SOC |
| Data | Client events, orders, patron accounts, and reports (card data only in the payment service and the tokenization provider) | Owner financial data, settlement records, venue operating data |
| Procedures | P06 policy hierarchy; P08 runbook with the client notification path; SL-1 support procedures | P06; P08; settlement procedures |
| Subservice organizations (carved out) | Cloud provider A; edge provider; tokenization provider; processors; email and SMS providers | Cloud provider B; cloud POS vendor; building management integrators |

## 3. Readiness results
**SL-1 white-label ticketing**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 26 | 7 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | 14 | 4 | 0 | 0 |

**SL-2 venue management services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 26 | 6 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 2 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** has no Not ready criteria, but 13 are partially ready: CC2.3, CC6.2, CC6.3, CC6.8, CC7.2, CC7.4, CC9.2, A1.3, PI1.3, P1.1, P2.1, P4.2, and P6.1. The Security items are the same weaknesses found in P03 and P07: client checkout template scripts (POAM-002), client user access (POAM-004), the untested client notification path (POAM-008), and tag vendors (POAM-009). Because the SL-1 period starts on 2027-01-01, POAM-002 (2026-12-15) and POAM-008 (2026-11-30) must close first; POAM-004 (2027-01-31) closes one month into the period and will appear as a described deficiency for January unless a compensating control is evidenced. The new Privacy items depend on POAM-022 and POAM-025 (2027-03-31), so management will decide by 2026-11-30 whether to add Privacy in 2027 or in 2028.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC2.3 (no system description or written owner commitments) and PI1.4 (no automated reconciliation before owner statements are issued). Partially ready: CC3.1, CC6.1, CC6.6, CC7.1, CC7.2, CC9.2, A1.3, PI1.1, and PI1.3. Closing the system description and commitments by 2027-01-31, owner portal MFA and settlement dual review by 2026-12-31, and reconciliation by 2027-03-31 makes SL-2 ready for its 2027-04-01 period. The OT items (CC6.6, CC7.1, CC7.2) depend on POAM-006, POAM-012, and POAM-019, which reach the managed venues by 2027-03-31; if they slip, they would be described in the report with their compensating controls.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC6.8, CC7.2, CC7.4, CC9.2, PI1.3; SL-2 CC6.1, PI1.3, A1.3 | Template redesign and tamper detection; tabletop with the client path; tag vendor review; accessible seating parity automation; owner portal MFA; settlement dual review; offline drills | Script inventory and alerts; tabletop report; parity reports; MFA configuration |
| 2027 Q1 | SL-1 CC2.3, CC6.2, CC6.3, A1.3, P1.1, P2.1, P4.2, P6.1; SL-2 CC2.3, CC3.1, PI1.1, PI1.4, CC6.6, CC7.1, CC7.2, CC9.2 | Client MFA and attestations; responsibility matrix; failover retest; privacy notice and signals; retention purge; SL-2 system description; reconciliation; OT work at managed venues | Client attestations; failover report; consent logs; reconciliation reports |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines); SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | Any SL-2 items still partially ready | Close remaining OT items at managed venues | Network test reports |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports and the PCI DSS ROCs. Status: 13 collecting, 5 ready, 7 not started (each tied to a POA&M item or a 2026 Q4 to 2027 Q1 action).

**Client communication:** SL-1 clients receive the 2025 report, a bridge letter, the PCI DSS AOC, and a letter describing the checkout template redesign; SL-2 owners receive this summary and the expected SL-2 report date (2027-11).
