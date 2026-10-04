# Business Impact Analysis: Cris Santos Company Holdings | Wholesale Trade | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board audit and risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud and network, the group ERP, the EDI and integration hub, finance, HR).
- **Division BIAs:** IT Distribution (focus), Logistics and Warehousing, and Online Retail. They are rows in the same workbook (`bia.csv`, `division` column), so cross-division dependencies show in one place.

It supports:
- the availability rating of the Order-to-Fulfillment Platform in the SSP (P02);
- impact ratings in the group and division risk registers (P01);
- the recovery order in the incident runbook (P08);
- contract commitments: 3PL client service levels (Logistics), DoD installation schedules under prime subcontracts (IT Distribution), and payment brand rules for the storefront (Online Retail);
- the Availability category of the Logistics 3PL SOC 2 readiness work (P09).

No federal continuity rule applies to a distributor, warehouse operator, or online retailer. The drivers below are revenue, contracts, worker safety, and notice clocks.

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and network, SYS-G4 group ERP, SYS-G5 EDI and integration hub, and SYS-G6 data platform. Division systems are SYS-D1 to SYS-D4 (IT Distribution: reseller portal, Federal Fulfillment Enclave, Lifecycle Services platform, forecasting), SYS-D5 to SYS-D7 (Logistics: WMS, TMS, DC automation), and SYS-D8 to SYS-D10 (Online Retail: storefront, contact center, marketplace). See `../00_company-facts.md` sections 3 and 7.

The key structural fact: **Logistics physically handles every product the group sells.** The 9 DCs receive, store, and ship for IT Distribution, Online Retail, and about 140 3PL clients, and the two federal integration centers sit inside DC-1 and DC-6. A DC or WMS outage is therefore a three-division outage.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: IT Distribution about $34.5 million per day, Online Retail about $11 million per day, Logistics about $3.8 million per day of external 3PL revenue.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue lost (not just delayed) | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot take, fulfill, or ship orders | One DC, channel, or service line stops | Staff slowed but working |
| Regulatory | Missed DoD reporting or delivery duty, reportable breach, or SEC disclosure | Missed contractual or internal deadline | Internal policy deviation |
| Safety | Plausible worker injury (DC automation restarts, fleet) | Unsafe conditions contained by procedure | None |
| Reputation | National media, loss of major resellers, primes, or 3PL clients | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 26 processes: 8 group shared services, 6 IT Distribution, 6 Logistics, and 6 Online Retail. 15 are High, 9 Moderate, and 2 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones, hub network, and keys | Group | High | 4 h | 2 h | 1 h |
| BP-G04 Wide-area network and site connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-OR01 Storefront, mobile app, and checkout | Online Retail | High | 4 h | 2 h | 1 h |
| BP-OR02 Payment authorization | Online Retail | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-LW02 Pick, pack, and ship | Logistics | High | 8 h | 4 h | 1 h |
| BP-LW03 DC automation | Logistics | High | 8 h | 4 h | 24 h |
| BP-G05 Group ERP order-to-cash and procure-to-pay | Group | High | 12 h | 4 h | 1 h |
| BP-ID01 Order capture: reseller portal, EDI, and quoting | IT Distribution | High | 12 h | 4 h | 1 h |
| BP-G06 EDI and integration hub | Group | High | 12 h | 4 h | 1 h |
| BP-LW04 Transportation management and fleet dispatch | Logistics | High | 12 h | 6 h | 4 h |
| BP-LW05 3PL client fulfillment and client portal | Logistics | High | 12 h | 6 h | 1 h |
| BP-LW01 Receiving and inbound inspection | Logistics | High | 24 h | 8 h | 4 h |
| BP-ID03 Federal order management and integration | IT Distribution | High | 48 h | 24 h | 4 h |
| BP-OR04 Contact center and phone orders | Online Retail | Moderate | 24 h | 8 h | 4 h |
| BP-OR03 Order fraud screening | Online Retail | Moderate | 24 h | 8 h | 4 h |
| BP-ID04 Section 889 and compliance screening | IT Distribution | Moderate | 24 h | 8 h | 4 h |
| BP-ID02 Purchasing, supplier management, and automated reordering | IT Distribution | Moderate | 48 h | 24 h | 4 h |
| BP-OR05 Marketplace seller management and payouts | Online Retail | Moderate | 72 h | 24 h | 4 h |
| BP-LW06 Import entries and customs filings | Logistics | Moderate | 72 h | 24 h | 24 h |
| BP-ID05 Lifecycle Services and ITAD | IT Distribution | Moderate | 72 h | 48 h | 24 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-G08 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-OR06 Returns and refurbishment | Online Retail | Low | 120 h | 72 h | 24 h |
| BP-ID06 Pricing, vendor rebates, and programs | IT Distribution | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Lost versus delayed revenue.** Online Retail loses sales outright during an outage (consumers buy elsewhere), so the storefront and payments have 4-hour MTDs. Reseller orders are mostly delayed for the first half day, so order capture and the ERP have 12-hour MTDs.
- **Carrier cut-offs and client service levels** drive the WMS (BP-LW02) and 3PL fulfillment (BP-LW05). 3PL clients also rely on the WMS inventory record for their own financial statements, which is why the division issues a SOC 1 report.
- **Worker safety** drives DC automation (BP-LW03). Restarting conveyors and sortation after an uncontrolled stop needs lockout and checks. Its RPO is 24 hours because PLC programs change rarely and are backed up after each change.
- **Federal duties** make BP-ID03 High even though it tolerates 48 hours: DoD installation schedules, CUI safeguarding, and the 72-hour DFARS reporting clock continue during an outage.
- **Screening is a gate, not a convenience.** If Section 889 screening (BP-ID04) is down, federal and export orders are held, never released unscreened.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | One identity outage stops all three divisions. Break-glass accounts per critical system are the fallback; FFE users have a separate government-community tenant |
| Group ERP (BP-G05) | Group | Every division | Orders from the reseller portal and the storefront both release to the WMS through the ERP |
| WMS and DCs (BP-LW02, BP-LW01) | Logistics | IT Distribution, Online Retail, 3PL clients | Every shipment leaves a Logistics DC. The integration centers ship DoD jobs through the WMS |
| DC buildings and badge systems | Logistics | IT Distribution integration centers and Lifecycle Services | Physical protection of CUI at IC-1 and IC-2 is partly provided by Logistics; it is in the CMMC assessment scope (P02, P03) |
| Receiving inspection (BP-LW01) | Logistics | IT Distribution, Online Retail | The authenticity check that stops tampered or counterfeit stock is run by one division for all (P08) |
| EDI hub (BP-G06) | Group | Order capture, receiving, supplier catalogs | Advance ship notices drive DC receiving; a tampered notice is the P08 entry path |
| Purchasing (BP-ID02) | IT Distribution | Online Retail | One purchasing team and the AI-001 forecasts buy for both divisions |
| SOC facts (BP-G02) | Group | DoD, prime, customer, state, and SEC notices | Every notice clock in P08 depends on the SOC establishing what happened |
| Data platform (SYS-G6) | Group | AI-001 forecasts, Online Retail fraud screening | Not needed for same-day operations, so Moderate; outages degrade decisions rather than stop them |

**Single points of failure found:**
- SYS-G1 (mitigated by break-glass accounts, tested quarterly).
- The single WMS instance for all 9 DCs (P01 LW-004). A regional failover exists, but a WMS application defect or ransomware would stop every DC.
- One payment service provider for the storefront. The secondary route is configured but has never been tested (P01 OR-009).
- Three automation vendors with persistent remote access to DC OT (P01 LW-001; gap 6).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in a separate provider B account |
| SYS-G4 group ERP (SaaS) | BP-G05, BP-ID01, BP-ID02, BP-G07 | Vendor replication (RPO 15 minutes per contract); nightly export to the group vault |
| SYS-G5 EDI hub | BP-G06, BP-LW01 | Value-added network retains messages 7 days; hourly snapshots of the integration layer |
| SYS-D5 WMS (provider A) | BP-LW01, BP-LW02, BP-LW05 | Database replica in a second region; hourly snapshots to the immutable vault; restore tested quarterly |
| SYS-D7 DC automation | BP-LW03 | PLC program backups after each change, held by the OT engineering team; not yet in the group vault at 4 DCs |
| SYS-D8 storefront (provider A) | BP-OR01 | Multi-zone deployment; database point-in-time recovery |
| SYS-D2 FFE (provider B government-community) | BP-ID03 | Snapshots every 4 hours to a vault in the same government-community region |
| People | All | Cross-trained DC teams; inside sales take orders by phone; contact center agents work remotely |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones, hubs, and keys
3. WAN and DC connectivity
4. Group ERP
5. Storefront and checkout, then payment authorization (priorities 5 and 6; both run in provider A and often recover in parallel)
7. to 10. Pick-pack-ship, order capture, EDI hub, security monitoring
11. to 15. DC automation, receiving, transportation, 3PL fulfillment, federal integration
16. to 26. Purchasing, contact center, fraud screening, compliance screening, marketplace, imports, Lifecycle Services, financial close, returns, payroll, and pricing.

Section 889 screening (BP-ID04) is placed after order capture because federal orders are held, not shipped, until it is back.

## 8. Key findings
1. **Logistics is the group's operational single point of failure.** Every division's revenue leaves through the same 9 DCs and one WMS. WMS restore tests pass quarterly, but no test has covered a ransomware scenario that also hits the WMS replica (P01 GR-02).
2. **DC automation recovery is not in the group backup design.** PLC programs at 4 DCs are backed up only on OT engineers' laptops (P01 LW-003; P07 CP-9).
3. **The storefront's secondary payment route is untested**, so the 2-hour RTO for payment authorization is a plan, not a demonstrated capability (P01 OR-009).
4. **Notification capacity is itself a process.** If the SOC, the two certificate holders, or the contracts team are unavailable, the 72-hour DIBNet clock still runs. P08 adds two more certificate holders and an out-of-band contact list.
