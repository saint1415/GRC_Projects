# System Security Plan: Hosting Control Plane and Customer Portal (HCP)

**Organization:** Cris Santos Company, LLC (cloud hosting and managed infrastructure provider) | **Tier:** Small | **Vertical:** Information Technology
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-25
**Control baseline:** FedRAMP Rev5 Class C control list (FedRAMP Consolidated Rules for 2026, rule FRC-CSF-BSL), used as a readiness target. See P03 for why FedRAMP does not yet apply.

## 1. System Name and Identifier
Hosting Control Plane and Customer Portal (**HCP**), identifier CSC-SYS-001.

## 2. System Overview
The HCP is the set of systems that lets the company sell, run, and manage its three service lines: managed private cloud, managed services, and authoritative DNS and edge services. Customers use it to order, start, stop, snapshot, and console into their virtual machines (VMs), manage DNS zones, and open tickets. Company engineers use its management layer to run the hypervisor clusters and to reach managed customer servers.

**Users:**
- About 2,600 customer user accounts from about 430 business customers, including 14 community banks.
- 60 employees. Privileged users are the 12 platform engineers, 10 software engineers, 6 managed services engineers, 2 IT staff, and the NOC's 16 staff (limited operator rights).

**Major components** (IDs from `../00_company-facts.md` section 3):
- **SYS-01:** customer portal and public API (company-built)
- **SYS-02:** control plane orchestration services: provisioning engine, job queue, tenant database, metering
- **SYS-03:** workforce identity provider (SaaS) with hardware security keys
- **SYS-04:** public cloud tenant (IaaS/PaaS) hosting SYS-01, SYS-02, build runners, and control plane backups
- **SYS-06:** hypervisor managers and host baseboard management controllers (BMCs) on the management network at DC-1 and DC-2
- **SYS-07:** source code repository (SaaS) and CI/CD pipeline, which also builds and signs the VM templates customers deploy
- **SYS-08:** remote monitoring and management (RMM) tool (SaaS), with agents on about 1,900 customer servers
- The **management interfaces** of SYS-05 (96 hypervisor hosts, 6 storage arrays) and SYS-09 (routers, firewalls, authoritative DNS)
- The **logging** in SYS-11 (SaaS SIEM with AI-assisted alert triage) that supports the components above

The public cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | Status for the HCP |
|---|---|---|---|
| C-IT-R01 | FedRAMP | 44 U.S.C. 3607-3616; FedRAMP Consolidated Rules for 2026 | **Readiness target, not yet applicable.** No federal agency uses the service today. The company is preparing for a Rev5 Class C Agency Certification with a prospective agency sponsor (P03) |
| C-IT-R05 | Bank service provider notification rule | 12 CFR 53.4 (OCC); 12 CFR 225.303 (FRB); 12 CFR 304.24 (FDIC) | **Applies.** The company performs covered services for 14 community banks (P08) |
| C-IT-R06 | CIRCIA (pending rule) | 6 U.S.C. 681b; proposed 6 CFR Part 226 | Not in force. No final rule as of 2026-09-25. Tracked only |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2) (reasonable measures) and 501.171(6) (third-party agent notice to the covered entity within 10 days) | **Applies** when the company maintains or processes customers' personal information on their behalf |
| Contract | Master services agreement (MSA) | Availability (99.95% private cloud, 99.9% portal); confidentiality; incident notice within 72 hours of confirmation | Applies to every customer |
| Internal | Security policies POL-01 to POL-05 | P06 | Approved 2026-09-25 |

**Not applicable, with reasons:**
- **C-IT-R02 (CMMC) and C-IT-R03 (DFARS 252.204-7012):** the MSA prohibits covered defense information and CUI, and no DoD contract clauses have been flowed down to the company.
- **C-IT-R04 (DOJ Data Security Program, 28 CFR Part 202):** no vendor, employment, or investment agreement gives a country of concern or covered person access to customer data, and all staff and contractors are U.S.-based. The Controller rechecks this at each new vendor contract.
- **HIPAA:** the MSA prohibits PHI and the company signs no business associate agreements.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer on 2026-09-25.

### 4.2 System Authorization Decision
There is no federal authorization. FedRAMP Rev5 Agency Certification would require the sponsoring agency to issue an Authorization to Operate first (FRC-APS-ATO). The equivalent internal decision:
- The COO accepted continued operation of the HCP on 2026-09-25, with the conditions in the P07 POA&M.
- The CEO accepted the Very High and High risks in P01 on 2026-09-25, each with a dated treatment plan. R-001 (RMM compromise) is accepted only until its first milestone on 2026-10-15.

### 4.3 System Operational Status
**Operational.** Major modifications planned:
- Separate production cloud account and separate backup account (P01 R-002, R-004), due 2026-12-31 to 2027-02-28
- Federation of hypervisor managers to the identity provider (R-003), due 2026-12-31
- SIEM onboarding of management-plane logs (R-015), due 2027-01-31

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Overall accountability; accepts Moderate risks |
| Risk acceptor (authorizing official equivalent) | Chief Executive Officer | Accepts High and Very High risks; signs agency and bank contracts |
| Information Security Officer | IT Manager (part-time) | Day-to-day security, SIEM, identity provider, this plan |
| Technical owner: portal, control plane, cloud tenant, CI/CD | Engineering Manager (Control Plane) | SYS-01, SYS-02, SYS-04, SYS-07 |
| Technical owner: hypervisor, BMC, and network management | Director of Platform Engineering | SYS-05, SYS-06, and SYS-09 management interfaces |
| Technical owner: RMM | Managed Services Lead | SYS-08 |
| Operations and first response | NOC and Support Manager | 24x7 monitoring, incident intake, customer and bank notices |
| Readiness support | FedRAMP advisor (contracted) | Advises on FedRAMP rules. Not an independent assessor |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 and adjusted for a hosting provider. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Hosted customer data (VM contents, customer DNS zones) | Moderate | Moderate | Moderate | The MSA prohibits PHI, CUI, and payment card data, so tenants hold business data up to Moderate. The prospective agency application is Moderate |
| IT infrastructure management (tenant inventory, service credentials, VM templates, hypervisor configuration) | Moderate | Moderate | Moderate | Service credentials and templates can affect every customer at once. That aggregation is rated Very High impact in the risk register (P01) but does not change the FIPS 199 level |
| Information security (audit logs, SIEM alerts, vulnerability data) | Moderate | Moderate | Low | Needed for investigations; a SIEM outage is tolerable for 24 hours (P05 BP-07) |
| Customer account and billing contact data | Moderate | Low | Low | Personal contact data of customer staff |
| **HCP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Availability:** Moderate. The BIA (P05) sets a 4-hour MTD for hosting and 2 hours for DNS, driven by SLA credits and the bank notification threshold. These outages cause serious, not severe or catastrophic, harm to customers.

**Baseline:** the FedRAMP Rev5 Class C control list, which FedRAMP aligns with Moderate. It contains **180 base controls and 142 enhancements**. 176 of the base controls are in the NIST SP 800-53B Moderate baseline. Four (CA-8, IR-9, SC-45, SI-6) are FedRAMP additions. The Moderate baseline control CA-5 is not in the Class C list; the company keeps a POA&M anyway (P07). Every base control is documented in `control-implementation.csv`, with enhancements recorded in the base control's row.

## 7. Authorization Boundary Description
**Inside the boundary:**
- The customer portal, public API, and control plane services, and their databases, build runners, and backups in the public cloud tenant
- The workforce identity provider tenant configuration
- The code repository and CI/CD pipeline, including the VM template signing key
- The RMM tool tenant and its technician accounts
- Hypervisor managers, host BMCs, the management network, and the bastion host at DC-1 and DC-2
- The management interfaces of the hypervisor hosts, storage arrays, routers, firewalls, and authoritative DNS
- The SIEM tenant for the log sources above
- 64 laptops and 6 NOC workstations used by privileged staff

**Outside the boundary (interconnected or supporting):**
- Customer VMs and customer servers reached through the RMM tool. These are customer systems. The company is responsible for the platform and the tools that reach them, not for customers' guest operating systems (P04 section 5)
- Colocation facilities (physical controls inherited, P09 vendor review)
- The public cloud provider's infrastructure below the tenant, the SaaS vendors' platforms, the DDoS scrubbing service, and upstream carriers
- Billing (SYS-13), the productivity suite and ticketing (SYS-10), and HR and payroll systems

**Federal tenants (future):** a Class C certification would require the company to identify all information resources likely to handle federal customer data, including metadata, and to document information flows and third-party resources (MAS-CSO-IIR, MAS-CSO-FLO, MAS-CSO-TPR, MAS-CSO-MDI). That work is in the P03 roadmap.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Customers (portal and public API) | Bidirectional | Orders, VM actions, DNS changes, tickets, console sessions | MSA and acceptable use terms |
| Customer servers (RMM agents) | Bidirectional | Monitoring data, patch jobs, scripts | Managed services addendum. **No script-approval terms (gap)** |
| Bank customers | Outbound notices | Incident notices under 12 CFR 53.4 | Bank vendor contracts. **Bank-designated contacts not current (gap)** |
| Public cloud provider | Hosting | All HCP workloads and backups | Provider customer agreement |
| RMM vendor | Hosting | Technician sessions, agent commands, audit logs | Vendor terms. **No security or incident notice terms (gap)** |
| SIEM vendor | Inbound logs | Identity, cloud, and endpoint logs | Vendor terms; 90-day retention |
| Code hosting vendor | Hosting | Source code, pipeline definitions | Vendor terms |
| DDoS scrubbing service | Bidirectional | Customer traffic during mitigation; secondary DNS | Service contract |
| Colocation providers | Physical hosting; cross-connects | None (physical) | Colocation contracts with SOC 2 Type 2 reports |
| Status page provider | Outbound | Service status | Vendor terms |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Customer portal and public API (SYS-01) | Company-built web application | Public cloud tenant | Engineering Manager (Control Plane) |
| Control plane services and tenant database (SYS-02) | Containers and managed database | Public cloud tenant | Engineering Manager (Control Plane) |
| Build runners and control plane backups | Virtual machines and object storage | Public cloud tenant (same account and region as production, **gap**) | Engineering Manager (Control Plane) |
| Workforce identity provider (SYS-03) | SaaS | Identity vendor | IT Manager |
| Code repository and CI/CD pipeline (SYS-07) | SaaS plus runners | Code hosting vendor; cloud tenant | Engineering Manager (Control Plane) |
| RMM tool tenant (SYS-08) | SaaS | RMM vendor | Managed Services Lead |
| Hypervisor managers (4 clusters) and bastion host (SYS-06) | Virtual appliances | DC-1 and DC-2 management network | Director of Platform Engineering |
| Host BMCs (96) | Firmware interfaces | DC-1 and DC-2 management network | Director of Platform Engineering |
| Storage array management (6 arrays) | Appliance interfaces | DC-1 and DC-2 | Director of Platform Engineering |
| Routers, firewalls, and authoritative DNS servers (SYS-09) | Network appliances and servers | DC-1, DC-2, and the scrubbing service (secondary DNS) | Director of Platform Engineering |
| SIEM tenant (SYS-11) | SaaS | SIEM vendor | IT Manager |
| Laptops (64) and NOC workstations (6) (SYS-12) | Endpoints with EDR and full-disk encryption | Florida HQ and remote | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of the 180 Class C base controls:
- Implemented: 38
- Partially implemented: 99
- Planned: 40
- Not applicable: 3 (AC-18, PE-5, SC-15; no wireless networks, output devices, or collaborative computing devices inside the boundary)

By inheritance: 148 system-specific, 24 hybrid, and 8 common (inherited from the colocation providers for facility power, fire, environment, and visitor controls).

The control statements are the same evidence base as the FedRAMP readiness gap analysis (P03). Status mapping: Met = Implemented, Partially met = Partially implemented, Not met = Planned.

**FedRAMP parameters:** organization-defined parameters are not yet assigned following FedRAMP Rev5 Controls Guidance (FRC-CSF-ACP). This plan will be converted into a FedRAMP Security Decision Record in human-readable and JSON form before any application (SDR-CSO-FRR; P03 roadmap).

### 10.2 Control assessment status
An independent assessor ran a mock control assessment of 22 controls from 2026-08-10 to 2026-08-21 (P07). Results are in P07 `assessment-results.csv`; weaknesses are tracked in P07 `poam.csv` (21 items). The assessor was not the FedRAMP advisor and was not involved in operating the controls. This was not a FedRAMP independent assessment; a FedRAMP Recognized independent assessment service would be engaged after the sponsor decision (P03).

## 11. Digital Identity Acceptance Statement
Assurance levels follow NIST SP 800-63.
- **Workforce (all 60 staff):** single sign-on with hardware security keys, which are phishing-resistant, hardware-based authenticators. This meets the intent of authenticator assurance level 3 for privileged users. **Gap:** hypervisor managers and BMCs use local accounts with shared root credentials and no MFA (P01 R-003; POAM-003). Target: federation to the identity provider or bastion-only access with MFA by 2026-12-31.
- **Customer users:** password with optional MFA; 38% of customer administrators have enrolled. Customers can delete VMs and change DNS, so the target is authenticator assurance level 2 for customer administrator roles (required MFA) by 2027-01-31 (R-007).
- **Identity proofing:** workforce identities are verified by HR at hire with background checks. Customer administrators are not proofed today. The target is address or account confirmation for new customer administrators. Agency users would be proofed by their agency and would sign in with federal credentials (IA-2(12), IA-8(1); planned).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), risk register (P01), FedRAMP readiness gap analysis (P03), cloud control map and diagram (P04), BIA (P05), policies POL-01 to POL-05 (P06), control assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness (P09), AI risk assessment for SIEM triage (P10).

## 13. Acronym List and Glossary
- **API:** application programming interface
- **ATO:** authorization to operate (issued by a federal agency)
- **BMC:** baseboard management controller (out-of-band hardware management interface)
- **CI/CD:** continuous integration and continuous delivery
- **EDR:** endpoint detection and response
- **HCP:** Hosting Control Plane and Customer Portal
- **HSM:** hardware security module
- **MSA:** master services agreement
- **NOC:** network operations center
- **POA&M:** plan of action and milestones
- **RMM:** remote monitoring and management
- **SDR:** Security Decision Record (FedRAMP's machine-readable security plan format under the 2026 rules)
- **SIEM:** security information and event management
- **VM:** virtual machine

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.1 | 2026-07-31 | Draft from the FedRAMP readiness fieldwork | IT Manager |
| 1.0 | 2026-09-25 | Updated for P06 policy approvals and P07 results; approved | IT Manager |
