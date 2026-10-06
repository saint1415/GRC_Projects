# Business Impact Analysis: Cris Santos Company | Financial Services | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed payment processor serving merchants) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Director of Information Security with the vCISO, the process owners named in `bia.csv`, and the VP Platform Engineering | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the board audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: Merchant Processing, Integrated Payments, Settlement and Treasury Operations, Risk, Fraud, and Compliance, Merchant Services, and Corporate. It rates 17 business processes and quantifies what an outage costs in money, merchant operations, and regulatory and card brand exposure.

The results feed:
- the recovery runbooks and failover tests (gap 8 in `../00_company-facts.md`);
- both incident runbooks in P08 and their recovery order, including PCI DSS 12.10.1, which requires the incident response plan to cover business recovery and continuity procedures;
- the availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment (P09);
- the four-hour test in the bank service provider notice rules: 12 CFR 53.4(a) for Bank A (OCC) and 12 CFR 304.24(a) for Bank B (FDIC). A computer-security incident that materially disrupts or degrades covered services to a sponsor bank for four or more hours, or is reasonably likely to, must be reported to the bank's designated point of contact as soon as possible (section 7).

The FTC Safeguards Rule does not require a BIA, but its incident response plan element (16 CFR 314.4(h)) asks for a plan to "recover from" security events. This BIA sets what "recovered" means.

## 2. System and business description
The company authorizes, clears, and settles card payments for about 31,000 merchants in all 50 states: about 2.25 million transactions and about $104 million of merchant sales a day. Processing runs on the Payment Processing Platform (PPP) described in the SSP (P02):
- the core authorization platform, merchant portal, and hosted payment page in a multi-account landing zone in Cloud A, with a warm standby in a second region (SYS-01, SYS-04, SYS-05);
- the settlement and funding engine and the company-owned payment HSMs on premises in a Florida colocation cage, with a disaster recovery cage outside Florida (SYS-02, SYS-03);
- bank connectivity servers that send funding files to both sponsor banks (SYS-16);
- the acquired Integrated Payments gateway in Cloud B (SYS-06).

About 600 staff work from the Florida headquarters, the acquired office, and remotely. See `../00_company-facts.md` sections 1, 3, and 7.

**Contract commitments that set the numbers:**
- Merchant agreements promise 99.95% monthly availability for authorization (about 22 minutes of downtime a month). ISV partner agreements promise the same for the Integrated Payments API.
- Each sponsor agreement requires the clearing files and the daily merchant funding file by the bank's cutoff (Bank A 03:00, Bank B 04:00 Eastern). These services are named in both agreements as subject to the Bank Service Company Act (12 U.S.C. 1867(c)), which makes them covered services under 12 CFR 53.2(b)(5) and 304.22(b)(5).

## 3. Impact categories and values
Dollar values are scaled to the company's own receipts ($100.0 million a year, about $274,000 a day: about $186,000 from Merchant Processing, $66,000 from Integrated Payments, and $22,000 from other fees), not to the merchant sales it carries (about $104 million a day).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per event) | More than $100,000 (service credits, lost fees, merchant and ISV attrition, interchange downgrades, card brand assessments) | $25,000 to $100,000 | Less than $25,000 |
| Operations (merchant operations) | Merchants cannot accept cards, or are not settled or funded | One channel, one business line, or one service stops (for example the virtual terminal) | Staff slowed but merchants unaffected |
| Regulatory and card brand | Bank service provider notice under 12 CFR 53.4 or 304.24; reportable card data compromise; PCI DSS requirement not in place | Missed card network deadline or contract service level | Internal policy deviation |
| Safety | Not applicable: no process affects physical safety | | |
| Reputation | Loss of a sponsor bank, a top-20 ISV partner, or many merchants; trade press coverage | Merchant complaints and social media | Internal only |

**How loss at MTD was estimated.** Estimated loss is lost fee revenue plus contractual service credits, overtime, interchange downgrades, and an attrition reserve for merchants and ISVs that move volume away, over the MTD. The process owners supplied the assumptions: service credits under the merchant and ISV agreements; about 0.6% of affected merchants moving to another processor after a 2-hour authorization outage; and interchange downgrades on transactions presented a day late. Delayed merchant funding is shown separately, because it is the merchants' cash, not the company's.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-02 Card-not-present authorization | Merchant Processing | High | 2 | 1 | 0.25 | $185,000 |
| 2 | BP-01 Card-present authorization | Merchant Processing | High | 2 | 1 | 0.25 | $150,000 |
| 3 | BP-03 Integrated Payments gateway authorization | Integrated Payments | High | 2 | 1 | 0.25 | $120,000 |
| 4 | BP-15 Security monitoring and incident response | Corporate | High | 24 | 4 | 1 | $15,000 |
| 5 | BP-06 Merchant funding | Settlement and Treasury | High | 12 | 8 | 0.25 | $140,000 (plus about $104 million of merchant funding delayed) |
| 6 | BP-05 Clearing and settlement | Settlement and Treasury | High | 24 | 8 | 0.25 | $310,000 |
| 7 | BP-07 Reconciliation and settlement exceptions | Settlement and Treasury | High | 24 | 12 | 1 | $45,000 |
| 8 | BP-11 Merchant portal and virtual terminal (core) | Merchant Processing | Moderate | 24 | 8 | 1 | $35,000 |
| 9 | BP-09 Fraud scoring and fraud operations | Risk, Fraud, and Compliance | Moderate | 24 | 8 | 4 | $70,000 |
| 10 | BP-13 Merchant support and contact center | Merchant Services | Moderate | 24 | 8 | 24 | $30,000 |
| 11 | BP-04 Recurring billing | Merchant Processing | Moderate | 24 | 8 | 0.25 | $20,000 |
| 12 | BP-12 Integrated Payments partner portal | Integrated Payments | Moderate | 24 | 8 | 1 | $25,000 |
| 13 | BP-08 Chargebacks and disputes | Risk, Fraud, and Compliance | Moderate | 72 | 48 | 24 | $60,000 |
| 14 | BP-10 Merchant risk monitoring | Risk, Fraud, and Compliance | Moderate | 72 | 24 | 24 | $50,000 |
| 15 | BP-17 Merchant statements and partner data feeds | Merchant Processing | Low | 72 | 48 | 24 | $25,000 |
| 16 | BP-14 Merchant onboarding and underwriting | Merchant Services | Low | 120 | 72 | 24 | $40,000 |
| 17 | BP-16 Finance, payroll, and HR | Corporate | Low | 120 | 72 | 24 | $20,000 |

**Summary:** 7 High, 7 Moderate, and 3 Low processes (17 in total). The sum of estimated losses at each process's MTD is $1,340,000. Direct fee revenue tied to the three authorization processes is $252,000 a day.

**Enterprise-wide scenarios:**
- **Primary Cloud A region lost for 8 hours, failover fails** (BP-01, BP-02, BP-04, BP-11): about $36 million of merchant sales cannot be authorized. Estimated loss about $1.1 million: service credits about $600,000, lost fees about $85,000, and an attrition reserve of about $400,000. If clearing or funding is also delayed, the 12 CFR 53.4 and 304.24 analysis applies.
- **Settlement environment down for 24 hours** (ransomware at the primary colocation cage; BP-05, BP-06, BP-07): estimated loss about $495,000, plus one full day of merchant funding (about $104 million) delayed for 31,000 merchants. Both sponsor banks must be notified (P08 `ir-runbook-settlement-ransomware.md`).
- **Integrated Payments gateway down for 8 hours** (BP-03, BP-12): estimated loss about $420,000, mostly ISV service credits and attrition.

**What drives the values:**
- **Authorization (BP-01 to BP-03) is real time.** There is no manual workaround for card-not-present sales, and card-present merchants can only take offline authorizations at their own risk. A 2-hour MTD reflects when large merchants and ISVs switch to backup processors.
- **Settlement, funding, and reconciliation (BP-05 to BP-07) run on a daily cycle** and are covered services for both sponsor banks. Funding has the shortest MTD in the cycle (12 hours) because the banks' cutoffs are fixed.
- **Security monitoring (BP-15) is High for regulatory reasons, not revenue.** PCI DSS requires logs to be collected and reviewed without gaps, and notice clocks keep running during an outage.
- **Fraud scoring (BP-09) has a fallback.** When the model is down, the switch applies fallback rules, so authorizations continue at higher fraud and false-decline rates.

## 5. Key findings
1. **Authorization failover does not meet the MTD.** The 2025-11 failover test to the secondary Cloud A region took 2 hours 40 minutes against a 1-hour RTO and a 2-hour MTD. Most of the time went to manual database promotion and DNS changes (P01 R-006; P07 CP-4).
2. **Settlement recovery does not meet the funding cutoff.** The 2026-02-21 disaster recovery test of the settlement engine at the DR cage took 11 hours against an 8-hour RTO. Run at night, it would have missed both banks' funding cutoffs (P01 R-007). Neither sponsor bank took part in the test.
3. **The Integrated Payments gateway has no warm standby.** It runs in one Cloud B region with database snapshots only. Its actual RTO for a region failure is unknown (P01 R-008).
4. **Payment HSMs are a single point of failure for settlement.** The colocation HSMs are paired within each cage, but the key ceremony to load the DR cage HSMs after a key rotation was last done in 2025-08. Every later key rotation must be replicated before a failover can work (P05 resource table; P01 R-017).
5. **Monitoring does not cover Cloud B** (gap 1). An attack on the gateway would not be seen by the MSSP, which is why BP-15 is High and why the P08 scenario starts there.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Core payment platform | Containers in the Cloud A CDE production account across 3 zones, warm standby in the CDE recovery account in a second region | BP-01, BP-02, BP-04, BP-09 |
| SYS-01 Token vault database | Managed relational database with synchronous replication across zones and asynchronous replication to the second region | BP-01, BP-02, BP-04, BP-11 |
| SYS-02 Settlement and funding engine | Batch servers and a settlement database at the primary colocation cage; database log shipping every 15 minutes to the DR cage | BP-05, BP-06, BP-07, BP-08, BP-17 |
| SYS-03 Payment HSMs | Paired company-owned HSMs in each colocation cage; cloud payment HSM service for the authorization path | BP-01 to BP-06 |
| SYS-04, SYS-05 Merchant portal and hosted payment page | Cloud A, behind the content delivery service | BP-02, BP-11 |
| SYS-06 Integrated Payments gateway | Containers and a managed database in one Cloud B region; daily snapshots | BP-03, BP-12 |
| SYS-07 Identity provider and PAM vault | Workforce sign-in and privileged access; break-glass accounts for each cloud and the colocation sites | All |
| SYS-09 SIEM, EDR, and MSSP | Detection and investigation; cloud-native log buffers of 30 days in each account | BP-15 and recovery validation |
| SYS-11, SYS-12 Fraud model and data platform | Model serving in Cloud A; training environment in the analytics account | BP-09, BP-10 |
| SYS-13, SYS-14 Onboarding, CRM, support, and contact center | SaaS | BP-10, BP-13, BP-14 |
| SYS-16 Bank connectivity | Managed file transfer servers at the primary cage, standby at the DR cage | BP-05, BP-06, BP-07 |
| Card network links | Dedicated encrypted links from both cages and from Cloud A, under the sponsor banks' memberships | BP-01 to BP-05, BP-08 |
| People | Site reliability engineers (on call), settlement and treasury staff (45), fraud analysts, support and contact center staff, security team and MSSP | All |

## 7. Sponsor bank covered services and the four-hour test
Both sponsor agreements name clearing, settlement, reconciliation, and merchant funding file services as services performed for the bank and subject to examination under 12 U.S.C. 1867(c). That makes BP-05, BP-06, and BP-07 **covered services** for both banks. The text of 12 CFR 53.4 and 12 CFR 304.24 was verified on the eCFR (2026-09-23 version); the two sections are identical in substance.

| Rule element (verified text, summarized) | What this BIA supplies | Status |
|---|---|---|
| Notify at least one bank-designated point of contact at each affected banking organization customer as soon as possible after determining that a computer-security incident has materially disrupted or degraded, or is reasonably likely to, covered services for four or more hours (53.4(a); 304.24(a)) | The covered processes (BP-05 to BP-07), their MTDs, and which bank each file serves. Funding (BP-06) has a 12-hour MTD, but a 4-hour disruption is reportable well before the MTD | Decision step written into both P08 runbooks |
| Use the bank-designated contact; if none was provided, notify the CEO and CIO or two individuals of comparable responsibilities (53.4(a)(1)-(2); 304.24(a)(1)-(2)) | Contacts per bank | Bank A contacts on file; **Bank B contacts not on file (gap 7)**, due 2026-10-15 |
| Scheduled maintenance, testing, or software updates previously communicated to the bank are excluded (53.4(b); 304.24(b)) | Disaster recovery tests and maintenance windows must be announced to both banks in advance | Added to the change calendar |
| Authorization (BP-01 to BP-03) | Not named as a covered service in either agreement; an authorization outage alone does not trigger the notice, but one that also delays clearing or funding does | Recorded in P08 |

**Federal Reserve parallel (12 CFR 225.303).** Not applicable: no services are performed for a Board-supervised banking organization.

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-07 identity provider, PAM vault, and break-glass accounts | 1 h | Break-glass accounts with hardware keys sealed at headquarters and with the VP Platform Engineering |
| 2 | Cloud A network hub, payment HSM service, card network links | 1 h | Provider-managed across zones; secondary region for regional failures |
| 3 | SYS-01 authorization path and SYS-05 hosted payment page (BP-01, BP-02) | 1 h target; 2 h 40 min demonstrated | Automated database promotion and DNS failover (R-006, due 2027-03-31) |
| 4 | SYS-06 Integrated Payments gateway (BP-03) | 1 h target; unknown for a region failure | Second-region standby planned with the 2027 migration (R-008) |
| 5 | SYS-09 log collection, SIEM feeds, and MSSP access (BP-15) | 4 h | Cloud-native log buffers for 30 days; MSSP platform is independent |
| 6 | SYS-03 colocation HSMs, SYS-02 settlement database, SYS-16 bank connectivity (BP-06, BP-05) | 8 h target; 11 h demonstrated | DR cage with 15-minute log shipping; ask the sponsor bank to hold the ACH window (R-007) |
| 7 | SYS-02 reconciliation (BP-07) | 12 h | Spreadsheet matching from network and bank reports |
| 8 | SYS-04 merchant portal and virtual terminal (BP-11) | 8 h | Internal refund tool with dual approval |
| 9 | SYS-11 fraud model (BP-09) | 8 h | Fallback rules in the switch |
| 10 | SYS-14 contact center and ticketing (BP-13) | 8 h | Backup contact center number; status page |
| 11 | Recurring billing scheduler (BP-04) | 8 h | Re-run missed batches |
| 12 | SYS-06 partner portal (BP-12) | 8 h | Secure upload for urgent boarding |
| 13 | Chargeback system (BP-08) | 48 h | Network dispute portals |
| 14 | SYS-13 merchant risk monitoring (BP-10) | 24 h | Daily exception report; manual funding holds |
| 15 | Statements and partner feeds (BP-17) | 48 h | Regenerate and send late |
| 16 | SYS-13 onboarding (BP-14) | 72 h | Secure upload queue |
| 17 | Payroll and ERP SaaS (BP-16) | 72 h | Repeat the prior payroll |

**Treatment (tracked in P01 and P07):** automate authorization failover and test it every six months (R-006, due 2027-03-31); fix the settlement DR runbook and run a test with both sponsor banks (R-007, due 2027-02-28); build a second-region standby for the gateway as part of the 2027 migration (R-008, due 2027-09-30).
