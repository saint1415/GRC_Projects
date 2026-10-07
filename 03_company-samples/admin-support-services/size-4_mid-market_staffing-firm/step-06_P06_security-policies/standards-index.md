# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-22 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent but gave staff and vendors few measurable rules for SaaS configuration, logging, vendors, retention, or payroll controls (P03 G-022, G-038, G-045, G-068; P01 R-014, R-021, R-046). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps) sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts it, the Security Manager reviews it for consistency, and the COO signs it.
- **Exceptions:** under POL-01 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks, and the SOC 2 examination (P09) will test the ones in scope.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-22) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration, change, and secure development standard** | POL-01 | IT Director | Draft in progress | 2027-03-31 | Baselines for laptops, kiosks, containers, network devices, and the ATS, payroll, credentialing, and VMS tenants; quarterly configuration export compared with baseline; change log with business owner and IT Director approval for settings that affect pay, I-9s, credential verification, or AI behavior; code review, secret and dependency scanning, and no credentials in code or images for firm-written code and contractors | CM-2, CM-3, CM-6, SA-11, SA-15 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress | 2027-01-31 | Required events per system class; identity, payroll, ATS, credentialing, VMS, cloud, and endpoint logs in the SIEM; 1 year searchable and 3 years in the write-once bucket; monthly export of payroll audit reports; alerts for payroll register exports, more than 20 bank changes in an hour, bank changes from new devices, ATS bulk downloads, and warehouse queries on Restricted columns; MSSP escalation within 30 minutes | AU-2, AU-6, AU-6(1), AU-11, AU-12, SI-4 |
| STD-03 | **Vendor risk management standard** | POL-01 | Security Manager with the General Counsel | Draft in progress | 2026-12-31 | Tiers (Tier 1: Restricted data at scale or a High-criticality BIA process; Tier 2: limited personal information; Tier 3: none); purchasing gate; security addendum with 72-hour breach notice, no-training and deletion terms for AI vendors, and data return at exit; Tier 1 annual SOC 2 Type 2 review with complementary control mapping and bridge letter; Tier 2 questionnaire every 2 years | SA-4, SA-9, SR-6, RA-3(1) |
| STD-04 | **Records retention and disposal standard** | POL-04 | Director of Compliance and Privacy | Draft in progress | 2026-12-31 | The POL-04 4.6 schedule by system; quarterly purge jobs with reports; legal hold procedure; certified destruction for devices; finger template deletion report from the timekeeping vendor monthly | SI-12, MP-6 |
| STD-05 | **AI use standard** | POL-01, POL-05 | Director of Recruiting Operations with the vCISO and the General Counsel | Draft in progress | 2026-12-31 | AI inventory including features inside SaaS; tiering per P10; review before use; no automatic rejection or advancement; candidate notice and accommodation path; quarterly bias and validity tests for High-tier tools; vendor data use terms; decommissioning criteria | PM-9, RA-3, SA-9, PL-4 |
| STD-06 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due | 2026-12-31 | 14-character minimum and banned list; MFA for all staff; phishing-resistant authenticators for payroll, billing, and administrators by 2027-03-31; no SMS for accounts that can change pay; separate administrator accounts; API keys in the secrets service, scoped and rotated; break-glass accounts tested quarterly | IA-2, IA-2(1), IA-5, AC-6(2), AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03 | IT Director with the Director of Payroll and Billing | Draft in progress | 2026-12-31 | Recovery objectives from the BIA (P05); off-cycle manual payroll procedure with the bank and payroll vendor, tested twice a year; daily assignment and credential status exports; quarterly restore tests of the warehouse, integration platform, and archive; annual recovery exercise | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director | Existing (2024); minor update | 2027-03-31 | TLS 1.2 or higher; encryption at rest for all Restricted data; company-managed keys for the warehouse and archive; separate backup keys | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024); update due | 2026-12-31 | Monthly authenticated scans (moving from quarterly); container image scanning; weekly known-exploited vulnerability review; remediation targets: Critical 14 days for internet-facing systems and 30 days otherwise, High 60 days; firmware schedule for clocks and kiosks | RA-5, SI-2, SI-5 |
| STD-10 | **Payroll and bank-change controls standard** | POL-02 | Director of Payroll and Billing | Draft in progress | 2026-12-31 | Call-back to the number on file or a one-payroll hold for new bank accounts; no bank changes by email, text, or unverified call; second review of new associates without an E-Verify case and of manual punches; Controller approval of each register; monthly analytics on duplicate bank accounts and addresses; pay continuity within 1 business day for diverted pay | AC-5, AU-6, IA-2 |

**Summary:** 10 standards. Seven are new and in draft (STD-01 to STD-05, STD-07, STD-10). STD-06, STD-08, and STD-09 exist from 2024 and need updates.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Vendor risk; STD-04 Retention and disposal; STD-05 AI use; STD-06 Authenticator and privileged access; STD-07 Contingency and recovery; STD-09 Vulnerability and patch; STD-10 Payroll and bank-change controls |
| 2027 Q1 | STD-01 Configuration, change, and secure development; STD-02 Logging and monitoring; STD-08 Encryption and key management |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
