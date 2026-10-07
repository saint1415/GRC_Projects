# Business Impact Analysis: Cris Santos Company | Information Technology | Small

**Organization:** Cris Santos Company, LLC (cloud hosting and managed infrastructure provider) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Information Security Officer) with the Director of Platform Engineering, the Engineering Manager (Control Plane), the NOC and Support Manager, and the Managed Services Lead | **Approved:** Chief Operating Officer, 2026-09-25

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency planning controls (CP-2, CP-9, CP-10) that the FedRAMP Rev5 Class C control list requires (P03);
- the availability rating in the SSP (P02) and the Availability criteria in the SOC 2 readiness assessment (P09);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the 4-hour threshold in the bank service provider notification rule (12 CFR 53.4(a); 225.303(a); 304.24(a)).

## 2. System and business description
The company hosts about 2,300 customer virtual machines on company-owned hypervisor clusters in two colocation facilities (DC-1 in Florida, DC-2 in another state). It also runs managed services for 58 customers through an RMM tool, and authoritative DNS for hosted domains. Customers manage their services through the Hosting Control Plane and Customer Portal (HCP), which runs in a public cloud tenant. See `../00_company-facts.md` sections 1 and 3.

The MSA makes customers responsible for backing up their own VM data unless they buy the replication tier (about 30% of VMs). That split drives the RPO values below.

## 3. Impact categories and values
Dollar values are scaled to $24.0 million in annual revenue, about $66,000 per day and $2.0 million per month.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $250,000 (about 4 days of revenue, or the 25% SLA credit tier) | $50,000 to $250,000 | Less than $50,000 |
| Operations | Most customers cannot run or reach their workloads | One service line, cluster, or data center impaired | Staff slowed but customers unaffected |
| Regulatory and contractual | Bank notification duty triggered; MSA breach across many customers; incident that would be FedRAMP reportable once certified | Missed contractual notice or SLA for a few customers | Internal policy deviation |
| Safety | Not rated. The company does not operate safety systems; customer safety impacts are covered by customers' own BIAs | | |
| Reputation | Trade press coverage, loss of bank customers, or loss of the prospective agency sponsor | Customer complaints or churn of a few accounts | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Customer workload hosting | High | 4 h | 2 h | 15 min (replication tier only) |
| BP-02 Control plane and customer portal | High | 8 h | 4 h | 1 h |
| BP-03 Authoritative DNS and edge network | High | 2 h | 1 h | 24 h |
| BP-04 Managed services through the RMM tool | Moderate | 72 h | 24 h | 24 h |
| BP-05 24x7 NOC and customer support | High | 4 h | 2 h | 4 h |
| BP-06 Software and VM template delivery | Moderate | 72 h | 48 h | 24 h |
| BP-07 Security monitoring and incident response | Moderate | 24 h | 8 h | 1 h |
| BP-08 Billing and collections | Low | 240 h | 120 h | 24 h |
| BP-09 Sales, onboarding, and contracts | Low | 120 h | 72 h | 24 h |
| BP-10 Payroll and HR | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Contracts drive BP-01 and BP-03.** A full outage of about 7 hours in one month drops availability below 99.0%, which triggers the 25% credit tier (about $350,000). The bank customers' 4-hour notification threshold sits inside the same window, so the MTD is 4 hours for hosting and 2 hours for DNS and routing, since nothing is reachable without them.
- **The control plane (BP-02) can be down longer than hosting.** Running VMs keep running without it. After a business day, though, customers cannot recover their own workloads and support volume overwhelms the NOC.
- **The RMM tool (BP-04) is deliberately low on the list.** After any compromise it must be validated before it is trusted again (P08). A fast restore of a compromised tool would spread harm.
- **Customer data recovery is shared.** The company commits to a 15-minute RPO only for replicated VMs. For the other 70%, the RPO is whatever the customer's own backups provide. Account managers must make this clear at renewal.

**Key findings:**
1. **The control plane RPO is not met.** Nightly backups give a 24-hour RPO against the 1-hour target, and they have never been restore-tested, so the 4-hour RTO is unproven (gap 9; risk R-005 in P01).
2. **A DC-1 loss would strand about 70% of customer VMs.** Only replicated VMs can fail over to DC-2. DC-1 is in Florida and exposed to hurricanes (risk R-018).
3. **Break-glass access is missing.** If the workforce identity provider fails, nobody can reach the hypervisor managers except with the shared root credentials in the vault, which is itself a gap (gap 4).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-05 Private cloud platform | 96 hypervisor hosts in 4 clusters, 6 storage arrays; DC-2 replicas for the paid tier | BP-01 |
| SYS-06 Virtualization and out-of-band management | Hypervisor managers and host BMCs | BP-01, BP-02 |
| SYS-09 Edge network and DNS | Routers, firewalls, DDoS scrubbing, authoritative DNS (primary at DC-1, secondary at DC-2 and at the scrubbing service) | BP-01, BP-03 |
| SYS-01, SYS-02, SYS-04 Portal, control plane, and cloud tenant | Portal, API, orchestration, tenant database, nightly database backup | BP-02, BP-08 (metering) |
| SYS-03 Workforce identity provider | SSO with hardware security keys for all staff | All |
| SYS-08 RMM tool | Agents on about 1,900 customer servers | BP-04 |
| SYS-10 Ticketing, status page, productivity suite | Customer communication; the status page runs on a separate provider | BP-05, BP-09 |
| SYS-11 SIEM | Log collection and AI-assisted triage | BP-07 |
| SYS-07 Code hosting and CI/CD | Source, build runners, template signing key | BP-06 |
| Third parties | Two colocation providers, two carriers per site, DDoS scrubbing, public cloud provider, RMM vendor, SIEM vendor, payroll provider | As listed in `bia.csv` |
| People and facilities | NOC (can work remotely), platform engineers with DC-1 and DC-2 cage access | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-09 edge network and DNS (BP-03) | 1 h | Second carrier; secondary DNS at DC-2 and the scrubbing service |
| 2 | SYS-05 and SYS-06 hosting platform (BP-01) | 2 h | Fail replicated VMs to DC-2; spare hosts at DC-1 |
| 3 | SYS-10 status page and NOC phones (BP-05) | 2 h | Separately hosted status page; NOC cell phones |
| 4 | SYS-04, SYS-02, SYS-01 control plane and portal (BP-02) | 4 h | NOC performs urgent VM actions in the hypervisor managers |
| 5 | SYS-11 SIEM (BP-07) | 8 h | EDR console and cloud-native alerts to IT on-call |
| 6 | SYS-08 RMM tool (BP-04) | 24 h, after integrity validation | Customers' own remote access for urgent work |
| 7 | SYS-07 CI/CD (BP-06) | 48 h | Two-person build from a clean workstation |
| 8 | Payroll SaaS (BP-10) | 72 h | Repeat the prior payroll |
| 9 | Productivity and e-signature SaaS (BP-09) | 72 h | Email and phone |
| 10 | SYS-13 billing (BP-08) | 120 h | Invoice from prior-month usage |

**Identity comes first in practice.** SYS-03 is not a process, but every recovery step above needs administrator sign-in. Two break-glass accounts per critical system (identity provider, cloud tenant, hypervisor managers) are to be created and stored offline (POL-02 4.7; P07 POAM-001).
