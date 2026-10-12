# Scenario facts: Cris Santos Company | Information Technology | Enterprise

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, a standard, or a government program page, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; large accelerated filer, not a smaller reporting company) |
| Business | Public cloud and managed infrastructure provider (NAICS 518210). Three service lines: **SL-1 Commercial Cloud** (multi-tenant IaaS and PaaS: compute, block and object storage, managed databases, managed Kubernetes, networking, DNS, and content delivery); **SL-2 Government Cloud** (a dedicated U.S. government region for federal, state, and local agencies and defense contractors); **SL-3 Managed Infrastructure Services** (patching, monitoring, backup, and operations of customer servers, delivered through the company's fleet automation service and, for customers of an acquired business, a legacy remote monitoring and management (RMM) tool) |
| Location | Headquartered in Florida. Six commercial regions (R1 to R6) in six states, each with three company-operated data centers (availability zones), for 18 commercial data centers. R1 is in Florida. The **Government region (G1)** has two company-operated data centers (G1-A and G1-B) in two eastern states. 41 edge points of presence (PoPs) in colocation facilities. **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: about 5,200 in engineering, 2,100 in data center operations, 1,800 in support and customer success, 1,500 in sales and marketing, 480 in security (including a 24x7 SOC of about 140), and 920 in general and administrative roles. About 1,400 contractors. G1 operations staff are U.S. persons by company design (EV-006, EV-004) |
| Customers | About 41,000 business customers and about 310,000 customer console identities. Includes **38 federal civilian agencies and 12 state and local agencies on SL-2**, 21 federal agencies on SL-1, about 420 defense industrial base (DIB) companies storing controlled unclassified information (CUI) on SL-2, **about 210 banking organizations** on SL-1 and SL-3, and about 1,100 health care customers using HIPAA-eligible SL-1 services under business associate agreements (BAAs) (EV-045) |
| Revenue | About $4.8 billion a year (fictional), about $13.2 million per calendar day. SL-1 about 78%, SL-2 about 12%, SL-3 about 10% (EV-036, EV-052) |
| Service commitments | SLA: 99.99% monthly availability for multi-zone compute and storage, 99.95% for single-zone resources, 99.9% for the console and API. Customer agreement: security incident notice "without undue delay and within 72 hours of confirmation". SL-2 agreements add FedRAMP incident communication. A bank addendum and a DFARS addendum are offered to those customers (EV-042) |
| FedRAMP status | **FR-1:** SL-1 Commercial Cloud holds a FedRAMP Rev5 Class C certification (originally a FedRAMP Moderate agency authorization, 2020), 64 services in scope. **FR-2:** SL-2 Government Cloud holds a Rev5 Class C certification (originally Moderate, 2022), 52 services in scope. **Class D upgrade:** a civilian agency (the "sponsoring agency") plans to move a High-impact workload to G1 and will sponsor a **Rev5 Class D Agency Certification** for SL-2. FedRAMP stops accepting new Rev5 certification applications on 2027-06-11 (fedramp.gov Important Dates, retrieved 2026-10-05). Applicability is in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-IT-R01; EV-029, EV-065) |
| Other regulatory status | Bank service provider for about 210 banking organizations (12 CFR 53.4; 225.303; 304.24). HIPAA business associate for the HIPAA-eligible SL-1 services. DIB customers flow down DFARS 252.204-7012(b)(2)(ii)(D) by contract addendum (FedRAMP Moderate equivalent and paragraphs (c) to (g)). No direct DoD prime contracts. SOX Section 404 IT general controls are tested by a separate SOX program. Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv), with counsel's review (EV-056): CMMC applies only indirectly, CIRCIA is not in force, and the full list of rules and their basis is there |
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
The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Notes |
|---|---|---|
| SYS-01 | Customer portal (console) and public API | Global instance for R1 to R6; separate instance in G1 |
| SYS-02 | Regional control plane services | Provisioning, placement, metering, tenant database, customer identity and access service. One control plane per region |
| SYS-03 | Workforce identity platform | SSO with phishing-resistant MFA, privileged access management (PAM) with just-in-time elevation, identity governance. AQ-1 staff are still on a separate legacy directory (EV-007) |
| SYS-04 | Hypervisor fleet and host management | About 240,000 commercial hosts and 9,000 G1 hosts; out-of-band management network for baseboard management controllers (BMCs). About 1,900 hosts in R3 run a hypervisor release that leaves vendor support on 2027-03-31 (EV-010) |
| SYS-05 | Storage services | Block and object storage, snapshots, and the immutable backup vault service |
| SYS-06 | Global network and edge | Backbone, 41 edge PoPs, DDoS mitigation, authoritative DNS, content delivery |
| SYS-07 | Key management service and PKI | Customer key management service backed by hardware security modules (HSMs); internal certificate authorities |
| SYS-08 | Software supply chain | Source repositories, CI/CD, artifact signing with HSM-held keys, release orchestration |
| SYS-09 | Fleet automation service | Deploys host software and guest-agent updates to customer virtual machines (VMs) that run the guest agent, and runs SL-3 managed-services jobs on about 48,500 customer servers. Can reach every host and enrolled guest (EV-024) |
| SYS-10 | Legacy RMM tool (AQ-1) | SaaS RMM from the acquired managed services provider. About 9,500 servers of 140 SL-3 customers. Migration to SYS-09 due 2027-03-31 (EV-008, EV-053) |
| SYS-11 | Security operations platform | SIEM and security data lake, EDR, vulnerability management, and AI-driven alert triage (P10; EV-018) |
| SYS-12 | Corporate IT | About 15,000 endpoints; productivity, ticketing, and CRM SaaS |
| SYS-13 | Billing, metering, and ERP | SOX-relevant |
| SYS-14 | External cloud tenancy (Cloud provider X, vendor-agnostic) | Public status page, out-of-band recovery vault for control plane state, corporate analytics |
| SYS-15 | Third parties | About 2,600 vendors (hardware manufacturers, colocation providers for PoPs, carriers, utilities, SaaS). 310 are tier 1 or tier 2 (EV-040) |
| SYS-16 | AI portfolio | 15 use cases governed by the AI governance committee (formed 2025) (EV-055) |

**SSP system (P02):** the *Hosting Control Plane and Customer Portal, Government Region (HCP-G)*: the G1 instances of SYS-01, SYS-02, SYS-04 host management, SYS-05 storage control services, SYS-07 key management, the G1 channel of SYS-09, and the G1 logging in SYS-11, categorized High as the system behind the Rev5 Class D upgrade of SL-2, inheriting common controls from enterprise providers.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. At this size the sources are enterprise systems of record: the workforce identity platform and HR system, the CMDB and provisioning system, the network policy repository, the SIEM, SOC case platform and vulnerability platform, the key management service, the fleet automation and release systems, the third-party risk register and contract repository, the FedRAMP compliance group's records, board and disclosure committee records, Internal Audit and SOX workpapers, and the SEC filings.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv), reviewed by the General Counsel's office.
- **Gaps against the FedRAMP rules and the other applicable rules** are judged in the gap analysis (P03), and **whether controls work** is tested by Internal Audit in the control assessment (P07). Both cite evidence IDs.

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
| 2026-05-04 to 2026-05-29 | Intake: evidence requests, exports from systems of record, inventories, obligations register (reviewed by counsel) |
| 2026-06-01 to 2026-07-31 | Enterprise BIA, risk analysis, and regulatory gap analysis (gap analysis evidence sampling completed 2026-08-14) |
| 2026-06-22 to 2026-07-10 | POL-01 to POL-05 and the policy hierarchy drafted from the intake evidence and early risk and gap results |
| 2026-07-13 to 2026-08-28 | Control assessment of HCP-G by Internal Audit (Class D readiness): operating tests of controls in force under the existing policy hierarchy; design review of the draft policies |
| 2026-08-31 to 2026-09-04 | SOC 2 readiness and AI portfolio review |
| 2026-09-08 | Executive risk committee approvals, including POL-02 to POL-05 (effective 2026-10-01) |
| 2026-09-10 | Results to the risk and technology committee and the audit committee of the board; POL-01 approved by the risk and technology committee (effective 2026-10-01) |
| 2026-10-05 | FedRAMP rule sources re-checked (Consolidated Rules for 2026, version 2026.10.05.01) |
| 2027-01 (planned) | Internal Audit follow-up: retest of POAM-001, POAM-009 and POAM-010, and operating effectiveness of the controls the new policies introduced, after one quarter of operation |

## 7. Facts added while building the deliverables
| Fact | Used in |
|---|---|
| G1 has about 26,000 customer console identities, about 260 U.S.-person operations staff, and about 40 engineers outside G1 operations who hold G1 roles (EV-004, EV-005) | P02 |
| FR-1 and FR-2 annual FedRAMP independent assessment last completed 2026-03, with no open High findings (EV-030) | P02, P03 |
| Class D schedule: sponsoring agency letter 2026-08-20; independent assessment 2027-04; agency ATO target 2027-05-21; application by 2027-05-28 (EV-065, EV-079) | P02, P03, P07 |
| Two FedRAMP Reportable Incidents and three drills since the IEC rules were adopted early (2026-08-03); incident response plan v7 approved 2026-09-08 (EV-076, EV-IR-6, EV-IR-8) | P03, P07 |
| About 180 AQ-1 technicians still use the legacy directory (EV-007) | P06 |
| Bank addendum signed by 196 of 210 banking organizations (EV-042) | P03 |
| SOC 2 Type 2 reports issued for SL-1 since 2021 and SL-2 since 2023; ISO/IEC 27001 certification held for SL-1 and SL-2; first SL-3 Type 2 period 2027-04-01 to 2027-09-30 (EV-033) | P09 |
| Disclosure committee tabletop on the provider tooling scenario set for 2026-11-18 | P01, P07, P08 |
| Funded treatment for 2026 Q4 to 2027 Q2: about $38 million (Class D program about $14.5 million) | P01, P07 |
