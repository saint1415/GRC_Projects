# Scenario facts: Cris Santos Company | Information Technology | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation, a standard, or a government program page, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (cloud hosting and managed infrastructure provider) |
| Business | Cloud hosting and managed infrastructure (NAICS 518210). Three service lines: (1) **managed private cloud**: customer virtual machines on company-owned hypervisor clusters in two leased colocation facilities; (2) **managed services**: patching, monitoring, and backup for customer servers, performed remotely through a remote monitoring and management (RMM) tool; (3) **authoritative DNS and edge services** bundled with hosting |
| Location | Headquarters and 24x7 network operations center (NOC) in Florida. **DC-1**: primary colocation facility in Florida. **DC-2**: secondary colocation facility about 450 miles away in another state |
| Workforce | 60 employees: 6 executive and administration, 8 sales and account management, 16 NOC and customer support, 12 platform engineering, 10 software engineering (control plane and portal), 6 managed services engineers, 2 IT (IT Manager and one IT specialist) |
| Customers | About 430 business customers (software companies, e-commerce firms, professional services firms, manufacturers). Includes **14 community banks**. About 2,300 customer virtual machines; 58 managed services customers with about 1,900 customer servers reached through the RMM tool; about 2,600 customer user accounts in the customer portal |
| Revenue | $24.0 million a year (fictional). Under the SBA standard of $40.0 million for NAICS 518210 (13 CFR 121.201), so SBA-small |
| Service commitments | Master services agreement (MSA): 99.95% monthly availability for the private cloud and 99.9% for the portal; customer data confidentiality clause; security incident notice to customers "without undue delay and within 72 hours of confirmation" |
| Federal status | **No federal customer today.** A civilian federal agency program office sent a letter of interest in May 2026 to host a Moderate-impact case management application on the managed private cloud, and would act as agency sponsor for a FedRAMP Rev5 Agency Certification if the company shows readiness. Decision gate with the agency: 2026-12-31 |
| Bank customers | The 14 community banks buy hosting and managed services that support their operations. The company treats these as covered services under the Bank Service Company Act, as the banks' vendor contracts state, so it is a **bank service provider** (12 CFR 53.4, 225.303, 304.24) |
| Not in scope | PHI: the MSA prohibits hosting protected health information and the company signs no business associate agreements. DoD CUI and covered defense information: the MSA prohibits it and no DFARS 252.204-7012 or CMMC clauses have been flowed down. Payment cards: customer billing uses the payment processor's hosted page. DOJ bulk data rule (28 CFR Part 202): no vendor, employment, or investment agreements give countries of concern or covered persons access to customer data; all staff and contractors are U.S.-based |
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

| ID | System | Hosting | Holds customer data? | Notes |
|---|---|---|---|---|
| SYS-01 | Customer portal and public API | Company-built; runs in SYS-04 | Yes (tenant metadata, customer credentials) | Customers order, start, stop, snapshot, and console into VMs; manage DNS; open tickets. MFA is optional for customers |
| SYS-02 | Control plane (orchestration services) | Company-built; runs in SYS-04 | Yes (tenant inventory, API credentials to SYS-06) | Provisioning engine, job queue, tenant database, metering. Holds service credentials that can act on every customer VM |
| SYS-03 | Workforce identity provider (SSO and MFA) | SaaS | No (identities only) | Hardware security keys for all 60 employees since 2025 |
| SYS-04 | Public cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts SYS-01, SYS-02, their databases, CI/CD build runners, and control-plane backups. Production and non-production share one account, separated only by network rules |
| SYS-05 | Private cloud platform | Company-owned hardware in DC-1 and DC-2 | Yes (customer VMs) | 96 hypervisor hosts in 4 clusters (3 at DC-1, 1 at DC-2) and 6 storage arrays. DC-2 holds replicas only for customers on the paid replication tier (about 30% of VMs) |
| SYS-06 | Virtualization management and out-of-band management | Company-owned, DC-1 and DC-2 | Yes (full control of customer VMs) | Hypervisor managers and host baseboard management controllers (BMCs) on a management network |
| SYS-07 | Source code repository and CI/CD pipeline | SaaS code hosting plus build runners in SYS-04 | No (source code, VM templates, signing key) | Builds the control plane, portal, and the VM templates customers deploy |
| SYS-08 | Remote monitoring and management (RMM) tool | SaaS (RMM vendor) | Yes (agent access to customer servers) | Agents on about 1,900 customer servers; can run scripts on any of them |
| SYS-09 | Edge network and authoritative DNS | Company-owned routers and firewalls in DC-1 and DC-2; DDoS scrubbing service | Yes (customer DNS zones) | Two upstream carriers per site |
| SYS-10 | Ticketing, status page, and productivity suite | SaaS | Incidental | Customer tickets, email, chat, files |
| SYS-11 | Security monitoring (SIEM) with AI-assisted alert triage | SaaS (SIEM vendor) | Yes (logs) | Collects SYS-03, SYS-04, and endpoint logs. Not yet SYS-05, SYS-06, SYS-08, or SYS-09 logs. The AI triage feature was enabled in April 2026 (see P10) |
| SYS-12 | Endpoints | Company-managed | Cached | 64 laptops and 6 NOC workstations; endpoint detection and response (EDR) on all |
| SYS-13 | Billing and finance | SaaS | Customer contact and billing data | Card payments go through the processor's hosted page |

**SSP system (P02):** the *Hosting Control Plane and Customer Portal (HCP)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-06, SYS-07, and SYS-08, with the management interfaces of SYS-05 and SYS-09 and the supporting logging in SYS-11.

## 4. Current security posture: partially compliant

**In place today:**
- Phishing-resistant MFA (hardware security keys) for all workforce SSO, the cloud console, the code repository, and the RMM tool's web console
- A bastion host with MFA as the path into the management network for hypervisor administration
- EDR and full-disk encryption on all laptops and NOC workstations
- 24x7 NOC availability monitoring of the platform and a public status page
- Infrastructure-as-code for SYS-04; pull-request review with one approver for control plane code
- Quarterly external vulnerability scans and an annual external penetration test of the portal and API (last: 2026-03)
- TLS 1.2 or higher on the portal, API, and all control plane connections
- Self-encrypting drives in the storage arrays
- Background checks for all hires; annual security awareness training
- Colocation providers with badge, biometric, and camera controls, each with a SOC 2 Type 2 report
- Nightly control plane database backups; paid VM replication to DC-2 for about 30% of customer VMs
- Cyber insurance with an incident response panel

**Missing or weak, found in the 2026 assessments:**
1. No documented risk assessment has ever been performed (the 2026 register in P01 is the first).
2. Security policies are unapproved 2022 drafts written to answer customer questionnaires.
3. The RMM tool has standing access to every managed customer server. Three shared RMM technician accounts exist, the console has no source-IP restriction, and script execution needs no second approval.
4. Hypervisor managers and host BMCs use local accounts. Shared root credentials sit in a password vault, there is no MFA at that layer, and the management network is reachable from the NOC network.
5. Hypervisor, BMC, network device, and RMM logs are not sent to the SIEM. SIEM retention is 90 days.
6. No authenticated vulnerability scanning of internal systems. One hypervisor cluster runs a release one major version behind, and BMC firmware is not patched on a schedule.
7. Change management for data center infrastructure is informal (no records, no approval step). Control plane hotfixes can bypass pull-request review.
8. Customer portal MFA is optional; 38% of customer administrator accounts use it.
9. Control plane backups sit in the same account and region as production, are not immutable, and have never been restore-tested. There is no control plane recovery runbook.
10. Customer VM volumes are not encrypted at rest by default, and nobody has documented which cryptographic modules protect customer data or whether they are FIPS 140 validated.
11. Access removal at termination takes up to 3 business days. No access reviews for the RMM tool, hypervisor managers, or the cloud tenant.
12. No written incident response plan. No customer or bank notification procedure, and no current list of bank-designated points of contact.
13. Vendor risk management is informal. The colocation SOC 2 reports were last reviewed in 2024, the RMM vendor's report has never been reviewed, and the VM template signing key is stored as a CI/CD pipeline secret, not in a hardware security module.
14. No role-based security training for privileged administrators and no insider threat awareness content.
15. Two BMC interfaces at DC-2 still had the manufacturer's default administrator account enabled (found during P07 testing).

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
| 2026-07-13 to 2026-07-31 | Risk assessment and FedRAMP readiness gap analysis fieldwork, with the FedRAMP advisor |
| 2026-08-10 to 2026-08-21 | Control assessment fieldwork (DC-1 walkthrough 2026-08-12; DC-2 visit 2026-08-18) |
| 2026-08-24 to 2026-09-04 | SOC 2 readiness self-assessment and AI risk assessment |
| 2026-09-25 | Deliverables approved by the COO (Moderate and below) and the CEO (High) |
