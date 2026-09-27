# Business Impact Analysis: Cris Santos Company | Finance and Insurance | Mid-Market

**Organization:** Cris Santos Company, Inc. (privately held bank holding company) and its subsidiary Cris Santos Bank, N.A. (regional commercial bank) | **Tier:** Mid-Market (600 employees; $2.5 billion in total assets) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Risk and Compliance Manager with the ISO, the CIO, and the process owners named in `bia.csv` | **Fieldwork:** 2026-06-29 to 2026-07-24 | **Approved:** Chief Operating Officer, 2026-09-18 (reviewed by the Board Risk Committee on 2026-09-15)

## 1. Overview and purpose
This BIA covers every business unit of the bank: retail banking (28 branches), digital banking, commercial banking and treasury management, payments operations (two wire rooms and ACH), correspondent services, lending and mortgage, deposit and loan operations, BSA/AML, finance and treasury, the contact center, and enterprise support. It rates 17 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and customer harm.

The results feed:
- the measures to protect against destruction, loss, or damage of customer information from environmental hazards or technological failures that the Interagency Guidelines require the bank to consider (12 CFR 30 App. B III.C.1.h; N52-R02), and the business continuity plan that implements them;
- the notification incident determination in the runbooks (P08): the BIA tells the ISO and the CEO which outages would disrupt services to "a material portion" of customers or a business line whose failure would cause material loss (12 CFR 53.2(b)(7));
- the FIPS 199 availability rating and contingency controls in the SSP for the Core and Online Banking Platform (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment of correspondent services (P09).

## 2. System and business description
The bank serves about 107,500 deposit customers from 22 Florida and 6 Georgia branches and 18 respondent institutions. Deposits, loans, and the general ledger run on a core banking system hosted by a core processor (SYS-01). Customers and staff move money through the Core and Online Banking Platform (COBP, P02): vendor-hosted online and mobile banking (SYS-02) and the payments hub and correspondent portal that the bank runs in its cloud landing zone (SYS-03, SYS-06), reached through the identity provider (SYS-05) from the operations center, the two wire rooms, and the branches (SYS-07). Cards and ATMs run through a card processor (SYS-11). Lending runs on a SaaS loan origination system (SYS-04) with the AI credit model in the landing zone (SYS-10). See `../00_company-facts.md` sections 1 to 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $105 million a year in net revenue, about $420,000 per business day. Net interest income keeps accruing during most outages, so the estimates use lost fee income (about $150,000 a business day in total, split by process in section 7 of the scenario facts), overtime, customer compensation (for example, interest claims on late wires), and exposure to fraud and liquidity costs.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per event) | More than $250,000, or more than $50 million of customer payments delayed past settlement | $50,000 to $250,000 | Less than $50,000 |
| Operations | A business unit cannot deliver its core service (all branches, all wires, correspondent services) | One service line or a group of branches stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory | Event that may be a notification incident under 12 CFR Part 53, requires customer notice under Supplement A, or requires outbound 53.4 notices to respondent banks | A missed filing or settlement deadline (SAR, Call Report, ACH settlement, Regulation B notice) | Internal policy deviation |
| Customer harm (recorded in the `impact_safety` and `customer_harm_impact` columns) | Customers lose funds or cannot reach their money for payroll, closings, or benefits | Customer payments delayed but completed the same week | None |
| Reputation | Regional media coverage, loss of respondent institutions, or loss of treasury management customers | Customer complaints or online reviews | Internal only |

The bank has no processes that affect physical safety, so the template's Safety column records customer financial harm instead.

**How loss at MTD was estimated.** Estimated loss at MTD is lost fee income plus overtime and expected customer compensation over the process's MTD, from process owner estimates. Payments delayed are shown separately in the `quantified_operational_impact` column because they are timing, not loss, unless settlement is missed.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 Outgoing and incoming wire transfers | Payments Operations | High | 8 | 4 | 0.25 | $85,000 |
| 2 | BP-02 Correspondent wire and ACH processing | Correspondent Services | High | 8 | 4 | 0.25 | $60,000 |
| 3 | BP-03 Branch teller and deposit services | Retail Banking | High | 8 | 4 | 1 | $70,000 |
| 4 | BP-08 Contact center, fraud line, and phones | Customer Contact Center | Moderate | 24 | 4 | 24 | $15,000 |
| 5 | BP-05 ACH origination and receipt | Payments Operations | High | 24 | 8 | 1 | $45,000 |
| 6 | BP-04 Online and mobile banking | Digital Banking | High | 12 | 6 | 1 | $40,000 |
| 7 | BP-13 General ledger, liquidity, and regulatory reporting | Finance and Treasury | Moderate | 24 | 8 | 4 | $40,000 |
| 8 | BP-14 Check and item processing | Deposit Operations | Moderate | 24 | 12 | 4 | $35,000 |
| 9 | BP-06 Treasury management services | Treasury Management | Moderate | 24 | 12 | 4 | $25,000 |
| 10 | BP-07 Debit card and ATM services | Deposit Operations | Moderate | 24 | 8 | 1 | $30,000 |
| 11 | BP-09 Loan servicing and payments | Loan Operations | Moderate | 24 | 12 | 4 | $20,000 |
| 12 | BP-15 Account opening and maintenance | Retail Banking | Moderate | 48 | 24 | 4 | $15,000 |
| 13 | BP-10 Loan origination (including AI-001) | Lending | Moderate | 72 | 48 | 24 | $60,000 |
| 14 | BP-11 Mortgage origination and closing | Mortgage Lending | Moderate | 72 | 48 | 24 | $50,000 |
| 15 | BP-12 BSA/AML monitoring and SAR filing | BSA/AML | Moderate | 72 | 48 | 24 | $25,000 |
| 16 | BP-16 Payroll and HR | Enterprise | Low | 120 | 72 | 24 | $20,000 |
| 17 | BP-17 Data warehouse and reporting | Enterprise | Low | 168 | 120 | 24 | $10,000 |

**Summary:** 5 High, 10 Moderate, and 2 Low processes (17 in total). The sum of estimated losses at each process's MTD is $645,000.

**Enterprise-wide scenario (core processor down for 72 hours).** The core supports 12 of the 17 processes. A 72-hour core outage would cost about $850,000 in lost fees, overtime, and customer compensation, and would delay about $500 million of customer and respondent payments. It would almost certainly be a notification incident for the bank and the holding company, and the bank would owe notices to its bank respondents (P08 `ir-runbook-core-outage.md`). Response and notification costs come on top (P01 R-003).

**What drives the values:**
- **Wires and correspondent payments (BP-01, BP-02)** carry about $165 million a day. A wire that settles without a matching bank record risks a duplicate or lost payment, so the RPO is 15 minutes. After 8 hours, same-day settlement is missed for every pending wire.
- **Branch services (BP-03)** depend on the core. The core processor's offline teller mode lets branches keep taking deposits and paying limited withdrawals for part of a day, which is why the MTD is 8 hours.
- **Phones (BP-08)** have a 4-hour RTO although the process is Moderate, because the wire callback and the fraud line need working phones. Without callbacks, the bank must stop accepting wire requests by email or phone.
- **Account maintenance (BP-15)** is Moderate for availability but important for integrity: an unverified contact change can redirect the wire callback to an attacker (gap 2; P08).
- **Lending and BSA (BP-10 to BP-12)** have deadlines counted in days, so 72 hours of downtime is tolerable if no data is lost.

## 5. Key findings
1. **Core processor commitments meet the BIA, but only in the SOC report.** The core processor's SOC 2 system description states an RTO of 4 hours and an RPO of 15 minutes, which meets the BIA for BP-03, BP-07, and BP-09. The contract sets no recovery time or incident notice terms, so the commitment is not enforceable until the 2027 renewal (P01 R-003; P09 `vendor-soc2-review.csv`).
2. **Bank-run payments recovery is unproven.** The payments hub and correspondent portal failover to the second region took 9 hours in the only test (2025) against the 4-hour RTO for BP-01 and BP-02 (gap 6; P01 R-004; P07 CP-4). The secondary wire room has been exercised only for customer wires, not correspondent processing.
3. **Correspondent services have no recovery commitment.** The respondent agreements promise only "commercially reasonable" availability. Respondents cannot rely on the 4-hour RTO this BIA sets, and the bank has no procedure for its own 53.4 notices to them (gap 12; P08; P09).
4. **Legacy item processing servers are a single point of failure.** BP-14 runs on 14 unsupported servers in the headquarters server room. They are backed up nightly but have no tested rebuild procedure (gap 10; P01 R-014).
5. **Phones and contact data are part of payment integrity.** BP-08 and BP-15 look Moderate on availability, but the wire callback depends on both working phones and trustworthy numbers on file.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Core banking system | System of record for deposits, loans, and the general ledger; hosted by the core processor | BP-01 to BP-03, BP-05 to BP-07, BP-09, BP-12 to BP-15 |
| SYS-02 Online and mobile banking | Vendor-hosted; business wire, ACH, and positive pay | BP-04, BP-05, BP-06 |
| SYS-03 Payments hub and correspondent portal | Bank-run in the production account; 4 payments workstations | BP-01, BP-02, BP-05 |
| SYS-05 Identity provider | Workforce SSO and MFA; customer identity service for the correspondent portal | All |
| SYS-06 Cloud landing zone | Production, backup (second region), security and log archive, shared network accounts | BP-01, BP-02, BP-05, BP-10, BP-13, BP-17 |
| SYS-07 Networks, server room, and endpoints | 28 branches and 2 operations sites on SD-WAN; about 60 servers (item processing, directory, file shares); 640 endpoints | All |
| SYS-11 and SYS-08 Card processing and ATMs | Card processor authorization and stand-in; 58 ATMs and interactive teller machines | BP-03, BP-07 |
| SYS-04 and SYS-10 Lending systems | LOS; credit decisioning service | BP-10, BP-11 |
| SYS-13 AML monitoring | Vendor SaaS with alert scoring | BP-12 |
| SYS-09 Productivity suite and phones | Email, files, main phone lines, contact center platform | BP-08, BP-16 |
| Facilities | Headquarters campus (operations center, primary wire room, server room); Georgia regional office (alternate operations site, secondary wire room) | BP-01, BP-02, BP-05, BP-13, BP-14 |
| People | 14 primary and 4 secondary wire room staff; 9 correspondent operations staff; tellers and universal bankers; IT (38) and information security (4); MSSP | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 identity provider and break-glass accounts | 1 h | Sealed break-glass accounts for the identity provider, the cloud management account, and the payments hub |
| 2 | SYS-07 SD-WAN, operations site networks, and circuits to the core processor | 2 h | Cellular backup at each branch; dual circuits at both operations sites |
| 3 | SYS-06 production account network, then SYS-03 payments hub and correspondent portal | 4 h | Failover to the second region (**9 hours in the 2025 test**); secondary wire room with 2 payments workstations |
| 4 | SYS-01 core banking (core processor) | 4 h | Core processor's secondary data center (stated RTO 4 h, RPO 15 min); offline teller mode |
| 5 | Phones, contact center, and SYS-09 email | 4 h | Forward lines to cell phones; callbacks from branch cell phones to the number on file |
| 6 | SYS-02 online and mobile banking | 6 h | Provider recovery; branches and contact center; business wire requests to relationship managers with callback |
| 7 | SYS-07 item processing servers | 12 h | Restore from the backup appliance; transport paper items to the item processing provider |
| 8 | SYS-11 card processing and SYS-08 ATMs | 8 h | Card processor stand-in authorization |
| 9 | SYS-12 SIEM and EDR console | 8 h | MSSP runs from its own platform; needed to confirm a clean recovery |
| 10 | SYS-13 AML monitoring | 48 h | Manual review of large cash and wire activity from core reports |
| 11 | SYS-04 LOS and SYS-10 credit decisioning service | 48 h | Paper applications and manual underwriting |
| 12 | Payroll SaaS | 72 h | Repeat the prior payroll |
| 13 | SYS-06 data warehouse | 120 h | Core standard reports |
