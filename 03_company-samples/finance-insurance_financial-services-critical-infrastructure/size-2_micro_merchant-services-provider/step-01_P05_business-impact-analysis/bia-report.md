# Business Impact Analysis: Cris Santos Company | Financial Services | Micro

**Organization:** Cris Santos Company, LLC (merchant services provider, an ISO) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Operations Manager (Qualified Individual and security lead) with the Owner, the Merchant Support Lead, the Onboarding and Risk Specialist, the Terminal and Integration Technician, and the MSP lead technician, 2026-07-13 to 2026-07-24 | **Approved:** Owner, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It feeds:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- PCI DSS 12.10.1, which requires the incident response plan to include business recovery and continuity procedures (the company has no plan yet; gap 5 in `../00_company-facts.md`).

**What this company does not run.** The company does not authorize, clear, or settle card transactions. The processor partner does, on its own platform. If the processor partner is down, merchants cannot take cards no matter what the company does. This BIA therefore covers the company's own functions: helping merchants, keying backup sales, administering gateway settings, and boarding new merchants.

**Regulatory drivers checked.** The bank service provider notice in 12 CFR 53.4 (C-FINANCIAL-R01) is triggered by a disruption of "covered services" to a bank for four or more hours. The company performs no covered services for the sponsor bank (P03 section 1.3), so no process below carries that four-hour clock. The FTC Safeguards Rule incident response plan element (16 CFR 314.4(h)) does not apply because of the 314.6 exception (P03 section 1.2). The drivers here are the merchant agreements, the ISO agreement, and PCI DSS.

## 2. System and business description
One Florida office suite and 7 employees serve about 850 merchants. Nearly everything is SaaS:
- the processor partner's gateway reseller console (SYS-01) and partner portal (SYS-02);
- the CRM and merchant document store (SYS-03);
- the productivity suite (SYS-04) and its backup (SYS-10);
- the cloud phone system (SYS-05).

On site are 9 MSP-managed laptops (SYS-06), the office network (SYS-07), and about 40 spare terminals (SYS-09). The website and application intake (SYS-08) run on cloud web hosting. Staff can work from home with the same laptops and the phone app. See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual receipts, about $4,400 per business day. Merchant attrition is the main cost driver: each merchant is worth about $1,300 a year in residuals.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25,000 (for example, losing 20 merchants) | $5,000 to $25,000 | Less than $5,000 |
| Operations (merchant operations) | Merchants cannot get help to take cards | One service stops (for example, new boarding) | Staff slowed; merchants unaffected |
| Regulatory and contract | Card brand or ISO agreement breach; reportable breach; PCI DSS requirement not in place | Missed contract service level or card network deadline | Internal policy deviation |
| Safety | Not applicable: no process affects physical safety | | |
| Reputation | Loss of the processor partner relationship or of many merchants; local news | Merchant complaints and online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Merchant help desk and terminal troubleshooting | High | 8 h | 4 h | 24 h |
| BP-02 Backup keyed-entry service | Moderate | 24 h | 8 h | 24 h |
| BP-03 Gateway administration for online and virtual terminal merchants | Moderate | 24 h | 8 h | 24 h |
| BP-04 Merchant onboarding and underwriting | Moderate | 72 h | 48 h | 24 h |
| BP-05 Terminal deployment and swaps | Moderate | 48 h | 24 h | 24 h |
| BP-06 Chargeback and retrieval support | Moderate | 72 h | 48 h | 24 h |
| BP-07 Merchant risk monitoring and fraud filter settings | Moderate | 24 h | 8 h | 24 h |
| BP-08 Residuals, agent commissions, finance, and payroll | Low | 120 h | 72 h | 24 h |
| BP-09 Sales and agent management | Low | 120 h | 72 h | 24 h |

Totals: 9 processes; 1 High, 6 Moderate, 2 Low.

**What drives the values:**
- **The help desk (BP-01) is the only High process.** A merchant whose terminal fails calls the company first. One business day without an answer is the most the Owner will accept before merchants start moving to other ISOs.
- **Most company data is not transaction data.** Transactions, settlement, and gateway settings live on the processor partner's platform. The company's own data is tickets, merchant files, and change records, so a 24-hour RPO is enough everywhere.
- **Keyed entry (BP-02) is a convenience, not a lifeline.** Merchants can key their own sales in the gateway app. That matters for P01 and P03: the company could stop the service and shrink its PCI DSS scope without hurting merchants much (P01 R-003).

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Gateway reseller console (SaaS) | Merchant gateway users, hosted payment pages, fraud filters, keyed entry | Processor partner's platform resilience (its PCI DSS AOC; no SOC 2 report offered) | BP-01, BP-02, BP-03, BP-07, BP-09 |
| SYS-02 Processor partner portal (SaaS) | Boarding, residuals, chargebacks, change requests | Processor partner's platform resilience | BP-01, BP-04, BP-05, BP-06, BP-07, BP-08 |
| SYS-03 CRM and merchant document store (SaaS) | Merchant files and applications | CRM vendor backups (SOC 2 Type 2 report, reviewed in P09) plus a monthly export to the suite | BP-04, BP-09 |
| SYS-04 Productivity suite (SaaS) | Email, files, chat, ticket notes | Daily suite backup (SYS-10), 1-year retention | BP-01 to BP-09 |
| SYS-05 Cloud phone system (SaaS) | Main line, support queue, mobile app | Vendor service; call routing settings documented by the MSP | BP-01, BP-02 |
| SYS-06 Laptops | 7 in use, 2 spares | No local data by design; MSP reimages | All |
| SYS-07 Office network and internet | Firewall, Wi-Fi, one internet line | Staff work from home; firewall configuration backed up by the MSP | All (office only) |
| SYS-08 Website and application intake (cloud workload) | Online application form and upload bucket | Hosting provider snapshots, retention unknown; **no backup the company controls** | BP-04 |
| SYS-09 Spare terminals | About 40 key-injected terminals | Processor partner ships replacements | BP-05 |
| SYS-10 Suite backup (SaaS, MSP-operated) | Daily copy of email and files | **Never restore-tested** | BP-08 and all suite data |
| People | Two support staff, the Technician, the Onboarding and Risk Specialist, the Operations Manager | Cross-training: the Operations Manager covers the help desk; the Technician covers keyed entry | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Processor partner (gateway, portal, deployment center) | BP-01 to BP-07 | PCI DSS AOC (Level 1 service provider) on file; no availability commitment to the company in the ISO agreement |
| CRM vendor | BP-04, BP-09 | SOC 2 Type 2 report (P09): stated RTO 8 h and RPO 1 h, which meet this BIA |
| Phone vendor | BP-01, BP-02 | Standard service terms only |
| Suite vendor and backup service | All suite data | Vendor service terms; backup never restore-tested |
| MSP | Laptop rebuilds, firewall, backup restores | 4-business-hour response time; no recovery time commitment |
| Web hosting and storage provider | BP-04 (online applications only) | Standard terms; the web developer holds the only admin login |
| Internet provider | Office work only | None; single line, but home working covers it |

**Key findings:**
1. **The company's biggest dependency is outside its control.** If the processor partner's gateway or portal is down, BP-01 to BP-07 stop or degrade. The ISO agreement gives the company no availability commitment and no status notification. Ask for both at renewal (P01 R-018).
2. **Home working removes the office as a single point of failure.** The phone app, SaaS tools, and laptops all work from home. A hurricane or internet outage at the office is a Low risk (P01 R-016).
3. **Two recovery paths are unproven.** The suite backup (SYS-10) has never been restore-tested, and the website bucket (SYS-08) has no backup the company controls. Both are inside the RPO on paper only.
4. **One person holds the keys.** The Operations Manager is the only person who knows the administrator settings for most systems, and the web developer is the only one with the hosting login (P01 R-019, R-020).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Phone system (SYS-05) and email (SYS-04) | 1 h | Mobile phone app; forward the main line to support specialists' mobile phones |
| 2 | Clean laptops for support staff (SYS-06) | 4 h | Spare laptops; MSP reimages |
| 3 | Gateway console access (SYS-01) | 4 h | Vendor-hosted; processor partner's gateway support resets merchant users |
| 4 | Fraud filter and merchant risk tools (SYS-01, SYS-02) | 8 h | Processor partner's risk team holds suspicious deposits |
| 5 | Spare terminal shipments (SYS-09) | 24 h | Processor partner ships direct |
| 6 | CRM (SYS-03) and processor partner portal boarding (SYS-02) | 48 h | Hold applications; submit later |
| 7 | Chargeback support (SYS-02) | 48 h | Merchants respond directly in the portal |
| 8 | Website intake (SYS-08) | 72 h | Agents and merchants send applications through the CRM's secure upload link |
| 9 | Suite file restore (SYS-10) | 72 h | Payroll service repeats the prior run |
| 10 | Office network and internet (SYS-07) | 72 h | Staff work from home |

**Treatment (tracked in P01 and P07):** first restore test of the suite backup by 2026-10-31 and quarterly after (R-010); a company-held copy or deletion of the website bucket contents (R-005); written administrator runbook and a second administrator for each system (R-019); hosting login transferred to the company (R-020).
