# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Information Security Manager (index); each standard has its own owner below |
| Approved by | Chief Information Officer, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2023 policies stated intent but had few supporting standards, so staff, vendors, and the servicer had no measurable rules for configuration, logging, vendors, student authentication, or retention (gap 10 in `../00_company-facts.md`; P03 314.3(a); P01 R-040 and R-027). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps) sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) → standard (STD) → procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Information Security Manager reviews it for consistency, the Qualified Individual confirms it meets 16 CFR Part 314, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register. MFA and encryption exceptions also need the Qualified Individual's written approval.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | Information Security Manager | Draft in progress (gap 10) | 2027-03-31 | Benchmark-based baselines for staff endpoints, lab images, cloud virtual machines, network devices, and SaaS tenant settings; documented deviations; monthly drift report; change control for SIS configuration and integration jobs with a second reviewer; new SaaS AI features off until reviewed | CM-2, CM-3, CM-4, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Information Security Manager | Draft in progress (gap 6) | 2027-01-31 | Required event types per system class (SIS and FAMS: record views of other students, exports, grade changes, refund bank changes, role changes); all SILP components send logs to the SIEM; 12 months searchable and 3 years archived; detections for credential stuffing and bank-change bursts; monthly user activity review; MSSP escalation within 30 minutes | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor risk management standard** | POL-01 | Chief Compliance Officer | Draft in progress (gap 3) | 2026-12-31 | Vendor tiers (Tier 1: customer information or education records at scale, privileged access, or a High-criticality process; Tier 2: limited student data; Tier 3: no student data); required contract terms (safeguards, FERPA school-official terms, MFA, 72-hour incident notice, return or deletion, right to assess); Tier 1 annual SOC 2 Type 2 review with CUEC mapping and bridge letter; Tier 2 reassessed every 2 years; purchasing and card gate | SA-4, SA-9, SR-6, RA-3(1) |
| STD-04 | **Student identity and account recovery standard** | POL-02 | Chief Information Officer with the Vice President of Enrollment Management | New; draft in progress (gaps 1 and 12) | 2026-11-30 | Student MFA by default (opt-out only with Qualified Individual approval); step-up MFA and prior-contact confirmation for refund bank, contact, and MFA changes; 3-business-day hold on refunds to new accounts; identity-proofed help desk resets (no security questions); applicant document and liveness verification for online programs; fraud indicators and OIG referral handoff | IA-2(2), IA-5, IA-11, IA-12, IA-12(2), IA-12(3) |
| STD-05 | **AI use standard** | POL-01, POL-05 | Provost and Chief Academic Officer with the vCISO | Draft in progress (gap 9) | 2026-12-31 | AI inventory; risk tiering per P10; security, FERPA, and bias review before use; contract with no-training and deletion terms; no FAFSA-derived inputs; human review before any action on an individual; notice to affected students and applicants; monitoring and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | Chief Information Officer | Existing (2023); update due | 2026-12-31 | 14-character minimum for staff and 12 for students with a banned list; MFA for all; phishing-resistant MFA for administrators; separate admin accounts; vaulted and rotated service credentials; unique lab local administrator passwords; break-glass accounts tested quarterly, including the emergency notification console; semiannual and quarterly access review procedures | IA-2, IA-5, AC-2, AC-6(2), AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | Chief Information Officer | Draft in progress (gap 5) | 2026-12-31 | Recovery objectives from the BIA (P05); IT DR plan; quarterly restore tests per college-managed workload; annual DR exercise; emergency refund procedure; Clery notification fallback path | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | Information Security Manager | Existing (2023); minor update | 2027-03-31 | TLS 1.2 or higher; encryption at rest for all Restricted data; enforced email encryption for aid data; college-managed keys for cloud workloads; separate backup keys | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Information Security Manager | Existing (2023); update due | 2026-12-31 | Monthly authenticated scans of all VLANs, including labs and campus safety (moving from quarterly); scans after material changes; weekly known-exploited vulnerability review; remediation targets: Critical 14 days internet-facing and 30 days otherwise, High 60 days; annual risk-based penetration test including portals and internal networks | RA-5, SI-2, SI-5, CA-8 |
| STD-10 | Facility and campus safety systems security standard | POL-01 | Director of Campus Safety | Existing (2023); update for Campus 3 | 2027-03-31 | Badge access for network closets at all campuses; campus safety devices on a dedicated VLAN; supported firmware; vendor remote access only through the broker; quarterly badge review | PE-2, PE-3, SA-22, MA-4 |
| STD-11 | **Data retention and disposal standard** | POL-04 | Chief Compliance Officer with the Director of Financial Aid | New; draft in progress (gap 10) | 2027-03-31 | Retention schedule by record type that keeps 34 CFR 668.24(e) minimums and disposes of other customer information no later than 2 years after last use (314.4(c)(6)(i)); annual disposal run with a report; annual review of the schedule (314.4(c)(6)(ii)); sanitization certificates for leased devices | SI-12, MP-6 |

**Summary:** 11 standards. The 7 new or redrafted standards requested in the gap analysis (STD-01 to STD-05, STD-07, and STD-11) are in draft. STD-06, STD-08, STD-09, and STD-10 exist from 2023 and need updates.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Vendor risk; STD-04 Student identity; STD-05 AI use; STD-06 Authenticator and privileged access; STD-07 Contingency and recovery; STD-09 Vulnerability and patch |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging and monitoring; STD-08 Encryption; STD-10 Facility and campus safety; STD-11 Retention and disposal |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process
