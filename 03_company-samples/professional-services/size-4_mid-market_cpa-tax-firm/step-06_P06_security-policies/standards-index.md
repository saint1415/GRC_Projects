# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (and Cris Santos Assurance, LLP) |
| Owner | GRC Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-22 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.7; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 WISP had policies but few measurable standards, so staff, practice administrators, and vendors had no fixed rules for SaaS settings, logging, vendors, retention, AI, or the offshore program (gap 14 in `../00_company-facts.md`; P03 G-001; P01 R-029 and R-040). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps) sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts it, the GRC Manager reviews it for consistency, the Qualified Individual confirms it meets 16 CFR 314.4, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 4.8, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-22) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration and SaaS baseline standard** | POL-01, POL-04 | Chief Information Officer | Draft in progress | 2027-03-31 | Benchmark baselines for laptops, desktops, servers, cloud images, and network devices; documented baselines for each SaaS tenant (tax software, portal, productivity suite, identity provider, CAS platform), including MFA, forwarding, sharing, and AI feature settings; tenant setting changes through change control; weekly drift report | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Director of Information Security | Draft in progress | 2027-01-31 | Required event types per system class; tax software, portal, DMS, and CAS platform activity in the SIEM; alerts for bulk downloads, new inbox rules and forwarding, token reuse, and bank-change spikes; inbox-rule alerts may be tuned but never suppressed; 1 year searchable and 7 years archived; MSSP high-severity escalation within 30 minutes | AU-2, AU-6, AU-6(1), AU-11, SI-4 |
| STD-03 | **Vendor risk management standard** | POL-01 | GRC Manager | Draft in progress | 2026-12-31 | Tiers (Tier 1: Restricted data at scale, privileged access, or a High-criticality BIA process; Tier 2: limited Restricted data; Tier 3: no client data); security terms and breach notice of 10 days or less before any client data; BAA where ePHI is involved; IRC 7216 contractor notice; Tier 1 annual SOC 2 Type 2 review with complementary user entity control mapping and bridge letter; Tier 2 every 2 years | SA-4, SA-9, SR-6, RA-3(1), PS-6 |
| STD-04 | **Data handling, IRC 7216 disclosure, and retention standard** | POL-04 | Privacy Officer | Existing (2024 retention schedule); update in progress | 2027-03-31 | Retention schedule (7 years for tax files; 3 years minimum for Forms 8878 and 8879; 6 years for HIPAA documentation); annual disposal run with legal hold checks; consent templates, expiry tracking, and the release gate; PHI handling procedure for engagement teams | SI-12, MP-6, AC-21 |
| STD-05 | **AI use standard** | POL-01, POL-05 | General Counsel with the Director of Information Security | Draft in progress | 2026-12-31 | AI inventory; risk tiering per P10; intake and review before any AI tool or feature goes live; IRC 7216 basis for any client data; vendor terms (U.S. processing, no training, deletion); human review of outputs; adverse impact testing for any tool used in employment decisions; monitoring and decommissioning triggers | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | Chief Information Officer | Existing (2024); update in progress | 2026-12-31 | 14-character minimum and banned list; number matching for all; security keys for administrators, partners, finance, and CAS payroll staff; separate privileged accounts; vaulted and rotated service accounts; break-glass accounts tested quarterly; service desk identity verification for resets | IA-2, IA-2(8), IA-5, AC-6(2), AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | Chief Operating Officer with the Chief Information Officer | Draft in progress | 2026-12-31 | Recovery objectives from the BIA (P05); quarterly restore tests of the DMS and workpaper application; annual CAS repeat-payroll exercise; deadline-week vendor outage procedure; early-extension triggers | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | Chief Information Officer | Existing (2024); minor update | 2027-03-31 | TLS 1.2 or higher; encryption at rest for all Restricted data; Company-managed keys for cloud workloads and the enclave; separate backup keys; enforced encryption for any email with tax attachments | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Director of Information Security | Existing (2024); update in progress | 2026-12-31 | Monthly authenticated scans of internet-facing services and quarterly internally; assessment after every material change; known-exploited vulnerabilities on internet-facing services fixed within 7 days; Critical 14 days, High 30 days otherwise; annual penetration test scope set from P01 | RA-5, SI-2, CA-8 |
| STD-10 | Facility and remote work security standard | POL-01, POL-05 | Chief Operating Officer | Existing (2024); update in progress | 2027-06-30 | Badge access for every network closet; pull printing at every office; visitor logs; quarterly badge review; home printing only by approval with shredding | PE-2, PE-3, PE-5, PE-8 |
| STD-11 | **Offshore preparation program security standard** | POL-01, POL-04 | Director of Tax Operations | Draft in progress | 2026-12-15 | Consent signed before routing; SSN masking in the tax software and in DMS images; U.S.-hosted desktops with no export, print, clipboard, or drive mapping; route limited to assigned returns; named vendor accounts with MFA; turnover reported within 1 business day; annual vendor assessment; IRC 6713 and 7216 notice to each vendor individual | SA-9(5), PS-7, AC-3, AC-4, AC-21 |

**Summary:** 11 standards. Six are new and in draft (STD-01, STD-02, STD-03, STD-05, STD-07, STD-11). Five exist from 2024 and are being updated (STD-04, STD-06, STD-08, STD-09, STD-10).

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-11 Offshore program (2026-12-15); STD-03 Vendor risk; STD-05 AI use; STD-06 Authenticator; STD-07 Contingency; STD-09 Vulnerability and patch |
| 2027 Q1 | STD-01 Configuration and SaaS baseline; STD-02 Logging and monitoring; STD-04 Data handling and retention; STD-08 Encryption |
| 2027 Q2 | STD-10 Facility and remote work |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
