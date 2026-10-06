# Scenario facts: Cris Santos Company | Information Technology | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, a standard, or a government program page, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; large accelerated filer, not a smaller reporting company) |
| Business | Public cloud and managed infrastructure provider (NAICS 518210). Three service lines: **SL-1 Commercial Cloud** (multi-tenant IaaS and PaaS: compute, block and object storage, managed databases, managed Kubernetes, networking, DNS, and content delivery); **SL-2 Government Cloud** (a dedicated U.S. government region for federal, state, and local agencies and defense contractors); **SL-3 Managed Infrastructure Services** (patching, monitoring, backup, and operations of customer servers, delivered through the company's fleet automation service and, for customers of an acquired business, a legacy remote monitoring and management (RMM) tool) |
| Location | Headquartered in Florida. Six commercial regions (R1 to R6) in six states, each with three company-operated data centers (availability zones), for 18 commercial data centers. R1 is in Florida. The **Government region (G1)** has two company-operated data centers (G1-A and G1-B) in two eastern states. 41 edge points of presence (PoPs) in colocation facilities. **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: about 5,200 in engineering, 2,100 in data center operations, 1,800 in support and customer success, 1,500 in sales and marketing, 480 in security (including a 24x7 SOC of about 140), and 920 in general and administrative roles. About 1,400 contractors. G1 operations staff are U.S. persons by company design |
| Customers | About 41,000 business customers and about 310,000 customer console identities. Includes **38 federal civilian agencies and 12 state and local agencies on SL-2**, 21 federal agencies on SL-1, about 420 defense industrial base (DIB) companies storing controlled unclassified information (CUI) on SL-2, **about 210 banking organizations** on SL-1 and SL-3, and about 1,100 health care customers using HIPAA-eligible SL-1 services under business associate agreements (BAAs) |
| Revenue | About $4.8 billion a year (fictional), about $13.2 million per calendar day. SL-1 about 78%, SL-2 about 12%, SL-3 about 10% |
| Service commitments | SLA: 99.99% monthly availability for multi-zone compute and storage, 99.95% for single-zone resources, 99.9% for the console and API. Customer agreement: security incident notice "without undue delay and within 72 hours of confirmation". SL-2 agreements add FedRAMP incident communication. A bank addendum and a DFARS addendum are offered to those customers |
| FedRAMP status | **FR-1:** SL-1 Commercial Cloud holds a FedRAMP Rev5 Class C certification (originally a FedRAMP Moderate agency authorization, 2020), 64 services in scope. **FR-2:** SL-2 Government Cloud holds a Rev5 Class C certification (originally Moderate, 2022), 52 services in scope. **Class D upgrade:** a civilian agency (the "sponsoring agency") plans to move a High-impact workload to G1 and will sponsor a **Rev5 Class D Agency Certification** for SL-2. FedRAMP stops accepting new Rev5 certification applications on 2027-06-11 (fedramp.gov Important Dates, retrieved 2026-10-05) |
| Other regulatory status | Bank service provider for about 210 banking organizations (12 CFR 53.4; 225.303; 304.24). HIPAA business associate for the HIPAA-eligible SL-1 services. DIB customers flow down DFARS 252.204-7012(b)(2)(ii)(D) by contract addendum (FedRAMP Moderate equivalent and paragraphs (c) to (g)). No direct DoD prime contracts. SOX Section 404 IT general controls are tested by a separate SOX program |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); disclosure committee; three lines model; growth by acquisition (AQ-1, a managed services provider acquired 2025-07) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board (audit committee; risk and technology committee) | Cyber oversight (Item 106 disclosure). The risk and technology committee receives quarterly cyber reporting |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk; take part in materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Security program owner; chairs the policy governance committee |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee |
| Chief Technology Officer (CTO) | Owns the cloud platform engineering organization; chairs the AI governance committee |
| GRC team (14, including a FedRAMP compliance group of 5), Security Operations Center (24x7, in-house), Internal Audit (in-house IT audit team of 9) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | Customer portal (console) and public API | Global instance for R1 to R6; separate instance in G1 |
| SYS-02 | Regional control plane services | Provisioning, placement, metering, tenant database, customer identity and access service. One control plane per region |
| SYS-03 | Workforce identity platform | SSO with phishing-resistant MFA, privileged access management (PAM) with just-in-time elevation, identity governance. AQ-1 staff are still on a separate legacy directory |
| SYS-04 | Hypervisor fleet and host management | About 240,000 commercial hosts and 9,000 G1 hosts; out-of-band management network for baseboard management controllers (BMCs). About 1,900 hosts in R3 run a hypervisor release that leaves vendor support on 2027-03-31 |
| SYS-05 | Storage services | Block and object storage, snapshots, and the immutable backup vault service |
| SYS-06 | Global network and edge | Backbone, 41 edge PoPs, DDoS mitigation, authoritative DNS, content delivery |
| SYS-07 | Key management service and PKI | Customer key management service backed by hardware security modules (HSMs); internal certificate authorities |
| SYS-08 | Software supply chain | Source repositories, CI/CD, artifact signing with HSM-held keys, release orchestration |
| SYS-09 | Fleet automation service | Deploys host software and guest-agent updates to customer virtual machines (VMs) that run the guest agent, and runs SL-3 managed-services jobs on about 48,500 customer servers. Can reach every host and enrolled guest |
| SYS-10 | Legacy RMM tool (AQ-1) | SaaS RMM from the acquired managed services provider. About 9,500 servers of 140 SL-3 customers. Migration to SYS-09 due 2027-03-31 |
| SYS-11 | Security operations platform | SIEM and security data lake, EDR, vulnerability management, and AI-driven alert triage (P10) |
| SYS-12 | Corporate IT | About 15,000 endpoints; productivity, ticketing, and CRM SaaS |
| SYS-13 | Billing, metering, and ERP | SOX-relevant |
| SYS-14 | External cloud tenancy (Cloud provider X, vendor-agnostic) | Public status page, out-of-band recovery vault for control plane state, corporate analytics |
| SYS-15 | Third parties | About 2,600 vendors (hardware manufacturers, colocation providers for PoPs, carriers, utilities, SaaS). 310 are tier 1 or tier 2 |
| SYS-16 | AI portfolio | 15 use cases governed by the AI governance committee (formed 2025) |

**SSP system (P02):** the *Hosting Control Plane and Customer Portal, Government Region (HCP-G)*: the G1 instances of SYS-01, SYS-02, SYS-04 host management, SYS-05 storage control services, SYS-07 key management, the G1 channel of SYS-09, and the G1 logging in SYS-11, categorized High as the system behind the Rev5 Class D upgrade of SL-2, inheriting common controls from enterprise providers.

## 4. Current security posture: mature, with residual gaps
**In place today:**
- A program aligned to CSF 2.0, run under the three lines model, with annual risk analysis tied to ERM (NIST IR 8286)
- Two FedRAMP Rev5 Class C certifications with annual independent assessments by a FedRAMP Recognized assessment service
- A policy hierarchy of policies, standards, procedures, and an exceptions register
- 24x7 in-house SOC; EDR on corporate endpoints and on host management servers
- PAM with just-in-time elevation and phishing-resistant MFA for all workforce and privileged access (except AQ-1 legacy accounts)
- HSM-backed signing of host software and guest-agent releases
- Immutable, cross-region backups of control plane state, plus a copy in the out-of-band recovery vault
- Annual disaster recovery tests for every regional control plane
- Tiered third-party risk program with annual SOC report reviews for tier-1 vendors
- Annual SOC 2 Type 2 reports for SL-1 and SL-2
- SEC Item 106 disclosure in the 10-K

**Residual gaps:**
1. **AQ-1 integration.** The legacy RMM tool (SYS-10) reaches about 9,500 customer servers. AQ-1 technicians sign in through the legacy directory with app-based MFA, not PAM, and RMM logs reach the SIEM only as a daily batch.
2. **Fleet automation blast radius.** SYS-09 can push to every host and enrolled guest. Two-person approval applies to host releases but not to guest-agent channel releases, and the same team can author and approve a guest-agent release.
3. **FedRAMP 2026 rules and the Class D upgrade.** The Consolidated Rules for 2026 require new practices (Security Decision Record in JSON, trust center, Ongoing Certification Reports, persistent vulnerability timeframes, PAIN ratings) with mandatory dates from 2026-12-07 to 2028-02-01. Of the 87 controls and enhancements that Class D adds to Class C, 43 are not yet fully in place in G1 (2 do not apply).
4. **Cryptographic modules.** Two G1 services use a cryptographic library update stream whose validation is pending under the NIST Cryptographic Module Validation Program. Class D requires active validations.
5. **Third parties and hardware supply chain.** No tamper-evidence checks on server deliveries to G1 (SR-9), and 26 tier-1 vendor SOC reviews are overdue.
6. **Legacy hypervisor.** About 1,900 R3 hosts run a hypervisor release that leaves vendor support on 2027-03-31.
7. **AI.** 15 use cases; 10 reviewed by the AI governance committee. The SOC's AI triage can isolate hosts and suspend customer accounts without a human for some alert classes.
8. **Materiality.** The materiality worksheet does not yet quantify SLA credits, customer churn, and federal certification impact for a multi-tenant incident, and it was last exercised in 2026-02, before AQ-1 reporting lines were added.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 | HCP-G, categorized High. The registry default ("Hosting control plane and customer portal") is kept, scoped to its Government region instance, because that instance is the high-value system the Class D upgrade depends on |
| P03 | All applicable regulations across the enterprise. Primary: FedRAMP Consolidated Rules for 2026, for maintaining FR-1 and FR-2 (Rev5 Class C) and for the Class D upgrade of SL-2. Also: SEC Item 1.05 and Item 106, bank service provider notification, HIPAA (business associate), DFARS 252.204-7012 contractual flow-down, CMMC applicability, DOJ Data Security Program, state breach laws (Florida worked example), and CIRCIA status |
| P08 | Compromise of provider tooling affecting downstream customers (registry default): an attacker uses a stolen engineer session to push a malicious guest-agent update through the fleet automation service, with an **SEC materiality assessment and 8-K Item 1.05** step, FedRAMP, bank, DFARS, HIPAA, and multi-state customer notification workflows |
| P09 | SOC 2 Type 2 readiness across SL-1, SL-2, and SL-3 |
| P10 | Enterprise AI portfolio (15 use cases) with the AI governance committee; full assessment of AI-001, AI-driven security operations (alert triage), the registry default |
| Cloud | The company is itself a cloud provider. P04 covers its own platform, its internal landing zones, an external public cloud (vendor-agnostic) used for recovery and status, and SaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise BIA, risk analysis, and regulatory gap analysis |
| 2026-07-13 to 2026-08-28 | Control assessment of HCP-G by Internal Audit (Class D readiness) |
| 2026-08-31 to 2026-09-04 | SOC 2 readiness and AI portfolio review |
| 2026-09-08 | Executive risk committee approvals |
| 2026-09-10 | Results to the risk and technology committee and the audit committee of the board |
| 2026-10-05 | FedRAMP rule sources re-checked (Consolidated Rules for 2026, version 2026.10.05.01) |
