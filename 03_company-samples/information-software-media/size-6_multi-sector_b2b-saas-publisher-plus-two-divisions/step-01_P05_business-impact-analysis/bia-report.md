# Business Impact Analysis: Cris Santos Company Holdings | Information | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-17

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud landing zones and keys, CI/CD, the group data platform, finance, and HR).
- **Division BIAs:** Cloud Software (focus), Technology Consulting, and Payments and Payroll. They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the availability commitments in the Workforce Cloud MSA (99.95% monthly) and SOC 2 report (P09);
- the incident response plan and testing duties of the FTC Safeguards Rule for Payments and Payroll (16 CFR 314.4(h)) and PCI DSS requirement 12.10;
- client service levels for consulting's managed application services;
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud platform (landing zones in providers A and B, CI/CD, secrets, data platform), and SYS-G4 corporate SaaS. Division systems are SYS-D1 (the Workforce Cloud Platform, WCP), SYS-D2 (consulting delivery systems), SYS-D3 (payroll engine), and SYS-D4 (payments platform). See `../00_company-facts.md` sections 3 and 7.

The divisions are closely linked. Workforce Cloud captures the hours and direct deposit details that Payments and Payroll pays out, and consultants implement most new Workforce Cloud tenants. An outage or breach in one division usually reaches another.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Cloud Software about $24.7 million per day, Technology Consulting about $14.8 million per day, and Payments and Payroll about $9.9 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (WCP, payroll, payments, managed services) | One service line, region, or client group stops | Staff slowed but working |
| Regulatory and contractual | Reportable breach, bank or sponsor bank notice, SEC disclosure, or missed tax deadline | Missed SLA or contract deadline | Internal policy deviation |
| Safety and worker harm | Workers paid late or not at all; hospitals lose staffing data | Delayed but recoverable | None |
| Reputation | National media, loss of enterprise customers, regulator attention | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 26 processes: 7 group shared services, 8 Cloud Software, 5 Technology Consulting, and 6 Payments and Payroll. 11 are High, 11 Moderate, and 4 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones, network, and keys | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-PY03 Card and ACH payment acceptance | Payments and Payroll | High | 2 h | 1 h | 1 h |
| BP-SW01 Workforce Cloud scheduling and time capture | Cloud Software | High | 4 h | 2 h | 1 h |
| BP-PY01 Payroll processing and direct deposit | Payments and Payroll | High | 12 h | 4 h | 1 h |
| BP-SW03 Payroll and HR export and integration service | Cloud Software | High | 12 h | 4 h | 1 h |
| BP-SW02 Employee self-service mobile app | Cloud Software | High | 8 h | 4 h | 1 h |
| BP-PY04 Settlement and merchant funding | Payments and Payroll | High | 24 h | 8 h | 1 h |
| BP-IC02 Managed application services | Technology Consulting | High | 8 h | 4 h | 4 h |
| BP-SW04 Public APIs and partner integrations | Cloud Software | Moderate | 24 h | 8 h | 1 h |
| BP-PY02 Payroll tax calculation, deposits, and filing | Payments and Payroll | High | 48 h | 24 h | 4 h |
| BP-SW05 Customer support and incident notices | Cloud Software | Moderate | 24 h | 8 h | 4 h |
| BP-IC04 Health-system staffing integrations | Technology Consulting | Moderate | 24 h | 8 h | 4 h |
| BP-G04 Source hosting and CI/CD release pipeline | Group | Moderate | 72 h | 24 h | 4 h |
| BP-SW06 Tenant provisioning and implementation | Cloud Software | Moderate | 72 h | 24 h | 4 h |
| BP-IC01 Client implementation and data migration projects | Technology Consulting | Moderate | 72 h | 24 h | 24 h |
| BP-PY05 Merchant onboarding and risk scoring | Payments and Payroll | Moderate | 72 h | 24 h | 4 h |
| BP-G05 Group data platform and reporting | Group | Moderate | 72 h | 24 h | 4 h |
| BP-IC03 Federal engagement delivery | Technology Consulting | Moderate | 72 h | 48 h | 24 h |
| BP-G06 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-SW07 Workforce assistant (generative AI feature) | Cloud Software | Low | 72 h | 24 h | 24 h |
| BP-G07 Group workforce payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-SW08 Attrition-risk insights and analytics | Cloud Software | Low | 120 h | 72 h | 24 h |
| BP-IC05 Time, expense, and client billing | Technology Consulting | Low | 120 h | 72 h | 24 h |
| BP-PY06 Disputes and chargebacks | Payments and Payroll | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Merchants at the point of sale** drive card acceptance (BP-PY03) to the shortest MTD in the group, 2 hours. There is no manual path inside the division.
- **Shift workers clocking in** drive the WCP (BP-SW01). The MSA promises 99.95% monthly availability, which allows about 22 minutes of downtime a month. About 420 bank customers use the WCP for their own staff, so a disruption of 4 hours or more may also require bank service provider notices (12 CFR 53.4; P08).
- **Workers' pay** drives payroll (BP-PY01) and the handoff that feeds it (BP-SW03). The binding limit is sponsor bank A's ACH origination cutoff, not the system itself. A missed cutoff means about 2.4 million workers may be paid late.
- **Client service levels** drive consulting's managed application services (BP-IC02). Project work (BP-IC01, BP-IC03) can pause for days.
- **AI features are optional.** The workforce assistant and attrition-risk insights (BP-SW07, BP-SW08) can be switched off without stopping any customer's operations.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all three divisions at once. Break-glass accounts per critical system and cloud account are the fallback. The 2,600 consultants from the acquired firm still sign in through their own identity provider (gap 9), which is a second point of failure for them |
| Landing zones and keys (SYS-G3) | Group | WCP, payroll engine, payments platform | Group-managed keys protect every division's data. Losing key access stops all encrypted services |
| Payroll handoff (BP-SW03) | Cloud Software | Payments and Payroll (BP-PY01) | Hours and direct deposit details come from the WCP each night. If the handoff is late, payroll is late |
| Direct deposit changes (BP-SW02) | Cloud Software | Payments and Payroll | Account changes entered in the app are a known fraud path (P01 PY-006) |
| Checkout pages (BP-PY03) | Payments and Payroll | Cloud Software customers | Checkout is embedded in WCP pages; a WCP outage also stops merchants' online payments |
| Migration toolkit (BP-IC01) | Technology Consulting | WCP tenants (BP-SW06) | Consultants load customer data into new tenants with static keys (gap 1). This is the entry point in the P08 scenario |
| SOC facts (BP-G02) | Group | All notices | Every notice clock in P08 depends on the SOC establishing what happened |
| Customer notices (BP-SW05) | Cloud Software | About 38,000 customers and 420 bank customers | DPA clocks of 72 hours, or 48 hours for about 1,240 customers |

**Single points of failure found:** SYS-G1 (mitigated by break-glass accounts tested quarterly); sponsor bank A for ACH origination (P01 PY-009, contingency bank agreement in negotiation); the single WCP export bucket that both the payroll engine and third-party payroll providers read (P01 SW-003).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | All cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| SYS-D1 WCP (provider A) | BP-SW01 to BP-SW08 | Database replicas to a warm standby region; point-in-time recovery; daily immutable backups to provider B; restore tested twice a year |
| SYS-D3 payroll engine (provider B) | BP-PY01, BP-PY02 | Synchronous replicas across zones; immutable backups; pay-run journals |
| SYS-D4 payments platform (provider B, CDE accounts) | BP-PY03 to BP-PY06 | Active-active across two zones; tokenization vault replicated |
| SYS-D2 consulting delivery systems | BP-IC01 to BP-IC05 | Collaboration SaaS retention; migration toolkit rebuilt from code |
| People | All | Cross-trained teams; payroll operations centers in two states; remote work for consultants |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones, network, and keys
3. SOC visibility (SIEM and EDR)
4. Card and ACH payment acceptance
5. WCP scheduling and time capture
6. Payroll processing and direct deposit
7. WCP payroll and HR export service
8. Employee self-service mobile app
9. Settlement and merchant funding
10. Managed application services
11. to 26. APIs, payroll tax, customer support, health-system integrations, CI/CD, tenant provisioning, implementation projects, merchant onboarding, the data platform, federal delivery, financial close, the workforce assistant, group payroll and HR, attrition-risk insights, consultant billing, and disputes.

## 8. Key findings
1. **RTOs for shared services are shorter than any division's, as they must be.** Group identity (RTO 1 hour) met its target in both 2026 failover tests.
2. **Payroll depends on the WCP more than either division's continuity plan admits.** The payroll engine has its own recovery design, but without the WCP handoff it has no current hours or bank details. The two continuity plans were written separately (P07 CP-2 finding; POAM-024).
3. **The export service is High for availability and High for confidentiality.** Its recovery is urgent, and so is its protection: the handoff files are the most sensitive data in the WCP (gap 2; P01 SW-003; the P08 scenario).
4. **Notification capacity is itself a process** (BP-SW05, BP-G02, BP-G06). If the SOC or the support desk is down during an incident, the 48-hour and 72-hour customer clocks keep running. The P08 runbook uses out-of-band channels for this reason.
