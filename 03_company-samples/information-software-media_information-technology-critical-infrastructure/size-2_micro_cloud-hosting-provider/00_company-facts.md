# Scenario facts: Cris Santos Company | Information Technology | Micro

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given and was checked against the primary source (eCFR point-in-time 2026-09-23, the U.S. Code on govinfo.gov, and the Florida Statutes as published by the Florida Legislature).

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (managed cloud hosting provider) |
| Business | Managed cloud hosting and managed infrastructure (NAICS 518210). Two service lines: (1) **managed private cloud hosting**: customer virtual machines (VMs) on a company-owned hypervisor cluster in two leased racks at one Florida colocation facility (DC-1); (2) **managed server services**: patching, monitoring, and backup checks for customer servers, done remotely through a SaaS remote monitoring and management (RMM) tool. Managed DNS (resold from a SaaS DNS provider) and VM backup are sold as add-ons |
| Location | Florida. One small office suite (no customer data or servers on site) and two racks at DC-1, about 30 miles from the office. There is no second data center |
| Workforce | 7 employees: Owner and Managing Member, Operations Manager, Lead Systems Engineer, 2 Systems Engineers, 2 Support Engineers |
| Customers | About 70 business customers, mostly in Florida: professional services firms, small manufacturers, local retailers and e-commerce sites, and **2 community banks**. About 260 customer VMs; about 145 of them (56%) on the backup add-on. 22 managed services customers with about 310 servers reached through the RMM tool. About 180 customer portal user accounts, 72 of them customer administrators |
| Bank customers | **Bank A**, a national bank (OCC-supervised): 6 hosted VMs (loan document imaging and a file server, both holding bank customer information) plus RMM patching of 8 branch servers. **Bank B**, a state-chartered nonmember bank (FDIC-supervised): RMM patching and backup monitoring of 9 servers in its own office. Both vendor contracts treat these as services subject to the Bank Service Company Act, so the company is a **bank service provider** (12 CFR 53.2(b)(2) and (5); 12 CFR 304.22(b)(2) and (5)). Both contracts also require the company to "implement appropriate measures designed to meet the objectives" of the Interagency Guidelines Establishing Information Security Standards (12 CFR Part 30, App. B; 12 CFR Part 364, App. B, III.D.2) and to notify the bank of unauthorized access to its customer information within 24 hours (EV-022). Applicability is decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-IT-R05, CON-BANK) |
| Revenue | About $1.1 million a year (fictional): hosting about $650,000, managed services about $380,000, DNS and other about $70,000. SBA-small (standard $40.0 million for NAICS 518210, 13 CFR 121.201) |
| Service commitments | Master services agreement (MSA): 99.9% monthly availability for hosting, with service credits of 10% below 99.9% and 25% below 99.0%; security incident notice to affected customers "without undue delay and within 72 hours of confirmation". The MSA makes customers responsible for backing up their own VMs unless they buy the backup add-on |
| Federal status | **No federal customer.** In April 2026 a regional federal office asked, through a reseller, whether the company could host a small application. The Owner declined because the service has no FedRAMP authorization and the cost is out of reach at this size (EV-034). FedRAMP does not apply: decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-IT-R01) and recorded in P03 row G-001 |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): PHI (the MSA prohibits it; the company signs no business associate agreements). DoD CUI and covered defense information (the MSA prohibits them; no DFARS or CMMC clauses). Payment cards (customers pay through the processor's hosted page). DOJ Data Security Program, 28 CFR Part 202 (no data brokerage, vendor, employment, or investment agreement gives a country of concern or covered person access to customer data; all staff and vendors' support teams used are U.S.-based) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Owner and Managing Member | Accepts Moderate, High, and Very High risks with a dated treatment plan; approves policies and spending; signs bank and customer contracts. Former lead engineer who still holds standing administrator accounts (EV-002; EV-004; EV-010) |
| Operations Manager | **Compliance Coordinator**: policies, vendor contracts, bank contact lists, customer notices, training records, cyber insurance. Also billing, payroll, and HR (onboarding and terminations) |
| Lead Systems Engineer | Designated **Information Security Lead** in writing on 2026-06-15 (about 20% of the role) (EV-030): owns the hypervisor cluster, storage, network, VPN, identity provider, and the MDR relationship; runs the security program day to day |
| Systems Engineers (2) | Cluster, backup, and cloud tenant administration; managed services engineering; RMM script authors |
| Support Engineers (2) | Support desk, customer portal administration, routine RMM patching; first responders for customer reports |
| Managed detection and response (MDR) provider | Outside service, contracted since 2025-11: 24x7 monitoring of the company's laptops (EDR agent), identity provider, and firewalls, with AI-assisted alert triage in its platform (P10). It is the company's "MSP" in the tier sense: the outside party that runs a technical control the company cannot staff |
| Colocation provider (DC-1) | Building security, power, cooling, and remote hands. SOC 2 Type 2 report (P09) |
| Independent assessor | IT security consultant engaged for the P07 control assessment; not involved in operating any control or in P01 or P03 |
| Outside counsel and cyber insurer | Contract and breach advice; the insurer's 24x7 breach hotline and panel vendors |

**Where roles overlap, and how that is compensated.** The Lead Systems Engineer both runs the systems and judges their security. The Operations Manager both processes terminations and checks that access was removed. Compensating checks: the MDR provider watches activity the engineers cannot hide from; an independent consultant tests controls each year (P07); the Owner reviews the monthly security report; and two-person approval is being added for the riskiest actions (multi-customer RMM scripts, backup deletion).

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds customer data? | Notes |
|---|---|---|---|---|
| SYS-01 | Customer portal and billing | Commercial hosting automation and billing software (licensed), on one VM in SYS-04 | Yes (customer contacts, portal credentials, invoices) | Customers order, start, stop, and reboot VMs, open the VM console, open tickets, and pay invoices. MFA is optional for customers: 15 of 72 customer administrator accounts (21%) use it (EV-011) |
| SYS-02 | Cluster management: hypervisor manager and host baseboard management controllers (BMCs) | Company-owned, management network at DC-1 | Yes (full control of every customer VM) | One shared local administrator account used by all engineers; BMCs use shared local passwords. SYS-01 calls the hypervisor manager API with a service account that has full administrator rights; its password sits in a configuration file on the portal VM (EV-005; EV-013; EV-047) |
| SYS-03 | Private cloud hosting platform | 6 hypervisor hosts in one cluster, 1 dual-controller storage array, 2 switches, 2 firewalls (high-availability pair), and 1 backup appliance, in 2 racks at DC-1 | Yes (customer VMs) | About 260 VMs. The colocation provider supplies blended internet bandwidth with basic DDoS filtering (EV-007; EV-021; EV-025) |
| SYS-04 | Public cloud tenant (IaaS) | Public cloud provider (vendor-agnostic) | Yes | The single cloud workload: the SYS-01 VM and its managed database, plus object storage holding the off-site copy of SYS-05 backups. One account; backups are in the same account as the portal and are not immutable (EV-010) |
| SYS-05 | Backup service | Backup software on the backup appliance at DC-1, copying nightly to SYS-04 object storage | Yes | Nightly backups of the 145 add-on VMs (14 days kept locally, 30 days in the cloud copy); nightly configuration backup of the hypervisor manager; nightly SYS-01 database dump (EV-009) |
| SYS-06 | RMM tool | SaaS (RMM vendor) | Yes (agent access to customer servers) | Agents on about 310 servers of 22 customers, including both banks. 3 named technician accounts and 2 shared "support" accounts whose one-time-code seed is stored in the team password vault. Any technician can run a script on all customers' servers at once. The vendor keeps audit logs 30 days (EV-004; EV-013) |
| SYS-07 | Workforce identity provider and productivity suite | SaaS | Incidental | Single sign-on with push-approval MFA for the suite, ticketing, the MDR console, and the firewall VPN. The RMM tool, hypervisor manager, and cloud tenant use their own local sign-in (EV-002) |
| SYS-08 | Managed DNS | SaaS DNS provider (resold) | Yes (customer DNS zones) | About 190 customer zones under one company account with MFA. No zone export is kept outside the provider (EV-014) |
| SYS-09 | Ticketing and documentation (professional services automation, PSA) | SaaS | Yes (customer server passwords in its documentation vault) | Readable by all 7 staff (EV-012) |
| SYS-10 | Endpoints | Company-managed | Cached | 9 laptops (7 in use, 2 spares) with full-disk encryption and the MDR's EDR agent (EV-015) |
| SYS-11 | MDR platform with AI alert triage | SaaS (MDR provider) | Logs | Collects EDR, identity provider, and firewall logs. **Not** hypervisor manager, BMC, RMM, cloud tenant, or DNS logs. The AI triage scores and auto-closes low-risk alerts (about 91% of about 2,140 alerts in July 2026) and can isolate a laptop or suspend an identity provider account on its own (P10). On 2026-06-27 it suspended the on-call Systems Engineer's account during a host failure, locking him out of the VPN for about 50 minutes (EV-015; EV-017; EV-018; EV-051) |

**SSP system (P02):** the *Hosting Control Plane and Customer Portal (HCP)*: the customer portal (SYS-01), cluster and out-of-band management (SYS-02), the management interfaces of the hosting platform (SYS-03), the cloud tenant (SYS-04), the backup service (SYS-05), the RMM tool (SYS-06), the identity provider (SYS-07), DNS administration (SYS-08), the PSA vault (SYS-09), and the administrator laptops (SYS-10), monitored through the MDR service (SYS-11).

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). For a 7-person hosting provider the systems of record are the admin consoles of the tools it runs (identity provider, RMM tool, hypervisor manager, firewalls, storage array, backup software, cloud tenant, PSA, DNS account, password vault, MDR console), the payroll service, the portal's billing module and the card statements, the contracts folder, the hardware spreadsheet, the ticket history, and the Owner's and Operations Manager's inboxes. Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the bank contract measures, the bank notice rule, and Fla. Stat. 501.171** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 system | Registry default kept: the Hosting Control Plane and Customer Portal. At this size the "control plane" is commercial portal software plus the cluster manager and RMM tool, not company-built code |
| P03 regulation | The registry default (FedRAMP) **does not apply**: there is no federal customer (44 U.S.C. 3607-3616 reach cloud services used by agencies). P03 records that finding and analyzes the rules that bind today because of the bank customers: (A) the bank service provider notification rule (12 CFR 53.4; 12 CFR 304.24; parallel 12 CFR 225.303); (B) the Interagency Guidelines Establishing Information Security Standards, which both bank contracts flow down (12 CFR Part 30, App. B and Supplement A; 12 CFR Part 364, App. B, III.D.2) and which bank examiners can apply to the company's services under 12 U.S.C. 1867(c); and (C) Fla. Stat. 501.171(2), (6), and (8) for a third-party agent |
| P08 incident | Registry default kept: compromise of provider tooling affecting downstream customers. An attacker signs in to the RMM tool with a shared support account and pushes a malicious script to managed customer servers, including Bank A's. The MDR provider, the cyber insurer, and the banks are in the notification chain |
| P09 SOC 2 | Security plus Availability. Readiness self-assessment used to answer both banks' 2026 vendor due diligence questionnaires (due 2026-10-30) and to decide on a SOC 2 Type 1 examination in 2027. Also a review of the colocation provider's SOC 2 Type 2 report |
| P10 AI | Registry default adapted: the company does not run its own security operations. The AI-driven alert triage runs inside the MDR provider's platform, configured by the provider for the company. Assessed as a third-party AI service the company relies on |
| Cloud | Hosting runs on company-owned hardware in a colocation facility. The single cloud workload is the IaaS tenant (SYS-04). Everything else is SaaS. Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-27 | MDR AI triage automatically suspends the on-call Systems Engineer's account during a host failure (P10) |
| 2026-07-06 to 2026-07-17 | Intake: evidence requests, exports from the admin consoles, the payroll service and the billing module, the contracts folder, inventories, obligations register |
| 2026-07-20 to 2026-07-31 | BIA, risk assessment, and gap analysis (Lead Systems Engineer and Operations Manager) |
| 2026-07-28 | Independent consultant engaged for the P07 assessment |
| 2026-08-03 to 2026-08-14 | Policies drafted from the gaps |
| 2026-08-17 to 2026-08-19 | Control assessment by the independent consultant (DC-1 walkthrough 2026-08-18): operating tests of controls already in place; design review of the draft policies |
| 2026-08-24 to 2026-08-28 | SOC 2 readiness self-assessment, colocation report review, and AI risk assessment |
| 2026-09-15 | Deliverables and policies approved by the Owner |
| 2026-10-01 | POL-02, POL-03, and POL-04 take effect |
| 2026-10-15 | Shared RMM support accounts removed (POAM-001 first milestone; R-001 tolerance limit in the SSP) |
| 2026-10-28 | First incident response tabletop with the MDR provider and a bank scenario (POAM-011) |
| 2026-10-30 | Both banks' 2026 vendor due diligence questionnaires due (answered with P09, P07, and the SSP) |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |
