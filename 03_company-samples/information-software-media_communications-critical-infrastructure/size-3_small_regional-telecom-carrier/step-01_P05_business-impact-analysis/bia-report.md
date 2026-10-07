# Business Impact Analysis: Cris Santos Company | Communications | Small

**Organization:** Cris Santos Company, LLC (regional broadband and wired telecommunications carrier) | **Tier:** Small (250 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager with the NOC Manager, Director of Customer Operations, and Billing Manager | **Approved:** COO, 2026-09-04

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the OSS/BSS recovery plan the company does not yet have (P03 G-060).

For a carrier, some downtime drivers are regulatory clocks, not only revenue. An outage that affects 911 must be reported to the affected PSAP within 30 minutes and to the FCC within 120 minutes (47 CFR 4.9(h)(4) and 4.9(f)). Those clocks keep running during a cyber incident.

## 2. System and business description
The company serves about 64,000 accounts in three Florida counties from two central offices and 42 remote cabinets: broadband for about 61,000 subscribers, 23,400 voice lines, and dedicated Ethernet for business and government customers. Operations run on the Network Operations and Customer Billing Platform (OSS/BSS): a SaaS billing and care system, a cloud tenant hosting the OSS, mediation, and customer portal, an identity provider, and the network management plane. See `../00_company-facts.md` sections 1 and 3.

## 3. Impact categories and values
Dollar values are scaled to $92.4 million in annual receipts, about $253,000 per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $500,000 (about 2 days of revenue, including SLA credits) | $100,000 to $500,000 | Less than $100,000 |
| Operations | Service lost across a central office serving area, or care cannot reach customers | One service, one cabinet area, or one department stops | Staff slowed but working |
| Regulatory | Missed FCC outage, PSAP, CPNI breach, or CALEA duty | Late filing or documentation gap | Internal policy deviation |
| Public safety | 911 calling unavailable for part of the service area | 911 degraded but calls complete through alternates | None |
| Reputation | Regional media coverage, county or state inquiries, loss of government contracts | Customer complaints and social media | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Voice service and 911 call completion | High | 2 h | 1 h | 24 h |
| BP-02 Broadband internet service delivery | High | 4 h | 2 h | 24 h |
| BP-03 Network monitoring, outage response, regulatory outage reporting | High | 2 h | 1 h | 1 h |
| BP-04 Lawful-intercept support (CALEA) | High | 8 h | 4 h | 24 h |
| BP-05 Customer care and account support | High | 24 h | 8 h | 1 h |
| BP-06 Service provisioning and activation | Moderate | 48 h | 24 h | 4 h |
| BP-07 Field operations and repair dispatch | Moderate | 24 h | 8 h | 4 h |
| BP-08 Billing, mediation, and collections | Moderate | 120 h | 72 h | 24 h |
| BP-09 Payroll, HR, and finance | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Public safety drives BP-01 and BP-03.** The RPO for network elements is the age of the last nightly configuration backup (24 h). Their recovery depends on those backups being intact and reachable, which today they may not be (P01 R-025).
- **BP-08's RTO is set by the switches, not the bill cycle.** Switches buffer CDRs for 72 hours. If mediation is down longer, toll records are lost. That is lost revenue and also a gap in the CPNI record customers can dispute.
- **BP-05 is High because outages create call surges.** Customers call when the network fails, and agents must still authenticate callers before discussing call detail (47 CFR 64.2010(b)).

**Key finding:** the network processes (BP-01 to BP-03) have engineered redundancy (a second SBC, a backup NOC workspace) and practiced storm procedures. The IT side does not: the cloud tenant's backups sit in the production account and have **never been restore-tested**, so the RTOs for BP-06 and BP-08 are unproven (P01 R-008). The BSS vendor's stated 4-hour RTO and 1-hour RPO meet BP-05 (P09 vendor review).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-07 Voice core | Softswitch, SBCs at CO-1 and CO-2, TDM switch, SS7 hub link, 911 trunks | BP-01, BP-04, BP-08 |
| SYS-08 IP/MPLS and access network | Core and edge routers, OLTs, DSLAMs, cabinet switches, DNS and DHCP | BP-01, BP-02 |
| SYS-09 Network management plane | NOC monitoring, element managers, TACACS+, syslog, configuration backups, jump hosts | BP-01, BP-02, BP-03, BP-07 |
| SYS-10 Lawful-intercept mediation | Mediation appliance and TTP link | BP-04 |
| SYS-01 BSS (SaaS) | Accounts, billing, CPNI approvals, agent desktop | BP-05, BP-06, BP-08 |
| SYS-02 OSS (cloud tenant) | Inventory, provisioning, tickets, dispatch | BP-03, BP-06, BP-07 |
| SYS-03 Mediation and rating (cloud tenant) | CDR collection, rating, archive | BP-08 |
| SYS-04 Portal and app; SYS-11 contact center; SYS-12 chatbot | Customer channels | BP-05 |
| SYS-05 Identity provider | Workforce sign-in and MFA | All |
| Power and facilities | CO-1 and CO-2 generators with 72 hours of fuel; cabinet batteries (about 8 hours) | BP-01, BP-02 |
| Third parties | NG911 system service provider, SS7 hub, upstream transit, BSS vendor, CCaaS vendor, CALEA TTP, overflow call center | As listed in `bia.csv` |
| People | NOC (24x7), network engineers, field technicians, care agents, 3 CALEA-authorized employees | As listed in `bia.csv` |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-07 voice core and 911 trunks | 1 h | Fail VoIP to the CO-2 SBC; PSAP notification in parallel |
| 2 | SYS-09 management plane (clean jump host, TACACS+, configuration backups) | 1 h | Break-glass local console access with sealed credentials (to be created; P07 POAM-003) |
| 3 | SYS-08 core and access network | 2 h | Restore device configurations from the offline copy (to be created; R-025) |
| 4 | SYS-05 identity provider | 2 h | Vendor-hosted; break-glass administrator accounts |
| 5 | SYS-10 lawful-intercept mediation | 4 h | TTP re-provisions from its order records |
| 6 | SYS-01 BSS and SYS-11 contact center | 8 h | Vendor-hosted; offline account report; callback queue |
| 7 | SYS-02 OSS | 24 h | Paper work orders; phone dispatch |
| 8 | SYS-03 mediation and rating | 72 h | Switch CDR buffers (72 hours) |
| 9 | SYS-04 portal and SYS-12 chatbot | 72 h | Phone channel; status page |
| 10 | Payroll SaaS | 72 h | Repeat prior payroll |
