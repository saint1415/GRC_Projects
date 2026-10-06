# Scenario facts: Cris Santos Company | Information Technology | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, a standard, or a government program page, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (private; private equity-backed; board with an audit committee) |
| Business | Cloud hosting and managed infrastructure provider (NAICS 518210). Five service lines: (1) **managed private cloud** (commercial): customer virtual machines (VMs) on company-owned hypervisor clusters in three leased colocation data centers; (2) **Government Cloud**: a separate partition of the same platform, with dedicated clusters, holding a FedRAMP Rev5 certification (see Federal status); (3) **managed services**: patching, monitoring, and administration of customer servers through a remote monitoring and management (RMM) tool; (4) **managed backup and disaster recovery** for customer workloads; (5) **authoritative DNS and edge services** with a contracted DDoS scrubbing service |
| Location | Headquarters and the primary 24x7 network operations center (NOC) in Florida. **DC-1**: colocation data center in Florida (commercial only). **DC-2**: colocation data center in a Mid-Atlantic state (commercial and government). **DC-3**: colocation data center in a Southwest state (commercial and government). A secondary NOC desk operates from the DC-2 metro office |
| Workforce | 600 employees: 52 executive, finance, HR, legal, and administration; 78 sales, marketing, and account management; 118 NOC and customer support; 86 platform engineering (hypervisors, storage, data center networks); 96 software engineering (control plane, portal, API, CI/CD); 34 site reliability and cloud operations; 58 managed services engineers; 20 backup and disaster recovery services; 22 security and GRC; 16 corporate IT; 20 product and program management. About 40 contractors, all U.S.-based |
| Customers | About 2,300 business customers. **Commercial private cloud:** about 1,850 customers and about 24,000 VMs (DC-1 about 13,000, DC-2 about 6,500, DC-3 about 4,500). **Government Cloud:** 7 federal civilian agencies and 19 defense contractors, about 2,100 VMs. **Managed services:** 410 customers, about 11,200 customer servers reached through the RMM tool. **Backup and DR:** 620 customers, about 4.8 PB protected. **Banks:** 38 community and regional banks buy hosting, managed services, or backup. About 19,000 customer user accounts in the portal, about 3,400 of them customer administrators |
| Revenue | About $100 million a year (fictional): managed private cloud $46 million; Government Cloud $14 million; managed services $20 million; backup and DR $12 million; DNS, edge, and other $8 million. Not SBA-small (standard $40.0 million for NAICS 518210; 13 CFR 121.201) |
| Service commitments | Master services agreement (MSA): 99.95% monthly availability for the private cloud and Government Cloud, 99.9% for the portal; service credits of 10% below 99.95%, 25% below 99.0%, and 50% below 95.0%; customer data confidentiality clause; security incident notice "without undue delay and within 72 hours of confirmation". Government Cloud agency terms and the bank addendum add their own notice terms (P08) |
| Federal status | **FedRAMP Rev5 certification in place.** The Government Cloud received a legacy FedRAMP Rev5 **Moderate** agency authorization on 2024-05-20, with a civilian agency as sponsor; 6 more agencies have since issued their own ATOs that reuse the package. Annual independent assessments by a FedRAMP Recognized independent assessment service (last: March 2026). Monthly continuous monitoring deliverables go to the agencies through the legacy secure repository. FedRAMP's Consolidated Rules for 2026 take mandatory effect on 2027-01-01, and certifications that do not follow them by 2028-02-01 are lost (fedramp.gov, Updating to 2026 Rules, checked 2026-10-05). The company also holds a GSA Multiple Award Schedule contract through which agencies order the service, so FAR clauses 52.204-21, 52.204-23, 52.204-25, and 52.204-30 apply to it |
| Defense customers | 19 defense contractors store controlled unclassified information (CUI) and covered defense information in the Government Cloud. Their contracts with the company flow down the cloud provider duties of DFARS 252.204-7012(b)(2)(ii)(D): FedRAMP Moderate equivalent security and compliance with paragraphs (c) through (g) (incident reporting within 72 hours, malicious software, media preservation, forensic access, damage assessment). The company is not itself a DoD prime contractor; CMMC (32 CFR Part 170) binds those customers, who rely on the company's FedRAMP Moderate status under 32 CFR 170.16(c)(2) |
| Bank customers | The 38 banks' vendor contracts treat the company's services as services subject to the Bank Service Company Act, so the company is a **bank service provider** (12 CFR 53.2(b)(2), 53.4; 225.303; 304.24) |
| Not in scope | PHI: the MSA prohibits it and the company signs no business associate agreements. Payment cards: billing uses the payment processor's hosted page. DOJ Data Security Program (28 CFR Part 202): no vendor, employment, or investment agreement gives a country of concern or covered person access to customer data; all staff and contractors are U.S.-based (rechecked in P03). CUI and federal data are prohibited in the commercial partition and in the managed services line |
| State law approach | Customers, their data subjects, and employees live in many states. State breach law is treated generically ("each state where affected individuals reside"), with Florida (Fla. Stat. 501.171) as the worked example |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk and FedRAMP status reporting; oversees the co-sourced internal audit firm |
| Chief Executive Officer (CEO) | Accepts High risks; approves the risk appetite and the security budget; signs agency, bank, and GSA contracts |
| Chief Technology Officer (CTO) | Executive sponsor of the security program and **system owner** of the HCP (P02); accepts Moderate risks; approves policies POL-02 to POL-05 |
| Chief Financial Officer (CFO) | Cyber insurance, vendor contracts, SOC 2 engagement sponsor |
| General Counsel | Legal lead for incidents, breach and contract notices, government contracts, and AI legal review |
| Director of Security | Leads the 22-person security and GRC team; owns POL-01; FedRAMP senior security official who receives Emergency messages from the FedRAMP Security Inbox; reports to the CTO and to the audit committee each quarter |
| GRC Manager (with 3 GRC analysts) | Risk register, FedRAMP package and continuous monitoring, SOC 2, policies and standards, vendor risk program |
| Security Operations Manager (with 6 SOC analysts) | Security monitoring, incident command, federal incident response coordinator for FedRAMP incident reports; oversees the managed detection and response (MDR) partner |
| Security Engineering Lead (with 3 engineers) | Privileged access management (PAM), vulnerability scanning, SIEM content, cryptography |
| VP Platform Engineering | Data centers, hypervisor clusters, storage, data center networks, out-of-band management |
| VP Software Engineering | Control plane, portal, public API, CI/CD pipeline, VM template build and signing |
| Director of Cloud Operations | Public cloud landing zone and site reliability for the control plane |
| Director of NOC and Customer Support | 24x7 NOC; first responder for incidents; status page; customer and bank notices |
| Director of Managed Services | RMM tool and managed services delivery |
| Director of Backup and DR Services | Managed backup platform and customer restore and DR services |
| Federal Program Director | Government Cloud business owner; agency and defense customer relationships; FedRAMP Marketplace listing |
| Director of Corporate IT | Workforce identity provider, endpoints, productivity suite, HR and finance SaaS |
| HR Director | Onboarding, terminations, background checks, training records, hiring tools |
| Co-sourced internal audit firm | Annual IT audit for the audit committee; performed the P07 assessment. Independent of the teams it assesses |
| FedRAMP Recognized independent assessment service | Annual FedRAMP independent assessment of the Government Cloud. Not involved in P01 to P10 |
| Outside counsel | Breach, contract, and government contracting advice; engaged through the cyber insurer's panel for incidents |

**Where roles overlap:** the Director of Security both runs security operations and owns the program it is assessed against, and the GRC team writes the FedRAMP package it also reports on. The company compensates with the co-sourced internal audit firm (reports to the audit committee) and the FedRAMP independent assessor, neither of which designs or operates controls.

## 3. Systems

| ID | System | Hosting | Holds customer data? | Notes |
|---|---|---|---|---|
| SYS-01 | Customer portal and public API | Company-built; runs in SYS-04 | Yes (tenant metadata, customer credentials) | Two partitions: commercial and government. Customer administrator MFA is required in the government partition and optional in the commercial partition (58% of commercial customer administrators enrolled). Agency users sign in with federal credentials through federation |
| SYS-02 | Control plane orchestration services | Company-built; runs in SYS-04 | Yes (tenant inventory, service credentials) | Provisioning engine, job queue, tenant database, metering. Separate deployments for the commercial and government partitions in separate cloud accounts. Holds service credentials that act on every VM in its partition |
| SYS-03 | Workforce identity provider (SSO, MFA) | SaaS (the vendor holds its own FedRAMP certification) | No (identities only) | Phishing-resistant hardware security keys for all workforce since 2025 |
| SYS-04 | Public cloud landing zone: 10 accounts (organization management, security tooling, log archive, identity and shared services, network hub, HCP commercial production, HCP government production, CI/CD build, non-production, backup) | Public cloud provider (vendor-agnostic; government account in regions covered by the provider's own FedRAMP certification) | Yes | Hosts SYS-01, SYS-02, build runners, and control plane backups |
| SYS-05 | Private cloud platform | Company-owned hardware in DC-1, DC-2, DC-3 | Yes (customer VMs) | 540 hypervisor hosts in 16 clusters and 28 storage arrays. DC-1: 7 clusters, 236 hosts. DC-2: 5 clusters, 176 hosts (2 government clusters, 64 hosts). DC-3: 4 clusters, 128 hosts (1 government cluster, 32 hosts). Paid replication tier covers about 35% of commercial VMs |
| SYS-06 | Virtualization management, out-of-band management, and privileged access | Company-owned, all three data centers; PAM is SaaS-managed software on company hosts | Yes (full control of customer VMs) | Hypervisor managers, host baseboard management controllers (BMCs), management networks, PAM with session recording and just-in-time elevation |
| SYS-07 | Source code repository and CI/CD pipeline | SaaS code hosting plus build runners in SYS-04 | No (source, VM templates, signing keys) | Builds the control plane, portal, and VM templates. Government templates are signed with a key in a cloud hardware security module (HSM); commercial templates with a key stored as a pipeline secret |
| SYS-08 | RMM tool | SaaS (RMM vendor) | Yes (agent access to customer servers) | Agents on about 11,200 commercial customer servers; can run scripts on any of them. Not used for Government Cloud tenants |
| SYS-09 | Edge network and authoritative DNS | Company routers and firewalls in each data center; contracted DDoS scrubbing service | Yes (customer DNS zones) | Two upstream carriers per data center |
| SYS-10 | Managed backup platform | Company backup software and immutable object storage in DC-2 and DC-3 | Yes (customer backup copies) | Backs up customer VMs and servers; write-once retention options for customers |
| SYS-11 | Security operations stack | SaaS SIEM (vendor holds its own FedRAMP certification) with AI-assisted alert triage; EDR; vulnerability scanners; MDR partner | Yes (logs) | 24x7 tier-1 triage by the MDR partner; in-house SOC by day and on call. AI triage enabled in March 2026 (P10) |
| SYS-12 | IT service management: ticketing, change management, configuration management database (CMDB), status page | SaaS | Incidental | The status page runs on a separate provider from the platform |
| SYS-13 | Corporate IT: productivity suite, 680 laptops and 40 NOC workstations, HR, payroll, finance, and billing SaaS | SaaS and company-managed endpoints | Customer contact and billing data; employee data | EDR and full-disk encryption on all endpoints |
| SYS-14 | FedRAMP package repository | Legacy secure repository folders shared with agencies | FedRAMP package and continuous monitoring data | A FedRAMP-compatible trust center is not yet in place (P03) |
| SYS-15 | Third-party vendors | Various | Varies | About 260 vendors; 34 with access to customer data or production systems; 14 rated Tier 1 |

**SSP system (P02):** the *Hosting Control Plane and Customer Portal (HCP)*: SYS-01, SYS-02 (both partitions), SYS-03, SYS-04, SYS-06, SYS-07, and the logging in SYS-11, with the 3 government clusters of SYS-05 and the management interfaces of all SYS-05 clusters and SYS-09. The FedRAMP-certified Government Cloud is the government partition of this boundary.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- FedRAMP Rev5 Moderate certification (legacy agency path) since 2024-05-20, with annual independent assessments and monthly continuous monitoring deliverables
- SOC 2 Type 2 report (Security, Availability) for the commercial private cloud and the backup service; latest period 2025-07-01 to 2026-06-30, unqualified opinion with 3 exceptions
- Phishing-resistant MFA (hardware security keys) for all workforce single sign-on, the cloud consoles, the code repository, and the RMM console
- PAM with session recording and just-in-time elevation for the government clusters and all DC-2 and DC-3 clusters
- EDR on all endpoints and servers the company manages; SaaS SIEM with 24x7 MDR triage
- Multi-account cloud landing zone built with infrastructure as code; pull-request review with two approvers for control plane code
- FIPS 140-validated cryptographic modules for the government partition (TLS termination, storage encryption, HSM)
- Immutable control plane backups in a separate backup account and second region; quarterly restore tests for the government partition
- Monthly authenticated vulnerability scanning and an annual penetration test for the Government Cloud
- A FedRAMP Security Inbox (since 2026-01) and a Government Cloud administrator guide (2025)
- Change advisory board for production changes; written incident response plan (2024), tabletop in February 2026
- Vendor risk program with tiering; background checks for all hires; annual awareness and role-based training
- Cyber insurance with an incident response panel

**Missing or weak, found in the 2026 assessments:**
1. **Two-speed security.** Controls built for the Government Cloud were not extended to the commercial partition and DC-1. Two older DC-1 clusters (64 hosts) still use local hypervisor accounts outside PAM; DC-1 BMC firmware lags; commercial access reviews are semiannual, not quarterly.
2. **FedRAMP 2026 rules transition not planned.** No machine-readable certification package, no FedRAMP-compatible trust center, no Ongoing Certification Reports or Quarterly Reviews, no availability status service that meets the new rules, vulnerability response still on the legacy POA&M model, and no incident reporting process built on the Potential Agency Impact N-rating (PAIN) and its 1-hour clock.
3. **Assessment scope too narrow.** The 2024 boundary treated the shared CI/CD pipeline, the workforce identity provider tenant, the SIEM tenant, and IT service management as external services. Third-party information resources are not documented the way the 2026 Minimum Assessment Scope rules require.
4. **RMM tool exposure.** Standing access to about 11,200 customer servers; scripts can run across all customers with no second approval; 2 shared RMM super-administrator accounts used by the on-call rotation; RMM logs are not in the SIEM.
5. **Commercial VM template signing.** The commercial signing key is a pipeline secret, and signature verification is not enforced at deployment in the commercial partition.
6. **Logging at scale.** Government partition logs are complete with 1 year online retention. Commercial hypervisor and BMC logs reach the SIEM from DC-2 and DC-3 but only partly from DC-1; commercial retention is 90 days online.
7. **Vulnerability management at scale.** Commercial clusters are scanned quarterly, not monthly; 14% of DC-1 BMCs run outdated firmware; known exploited vulnerability (KEV) tracking is manual.
8. **Recovery at scale.** DC-1 holds about 54% of commercial VMs, and only replicated VMs (about 35%) can fail over. The commercial control plane partition missed its 4-hour RTO in its only restore test (2025). DC-1 is exposed to hurricanes.
9. **Third-party risk at scale.** Annual reviews completed for 9 of 14 Tier 1 vendors; 4 Tier 1 contracts lack incident notice terms; the RMM vendor's SOC 2 report has exceptions that were never followed up.
10. **Customer identity.** Commercial customer administrator MFA is optional (58% enrolled).
11. **AI adopted without governance.** SIEM AI triage auto-closes commercial alerts; a coding assistant is used by about 70 engineers; a support reply assistant drafts ticket answers; HR is piloting AI resume screening. None was reviewed before use.
12. **Privileged access in the commercial partition.** 214 engineers hold privileged roles; just-in-time elevation exists only in the government partition and DC-2 and DC-3.
13. **Software supply chain.** No software bill of materials (SBOM) for VM templates or control plane releases; build provenance is not recorded.
14. **Bank notice readiness.** Bank-designated contacts verified for 31 of 38 banks; the 4-hour determination step is in the 2024 plan but has never been exercised.
15. **Long-lived CI/CD deploy token (found during P07 testing).** A deploy token created in 2024 for a migration had write access to the government partition's deployment repository, no expiry, and was missing from the secrets inventory.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | **FedRAMP applies.** P03 is a transition gap analysis of the existing Rev5 certification against the FedRAMP Consolidated Rules for 2026, using the Rev5 Class C rule set and control list (the class the company and its sponsoring agency target, because Class C covers most Low and Moderate security objectives). Also analyzed because they apply to the primary business line: the bank service provider notification rule; the DFARS 252.204-7012 cloud provider duties flowed down by defense customers; FAR safeguarding and reporting clauses; Fla. Stat. 501.171 third-party agent duties |
| P08 incidents | **Two incident types:** (1) compromise of provider tooling affecting downstream customers: an attacker uses a stolen managed services engineer session to push a malicious script through the RMM tool to managed customer servers, including bank customers, and attempts to pivot into the HCP; (2) loss of DC-1 after a hurricane or facility failure. Both integrated with crisis management and legal |
| P09 SOC 2 | Readiness for the next SOC 2 Type 2 examination with expanded scope: add Confidentiality and Processing Integrity (backup service) and bring the managed services line and DC-3 into scope. Target period 2027-01-01 to 2027-09-30. Plus a vendor SOC 2 review program for Tier 1 vendors |
| P10 AI | AI use-case portfolio: AI-001 AI-driven security operations (alert triage), AI-002 coding assistant, AI-003 support reply assistant, AI-004 hardware failure and capacity forecasting, AI-005 resume screening pilot |
| Cloud | Vendor-agnostic multi-account landing zone. AWS, Azure, and Google Cloud equivalents appear only in an equivalents table |
| Registry defaults kept | Primary system "Hosting control plane and customer portal", incident "Compromise of provider tooling affecting downstream customers", and AI use case "AI-driven security operations (alert triage)" all fit this business at this size and are kept. The second incident type and the other AI use cases were added because the Mid-Market tier calls for two incident types and an AI portfolio |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and FedRAMP transition and regulatory gap analysis fieldwork |
| 2026-08-03 to 2026-08-21 | Control assessment fieldwork by the co-sourced internal audit firm (DC-1 walkthrough 2026-08-11; DC-2 walkthrough 2026-08-13) |
| 2026-08-24 to 2026-09-11 | SOC 2 readiness assessment and AI governance assessment |
| 2026-09-22 | Results to the board audit committee; deliverables approved by the CTO (Moderate and below) and the CEO (High and above) |
| 2026-10-01 | Policies POL-01 to POL-05 take effect |

## 7. Facts added while building the deliverables
These details were added during the build and are used consistently across P01 to P10.

| Topic | Added fact |
|---|---|
| Revenue per day | About $274,000 a day company-wide; managed private cloud about $126,000; Government Cloud about $38,000; managed services about $55,000; backup and DR about $33,000 |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics; the policy requires notice through the carrier hotline before incident vendors are engaged |
| Legacy POA&M | 41 open items in the Government Cloud POA&M at 2026-07-31, 3 of them past their scheduled date |
| Privileged population | 214 engineers with privileged roles: 86 platform, 58 managed services, 34 site reliability, 22 software engineers with production deploy rights, 14 security |
| Workforce activity | 74 terminations and 41 internal transfers in the 12 months to 2026-06-30 |
| SIEM volume | About 41,000 alerts in July 2026; the AI triage feature auto-closed 68% of commercial-partition alerts without human review. Auto-close is disabled for government-partition alerts |
| RMM | The vendor keeps audit logs for 90 days; its SOC 2 report (period ending 2026-03-31) has 2 exceptions on administrator access reviews |
| Bank contacts | Designated points of contact verified for 31 of 38 banks (last full verification 2025-11) |
| FedRAMP Security Inbox | Established 2026-01-05. FedRAMP's April 2026 Emergency Test message reached the Director of Security, but the required action was completed after the timeframe in the message |
| SOC 2 exceptions (2025-2026 report) | 2 of 25 sampled terminations removed late; 1 of 40 sampled changes lacked documented approval; 1 quarterly restore test for a backup service region was skipped |
| P07 scope | 40 controls (the 34 base controls FedRAMP requires in each year's independent assessment for Rev5 Class C under IVV-CSF-AIA, plus 6 enhancements tied to top risks), 185 determination statements |
| Additional role titles | VP Sales; Financial Services Account Director (relationship owner for the 38 banks); Data Center Operations Managers for DC-1, DC-2, DC-3; Director of Communications |
