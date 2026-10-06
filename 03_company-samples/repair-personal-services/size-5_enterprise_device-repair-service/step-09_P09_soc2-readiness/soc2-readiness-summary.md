# SOC 2 Readiness Summary: Cris Santos Company | Other Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded national electronics and device repair chain) |
| Tier / Vertical | Enterprise / Other Services (except Public Administration) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs with short topic labels written for this analysis; read the AICPA text for the criteria |
| Service lines | SL-1 claims repair fulfillment (4 protection plan administrators, 2 wireless carriers); SL-2 enterprise device lifecycle services (about 1,400 business, school district, and health care clients) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and (new) Processing Integrity. SL-2: Security, Availability, Confidentiality |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report; Processing Integrity added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-28 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's work is consumer repair, which SOC 2 does not cover. Two service lines are different: the company **provides services to other businesses** that rely on its systems and controls, so it is a service organization for them, and their vendor programs ask for a CPA's SOC 2 report.
- **SL-1 claims repair fulfillment.** Protection plan administrators and wireless carriers send claims through the SL-1 claims API; the company repairs the device and reports status and outcome, which the clients use to settle their customers' claims. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2024; the 2025 report had 2 exceptions (a late access removal and a missed quarterly review), since remediated. Two carriers now ask for **Processing Integrity**, because wrong or missing status updates cause payout errors on their side.
- **SL-2 enterprise device lifecycle services.** Business, school, and health care clients send fleets for repair, imaging, sanitization, and disposition, and track them on the asset portal. Clients' vendor programs now require a SOC 2 Type 2 report, with sanitization (CC6.5 and C1.2) as the main concern. 38 health care clients also hold BAAs with the company (P03 HIPAA rows).

**Alternatives considered:** for SL-2, an electronics recycling or data sanitization industry certification (useful for downstream recyclers but does not cover the company's IT controls, so it would complement SOC 2, not replace it); ISO/IEC 27001 certification (some clients accept it, but the larger clients require SOC 2 Type 2). For SL-1, no alternative was requested.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the PCI DSS ROC, the SOX program, and the California cybersecurity audit. The cloud providers, the notification provider, and the courier are subservice organizations presented with the carve-out method; their own reports are reviewed under CC9.2.

**Not a SOC 2 matter:** the company is not a SOC 2 service organization for consumer repairs or for card payments. The STPP's payment controls are validated through the PCI DSS ROC.

## 2. System description (scope)
| Element | SL-1 claims repair fulfillment | SL-2 enterprise device lifecycle services |
|---|---|---|
| Services | Claim intake by API, repair at depots and stores, status and outcome reporting | Depot repair, imaging and provisioning, sanitization, IT asset disposition, asset portal |
| Infrastructure | STPP and the SL-1 claims API on Cloud provider A, second-region standby, landing zone controls (P02, P04) | Asset portal and sanitization record store on Cloud provider B; depot systems and sanitization stations at the three depots |
| Software | Company-built STPP and claims API | Commercial depot management software; sanitization software; company-built asset portal |
| People | Claims operations team; depot and store technicians; STPP team; SOC | Enterprise services teams at Depot Central and Depot West; sanitization teams at all depots; SOC |
| Data | Client customer names and contacts, device identifiers, claim status, repair outcomes | Client asset records; data on client devices (including ePHI for 38 health care clients) until sanitized; sanitization certificates |
| Procedures | P06 policy hierarchy; P08 runbook; claims operations procedures | P06; P08; STD-04.3 sanitization standard; receiving and chain-of-custody procedures |
| Subservice organizations (carved out) | Cloud provider A; notification provider; national courier | Cloud provider B; national courier; downstream recyclers and refurbishers |

## 3. Readiness results
**SL-1 claims repair fulfillment**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 30 | 3 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 enterprise device lifecycle services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 24 | 8 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready for its next Type 2 on the existing categories once the claims API authorization fix is released and retested (CC6.1, CC8.1; POAM-010 by 2026-11-15) and the expired AOC is collected (CC9.2). The new Processing Integrity criteria have 2 partially ready items: input validation against the device catalog (PI1.2) and a daily status reconciliation with each client (PI1.3), both due by 2027-02-28, before the period's first quarter closes.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC6.5 and C1.2, both about sanitization that cannot be shown per device at Depot West. Partially ready: CC1.3, CC2.3, CC3.1, CC6.1, CC6.2, CC6.3, CC6.7, CC9.2, A1.2, C1.1. The gaps match the Internal Audit findings (P07 MP-6, IA-5) and the P03 gap analysis: sanitization verification and records, default passwords on stations, client accounts on the asset portal, downstream recycler terms, and the BAA inventory. Closing POAM-006, POAM-015, and POAM-022, and drafting the system description, by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01. Downstream recycler addenda that are still open at that date would be described in the report with the rerouting of SL-2 lots as the compensating control.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC6.1, CC8.1, CC9.2; SL-2 CC6.1, CC6.5, C1.2, A1.2, C1.1, CC6.7, CC1.3 | Claims API fix and retest; AOC collection; station passwords and PAM; Depot West per-device verification and real-time record sync; BAA abstracts; serial capture at receiving; RACI update | Retest report; AOCs; verification logs; sanitization records; BAA abstracts |
| 2027 Q1 | SL-1 PI1.2, PI1.3; SL-2 CC2.3, CC3.1, CC6.2, CC6.3, CC9.2 | Catalog validation and daily reconciliation; SL-2 system description and commitments register; asset portal client attestations; downstream recycler addenda and SL-2 lot rerouting | Reconciliation reports; system description; attestations; amended contracts |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines); SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | SL-2 period running; SL-1 mid-period review | Monitor evidence collection monthly | Evidence map status |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 14 collecting, 4 ready, 7 not started (each tied to a POA&M item or a 2027 Q1 action).

**Client communication:** SL-1 clients receive the 2025 report, a bridge letter, and a Processing Integrity roadmap letter; SL-2 clients receive this summary, a description of the sanitization remediation, and the expected first report date (2027-11). Health care clients with BAAs also receive the BA notice contact and terms confirmation (POAM-022).
