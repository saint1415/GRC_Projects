# SOC 2 Readiness Summary: Cris Santos Company | Manufacturing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded connected medical device manufacturer) |
| Tier / Vertical | Enterprise / Manufacturing (NAICS 334510) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Service lines | SL-1 DDC hospital services (about 2,300 hospitals); SL-2 Remote Cardiac Monitoring service (about 5,200 practices and hospitals) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and (new) Processing Integrity. SL-2: all five categories: Security, Availability, Confidentiality, Processing Integrity, and Privacy |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report; Processing Integrity added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-24 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's revenue comes from selling devices, which SOC 2 does not cover. Two service lines are different: the company **operates systems that hold customers' data and deliver services to them**, so it is a service organization for those customers, and their vendor programs ask for a CPA's SOC 2 report.
- **SL-1 DDC hospital services.** Remote viewing, secondary alarm notifications, EHR interfaces, drug library and firmware distribution, and the ultrasound image archive. The company is each hospital's business associate. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2023; the 2025 report had no exceptions. Hospital pharmacy and biomedical engineering groups now ask for **Processing Integrity**, because drug library delivery and result delivery to EHRs must be complete and accurate.
- **SL-2 RCM service.** ECG monitoring with technician review and urgent physician notification. Two large health systems require a SOC 2 Type 2 report by 2027 that includes **Processing Integrity** (report accuracy and turnaround) and **Privacy**, because the company handles patient enrollment communications on their behalf.

**Why Privacy is out of scope for SL-1 and in scope for SL-2.** For SL-1 the company never deals with patients; its privacy duties are the business associate terms, which the Security and Confidentiality criteria already cover. For SL-2 the company enrolls patients, runs the phone gateway app, and sends notices the health systems delegated to it, so its privacy commitments are directly testable.

**Alternatives considered:** HITRUST certification (some hospital customers accept it, but most accept SOC 2 and one framework per service line is cheaper to run); FDA inspections and the QMS (they address device quality, not the service commitments customers rely on, so they complement SOC 2 rather than replace it).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the HIPAA program, and SOX. Cloud provider A and the ticketing and notification vendors are subservice organizations presented with the carve-out method; their own SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 DDC hospital services | SL-2 RCM service |
|---|---|---|
| Services | Remote viewing, secondary alarms, EHR interfaces, drug library and firmware distribution, image archive | ECG ingestion, arrhythmia algorithm (AI-002), technician review, reports, urgent physician calls |
| Infrastructure | Cloud provider A DDC workload accounts, landing zone controls (P04); DG-10 gateways at hospitals (customer-hosted, company-maintained) | Cloud provider A RCM workload accounts; technician virtual desktops; two monitoring centers |
| Software | Company-built DDC services; update service | Company-built RCM platform; CR-100 phone gateway app |
| People | Digital health team; site reliability; SOC; identity and cloud platform teams | 700 RCM staff; RCM platform team; SOC |
| Data | Telemetry, alarms, results, pump events, images (PHI for hospitals) | ECG data, events, reports, patient contact details (PHI for practices and hospitals) |
| Procedures | P06 policy hierarchy; P08 runbook; SL-1 operating procedures | P06; P08; RCM clinical operating procedures |
| Subservice organizations (carved out) | Cloud provider A; notification service; content delivery network | Cloud provider A; telephony carriers; ticketing vendor |

## 3. Readiness results
**SL-1 DDC hospital services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 31 | 2 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 RCM service**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 28 | 5 | 0 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | 14 | 4 | 0 | 0 |

**SL-1** is ready for its next Type 2 on the existing categories, with two Security items partially ready: CC8.1 (firmware releases reached the update service before PLM approval, P07 CM-3) and CC9.2 (five inherited subcontractors without BAAs). The new Processing Integrity criteria have two partially ready items: PI1.1 (EHR interface specifications 81% complete) and PI1.4 (first-generation IV-300 drug libraries are unsigned, so delivery cannot be verified end to end).

**SL-2** is not yet ready for a Type 2 period to start. Not ready: A1.3 (the 2026-04-18 DR test missed the 2-hour RTO). Partially ready: CC2.3, CC6.3, CC7.5, CC9.1, CC9.2, A1.2, C1.2, PI1.1, PI1.3, P1.1, P4.2, P4.3, P6.4. Closing POAM-026 (RCM recovery) and POAM-022 (subcontractor BAAs), drafting the SL-2 system description, and completing the retention register by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01. PI1.3 (AI-002 subgroup monitoring) closes by 2027-03-31 under P10.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 and SL-2 CC9.2, P6.4; SL-2 CC9.1, P1.1 | Subcontractor BAAs (POAM-022); RCM continuity plan update; delegated notice content with the second health system | Signed BAAs; updated plan; notice records |
| 2027 Q1 | SL-1 CC8.1, PI1.1; SL-2 CC2.3, CC6.3, CC7.5, A1.2, A1.3, C1.2, PI1.1, PI1.3, P4.2, P4.3 | Promotion gate for all lines (POAM-010); interface specifications; SL-2 system description; mover automation; RCM recovery automation and retest (POAM-026); retention register and automation; AI-002 subgroup monitoring | Release records; DR retest report; retention logs; monitoring reports |
| 2027 Q1 (March) | Readiness check by Internal Audit for SL-2 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | SL-1 PI1.4 | Signed library check and module swap progress (POAM-023); described as a carve-out limitation if still open when the SL-1 period starts | Delivery confirmations for signed libraries |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 14 collecting, 4 ready, 7 not started (each tied to a POA&M item or a 2027 Q1 action).

**Customer communication:** SL-1 customers receive the 2025 report, a bridge letter, and a note on the Processing Integrity addition; SL-2 customers and the two health systems receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11).
