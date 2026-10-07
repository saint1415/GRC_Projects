# Business Impact Analysis: Cris Santos Company | Information Technology | Micro

**Organization:** Cris Santos Company, LLC (managed cloud hosting provider) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Lead Systems Engineer (Information Security Lead) with the Operations Manager, both Systems Engineers, and one Support Engineer, 2026-07-20 to 2026-07-31 | **Approved:** Owner, 2026-09-15

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the SSP (P02) and the Availability criteria in the SOC 2 readiness check (P09);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the four-hour test in the bank service provider notification rule (12 CFR 53.4(a); 12 CFR 304.24(a)), which decides when a hosting or RMM outage must be reported to Bank A or Bank B;
- the "measures to protect against destruction, loss, or damage ... due to ... technological failures" that both bank contracts flow down from the Interagency Guidelines (12 CFR Part 30, App. B, III.C.1.h).

## 2. System and business description
Seven people run managed hosting for about 70 business customers. About 260 customer VMs run on six hypervisor hosts and one storage array in two racks at a single Florida colocation facility (DC-1). The customer portal runs in a public cloud tenant. The company also patches about 310 customer servers through a SaaS RMM tool and hosts about 190 customer DNS zones with a SaaS DNS provider. Two community banks are customers. See `../00_company-facts.md` sections 1 and 3.

The MSA makes customers responsible for their own VM backups unless they buy the backup add-on (145 of about 260 VMs). That split drives the RPO values below.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue: about $3,000 a day and $92,000 a month.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $15,000 (about 5 days of revenue, or the 25% service credit across most hosting customers) | $3,000 to $15,000 | Less than $3,000 |
| Operations | Most customers cannot run or reach their workloads | One service line or a few customers impaired | Staff slowed; customers unaffected |
| Regulatory and contractual | Bank notice duty triggered; MSA breach across many customers | Missed contractual notice or SLA for a few customers | Internal policy deviation |
| Safety | Not rated. The company runs no safety systems; customers rate safety in their own BIAs | | |
| Reputation | Loss of a bank customer or of several customers at once | Complaints or churn of one or two accounts | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Customer VM hosting | High | 4 h | 2 h | 24 h (backup add-on VMs only) |
| BP-02 Customer portal and provisioning | Moderate | 24 h | 8 h | 24 h |
| BP-03 Managed DNS | High | 4 h | 2 h | 24 h |
| BP-04 Managed server services through the RMM tool | Moderate | 72 h | 24 h | 24 h |
| BP-05 Customer support, on-call, and incident communication | High | 4 h | 2 h | 4 h |
| BP-06 Backup and restore service | Moderate | 24 h | 8 h | 24 h |
| BP-07 Security monitoring (MDR) | Moderate | 24 h | 8 h | 24 h |
| BP-08 Billing, payroll, and administration | Low | 240 h | 120 h | 24 h |

**What drives the values:**
- **Contracts and the bank rule drive BP-01.** About 7.3 hours of downtime in a month triggers the 25% credit tier. Bank A's covered services sit on the same platform, and a security incident likely to disrupt them for 4 hours or more must be reported to the bank as soon as possible. So the MTD is 4 hours.
- **The portal (BP-02) can be down longer than hosting.** Running VMs keep running. Engineers can act in the hypervisor manager for urgent requests.
- **The RMM tool (BP-04) is low on the list on purpose.** After any compromise it must be checked before anyone trusts it again (P08). Restoring a compromised tool fast would spread harm to 22 customers.
- **Customer data recovery is shared.** The company's 24-hour RPO covers only the 145 add-on VMs. For the rest, the RPO is whatever the customer's own backups give.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-03 Hosting platform | 6 hosts in one cluster, 1 storage array, 2 switches, 2 firewalls, at DC-1 | Cluster tolerates one host failure; nightly backups for add-on VMs | BP-01 |
| SYS-02 Cluster management | Hypervisor manager and host BMCs | Nightly configuration backup to SYS-05 | BP-01, BP-02 |
| SYS-01 and SYS-04 Portal and cloud tenant | Portal VM, managed database, object storage | Nightly database dump to object storage in the same account (**never restore-tested**) | BP-02, BP-08 |
| SYS-05 Backup service | Backup appliance at DC-1 with a nightly cloud copy | Local copy 14 days, cloud copy 30 days; **restores never tested and recorded** | BP-06, BP-01 |
| SYS-06 RMM tool | Agents on about 310 customer servers | Vendor-hosted; scripts and policies live only in the tool | BP-04 |
| SYS-08 Managed DNS | About 190 zones at the DNS provider | **No copy outside the provider** | BP-03 |
| SYS-07 Identity provider and suite | Sign-in for staff, VPN, ticketing, MDR console | Vendor service resilience | All |
| SYS-09 PSA | Tickets, customer contacts, documentation vault | Vendor service resilience | BP-05 |
| SYS-11 MDR platform | Log collection, triage, and escalation | MDR provider | BP-07 |
| People | 5 technical staff on one after-hours rotation; Operations Manager | The Lead Systems Engineer is the only person who has rebuilt the cluster (key-person risk, P01 R-018) | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Colocation provider (DC-1) | BP-01, BP-02 (management), BP-06 (local copy) | SOC 2 Type 2 report reviewed 2026-08-26 (P09); redundant power and cooling described; no commitment for a site loss |
| Public cloud provider | BP-02, BP-06 (cloud copy) | Provider's standard service commitments; the company uses a single region |
| RMM vendor | BP-04 | None reviewed; contract has no security or incident notice terms |
| SaaS DNS provider | BP-03 | Provider's published service commitment; no account-recovery plan at the company |
| MDR provider | BP-07 | MDR service contract (24x7); no SOC 2 report requested yet |
| PSA, suite, and identity vendors | BP-05, BP-08, sign-in for all | Vendors' standard commitments |
| Hardware vendor | BP-01 parts | Next-business-day parts contract on hosts and the storage array |
| Payroll service and payment processor | BP-08 | Vendors' standard commitments |

**Key findings:**
1. **There is no second site.** A host failure meets the 2-hour RTO, but a DC-1 loss (hurricane, fire, or facility failure) strands all 260 VMs. Only the 145 add-on VMs could be restored, and only into the cloud tenant, which nobody has tried. Realistic recovery after a site loss is days, not hours (P01 R-009).
2. **Backups are unproven and exposed.** Nobody has run and recorded a restore test, and the cloud copy sits in the same account as the portal, so one stolen administrator credential could delete both (P01 R-002).
3. **DNS has no off-provider copy.** Losing the DNS account would leave about 190 customer zones to be rebuilt by hand (P01 R-025). A nightly zone export fixes the RPO.
4. **The bank clock sits inside the hosting MTD.** Any incident likely to disrupt Bank A's VMs or either bank's managed servers for 4 hours or more needs a determination within the first hours. The P08 runbook puts that decision at the 2-hour mark.
5. **One person holds the recovery knowledge.** The Lead Systems Engineer has done every cluster rebuild. A written recovery runbook and a second trained engineer are needed (P01 R-018).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | DC-1 network, firewalls, VPN, and cluster management (SYS-03, SYS-02) | 2 h | Colocation remote hands for power cycling; engineer on site within 1 hour |
| 2 | Managed DNS account (SYS-08) | 2 h | Rebuild urgent zones from the nightly export (once POAM-006 closes); registrar DNS as a stopgap |
| 3 | Support line, ticketing, and contact lists (SYS-09) | 2 h | Phone forwarding to on-call mobile; printed contact list in the incident kit |
| 4 | Customer portal (SYS-01, SYS-04) | 8 h | Engineers act in the hypervisor manager on verified requests |
| 5 | Backup service (SYS-05) | 8 h | Cloud copy if the appliance is down |
| 6 | MDR monitoring (SYS-11) | 8 h | EDR keeps blocking locally; identity provider email alerts |
| 7 | RMM tool (SYS-06) | 24 h, **after integrity validation** | Customers' own remote access with their approval |
| 8 | Billing, payroll, and administration | 120 h | Prior-month invoices; repeat payroll |

**Identity comes first in practice.** Every step above needs an administrator sign-in. Two break-glass accounts per critical system (identity provider, cloud tenant, hypervisor manager, RMM tool) will be created, sealed, and stored offline (POL-02 B.7; POAM-002).
