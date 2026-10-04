# Business Impact Analysis: Cris Santos Company | Information | Sole Proprietorship

**Organization:** Cris Santos Company (independent B2B SaaS software publisher) | **Tier:** Sole Proprietorship (owner-developer only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-developer, 2026-08-25 | **Adopted:** Owner-developer, 2026-09-25

## 1. Overview and purpose
This one-page BIA lists the five business functions the company depends on, how long each can be down, and how much data each can lose. It feeds:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the contingency section of the consolidated policy (P06, POL-01 section 11).

No regulation requires this BIA. It exists because the company sells an always-on service to about 240 small businesses, its website promises "99.9% uptime", and its two largest subscribers ask about recovery in their annual security questionnaires.

## 2. Business description
One owner-developer builds and runs a multi-tenant online booking and appointment-reminder application for small salons, barbershops, pet groomers, and home-cleaning services. The product runs on a managed application platform and managed database from one hosting provider (SYS-01) and depends on SaaS services for code and deployment, messaging, AI drafting, payments, monitoring, and support (SYS-02 to SYS-08). The owner works from a home office on one laptop and one phone (SYS-09). See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue, or about $490 per calendar day. Most cost comes from subscribers who cancel after an outage, not from lost daily revenue.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $3,000 (cancellations or credits worth more than a week of revenue) | $500 to $3,000 | Less than $500 |
| Operations | Subscribers cannot see or take bookings | Reminders, support, or releases delayed | Administrative delay only |
| Regulatory and contract | Breach notice duties or a broken contract promise to many subscribers | A missed commitment to one subscriber | Internal policy deviation |
| Safety | Not applicable. No function affects anyone's physical safety | | |
| Reputation | Public complaints or lost referrals among subscribers | Support complaints | None outside the company |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Online booking and scheduling | High | 24 h | 4 h | 1 h |
| BP-02 Appointment reminders and client messaging | Moderate | 24 h | 12 h | 1 h |
| BP-03 Subscriber support and onboarding | Moderate | 48 h | 24 h | 24 h |
| BP-04 Software development and release | Moderate | 72 h | 24 h | 24 h |
| BP-05 Subscription billing and collections | Low | 168 h | 72 h | 24 h |

**What drives the values:** subscribers run their working day from the calendar, so BP-01 sets the pace. The 1-hour RPO for BP-01 and BP-02 relies on the provider's point-in-time recovery, which only works if the production account itself survives (backups sit in the same account; P01 R-007). The 4-hour RTO for BP-01 is **only just supported**: the first restore test on 2026-08-27 took 2 hours 10 minutes, with 40 minutes spent finding commands. Billing (BP-05) can wait a week because the payment processor retries charges on its own.

**Single-person dependency (the key finding).** The owner-developer is the only developer, the only administrator, and the only person who can deploy, restore, or rotate a secret. Every second factor sits in one authenticator app on one phone, and recovery codes are not stored offline. If the owner is ill, injured, or loses the phone, every function above passes its MTD at once and subscribers cannot even get their data out. Actions (P01 R-006, due 2026-12-31):
1. Store recovery codes, a second hardware security key, and a one-page emergency access sheet (where the accounts are, how to put the platform in maintenance mode, how to send subscribers their exports) in a sealed envelope held by the owner's attorney.
2. Set up the password manager's emergency access feature for a designated trusted person, with a waiting period.
3. Sign a standby arrangement, under a nondisclosure agreement, with a freelance developer who can keep the platform running or hand subscribers their data if the owner is out for more than 3 days.
4. Keep the self-service client export in the product working and tell subscribers about it, so they never depend on the owner for their own data.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Production platform | Web application, booking pages, job worker, admin console, managed database, photo storage | BP-01, BP-02, BP-03 |
| SYS-08 Domain registrar and DNS | The domain that every booking link and email uses | BP-01, BP-02 |
| SYS-02 Source repository and CI/CD | Code and deployments; needed to ship any fix | BP-01, BP-04 |
| SYS-03 Messaging providers | SMS and email delivery of confirmations and reminders | BP-02 |
| SYS-04 AI model provider | Smart Replies drafts (optional feature) | BP-02 |
| SYS-07 Help desk and chat | Support tickets and chat | BP-03 |
| SYS-05 Payment processor | Subscription billing | BP-05 |
| SYS-09 Laptop and phone | The only administration devices; the phone holds every second factor | All |
| People | Owner-developer; freelance support contractor (about 10 hours a week) | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone, authenticator, password manager | 1 h | Recovery codes and spare security key in the sealed envelope; replacement phone from the carrier |
| 2 | A clean administration device | 2 h | Reinstall the laptop from the operating system's recovery; use a borrowed device only through the password manager's web vault |
| 3 | DNS and the domain | 1 h | Registrar support; status page on a separate domain |
| 4 | SYS-01 database and application | 4 h | Point-in-time restore to a new instance; redeploy from the repository |
| 5 | SYS-03 reminders | 12 h | Swap provider keys; subscribers call clients from the day digest |
| 6 | SYS-07 support channels | 24 h | Email from the business account |
| 7 | SYS-02 CI/CD | 24 h | Command-line deploy from the laptop |
| 8 | SYS-05 billing | 72 h | Processor retries; manual invoices |
| 9 | SYS-04 Smart Replies | When convenient | Feature flag stays off |
