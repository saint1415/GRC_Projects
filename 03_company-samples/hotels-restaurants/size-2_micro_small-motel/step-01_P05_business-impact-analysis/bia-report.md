# Business Impact Analysis: Cris Santos Company | Accommodation and Food Services | Micro

**Organization:** Cris Santos Company, LLC (independent 38-unit roadside motel) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Assistant Manager (Security and Privacy Lead) with the Owner-Manager, the Night Auditor, the Head Housekeeper, and the MSP lead technician, 2026-07-13 to 2026-07-24 | **Approved:** Owner-Manager, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the motel, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the short contingency plan the motel will write by 2026-12-31 (P01 R-011, R-022).

No law requires a motel to keep a contingency plan. PCI DSS v4.0.1 asks for an incident response plan that covers business recovery and continuity (requirement group 12.10), and the merchant agreement expects card payments to be taken only in approved ways during an outage. Those, and the motel's own cash flow, are the drivers here.

## 2. System and business description
One Florida motel beside an interstate exit: 38 units, 7 employees, a front desk open 24 hours, about 5,900 stays a year, and about 30% of room-nights from work crews. Nearly everything runs in vendor SaaS: the all-in-one cloud PMS with its booking engine, channel manager, point-of-sale module, and card vault (SYS-01), the payment gateway (SYS-02), the productivity suite (SYS-05), and the accounting and payroll services (SYS-08). On site are the front desk and back office PCs, a laptop, and 2 tablets (SYS-03), the office and guest networks (SYS-04), the door lock system (SYS-06), and CCTV (SYS-07). The MSP runs IT. See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $3,000 a day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $9,000 (about 3 days of revenue) | $2,000 to $9,000 | Less than $2,000 |
| Operations | Guests cannot check in or get keys | One function stops; front desk slowed | Staff slowed but working |
| Regulatory | Reportable card or personal data breach; acquirer non-compliance | Guest register not available; tax filing late | Internal policy deviation |
| Safety | A guest is stranded at night or a key reaches the wrong person | A guest waits for a room or a key | None |
| Reputation | Loss of a crew account or a run of poor OTA reviews | Individual complaints or reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Check-in, check-out, and room keys | High | 4 h | 2 h | 1 h |
| BP-02 Reservations and distribution | High | 8 h | 4 h | 1 h |
| BP-03 Card payments, deposits, and no-show charges | High | 8 h | 4 h | 1 h |
| BP-04 Night audit and guest register | Moderate | 24 h | 12 h | 24 h |
| BP-05 Housekeeping and room status | Moderate | 24 h | 8 h | 24 h |
| BP-06 Crew accounts and direct billing | Moderate | 72 h | 48 h | 24 h |
| BP-07 Guest Wi-Fi, lobby market, and guest services | Moderate | 24 h | 8 h | 24 h |
| BP-08 Accounting, payroll, and tax filings | Low | 72 h | 48 h | 24 h |

**What drives the values:**
- Check-in (BP-01) has the shortest MTD because guests arrive through the evening and night. A guest who cannot get a key at midnight is stranded, and walk-ins go to the next exit.
- Reservations (BP-02) and payments (BP-03) can run on paper and standalone terminals for most of a shift. Past 8 hours, the OTAs keep selling rooms that are already gone, and walked guests cost about $150 each in another motel's rate and goodwill.
- The register (BP-04) only has to be available for inspection (Fla. Stat. 509.101(2)); one missed night audit can be rerun.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Cloud PMS (SaaS) | Reservations, profiles, folios, register, booking engine, channel manager, point-of-sale module, card vault | PMS vendor's replication and backups (SOC 2 report states RPO 15 minutes and RTO 4 hours; see P09) | BP-01 to BP-07 |
| SYS-02 Payment gateway and 2 P2PE terminals | Card authorization and settlement | Transactions held at the gateway; terminals can run in standalone mode | BP-01, BP-03, BP-06, BP-07 |
| SYS-03 Endpoints | Front desk PC, back office PC, laptop, 2 tablets | No local business data by design, except the lock database on the back office PC | All |
| SYS-04 Motel network and internet | Firewall, office network, staff and guest Wi-Fi, one internet line | Firewall configuration backed up by the MSP | All |
| SYS-05 Productivity suite (SaaS) | Email, shared front desk mailbox, files | Vendor resilience; nightly copy to SYS-09 | BP-06, BP-08 |
| SYS-06 Door lock system | Lock software and database on the back office PC; USB encoder at the front desk | **Excluded from the nightly backup until 2026-08-12** (found in P07 testing on 2026-08-04); never restore-tested. Rebuilding from the lock vendor takes 1 to 2 days | BP-01 |
| SYS-07 CCTV | 10 cameras and a recorder | 21 days on the recorder; not backed up | Property security |
| SYS-08 Accounting SaaS and payroll service | Books, payroll, PIN time clock | Vendor-hosted | BP-08 |
| SYS-09 Cloud backup (MSP-operated) | Nightly copy of the back office PC and the suite, 30 days of versions | **No restore test since setup in 2024** | BP-06, BP-08 |
| People | 7 employees; Owner-Manager lives on site | Cross-training: the Owner-Manager and Assistant Manager can work every front desk shift | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Agreement and evidence of recovery capability |
|---|---|---|
| PMS vendor | BP-01 to BP-07 | SOC 2 Type 2 report reviewed (P09): RTO 4 h and RPO 15 min meet BP-02 and BP-03 but **not the 2-hour RTO of BP-01**. Paper arrivals and offline key encoding cover the gap |
| Payment gateway and P2PE solution provider | BP-03 (and card payments in BP-01, BP-06, BP-07) | Service provider AOC (2026-01); standalone terminal mode; no availability commitment in the merchant agreement |
| MSP | Recovery of every on-site system; operates the backup | Contract has a 4-business-hour response time and **no recovery time commitment** |
| Door lock vendor | Key encoding if the lock software or database is lost | Remote support only; no written recovery commitment |
| Internet service provider | Every SaaS function and the terminals | One line; no failover |
| Productivity suite vendor | BP-06 (crew correspondence), BP-08 | Vendor service commitments (standard terms) |
| 3 OTAs | About half of transient bookings | OTA extranets reachable from any phone |

**Key findings:**
1. **Check-in depends on the door lock database, and its backup is unproven.** The lock software runs on the back office PC. P07 testing on 2026-08-04 found that the MSP's backup job excluded its database; the MSP added it on 2026-08-12, but it has never been restored. Until a restore test with the lock vendor succeeds, a failed PC means no new keys until the vendor rebuilds the system (risk R-009).
2. **The PMS vendor meets the BIA except for check-in.** Its RTO of 4 hours exceeds BP-01's 2 hours. The fallback is the printed arrivals list from each night audit plus offline key encoding. That fallback only works if the lock system survives.
3. **The internet line is a single point of failure** for the PMS, the terminals, and the OTAs (risk R-011).
4. **The MSP contract has no recovery commitment.** A 4-business-hour response time on a Saturday night is not a recovery time. The P01 treatment for R-020 adds one at renewal.
5. **The cloud backup is unproven.** There has been no restore test since setup (risk R-012).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Internet and office network (SYS-04) | 2 h | Cellular failover router (to be installed by 2026-12-31); the Owner-Manager's phone hotspot for the front desk PC until then |
| 2 | Front desk PC and the door lock system on the back office PC (SYS-03, SYS-06) | 2 h | Owner-Manager's laptop for the PMS; key encoding needs the back office PC, so the MSP restores it first |
| 3 | PMS access (SYS-01) | 2 h (vendor RTO 4 h) | Printed arrivals list; paper registration cards |
| 4 | Payment terminals and gateway (SYS-02) | 4 h | Standalone terminal mode |
| 5 | Channel manager and OTA connections (in SYS-01) | 4 h | Close inventory in the OTA extranets |
| 6 | Housekeeping tablets and staff Wi-Fi (SYS-03, SYS-04) | 8 h | Paper room status board |
| 7 | Email and the shared front desk mailbox (SYS-05) | 8 h | Owner-Manager's phone; crew contacts by phone |
| 8 | Guest Wi-Fi (SYS-04) | 8 h | Notice at the desk; fee credit if the outage lasts overnight |
| 9 | Accounting and payroll (SYS-08) and the back office PC files from SYS-09 | 48 h | Payroll service repeats the prior payroll |
