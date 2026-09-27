# Business Impact Analysis: Cris Santos Company | Health Care and Social Assistance | Micro

**Organization:** Cris Santos Company, LLC (primary care office, two physicians) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (Privacy and Security Officer) with both physicians, the Billing Specialist, and the MSP lead technician, 2026-07-20 to 2026-07-31 | **Approved:** owner physician, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the practice, how long each can be down, and how much data each can lose. It supports:
- the contingency plan required by the HIPAA Security Rule (45 CFR 164.308(a)(7)), including the Applications and Data Criticality Analysis (164.308(a)(7)(ii)(E));
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

The CMS emergency preparedness conditions (42 CFR 482.15 and the parallel rules) do not apply: physician offices are not among the covered provider types. The HIPAA contingency plan standard is the driver here.

## 2. System and business description
One Florida office suite, 7 employees, about 3,500 active patients, and about 40 visits per clinic day. Nearly everything runs in vendor SaaS: the EHR/PM with portal, e-prescribing, and clearinghouse (SYS-01), the productivity suite (SYS-02), and cloud fax (SYS-06). On site are 10 computers and 2 tablets (SYS-03), the office network (SYS-04), and the ECG machine and spirometer (SYS-07). The MSP runs IT. See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $4,400 per clinic day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $15,000 (about 3 clinic days) | $4,000 to $15,000 | Less than $4,000 |
| Operations | The office cannot see patients | One function stops; visits slowed | Staff slowed but working |
| Regulatory | Reportable breach or federal program issue | Missed documentation or timeliness requirement | Internal policy deviation |
| Safety | Plausible patient harm (missed allergy, medication, or critical result) | Delayed but safe care | None |
| Reputation | Local media coverage or loss of hospital referral relationships | Patient complaints or online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Patient visits and clinical documentation | High | 8 h | 4 h | 1 h |
| BP-02 Scheduling, check-in, and eligibility | High | 8 h | 4 h | 1 h |
| BP-03 E-prescribing and refills | High | 8 h | 4 h | 1 h |
| BP-04 In-office diagnostics (ECG and spirometry) | Moderate | 24 h | 8 h | 24 h |
| BP-05 Referrals, records requests, and faxed results | Moderate | 24 h | 8 h | 24 h |
| BP-06 Claims and billing | Moderate | 72 h | 48 h | 24 h |
| BP-07 Patient communications | Moderate | 24 h | 8 h | 24 h |
| BP-08 Office administration and payroll | Low | 72 h | 48 h | 24 h |

**What drives the values:**
- Patient safety drives BP-01 and BP-03. Physicians cannot safely prescribe without allergy and medication lists.
- An MTD of 8 hours is one clinic day. Past that, about 40 visits must be cancelled and rebooked, with about $4,400 of revenue delayed each day.
- Claims (BP-06) tolerate 72 hours because payers accept late claims within their filing limits, and the practice holds a 30-day cash reserve.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 EHR/PM (SaaS) | Chart, schedule, portal, e-prescribing, lab interface, clearinghouse | EHR vendor's backups and replication (vendor SOC 2 report states RPO 15 minutes; see P09) | BP-01, BP-02, BP-03, BP-06, BP-07 |
| SYS-02 Productivity suite (SaaS) | Email and the shared drive | Vendor service resilience; shared drive copied nightly to SYS-05 | BP-05, BP-07, BP-08 |
| SYS-05 File-sync backup (SaaS) | Nightly copy of the shared drive, 30 days of versions | **Never restore-tested** | BP-08 |
| SYS-06 Cloud fax (SaaS) | Inbound and outbound fax | Faxes queue at the vendor | BP-05 |
| SYS-03 Endpoints | 6 desktops, 4 laptops, 2 tablets | No local data by design, except the procedure-room workstation (results imported the same day) | All |
| SYS-04 Office network and internet | Firewall, Wi-Fi, one internet line | Firewall configuration backed up by the MSP | All |
| SYS-07 ECG machine and spirometer | Connected by USB to the procedure-room workstation | Paper ECG printout | BP-04 |
| People | 2 physicians, 2 MAs, Front Desk Coordinator, Billing Specialist, Office Manager | Cross-training: the Office Manager covers the front desk and billing | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | BAA | Evidence of recovery capability |
|---|---|---|---|
| EHR vendor (with its clearinghouse, e-prescribing network, and lab interface) | BP-01, BP-02, BP-03, BP-06 | Yes | SOC 2 Type 2 report reviewed (P09); RTO 4 h and RPO 15 min meet this BIA |
| MSP | Recovery of every on-site system; operates the backup | Yes | No written recovery commitment; the MSP contract has only a 4-business-hour response time |
| Productivity suite vendor | BP-05, BP-07, BP-08 | Accepted 2026-08-14 | Vendor service commitments (standard terms) |
| Backup service (MSP subcontractor) | Restore of the shared drive | Through the MSP (flow-down not verified) | None until the first restore test |
| Cloud fax vendor | BP-05 | Yes | Vendor service commitments |
| Internet provider | Every SaaS function | Not a business associate (conduit) | None; single line |

**Key findings:**
1. **The EHR vendor meets the BIA.** Its stated RTO (4 h) and RPO (15 min) meet the targets for BP-01 to BP-03.
2. **The shared-drive backup is unproven.** SYS-05 has never been restore-tested, so the 24-hour RPO and 48-hour RTO for BP-08 are assumptions (risk R-005).
3. **The internet line is a single point of failure for every High function** (risk R-010).
4. **The MSP contract has no recovery commitment.** Its 4-business-hour response time is not a recovery time. The contract amendment in P01 (R-013) adds one.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Internet and office network (SYS-04) | 2 h | Cellular failover router (to be installed by 2026-11-30); physician phone hotspot until then |
| 2 | Clean endpoints for the front desk and physicians (SYS-03) | 4 h | Physicians' encrypted laptops and the tablets; MSP reimages desktops |
| 3 | EHR/PM access (SYS-01) | 4 h | Vendor-hosted; paper downtime forms until restored |
| 4 | Cloud fax (SYS-06) | 8 h | Vendor web portal from any clean device |
| 5 | Procedure-room workstation and devices (SYS-07) | 8 h | Paper ECG printouts; refer spirometry |
| 6 | Email and phones (SYS-02) | 8 h | Office line forwarded to a cell phone |
| 7 | Claims (through SYS-01) | 48 h | Queue charges |
| 8 | Shared drive restore (SYS-05 to SYS-02) | 48 h | Payroll service repeats prior payroll |
