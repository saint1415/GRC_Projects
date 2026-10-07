# SOC 2 Readiness Summary: Cris Santos Company | Communications | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded regional broadband and wired telecommunications carrier) |
| Tier / Vertical | Enterprise / Communications |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 managed network services (managed SD-WAN, managed firewall, managed Wi-Fi; about 3,400 business customers); SL-2 hosted unified communications (cloud voice, collaboration, and contact center seats; about 1,250 business customers and 96,000 seats) |
| Categories in scope | SL-1: Security, Availability, Confidentiality. SL-2: Security, Availability, Confidentiality, and Processing Integrity. Privacy considered and excluded for both (section 1) |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (third annual report). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's revenue is transmission: voice, broadband, transport, and wholesale. Transmission customers rely on contract SLAs and the CPNI rules, not on a SOC report, so SOC 2 does not fit those services. Two service lines are different, because business customers **rely on the company's processing for their own controls**, which makes the company a service organization for them:
- **SL-1 managed network services.** The company configures and operates customers' SD-WAN, firewalls, and Wi-Fi through vendor cloud controllers. Customers' auditors treat the firewall rule changes and access to their networks as part of their own control environment. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2024; the 2025 report had one exception (a late access removal), since remediated.
- **SL-2 hosted unified communications.** Customers run their phone systems and contact centers on the platform, which stores call recordings, voicemail, and call records and produces the call detail and contact center reports customers use for billing and staffing. Enterprise and public sector buyers now ask for a SOC 2 Type 2 report that includes **Processing Integrity**, because complete and accurate call records and recordings are the core commitment.

**Categories considered:**
| Category | SL-1 | SL-2 | Why |
|---|---|---|---|
| Security | In scope | In scope | Required for every SOC 2 report |
| Availability | In scope | In scope | Both service agreements carry availability commitments (P05 BP-08, BP-09) |
| Confidentiality | In scope | In scope | Customer network configurations (SL-1) and recordings and call records (SL-2) |
| Processing Integrity | Not in scope | In scope | SL-1 processes no customer transactions; SL-2 call records and recordings must be complete and accurate |
| Privacy | Not in scope | Not in scope | The company processes end users' data on behalf of business customers, which own their privacy notices and consents; the commitments to customers are covered by Confidentiality. Revisit if SL-2 adds consumer-facing features |

**Alternatives considered:** no Communications-specific assurance scheme replaces SOC 2 for these buyers (the vertical overlay lists none). An ISO/IEC 27001 certification was considered; customers' vendor programs ask for SOC 2 Type 2, and one report per service line built on the enterprise common controls is cheaper to run.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the CPNI certification evidence package, and the SOX program. Cloud providers A and B, the SD-WAN and firewall vendors' cloud controllers, and the telephone number and messaging partners are subservice organizations presented with the carve-out method; their own SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 managed network services | SL-2 hosted unified communications |
|---|---|---|
| Services | Managed SD-WAN, managed firewall, managed Wi-Fi: design, change management, monitoring, incident response | Cloud voice, collaboration, contact center seats, call recording, voicemail, call detail reporting |
| Infrastructure | Vendor cloud controllers; managed services orchestration on Cloud provider A; customer-premises devices | Cloud provider B (two regions); interconnect SBC pair in the voice core (P04) |
| Software | Vendor controller software; company orchestration and portal | Commercial UC platform software, customer-managed on Cloud B; service portal; AI transcription pilot (AI-011) |
| People | Managed services operations center; SOC; identity and cloud platform teams | UC operations team; SOC; NOC (interconnect); identity and cloud platform teams |
| Data | Customer network configurations, device logs, administrator accounts | Recordings, voicemail, call records, contact center data, customer administrator accounts |
| Procedures | P06 policy hierarchy; P08 runbook; SL-1 operating procedures | P06; P08; SL-2 operating procedures (being written, CC5.3) |
| Subservice organizations (carved out) | Cloud provider A; SD-WAN and firewall vendors' controllers | Cloud provider B; telephone number and messaging partners |

## 3. Readiness results
**SL-1 managed network services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 32 | 1 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 hosted unified communications**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 22 | 9 | 2 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 1 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready for its next Type 2. The one partially ready item (CC6.8) is lapsed threat signature subscriptions on about 3% of managed customer firewalls; an automated renewal check closes it by 2026-12-31.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC4.1 (no separate evaluation of SL-2 controls yet), CC5.3 (SL-2 operating procedures not written), PI1.4 (no reconciliation of call records delivered to customers). Partially ready: CC2.3, CC3.4, CC6.1, CC6.2, CC6.6, CC7.1, CC7.2, CC7.4, CC9.2, A1.3, C1.2, PI1.1. Four of these come from enterprise gaps Internal Audit found (P07): the management plane and AQ networks the interconnect SBCs depend on (CC6.6; POAM-002, POAM-003), patching (CC7.1; POAM-008), network monitoring (CC7.2; POAM-004), and vendor terms (CC9.2; POAM-014). The incident plan item (CC7.4) closes with POAM-013 by 2026-11-30. The rest are SL-2-specific: customer administrator MFA and reviews, deletion of recordings at contract end, a system description with processing specifications, and an AI transcription feature enabled before council review (CC3.4; POAM-023). Closing the SL-2-specific items by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01. Items that close by 2027-03-31 through enterprise POA&M work have compensating controls today and would be described in the report if still open when the period starts.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC6.8; SL-2 CC3.4, CC6.1, CC7.4 | Subscription renewal check; council review of AI-011; MFA for all SL-2 customer administrators; incident plan update and tabletop (POAM-013) | Subscription reports; council minutes; MFA enforcement report; tabletop report |
| 2027 Q1 | SL-2 CC2.3, CC4.1, CC5.3, CC6.2, CC6.6, CC7.1, CC7.2, CC9.2, A1.3, C1.2, PI1.1, PI1.4 | SL-2 procedures and system description; Internal Audit SL-2 readiness assessment; customer administrator attestation; deletion certificates; daily call record reconciliation; enterprise POA&M items (POAM-002, POAM-003, POAM-004, POAM-008, POAM-014) | Procedures; attestation records; reconciliation reports; failover test with recording restore |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines); SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | Contract standardization (CC2.3) at renewals | Standard 24-hour notice commitment | Amended agreements |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 12 collecting, 6 ready, 7 not started (each tied to a POA&M item or a 2026 Q4 or 2027 Q1 action).

**Customer communication:** SL-1 customers receive the 2025 report and a bridge letter; SL-2 customers and prospects receive this summary, a bridge letter describing the remediation, and the expected SL-2 report date (2027-11).
