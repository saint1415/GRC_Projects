# SOC 2 Readiness Summary: Cris Santos Company | Critical Manufacturing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded power and distribution transformer manufacturer) |
| Tier / Vertical | Enterprise / Critical Manufacturing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Service lines | SL-1 Fleet Monitoring Service (FMS; about 60 utility subscribers, 14,500 monitored transformers); SL-2 Spare Transformer Reserve Service (STRS; 27 utility members, 64 spare large power and generator step-up transformers in 3 yards) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and (new) Processing Integrity. SL-2: Security, Availability, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (third annual report; Processing Integrity added). The second report, for calendar 2026, is under way on the existing three categories. SL-2: first Type 2, period 2027-04-01 to 2027-09-30, report expected 2027-11 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-17 to 2026-09-04 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's revenue comes from building and servicing transformers, which SOC 2 does not cover: utilities buy equipment, and their own controls do not depend on company systems. Two service lines are different. The company **operates systems on behalf of utilities**, so it is a service organization for them, and their vendor programs ask for a CPA's SOC 2 report.
- **SL-1 Fleet Monitoring Service.** Utilities push monitoring data from their own data platforms to the FMS, which returns condition analytics and advisories. Subscription agreements commit to 99.5% monthly portal availability, confidentiality of utility data, and condition advisories within 24 hours of a high-severity alert. SL-1 received its first SOC 2 Type 2 report (Security, Availability, Confidentiality) for 2025, with one exception (a late access removal, remediated). Subscribers now ask for **Processing Integrity**, because the value of the service is advisories that are complete, accurate, and on time.
- **SL-2 Spare Transformer Reserve Service.** Members rely on the company's registry and dispatch process to reserve and receive a spare large power transformer after an emergency. Member agreements commit to a dispatch decision within 24 hours of a qualifying request, accurate reservation and allocation records, and confidentiality of member asset data. **Five members asked for a SOC 2 Type 2 report by 2027-12-31**, including Processing Integrity.

**Alternatives considered:**
- **Answering each utility's questionnaire separately.** The 88 addendum utilities already send their own supplier questionnaires under their CIP-013-2 supply chain programs. A SOC 2 report for the two service lines answers many of those questions once and is what the five STRS members asked for.
- **ISO/IEC 27001 certification.** A private standard that certifies the management system but does not report on the operating effectiveness of controls over a period. Members asked specifically for SOC 2 Type 2.
- **ISA/IEC 62443 certification of the TMU product.** A private OT and product security standard. Relevant to the TMU product, not to the service lines; considered separately by the Director of Product Security.
- **A SOC report for the whole company.** Rejected: the manufacturing business has no user entities whose controls depend on it.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04) support both service lines, so one set of evidence serves both reports, the SOX IT general controls, and the Internal Audit assessment (P07). The cloud providers, the notification service, and the EDI provider are subservice organizations presented with the carve-out method; their own SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 Fleet Monitoring Service | SL-2 Spare Transformer Reserve Service |
|---|---|---|
| Services | Ingest of utility-pushed monitoring data; condition analytics; advisories; subscriber portal | Spare reservation, allocation, and dispatch decisions; member portal; storage and readiness of spare units |
| Infrastructure | Cloud provider B managed containers and data services; second-region warm standby; landing zone controls (P04). **No connection into utility networks or to TMUs** | Cloud provider A member portal; spare registry in the ERP (inherits EPSP controls, P02); 3 spare yards (Florida, Tennessee, Texas) |
| Software | Company-built ingestion, analytics (AI-003), and portal | Company-built member portal; ERP spare asset module |
| People | Digital Services team (180); SOC; identity and cloud platform teams | Spares and services desk; yard managers; field service crews; EPSP team; SOC |
| Data | Utility asset health data for about 14,500 transformers (about 2,100 made by other manufacturers); subscriber user contacts | Member asset data; reservation and allocation records; spare unit condition records |
| Procedures | P06 policy hierarchy; P08 runbook (section 7A); FMS operations procedures | P06; P08; member handbook; dispatch procedure |
| Subservice organizations (carved out) | Cloud provider B; notification service | Cloud provider A; heavy-haul carriers and rigging contractors (for delivery, outside the system boundary) |

## 3. Readiness results
**SL-1 Fleet Monitoring Service**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 33 | 0 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 Spare Transformer Reserve Service**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 24 | 6 | 3 | 0 |
| Availability (A1, 3) | 1 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

Privacy is not selected for either line: both process utility asset and operational data, and personal information is limited to business contact details of customer users.

**SL-1** is ready for its next Type 2 on the existing categories. The new Processing Integrity criteria have 3 partially ready items (PI1.2, PI1.3, PI1.4): feed-gap alerts for subscriber data, documented validation of AI-003 model releases (P10), and a report that proves the 24-hour advisory commitment for every high-severity alert.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC6.3, CC6.4, CC8.1. Partially ready: CC2.3, CC3.1, CC6.1, CC6.2, CC7.5, CC9.2, A1.2, A1.3, PI1.1, PI1.3, PI1.4. Most gaps are inherited from the EPSP, because the spare registry lives in the ERP: separation of duties (P07 AC-5), change approval (P07 CM-3), and recovery time (P07 CP-10). The rest are specific to the service: spare yard physical security (POAM-023), the untested manual dispatch fallback (POAM-024), written allocation rules, and a monthly reconciliation of the registry to the units in the yards. Closing POAM-001, POAM-003, POAM-006, POAM-014, POAM-023, and POAM-024 by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-2 CC3.1, CC6.1, CC6.2, CC6.3, CC8.1, PI1.1, PI1.3; SL-1 PI1.4 | Commitments register; member administrator attestations and portal inactivity disablement; split reservation and allocation roles and enforce ERP change approval (POAM-001, POAM-003); written allocation rules; FMS advisory timer | Attestations; role matrix; change workflow records; advisory timer reports |
| 2027 Q1 | SL-2 CC2.3, CC6.4, CC7.5, CC9.2, A1.2, A1.3, PI1.4; SL-1 PI1.2, PI1.3 | SL-2 system description; yard intrusion detection and CCTV (POAM-023); ERP failover retest with the STRS registry and manual dispatch test (POAM-006, POAM-024); vendor reviews (POAM-014); monthly yard reconciliation; FMS feed-gap alerts; AI-003 validation step | Retest report; yard monitoring records; reconciliations; model validation records |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines); SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 to Q4 | SL-1 period runs all year; SL-2 period ends 2027-09-30 | Quarterly evidence reviews by the GRC team | Quarterly evidence packages |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 13 collecting, 5 ready, 7 not started (each tied to a POA&M item or a 2026 Q4 or 2027 Q1 action).

**Customer communication:** FMS subscribers receive the 2025 report, a bridge letter, and a Processing Integrity roadmap letter; STRS members receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11), ahead of the five members' 2027-12-31 request.
