# Business Impact Analysis: Cris Santos Company | Information | Small

**Organization:** Cris Santos Company, LLC (B2B SaaS software publisher) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (security and compliance lead) with the Platform Engineering Lead, Engineering Manager, Customer Support Manager, and COO | **Approved:** CTO, 2026-09-22

## 1. Overview and purpose
This BIA identifies which business processes the company and its customers depend on, how long each can be down, and how much data each can lose. It covers all 10 business processes in `bia.csv`. It supports:
- the disaster recovery (DR) and contingency plan the company does not yet have (SSP control CP-2, due 2027-01-31; P01 R-006 and R-028);
- the SOC 2 Availability category, which is new to scope for the Type 2 (criteria A1.1 to A1.3, P09);
- the 99.9% monthly availability SLA in the MSA (P03 row G-039);
- the availability rating in the SSP (P02) and impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

No federal or state law sets recovery times for this company. The drivers are customer contracts (SLA and service credits), customers' payroll deadlines, and the SOC 2 availability commitments.

## 2. System and business description
The company sells the Workforce Scheduling Platform (WSP), a multi-tenant SaaS platform used by about 310 customer organizations and about 140,000 workers in 46 states. Workers clock in and out, view schedules, and swap shifts; managers approve timesheets that become payroll export files for customers' payroll systems. The WSP runs in one public-cloud production account in one primary region (SYS-01), built and deployed by a SaaS CI/CD pipeline (SYS-03), with workforce access through the identity provider (SYS-04). See the SSP (P02) and `../scenario-facts.md` sections 3 and 4.

Customer usage peaks at shift changes (about 05:00 to 08:00 and 14:00 to 16:00 local time across four U.S. time zones), and payroll exports peak on Monday and Tuesday mornings.

## 3. Impact categories and values
Dollar values are scaled to $28.2 million in annual receipts, about $77,000 per calendar day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $230,000 (about 3 days of receipts), counting SLA service credits, emergency labor, and expected churn | $50,000 to $230,000 | Less than $50,000 |
| Operations | All customers cannot capture time or see schedules | One feature or a subset of customers is down | Staff or customers slowed but working |
| Regulatory and contractual | Customer data exposed, or the SLA missed for most customers, triggering DPA notices or SLA credits at scale | A single contract commitment missed (for example, one customer's credit) | Internal policy deviation |
| Worker harm (safety) | Workers paid late or wrongly at scale, or customer sites cannot confirm who is on site during an emergency roll call | Workers miss shifts or pay corrections are needed for a few customers | None |
| Reputation | Loss of several customers, public post-incident scrutiny, or an unfavorable SOC 2 report | Customer complaints and escalations | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Time capture (clock-in and clock-out) | High | 8 h | 2 h | 15 min |
| BP-02 Schedule publishing and viewing | High | 12 h | 4 h | 1 h |
| BP-03 Timesheet approval and payroll export | High | 24 h | 8 h | 15 min |
| BP-04 Shift notifications and swaps | Moderate | 24 h | 8 h | 4 h |
| BP-05 Customer support | Moderate | 24 h | 8 h | 24 h |
| BP-06 Software build and deployment | Moderate | 48 h | 24 h | 24 h |
| BP-07 Corporate operations | Moderate | 72 h | 24 h | 24 h |
| BP-08 Customer onboarding and implementation | Low | 120 h | 72 h | 24 h |
| BP-09 Billing and collections | Low | 168 h | 72 h | 24 h |
| BP-10 AI assistant (beta) | Low | 168 h | 72 h | 24 h |

Totals: 3 High, 4 Moderate, and 3 Low processes.

**What drives the values:**
- **Time capture sets the tightest targets.** The mobile and kiosk apps queue punches offline for up to 24 hours, but web punches and new sign-ins fail at once, and customers treat any clock-in failure at a shift change as an outage. The MTD of 8 hours equals one full shift cycle. Any outage longer than about 43 minutes in a 30-day month breaks the 99.9% SLA and earns customers service credits. The 2-hour RTO is the longest outage the CTO judged would keep credits and escalations within the Moderate impact bands.
- **Payroll deadlines drive BP-03.** Most customers run weekly or biweekly payroll with fixed submission cut-offs. A missed export means late or wrong pay for workers, which is why the RPO follows BP-01: exports are built from punches.
- **Recovery point for punches is 15 minutes.** Lost punches become wage-and-hour errors for customers. Database point-in-time recovery meets this inside the primary region.
- **The AI assistant is optional.** It can be switched off by feature flag, and scheduling works without it.

**Key findings:**
1. **The 2-hour RTO for BP-01 is unproven.** The only restore test (January 2026) took 5 hours. There is no written recovery runbook, and only the Platform Engineering Lead has rebuilt production (P01 R-006 and R-028; SSP CP-4 and CP-10).
2. **The 15-minute RPO holds only inside the primary region.** Snapshots are copied to the second region once a day, so after a regional outage up to 24 hours of punches could be lost unless the offline queues cover the gap. The DR plan must either replicate the database continuously to the second region or document the 24-hour regional RPO and tell customers.
3. **Backups can be deleted with production.** Snapshots and cross-region copies are in the production account (P01 R-007). A destructive attacker could remove both the database and its recovery points.
4. **Staff access depends on the identity provider.** Engineers reach the cloud console and CI only through single sign-on, so an identity provider outage slows recovery. Two sealed emergency cloud accounts are needed (section 6, priority 1).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 managed database | Multi-tenant system of record for punches, schedules, and timesheets | BP-01, BP-02, BP-03, BP-04, BP-08, BP-10 |
| SYS-01 application tier | Web application, mobile API, background workers, internal admin console | BP-01 to BP-05, BP-08, BP-10 |
| SYS-01 object storage | Payroll export files | BP-03 |
| SYS-01 cache, message queue, key management, secrets manager | Session state, notification and export jobs, encryption keys, application secrets | BP-01 to BP-04 |
| SYS-04 identity provider | Workforce single sign-on and MFA to consoles, CI, and support tools | All (staff access) |
| SYS-06 observability and status page | Uptime monitoring, alerts, public status page | All (detection and customer updates) |
| SYS-07 email and SMS delivery | Shift reminders and swap requests | BP-04 |
| SYS-05 support tooling | Ticketing and chat SaaS | BP-05 |
| SYS-03 source repository and CI/CD | Builds and deploys fixes | BP-06 |
| SYS-09 corporate SaaS | Email, chat, HR, finance, CRM, payment processor | BP-07, BP-09 |
| SYS-08 AI model provider | Generative summaries and swap suggestions | BP-10 |
| SYS-10 laptops | Staff endpoints | All |
| People | Platform Engineering Lead and on-call engineers (6 with production access), Customer Support Manager and 10 agents, COO | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-04 identity provider access for responders | 1 h | Two sealed emergency cloud accounts with hardware keys held by the CTO and Platform Engineering Lead (to be created with the DR plan) |
| 2 | SYS-01 managed database | 2 h (target); 5 h measured in January 2026 | Point-in-time restore in the primary region; snapshot restore in the second region |
| 3 | SYS-01 application tier and punch ingestion (BP-01) | 2 h | Redeploy from infrastructure code and signed images; mobile and kiosk offline queues hold punches for 24 h |
| 4 | SYS-06 status page and monitoring | 2 h | Status page is hosted by a separate provider; manual customer email from the support tool |
| 5 | SYS-01 schedule views and object storage for payroll exports (BP-02, BP-03) | 4 h to 8 h | Customers export or print the last published schedule; payroll from prior period with adjustments |
| 6 | SYS-07 notification delivery (BP-04) | 8 h | In-app messages; managers contact workers directly |
| 7 | SYS-05 support tooling (BP-05) | 8 h | Status page and support phone line forwarded to managers' mobile phones |
| 8 | SYS-03 CI/CD (BP-06) | 24 h | Manual build and deploy runbook from a clean laptop (to be written, P01 R-028) |
| 9 | SYS-09 corporate SaaS (BP-07, BP-09) | 24 h to 72 h | Personal phones and the out-of-band contact list; payroll provider repeats prior payroll |
| 10 | SYS-08 AI assistant (BP-10) | 72 h | Feature flag off; standard swap lists |

## 7. Next steps
| Action | Owner | Due | Links |
|---|---|---|---|
| Write the DR plan and regional recovery runbook, including the regional RPO decision | Platform Engineering Lead | 2027-01-31 | R-006, R-028; SSP CP-2 |
| Semiannual restore and regional failover tests, the next run by a second engineer | Platform Engineering Lead | First test 2026-12-15 | CP-4; P09 A1.3 |
| Move backup copies to a separate backup account with write-once retention | Platform Engineering Lead | 2026-12-15 | R-007 |
| Create two sealed emergency cloud accounts | CTO | 2026-11-30 | Priority 1 above |
| Review this BIA | IT Manager | 2027-08-31, or after a major change | |
