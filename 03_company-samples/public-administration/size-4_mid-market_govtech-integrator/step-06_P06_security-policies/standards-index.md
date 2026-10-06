# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | GRC Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent, but the company had no measurable rules for remote administration of agency systems, AI, or screening by position, and its configuration standard covered only the cloud (gap 8 in `../00_company-facts.md`; P01 R-001, R-004, R-009). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds, including the CJIS and Pub. 1075 values the agencies require. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure or runbook. A standard may not weaken its parent policy or an agency requirement.
- **Approval:** the standard's owner drafts it, the GRC Manager reviews it for consistency with the SSP parameter values (PL-11), and the parent policy's approver signs it.
- **Agency values:** where CJISSECPOL v6.1, Pub. 1075, or a contract sets a stricter value, the standard states that value and cites it.
- **Exceptions:** under POL-01 statement 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | Configuration standard | POL-01, POL-04 | Director of Cloud Operations with the Director of Managed Services | Existing (2024) for the cloud; extension to managed agency servers in draft (gap 8) | 2027-03-31 | Benchmark-based baselines for container images, cloud accounts, laptops, and (new) agency servers the company administers; daily posture checks; documented deviations with approval; emergency changes with a second approver and review within 2 business days | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | Logging and monitoring standard | POL-03 | Security Operations Manager | Existing (2025); update in draft (gap 4) | 2026-12-31 | Event types and rationale per system class; application audit events for regulated tenants and SYS-10 session logs to the SIEM; retention 7 years for FTI enclave audit records and at least 1 year for CJI systems; alert within 1 hour of a logging failure; weekly review of regulated-record access with referral rules; MDR escalation within 30 minutes | AU-2, AU-5, AU-6, AU-11, SI-4 |
| STD-03 | Vendor risk management standard | POL-01 | Director of Contracts and Compliance | Draft in progress (gap 7) | 2026-12-31 | Tiers (Tier 1: agency data at scale, agency system access, or supports a High-criticality process; Tier 2: limited agency data; Tier 3: none); contract terms before any agency data or access (security, breach notice within 72 hours, data use, deletion); FTI only with IRS approval and Exhibit 7 terms; CJI only with the Security Addendum; Tier 1 annual SOC 2 Type 2 (or equivalent) review with complementary control mapping and bridge letter; Tier 2 every 2 years | SA-4, SA-9, SR-6, SR-8 |
| STD-04 | **Remote administration of agency systems standard** | POL-02 | Director of Managed Services with the Director of Information Security | New, draft in progress (gap 1) | 2026-11-30 | No standing credentials: agency credentials in the vault, released per session, rotated after use; phishing-resistant MFA for every engineer; session recording kept at least 1 year (CJIS AU-11); SYS-10 logs to the SIEM; no path from SYS-10 into the landing zone; automation tokens scoped per agency and stored in the secrets manager; FIPS 140-3 certified modules for agent traffic to CJI systems; agency-side accounts removed within 24 hours of termination; patching to CJIS timelines (critical 15 days, high 30) with a monthly report to each agency | AC-17, MA-4, IA-5, AU-2, SI-2 |
| STD-05 | **AI use and development standard** | POL-01, POL-05 | Director of Data and AI with the vCISO | New, draft in progress (gap 9) | 2026-12-31 | AI inventory; risk tiering per P10; review before use or release; signed data-use and no-training terms for any service touching Restricted data; no FTI or CJI to any AI service; human review rules for consequential decisions; bias testing before release and quarterly for High-tier use cases; model version and prompt logging; developer documentation for deployers (Colorado SB26-189); decommissioning criteria | PM-9, SA-9, SA-11, RA-3, PL-4 |
| STD-06 | Authenticator and privileged access standard | POL-02 | Director of Information Security | Existing (2024); update in draft | 2026-12-31 | 14-character minimum with a banned list; MFA for all; phishing-resistant keys for administrators and anyone with access to regulated data or agency systems by 2027-01-31; just-in-time elevation with a 4-hour limit; lockout values (CJI: 5 in 15 minutes, administrator release; FTI enclave: 3 in 120 minutes); secrets rotated every 90 days; break-glass tested quarterly | IA-2, IA-5, AC-6(5), AC-7 |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | Director of Cloud Operations | Draft in progress (gap 5) | 2026-12-31 | Recovery objectives from the BIA (P05) and contracts (RTO 8 hours and RPO 1 hour for regulated tenants); timed restore of each regulated tenant twice a year; annual region B failover exercise; document storage in the write-once vault; rebuild runbook for a clean account; plan for loss of SYS-10 | CP-2, CP-4, CP-6, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | Director of Cloud Operations | Existing (2024); FIPS update in draft (gap 6) | 2026-10-31 | TLS 1.2 or higher; FIPS 140-3 certified modules for CJI in transit (no FIPS 140-2 certificates after 2026-09-21); FIPS 140 validated modules for FTI in transit and at rest; customer-managed keys for regulated data with annual rotation; module inventory kept current | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Operations Manager | Existing (2024); update for managed systems in draft | 2026-11-30 | Weekly authenticated scans of cloud workloads; monthly scans of managed agency servers (with the agency); remediation within CJIS timelines (critical 15 days, high 30, medium 60, low 90) for every system that handles CJI, and the same targets elsewhere; weekly known-exploited vulnerability review; annual penetration test | RA-5, SI-2, SI-5 |
| STD-10 | **Personnel screening standard for designated positions** | POL-01 | HR Director | New, draft in progress (gap 2) | 2026-10-31 | Position designation for CJI, FTI, and motor vehicle data access; fingerprint-based checks (CJI) and Pub. 1075 background investigations (FTI) completed and Security Addendum certification or penalty notice signed before access; provisioning blocked until HR clears the gate; reinvestigation within 5 years for FTI positions; annual FTI recertification with access suspended at expiry; monthly authorized-staff lists to AG-01 | PS-2, PS-3, PS-6, AT-2 |

**Summary:** 10 standards. Four are new and in draft (STD-03, STD-04, STD-05, STD-10); STD-07 is a draft that replaces the 2024 contingency procedure; five exist and are being updated (STD-01, STD-02, STD-06, STD-08, STD-09).

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 (by 2026-10-31) | STD-08 Encryption (FIPS 140-3); STD-10 Personnel screening |
| 2026 Q4 (by 2026-12-31) | STD-04 Remote administration (2026-11-30); STD-09 Vulnerability and patch (2026-11-30); STD-02 Logging; STD-03 Vendor risk; STD-05 AI; STD-06 Authenticator; STD-07 Contingency |
| 2027 Q1 | STD-01 Configuration (extension to managed agency servers) |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
