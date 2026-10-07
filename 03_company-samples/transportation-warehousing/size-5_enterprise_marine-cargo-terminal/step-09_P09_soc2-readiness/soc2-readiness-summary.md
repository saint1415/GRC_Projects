# SOC 2 Readiness Summary: Cris Santos Company | Transportation and Warehousing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-port marine cargo terminal operator) |
| Tier / Vertical | Enterprise / Transportation and Warehousing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is in the AICPA publication |
| Service lines | SL-1 Cargo Visibility and Appointment Platform (CVAP), used by about 4,100 trucking companies and about 900 API customers; SL-2 hosted terminal technology services for 4 client terminals (C-01 to C-04) |
| Categories in scope | SL-1: Security, Availability, and (new for 2027) Confidentiality and Processing Integrity. SL-2: Security, Availability, Confidentiality and Processing Integrity. Privacy is out of scope for both (section 2) |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (third annual report; two categories added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's work is cargo handling, which SOC 2 does not cover; ocean carriers rely on terminal services agreements, MTSA compliance and CTPAT for assurance. Two service lines are different: the company **provides technology services to other businesses**, so it is a service organization for them, and they ask for a CPA's SOC 2 report.
- **SL-1 CVAP.** Container availability, holds, vessel schedules, truck appointments and subscription APIs for all 8 terminals. Trucking companies, cargo owners, brokers and forwarders rely on its availability every time a truck is dispatched. SL-1 has issued SOC 2 Type 2 reports (Security, Availability) since the 2025 period. API subscribers now ask for **Confidentiality** (their cargo data) and **Processing Integrity** (whether availability and hold status are accurate and current).
- **SL-2 hosted terminal technology.** The company runs the TOS and gate environments of 4 client terminals on ETOP. Each client is an MTSA facility operator with its own FSP and Cybersecurity Plan and relies on the company for systems it has delegated (101.615). The clients have asked for a SOC 2 Type 2 report with **Processing Integrity** by 2027, because accurate moves, holds and billing data are the core of the service.

**Alternatives considered:** ISO/IEC 27001 certification (clients asked for a CPA attestation report they can map to their own Subpart F vendor oversight and give to their auditors); client audits under the agreements (still allowed, but one SOC 2 report replaces four separate audits); CTPAT validation (covers supply chain security for the company itself, not the services it provides to clients).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the SOX program and the Subpart F Plan audits. Cloud provider A and B, the identity SaaS and the messaging service are subservice organizations presented with the carve-out method; their own SOC 2 reports are reviewed under CC9.2. The customs data exchange service and the port community systems are not subservice organizations (they send data into the system), but their reliability affects Processing Integrity, so their controls are described as complementary inputs.

## 2. System description (scope)
| Element | SL-1 CVAP | SL-2 hosted terminal technology |
|---|---|---|
| Services | Availability, holds and schedules lookup; truck appointments; subscription APIs; notifications | TOS and gate environments operated for client terminals: vessel and yard planning, equipment dispatch interface, gate module, billing feeds |
| Infrastructure | Cloud provider B managed containers and database, second-region standby, landing zone controls (P04) | Cloud provider A ETOP spokes for C-01 to C-04 (P02), landing zone controls, EDI and integration hub |
| Software | Company-built platform and APIs | Commercial TOS software (customer-managed by the company); integration hub |
| People | Digital services team; SOC; identity and cloud platform teams | TOS platform team; client success team; SOC; CySO's team |
| Data | Container status and holds from the TOS; appointments; driver profiles (name, phone, driver license number and state, TWIC status); subscriber API data | Each client's terminal data: container inventory, holds, moves, gate transactions, client user accounts |
| Procedures | P06 policy hierarchy; P08 runbook; SL-1 support procedures | P06; P08 (including client notification); client onboarding and exit procedures |
| Subservice organizations (carved out) | Cloud provider B; messaging and notification service | Cloud provider A; identity SaaS; TOS software vendor (remote support) |

**Why Privacy is out of scope.** SL-1 makes no privacy commitments to drivers beyond its privacy notice, and driver personal information is protected under the Security and Confidentiality criteria; the company will reconsider Privacy after driver license numbers are tokenized (2027-06-30). SL-2 environments hold the clients' terminal business data; personal information is limited to client user accounts and gate records that the clients control.

## 3. Readiness results
**SL-1 CVAP**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 33 | 0 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 hosted terminal technology**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 23 | 8 | 2 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** is ready for its next Type 2 on Security and Availability. The new categories have 3 partially ready items (C1.2, PI1.1, PI1.3): a retention schedule for subscriber data, published processing specifications, and retained evidence of the 15-minute reconciliation with the TOS. All three close by 2026-12-31, before the 2027 period starts.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC7.4, CC7.5, A1.3. Partially ready: CC1.3, CC2.3, CC3.1, CC6.1, CC6.2, CC6.3, CC8.1, CC9.2, A1.2, C1.2, PI1.1, PI1.3. The gaps are the same ones Internal Audit found in ETOP (P07): client notice terms and joint drills (POAM-011), platform recovery and failover testing (POAM-005), client account management (POAM-018), vendor support accounts outside PAM (POAM-015), role conflicts (POAM-017), rule change testing (POAM-014) and port partner terms (POAM-022). Closing them by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01. Items that close later (POAM-022 in part) have compensating controls today and would be described in the report if still open when the period starts.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 C1.2, PI1.1, PI1.3; SL-2 CC3.1, CC6.1, CC6.2, CC6.3, CC8.1, C1.2, PI1.1, PI1.3 | SL-1 retention schedule and processing specifications; reconciliation evidence retained; SL-2 system description; vendor accounts into PAM; client account disablement; role conflicts removed; change tool gate; client exit procedure | Reconciliation results; account job reports; change records; signed system descriptions |
| 2027 Q1 | SL-2 CC1.3, CC2.3, CC7.4, CC7.5, A1.2, A1.3, CC9.2 | Amended client agreements and responsibility matrices; joint drills with each client; failover test of all 11 environments; port partner addenda | Signed agreements; drill reports; DR test report |
| 2027 Q1 (March) | Readiness check by Internal Audit for both service lines | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 to Q3 | SL-2 Type 2 period (2027-04-01 to 2027-09-30); SL-1 period running all year | Monthly evidence collection per the evidence map | Evidence map items |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 12 collecting, 6 ready, 7 not started (each tied to a POA&M item or a 2026 Q4 action).

**Customer communication:** SL-1 subscribers receive the 2025 report, a bridge letter and a note on the categories added for 2027. SL-2 clients receive this summary, a bridge letter describing the remediation, the amended agreements, and the expected SL-2 report date (2027-11). Because each client must oversee its own vendors under Subpart F (101.650(f)), the company also gives each client a signed responsibility matrix for the controls it operates on their behalf (POAM-011).
