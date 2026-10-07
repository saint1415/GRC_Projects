# Scenario facts: Cris Santos Company | Information | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or FTC guidance page, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; the founder and Chief Executive Officer is the sole owner) |
| Business | B2B SaaS software publisher (NAICS 513210). Sells the **Vendor Compliance Platform (VCP)**, a multi-tenant SaaS service that collects and tracks subcontractor and supplier compliance documents (certificates of insurance, W-9 tax forms, business licenses, safety certifications) for mid-size property management companies and general contractors |
| Location | Florida. One small leased office; 3 of 7 employees work remotely, all in Florida. One part-time contract developer works remotely from another U.S. state. No offshore staff, contractors, or hosting |
| Workforce | 7 employees: Founder and Chief Executive Officer, Chief Technology Officer (CTO), Senior Software Engineer, Software Engineer, Customer Success Manager, Account Executive, Operations and Finance Manager. Plus 1 part-time contract developer (about 15 hours a week) |
| Customers | 45 customer organizations (mid-size property management companies and general contractors, typically 200 to 2,000 employees) in Florida and 5 other southeastern states. About 900 customer users. Two anchor customers provide about 30% of revenue |
| Data held for customers | About 41,000 vendor records with about 52,000 vendor contacts (name, business email, phone, address); about 165,000 stored documents. Of about 29,000 W-9 forms, about 9,800 show a **Social Security number** as the taxpayer identification number (sole proprietors and single-member LLCs); about 4,100 of those individuals have Florida addresses, and the rest live in about 20 other states. Certificates of insurance show insurer names, policy numbers, limits, and dates. **No** payment card data, bank account data, or health data |
| Revenue | About $1.1 million in annual receipts (fictional), about $3,000 per calendar day. SBA-small (standard $47.0 million for NAICS 513210) |
| Role under privacy and breach laws | For customer vendor data: a **service provider** acting on customers' instructions under the DPA, and a **third-party agent** under Fla. Stat. 501.171(1)(h). The customers own the data. For its own employee data, customer user accounts, and sales contacts: the business that owns the data |
| Customer commitments (MSA, DPA, security exhibit) | Notice of a security incident affecting customer data without undue delay and within 72 hours of confirmation; a published sub-processor list with 30 days' notice of new sub-processors; deletion of customer data within 60 days after termination; customer data used only to provide the service; security exhibit promising encryption in transit and at rest, MFA for personnel access, **annual third-party penetration testing**, and **daily backups retained 30 days**; 99.5% monthly uptime target (service credits for the 2 anchor customers only) |
| Public statements | Website security page: "bank-level 256-bit encryption" and "your vendors' tax IDs are encrypted and never leave our platform." Product page: "AI reads certificates with 99% accuracy" |
| Assurance | None yet. Two mid-market prospects require a SOC 2 report before signing, and one anchor customer's renewal (2027-06-30) requires one. Target: **SOC 2 Type 1** (Security and Confidentiality) as of 2027-03-31, then a Type 2 |
| Not in scope | HIPAA and the FTC Health Breach Notification Rule (no health data); PCI DSS (customers pay through a payment processor's hosted page; no card data held); COPPA (B2B service, not directed to children); FCC CPNI rules (not a carrier); FedRAMP (no federal customers); SEC disclosure rules (private); bank service provider notification rules (no banking customers); CCPA (not a "business": revenue far below the threshold and no selling or sharing; no California customers); DOJ Data Security Program and PADFA (P03 section 1) |
| State law approach | Florida law is cited where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). Vendors live in about 21 states, so other state law is treated generically: "each state where affected individuals reside," with Florida as the worked example |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Founder and Chief Executive Officer (owner) | Accepts Moderate risk and approves treatment plans for High and Very High risks; approves the budget, policies, these deliverables, and every public security statement |
| Chief Technology Officer (CTO) | System owner of the VCP and designated **security and compliance lead** (part-time duties). Runs the cloud account and CI/CD; accepts Low risk; maintains the SSP, risk register, and policy set |
| Operations and Finance Manager | Designated **privacy lead**. Contracts, DPAs, sub-processor list, cyber insurance, onboarding and offboarding checklists, training records |
| Senior Software Engineer | Second cloud administrator; backup technical lead for incidents; backups and deployments |
| Software Engineer | Application development, code review |
| Customer Success Manager | Customer onboarding and support; uses the internal admin console; customer communications during incidents |
| Account Executive | Sales; answers customer security questionnaires (from 2026-09-15 only with CTO approval) |
| Contract developer (part-time, U.S.-based) | Feature development under a contractor agreement with a confidentiality clause and no security terms |
| Managed service provider (MSP) | Manages the 7 company laptops (device management, disk encryption, antivirus, patching), administers the productivity suite (users, MFA policy, email security), and runs the help desk. Holds 2 global administrator accounts in the suite. No access to the production cloud account |
| Outside counsel (as needed) | Wrote the MSA and DPA templates in 2024; advises on breach notification together with the cyber insurer's panel counsel |
| Independent security consultant | Performed the P07 control assessment under a fixed-fee engagement; not involved in the risk or gap analysis or in operating any control; will not be the SOC 2 auditor |

## 3. Systems
| ID | System | Hosting | Holds customer vendor data? | Notes |
|---|---|---|---|---|
| SYS-01 | VCP production environment: web application, API, and background workers (document processing, AI extraction, reminder jobs) on a managed container service; managed relational database (multi-tenant); object storage bucket for uploaded documents; provider-managed encryption keys; internal admin console | Public cloud, one account, one region (vendor-agnostic) | Yes | Tenant isolation is enforced in application code (every query filtered by tenant ID). Database point-in-time recovery for 7 days and daily snapshots kept 7 days, both in the same account. Document bucket versioning is off. Application secrets are stored as container environment variables |
| SYS-02 | Source repository and CI/CD pipeline | SaaS | No (holds secrets) | Deploys to production with **one long-lived static cloud access key with administrator rights**, created in March 2024 and never rotated |
| SYS-03 | Productivity suite (email, files, chat, calendar) with its identity service | SaaS, administered by the MSP | Incidental (email attachments) | Its identity service is the single sign-on for the repository, support desk, and CRM. The cloud console uses separate per-person cloud accounts with MFA |
| SYS-04 | Transactional email delivery service | SaaS | Yes (vendor contact names and emails) | Sends document expiry reminders and upload links to vendors |
| SYS-05 | Error tracking and log management | SaaS | Yes (incidental) | 14-day retention. Some error payloads contain text extracted from W-9s, including TINs |
| SYS-06 | Generative AI model provider (API) | SaaS | Yes | Used by the AI document extraction feature (P10) since 2026-04-20, under click-through API terms |
| SYS-07 | Business SaaS: support desk, CRM, accounting, and the payment processor for customer billing | SaaS | Incidental (support tickets with screenshots) | The payment processor hosts the payment page; the company holds no card data |
| SYS-08 | Endpoints: 7 company laptops; the contract developer's personal laptop | Company laptops MSP-managed; the contractor's laptop unmanaged | Incidental (cached; occasional database extracts) | Company laptops have device management, full-disk encryption, and antivirus. The contractor's laptop has none of these under company control |

**Sub-processors listed in the published DPA list (4):** the cloud provider (SYS-01), the email delivery service (SYS-04), the error tracking and log management service (SYS-05), and the support desk SaaS (SYS-07). The AI model provider (SYS-06) has processed customer data since 2026-04-20 but is **not on the list**.

**SSP system (P02):** the *Vendor Compliance Platform (VCP)*: the multi-tenant production environment (SYS-01) and the components that build, operate, and support it (SYS-02, the SYS-03 identity service, SYS-05), with interfaces to SYS-04 and SYS-06, administered from SYS-08 laptops.

## 4. Current security posture: early, informal, with large gaps
**In place today:**
- MFA on the productivity suite (enforced by the MSP), the cloud console accounts, and the repository
- TLS 1.2 or higher in transit; storage encryption at rest with provider-managed keys (database and document bucket)
- Database point-in-time recovery (7 days) and daily snapshots (7 days)
- Branch protection with one required pull request review on the main branch; infrastructure as code for about 60% of production resources
- Dependency vulnerability alerts from the source repository host
- MSP-managed company laptops: device management, full-disk encryption, antivirus, monthly patching, screen lock
- Customer passwords hashed with an adaptive algorithm; customer login lockout after repeated failures
- MSA and DPA templates written by outside counsel (2024), with a published sub-processor list
- External uptime monitoring and a public status page; a team password manager
- Cyber insurance policy (bound February 2026) with a 24x7 breach hotline and panel vendors

**Missing:**
1. No written security policies and no prior risk assessment. Security work is done by the CTO when time allows.
2. CI/CD deploys with one long-lived static cloud access key with administrator rights (March 2024, never rotated). A copy sits in the contract developer's local environment file on an unmanaged personal laptop.
3. All 3 engineers, the CTO, and the contract developer hold full administrator rights in the production cloud account. There are no separate roles for routine work.
4. Cloud audit logging is the provider's default (management events, 90 days). There is no object-level access logging on the document bucket, no database audit logging, and no alerting.
5. W-9 Social Security numbers are stored as uploaded with no extra protection beyond storage encryption, are sent to the AI model provider during extraction, and appear in some error-tracking payloads.
6. Engineers occasionally copy production database extracts to laptops for debugging, including the contractor's personal laptop.
7. Backups have never been restore-tested; snapshots are kept 7 days (the security exhibit promises 30) in the same account as production; the document bucket has no versioning.
8. No incident response plan and no customer security contact list, although the DPA promises notice within 72 hours.
9. No review of sub-processors. The AI model provider was added on click-through terms without updating the sub-processor list or notifying customers.
10. Offboarding is ad hoc. Access is removed when someone remembers.
11. The admin console's "view as customer" feature lets the Customer Success Manager and all engineers open any tenant without customer approval, and those sessions are not logged.
12. No security awareness or secure coding training.
13. Public statements, the security exhibit, and questionnaire answers are not checked against practice. Questionnaire answers have said "SOC 2 compliant" and "annual penetration test performed"; no SOC 2 audit or penetration test has ever been done.
14. Data of terminated customers is kept indefinitely (2 former customers, ended 5 and 11 months ago), although the DPA promises deletion within 60 days.
15. The AI document extraction feature went live for all customers on 2026-04-20 without a risk assessment or accuracy testing to support the "99% accuracy" claim.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Gap analysis against FTC Act Section 5 data security expectations (FTC business guidance) and the company's own security representations and DPA commitments. The SOC 2 criteria are mapped in each row and assessed criterion by criterion in P09. CCPA and the DOJ Data Security Program are applicability checks only |
| P08 incident | Cloud credential compromise exposing customer data (registry default, kept because it fits): the long-lived CI/CD cloud key is stolen from the contractor's personal laptop by information-stealing malware and used to download the document bucket (including W-9s with SSNs) and copy a database snapshot. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | SOC 2 Type 1 readiness self-assessment for Security plus Confidentiality (the second category customers ask about, because the platform stores vendors' tax forms). Evidence inventory, plus reviews of key vendors' assurance reports |
| P10 AI | Generative AI feature embedded in the product (registry default, refined): AI document extraction that reads certificates of insurance and W-9s, fills in fields, and drafts a compliance summary for the customer's reviewer |
| Cloud | SaaS plus a single cloud workload: the company's own production account (SYS-01). Vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |
| Primary system | "Multi-tenant SaaS production platform" (registry default) is the VCP |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-04-20 | AI document extraction released to all customers |
| 2026-07-27 to 2026-08-07 | Risk assessment and gap analysis (CTO with the Operations and Finance Manager; MSP lead technician for laptops and the suite) |
| 2026-08-24 to 2026-08-26 | Control assessment (independent security consultant) |
| 2026-08-31 to 2026-09-04 | SOC 2 readiness self-assessment and AI risk assessment |
| 2026-09-15 | Deliverables approved by the Chief Executive Officer |
| 2026-11-12 | First incident response tabletop exercise (P08 scenario) |
| 2027-03-31 | Target SOC 2 Type 1 report date ("as of" date); report expected by 2027-05-31 |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Registry defaults | The primary system, P08 incident, and P10 use case are the registry defaults. The AI use case was narrowed to document extraction because that is the generative AI feature this product actually has | All |
| Customer sign-in | Customer passwords need 8 characters with no breached-password check; accounts lock for 15 minutes after 5 failed attempts; 3 customers sign in through their own single sign-on | P02, P03 |
| Former Customer Success Manager | Left in March 2026; the suite account was disabled on the last day, but the admin console and support desk accounts stayed active until P07 found them; disabled 2026-08-26. The admin console keeps no sign-in history | P01, P07 |
| Account Executive | Moved from customer support to sales in 2025 and kept an admin console account until 2026-08-26 | P07 |
| Root account | The cloud root password is in a team vault entry that all engineers and the contractor can open; its MFA device is the CTO's personal phone; unchanged since 2024 (found in P07) | P01 R-025, P07 |
| Contractor's laptop | Held the CI key and 3 production extracts with vendor tax IDs, the newest from 2026-07-14; the extracts were deleted 2026-08-28 and the deletion confirmed in writing | P07, P08 |
| Dependency alerts | 14 High-severity dependency alerts older than 30 days at fieldwork | P01, P03, P07 |
| Error tracking | 14-day retention; offers data scrubbing that is not turned on | P04, P09 |
| Model provider terms | Standard API terms say inputs are not used for training but allow retention for up to 30 days for abuse monitoring; its SOC 2 Type 2 report (Security) does not cover the zero-retention option | P03, P09, P10 |
| AI auto-accept | A customer setting that saves extracted fields without review; turned on by 31 of 45 customers | P10 |
| AI test results | 400-document test set (2026-09-02): 93.5% field-level accuracy; 7 of 250 certificates with a critical error; phone photos and handwritten forms much worse (13.9% versus 0.9%) | P03 G-034, P10 |
| AI coding assistant | The company licenses a business AI coding assistant with no training on inputs, used by the CTO, the engineers, and the contractor | P06 POL-04 4.7, P10 AI-002 |
| Uptime | External monitor: 99.94% over August 2025 to July 2026; lowest month 99.71% | P03 G-041 |
| Questionnaires | 14 customer and prospect security questionnaires answered in the last 12 months from a 2024 answer document | P03 G-040 |
| MSP contract | Covers laptops, the productivity suite, and the help desk, with a 4-business-hour response time, no recovery commitment, no security incident notice term, and no notice of technician changes. The MSP holds 2 suite global administrator accounts | P04, P05, P09 V-04 |
| Finances and payroll | A cash reserve covers about 60 days of expenses; payroll runs biweekly through an outside payroll service | P05 |
| SOC 2 plan | CPA firm to be engaged by 2026-12-15; a compliance automation tool for evidence collection from 2026-11; readiness check with the CPA firm 2027-02-28 | P01, P09 |
