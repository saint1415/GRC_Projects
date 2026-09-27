# SOC 2 Readiness Summary: Cris Santos Company | Health Care | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-specialty medical group) |
| Tier / Vertical | Enterprise / Health Care and Social Assistance |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 patient-app platform (licensed to about 45 independent practices); SL-2 lab reference testing (about 260 client practices) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and (new) Privacy. SL-2: Security, Availability, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report; Privacy added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the group's work is patient care, which SOC 2 does not cover. Two service lines are different: the group **provides services to other businesses**, so it is a service organization for them, and their clients ask for a CPA's SOC 2 report.
- **SL-1 patient-app platform.** Independent practices license the white-labeled app for scheduling, messaging, results viewing, and bill pay. The group is their HIPAA business associate. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2024; the 2025 report had one exception (a late access removal), since remediated. Several clients now ask for Privacy because the app collects consents and preferences directly from their patients.
- **SL-2 lab reference testing.** Client practices and two regional health systems send specimens and receive results through the outreach portal and interfaces. The health systems' vendor programs now require a SOC 2 Type 2 report including **Processing Integrity**, because result accuracy is the core commitment.

**Alternatives considered:** HITRUST certification (common in health care; the health systems accept SOC 2 with Processing Integrity, and one assessment framework per service line is cheaper to run); CLIA and accreditation inspections (they address test quality, not IT controls, so they complement SOC 2 rather than replace it).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports and the HIPAA and SOX programs. The cloud providers and the EHR vendor are subservice organizations presented with the carve-out method; their own SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 patient-app platform | SL-2 lab reference testing |
|---|---|---|
| Services | Scheduling, secure messaging, results viewing, bill pay for client practices' patients | Test ordering, specimen tracking, testing, result reporting for client practices |
| Infrastructure | Cloud provider B managed containers, second-region standby, landing zone controls (P04) | Cloud provider A LIS workload account, interface engines, outreach portal; central lab on-premises segment (P02) |
| Software | Group-built app and APIs; cloud AI service for the virtual assistant (AI-008) | Commercial LIS; instrument middleware; outreach portal |
| People | Digital health team; SOC; identity and cloud platform teams | Lab staff; LIS team; client services; SOC |
| Data | Client patients' demographics, messages, results displays, payment tokens (card data handled by a payment processor) | Orders, specimens, results for client patients |
| Procedures | P06 policy hierarchy; P08 runbook; SL-1 support procedures | P06; P08; lab procedures and validation plan |
| Subservice organizations (carved out) | Cloud provider B; messaging and notification services; payment processor | Cloud provider A; LIS vendor (remote support); courier and specimen tracking service |

## 3. Readiness results
**SL-1 patient-app platform**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 33 | 0 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | 15 | 3 | 0 | 0 |

**SL-2 lab reference testing**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 18 | 13 | 2 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 2 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready for its next Type 2 on the existing categories. The new Privacy criteria have 3 partially ready items (P3.2, P4.2, P6.2): central consent records, per-client retention, and an automated disclosure log.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC6.3, CC8.1, PI1.3. Partially ready: CC1.3, CC2.3, CC3.1, CC3.3, CC6.1, CC6.2, CC6.6, CC6.7, CC6.8, CC7.1, CC7.2, CC7.5, CC9.2, A1.3, PI1.1, PI1.4. The gaps are the same ones Internal Audit found in the LIS (P07): client account management, change control for autoverification rules, result reconciliation, recovery time, and vendor assurance. Closing POAM-002, POAM-003, POAM-006, POAM-007, POAM-011, and POAM-015 by 2027-03-31 makes SL-2 ready to start its period. Items that close later (CC2.3, CC6.8, CC7.1, due 2027-06-30) have compensating controls today and would be described in the report if still open when the period starts.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-2 CC6.1, CC6.2, CC6.3, CC8.1, CC3.3, CC9.2 | Portal account cleanup and MFA; lab change board and role split; fraud scenario; vendor assurance | Inactivity job reports; attestations; change board minutes; vendor reviews |
| 2027 Q1 | SL-2 CC1.3, CC3.1, CC6.6, CC6.7, CC7.2, CC7.5, A1.3, PI1.1, PI1.3, PI1.4; SL-1 P3.2, P4.2, P6.2 | SL-2 system description; AQ SD-WAN migration; lab TLS; SIEM integrity use case; DR retest; rule attribution; reconciliation; SL-1 privacy tooling | DR retest report; reconciliation reports; consent and disclosure logs |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines); SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | Remaining SL-2 partially ready items (CC2.3, CC6.8, CC7.1), due 2027-06-30 | Analyzer workstation replacement; client agreement renewals | Replacement records; amended agreements |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 11 collecting, 7 ready, 7 not started (each tied to a POA&M item or a 2027 Q1 action).

**Client communication:** SL-1 clients receive the 2025 report, a bridge letter, and a Privacy roadmap letter; SL-2 clients and the two health systems receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11).
