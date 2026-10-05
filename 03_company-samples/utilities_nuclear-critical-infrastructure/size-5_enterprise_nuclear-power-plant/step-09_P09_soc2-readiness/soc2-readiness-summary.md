# SOC 2 Readiness Summary: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded nuclear generation company) |
| Tier / Vertical | Enterprise / Nuclear Reactors, Materials, and Waste |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Service lines | SL-1 monitoring and diagnostics (about 9,600 non-safety equipment points for the fleet and 6 external generation owners, 14 plants); SL-2 dosimetry processing (NVLAP-accredited processor, about 46,000 dosimeters a quarter, about 70% for about 140 external licensees) |
| Categories in scope | SL-1: Security, Availability, Confidentiality. SL-2: Security, Availability, Confidentiality, Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (the 2025 report was issued; the 2026 period is under way). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive; updated 2026-09-04 with Internal Audit results (P07) |

## 1. Why SOC 2 for this organization
Most of the company's work is generating electricity, which SOC 2 does not cover. Two service lines are different: the company **provides services to other businesses**, so it is a service organization for them, and their clients ask for a CPA's SOC 2 report.
- **SL-1 monitoring and diagnostics.** The fleet M&D center watches non-safety equipment for 6 outside generation owners (14 plants, including 2 nuclear plants owned by others) as well as the company's own seven units. Clients send equipment data outbound from their plants; the company never connects to client control systems. Clients' supplier programs require a SOC 2 Type 2 report on Security, Availability, and Confidentiality, and SL-1 has issued one since the 2025 period.
- **SL-2 dosimetry processing.** Hospitals, universities, industrial radiography firms, and other nuclear plants send dosimeters for processing. Their licenses require processing by an NVLAP-accredited processor (10 CFR 20.1501(d)), which the laboratory is, but NVLAP accreditation addresses measurement quality, not IT controls. The larger clients now ask for a SOC 2 Type 2 report with **Processing Integrity**, because an accurate dose of record is the core commitment.

**Alternatives considered:** ISO/IEC 27001 certification (some international generation clients accept it, but the US clients ask for SOC 2, and one framework per service line is cheaper to run); NVLAP accreditation for SL-2 (required and kept, but it complements SOC 2 rather than replacing it).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04) support both service lines, so one set of evidence serves both reports, the SOX program, and the Internal Audit plan. Cloud provider B, the DC-2 colocation provider, and the M&D analytics vendor are subservice organizations presented with the carve-out method; their own SOC reports are reviewed under CC9.2. The station CDA programs are outside both systems.

## 2. System description (scope)
| Element | SL-1 monitoring and diagnostics | SL-2 dosimetry processing |
|---|---|---|
| Services | Equipment condition monitoring, anomaly advisories, and engineering reports for client plants | Dosimeter processing, dose reports, and dose history for client licensees' workers |
| Infrastructure | M&D platform on Cloud provider B (SYS-12), landing zone controls (P04) | Dosimeter readers and the dose record database in DC-1 (SYS-13), replicas in DC-2; client portal on Cloud provider B |
| Software | Company-built analytics and models (including AI-001 models used for the fleet); vendor analytics service | Commercial dosimetry software; company-built client portal |
| People | M&D center engineers and analysts; SOC; identity and cloud platform teams | Laboratory staff; client services; SOC; DC-1 operations |
| Data | Client equipment sensor data and engineering reports (Confidential); no personal information | Client worker names, identifiers, and dose results (Confidential personal information) |
| Procedures | P06 policy hierarchy; P08 runbook; M&D center procedures | P06; P08; NVLAP quality manual and laboratory procedures |
| Subservice organizations (carved out) | Cloud provider B; M&D analytics vendor | Cloud provider B; DC-2 colocation provider |

## 3. Readiness results
**SL-1 monitoring and diagnostics**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 32 | 1 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) |  |  |  | 5 |
| Privacy (P1-P8, 18) |  |  |  | 18 |

**SL-2 dosimetry processing**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 26 | 7 | 0 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) |  |  |  | 18 |

**SL-1** is ready for its next Type 2 period on the existing categories, with one carry-over: the M&D analytics vendor receives client data without a security addendum or a SOC report (partially ready: CC9.2, C1.1). POAM-016 closes it by 2027-03-31. If it is still open at the start of the period, the report will describe the vendor as a subservice organization without its own report, and clients will see that.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: A1.3. Partially ready: CC2.3, CC4.1, CC6.1, CC6.6, CC6.7, CC7.5, CC8.1, A1.2, C1.1, PI1.1, PI1.5. The central gap is that the dose record database has never been restored from backup (POAM-019), which affects recovery (CC7.5, A1.2, A1.3) and stored data integrity (PI1.5). The other gaps are older client agreements and identifiers, the client portal penetration test, report delivery by email, change records for dose algorithm and reader firmware, and the missing system description. Closing them by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-2 CC7.5, A1.2, A1.3, PI1.5; SL-1 C1.1; both CC7.4 | Dose record restore test (POAM-019); M&D analytics vendor addendum (POAM-016); disclosure committee tabletop (POAM-013) | Restore test report; signed addendum; tabletop report |
| 2027 Q1 | SL-2 CC2.3, CC4.1, CC6.1, CC6.6, CC6.7, CC8.1, PI1.1, C1.1; SL-1 CC9.2 | SL-2 system description; Internal Audit readiness assessment; portal penetration test; identifier migration; encrypted report delivery; change record linkage; vendor SOC 2 report or equivalent | Description; readiness report; test report; migration records |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines) | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | SL-2 Type 2 period starts 2027-04-01; SL-1 2027 period under way | Monthly evidence collection per the evidence map | All recurring evidence |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 11 collecting, 7 ready, 7 not started (each tied to a POA&M item or a 2027 Q1 action).

**Client communication:** SL-1 clients receive the 2025 report, a bridge letter, and a note on the vendor addendum; SL-2 clients receive this summary, a letter describing the remediation, and the expected first report date (2027-11).
