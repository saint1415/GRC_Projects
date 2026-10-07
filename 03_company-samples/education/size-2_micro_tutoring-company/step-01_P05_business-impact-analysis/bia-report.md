# Business Impact Analysis: Cris Santos Company | Educational Services | Micro

**Organization:** Cris Santos Company, LLC (K-12 tutoring and learning center) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Center Director (Information Security Coordinator) with the Owner, the Director of Tutoring, the Enrollment and Billing Coordinator, and the MSP lead technician, 2026-07-13 to 2026-07-24 | **Approved:** Owner, 2026-08-28

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It supports:
- the safeguards and testing that the COPPA Rule's written information security program must contain (16 CFR 312.8(b)(3)-(4)), including keeping children's personal information available and intact;
- the district contract, which requires sessions to be delivered or made up and data to be protected;
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

No federal rule sets recovery times for a tutoring company. The targets below are business decisions, approved by the Owner.

## 2. System and business description
One Florida learning center, 7 employees, 14 contractor tutors, about 420 students in the last 12 months (about 250 under 13), and about 300 sessions a week. Nearly everything runs in vendor SaaS: the tutoring and learning platform (SYS-01), the scheduling, enrollment, and billing platform (SYS-02), and the productivity suite (SYS-03). On site are 7 laptops, 1 front-desk desktop, and 10 student tablets (SYS-04) and the center network (SYS-05). The MSP runs IT and the suite backup (SYS-06). Contractor tutors teach online from their own computers (SYS-07). See `../00_company-facts.md` sections 1 and 3.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $3,700 per operating day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $11,000 (about 3 operating days) | $3,500 to $11,000 | Less than $3,500 |
| Operations | No sessions can run, in person or online | One function stops; sessions slowed or moved | Staff slowed but working |
| Regulatory | Reportable breach of children's information, or a breach of the district contract's data terms | Missed contract reporting or a late parent request | Internal policy deviation |
| Safety | A child left unsupervised or contacted by an unknown adult | Supervision gap quickly closed | None |
| Reputation | Local news coverage, or the district ends or does not renew the contract | Parent complaints or online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Scheduling, enrollment, and parent communication | High | 24 h | 8 h | 4 h |
| BP-02 In-person tutoring at the learning center | High | 24 h | 8 h | 24 h |
| BP-03 Online tutoring sessions | High | 24 h | 4 h | 24 h |
| BP-04 District after-school program | Moderate | 72 h | 24 h | 24 h |
| BP-05 Assessments and progress reporting | Moderate | 72 h | 48 h | 24 h |
| BP-06 Student intake and records | Moderate | 72 h | 48 h | 24 h |
| BP-07 Billing and payments | Moderate | 120 h | 72 h | 24 h |
| BP-08 Administration, payroll, and contractor management | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- Revenue and family trust drive BP-01 to BP-03. An MTD of 24 hours is one operating day: past that, about 60 sessions must be cancelled and made up, and about $3,700 of billing is delayed.
- BP-03 has the shortest RTO (4 hours) because online families have no in-person fallback for a session that starts the same afternoon.
- The district program (BP-04) tolerates 72 hours because it runs only on Tuesdays and Thursdays. The reputational impact is Severe: losing the contract would remove about 16 percent of revenue.
- Billing (BP-07) tolerates 120 hours because invoices go out once a month and the cash reserve covers about 45 days.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Tutoring and learning platform (SaaS) | Online classroom, lesson materials, practice exercises, session notes, assessments, progress reports, recordings | Vendor backups and replication (vendor SOC 2 report: RTO 8 h, RPO 1 h; see P09). **The company has never exported its own copy** | BP-02, BP-03, BP-04, BP-05 |
| SYS-02 Scheduling, enrollment, and billing platform (SaaS) | Schedule, family accounts, enrollment agreements and consent records, invoices, payments | Vendor's standard terms state daily backups; **no stated RTO or RPO and no SOC 2 report** | BP-01, BP-07 |
| SYS-03 Productivity suite (SaaS) | Email, shared drive ("Student files" folder, district rosters, HR files), calendar, video meetings | Vendor service resilience; email and shared drive copied nightly to SYS-06 | BP-01, BP-03, BP-04, BP-06, BP-08 |
| SYS-06 Suite backup (SaaS, MSP-operated) | Nightly copy of email and the shared drive, 30 days of versions | **Never restore-tested** | BP-06, BP-08 |
| SYS-04 Endpoints | 7 laptops, 1 front-desk desktop, 10 student tablets | No local data by design; the front-desk desktop caches downloaded files | All |
| SYS-05 Center network | Firewall, staff Wi-Fi, student and guest Wi-Fi, one internet line | Firewall configuration backed up by the MSP | BP-01, BP-02 |
| SYS-07 Contractor tutors' computers | Personal computers used for online sessions | Not managed; tutors can switch to another device and sign in | BP-03, BP-04 |
| People | Owner, Center Director, Director of Tutoring, Enrollment and Billing Coordinator, 3 Lead Tutors, 14 contractor tutors | The Center Director covers the front desk; Lead Tutors cover sessions | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Data protection terms | Evidence of recovery capability |
|---|---|---|---|
| Tutoring platform vendor | BP-02 (partly), BP-03, BP-04, BP-05 | Standard terms; data processing addendum available but not signed (P03) | SOC 2 Type 2 report reviewed 2026-08-18 (P09): RTO 8 h does **not** meet the 4-hour RTO for BP-03; RPO 1 h meets every RPO |
| Scheduling and billing platform vendor | BP-01, BP-07 | Standard terms | None beyond "daily backups" in the terms |
| Productivity suite vendor | BP-01, BP-03 (fallback), BP-06, BP-08 | Standard business terms | Vendor service commitments |
| MSP | Recovery of every company device; operates the suite backup | Service contract (no security terms) | 4-business-hour response time; no recovery commitment |
| Backup service (MSP subcontractor) | Restore of email and the shared drive | Through the MSP | None until the first restore test |
| Internet provider | BP-01 and BP-02 at the center; contractor tutors use their own home lines | Not applicable | None; single line |
| School district | BP-04 (sites, rosters) | Data privacy agreement | Not applicable |

**Key findings:**
1. **The tutoring platform's RTO is longer than online sessions can wait.** The vendor's 8-hour RTO exceeds the 4-hour RTO for BP-03. The workaround (a staff-hosted suite video meeting with recording off) covers the gap and must be written into the downtime steps (risk R-011).
2. **The suite backup is unproven.** SYS-06 has never been restore-tested, so the 24-hour RPO for BP-06 and BP-08 is an assumption (R-010).
3. **The scheduling platform is a blind spot.** It runs the highest-priority function and its vendor states no recovery objectives. A weekly schedule export is the minimum protection (R-020).
4. **The MSP contract has no recovery commitment.** Its 4-business-hour response time is not a recovery time. The contract amendment in P01 (R-013) adds one.
5. **Children's data is concentrated in two places.** The platform (SYS-01) is the system of record; the "Student files" folder (SYS-03) holds the most sensitive documents (evaluation reports). Both drive the confidentiality impact in P02 and P01.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Scheduling platform access (SYS-02) from a clean device | 4 h | Weekly printed schedule; front desk phone |
| 2 | Clean staff laptops and front-desk desktop (SYS-04); center network (SYS-05) | 8 h | Staff use clean laptops; phone hotspot if the line is down |
| 3 | Tutoring platform (SYS-01): confirm accounts are clean | 4 h (vendor-hosted) | Suite video meetings for online sessions; printed packets in person |
| 4 | Email and video meetings (SYS-03) | 8 h | Text messages to parents from the suite's mobile app on a clean phone |
| 5 | District program reporting | 24 h | Paper attendance sheets |
| 6 | Shared drive restore (SYS-06 to SYS-03) | 48 h | Ask parents to re-send documents |
| 7 | Billing batch (SYS-02) | 72 h | Re-run on restore |
| 8 | Payroll and HR files | 72 h | Payroll service repeats the prior run |
