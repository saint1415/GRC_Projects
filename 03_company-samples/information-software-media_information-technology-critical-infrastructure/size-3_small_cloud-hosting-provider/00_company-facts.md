# Scenario facts: Cris Santos Company | Information Technology | Small

All 11 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation, a standard, or a government program page, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (cloud hosting and managed infrastructure provider) |
| Business | Cloud hosting and managed infrastructure (NAICS 518210). Three service lines: (1) **managed private cloud**: customer virtual machines on company-owned hypervisor clusters in two leased colocation facilities; (2) **managed services**: patching, monitoring, and backup for customer servers, performed remotely through a remote monitoring and management (RMM) tool; (3) **authoritative DNS and edge services** bundled with hosting |
| Location | Headquarters and 24x7 network operations center (NOC) in Florida. **DC-1**: primary colocation facility in Florida. **DC-2**: secondary colocation facility about 450 miles away in another state |
| Workforce | 60 employees: 6 executive and administration, 8 sales and account management, 16 NOC and customer support, 12 platform engineering, 10 software engineering (control plane and portal), 6 managed services engineers, 2 IT (IT Manager and one IT specialist) (EV-003) |
| Customers | About 430 business customers (software companies, e-commerce firms, professional services firms, manufacturers). Includes **14 community banks**. About 2,300 customer virtual machines; 58 managed services customers with about 1,900 customer servers reached through the RMM tool; about 2,600 customer user accounts in the customer portal (EV-045) |
| Revenue | $24.0 million a year (fictional). Under the SBA standard of $40.0 million for NAICS 518210 (13 CFR 121.201), so SBA-small (EV-044) |
| Service commitments | Master services agreement (MSA): 99.95% monthly availability for the private cloud and 99.9% for the portal; customer data confidentiality clause; security incident notice to customers "without undue delay and within 72 hours of confirmation" (EV-039) |
| Federal status | **No federal customer today.** A civilian federal agency program office sent a letter of interest in May 2026 to host a Moderate-impact case management application on the managed private cloud, and would act as agency sponsor for a FedRAMP Rev5 Agency Certification if the company shows readiness. Decision gate with the agency: 2026-12-31 (EV-041). FedRAMP applicability is decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-IT-R01) |
| Bank customers | The 14 community banks buy hosting and managed services that support their operations. The company treats these as covered services under the Bank Service Company Act, as the banks' vendor contracts state, so it is a **bank service provider** (12 CFR 53.4, 225.303, 304.24), determined in the intake obligations register (C-IT-R05) from the bank vendor contracts (EV-040) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv). PHI: the MSA prohibits hosting protected health information and the company signs no business associate agreements. DoD CUI and covered defense information: the MSA prohibits it and no DFARS 252.204-7012 or CMMC clauses have been flowed down. Payment cards: customer billing uses the payment processor's hosted page. DOJ bulk data rule (28 CFR Part 202): no vendor, employment, or investment agreements give countries of concern or covered persons access to customer data; all staff and contractors are U.S.-based |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Chief Executive Officer (majority owner, Cris Santos) | Accepts High and Very High risks; signs agency and bank contracts; approves the FedRAMP investment decision |
| Chief Operating Officer (COO) | Executive owner of the security program; accepts Moderate risks; approves policies |
| IT Manager | Designated **Information Security Officer** (part-time); runs corporate IT, the identity provider, and the SIEM; coordinates compliance work |
| Director of Platform Engineering | Owns the private cloud: hypervisor clusters, storage, data center networks, and out-of-band management |
| Engineering Manager (Control Plane) | Owns the control plane, customer portal, public API, and CI/CD pipeline |
| NOC and Support Manager | 24x7 NOC; first responder for incidents; customer status communications |
| Managed Services Lead | Owns the RMM tool and managed services delivery |
| Controller | Vendor contracts, cyber insurance, billing |
| HR Manager | Onboarding, terminations, background checks, training records |
| Sales Director | Relationship owner for the bank customers and the prospective agency sponsor |
| FedRAMP advisor (contracted) | Advisory service for FedRAMP readiness, engaged 2026-07 (fedramp.gov recommends an advisor as step 1) |
| Outside counsel | Contract, breach, and government contracting advice |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds customer data? | Notes |
|---|---|---|---|---|
| SYS-01 | Customer portal and public API | Company-built; runs in SYS-04 | Yes (tenant metadata, customer credentials) | Customers order, start, stop, snapshot, and console into VMs; manage DNS; open tickets. MFA is optional for customers (EV-011) |
| SYS-02 | Control plane (orchestration services) | Company-built; runs in SYS-04 | Yes (tenant inventory, API credentials to SYS-06) | Provisioning engine, job queue, tenant database, metering. Holds service credentials that can act on every customer VM (EV-007) |
| SYS-03 | Workforce identity provider (SSO and MFA) | SaaS | No (identities only) | Hardware security keys for all 60 employees since 2025 (EV-001) |
| SYS-04 | Public cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts SYS-01, SYS-02, their databases, CI/CD build runners, and control-plane backups. Production and non-production share one account, separated only by network rules (EV-006) |
| SYS-05 | Private cloud platform | Company-owned hardware in DC-1 and DC-2 | Yes (customer VMs) | 96 hypervisor hosts in 4 clusters (3 at DC-1, 1 at DC-2) and 6 storage arrays. DC-2 holds replicas only for customers on the paid replication tier (about 30% of VMs) (EV-014, EV-017) |
| SYS-06 | Virtualization management and out-of-band management | Company-owned, DC-1 and DC-2 | Yes (full control of customer VMs) | Hypervisor managers and host baseboard management controllers (BMCs) on a management network |
| SYS-07 | Source code repository and CI/CD pipeline | SaaS code hosting plus build runners in SYS-04 | No (source code, VM templates, signing key) | Builds the control plane, portal, and the VM templates customers deploy |
| SYS-08 | Remote monitoring and management (RMM) tool | SaaS (RMM vendor) | Yes (agent access to customer servers) | Agents on about 1,900 customer servers; can run scripts on any of them (EV-010) |
| SYS-09 | Edge network and authoritative DNS | Company-owned routers and firewalls in DC-1 and DC-2; DDoS scrubbing service | Yes (customer DNS zones) | Two upstream carriers per site (EV-012) |
| SYS-10 | Ticketing, status page, and productivity suite | SaaS | Incidental | Customer tickets, email, chat, files |
| SYS-11 | Security monitoring (SIEM) with AI-assisted alert triage | SaaS (SIEM vendor) | Yes (logs) | Collects SYS-03, SYS-04, and endpoint logs. Not yet SYS-05, SYS-06, SYS-08, or SYS-09 logs (EV-021). The AI triage feature was enabled in April 2026 (EV-046; see P10) |
| SYS-12 | Endpoints | Company-managed | Cached | 64 laptops and 6 NOC workstations; endpoint detection and response (EDR) on all (EV-022) |
| SYS-13 | Billing and finance | SaaS | Customer contact and billing data | Card payments go through the processor's hosted page (EV-044) |

**SSP system (P02):** the *Hosting Control Plane and Customer Portal (HCP)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-06, SYS-07, and SYS-08, with the management interfaces of SYS-05 and SYS-09 and the supporting logging in SYS-11.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the FedRAMP Rev5 Class C rules and the bank service provider rule** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | FedRAMP does **not** yet apply (no federal customer). P03 is a **FedRAMP Rev5 Class C readiness gap analysis** (Class C is the class FedRAMP aligns with Moderate), done because the company is pursuing its first agency sponsor. Secondary regulation: the bank service provider notification rule (12 CFR 53.4; 225.303; 304.24), which applies today |
| P08 incident | Compromise of provider tooling affecting downstream customers: an attacker uses a stolen RMM technician session to push a malicious script to managed customer servers |
| P09 SOC 2 | Real SOC 2 readiness assessment (the company is a service organization). Security, Availability, and Confidentiality. Requested by the bank customers and two enterprise prospects. Target: Type 1 as of 2027-03-31, then a Type 2 period 2027-04-01 to 2027-09-30. Includes a review of the DC-1 colocation provider's SOC 2 Type 2 report (carved-out subservice organization) |
| P10 AI | AI-assisted alert triage in the SIEM (vendor feature) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, exports, inventories, obligations register |
| 2026-07-13 to 2026-07-31 | BIA interviews, risk assessment and FedRAMP readiness gap analysis fieldwork, with the FedRAMP advisor |
| 2026-08-03 to 2026-08-07 | Policies drafted from the gaps |
| 2026-08-10 to 2026-08-21 | Control assessment fieldwork (DC-1 walkthrough 2026-08-12; DC-2 visit 2026-08-18): operating tests of controls already in place; design review of the draft policies |
| 2026-08-24 to 2026-09-04 | SOC 2 readiness self-assessment and AI risk assessment |
| 2026-09-25 | Deliverables and policies approved by the COO (Moderate and below) and the CEO (High) |
| 2027-01 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These details were added during the build and are used consistently across P02 to P10.
- **Bank contacts:** designated points of contact are on file for 9 of the 14 banks, last verified in 2023 (EV-055; P03 G-227; POAM-019).
- **Incident history:** 3 security incidents were handled ad hoc in 2025-2026, one of them a compromised customer VM rebuilt from a clean template (EV-028; P07 IR-4).
- **SIEM volume:** about 9,800 alerts in July 2026, 71% auto-closed by the AI triage feature without review (EV-AU-6; P10).
- **RMM tool:** the vendor keeps audit logs for 90 days by default; the contract has no security or incident notice terms (EV-010, EV-037; P08; POAM-020).
- **Contract engineers:** 2 contract engineers work alongside the 60 employees (EV-001, EV-037; P03 PS-7; P10 fairness groups).
- **DC-1 colocation report:** SOC 2 Type 2 (Security and Availability), period 2025-07-01 to 2026-06-30, unqualified, received 2026-08-07 (EV-057) and reviewed 2026-09-02 by the Controller and the IT Manager (P09).
- **AI-002:** an enterprise coding assistant is in pilot with 4 software engineers (EV-036, EV-046; P10).
- **Assessment scope:** the P07 mock assessment covered 22 controls with a contracted independent assessor who is not the FedRAMP advisor.
