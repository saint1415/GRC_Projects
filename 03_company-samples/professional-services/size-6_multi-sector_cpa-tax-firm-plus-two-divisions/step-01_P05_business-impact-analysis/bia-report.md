# Business Impact Analysis: Cris Santos Company Holdings | Professional Services | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the division continuity leads (Tax and Advisory, CPA Partners, Wealth, Practice Cloud) | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-10

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud and network, email, finance, HR).
- **Division BIAs:** CPA and Tax Services (focus; Tax and Advisory plus the CPA Partners attest practice), Wealth Management, and Practice Management Software. They are rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the recovery parts of Tax and Advisory's written incident response plan (16 CFR 314.4(h)) and the asset prioritization in 314.4(c)(2) ("in accordance with their relative importance to business objectives");
- Wealth's Regulation S-P response program (17 CFR 248.30(a)(3)) and its business continuity planning under its compliance program;
- Practice Cloud's availability commitments in its SOC 2 report (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and office network, and SYS-G4 email. Division systems are SYS-T1 (tax preparation and e-file), SYS-T2 (client accounting services), SYS-T3 (attest platform), SYS-W1 (Wealth platform), and SYS-S1 (Practice Cloud, which also hosts Tax and Advisory's client portal). See `../00_company-facts.md` sections 3 and 7.

**The tax calendar drives the focus division.** About 62% of Tax and Advisory revenue is billed from February through April. The values for tax processes are **peak-season** values (mid-January to April 15, and October 1 to 15). Outside those windows the MTD for BP-T01 and BP-T02 relaxes to 72 hours. Wealth runs on market hours all year. Practice Cloud's peak follows its customers' filing season.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Tax and Advisory about $92 million per business day in season (about $38 million on average), Wealth about $21 million per business day, and Practice Cloud about $14 million per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 business day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (returns, payroll, trading, the Practice Cloud service) | One region, office group, or service line stops | Staff slowed but working |
| Regulatory | Missed filing deadlines for many clients, a reportable data breach (FTC, IRS, SEC, states), or an SEC disclosure | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Not applicable. No group process affects physical safety; harm to clients is financial and is scored under Regulatory and Reputation | | |
| Reputation | National media, loss of Practice Cloud customers or advisers, or regulator attention | Regional media or client complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 27 processes: 7 group shared services, 11 CPA and Tax Services (10 Tax and Advisory, 1 CPA Partners), 5 Wealth, and 4 Practice Cloud. 12 are High, 11 Moderate, and 4 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and hub network | Group | High | 4 h | 2 h | 1 h |
| BP-W01 Trading and portfolio management | Wealth | High | 4 h | 2 h | 1 h |
| BP-S01 Practice Cloud service for customer firms | Practice Cloud | High | 4 h | 2 h | 1 h |
| BP-G04 Office network and connectivity | Group | High | 8 h | 4 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-W02 Client money movement and custodian instructions | Wealth | High | 8 h | 4 h | 1 h |
| BP-T01 Individual return preparation and review | Tax | High | 12 h | 4 h | 1 h |
| BP-T03 Client document intake and portal | Tax | High | 12 h | 4 h | 1 h |
| BP-T02 Electronic filing and acknowledgments | Tax | High | 24 h | 8 h | 1 h |
| BP-T04 Form 8879 e-signature and return delivery | Tax | High | 24 h | 8 h | 1 h |
| BP-T06 Client accounting services: payroll | Tax | High | 24 h | 8 h | 4 h |
| BP-G05 Email and collaboration | Group | Moderate | 24 h | 8 h | 1 h |
| BP-S02 Practice Cloud support and security notices | Practice Cloud | Moderate | 24 h | 8 h | 4 h |
| BP-W03 Adviser CRM and client service | Wealth | Moderate | 24 h | 8 h | 4 h |
| BP-W04 Client portal and statements | Wealth | Moderate | 24 h | 12 h | 4 h |
| BP-T05 Business, trust, and exempt organization returns | Tax | Moderate | 48 h | 24 h | 4 h |
| BP-T07 Client accounting services: bookkeeping | Tax | Moderate | 72 h | 24 h | 24 h |
| BP-CP01 Attest engagements | CPA Partners | Moderate | 72 h | 24 h | 4 h |
| BP-W05 Compliance surveillance and books and records | Wealth | Moderate | 72 h | 24 h | 4 h |
| BP-S04 Practice Cloud release pipeline | Practice Cloud | Moderate | 72 h | 24 h | 4 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-G06 Payroll and HR, including seasonal hiring | Group | Moderate | 120 h | 72 h | 24 h |
| BP-T08 IRS and state notice representation | Tax | Low | 120 h | 72 h | 24 h |
| BP-T10 AI document extraction assistant | Tax | Low | 72 h | 24 h | 24 h |
| BP-S03 AI document intake feature | Practice Cloud | Low | 72 h | 24 h | 24 h |
| BP-T09 Referral and integrated planning interface | Tax | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Deadlines and money per day** drive the tax processes. In season a full-day outage of SYS-T1 stops about $92 million of work, and a lost day near April 15 means late returns and penalties for clients. Extensions are the workaround, which is why e-file (BP-T02) can wait longer than preparation (BP-T01): signed returns queue and can be released in bulk.
- **Clients' employees** drive payroll (BP-T06). It is the one client accounting process with a hard external clock.
- **Market hours and fraud controls** drive Wealth. Trading (BP-W01) cannot wait; money movement (BP-W02) can pause, but its fraud checks must never be bypassed during an outage.
- **Customers' filing season** drives Practice Cloud (BP-S01). About 26,000 customer firms, and Tax and Advisory itself, depend on the portal from January to April.
- **The AI tools are Low.** Preparers can key data by hand (BP-T10), and Practice Cloud customers can turn the intake feature off (BP-S03). Their risk is confidentiality and accuracy, not availability (P10).

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all three divisions at once. Break-glass accounts per critical system are the fallback |
| Office network (SYS-G3) | Group | Tax offices; Wealth branches | SYS-T1 is only as available as office connectivity. Cellular failover exists at every tax office |
| Email (SYS-G4) | Group | All divisions | One tenant for every division and seasonal staff. Moderate for availability but the main entry point for business email compromise (P08) |
| Practice Cloud service (BP-S01) | Practice Cloud | Tax and Advisory document intake and e-signature (BP-T03, BP-T04) | The tax division's client portal is a tenant of the group's own product. A Practice Cloud outage is a tax division outage in season |
| Referral interface (BP-T09) | Tax and Advisory | Wealth CRM (BP-W03) | Low for availability; high for confidentiality and IRC 7216 (gap 1) |
| Integrated planning data | Wealth | Tax and Advisory | Wealth sends custodial statements for 210,000 integrated planning households; Tax and Advisory holds them for Wealth (Regulation S-P service provider) |
| SOC facts (BP-G02) | Group | Every notice in P08 | Every notice clock depends on the SOC establishing what happened |
| Group services for CPA Partners | Group | Attest engagements (BP-CP01) | Provided under the 2021 administrative services agreement; inheritance not documented (gap 7) |
| HR events (BP-G06) | Group | SYS-G1 accounts | Seasonal onboarding and offboarding drive access for about 11,000 accounts (gap 2) |

**Single points of failure found:** SYS-G1 (mitigated by break-glass accounts, tested quarterly); the tax engine vendor's transmitter for e-file (no second transmitter; accepted, P01 TX-019); one payroll SaaS vendor for 21,000 client payrolls (P01 TX-015).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| SYS-T1 return data store | BP-T01, BP-T02, BP-T05 | Continuous database replication to a second zone; hourly immutable snapshots to provider B |
| SYS-S1 Practice Cloud | BP-S01, BP-T03, BP-T04 | Database replicas; warm standby region in provider B |
| SYS-T2 payroll and bookkeeping SaaS | BP-T06, BP-T07 | Vendor replication (RPO 4 hours per contract); daily export of payroll registers |
| SYS-W1 Wealth platform | BP-W01 to BP-W05 | Vendor replication; custodians hold the books of record |
| SYS-T3 attest platform | BP-CP01 | Daily immutable backups |
| People | All | Cross-trained teams; preparers can work from any office; seasonal staffing plan |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones and hub network
3. Office network and connectivity
4. SOC visibility (SIEM, EDR, email gateway)
5. to 9. Tax preparation, document intake (Practice Cloud tenant), e-file, Form 8879 e-signature, and payroll
10. Wealth trading (often recovered in parallel by the custodians' platforms)
11. The Practice Cloud service for all customers (runs in provider B, so it often recovers in parallel)
12. to 27. Wealth money movement, email, business returns, Practice Cloud support, adviser CRM, Wealth portal, bookkeeping, attest engagements, compliance records, release pipeline, financial close, notice representation, the two AI features, the referral interface, and HR.

Recovery order changes by season: from May to December, Wealth trading and Practice Cloud move ahead of tax preparation.

## 8. Key findings
1. **Shared services must recover first, as they must.** The group identity RTO of 1 hour was met in two tests in 2026.
2. **Practice Cloud is both a division and a dependency.** Its 2-hour RTO protects outside customers and Tax and Advisory together; a Practice Cloud outage in season stops tax document intake and e-signature.
3. **Email is Moderate for availability but central to the top risk.** Its recovery can wait a day; its protection against business email compromise cannot (P01 GR-02; P08).
4. **The referral interface is Low for availability and High for confidentiality.** It can stop for days with little effect, but every transfer must follow an IRC 7216 consent (P03).
5. **Notification capacity is itself a process** (BP-G02, BP-S02, BP-G07). If the SOC or the Practice Cloud support desk is down during an incident, notice clocks keep running. The P08 runbook uses out-of-band channels for this reason.
