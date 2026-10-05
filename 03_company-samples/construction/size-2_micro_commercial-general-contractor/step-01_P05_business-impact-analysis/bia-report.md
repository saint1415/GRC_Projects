# Business Impact Analysis: Cris Santos Company | Construction | Micro

**Organization:** Cris Santos Company, LLC (commercial and institutional building general contractor) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (security and compliance lead) with the Owner, the Project Manager and Estimator, and the MSP lead technician, 2026-07-20 to 2026-07-31 | **Approved:** Owner and President, 2026-08-31

## 1. Overview and purpose
This BIA lists the company's 7 business functions, how long each can be down, and how much data each can lose. It supports:
- the short IT contingency plan due 2026-11-30 (P02 control CP-2);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

No federal rule requires this company to have a contingency plan. FAR 52.204-21 and CMMC Level 1 do not include one. The BIA exists because the company cannot afford a missed bid, a missed payroll, or a diverted payment.

For a contractor this size, **the integrity of payment details matters more than availability.** A two-day outage of the accounting system is an inconvenience. One altered bank record can cost up to $78,000, which is close to a year of the company's profit (P01 R-001, R-002). The BIA therefore records integrity workarounds, such as confirming bank details by phone, alongside the usual downtime values.

## 2. System and business description
One Florida flex-space office with a tool room and a small yard, 4 active jobsites, and 7 employees. Almost everything runs in vendor SaaS:
- the project management and pay application platform (SYS-01)
- small-business accounting (SYS-02) and the payroll service (SYS-03)
- the productivity suite for email and files (SYS-04), with a cloud backup run by the MSP (SYS-07)

On site are 4 laptops, 1 desktop, 5 phones, and 2 tablets (SYS-05) and the office network (SYS-06). Payments leave through the bank portal (SYS-08). See `../00_company-facts.md` sections 3 and 4.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $4,400 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25,000 (a diverted payment, a lost bid, or more than 5 days of revenue) | $5,000 to $25,000 | Less than $5,000 |
| Operations | Two or more jobsites stop, or a bid is missed | One jobsite or one office function stops | Staff slowed but working |
| Regulatory and contractual | Missed federal payment or payroll obligation (FAR 52.232-27, 52.222-8), an inaccurate federal representation, or a reportable breach | Missed contract deliverable date | Internal policy deviation |
| Safety | Crews work from wrong drawings | Delayed inspections | None |
| Reputation | An owner or the surety loses confidence; subcontractors stop bidding to the company | Owner or subcontractor complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Progress billing and collections | High | 72 h | 24 h | 24 h |
| BP-02 Subcontractor and supplier payments | High | 120 h | 48 h | 24 h |
| BP-03 Project documents and field coordination | High | 24 h | 8 h | 4 h |
| BP-04 Estimating and bid submission (bid weeks) | High | 8 h | 4 h | 24 h |
| BP-05 Payroll and certified payroll | High | 48 h | 24 h | 24 h |
| BP-06 Federal contract administration | Moderate | 72 h | 24 h | 24 h |
| BP-07 Office administration and records | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **Bid deadlines drive BP-04.** A late bid is rejected. During bid weeks the tolerable outage is one working day or less; outside bid weeks it relaxes to 72 hours. The DoD bid expected in late 2026 is worth about 29% of a year's revenue.
- **Drawings drive BP-03.** Crews can work from printed sets for about a day. After that, the risk of building from superseded sheets rises.
- **Federal rules drive BP-02 and BP-05.** On FC-1, subcontractors must be paid within 7 days of the company's receipt of payment (FAR 52.232-27(c)(1)), and certified payrolls are due weekly (FAR 52.222-8(b)(1)).
- **Cash drives BP-01.** Billing is monthly, so a 3-day outage outside pay app week is survivable. The real exposure is integrity. On FC-1, a payment sent to wrong EFT information that the company supplied in SAM is the company's loss to recover (FAR 52.232-33(e)(2)).

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Project management and pay application platform (SaaS) | Drawings, RFIs, submittals, daily logs, pay apps | Vendor backups and replication (SOC 2 report states RTO 4 h and RPO 1 h; P09). No company export | BP-01, BP-03 |
| SYS-02 Accounting (SaaS) | Billing, accounts payable, vendor bank details, ACH file | Vendor service resilience | BP-01, BP-02 |
| SYS-03 Payroll service (SaaS) | Payroll, direct deposit, certified payroll reports | Vendor service resilience; vendor can repeat a prior payroll | BP-05 |
| SYS-04 Productivity suite (SaaS) | Email and the shared drive (estimates, contracts, HR files) | Vendor resilience; daily copy to SYS-07 | BP-01, BP-02, BP-04, BP-06, BP-07 |
| SYS-07 Cloud backup (SaaS, run by the MSP) | Daily copy of email and files, 30 days | **Never restore-tested** | BP-04, BP-07 |
| SYS-05 Endpoints | 4 laptops, 1 desktop, 5 phones, 2 tablets | Estimates and drawings live in SaaS; laptops can be reimaged by the MSP | All |
| SYS-06 Office network and internet | Firewall, Wi-Fi, one internet line | MSP keeps the firewall configuration; phones can act as hotspots | All office work |
| SYS-08 Bank portal | ACH and wire release | Bank-hosted | BP-02 |
| People | 7 employees; only the Office Manager knows payroll, billing entry, and the bank portal steps | Owner can release payments; payroll service support line | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| SYS-01 vendor | BP-01, BP-03 | SOC 2 Type 2 report reviewed (P09); RTO 4 h and RPO 1 h meet this BIA |
| Accounting vendor | BP-01, BP-02 | Standard service terms only |
| Payroll service | BP-05 | Standard service terms; repeat-payroll option confirmed by phone 2026-07-23 |
| Productivity suite vendor | Email and files for every function | Standard service commitments |
| MSP (and its backup subcontractor) | Endpoint and network recovery; restore of email and files | No written recovery commitment; business-hours response only |
| Bank | BP-02 | Bank treasury agreement |
| Internet provider and cellular carrier | Office SaaS access; jobsite tablets | None; one office line |

**Key findings:**
1. **The SYS-01 vendor meets the BIA.** Its stated RTO (4 h) and RPO (1 h) meet the targets for BP-03.
2. **The email and file backup is unproven.** SYS-07 has never been restore-tested, so the 24-hour RPO for BP-04 and BP-07 is an assumption (risk R-013).
3. **One person holds most of the back office.** Only the Office Manager knows how to run payroll, enter billing, and prepare payments. An absence during an incident would stall BP-02 and BP-05 (risk R-022).
4. **The MSP contract has no recovery commitment.** It promises business-hours response, not recovery. After-hours work is billed hourly and not guaranteed.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Company phones and the printed contact card (out-of-band channel) | 1 h | Card in the office binder and in the Owner's truck: verified numbers for owners' accounts payable, the bank fraud desk, the MSP, the insurer, and the top 10 subcontractors |
| 2 | SYS-04 email access for named users | 4 h | Vendor-hosted; phones and text messages meanwhile |
| 3 | A clean laptop for estimating (bid weeks) | 4 h | Any company laptop; MSP reimages if needed |
| 4 | SYS-01 project management platform | 8 h | Printed drawing sets in each storage container |
| 5 | SYS-06 office network and internet | 8 h | Phone hotspots |
| 6 | SYS-03 payroll | 24 h | Repeat prior payroll through the payroll service |
| 7 | SYS-02 accounting and SYS-08 bank portal | 24 h | Manual pay app from spreadsheets; manual ACH from the last approved batch |
| 8 | SYS-10 federal portals | 24 h | Any clean device with the Owner's sign-in |
| 9 | SYS-07 restore of email and files | 72 h | Request copies of contracts and certificates from owners, the insurer, and the surety |

**After any suspected business email compromise, "recovered" means "verified".** No payment instruction received or changed during the incident window may be used until it is confirmed by phone to a number already on file (P08).
