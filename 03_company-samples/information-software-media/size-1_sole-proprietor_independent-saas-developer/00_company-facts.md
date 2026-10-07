# Scenario facts: Cris Santos Company | Information | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or FTC guidance page, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-developer files Schedule C) |
| Business | Independent B2B SaaS software publisher (NAICS 513210). The owner builds, runs, and sells one multi-tenant online booking and appointment-reminder application to small appointment-based businesses: hair salons, barbershops, pet groomers, and home-cleaning services |
| Location | Florida. The owner works from a home office. No other premises |
| Workforce | The owner-developer only (0 employees). Uses a freelance support contractor and other contracted services instead of staff |
| Customers | About 240 subscriber businesses (1 to 9 locations each) in 11 states, about 70% of them in Florida. About 520 subscriber staff user accounts. About 88,000 end-client records (the subscribers' own clients), about 61,000 of them Florida residents |
| Revenue | About $180,000 a year (fictional): monthly subscriptions of $39 to $129, about $15,000 a month or $490 per calendar day. SBA-small (standard $47.0 million for NAICS 513210) |
| Data processed | For subscribers' end clients: name, mobile phone number, email address, appointment history, free-text service notes, optional home address (home-cleaning and mobile grooming), pet names, and uploaded reference photos. For subscriber staff: name, work email, role, and password (salted and hashed by the application framework). **No** Social Security numbers, government ID numbers, financial account or payment card numbers, health records, or precise geolocation are collected by design. Free-text service notes can contain anything a subscriber types |
| Payments | Subscription fees are billed through a payment processor. Subscribers can take booking deposits through their own payment processor accounts connected to the platform. Clients enter card details only on the processor's hosted checkout page, so the company never receives, stores, or transmits card numbers |
| Role under privacy and breach laws | For end-client data: a service provider acting on each subscriber's instructions, and a "third-party agent" under Fla. Stat. 501.171(1)(h); the subscriber owns the data. For subscriber staff accounts and billing contacts: the business that owns the data |
| Customer commitments (Terms of Service and DPA) | Online Terms of Service and a Data Processing Addendum (click-through, adapted by the owner from a template in 2024): subscriber data used only to provide the service; notice of a security incident affecting subscriber data without undue delay and within 72 hours of confirmation; a public sub-processor list with 14 days' notice of changes; deletion of subscriber data within 30 days after account closure; data export on request. Two larger subscribers (a 9-location salon group and a pet grooming franchise group) signed negotiated DPAs with **48-hour** incident notice and an annual security questionnaire |
| Public statements | The website security page states "bank-level 256-bit encryption", "automatic backups every day", "we never share your data with third parties", and "99.9% uptime". The Smart Replies release note (June 2026) states "your data is never used to train AI" |
| Assurance | **No SOC 2 report yet.** The owner answers about 6 security questionnaires a year from a self-written answer document. Both larger subscribers have asked for a SOC 2 report; the owner has told them one is "planned" |
| Not in scope | HIPAA (subscribers are not health care providers or health plans; no business associate agreements); GLBA Safeguards Rule (not a financial institution); payment card data (hosted checkout only); COPPA (booking pages are not directed to children; parents book for children); FCC CPNI (not a carrier); FedRAMP (no federal customers); SEC disclosure rules (not a public company). CCPA and the DOJ Data Security Program are checked and found not to apply in P03 |
| State law approach | Florida law is cited only where unavoidable (breach notification, Fla. Stat. 501.171). Subscribers and end clients in other states are handled generically: "each state where affected individuals reside" |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-developer | Every role: owner, developer, system administrator, security and privacy lead, incident commander, and risk acceptor |
| Freelance support contractor | About 10 hours a week. Answers help desk tickets and live chat and helps subscribers set up. Has a named help desk account, but **signs in to the platform's admin console with the owner's own super-admin login** (shared credential). The freelance agreement has a confidentiality clause and no security terms |
| Contract security consultant | Independent freelance consultant engaged by the hour for the August 2026 review: secret scan, configuration review, restore test, and challenge of the owner's self-review. No standing access |
| Outside accountant (CPA firm) | Taxes and bookkeeping review. Access to the accounting SaaS only |
| Outside counsel | None retained. Breach counsel to be identified (P08) |
| Cyber insurance | None. A technology errors and omissions policy with a cyber endorsement was quoted in July 2026 but not bought |

## 3. Systems
| ID | System | Hosting | Holds subscriber or end-client data? | Notes |
|---|---|---|---|---|
| SYS-01 | Production platform: web application and public booking pages, background job worker (reminders, Smart Replies calls), admin console, managed relational database, object storage for photo uploads | Managed application platform (PaaS) and managed database service from one hosting provider, one region (vendor-agnostic) | Yes | Multi-tenant. Tenant isolation is enforced in application code (every query scoped by account ID). Database: daily automated backups kept 7 days and 7-day point-in-time recovery, in the same provider account. Photo uploads: no versioning. The admin console can open and export any subscriber's account and does not log who did what. The hosting provider has a SOC 2 Type 2 report |
| SYS-02 | Source repository and CI/CD | SaaS | No (holds secrets) | Private repository for the product and one public demo repository. CI deploys with a **long-lived hosting platform API token** stored as a CI secret (created 2024, never rotated). Dependency alerts are on but not triaged |
| SYS-03 | Messaging providers: transactional email service and SMS provider | SaaS | Yes | Appointment confirmations and reminders |
| SYS-04 | Generative AI model provider (API) | SaaS | Yes | Used by Smart Replies (P10). Added June 2026. **Not on the public sub-processor list; no signed DPA** |
| SYS-05 | Payment processor | SaaS | Billing contacts only | Subscription billing; subscribers' connected accounts for deposits (hosted checkout) |
| SYS-06 | Error monitoring and uptime monitoring | SaaS | Yes (incidental) | Error reports capture request data, including end-client names and phone numbers in some errors; 90-day retention |
| SYS-07 | Help desk and live chat | SaaS | Yes (incidental) | Owner and support contractor have named accounts |
| SYS-08 | Back office SaaS: business email and file suite, accounting SaaS, password manager, domain registrar and DNS | SaaS | Incidental | Email and password manager use MFA. **The domain registrar account has a password only** |
| SYS-09 | Endpoints: one laptop and one mobile phone | Owner devices | Yes (local copy) | Laptop: full-disk encryption on, automatic updates, built-in antivirus; also used for personal purposes. Holds a **local copy of the production database** (restored from a backup in April 2026 for debugging) and the plaintext `.env` file with production secrets. Phone: the only authenticator app for every account; recovery codes not stored offline |

**Sub-processors on the public list (5):** hosting provider (SYS-01), email service and SMS provider (SYS-03), error monitoring (SYS-06), help desk (SYS-07). Missing from the list: the AI model provider (SYS-04).

**SSP system (P02):** the *Multi-tenant Booking Platform (MBP)*: SYS-01 to SYS-09 as one system boundary, with the SaaS sub-processors treated as external services.

## 4. Current security posture: early (good technical habits, few formal controls)
**In place today:**
- MFA (authenticator app) on the hosting console, source repository, business email, password manager, and payment processor
- Unique passwords in a password manager
- Laptop full-disk encryption, automatic OS updates, built-in antivirus and host firewall
- TLS on every endpoint (managed certificates); database and object storage encrypted at rest by the hosting provider
- Daily database backups and 7-day point-in-time recovery (provider feature)
- Subscriber passwords salted and hashed by the application framework; sign-in rate limiting
- Dependency alerts in the repository; framework updates about monthly
- Online Terms of Service, DPA, and public sub-processor list

**Missing:**
1. No written policies, no risk assessment, and no incident plan before this work.
2. The support contractor uses the owner's super-admin login (shared credential; no individual accountability; the admin console can open and export any subscriber's data).
3. Production secrets (hosting API token, database connection string with password, messaging and model API keys) sit in a plaintext `.env` file on the laptop and as a long-lived CI token; none has ever been rotated.
4. A full local copy of production data sits on the laptop for development.
5. No log review. The hosting audit log keeps 30 days and nobody reads it; admin console actions are not logged at all.
6. Backups were never restore-tested before 2026-08-27 and live in the same provider account as production; photo uploads have no backup or versioning.
7. The owner is a single point of failure: the only person who can deploy, operate, or restore; every second factor is on one phone; recovery codes are not stored offline.
8. The AI model provider was added in June 2026 with no DPA, no 14-day sub-processor notice, and no update to public statements. Smart Replies sends free-text service notes to the model.
9. Public statements are not accurate: "we never share your data with third parties" (six service providers receive it); "99.9% uptime" (measured 99.82% over the last 12 months); "never used to train AI" (not confirmed in any signed terms).
10. No vendor review: sub-processor SOC 2 reports and terms have not been reviewed.
11. The domain registrar account has no MFA.
12. Dependency alerts are not triaged (14 open on 2026-08-27, 2 rated high severity).
13. Data of 31 closed subscriber accounts is kept indefinitely, although the DPA promises deletion within 30 days.
14. No security or secure coding training (self-taught).
15. No cyber insurance and no breach counsel.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Reasonable-security checklist under FTC Act Section 5 (FTC business guidance), plus the company's own public and contract representations, organized so it also prepares for SOC 2. CCPA, COPPA, and the DOJ Data Security Program are applicability checks only |
| P08 incident | Cloud credential compromise exposing customer data: a malicious development package on the laptop steals the plaintext `.env` file, and the attacker uses the hosting API token and database connection string to copy the production database and photo storage. Registry default kept |
| P09 SOC 2 | Security criteria (CC series) only. The owner's readiness self-check, plus a review of the hosting provider's SOC 2 Type 2 report. The company has no SOC 2 report yet |
| P10 AI | Smart Replies: a generative AI feature embedded in the product, built on a third-party model API (the one third-party AI tool in scope). Registry default kept. The owner's AI coding assistant is listed as a Low-tier second inventory row |
| Cloud | PaaS and SaaS only; no IaaS. The tier default (SaaS tenants only) is extended to the managed application platform and managed database, because the product itself runs there. The owner manages no servers, operating systems, or networks. Vendor-agnostic; provider names appear only in the P04 equivalents table |
| Primary system | Registry default "Multi-tenant SaaS production platform" kept and named the Multi-tenant Booking Platform (MBP) |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-03-11 | 14-hour outage from a failed database migration (the only major outage in the last 12 months) |
| 2026-06-15 | Smart Replies released in beta to 30 opt-in subscribers |
| 2026-08-24 to 2026-08-28 | Self-assessment: BIA, risk register, gap analysis, cloud mapping, control assessment |
| 2026-08-27 | Tests with the contract security consultant: secret scan, configuration review, sign-in tests, restore test |
| 2026-09-08 to 2026-09-10 | SOC 2 self-check, hosting provider report review, AI use assessment |
| 2026-09-25 | Deliverables adopted by the owner-developer |
| 2026-10-31 | First remediation milestones due |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Public demo repository | The consultant's secret scan on 2026-08-27 found an old hosting API token in the commit history of the public demo repository. It had been revoked in 2025 when the owner changed hosting plans, so it was not usable. The current token was not found in any repository | P04, P07, P08 |
| Restore test | On 2026-08-27 the owner restored the production database to a scratch instance from point-in-time recovery, witnessed by the consultant. It took 2 hours 10 minutes, including 40 minutes finding the right commands | P05, P07 |
| Photo links | Uploaded photos are served from object storage through unguessable public links that never expire (found in P04 mapping) | P01, P04 |
| Data exports | When a subscriber asks for an export, the owner emails a CSV file as an attachment | P03, P04 |
| Smart Replies use | Through 2026-09-04, Smart Replies drafted about 4,100 replies. 6 of the 30 beta subscribers turned on "auto-send for booking confirmations", which sends drafts without human review | P01, P10 |
| Hosting provider assurance | The hosting provider's SOC 2 Type 2 report (Security and Availability, 12-month period ending 2026-03-31) was downloaded from its trust portal. The owner reviewed it on 2026-09-09 | P02, P09 |
| Hosting audit log | The hosting provider's account audit log keeps 30 days of console and API events | P02, P04, P08 |
| March 2026 outage impact | The 14-hour outage on 2026-03-11 led to 3 subscriber cancellations, about $2,300 a year of revenue | P05 |
| Automated tests | About 1,100 unit and integration tests run in CI on every push; none covers tenant isolation, authorization, export, or deletion | P02, P03, P09 |
| Dependency alerts | Of the 14 open alerts on 2026-08-27, the 2 high-severity ones had been open for more than 30 days | P07 |
| Smart Replies sample | In a sample of 50 beta drafts, 3 offered a time slot that was already taken; staff caught all 3 before sending | P10 |
| Hosting provider report exception | The hosting provider's SOC 2 Type 2 report notes one exception (2 of 40 sampled provider staff terminations removed access after the 1-day target), remediated | P09 |
| Subscriber deletion feature | Deleting a subscriber account removes database records but leaves uploaded photos in storage (found in owner testing on 2026-08-26) | P03 |
