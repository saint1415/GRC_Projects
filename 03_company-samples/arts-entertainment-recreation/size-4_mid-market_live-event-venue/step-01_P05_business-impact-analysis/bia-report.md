# Business Impact Analysis: Cris Santos Company | Arts, Entertainment, and Recreation | Mid-Market

**Organization:** Cris Santos Company, Inc. (live event venue operator with ticketing; three Florida venues) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager and the GRC Analyst with the process owners named in `bia.csv` and the three venue General Managers | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: venue operations at the Amphitheater, the Music Hall, and the Club; ticketing, box offices, and the call center; food and beverage; premium seating and group sales; marketing and digital; booking; finance; HR; and the County Performing Arts Center (County PAC) services that start on 2027-07-01. It rates 15 business processes and quantifies what an outage costs in money, operations, contractual and regulatory exposure, and attendee safety.

The results feed:
- the availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08), including the event-day outage runbook;
- PCI DSS v4.0.1 Requirement 12.10.1, which expects the incident response plan to cover business recovery and continuity (N71-R04);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment for the County PAC agreement (P09).

## 2. System and business description
The company runs about 410 shows a year for about 1.55 million attendees across three Florida venues. Ticketing runs on a white-label SaaS platform, with the company as merchant of record; the checkout form is embedded in the company's own website. Box offices and all food, beverage, and merchandise sales use validated P2PE devices. The central box office, call center, premium sales, finance, and IT sit at headquarters. Systems are described in `../00_company-facts.md` section 3.

**What makes venues different:** the most time-critical window is not the business day but **the 60 to 90 minutes before doors**, when up to 19,500 people arrive at the Amphitheater at once. An outage then is a crowd safety problem before it is a revenue problem. The same outage on a dark day costs little. The values in this BIA are therefore **event-day values** for the event-day processes (BP-01 to BP-04, BP-08, BP-09, BP-14).

## 3. Impact categories and values
Dollar values are scaled to $100.0 million in annual revenue. The worst single loss event is a cancelled Amphitheater headliner, which costs about $1.2 million (about $780,000 of ticket refunds, $305,000 of food and beverage sales, $40,000 of sponsor make-goods, and $75,000 of staff and contractor costs).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per event or per day) | More than $100,000, or a cancelled show | $25,000 to $100,000 | Less than $25,000 |
| Operations | A show cannot open doors or must stop, or a venue cannot sell | One service (bars, box office, one channel) stops | Staff slowed but working |
| Contractual and regulatory | Missed acquirer or card brand notice, missed breach notice, or breach of an artist or County PAC agreement | Late settlement, late filing, or missed internal deadline | Internal policy deviation |
| Attendee safety | Crowd pressure at gates or loss of the command post's view of egress | Reduced monitoring covered by extra staff | None |
| Reputation | Regional media coverage, an artist or promoter lost, or the County PAC relationship damaged | Patron complaints and social media | Internal only |

**How loss at MTD was estimated.** Loss is revenue that is not recovered plus extra costs (overtime, refunds, penalties) over the MTD, for the worst common case (an Amphitheater show night for event-day processes). Owners estimated recovery rates: most online, phone, and premium sales shift to later rather than being lost, while food and beverage sales missed during a show are lost.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 Event entry and access control | Venue operations | High | 1 | 0.5 | 0 | $75,000 |
| 2 | BP-02 Venue safety, security, and crowd management | Venue operations | High | 2 | 1 | 24 | $40,000 |
| 3 | BP-03 Food, beverage, and merchandise sales | Food and beverage | High | 2 | 1 | 0 | $210,000 |
| 4 | BP-08 Production and show operations | Venue operations | Moderate | 1 | 0.5 | 24 | $120,000 |
| 5 | BP-04 Box office window sales and will-call | Ticketing | Moderate | 4 | 2 | 1 | $6,000 |
| 6 | BP-09 Patron communications and urgent event notices | Marketing and digital | Moderate | 4 | 2 | 24 | $15,000 |
| 7 | BP-05 Online ticket sales and high-demand on-sales | Ticketing and digital | High | 8 | 4 | 0.25 | $150,000 |
| 8 | BP-07 Show settlement and artist payments | Finance | Moderate | 24 | 12 | 4 | $25,000 |
| 9 | BP-15 County PAC ticketing and settlement services (from 2027-07-01) | Ticketing and finance | Moderate | 24 | 8 | 4 | $15,000 |
| 10 | BP-14 Event staffing and credentials | HR and venue operations | Moderate | 24 | 12 | 24 | $30,000 |
| 11 | BP-11 Guest services and accessibility requests | Ticketing | Moderate | 24 | 8 | 24 | $5,000 |
| 12 | BP-06 Phone, group, and premium seating sales | Premium seating and group sales | Moderate | 24 | 8 | 4 | $10,000 |
| 13 | BP-10 Website, marketing campaigns, and patron data platform | Marketing and digital | Low | 72 | 24 | 24 | $20,000 |
| 14 | BP-12 Booking, holds, and artist contracts | Booking | Low | 72 | 48 | 24 | $10,000 |
| 15 | BP-13 Finance, accounts payable, and payroll | Finance | Low | 120 | 72 | 24 | $20,000 |

**Summary:** 4 High, 8 Moderate, and 3 Low processes (15 in total). The sum of estimated losses at each process's MTD is $751,000.

**Enterprise-wide scenario.** If the ticketing platform and the corporate and venue networks were unavailable for 24 hours on a day with an Amphitheater headliner and shows at the Music Hall and the Club, the estimated loss is about $1.5 million if the Amphitheater show is cancelled (the $1.2 million cancellation above, plus about $150,000 of lost online demand and about $150,000 at the other two venues). If the written manual entry procedure works and the show goes ahead, the estimate falls to about $350,000. **That difference is the value of a drilled manual entry procedure at every venue** (P01 R-018).

**What drives the values:**
- **Attendee safety** drives BP-01, BP-02, and BP-08. The manual entry procedure (offline scanning, printed manifests, wristbands) is the real recovery strategy for BP-01, because no IT recovery is fast enough during doors.
- **Revenue in a short window** drives BP-03. Most food and beverage sales happen in about 2 hours per show, and the venues are cashless.
- **Artist and County PAC agreements** drive BP-05, BP-07, and BP-15. Many artist agreements fix the on-sale time and require settlement on show night. The County PAC agreement sets monthly settlement and a 48-hour incident notice.
- **An RPO of 0 or 15 minutes** for BP-01, BP-03, and BP-05 is met by the vendors (the ticketing platform, the POS vendor, and the payment partner keep the transactions), not by company backups.

## 5. Key findings
1. **The ticketing vendor's recovery commitments meet sales, not entry.** The vendor's SOC 2 system description states RTO 4 hours and RPO 15 minutes, which meets BP-04 and BP-05 but **not BP-01** (RTO 0.5 hours). BP-01 depends on scanners working offline from a manifest downloaded before doors. That download is a checklist step only at the Amphitheater (P01 R-018).
2. **The manual entry procedure exists at one venue of three.** The Amphitheater wrote and drilled its procedure in 2025 after it opened under the company. The Music Hall and the Club have none (P01 R-018; P08 event-day runbook).
3. **Offline card acceptance is unconfirmed.** Whether the POS vendor's P2PE solution allows offline acceptance is governed by its P2PE Instruction Manual. The Director of Food and Beverage must confirm with the POS vendor before relying on it for BP-03 (P01 R-019).
4. **Company-managed recovery is unproven.** The settlement application (BP-07, BP-15) and the patron data platform (BP-10) are backed up to the separate backup account, but neither has ever been restored (gap 9). Their RTOs are targets, not demonstrated capabilities (P01 R-022; P07 CP-4).
5. **The Club has one internet connection.** The Amphitheater and the Music Hall have two internet providers; the Club has one plus a cellular backup that has never carried the scanners and POS together (P01 R-020).
6. **Urgent notices depend on two vendors.** Weather holds at the Amphitheater go out through the marketing platform and the ticketing platform. Neither vendor's contract states a notice delivery commitment (P09 vendor reviews).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Ticketing platform (SaaS) | Sales, box office and call center apps, scanning manifests, reports, buyer messages | BP-01, BP-04, BP-05, BP-07, BP-09, BP-11, BP-15 |
| SYS-02 Payment partner | Gateway, virtual terminal, card vault, box office P2PE devices | BP-04, BP-05, BP-06, BP-15 |
| SYS-03 POS and P2PE devices | Food, beverage, and merchandise sales (MID-F) | BP-03, BP-07 |
| SYS-04 Website and tag manager | Event pages with the embedded checkout form | BP-05, BP-09, BP-10 |
| SYS-05 Cloud landing zone | Settlement application, patron data platform, website hosting, backups | BP-05, BP-07, BP-10, BP-15 |
| SYS-06 Identity provider | Staff sign-in to ticketing, email, cloud, CRM, finance | All staff processes |
| SYS-08 Networks and internet | SD-WAN at 4 sites; dual ISP at the Amphitheater and Music Hall; single ISP plus cellular at the Club | BP-01 to BP-04 |
| SYS-09 Scanners and endpoints | 180 scanners; 520 laptops and PCs; 64 tablets | BP-01, BP-04, BP-06, BP-07 |
| SYS-10 CCTV, crowd analytics, and door access | Monitoring and staff doors | BP-02, BP-14 |
| SYS-12 Marketing platform | Email and SMS notices | BP-09, BP-10 |
| SYS-14 Production systems | Standalone consoles | BP-08 |
| People | Door staff and security supervisors (staffing contractors), box office and call center staff, bar staff, settlement staff, IT and security team, MSSP | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Manual entry procedure for BP-01 at every venue | Immediate | Offline scanning, printed manifests, wristbands (to be written and drilled at the Music Hall and the Club; R-018) |
| 2 | SYS-10 radios, door access, CCTV | 1 h | Extra guards; manual keys |
| 3 | SYS-08 internet and Wi-Fi for scanners and POS | 1 h | Second ISP or cellular failover; scanners offline mode |
| 4 | SYS-03 POS | 1 h | Vendor support line; offline mode only if the P2PE manual allows |
| 5 | SYS-06 identity provider and break-glass access | 2 h | Two break-glass accounts per critical system, stored sealed |
| 6 | SYS-02 box office P2PE devices | 2 h | Standalone devices need no company network; spare devices at HQ |
| 7 | SYS-01 ticketing platform (vendor) | 4 h | Vendor recovery; printed will-call lists; mobile app |
| 8 | SYS-12 and SYS-01 messaging for urgent notices | 2 h | Ticketing buyer messages; social media; venue screens |
| 9 | SYS-04 website and tag manager | 4 h | Vendor-hosted fallback event pages |
| 10 | SYS-05 settlement application | 12 h | Spreadsheet settlement from ticketing and POS reports |
| 11 | SYS-16 SIEM and EDR console (MSSP) | 8 h | MSSP runs from its own platform; needed to validate clean recovery |
| 12 | SYS-05 patron data platform | 24 h | Rebuild from the ticketing API |
| 13 | SYS-11 premium CRM and SYS-02 virtual terminal | 8 h | Callback orders; card vault charges continue at the partner |
| 14 | SYS-13 finance and payroll | 72 h | Repeat the prior payroll |
