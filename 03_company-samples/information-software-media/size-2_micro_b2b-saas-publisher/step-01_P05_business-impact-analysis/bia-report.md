# Business Impact Analysis: Cris Santos Company | Information | Micro

**Organization:** Cris Santos Company, LLC (B2B SaaS software publisher, Vendor Compliance Platform) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** CTO (security and compliance lead) with the Senior Software Engineer, Customer Success Manager, Operations and Finance Manager, and the MSP lead technician, 2026-07-27 to 2026-08-07 | **Approved:** Chief Executive Officer, 2026-09-15

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It covers all 8 business processes in `bia.csv`. It supports:
- the contingency plan the company does not yet have (SSP control CP-2, due 2026-12-31; P01 R-008);
- the SOC 2 Type 1 readiness work (P09), where recovery is part of the Security criteria (CC7.5, CC9.1);
- the 99.5% monthly uptime target and the backup promise in the security exhibit (P03 rows G-039 and G-041);
- the availability rating in the SSP (P02), impact ratings in the risk register (P01), and the recovery order in the incident response runbook (P08).

No federal or state law sets recovery times for this company. The drivers are customer contracts, customers' need to check vendors before work starts on a site, and the promises the company has made in writing.

## 2. System and business description
The company sells the Vendor Compliance Platform (VCP) to 45 mid-size property management companies and general contractors. About 900 customer users track about 41,000 vendors and about 165,000 stored documents (certificates of insurance, W-9s, licenses). The VCP runs in one public-cloud account in one region (SYS-01) and is deployed by a SaaS CI/CD pipeline (SYS-02). Staff sign in through the productivity suite's identity service (SYS-03), which the MSP administers. See `../00_company-facts.md` sections 1 and 3.

Use peaks on weekday mornings (about 06:00 to 09:00 Eastern), when project managers confirm that subcontractors arriving on site are insured. Monthly compliance reports run in the first week of each month.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual receipts, about $3,000 per calendar day. One average customer pays about $24,000 a year, so losing one customer is a Moderate cost and losing an anchor customer is Severe.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25,000 (service credits, emergency labor, and expected churn) | $5,000 to $25,000 | Less than $5,000 |
| Operations | No customer can check vendor status or upload documents | One function or a few customers are affected | Staff or customers slowed but working |
| Regulatory and contractual | Customer data lost or exposed, triggering DPA notices; uptime target missed for all customers | One contract commitment missed for one customer | Internal policy deviation |
| Customer harm (the `impact_safety` column) | Customers let uninsured or unlicensed vendors work on site at scale, or vendors' tax IDs are exposed | A few customers delay site work or must re-collect documents | None |
| Reputation | Loss of an anchor customer or a prospect walking away during SOC 2 due diligence | Customer complaints and escalations | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Customer compliance checks | High | 24 h | 4 h | 1 h |
| BP-02 Document intake and AI extraction | High | 48 h | 8 h | 1 h |
| BP-03 Expiry tracking and automated reminders | Moderate | 72 h | 24 h | 24 h |
| BP-04 Customer support and onboarding | Moderate | 48 h | 24 h | 24 h |
| BP-05 Software build and deployment | Moderate | 72 h | 24 h | 24 h |
| BP-06 Compliance reports and exports | Moderate | 72 h | 24 h | 24 h |
| BP-07 Sales and security questionnaires | Low | 168 h | 72 h | 24 h |
| BP-08 Billing, payroll, and corporate administration | Low | 168 h | 72 h | 24 h |

Totals: 2 High, 4 Moderate, and 2 Low processes.

**What drives the values:**
- **The uptime target sets BP-01's RTO.** A 99.5% monthly target allows about 3.6 hours of downtime in a 30-day month. A 4-hour RTO for a single outage is the longest the CTO judged would keep service credits for the 2 anchor customers within the Moderate cost band. The 24-hour MTD equals one working morning lost for every customer.
- **Lost uploads drive BP-02's RPO.** Vendors upload a tax form or certificate once. If the file is lost, the customer must chase the vendor again, which can take days. That makes a lost upload a loss of customer data under the DPA, so the RPO is 1 hour even though the MTD is 48 hours.
- **Reminders and reports can catch up.** Expiry jobs run from the database state and can be re-run, and reports are monthly, so BP-03 and BP-06 tolerate 72 hours.
- **The AI feature is not critical.** If the AI model provider is unavailable, documents go to a manual review queue. That is slower but keeps BP-02 inside its MTD.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 managed database | Multi-tenant system of record: vendors, requirements, statuses, extracted fields | Point-in-time recovery (7 days) and daily snapshots (7 days), same account. **Never restore-tested** | BP-01, BP-02, BP-03, BP-06 |
| SYS-01 document bucket | About 165,000 uploaded files | Provider storage durability only. **Versioning is off**, so a deleted or overwritten file cannot be recovered | BP-01, BP-02, BP-06 |
| SYS-01 application tier and workers | Web app, API, document processing, reminder jobs, admin console | Redeploy from the repository; about 60% of resources are in infrastructure code, the rest were created by hand in the console | BP-01 to BP-04, BP-06 |
| SYS-02 repository and CI/CD | Source code, build and deploy pipeline | SaaS provider; local clones on engineers' laptops | BP-05 |
| SYS-03 productivity suite and identity | Staff email, files, chat, single sign-on | SaaS provider; MSP administration | All (staff access) |
| SYS-04 email delivery | Reminders and upload links to vendors | SaaS provider; messages queue for retry | BP-02, BP-03 |
| SYS-06 AI model provider | Field extraction and compliance summaries | Not needed for recovery; manual review queue | BP-02 |
| SYS-07 business SaaS | Support desk, CRM, accounting, payment processor | SaaS providers | BP-04, BP-07, BP-08 |
| SYS-08 laptops | 7 company laptops (MSP-managed) | MSP reimages; no customer data should be stored locally | All |
| People | CTO and Senior Software Engineer are the only people who can rebuild production; Customer Success Manager handles customers | Cross-training planned (P01 R-019) | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Contract | Evidence of recovery capability |
|---|---|---|---|
| Cloud provider | BP-01, BP-02, BP-03, BP-06 | Provider's standard terms and DPA | SOC 2 Type 2 report reviewed 2026-09-02 (P09 V-01). Regional outages are the provider's risk; restoring the company's own data and configuration is the company's job |
| AI model provider | AI extraction in BP-02 only | Click-through API terms (no DPA yet; P10) | Not needed for recovery; manual queue |
| Email delivery service | BP-03 reminders and BP-02 upload links | DPA (sub-processor) | Vendor's published commitments |
| Source repository and CI/CD SaaS | BP-05 | Standard terms | Local clones of the code |
| Productivity suite vendor and MSP | Staff access to everything (single sign-on) | Suite standard terms; MSP contract with a 4-business-hour response time and no recovery commitment | No written recovery commitment from the MSP |
| Support desk SaaS | BP-04 | DPA (sub-processor) | Vendor's published commitments; shared mailbox as fallback |
| Payment processor and payroll service | BP-08 | Standard terms | Prior payroll can be repeated |

## 6. Key findings
1. **The 4-hour RTO for BP-01 is unproven.** No restore has ever been tried, there is no written recovery procedure, and about 40% of production was built by hand in the console. Only the CTO and the Senior Software Engineer could rebuild it (P01 R-008 and R-019; SSP CP-2, CP-4, CP-10).
2. **Deleted documents cannot be recovered.** The document bucket has no versioning, so a faulty script, a mistaken delete, or an attacker could remove customer files for good. The 1-hour RPO for BP-02 cannot be met for deletions (P01 R-007).
3. **Backups share an account with production.** Database snapshots live in the same account, and 5 people hold administrator rights there, including the static CI key. Anyone holding those rights could delete the database and its recovery points together (P01 R-001 and R-002).
4. **The written promise does not match practice.** The security exhibit says daily backups are retained 30 days; snapshots are kept 7 days (P03 G-039).
5. **The MSP contract has no recovery commitment.** The MSP's 4-business-hour response time covers laptops and the suite, which staff need to reach the cloud console. An emergency cloud administrator account that does not depend on the suite's single sign-on is planned (section 6, priority 1).

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Responder access: suite identity service and cloud console accounts | 1 h | One sealed emergency cloud administrator account with a hardware key, held by the Chief Executive Officer (to be created with the contingency plan) |
| 2 | SYS-01 managed database | 4 h (target; never tested) | Point-in-time restore in the same region; restore from snapshot |
| 3 | SYS-01 application tier and document bucket (BP-01, BP-02) | 4 h | Redeploy from the repository; recreate hand-built resources from the recovery runbook (to be written) |
| 4 | Status page and uptime monitoring | 1 h | Status page is hosted by a separate provider; customer email from the support desk |
| 5 | SYS-04 email delivery and reminder jobs (BP-03) | 24 h | Customer Success Manager sends expiry lists to customers |
| 6 | SYS-07 support desk (BP-04) | 24 h | Shared support mailbox in the suite |
| 7 | SYS-02 CI/CD (BP-05) | 24 h | Manual build and deploy from a clean company laptop |
| 8 | Compliance reports (BP-06) | 24 h | Prior month's reports |
| 9 | Corporate SaaS and billing (BP-07, BP-08) | 72 h | Payroll service repeats prior payroll; invoices sent late |

## 8. Next steps
| Action | Owner | Due | Links |
|---|---|---|---|
| Turn on document bucket versioning with a 35-day retention of old versions | Senior Software Engineer | 2026-09-30 | R-007 |
| Copy database snapshots and bucket versions to a separate backup account with write-once retention of 35 days | Senior Software Engineer | 2026-11-30 | R-001, R-002; POAM-007 |
| First restore test of the database and a sample of documents, timed against the 4-hour RTO | Senior Software Engineer | 2026-10-31 | R-008; POAM-008 |
| Short contingency plan and recovery runbook, including the emergency cloud account | CTO | 2026-12-31 | R-008, R-019; SSP CP-2 |
| Review this BIA | CTO | 2027-07-31, or after a major change | |
