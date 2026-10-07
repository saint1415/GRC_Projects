# SOC 2 Readiness Summary: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded staffing and workforce solutions company) |
| Tier / Vertical | Enterprise / Administrative and Support and Waste Management and Remediation Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs are listed with short topic labels in our own words; the criteria text is not reproduced |
| Service lines | SL-1 Workforce Management Platform (about 60 managed service provider clients, about 2,300 supplier firms); SL-2 payrolling and employer-of-record services (about 340 clients, about 6,000 client-sourced workers a week) |
| Categories in scope | All five categories were assessed for each line. SL-1: Security, Availability, Confidentiality, and (new) Processing Integrity; Privacy not applicable (see section 1). SL-2: Security, Availability, Confidentiality, Processing Integrity, and Privacy |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report; Processing Integrity added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (26 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the firm's work is supplying temporary labor, which SOC 2 does not cover: the firm is the associates' employer, not a service organization processing client data. Two service lines are different, because in them the firm **operates a system that processes client information on the client's behalf**:
- **SL-1 Workforce Management Platform (WMP).** Large clients run their whole contingent labor program on the firm's own vendor management system: requisitions, supplier firms' submittals, worker onboarding records, time, and consolidated invoicing. Client finance teams rely on the WMP's invoice calculations, and their procurement teams require a SOC 2 Type 2. SL-1 has issued a Type 2 report (Security, Availability, Confidentiality) every year since 2024; the 2025 report had no exceptions. Clients now ask for **Processing Integrity**, because the WMP computes the invoices they pay.
- **SL-2 payrolling and employer-of-record.** Clients recruit workers themselves and send them to the firm to be hired, onboarded, and paid through the firm's payroll engine. Clients rely on the firm to pay those workers accurately and on time and to protect their data, so their vendor programs ask for a SOC 2 Type 2 including **Processing Integrity**. Because the firm is the workers' W-2 employer and collects their personal information directly, **Privacy** applies to SL-2.

**Why Privacy is not applicable to SL-1.** In the WMP, supplier firms and clients collect worker information and give the privacy notices; the WMP stores and processes it for them. The firm's commitments to clients about that information are tested under Confidentiality. This was confirmed with the service auditor in the 2026 planning meeting.

**Alternatives considered:** a SOC 1 report for SL-2 (some clients' auditors ask whether payrolling affects their financial reporting; the firm will offer a SOC 1 Type 2 for SL-2 in 2028 if more than 10 clients ask); ISO/IEC 27001 certification (requested by two multinational SL-1 clients; the firm maps its controls but is not pursuing certification now).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports and the SOX program. The cloud providers, the paycard program manager, and the payroll tax filing service are subservice organizations presented with the carve-out method; their own SOC reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 Workforce Management Platform | SL-2 payrolling and employer-of-record |
|---|---|---|
| Services | Requisitions, supplier submittals, worker onboarding records, time approval, consolidated invoicing and supplier remittance | Hiring, onboarding (Form I-9, E-Verify, tax forms), weekly pay, tax filing, W-2s, and client pay reports for client-sourced workers |
| Infrastructure | Cloud provider A managed containers, second-region warm standby, landing zone controls (P04) | The ALPP: payroll engine on Cloud provider A, integration platform, SFTP staging, SaaS onboarding and time capture (P02) |
| Software | Firm-built WMP application and APIs | Commercial staffing back-office software (customer-managed); vendor SaaS for onboarding and time capture; client intake integrations |
| People | WMP product and engineering; client program teams; SOC | Payrolling services team; payroll operations; Treasury; SOC |
| Data | Client requisitions, rate cards, worker names, credentials, time, invoices | Worker SSNs, bank accounts, tax data, Form I-9 records, hours, rates, pay registers |
| Procedures | P06 policy hierarchy; P08 runbook; WMP support procedures | P06; P08; payroll procedures; PRC-09 employment compliance procedures |
| Subservice organizations (carved out) | Cloud provider A; email and notification services | Cloud provider A; onboarding and time capture SaaS vendors; banks and the paycard program manager; payroll tax filing service |

## 3. Readiness results
**SL-1 Workforce Management Platform**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 32 | 1 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 payrolling and employer-of-record**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 23 | 8 | 2 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 2 | 1 | 0 |
| Privacy (P1-P8, 18) | 15 | 3 | 0 | 0 |

**SL-1** is ready for its next Type 2 on the existing categories. The two partially ready items are CC9.2 (supplier firms that upload worker documents have no incident notice term) and PI1.1 (invoice processing specifications are not kept in one controlled document per client program). Both close by 2027-03-31; the 2027 period can start on 2027-01-01 with these described as being remediated.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC6.3, CC8.1, PI1.2. Partially ready: CC1.3, CC2.3, CC3.1, CC6.1, CC6.6, CC7.2, CC7.5, CC9.2, A1.3, C1.2, PI1.3, PI1.4, P4.2, P4.3, P6.4. These are the same weaknesses Internal Audit found in the ALPP (P07): pay rule separation of duties and change approval, intake validation, pay file integrity, associate sign-in, detection, recovery time, vendor assurance, and retention. Closing POAM-015, POAM-019, POAM-009, POAM-010, POAM-016, and POAM-020 by 2027-03-31, and writing the SL-2 system description, makes SL-2 ready to start its period on 2027-04-01. POAM-001 (associate sign-in) closes 2027-01-31 and POAM-005 (retention purges) by 2027-06-30; the purge gap has a compensating control (access to records past retention is limited and logged) and would be described in the report if still open when the period starts.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-2 CC6.3, CC8.1, PI1.3, PI1.4, CC9.2, P6.4, CC7.2 | Role split and second-approver workflow (POAM-015); pay file hashing (POAM-019); paycard SOC review (POAM-009); bulk export detection (POAM-016) | Role assignments; change approvals; hash verification logs; vendor review record; SOC alert dispositions |
| 2027 Q1 | SL-2 CC1.3, CC2.3, CC3.1, CC6.1, CC6.6, CC7.5, A1.3, PI1.2; SL-1 CC9.2, PI1.1 | SL-2 system description; associate passkeys (POAM-001); DR retest (POAM-010); intake validation (POAM-020); supplier agreement update; SL-1 processing specifications | DR retest report; intake exception queue; system description; supplier agreements |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines); SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | SL-2 C1.2, P4.2, P4.3 | Retention purges live (POAM-005), due 2027-06-30 | Purge logs; disposal certificates |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 13 collecting, 4 ready, 9 not started (each tied to a POA&M item or a 2027 Q1 action).

**Client communication:** SL-1 clients receive the 2025 report, a bridge letter, and a note that Processing Integrity joins the 2027 report; SL-2 clients receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11).
