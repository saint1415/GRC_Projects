# Business Impact Analysis: Cris Santos Company | Information Technology | Sole Proprietorship

**Organization:** Cris Santos Company (web hosting reseller) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner, 2026-08-18, challenged by the contract security consultant on 2026-08-19 | **Adopted:** Owner, 2026-09-28

## 1. Overview and purpose
This one-page BIA lists the five business functions the company depends on, how long each can be down, and how much data it can lose. It feeds:
- the availability rating in the system security plan (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the contingency rules in POL-01 section 11 (P06).

## 2. Business description
One person resells shared hosting, business email, and domains from one upstream wholesale hosting provider, and keeps 120 customer websites updated and scanned under care plans. About 150 small business customers depend on the company for about 270 websites and 410 mailboxes. Everything runs in SaaS tools and in the upstream provider's data centers. The company owns no servers. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue, or about $490 per calendar day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (about 10 days of revenue, or a month of service credits for most customers) | $1,000 to $5,000 | Less than $1,000 |
| Operations | Customer websites or email down, or customers cannot reach the company | Updates, provisioning, or billing delayed | Administrative delay only |
| Regulatory | A missed legal notice deadline (for example the 10-day third-party agent notice) or a deceptive-practice claim | A missed contract commitment | Internal policy deviation |
| Safety | Not applicable: no customer site supports physical safety | | |
| Reputation | Loss of several customers or public reports of compromised customer sites | Customer complaints or bad reviews | None outside the company |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Customer website and email hosting | High | 24 h | 8 h | 24 h |
| BP-02 Customer support and incident handling | High | 24 h | 4 h | 24 h |
| BP-03 Account provisioning, billing, and domain renewals | Moderate | 72 h | 24 h | 24 h |
| BP-04 Website care plan maintenance | Moderate | 72 h | 24 h | 24 h |
| BP-05 Business administration | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **BP-01** is the business. If the upstream platform or DNS fails, every customer's website and email stop together, and the 99.9% uptime guarantee allows only about 43 minutes a month. The 8-hour RTO depends on the upstream provider; the owner's part is DNS, account settings, and escalation. The 24-hour RPO is the upstream provider's nightly backup.
- **BP-02** has the shortest RTO because customers need a person during an outage or a compromise, and the Florida 10-day third-party agent clock (P03, P08) keeps running even when the owner is busy restoring.
- **BP-04** can wait 72 hours. A compromised site management dashboard is more dangerous than an unavailable one, so pausing it is an acceptable first step in P08.

**Gaps against these targets (not supported today):**
- **RPO for BP-01.** The upstream backups are the only copy for 235 sites. They are kept 7 days with the same provider and are deleted when an account is terminated, so a provider failure or a malicious account deletion could lose everything (P01 R-005).
- **The owner's own restore time is unknown.** The first restore test was run on 2026-08-19 (P07 CP-9).

**Single-person dependency (the key finding).** The owner is the only person who can run support, change DNS, restore a site, renew domains, or deal with the upstream provider. Every second factor is on one phone, and the recovery codes are not stored offline. If the owner is ill, injured, or without the phone, BP-01 and BP-02 exceed their 24-hour MTD and nobody can act for customers. The freelance developer works about 8 hours a week and has dashboard access only. Actions (P01 R-009, due 2026-12-31):
1. Store recovery codes and a one-page emergency access sheet (accounts, upstream provider and registrar support numbers, customer contact export) in a sealed envelope held by the owner's attorney.
2. Sign a written backup-operator arrangement with the freelance developer or another local hosting professional, covering outage communication, renewals, and restores, with access granted only when the envelope is opened.
3. Ask the upstream provider and the registrar how a designated person can act on the reseller account if the owner is incapacitated, and record the answer.
4. Keep a customer contact export (name, phone, email) printed and offline, updated monthly.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-02 Upstream reseller hosting platform | Servers, control panels, mailboxes, nightly backups (7 days) | BP-01, BP-03, BP-04 |
| SYS-03 Registrar reseller account and DNS | Domains and nameserver settings for about 230 domains | BP-01, BP-03 |
| SYS-01 Customer portal | Tickets, billing, provisioning automation, customer contacts | BP-02, BP-03 |
| SYS-07 Phone and laptop | Every second factor; support calls; admin access | All |
| SYS-06 Email, files, password manager | Credentials and correspondence | BP-02, BP-05 |
| SYS-04 Site management dashboard | Bulk updates, premium backups, one-click admin access | BP-04 |
| SYS-05 Security and uptime service | Scans, uptime alerts, AI triage | BP-02, BP-04 |
| People | Owner; freelance developer (about 8 hours a week); contract security consultant on call | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone, authenticator, password manager | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | A clean access device and internet | 2 h | Phone hotspot; laptop reinstalled from clean media |
| 3 | SYS-02 reseller console and customer hosting | 8 h (provider-run) | Upstream provider escalation; restore accounts from the upstream backup |
| 4 | SYS-03 registrar and DNS | 8 h | Registrar support line; nameserver records documented offline |
| 5 | SYS-01 customer portal and customer contact channel | 4 h for contacts; 24 h for billing | Printed customer contact list; phone and text |
| 6 | SYS-05 security and uptime service | 24 h | Manual checks of the most important sites |
| 7 | SYS-04 site management dashboard | 24 h, and only after it is verified clean (P08) | Site-by-site updates through each site's admin area |
| 8 | SYS-06 and SYS-08 administration tools | 72 h | Vendor portals from the phone |
