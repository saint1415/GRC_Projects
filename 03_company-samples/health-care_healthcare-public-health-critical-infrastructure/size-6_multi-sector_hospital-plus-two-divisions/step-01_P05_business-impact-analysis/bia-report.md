# Business Impact Analysis: Cris Santos Company Holdings | Healthcare and Public Health | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the Hospital System, Health Plan, and College continuity leads and the system emergency management director | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15
**Sources:** process owner interviews by division, 2026-05-04 to 2026-06-05 (EV-088 group, EV-089 Hospital System, EV-090 Health Plan, EV-091 College), FY2025 revenue by division (EV-003), hospital, patient, member and student volumes (EV-037, EV-038, EV-065, EV-075), backup, failover and recovery records (EV-021, EV-046, EV-047, EV-067), and downtime records (EV-048). The `source_evidence` column in `bia.csv` names the source of each process's values. Downtime limits are the owners' statements, reviewed and approved by the board risk committee.

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on: identity (SYS-G1), the SOC (SYS-G2), the two data centers, network, voice, file service, cloud platform, and backup vault (SYS-G3), and ERP, HR, and payroll (SYS-G4).
- **Division BIAs:** the Hospital System (focus), the Health Plan, and the College. They are rows in the same workbook (`bia.csv`, `division` column) so dependencies between divisions are visible in one place.

It feeds:
- each covered entity's contingency plan and applications and data criticality analysis (45 CFR 164.308(a)(7), including (7)(ii)(E));
- the hospitals' unified and integrated emergency preparedness program (42 CFR 482.15(a) and (f)), which must address continuity of operations and the services each hospital can provide in an emergency (482.15(a)(3));
- the College's GLBA Safeguards Rule incident response plan, which must cover recovery from security events (16 CFR 314.4(h));
- the impact ratings in the risk registers (P01), the availability rating of the HCIS in the SSP (P02), and the recovery order and diversion criteria in the incident runbook (P08).

## 2. System and business description
Corporate runs SYS-G1 to SYS-G4. The Hospital System's clinical systems (SYS-H1 enterprise EHR and SYS-H2 ancillary systems) run in group data center DC1 with a replica in DC2; its medical devices and clinical OT (SYS-H3) are on hospital device networks. The Health Plan's claims core is in DC1 and its UM platform and portals run at cloud provider A (SYS-P1). The College runs SaaS academic systems (SYS-E1) and its own campus IT and directory (SYS-E2); since 2025 its administrative file shares sit on the group file service in DC1. See the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv).

## 3. Impact categories and values
Dollar values use FY2025 revenue by division (EV-003) spread over 365 days: the Hospital System about $10.5 billion, or about $28.8 million a day; the Health Plan about $7.1 billion in premiums and fees, or about $19.5 million a day; and the College about $0.4 billion, or about $1.1 million a day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (hospital care, claims and authorizations, instruction), or a hospital must divert ambulances | One hospital, region, or service line stops | Staff slowed but working |
| Regulatory | Reportable breach, EMTALA exposure, a missed CMS, state, or Federal Student Aid deadline, or an SEC disclosure | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Plausible patient or member harm (delayed treatment, medication error, missed critical result, delayed authorization) | Delayed but safe care | None |
| Reputation | National media, regulator attention, or loss of community-connect practices or employer clients | Regional media or complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 34 processes: 8 group shared services, 15 Hospital System, 6 Health Plan, and 5 College. 18 are High, 14 Moderate, and 2 Low. The table lists them in recovery order.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G04 Wide-area network, site connectivity, and voice | Group | High | 4 h | 2 h | 1 h |
| BP-G03 Data center compute, storage, and virtualization | Group | High | 4 h | 2 h | 15 min |
| BP-G05 Backup vault and recovery services | Group | High | 8 h | 4 h | 24 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-H09 Clinical communications | Hospital System | High | 2 h | 1 h | 1 h |
| BP-H08 Patient transfers, bed management, and EMS communications | Hospital System | High | 2 h | 1 h | 1 h |
| BP-H01 Emergency department care | Hospital System | High | 4 h | 2 h | 15 min |
| BP-H02 Inpatient care and medication administration | Hospital System | High | 4 h | 2 h | 15 min |
| BP-H06 Pharmacy order verification and dispensing | Hospital System | High | 4 h | 2 h | 15 min |
| BP-H04 Laboratory testing and blood bank | Hospital System | High | 4 h | 2 h | 15 min |
| BP-H07 Medical device operation and clinical networks | Hospital System | High | 4 h | 2 h | 24 h |
| BP-H03 Surgical services | Hospital System | High | 8 h | 4 h | 15 min |
| BP-H05 Diagnostic imaging | Hospital System | High | 8 h | 4 h | 1 h |
| BP-P01 Prior authorization and utilization management | Health Plan | High | 12 h | 4 h | 1 h |
| BP-H13 Community-connect EHR for 64 practices | Hospital System | High | 24 h | 8 h | 15 min |
| BP-P03 Enrollment and eligibility | Health Plan | High | 24 h | 8 h | 4 h |
| BP-H10 Patient access and registration | Hospital System | Moderate | 24 h | 8 h | 1 h |
| BP-G06 Group file, email, and collaboration services | Group | Moderate | 24 h | 8 h | 4 h |
| BP-H12 Patient portal and telehealth | Hospital System | Moderate | 24 h | 12 h | 4 h |
| BP-P04 Member services and portals | Health Plan | Moderate | 24 h | 12 h | 4 h |
| BP-E02 Instruction and learning management | College | Moderate | 24 h | 8 h | 24 h |
| BP-E03 Clinical placement and compliance clearance | College | Moderate | 48 h | 24 h | 24 h |
| BP-P02 Claims adjudication and payment | Health Plan | High | 72 h | 24 h | 4 h |
| BP-P05 ASO claims administration for 40 self-funded employers | Health Plan | Moderate | 72 h | 24 h | 4 h |
| BP-P06 Care management | Health Plan | Moderate | 48 h | 24 h | 24 h |
| BP-H11 Revenue cycle and claims | Hospital System | Moderate | 72 h | 48 h | 24 h |
| BP-H14 Public health and quality reporting | Hospital System | Moderate | 72 h | 24 h | 4 h |
| BP-E01 Financial aid processing and Title IV disbursement | College | Moderate | 72 h | 24 h | 24 h |
| BP-E04 Registrar and student records | College | Moderate | 72 h | 24 h | 24 h |
| BP-G08 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-H15 Sepsis prediction alerting | Hospital System | Low | 72 h | 24 h | 24 h |
| BP-G07 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-E05 Admissions and enrollment | College | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Patient safety and EMTALA** drive the Hospital System's 2-hour and 4-hour MTDs. Clinicians cannot safely treat without allergies, medications, and results for long, and a hospital that cannot accept more emergency patients must decide on diversion (BP-H08). Paper downtime procedures buy hours, not days.
- **Data center recovery is the bottleneck.** The clinical RTOs assume failover to DC2. In a ransomware case where both data centers are affected (group gap 1), recovery comes from the immutable vault (BP-G05), and the estimated EHR rebuild time of 5 to 7 days is far beyond every clinical MTD.
- **Member access and decision timeframes** drive prior authorization (BP-P01). Claims (BP-P02) can wait longer because payment can be pended within prompt-pay limits.
- **The College's processes are Moderate or Low.** Instruction and financial aid can be delayed by days with notice to students. The College matters to this BIA mostly for its **data** (student financial information on the group file service) and for the student rosters that feed hospital accounts.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Hospital System, Health Plan, corporate | A group identity outage stops the hospitals and the Health Plan at once. Break-glass accounts per critical system are the fallback; the College is not yet on SYS-G1 |
| DC1 and DC2 (SYS-G3) | Group | EHR, ancillary systems, claims core, College file shares | One compromise of the shared data centers reaches all three divisions (group gap 1) |
| WAN and voice | Group | All hospitals; EMS and transfer calls | The EHR is only as available as hospital connectivity; EMS coordination depends on voice and radio |
| SOC facts | Group | Every notice in P08 | Breach, Safeguards Rule, insurance, and SEC clocks depend on the SOC establishing what happened |
| Eligibility (BP-P03) | Health Plan | Hospital patient access | About 140,000 shared patients and members |
| Claims payment (BP-P02) | Health Plan | Hospital revenue cycle (BP-H11) | Shared members' claims |
| Admission notices | Hospital System | Health Plan care management (BP-P06) | Routine feed between two covered entities; minimum-necessary protocol not written (group gap 7) |
| Student rosters (BP-E03) | College | Hospital student EHR accounts | About 3,100 College students a year; rosters arrive by email (group gap 4) |
| Group file service (BP-G06) | Group | College financial aid and registrar | College customer information under the Safeguards Rule now sits in DC1 |

**Single points of failure found:**
- **SYS-G1:** mitigated by sealed break-glass accounts, tested quarterly.
- **The shared directory forest across DC1 and DC2:** not mitigated today. A clean-room recovery environment at provider B is planned (P01 GR-01; POAM-012).
- **One clinical interface engine** for all 9 hospitals: mitigated by an active-passive pair across the two data centers.
- **The transfer center:** one location, mitigated by a documented relocation to the flagship's command center.

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) and group directory | All except the College | Vendor multi-region service; directory domain controllers in both data centers; configuration exported daily |
| DC1 and DC2 compute and storage | BP-H01 to BP-H06, BP-H13, BP-P02, BP-P05, BP-G06 | Synchronous storage replication for the EHR (15 minutes); daily copies to the provider B vault |
| Immutable backup vault (provider B) | Recovery of everything above | Daily immutable copies, 35-day retention, separate backup identity |
| SYS-H1 EHR and downtime workstations | All Hospital System clinical processes | Replication to DC2; downtime workstations refresh reports every 2 hours |
| SYS-H2 LIS, blood bank, PACS, archive, pharmacy automation | BP-H04 to BP-H06 | Replication to DC2; PACS archive tier at provider A |
| SYS-H3 devices and device networks | BP-H07, BP-H09 | Device configurations and drug libraries held by clinical engineering; restored from the vault |
| SYS-P1 claims core (DC1); UM and portals (provider A) | BP-P01 to BP-P06 | Nightly backups to the vault; cloud workloads deployed from code |
| SYS-E1 College SaaS | BP-E01 to BP-E05 | Vendor backups under contract; exports of student records weekly |
| People | All | Cross-trained clinical staff; downtime-trained super users on every unit; 85% of Health Plan claims staff can work remotely |

## 7. Recovery priorities
The full order is in `bia.csv` (`recovery_priority`, 1 to 34) and the table in section 4:
1. to 5. Identity and break-glass access, WAN and voice, data center compute and storage, the backup vault, and SOC visibility.
6. to 14. Hospital clinical processes: clinical communications, transfers and EMS coordination, ED care, inpatient care and medication administration, pharmacy, laboratory and blood bank, medical devices, surgery, and imaging.
15. to 17. Prior authorization, the community-connect EHR (it recovers with SYS-H1), and eligibility.
18. to 34. Registration, file and email, portals, member services, College instruction and clinical placement, claims, ASO claims, care management, revenue cycle, public health reporting, College financial aid and registrar, financial close, sepsis alerting, payroll, and admissions.

## 8. Key findings
1. **Clinical MTDs of 2 to 4 hours are met only by failover, not by restore.** Failover to DC2 was tested in 2026 (EHR back in 1 hour 40 minutes; EV-047). A restore from the vault after ransomware has never been tested, and the estimate is 5 to 7 days (EV-021, EV-046) (P01 GR-01; POAM-012).
2. **Diversion is a BIA output.** The P08 runbook uses these MTDs as its diversion triggers: when ED care, laboratory, imaging, or communications will be down longer than their MTD, the hospital's incident command decides on diversion with the ED medical lead.
3. **The College depends on group services for data, not for operations.** Its processes can wait, but its financial aid files on the group file service make it part of any data center incident (P08).
4. **Notification capacity is itself a process** (BP-G02, BP-G08, BP-H08). If the SOC, voice, or email is down, notice clocks and EMS coordination still run, which is why the runbook uses out-of-band channels.
