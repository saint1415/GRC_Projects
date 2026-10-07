# Business Impact Analysis: Cris Santos Company | Financial Services | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded merchant payment processor; about 410,000 merchants in all 50 states) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-09-08 | **Reported to:** board risk and technology committee, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including the sponsor banks, card networks, cloud providers, and other third parties. It feeds:
- the enterprise business continuity and disaster recovery plans, including the PCI DSS incident response plan's business recovery and continuity procedures (PCI DSS 12.10.1);
- the BCDR plan the payouts subsidiary must keep under 23 NYCRR 500.16(a)(2), which must identify essential data, facilities, services, personnel, and third parties (500.16(a)(2)(i) and (vi));
- the asset inventory's recovery time objectives (500.13(a)(1)(v));
- the availability rating and recovery objectives in the Core Payment Processing Platform System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order and the 4-hour bank notice test in the incident runbook (P08);
- the Availability and Processing Integrity criteria for the two SOC 2 service lines (P09).

**Results in one line:** 18 processes were analyzed; 9 are High criticality, 7 Moderate, and 2 Low. 7 processes need recovery within 4 hours. 10 processes are covered services under at least one sponsor agreement, so a disruption of 4 or more hours triggers bank service provider notices. The dependency map (`dependency-map.csv`) lists 26 dependencies (23 on third parties), 16 of them single points of failure and 4 never tested (including all three sponsor banks, which have never joined a recovery test).

## 2. System and business description
Cris Santos Company authorizes, clears, and settles about 13.8 billion card transactions a year (about $780 billion in processed volume) for about 410,000 merchants. It has 12,000 employees and about $4.8 billion in annual receipts. The technology estate is described in `../00_company-facts.md` section 3:
- **Cloud A:** the authorization platform, token vault, portals, and hosted payment pages (SYS-01, SYS-04), active-active in two regions, and the data and AI platform (SYS-11).
- **DC-1 (Florida) and DC-2 (another state):** the clearing, settlement, and merchant funding platform on a mainframe and 46 midrange batch servers (SYS-02), the payment HSMs (SYS-03), and card network and bank connectivity (SYS-10).
- **Cloud B:** the Integrated Payments platform (SYS-05) and the payouts platform of Cris Santos Payouts, LLC (SYS-06).
- **Shared services:** identity (SYS-07), the Cyber Fusion Center (SYS-08), the engineering platform (SYS-09), and SaaS for onboarding, contact centers, and corporate IT (SYS-12 to SYS-14).

Three sponsor banks (A, B, and C) hold the card network memberships and originate the merchant funding ACH files the company prepares. Each sponsor agreement names authorization, clearing, settlement, reconciliation, and merchant funding file services as services performed for the bank under the Bank Service Company Act (12 U.S.C. 1867(c)).

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the materiality framework in the disclosure committee's playbook (P08 section 6). Values are per 24 hours of outage unless stated. Payment processing has no direct physical safety impact, so the Safety category is rated N/A for every process; critical infrastructure effects are captured under Operations.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $250,000 to $1 million per day | Less than $250,000 per day |
| Operations | Authorization or merchant funding stops for more than 1% of merchants, or any sponsor bank cutoff is missed | One service line, one sponsor bank program, or one region degraded | Staff slowed but working |
| Regulatory | Bank service provider notice triggered (4 or more hours); card brand compromise report; NYDFS 72-hour notice; missed SEC filing | Missed contractual report or audit deadline | Internal policy deviation |
| Safety | Not applicable to payment processing (rated N/A) | | |
| Reputation | National media, analyst or ratings action, loss of a sponsor bank or a top-50 merchant | Trade press; partner or merchant complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
Listed in recovery priority order.

| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h | Bank covered service |
|---|---|---|---|---|---|---|
| BP-01 Card authorization | High | 2 h | 15 min | 0 (synchronous) | $11.60M | Yes (A, B, C) |
| BP-02 Token vault and tokenization | High | 2 h | 15 min | 0 (synchronous) | $3.10M | Yes (A, B, C) |
| BP-03 E-commerce gateway and hosted payment pages | High | 2 h | 30 min | 15 min | $4.60M | Yes (A, B, C) |
| BP-10 Fraud scoring and risk monitoring (AI-001) | High | 4 h | 1 h | 24 h | $1.80M | No |
| BP-07 Integrated Payments API and hosted fields (SL-1) | High | 2 h | 1 h | 15 min | $3.00M | Yes (B) |
| BP-05 Merchant funding files to the sponsor banks | High | 8 h | 6 h | 15 min | $2.10M | Yes (A, B, C) |
| BP-04 Clearing file submission to the card networks | High | 12 h | 6 h | 15 min | $2.40M | Yes (A, B, C) |
| BP-08 Payouts (Cris Santos Payouts, LLC) | High | 8 h | 4 h | 15 min | $0.58M | Yes (C) |
| BP-14 Treasury and sponsor bank cash management | Moderate | 24 h | 8 h | 1 h | $0.70M | Yes (A, B, C) |
| BP-06 Settlement reconciliation, interchange, and fees | High | 24 h | 12 h | 15 min | $0.90M | Yes (A, B, C) |
| BP-13 Contact centers and merchant support | Moderate | 12 h | 4 h | 24 h | $0.50M | No |
| BP-11 Merchant and partner portals, virtual terminal | Moderate | 24 h | 8 h | 1 h | $0.40M | No |
| BP-09 Chargeback and dispute processing | Moderate | 72 h | 24 h | 4 h | $0.35M | Yes (A, B, C) |
| BP-12 Merchant onboarding, underwriting, and KYC | Moderate | 72 h | 48 h | 24 h | $0.30M | No |
| BP-16 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.30M | No |
| BP-15 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M | No |
| BP-17 Data, analytics, and merchant reporting feeds | Low | 72 h | 48 h | 24 h | $0.10M | No |
| BP-18 Partner onboarding and developer portal | Low | 72 h | 48 h | 24 h | $0.05M | No |

**What drives the values:**
- **Real-time payments** set the shortest MTDs. Authorization, tokenization, and the e-commerce gateway (BP-01 to BP-03) and Integrated Payments (BP-07) fail merchants within minutes, and large merchants route to backup processors and may not return. Merchant agreements promise 99.99% monthly availability, about 4.3 minutes of downtime a month.
- **Bank cutoffs** set the settlement objectives. Funding files (BP-05) must reach Bank A by 03:00, Bank B by 04:00, and Bank C by 05:00 Eastern. A missed cutoff delays about $2.1 billion of merchant funding for a business day. The 6-hour RTO leaves room to finish the batch before the earliest cutoff after a failure at the start of the nightly run.
- **The 4-hour regulatory line.** A computer-security incident that disrupts covered services to a bank for four or more hours requires notice to each affected bank's designated contact as soon as possible (12 CFR 53.4, 304.24, 225.303). Ten processes are covered services, so any outage that will clearly run past 4 hours on them is a notice decision, not only an operations decision (P08 section 7).
- **Licensed activity.** Payouts (BP-08) is the licensed business of the NYDFS-regulated subsidiary, so its outage is weighed for the NYDFS 72-hour notice (500.17(a)) as well as for merchant harm.
- **Regulation tightens** financial close (BP-15) during the quarter-end window, when the MTD drops to 48 hours because of SEC filing deadlines.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Settlement recovery is the largest gap (DEP-03, DEP-04, DEP-13, DEP-14).** The 2026-04-25 disaster recovery test restored the settlement platform in DC-2 in 9.5 hours against a 6-hour RTO, mainly because of manual batch scheduler restarts and a 22-minute replication lag. In a real event that would have missed Bank A's 03:00 funding cutoff and triggered notices to all three banks. This is P01 risk R-004 and POA&M item POAM-006.
2. **The sponsor banks have never joined a recovery test (DEP-06 to DEP-08).** Each bank can hold its ACH window open for up to 2 hours by agreement, but the procedure has never been rehearsed. Bank C (sponsor since 2026-03-01) has not yet given designated contacts for 225.303 notices that are loaded in the incident tooling (P01 R-013; POAM-007). A joint exercise is planned (POAM-016).
3. **Managed file transfer is a single-vendor dependency on the settlement path (DEP-09).** Every clearing and funding file passes through the MFT appliances. They cannot run the company's EDR agent, and the manual fallback (secure upload to bank and network portals) has been drilled only with Bank A. File transfer products have been a repeated target of mass exploitation campaigns, so this is the initial access path in the P08 scenario (P01 R-003; POAM-009).
4. **Cloud concentration (DEP-01).** Cloud A carries all Merchant Acquiring authorization, about 70% of all authorization volume. The two-region active-active design met its 15-minute target in the 2026-02-21 failover test, but it does not protect against a provider-wide control plane failure. The exit plan is a document only (P01 R-008).
5. **Hosted payment fields at ISV partners (DEP-23).** Tamper-detection covers 64% of ISV integrations, so a script attack in a partner checkout could go unseen (POAM-021).
6. **People (DEP-25).** 5 of the 18 mainframe and settlement batch engineers are eligible to retire by 2028 (P01 R-024).
7. **Industry-wide dependencies (DEP-05, DEP-19).** The card networks and instant payment rails are single points of failure the company cannot remove; workarounds are procedural (network stand-in processing; next-day funding).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Authorization platform (Cloud A, two regions) | Authorization switch, gateways, token vault | BP-01 to BP-03, BP-10 |
| SYS-02 Settlement platform (DC-1, DR in DC-2) | Clearing file builder, interchange and fee engine, reconciliation, funding files, chargebacks | BP-04 to BP-06, BP-08, BP-09, BP-14, BP-15 |
| SYS-03 Payment HSM estate | PAN encryption, tokenization, PIN translation, TLS keys | BP-01, BP-02, BP-04, BP-05, BP-07 |
| SYS-04 Portals and hosted payment pages | Merchant self-service, virtual terminal, payment pages | BP-03, BP-09, BP-11 |
| SYS-05 Integrated Payments platform (Cloud B) | Partner APIs and hosted fields | BP-07 |
| SYS-06 Payouts platform (Cloud B) | Instant and same-day payouts | BP-08 |
| SYS-07 Identity platform | SSO, MFA, PAM, identity governance | All |
| SYS-08 Cyber Fusion Center tooling | Detection and response for recovery validation | All |
| SYS-10 Bank and network connectivity | MFT appliances, network interface processors, treasury workstations | BP-01, BP-04, BP-05, BP-14 |
| SYS-11 Data and AI platform | Model serving for AI-001; data lake | BP-10, BP-17 |
| Immutable backups and virtual tape | Write-once cloud backup accounts; virtual tape replication DC-1 to DC-2 | RPO for all platforms |
| People | Settlement operators and mainframe engineers, platform engineers, Cyber Fusion Center, contact center agents | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-07 identity platform and break-glass accounts; PAM vault in DC-1 | 1 h | Sealed break-glass accounts; PAM works without SSO |
| 2 | Network core, card network links, DNS, and DC-1 to Cloud A interconnect | 1 h | Diverse carriers; DC-2 links |
| 3 | Cyber Fusion Center tooling (EDR console, SIEM) for clean-environment validation | 2 h | Local log buffers; network sensors |
| 4 | SYS-03 payment HSMs and key availability | 15 min | HSM clusters in DC-1, DC-2, and Cloud A |
| 5 | SYS-01 authorization platform and token vault | 15 min | Second Cloud A region; network stand-in |
| 6 | SYS-04 hosted payment pages and e-commerce gateway | 30 min | Direct origin serving at reduced capacity |
| 7 | SYS-11 model serving for fraud scoring | 1 h | Fallback rules in the switch |
| 8 | SYS-05 Integrated Payments platform | 1 h | Cloud B second region |
| 9 | SYS-10 MFT and SYS-02 settlement platform (clearing and funding) | 6 h target (9.5 h achieved in the last test) | DC-2; manual portal upload; bank cutoff extension |
| 10 | SYS-06 payouts platform | 4 h after settlement outputs are available | Next-day funding through the banks |
| 11 | Treasury workstations and bank portals | 8 h | Call-back verified phone instructions |
| 12 | Contact center platform and portals | 4 to 8 h | Backup carrier; overflow vendor |
| 13 | Chargeback system, onboarding, ERP and payroll | 24 to 48 h | Network portals; repeat prior payroll |
| 14 | Data lake, reporting feeds, developer portal | 48 h | Regenerate from settlement data |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Settlement recovery 9.5 h against a 6 h RTO | P01 R-004; P02 CP-10; P03 G-176 (500.16(a)(2)); POAM-006 |
| Sponsor banks never in a recovery test; no joint cutoff procedure rehearsed | P01 R-014; P02 CP-2(1); POAM-016 |
| Bank C designated contacts not loaded for 225.303 notices | P01 R-013; P03 G-136; POAM-007 |
| MFT single-vendor dependency without EDR; manual fallback drilled with one bank | P01 R-003; POAM-009 |
| Cloud A provider-wide failure not covered | P01 R-008 |
| Hosted fields tamper-detection at 64% of ISV integrations | P01 R-010; P03 G-039 and G-086; POAM-021 |
| Asset records missing support dates or RTOs for about 18% of assets | P03 G-170 (500.13(a)); POAM-018 |
| Mainframe skills concentration | P01 R-024 |
