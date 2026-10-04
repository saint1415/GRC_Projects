# SOC 2 Readiness Summary: Cris Santos Company | Information | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded B2B SaaS software publisher) |
| Tier / Vertical | Enterprise / Information |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criteria are cited by ID with short topic labels in our own words |
| Service lines | SL-1 Operations Cloud (about 9,800 customers); SL-2 Data Cloud (about 3,100 customers); SL-3 Conversational AI service (AQ-01, about 1,150 customers) |
| Categories in scope | SL-1: Security, Availability, Confidentiality. SL-2: Security, Availability, Confidentiality, Processing Integrity (Availability, Confidentiality, and Processing Integrity are new). SL-3: Security, Availability, Confidentiality (first report) |
| Target reports | SL-1: Type 2, period 2026-10-01 to 2027-09-30 (eighth annual report). SL-2: Type 2 with expanded categories, period 2027-04-01 to 2028-03-31. SL-3: Type 1 as of 2027-06-30, then first Type 2 for 2027-07-01 to 2027-12-31 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 183 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-14 to 2026-08-28 by the Director of Trust and Assurance and the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive; approved by the CTO 2026-09-08 |

## 1. Why SOC 2 for this organization
The company is a service organization for about 9,800 businesses, and their auditors and security teams need assurance about controls they cannot see. The MSA promises a current SOC 2 Type 2 report, and Enterprise customers, banking customers' vendor programs, and public sector buyers require one. Each product is sold separately and has its own system and subservice organizations, so each service line needs its own report.

**Alternatives considered (vertical profile):**
- **ISO/IEC 27001 certification:** the company holds it for the Operations Cloud, and some non-U.S. buyers prefer it, but U.S. customers ask for SOC 2 because it reports test results and exceptions. Both are kept and share evidence.
- **FedRAMP:** required only for federal agencies. The Government Edition holds a FedRAMP Moderate authorization, and agencies rely on it, so the Government Edition is not a SOC 2 service line here.

**Relationship to other assurance:** enterprise common controls (P02 section 10.3; P04 section 5) support all three service lines, so one set of evidence serves the three SOC 2 reports, ISO/IEC 27001, the CCPA cybersecurity audit starting in 2027, and parts of the FedRAMP package. Cloud providers A and B, the source hosting and CI service, the SIEM vendor, the support ticketing service, and the AI model providers are subservice organizations presented with the carve-out method; their SOC 2 reports are reviewed under CC9.2 (14 reviews are overdue, POAM-010).

**Relationship to P03:** P03 tests the FTC's expectations and the company's own statements. This file checks each criterion. Where the same weakness appears in both (for example, the trust page statements under CC2.3, or deletion under C1.2), both point to the same POA&M item in P07.

## 2. System descriptions (scope)
| Element | SL-1 Operations Cloud | SL-2 Data Cloud | SL-3 Conversational AI service |
|---|---|---|---|
| Services | Case management, field service, employee service desk, AI Assist | Analytics dashboards, data pipelines, customer data platform | Virtual agents for customers' chats and calls, with handoff to the Operations Cloud |
| Infrastructure | Cloud provider A, 14 cells in two regions plus a recovery region (P02) | Cloud provider B, landing zone accounts | Cloud provider B, AQ-01's own cloud organization (outside the landing zone until 2027-03-31) |
| Software | Company-built services; AI Assist orchestration calling model providers | Company-built pipelines; managed warehouse | AQ-01-built bots; fine-tuned models; speech-to-text service |
| People | Platform engineering, SRE, support, SOC, identity, cloud platform | Data Cloud engineering, SOC, identity, cloud platform | About 420 AQ-01 staff, moving onto enterprise functions |
| Data | Customer case data with end-consumer personal information | Event streams and derived analytics from customers' Operations Cloud tenants | Conversation transcripts and recordings |
| Procedures | P06 policy hierarchy; P08 runbook; support and SRE procedures | P06; P08; pipeline procedures | P06 adopted; AQ-01 procedures being rewritten |
| Subservice organizations (carved out) | Cloud provider A; CDN and DNS providers; email and SMS delivery; AI model providers; support ticketing | Cloud provider B | Cloud provider B; telephony carrier; speech-to-text provider; AI model provider |

## 3. Readiness results
**SL-1 Operations Cloud**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 24 | 9 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 Data Cloud**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 28 | 5 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 0 | 1 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-3 Conversational AI service**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 9 | 15 | 9 | 0 |
| Availability (A1, 3) | 0 | 2 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is in its period (started 2026-10-01). Partially ready: CC2.3, CC6.1, CC6.2, CC6.3, CC6.7, CC7.1, CC7.2, CC8.1, CC9.2, A1.3, C1.2. These are the same gaps Internal Audit found (P07). Items closing in the first quarter of the period (CC2.3, C1.2, CC6.7, CC7.2, CC8.1, CC7.1, CC9.2) will likely be described as exceptions for the months before they close; the CTO accepted that on 2026-09-08 rather than shorten the period, because customers expect an annual report. The two trust page statements are corrected before 2026-10-30 so the system description does not repeat them.

**SL-2** is ready to start its expanded period on 2027-04-01 if the items due by 2027-03-31 close. Not ready: C1.2 (13-month snapshots). Partially ready: CC2.3, CC3.1, CC6.2, CC6.3, CC9.2, A1.3, PI1.1, PI1.3, PI1.4.

**SL-3** is not ready for a Type 2 period. Not ready: CC2.3, CC3.1, CC6.1, CC6.3, CC6.6, CC6.7, CC7.1, CC7.2, CC7.5, A1.3, C1.1. Partially ready: CC1.3, CC1.4, CC2.1, CC3.4, CC4.1, CC5.1, CC5.2, CC5.3, CC6.2, CC6.8, CC7.3, CC7.4, CC8.1, CC9.1, CC9.2, A1.1, A1.2, C1.2. Most gaps follow from AQ-01 running outside the enterprise platform. The plan is a Type 1 as of 2027-06-30, after the landing zone migration, then a six-month Type 2 from 2027-07-01. The entity-level criteria (CC1.1, CC1.2, CC1.5, CC2.2, CC3.2, CC3.3, CC4.2) are ready because enterprise controls have applied to AQ-01 since 2025-10.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC2.3, C1.2, CC6.7, CC7.2, CC8.1, CC7.1, CC9.2; SL-3 CC2.3, C1.1, CC7.1, CC6.6 (guardrails), CC6.7, CC6.3 | Trust page correction (POAM-021); offboarding reconciliation (POAM-011); minimized export and detections (POAM-001, POAM-003); change review gate (POAM-009); image deploy gate (POAM-008); overdue vendor reviews (POAM-010); stop AQ-01 pooled training (POAM-020); AQ-01 guardrails (POAM-019) | Statement reviews; deletion reconciliations; export configuration; SOC cases; vendor reviews; model training register |
| 2027 Q1 | SL-1 CC6.1, CC6.2, CC6.3, A1.3; SL-2 CC2.3, CC3.1, C1.2, A1.3, PI1.1, PI1.3, PI1.4; SL-3 CC6.1, CC6.2, CC5.2, CC3.1 | Tenant access tool rebuild (POAM-004); non-human identities (POAM-005); Cell 4 retest (POAM-007); Data Cloud system description and snapshot lifecycle (POAM-022); pipeline reconciliation; AQ-01 federation and key removal (POAM-002); AQ-01 landing zone migration | Recordings and approvals; certifications; DR retest; snapshot records; reconciliation reports; federation records |
| 2027 Q1 (March) | Readiness check by Internal Audit for SL-2 and SL-3 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | SL-2 period starts 2027-04-01; SL-3 A1.3, CC7.5 (DR test by 2027-05-31); SL-3 Type 1 as of 2027-06-30 | AQ-01 DR test; SL-3 system description final | DR test report; Type 1 report |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "All" or naming more than one service line are enterprise common controls collected once and used for every report. Status: 15 collecting, 1 ready, 9 not started (each tied to a POA&M item or a 2027 action).

**Customer communication:** SL-1 customers receive the 2025-2026 report (period ended 2026-09-30, report expected 2026-11-30) and a bridge letter; SL-2 customers receive the current Security-only report, a bridge letter, and the expected date of the expanded report (2028-05); SL-3 customers receive this readiness summary under NDA, the enterprise ISO/IEC 27001 certificate scope statement (which does not yet cover AQ-01), and the planned Type 1 date (2027-08).
