# Business Impact Analysis: Cris Santos Company Holdings | Real Estate | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees plus about 52,000 contractor sales associates) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads and the Group Treasurer | **Fieldwork:** 2026-05-04 to 2026-07-24 | **Approved:** board risk committee, 2026-09-17

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on: identity (SYS-G1), the SOC (SYS-G2), the cloud platform and Group Data Platform (SYS-G3), email and collaboration (SYS-G4), the treasury and payments hub (SYS-G5), finance, and HR.
- **Division BIAs:** Residential Brokerage (focus), Mortgage and Title, and Homebuilding. They are kept as rows in one workbook (`bia.csv`, `division` column) so that cross-division dependencies are visible in one place. A residential sale often touches all three divisions in a single day.

It supports:
- the availability rating of the Transaction Management and Closing Communications System (TMCC) in the SSP (P02) and the impact ratings in the risk registers (P01);
- the recovery order in the incident runbook (P08);
- the incident response plans of Home Loans and Title under the FTC Safeguards Rule (16 CFR 314.4(h)), which must address how the institutions respond to and recover from security events;
- the Availability and Processing Integrity criteria in Title's SOC 2 readiness work (P09).

## 2. System and business description
Three divisions share corporate services. The division systems are SYS-B1 to SYS-B4 (Residential Brokerage), SYS-M1 and SYS-M2 (Mortgage and Title), and SYS-H1 to SYS-H3 (Homebuilding). See `../00_company-facts.md` sections 3 and 7.

The flow that matters most is the residential closing:
1. A contract is signed in the transaction platform (SYS-B1, brokerage) or the Homebuilding sales platform (SYS-H2).
2. Title opens the order and prepares the settlement statement (SYS-M2); Home Loans underwrites and funds the loan (SYS-M1).
3. Wire instructions reach the buyer only through the Closing Communications Portal (SYS-B2).
4. Funds are received and disbursed from title escrow trust accounts through the treasury and payments hub (SYS-G5).

Title closes about 510 transactions and sends about 2,560 disbursement wires (about $208 million) per business day.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 1. Per business day (about 250 a year): Homebuilding about $32 million, Residential Brokerage about $30 million (gross commission income), and Mortgage and Title about $10 million. Funds in motion are far larger than revenue: about $208 million a day leaves title escrow trust accounts.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, more than 1 day of a division's revenue, or any loss of customer funds above the $10 million insurance sublimit | $1 million to $25 million | Less than $1 million |
| Operations | A division cannot close, fund, or disburse; or closings stop in a state | One region, line, or service stops | Staff slowed but working |
| Regulatory | Missed trust fund duty (Fla. Stat. 626.8473(4) worked example), escrow deposit deadline, disclosure deadline, or a reportable breach or SEC disclosure | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Plausible physical harm (jobsite, smart lock, or home access) | Delayed but safe | None |
| Reputation | National media, lender or investor relationship at risk, or regulator attention | Regional media or client complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 29 processes: 8 group shared services, 8 Residential Brokerage, 7 Mortgage and Title, and 6 Homebuilding. 12 are High, 14 Moderate, and 3 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce and agent identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G04 Cloud landing zones and hub network | Group | High | 4 h | 2 h | 1 h |
| BP-G03 Treasury and payments hub (wire and ACH release, positive pay, payee verification) | Group | High | 4 h | 2 h | 1 h |
| BP-G05 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-G02 Email and collaboration | Group | High | 8 h | 4 h | 1 h |
| BP-MT01 Closing and disbursement of funds | Mortgage and Title | High | 8 h | 4 h | 1 h |
| BP-BR02 Wire instruction delivery and closing communications | Brokerage | High | 8 h | 4 h | 1 h |
| BP-BR01 Contract-to-close transaction management | Brokerage | High | 8 h | 4 h | 1 h |
| BP-MT04 Underwriting and loan funding | Mortgage and Title | High | 8 h | 4 h | 1 h |
| BP-MT02 Title production and settlement statements | Mortgage and Title | High | 24 h | 8 h | 4 h |
| BP-MT03 Loan origination, disclosures, and rate locks | Mortgage and Title | High | 24 h | 8 h | 4 h |
| BP-BR03 Earnest money escrow deposits, refunds, and reconciliation | Brokerage | High | 24 h | 8 h | 4 h |
| BP-MT07 Borrower point-of-sale portal and applications | Mortgage and Title | Moderate | 24 h | 12 h | 4 h |
| BP-MT06 Title escrow trust account reconciliation | Mortgage and Title | Moderate | 48 h | 24 h | 24 h |
| BP-HB03 New-home sales, contracts, and buyer deposits | Homebuilding | Moderate | 48 h | 24 h | 4 h |
| BP-HB04 Home completion, closing readiness, and handover | Homebuilding | Moderate | 48 h | 24 h | 4 h |
| BP-BR04 Agent onboarding and offboarding | Brokerage | Moderate | 48 h | 24 h | 24 h |
| BP-BR05 Listing, CRM, and lead management | Brokerage | Moderate | 72 h | 24 h | 4 h |
| BP-BR06 Property management rent collection and owner distributions | Brokerage | Moderate | 72 h | 24 h | 4 h |
| BP-BR07 Tenant screening and leasing | Brokerage | Moderate | 48 h | 24 h | 24 h |
| BP-HB01 Construction scheduling and purchasing | Homebuilding | Moderate | 72 h | 24 h | 4 h |
| BP-HB02 Trade partner payments | Homebuilding | Moderate | 72 h | 48 h | 24 h |
| BP-MT05 Loan sale and investor delivery | Mortgage and Title | Moderate | 72 h | 48 h | 24 h |
| BP-G06 Group Data Platform analytics and reporting | Group | Moderate | 72 h | 24 h | 4 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-G08 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-BR08 Relocation services | Brokerage | Low | 120 h | 72 h | 24 h |
| BP-HB05 Warranty service and smart-home device management | Homebuilding | Low | 120 h | 72 h | 24 h |
| BP-HB06 Design studio selections and card deposits | Homebuilding | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Same-day closings** drive the 8-hour MTDs for disbursement (BP-MT01), wire instruction delivery (BP-BR02), contract-to-close (BP-BR01), and funding (BP-MT04). A closing missed by a day costs rate locks, moving dates, and sometimes the sale.
- **The fallback is the threat.** When the Closing Communications Portal (SYS-B2) is down, staff are tempted to send wire instructions by email, which is exactly what business email compromise exploits. The BIA therefore sets the portal's RTO at 4 hours and forbids email instructions as a workaround: instructions are read by phone from a verified number only.
- **Trust fund and escrow duties** drive BP-MT01, BP-MT06, and BP-BR03. Title trust funds may be used only as the closing instructions allow (Fla. Stat. 626.8473(4), worked example), and brokers must place deposits in escrow by the end of the third business day (Fla. Admin. Code r. 61J2-14.008(3), worked example). Reconciliation can wait a day; disbursement cannot.
- **Homebuilding is schedule-driven, not hour-driven.** Construction, trade payments, and warranty can absorb 2 to 5 days because work is planned days ahead. Its closings depend on Title and Home Loans, not on its own systems.
- **Integrity outweighs availability for the money processes.** The treasury hub (BP-G03) has a 2-hour RTO, but recovery must restore payee verification and dual approval before any release. A fast recovery that skips them would move the risk, not reduce it.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all three divisions at once. Break-glass accounts per critical system and bank-token wire release by two officers are the fallbacks |
| Treasury and payments hub (SYS-G5) | Group | Title disbursements, brokerage escrow, owner payouts, trade partner payments, agent commissions | One hub moves every division's money. It is also the place where payee verification should be enforced for every division (scenario gap 2) |
| Email (SYS-G4) | Group | All divisions; about 52,000 contractor agents | The main business email compromise target. Recovery restores mail-flow security rules before mailboxes |
| SOC facts (SYS-G2) | Group | Every notice in P08; SEC disclosure | Notice clocks for two financial institutions, many states, and the SEC depend on the SOC establishing what happened |
| Closing Communications Portal (BP-BR02) | Brokerage | Title closings (BP-MT01) | Title owns the wire instructions; the brokerage runs the portal. Title is co-data owner |
| Title closings (BP-MT01) | Mortgage and Title | Brokerage commissions; Homebuilding closings (BP-HB04); Home Loans fundings | 58% of Title's closings are brokerage transactions and 15% are Homebuilding closings |
| Home Loans funding (BP-MT04) | Mortgage and Title | Homebuilding closings | About 78% of Homebuilding buyers finance with Home Loans |
| Lead and file transfers | Brokerage and Homebuilding | Home Loans (SYS-M1) | Affiliate referrals by API from SYS-B3 and SYS-H2 (scenario gap 4). Not time-critical, but a data protection concern |
| Title production vendor (SYS-M2) | Third party | BP-MT01, BP-MT02, BP-MT06 | The vendor contract states an RTO of 12 hours; the BIA needs 8 hours for title production and 4 hours for disbursement support |

**Single points of failure found:**
1. **SYS-G1 identity:** mitigated by break-glass accounts, tested quarterly.
2. **The SYS-G5 bank connectivity gateway:** one vendor connects all 6 banks. Bank portals with hardware tokens are the fallback, but only Title has rehearsed them (P01 GR-08).
3. **The title production vendor's RTO (12 hours) exceeds the BIA RTO for title production (8 hours).** The contract is due for renewal in 2027 (P01 MT-008; POAM in P07).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones (providers A and B) | TMCC, SYS-G5, Homebuilding ERP, Group Data Platform | Infrastructure as code; immutable backups in provider B |
| SYS-G5 treasury and payments hub | BP-G03, BP-MT01, BP-MT04, BP-BR03, BP-BR06, BP-HB02 | Hub database replicated to provider B; bank files retained at the banks; paper callback logs as fallback |
| SYS-B2 portal and TMCC integration service | BP-BR02, BP-MT01 | Database replication to the provider B warm standby (RPO 15 minutes) |
| SYS-B1 transaction platform (SaaS) | BP-BR01 | Vendor replication; nightly read-only export of open files to the group backup vault |
| SYS-M2 title production (vendor-hosted) | BP-MT01, BP-MT02, BP-MT06 | Vendor backups (contract RPO 1 hour, RTO 12 hours) |
| SYS-M1 loan origination (SaaS) | BP-MT03, BP-MT04, BP-MT05, BP-MT07 | Vendor replication; daily export to the group backup vault |
| SYS-H1 Homebuilding ERP | BP-HB01, BP-HB02 | Immutable backups in provider B; restore test once a year |
| People | All | Title closers can work from any office or remotely; 2 disbursement centers back each other up |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones and hub network
3. Treasury and payments hub, with payee verification and dual approval restored first
4. SOC visibility (SIEM and EDR)
5. Email and collaboration, with mail-flow security rules restored before mailboxes
6. to 9. Title closing and disbursement, wire instruction delivery (SYS-B2), contract-to-close (SYS-B1), and loan funding
10. to 13. Title production, loan origination, brokerage escrow, and the borrower portal
14. to 29. Title reconciliation, Homebuilding sales and handover, agent onboarding and offboarding, CRM, property management, tenant screening, construction, trade payments, loan sales, the Group Data Platform, financial close, payroll, relocation, warranty and smart-home, and design studios.

## 8. Key findings
1. **Money moves through one hub, but payee verification does not.** Title verifies payees out of band; the brokerage and Homebuilding do not for several payment types (scenario gap 2). The BIA rates SYS-G5 as the third recovery priority so that, when it comes back, it comes back with the same controls for every division.
2. **The Closing Communications Portal's availability is a security control.** Every hour it is down pushes staff toward email. Its 4-hour RTO was met in the 2026-06 failover test to provider B.
3. **The title production vendor cannot meet the BIA RTO** (12 hours against 8). Title has a manual commitment process for urgent files, but disbursement reconciliation (BP-MT06) depends on the vendor's ledger.
4. **Homebuilding recovers more slowly by design** and that is acceptable, except for trade partner payments, where bank account changes accepted by email are the real risk (P01 HB-001), not downtime.
5. **Notification capacity is itself a process** (BP-G05, BP-G07). If the SOC or the disclosure team is down during an incident, the FTC, state, and SEC clocks keep running. The P08 runbook uses out-of-band channels for this reason.
