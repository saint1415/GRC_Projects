# Business Impact Analysis: Cris Santos Company | Financial Services | Small

**Organization:** Cris Santos Company, LLC (payment processor serving merchants) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Information Security Lead) with the CTO, CFO, Settlement Operations Manager, Merchant Support Manager, and Risk and Fraud Manager, during fieldwork 2026-07-13 to 2026-07-24 | **Approved:** COO, 2026-08-31

## 1. Overview and purpose
This BIA identifies the business processes the processor depends on, how long each can be down, and how much data it can lose. It feeds:
- the platform recovery runbook and failover test that do not exist yet (gap 15 in `../00_company-facts.md`);
- the incident response plan's recovery order (POL-03 and the P08 runbook), including PCI DSS 12.10.1, which requires the plan to cover business recovery and continuity procedures;
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01, especially R-006 and R-008);
- the four-hour test in the bank service provider notice rule, 12 CFR 53.4(a): a computer-security incident that materially disrupts or degrades covered services to the sponsor bank for four or more hours must be reported to the bank's designated point of contact as soon as possible.

The FTC Safeguards Rule does not require a BIA, but its incident response plan element (16 CFR 314.4(h)) asks for a plan to "recover from" security events. This BIA sets what "recovered" means.

## 2. System and business description
The processor authorizes, clears, and settles card payments for about 4,200 merchants in 41 states: about 260,000 transactions a day, about $6.8 billion a year. Everything runs on the Payment Processing Platform (PPP) in one public cloud tenant (see P02 and P04): the authorization switch, API and terminal gateways, token vault, settlement and funding engine, payment HSM service, merchant portal, and hosted payment page. The platform runs across several availability zones in one region. Database snapshots are copied daily to a second region, but no workloads run there. The Florida office holds all 60 staff; nothing in the CDE runs there. See `../00_company-facts.md` sections 1 and 3.

**Contract commitments that set the numbers:**
- Merchant agreements promise 99.9% monthly availability for authorization (about 43 minutes of downtime a month).
- The sponsor agreement requires the clearing files and the daily merchant funding file to reach the sponsor bank by its daily cutoff. These are the covered services under the Bank Service Company Act (12 U.S.C. 1867(c)) named in the agreement.

## 3. Impact categories and values
Dollar values are scaled to the processor's own receipts ($28.2 million a year, about $77,000 a day), not to the merchant sales it carries (about $18.6 million a day).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $250,000 (service credits, lost fees, merchant attrition, card brand assessments) | $50,000 to $250,000 | Less than $50,000 |
| Operations (merchant operations) | Merchants cannot accept cards, or are not settled or funded | One channel or service stops (for example the virtual terminal) | Staff slowed but merchants unaffected |
| Regulatory and card brand | Sponsor bank notice under 12 CFR 53.4; reportable card data compromise; PCI DSS requirement not in place | Missed card network deadline or contract service level | Internal policy deviation |
| Safety | Not applicable: no process affects physical safety | | |
| Reputation | Loss of the sponsor bank relationship, a software-platform partner, or many merchants; trade press coverage | Merchant complaints and social media | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Card authorization | High | 4 h | 1 h | 15 min |
| BP-02 Recurring billing | Moderate | 24 h | 8 h | 15 min |
| BP-03 Clearing and settlement | High | 24 h | 8 h | 1 h |
| BP-04 Merchant funding | High | 24 h | 8 h | 1 h |
| BP-05 Chargebacks and disputes | Moderate | 72 h | 48 h | 24 h |
| BP-06 Fraud and merchant risk monitoring | Moderate | 24 h | 8 h | 4 h |
| BP-07 Merchant portal and virtual terminal | Moderate | 24 h | 8 h | 1 h |
| BP-08 Merchant support | Moderate | 24 h | 8 h | 24 h |
| BP-09 Security monitoring and incident response | High | 24 h | 4 h | 1 h |
| BP-10 Merchant onboarding and underwriting | Low | 120 h | 72 h | 24 h |
| BP-11 Finance, payroll, and HR | Low | 120 h | 72 h | 24 h |

Totals: 11 processes; 4 High, 5 Moderate, 2 Low.

**What drives the values:**
- **Authorization (BP-01) is real time.** There is no manual workaround for card-not-present sales. After about 4 hours, large merchants switch to backup processors, and the outage becomes a reportable event for the sponsor bank if it also delays settlement or funding.
- **Settlement and funding (BP-03, BP-04) run on a daily cycle.** A missed cutoff delays money for every merchant. Both are covered services for the sponsor bank, so an incident that disrupts them for four or more hours triggers the 12 CFR 53.4 notice.
- **Security monitoring (BP-09) is High for regulatory reasons, not revenue.** PCI DSS requires logs to be collected and reviewed without gaps. The 9-day log forwarding failure in May 2026 is the example (gap 7).
- **Fraud scoring (BP-06) has a fallback.** When the model is down, the authorization switch applies fallback rules, so authorizations continue at higher fraud risk.

**Key findings:**
1. **The authorization RPO and RTO hold only for a zone failure.** A failure of the whole primary region would leave the processor with daily snapshots in the second region: an actual RPO of up to 24 hours and an unknown RTO, because no recovery runbook exists and failover has never been tested. That is far beyond the 4-hour MTD for BP-01 and the 24-hour MTD for BP-03 and BP-04 (risk R-006 in P01).
2. **Settlement database restores have not been tested since the March 2026 migration** (risk R-008). The 8-hour RTO for BP-03 and BP-04 is unproven.
3. **The payment HSM service is a single point of failure.** Without it, no card number can be tokenized or decrypted. Its second-region configuration must be confirmed with the provider.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Authorization switch, API and terminal gateways | Container workloads across zones in the primary region | BP-01, BP-02, BP-06 |
| SYS-01 Token vault and settlement database | Managed relational database with synchronous replication across zones, point-in-time recovery (5-minute log backups), and daily snapshots copied to the second region | BP-01 to BP-05, BP-07 |
| SYS-02 Payment HSM service | Keys for PAN encryption and tokenization | BP-01, BP-02, BP-03 |
| SYS-03 Merchant portal and virtual terminal | Web application | BP-05, BP-07 |
| SYS-04 Hosted payment page | Served through the content delivery service | BP-01 |
| SYS-05 Identity provider | Workforce single sign-on and MFA; two break-glass accounts for the cloud console | All |
| SYS-07 SIEM, EDR, web application firewall | Security monitoring; cloud-native logs held in the tenant for 7 days as a buffer | BP-09 (and protects BP-01) |
| SYS-09 Fraud-detection model | Licensed model hosted in the tenant; fallback rules in the switch | BP-06 |
| SYS-10, SYS-12 Productivity suite and ticketing | SaaS | BP-08, BP-09 |
| SYS-11 Merchant onboarding and CRM | SaaS | BP-10 |
| Card network links | Dedicated encrypted links under the sponsor bank's membership | BP-01, BP-03, BP-05 |
| People | 4 platform engineers (one on call), 6 settlement and finance staff, 9 support staff, IT Manager | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 identity provider and break-glass cloud accounts | 1 h | Break-glass accounts with hardware keys held in the office safe and by the CTO |
| 2 | Cloud tenant network, SYS-02 payment HSM service, card network links | 1 h | Provider-managed across zones; second-region HSM configuration to be confirmed (finding 3) |
| 3 | SYS-01 authorization path (BP-01) | 1 h | Zone failover is automatic; region failover is not built (R-006) |
| 4 | SYS-07 log collection and alerting (BP-09) | 4 h | Cloud-native log buffer in the tenant for 7 days |
| 5 | SYS-01 settlement and funding engine (BP-03, BP-04) | 8 h | Point-in-time restore; send files in the next cutoff window |
| 6 | SYS-12 ticketing and phone line (BP-08) | 8 h | Phones forwarded to mobile phones; shared inbox |
| 7 | SYS-03 merchant portal (BP-07) | 8 h | Internal refund tool with dual approval |
| 8 | SYS-01 recurring billing scheduler (BP-02) | 8 h | Re-run missed batches |
| 9 | SYS-09 fraud model (BP-06) | 8 h | Fallback rules in the switch |
| 10 | Dispute processing (BP-05) | 48 h | Network dispute portal |
| 11 | SYS-11 CRM and onboarding (BP-10); payroll SaaS (BP-11) | 72 h | Secure upload queue; repeat prior payroll |

**Treatment (tracked in P01 and P07):** build a warm standby in the second region for the authorization path and a recovery runbook, with a semiannual failover test (R-006, due 2027-03-31); run quarterly settlement database restore tests (R-008, first test by 2026-11-30).
