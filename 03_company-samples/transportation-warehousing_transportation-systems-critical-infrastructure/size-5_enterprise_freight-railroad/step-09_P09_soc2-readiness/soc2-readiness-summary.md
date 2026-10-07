# SOC 2 Readiness Summary: Cris Santos Company | Transportation Systems | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company of 64 freight railroads, with a rail services segment) |
| Tier / Vertical | Enterprise / Transportation Systems |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 hosted PTC back office (27 unaffiliated short lines, 310 of their locomotives); SL-2 dispatch and car management platform (18 short lines and industrial railroads) |
| Categories in scope | SL-1: Security, Availability, Confidentiality. SL-2: Security, Availability, Confidentiality, and Processing Integrity |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the Vice President, Technology Services; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's work is running its own railroads, which SOC 2 does not cover. Two service lines are different: the company **sells technology services to unaffiliated railroads**, so it is a service organization for them, and their auditors, lenders, and Class I partners ask for a CPA's SOC 2 report.
- **SL-1 hosted PTC back office.** 27 short lines that must carry onboard PTC apparatus to run on Class I PTC lines (49 CFR 236.1006(a)) use the company's back office instead of building their own. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2024; the 2025 report was unqualified with one exception (late removal of a vendor engineer's access), since remediated.
- **SL-2 dispatch and car management.** 18 short lines and industrial railroads use tenant consoles on the CAD and the TMS for dispatch, car management, waybills, and interchange EDI. Two SL-2 customers have asked for a SOC 2 report by 2027. Because customers rely on accurate car records and interchange data for billing and for their own regulatory records, SL-2 adds **Processing Integrity**.

**Alternatives considered:** a SOC 1 report (useful for customers' financial statement auditors, but customers asked about security and availability, not only financial reporting); sharing the TSA-approved CIP or CAP results (not possible: they are SSI under 49 CFR part 1520 and cannot go to customers that are not covered persons with a need to know); ISO/IEC 27001 certification (customers and Class I partners asked specifically for SOC 2).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the CAP assessments, and the SOX program. The cloud providers, the colocation provider for DC-2, the PTC software vendor, and the EDI network provider are subservice organizations presented with the carve-out method; their own SOC reports are reviewed under CC9.2. SSI is never placed in a SOC 2 system description; the description is reviewed by the Assistant Vice President, Rail Security before release.

## 2. System description (scope)
| Element | SL-1 hosted PTC back office | SL-2 dispatch and car management |
|---|---|---|
| Services | PTC back office for customers' onboard apparatus: initialization, track data, interoperable messaging with Class I back offices, key management | Dispatch consoles for customer territories; car management, waybills, interchange EDI, customer reports |
| Infrastructure | PTC back office in DC-1 with standby in DC-2; HSMs; industry messaging network connection (P02) | CAD tenants in DC-1 and DC-2 (P02); TMS tenants in Cloud provider A with a standby region (P04) |
| Software | Vendor-certified PTC back office software; company tenant management tools | Commercial CAD; company-configured TMS |
| People | Train control team (24/7 desk); SOC; identity and data center teams | Technology services support desk; NOC; TMS team; SOC |
| Data | Customers' locomotive, track, and PTC message data; customer user accounts | Customers' movement authority records, car and waybill data, interchange events; customer user accounts |
| Procedures | P06 policy hierarchy; P08 runbook; SL-1 support procedures | P06; P08; SL-2 onboarding and support procedures |
| Subservice organizations (carved out) | DC-2 colocation provider; PTC software vendor (remote support); industry messaging network operator | Cloud provider A; DC-2 colocation provider; CAD software vendor; EDI network provider |

## 3. Readiness results
**SL-1 hosted PTC back office**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 31 | 2 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 dispatch and car management platform**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 26 | 6 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 2 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

Across both service lines: 66 Ready, 13 Partially ready, 2 Not ready, 41 N/A (122 rows).

**SL-1** is ready for its next Type 2 period, with 3 partially ready items that the service auditor would likely report as exceptions if still open on 2027-01-01: CC6.1 (the corporate-to-OT directory trust, POAM-005, due 2026-12-31), CC7.1 (PTC patching without documented compensating measures, POAM-003, due 2026-12-31), and A1.3 (PTC back office recovery took 9.5 hours against the 4-hour commitment, POAM-006, due 2027-03-31). A1.3 will be open at the start of the period, so the company will tell customers in the bridge letter and describe it in the system description.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC6.6 (an AQ-06 site reached the TMS integration APIs through a legacy VPN) and PI1.3 (no automated reconciliation of interchange events with car records). Partially ready: CC2.3, CC3.1, CC6.1, CC6.2, CC8.1, CC9.2, A1.3, C1.2, PI1.1, PI1.4. The security gaps are the same ones Internal Audit found in the TDPB (P07): the directory trust, emergency change approvals, vendor assurance, and the acquired railroad boundary. Closing POAM-005, POAM-011, POAM-015, and the interim step of POAM-018 by 2026-12-31, and the SL-2-specific items by 2027-03-31, makes SL-2 ready to start its period on 2027-04-01.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC6.1, CC7.1; SL-2 CC6.1, CC6.2, CC6.6 (interim), CC8.1, CC9.2 | Directory trust removal; PTC compensating measures; SL-2 customer attestations; AQ VPN restriction; emergency change workflow rule; vendor review backlog | Trust removal record; CIP filing; attestations; change tickets; vendor reviews |
| 2027 Q1 | SL-1 A1.3; SL-2 CC2.3, CC3.1, A1.3, C1.2, PI1.1, PI1.3, PI1.4 | PTC failover automation and retest; SL-2 system description and commitments register; TMS tenant restore test; customer exit procedure; daily EDI reconciliation; output review | DR retest report; system description; reconciliation exception reports |
| 2027 Q1 (March) | Readiness check by Internal Audit for SL-2; mock walkthrough with the service auditor | Walkthrough of every SL-2 criterion | Walkthrough results |
| 2027 Q2 | SL-2 Type 2 period starts 2027-04-01; SL-1 period already running since 2027-01-01 | AQ-06 SD-WAN migration completes CC6.6 (POAM-018, 2027-05-31) | Quarterly evidence per the map |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 11 collecting, 6 ready, 8 not started (each tied to a POA&M item or a 2027 Q1 action).

**Customer communication:** SL-1 customers receive the 2026 report when issued, a bridge letter, and a note on the PTC recovery remediation; SL-2 customers receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11). Neither communication includes SSI.
