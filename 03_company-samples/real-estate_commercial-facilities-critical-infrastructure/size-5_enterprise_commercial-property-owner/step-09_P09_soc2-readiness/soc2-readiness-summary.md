# SOC 2 Readiness Summary: Cris Santos Company | Commercial Facilities | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded office and retail REIT), through its taxable REIT subsidiary Cris Santos Building Services (the TRS) |
| Tier / Vertical | Enterprise / Commercial Facilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; read the official AICPA text for the criteria and points of focus |
| Service lines | SL-1 property management and building operations services for 50 properties (22 JV properties for 6 JV partners; 28 properties of 9 third-party owners); SL-2 tenant experience platform licensed to third-party owners for 36 buildings |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and Processing Integrity. SL-2: Security, Availability, Confidentiality, and (new) Privacy |
| Target reports | SL-1: first Type 2, period 2027-04-01 to 2027-09-30, report by 2027-12-31 as the management agreements require. SL-2: third annual Type 2, period 2027-01-01 to 2027-12-31, with Privacy added |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-28 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this company
Most of the company's revenue is rent, which SOC 2 does not cover. Two TRS service lines are different: the company **provides services to other businesses**, so it is a service organization for them, and those clients ask for a CPA's SOC 2 report.
- **SL-1 property management and building operations.** JV partners and third-party owners rely on the company to run their buildings' engineering, security, access control, and video, and to report operating data and submeter bills accurately. Their management agreements (amended 2026) require a SOC 2 Type 2 report by 2027-12-31. **Processing Integrity** is in scope because owners bill their own tenants from the company's submeter calculations and rely on its service-level reports. A SOC 1 report on rent billing and accounting is handled separately by the Controller.
- **SL-2 tenant experience platform.** Third-party owners license the company-built app (mobile credentials, amenity bookings, notices, service requests, and the AI-008 virtual assistant) for their own buildings. SL-2 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2025, with no exceptions in the 2025 report. Several clients now ask for **Privacy**, because the app collects personal information and consents directly from their tenants' employees.

**Alternatives considered:** the vertical overlay names no sector assurance scheme as an alternative to SOC 2. ISO/IEC 27001 certification was considered for SL-2 but the clients' vendor programs ask for SOC 2. PCI DSS validation covers only card acceptance (P03) and does not address these services.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the SOX program, and the 2027 CPPA cybersecurity audit (11 CCR 7123). The cloud providers, the colocation providers, and the access control and video platform vendor are subservice organizations presented with the carve-out method; their own SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 property management and building operations | SL-2 tenant experience platform |
|---|---|---|
| Services | Engineering and BAS operation, access control and video administration, RSOC monitoring, work orders, service-level and operating reports, submeter billing | Mobile credentials, amenity bookings, building notices, service requests, virtual assistant |
| Infrastructure | BAACS (Platform A at managed towers, Platform B at managed parks and retail), OT remote access gateway, smart building data platform and data warehouse in Cloud provider A (P02, P04) | Company-built application on managed containers in Cloud provider B, two regions; landing zone controls (P04) |
| Software | Commercial BAS platforms; access control and video platform (vendor SaaS); property management and ERP (vendor SaaS); data warehouse reports | Company-built app and APIs; cloud AI service for the virtual assistant (AI-008) |
| People | TRS management team; engineering; corporate security and RSOCs; OT security team; Cyber Defense Center | Digital products team; identity and cloud platform teams; Cyber Defense Center |
| Data | Owners' operating data, meter reads, tenant contacts, tenant employee credential records at managed properties | Tenant employee profiles, phone numbers, mobile credential data, bookings, consents |
| Procedures | P06 policy hierarchy; P08 runbook; degraded-mode procedures; owner reporting procedures | P06; P08; secure development lifecycle; release procedures |
| Subservice organizations (carved out) | Cloud provider A; colocation providers; access control and video platform vendor; property management and ERP vendor | Cloud provider B; access control and video platform vendor (credential integration); SMS and messaging provider |

## 3. Readiness results
**SL-1 property management and building operations services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 21 | 11 | 1 | 0 |
| Availability (A1, 3) | 1 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 2 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 tenant experience platform**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 31 | 2 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | 14 | 4 | 0 | 0 |

**SL-2** is ready for its next Type 2 on the existing categories, with two partially ready Security items (CC6.1: MFA is optional for tenant users; CC9.2: the credential integration depends on the platform vendor, whose recovery commitment is below the BIA). The new Privacy criteria have 4 partially ready items (P2.1, P3.2, P4.2, P6.2): presence sharing on by default in older app versions, central consent records for precise location, per-client retention, and an automated disclosure log. All are due by 2027-03-31; the Privacy items would be described in the 2027 report if still open at the start of the period.

**SL-1** is not yet ready for a Type 2 period to start. Not ready: CC7.2 and PI1.3. Partially ready: CC1.3, CC2.3, CC6.1, CC6.2, CC6.3, CC6.4, CC6.8, CC7.1, CC7.5, CC8.1, CC9.2, A1.2, A1.3, PI1.1, PI1.4. The Security and Availability gaps are the same ones Internal Audit found in the BAACS (P07), limited to the 50 managed properties: OT monitoring and logging at Platform B, emergency changes by integrators, default device passwords, local OT accounts, firmware currency, Platform B recovery time, RSOC failover, and the platform vendor's recovery commitment. The Processing Integrity gaps are specific to SL-1: there are no automated completeness and accuracy checks before owner reports and submeter bills are released, and 14 submeter bills were corrected after release in the first half of 2026 (P01 R-053). None of the acquired properties is an SL-1 property, so the Platform C and Integrator C gaps do not affect SL-1.

Closing POAM-001, POAM-002, POAM-005 (SL-1 properties first), POAM-008, POAM-009, POAM-010, POAM-011, POAM-013, POAM-014, and POAM-017, the SL-1 system description, and the PI1.3 checks by 2027-03-31 makes SL-1 ready to start its period on 2027-04-01. Items that close later have compensating controls today and would be described in the report if still open when the period starts.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC1.3, CC6.1 to CC6.4, CC6.8, CC8.1; SL-2 P2.1 | SL-1 system description; default passwords and local OT accounts; credential auto-suspend; OT closet locks; Platform B workstation refresh at SL-1 properties; emergency change procedure; presence sharing default off | Suspension reports; change tickets with approvals; walkthrough results |
| 2027 Q1 | SL-1 CC2.3, CC7.1, CC7.2, CC7.5, CC9.2, A1.2, A1.3, PI1.1, PI1.3, PI1.4; SL-2 CC6.1, CC9.2, P3.2, P4.2, P6.2 | Commitments annex; OT logging and monitoring at all 50 SL-1 properties; firmware waves; Platform B restore within RTO; platform vendor amendment; degraded-mode procedures and RSOC full-shift test; automated PI checks; risk-based MFA; consent records; per-client retention; disclosure log | SIEM coverage for SL-1 properties; restore test reports; PI check results; consent and disclosure logs |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines) and a mock walkthrough with the service auditor | Confirm SL-1 readiness to start the period on 2027-04-01 | Walkthrough results |
| 2027 Q2 to Q4 | Operating effectiveness periods | SL-2 period 2027-01-01 to 2027-12-31; SL-1 period 2027-04-01 to 2027-09-30 | Type 2 samples per the evidence map |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports (14 of 25). Status: 13 collecting, 5 ready, 7 not started (each tied to a POA&M item or a 2027 Q1 action).

**Client communication:** SL-2 clients receive the 2025 report, a bridge letter, and a Privacy roadmap letter. SL-1 JV partners and owners receive this summary, the remediation calendar, and the expected first report date (2027-11), well before the 2027-12-31 contractual deadline.
