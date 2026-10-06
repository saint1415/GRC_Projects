# SOC 2 Readiness Summary: Cris Santos Company | Management of Companies and Enterprises | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company with four operating subsidiaries) |
| Tier / Vertical | Enterprise / Management of Companies and Enterprises |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 dealer financing platform (Finance; about 1,400 independent dealers); SL-2 connected equipment monitoring (Manufacturing; about 650 commercial customers, about 38,000 units) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, Processing Integrity, and (new) Privacy. SL-2: Security, Availability, Confidentiality |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report; Privacy added). SL-2: Type 1 as of 2027-06-30, then a first Type 2 for 2027-07-01 to 2027-12-31 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of what the group does is selling building materials, servicing homes, building equipment, and lending, none of which needs a SOC 2 report. **The shared services GBS provides to the subsidiaries also do not need one**: the subsidiaries are part of the same consolidated group, and the controls over them are covered by the SOX program and the Internal Audit plan, not by a service auditor's report.

Two service lines are different, because outside businesses rely on them and ask for a CPA's SOC 2 report:
- **SL-1 dealer financing platform (Finance).** Independent HVAC and home-improvement dealers use the portal and API to submit customers' financing applications, get decisions, sign documents, and receive funding. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality, Processing Integrity) every year since 2024; the 2025 report had no exceptions. Larger dealers and their lender partners now ask for Privacy, because the platform collects applicants' personal and credit information.
- **SL-2 connected equipment monitoring (Manufacturing).** Commercial building owners and facilities managers receive telemetry, fault alerts, and dashboards for their rooftop units. Two national property management customers made a SOC 2 Type 2 report a condition of their 2027 renewals.

**Alternatives considered:** ISO/IEC 27001 certification (customers asked specifically for SOC 2; one framework per service line is cheaper to run); relying on the cloud provider's SOC 2 report (it covers only the infrastructure, not the group's application, people, and processes). The vertical overlay names no sector-specific alternative.

**Relationship to other assurance:** the group common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the SOX program, and Finance's Safeguards Rule testing. GBS is part of the same service organization and is **included** in each system description, not carved out. Cloud provider B, the consumer reporting agencies, the e-signature provider, the ACH bank (SL-1), and the cellular connectivity provider (SL-2) are subservice organizations presented with the carve-out method; their own reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 dealer financing platform | SL-2 connected equipment monitoring |
|---|---|---|
| Services | Credit applications, decisions, documents, and funding for dealers' customers | Telemetry, fault alerts, and dashboards for commercial HVAC equipment |
| Infrastructure | Cloud provider B managed platform, second-region standby, landing zone controls (P04) | Cloud provider B managed platform; cellular connectivity to units |
| Software | Group-built dealer portal and API; decision engine; fraud model (AI-004) | Group-built device platform, dashboards, and alerting; device firmware |
| People | Finance platform engineering, underwriting, dealer support; GBS SOC, IAM, and cloud platform teams | Connected services team (28); GBS SOC, IAM, and cloud platform teams |
| Data | Applicant and borrower personal information, credit data, bank account data, dealer account data | Equipment telemetry; commercial customer business contacts |
| Procedures | P06 policy hierarchy; P08 runbook; SL-1 operating procedures | P06; P08; SL-2 operating procedures (being written) |
| Subservice organizations (carved out) | Cloud provider B; consumer reporting agencies; e-signature provider; ACH originating bank | Cloud provider B; cellular connectivity provider |

## 3. Readiness results
**SL-1 dealer financing platform**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 30 | 3 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 5 | 0 | 0 | 0 |
| Privacy (P1-P8, 18) | 15 | 3 | 0 | 0 |

**SL-2 connected equipment monitoring**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 23 | 8 | 2 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready for its next Type 2 on the existing categories, with three partially ready Security criteria that come from **shared GBS controls**, not from Finance: CC6.1 (phishing-resistant MFA for administrators, POAM-002), CC6.2 (service desk resets, POAM-001, and dealer account inactivity), and CC9.2 (vendor reassessments, POAM-012 and POAM-013). If POAM-001 is not closed before 2027-01-01, the CC6.2 control would likely produce an exception for the first weeks of the period; the description would disclose it. The Privacy gaps (P4.2, P4.3, P6.2) and C1.2 come from data retention in the warehouse (POAM-022) and the disclosure log.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC2.3 (no system description or published commitments) and CC8.1 (firmware releases outside change control). Partially ready: CC1.3, CC3.2, CC4.1, CC6.1, CC6.2, CC7.1, CC7.2, CC9.2, A1.2, C1.2. That is why the plan is a Type 1 first, as of 2027-06-30.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | Both CC6.2; SL-1 CC9.2 (Finance vendors), P6.2; SL-2 CC1.3 | Verified identity proofing at the service desk; re-tier the provider; vendor disclosures in the log; SL-2 roles | Reset tickets with proofing records; vendor reviews; disclosure log |
| 2027 Q1 | Both CC6.1; SL-1 CC9.2, C1.2, P4.2, P4.3; SL-2 CC2.3, CC3.2, CC7.1, CC7.2, CC8.1, CC9.2, C1.2 | Phishing-resistant MFA for all privileged accounts; warehouse purge; SL-2 system description and commitments; firmware change control and scanning; device telemetry use cases; carrier assurance | Purge reports; firmware release records; SOC device use case alerts |
| 2027 Q2 | SL-2 CC4.1, CC6.1, A1.2 | Internal Audit readiness review of SL-2 (2027-05); certificate rotation on older units; second carrier profile | Readiness review report; certificate inventory; carrier test |
| 2027-06-30 | SL-2 Type 1 as of this date; SL-2 Type 2 period starts 2027-07-01 | Service auditor fieldwork | Type 1 report |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. 15 items are marked "Both": they are group common controls collected once and used for both reports. Status: 12 collecting, 6 ready, 7 not started (each tied to a POA&M item or a 2027 action).

**Customer communication:** SL-1 dealers and lender partners receive the 2025 report, a bridge letter, and a letter describing the Privacy addition and the CC6.2 remediation. SL-2 customers receive this summary, the remediation timeline, and the expected Type 1 date (2027-06-30).
