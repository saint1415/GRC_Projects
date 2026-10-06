# SOC 2 Readiness Summary: Cris Santos Company | Accommodation and Food Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded hotel franchisor, manager, and owner) |
| Tier / Vertical | Enterprise / Accommodation and Food Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; labels are written for this checklist, not AICPA text |
| Service lines | SL-1 franchise technology services (640 franchised hotels); SL-2 independent hotel distribution services (about 180 unbranded independent hotels) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and (new for 2027) Processing Integrity. SL-2: Security, Availability, Confidentiality, Processing Integrity, and Privacy. All five categories are covered across the two lines |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fifth annual report; Processing Integrity added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-17 to 2026-08-28 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive, 2026-09-04 |

## 1. Why SOC 2 for this organization
Most of the company's revenue comes from running and franchising hotels, which SOC 2 does not cover. Two service lines are different: the company **provides technology services to other businesses**, so it is a service organization for them, and they ask for a CPA's SOC 2 report.
- **SL-1 franchise technology services.** The company administers the brand cloud PMS tenant, CRS access, the managed property network (410 subscribing hotels), and the technology help desk for 640 independently owned franchised hotels. Franchisees, their lenders, and management companies ask for SOC 2. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2023. The 2025 report had 2 exceptions (late removal of franchisee accounts and one missed quarterly hub rule review). Owners now ask for **Processing Integrity**, because reservations delivered from the CRS to the PMS and the night audit reports drive their revenue and the franchise fees they pay.
- **SL-2 independent hotel distribution services.** About 180 unbranded independent hotels use the company's CRS and booking engine under client agreements. Larger clients and two hotel management companies now require a SOC 2 Type 2 report including **Processing Integrity** (rates, mandatory fees, and reservations must reach channels correctly) and **Privacy** (the booking engine collects guest personal information directly on the clients' behalf).

**The 2026 SL-1 report in progress.** The 2026 period (2026-01-01 to 2026-12-31) is already running. The service auditor is likely to report exceptions for the hub rule (CC6.6), the missed service provider segmentation test (CC7.1), and inactive franchisee accounts (CC6.1). This readiness review targets the 2027 period so that those exceptions are closed before it starts.

**Alternatives considered:**
- **PCI DSS service provider AOC** (the vertical's main assurance alternative). The company already gives franchisees and SL-2 clients its service provider AOC and responsibility matrix (PCI DSS 12.9.2). It covers card data only, not availability, reservation accuracy, or guest privacy, so it complements SOC 2 and does not replace it.
- **ISO/IEC 27001 certification.** Not requested by any franchisee or client; would add a second framework to maintain.
- **Bridge letters only.** Acceptable to franchisees between reports, but not to the management companies that require a Type 2 report for SL-2.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04) support both service lines, so one set of evidence serves both reports, the PCI DSS service provider ROC, and SOX IT general controls. Subservice organizations are presented with the carve-out method: Cloud provider A, the PMS vendor, the colocation providers, and the SD-WAN carriers (SL-1); Cloud provider A, the distribution switch, and the payment gateway (SL-2). Their SOC 2 reports and AOCs are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 franchise technology services | SL-2 independent hotel distribution services |
|---|---|---|
| Services | PMS tenant administration, CRS access, managed property network, and help desk for franchised hotels | Central reservations, booking engine, rate and inventory distribution to online travel agencies and global distribution systems |
| Infrastructure | Brand cloud PMS (vendor SaaS); managed network hubs in colocation DC-1 and DC-2 and the cloud hub; hotel firewalls and SD-WAN at subscribing hotels | Cloud provider A: CRS, booking engine, and the SL-2 client tenant with logical isolation for 180 clients; second-region standby |
| Software | PMS tenant configuration and interfaces; franchise portal; identity platform federation | Company-built CRS and booking engine; channel connectivity; guest chatbot (AI-002) |
| People | Franchise technology services team; PMS tenant administration; network engineering; SOC | Distribution and reservations team; CRS engineering; payments team; SOC |
| Data | Franchised hotels' reservations, folios, guest profiles, and tokens (card data only as tokens) | Clients' rates, inventory, reservations, guest profiles, and tokens |
| Procedures | P06 policy hierarchy and brand technology standards BS-TECH-01 to BS-TECH-06; P08 runbook (franchise track) | P06; P08; SL-2 client support procedures |
| Subservice organizations (carved out) | Cloud provider A; PMS vendor; colocation providers; SD-WAN carriers | Cloud provider A; distribution switch; payment gateway |

## 3. Readiness results
**SL-1 franchise technology services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 27 | 6 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 independent hotel distribution services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 27 | 6 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 1 | 1 | 0 |
| Privacy (P1-P8, 18) | 13 | 4 | 1 | 0 |

Across both lines: 82 Ready, 20 Partially ready, 2 Not ready, 18 N/A (122 rows).

**SL-1** is ready on its existing categories except for six Security items, all tied to findings Internal Audit raised in P07: CC6.1 and CC6.2 (inactive franchisee accounts and missing attestations, POAM-008), CC6.3 (card display permission, POAM-007), CC6.6 and CC7.1 (the hub rule and the missed segmentation test, POAM-004), and CC2.3 (212 older franchise agreements without the responsibility acknowledgment, POAM-012). The two new Processing Integrity items (PI1.1, PI1.4) need written processing objectives and an automated daily CRS-to-PMS reconciliation by 2026-12-31. CC2.3 closes after the period starts (2027-03-31); until then the system description will state which agreements carry the terms.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: PI1.4 (missing fee codes in one global distribution system feed and total price errors, POAM-021) and P4.2 (no retention schedule, POAM-018). Partially ready: CC1.3, CC2.3, CC3.1, CC6.2, CC6.7, CC9.2, C1.2, PI1.1, P1.1, P4.3, P6.2, P6.7. Most depend on writing the first SL-2 system description and service commitments (due 2027-01-31). Closing POAM-018 and POAM-021 and the SL-2 actions by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC6.1, CC6.2, CC6.3, CC6.6, CC7.1, PI1.1, PI1.4; SL-2 CC6.7, PI1.4 | Disable inactive franchisee accounts and enforce attestations; remove excess card display permission; verify the hub rule and run the segmentation retest (2026-10-23); SL-1 processing objectives and daily reconciliation; purge historical chat transcripts; fix fee codes and the chatbot total price rule | Inactivity job reports; attestations; monthly permission reviews; segmentation report; reconciliation reports; feed audits |
| 2027 Q1 (January) | SL-2 CC1.3, CC2.3, CC3.1, PI1.1, P1.1 | Write the SL-2 system description and service commitments; client communication procedure; link client privacy notices | System description; client notices |
| 2027 Q1 (March) | SL-1 CC2.3; SL-2 CC6.2, CC9.2, C1.2, P4.2, P4.3, P6.2, P6.7 | Franchise side letters; client administrator attestations; distribution switch SOC 2 report; retention schedule and first purge; automated disclosure log | Side letters; attestations; switch report review; purge reports; disclosure log |
| 2027 Q1 (March) | Readiness check by Internal Audit for SL-2; SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q4 | Both lines | Bridge letters for franchisees and clients; plan the 2028 periods | Bridge letters |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports, the PCI DSS service provider ROC, and SOX. Status: 12 collecting, 5 ready, 8 not started (each tied to a POA&M item or a dated action above).

**Communication:** franchisees receive the 2025 SL-1 report, a bridge letter, and a note that Processing Integrity is added for 2027; SL-2 clients and the two management companies receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11).
