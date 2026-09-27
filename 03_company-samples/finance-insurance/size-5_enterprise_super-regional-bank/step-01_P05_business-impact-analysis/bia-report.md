# Business Impact Analysis: Cris Santos Company | Finance and Insurance | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded bank holding company; principal subsidiary Cris Santos Bank, N.A.) | **Tier:** Enterprise (12,000 employees; $86.4 billion in average total consolidated assets) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** Director of Enterprise Resilience and the GRC team with process owners, 2026-05-04 to 2026-06-26 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-07-17 | **Reported to:** board risk committee, 2026-09-15

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the bank and its broker-dealer depend on, how long each can be down, how much data each can lose, and what each depends on, including third parties, Federal Reserve payment services, and the acquired bank's remaining platform. It feeds:
- the business continuity and disaster recovery program, which is one of the measures the Interagency Guidelines require the bank to consider against destruction, loss, or damage of customer information from environmental hazards or technological failures (12 CFR 30 App. B III.C.1.h);
- the 12 CFR 53.3 notification incident test, which asks whether an incident has materially disrupted or degraded, or is reasonably likely to, the bank's ability to serve a material portion of its customers or a business line whose failure would cause a material loss (53.2(b)(7)). The MTDs below tell responders when an outage reaches that point;
- the availability rating and recovery objectives in the CBDC System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order and the materiality inputs in the BEC and wire fraud runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 21 processes were analyzed; 10 are High criticality, 10 Moderate, and 1 Low. 11 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies, 15 of them single points of failure and 2 never tested by the bank.

## 2. System and business description
Cris Santos Company, Inc. is the publicly traded parent of Cris Santos Bank, N.A., a national bank with 610 branches and about 1,480 ATMs in Florida, Georgia, Alabama, South Carolina, North Carolina, and Tennessee, and of Cris Santos Investment Services, LLC, a broker-dealer and investment adviser. The group has 12,000 employees, about 3.6 million consumer customers, about 290,000 business clients, and about $4.8 billion in annual revenue. The technology estate is described in `../00_company-facts.md` section 3: a core banking platform on a mainframe in two bank data centers (SYS-01), a digital banking platform on Cloud provider A (SYS-02), a payments hub connected to Federal Reserve payment services (SYS-03), a vendor-hosted treasury management platform (SYS-04), an identity platform (SYS-05), a multi-cloud and data center estate (SYS-06), branches and ATMs (SYS-07), about 22,000 endpoints (SYS-08), and about 2,400 third parties (41 critical). The acquired bank merged in on 2025-10-01; its core conversion finished on 2026-05-16, but about 2,900 of its business clients still use its legacy commercial online banking platform until 2027-02-26.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day (about $19 million per business day) and to the materiality playbook used by the disclosure committee (P08 section 7). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | A tier-1 service stops for all customers, or more than 100 branches cannot serve customers | One service, one state, or up to 100 branches stop | Staff slowed but working |
| Regulatory | Notification incident under 12 CFR 53.3; missed payment system settlement obligations; missed SEC or Call Report deadline; SAR deadlines missed | Missed contractual or internal regulatory deadline | Internal policy deviation |
| Safety | Not rated for this business (branch physical safety is handled in the physical security program) | | |
| Reputation | National media, rating agency or analyst action, or loss of commercial or institutional clients | Regional media; client complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 Wire transfer processing | High | 4 h | 2 h | 0 | $6.80M |
| BP-09 Commercial treasury management services (SL-1) | High | 4 h | 2 h | 15 min | $5.20M |
| BP-11 Sanctions screening and payment fraud detection | High | 2 h | 1 h | 15 min | $1.20M |
| BP-04 Deposit account servicing and core posting | High | 8 h | 4 h | 15 min | $8.90M |
| BP-15 Treasury, liquidity, and Federal Reserve account management | High | 4 h | 2 h | 15 min | $2.00M |
| BP-07 Card authorization (debit and credit) | High | 2 h | 1 h | 0 | $1.90M |
| BP-02 ACH origination and receipt | High | 12 h | 4 h | 15 min | $4.50M |
| BP-05 Consumer and small business digital banking | High | 8 h | 4 h | 15 min | $3.10M |
| BP-06 Branch and teller operations | High | 8 h | 4 h | 15 min | $2.40M |
| BP-10 Contact centers and customer authentication | Moderate | 8 h | 4 h | 1 h | $0.80M |
| BP-03 Instant payments and person-to-person transfers | Moderate | 8 h | 4 h | 15 min | $0.60M |
| BP-20 Legacy commercial online banking for acquired bank clients | High | 8 h | 8 h | 1 h | $0.40M |
| BP-17 Brokerage and advisory services | Moderate | 24 h | 8 h | 1 h | $0.90M |
| BP-08 ATM network | Moderate | 24 h | 8 h | 15 min | $0.35M |
| BP-18 Institutional trust, custody, and retirement plan services (SL-2) | Moderate | 24 h | 12 h | 1 h | $0.60M |
| BP-12 Consumer lending origination | Moderate | 72 h | 24 h | 1 h | $1.10M |
| BP-13 Commercial lending and loan servicing | Moderate | 48 h | 24 h | 1 h | $0.70M |
| BP-14 BSA/AML monitoring and SAR filing | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-16 Financial close, regulatory and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-19 Payroll and human resources | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-21 Marketing and customer analytics | Low | 168 h | 72 h | 24 h | $0.08M |

Rows are in recovery priority order (the `recovery_priority` column). BP-01, BP-09, and BP-11 share priority 1 because a wire cannot be released without sanctions screening and most commercial wires start in the treasury platform.

**What drives the values:**
- **Payment system deadlines** set the shortest MTDs. Wires, sanctions screening, card authorization, and the Federal Reserve account position (BP-01, BP-07, BP-11, BP-15) must work the same business day, and accepted payment messages cannot be lost (RPO zero).
- **The core drives the dollar value.** BP-04 has the largest daily impact ($8.9 million) because every channel reads balances from the core. A core outage longer than its 8-hour MTD would almost certainly be a notification incident under 12 CFR 53.2(b)(7)(i).
- **Clients and contracts** set the treasury (BP-09) and institutional (BP-18) objectives, because commercial and institutional clients rely on them and receive SOC reports (P09).
- **Regulation** sets BSA/AML (BP-14: the 30-day SAR clock under 12 CFR 21.11(d) keeps running during an outage) and financial reporting (BP-16: MTD drops to 48 hours in the quarter-end window).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Treasury management platform (DEP-07).** One vendor serves all 41,000 commercial clients on the main platform. Its contract RTO is 4 hours against the 2-hour BIA RTO for BP-09. The fallback (phone and secure file instructions verified by the callback team) was tested at a 200-instruction scale in 2026-02, not at a full-day scale. This is P01 risk R-022 and POA&M item POAM-018 (renegotiate at the 2027-06 renewal; interim surge staffing for the callback team).
2. **Legacy commercial platform (DEP-08).** About 2,900 acquired bank clients use a platform with a 24-hour contract RTO against an 8-hour BIA RTO, SMS one-time passcodes, no out-of-band confirmation of new beneficiaries, and only login events in the SIEM. The bank has never tested its restore. Migration to SYS-04 is due 2027-02-26 (R-004, POAM-004).
3. **No isolated copy of core data (DEP-25).** Core data is replicated from DC-1 to DC-2 and backed up to virtual tape in DC-2. A destructive attack with administrator access could reach both. A logically isolated, immutable cyber vault is funded for 2027 (R-002, POAM-020).
4. **Card processor (DEP-09).** One processor handles every debit and credit authorization. Stand-in authorization covers core outages, not processor outages. The processor's latest SOC report review is late (R-023, POAM-012).
5. **Federal Reserve payment services (DEP-06).** An industry-wide single point of failure the bank cannot remove. The fallback is procedural: Federal Reserve contingency procedures and a correspondent bank for up to 300 priority wires a day (DEP-20).
6. **Sanctions screening capacity (DEP-13).** If the screening engine fails in both data centers, manual review handles about 400 wires an hour against a peak of 2,500. This is why BP-11 has a 1-hour RTO.
7. **Clearing firm (DEP-15).** The broker-dealer's clearing contract has no 72-hour breach notice term, which Regulation S-P now requires the broker-dealer's policies to demand of service providers (17 CFR 248.30(a)(5)(i)(B)) (R-041, POAM-021).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Core banking platform (DC-1, recovery in DC-2) | Deposits, loans, customer information file, nightly batch | BP-04, BP-06, BP-07, BP-12, BP-13 |
| SYS-02 Digital banking platform (Cloud provider A) | Online and mobile banking, payment initiation | BP-03, BP-05 |
| SYS-03 Payments hub (DC-1 and DC-2) | Wires, ACH, instant payments, Federal Reserve connectivity | BP-01, BP-02, BP-03, BP-15 |
| SYS-04 Treasury management platform (vendor SaaS) | Commercial online banking and payment initiation | BP-09, BP-02 |
| SYS-05 Identity platform and CIAM | Workforce SSO, MFA, PAM, IGA; customer authentication | All |
| SYS-06 Cloud provider B workloads | Enterprise data platform, credit decisioning | BP-12, BP-21 |
| SYS-07 Network, branches, ATMs | SD-WAN, branch networks, ATM network | BP-06, BP-08 |
| SYS-10 Card processing (card processor) | Authorization and settlement | BP-07, BP-08 |
| SYS-11 Fraud and financial crime platforms | Sanctions screening, fraud scoring, AML monitoring | BP-01, BP-05, BP-09, BP-11, BP-14 |
| SYS-14 Broker-dealer systems (clearing firm) | Brokerage and advisory accounts | BP-17 |
| Immutable backups | Separate backup accounts with write-once retention in both clouds and for distributed systems | RPO for cloud and distributed workloads |
| People and facilities | Wire operations room and alternate room, callback team, financial crimes team, contact centers, 610 branches | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; CIAM second region |
| 2 | Data center network core, SD-WAN, DNS, and Federal Reserve connectivity | 1 h | DC-2 network core; dual carriers |
| 3 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | Cyber Defense Center standby tooling in DC-2 |
| 4 | Payments hub and sanctions screening (SYS-03, SYS-11) | 2 h | Alternate wire room; correspondent bank for priority wires; manual screening queue |
| 5 | Core banking platform (SYS-01) | 4 h | DC-2 failover; stand-in files for branches and cards |
| 6 | Treasury management platform connectivity (SYS-04) | 2 h (vendor contract 4 h) | Phone and secure file instructions with callback |
| 7 | Card processor connectivity and stand-in (SYS-10) | 1 h | Processor stand-in authorization |
| 8 | Digital banking and CIAM (SYS-02) | 4 h | Branches and contact centers |
| 9 | Contact center service and telephony | 4 h | Backup carrier; site rerouting |
| 10 | Legacy commercial online banking platform | 8 h target (24 h per vendor contract) | Phone and secure file instructions with callback |
| 11 | Broker-dealer systems and clearing firm links (SYS-14) | 8 h | Clearing firm trade desk |
| 12 | ATM network | 8 h | Branches; network ATMs |
| 13 | Trust accounting and custody platform | 12 h | Manual instructions to the sub-custodian |
| 14 | Loan origination systems and credit decisioning (SYS-09, SYS-06) | 24 h | Queue applications |
| 15 | AML monitoring and case management | 48 h | Risk-based manual review of large wires |
| 16 | ERP, general ledger, HR and payroll | 48 to 72 h | Last close; repeat prior payroll |
| 17 | Enterprise data platform and marketing tools | 72 h | Pause campaigns |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Treasury platform contract RTO 4 h against 2 h BIA RTO; fallback not tested at full-day scale | P01 R-022; P03 G-033; POAM-018 |
| Legacy commercial platform: 24 h contract RTO, never tested, weak authentication and logging | P01 R-004; P03 G-017; POAM-004 |
| No logically isolated immutable copy of core data | P01 R-002; P03 G-035; POAM-020 |
| Card processor single point of failure; SOC report review late | P01 R-023; P03 G-043; POAM-012 |
| Clearing firm contract lacks the Regulation S-P 72-hour notice term | P01 R-041; P03 G-092; POAM-021 |
| Manual sanctions screening capacity far below peak volume | P01 R-028; P02 CP-2 |
