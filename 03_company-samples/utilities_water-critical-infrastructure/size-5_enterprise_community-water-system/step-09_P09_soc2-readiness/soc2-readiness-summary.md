# SOC 2 Readiness Summary: Cris Santos Company | Water and Wastewater Systems | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded parent of state-regulated community water utilities) |
| Tier / Vertical | Enterprise / Water and Wastewater Systems |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Service lines | SL-1 contract operations and remote monitoring (38 municipal and industrial drinking water systems); SL-2 utility billing and customer care (27 municipal utilities, about 610,000 accounts) |
| Categories in scope | SL-1: Security, Availability, and (new for 2027) Confidentiality. SL-2: Security, Availability, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report; Confidentiality added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (23 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's work is running its own regulated water systems, which SOC 2 does not cover; primacy agencies, EPA, and the public utility commissions oversee that. Two service lines are different: the company **provides services to other utilities**, so it is a service organization for them, and their councils, auditors, and insurers ask for a CPA's SOC 2 report.
- **SL-1 contract operations and remote monitoring.** The company operates 38 client drinking water systems under operations and maintenance contracts and monitors them 24x7 from the ROCCs through the contract-services monitoring platform. SL-1 has issued a SOC 2 Type 2 report (Security, Availability) every year since 2024. The 2025 report had one exception (a contract operator's monitoring platform account removed 6 days late), since remediated. Clients now ask for Confidentiality because the company holds their SCADA diagrams, credentials, and parts of their RRAs and ERPs. The client systems' owners certify their own RRAs and ERPs; SL-1 supports them under contract.
- **SL-2 utility billing and customer care.** The company bills, takes payments, answers calls, and manages meter data for 27 municipal utilities in separate CIS tenants. Clients' auditors ask for a SOC 2 Type 2 report including **Processing Integrity**, because accurate bills and timely payment posting are the core commitments, and because SL-2 is a third-party agent holding their customers' personal information.

**Alternatives considered:** a SOC 1 report for SL-2 (useful to client financial auditors for billing revenue, and planned as a later addition, but it does not cover security of client customer data); ISO/IEC 27001 certification (some clients accept it, but most municipal procurement documents name SOC 2); relying on the company's SDWA section 1433 program (it covers the company's own systems, not the service commitments to clients).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the SOX program, and the RRA cyber elements. The cloud providers, the payment processor, the bill print vendor, the AMI vendors, and the colocation providers are subservice organizations presented with the carve-out method; their own SOC reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 contract operations and remote monitoring | SL-2 utility billing and customer care |
|---|---|---|
| Services | 24x7 remote monitoring and alarm response; on-site operation and maintenance; monthly operating reports | Billing, payment processing, contact center, meter data management, collections support |
| Infrastructure | Contract-services monitoring platform at the GCR ROCC with a standby at the Georgia ROCC; read-only connections to 31 client SCADA systems and control-capable connections to 7; OT remote access gateway for control sessions; SL-1 client reporting portal on Cloud provider B | CIS client tenants on Cloud provider A with a second-region standby; AMI head-ends (SaaS); contact center platform (SaaS) |
| Software | Commercial monitoring platform; client reporting portal (company-built) | Commercial CIS (customer-managed); company-built client portals |
| People | About 640 contract operators; ROCC staff; OT security; SOC | About 230 SL-2 staff; CIS team; SOC |
| Data | Client process data, alarms, SCADA diagrams and credentials (Restricted) | Client customers' names, addresses, account and usage data, bank account numbers for bank draft (Confidential); card data handled only by the payment processor |
| Procedures | P06 policy hierarchy; P08 runbook; SL-1 operating procedures | P06; P08; billing procedures and client specifications |
| Subservice organizations (carved out) | Cloud provider B; telemetry carriers; colocation providers | Cloud provider A; payment processor; bill print vendor; client AMI vendors; contact center platform vendor |

## 3. Readiness results
**SL-1 contract operations and remote monitoring**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 30 | 3 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 utility billing and customer care**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 25 | 7 | 1 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 2 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

Privacy is out of scope for both lines: SL-1 does not collect personal information from the public, and SL-2 processes client customers' information on each client's behalf, so notices and choices remain the client's responsibility and are listed as complementary user entity controls.

**SL-1** is ready for its next Type 2 on Security and Availability. Partially ready: CC6.2 (manual OT domain disablement, POAM-002, due 2027-01-31), CC6.6 (7 client connections still allow write commands, P01 R-054, due 2027-06-30), CC9.2 (integrator attestation and contract terms, POAM-012, due 2027-03-31), and the new C1.1 (client confidential information inventory incomplete for 9 of 38 clients, due 2026-12-31). CC6.6 and CC9.2 will still be open when the period starts on 2027-01-01; per-session gateway approval for every control session is the compensating control, and the service auditor will be told in the planning meeting.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC8.1 (no tenant isolation test in the release pipeline; client configuration changes made directly in production) and PI1.3 (rate table changes without independent verification; 3 billing errors in 2026 traced to rate entry). Partially ready: CC2.3, CC3.1, CC4.1, CC6.1, CC6.3, CC7.2, CC9.2, C1.1, PI1.1, PI1.4. All SL-2 items are due by 2027-03-31, which lets the period start on 2027-04-01 after an Internal Audit readiness test in March.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 C1.1; SL-2 CC9.2 | Client confidential information inventory; SOC reports for the bill print and client AMI vendors; amend 9 inherited contracts (POAM-023) | Inventory; vendor reviews; amended contracts |
| 2027 Q1 (January) | SL-1 CC6.2; SL-2 CC3.1, CC6.3, PI1.4 | OT domain federation (POAM-002); SL-2 commitments register; tenant-scoped roles; reconcile every SL-2 bill print file | Provisioning records; certifications; reconciliations |
| 2027 Q1 (February) | SL-2 CC2.3, PI1.1, PI1.3 | SL-2 system description and client control responsibilities; client specifications; second-person verification and test bills for rate changes | System description; rate change records |
| 2027 Q1 (March) | SL-1 CC9.2; SL-2 CC4.1, CC6.1, CC7.2, CC8.1, C1.1 | Integrator attestation (POAM-012); Internal Audit readiness test of SL-2 controls; tokenization; egress detection; tenant isolation test in the pipeline; extract registration | Attestations; readiness test results; pipeline records |
| 2027 Q2 | SL-1 CC6.6 (due 2027-06-30) | Read-only connections at the remaining 7 clients or per-session control | Client connection register |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" (11 of 23) are enterprise common controls collected once and used for both reports. Status: 12 collecting, 4 ready, 7 not started (each tied to a remediation action above).

**Client communication:** SL-1 clients receive the 2025 report, a bridge letter, and a Confidentiality roadmap letter. SL-2 clients receive this summary, a description of the remediation plan, and the expected first report date (2027-11).
