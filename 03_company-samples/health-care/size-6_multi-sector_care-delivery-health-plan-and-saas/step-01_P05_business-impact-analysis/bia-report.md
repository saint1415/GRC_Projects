# Business Impact Analysis: Cris Santos Company Holdings | Health Care | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-01 to 2026-07-31 | **Approved:** board risk committee, 2026-09-10

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud and network, the Group Data Platform, finance, HR).
- **Division BIAs:** Care Delivery (focus), Health Plan, and Health-Tech SaaS. They are kept as rows in the same workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- each covered entity's contingency plan and applications and data criticality analysis (45 CFR 164.308(a)(7), including (7)(ii)(E));
- the ASC emergency preparedness program (42 CFR 416.54);
- the SaaS availability commitments in its SOC 2 report (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, and SYS-G3 cloud, network, and the Group Data Platform. Division systems are SYS-D1 (Care Delivery EHR, LIS, PACS; vendor-hosted EHR), SYS-D2 (Health Plan claims core in a colocation data center, plus UM and portals in the cloud), SYS-D3 (the SaaS on provider B), and SYS-D4 (the Care Delivery patient-app platform). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Care Delivery about $20 million per day, Health Plan about $26 million per day in premiums, and the SaaS about $3.3 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (care, claims, SaaS) | One region, line, or service stops | Staff slowed but working |
| Regulatory | Reportable breach, missed CMS or state deadline, or SEC disclosure | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Plausible patient or enrollee harm (missed result, delayed surgery, delayed authorization) | Delayed but safe care | None |
| Reputation | National media, loss of SaaS customers, or regulator attention | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 25 processes: 7 group shared services, 8 Care Delivery, 6 Health Plan, and 4 SaaS. 13 are High, 10 Moderate, and 2 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and hub network | Group | High | 4 h | 2 h | 1 h |
| BP-G04 Wide-area network and site connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-CD01 Clinical documentation and care delivery | Care Delivery | High | 8 h | 4 h | 1 h |
| BP-CD02 Ambulatory surgery | Care Delivery | High | 8 h | 4 h | 1 h |
| BP-CD04 Laboratory testing and results | Care Delivery | High | 8 h | 4 h | 1 h |
| BP-CD05 E-prescribing | Care Delivery | High | 8 h | 4 h | 1 h |
| BP-CD03 Diagnostic imaging | Care Delivery | High | 12 h | 6 h | 1 h |
| BP-HP01 Prior authorization and UM | Health Plan | High | 12 h | 4 h | 1 h |
| BP-HT01 Care-coordination service for customers | SaaS | High | 4 h | 2 h | 1 h |
| BP-HP03 Enrollment and eligibility | Health Plan | High | 24 h | 8 h | 4 h |
| BP-HP02 Claims adjudication and payment | Health Plan | High | 72 h | 24 h | 4 h |
| BP-CD06 Patient access and the patient app | Care Delivery | Moderate | 24 h | 8 h | 4 h |
| BP-CD08 White-label patient app for 38 practices | Care Delivery | Moderate | 24 h | 8 h | 4 h |
| BP-HP04 Member services and portals | Health Plan | Moderate | 24 h | 12 h | 4 h |
| BP-HT03 Customer support and incident notices | SaaS | Moderate | 24 h | 8 h | 4 h |
| BP-CD07 Revenue cycle and claims | Care Delivery | Moderate | 72 h | 48 h | 24 h |
| BP-G05 Group Data Platform analytics and reporting | Group | Moderate | 72 h | 24 h | 4 h |
| BP-HP05 Care management | Health Plan | Moderate | 48 h | 24 h | 24 h |
| BP-HT04 SaaS release pipeline | SaaS | Moderate | 72 h | 24 h | 4 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-HT02 Care summary assist (AI feature) | SaaS | Low | 72 h | 24 h | 24 h |
| BP-G06 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-HP06 Broker management and commissions | Health Plan | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Patient safety** drives Care Delivery's 8-hour MTDs. Providers cannot safely treat without allergies, medications, and results, and ASC cases in progress cannot wait.
- **Enrollee access and regulatory decision timeframes** drive prior authorization (BP-HP01). The UM model is not needed to decide: reviewers can work the queue without model scores, which is why its outage alone is not severe.
- **Customer commitments** drive the SaaS (BP-HT01): about 420 customers rely on it for transitions of care, and its SOC 2 report includes the Availability category.
- **Revenue more than time** drives claims (BP-HP02, BP-CD07): payment can be pended or estimated, and payers accept late claims within filing limits.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all three divisions at once. Break-glass accounts per critical system are the fallback |
| WAN and cloud hubs | Group | Care Delivery sites; SaaS; portals | The hosted EHR is only as available as site connectivity |
| SOC facts | Group | Health Plan, Care Delivery, SaaS notices; SEC filing | Every notice clock in P08 depends on the SOC establishing what happened |
| Eligibility (BP-HP03) | Health Plan | Care Delivery front desks | About 210,000 shared patients and members |
| Claims payment (BP-HP02) | Health Plan | Care Delivery revenue (BP-CD07) | Shared members' claims |
| Care Delivery data via the GDP | Care Delivery | Health Plan care management (BP-HP05) | Routine feed; needs a minimum-necessary protocol (P03) |
| Group Data Platform (BP-G05) | Group | Health Plan UM monitoring, Care Delivery quality, SaaS analytics | Not needed for real-time care or claims, so Moderate; a GDP incident is still a breach risk for all three (P08) |
| SaaS incident notices (BP-HT03) | SaaS | External customers (covered entities) | BAA clocks of 72 hours for 42 customers |

**Single points of failure found:** SYS-G1 (mitigated by break-glass accounts, tested quarterly); one clearinghouse for 85% of Care Delivery claims (P01 CD-020); one claims operations center (P01 HP-018, accepted because of remote work).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| SYS-D1 EHR (vendor-hosted) | BP-CD01 to BP-CD05 | Vendor replication (RPO 15 minutes per contract) |
| LIS and PACS | BP-CD03, BP-CD04 | Immutable backups; PACS archive replication |
| SYS-D2 claims core (colocation) | BP-HP02, BP-HP03 | Nightly backups to disk and the provider B vault; restore tested once a year (P01 HP-003) |
| SYS-D3 SaaS | BP-HT01 | Database replicas; warm standby region |
| Group Data Platform | BP-G05, BP-HP05 | DR replica in provider B; daily immutable backups |
| People | All | Cross-trained teams; remote work for 90% of Health Plan claims staff |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones and hub network
3. WAN and site connectivity
4. SOC visibility (SIEM and EDR)
5. to 9. Care Delivery clinical processes (EHR access, ASCs, lab, e-prescribing, imaging)
10. Health Plan prior authorization and UM
11. SaaS care-coordination service (runs in provider B, so it often recovers in parallel)
12. to 25. Eligibility, patient app, white-label practices, claims, member services, SaaS support, revenue cycle, the Group Data Platform, care management, release pipeline, finance, the AI summary feature, HR, and broker management.

## 8. Key findings
1. **RTOs for shared services are shorter than any division's**, as they must be. The group identity RTO of 1 hour has been met in two tests in 2026.
2. **The Health Plan claims core RTO of 24 hours is unproven after ransomware**, because restores are tested once a year (P01 HP-003; POAM-017 covers the documentation gap).
3. **The Group Data Platform is Moderate for availability but High for confidentiality** (P02). Its recovery can wait; its protection cannot.
4. **Notification capacity is itself a process** (BP-HT03, BP-G02, BP-G07). If the SOC or the support desk is down during an incident, notice clocks keep running. The P08 runbook uses out-of-band channels for this reason.
