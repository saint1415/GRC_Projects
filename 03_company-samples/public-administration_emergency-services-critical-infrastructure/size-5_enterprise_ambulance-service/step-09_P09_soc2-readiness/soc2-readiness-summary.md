# SOC 2 Readiness Summary: Cris Santos Company | Emergency Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded private ambulance provider) |
| Tier / Vertical | Enterprise / Emergency Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 EMS billing services (46 public EMS agencies); SL-2 managed transportation (3 state Medicaid programs and 6 managed care plans) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and Processing Integrity. SL-2: Security, Availability, Confidentiality, and Privacy |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (third annual report; Availability and Processing Integrity added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's work is emergency and interfacility ambulance service, which SOC 2 does not cover. Two service lines are different: the company **provides services to other organizations**, so it is a service organization for them, and they ask for a CPA's SOC 2 report.
- **SL-1 EMS billing services.** Public fire-rescue departments and county EMS agencies outsource claims, payment posting, and reporting to the company, which is their HIPAA business associate. SL-1 issued its first SOC 2 Type 2 report (Security and Confidentiality) for 2025, and the 2026 period is under way. Agencies now ask for Availability (claim filing deadlines) and Processing Integrity (claims and remittance accuracy). The 9 agencies that came with AQ-02 joined the platform in 2026-08.
- **SL-2 managed transportation.** State Medicaid programs and managed care plans use the company as their non-emergency medical transportation broker. Their vendor programs now require a SOC 2 Type 2 report including **Privacy**, because the company collects consents and preferences directly from members through the contact centers and the member app.

**Alternatives considered:** HITRUST certification (several plans accept it, but the agencies and state programs accept SOC 2, and one framework per service line is cheaper to run); state Medicaid contract audits (they test contract performance, not IT controls, so they complement SOC 2 rather than replace it).

**What SOC 2 does not cover:** the 911 dispatch business itself. County agreements ask for security questionnaires and the P07 Internal Audit summary instead. The enterprise common controls (P02 section 10.3; P04 section 5) support both service lines and dispatch, so one set of evidence serves both reports, the HIPAA program, and the SOX program. The cloud providers, the revenue cycle platform vendor, and the telephony vendor are subservice organizations presented with the carve-out method; their own SOC reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 EMS billing services | SL-2 managed transportation |
|---|---|---|
| Services | Claims preparation and submission, payment posting, denials work, and reporting for public EMS agencies | Trip intake, eligibility checks, assignment to network providers, member reminders, provider payments, and encounter reporting |
| Infrastructure | Revenue cycle platform (vendor SaaS) and the SL-1 client portal on Cloud provider A, landing zone controls (P04) | Company-built managed transportation platform, member app, and network provider portal on Cloud provider B, with a warm standby region (P04) |
| Software | Revenue cycle platform; client portal; trip import interfaces from agencies' ePCR systems | Managed transportation platform; member app; provider portal; contact center platform |
| People | Billing services staff (about 180); SOC; identity and cloud platform teams | Contact center agents and network operations staff (about 1,050); SOC; identity and cloud platform teams |
| Data | Agency patients' demographics, trip data, claims, and remittances | Members' eligibility, addresses, mobility needs, trip history, and consents |
| Procedures | P06 policy hierarchy; P08 runbook; SL-1 billing procedures | P06; P08; SL-2 contact center and network operations procedures |
| Subservice organizations (carved out) | Cloud provider A; revenue cycle platform vendor; clearinghouses | Cloud provider B; telephony and contact center platform vendor; messaging service |
| Other parties (not subservice organizations) | Agencies' own ePCR vendors (data sources) | About 1,400 network transportation providers (complementary controls in their agreements) |

## 3. Readiness results
**SL-1 EMS billing services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 31 | 2 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 managed transportation**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 20 | 11 | 2 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | 12 | 5 | 1 | 0 |

Across both service lines: 73 Ready, 23 Partially ready, 3 Not ready, and 23 N/A (122 rows).

**SL-1** is ready for its next Type 2 on Security and Confidentiality. The new categories have 3 partially ready items (A1.3, PI1.2, PI1.4): a client portal failover test, import completeness checks for the AQ-02 agencies, and remittance reconciliation. Two Security items (CC3.4, CC9.2) trace to the AQ-02 integration.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC2.3, CC9.2, P6.4. Partially ready: CC1.3, CC3.2, CC4.1, CC6.1, CC6.2, CC6.3, CC6.6, CC6.7, CC7.2, CC7.3, CC8.1, C1.1, C1.2, P2.1, P4.2, P4.3, P6.2, P6.5. Most of the gaps trace to one source: about 1,400 small network providers reach member data through the provider portal, with MFA on 62% of accounts, attestations missing for 38% of providers, downloadable manifests, and agreements without security, privacy, or breach notice terms (POAM-013; P01 R-014). Closing POAM-013 and writing the system description by 2027-01-31 makes SL-2 ready to start its period on 2027-04-01. Items due by 2027-03-31 (CC4.1, P4.2, P4.3, P6.2) have compensating controls today and would be described in the report if still open when the period starts.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC3.4, CC9.2, PI1.2; SL-2 CC1.3, CC6.1, CC6.2, CC6.3, CC6.6, CC6.7, CC7.2, CC7.3, C1.1, P2.1 | AQ-02 change review and BAAs; import count checks; provider portal MFA, masking, view-only manifests, bot detection; SOC routing for provider incidents; consent in phone bookings | MFA and attestation reports; SIEM use cases; consent records |
| 2027 Q1 | SL-1 A1.3, PI1.4; SL-2 CC2.3, CC3.2, CC8.1, CC9.2, C1.2, P6.4, P6.5 | SL-1 client portal failover test; remittance reconciliation; SL-2 system description; provider tiering; assignment rule change control; provider agreement renewals with security, privacy, and 10-day breach notice terms | Failover report; reconciliations; signed provider agreements |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines; closes SL-2 CC4.1); SL-2 P4.2, P4.3, P6.2 | Mock walkthrough with the service auditor; per-client retention and disposal; per-member disclosure report | Walkthrough results; retention settings |
| 2027 Q2 | SL-2 Type 2 period starts 2027-04-01 | Monitor evidence collection monthly | Evidence map status |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 12 collecting, 7 ready, 6 not started (each tied to a POA&M item or a 2027 Q1 action).

**Client communication:** SL-1 agencies receive the 2025 report, a bridge letter, and a letter describing the new categories; SL-2 state programs and plans receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11).
