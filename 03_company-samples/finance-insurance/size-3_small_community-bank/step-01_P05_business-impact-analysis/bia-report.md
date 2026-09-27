# Business Impact Analysis: Cris Santos Company | Finance and Insurance | Small

**Organization:** Cris Santos Bank, N.A. (community commercial bank; subsidiary of Cris Santos Company, a bank holding company) | **Tier:** Small (120 employees; $510 million in total assets) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Information Security Officer) with the COO, Deposit Operations Manager, Treasury Management Officer, Chief Credit Officer, Chief Financial Officer, and BSA/AML Officer, during fieldwork 2026-07-13 to 2026-07-24 | **Approved:** President and CEO, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the bank depends on, how long each can be down, and how much data each can lose. It supports:
- the measures to protect against destruction, loss, or damage of customer information from environmental hazards or technological failures that the Interagency Guidelines require the bank to consider (12 CFR 30 App. B III.C.1.h; N52-R02), and the business continuity plan that implements them;
- the availability rating in the SSP for the Wire and Digital Banking Platform (P02);
- impact ratings in the risk register (P01), especially R-003, R-010, and R-014;
- the recovery order in the incident response runbook (P08);
- the availability commitments checked in the core processor SOC report review (P09).

## 2. System and business description
The bank serves about 16,000 deposit customers from six Florida branches. The main office (Branch 1) also houses the operations center and the wire room. Deposits, loans, and the general ledger run on a core banking system hosted by a core processor (SYS-01). Customers and staff move money through the Wire and Digital Banking Platform (WDBP, P02): vendor-hosted online and mobile banking (SYS-02) and a vendor-hosted wire and ACH platform (SYS-03), reached from bank endpoints through the identity provider (SYS-05). Cards and ATMs run through a card processor (SYS-11). Lending runs on a SaaS loan origination system (SYS-04) with the AI credit model pilot (SYS-10) in the bank's cloud tenant (SYS-06). See `../00_company-facts.md` sections 1 to 4.

## 3. Impact categories and values
Dollar values are scaled to about $20 million a year in net revenue (fictional), about $80,000 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (direct loss and lost revenue) | More than $250,000 (about 3 business days of net revenue, or one large fraudulent wire) | $50,000 to $250,000 | Less than $50,000 |
| Operations | All branches cannot serve customers, or no wires can be sent | One branch or one service line stops | Staff slowed but working |
| Regulatory | Event that may be a notification incident under 12 CFR Part 53, or that requires customer notice under Supplement A | A missed filing or settlement deadline (SAR, Call Report, ACH settlement) | Internal policy deviation |
| Customer harm (recorded in the `impact_safety` column) | Customers lose funds or cannot reach their money for payroll, closings, or benefits | Customer payments delayed but completed the same week | None |
| Reputation | Regional media coverage, or loss of business treasury management customers | Customer complaints or online reviews | Internal only |

The bank has no processes that affect physical safety, so the template's Safety column records customer financial harm instead.

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Outgoing and incoming wire transfers | High | 8 h | 4 h | 15 min |
| BP-02 Branch teller and deposit account services | High | 8 h | 4 h | 1 h |
| BP-03 Online and mobile banking | High | 24 h | 8 h | 1 h |
| BP-04 ACH origination and receipt | High | 24 h | 8 h | 1 h |
| BP-05 Debit card and ATM services | Moderate | 24 h | 8 h | 1 h |
| BP-06 Loan servicing and payments | Moderate | 24 h | 8 h | 1 h |
| BP-07 Loan origination and underwriting | Moderate | 72 h | 48 h | 24 h |
| BP-08 BSA/AML monitoring and SAR filing | Moderate | 72 h | 48 h | 24 h |
| BP-09 General ledger, liquidity, and regulatory reporting | Moderate | 24 h | 8 h | 4 h |
| BP-10 Customer service, phones, and email | Moderate | 24 h | 4 h | 24 h |
| BP-11 Payroll and HR | Low | 120 h | 72 h | 24 h |

Totals: 11 processes, 4 High, 6 Moderate, 1 Low.

**What drives the values:**
- **Wires (BP-01)** carry about $4 million a day, and business customers use them for real estate closings and payroll. A wire that settles without a matching bank record risks a duplicate or lost payment, so the RPO is 15 minutes. An MTD of 8 hours is one business day: after that, same-day settlement is missed for every pending wire.
- **Branch services (BP-02)** depend entirely on the core. The core processor's offline teller mode lets branches keep taking deposits and paying limited withdrawals for part of a day, which is why the MTD is 8 hours rather than less.
- **Phones (BP-10)** have a short RTO (4 hours) even though the process is Moderate, because the wire callback standard needs working phones. Without callbacks, the bank must stop accepting wire requests by email or phone (P08).
- **Loan origination and BSA (BP-07, BP-08)** have deadlines counted in days (Regulation B notice timing, SAR and currency transaction report filing), so 72 hours of downtime is tolerable if no data is lost.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Core banking system | System of record for deposits, loans, general ledger, and the AML monitoring module; hosted by the core processor | BP-01, BP-02, BP-04, BP-05, BP-06, BP-08, BP-09 |
| SYS-02 Online and mobile banking | Vendor-hosted; business wire and ACH initiation | BP-03, BP-04 |
| SYS-03 Wire and ACH platform | Vendor-hosted; 2 payments workstations and 5 wire-room PCs | BP-01, BP-04 |
| SYS-05 Identity provider | Single sign-on and MFA for the admin console, wire platform, LOS, and cloud tenant | BP-01, BP-03, BP-07 |
| SYS-07 Branch networks and endpoints | Six branch networks, SD-WAN, private circuits to the core processor, 110 endpoints including 34 teller workstations | All |
| SYS-11 and SYS-08 Card processing and ATMs | Card processor authorization and stand-in; 9 ATMs | BP-05 |
| SYS-04, SYS-06, SYS-10 Lending systems | LOS, credit decisioning service, reporting data warehouse | BP-07, BP-08, BP-09 |
| SYS-09 Productivity suite and phone service | Email, files, main phone lines | BP-10, BP-11 |
| Facilities | Main office (operations center and wire room); Branch 4 as the designated alternate wire and operations site (R-014) | BP-01, BP-04, BP-09 |
| People | 9 staff on the wire room access list; tellers and universal bankers; deposit and loan operations; IT Manager and 2 IT specialists; MSSP | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 Identity provider and break-glass accounts | 1 h | Sealed break-glass administrator accounts. The cloud tenant has one today; POL-02 requires them for the admin console and the wire platform |
| 2 | SYS-07 Branch networks, SD-WAN, and circuits to the core processor | 2 h | Cellular backup at each branch; core processor offline teller mode |
| 3 | SYS-01 Core banking (core processor) | 4 h | Core processor's secondary data center (stated RTO 4 h, RPO 15 min; P04, P09); offline teller mode at branches |
| 4 | SYS-03 Wire platform and payments workstations | 4 h | Alternate wire procedure; spare payments workstation at Branch 4 (**untested since 2023**, R-010) |
| 5 | Phones and SYS-09 email | 4 h | Forward main lines to cell phones; callbacks from branch cell phones to the number on file |
| 6 | SYS-02 Online and mobile banking | 8 h | Provider recovery; branches and phone banking; business wire requests to branches with callback |
| 7 | SYS-11 Card processing and SYS-08 ATMs | 8 h | Card processor stand-in authorization |
| 8 | SYS-06 Reporting data warehouse and AML reports | 48 h | Restore from the backup vault; manual review of large cash and wire activity from core reports |
| 9 | SYS-04 LOS and SYS-10 AI credit model | 48 h | Paper applications and manual underwriting |
| 10 | Payroll SaaS | 72 h | Repeat the prior payroll |

## 7. Key findings
1. **Core processor commitments meet the BIA.** The core processor's SOC 2 system description states an RTO of 4 hours and an RPO of 15 minutes (P04; reviewed in P09 on 2026-08-20). That meets the 4-hour RTO and 1-hour RPO for BP-02 and BP-06. The contract, however, sets no recovery time or incident notice terms, so the commitment is not enforceable until the 2027 renewal (R-003).
2. **The wire alternate procedure is unproven.** The 8-hour MTD for wires depends on the alternate wire procedure and the spare payments workstation at Branch 4. Neither has been tested since 2023 (gap 10; R-010; first semiannual test 2026-11-12).
3. **Single site for wires and operations.** The operations center and the wire room share the main office building. A hurricane or building loss would stop BP-01, BP-04, and BP-09 at once. Branch 4 is designated as the alternate site (R-014, due 2027-05-31).
4. **Other providers not yet checked.** The recovery commitments of the digital banking provider and the payments service provider have not been compared with these RTOs and RPOs. Their SOC reports are due for review by 2026-11-30 (P02 SR-6).
5. **Bank-managed backups share the production account.** The backup vault in the cloud tenant holds the data warehouse, the decisioning service, and monthly wire configuration exports. It is in the same account as production and is not immutable, so the 48-hour RTO for BP-07 and BP-08 is at risk in a ransomware event (R-004).
