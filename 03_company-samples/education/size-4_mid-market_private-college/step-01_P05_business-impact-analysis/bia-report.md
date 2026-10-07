# Business Impact Analysis: Cris Santos Company | Educational Services | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed private, for-profit college) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Information Security Manager with the vCISO (Qualified Individual), the process owners named in `bia.csv`, and the Campus Directors | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Information Officer, 2026-09-17 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: the 3 campuses, the online division, student financial services (financial aid and student accounts), enrollment management, academic affairs, student affairs (including campus safety and counseling), corporate partnerships, and enterprise support (IT, HR, finance). It rates 16 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and student safety and welfare.

The results feed:
- the recovery part of the written incident response plan required by 16 CFR 314.4(h)(2), and the IT disaster recovery plan due 2026-12-31 (gap 5);
- the Clery Act emergency notification procedures (34 CFR 668.46(g), section 7 below);
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability criteria in the SOC 2 readiness assessment for the employer education services (P09).

## 2. System and business description
The college serves about 7,800 students (4,300 at 3 Florida campuses and 3,500 fully online, living in 41 states) with 600 employees. Student business runs on the Student Information and Learning Platform (SILP) described in the SSP (P02): the SaaS SIS and LMS, the SaaS financial aid management system (FAMS), SAIG access to the Department of Education, the identity provider, the 4-account cloud landing zone (integration platform, data warehouse, employer partner portal, file services, backups), and the MSSP-operated SIEM. Campus safety systems (door access control, CCTV, and a SaaS emergency notification service) sit outside the SILP but depend on the same identity provider and campus networks. About 90 vendors handle student data (see `../00_company-facts.md` sections 3, 4, and 7).

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual receipts over about 250 business days, or about $400,000 a day: online division about $152,000, Campus 1 about $120,000, Campus 2 about $76,000, and Campus 3 about $52,000. Title IV draws run about $1.2 million per business day during term-start peaks.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $100,000 in unrecovered receipts or extra cost, or more than $1 million of Title IV cash delayed | $20,000 to $100,000 | Less than $20,000 |
| Operations | A whole modality (all online students or all 3 campuses) or a whole office (financial aid, student accounts) stops | One campus, program, or office function stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory | Title IV deadline missed, Clery emergency procedure fails, reportable breach, or an administrative capability finding | Missed accreditor, employer contract, or internal documentation deadline | Internal policy deviation |
| Student safety and welfare | Students or staff physically at risk, or students left without living funds | Students inconvenienced or delayed in a way that is later made whole | None |
| Reputation | Regional media coverage, accreditor inquiry, loss of an employer partner, or a visible drop in starts | Student complaints or online reviews | Internal only |

**How loss at MTD was estimated.** Estimated loss is receipts that are not recovered plus extra labor and remediation cost, over the MTD. The process owners supplied the assumptions: about 2% of new online starts are lost if admissions stops for 3 days near a start date; exam rescheduling and term extensions cost about $150 per affected online student; refund and aid delays mostly delay cash rather than lose it. For BP-04 the delayed Title IV cash is shown separately, because it is recovered once disbursement resumes.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-07 Campus emergency notification and physical security | Campus safety | High | 1 | 0.5 | 24 | $0 (safety and regulatory driven) |
| 2 | BP-02 Online instruction and proctored exams | Online division | High | 12 | 6 | 1 | $60,000 |
| 3 | BP-01 Registration, enrollment, and academic records | Academic affairs | High | 24 | 8 | 1 | $45,000 |
| 4 | BP-09 Student identity and IT support | Enterprise (IT) | Moderate | 24 | 8 | 24 | $15,000 |
| 5 | BP-11 Counseling and wellness services | Student affairs | Moderate | 24 | 8 | 24 | $2,000 |
| 6 | BP-08 Student and staff communications | Enterprise | Moderate | 24 | 8 | 24 | $10,000 |
| 7 | BP-03 On-campus instruction, labs, and clinical rotations | Campuses 1-3 | Moderate | 48 | 24 | 24 | $25,000 |
| 8 | BP-04 Title IV aid processing and disbursement | Student financial services | High | 72 | 24 | 4 | $40,000 (plus about $3.6 million of Title IV cash delayed) |
| 9 | BP-05 Student accounts and Title IV credit balance refunds | Student financial services | High | 72 | 48 | 4 | $20,000 |
| 10 | BP-06 Admissions and new-student onboarding | Enrollment management | Moderate | 72 | 24 | 24 | $90,000 |
| 11 | BP-12 Employer partner services | Corporate partnerships | Moderate | 72 | 24 | 24 | $30,000 |
| 12 | BP-13 Payroll and HR | Enterprise (HR and finance) | Moderate | 72 | 48 | 24 | $15,000 |
| 13 | BP-14 Finance, procurement, and accounts payable | Enterprise (HR and finance) | Low | 120 | 72 | 24 | $5,000 |
| 14 | BP-16 Library and learning resources | Academic affairs | Low | 120 | 72 | 24 | $5,000 |
| 15 | BP-10 Student success advising and early alert | Student affairs | Low | 168 | 72 | 24 | $10,000 |
| 16 | BP-15 Institutional reporting and compliance | Academic affairs | Low | 168 | 120 | 24 | $5,000 |

**Summary:** 5 High, 7 Moderate, and 4 Low processes (16 in total). The sum of estimated losses at each process's MTD is $377,000.

**Enterprise-wide scenario.** If the whole SILP were down for 72 hours at the start of an online term (for example, ransomware), the unrecovered cost would be about $380,000: about $180,000 for exam rescheduling, term extensions, and online withdrawals, about $120,000 in lost new starts, about $50,000 of campus disruption, and about $30,000 of overtime. About $3.6 million of Title IV cash would also be delayed. Incident response and breach notification costs come on top (see P01 R-001 and R-002).

**What drives the values:**
- **Safety and a federal "immediately" standard** drive BP-07. Clery requires procedures to immediately notify the campus community once a significant emergency is confirmed (34 CFR 668.46(g)(1)), so the MTD is 1 hour and the RTO 30 minutes.
- **Online students have no fallback classroom.** An LMS outage stops all 3,500 online students at once, and timed exams in 8-week terms leave little slack (BP-02).
- **Enrollment status drives money.** Enrollment and attendance records in the SIS and LMS determine Title IV eligibility and disbursement, which is why BP-01 has an 8-hour RTO even though aid itself (BP-04) can wait up to 3 days.
- **Credit balance refunds have a legal clock.** A Title IV credit balance must be paid no later than 14 days after it occurs (34 CFR 668.164(h)(2)). The 72-hour MTD for BP-05 leaves time to catch up within that deadline, except during the first 3 weeks of a term (finding 4).

## 5. Key findings
1. **SIS vendor recovery objectives do not meet the BIA.** The SIS vendor's SOC 2 system description states RTO 24 hours and RPO 4 hours. BP-01 needs RTO 8 hours and RPO 1 hour. Printed rosters keep classes running, but lost grade, attendance, and add/drop entries must be re-keyed. Action: negotiate recovery terms at the 2027 renewal and add a nightly read-only roster and enrollment extract to the file service (P01 R-013; P09 vendor review).
2. **College-managed recovery is unproven.** The integration platform (BP-01, BP-04, BP-05, BP-06), data warehouse (BP-10, BP-15), and employer partner portal (BP-12) have never been restore-tested, and there is no IT disaster recovery plan (gap 5). Their RTOs of 8 to 120 hours are targets, not demonstrated capabilities (P01 R-014 to R-016; P07 CP-4).
3. **Emergency notification has a single point of failure.** The emergency notification console is reached only through SSO, with no break-glass account, so an identity provider outage or ransomware that forces a password reset could delay a Clery emergency notification beyond the 30-minute RTO (gap 7; section 7).
4. **The refund clock is tight at term start.** About 1,800 refunds can fall due in a term-start week. A 72-hour outage then pushes some refunds close to the 14-day deadline. A documented paper-check procedure from the last reconciled refund file is needed (P01 R-018).
5. **Campus 3 is fragile.** Its flat network carries staff, lab, and campus safety devices, so malware in a lab could also take door controllers and cameras offline (gap 7; P01 R-003).
6. **The LMS vendor just meets BP-02.** Its RTO of 6 hours equals the BIA RTO, with no margin during exam weeks. The proctoring vendor (AI-005) has no stated recovery objectives.

## 6. Resource requirements
| Resource | Description | Supports | Backup or replication method |
|---|---|---|---|
| SYS-06 Identity provider (SaaS) | SSO and MFA for staff, faculty, and students | All | Vendor-operated; break-glass accounts for critical systems (gap for emergency notification) |
| SYS-01 SIS (SaaS) | Records, student accounts, refunds, student portal | BP-01, BP-04, BP-05, BP-10, BP-12, BP-15 | Vendor backups; stated RTO 24 h, RPO 4 h |
| SYS-02 LMS (SaaS) with proctoring and AI tutor integrations | Online and campus course delivery and exams | BP-02, BP-03, BP-16 | Vendor backups; stated RTO 6 h, RPO 1 h |
| SYS-03 FAMS (SaaS) | Aid processing and the student aid portal | BP-04 | Vendor backups (no stated objectives) |
| SYS-04 SAIG workstations (3) | ISIR downloads and data exchange with the Department | BP-04 | Reinstall Department software on a spare workstation; re-request ISIRs |
| SYS-08 Workloads account: integration platform | 37 scheduled interfaces (SIS, FAMS, LMS, CRM, ERP, bank, emergency notification contact sync) | BP-01, BP-04, BP-05, BP-06, BP-07 | Daily backup to the backup account; never restore-tested |
| SYS-08 Workloads account: data warehouse and AI-002 model | Reporting, early alert, institutional research | BP-10, BP-15 | Daily backup; rebuild from SIS extracts |
| SYS-08 Workloads account: employer partner portal | Partner reporting and invoices | BP-12 | Daily backup; never restore-tested |
| SYS-08 Backup account | Write-once backups, 30-day retention, second region | Recovery of all SYS-08 workloads | Separate credentials |
| SYS-10 Campus networks and SD-WAN | 3 campuses; dual internet at Campus 1, single at Campuses 2 and 3 | BP-03, BP-07, campus staff | Cellular failover at Campus 1 only |
| SYS-11 Staff endpoints (780) | Laptops and desktops | All | Standard image; 20 pre-imaged spares at Campus 1 |
| SYS-13 Campus safety systems | Emergency notification (SaaS), door controllers, CCTV | BP-07 | Vendor-hosted notification; doors fail locked with key override |
| SYS-14 SIEM (MSSP) | Detection and investigation | Recovery validation | MSSP platform |
| Third parties | SIS, LMS, FAMS, CRM, identity, email, ERP, emergency notification, proctoring, payment plan, and counseling records vendors; the third-party servicer; the bank; the Department of Education | As listed in `bia.csv` | Vendor SOC 2 reviews (P09) |
| People and facilities | Registrar, financial aid, student accounts, admissions, online learning, campus safety, IT and security team, MSSP | All | Cross-training: at least 2 trained people per critical task |

## 7. Clery Act emergency notification linkage (34 CFR 668.46(g))
The college publishes an annual security report, so its emergency response and evacuation procedures must meet 34 CFR 668.46(g) (text verified on eCFR, 2026-09-23 version). Those procedures now depend on SaaS and the identity provider. The BIA supplies the cyber content they lack:

| 668.46(g) requirement (verified text, summarized) | What this BIA supplies | Status |
|---|---|---|
| (g)(1) Procedures to immediately notify the campus community upon confirmation of a significant emergency or dangerous situation | BP-07 MTD 1 hour, RTO 30 minutes; manual alternates (public address, radio, officers) | Written here; procedures updated by 2026-12-15 |
| (g)(2)(iv) Process to initiate the notification system | Break-glass account for the notification console and a vendor-hosted secondary sign-in that does not depend on SSO | Gap (finding 3); due 2026-11-30 |
| (g)(2)(ii) Determine which segments of the campus community receive a notification | Contact lists synced nightly from the SIS by the integration platform (RPO 24 h); a weekly export kept by Campus Safety | Export procedure due 2026-11-30 |
| (g)(4) Titles of those responsible for confirming, deciding content, and initiating | Director of Campus Safety, with each Campus Director as alternate; IT on call for console access | To be added to the procedures |
| (g)(6) Test emergency response and evacuation procedures at least annually and document each test | The 2027 annual test will include an identity provider outage injection (sign-in through the break-glass path) | Planned for 2027-02 |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-13 emergency notification console access (break-glass) | 30 min | Public address, radio, officers in person |
| 2 | SYS-06 identity provider and break-glass administrator access | 1 h | Two break-glass accounts per critical system, stored sealed and offline |
| 3 | SYS-11 clean endpoints for the registrar, financial aid, student accounts, and the service desk | 4 h | 20 pre-imaged spare laptops |
| 4 | SYS-02 LMS access (vendor-hosted) and the proctoring integration | 6 h | Deadline extensions; email course materials; reschedule exams |
| 5 | SYS-01 SIS access (vendor-hosted) | 8 h | Printed rosters; nightly read-only extract (to be added) |
| 6 | SYS-07 email suite | 8 h | Emergency notification text messages; website banner |
| 7 | SaaS counseling records application | 8 h | Crisis line; paper intake |
| 8 | SYS-08 integration platform | 24 h | Manual file transfers between SIS, FAMS, and the bank |
| 9 | SYS-03 FAMS and SYS-04 SAIG workstations | 24 h | Spare workstation with the Department software |
| 10 | SYS-10 campus networks (Campus 3 last, after segmentation checks) | 24 h | Remote work; reschedule labs |
| 11 | SYS-05 CRM | 24 h | Phone and paper applications |
| 12 | SYS-08 employer partner portal | 24 h | Encrypted file reports to partners |
| 13 | SYS-09 ERP (payroll) | 48 h | Repeat the prior payroll |
| 14 | SYS-08 data warehouse and AI-002 model | 120 h | SIS standard reports |

The `recovery_priority` column in `bia.csv` orders the processes. The table above orders the resources those processes depend on.
