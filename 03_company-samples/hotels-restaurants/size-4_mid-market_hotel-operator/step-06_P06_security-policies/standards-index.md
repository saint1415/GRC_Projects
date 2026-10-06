# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | GRC Analyst (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent but had few supporting standards, so staff, vendors, and the franchisor had no measurable rules for configuration, logging, vendors, or payment devices (gap 13 in `../00_company-facts.md`; P03 rows G-006, G-041, G-087; P01 R-041 and R-050). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps) sit under the standards and are owned by the teams that run them. Several PCI DSS requirements also need a targeted risk analysis to set a frequency (PCI DSS 12.3.1); those analyses are attached to the standard that sets the frequency.

## 2. How standards work
- **Hierarchy:** policy (POL) then standard (STD) then procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts the standard, the GRC Analyst reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07, the QSA-supported assessment, or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-02 | IT Director | Draft in progress (gap 13) | 2027-03-31 | Benchmark-based baselines for PCs, servers, cloud workloads, firewalls, POS workstations, and lock servers; no vendor default passwords before connection; only needed services; documented deviations; monthly drift report; baselines reviewed yearly | CM-2, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress (gap 6) | 2027-01-31 | Required events per system class; every CDE component, lock server, and franchised-hotel firewall log source in the SIEM; automated daily review of CDE events; SYS-01 card display and export reports reviewed daily by rule; 12 months retention with 3 months searchable; time synchronization; MSSP high-severity escalation within 30 minutes | AU-2, AU-6, AU-6(1), AU-8, AU-11, SI-4 |
| STD-03 | **Vendor and franchisor risk standard** | POL-01 | GRC Analyst with the General Counsel | Draft in progress (gaps 3 and 9) | 2026-12-31 | Vendor tiers (Tier 1: card data, guest data at scale, privileged access, or a High-criticality process; Tier 2: limited data; Tier 3: no data); current AOC for every card vendor each year; Tier 1 SOC 2 Type 2 review with complementary user entity control mapping; PCI DSS responsibility matrix for every card vendor and the franchisor; incident notice within 72 hours for Tier 1 and fast enough for the 24-hour acquirer clock where card data is involved; exit and data return terms | SA-9, SR-6, SR-8, CA-3 |
| STD-04 | **Payment device and card data handling standard (with the retention schedule)** | POL-04, POL-05 | Chief Financial Officer with the Resort Directors of Food and Beverage | Draft in progress (gaps 2, 12, and 13) | 2026-11-30 | Device list with serial numbers; weekly logged inspections (targeted risk analysis attached); staff training; payment links instead of forms; pause-and-resume recording in the CRO; no card data in email, chat, files, or paper; quarterly data discovery scans; the retention schedule in POL-04 4.6 | CM-8, SR-10, SI-12, MP-4, MP-6 |
| STD-05 | **AI use standard** | POL-01, POL-05 | General Counsel with the vCISO | Draft in progress (gap 11) | 2026-12-31 | AI inventory; risk tiering per P10; security, privacy, legal, and business review before use; contracts with no-training and retention terms; human approval rules for pricing, hiring, and guest-facing answers; total price in every AI price display; emergency pricing mode; bias testing; decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due | 2027-03-31 | 14-character minimum and banned list; MFA for all; phishing-resistant MFA for administrators; privileged access only through the broker; vendor sessions approved and recorded; approved roles for full card display; break-glass accounts tested quarterly; interface credentials vaulted and rotated yearly | IA-2, IA-5, AC-6(5), AC-17, MA-4 |
| STD-07 | Contingency and recovery standard | POL-03 | IT Director with the Director of Loss Prevention and Safety | Draft in progress (gap 10) | 2026-12-31 | Recovery objectives from the BIA (P05); quarterly restore tests of company-managed workloads and lock servers; nightly lock server backups to the cloud backup account; downtime procedures and drills twice a year at every hotel; IT section in every hotel hurricane plan | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director | Existing (2024); minor update | 2027-03-31 | TLS 1.2 or higher; encryption at rest for Restricted data; company-managed keys for cloud workloads; separate backup keys | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024); update due | 2026-12-31 | Monthly authenticated internal scans of every in-scope site including Hotels 3 to 6; quarterly ASV scans; known-exploited vulnerabilities on edge devices patched within 72 hours; critical patches within 30 days; annual internal and external penetration tests and segmentation tests | RA-5, SI-2, CA-8 |
| STD-10 | Facility security standard | POL-02 | Director of Loss Prevention and Safety | Existing (2024); update for Hotels 3 to 6 | 2027-03-31 | Badge access or key logs for every server room and network closet; visitor logs for back-of-house areas; quarterly access list reviews | PE-2, PE-3, PE-8 |

**Summary:** 10 standards. The 6 new standards requested by the gap analysis (STD-01 to STD-05 and STD-07) are in draft. STD-06, STD-08, STD-09, and STD-10 exist from 2024 and need updates.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Vendor and franchisor risk; STD-04 Payment device and card data handling; STD-05 AI use; STD-07 Contingency and recovery; STD-09 Vulnerability and patch |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging and monitoring; STD-06; STD-08; STD-10 |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
