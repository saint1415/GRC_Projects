# Business Impact Analysis: Cris Santos Company Holdings | Management of Companies and Enterprises | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's business continuity team with the Insurance and Health Care Services continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
The holding company is the focus of this sample. Its own business is running the shared services that every subsidiary depends on, so its BIA is the group BIA. The analysis works at two levels:
- **Group BIA (focus):** the corporate shared services on the Shared Corporate Services Platform (SCSP) and the common infrastructure: identity, security operations, cloud and network, integration services, treasury, payroll, the financial close, HR, email, board and disclosure, and the group health plan.
- **Division BIAs:** Insurance (two Florida-domiciled property and casualty and workers' compensation insurers) and Health Care Services (340 urgent care and occupational medicine clinics).

All rows are kept in one workbook (`bia.csv`, `division` column) so that cross-division dependencies are visible in one place.

The BIA feeds:
- the group contingency plans for the SCSP and common infrastructure, and each division's contingency plan;
- Health Care Services' HIPAA contingency plan and applications and data criticality analysis (45 CFR 164.308(a)(7)(ii)(E));
- the insurers' information security programs, which must protect against loss of nonpublic information from catastrophes or technological failures (NAIC Model #668 sec. 4D(2)(j), as enacted in Alabama, South Carolina, and Tennessee);
- the availability rating in the SSP (P02), impact ratings in the risk registers (P01), the recovery order in the incident runbook (P08), and the availability commitments assessed in P09.

## 2. System and business description
Three divisions share corporate services. The SCSP is the SSP system (P02): the group identity platform (SYS-G1), ERP and consolidation (SYS-G4), HCM and payroll (SYS-G5), and the treasury and payments hub (SYS-G6), with their integration services in cloud provider A. Common infrastructure is SYS-G2 (SOC) and SYS-G3 (two cloud providers, the WAN, and one colocation data center). Division systems are SYS-I1 to SYS-I4 for Insurance and SYS-H1 to SYS-H3 for Health Care Services. See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Insurance about $39 million per day and Health Care Services about $10.4 million per day. Treasury releases about $65 million in payments per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (claims, clinic care, payments, payroll) | One region, line, or service stops | Staff slowed but working |
| Regulatory | Reportable breach, missed SEC filing, missed state insurance or workers' compensation deadline, wage law violation | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Plausible patient harm (missed result, missed allergy, delayed transfer) | Delayed but safe care or delayed benefit payment | None |
| Reputation | National media, regulator attention, or loss of independent agencies or employer clients | Regional media or complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists **29 processes**: 12 group shared services, 9 Insurance, and 8 Health Care Services. **15 are High, 12 Moderate, and 2 Low.**

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones, WAN, and colocation | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-H01 Patient registration, triage, and clinical documentation | Health Care Services | High | 8 h | 4 h | 1 h |
| BP-H02 Point-of-care lab and on-site X-ray results | Health Care Services | High | 8 h | 4 h | 1 h |
| BP-H03 E-prescribing | Health Care Services | High | 8 h | 4 h | 1 h |
| BP-H04 Clinical documentation at the 50 acquired clinics | Health Care Services | High | 8 h | 4 h | 24 h |
| BP-G12 SCSP integration services and managed file transfer | Group | High | 8 h | 4 h | 1 h |
| BP-G04 Treasury payments and cash management | Group | High | 8 h | 4 h | 1 h |
| BP-G10 Email and collaboration | Group | High | 8 h | 4 h | 1 h |
| BP-I01 First notice of loss and personal lines claims handling | Insurance | High | 12 h | 4 h | 1 h |
| BP-I04 Catastrophe claims surge | Insurance | High | 24 h | 8 h | 4 h |
| BP-I02 Claims payments | Insurance | High | 24 h | 8 h | 1 h |
| BP-I03 Workers' compensation claims, benefit payments, and bill review | Insurance | High | 24 h | 12 h | 4 h |
| BP-G09 Board, disclosure, and investor communications | Group | Moderate | 24 h | 8 h | 4 h |
| BP-H05 Occupational health employer services | Health Care Services | Moderate | 24 h | 8 h | 4 h |
| BP-H06 Online check-in and telehealth | Health Care Services | Moderate | 24 h | 8 h | 4 h |
| BP-I06 Agent and policyholder portals | Insurance | Moderate | 24 h | 12 h | 4 h |
| BP-G05 Payroll | Group | High | 48 h | 24 h | 4 h |
| BP-I05 Policy issuance, endorsements, and billing | Insurance | Moderate | 48 h | 24 h | 4 h |
| BP-G11 HR records, onboarding, and offboarding | Group | Moderate | 72 h | 24 h | 4 h |
| BP-G06 Financial close, consolidation, and SEC reporting | Group | Moderate | 72 h | 48 h | 4 h |
| BP-H08 Work-injury reports to the insurer and employers | Health Care Services | Moderate | 72 h | 24 h | 24 h |
| BP-H07 Revenue cycle and claims | Health Care Services | Moderate | 72 h | 48 h | 24 h |
| BP-I07 Underwriting and rating | Insurance | Moderate | 72 h | 24 h | 24 h |
| BP-G07 Accounts payable and procurement | Group | Moderate | 120 h | 72 h | 24 h |
| BP-G08 Group health plan administration | Group | Moderate | 120 h | 72 h | 24 h |
| BP-I09 Statutory reporting and reinsurance | Insurance | Low | 120 h | 72 h | 24 h |
| BP-I08 Special investigations and fraud scoring | Insurance | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Shared services carry the shortest clocks.** Identity and the network hub (BP-G01, BP-G03) have 4-hour MTDs because every division's processes stop without them. The SCSP integration services (BP-G12) and treasury (BP-G04) have 8-hour MTDs because claims payments and payroll cannot reach the banks without them, and bank cut-off times do not move.
- **Patient safety** drives the Health Care Services 8-hour MTDs. Clinicians cannot safely treat walk-in patients without allergies, medications, and prior results.
- **Claimants and catastrophes** drive Insurance. First notice of loss has a 12-hour MTD that shortens to 8 hours during a declared catastrophe.
- **Calendar windows** change two values. The financial close MTD shortens from 72 to 24 hours during the 10-day quarter-close window. Payroll is High despite a 48-hour MTD because a missed pay date is a wage-law and reputation event for all 45,000 employees.
- **Disclosure capacity is a process** (BP-G09). If the disclosure tool and filing agent are unavailable, the 4-business-day Form 8-K clock still runs.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in and MFA (SYS-G1) | Group | Every process | An identity outage, or a compromise of the identity platform, stops or exposes all three divisions at once. Division help desks also reset MFA through it (P08 scenario) |
| Network hub and colocation (SYS-G3) | Group | Claims, portals, workers' compensation, occupational health portal | The workers' compensation platform (SYS-I4) runs only in the colocation data center |
| Integration services and treasury (BP-G12, BP-G04) | Group | Insurance claims payments (BP-I02, BP-I03); payroll (BP-G05) | One integration layer carries every division's payment files |
| HR onboarding (BP-G11) | Group | Catastrophe surge (BP-I04) | 1,500 adjuster accounts in 72 hours after a hurricane |
| SOC facts (BP-G02) | Group | Every notice in P08; the disclosure committee | Every notice clock depends on the SOC establishing what happened |
| Work-injury reports (BP-H08) | Health Care Services | Workers' compensation claims (BP-I03) | About 18% of the insurer's injured-worker claims in 4 states are treated in the group's clinics. Adjusters also have direct EHR read access (gap 6) |
| Claims to the group health plan (BP-H07) | Health Care Services | Group health plan (BP-G08) | About 9,000 covered lives a year are clinic patients |
| General ledger feeds (BP-G12) | Insurance and Health Care Services | Financial close (BP-G06) | ICFR depends on complete and accurate feeds from every entity |

**Single points of failure found:**
- **SYS-G1.** Mitigated by sealed break-glass accounts per critical system, tested quarterly.
- **The integration services.** The warm standby in provider B took 6 hours to fail over in the 2026-02 test, against a 4-hour RTO (P01 GR-09).
- **The colocation data center for SYS-I4.** There is no second site; recovery is from the provider B vault onto rebuilt servers, estimated at 36 hours, beyond the 12-hour RTO (P01 INS-007).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) and directory servers | All | Vendor multi-region service; configuration exported daily; directory servers replicated between colocation and provider A |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| SCSP integration services and file transfer | BP-G12, BP-G04, BP-G05, BP-I02 | Message queues replicated to provider B; warm standby |
| SYS-G4 ERP, SYS-G5 HCM, SYS-G6 treasury (SaaS) | BP-G04 to BP-G07, BP-G11 | Vendor replication (contract RPO 1 hour for each); nightly group export to the provider B vault |
| SYS-I2 claims (provider A) | BP-I01, BP-I02, BP-I08 | Database replicas; warm standby in provider B |
| SYS-I4 workers' compensation (colocation) | BP-I03 | Nightly backups to disk and the provider B vault; restore tested once a year |
| SYS-H1 EHR (vendor-hosted) | BP-H01 to BP-H03 | Vendor replication (contract RPO 15 minutes) |
| Legacy EHR at 50 clinics | BP-H04 | Nightly backup by the hosting provider only (RPO 24 hours) |
| People | All | Cross-trained treasury and payroll staff; remote work for claims staff; pre-staged surge adjuster accounts |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones, WAN, and colocation
3. SOC visibility (SIEM and EDR)
4. to 7. Clinical processes at all 340 clinics (EHR, results, e-prescribing, acquired clinics)
8. to 10. Integration services, treasury payments, and email
11. to 14. Insurance claims handling, catastrophe surge, claims payments, and workers' compensation
15. to 29. Disclosure, occupational health portal, telehealth, agent and policyholder portals, payroll, policy and billing, HR records, financial close, work-injury reports, revenue cycle, underwriting, payables, health plan administration, statutory reporting, and fraud scoring.

## 8. Key findings
1. **The holding company's shared services set the floor for every division.** No division can recover faster than SYS-G1 and the network hub. Their 1-hour and 2-hour RTOs were met in the two 2026 failover tests.
2. **The integration services RTO is not yet achievable.** The 2026-02 test took 6 hours against a 4-hour RTO, and claims payments and payroll both depend on it (P01 GR-09; P07 CP-4 finding).
3. **The acquired clinics' 24-hour RPO is far from the division's 1-hour target** (BP-H04). Migration to SYS-H1 by 2027-03-31 closes it (P01 HCS-004).
4. **The workers' compensation platform has no second site.** The estimated 36-hour rebuild exceeds its 12-hour RTO (P01 INS-007).
5. **Catastrophe surge is a security process as well as a business one.** The fastest way to meet the 72-hour onboarding target is weak identity proofing, which P01 rates as a risk (INS-005).
6. **Notification capacity is itself a process** (BP-G02, BP-G09, BP-G10). The P08 runbook uses out-of-band channels because the SOC, email, and the disclosure tool may be affected by the same incident.
