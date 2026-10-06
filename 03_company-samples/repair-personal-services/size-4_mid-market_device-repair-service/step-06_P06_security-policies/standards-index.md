# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent, but the rules that make them testable were missing or out of date: how a technician may test a phone without opening its photos, how a recycling device is wiped and proven wiped, which scripts may run on the checkout page, and how fast a leaver's manufacturer portal account must close (P03; P01 R-001, R-004, R-008, R-014). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, checklists, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure, checklist, or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | Security Manager | Draft in progress | 2027-03-31 | Benchmark-based baselines for office endpoints, counter tablets, bench images, container images, network devices, CCTV recorders, and SaaS tenants; default credentials changed before connection; monthly drift report; change records for network and infrastructure changes | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress | 2027-01-31 | Required event types per system, including SYS-01 exports and bulk views, bench session records, lab storage access, and portal and API application logs; all sent to the SIEM; 1 year searchable and 3 years archived; alerts on bulk exports, after-hours lab access, and checkout page changes; monthly Store Manager review of staff activity flags | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor risk management standard** | POL-01 | GRC Analyst with the Chief Financial Officer | Draft in progress | 2026-12-31 | Vendor tiers (Tier 1: customer data at scale, payment functions, or a High-criticality process; Tier 2: limited customer data; Tier 3: no customer data); standard security and data-use addendum (no AI training on company data, deletion, breach notice within 72 hours); annual SOC 2 Type 2 or PCI DSS AOC review for Tier 1 with CUEC mapping and bridge letter; site assessment of the recycler; offboarding checklist | SA-4, SA-9, SR-6, RA-3(1) |
| STD-04 | **Media sanitization and device disposal standard** | POL-04 | Depot Director | Existing (SP 800-88 Rev. 1 procedure); update to Rev. 2 in progress | 2026-11-30 | All recycling drop-offs and retired media sanitized at the Depot line; clear, purge, or destroy by media type per NIST SP 800-88 Rev. 2 and the IEEE 2883 techniques it points to; verification and validation for every device; certificate per device with the Rev. 2 section 4.6 fields; recycler certificates by serial number; quarterly sample re-check | MP-6, SR-12 |
| STD-05 | **AI use standard** | POL-01, POL-05 | vCISO with the Director of Customer Experience | Draft in progress | 2026-12-31 | AI inventory; risk tiering per P10; security and privacy review before use; data-use terms with no-training clause; human review of outputs; disclosure to customers; recording consent for call summaries; adverse impact monitoring for any tool that ranks people; claims about AI performance only from measured data | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due | 2027-03-31 | 14-character minimum and banned list; MFA everywhere including vendor portals; security keys for administrators by 2027-06-30; separate privileged accounts; secrets in the secrets service; break-glass accounts tested quarterly; local accounts reconciled monthly | IA-2, IA-5, AC-6(2), AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | IT Director | New, draft in progress | 2026-12-31 | Recovery objectives from the BIA (P05); quarterly restore tests for the lab and the workloads account; annual recovery test of the partner API and mail-in portal; store downtime kits; manual claims desk procedure; Depot relocation and storm procedures | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | **Customer data access and bench standard** | POL-02, POL-04, POL-05 | Depot Director with the Director of Retail Operations | Existing (2025); update for the bench image rollout | 2026-11-30 | Test checklists by repair type (what may be opened and what may not); standard bench image with session recording, USB blocking, EDR, and phone-pairing control; named bench accounts; transfer drives logged per ticket; cache wipe at ticket close; monthly flag review; evidence handling for suspected misuse | AC-6, MP-7, AU-12, PS-6 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024); update due | 2026-12-31 | Monthly authenticated scans (weekly for internet-facing systems); weekly known-exploited vulnerability review; remediation targets: Critical 14 days internet-facing and 30 days otherwise, High 60 days; legacy bench PCs isolated until replaced | RA-5, SI-2, SA-22 |
| STD-10 | Facility, device custody, and payment terminal standard | POL-04 | Director of Retail Operations | Existing (2024); update due | 2026-11-15 | Locked cabinets for devices; key logs or badge readers on back rooms; terminal list reconciled monthly with the processor; weekly terminal inspection recorded in SYS-01 checklists with Regional Manager review; tamper training; release checks | PE-3, PE-6, CM-8, MP-4 |
| STD-11 | Secure development standard | POL-01, POL-04 | Digital Engineering Manager | New, draft in progress | 2027-03-31 | Threat modeling for new endpoints; static analysis, dependency, and secret scanning gates; pipeline secrets in the secrets service with short-lived credentials; checkout page script inventory, content security policy, subresource integrity, and change detection; annual penetration test with retest | SA-8, SA-11, CM-3, SI-4 |

**Summary:** 11 standards. Six are in draft (STD-01, STD-02, STD-03, STD-05, STD-07, STD-11). Five exist and need updates (STD-04, STD-06, STD-08, STD-09, STD-10). STD-04, STD-08, and STD-10 are due first because the Manufacturer A audit (2026-10) and the SAQ attestations (2026-12-15) rely on them.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-04 Sanitization; STD-08 Customer data access and bench; STD-10 Facility and terminals; STD-03 Vendor risk; STD-05 AI use; STD-07 Contingency; STD-09 Vulnerability |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging; STD-06 Authenticators; STD-11 Secure development |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
