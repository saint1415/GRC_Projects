# System Security Plan: Hosting Control Plane and Customer Portal (HCP)

**Organization:** Cris Santos Company, Inc. (cloud hosting and managed infrastructure provider) | **Tier:** Mid-Market | **Vertical:** Information Technology
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 2.0, 2026-09-22
**Control baseline:** FedRAMP Rev5 Class C control list (FedRAMP Consolidated Rules for 2026, rule FRC-CSF-BSL), applied to both partitions. The government partition holds a FedRAMP Rev5 Moderate certification (legacy agency path) since 2024-05-20. P03 analyzes the transition to the 2026 rules.

## 1. System Name and Identifier
Hosting Control Plane and Customer Portal (**HCP**), identifier CSC-HCP-01. The government partition is the cloud service offering listed on the FedRAMP Marketplace as the company's **Government Cloud**. The commercial partition is the same platform for commercial customers and is documented here so that one set of controls covers both.

## 2. System Overview
The HCP is the set of systems that lets the company sell, run, and manage its five service lines: managed private cloud, Government Cloud, managed services, backup and disaster recovery (DR), and authoritative DNS and edge services. Customers use it to order, start, stop, snapshot, and console into their virtual machines (VMs), manage DNS zones, request restores, and open tickets. Company engineers use its management layer to run 16 hypervisor clusters in three colocation data centers (DC-1 Florida, DC-2 Mid-Atlantic, DC-3 Southwest).

**Users:**
- About 19,000 customer user accounts (about 3,400 customer administrators) from about 2,300 business customers, including 7 federal civilian agencies, 19 defense contractors, and 38 community and regional banks.
- About 4,000 agency and defense users of the government partition, who sign in with federal credentials or their organization's identity provider through federation.
- 600 employees and about 40 U.S.-based contractors. **214 engineers hold privileged roles** (86 platform, 58 managed services, 34 site reliability, 22 software engineers with production deploy rights, 14 security). NOC staff hold limited operator rights.

**Major components** (IDs from `../00_company-facts.md` section 3):
| ID | Component | Hosting and service model | Partition |
|---|---|---|---|
| SYS-01 | Customer portal and public API (company-built) | Containers in SYS-04 | Commercial and government deployments |
| SYS-02 | Control plane orchestration services: provisioning engine, job queue, tenant database, metering | Containers and managed databases in SYS-04 | Separate deployments in separate cloud accounts |
| SYS-03 | Workforce identity provider (SSO, hardware security keys) | SaaS; the vendor holds its own FedRAMP certification | Shared |
| SYS-04 | Public cloud landing zone, 10 accounts | IaaS/PaaS, vendor-agnostic; the government account uses regions covered by the provider's own FedRAMP certification | Separate production accounts per partition |
| SYS-05 (in part) | The 3 government clusters (96 hosts) at DC-2 and DC-3, and the management interfaces of all 16 clusters | Company-owned hardware in colocation | Government clusters; commercial management interfaces |
| SYS-06 | Hypervisor managers, host BMCs, management networks, privileged access management (PAM) | Company-operated in all three data centers | Per cluster |
| SYS-07 | Source code repository (SaaS) and CI/CD pipeline with build runners in SYS-04; HSM-backed signing for government templates | SaaS plus IaaS | Shared pipeline, separate deployment repositories |
| SYS-09 (in part) | Management interfaces of routers, firewalls, and authoritative DNS | Company-operated; DDoS scrubbing contracted | Shared |
| SYS-11 (in part) | SIEM tenant with AI-assisted alert triage, EDR, scanners, MDR partner feeds | SaaS; the SIEM vendor holds its own FedRAMP certification | Separate indexes per partition |

The RMM tool (SYS-08), the backup platform (SYS-10), IT service management (SYS-12), and corporate IT (SYS-13) connect to the HCP and are described in section 8. **Boundary change for 2027:** the CI/CD pipeline, identity provider tenant, SIEM tenant, and IT service management were treated as external services in the 2024 package. Under the 2026 Minimum Assessment Scope rules they are information resources that can affect federal customer data, so this plan brings SYS-03, SYS-07, and SYS-11 inside the boundary and lists SYS-12 as a third-party information resource (P03 MAS rows; P01 R-035).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the HCP |
|---|---|---|---|
| C-IT-R01 | FedRAMP | 44 U.S.C. 3607-3616; FedRAMP Consolidated Rules for 2026 | **Applies to the government partition.** Rev5 Moderate certification since 2024-05-20. The 2026 rules must be followed for each ruleset by its "maintaining" date (for example VDR and VER from 2026-12-07; most others from 2027-01-01) and in full by 2028-02-01 or the certification is lost (P03). The Rev5 Class C control list is the baseline for both partitions |
| C-IT-R03 | DFARS Safeguarding CDI and Cyber Incident Reporting | 48 CFR 252.204-7012(b)(2)(ii)(D) | **Applies by contract flow-down.** 19 defense contractors store covered defense information in the Government Cloud and require FedRAMP Moderate equivalent security plus paragraphs (c) to (g): report within 72 hours of discovery, submit malicious software, preserve images and monitoring data for at least 90 days, give DoD forensic access, and support damage assessment (P08) |
| C-IT-R02 | CMMC Program | 32 CFR Part 170 | **Applies to the defense customers, not to the company.** Those customers may use a cloud offering that is FedRAMP Authorized at Moderate or higher, or equivalent, for Level 2 (32 CFR 170.16(c)(2)), and must document the customer responsibility matrix in their own SSPs. The company provides that matrix with the package |
| C-IT-R05 | Bank service provider notification rule | 12 CFR 53.4 (OCC); 12 CFR 225.303 (FRB); 12 CFR 304.24 (FDIC) | **Applies.** Notice to each affected bank's designated contact as soon as possible after determining a computer-security incident has materially disrupted or degraded covered services, or is reasonably likely to, for 4 or more hours (P05, P08) |
| C-IT-R04 | DOJ Data Security Program | 28 CFR Part 202 | **Not triggered today.** No vendor, employment, or investment agreement gives a country of concern or covered person access to customer data, and all staff and contractors are U.S.-based. Government-related data has no volume threshold, so the GRC Manager rechecks at every new vendor with access to the government partition (P03) |
| C-IT-R06 | CIRCIA (pending rule) | 6 U.S.C. 681b; proposed 6 CFR Part 226 | Not in force. No final rule as of 2026-09-25. Tracked only |
| Contract | GSA Multiple Award Schedule | FAR 52.204-21, 52.204-23, 52.204-25, 52.204-30 | Basic safeguarding of federal contract information and reporting of covered telecommunications, Kaspersky, and FASCSA-covered articles (P03, P08) |
| State | Florida Information Protection Act and other state breach laws | Fla. Stat. 501.171(6) as the worked example | As a third-party agent, notify the customer within 10 days of determining a breach of personal information it maintains for that customer. Other states' laws apply where affected individuals reside |
| Contract | Master services agreement (MSA), agency terms, bank addendum | MSA | 99.95% availability; confidentiality; incident notice within 72 hours of confirmation |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-10 | P06 | Approved 2026-09-22, effective 2026-10-01 |

**Not applicable:** HIPAA (the MSA prohibits PHI and the company signs no business associate agreements); PCI DSS (billing uses the payment processor's hosted page, outside the HCP).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Technology Officer (system owner) on 2026-09-22, after the control assessment (P07), and presented to the board audit committee the same day.

### 4.2 System Authorization Decision
- **Federal authorization (government partition).** The sponsoring civilian agency issued an ATO on 2024-05-20, and 6 more agencies issued ATOs that reuse the package. Annual FedRAMP independent assessment: March 2026, by a FedRAMP Recognized independent assessment service. Under the 2026 rules the company must keep the certification by meeting each ruleset's deadlines (P03 roadmap).
- **Internal decision (whole HCP).** The CTO accepted continued operation of both partitions on 2026-09-22, with the conditions in the P07 POA&M. The CEO accepted the High and Very High risks in P01 on the same date, each with a dated treatment plan.
- **Conditions:** the High POA&M items must meet their milestones; the audit committee receives POA&M status each quarter; any change that would be a significant change under the FedRAMP Significant Change Notification rules goes through the change advisory board with the Federal Program Director.

### 4.3 System Operational Status
**Operational.** Major modifications planned:
- Federate DC-1 clusters A and B through PAM and retire their local accounts and legacy VPN path (P01 R-003), due 2026-12-31 to 2027-01-31
- Move the commercial VM template signing key into the HSM and verify signatures at deployment (R-011), due 2026-12-31
- Onboard DC-1 clusters A and B and the RMM tool to the SIEM (R-015), due 2027-01-31
- Machine-readable certification package, trust center, and Ongoing Certification Reports (R-023), due 2027-04-02 to 2027-08-01

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Technology Officer | Accountable for the HCP; accepts Moderate risk; approves this plan |
| Risk acceptor for High risk (authorizing official equivalent) | Chief Executive Officer | Accepts High risk; approves the risk appetite; signs agency, bank, and GSA contracts |
| Oversight | Board audit committee | Quarterly cyber risk and FedRAMP status |
| Senior security official | Director of Security | Security program owner; receives FedRAMP Security Inbox messages; owns POL-01 |
| Security plan and package | GRC Manager (3 GRC analysts) | This plan, the FedRAMP package, continuous monitoring, POA&M |
| Federal incident response coordinator | Security Operations Manager | Incident command and FedRAMP incident reports (P08) |
| Technical owner: portal, control plane, CI/CD | VP Software Engineering | SYS-01, SYS-02, SYS-07 |
| Technical owner: cloud landing zone | Director of Cloud Operations | SYS-04 and identity federation |
| Technical owner: hypervisors, BMCs, networks | VP Platform Engineering | SYS-05, SYS-06, SYS-09 |
| Government Cloud business owner | Federal Program Director | Agency relationships, significant change notices to agencies, Marketplace listing |
| Independent assessment | Co-sourced internal audit firm; FedRAMP Recognized independent assessment service | P07 assessment; annual FedRAMP assessment |
| Monitoring | MDR partner | 24x7 tier-1 triage |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 and adjusted for a hosting provider. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Hosted customer data, including federal data and CUI in the government partition | Moderate | Moderate | Moderate | Agencies and defense customers place Moderate workloads in the Government Cloud; the MSA prohibits PHI and payment card data. Loss would have a serious adverse effect on customers |
| IT infrastructure management (tenant inventory, service credentials, VM templates, hypervisor and BMC configuration) | Moderate | Moderate | Moderate | Service credentials and templates can affect every customer in a partition at once. That aggregation is rated Very High impact in P01, but no single information type reaches the FIPS 199 High definition for an agency |
| Information security (audit logs, SIEM alerts, vulnerability data) | Moderate | Moderate | Low | Needed for investigations and FedRAMP reports; a SIEM outage of up to 24 hours is tolerable with EDR still active (P05 BP-10) |
| Customer account, billing, and contact data | Moderate | Low | Low | Personal contact data of customer staff; billing can catch up (P05 BP-13) |
| **HCP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Availability was considered for High.** The BIA gives hosting and DNS 2- to 4-hour MTDs, and 38 banks depend on the platform. The team kept availability at Moderate because agencies run their own continuity plans, government VMs are replicated between DC-2 and DC-3, and no agency has designated the service as supporting a High-impact system. A move to High would need FedRAMP High controls and is not planned.

## 7. Authorization Boundary Description
**Inside the boundary:**
- both deployments of SYS-01 and SYS-02, in the commercial and government production accounts;
- all 10 accounts of the cloud landing zone (SYS-04), including the CI/CD build, log archive, security tooling, and backup accounts;
- the identity provider tenant (SYS-03) and its federation to the cloud, code hosting, PAM, and hypervisor managers;
- the code repository and pipeline (SYS-07) and the HSM that signs government templates;
- the 3 government clusters, and the hypervisor managers, BMCs, management networks, and PAM (SYS-06) for all 16 clusters;
- the management interfaces of the edge routers, firewalls, and authoritative DNS (SYS-09);
- the SIEM tenant and its use cases (SYS-11).

**Outside the boundary (external services and third-party information resources):**
- the 13 commercial clusters' customer workloads (customer-managed guests);
- the public cloud provider's infrastructure, the identity, SIEM, code hosting, and productivity suite vendors' platforms (each with its own FedRAMP certification or SOC 2 report);
- the colocation providers' facilities (DC-1, DC-2, DC-3);
- the RMM tool (SYS-08), which is barred from government tenants;
- the backup platform (SYS-10), which serves commercial customers only;
- IT service management (SYS-12), recorded as a third-party information resource because tickets and change records describe the government partition;
- the MDR partner, the DDoS scrubbing service, and the upstream carriers.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Agency identity providers (federal PIV federation) | Inbound assertions | Agency user identities | Agency ATO terms; interconnection documented (CA-3) |
| Defense customers' identity providers | Inbound assertions | Customer user identities | Customer contracts with DFARS 252.204-7012 flow-down |
| Agencies (FedRAMP deliverables and incident reports) | Outbound | Package, monthly continuous monitoring data, incident reports | Agency ATOs; legacy secure repository (SYS-14) until the trust center exists |
| RMM tool (SYS-08) | Bidirectional with the identity provider and the SIEM (planned) | Engineer sign-in, audit logs | RMM vendor contract (**no incident notice terms: gap**, P09) |
| Backup platform (SYS-10) | Inbound job status | Commercial restore requests through the portal | Internal; commercial only |
| IT service management (SYS-12) | Bidirectional | Tickets, changes, CMDB, status posts | SaaS contract with SOC 2 Type 2 |
| MDR partner | Inbound logs, outbound case updates | Security alerts, case data | MDR contract; SOC 2 Type 2 |
| DDoS scrubbing service | Inbound clean traffic; secondary DNS | DNS zones, traffic | Contract; SOC 2 Type 2 |
| Upstream carriers (2 per site) | Bidirectional | Internet traffic | Carrier contracts with priority-of-service terms |
| Colocation providers | Inbound access logs | Cage access records | Colocation contracts; SOC 2 Type 2 |
| Bank customers | Outbound notices | Incident notices | Bank addendum (12 CFR 53.4 notice to designated contacts) |

## 9. System Component Inventory
The CMDB holds the full inventory (CM-8). Summary by component class:

| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Portal and API containers, commercial and government | Managed containers | HCP commercial and government production accounts | VP Software Engineering |
| Control plane services and tenant databases | Managed containers; managed relational databases with point-in-time recovery | HCP production accounts | VP Software Engineering |
| Organization management, identity and shared services, network hub | Cloud organization, federation, network services | Organization, identity, and network hub accounts | Director of Cloud Operations |
| Log archive (write-once) and security tooling | Object storage with retention lock; posture service | Log archive and security tooling accounts | Security Operations Manager |
| Control plane backups | Backup vault with write-once retention, second region | Backup account | Director of Backup and DR Services |
| Build runners and HSM | Ephemeral runners; cloud HSM | CI/CD build account | VP Software Engineering |
| Non-production | Test deployments with synthetic data | Non-production account | VP Software Engineering |
| Identity provider tenant | SaaS | Identity vendor | Director of Cloud Operations |
| Code repository | SaaS | Code hosting vendor | VP Software Engineering |
| SIEM tenant with AI triage | SaaS | SIEM vendor | Security Operations Manager |
| Government clusters (3 clusters, 96 hosts, storage arrays) | Hypervisor hosts and storage | DC-2 (2 clusters, 64 hosts), DC-3 (1 cluster, 32 hosts) | VP Platform Engineering |
| Hypervisor managers and BMCs for 16 clusters (540 hosts) | Management software and firmware | DC-1, DC-2, DC-3 | VP Platform Engineering |
| PAM bastions and session recording | SaaS-managed software on company hosts | DC-2, DC-3 (DC-1 partial) | Security Engineering Lead |
| Edge routers, firewalls, authoritative DNS servers | Network | DC-1, DC-2, DC-3 | VP Platform Engineering |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The HCP uses the FedRAMP Rev5 Class C control list (rule FRC-CSF-BSL): **180 base controls** and **142 Class C enhancements**. `control-implementation.csv` has one row per base control, with the Class C enhancements listed in each statement and covered by it. 176 of the 180 base controls are in the NIST SP 800-53B Moderate baseline; 4 are FedRAMP additions (CA-8, IR-9, SC-45, SI-6).
- **One baseline, two partitions.** Every statement says where the government partition and the commercial partition differ. The gaps are mostly in the commercial partition and DC-1 (gap 1, "two-speed security").
- **Organization-defined parameters** are those of the 2024 FedRAMP package. They must be re-assigned under the 2026 rules (FRC-CSF-ACP) and recorded in the Security Decision Record (PL-11; P03).
- **Not applicable (3):** AC-18 (no wireless inside the boundary), PE-5 (no output devices in the cages), SC-15 (no collaborative computing devices). Each has a written justification.
- **Mapping to CSF 2.0:** 134 rows use NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`); the other 46 rows use an author mapping because NIST gives no CSF reference for those controls.

**Status of the 180 documented controls:**
| Status | Count |
|---|---|
| Implemented | 121 |
| Partially implemented | 55 |
| Planned | 1 (SR-10) |
| Not applicable | 3 |

**Inheritance of the 180 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 129 | Company |
| Hybrid | 35 | Public cloud provider (16), SIEM vendor (8), colocation providers (8), identity provider vendor (5), MDR partner, DDoS scrubbing service |
| Common/Inherited | 16 | Colocation providers (11 physical and environmental controls), SIEM vendor (AU-4, AU-7), public cloud provider (SC-39, SI-16), productivity suite vendor (SI-8) |

Inherited controls are evidenced by each provider's FedRAMP package or SOC 2 Type 2 report, reviewed each year (P09 `vendor-soc2-review.csv`).

**Where the 55 Partially implemented controls cluster:** contingency planning (5 of 9 CP controls), incident response (5 of 9 IR), supply chain (5 of 9 SR), and access, audit, and identification in the commercial partition. They trace to the 15 known gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
- **Co-sourced internal audit firm:** assessed 40 controls (the 34 base controls in the Rev5 Class C annual independent assessment list, IVV-CSF-AIA, plus 6 enhancements tied to top risks) and 185 determination statements from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, `poam.csv`).
- **FedRAMP Recognized independent assessment service:** annual assessment of the government partition, March 2026. Its findings are in the legacy FedRAMP POA&M (41 open items at 2026-07-31, 3 past their scheduled date).
- Weaknesses from both are reported to the audit committee each quarter.

## 11. Digital Identity Acceptance Statement
- **Workforce.** All workforce users sign in through the identity provider with hardware security keys, which are phishing-resistant and bound to a separate device (IA-2(1), IA-2(2), IA-2(6), IA-2(8)). Privileged actions need just-in-time elevation through PAM. Exception: DC-1 clusters A and B still accept local accounts with a password from a jump host (P01 R-003; POA&M), due to be federated by 2026-12-31.
- **Agency users.** Agencies sign in with PIV credentials through federation (IA-2(12), IA-8(1)), so the assurance level is set and proofed by the agency.
- **Defense contractor and commercial customer users.** Government partition customer administrators must use MFA, enforced by the portal. Commercial customer administrator MFA is optional and only 58% are enrolled. That is below the company's standard for accounts that can delete VMs or change DNS, and is tracked as P01 R-007, with MFA required by 2027-03-31. The FedRAMP Secure Configuration Guide (SCG rules) already requires the company to document the secure defaults for privileged customer accounts, and the government partition's guide does.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); FedRAMP transition and regulatory gap analysis (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10); the 2024 FedRAMP SSP and its attachments (legacy secure repository); the Government Cloud administrator guide (2025).

## 13. Acronym List and Glossary
- **ATO:** authorization to operate
- **BMC:** baseboard management controller
- **CMDB:** configuration management database
- **CUI:** controlled unclassified information
- **FSI:** FedRAMP Security Inbox
- **HCP:** Hosting Control Plane and Customer Portal
- **HSM:** hardware security module
- **KEV:** CISA Known Exploited Vulnerabilities catalog
- **MAS:** FedRAMP Minimum Assessment Scope rules
- **MDR:** managed detection and response
- **PAIN:** Potential Agency Impact N-rating (FedRAMP 2026 rules)
- **PAM:** privileged access management
- **PIV:** personal identity verification (federal credential)
- **RMM:** remote monitoring and management
- **SBOM:** software bill of materials

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2024-04-15 | Legacy FedRAMP SSP for the government partition (separate document) | GRC Manager |
| 1.9 | 2026-07-31 | Draft covering both partitions under the Rev5 Class C control list; boundary expanded per the 2026 Minimum Assessment Scope rules | GRC Manager |
| 2.0 | 2026-09-22 | Updated with P07 results; approved by the Chief Technology Officer | GRC Manager |
