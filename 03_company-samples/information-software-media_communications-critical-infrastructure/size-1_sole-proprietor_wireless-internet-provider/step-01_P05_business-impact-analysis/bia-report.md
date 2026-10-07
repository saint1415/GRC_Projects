# Business Impact Analysis: Cris Santos Company | Communications | Sole Proprietorship

**Organization:** Cris Santos Company (owner-operated wireless internet service provider) | **Tier:** Sole Proprietorship (owner-operator only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-operator, 2026-07-21, with the on-call network consultant | **Adopted:** Owner-operator, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the company depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the contingency section of the consolidated policy (POL-01 section 11).

No regulation requires a BIA from this business. The CPNI rules require "reasonable measures" to protect CPNI (47 CFR 64.2010(a)), and knowing which systems hold CPNI and how fast they must come back is part of that.

## 2. Business description
One owner-operator runs a fixed wireless internet service for about 310 rural accounts in Florida from a home office, with the network core in a locked shed at the base of the owner's tower (SITE-1) and access points on three more towers (SITE-2 to SITE-4). 52 accounts also buy a home phone add-on (58 interconnected VoIP lines) that the company sells under its own name from a wholesale VoIP platform. The company has no employees. The subscriber billing platform, the VoIP reseller portal, the cloud radio controller, email, and accounting are SaaS. The network itself is owner-operated equipment. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue, or about $490 per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $3,500 (about a week of revenue, or credits plus emergency repair) | $500 to $3,500 | Less than $500 |
| Operations | Most subscribers without service | One tower site or one function down | Administrative delay only |
| Regulatory | Reportable CPNI breach; missed FCC filing or 911 duty | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Home phone customers cannot call 911 | Delayed contact for customers who rely on the service | None |
| Reputation | Customers switch to another provider in numbers (rural customers have one or two alternatives) | Complaints and online reviews | None outside the company |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Internet service delivery | High | 8 h | 4 h | 24 h |
| BP-02 Home phone service (VoIP add-on) | High | 8 h | 4 h | 24 h |
| BP-03 Customer support and outage communications | Moderate | 24 h | 8 h | 24 h |
| BP-04 Billing and payments | Moderate | 120 h | 72 h | 24 h |
| BP-05 Installations, field service, and tower work | Low | 120 h | 72 h | 24 h |

**What drives the values:** every subscriber depends on BP-01 at once, and the home phone lines (BP-02) ride on it, so a network outage is also a 911 outage for 52 households. Billing (BP-04) can wait several days because autopay can be rerun. The 24-hour RPO for BP-02 and BP-04 is met by the wholesale VoIP platform's and billing vendor's backups (the billing vendor's is confirmed in its SOC 2 report, P09). **The 24-hour RPO for BP-01 is not supported today:** the last saved router and switch configuration is 4 months old, and nobody has tested a restore (P01 R-011).

**Single-person dependency (the key finding).** The owner-operator is the only network engineer, the only person with the router, VoIP portal, billing, and radio controller credentials, the only support contact, and the officer for the CPNI and CALEA duties. The second factor for every SaaS account is on the owner's one phone. If the owner is ill, injured, or without the phone during an outage, BP-01 and BP-02 pass their 8-hour MTD and nobody can tell customers why. Actions (P01 R-010, due 2026-12-31):
1. Store an emergency access sheet (router and portal recovery steps, MFA recovery codes, vendor support numbers) in a sealed envelope with the owner's attorney, for release to the on-call network consultant.
2. Sign a short standby agreement with the network consultant to restore service if the owner cannot.
3. Record a voicemail and text-line message that points customers to the website outage banner.
4. Ask the wholesale VoIP provider how a designated person can reach the reseller account if the owner is incapacitated, and record the answer.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-05 Network | Edge router, core switch, upstream circuit, backhaul, access points, customer radios, ATAs; spare router in the shed | BP-01, BP-02 |
| SITE-1 power | Batteries for about 2 hours; generator started by hand | BP-01, BP-02 |
| SYS-02 VoIP reseller portal | Lines, 911 addresses, CDRs, call forwarding | BP-02, BP-04 |
| SYS-04 Cloud radio controller | Radio configuration, firmware, alerts | BP-01, BP-05 |
| SYS-01 Billing platform | Accounts, invoices, text line, portal | BP-03, BP-04 |
| SYS-08 AI support assistant | Answers on the portal chat and text line | BP-03 |
| SYS-06 Laptop and phone | Management access; MFA app; support calls | All |
| SYS-03 and SYS-07 | Email and files; accounting | BP-03, BP-04 |
| Contracted services | Upstream fiber provider, wholesale VoIP provider, network consultant, tower contractor, bookkeeper | BP-01, BP-02, BP-04, BP-05 |
| People | Owner-operator only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and MFA | 1 h | Recovery codes in the sealed envelope; replacement phone from the mobile carrier |
| 2 | SITE-1 power and upstream circuit | 2 h | Start the generator; call the upstream provider's repair line |
| 3 | Edge router and core switch | 4 h | Spare router loaded with the last saved configuration (POL-01 11.3 sets a weekly copy) |
| 4 | Home phone lines and 911 addresses (SYS-02) | 4 h (vendor-hosted) | Forward lines to customers' mobile numbers through the wholesale provider |
| 5 | Access points and backhaul (SYS-04) | 8 h per site | Swap radios from spares; contractor climb if needed |
| 6 | Customer support channels (SYS-01, SYS-08) | 8 h | Owner's mobile and voicemail greeting; turn the AI assistant off |
| 7 | Billing run (SYS-01, SYS-07) | 72 h | Delay invoices; processor keeps taking payments |
