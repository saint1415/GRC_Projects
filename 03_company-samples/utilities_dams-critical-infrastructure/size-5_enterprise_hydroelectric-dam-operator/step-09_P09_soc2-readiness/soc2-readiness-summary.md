# SOC 2 Readiness Summary: Cris Santos Company | Dams | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded hydroelectric generation company) |
| Tier / Vertical | Enterprise / Dams |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Topic labels in the CSV are short descriptions in the company's own words, not the criteria text |
| Service lines | SL-1 contract remote operations (27 non-BES plants of 11 client dam owners, from the Contract Operations Center); SL-2 dam safety monitoring (DSMS: 138 client dams of 46 clients) |
| Categories in scope | SL-1: Security, Availability, Confidentiality. SL-2: Security, Availability, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (21 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's work is running its own dams and selling power, which SOC 2 does not cover; the generation business answers to FERC and NERC (P03). Two service lines are different: the company **provides services to other dam owners**, so it is a service organization for them, and they ask for a CPA's SOC 2 report.
- **SL-1 contract remote operations.** The Contract Operations Center monitors 27 non-BES plants of 11 clients around the clock and operates them on the owner's instruction through client-owned VPN endpoints. Several client plants have gated spillways, so a security failure here could affect a client's dam. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2024.
- **SL-2 dam safety monitoring.** The DSMS collects instrument readings from 138 client dams and alerts clients when trigger points are exceeded; it also runs the AI-001 anomaly detection model (P10). Clients rely on it as part of their own dam safety surveillance. They now ask for a SOC 2 Type 2 report including **Processing Integrity**, because alert accuracy and timeliness are the core commitment.

**Alternatives considered:** a SOC 1 report (not relevant: neither service affects clients' financial reporting); ISO/IEC 27001 certification (some clients accept it, but most U.S. dam owners and their insurers ask for SOC 2); relying on the company's NERC CIP and FERC programs (they cover the company's own assets, not the services it sells, and clients cannot rely on them as assurance).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 6) support both service lines, so one set of evidence serves both reports, the SOX program, and the CIP program where they overlap. Cloud provider B, the cellular carriers, and colocation providers are subservice organizations presented with the carve-out method; their SOC reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 contract remote operations | SL-2 dam safety monitoring |
|---|---|---|
| Services | 24x7 monitoring of 27 client plants; operation on documented owner instructions; alarm response and client call-out | Data collection from client dataloggers; trigger-point checks; alerts; AI-001 anomaly scores (advisory); client portal and reports |
| Infrastructure | COC in Georgia on its own network (no path to the HFCDMS); client-owned VPN endpoints; client portal on Cloud provider B | Cloud provider B containers in two regions; landing zone controls (P04) |
| Software | Commercial monitoring and HMI software; company-built client portal | Company-built DSMS; managed machine learning service for AI-001 |
| People | 34 COC operators; Hydro Services engineers; SOC | 48 DSMS analysts and data engineers; dam safety engineers; SOC |
| Data | Client plant status, alarms, operating logs (client CEII) | Client instrument readings, trigger points, inundation-related data (client CEII) |
| Procedures | P06 policy hierarchy; P08 runbook; COC operating procedures; owner instruction procedure | P06; P08; DSMS operating and alert procedures; AI council process (P10) |
| Subservice organizations (carved out) | Cloud provider B (portal); colocation for COC backups | Cloud provider B; cellular carriers for client dataloggers |

## 3. Readiness results
**SL-1 contract remote operations**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 31 | 2 | 0 | 0 |
| Availability (A1, 3) | 1 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 dam safety monitoring**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 29 | 3 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready for its next Type 2 on the existing categories except for CC6.1, CC6.2, A1.2, A1.3 (partially ready). There are two causes: 6 of 27 client endpoints still accept shared COC credentials (CC6.1, CC6.2; POAM-021), and the backup operating position at HOC-B has never been tested for SL-1 (A1.2, A1.3). Both are due before 2027-03-01, so the 2027 period can start on time; if the endpoint work slips, the report would describe the exception for the affected months.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC8.1. Partially ready: CC1.3, CC2.3, CC3.1, A1.3, PI1.1, PI1.3, PI1.4. The root cause is the same one P01 rated High (R-042): alert thresholds and AI-001 model versions change inside the application without formal change control, so the service auditor could not test that the alerts clients rely on behave as designed. Closing POAM-019 by 2026-12-31 and POAM-020 by 2027-01-31, and finalizing the system description by 2027-01-31, makes SL-2 ready to start its period on 2027-04-01.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-2 CC8.1, PI1.3; SL-1 CC6.1, CC6.2; SL-2 CC1.3 | Threshold and model change workflow (POAM-019); named credentials at the 6 endpoints (POAM-021); SL-2 RACI | Change records; endpoint credential register |
| 2027 Q1 | SL-2 CC2.3, CC3.1, PI1.1, PI1.4, A1.3; SL-1 A1.2, A1.3 | System description with AI-001 limits; alert delivery reconciliation; DSMS DR retest (POAM-020); SL-1 HOC-B backup test | System description; delivery reconciliation; DR reports |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines); SL-2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 onward | Operate and collect | Quarterly evidence reviews by the GRC team | Evidence map items |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once for both reports. Status: 10 collecting, 5 ready, 6 not started (each tied to a POA&M item or a dated action).

**Client communication:** SL-1 clients receive the 2025 report, a bridge letter, and a note on the credential changes at their endpoints; SL-2 clients receive this summary, a bridge letter describing the remediation, a plain statement that AI-001 alerts are advisory and never replace trigger-point checks (P10), and the expected SL-2 report date (2027-11).
