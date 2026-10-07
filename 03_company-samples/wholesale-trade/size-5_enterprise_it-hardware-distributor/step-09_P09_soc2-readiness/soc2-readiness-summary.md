# SOC 2 Readiness Summary: Cris Santos Company | Wholesale Trade | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded IT hardware and software distributor) |
| Tier / Vertical | Enterprise / Wholesale Trade |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 reseller commerce platform (about 9,500 reseller accounts); SL-2 lifecycle services: configuration, imaging, and ITAD sanitization (about 1,200 enterprise customers) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and (new for 2027) Processing Integrity and Privacy. SL-2: Security, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report; Processing Integrity and Privacy added). SL-2: first Type 2, period 2027-07-01 to 2027-12-31 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's business is buying and reselling products, which SOC 2 does not cover. Two service lines are different: the company **provides services that affect its customers' own operations and data**, so it is a service organization for them.
- **SL-1 reseller commerce platform.** About 9,500 reseller accounts use the platform and its APIs to see contract pricing, place orders, provision cloud subscriptions, and download invoices; about 430 resellers connect their own procurement systems by API. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) each year since 2024. Large resellers now ask for **Processing Integrity** (order and price accuracy, subscription provisioning), and software publishers and resellers ask how end-user license registrant data is handled, so **Privacy** is added for 2027.
- **SL-2 lifecycle services.** Enterprise customers send devices for imaging and configuration, and retired devices for sanitization and resale. Their vendor risk programs require a SOC 2 Type 2 report with **Confidentiality** (customer data on devices) and **Processing Integrity** (the right sanitization method on the right device, and accurate certificates).

**Alternatives considered:** a standardized security questionnaire (customers accept it only as a bridge); ISO/IEC 27001 certification (some customers accept it, but the large resellers and enterprise customers ask for SOC 2); CMMC Level 2 (covers only the FSCE, not these service lines, which are kept out of the CUI scope by design).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the SOX program, and the Level 1 (Self) self-assessment. Cloud providers A and B, the payment processor, and the sanitization software vendor are subservice organizations presented with the carve-out method; their own reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 reseller commerce platform | SL-2 lifecycle services |
|---|---|---|
| Services | Catalog, contract pricing, quoting, ordering, cloud subscription provisioning, invoices, order APIs | Imaging and configuration of new devices; collection, sanitization, certificates, and resale of retired devices |
| Infrastructure | Cloud provider B managed containers with second-region standby; landing zone controls (P04); integration with the ERP on Cloud provider A | Lifecycle services platform on Cloud provider A; imaging and sanitization factories at FL-2 and TX-1 |
| Software | Company-built platform and API gateway; payment processor's hosted payment fields | Commercial sanitization software; imaging tools; asset tracking |
| People | E-commerce engineering; reseller support; SOC; identity and cloud platform teams | Services staff at FL-2 and TX-1 (about 950), including agency workers; SOC |
| Data | Reseller users, contract pricing, orders, invoices, end-user license registrants (personal information) | Customer asset lists, device images, data on devices awaiting sanitization, sanitization records |
| Procedures | P06 policy hierarchy; P08 runbook; platform runbooks | P06; P08; sanitization and imaging procedures |
| Subservice organizations (carved out) | Cloud provider B; payment processor; email notification service | Cloud provider A; sanitization software vendor; logistics carriers |

## 3. Readiness results
**SL-1 reseller commerce platform**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 30 | 3 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | 13 | 4 | 1 | 0 |

**SL-2 lifecycle services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 21 | 10 | 2 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 1 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**Totals across both service lines (122 rows):** Ready 75, Partially ready 22, Not ready 4, N/A 21.

**SL-1** is ready for its next Type 2 on the existing categories except three Security items that match P07 findings: CC6.1 (static API keys, POAM-011), CC7.2 (no fraud detection on API orders and ship-to changes, POAM-012), and CC8.1 (emergency change approvals, POAM-015). C1.1 is partially ready because customer uploads were not inspected for CUI markings (POAM-007). For the new categories: PI1.2 depends on ship-to risk scoring (POAM-012); Privacy has one Not ready item (P6.2, no log of disclosures to software publishers) and four partially ready items (P2.1, P4.2, P4.3, P6.7).

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC2.3 (no system description or published commitments), CC7.1 (factory imaging servers outside vulnerability scanning), PI1.4 (certificates not reconciled automatically to customer asset lists). Partially ready: CC1.3, CC3.2, CC5.3, CC6.1, CC6.2, CC6.5, CC6.7, CC7.2, CC8.1, CC9.2, C1.1, C1.2, PI1.3. Most items close by 2027-01-31; PI1.4 (2027-03-31) and the TX-1 factory segmentation in CC6.1 (2027-02-28) set the period start of 2027-07-01, which leaves a quarter of operation before the period begins.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 C1.1, CC7.2, CC8.1, PI1.2; SL-2 CC1.3, CC3.2, CC6.2, CC6.7, CC7.1, CC7.2, CC8.1, C1.1 | CUI upload detection; fraud scoring and holds; emergency change hold; SL-2 charter and risk workshop; factory scanning and SIEM onboarding; managed file transfer for customer images | DLP reports; fraud alerts; change records; scan and log coverage |
| 2027 Q1 | SL-1 CC6.1, P2.1, P4.2, P4.3, P6.2, P6.7; SL-2 CC2.3, CC5.3, CC6.1, CC6.5, CC9.2, C1.2, PI1.3, PI1.4 | API token service; privacy disclosure log and retention jobs; SL-2 system description; verification at 10%; factory segmentation; sanitization vendor review; certificate reconciliation | Token inventory; disclosure log; certificates reconciled; segmentation evidence |
| 2027 Q2 | Readiness check by Internal Audit (both lines) | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q3 | SL-2 Type 2 period starts 2027-07-01 | Evidence collection per the evidence map | Period evidence |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" (9) are enterprise common controls collected once and used for both reports; 10 are SL-1 only and 6 are SL-2 only. Status: 10 collecting, 6 ready, 9 not started (each tied to a POA&M item or a remediation action above).

**Customer communication:** SL-1 resellers receive the 2025 report, a bridge letter, and a roadmap letter for Processing Integrity and Privacy; SL-2 customers receive this summary, a bridge letter describing the remediation, and the expected first report date (2028-02).
