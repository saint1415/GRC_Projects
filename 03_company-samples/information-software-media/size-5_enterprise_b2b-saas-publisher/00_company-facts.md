# Scenario facts: Cris Santos Company | Information | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given; regulatory facts were checked against primary sources on the dates shown in P03.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; common stock listed on a U.S. national securities exchange; not a smaller reporting company) |
| Business | B2B SaaS software publisher (NAICS 513210). Its main product, the **Operations Cloud**, is a multi-tenant SaaS suite for customer service case management, field service scheduling, and employee service desks. It also sells the **Data Cloud** (analytics and customer data platform), the **Conversational AI service** (from the 2025 acquisition of AQ-01), and a separately hosted **Government Edition** of the Operations Cloud for federal agencies. Generative AI features (**AI Assist**) are embedded in the Operations Cloud |
| Location | Headquartered in Florida. Offices in Florida, Texas, North Carolina, Colorado, Washington, and New York; about 30% of staff work remotely from other U.S. states. All company workforce and all hosting are in the United States. One contracted follow-the-sun support vendor uses agents in two countries that are **not** countries of concern under 28 CFR 202.601. **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: about 4,300 engineering and product, 2,100 customer support and success, 2,900 sales and marketing, 1,200 professional services, 1,500 general and administrative |
| Customers | About 9,800 business customers (Operations Cloud), 3,100 of which also buy the Data Cloud and about 1,150 the Conversational AI service. About 1.9 million named users. Customer tenants hold about 310 million end-customer (consumer) records. Notable segments: about 140 banking organizations, about 1,100 health care organizations (the terms of service prohibit protected health information; no business associate agreements are signed), about 260 state and local government bodies (commercial edition), and 45 federal civilian agencies (Government Edition only; no Department of Defense customers) |
| Revenue | About $4.8 billion a year (fictional), 94% subscription. About $13.2 million per calendar day. Not small under the SBA standard for NAICS 513210 ($47.0 million) |
| Role under privacy and breach laws | For customer data: a **service provider / processor** acting on customers' instructions under the Data Processing Addendum (DPA); a **third-party agent** under Fla. Stat. 501.171(6). For its own employees, customer contacts, and about 3.4 million marketing contacts (about 420,000 California residents): the **business / controller** that owns the data |
| Customer commitments (MSA, DPA, trust page) | 99.95% monthly availability for Enterprise-tier customers (99.9% standard) with service credits; notice of a security incident affecting customer data without undue delay and within 48 hours of confirmation (standard DPA since 2024; about 2,600 older contracts say 72 hours and about 310 negotiated contracts say 24 hours); 30 days' notice of new sub-processors with a right to object; deletion of customer data within 30 days after termination from production and within 90 days from backups; customer data never used to train AI models shared across customers; current SOC 2 Type 2 report and ISO/IEC 27001 certificate available under NDA |
| Public statements | The trust page states that "customer data is never accessed by our staff without customer permission," that "all administrative access is logged and recorded," and that "we never use your data to train AI models for other customers" |
| Assurance | Operations Cloud: annual SOC 2 Type 2 (Security, Availability, Confidentiality) since 2019, period October 1 to September 30; ISO/IEC 27001 certificate. Data Cloud: SOC 2 Type 2 (Security only) since 2025. Conversational AI service: no SOC 2 report yet. Government Edition: FedRAMP Moderate authorization (agency sponsored, granted 2024) with continuous monitoring. SOX Section 404 IT general controls over financial systems are tested by the SOX program |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); SOX IT general controls; FedRAMP for the Government Edition; bank service provider notification (12 CFR 53.4, 225.303, 304.24) for banking customers; CCPA cybersecurity audit; DOJ Data Security Program diligence; growth by acquisition |
| Not in scope | HIPAA (no business associate agreements; protected health information prohibited by contract), COPPA (not directed to children; customers are the operators of any child-directed service), FCC CPNI rules (not a carrier or interconnected VoIP provider), PADFA (not a data broker), PCI DSS for the platform (customer billing runs through a payment processor; the platform does not store card numbers), DFARS 252.204-7012 and CMMC (no Department of Defense contracts). Non-U.S. laws that may apply to non-U.S. customers are outside the scope of these deliverables |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board of directors (audit committee; cybersecurity and risk committee) | Cyber risk oversight (Item 106(c)(1)); the cybersecurity and risk committee receives quarterly reports |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Program owner; reports to the CEO; quarterly reporting to the cybersecurity and risk committee |
| Chief Technology Officer (CTO) | Owns product engineering and the production platforms; **authorizing official** for the SSP system (P02) |
| Chief Privacy Officer | Privacy program, DPA terms, breach determinations for personal information, CCPA program |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Data and AI Officer | Chairs the AI governance council |
| General Counsel | Chairs the disclosure committee; contracts and regulatory matters |
| Chief Audit Executive | Heads Internal Audit; reports functionally to the audit committee and administratively to the CFO |
| GRC team (12), Security Operations Center (24x7, in-house, three U.S. sites), Internal Audit (in-house IT audit team of 9) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | Operations Cloud production platform (commercial, multi-tenant) | Cloud provider A, two U.S. regions plus a recovery region; 14 cells (each cell is an isolated stack of application services and databases serving a set of tenants); about 9,800 tenants |
| SYS-02 | Data Cloud (analytics and customer data platform) | Cloud provider B; about 3,100 tenants; monthly snapshots kept 13 months |
| SYS-03 | Government Edition | Separate environment in Cloud provider A government regions; FedRAMP Moderate boundary with its own SSP and continuous monitoring; 45 agencies, about 38,000 users |
| SYS-04 | Identity platform (workforce SSO, MFA, privileged access management, identity governance) and the customer identity service | About 46,000 non-human identities (service accounts, workload roles, API keys) across the clouds |
| SYS-05 | Software factory: source hosting, CI/CD pipelines, artifact registry, build signing | About 3,800 repositories; 9 legacy pipelines still deploy with long-lived static cloud keys |
| SYS-06 | Security operations stack: SIEM, EDR, cloud security posture management, secret scanning | 24x7 SOC |
| SYS-07 | Corporate SaaS, ERP and finance (SOX-relevant), CRM and marketing database | CRM holds about 3.4 million business contacts |
| SYS-08 | Endpoints | About 14,500 company laptops and test devices |
| SYS-09 | AQ-01 Conversational AI platform (acquired 2025-08) | Cloud provider B, in AQ-01's own cloud organization outside the enterprise landing zone; AQ-01's own identity provider; integrates with SYS-01 through a shared export bucket |
| SYS-10 | Third parties | About 1,450 vendors; 58 sub-processors listed on the public sub-processor page |
| SYS-11 | AI portfolio | 16 use cases governed by the AI governance council formed in 2025 |

**SSP system (P02):** the *Operations Cloud Production Platform (OCP)*: the commercial multi-tenant production environment (SYS-01) with its cells, shared platform services, and the support "tenant access" tool, inheriting common controls from the identity platform (SYS-04), the software factory (SYS-05), the security operations stack (SYS-06), and the Cloud provider A landing zone; the Data Cloud, the Government Edition, and AQ-01 are interconnected systems outside the boundary.

## 4. Current security posture: mostly compliant, with targeted gaps
**In place today:**
- A mature program aligned to NIST CSF 2.0, with a policy hierarchy of policies, standards, procedures, and exceptions
- Annual enterprise risk analysis integrated with ERM (NIST IR 8286)
- 24x7 in-house SOC; EDR on 99% of company endpoints
- Phishing-resistant MFA for all workforce sign-ins; privileged access management with just-in-time elevation for production
- Infrastructure as code and guardrails in the Cloud provider A and B landing zones
- Encryption at rest and in transit, with customer-managed key options for Enterprise customers
- Annual SOC 2 Type 2 and ISO/IEC 27001 for the Operations Cloud; FedRAMP Moderate for the Government Edition
- Annual disaster recovery tests per cell; immutable backups in separate accounts
- A product security program (threat modeling, code scanning, bug bounty, annual third-party penetration tests)
- SEC Item 106 disclosure in the annual report; a disclosure committee that ran a tabletop in 2025

**Targeted gaps:**
1. **Acquisition integration (AQ-01).** AQ-01 runs in its own cloud organization outside the landing zone, on its own identity provider. Its CI pipelines use 31 long-lived static cloud access keys older than one year, its cloud audit logs do not reach the SIEM, and a cross-account role lets its integration service read the whole shared export bucket of Operations Cloud transcripts and case exports for all 1,150 shared customers.
2. **Non-human identities and secrets.** About 17% of the 46,000 non-human identities have permissions unused for 90 days; secret scanning found 212 live secrets in repositories in 2026 H1; 9 legacy pipelines deploy with long-lived keys.
3. **Support access to customer tenants.** The "tenant access" tool requires a ticket and manager approval, but customer approval only for tenants that opted into "restricted access" (about 9% of tenants). Session recording covers 82% of sessions; the legacy console path is not recorded. This contradicts the trust page statements.
4. **Third parties.** 14 of 58 sub-processor SOC report reviews are overdue; three AI model providers were added in 2026; the follow-the-sun support vendor's subcontractors have not been checked for Data Security Program purposes.
5. **AI.** 16 AI use cases; 11 have completed council review. AI Assist is generally available to about 2,300 customers. Red-team testing found indirect prompt injection through case content. AQ-01 still uses customer transcripts to improve its models under AQ-01's pre-acquisition terms, which conflicts with the "never train for other customers" statement for customers who bought both products.
6. **Notification readiness.** Contract notice terms (24, 48, and 72 hours) are not in a searchable obligations register, and the incident runbook does not yet include the bank service provider notice or the FedRAMP incident communications steps.
7. **CCPA cybersecurity audit.** The company meets the 7120 criteria; its first audit covers 2027-01-01 to 2028-01-01 with the report due 2028-04-01. Readiness work has not started, and the in-house IT audit team helped design the control framework in 2025, which raises an independence question under 7122(a)(2).
8. **Data retention against commitments.** Data Cloud monthly snapshots are kept 13 months, longer than the 90-day backup deletion commitment; the Operations Cloud tenant offboarding job failed silently for 23 terminated tenants.
9. **Resilience.** In the 2026 DR tests, the largest cell (Cell 4, about 1,240 tenants) took 6.5 hours to fail over to the recovery region against a 4-hour RTO.
10. **Government Edition.** 6 FedRAMP POA&M items are past their remediation dates (reported to the agencies in monthly continuous monitoring).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | All applicable U.S. rules across the enterprise: FTC Act Section 5 (FTC guidance and the company's own representations), SEC Item 1.05 and Item 106, CCPA service provider duties and the cybersecurity audit, state comprehensive privacy laws as a processor (generic), Fla. Stat. 501.171, FedRAMP for the Government Edition, bank service provider notification, and the DOJ Data Security Program. SOC 2 criteria are assessed in P09 |
| P08 | Cloud credential compromise exposing customer data: a long-lived AQ-01 CI access key leaks through a publicly readable build log and is used, through the cross-account role, to copy Operations Cloud transcript and case exports for shared customers. Includes an **SEC materiality assessment and 8-K Item 1.05** step, a multi-state notification workflow, customer DPA notices, and bank service provider notice |
| P09 | SOC 2 Type 2 readiness across three service lines: SL-1 Operations Cloud, SL-2 Data Cloud, SL-3 Conversational AI service |
| P10 | Enterprise AI portfolio (16 use cases) with the AI governance council; full assessment of AI-001 AI Assist, the generative AI feature embedded in the Operations Cloud |
| Cloud | Multi-cloud (vendor-agnostic): Cloud provider A (Operations Cloud, Government Edition) and Cloud provider B (Data Cloud, AQ-01), with common controls |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and regulatory gap analysis (evidence sampling completed 2026-08-14) |
| 2026-07-13 to 2026-08-28 | Control assessment fieldwork (Internal Audit) |
| 2026-08-19 | AI governance council portfolio review |
| 2026-09-04 | Internal Audit report issued |
| 2026-09-08 | Executive risk committee approvals |
| 2026-09-10 | Results to the cybersecurity and risk committee and the audit committee of the board |
| 2026-10-01 | SL-1 SOC 2 period 2026-10-01 to 2027-09-30 starts |
| 2026-11-12 | Disclosure committee tabletop on the P08 scenario |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1 to 6.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Information Officer (CIO) | Corporate IT, ERP, endpoints, and corporate SaaS |
| Chief Product Officer | Product decisions, including AI Assist features |
| Chief Customer Officer | Customer support and success; owner of customer notices during incidents |
| Chief Compliance Officer | Regulatory compliance program; second line with the GRC team |
| Chief People Officer | Onboarding, terminations, training records |
| Controller | SOX program owner |
| Vice President, Platform Engineering | **System owner of the OCP** (P02) and owner of SL-1 for SOC 2 |
| Vice President, Site Reliability Engineering | Availability, capacity, disaster recovery |
| Vice President, Data Cloud | Owner of SYS-02 and SL-2 |
| General Manager, Conversational AI (AQ-01) | Owner of SYS-09 and SL-3 |
| General Manager, Government Edition | Owner of SYS-03 and its FedRAMP authorization |
| Vice President, Integration Management Office | Integration of acquired companies |
| Vice President, Customer Support | Support operations and the tenant access tool |
| Vice President, Investor Relations; Vice President, Corporate Communications | Investor and public communications during incidents |
| Director of Security Operations | Runs the SOC; incident commander |
| Director of Identity and Access Management | Identity platform (SYS-04) |
| Director of Cloud Platform Engineering | Landing zones in both clouds (common control provider) |
| Director of Product Security | Secure development, code and secret scanning, penetration tests, bug bounty |
| Director of Third-Party Risk Management | Vendor tiering, sub-processor reviews, DSP diligence |
| Director of GRC | Runs the GRC team, the common control catalog, and the policy program |
| Director of Trust and Assurance | SOC 2, ISO/IEC 27001, and customer assurance requests |
| Director of FedRAMP Compliance | Government Edition continuous monitoring and agency reporting |
| Director of Endpoint Engineering | Laptops, EDR, and endpoint baselines |
| Vice President, Workplace and Facilities | Office physical security |

**Cells and volumes.** The OCP runs 14 cells in two U.S. regions (cells 1 to 8 in region 1, cells 9 to 14 in region 2), each with a warm standby in the recovery region. Cell 4 is the largest (about 1,240 tenants). The OCP handles about 2.4 billion API calls and about 6 million new cases a day. Revenue of about $4.8 billion a year is about $13.2 million per calendar day and about $19.2 million per business day. About 4.6 million SLA-eligible tenant-hours a year are tracked for service credits.

**AQ-01.** AQ-01 was acquired in 2025-08 with about 420 employees. Its identity provider is not federated with the identity platform (planned 2027-01-31). The shared export bucket (in AQ-01's cloud organization) receives nightly exports of case transcripts and conversation records for the 1,150 shared customers so AQ-01 models can answer customer questions.

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel.

**Employee and marketing data.** About 1,100 employees live in California. The CRM marketing database holds about 3.4 million business contacts, about 420,000 of them California residents, which is why the CCPA cybersecurity audit criteria in Cal. Code Regs. tit. 11, 7120(b)(2)(A) are met.
