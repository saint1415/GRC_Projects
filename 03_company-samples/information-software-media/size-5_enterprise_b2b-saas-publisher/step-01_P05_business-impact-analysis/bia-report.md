# Business Impact Analysis: Cris Santos Company | Information | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded B2B SaaS software publisher) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners and Site Reliability Engineering, 2026-06-01 to 2026-07-15 | **Approved:** Chief Technology Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** cybersecurity and risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company and its customers depend on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the acquired company AQ-01. It feeds:
- the recovery objectives and availability rating in the Operations Cloud Production Platform (OCP) System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the cloud credential compromise runbook (P08), and the quantitative inputs to the SEC materiality worksheet;
- the Availability criteria for the three SOC 2 service lines (P09);
- the contingency planning and testing evidence the Government Edition reports under its FedRAMP authorization.

**Results in one line:** 17 processes were analyzed; 7 are High criticality, 9 Moderate, and 1 Low. 8 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 24 dependencies, 17 of them single points of failure and 4 never tested.

## 2. System and business description
Cris Santos Company sells B2B SaaS to about 9,800 business customers from its Florida headquarters. The technology estate is described in `../00_company-facts.md` section 3: the Operations Cloud production platform in 14 cells on Cloud provider A (SYS-01), the Data Cloud on Cloud provider B (SYS-02), the Government Edition in Cloud provider A government regions (SYS-03), the identity platform (SYS-04), the software factory (SYS-05), the security operations stack (SYS-06), corporate SaaS and ERP (SYS-07), about 14,500 endpoints (SYS-08), the acquired AQ-01 Conversational AI platform (SYS-09), and about 1,450 vendors (SYS-10). Because customers run their own operations on the platform, an outage harms about 9,800 other businesses at once, which is why contract commitments, not internal convenience, set most of the objectives below.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $2 million per day, or more than $20 million cumulative | $250,000 to $2 million per day | Less than $250,000 per day |
| Operations | A core product stops for all cells, or more than 1,000 customers cannot operate | One cell, one product, or up to 1,000 customers affected | Staff slowed but working |
| Regulatory and contractual | Missed SEC filing; missed customer, bank service provider, or FedRAMP notice; breach of customer personal information in many states | Missed SLA in one product; single-state notice | Internal policy deviation |
| Safety | Indirect: customers' field crews or emergency services rely on dispatch | Delayed but safe customer operations | None |
| Reputation | National media, analyst or ratings action, loss of Enterprise customers | Trade press; customer escalations | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-10 Security monitoring and incident response | High | 4 h | 2 h | 1 h | $0.10M |
| BP-04 Customer sign-in, SSO federation, and API access | High | 4 h | 2 h | 15 min | Not additive |
| BP-01 Operations Cloud case management (customer service and agent workspace) | High | 8 h | 4 h | 15 min | $38.50M |
| BP-02 Field service scheduling and mobile dispatch | High | 8 h | 4 h | 15 min | $9.50M |
| BP-03 Employee service desk (IT and HR service management for customers' workforces) | Moderate | 24 h | 4 h | 15 min | $6.00M |
| BP-11 Customer support operations | High | 12 h | 4 h | 1 h | $2.20M |
| BP-07 Conversational AI service (SL-3) | High | 8 h | 4 h | 1 h | $1.60M |
| BP-08 Government Edition service delivery | High | 8 h | 4 h | 15 min | $1.10M |
| BP-17 Customer data exports and integrations | Moderate | 24 h | 8 h | 1 h | $1.30M |
| BP-16 Workforce collaboration and corporate SaaS | Moderate | 24 h | 8 h | 4 h | $1.20M |
| BP-05 AI Assist (generative AI features in the Operations Cloud) | Moderate | 24 h | 8 h | 1 h | $0.90M |
| BP-06 Data Cloud analytics and customer data platform (SL-2) | Moderate | 24 h | 12 h | 4 h | $2.80M |
| BP-09 Software build, signing, and release | Moderate | 72 h | 24 h | 1 h | $0.60M |
| BP-15 Sales, CRM, and marketing | Low | 72 h | 48 h | 24 h | $0.70M |
| BP-14 Payroll and HR | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-12 Billing, invoicing, and collections | Moderate | 120 h | 72 h | 24 h | $0.80M |
| BP-13 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |

**What drives the values:**
- **Contracts and customers, not internal tolerance,** set the shortest objectives. The 99.95% Enterprise SLA allows about 22 minutes of downtime a month, so a 4-hour RTO is a disaster objective for a regional failure, not a normal operating target. Day-to-day failures are handled by high availability inside each region.
- **Customer identity and the API gateway (BP-04)** have the shortest RTO because every product depends on them. Their cost is shown in BP-01 to BP-03 and is not added again.
- **Security monitoring (BP-10)** has a low direct cost but a 4-hour MTD: losing detection during an attack widens exposure, and the 24-hour, 48-hour, and 72-hour customer notice clocks keep running.
- **Regulation** tightens financial close (BP-13) during the quarter-end window, when the MTD drops to 48 hours because of SEC filing deadlines, and drives Government Edition objectives (BP-08) through the FedRAMP authorization and agency contracts.
- **Confidentiality, not availability,** makes the export path (BP-17) a regulatory process: it is the path used in the P08 scenario.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Cell 4 recovery (DEP-01).** In the 2026-05-16 DR tests, 13 cells failed over within 4 hours, but Cell 4 (about 1,240 tenants, the largest) took 6.5 hours because its database restore and cache warm-up do not scale with tenant count. This is P01 risk R-008 and POA&M item POAM-007.
2. **AQ-01 (DEP-03, DEP-16).** AQ-01 runs outside the landing zone, on its own identity provider and on-call rotation, and its regional recovery has never been tested. The shared export bucket that feeds AQ-01 is a confidentiality single point of failure for 1,150 customers (P01 R-002, R-003; POAM-001 to POAM-003).
3. **Single managed DNS provider (DEP-06).** Every product domain resolves through one provider with no secondary and no tested fallback. A provider outage would make all products unreachable even though the platform is healthy (P01 R-016).
4. **AI model providers (DEP-08).** Each AI Assist feature depends on one model provider, and switching providers has never been tested. The feature flag limits the outage to the AI features (P01 R-041).
5. **Software factory (DEP-09).** If the source hosting and CI service is down, the break-glass path can redeploy existing signed builds but has only been walked through in a tabletop.
6. **Industry lessons applied (DEP-12).** EDR updates are rolled out in rings after the industry-wide faulty security-agent update in 2024 showed how one vendor update can take down many endpoints at once.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Operations Cloud production platform | 14 cells, shared platform services, tenant access tool | BP-01 to BP-05, BP-11, BP-17 |
| SYS-04 Identity platform and customer identity service | Workforce SSO, MFA, PAM; customer sign-in and API gateway | All |
| SYS-02 Data Cloud | Analytics and customer data platform on Cloud provider B | BP-06 |
| SYS-03 Government Edition | FedRAMP Moderate environment in government regions | BP-08 |
| SYS-09 AQ-01 Conversational AI platform | Virtual agents; shared export bucket | BP-07, BP-17 |
| SYS-05 Software factory | Source, CI/CD, artifact registry, signing | BP-09 and every recovery that needs a fix |
| SYS-06 Security operations stack | SIEM, EDR, cloud threat detection | BP-10 and validation of every recovery |
| SYS-07 Corporate SaaS and ERP | Billing, ERP, HR and payroll, CRM, productivity | BP-12 to BP-16 |
| Immutable backups | Separate backup accounts with write-once retention; second-region copies | RPO for all production data |
| People | Site reliability engineers, SOC, support, identity and cloud platform teams | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Identity platform, break-glass accounts, and security tooling (SIEM, EDR) | 1 to 2 h | Sealed break-glass accounts; cloud native alerts |
| 2 | Customer identity service, API gateway, DNS, and CDN | 2 h | Warm standby; direct-to-origin routing |
| 3 | OCP cells for case management and field service (BP-01, BP-02, BP-03) | 4 h (Cell 4: 6.5 h until POAM-007 closes) | Recovery region; customer email and phone fallbacks |
| 4 | Government Edition | 4 h | Second government region |
| 5 | Customer support tools and telephony | 4 h | Status page; mobile forwarding |
| 6 | Customer exports and integrations (after integrity checks) | 8 h | Re-run exports |
| 7 | Conversational AI service (AQ-01) | 4 h target, not tested | Route all contacts to human agents |
| 8 | Data Cloud | 12 h | Standard reports in the Operations Cloud |
| 9 | AI Assist | 8 h | Manual replies and summaries |
| 10 | Software factory | 24 h | Break-glass deploy from the signed artifact cache |
| 11 | Corporate collaboration | 8 h | Out-of-band bridge |
| 12 | Billing | 72 h | Manual invoices for the top 200 customers |
| 13 | Financial close (48 h at quarter end) | 72 h | ERP export and filing agent |
| 14 | Payroll and HR | 48 h | Repeat prior payroll |
| 15 | Sales and marketing systems | 48 h | Spreadsheets |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Cell 4 failover 6.5 h against a 4 h RTO | P01 R-008; P02 CP-10; POAM-007 |
| AQ-01 outside the landing zone; shared export bucket; recovery never tested | P01 R-002, R-003, R-036; POAM-001 to POAM-003 |
| Single managed DNS provider with no tested fallback | P01 R-016 |
| Single model provider per AI Assist feature | P01 R-041; P10 section 8 |
| Data Cloud snapshot retention longer than the deletion commitment | P01 R-022; P03 G-040; POAM-022 |
| Support vendor subcontractors not verified for 28 CFR 202 | P01 R-031; P03 G-073; POAM-010 |
