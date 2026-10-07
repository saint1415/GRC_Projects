# Business Impact Analysis: Cris Santos Company | Government Services and Facilities | Sole Proprietorship

**Organization:** Cris Santos Company (facilities support contractor operating government buildings, NAICS 561210) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner, 2026-08-10, with the on-call IT technician (under NDA) | **Adopted:** Owner, 2026-09-04

## 1. Overview and purpose
This one-page BIA lists the five business functions the business depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency planning controls (CP-2, CP-9) that the city contract's security exhibit requires at the SP 800-53 Rev. 5 Moderate baseline;
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08).

## 2. Business description
One building controls technician runs the BAS and access control systems of three city buildings (CT-C) and supports the BAS of a GSA federal office building as a subcontractor (CT-F). The customers own every building system. The owner's own tools are one laptop, one phone, a business productivity suite, an accounting service, a remote-desktop subscription, the home office network, and a consumer AI chatbot. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts, or about $720 per working day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (about a week and a half of receipts) or loss of a contract | $1,000 to $5,000 | Less than $1,000 |
| Operations | A city building closes or a contract service level is missed | Work delayed but buildings run normally | Administrative delay only |
| Regulatory and contract | Breach of a contract security term, a missed incident notice, or a FAR reporting clock | Late deliverable or documentation gap | Internal policy deviation |
| Safety | Doors left unlocked, people locked in, or unsafe temperatures in an occupied public building | Comfort complaints; doors on the wrong schedule for a short time | None |
| Reputation | The city or the prime ends or does not renew the work | Complaint from the customer | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 City building operations (BAS) | High | 24 h | 4 h | 24 h |
| BP-02 City access control administration | High | 24 h | 4 h | 24 h |
| BP-03 Federal building BAS support (subcontract) | Moderate | 72 h | 24 h | 24 h |
| BP-04 Billing and contract administration | Low | 240 h | 120 h | 24 h |
| BP-05 Communications and records | Moderate | 24 h | 8 h | 24 h |

**What drives the values:** the city contract's service levels drive BP-01 and BP-02 (critical alarms worked within 4 hours; badge removals within 4 business hours). The buildings themselves are more resilient than the owner: field controllers keep running their last programs and door controllers keep their cached schedules if the owner, the supervisory controller, or the cloud service is unavailable. What fails first is the city's ability to change anything. BP-03 is lower because the prime has its own technicians and GSA's systems never sit on the owner's devices. The 24-hour RPO for BP-01 is **not supported today**: controller programs and door schedule exports exist only on the laptop and have never been restored (P01 R-005).

**Single-person dependency (the key finding).** The owner is the only BAS technician the city has, one of only two access control administrators (with the city IT manager), the only person who holds the BAS supervisory credentials, and the only contact for both customers' incident notices. Every MFA prompt goes to the owner's one phone. If the owner is ill, injured, or without the phone, BP-01 and BP-05 exceed their MTD within a day and nobody else can change a schedule or a setpoint. Actions (P01 R-006 and R-007, due 2026-12-31):
1. Ask the city in writing to pre-approve a backup controls firm for emergencies, as the contract requires for any subcontracted administration, and agree on how that firm would get temporary credentials.
2. Write a one-page manual operation sheet for each city building so the city maintenance worker can run critical equipment in hand mode.
3. Store recovery codes for the productivity suite, the password manager, and the remote-desktop service, plus a one-page emergency access sheet, in a sealed envelope held by the owner's attorney.
4. Give the city IT manager a written list of the owner's accounts in city systems so the city can disable or reset them if the owner is unavailable.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Business laptop | BAS engineering software, VPN client, controller program backups | BP-01, BP-02, BP-04 |
| SYS-03 Mobile phone | All MFA prompts; alarm texts; access control mobile app | BP-01, BP-02, BP-05 |
| SYS-02 Productivity suite | Email, alarm emails, drawings, cardholder exports, CT-F work orders | BP-01, BP-02, BP-03, BP-05 |
| City VPN and identity provider (city-run) | The approved remote path into SYS-08 | BP-01, BP-02 |
| SYS-04 Remote-desktop service | After-hours path into the city hall BAS workstation (to be removed; P01 R-001) | BP-01 |
| SYS-05 Accounting SaaS | Invoices and payments | BP-04 |
| SYS-06 Home office network | Internet for remote work; phone hotspot is the fallback | BP-01, BP-02, BP-05 |
| GSA PIV card and GSA workstation | The only way into GSA's BAS | BP-03 |
| Work van and tools | Site visits, parts, locked drawings cabinet | BP-01, BP-03 |
| People | Owner only; city IT manager as backup access control administrator | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and MFA | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Internet | 1 h | Phone hotspot |
| 3 | City VPN and access control tenant sign-in | 2 h | City IT manager resets access; city IT manager disables badges in the meantime |
| 4 | A clean laptop with the BAS engineering software | 24 h | No spare laptop today; the IT technician rebuilds or replaces it. Until then, drive to site and work at the city hall BAS workstation |
| 5 | Controller programs and door schedule copies | 24 h | Today only on the laptop; after POAM-004, from the cloud backup folder |
| 6 | Email and files | 8 h | Vendor web access from any device |
| 7 | Accounting SaaS | 120 h | Spreadsheet invoices |
