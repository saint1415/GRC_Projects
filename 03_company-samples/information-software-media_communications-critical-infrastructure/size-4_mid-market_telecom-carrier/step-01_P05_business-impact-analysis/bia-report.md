# Business Impact Analysis: Cris Santos Company | Communications | Mid-Market

**Organization:** Cris Santos Company, Inc. (regional broadband and wired telecommunications carrier) | **Tier:** Mid-Market (850 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager and the GRC analyst with the vCISO and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-17 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: Network Operations, Business Services, Customer Operations, Field Operations, Billing and Finance, Sales and Marketing, Regulatory and Legal, and corporate functions. It rates 16 business processes and quantifies what an outage costs in money, operations, regulatory exposure, public safety, and reputation.

For a carrier, several downtime limits are set by regulatory clocks and by 911, not by revenue. An outage that potentially affects a PSAP must be reported to that PSAP within 30 minutes and to the FCC within 120 minutes for wireline service (47 CFR 4.9(h)(4), 4.9(f)). Five company central offices are the last service-provider facility before 7 PSAPs, which makes the company a covered 911 service provider with physical diversity, backup power, and monitoring duties (47 CFR 9.19). Those clocks and duties keep running during a cyberattack.

The results feed:
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the 911 reliability rows of the gap analysis (P03);
- the recovery order in both incident runbooks (P08);
- the Availability criteria and SLA commitments in the SOC 2 readiness assessment for Business Services (P09);
- the IT contingency plan the company is writing (P07 POAM-010).

## 2. System and business description
The company serves about 205,000 accounts in parts of 11 Florida counties from 9 central offices, 2 metro POPs, and 268 remote cabinets: broadband for about 197,000 subscribers, about 74,000 voice lines, protected business data circuits for 3,400 sites, and Business Services (hosted voice, managed SD-WAN, colocation) for about 600 business customers. Operations run on the Network Operations and Customer Billing Platform (OSS/BSS) described in the SSP (P02): the SaaS BSS, the legacy CLEC billing system, the OSS, mediation, and portal in a 5-account cloud landing zone, the identity provider, the SIEM, and the network management plane. See `../00_company-facts.md` sections 1, 3, and 7.

## 3. Impact categories and values
Dollar values are scaled to $318 million in annual receipts, about $871,000 per day: residential broadband about $411,000, business data services about $197,000, voice about $126,000, Business Services about $104,000, and other about $33,000.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per event) | More than $100,000 in lost revenue, SLA credits, and extra labor, or more than $2 million of cash delayed | $20,000 to $100,000 | Less than $20,000 |
| Operations | Service lost across a central office serving area, or a business unit cannot deliver its core service | One service, one cabinet area, or one department stops | Staff slowed but working |
| Regulatory | Missed PSAP, NORS, CPNI breach, CALEA, or 911 reliability duty; FCC enforcement exposure | Late filing, documentation gap, or contract SLA breach | Internal policy deviation |
| Public safety | 911 calls cannot be completed or answered for part of the service area | 911 degraded but calls complete through alternates | None |
| Reputation | Regional media coverage, county or state inquiries, loss of a government or hospital customer | Customer complaints and social media | Internal only |

**How loss at MTD was estimated.** Estimated loss is unrecovered revenue plus SLA credits plus extra labor over the MTD. Process owners supplied the assumptions: subscription revenue is not lost for short outages, but SLA credits (10% to 25% of monthly charges for affected business circuits and hosted voice customers after the SLA threshold) and overtime are. For billing (BP-13), the loss is toll revenue lost if switch CDR buffers overflow plus overtime; delayed cash is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 Voice service and 911 call completion | Network Operations | High | 2 | 1 | 24 | $45,000 |
| 1 | BP-04 Network monitoring, outage response, and regulatory outage reporting | Network Operations | High | 1 | 0.5 | 1 | $5,000 |
| 2 | BP-02 911 facilities serving PSAPs (covered 911 service) | Network Operations | High | 1 | 0.5 | 24 | $10,000 |
| 2 | BP-06 Hosted voice (UCaaS) for business customers | Business Services | High | 2 | 1 | 0.25 | $40,000 |
| 3 | BP-03 Broadband internet service delivery | Network Operations | High | 4 | 2 | 24 | $60,000 |
| 3 | BP-05 Business data services | Network Operations | High | 4 | 2 | 24 | $120,000 |
| 4 | BP-08 Lawful-intercept support (CALEA) | Network Operations | High | 8 | 4 | 24 | $5,000 |
| 5 | BP-09 Customer care and account support | Customer Operations | High | 24 | 8 | 1 | $70,000 |
| 6 | BP-07 Managed SD-WAN and firewall service | Business Services | Moderate | 8 | 4 | 24 | $25,000 |
| 6 | BP-12 Field operations and repair dispatch | Field Operations | Moderate | 24 | 8 | 4 | $35,000 |
| 7 | BP-11 Service provisioning and activation | Network Operations | Moderate | 48 | 24 | 4 | $40,000 |
| 7 | BP-15 Regulatory filings and robocall traceback response | Regulatory and Legal | Moderate | 24 | 8 | 24 | $5,000 |
| 8 | BP-13 Billing, mediation, and collections | Billing and Finance | Moderate | 120 | 72 | 24 | $90,000 (plus about $4.2 million cash delayed) |
| 9 | BP-10 Retail store operations | Customer Operations | Low | 72 | 24 | 24 | $15,000 |
| 9 | BP-16 Payroll, HR, and finance | Corporate | Low | 120 | 72 | 24 | $25,000 |
| 10 | BP-14 CPNI-based marketing and campaign management | Sales and Marketing | Low | 336 | 168 | 24 | $20,000 |

Processes that share a priority number are recovered in parallel by different teams.

**Summary:** 8 High, 5 Moderate, and 3 Low processes (16 in total). The sum of estimated losses at each process's MTD is $610,000.

**Enterprise-wide scenario.** If corporate IT and the cloud landing zone were down for 72 hours (for example, ransomware; P08 second runbook) while the network kept passing traffic, the company would lose about $310,000 (care overtime and lost sales $210,000, deferred installs $60,000, dispatch overtime $40,000) and delay about $2.6 million of billing. If the attack also reached the management plane and caused a service-area outage, SLA credits alone could exceed $500,000 in the first day, and 911 duties would apply. Incident response and notification costs come on top (P01 R-001 to R-004).

**What drives the values:**
- **Public safety drives BP-01, BP-02, BP-04, and BP-06.** The 30-minute PSAP clock sets BP-04's RTO. BP-02's MTD of 1 hour reflects that a PSAP without trunks cannot answer local 911 calls.
- **SLA credits, not subscription revenue, drive BP-05 and BP-06.** A 4-hour outage of protected business circuits costs about $120,000 in credits.
- **BP-13's RTO is set by the switches, not the bill cycle.** Switches buffer CDRs for 72 hours. If mediation is down longer, toll records are lost. Those records are CPNI that customers may dispute.
- **BP-09 is High because outages create call surges,** and agents must still authenticate callers before discussing call detail (47 CFR 64.2010(b)).
- **BP-15 has a 24-hour MTD** because robocall traceback requests must be answered within 24 hours (47 CFR 64.6305(a)(2)).

## 5. Key findings
1. **The network side is engineered for availability; the IT side is not proven.** Voice has two geo-redundant core nodes, protected rings carry business circuits, and the NOC can move to CO-4. But cloud restores have been tested only for the OSS. The RTOs for mediation (BP-13), the portal (BP-09), and the data warehouse (BP-14) are targets, not demonstrated capabilities (gap 9; P01 R-026; P07 CP-4).
2. **Network element recovery at scale is untested.** Nightly configuration backups exist for every element, with a copy at CO-4, but no one has restored more than a handful of devices at once. A destructive attack on the 268 cabinet switches (P01 R-004) would rely on that untested capability (P01 R-027).
3. **911 facilities have two known single points of failure.** Two of 14 legacy 911 circuit pairs share a fiber segment, and the CO-6 generator failed its full-load test in 2026-05 (gap 11; P01 R-014, R-015). Both affect BP-02 directly.
4. **The BSS vendor's recovery objectives do not meet the BIA.** The vendor's SOC 2 system description states RTO 12 hours and RPO 1 hour. Customer care (BP-09) needs RTO 8 hours. The hourly offline account report covers authentication and balances, so care can run in a reduced mode, but not for 12 hours of peak outage traffic (P01 R-025; P09 vendor review).
5. **Hosted voice has the tightest data objective.** Customers change call routing many times a day, so the RPO is 15 minutes. The standby cluster node replicates continuously, but backups of the cluster configuration run nightly and have never been restored (P09 A1.3).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-07 Voice core | Softswitch nodes at CO-1 and CO-4, 4 SBCs, TDM host switches, SS7 hub link, STIR/SHAKEN signing, 911 trunks | BP-01, BP-02, BP-06, BP-08, BP-13 |
| SYS-08 IP/MPLS and access network | Core and edge routers, broadband network gateways, OLTs, DSLAMs, 268 cabinet switches, POP switches, DNS and DHCP | BP-01, BP-02, BP-03, BP-05 |
| SYS-09 Network management plane | NOC monitoring, element managers, TACACS+, syslog, configuration backups, jump hosts | BP-01 to BP-05, BP-07, BP-12 |
| SYS-10 Lawful-intercept mediation | Mediation appliance and TTP link | BP-08 |
| SYS-01 BSS (SaaS) and SYS-18 legacy CLEC billing | Accounts, billing, CPNI approvals, agent desktop | BP-09, BP-11, BP-13, BP-14 |
| SYS-02 OSS (cloud) | Inventory, provisioning, tickets, dispatch | BP-04, BP-11, BP-12 |
| SYS-03 Mediation and rating (cloud) | CDR collection, rating, archive | BP-13, BP-15 |
| SYS-04 portal, SYS-11 contact center, SYS-12 chatbot | Customer channels | BP-09 |
| SYS-15 Business Services platform | Hosted voice cluster, SD-WAN orchestrator, colocation | BP-06, BP-07 |
| SYS-05 identity provider; SYS-13 landing zone; SYS-16 SIEM | Sign-in, hosting, backups, detection | All |
| Power and facilities | Central office generators (72 hours of fuel) and batteries (about 8 hours); cabinet batteries (about 8 hours); CO-1 data hall cooling | BP-01 to BP-06 |
| Third parties | State NG911 system service provider, SS7 hub, upstream transit providers, STI certificate authority, BSS vendor, CCaaS vendor, chatbot vendor, CALEA TTP, overflow call center, SD-WAN orchestrator vendor | As listed in `bia.csv` |
| People | NOC (24x7, 48 staff), network engineers, 290 field staff, 140 care agents, Business Services engineers, 4 CALEA-authorized employees | As listed in `bia.csv` |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-09 NOC monitoring (CO-1 or CO-4) and printed PSAP contacts | 0.5 h | Secondary NOC at CO-4; NORS filed from any internet connection |
| 2 | SYS-07 voice core and 911 trunks; BP-02 911 facilities | 0.5 to 1 h | Fail to the CO-4 node; diverse circuit of each pair; state NG911 provider re-routes to backup PSAPs |
| 3 | SYS-05 identity provider and break-glass accounts | 1 h | Vendor-hosted; sealed break-glass accounts for the IdP, cloud, and network elements |
| 4 | SYS-15 hosted voice cluster | 1 h | Standby node; main-number forwarding through the customer portal |
| 5 | SYS-08 core and access network | 2 h | Restore element configurations from the CO-4 copy; protected rings |
| 6 | SYS-10 lawful-intercept mediation | 4 h | TTP re-provisions from its order records |
| 7 | SYS-15 SD-WAN orchestrator access | 4 h | Direct console access through jump hosts |
| 8 | SYS-01 BSS and SYS-11 contact center | 8 h (BSS vendor states 12 h) | Hourly offline account report; callback queue |
| 9 | SYS-02 OSS | 8 h (dispatch), 24 h (provisioning) | Phone dispatch; paper work orders |
| 10 | SYS-16 SIEM and EDR console | 8 h | MDR runs from its own platform; needed to validate clean recovery |
| 11 | SYS-03 mediation and rating | 72 h | Switch CDR buffers (72 hours) |
| 12 | SYS-04 portal and SYS-12 chatbot | 24 h | Phone channel; status page; chatbot outage-message mode |
| 13 | SYS-18 legacy CLEC billing; payroll and finance SaaS | 72 h | Hold bill cycles; repeat prior payroll |
| 14 | SYS-13 data warehouse | 168 h | Pause CPNI-based campaigns |
