# Business Impact Analysis: Cris Santos Company Holdings | Finance and Insurance | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. (bank holding company) | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's operational resilience team with the three division continuity leads | **Fieldwork:** 2026-05-01 to 2026-07-31 | **Approved:** holding company board risk committee and bank board risk committee, 2026-09-10

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, data centers, cloud and network, email, the enterprise data platform, finance, HR).
- **Division BIAs:** Banking (focus), Financial Software and Data Services, and Commercial Real Estate. They are rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the bank's business continuity program and the "destruction, loss, or damage" measures the bank must consider under 12 CFR 30 App. B III.C.1.h;
- the Financial Software division's availability commitments to 310 client institutions and its SOC 2 Availability criteria (P09);
- the 4-hour test that triggers bank service provider notices (12 CFR 53.4, 225.303, 304.24) and the notification incident test for the bank and the holding company (12 CFR 53.2(b)(7), 225.301(b)(7));
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Shared corporate services are SYS-G1 identity, SYS-G2 SOC, SYS-G3 hybrid infrastructure (two group data centers plus landing zones in cloud providers A and B), and SYS-G4 email and collaboration. Division systems are the bank's core (SYS-B1), payments hub (SYS-B2), lending (SYS-B3), and branch and card platforms (SYS-B4); the Financial Software division's digital banking platform (SYS-S1) and data services platform (SYS-S2); and Commercial Real Estate's loan system (SYS-R1) and property management systems (SYS-R2). The SSP system in P02 is the Core and Digital Banking Platform (SYS-B1 plus SYS-S1). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: the bank earns about $61 million per business day, Financial Software about $6.4 million, and Commercial Real Estate about $4.8 million.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $50 million for the group, or more than 1 business day of a division's revenue | $5 million to $50 million | Less than $5 million |
| Operations | A division cannot deliver its core service (payments, deposits, the platform, loan funding) | One region, product, or channel stops | Staff slowed but working |
| Regulatory | Notification incident (12 CFR 53.3, 225.302), client bank notices (53.4), missed payment system or filing deadline, or SEC disclosure | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Staff or customer physical safety at branches and facilities (building security, alarms) | Degraded but safe | None |
| Reputation | National media, loss of client institutions, or supervisory attention | Regional media or complaints | Internal only |

Safety is rated only where a process affects physical security or building conditions; for purely digital processes it is N/A.

## 4. Process criticality and downtime
`bia.csv` lists 26 processes: 7 group shared services, 9 Banking, 5 Financial Software, and 5 Commercial Real Estate. 13 are High, 11 Moderate, and 2 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Data centers, cloud landing zones, and network | Group | High | 4 h | 2 h | 15 min |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-B01 Wire transfers | Banking | High | 4 h | 2 h | 15 min |
| BP-B03 Core deposit and loan processing | Banking | High | 8 h | 4 h | 15 min |
| BP-B05 Card authorization and ATM service | Banking | High | 4 h | 2 h | 1 h |
| BP-B02 ACH and real-time payments | Banking | High | 8 h | 4 h | 15 min |
| BP-B04 Digital banking for bank customers | Banking | High | 8 h | 4 h | 1 h |
| BP-B06 Contact center and fraud operations | Banking | High | 8 h | 4 h | 1 h |
| BP-S01 Digital banking platform service for client institutions | Financial Software | High | 4 h | 2 h | 1 h |
| BP-S02 Client support and client incident notices | Financial Software | High | 8 h | 4 h | 1 h |
| BP-R01 CRE loan closing and funding | Commercial Real Estate | High | 24 h | 8 h | 4 h |
| BP-R03 Physical access control and building security | Commercial Real Estate | High | 8 h | 4 h | 24 h |
| BP-G04 Email and collaboration | Group | Moderate | 24 h | 8 h | 4 h |
| BP-B09 Treasury management services | Banking | Moderate | 24 h | 12 h | 4 h |
| BP-B07 Consumer and small business lending | Banking | Moderate | 48 h | 24 h | 4 h |
| BP-R02 CRE loan servicing and investor remittance | Commercial Real Estate | Moderate | 48 h | 24 h | 4 h |
| BP-B08 BSA/AML monitoring and SAR filing | Banking | Moderate | 72 h | 24 h | 4 h |
| BP-S03 Cash-flow data service | Financial Software | Moderate | 48 h | 24 h | 24 h |
| BP-G05 Enterprise data platform and risk data aggregation | Group | Moderate | 72 h | 24 h | 4 h |
| BP-S04 Platform release pipeline | Financial Software | Moderate | 72 h | 24 h | 4 h |
| BP-G06 Financial close, regulatory, and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-R04 Building operations | Commercial Real Estate | Moderate | 24 h | 8 h | 24 h |
| BP-G07 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-S05 Client onboarding and core data conversion | Financial Software | Low | 120 h | 72 h | 24 h |
| BP-R05 Lease administration and tenant billing | Commercial Real Estate | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Payment system cutoffs and customer access to funds** drive the bank's 4 to 8 hour MTDs. Wires (BP-B01) have the shortest: correspondent and client settlement cannot wait past the day's cutoff, and an outage of that length is exactly what the notification incident test in 12 CFR 53.2(b)(7) asks about.
- **The 4-hour rule** drives the platform (BP-S01). A disruption of covered services for 4 hours or more obliges the division to notify every affected client bank (12 CFR 53.4(a)). An MTD of 4 hours means the notice duty and the business tolerance arrive together.
- **Loss exposure, not downtime,** drives CRE funding (BP-R01). A closing can be postponed a day; a wire sent on false instructions cannot be undone. That is why the process is High despite a 24-hour MTD.
- **RPO of 15 minutes** for core, wires, and ACH is met by synchronous replication between the two data centers. A lost posted transaction is worse than a delayed one.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all three divisions. Break-glass accounts per critical system are the fallback |
| Data centers and WAN (SYS-G3) | Group | Bank core, wires, ACH, branches | Two data centers in active and hot-standby modes; branches have cellular failover |
| Data center buildings | Commercial Real Estate | Group data centers | Physical access control and building systems for the data center buildings are run by Group Property Management (BP-R03). The data center team runs power and cooling |
| Digital banking platform (SYS-S1) | Financial Software | Bank digital banking (BP-B04), treasury management (BP-B09), business wire and ACH initiation | The bank is the platform's largest tenant; one platform outage hits the bank and 310 client institutions at once, and triggers both the bank's notification incident test and the division's client notices |
| Wire release (BP-B01) | Banking | CRE funding (BP-R01) | CRE Lending is a business customer of the bank. Its funding wires are released by bank wire operations; a fraudulent funding instruction becomes a bank wire (P08) |
| Cash-flow attributes (BP-S03) | Financial Software | Bank lending (BP-B07) | The AI credit model reads attributes from SYS-S2. Lending can continue manually |
| SOC facts (BP-G02) | Group | Every notice in P08 | OCC, Federal Reserve, client bank, state, SAR, and SEC clocks all depend on facts the SOC establishes |
| Email (SYS-G4) | Group | CRE closing, client support, treasury management | Not needed for payments to run, but the main channel attackers use to change payment instructions |

**Single points of failure found:** SYS-G1 (mitigated by break-glass accounts, tested quarterly); the payment initiation gateway between SYS-S1 and SYS-B2 runs as one cluster in the primary data center with a cold standby in the secondary (P01 BR-004); one alarm monitoring vendor for all branches (accepted, P01 RR-012).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 data centers | BP-B01, BP-B02, BP-B03, BP-B05 | Synchronous replication of core and payments databases to the secondary data center; immutable backups to the provider B vault |
| SYS-G3 landing zones | SYS-S1, SYS-S2, SYS-B3 model serving, enterprise data platform | Infrastructure as code; database replicas in the warm standby region; immutable backups in provider B |
| SYS-S1 digital banking platform | BP-B04, BP-B09, BP-S01 | Continuous replication to the warm standby region (RPO under 1 hour) |
| SYS-B4 card processing | BP-B05 | Card processor's own DR (contract and SOC 1 report) |
| SYS-R1 loan system (SaaS) | BP-R01, BP-R02 | Vendor replication; nightly export to the group vault |
| SYS-R2 access control and building automation | BP-R03, BP-R04 | Controller configuration backed up daily |
| People | All | Two wire rooms and three contact centers in different states; cross-trained platform operations in two locations |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Data centers, landing zones, and network
3. SOC visibility (SIEM, EDR, email security)
4. to 9. Bank wires, core processing, card and ATM, ACH, digital banking for bank customers, contact center and fraud
10. and 11. Platform service for client institutions and client notices (runs in provider A, so it often recovers in parallel with the bank's data center processes)
12. and 13. CRE loan funding (only with independent callbacks) and building security
14. to 26. Email, treasury management, lending, servicing, BSA/AML, the cash-flow data service, the enterprise data platform, the release pipeline, financial reporting, building operations, payroll, client conversions, and lease billing.

## 8. Key findings
1. **Shared services have shorter RTOs than any division process**, as they must. The identity RTO of 1 hour was met in two 2026 tests; the core failover RTO of 4 hours was met in the June 2026 semiannual test (2 hours 50 minutes).
2. **The platform's 4-hour MTD equals the regulatory notice trigger.** Any SYS-S1 outage or deliberate suspension that reaches 4 hours becomes a client notice event for up to 212 client banks and a notification incident question for the bank. P08 shows that a containment decision can start these clocks.
3. **The payment initiation gateway is a hidden single point of failure** for digital wires and ACH (P01 BR-004).
4. **Notification capacity is itself a process** (BP-G02, BP-S02, BP-G06). If the SOC, client support, or finance is down during an incident, notice clocks keep running. The P08 runbook uses out-of-band channels for this reason.
