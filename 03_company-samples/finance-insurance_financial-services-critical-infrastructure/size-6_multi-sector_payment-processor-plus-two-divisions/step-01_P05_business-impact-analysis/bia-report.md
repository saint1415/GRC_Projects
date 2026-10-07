# Business Impact Analysis: Cris Santos Company Holdings | Financial Services | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-01 to 2026-07-31 | **Approved:** board risk committee, 2026-09-10

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, data centers and network, cloud landing zones, the group data platform, email, finance, HR).
- **Division BIAs:** Payment Processing (focus), Payments Software Platform, and Merchant Consulting. They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the incident response plan's business recovery and continuity procedures, which PCI DSS 12.10.1 requires for each service provider CDE (the processor and the gateway);
- the "recover from" element of the incident response plan under the FTC Safeguards Rule (16 CFR 314.4(h));
- the **four-hour test** in the bank service provider notice rules (12 CFR 53.4; 225.303; 304.24): a computer-security incident that materially disrupts or degrades covered services to a sponsor bank for four or more hours must be reported to that bank as soon as possible;
- the Availability commitments in the Software division's SOC 2 report and the processor's first SOC 2 (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Corporate runs SYS-G1 identity, SYS-G2 SOC, SYS-G3 (two group data centers, landing zones in providers A and B, and the network), SYS-G4 the group data platform, and SYS-G5 email. The processor's CDE (SYS-P1 to SYS-P6) runs active-active in both data centers, with its e-commerce, portal, and dispute services in provider A. The Software division runs the commerce SaaS (SYS-S1), the gateway (SYS-S2), and device management (SYS-S3) in provider B. Merchant Consulting works mostly in the processor's dispute platform (SYS-P6), its own engagement tenant (SYS-M1), and clients' environments. See `../00_company-facts.md` sections 1, 3, and 7.

**Commitments that set the numbers:**
- Merchant agreements promise 99.95% monthly availability for authorization. Card network rules also expect continuous availability.
- Each sponsor agreement requires clearing and merchant funding files by the bank's daily cutoff. These are the covered services under the Bank Service Company Act (12 U.S.C. 1867(c)).
- Software terms promise 99.9% monthly availability for the gateway and point of sale; ISVs build their own commitments on top.
- Consulting dispute work must meet card network response windows that are counted in days.

## 3. Impact categories and values
Dollar values use the fictional revenue in `../00_company-facts.md` section 7: Payment Processing about $35.6 million per calendar day, the Software division about $9.3 million per calendar day, and Merchant Consulting about $6.4 million per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (authorization, settlement and funding, gateway, point of sale) | One channel, region, or service stops | Staff slowed but customers unaffected |
| Regulatory and card brand | Bank service provider notice, card brand compromise report, FTC notice, PCI DSS requirement not in place, or SEC disclosure | Missed card network deadline or contract service level | Internal policy deviation |
| Safety | Not applicable: no process affects physical safety | | |
| Reputation | Loss of a sponsor bank, a large ISV, or many merchants; national media | Merchant or client complaints; trade press | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 30 processes: 8 group shared services, 11 Payment Processing, 7 Software division, and 4 Merchant Consulting. 12 are High, 14 Moderate, and 4 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Data center and network operations | Group | High | 2 h | 30 min | 15 min |
| BP-G04 Cloud landing zones and hub network | Group | High | 4 h | 2 h | 1 h |
| BP-PP01 Card authorization | Payment Processing | High | 2 h | 30 min | 15 min |
| BP-PP02 Token vault and key services | Payment Processing | High | 2 h | 30 min | 15 min |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-PP05 E-commerce payment API and hosted fields | Payment Processing | High | 2 h | 1 h | 15 min |
| BP-SW01 Payment gateway and developer APIs | Software | High | 2 h | 1 h | 15 min |
| BP-SW02 Cloud point-of-sale service | Software | High | 4 h | 2 h | 15 min |
| BP-SW03 Online storefronts and checkout | Software | High | 4 h | 2 h | 1 h |
| BP-PP03 Clearing and settlement | Payment Processing | High | 24 h | 6 h | 1 h |
| BP-PP04 Merchant funding | Payment Processing | High | 24 h | 6 h | 1 h |
| BP-PP06 Fraud scoring | Payment Processing | Moderate | 24 h | 4 h | 4 h |
| BP-PP08 Merchant portal and virtual terminal | Payment Processing | Moderate | 24 h | 8 h | 1 h |
| BP-PP11 Sponsor bank and card network notices | Payment Processing | Moderate | 24 h | 8 h | 4 h |
| BP-SW06 ISV and merchant support and incident notices | Software | Moderate | 24 h | 8 h | 4 h |
| BP-PP10 Merchant support | Payment Processing | Moderate | 24 h | 8 h | 24 h |
| BP-MC01 Dispute management services | Merchant Consulting | Moderate | 72 h | 24 h | 4 h |
| BP-PP07 Chargebacks and disputes | Payment Processing | Moderate | 72 h | 24 h | 4 h |
| BP-G06 Email and collaboration | Group | Moderate | 24 h | 8 h | 4 h |
| BP-SW07 Software release pipeline | Software | Moderate | 72 h | 24 h | 4 h |
| BP-MC04 Client engagement records and communications | Merchant Consulting | Moderate | 48 h | 24 h | 24 h |
| BP-SW04 Point-of-sale device management | Software | Moderate | 48 h | 24 h | 24 h |
| BP-G05 Group data platform analytics and model training | Group | Moderate | 72 h | 24 h | 24 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-PP09 Merchant onboarding and underwriting | Payment Processing | Low | 120 h | 72 h | 24 h |
| BP-G08 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-MC02 Integration and implementation services | Merchant Consulting | Low | 120 h | 72 h | 24 h |
| BP-SW05 Merchant insights assistant (AI feature) | Software | Low | 120 h | 72 h | 24 h |
| BP-MC03 Advisory and PCI readiness services | Merchant Consulting | Low | 168 h | 120 h | 24 h |

**What drives the values:**
- **Authorization is real time.** About 80 million authorizations a day pass through SYS-P1, the token vault, and the card network links. There is no manual workaround for card-not-present sales, and large merchants move volume to backup processors within hours. That is why BP-PP01, BP-PP02, BP-G03, and both e-commerce paths (BP-PP05, BP-SW01) have 2-hour MTDs.
- **Settlement and funding run on a daily cycle, and they are the covered services.** A 6-hour RTO keeps each sponsor bank's cutoff reachable. Any incident that disrupts them for 4 or more hours triggers a notice to the affected bank under the rule for that bank's regulator.
- **The gateway is the Software division's authorization.** Its 2-hour MTD equals the processor's because about 70% of its traffic feeds BP-PP01.
- **Dispute work is measured in days, not hours.** Card network response windows allow a 72-hour MTD for BP-MC01 and BP-PP07, but adjustments also feed the next funding file.
- **Notice capacity is itself a process** (BP-PP11, BP-SW06, BP-G02, BP-G07). If the SOC, the bank liaison team, or email is down during an incident, notice clocks keep running.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops administration and operations in all three divisions. Authorization keeps running without workforce sign-in; break-glass accounts cover recovery |
| Data centers and card network links (SYS-G3) | Group | Processor CDE | Active-active design; the semiannual failover test passed on 2026-04-18 |
| Gateway traffic (SYS-S2) | Software | Processor authorization (BP-PP01) | About 70% of gateway transactions route to the processor; a gateway outage is a processor revenue outage |
| Hosted payment fields (SYS-P4) | Processor | Software storefronts (BP-SW03) | Storefronts for processor merchants cannot take cards without them |
| Payment HSMs (SYS-P2) | Processor | Software device management (BP-SW04) | Device keys are loaded through the processor's HSMs |
| Dispute platform (SYS-P6) | Processor | Merchant Consulting dispute services (BP-MC01) | 2,400 consulting analysts work inside the processor's CDE |
| Dispute adjustments | Merchant Consulting and processor | Merchant funding (BP-PP04) | Late or wrong adjustments change the funding file a sponsor bank receives |
| SYS-M1 federation | Merchant Consulting | SYS-G1 and the CDE | The acquired firm's identity provider is a path into the CDE (scenario gap 1) |
| SOC facts (SYS-G2) | Group | Every notice in P08 | Every clock depends on the SOC establishing what happened |

**Single points of failure found:**
- **The gateway runs active in one provider B region** (scenario gap 8). The warm standby has not been failed over since 2025-04, so its 1-hour RTO is unproven (P01 SW-004).
- **SYS-M1 is outside the group identity platform.** If it is compromised, the attacker inherits federated access to SYS-P6 (P01 MC-001, GR-02).
- **Sponsor bank contacts.** Notice to Banks B and D depends on fallback contacts because designated contacts are missing (scenario gap 4).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 data centers | BP-PP01 to BP-PP04 | Active-active authorization and vault; synchronous replication inside each data center and asynchronous between them (seconds); settlement database log shipping every 15 minutes |
| SYS-P2 payment HSM clusters | BP-PP01, BP-PP02, BP-SW04 | One cluster per data center; key backups under dual control in tamper-evident storage |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in the provider B vault (provider A workloads) and provider A vault (provider B workloads) |
| SYS-S2 gateway | BP-SW01 | Database replicas to a warm standby region; failover untested since 2025-04 |
| SYS-S1 commerce SaaS | BP-SW02, BP-SW03 | Point-in-time recovery; point-of-sale offline mode on devices |
| SYS-P6 dispute platform | BP-PP07, BP-MC01 | Point-in-time recovery; daily immutable backups |
| SYS-G4 data platform | BP-G05, BP-PP06 | Daily immutable backups |
| People | All | Cross-trained teams in four operations centers; remote work for dispute analysts and support |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Data centers, network, and card network links
3. Cloud landing zones and hub network
4. to 5. Card authorization, token vault, and key services
6. SOC visibility (SIEM, EDR, DNS and egress monitoring)
7. to 10. E-commerce API and hosted fields, the gateway, point of sale, and storefronts
11. to 12. Clearing and settlement, then merchant funding (each sponsor bank's cutoff)
13. to 30. Fraud scoring, merchant portal, bank and network notices, ISV and merchant notices, merchant support, dispute services and chargebacks, email, the release pipeline, consulting records, device management, the data platform, financial close, onboarding, payroll, integration services, the AI assistant, and advisory services.

## 8. Key findings
1. **Shared services set the floor.** Identity, data centers, and landing zones have RTOs equal to or shorter than any division process that depends on them, as they must.
2. **The gateway's recovery is unproven** (gap 8). Its RTO of 1 hour depends on a failover not tested since 2025-04 (P01 SW-004; POAM-019).
3. **The processor's own recovery is proven.** Authorization and the token vault failed over between data centers within 22 minutes in the 2026-04-18 test, inside the 30-minute RTO.
4. **A consulting outage becomes a funding issue.** Dispute adjustments made by consulting analysts feed the funding files; the four-hour test in 12 CFR 53.4 and its parallels can be triggered by containment actions in another division (P08 scenario).
5. **Notification capacity needs out-of-band channels.** The P08 runbook uses a crisis line and printed contact lists because email and chat may be watched by an attacker.
