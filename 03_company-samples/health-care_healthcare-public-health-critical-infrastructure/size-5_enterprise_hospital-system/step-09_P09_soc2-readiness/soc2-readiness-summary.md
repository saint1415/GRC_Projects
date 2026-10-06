# SOC 2 Readiness Summary: Cris Santos Company | Healthcare and Public Health | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded for-profit hospital system: 8 hospitals, 1,970 beds; FL, GA, AL) |
| Tier / Vertical | Enterprise / Healthcare and Public Health |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 affiliate EHR hosting (about 70 independent physician practices, about 1,450 users); SL-2 tele-critical care and telestroke (14 partner hospitals, about 210 monitored ICU beds) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and Processing Integrity. SL-2: Security, Availability, Confidentiality, and Privacy. Across the two service lines, all five categories are covered |
| Target reports | SL-1: first Type 2, period 2027-04-01 to 2027-09-30 (Type 1 issued as of 2025-12-31 for Security, Availability, Confidentiality). SL-2: first Type 2, period 2027-07-01 to 2027-12-31 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (26 evidence items) |
| Prepared | 2026-08-14 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the system's work is patient care, which SOC 2 does not cover. Two service lines are different: the system **provides services to other organizations**, so it is a service organization for them, and they ask for a CPA's SOC 2 report.
- **SL-1 affiliate EHR hosting.** About 70 independent physician practices use the system's EHR instance (part of the ECIS) under hosting agreements and BAAs; the system is their HIPAA business associate. A SOC 2 Type 1 report (Security, Availability, Confidentiality) was issued as of 2025-12-31. Larger practices now ask for a Type 2 report, and several ask for **Processing Integrity**, because the hosted interfaces deliver their laboratory results and orders.
- **SL-2 tele-critical care.** The virtual care center at H-01 monitors about 210 ICU beds overnight and provides telestroke consults for 14 partner hospitals, including 6 critical access hospitals. Partner vendor programs require a SOC 2 Type 2 report, and two partners asked for **Privacy**, because the service collects video and monitoring data about their patients.

**Alternatives considered:** HITRUST certification (common in health care; partners accept SOC 2, and one framework per service line costs less to run); CMS surveys and accreditation (they cover hospital conditions, not the IT controls partners rely on, so they complement SOC 2).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports and the HIPAA and SOX programs. Cloud providers, the DC-2 colocation provider, and the tele-ICU application vendor are subservice organizations presented with the carve-out method; their own SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 affiliate EHR hosting | SL-2 tele-critical care |
|---|---|---|
| Services | EHR access, practice management, results and orders exchange for practices' patients | Remote ICU monitoring, intensivist and nurse interventions, telestroke consults |
| Infrastructure | ECIS in DC-1 with hot standby in DC-2; immutable vault in Cloud provider A; zero-trust gateway (P02, P04) | Tele-critical care platform on Cloud provider B with second-region standby; site-to-cloud tunnels to partners; virtual care center at H-01 |
| Software | Commercial EHR (affiliate environment); integration engine | Vendor tele-ICU application; video service; partner EHR interfaces |
| People | Affiliate services team; EHR technical team; SOC; identity and data center teams | Intensivists and critical care nurses; virtual care operations; cloud platform team; SOC |
| Data | Practices' patient records, orders, results, charges | Partner patients' monitoring data, video, notes |
| Procedures | P06 policy hierarchy; P08 runbook; affiliate support procedures | P06; P08; virtual care protocols and partner contracts |
| Subservice organizations (carved out) | Colocation provider (DC-2); Cloud provider A; EHR vendor (support) | Cloud provider B; tele-ICU application vendor |

## 3. Readiness results
**SL-1 affiliate EHR hosting**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 28 | 5 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) |  |  |  | 18 |

**SL-2 tele-critical care**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 27 | 5 | 1 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) |  |  |  | 5 |
| Privacy (P1-P8, 18) | 14 | 4 | 0 | 0 |

**SL-1** is close to ready. Partially ready: CC6.2, CC6.3, CC7.5, CC8.1, CC9.2, A1.3, PI1.1, PI1.3. The gaps are the same ones Internal Audit found in the ECIS (P07): affiliate account management (POAM-015), emergency changes (POAM-012), cyber recovery (POAM-003), vendor reassessments (POAM-014), and result reconciliation (POAM-013). Closing them by 2027-03-31 lets the Type 2 period start on 2027-04-01. If POAM-003 slips, the report will describe failover as the recovery path for the 4-hour RTO and the vault restore as a known exception.

**SL-2** needs more work before a period can start. Not ready: CC9.1, A1.2. Partially ready: CC1.3, CC2.3, CC3.1, CC6.1, CC7.4, C1.2, P1.1, P2.1, P4.2, P6.2. The biggest item is the lack of an alternate virtual care center (CC9.1, A1.2; P01 R-029). The other items are documentation (system description, partner responsibility matrix, notices) and partner identity (MFA for clinicians at 4 partner hospitals).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC6.2, CC6.3, CC8.1, CC9.2, PI1.1 | Affiliate account cleanup and attestations; migration gate; vendor reassessments; processing objectives | Inactivity reports; attestations; change records |
| 2027 Q1 | SL-1 CC7.5, A1.3, PI1.3; SL-2 CC1.3, CC2.3, CC3.1, CC6.1, CC7.4, C1.2, P1.1, P4.2, P6.2 | Vault restore retest; reconciliation; SL-2 system description and partner playbook; partner MFA; retention rules; disclosure log | Retest report; reconciliation reports; partner sign-in configuration |
| 2027 Q1 (March) | Readiness check by Internal Audit for SL-1; SL-1 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | SL-2 CC9.1, A1.2, P2.1 | Alternate virtual care workstations at H-02 and failover test; partner contract amendments | Test report; amended contracts |
| 2027 Q2 (June) | Readiness check for SL-2; SL-2 Type 2 period starts 2027-07-01 | Mock walkthrough | Walkthrough results |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 14 collecting, 5 ready, 7 not started (each tied to a POA&M item or a dated action).

**Communication:** SL-1 practices receive the 2025 Type 1 report, a bridge letter, and the expected Type 2 date (2027-11); SL-2 partners receive this summary, a roadmap letter, and the expected report date (2028-02).
