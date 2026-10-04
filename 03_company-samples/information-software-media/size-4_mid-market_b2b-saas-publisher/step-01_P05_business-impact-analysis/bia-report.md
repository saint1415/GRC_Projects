# Business Impact Analysis: Cris Santos Company | Information | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed B2B SaaS publisher of a multi-tenant customer service platform) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** GRC Manager with the Director of Security, the VP Platform Engineering, and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-13 to 2026-08-07 | **Approved:** Chief Technology Officer, 2026-09-29 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: platform operations (the customer-facing service), the healthcare cell, engineering, security, customer support, customer success, finance, sales, people, and corporate IT. It rates 17 business processes and quantifies what an outage costs in service credits, lost revenue, operations, and regulatory or contractual exposure.

The results feed:
- the SSP's FIPS 199 availability rating and the contingency controls (P02);
- the HIPAA contingency plan for the healthcare cell, including the applications and data criticality analysis (45 CFR 164.308(a)(7), section 7 below);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability criteria (A1) and the availability commitments in the SOC 2 system description (P09).

## 2. System and business description
The company sells a customer service platform to about 2,400 business customers. Their 88,000 agents use it to answer about 1.9 million tickets and 650,000 chat conversations a day from end consumers. Everything customers buy runs on the Customer Engagement Platform (CEP) described in the SSP (P02):
- the production platform in the primary U.S. region (SYS-01);
- the separate healthcare cell for 46 customers under BAAs (SYS-02);
- the pilot-light DR region (SYS-03);
- the 10-account landing zone (SYS-04);
- the CI/CD pipeline (SYS-05), the identity provider (SYS-06), the admin console (SYS-07), and monitoring (SYS-08).

Messaging delivery (SYS-09), the AI model provider (SYS-10), and the data warehouse on a second cloud provider (SYS-11) are external services. See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
A subscription business does not lose revenue by the hour the way a store does. What it loses in an outage is **service credits**, which step up at fixed availability thresholds, then **customers**. Values come from the MSA credit schedule in `../00_company-facts.md` section 7: Enterprise plan revenue about $5.0 million a month and Standard plan about $3.33 million a month.

| Outage of the core service (30-day month) | Enterprise credit | Standard credit | Total credits |
|---|---|---|---|
| Up to 21 minutes | 0% | 0% | $0 |
| 22 to 43 minutes | 5% | 0% | about $250,000 |
| 44 minutes to 3.6 hours | 5% | 10% | about $583,000 |
| 3.6 to 7.2 hours | 10% | 10% | about $833,000 |
| More than 7.2 hours | 25% (cap) | 25% (cap) | about $2.08 million |

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (within the MTD) | More than $250,000 in credits or lost revenue | $25,000 to $250,000 | Less than $25,000 |
| Operations | Customers cannot run their support operations, or the company cannot operate or recover the platform | One channel, feature, or internal function stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory and contractual | Missed legal notice (bank customers at 4 hours, BAA, state breach law), or a HIPAA availability failure for ePHI | Missed contract commitment (status updates, onboarding milestones) | Internal policy deviation |
| Safety (end consumers) | Plausible harm to people (for example, patients unable to reach a clinic about urgent symptoms) | Delayed but safe service | None |
| Reputation | Public status page incident over 4 hours, press coverage, or an Enterprise termination right | Customer complaints, social media posts | Internal only |

**How loss at MTD was estimated.** Estimated loss is service credits for the share of revenue affected, plus extra labor or lost usage revenue, over the MTD. The share of customers affected comes from product usage data: all customers use the agent workspace and email ingestion, about 70% use chat, and about 65% use the API. Churn is not included, because it cannot be estimated reliably. It is discussed under the enterprise-wide scenario.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-15 Workforce access and collaboration | Corporate IT | High | 4 | 1 | 24 | $120,000 |
| 2 | BP-01 Ticketing and agent workspace | Platform operations | High | 4 | 1 | 0.083 | $858,000 |
| 3 | BP-04 API and integrations | Platform operations | High | 4 | 1 | 0.083 | $552,000 |
| 4 | BP-02 Live chat and messaging channels | Platform operations | High | 4 | 1 | 0.25 | $598,000 |
| 5 | BP-03 Channel ingestion (email, web forms, social) | Platform operations | High | 4 | 2 | 0.25 | $843,000 |
| 6 | BP-05 Healthcare edition service delivery | Healthcare cell | High | 4 | 2 | 0.083 | $55,000 |
| 7 | BP-09 Security monitoring and incident response | Security | High | 8 | 4 | 1 | $15,000 |
| 8 | BP-06 Help center and knowledge base | Platform operations | Moderate | 12 | 4 | 24 | $20,000 |
| 9 | BP-10 Software build and release (CI/CD) | Engineering | Moderate | 24 | 8 | 1 | $60,000 |
| 10 | BP-07 AI features (AI Assist and Answer Bot) | Platform operations | Moderate | 24 | 8 | 24 | $30,000 |
| 11 | BP-11 Company customer support | Customer support | Moderate | 8 | 4 | 1 | $15,000 |
| 12 | BP-13 Billing, invoicing, collections, and service credits | Finance | Moderate | 120 | 72 | 24 | $25,000 |
| 13 | BP-08 Customer reporting and analytics dashboards | Platform operations | Low | 72 | 24 | 24 | $10,000 |
| 14 | BP-12 Customer onboarding, implementation, and data migration | Customer success | Low | 72 | 48 | 24 | $40,000 |
| 15 | BP-14 Sales, renewals, and security questionnaires | Sales | Low | 72 | 48 | 24 | $50,000 |
| 16 | BP-16 Payroll, HR, and contractor management | People | Low | 120 | 72 | 24 | $10,000 |
| 17 | BP-17 Internal analytics and data warehouse | Engineering | Low | 168 | 120 | 24 | $5,000 |

**Summary:** 7 High, 5 Moderate, and 5 Low processes (17 in total). The sum of estimated losses at each process's own MTD is $3,306,000. That sum overstates a single event, because credits for BP-01 to BP-04 overlap and are capped at 25% a month.

**Priority notes.** BP-15 comes first even though it earns nothing directly: without the identity provider, nobody can reach the cloud console or CI/CD to recover anything else. BP-10 (CI/CD) is placed before BP-11 because emergency fixes depend on it during an incident. BP-11 runs on the company's own platform, so it recovers with BP-01, and its backup mailbox works at once.

**Enterprise-wide scenario.** If the whole CEP were down for 9 hours, which is how long the February 2026 regional failover test took, credits reach the 25% cap: about $2.08 million. Beyond 7.2 hours the credits stop growing, but the business risk does not:
- Enterprise customers gain a termination right if availability falls below 99.0% in 2 consecutive months.
- The 9 bank customers must be notified at 4 hours (12 CFR 53.4).
- Incident response and any notification costs come on top (P01 R-001, R-010).

**What drives the values:**
- **Contract steps, not time,** drive BP-01 to BP-04. Most of the credit exposure is incurred in the first hour. That is why the RTO for the core service is 1 hour, even though the MTD is 4 hours.
- **Regulatory and contractual clocks** drive BP-05 and BP-09. The bank service provider notice is due when an incident disrupts covered services for 4 or more hours. Notice clocks keep running even when monitoring is down.
- **Recovery dependencies** drive BP-15 and BP-10.

## 5. Key findings
1. **Regional recovery does not meet the BIA.** The platform survives the loss of a data center within the region (multi-zone design), but the loss of the primary region is a different event. The February 2026 failover test took 9 hours against a 4-hour objective, which is also SOC 2 exception 4. For the core processes (BP-01 to BP-04), a 9-hour event reaches the 25% credit cap and the bank notice threshold. Action: warm standby in the DR region with automated failover (P01 R-006; P07 CP-4, CP-10; POAM-010).
2. **Search is the long pole.** Search indexes are not replicated to the DR region and take about 20 hours to rebuild. The agent workspace works without search, but agents cannot find prior tickets, so BP-01 stays degraded long after its RTO. Action: cross-region index snapshots every 15 minutes (P01 R-006).
3. **Backups can be deleted by a production administrator.** Backups sit in the DR account without write-once retention. A destructive attack with stolen administrator credentials could remove both production and backups (P01 R-007; P08 runbook 2).
4. **The identity provider is a single point of failure for recovery.** Break-glass accounts exist for the cloud organization, but root credentials for 3 accounts use software MFA, and the break-glass procedure was last tested in 2025 (P01 R-024; POAM-005).
5. **The company's own support runs on the platform it supports.** In a platform outage, the support desk also goes down. The backup mailbox and the status page are the only channels, and security contacts are on file for only 71% of customers (gap 14).
6. **The healthcare cell limits blast radius but shares recovery weaknesses.** It has its own account, keys, and database, so an incident in the main production account does not reach it. It uses the same pilot-light DR design, so its availability safeguards under the BAA have the same 9-hour weakness (section 7).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-06 Identity provider and just-in-time access tool | Workforce SSO, MFA, privileged access; break-glass accounts | All (recovery depends on it) |
| SYS-04 Landing zone: network hub, security tooling, and log archive accounts | Routing, guardrails, cloud audit logs | All |
| SYS-01 Managed relational database (12 shards) | Tickets, users, configuration; point-in-time recovery 7 days | BP-01 to BP-04, BP-06 to BP-08 |
| SYS-01 Container cluster and core services | Web, API, chat, and worker services | BP-01 to BP-04, BP-07, BP-11 |
| SYS-01 Object storage | Attachments | BP-01, BP-03 |
| SYS-01 Search cluster | Ticket and article search; per-tenant indexes | BP-01, BP-06 |
| SYS-02 Healthcare cell | Separate account, database shard, storage, search, keys | BP-05 |
| SYS-03 DR region | Database replicas, images, infrastructure code, 35-day backups | Recovery of SYS-01 and SYS-02 |
| SYS-05 Source hosting and CI/CD | Build, sign, deploy; emergency fixes | BP-10 |
| SYS-08 Monitoring and SIEM; MDR provider | Detection, investigation, status page | BP-09; recovery validation |
| SYS-09 Messaging delivery | Email delivery service, SMS provider, social connectors | BP-02, BP-03, BP-05, BP-11 |
| SYS-10 AI model provider | Standard and zero-retention endpoints | BP-07 |
| SYS-11 Data warehouse (cloud provider B) | Internal analytics | BP-17 |
| SYS-12 Corporate SaaS and endpoints | Productivity suite, CRM, HR, billing, 640 laptops | BP-12 to BP-16 |
| People | Platform engineering and site reliability on-call (35), security team (6), support (85), customer success (70) | As listed in `bia.csv` |

## 7. HIPAA contingency plan linkage (healthcare cell)
As a business associate, the company must meet the Security Rule's contingency plan standard for the ePHI it holds for its 46 healthcare customers (45 CFR 164.302; 164.308(a)(7)). The rest of the platform is not subject to HIPAA, but the same recovery design serves both. This BIA supplies the content the HIPAA contingency plan needs:

| 164.308(a)(7) requirement | Type | What this BIA supplies | Status |
|---|---|---|---|
| (ii)(A) Data backup plan | Required | RPO about 5 minutes (BP-05); daily snapshots and 35-day backup copies of the healthcare cell | Backups exist; not write-once (finding 3) |
| (ii)(B) Disaster recovery plan | Required | RTO 2 hours for BP-05; recovery order in section 8 | No written DR plan for the healthcare cell; failover test took 9 hours (finding 1) |
| (ii)(C) Emergency mode operation plan | Required | Clinics revert to phone and their own portals; security monitoring (BP-09) must continue during emergency operations | Not documented for the healthcare cell |
| (ii)(D) Testing and revision procedures | Addressable | Annual regional failover exercise (next 2027-02-17) that includes the healthcare cell | Planned; the company will implement it |
| (ii)(E) Applications and data criticality analysis | Addressable | Section 4 ranks BP-05 as High and lists its dependencies, including 6 sub-processors | Done in this BIA |

These rows are assessed in the gap analysis (P03) and the control assessment (P07, CP-2, CP-4, CP-9, CP-10).

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-06 identity provider and break-glass accounts | 1 h | Sealed break-glass accounts for the cloud organization and identity provider; out-of-band bridge on personal phones |
| 2 | SYS-04 network hub, security tooling, and log archive accounts | 1 h | Guardrails and logging run at the organization level and survive a workload account loss |
| 3 | SYS-01 managed database (all 12 shards) | 1 h in region; 9 h for region loss today (target 2 h) | Point-in-time recovery; promote the cross-region replica |
| 4 | SYS-01 container cluster and core services (agent workspace, API, chat) | 1 h | Redeploy from signed images and infrastructure code |
| 5 | SYS-09 channel ingestion connectors (email, SMS, social) | 2 h | Upstream mail servers queue and retry |
| 6 | SYS-02 healthcare cell | 2 h | Same procedure as SYS-01 in the healthcare account |
| 7 | SYS-08 SIEM, MDR feeds, and status page | 4 h | MDR works from its own platform; status page is hosted by a separate provider |
| 8 | SYS-01 search cluster | 4 h for recent data; about 20 h for a full rebuild today | Agent workspace runs without search; recent tickets first |
| 9 | SYS-05 CI/CD | 8 h | Break-glass deploy of a signed artifact with two-person approval |
| 10 | SYS-10 AI services | 8 h | Feature flags off; manual replies |
| 11 | SYS-12 corporate SaaS (CRM, billing, HR) | 48 to 72 h | Vendor-hosted; exported reports |
| 12 | SYS-11 data warehouse | 120 h | Reload from sources |
