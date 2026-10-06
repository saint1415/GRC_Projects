# Business Impact Analysis: Cris Santos Company | Information Technology | Mid-Market

**Organization:** Cris Santos Company, Inc. (cloud hosting and managed infrastructure provider) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** GRC Manager with the Director of Security, the process owners named in `bia.csv`, and the data center operations managers | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Technology Officer, 2026-09-22 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: managed private cloud, Government Cloud, managed services, backup and disaster recovery (DR) services, DNS and edge, the NOC and customer support, software engineering, security, and the corporate functions (sales, finance, HR, corporate IT). It rates 16 business processes and puts a dollar value on what an outage costs, using the service level agreement (SLA) credit tiers in the master services agreement (MSA) and the revenue of each service line.

The results feed:
- the contingency planning controls (CP-2, CP-4, CP-6, CP-7, CP-9, CP-10) in the FedRAMP Rev5 Class C control list (P02, P03);
- the availability rating in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the 4-hour threshold in the bank service provider notification rule (12 CFR 53.4(a); 225.303(a); 304.24(a)) and the bank notice steps in both runbooks (P08);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment (P09).

## 2. System and business description
The company hosts about 24,000 commercial VMs and about 2,100 Government Cloud VMs on 540 company-owned hypervisor hosts in 16 clusters across three colocation data centers: DC-1 (Florida, commercial only), DC-2 (Mid-Atlantic, commercial and government), and DC-3 (Southwest, commercial and government). Customers manage their services through the Hosting Control Plane and Customer Portal (HCP), which runs in a 10-account public cloud landing zone, with separate commercial and government partitions (P02, P04). The company also runs managed services for 410 customers through a remote monitoring and management (RMM) tool, managed backup for 620 customers, and authoritative DNS for hosted domains. See `../00_company-facts.md` sections 1 and 3.

Two facts shape the recovery values:
- **Data protection is shared.** The MSA makes commercial customers responsible for their own VM backups unless they buy the replication tier (about 35% of commercial VMs) or the backup service. Every Government Cloud VM is replicated between DC-2 and DC-3.
- **DC-1 concentrates risk.** DC-1 holds about 13,000 commercial VMs (54%) and sits in a hurricane-exposed region.

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual revenue, about $274,000 a day company-wide. Monthly fees are about $3.83 million for the commercial private cloud and about $1.17 million for the Government Cloud.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per outage) | More than $250,000 (credits, lost revenue, and recovery labor) | $50,000 to $250,000 | Less than $50,000 |
| Operations | Most customers of a service line cannot run or reach their workloads | One cluster, data center, or service function impaired | Staff slowed but customers unaffected |
| Regulatory and contractual | Bank notice duty triggered; FedRAMP reportable incident or a threat to the certification; MSA breach across many customers | Missed contractual notice or SLA for a few customers; late FedRAMP deliverable | Internal policy deviation |
| Safety | Not rated. The company does not operate safety systems; customers' safety impacts are in their own BIAs | | |
| Reputation | Trade press coverage, loss of bank or agency customers, or an agency questioning FedRAMP reuse | Complaints or churn of a few accounts | Internal only |

**How loss at MTD was estimated.** Estimated loss is the SLA credit the outage would trigger, plus lost usage revenue and extra labor, for an outage that lasts the full MTD. The MSA gives 10% of monthly fees below 99.95% monthly availability (about 22 minutes of outage), 25% below 99.0% (about 7.3 hours), and 50% below 95.0% (about 36.5 hours). For example, a 4-hour outage of all commercial hosting costs about 10% of $3.83 million plus 4 hours of revenue, about $404,000. Churn is not included in the per-process figures; it is estimated separately in the enterprise scenario below.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-05 Authoritative DNS and edge network | DNS and edge | High | 2 | 1 | 24 | $520,000 |
| 2 | BP-01 Commercial workload hosting | Managed private cloud | High | 4 | 2 | 0.25 | $404,000 |
| 3 | BP-02 Government Cloud workload hosting | Government Cloud | High | 4 | 2 | 0.25 | $124,000 |
| 4 | BP-06 24x7 NOC, status page, and customer support | NOC and customer support | High | 4 | 2 | 4 | $28,000 |
| 5 | BP-04 Control plane and portal (government partition) | Government Cloud | High | 8 | 4 | 1 | $28,000 |
| 6 | BP-03 Control plane and portal (commercial partition) | Managed private cloud | High | 8 | 4 | 1 | $62,000 |
| 7 | BP-10 Security monitoring and incident response | Security | Moderate | 24 | 8 | 1 | $12,000 |
| 8 | BP-08 Managed backup and customer restore | Backup and DR services | High | 12 | 6 | 1 | $46,000 |
| 9 | BP-15 Corporate IT, email, chat, and collaboration | Corporate IT | Moderate | 24 | 8 | 24 | $20,000 |
| 10 | BP-16 Physical data center operations | Platform engineering | Moderate | 24 | 8 | 24 | $10,000 |
| 11 | BP-07 Managed services delivery through the RMM tool | Managed services | Moderate | 72 | 24 | 24 | $96,000 |
| 12 | BP-09 Software and VM template delivery (CI/CD) | Software engineering | Moderate | 72 | 48 | 24 | $18,000 |
| 13 | BP-11 FedRAMP continuous monitoring and agency reporting | Government Cloud | Moderate | 168 | 72 | 24 | $6,000 |
| 14 | BP-12 Customer onboarding, orders, and contracts | Sales | Low | 120 | 72 | 24 | $40,000 |
| 15 | BP-14 Payroll and HR | Human resources | Low | 120 | 72 | 24 | $15,000 |
| 16 | BP-13 Billing, metering, and collections | Finance | Low | 240 | 120 | 24 | $20,000 |

**Summary:** 7 High, 6 Moderate, and 3 Low processes (16 in total). The sum of estimated losses at each process's MTD is $1,449,000.

**Enterprise-wide scenario: DC-1 lost for 5 days (hurricane).** About 4,550 replicated VMs fail over to DC-2 and DC-3 within the RTO; about 8,450 unreplicated VMs stay down until DC-1 returns or customers restore elsewhere. Customers with unreplicated DC-1 VMs fall below 95.0% for the month (50% credit, about $673,000); replicated customers fall below 99.95% (10% credit, about $72,000). Emergency labor, hardware, and freight add about $250,000. The immediate cost is about $1.0 million. If 5% of DC-1 customers leave, annual revenue falls by about $1.24 million. The Government Cloud is not hosted at DC-1, but its control plane and NOC staff are shared (P08 `ir-runbook-dc1-site-loss.md`).

**What drives the values:**
- **Contracts drive the hosting rows.** The 10% credit tier starts after about 22 minutes of monthly outage, so the cost of BP-01, BP-02, and BP-05 is mostly credits, not lost usage. The 25% tier at about 7.3 hours sets a hard ceiling above the 4-hour MTD.
- **The bank rule sits inside the same window.** A computer-security incident that materially disrupts or degrades covered services for 4 or more hours requires notice to each affected bank (12 CFR 53.4(a)). The 4-hour MTD for hosting and the 2-hour MTD for DNS keep the company below that line when recovery works.
- **The control planes can be down longer than hosting.** Running VMs keep running without them. After a business day, customers cannot recover their own workloads and support volume overwhelms the NOC.
- **The RMM tool and CI/CD are deliberately low on the list.** After a compromise they must be validated before they are trusted again (P08). A fast restore of a compromised tool would spread harm.
- **FedRAMP reporting is about cadence, not hours.** Missing a monthly deliverable by a few days is a deficiency; missing several threatens the certification. The 1-hour FedRAMP incident report clock depends on BP-10, not BP-11.

## 5. Key findings
1. **The commercial control plane does not meet its RTO.** Its only restore test (2025) took 9 hours against a 4-hour RTO. The government partition met its 4-hour RTO in its 2026-06 quarterly test. The difference is practice: the government runbook is rehearsed quarterly, the commercial one is not (gap 8; P01 R-005).
2. **DC-1 is the largest single loss.** It holds 54% of commercial VMs, and 65% of those have no replica. A 5-day loss costs about $1.0 million immediately and risks churn (P01 R-018; P08 `ir-runbook-dc1-site-loss.md`).
3. **DNS is the highest-cost minute.** A 2-hour DNS or edge outage costs more than a 4-hour hosting outage because it hits every customer at once (P01 R-012).
4. **Bank customers raise the stakes on both hosting and backup.** 38 banks use hosting, managed services, or backup. A failure of the backup service during a bank's own incident would delay that bank's recovery (BP-08).
5. **Recovery depends on identity.** Every recovery step needs administrator sign-in through the identity provider and PAM. Break-glass accounts exist for the government partition but are not documented for the commercial hypervisor managers at DC-1 (POL-02; P07).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-05 Private cloud platform | 540 hypervisor hosts in 16 clusters, 28 storage arrays; replication between data centers for the paid tier and for all government VMs | BP-01, BP-02 |
| SYS-06 Virtualization, out-of-band management, and PAM | Hypervisor managers, host BMCs, management networks, PAM with session recording | BP-01 to BP-04, BP-16 |
| SYS-09 Edge network and DNS | Routers, firewalls, authoritative DNS (primary in each data center; secondary at the scrubbing service), DDoS scrubbing | BP-01, BP-02, BP-05 |
| SYS-01, SYS-02, SYS-04 Portal, control plane, and landing zone | Two partitions; tenant databases with point-in-time recovery; immutable backups in the backup account and a second region | BP-03, BP-04, BP-13 (metering) |
| SYS-03 Workforce identity provider | SSO with hardware security keys; break-glass accounts | All |
| SYS-07 Code hosting and CI/CD | Source, build runners, HSM-backed signing key (government), pipeline-secret signing key (commercial) | BP-09 |
| SYS-08 RMM tool | Agents on about 11,200 customer servers | BP-07 |
| SYS-10 Managed backup platform | Backup software and immutable storage at DC-2 and DC-3, replica catalogs at each site | BP-08 |
| SYS-11 Security operations stack | SIEM with AI triage, EDR, scanners, MDR partner | BP-10 |
| SYS-12 IT service management and status page | Ticketing, change, CMDB; the status page on a separate provider | BP-06, BP-11, BP-16 |
| SYS-13 Corporate IT | Productivity suite, endpoints, payroll, HR, billing | BP-12 to BP-15 |
| SYS-14 FedRAMP package repository | Legacy secure repository for agency deliverables | BP-11 |
| Third parties | Three colocation providers, two carriers per site, DDoS scrubbing service, public cloud provider, RMM vendor, SIEM vendor, MDR partner, code hosting vendor, backup software vendor, payroll provider | As listed in `bia.csv` |
| People and facilities | NOC in Florida and the DC-2 metro office; platform engineers with cage access at each site; U.S.-person engineers with government cluster access | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-03 identity provider, PAM, and break-glass accounts | 1 h | Two break-glass accounts per critical system, sealed offline |
| 2 | SYS-09 edge network and DNS (BP-05) | 1 h | Second carrier; secondary DNS at the scrubbing service and another data center |
| 3 | SYS-05 and SYS-06 commercial and government hosting (BP-01, BP-02) | 2 h | Fail replicated VMs to the other data centers; spare hosts at each site |
| 4 | SYS-12 status page, NOC phones, and ticketing (BP-06) | 2 h | Separately hosted status page; secondary NOC desk; NOC mobile phones |
| 5 | SYS-01, SYS-02, SYS-04 government partition control plane (BP-04) | 4 h | NOC performs urgent VM actions through PAM |
| 6 | SYS-01, SYS-02, SYS-04 commercial partition control plane (BP-03) | 4 h target (9 h demonstrated) | NOC performs urgent VM actions in hypervisor managers |
| 7 | SYS-11 SIEM and MDR feeds (BP-10) | 8 h | EDR console and cloud-native alerts to the on-call SOC analyst |
| 8 | SYS-10 backup platform and restore queue (BP-08) | 6 h | Restore from the other site's replica catalog |
| 9 | SYS-13 corporate IT and communications (BP-15) | 8 h | Out-of-band messaging group; printed call trees |
| 10 | Colocation remote hands and spares (BP-16) | 8 h | Spares at each site; hardware maintenance vendor |
| 11 | SYS-08 RMM tool (BP-07) | 24 h, after integrity validation | Customers' own remote access for urgent work |
| 12 | SYS-07 CI/CD (BP-09) | 48 h | Two-person build from a clean workstation |
| 13 | SYS-14 FedRAMP deliverables (BP-11) | 72 h | Manual exports from scanners and the CMDB |
| 14 | CRM and e-signature (BP-12) | 72 h | Emailed order forms |
| 15 | Payroll SaaS (BP-14) | 72 h | Repeat the prior payroll |
| 16 | Billing SaaS (BP-13) | 120 h | Invoice from the prior month's usage |
