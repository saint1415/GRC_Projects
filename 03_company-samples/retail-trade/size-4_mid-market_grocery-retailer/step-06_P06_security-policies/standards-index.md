# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent but had few supporting standards, so staff and vendors had no measurable rules for store devices, configuration, logging, vendors, or the checkout page (gap 12 in `../00_company-facts.md`; P03 rows G-006, G-007, G-043, G-063; P01 R-040). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps) sit under the standards and are owned by the teams that run them. Where PCI DSS lets the company set a frequency, the standard cites the targeted risk analysis that supports it (POL-01 4.3).

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07, internal audit, or the QSA checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-02 | Security Manager | Draft in progress (gap 12) | 2027-03-31 | Benchmark-based baselines for store servers, registers (with the POS vendor), network devices, cloud virtual machines, and SaaS tenants; vendor defaults changed before deployment; only needed services; monthly drift report; documented deviations | CM-2, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress (gap 5) | 2027-01-31 | Required event types per system class, including CDE components; all EPP components send logs to the SIEM; automated daily review of CDE logs by MSSP use cases; 12 months retained with 3 months immediately searchable; alert on failures of logging, anti-malware, and EDR | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor and TPSP risk management standard** | POL-01 | Privacy and Compliance Manager | Draft in progress (gap 6) | 2026-12-31 | TPSP list and PCI DSS responsibility matrix; AOC on file and checked yearly; vendor tiers (Tier 1: card data, customer data at scale, or CDE access; Tier 2: limited data; Tier 3: no data or access); Tier 1 annual SOC 2 or AOC review with bridge letter; breach notice terms of 72 hours for Tier 1; data use and deletion terms; exit terms | SA-9, SR-6, RA-3(1), SA-4 |
| STD-04 | **Store and POS device standard** | POL-02, POL-05 | IT Director with the Director of Store Operations | Draft in progress (gaps 3, 4, 11) | 2026-12-31 | Complete inventory of PIN pads, registers, store servers, and OT devices, reconciled monthly with the processor's PIN pad records; PIN pad inspections daily for self-checkouts and weekly for staffed lanes (targeted risk analysis), logged; no unapproved connections; IoT devices on a separate VLAN at every site; vendor access only through the access broker; locked server enclosures | CM-8, SR-11, SC-7, AC-4, MA-4, PE-3 |
| STD-05 | **AI use standard** | POL-01, POL-05 | vCISO with the Director of E-commerce and Marketing | Draft in progress (gap 10) | 2026-12-31 | AI inventory; risk tiering per P10; security, privacy, and fairness review before use; no-training and deletion terms in vendor contracts; human review of outputs that reach customers, suppliers, applicants, or prices; fairness tests for pricing and hiring tools; no biometric identification in stores | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due | 2027-03-31 | 14-character minimum and banned list; MFA for all, including vendors and the agency; phishing-resistant MFA for administrators; vaulted and rotated service and vendor credentials; unique register local administrator passwords; break-glass accounts tested quarterly | IA-2, IA-5, AC-6(2), AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | IT Director | Draft in progress (gap 7) | 2026-12-31 | Recovery objectives from the BIA (P05); quarterly restore tests per company-managed workload; off-site immutable copies of store server images; yearly store offline-mode test; DC and refrigeration downtime procedures; yearly DR exercise | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director | Existing (2024); minor update | 2027-03-31 | Approved algorithms and protocols (TLS 1.2 or higher); encryption at rest for all Restricted data; company-managed keys for cloud workloads; separate backup keys; yearly review of cryptographic suites in use | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024); update due | 2026-12-31 | Monthly authenticated scans of support-center and cloud systems; quarterly company-run internal scans of the CDE with rescans; quarterly ASV scans; critical patches within 30 days (including vendor-managed registers), high within 60 days; yearly internal, external, and segmentation penetration tests | RA-5, SI-2, CA-8 |
| STD-10 | **Payment page script and change standard** | POL-01, POL-02 | Director of E-commerce and Marketing with the Security Manager | New (gap 2) | 2026-11-15 | Inventory of every script on website and app checkout pages with owner, written justification, and approval; integrity values and content security policy; no tag manager on checkout pages; change ticket and second-person approval for theme and tag changes; tamper detection on both checkouts with alerts to security, at a frequency set by targeted risk analysis | CM-3, CM-7, CM-8, SI-7 |

**Summary:** 10 standards. Six new standards were requested in the gap analysis (STD-01 to STD-05 and STD-10); five are in draft and STD-10 is being written first because of the QSA date. STD-06, STD-08, and STD-09 exist from 2024 and need updates. STD-07 is new.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-10 Payment page script and change (2026-11-15); STD-03 Vendor and TPSP; STD-04 Store and POS devices; STD-05 AI use; STD-07 Contingency and recovery; STD-09 Vulnerability and patch |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging and monitoring; STD-06; STD-08 |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
