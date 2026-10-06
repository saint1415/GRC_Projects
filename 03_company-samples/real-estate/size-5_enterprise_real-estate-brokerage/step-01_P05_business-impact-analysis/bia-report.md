# Business Impact Analysis: Cris Santos Company | Real Estate and Rental and Leasing | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded residential real estate brokerage with title and settlement, property management, and relocation lines; 9 states) | **Tier:** Enterprise (12,000 employees; about 38,000 contractor agents) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer, President of Title and Escrow, and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and acquired firms. It feeds:
- the availability rating and recovery objectives in the TMCC System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the "identify and manage the data, personnel, devices, systems, and facilities" element of Title and Escrow's Safeguards Rule program (16 CFR 314.4(c)(2));
- the recovery order in the BEC runbook (P08), where a Hub outage is treated as a fraud risk, not only a delay;
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 18 processes were analyzed; 7 are High criticality, 10 Moderate, and 1 Low. 3 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 24 dependencies, 14 of them single points of failure and 5 never tested.

## 2. System and business description
Cris Santos Company runs about 410 sales offices in 9 states, and Title and Escrow runs about 140 closing offices. The company has 12,000 employees, about 38,000 contractor agents, and about $4.8 billion in annual revenue. It closes about 840 transaction sides and about 350 title closings per business day, and sends about 1,520 outgoing wires (about $136 million) a day from 31 title escrow trust accounts. The technology estate is described in `../00_company-facts.md` section 3: two vendor platforms that carry the transaction and the closing (SYS-01, SYS-02), the company-built Closing Communications Hub and Disbursement Hub (SYS-03, SYS-04), an identity platform (SYS-05), a productivity suite with three legacy tenants at acquired brokerages (SYS-06), a multi-cloud estate with two colocation data centers (SYS-07), and property management, CRM, ERP, and relocation platforms (SYS-10 to SYS-13). Nine brokerages and title agencies were acquired in 2024-2026; four are not yet fully integrated (AQ-06 to AQ-09).

## 3. Impact categories and values
Dollar thresholds are scaled to about $19.2 million of revenue per business day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Closings or disbursements stop in more than one state, or more than 100 offices cannot transact | One state, one business line, or up to 100 offices stop | Staff slowed but working |
| Regulatory | Trust fund handling outside closing instructions; FTC or state notice event of 500 or more; missed SEC filing; license action | Missed contractual or documentation deadline; notice event under 500 | Internal policy deviation |
| Safety | Tenants without emergency repairs (habitability) | Delayed but safe service | None |
| Reputation | National media, analyst or ratings action, or loss of lender, homebuilder, or corporate clients | Regional media; client complaints | Internal only |

Safety is rated N/A for processes that cannot affect anyone's physical safety.

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-05 Closing funds disbursement | High | 4 h | 2 h | 15 min | $3.10M |
| BP-04 Closing and settlement statement preparation | High | 8 h | 4 h | 15 min | $1.64M |
| BP-06 Closing communications and wire instruction delivery | High | 8 h | 4 h | 15 min | $0.80M |
| BP-07 Payoff and lien verification | High | 24 h | 8 h | 1 h | $0.40M |
| BP-01 Contract-to-close transaction management | High | 24 h | 8 h | 1 h | $2.40M |
| BP-02 Earnest money deposit receipt and escrow accounting | High | 24 h | 8 h | 1 h | $0.30M |
| BP-18 Closing operations at AQ-09 (legacy closing software) | High | 8 h | 6 h | 15 min | $0.15M |
| BP-03 Title search, commitment, and policy issuance | Moderate | 48 h | 24 h | 1 h | $0.90M |
| BP-08 Listing management and consumer website and app | Moderate | 48 h | 12 h | 4 h | $0.60M |
| BP-09 Lead management and agent routing | Moderate | 48 h | 24 h | 4 h | $0.50M |
| BP-12 Rent collection and owner distributions | Moderate | 72 h | 24 h | 4 h | $0.30M |
| BP-13 Leasing and tenant screening | Moderate | 48 h | 24 h | 4 h | $0.15M |
| BP-14 Maintenance requests and emergency dispatch | Moderate | 24 h | 8 h | 4 h | $0.10M |
| BP-15 Corporate relocation services (SL-2) | Moderate | 48 h | 24 h | 4 h | $0.40M |
| BP-11 Agent commission calculation and payout | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-17 Payroll | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-16 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-10 Agent onboarding, licensing compliance, and offboarding | Low | 72 h | 24 h | 24 h | $0.05M |

**What drives the values:**
- **Money movement sets the shortest MTD.** Disbursement (BP-05) has a 4-hour MTD because lenders, sellers, and buyers expect same-day funding and banks close their wire windows in the afternoon. Funds are delayed, not lost, so the dollar impact is per diem interest, extension costs, and credits.
- **An outage of the Closing Communications Hub (BP-06) is a fraud risk, not only a delay.** When the Hub is down, parties fall back to email and phone, which is exactly how altered wire instructions reach buyers (P01 R-001). The workaround therefore forbids email instructions entirely.
- **Contract deadlines, not cash, drive the transaction platform (BP-01).** Commission income is deferred, not lost, for a day or two, but contract deadlines and lost deals make a multi-day vendor outage Severe.
- **Regulation tightens deposit handling (BP-02)** through each state's escrow deadlines (Florida worked example: the end of the third business day, r. 61J2-14.008(3)), and tightens financial close (BP-16) at quarter-end because of SEC filing deadlines.
- **Contracts set the relocation (BP-15) and settlement services objectives,** because business clients rely on them (P09).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Transaction platform concentration (DEP-01).** One vendor platform carries 100% of brokerage transactions. Its contract RTO is 24 hours against a BIA RTO of 8 hours, and the company has never tested working without it. A 3-day outage would defer about $7 million of company impact and put contract deadlines at risk across 9 states. This is P01 risk R-033 and POA&M item POAM-007.
2. **Disbursement Hub recovery (DEP-04).** The Hub met its RPO but recovered in 6.5 hours in the 2026-05-16 DR test, against a 2-hour process RTO for BP-05 and a 4-hour system RTO. Bank portals can carry about 150 urgent wires a day by hand, which is 10% of normal volume. This is P01 R-025 and POAM-011.
3. **Acquired firms (DEP-08, DEP-09).** AQ-06 to AQ-08 run their own email tenants without the enterprise email security stack or SIEM audit feeds. AQ-09 runs legacy closing software with nightly backups, so its real RPO is 24 hours against a 15-minute target, and its trust account wires need only one approver below $100,000. Neither restore has been tested.
4. **Verification providers (DEP-10, DEP-11).** Payee bank account verification covers about 86% of disbursements; the rest depends on manual callbacks. Consumer sign-in to the Hub relies on one-time codes sent by email, the channel an attacker may already control.
5. **Bank channels (DEP-05).** Five trust banks give real alternatives, but P07 testing found bank API client secrets stored as pipeline variables (POAM-010).
6. **Industry-wide dependencies (DEP-14).** County recording portals cannot be replaced; the workaround is procedural.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Transaction management platform | Vendor SaaS system of record for transactions | BP-01, BP-02, BP-11 |
| SYS-02 Title production and closing platform | Vendor SaaS for title, settlement statements, disbursement ledger | BP-03, BP-04, BP-05, BP-07 |
| SYS-03 Closing Communications Hub | Company-built portal on Cloud provider A | BP-04, BP-06, BP-07 |
| SYS-04 Disbursement Hub | Company-built payment service on Cloud provider A | BP-05 |
| SYS-05 Identity platform | SSO, MFA, PAM, identity governance | All |
| SYS-06 Productivity suite | Email, files, chat; three legacy tenants at AQ-06 to AQ-08 | BP-01, BP-04, BP-06, BP-07 |
| SYS-07 Cloud provider A, Cloud provider B, DC-1, DC-2 | TMCC workloads; consumer channels and data; network core and offline backups | All |
| SYS-08 Enterprise network | SD-WAN at about 550 offices with cellular failover at closing offices | All office-based processes |
| SYS-10 to SYS-13 | Property management, CRM, ERP and commission, relocation platforms | BP-08 to BP-17 |
| Immutable backups | Separate backup accounts with write-once retention; weekly copy to DC-2 | RPO for all Cloud A and B workloads |
| People | Closers, escrow accounting, payoff specialists, transaction coordinators, SOC, IT operations | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 2 | Network core, SD-WAN, DNS, and colocation connectivity | 2 h | Cellular failover at closing offices |
| 3 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | MSSP tooling |
| 4 | SYS-04 Disbursement Hub and bank channels | 2 h target (6.5 h demonstrated) | Bank portals with dual approval for urgent wires |
| 5 | SYS-03 Closing Communications Hub | 4 h | Phone-only confirmation by a second closer; no email instructions |
| 6 | SYS-02 title production platform access and integrations | 4 h (vendor) | Read-only export; manual settlement statements |
| 7 | AQ-09 legacy closing software | 6 h target (24 h RPO today) | Hand urgent closings to enterprise Texas offices |
| 8 | SYS-06 email and the payoff aggregation service | 8 h | Hub messaging; lender portals |
| 9 | SYS-01 transaction management platform | 8 h target (24 h per vendor contract) | Daily export; email copies |
| 10 | Consumer website, app, and CRM | 12 h | Static listing site; round-robin routing |
| 11 | Property management, relocation, and maintenance dispatch | 24 h (dispatch phone line immediately) | After-hours call center; exported files |
| 12 | ERP, commission, and payroll | 48 h | Repeat prior payroll; prior-day commission file |
| 13 | Data warehouse and analytics | 72 h | Last exports |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Transaction platform contract RTO 24 h against an 8 h BIA RTO; no tested fallback | P01 R-033; P03 G-012; POAM-007 |
| Disbursement Hub recovery 6.5 h against a 2 h process RTO | P01 R-025; P02 CP-10; POAM-011 |
| AQ-09 legacy closing software with a 24 h real RPO and single-approver wires | P01 R-004; POAM-005 |
| Legacy email tenants at AQ-06 to AQ-08 | P01 R-005; POAM-003; POAM-004 |
| Payee verification coverage at 86% | P01 R-002; POAM-006 |
| E-signature and tenant screening provider reviews overdue | P01 R-035; POAM-012 |
