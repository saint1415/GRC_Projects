# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies came with standards for cloud configuration, encryption, and endpoints, because those were built with the landing zone. Nothing set measurable minimums for the shop floor, suppliers, or AI, which is where the 2026 findings concentrate (P03; P01 R-004, R-010, R-020, R-026). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL), then standard (STD), then procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what the annual self-assessment and the co-sourced internal audit check.
- **Plant coverage:** every standard applies to both plants. Where Plant 2 cannot meet a standard before its integration date, the gap is a POA&M item, not an exception.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration and change standard** | POL-01 | Security Manager with the Manufacturing Systems Manager | Existing for cloud and endpoints (2024); shop-floor sections in draft | 2026-12-31 | Benchmark-based baselines for cloud workloads, endpoints, MES and DNC servers, terminals, and network devices; documented deviations; monthly drift report; every change to in-scope systems through the change advisory board with a security impact review; emergency changes reviewed within 2 business days | CM-2, CM-3, CM-4, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft (gap 3) | 2026-11-30 | Required event types per system class; every in-scope system, including MES, DNC, OT gateways, and plant firewalls, sends logs to the SIEM; 1 year searchable and 6 years in the write-once archive; MSSP high-severity escalation within 30 minutes; alerts for bulk export, impossible travel, new mailbox rules, and new sync clients | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Supplier and service provider security standard** | POL-01 | Director of Supply Chain with the Security Manager | Draft (gap 5, gap 10) | 2026-10-31 | DFARS 252.204-7012, 252.204-7020, and (from 2026-11-10) 252.204-7021 in every purchase order that involves CUI; SPRS and CMMC status checked before any CUI is sent and each year; vendor tiers with annual review of Tier 1 providers (P09); CRM on file for every ESP; security terms in IT and OT purchases | SA-4, SA-9, SR-3, SR-6 |
| STD-04 | **OT and shop-floor security standard** | POL-02, POL-04 | Manufacturing Systems Manager | Draft (gaps 1, 2, 8) | 2027-01-31 | Shop-floor VLANs behind an enclave firewall at each plant with no internet route; named sign-in on MES terminals; complete OT inventory with CMMC asset category; programs only from DNC or inventoried drives; vendor access only through the broker; compensating controls for unsupported systems; passive network monitoring; imaging steps for incident evidence | CM-8, SC-7, SA-22, MA-4, MP-7, SI-4 |
| STD-05 | **AI use standard** | POL-01, POL-05 | Director of Engineering with the vCISO | Draft (gap 11) | 2026-12-31 | AI inventory; tiering per P10; security, export, and legal review before use; no CUI in any AI tool outside the enclave; written boundary confirmation for any enclave AI feature; human review of outputs; numeric rule for engineering data; bias and performance testing for High-tier tools; monitoring and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Identity and privileged access standard | POL-02 | Security Manager | Existing (2024); update due | 2026-12-31 | 14-character minimum and banned list; MFA for all; hardware keys for administrators and, by 2027-01-31, phishing-resistant authenticators for all enclave users; vaulted and rotated service credentials; quarterly access reviews; break-glass accounts tested quarterly | IA-2, IA-5, AC-2, AC-6(2) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | IT Director | Draft (gap 7) | 2026-12-31 | Recovery objectives from the BIA (P05); nightly encrypted backups of every in-scope system to the backup account; quarterly restore tests for each High-criticality process; annual recovery exercise; revision check against PLM before any restored program is released | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Cryptography and key management standard | POL-04 | IT Director | Existing (2024); minor update | 2026-11-30 | FIPS-validated modules on every CUI path and store, recorded in the SSP module table; TLS 1.2 or higher; company-managed keys; separate backup keys | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024) for cloud and endpoints; update due | 2026-12-31 | Monthly authenticated scans of every in-scope system, including MES and DNC; passive discovery for controllers; remediation targets: Critical 15 days, High 30 days, Moderate 90 days; quarterly MES patch windows coordinated with production; unsupported software replaced or isolated | RA-5, SI-2, SA-22 |
| STD-10 | Physical security and visitor management standard | POL-05 | Facilities and Security Manager | Existing at Plant 1 (2024); Plant 2 rollout | 2026-10-31 | Electronic visitor system at both plants; escort in production, engineering, and test areas; foreign-national visits announced to trade compliance; quarterly badge review; camera retention 90 days | PE-2, PE-3, PE-8 |
| STD-11 | CUI marking and media handling standard | POL-04 | Director of Quality | Draft (gap 13) | 2026-11-30 | Banner on all printed CUI from both MES; cell cabinets and job-close return; locked shred bins with certificates; transport log; labeled encrypted USB drives only at the 8 legacy machines | MP-3, MP-4, MP-5, MP-6, MP-7 |

**Summary:** 11 standards. 4 exist from 2024 and need updates (STD-06, STD-08, STD-09, and STD-10 at Plant 1); STD-01 exists for the cloud and endpoints and is being extended to the shop floor; 6 are new drafts requested by the gap analysis (STD-02, STD-03, STD-04, STD-05, STD-07, STD-11).

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 (by 2026-10-31) | STD-03 Supplier and service provider security; STD-10 Physical security and visitor management |
| 2026 Q4 (by 2026-11-30) | STD-02 Logging and monitoring; STD-08 Cryptography; STD-11 CUI marking and media |
| 2026 Q4 (by 2026-12-31) | STD-01 Configuration and change; STD-05 AI use; STD-06 Identity and privileged access; STD-07 Contingency and recovery; STD-09 Vulnerability and patch |
| 2027 Q1 (by 2027-01-31) | STD-04 OT and shop-floor security |

All standards are in force before the readiness re-check in 2027-02, so that the C3PAO sees final, approved documents (draft evidence is not acceptable, 32 CFR 170.24(b)(1)).

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
