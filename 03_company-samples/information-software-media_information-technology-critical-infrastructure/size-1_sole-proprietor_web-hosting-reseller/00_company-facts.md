# Scenario facts: Cris Santos Company | Information Technology | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, a regulation, or FTC guidance, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner files Schedule C) |
| Business | Web hosting reseller (NAICS 518210). The owner resells shared web hosting, business email, and domain names under the company's own brand, using one upstream wholesale hosting provider's reseller program and one domain registrar's reseller program. The owner also sells **website care plans** (software updates, backups, malware scanning, uptime monitoring) for sites built on a popular open-source content management system (CMS), and builds a few sites a year with a freelance developer. The company owns no servers |
| Location | Florida. The owner works from a home office. No other premises |
| Workforce | The owner only (0 employees). A freelance web developer and other contracted services instead of staff |
| Customers | About 150 small business customers, about 85% in Florida and the rest in 5 other states: restaurants, real estate agents, churches, contractors, 2 small law firms, a residential property management company, and 12 online stores. The company hosts about **270 websites**, about **410 email mailboxes**, and about **230 domain registrations** |
| Care plans | **120 sites** are on care plans and are connected to the site management dashboard (SYS-04). 35 of them are on the premium plan, which adds off-site daily backups kept 30 days. The other **150 sites are "hosting only"**: the customer maintains the site software |
| Care-plan customers holding sensitive data | 9 of the 12 online stores (about 31,000 of the 38,000 shopper accounts), both law firms, and the property management company are on care plans, so their sites are connected to SYS-04. On the upstream platform a site runs as its hosting account user, so code on a site can read that account's files, including mailbox files stored in the same account |
| Personal information the company holds for customers | The 12 online stores hold about 38,000 shopper accounts (name, email, password hashed by the CMS, shipping address, order history), about 26,000 of them Florida residents. Card payments go through each store's payment processor (hosted payment fields or redirect), so card numbers are not stored on the hosted sites. The hosted mailboxes hold whatever customers send and receive. The property management company's mailboxes receive rental applications with Social Security numbers and driver license numbers, and the law firms' mailboxes hold client matter files |
| Revenue | About $180,000 a year (fictional): hosting plans of $15 to $60 a month, care plans of $79 to $199 a month, and domain renewals. About $15,000 a month, or about $490 per calendar day. SBA-small (standard $40.0 million for NAICS 518210, 13 CFR 121.201) |
| Payments | Customers pay through the customer portal (SYS-01), which embeds the payment processor's hosted card fields. The company never receives or stores card numbers. The processor's merchant agreement requires an annual PCI DSS self-assessment questionnaire (contractual, not law; last completed 2026-02) |
| Role under breach and privacy law | For data on customers' websites and in their mailboxes: a **third-party agent** under Fla. Stat. 501.171(1)(h), "contracted to maintain, store, or process personal information on behalf of a covered entity"; each customer owns its data. For its own customer contacts and customer portal sign-in credentials: the **covered entity** (501.171(1)(b) includes a sole proprietorship) |
| Customer commitments | Online Terms of Service adapted by the owner from a template in 2023: customers are responsible for their own content; "99.9% uptime guarantee" with a service credit of one month's hosting fee if missed; the company keeps account information confidential. **No security incident notice commitment.** The terms do not say who patches the CMS on hosting-only sites |
| Public statements | The website states: "Free daily backups kept for 30 days", "Enterprise-grade malware protection on every site", "Your data never leaves the USA", and "99.9% uptime guarantee" |
| Assurance | **No SOC 2 report.** In 2026 the two law firms and the property management company sent security questionnaires. The owner answered them from memory. The upstream hosting provider offers its SOC 2 Type 2 report under a nondisclosure agreement; before September 2026 it had never been requested |
| Not in scope | FedRAMP (no federal customers); CMMC and DFARS 252.204-7012 (no DoD contracts; no customer has disclosed defense work); bank service provider rule (no bank customers); HIPAA (no health care customers; the Terms of Service do not mention health information and no business associate agreement has been signed); GLBA Safeguards Rule (not a financial institution); payment card data on hosted sites (processor-hosted fields). The DOJ Data Security Program and CCPA are checked in P03 and found not to apply |
| State law approach | Florida law is cited where unavoidable (Fla. Stat. 501.171). Customers and their shoppers in other states are handled generically: "each state where affected individuals reside" |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner | Every role: owner, system administrator, support desk, security and privacy lead, incident commander, and risk acceptor |
| Freelance web developer | About 8 hours a week, U.S.-based, works from a personal laptop. Builds sites and applies care plan updates. Has a named **administrator** account on the site management dashboard (SYS-04), which reaches all 120 connected sites. **MFA is not turned on for that account.** Receives customer site and SFTP passwords from the owner by email. The freelance agreement has a confidentiality clause and no security terms |
| Contract security consultant | Independent consultant engaged by the hour for the August 2026 review: sign-in tests, configuration review, restore test, and challenge of the owner's self-review. No standing access |
| Outside accountant | Taxes and bookkeeping. Access to the accounting SaaS only |
| Breach counsel | None retained. To be identified (P08) |
| Cyber insurance | None. A technology errors and omissions policy with a cyber endorsement was quoted in August 2026; decision due 2026-12-31 |

## 3. Systems
| ID | System | Hosting | Holds customer data? | Notes |
|---|---|---|---|---|
| SYS-01 | Customer portal and billing automation | White-label client management and billing SaaS | Yes (customer contacts, portal sign-ins, invoices, tickets) | Customers sign up, pay, open tickets, and get single sign-on into their hosting control panel. **Stores the API credentials for SYS-02 and SYS-03**, so a portal administrator can create, suspend, or terminate any hosting account and change any domain's nameservers. **Owner's administrator login uses a password only** (MFA available, not turned on). Customer MFA is optional (used by 9% of customer accounts) |
| SYS-02 | Upstream reseller hosting platform | Upstream wholesale hosting provider (shared servers in U.S. data centers) | Yes (websites, databases, mailboxes) | Reseller management console plus a white-label hosting control panel for each customer account. The provider runs the servers, operating systems, hosting control software, server firewall, server-level malware scanning, and nightly backups kept 7 days. Backups are deleted with a terminated account. The reseller console uses MFA (authenticator app) and can sign in to any customer's control panel |
| SYS-03 | Domain registrar reseller account and DNS | Registrar reseller program (SaaS) | Yes (domain contact data) | About 230 domains on auto-renew charged to the owner's card. MFA on. Most DNS zones are served by SYS-02 nameservers |
| SYS-04 | Site management dashboard | Multi-site CMS management SaaS | Yes (administrator-level access to 120 sites; premium backups) | A connector plugin on each care-plan site gives the dashboard administrator-level access: bulk plugin, theme, and core updates; upload and install of any plugin package to many sites at once; one-click sign-in to each site's admin area; daily off-site backups for the 35 premium sites. Accounts: owner (MFA on) and freelance developer (MFA off). The dashboard offers MFA but does not enforce it. Activity log kept 30 days, never reviewed |
| SYS-05 | Website security and uptime service | SaaS | Yes (site files, scan findings, visitor IP addresses) | Daily malware and known-vulnerability scans and uptime checks for all 270 sites. Since 2026-05-04 its **AI alert triage** feature scores findings and auto-dismisses those it rates as false positives or low risk (P10). July 2026: 412 findings, 239 of them (58%) auto-dismissed |
| SYS-06 | Business email, file storage, and password manager | SaaS productivity suite | Incidental | Email and password manager use MFA. A spreadsheet of about **140 customer site administrator and SFTP passwords** is kept in file storage, outside the password manager |
| SYS-07 | Endpoints: one laptop and one mobile phone | Owner devices | Yes (cached downloads, site backups pulled for troubleshooting) | Laptop: full-disk encryption, automatic updates, built-in antivirus and host firewall; also used for personal purposes. Phone: the only authenticator app for every account; recovery codes are not stored offline |
| SYS-08 | Accounting SaaS and payment processor | SaaS | Billing contacts only | Card data only in the processor's hosted fields |
| SYS-09 | Consumer generative AI chat assistant | Free personal account (SaaS) | Yes (pasted log excerpts and site files) | The owner pastes server log excerpts and suspicious files into it for analysis (P10 AI-002) |

**SSP system (P02):** the *Hosting Control Plane and Customer Portal (HCP)*: SYS-01 to SYS-07 as one system boundary, with the upstream provider's servers and each SaaS vendor's platform treated as external services.

## 4. Current security posture: early (good habits in places, few formal controls)
**In place today:**
- MFA (authenticator app) on the upstream reseller console, the registrar reseller account, business email, the password manager, the payment processor, and the owner's dashboard account
- Unique passwords in a password manager for the owner's own accounts
- Laptop full-disk encryption, automatic OS updates, built-in antivirus and host firewall
- Free, automatically renewed TLS certificates on every hosted site and on the customer portal
- Upstream provider controls: server patching, server firewall, server-level malware scanning, nightly backups kept 7 days, physical security of U.S. data centers
- Daily malware and vulnerability scans and uptime checks for all 270 sites (SYS-05)
- Weekly bulk updates for the 120 care-plan sites; off-site daily backups kept 30 days for the 35 premium sites
- Online Terms of Service

**Missing:**
1. No written policies, no risk assessment, and no incident plan before this work.
2. The freelance developer's dashboard administrator account has no MFA. Any dashboard account can push code to all 120 connected sites at once, and the activity log is never reviewed.
3. The customer portal administrator login uses a password only, although the portal holds API credentials that control every hosting account and domain. Customer MFA is optional.
4. About 140 customer site and SFTP passwords sit in a spreadsheet in file storage, and credentials are sent to customers and the freelancer by plain email.
5. 235 of 270 sites rely only on the upstream provider's backups (7 days, same provider, deleted with the account). The owner has never restore-tested them. The website promises 30-day daily backups for every site.
6. No log review or sign-in alerting for the reseller console, the portal, or the dashboard. The AI triage feature auto-dismisses findings with no human review.
7. Nobody patches the 150 hosting-only sites. In August 2026 the security service flagged 64 sites running a plugin with a known vulnerability. The Terms of Service do not assign patching.
8. The owner is a single point of failure: the only person who can run support, renewals, or restores; every second factor is on one phone; recovery codes are not stored offline; no emergency access or successor arrangement exists.
9. No vendor review: the upstream SOC 2 report was never requested, and the dashboard and security service vendors' security terms and data locations were never checked.
10. Public statements are not accurate or not substantiated: 30-day backups (true for 35 sites only), "enterprise-grade malware protection on every site", "your data never leaves the USA" (not verified for SYS-04 and SYS-05), and the 99.9% uptime guarantee (no measurement before 2026-08; no service credits ever paid).
11. Customer data is pasted into a consumer AI chat assistant (SYS-09).
12. No customer security contact list and no incident notice process. The owner did not know about the 10-day third-party agent notice in Fla. Stat. 501.171(6)(a).
13. No cyber insurance and no breach counsel.
14. No security terms or training for the freelance developer, and no security training for the owner beyond self-study.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Primary system | Registry default "Hosting control plane and customer portal" kept. At this size the control plane is the reseller console, the portal that automates it, the registrar account, and the site management dashboard, all SaaS |
| P03 | FedRAMP (the vertical's primary regulation) does **not** apply: the company has no federal customer. P03 is a reasonable-security checklist under FTC Act Section 5 (15 U.S.C. 45), using the FTC's own business guidance, plus the Fla. Stat. 501.171 duties of a third-party agent and covered entity, plus the company's own public statements and Terms of Service. FedRAMP, CMMC, DFARS, the DOJ Data Security Program, the bank service provider rule, and CIRCIA are applicability checks only |
| P08 incident | Registry default kept: compromise of provider tooling affecting downstream customers. An attacker takes over the freelance developer's site management dashboard account and pushes a malicious plugin to the 120 connected customer sites |
| P09 SOC 2 | Security criteria (CC series) only. The owner's readiness self-check, plus a review of the upstream hosting provider's SOC 2 Type 2 report. No SOC 2 examination is planned at this size |
| P10 AI | Registry default adapted to one third-party tool: the AI alert triage feature in the website security service (SYS-05). The consumer AI chat assistant (SYS-09) is a second inventory row |
| Cloud | SaaS only; no IaaS. The upstream reseller hosting is treated as a SaaS-like managed service: the provider runs servers, operating systems, and hosting software; the company controls accounts, packages, and customer-level settings; customers control their own site content. Vendor-agnostic; provider names appear only in the P04 shared responsibility references |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2025-03-12 | A hosting-only customer's site was defaced through an outdated plugin and restored from the upstream backup |
| 2026-05-04 | The security service turned on AI alert triage for the owner's plan; the owner left it on |
| 2026-08-05 | A customer reported spam pages on its site. A web shell was found that the AI triage had auto-dismissed on 2026-07-21. The site was cleaned and restored |
| 2026-08-17 to 2026-08-21 | Self-assessment: BIA, risk register, gap analysis, cloud mapping, control assessment |
| 2026-08-19 | Tests with the contract security consultant: sign-in tests, account review, restore test, configuration review |
| 2026-09-03 | Nondisclosure agreement signed with the upstream provider; its SOC 2 Type 2 report received |
| 2026-09-08 to 2026-09-11 | SOC 2 self-check, upstream SOC 2 report review, AI use assessment |
| 2026-09-28 | Deliverables adopted by the owner |
| 2026-10-31 | First remediation milestones due |
