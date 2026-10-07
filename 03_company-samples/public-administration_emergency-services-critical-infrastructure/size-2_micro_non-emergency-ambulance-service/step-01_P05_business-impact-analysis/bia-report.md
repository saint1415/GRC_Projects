# Business Impact Analysis: Cris Santos Company | Emergency Services | Micro

**Organization:** Cris Santos Company, LLC (licensed BLS ambulance service, non-emergency transport only) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (Privacy and Security Officer) with the Owner, the Scheduler-Dispatcher, and the MSP lead technician, 2026-07-27 to 2026-08-07 | **Approved:** Owner, 2026-09-04

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It supports:
- the contingency plan required by the HIPAA Security Rule (45 CFR 164.308(a)(7)), including the Applications and Data Criticality Analysis (164.308(a)(7)(ii)(E)) (C-EMERGENCY-R04);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

No county or state rule sets a recovery time for a non-emergency ambulance service. The company has no 911 zone, so there is no county dispatch performance standard to meet. The HIPAA contingency plan standard and the safety of scheduled patients drive the values here.

## 2. System and business description
The company runs 2 BLS ambulances from one Florida office and garage and makes about 3,000 non-emergency transports a year. Nearly everything runs in vendor SaaS: the ambulance operations platform with its CAD board, trip scheduling, facility request portal, and ePCR (SYS-01), the productivity suite (SYS-02), the billing company's portal (SYS-03), and the hosted phone system with call recording and fax (SYS-04). On site and in the vehicles are 2 desktops, 1 laptop, 3 tablets, and 4 phones (SYS-05), the office network (SYS-06), and the vehicle hotspots and GPS trackers (SYS-07). The MSP backs up the suite to a cloud backup service (SYS-08). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $3,000 a day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $9,000 (about 3 days of revenue) | $2,500 to $9,000 | Less than $2,500 |
| Operations | Trips cannot be booked or dispatched | One function stops or runs on paper | Staff slowed but working |
| Regulatory | Reportable breach; state license action; Medicare overpayment finding | Missed documentation or record deadline (for example, the 48-hour hospital record rule) | Internal policy deviation |
| Safety | A dialysis patient misses a session, or a caller who describes an emergency is not sent to 911 | Delayed but safe transport (for example, a late discharge) | None |
| Reputation | A hospital or dialysis center stops using the company | Facility complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Trip request intake and scheduling | High | 8 h | 4 h | 1 h |
| BP-02 Dispatch and crew coordination | High | 4 h | 2 h | 1 h |
| BP-03 Patient care documentation and hospital record delivery | Moderate | 24 h | 8 h | 1 h |
| BP-04 Medical necessity documentation and trip packets | Moderate | 48 h | 24 h | 24 h |
| BP-05 Billing and claims | Moderate | 72 h | 48 h | 24 h |
| BP-06 Vehicle and equipment readiness | Moderate | 24 h | 8 h | 24 h |
| BP-07 Crew scheduling, payroll, and certification tracking | Low | 120 h | 72 h | 24 h |
| BP-08 State data reporting and records requests | Low | 336 h | 168 h | 24 h |

**What drives the values:**
- **Dialysis patients drive BP-02.** About 18 patients ride three times a week, with the first pickups at 5:00 a.m. Missing a session is a safety event, so dispatch has the shortest MTD (4 hours). Dispatch never fully stops: the Scheduler-Dispatcher can switch to the printed run sheet and phone calls to the crews.
- **Hospital relationships drive BP-01.** Discharge planners call several providers. After one missed day they move to a competitor, and about $3,000 of revenue a day is at stake.
- **A state records rule drives BP-03.** The receiving hospital must be able to get the patient care record on request within 48 hours of dispatch (Rule 64J-1.014, F.A.C.). The tablets work offline, so short outages rarely lose data.
- **Medicare documentation rules drive BP-04.** A scheduled repetitive trip needs a PCS dated no earlier than 60 days before the trip, and an unscheduled trip for a facility resident needs one within 48 hours after it (42 CFR 410.40(e)(2)-(3)).
- **Claims (BP-05) tolerate 72 hours** because payers accept claims within their filing limits and the company holds a 30-day cash reserve.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Ambulance operations platform (SaaS) | CAD board, schedule, facility portal, ePCR, hospital delivery, state export | Vendor backups and replication (SOC 2 system description: RTO 4 h, RPO 15 min; see P09) | BP-01, BP-02, BP-03, BP-04, BP-05, BP-08 |
| SYS-04 Hosted phone system (SaaS) | Request lines, call recording, on-call forwarding, fax-to-email | Vendor service resilience; calls forward to the on-call phone | BP-01, BP-02, BP-04 |
| SYS-02 Productivity suite (SaaS) | Email, shared drive, shared fax mailbox | Vendor resilience; nightly copy to SYS-08 | BP-04, BP-06, BP-07, BP-08 |
| SYS-08 Cloud backup (SaaS) | Nightly copy of mailboxes and the shared drive, 30 days of versions | **Never restore-tested** | BP-07 |
| SYS-03 Billing company portal | Claims status, remittances, denials | Billing company's own systems | BP-05 |
| SYS-05 Endpoints | 2 desktops, 1 laptop, 3 tablets, 4 phones | No local data by design, except unsynced ePCR records on tablets | All |
| SYS-06 Office network and internet | Firewall, Wi-Fi, one cable line | Firewall configuration backed up by the MSP | BP-01, BP-02 |
| SYS-07 Vehicle hotspots and GPS trackers | Tablet connectivity and vehicle location | Crew phones as backup connection | BP-02, BP-03, BP-06 |
| People | Owner, Office Manager, Scheduler-Dispatcher, 4 EMTs | The Owner and the Office Manager can both dispatch | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | BAA | Evidence of recovery capability |
|---|---|---|---|
| Operations platform vendor | BP-01, BP-02, BP-03, BP-04, BP-05, BP-08 | Yes | SOC 2 Type 2 report reviewed (P09). RPO 15 min meets every RPO here; **RTO 4 h does not meet the 2-hour RTO for BP-02** |
| Hosted phone and fax vendor | BP-01, BP-02, BP-04 | Signed 2026-08-21 | Vendor service commitments (standard terms) |
| MSP | Recovery of the office computers, firewall, and backup | Yes | Business hours only; 4-business-hour response; no recovery commitment |
| Billing company | BP-05 | Yes | Questionnaire answers only; no SOC 2 report offered |
| Productivity suite vendor | BP-04, BP-07, BP-08 | Yes | Vendor service commitments |
| Backup service (resold by the MSP) | Restore of mailboxes and the shared drive | Through the MSP (flow-down not verified) | None until the first restore test |
| Internet provider and cellular carrier | Every SaaS function at the office; tablet sync in vehicles | Not business associates (conduits) | None; one office line |

**Key findings:**
1. **The platform vendor's 4-hour RTO is longer than the 2-hour RTO for dispatch.** The gap is covered only by manual dispatch, which depends on a run sheet printed "most nights" and has never been practiced (risk R-008). A nightly printed run sheet and a quarterly manual dispatch drill are required.
2. **The MSP is not there when dispatch starts.** Dialysis pickups begin at 5:00 a.m., but the MSP works 7:00 a.m. to 6:00 p.m. on weekdays. An early-morning outage waits for the owner or the office staff (R-016, P08).
3. **The shared office backup is unproven.** SYS-08 has never been restore-tested, so the 24-hour RPO for BP-07 is an assumption (R-005).
4. **The office internet line is a single point of failure for intake and dispatch at the desk.** The crew phones and hotspots use a different carrier path and are the fallback (R-009).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Manual dispatch: printed run sheet and crew phones | Immediate | Paper run sheet; phone calls and texts to crew phones; paper status board |
| 2 | Request lines (SYS-04) | 15 min | Forward request lines to the on-call phone from the vendor's web portal |
| 3 | Platform access from a clean device (SYS-01) | 2 h | The owner laptop or the on-call phone; vendor-hosted data unaffected by office outages |
| 4 | Internet at the office (SYS-06) | 2 h | Hotspot from a crew phone or a spare vehicle hotspot |
| 5 | Vehicle hotspots and tablets (SYS-07, SYS-05) | 8 h | Tablets document offline; paper patient care report forms |
| 6 | Office desktops (SYS-05) | 1 business day | MSP reimages; the owner laptop covers the dispatch desk |
| 7 | Email and the shared fax mailbox (SYS-02, SYS-04) | 8 h | Fax-to-email reads from the phone vendor's web portal |
| 8 | Billing interface (SYS-03) | 48 h | Hold trips; billing company catches up |
| 9 | Shared drive restore (SYS-08 to SYS-02) | 72 h | Payroll service repeats the prior payroll; printed crew schedule |
