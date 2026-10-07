# SOC 2 Readiness Summary: Cris Santos Company | Retail Trade | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded regional supermarket chain; 112 stores; online ordering) |
| Tier / Vertical | Enterprise / Retail Trade |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; read the criteria in the AICPA publication |
| Service lines | SL-1 retail media network and data clean room (about 140 CPG brand clients); SL-2 supplier collaboration portal (about 1,400 suppliers) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and Processing Integrity (Privacy deferred to the second report). SL-2: Security, Availability, and Confidentiality |
| Target reports | First SOC 2 Type 2 for each service line, one service auditor, common period 2027-04-01 to 2027-09-30; reports expected 2027-11 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the Vice President, Retail Media and the Vice President, Supplier Collaboration; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's business is selling groceries to consumers, which SOC 2 does not cover. Two service lines are different: the company **provides services to other businesses**, so it is a service organization for them, and their large clients now require a CPA's SOC 2 Type 2 report.
- **SL-1 retail media and data clean room.** CPG brands buy sponsored product and display ads on the web and app, offsite audiences, and closed-loop sales measurement that the clean room returns as aggregated results. Brands share their own campaign and first-party data with the clean room and pay on measured results, so they ask about security, confidentiality, availability, and the accuracy of measurement (Processing Integrity).
- **SL-2 supplier collaboration portal.** Suppliers see store-level sales and inventory, forecasts, purchase orders, and invoice and deduction status. The data is commercially sensitive between competing suppliers, and suppliers plan production from it, so they ask about security, confidentiality, and availability.

Neither service line has a SOC 2 report today (00_company-facts.md section 4, gap 7).

**Alternatives considered:**
- **PCI DSS validation** is the vertical's usual assurance, but it covers only the cardholder data environment. SL-1 and SL-2 are deliberately kept out of the CDE (no card data; P04 section 7), so clients cannot rely on the company's AOC for them.
- **ISO/IEC 27001 certification** was considered; the largest CPG clients' vendor programs ask for SOC 2 Type 2 by name, and one framework per service line is cheaper to run.
- **Media measurement accreditation** by an industry body would complement SOC 2 Processing Integrity for SL-1 but does not cover security or confidentiality; it is a 2028 option.

**Privacy for SL-1.** The clean room processes loyalty members' personal information, so Privacy is relevant. It is deferred to the second report because the Tennessee data protection assessments and the privacy notice update must close first (POAM-019, POAM-023). Clients' data processing terms cover privacy until then.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04) support both service lines, so one set of evidence serves both reports, the PCI DSS program, and SOX. Cloud provider B, the ad server and clean room software vendors (SL-1), and the ERP vendor (SL-2) are subservice organizations presented with the carve-out method; their SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 retail media and data clean room | SL-2 supplier collaboration portal |
|---|---|---|
| Services | Sponsored products and display on the web and app; offsite audiences; closed-loop measurement returned as aggregated results | Store-level sales and inventory, forecasts, purchase orders, invoice and deduction status |
| Infrastructure | Cloud provider B data and analytics services, second region (P04) | Cloud provider B application services, second region (P04) |
| Software | Retail media platform and clean room (SYS-13) built on commercial ad server and clean room software | Company-built portal over ERP data feeds (SYS-09) |
| People | Retail media team; data science; SOC; identity and cloud platform teams | Supplier collaboration team; ERP team; SOC; identity and cloud platform teams |
| Data | Client campaign data; member-level basket data inside the clean room (never released); aggregated results. **No card data** (data contract and weekly scan under POAM-020) | Supplier item, store, sales, inventory, order, and deduction data; supplier user contact data |
| Procedures | P06 policy hierarchy; P08 runbook; clean room output rules (POL-04 4.10) | P06; P08; supplier onboarding and offboarding |
| Subservice organizations (carved out) | Cloud provider B; ad server and clean room software vendors | Cloud provider B; ERP vendor |

## 3. Readiness results
**SL-1 retail media and data clean room**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 27 | 5 | 1 |  |
| Availability (A1, 3) | 2 | 1 |  |  |
| Confidentiality (C1, 2) | 1 | 1 |  |  |
| Processing Integrity (PI1, 5) | 2 | 3 |  |  |
| Privacy (P1-P8, 18) |  |  |  | 18 |

**SL-2 supplier collaboration portal**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 30 | 3 |  |  |
| Availability (A1, 3) | 2 | 1 |  |  |
| Confidentiality (C1, 2) | 1 | 1 |  |  |
| Processing Integrity (PI1, 5) |  |  |  | 5 |
| Privacy (P1-P8, 18) |  |  |  | 18 |

**SL-1** is not yet ready for a Type 2 period to start. Not ready: CC6.7 (clean room thresholds and payment field exclusion). Partially ready: CC2.3, CC4.1, CC6.2, CC7.2, CC8.1, A1.3, C1.2, PI1.1, PI1.3, PI1.4. The Not ready item is the same weakness the risk register and gap analysis found (P01 R-015, R-038; P03 G-081; POAM-020), and it is also the one most likely to appear as an exception in a client's review.

**SL-2** is close to ready. Partially ready: CC2.3, CC4.1, CC6.2, A1.3, C1.2. The main item is automatic disabling of inactive supplier accounts (P01 R-046), due 2027-03-31.

Both service lines share four gaps (system description and agreements, Internal Audit coverage, recovery testing, and deletion at contract end), which are fixed once for both.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC6.7, CC8.1, CC6.2 | Clean room thresholds in all templates; data contract and weekly scan; template release review (POAM-020); first client administrator attestation | Scan results; template reviews; attestations |
| 2027 Q1 | SL-1 CC2.3, CC7.2, C1.2, PI1.1, PI1.3, PI1.4, A1.3, CC4.1; SL-2 CC2.3, CC6.2, C1.2, A1.3, CC4.1 | System descriptions and security exhibits; SIEM use cases for clean room queries; deletion jobs; published methodology; attribution jobs in the pipeline; automated reconciliation; inactivity disable for supplier accounts; recovery tests for both lines | Use case alerts; deletion records; reconciliations; recovery test reports |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines) | Mock walkthrough with the service auditor; confirm all Not ready and Partially ready items closed | Walkthrough results |
| 2027 Q2 to Q3 | Type 2 period 2027-04-01 to 2027-09-30 (both lines) | Operate controls; monthly evidence review by the GRC team | All evidence map items |
| 2027 Q4 | Reports issued (2027-11) | Bridge letters for clients from 2027-10-01 | Management assertion; bridge letters |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 10 collecting, 5 ready, 10 not started (each tied to a gap above or a POA&M item).

**Client communication:** CPG clients and suppliers who ask now receive this summary, the enterprise security overview, the subservice organizations' SOC 2 reports where their terms allow, and a letter with the expected report date (2027-11). Large CPG clients whose agreements require a SOC 2 report this year receive a management representation letter describing the remediation plan.
