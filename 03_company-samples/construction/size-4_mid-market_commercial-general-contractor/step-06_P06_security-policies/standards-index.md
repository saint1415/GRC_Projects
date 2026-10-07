# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies had standards for cloud configuration, endpoints, and encryption only. The 2026 assessments found that the rules that failed were the ones nobody had written down in measurable form: how CUI moves to the field, how a bank-change call-back is evidenced, how jobsite routers are configured, and how subcontractors are checked before they receive CUI (P03 G-003, G-020, G-118, G-122; P01 R-002, R-003, R-011). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps) sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register. No exception may allow CUI outside the CPE.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration and vulnerability management standard** | POL-01, POL-02 | Security Manager | Existing (2024) for cloud and endpoints; jobsite and CPE sections in draft | 2027-01-31 | Benchmark-based baselines for laptops, servers, cloud workloads, enclave laptops, the virtual desktop image, rugged tablets, and jobsite routers; no internet-facing router administration; monthly drift report; monthly authenticated scans including enclave laptops; remediation: Critical 15 days, High 30 days; data-movement test for every virtual desktop image change | CM-2, CM-3, CM-6, CM-7, RA-5, SI-2 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Existing (2024); update in draft | 2027-01-31 | Required event types per system class; SYS-01 audit logs, SYS-02 vendor-master changes, jobsite routers, and the CPE all monitored; CPE logs in a monitoring service inside the government-community cloud with 24x7 alerting; 1 year searchable retention; correlation of corporate and enclave identities; MSSP high-severity escalation within 30 minutes | AU-2, AU-6, AU-6(3), AU-11, AU-12, SI-4 |
| STD-03 | **Vendor and subcontractor security standard** | POL-01 | Director of Contracts and Compliance with the vCISO | New; draft | 2026-12-31 | Vendor tiers (Tier 1: holds CUI, FCI at scale, payment data, or client security details, or supports a High-criticality process); annual SOC 2 Type 2 or FedRAMP package review for Tier 1 with complementary control mapping; subcontractor CUI gate: DFARS 252.204-7012 in the subcontract, verified SPRS score, CMMC status when required, named CUI recipients; incident notice terms; data return at closeout | SA-4, SA-9, SR-6, RA-3(1), AC-20(1) |
| STD-04 | **Payment verification standard** | POL-01 | Controller | New; issued 2026-09-17 | Issued | Call-back script and evidence fields (number called, source of the number, person reached, time); second approver who did not enter the change; no override in the ERP workflow; 10-business-day hold on first payment above $50,000 to a changed account; quarterly sample of 25 changes by internal audit; owner remittance-change notice on every pay app | AC-5, SI-7, AT-2(3) |
| STD-05 | **AI use standard** | POL-01, POL-05 | vCISO with the AI review group | New; draft | 2026-12-31 | AI inventory; risk tiering per P10; security, privacy, and bias review before use; no CUI in any AI tool; no AI write access to payment fields; enterprise terms with no training on company data; human review of outputs; adverse impact testing for employment uses; worker notice for video analytics | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due | 2026-12-31 | 14-character minimum and banned list; MFA for all; FIDO2 for CPE users, administrators, executives, and payment roles; help desk reset verification for those roles; privileged access broker for servers; break-glass accounts tested quarterly | IA-2, IA-2(8), IA-5, AC-6(2) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | IT Director | New; draft | 2026-12-31 | Recovery objectives from the BIA (P05); quarterly restore tests for High-criticality processes; independent CPE backup; nightly SYS-01 and SYS-02 exports; MBSS rebuild test in a second region; preservation before rebuild for CUI incidents | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director | Existing (2024); FIPS update due | 2026-11-30 | Approved algorithms and protocols (TLS 1.2 or higher); FIPS-validated modules for all CUI at rest and in transit (enclave laptops in FIPS mode); encryption at rest for Restricted and FCI data on every device; company-managed keys for commercial cloud workloads | SC-8, SC-8(1), SC-12, SC-13, SC-28 |
| STD-09 | **CUI handling standard** | POL-04 | FC-4 Project Executive with the Director of Contracts and Compliance | New; draft | 2026-10-31 | CUI intake and distribution list; CPE workflow for CUI RFIs and submittals; marking checks for A&E packages; numbered printed sets, sign-out log, CUI room, sealed transport, locked shred bin with certificates; tablet use only as virtual desktop clients; quarterly content search of SYS-01 and the corporate suite for CUI markings | AC-4, MP-2, MP-3, MP-4, MP-5, MP-6 |
| STD-10 | Facility and jobsite security standard | POL-02 | Vice President of Operations | Existing (2024); update for the CUI room and trailer keys | 2026-11-30 | Badge access at offices, the yard, and the MBSS room; trailer lock rule; CUI room with badge lock and authorized-access list; visitor sign-in and escort; weekly reconciliation with installation gate records; key and combination inventory; quarterly badge review | PE-2, PE-3, PE-8 |

**Summary:** 10 standards. 5 are new (STD-03, STD-04, STD-05, STD-07, STD-09); STD-04 was issued with the policies on 2026-09-17 because payment fraud is the company's top recurring risk. 5 existed in 2024 and need updates (STD-01, STD-02, STD-06, STD-08, STD-10).

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q3 (issued) | STD-04 Payment verification |
| 2026 Q4 | STD-03 Vendor and subcontractor security; STD-05 AI use; STD-06 Authenticator and privileged access; STD-07 Contingency and recovery; STD-08 Encryption; STD-09 CUI handling; STD-10 Facility and jobsite security |
| 2027 Q1 | STD-01 Configuration and vulnerability management; STD-02 Logging and monitoring |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
