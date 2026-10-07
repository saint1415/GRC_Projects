# Business Impact Analysis: Cris Santos Company Holdings | Educational Services | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud and network, the group data platform, finance, HR).
- **Division BIAs:** Higher Education (focus), Education Software, and Student Health. They are kept as rows in one workbook (`bia.csv`, `division` column) so that cross-division dependencies are visible in one place.

It supports:
- the college's information security program under the FTC Safeguards Rule (16 CFR 314.4(b) and (h)), which needs to know which systems hold customer information and how fast they must recover;
- Student Health's contingency plan and applications and data criticality analysis as a HIPAA covered entity (45 CFR 164.308(a)(7)(ii)(E));
- the Education Software availability commitments in its SOC 2 report (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, and SYS-G3 cloud, network, and the group data platform. The college's student information system (SIS) and learning management system (LMS) run as a tenant on Education Software's Campus Platform (SYS-H1 on SYS-E1). This is the most important cross-division dependency in the group: **the college cannot teach online, register students, or disburse aid when the Campus Platform is down.** Other division systems are the financial aid management system and SAIG access (SYS-H2), the admissions CRM (SYS-H3), campus networks and legacy campus systems (SYS-H4), online proctoring (SYS-H5), the District Platform (SYS-E2), the support console and pipeline (SYS-E3), and the clinic EHR (SYS-S1) with Student Health's legacy domain (SYS-S2). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Higher Education about $26 million per day, Education Software about $16 million per day, and Student Health about $7 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (instruction, the platforms, clinical care) | One campus, product line, or clinic region stops | Staff slowed but working |
| Regulatory | Missed Title IV deadline, reportable breach, SEC disclosure, or customer contract breach at scale | Missed internal or single-contract deadline | Internal policy deviation |
| Safety | Plausible physical or health harm (campus emergency, missed result, student in crisis) | Delayed but safe service | None |
| Reputation | National media, loss of software customers, accreditor or regulator attention | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 28 processes: 7 group shared services, 10 Higher Education, 6 Education Software, and 5 Student Health. 14 are High, 10 Moderate, and 4 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-HE05 Campus safety and emergency notification | Higher Education | High | 2 h | 1 h | 24 h |
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and hub network | Group | High | 4 h | 2 h | 1 h |
| BP-G04 Campus and clinic network connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-ES01 Campus Platform service for college customers | Education Software | High | 4 h | 2 h | 1 h |
| BP-ES02 District Platform service for K-12 customers | Education Software | High | 4 h | 2 h | 1 h |
| BP-SH02 Counseling and crisis services | Student Health | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-HE01 Online instruction and course delivery | Higher Education | High | 8 h | 4 h | 1 h |
| BP-SH01 Clinical care at 96 clinic sites | Student Health | High | 8 h | 4 h | 1 h |
| BP-SH03 E-prescribing and laboratory results | Student Health | High | 8 h | 4 h | 1 h |
| BP-HE02 Registration, enrollment, and academic records | Higher Education | High | 24 h | 8 h | 1 h |
| BP-HE03 Student accounts, Title IV disbursement, and refunds | Higher Education | High | 72 h | 24 h | 1 h |
| BP-HE04 Financial aid processing and SAIG transmissions | Higher Education | High | 72 h | 24 h | 4 h |
| BP-ES03 Customer support and incident notices | Education Software | Moderate | 24 h | 8 h | 4 h |
| BP-HE06 Online proctoring and identity verification | Higher Education | Moderate | 24 h | 12 h | 4 h |
| BP-HE07 On-campus instruction, labs, and campus IT | Higher Education | Moderate | 24 h | 8 h | 24 h |
| BP-ES05 Data integrations and state reporting exports | Education Software | Moderate | 48 h | 24 h | 4 h |
| BP-HE08 Admissions and new student onboarding | Higher Education | Moderate | 72 h | 24 h | 24 h |
| BP-G05 Group data platform and student data warehouse | Group | Moderate | 72 h | 24 h | 4 h |
| BP-SH04 Billing and claims | Student Health | Moderate | 72 h | 48 h | 24 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-ES04 Release pipeline | Education Software | Moderate | 72 h | 24 h | 4 h |
| BP-G06 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-ES06 AI tutoring assistant (pilot) | Education Software | Low | 72 h | 24 h | 24 h |
| BP-SH05 Immunization compliance and enrollment checks | Student Health | Low | 120 h | 72 h | 24 h |
| BP-HE09 Student-success advising and early alerts | Higher Education | Low | 120 h | 72 h | 24 h |
| BP-HE10 Transcripts and enrollment verification requests | Higher Education | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Safety** drives the shortest times: campus emergency notification (BP-HE05) must work within the hour because the college must immediately notify the campus community on confirmation of a significant emergency (34 CFR 668.46(g)), and students in crisis need same-day counseling access (BP-SH02).
- **Online students have no classroom fallback.** About 295,000 students learn only through the LMS, so online instruction (BP-HE01) has an 8-hour MTD, and the Campus Platform that hosts it (BP-ES01) must recover in 2 hours.
- **Title IV timing, not hours, drives aid and refunds.** Credit balances must be paid within 14 days (34 CFR 668.164(h)(2)), so BP-HE03 and BP-HE04 tolerate 72 hours. Their **RPO is short** (1 hour for the ledger) because lost or altered disbursement and bank detail records are a payment integrity and fraud risk.
- **Customer commitments** drive both platforms (BP-ES01, BP-ES02): about 900 colleges and 5,400 districts rely on them, and the SOC 2 report includes the Availability category.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Campus Platform (BP-ES01) | Education Software | College instruction, registration, student accounts (BP-HE01 to BP-HE03) | The college is a customer of its sister division. A platform outage is a college outage, and a platform breach is a college breach (P08) |
| Sign-in (SYS-G1) | Group | Every federated process | A group identity outage stops all three divisions at once. Break-glass accounts per critical system are the fallback |
| Campus and clinic network (BP-G04) | Group | Campus safety, on-campus instruction, 96 clinics | Campus clinics share campus networks |
| SOC facts (BP-G02) | Group | FSA, FTC, HIPAA, customer, and SEC notices | Every notice clock in P08 depends on the SOC establishing what happened |
| Support console (BP-ES03, SYS-E3) | Education Software | The college tenant and about 6,300 other customer tenants | Standing cross-tenant read access (scenario gap 1) makes one support account a group-wide exposure |
| Enrollment and immunization feeds (BP-SH05) | Higher Education and Student Health | Each other | Two-way feed through the integration hub; the 2025 utilization extract to the warehouse used the same interface (scenario gap 2) |
| Student data warehouse (BP-G05) | Group | College advising, institutional research | Not needed in real time (Moderate), but it holds the largest copy of college data outside SYS-E1 |

**Single points of failure found:** SYS-G1 (mitigated by break-glass accounts, tested quarterly); the Campus Platform's single production region in provider B for the college tenant (warm standby exists for the platform, but the college's integration hub has no standby, P01 HE-014); one central financial aid office for SAIG transmissions (accepted, because SAIG access can be rebuilt on clean workstations within the 24-hour RTO).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All federated processes | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| SYS-E1 and SYS-E2 platforms | BP-ES01, BP-ES02, BP-HE01 to BP-HE03 | Database replicas; warm standby region; point-in-time recovery (RPO 15 minutes) |
| SYS-H2 FAMS (vendor SaaS) and SAIG workstations | BP-HE04 | Vendor replication; 4 pre-imaged spare SAIG workstations |
| SYS-S1 clinic EHR (vendor-hosted) | BP-SH01 to BP-SH05 | Vendor replication (RPO 15 minutes per contract) |
| SYS-S2 clinic file servers | Clinic forms and scanned intake documents | Nightly backups to the group vault since 2026-03; not yet restore-tested |
| Student data warehouse and integration hub | BP-G05, BP-HE09 | Disaster recovery replica in provider B; daily immutable backups |
| People | All | Cross-trained teams; remote work for financial aid, admissions, and support staff |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones and hub network
3. Campus and clinic network connectivity
4. SOC visibility (SIEM and EDR)
5. Campus safety and emergency notification
6. and 7. Campus Platform and District Platform (the college's instruction and records depend on 6)
8. to 10. Student Health counseling, clinical care, and e-prescribing
11. and 12. College online instruction, then registration and academic records
13. Education Software customer support and incident notices (needed to meet contract notice clocks)
14. to 28. Student accounts and refunds, financial aid and SAIG, proctoring, campus IT, integrations, admissions, the data platform, clinic billing, financial close, the release pipeline, immunization feeds, the AI tutor, advising, transcripts, and payroll.

## 8. Key findings
1. **The college's most critical systems are run by another division.** The college has no recovery capability of its own for its SIS and LMS. It relies on Education Software's warm standby, which is tested twice a year for the platform but has never been tested end to end with the college's integration hub and FAMS interfaces (P01 HE-014; P07 CP-4).
2. **Shared-service RTOs are shorter than any division's**, as they must be. Group identity met its 1-hour RTO in two 2026 tests.
3. **Student Health is the least recoverable division.** Its legacy file servers (SYS-S2) have been backed up to the group vault only since March 2026 and have never been restore-tested (P01 SH-004).
4. **The data warehouse is Moderate for availability but High for confidentiality.** Its recovery can wait; its protection cannot (P02, scenario gap 2).
5. **Notification capacity is itself a process** (BP-ES03, BP-G02, BP-G07). If the SOC or the support desk is down during an incident, the FSA, FTC, customer, and SEC clocks keep running. The P08 runbook uses out-of-band channels for this reason.
