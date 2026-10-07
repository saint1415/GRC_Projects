# Business Impact Analysis: Cris Santos Company | Government Services and Facilities | Micro

**Organization:** Cris Santos Company, LLC (facilities support contractor operating government buildings, NAICS 561210) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, with OT considerations from NIST SP 800-82 Rev. 3
**Prepared by:** Office and Compliance Manager (Information Security Officer) with the owner, the Lead Controls Technician, the Security Systems Technician, the Service Coordinator, and the MSP lead technician, 2026-07-13 to 2026-07-24 | **Approved:** owner, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It supports:
- the contingency planning controls (CP-2, CP-9, CP-10) that the county security exhibit requires at the NIST SP 800-53 Rev. 5 Moderate level;
- the customers' service levels: critical alarms acknowledged within 1 hour and a technician on site within 4 hours (county and city), emergency lockdown within 15 minutes and badge removal within 4 business hours (county), and response within 1 business day (federal subcontract);
- the availability rating in the SSP (P02), the impact ratings in the risk register (P01), and the recovery order in the incident response runbook (P08).

No regulation sets recovery times for a contractor of this size. The service levels in the county and city contracts are the binding drivers. The customers keep their own continuity duties for their buildings.

## 2. System and business description
Seven employees in one Florida office suite support 8 government buildings: 4 county buildings (CT-C), 3 city buildings (CT-M), and one federal office building under a subcontract (CT-F). The company runs a managed access control and video service for the county on its own cloud tenant (SYS-01), monitors BAS alarms for the county and city through a cloud monitoring service (SYS-02) and 7 site gateways (SYS-03), and dispatches work through a CMMS (SYS-05) and the productivity suite (SYS-04). The MSP runs the office IT. See `../00_company-facts.md` sections 1 and 3.

**What keeps running without the company's systems.** The customers own the field devices. BAS field controllers keep running their last programs and schedules, and door controllers keep enforcing the last cardholder list, if the cloud services, gateways, or office fail. What stops is the company's ability to **see** alarms, **change** anything remotely, and **revoke** a badge. That is why the safety-related functions have short downtime limits even though the buildings stay up.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual receipts, about $4,400 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $13,000 (about 3 business days of receipts, or emergency overtime and equipment damage at that level) | $4,000 to $13,000 | Less than $4,000 |
| Operations | A customer's buildings go unmonitored, or no work can be dispatched | One contract or function is degraded | Staff slowed but working |
| Regulatory and contractual | Missed customer incident notice or service level; a FAR reporting clock missed; a breach of customer personal information | A documentation or timeliness lapse the customer notices | Internal policy deviation |
| Safety | Plausible harm to building occupants (doors that should be locked are open, or cooling or alarm failures in occupied buildings) | Discomfort or equipment stress without harm | None |
| Reputation | Loss of a contract renewal or local media coverage of a government building security lapse | Customer complaint to the owner | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 24x7 alarm monitoring and emergency response | High | 4 h | 2 h | 24 h |
| BP-02 Access control administration and lockdown | High | 4 h | 2 h | 1 h |
| BP-05 Service dispatch and work orders | Moderate | 24 h | 8 h | 4 h |
| BP-03 BAS operation and preventive maintenance | Moderate | 48 h | 24 h | 24 h |
| BP-07 Engineering records (programs, schedules, drawings) | Moderate | 48 h | 24 h | 24 h |
| BP-04 Federal building controls support | Moderate | 72 h | 24 h | 24 h |
| BP-06 Video retrieval and export | Low | 72 h | 24 h | 24 h |
| BP-08 Billing, payroll, purchasing, and contracts | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- BP-01 and BP-02 are set by the contract service levels and occupant safety. A 4-hour MTD matches the 4-hour on-site commitment; the 2-hour RTO leaves time to diagnose and drive.
- BP-02 has a 1-hour RPO because a badge removal or schedule change that is lost after it was made leaves a door or a credential in the wrong state without anyone knowing.
- BP-01's RPO of 24 hours covers alarm configuration and point mappings, which change rarely. Alarm and trend history is kept by the vendor.
- BP-08 tolerates 5 days because invoices are monthly, payroll is biweekly, and the cash reserve covers about 45 days of expenses.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Access control and video tenant (SaaS) | Cardholders, schedules, access history, entrance video, face pilot | Vendor platform backups and replication (SOC 2 report, see P09). **Company has no export of its own configuration** | BP-02, BP-06 |
| SYS-02 BAS monitoring service (SaaS) | Alarms, trends, graphics, remote write for county buildings | Vendor platform; the vendor publishes an uptime target but no recovery point. **No export of point mappings or alarm rules** | BP-01, BP-03 |
| SYS-03 Site gateways (7) | Tunnels from each building to SYS-02; technician VPN | Configuration exists only on each gateway and the Lead Controls Technician's laptop; 1 spare gateway in the parts room | BP-01, BP-03 |
| SYS-05 CMMS (SaaS) | Work orders, assets, preventive maintenance | Vendor platform backups | BP-03, BP-04, BP-05 |
| SYS-04 Productivity suite (SaaS) | Email, files, drawings | Vendor resilience plus the suite backup (SYS-08, 1 year). **SYS-08 has never been restore-tested** | BP-02, BP-04, BP-05, BP-07, BP-08 |
| SYS-06 Endpoints | 6 laptops, 3 rugged tablets, 7 company phones | Laptops are not backed up; the engineering folders are excluded from sync | All |
| SYS-07 Office network | Firewall, Wi-Fi, one internet line | MSP keeps the firewall configuration | BP-05, BP-08 |
| People | 3 technicians on the on-call rotation; 2 PIV holders; one person who knows the gateway configuration | Owner can cover on-call; no backup administrator for SYS-03 | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Access control and video vendor | BP-02, BP-06 (doors keep working offline) | SOC 2 Type 2 report (P09). States a disaster recovery time of 4 hours and a recovery point of 1 hour, which **misses the 2-hour RTO for BP-02** |
| BAS monitoring vendor | BP-01, BP-03 (remote) | Service terms with a 99.5% monthly uptime target; no recovery point or SOC report |
| CMMS vendor | BP-05, BP-03, BP-04 | Vendor service terms |
| MSP | Recovery of laptops, office network, suite backup restores | No recovery commitment; only a 4-business-hour response time |
| Cellular carrier | On-call phone and field connectivity for BP-01 | None; technicians can use a second carrier's hotspot kept in the on-call bag (to be bought, P01 R-013) |
| Internet provider (office) | BP-05, BP-08 | None; single line. Dispatch can run from the Service Coordinator's phone |
| Payroll service | BP-08 | Vendor service terms |

**Key findings:**
1. **Alarm monitoring and lockdown are the critical functions, and both depend on cloud services the company does not run.** The access control vendor's stated 4-hour recovery time misses the 2-hour RTO for BP-02. The compensating measures are local: the lockdown buttons at the administration building and key lockdown with guards at the other 3 county buildings. Those manual steps are not written down for the libraries or the parks building (P01 R-011).
2. **Engineering records have no real backup.** Controller programs, door schedules, and gateway configurations live only on technician laptops. The 24-hour RPO for BP-07 is a target, not today's capability (P01 R-006).
3. **The suite backup is unproven.** SYS-08 has never been restore-tested.
4. **Key-person dependency.** Only the Lead Controls Technician can rebuild a gateway, and only 3 people share on-call (P01 R-013).
5. **The MSP contract has no recovery commitment**, and the MSP does not touch the gateways at all.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | On-call phone and alarm notifications (SYS-02, SYS-06) | 1 h | Customers call the on-call phone directly; technician patrols critical equipment |
| 2 | Access control administration (SYS-01) | 2 h | Local lockdown buttons (administration building); key lockdown and guards (other county buildings) |
| 3 | Dispatch (SYS-05, SYS-04, office phones) | 8 h | Paper log; office line forwarded to the Service Coordinator's phone |
| 4 | Site gateways and remote BAS access (SYS-03, SYS-02) | 24 h | Technicians work locally at each building; spare gateway from the parts room |
| 5 | Engineering records (laptops, SYS-04, SYS-08) | 24 h | Customer copies; rebuild critical sequences from drawings |
| 6 | Federal subcontract work orders (SYS-04, SYS-05) | 24 h | Prime phones in work orders |
| 7 | Video exports (SYS-01) | 24 h | Video stays in the vendor cloud for 30 days |
| 8 | Billing and payroll (SYS-04, SYS-09) | 72 h | Payroll service repeats prior payroll |
