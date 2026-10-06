# Business Impact Analysis: Cris Santos Company | Real Estate and Rental and Leasing | Mid-Market

**Organization:** Cris Santos Company, Inc. (residential real estate brokerage with property management and the Cris Santos Title and Closing, LLC subsidiary) | **Tier:** Mid-Market (600 employees, about 1,650 contractor agents) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager (Qualified Individual) with the vCISO, the IT Director, and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-13 to 2026-08-07 | **Approved:** Chief Operating Officer, 2026-09-29 (presented to the audit committee and to Title and Closing's board of managers the same day)

## 1. Overview and purpose
This BIA covers every business unit: the sales brokerage (22 offices), transaction services, Title and Closing, property management and leasing, inside sales and relocation, agent services, finance and escrow accounting, and enterprise support functions. It rates 17 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and funds at risk.

The results feed:
- the identification of data, systems, and facilities "in accordance with their relative importance to business objectives" required by the Safeguards Rule (16 CFR 314.4(c)(2));
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment (P09).

## 2. System and business description
The company closes about 12,600 transaction sides a year through about 1,650 contractor agents in 22 Florida offices. Title and Closing closes about 8,400 transactions a year and sends about 140 outgoing wires per business day (about $14.4 million) from its trust accounts. Property management collects about $9.6 million of rent a month for about 3,300 owners. Most of this work runs on the Transaction Management and Closing Communications System (TMCC) described in the SSP (P02): the transaction platform, the title production software, the identity provider, the productivity suite, the 4-account cloud landing zone with the Closing Communications Portal, 23 site networks on SD-WAN, about 740 company endpoints, and the MSSP-operated SIEM. The property management platform, CRM, banking platforms, and accounting system sit next to it (see `../00_company-facts.md` sections 3, 4, and 7).

## 3. Impact categories and values
Dollar values are scaled to $100 million in annual receipts over about 250 business days: about $232,000 per day for the brokerage, $96,000 for Title and Closing, $56,000 for property management, and $16,000 for referral and relocation services. Client money in motion is much larger than revenue: about $14.4 million of disbursements per business day and, in the first 5 days of each month, about $1.9 million of rent per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage, or per event) | More than $100,000 of lost revenue or extra cost, or a single funds loss above $100,000 | $20,000 to $100,000 | Less than $20,000 |
| Operations | Closings, disbursements, or a whole business line stop | One office, one process, or one region stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory | Trust or escrow fund duty breached (Fla. Stat. 626.8473, 475.25), FTC or Florida notice event, or license action | Missed deadline under a rule or contract that can be cured | Internal policy deviation |
| Safety | Plausible injury | Delayed emergency repair (water leak, no air conditioning in summer) | None |
| Reputation | Regional media, loss of the homebuilder or a lender client, or agents leaving | Client or agent complaints, online reviews | Internal only |

The template's safety column is N/A for most processes. Property maintenance dispatch (BP-14) is the only process with a plausible safety impact.

**How loss at MTD was estimated.** Estimated loss is revenue that is not recovered plus extra cost (overtime, rate-lock extensions, per diem interest, waived late fees) over the MTD. Process owners estimated that most delayed closings reschedule, so only about 25% of a day's Title and Closing revenue and about 10% of a day's brokerage revenue is lost per day of outage. Funds-at-risk is shown separately because a single diverted wire can exceed a day's revenue.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 Closing settlement and funds disbursement | Title and Closing | High | 8 | 4 | 0.25 | $45,000 |
| 2 | BP-02 Wire instruction delivery and payee verification | Title and Closing; Transaction Services | High | 8 | 4 | 1 | $20,000 |
| 3 | BP-03 Payoff and lien verification | Title and Closing | High | 24 | 8 | 1 | $15,000 |
| 4 | BP-04 Contract-to-close transaction management | Transaction Services | High | 24 | 8 | 1 | $30,000 |
| 5 | BP-14 Maintenance requests and emergency dispatch | Property Management | Moderate | 24 | 8 | 4 | $5,000 |
| 6 | BP-12 Rent collection and owner distributions | Property Management | High | 48 | 24 | 4 | $25,000 (plus about $3.8 million of rent delayed in the rent window) |
| 7 | BP-05 Earnest money deposit receipt and escrow | Finance | Moderate | 48 | 24 | 24 | $5,000 |
| 8 | BP-06 Title search, examination, and commitment | Title and Closing | Moderate | 48 | 24 | 4 | $10,000 |
| 9 | BP-09 Lead management and inside sales | Inside Sales and Relocation | Moderate | 48 | 24 | 4 | $25,000 |
| 10 | BP-08 Listing management and MLS syndication | Marketing | Moderate | 48 | 24 | 24 | $20,000 |
| 11 | BP-10 Agent onboarding, offboarding, and license compliance | Agent Services | Moderate | 72 | 24 | 24 | $5,000 |
| 12 | BP-11 Commission calculation and agent payouts | Finance | Moderate | 72 | 24 | 24 | $10,000 |
| 13 | BP-13 Tenant screening and leasing applications | Leasing | Moderate | 72 | 24 | 24 | $20,000 |
| 14 | BP-17 Company websites and client communications | Marketing | Low | 72 | 48 | 24 | $10,000 |
| 15 | BP-07 Recording, policy issuance, and post-closing | Title and Closing | Low | 120 | 72 | 24 | $5,000 |
| 16 | BP-15 Escrow and trust account reconciliation | Finance | Moderate | 120 | 72 | 24 | $5,000 |
| 17 | BP-16 Payroll, HR, and financial reporting | Finance and HR | Low | 120 | 72 | 24 | $10,000 |

**Summary:** 5 High, 9 Moderate, and 3 Low processes (17 in total). The sum of estimated losses at each process's MTD is $265,000.

**Enterprise-wide scenario.** If the TMCC were down for 72 hours (for example, ransomware), about 100 closings and 150 sales sides would slip. Unrecovered revenue would be about $140,000 (Title and Closing about $72,000, brokerage about $70,000). Rate-lock extensions and per diem interest would add about $60,000 and overtime about $40,000, for about $240,000 in total. About $43 million of client funds would wait in trust accounts. Incident response, notification, and any funds loss come on top (see P01 R-001, R-002, and R-004).

**What drives the values:**
- **Funds at risk**, not revenue, drives BP-01 to BP-03. An outage pushes staff and clients toward email and manual work, which is exactly when fraudsters strike.
- **Trust and escrow duties** drive BP-05 and BP-15 (Fla. Stat. 475.25(1)(k); r. 61J2-14.008 and 14.012; Fla. Stat. 626.8473).
- **Cash timing** drives BP-12. Rent concentrates in the first 5 days of the month, so the same outage costs far more on the 2nd than on the 20th.

## 5. Key findings
1. **The title production vendor's recovery objective does not meet the BIA.** Its SOC 2 system description states RTO 24 hours and RPO 1 hour. BP-01 needs RTO 4 hours and RPO 15 minutes. The printed disbursement worksheet makes the MTD achievable for funded files, but new closings cannot be balanced (P01 R-010; P09 vendor review VEN-02).
2. **A portal outage is a fraud event waiting to happen.** If the Closing Communications Portal is down, parties fall back to email. The phone-only fallback in BP-02 is written here for the first time and goes into the P08 runbook.
3. **Email and transaction data have no independent backup** (gap 5). The 1-hour RPO for BP-04 rests entirely on the transaction platform vendor and the productivity suite's retention (P01 R-013).
4. **Payee changes outside Title and Closing are unprotected** (gap 2). Owner payout accounts (BP-12), agent payout accounts (BP-11), and sales escrow refunds (BP-05) can be redirected without an out-of-band check. The 2025-11 loss of an $86,000 earnest money refund ($45,000 unrecovered) came from this path (P01 R-003).
5. **Offboarding is a recovery dependency.** During an outage of the identity provider, departing agents cannot be disabled; the printed disable list in BP-10 is the only fallback.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Transaction management platform (SaaS) | Contracts, compliance review, documents, agent and client portal | BP-04, BP-05, BP-08, BP-10, BP-11 |
| SYS-02 Title production and closing software (SaaS) | Settlement statements, disbursement ledger, positive pay files | BP-01, BP-02, BP-03, BP-06, BP-07, BP-15 |
| SYS-03 Identity provider | SSO and MFA for employees and agents | All |
| SYS-04 Productivity suite | Email, files, chat | BP-01 to BP-04, BP-09 |
| SYS-05 Cloud landing zone | Closing Communications Portal, integration service, data warehouse, backup account | BP-01, BP-02, recovery of all workloads |
| SYS-06 Site networks and SD-WAN | 23 sites; dual ISP at headquarters, single ISP with cellular backup at offices | All office work |
| SYS-07 Endpoints | 660 laptops and desktops, 80 phones; spare pre-imaged laptops at headquarters | All |
| SYS-08 SIEM (MSSP) | Detection and investigation | Recovery validation |
| SYS-09 Banking platforms | Escrow, trust, and operating accounts at 3 banks | BP-01, BP-05, BP-11, BP-12, BP-15 |
| SYS-10 Property management platform | Rent, owner statements, work orders, screening | BP-12, BP-13, BP-14 |
| SYS-11 CRM | Leads and scoring | BP-08, BP-09 |
| SYS-12 E-signature service | Contracts and closing documents | BP-01, BP-04 |
| SYS-13 Accounting system | General ledger, commissions, payouts | BP-05, BP-11, BP-15, BP-16 |
| Third parties | Title production vendor, transaction platform vendor, property management platform vendor, banks, lenders, underwriter, MSSP, cloud provider, contract development firm | As listed in `bia.csv` |
| People and facilities | Closers and payoff processors, escrow accounting, transaction coordinators, IT and security team, MSSP | All |

## 7. Regulatory and contractual time limits that shape recovery
| Requirement | What it means for recovery |
|---|---|
| Broker deposits placed in escrow by the end of the third business day (Fla. Stat. 475.25(1)(k); r. 61J2-14.008(3)) | BP-05 MTD is 48 hours, with a branch-deposit workaround |
| Written verification requested within 10 business days when another party holds the deposit (r. 61J2-14.008(2)(b)) | Verification requests resume within the BP-05 RTO; an unconfirmed deposit is also a fraud signal |
| Monthly reconciliation of broker escrow accounts (r. 61J2-14.012(2)) | BP-15 can wait up to 120 hours, but not across month-end |
| Title trust funds used only per closing instructions (Fla. Stat. 626.8473(4)) | Manual disbursement during an outage must keep dual approval and callbacks; no shortcut is allowed |
| Escrow dispute notice to the Florida Real Estate Commission within 15 business days of conflicting demands (r. 61J2-10.032(1)) | A diverted deposit can start this clock (P08) |
| FTC notice within 30 days of discovery of a notification event involving 500 or more consumers (16 CFR 314.4(j)) | Recovery must preserve logs that show what customer information was acquired (P08) |
| Florida individual notice within 30 days of determining a breach (Fla. Stat. 501.171(4)(a)) | Same as above |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-03 identity provider and break-glass accounts | 1 h | Two break-glass accounts per critical system, stored offline |
| 2 | SYS-09 banking access for wire release staff (bank-hosted) | 1 h | Hardware tokens and bank fraud desks; banks are outside the company's network |
| 3 | SYS-06 headquarters network and the title operations center | 2 h | Cellular failover kits; closers can work from offices with closing rooms |
| 4 | SYS-07 clean endpoints for closers and wire release staff | 2 h | 20 pre-imaged spare laptops at headquarters |
| 5 | SYS-02 title production software (vendor-hosted) | 4 h target (vendor states 24 h) | Printed disbursement worksheets; reschedule closings |
| 6 | SYS-05 Closing Communications Portal | 4 h | Phone-only instruction delivery (BP-02) |
| 7 | SYS-04 productivity suite | 4 h | Phone and text through the out-of-band group; no wire instructions by email in any case |
| 8 | SYS-01 transaction management platform (vendor-hosted) | 8 h | Daily deadline export; e-signature service |
| 9 | SYS-08 SIEM and EDR console | 8 h | MSSP runs from its own platform; needed to validate clean recovery |
| 10 | SYS-10 property management platform (vendor-hosted) | 8 h for work orders, 24 h for payments | Answering service; bank lockbox; prior-month ACH file |
| 11 | SYS-05 integration service | 24 h | Manual entry between systems |
| 12 | SYS-11 CRM and SYS-13 accounting system | 24 h | Shared lead mailbox; manual checks |
| 13 | SYS-05 data warehouse and headquarters file server | 72 h | Standard reports in each SaaS system |
