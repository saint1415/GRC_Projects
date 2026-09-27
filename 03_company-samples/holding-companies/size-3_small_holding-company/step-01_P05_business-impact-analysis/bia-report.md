# Business Impact Analysis: Cris Santos Company | Management of Companies and Enterprises | Small

**Organization:** Cris Santos Company, LLC (holding company with three operating subsidiaries) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager with the CFO, Controller, HR Director, and the three subsidiary Presidents | **Approved:** CEO, 2026-09-25

## 1. Overview and purpose
This BIA identifies which business processes the group depends on, how long each can be down, and how much data each can lose. Because the holding company runs shared services, one outage of the shared platform can stop work at every subsidiary at once. The BIA therefore covers the holding company's own processes and the subsidiary processes that depend on the shared platform.

It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the CSF 2.0 group profile outcomes for resilience and recovery (P03: GV.OC-04, PR.IR-03, RC.RP-01);
- Finance's incident response plan, which must cover recovery from security events affecting customer information (16 CFR 314.4(h)).

## 2. System and business description
The group has 60 employees at three Florida sites: HQ (holding company and Finance), the Supply warehouse, and the Home Services shop. Shared services run on the Shared Corporate Services Platform (SCSP): a cloud ERP, one identity provider, one productivity suite, a cloud tenant (integration service, reporting database, bank file transfer server, backup vault), an HRIS and payroll service, endpoints, and site networks. Each subsidiary also runs its own SaaS line-of-business system (SYS-10 to SYS-12). See `../00_company-facts.md` sections 3-4.

## 3. Impact categories and values
Dollar values are scaled to $27.3 million in consolidated receipts, about $105,000 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $250,000 (about 2.5 business days of receipts) or any single fraudulent payment over $100,000 | $50,000 to $250,000 | Less than $50,000 |
| Operations | Two or more subsidiaries stop, or one subsidiary cannot serve customers | One process stops at one subsidiary | Staff slowed but working |
| Regulatory | Reportable event under the Safeguards Rule (16 CFR 314.4(j)) or a state breach law; consumer account errors at Finance | Missed lender covenant or filing date | Internal policy deviation |
| Safety | Plausible harm to a person (for example, an elderly customer without air conditioning in summer heat) | Delayed but safe service | None |
| Reputation | Loss of a key supplier, the lender's confidence, or regional media coverage | Customer complaints or online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Treasury and payments | High | 24 h | 8 h | 4 h |
| BP-04 Supply order-to-cash | High | 24 h | 8 h | 1 h |
| BP-07 Home Services dispatch and field service | High | 24 h | 8 h | 4 h |
| BP-08 Group email, files, and collaboration | High | 24 h | 8 h | 24 h |
| BP-05 Finance loan payment collections and servicing | High | 48 h | 24 h | 4 h |
| BP-02 Payroll for all four employers | Moderate | 72 h | 24 h | 24 h |
| BP-06 Finance loan origination and disbursement | Moderate | 72 h | 24 h | 4 h |
| BP-03 Accounts payable and vendor management | Moderate | 120 h | 48 h | 24 h |
| BP-09 Month-end close, consolidation, and lender reporting | Moderate | 120 h | 72 h | 24 h |
| BP-10 HR onboarding, offboarding, and benefits | Low | 72 h | 48 h | 24 h |
| BP-11 Board and acquisition work | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **Cash and fraud drive BP-01.** Positive pay decisions have a daily bank cutoff, and an outage is when payment fraud is most likely to slip through.
- **Customers drive BP-04 and BP-07.** Contractors buy elsewhere after one lost day. Home Services has a safety driver: loss of cooling in Florida summer heat is a health risk for elderly customers, so emergency calls come first.
- **Consumer accounts drive BP-05.** Collections must post on the due date, or borrowers are charged late fees in error.
- **Payroll has a fixed deadline.** The file is due to the provider 2 business days before payday, so the MTD is 72 hours even though payroll runs every two weeks.

**Key findings:**
1. **The identity provider is a single point of failure for almost every process.** Every SaaS system except SYS-11 signs in through it, so only Home Services' dispatch system keeps running without it, and only because SYS-11 uses local accounts (a security gap; see P01 R-009). Break-glass accounts do not exist yet (P01 R-031).
2. **The 24-hour RPO for BP-08 is not achievable today.** Email and files have no independent backup (gap 8; P01 R-005).
3. **The cloud tenant backups have never been restore-tested**, so the 8-hour RTO for the bank file transfer server (BP-01, BP-05) and the 72-hour RTO for the integration service and reporting database (BP-09) are unproven (P01 R-004).
4. **Vendor recovery commitments must match the BIA.** The ERP vendor's SOC 2 system description states a 4-hour RTO and 1-hour RPO, which meets BP-03 and BP-09 (P09). The distribution system vendor must support BP-04's 1-hour RPO; its contract has not been checked (action for the Supply President, 2026-12-31).

## 5. Resource requirements
| Resource | Description | Supports | Backup or replication method |
|---|---|---|---|
| SYS-02 Identity provider | Single sign-on and MFA for all SaaS and the cloud console | BP-01 to BP-06, BP-08 to BP-11 | Provider-managed; break-glass accounts to be created |
| SYS-03 Productivity suite | Email, files, chat, phones | All | Provider retention only today; third-party backup planned (P01 R-005) |
| SYS-06 Bank portals | Wires, ACH, positive pay | BP-01, BP-02, BP-05, BP-06 | Bank-hosted |
| SYS-04 File transfer server | ACH collection files and positive pay files | BP-01, BP-05 | Daily backup, same account and region (gap) |
| SYS-04 Integration service and reporting database | Subsidiary feeds to the ERP; consolidated reporting | BP-04, BP-09 | Daily backup, same account and region (gap) |
| SYS-01 Cloud ERP | General ledger, payables, consolidation | BP-01, BP-03, BP-09 | Vendor-managed (RPO 1 h per SOC 2 system description) |
| SYS-05 HRIS and payroll | Payroll, HR records, benefits enrollment | BP-02, BP-10 | Vendor-managed |
| SYS-10, SYS-11, SYS-12 | Subsidiary line-of-business SaaS | BP-04, BP-07, BP-05, BP-06 | Vendor-managed |
| SYS-08 Endpoints | 50 laptops, 10 desktops, 16 tablets | All | Standard image; 3 spare laptops at HQ |
| SYS-09 Site networks | Firewalls and internet at three sites | All | Single circuit at each site; cellular failover planned at the warehouse |
| People | IT team (3), MSP after hours, CFO and Treasury and Payments Analyst, Controller, HR Director, subsidiary staff | All | Cross-training: CFO can run treasury alone; Controller can run payroll with the provider |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-02 Identity provider and break-glass accounts | 1 h | Break-glass accounts stored offline (to be created; P01 R-031) |
| 2 | SYS-09 HQ and warehouse internet and network | 2 h | Mobile hotspots; cellular failover at the warehouse (planned) |
| 3 | SYS-08 Clean endpoints for treasury, counter, and dispatch | 4 h | 3 spare laptops at HQ, imaged and kept offline |
| 4 | SYS-06 Bank portal access | 4 h | Bank-hosted; phone instructions with callback |
| 5 | SYS-03 Email, files, and phones | 8 h | Printed contact lists; personal phones for the incident team |
| 6 | SYS-04 File transfer server | 8 h | Upload the ACH and positive pay files directly in the bank portal |
| 7 | SYS-01 ERP (vendor-hosted; confirm integrity) | 8 h | Payments from the bank portal with CFO approval |
| 8 | SYS-12 and SYS-10 access through single sign-on | 8 h | Vendor-hosted; restored with SYS-02 |
| 9 | SYS-05 HRIS and payroll | 24 h | Provider reruns prior payroll |
| 10 | SYS-04 Integration service | 24 h | Manual journal entries from subsidiary system reports |
| 11 | SYS-04 Reporting database | 72 h | Rebuild from ERP exports |
| 12 | SYS-07 Board portal | 72 h | Encrypted email to managers |
