# Business Impact Analysis: Cris Santos Company | Real Estate and Rental and Leasing | Small

**Organization:** Cris Santos Company, LLC (residential real estate brokerage) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Qualified Individual) with the Closing Services Manager, Controller, Director of Property Management, and Transaction Coordination Manager | **Approved:** COO, 2026-09-21

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the recovery part of the written incident response plan required by the FTC Safeguards Rule (16 CFR 314.4(h));
- the criteria for assessing availability and integrity in the written risk assessment (314.4(b)(1)(ii));
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

## 2. System and business description
The company runs two Florida offices with 60 employees and about 140 contractor sales associates. Sales transactions run on the transaction management platform and email; closings run on the closing and escrow software and commercial online banking; property management runs on its own SaaS platform. Together these form the Transaction Management and Closing Communications System (TMCC) and its neighbors. See `../00_company-facts.md` sections 3-4.

## 3. Impact categories and values
Dollar values are scaled to $9.0 million in annual receipts, about $36,000 per business day. A single diverted closing wire is typically $150,000 to $450,000.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $100,000 (about 3 days of receipts, or one diverted wire) | $20,000 to $100,000 | Less than $20,000 |
| Operations | Closings stop, or clients cannot be reached | One office or one division stops | Staff slowed but working |
| Regulatory | Escrow or trust fund violation; reportable breach; Commission complaint | Missed documentation or deadline | Internal policy deviation |
| Safety | Not a primary factor. Rated only for urgent maintenance at managed rental homes | | |
| Reputation | Local media coverage of a client losing closing funds; loss of lender or builder relationships | Client complaints or online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Closing and disbursement | High | 8 h | 4 h | 1 h |
| BP-02 Client and agent communications | High | 8 h | 4 h | 4 h |
| BP-03 Contract-to-close transaction management | High | 24 h | 8 h | 4 h |
| BP-04 Escrow deposit handling and reconciliation | Moderate | 72 h | 24 h | 24 h |
| BP-05 Property management operations | Moderate | 72 h | 24 h | 24 h |
| BP-06 Listing, marketing, and lead response | Moderate | 72 h | 24 h | 24 h |
| BP-07 Tenant screening and leasing | Low | 120 h | 72 h | 24 h |
| BP-08 Commission disbursement, payroll, and accounting | Low | 120 h | 72 h | 24 h |
| BP-09 Agent onboarding, offboarding, and license compliance | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- Closing dates drive BP-01. An MTD of 8 hours equals one closing day, about 2.5 closings. The 1-hour RPO reflects the disbursement ledger: after a restore, every wire released since the last good copy must be matched to the bank's records before more funds move.
- BP-02 is rated High for a reason specific to this business: when the official channel is down, clients look for another one, and fraudsters supply it. The runbook (P08) tells staff to phone clients and say that no wire instructions will be sent until the portal is back.
- BP-04 follows the 3-business-day deposit rule (r. 61J2-14.008(3)), so its MTD is 72 hours.

**Key findings:**
- The closing software vendor and the transaction platform vendor must meet the RTOs for BP-01 and BP-03. The transaction platform vendor's SOC 2 report (P09) states a 4-hour RTO and 1-hour RPO, which meets BP-03. The closing software vendor's commitments are **not yet documented**.
- The company-managed backups of the portal and integration service have **never been restore-tested**, and email has no independent backup, so the RTOs for BP-02 are unproven (risk R-006 in P01).
- A hurricane that closes the Main Office would stop BP-01 and BP-04 at once. A remote closing procedure is planned (R-022).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-02 Closing and escrow software | Settlement statements, disbursement ledger | BP-01 |
| SYS-08 Commercial online banking | Escrow and trust account wires, positive pay | BP-01, BP-04, BP-05, BP-08 |
| SYS-03 Identity provider | Single sign-on and MFA for employees | All |
| SYS-04 Productivity suite | Email, files, chat | BP-01, BP-02, BP-05, BP-06 |
| SYS-05 Closing Communications Portal | Verified delivery of wire instructions and closing documents | BP-01, BP-02 |
| SYS-01 Transaction management platform, SYS-11 e-signature | Contracts and deadlines | BP-03 |
| SYS-10 Property management platform | Rents, owner distributions, screening | BP-05, BP-07 |
| SYS-06 Office networks and internet | Main Office single ISP; Branch Office single ISP | All office work |
| People | Closing Services staff, Controller, transaction coordinators, property managers, IT Manager, MSP | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-03 Identity provider and break-glass accounts | 1 h | Two break-glass admin accounts stored offline (to be created) |
| 2 | SYS-08 Online banking access with dual approval | 1 h | Bank relationship manager and wire room by phone, with callback |
| 3 | SYS-02 Closing software | 4 h | Vendor-hosted; manual settlement statements from the last export |
| 4 | SYS-04 Email and the phone system | 4 h | Cell phones; phone tree |
| 5 | SYS-05 Closing Communications Portal | 4 h | Deliver wire instructions only in person or by phone with callback |
| 6 | SYS-01 Transaction management platform and SYS-11 e-signature | 8 h | Paper addenda; weekly export of active files (to be built) |
| 7 | SYS-10 Property management platform | 24 h | Urgent maintenance by phone; accept checks |
| 8 | SYS-09 CRM | 24 h | Route leads by email |
| 9 | SYS-12 Accounting and payroll | 72 h | Manual commission checks; repeat prior payroll |
