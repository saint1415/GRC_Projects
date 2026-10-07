# Business Impact Analysis: Cris Santos Company | Real Estate and Rental and Leasing | Micro

**Organization:** Cris Santos Company, LLC (residential real estate brokerage with property management) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (security and compliance lead) with the Broker-owner, the Bookkeeper, the senior Transaction Coordinator, the Property Manager, and the MSP lead technician, 2026-07-27 to 2026-08-07 | **Approved:** Broker-owner, 2026-09-14

## 1. Overview and purpose
This BIA lists every business function of the brokerage, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order and the "verified channel first" rule in the incident response runbook (P08);
- the Florida broker escrow duties (Fla. Stat. 475.25(1)(k); Fla. Admin. Code ch. 61J2-14), which keep running when a system is down.

No federal rule requires this brokerage to have a contingency plan. The FTC Safeguards Rule does not apply to it (P03 section 1), and even its benchmark incident response element (16 CFR 314.4(h)) speaks of recovering from security events, not of a BIA. The BIA is done because the brokerage cannot protect client money without knowing which channels it depends on.

## 2. System and business description
One Florida office, 7 employees, and about 22 contractor sales associates. About 190 sales sides and 85 managed rental homes. Nearly everything runs in vendor SaaS: the transaction platform (SYS-01), email and files (SYS-02), e-signature (SYS-03), the property management platform (SYS-05), and accounting (SYS-06). Online banking for the two escrow accounts and the operating account is bank-hosted (SYS-04). On site are 9 company devices (SYS-07) and the office network (SYS-08). The MSP runs IT and the email backup (SYS-09). See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual receipts, about $4,400 per business day. A single buyer's closing wire is typically $60,000 to $250,000, so one diverted wire can exceed a month of receipts even though the money is the client's.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $20,000 (about 5 business days of receipts), or any loss of escrowed or client funds | $5,000 to $20,000 | Less than $5,000 |
| Operations | A closing cannot fund, or clients cannot be reached on a closing day | One line of business stops (sales or property management) | Staff slowed but working |
| Regulatory | Escrow violation, Florida Real Estate Commission complaint, or reportable breach | Missed documentation or notice step | Internal policy deviation |
| Safety | Not a primary factor. Rated only for urgent maintenance at managed rental homes | Urgent repair delayed beyond one day | None |
| Reputation | A client loses closing funds; local media coverage; owners move their homes to another manager | Client complaints or online reviews | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Escrow deposits and disbursements | High | 24 h | 4 h | 24 h |
| BP-02 Client and agent communications | High | 8 h | 4 h | 4 h |
| BP-03 Contract-to-close transaction management | High | 24 h | 8 h | 4 h |
| BP-04 Property management operations | Moderate | 72 h | 24 h | 24 h |
| BP-05 Listing marketing and lead response | Moderate | 72 h | 24 h | 24 h |
| BP-06 Leasing and tenant screening | Low | 120 h | 72 h | 24 h |
| BP-07 Commission disbursement, payroll, and accounting | Low | 120 h | 72 h | 24 h |
| BP-08 Agent onboarding, offboarding, and license compliance | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **Money movement drives BP-01.** The risk is less that the bank is down than that the channel used to confirm instructions (email and phone) is untrustworthy on a closing day. The 4-hour RTO is for a verified phone channel to the bank and a clean device for the Broker-owner to approve wires. The 24-hour RPO is acceptable because both escrow ledgers can be rebuilt from bank records, but only if the sales escrow ledger spreadsheet is backed up (it is in SYS-02, which SYS-09 covers).
- **BP-02 is High for a reason specific to this business.** When email is down or compromised, clients look for another channel, and fraudsters supply it. The runbook (P08) tells staff to phone clients and say that no wire instructions will come by email.
- **BP-03** follows contract deadlines and the 10-business-day deposit verification rule (r. 61J2-14.008(2)(b)). The transaction platform vendor's SOC 2 report states a 4-hour RTO and a 1-hour RPO, which meet the targets (P09).
- **BP-04** carries the only safety-related impact: urgent repairs at managed homes still need to be dispatched by phone.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-04 Online banking (bank-hosted) | Sales escrow, property management escrow, and operating accounts; dual control | Bank's own systems; branch and phone as fallback | BP-01, BP-04, BP-07 |
| SYS-02 Productivity suite (SaaS) | 29 mailboxes; shared files including the sales escrow ledger spreadsheet | Vendor resilience; SYS-09 nightly copy of employee mailboxes and shared files (30 days) | BP-01, BP-02, BP-05, BP-08 |
| SYS-09 SaaS-to-SaaS backup | Nightly copy of employee mailboxes and shared files | **Never restore-tested; agent mailboxes not covered** | BP-01, BP-02 |
| SYS-01 Transaction platform (SaaS) and SYS-03 e-signature | Contracts, disclosures, deadlines, signed documents | Vendor backups (SOC 2: RPO 1 h); no company copy | BP-03, BP-08 |
| SYS-05 Property management platform (SaaS) | Escrow ledger, rents, distributions, screening | Vendor backups (not yet documented) | BP-01, BP-04, BP-06 |
| SYS-06 Accounting SaaS | Operating books, commissions, payroll export | Vendor backups | BP-07 |
| SYS-07 Endpoints | 7 laptops, 2 desktops | Laptops carry no unique data by design; the scanning workstation keeps local scans (gap) | All |
| SYS-08 Office network | Firewall, Wi-Fi, one internet line | Firewall configuration backed up by the MSP | Office work only; staff can work from laptops elsewhere |
| People | Broker-owner (only escrow approver), Office Manager, Bookkeeper, 2 Transaction Coordinators, Property Manager, Leasing Assistant | Cross-training: the Office Manager covers transaction coordination; the Property Manager covers leasing | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Contract security terms | Evidence of recovery capability |
|---|---|---|---|
| Escrow bank | BP-01, BP-04, BP-07 | Bank treasury agreement | Bank's own; fraud desk number recorded 2026-08 |
| Productivity suite vendor | BP-02, BP-05, BP-08; ledger for BP-01 | Standard terms | Vendor service commitments |
| Transaction platform vendor | BP-03 | Standard terms; SOC 2 report under NDA | SOC 2 Type 2 reviewed (P09): RTO 4 h, RPO 1 h meet this BIA |
| Property management platform vendor | BP-04, BP-06; ledger for BP-01 | Standard terms | Not yet requested (P07 POAM-009) |
| MSP | Recovery of every company device; operates the backup | **No recovery time and no incident notice clause**; 8-business-hour response | None in writing |
| Backup vendor (MSP-operated) | Restore of employee mail and files | Through the MSP | None until the first restore test |
| Internet provider | Office access to every SaaS service | Not applicable | Single line; phone hotspots as fallback |

**Key findings:**
1. **The Broker-owner is a single point of failure for BP-01.** Only the Broker-owner can approve escrow wires, and the approval code arrives by text message on one phone. If the Broker-owner is unavailable on a closing day, a held deposit cannot reach the title company (P01 R-023).
2. **The email backup is unproven and incomplete.** SYS-09 has never been restored, and the 22 agent mailboxes, which carry most client communication, have no independent copy (P01 R-008).
3. **The MSP contract has no recovery commitment.** An 8-business-hour response time is not a recovery time. The contract amendment in P01 (R-013) adds one, with a 24-hour incident notice duty.
4. **The scanning workstation breaks the "no local data" rule.** It keeps scans of IDs and bank statements, so its loss is both a recovery and a disclosure problem (P01 R-011).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Verified phone channel to the escrow bank and a clean device for the Broker-owner | 1 h | Bank relationship manager and fraud desk numbers on the printed contact card; branch visit |
| 2 | SYS-02 email for employees (accounts secured first, then mail) | 4 h | Phone tree from the printed contact card; office line forwarded to a cell phone |
| 3 | SYS-04 online banking with dual control | 4 h | Wire request at the branch with the Broker-owner present |
| 4 | SYS-01 transaction platform and SYS-03 e-signature | 8 h | Vendor-hosted; printed weekly deadline list; paper addenda |
| 5 | SYS-07 clean laptops for staff | 8 h | MSP reimages; staff share clean laptops |
| 6 | SYS-05 property management platform | 24 h | Urgent maintenance by phone; accept checks |
| 7 | SYS-08 office network and internet | 24 h | Phone hotspots; work from home on laptops |
| 8 | SYS-06 accounting and payroll | 72 h | Manual commission checks; repeat prior payroll |
| 9 | SYS-09 restore of lost employee mail and files | 72 h | Ask clients and title companies to re-send documents |
