# Business Impact Analysis: Cris Santos Company | Educational Services | Small

**Organization:** Cris Santos Company, LLC (private career college) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Director (Qualified Individual) with the Registrar, Director of Financial Aid, Business Office Manager, and Dean of Academic Affairs | **Approved:** Campus President, 2026-08-21

## 1. Overview and purpose
This BIA identifies which business processes the college depends on, how long each can be down, and how much data it can lose. It supports:
- the recovery part of the written incident response plan required by 16 CFR 314.4(h)(2) and the contingency plan due 2026-12-31 (CP-2);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

## 2. System and business description
The college serves about 900 students from one Florida campus and online, with 60 employees. Student business runs on the Student Information and Financial Aid Platform (SIFAP): a SaaS SIS, a SaaS financial aid management system (FAMS), access to the Department of Education's student aid systems through SAIG, an identity provider, and a cloud tenant (integration server, reporting database, file server, backups). Teaching runs on a SaaS LMS and 5 campus labs. See `../00_company-facts.md` sections 3-4.

## 3. Impact categories and values
Dollar values are scaled to $20.7 million in annual receipts, about $80,000 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $250,000 (about 3 business days of receipts) | $50,000 to $250,000 | Less than $50,000 |
| Operations | Classes or aid processing stop for all students | One program, modality, or office stops | Staff slowed but working |
| Regulatory | Title IV deadline missed, reportable breach, or administrative capability finding | Missed internal or accreditor documentation deadline | Internal policy deviation |
| Safety and student welfare | Students harmed physically or left without living funds | Students inconvenienced financially (delayed refund within deadline) | None |
| Reputation | Regional media coverage, accreditor inquiry, or enrollment loss | Student complaints or online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Registration, enrollment, and academic records | High | 24 h | 8 h | 1 h |
| BP-02 Online instruction delivery | High | 24 h | 8 h | 4 h |
| BP-03 Title IV aid processing and disbursement | High | 72 h | 24 h | 24 h |
| BP-04 Student accounts and credit balance refunds | High | 72 h | 48 h | 24 h |
| BP-05 On-campus and clinical skills instruction | Moderate | 72 h | 24 h | 24 h |
| BP-06 Admissions and new student enrollment | Moderate | 72 h | 24 h | 24 h |
| BP-07 Staff and student communications | Moderate | 24 h | 4 h | 24 h |
| BP-08 Student success advising and early alert | Low | 168 h | 72 h | 24 h |
| BP-09 Payroll and HR | Low | 120 h | 72 h | 24 h |
| BP-10 Compliance and institutional reporting | Low | 168 h | 72 h | 24 h |

Four processes are High, three Moderate, and three Low.

**What drives the values:**
- **Enrollment status drives money.** A student's enrollment and attendance records in the SIS and LMS determine Title IV eligibility and disbursement. That is why BP-01 and BP-02 have the shortest RTOs even though aid itself (BP-03) can wait up to 3 days.
- **Credit balance refunds have a legal clock.** A Title IV credit balance must be paid no later than 14 days after it occurs (34 CFR 668.164(h)(2)). The 72-hour MTD for BP-04 leaves time to catch up within that deadline during a disbursement week.
- **Online students have no fallback classroom.** An LMS outage stops all 300 online students at once (BP-02), while on-campus classes can continue on paper (BP-05).

**Key finding:** the SaaS vendors' recovery commitments carry BP-01 and BP-02. The SIS and LMS SOC 2 reports reviewed in P09 state recovery objectives that meet these RTOs and RPOs. The college-managed workloads (integration server, file server, reporting database) are backed up daily, which meets their 24-hour RPO, but the backups have **never been restore-tested** and sit in the same account as production (P01 R-019). The 24-hour RTO for BP-03, which depends on the integration server, is therefore unproven.

## 5. Resource requirements
| Resource | Description | Supports | Backup or replication method |
|---|---|---|---|
| SYS-06 Identity provider (SaaS) | Single sign-on and MFA for all SaaS systems | All | Vendor-operated; 2 break-glass admin accounts (to be created, POL-02 4.7) |
| SYS-01 SIS (SaaS) | Records, student accounts, student portal | BP-01, BP-03, BP-04, BP-08, BP-10 | Vendor backups; stated RPO 1 h (P09) |
| SYS-02 LMS (SaaS) | Online and on-campus course delivery | BP-02, BP-05 | Vendor backups; stated RPO 4 h (P09) |
| SYS-03 FAMS (SaaS) | Aid processing and the student aid portal | BP-03 | Vendor backups (report requested) |
| SYS-04 SAIG workstations (2) | ISIR downloads and data transmissions to the Department | BP-03 | Reinstall the Department-provided software on a spare laptop; ISIRs can be re-requested |
| SYS-08 Integration server, file server, reporting database | Data sync, business office files, reports | BP-03, BP-04, BP-08, BP-10 | Daily backups to the cloud backup vault (isolation gap) |
| SYS-09 Campus network and internet | Firewall, VPN, Wi-Fi; single internet provider | BP-05, campus staff | Staff can work remotely over home internet |
| SYS-10 Staff endpoints (70) | Laptops and desktops | All | Standard image; 6 spare laptops |
| SYS-07 Email suite (SaaS) | Communications | BP-06, BP-07 | Vendor-operated; separate text alert service |
| People | Registrar, financial aid, business office, faculty, IT staff | All | Cross-training within each office (2 people per critical task) |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-06 Identity provider and break-glass admin access | 1 h | Break-glass accounts (to be created) |
| 2 | SYS-10 Clean staff endpoints for registrar, financial aid, and business office | 4 h | 6 pre-imaged spare laptops |
| 3 | SYS-01 SIS access (vendor-hosted) | 8 h | Printed rosters; paper add/drop log |
| 4 | SYS-02 LMS access (vendor-hosted) | 8 h | Deadline extensions; email course materials |
| 5 | SYS-07 Email suite | 4 h after identity restored | Text alert service and phone tree |
| 6 | SYS-03 FAMS and SYS-04 SAIG workstations | 24 h | Spare laptop with Department software |
| 7 | SYS-08 Integration server and file server | 24 h | Manual data entry between SIS and FAMS |
| 8 | SYS-09 Campus network and internet | 24 h | Remote work; reschedule labs |
| 9 | SYS-05 CRM | 24 h | Paper applications |
| 10 | SYS-08 Reporting database | 72 h | Rebuild from SIS exports |
| 11 | Payroll SaaS | 72 h | Repeat prior payroll |

The `recovery_priority` column in `bia.csv` orders the processes. The table above orders the resources that those processes depend on.
