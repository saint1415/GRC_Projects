# Business Impact Analysis: Cris Santos Company Holdings | Other Services | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-01 to 2026-07-31 | **Approved:** board risk committee, 2026-09-10

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud and network, the customer engagement platform, finance, HR).
- **Division BIAs:** Device Repair (focus), Electronics Retail, and IT Support Services. They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the availability rating of the STPP security plan (P02) and the recovery order in the incident runbook (P08);
- impact ratings in the group and division risk registers (P01);
- the availability commitments in IT Support's SOC 2 report and the service levels in Device Repair's enterprise and TPA agreements (P09);
- PCI DSS v4.0.1 Requirement 12.10.1, which expects the incident response plan to include business recovery and continuity procedures, for both merchants (P03).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud, network, and colocation data centers, SYS-G4 customer engagement platform, and SYS-G5 ERP and HR. Division systems are SYS-D1 (the STPP) and SYS-D2 (repair bench and depot technology) for Device Repair, SYS-D3 (commerce and payments) and SYS-D4 (store infrastructure) for Electronics Retail, and SYS-D5 (RMM, PSA, remote support, credential vault, managed backup) for IT Support. See `../00_company-facts.md` sections 1 and 3.

The divisions are tied together in four places that matter for continuity:
- **The 260 in-store repair counters** are Device Repair operations inside retail stores. They use the STPP for tickets, retail store networks for connectivity, and retail POS lanes for payment.
- **Protection plans** are sold by Retail and fulfilled by Device Repair through the TPA.
- **Trade-ins** are bought by Retail and sanitized by Device Repair depots before resale.
- **IT Support in-home technicians** open device repair tickets in the STPP and install products that Retail sells.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 1: Electronics Retail about $34.5 million per day, Device Repair about $10.7 million per day, and IT Support about $4.1 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (sell, repair, support) | One region, channel, or service line stops | Staff slowed but working |
| Regulatory and contractual | Reportable breach, card brand compromise case, SEC disclosure, or a breached business associate agreement | Missed internal or contractual service level | Internal policy deviation |
| Safety | Plausible harm to people (for example, a customer business that cannot reach its systems in an emergency) | Delayed but safe | None |
| Reputation | National media, loss of a manufacturer authorization or the TPA contract, or regulator attention | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 27 processes: 7 group shared services, 9 Device Repair, 6 Electronics Retail, and 5 IT Support. 12 are High, 12 Moderate, and 3 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and hub network | Group | High | 4 h | 2 h | 1 h |
| BP-G04 Wide-area network and store connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-ER01 Store checkout and payments | Retail | High | 4 h | 2 h | 1 h |
| BP-DR01 Repair intake, ticketing, and device release | Device Repair | High | 8 h | 4 h | 1 h |
| BP-DR02 Repair store payments | Device Repair | High | 8 h | 4 h | 1 h |
| BP-ER02 Website and app ordering | Retail | High | 8 h | 4 h | 1 h |
| BP-IT01 Managed IT services delivery | IT Support | High | 8 h | 4 h | 1 h |
| BP-DR03 Bench diagnostics and repair | Device Repair | High | 12 h | 8 h | 24 h |
| BP-IT03 Managed backup and recovery for customers | IT Support | High | 24 h | 8 h | 4 h |
| BP-DR04 Protection plan claim fulfillment | Device Repair | High | 24 h | 12 h | 4 h |
| BP-G05 Customer accounts, contact center, and chatbot | Group | Moderate | 24 h | 8 h | 4 h |
| BP-IT02 Consumer remote and in-home support | IT Support | Moderate | 24 h | 8 h | 4 h |
| BP-IT04 Customer incident notices | IT Support | Moderate | 24 h | 8 h | 4 h |
| BP-ER03 Order fulfillment, delivery, and pickup | Retail | Moderate | 24 h | 12 h | 4 h |
| BP-ER06 Protection plan and subscription sales | Retail | Moderate | 48 h | 24 h | 4 h |
| BP-DR06 Mail-in and enterprise depot repair | Device Repair | Moderate | 48 h | 24 h | 4 h |
| BP-DR05 Manufacturer warranty repair and parts | Device Repair | Moderate | 48 h | 24 h | 4 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-DR07 Data recovery and data transfer | Device Repair | Moderate | 72 h | 48 h | 24 h |
| BP-DR08 Trade-in and recycling sanitization | Device Repair | Moderate | 72 h | 48 h | 24 h |
| BP-ER04 Trade-in intake | Retail | Moderate | 72 h | 24 h | 24 h |
| BP-G06 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-DR09 AI-assisted diagnostics | Device Repair | Low | 72 h | 24 h | 24 h |
| BP-ER05 Loyalty and promotions | Retail | Low | 72 h | 48 h | 24 h |
| BP-IT05 AI remediation agent pilot | IT Support | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Custody of customer devices** drives Device Repair's 8-hour MTD for intake and release (BP-DR01). About 30,000 tickets a day move through the STPP, and a device must be released only to its owner. Paper claim tags work for hours, not days.
- **Payment scope** drives both merchants' payment processes (BP-DR02, BP-ER01). Degraded modes must not create new card data (no paper card numbers, no keyed entry outside P2PE terminals), or a short outage becomes a PCI DSS scope problem.
- **Customers' own security** drives IT Support's managed services (BP-IT01) and managed backup (BP-IT03). An RMM outage stops patching and monitoring for 4,200 businesses, including 610 medical and dental practices whose ePHI the division protects as a business associate.
- **Quality more than uptime** drives AI-assisted diagnostics (BP-DR09). It can be switched off without stopping repairs, but its outputs decide liquid damage flags that affect warranty coverage (P10).

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all three divisions at once. Break-glass accounts per critical system are the fallback |
| WAN and store connectivity | Group | Repair stores, retail stores, depots | The STPP and the retail payment switch are only as available as store connectivity; P2PE terminals fail over to cellular |
| SOC facts (SYS-G2) | Group | Every notice in P08 | The 24-hour acquirer and manufacturer clocks and the 4-business-day SEC clock depend on the SOC establishing what happened |
| In-store repair counters | Device Repair | Retail stores | Counter tickets use the STPP, retail store networks (SYS-D4), and retail lanes for payment. A retail network outage stops 260 counters; a counter compromise can reach retail lanes where segmentation failed (P03, P08) |
| Protection plan claims (BP-DR04) | Device Repair | Retail customers and the TPA | Retail sells the plans; Device Repair fulfills them. A repair outage becomes a retail reputation problem |
| Trade-in sanitization (BP-DR08) | Device Repair | Retail trade-in program (BP-ER04) | Retail cannot resell a trade-in until Device Repair certifies sanitization |
| Device tickets for in-home visits | IT Support | STPP (BP-DR01) | About 4% of tickets start in a customer's home |
| Customer accounts and chatbot (BP-G05) | Group | All three divisions | One sign-in and one chatbot for repair status, orders, and subscriptions. Not needed to repair or sell in stores, so Moderate |

**Single points of failure found:**
- SYS-G1 (mitigated by break-glass accounts, tested quarterly).
- The TPA interface: one integration carries 38% of repair volume (P01 DR-014).
- The RMM: one console reaches 310,000 customer endpoints, so it is a concentration risk for customers as well as an availability risk (P01 GR-03, IT-001).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| STPP (SYS-D1) on provider A | BP-DR01, BP-DR02, BP-DR04 to BP-DR06 | Managed database with point-in-time recovery; warm standby in provider B (read-only intake first); daily immutable backups |
| Bench workstations (SYS-D2) | BP-DR03, BP-DR07 | Rebuilt from the gold image; no customer data is meant to stay on benches (P03 gap 2) |
| Data recovery lab storage (SYS-D2) | BP-DR07 | Nightly backup to the provider B vault for open cases only |
| Retail payment switch and POS (SYS-D3) | BP-ER01 | Active-active in the two colocation data centers |
| RMM and PSA (SYS-D5, vendor SaaS) | BP-IT01, BP-IT02, BP-IT04 | Vendor multi-region service; configuration and scripts exported daily to provider B |
| Managed backup service (SYS-D5) | BP-IT03 | Customer backups in provider B with immutability; storage replicated across two regions |
| People | All | Cross-trained teams; depots can absorb mail-in work from a closed region |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones and hub network
3. WAN and store connectivity
4. SOC visibility (SIEM and EDR)
5. Retail checkout and payments
6. to 7. Repair intake and release, and repair store payments (the STPP)
8. Retail website and app
9. IT Support managed services (RMM)
10. Bench diagnostics and repair
11. to 12. Managed backup for customers, and protection plan claims
13. to 27. Customer accounts and chatbot, consumer support, customer incident notices, fulfillment, plan sales, depot repair, warranty repair, finance, data recovery, sanitization, trade-in intake, payroll, AI diagnostics, loyalty, and the AI agent pilot.

## 8. Key findings
1. **RTOs for shared services are shorter than any division's**, as they must be. The group identity RTO of 1 hour was met in two tests in 2026.
2. **The STPP standby has never carried full intake.** Failover to provider B was tested read-only in March 2026. Full intake and release from the standby is untested (POAM-019).
3. **The in-store counters are a continuity and a security dependency.** They depend on retail networks to work, and that same connection is the path P08 uses for the point-of-sale compromise. Segmentation fixes (POAM-009) must keep counter connectivity working.
4. **Notification capacity is itself a process** (BP-G02, BP-IT04, BP-G07). If the SOC or the PSA is down during an incident, the 24-hour acquirer, manufacturer, and TPA clocks keep running. The P08 runbook uses out-of-band channels for this reason.
5. **Sanitization is Moderate for availability but carries Severe regulatory impact.** Its recovery can wait; its quality cannot (P03 gap 4).
