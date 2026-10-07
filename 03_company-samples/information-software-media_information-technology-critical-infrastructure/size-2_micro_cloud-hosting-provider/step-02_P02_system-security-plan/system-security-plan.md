# System Security Plan: Hosting Control Plane and Customer Portal (HCP)

**Organization:** Cris Santos Company, LLC (managed cloud hosting provider) | **Tier:** Micro | **Vertical:** Information Technology
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Hosting Control Plane and Customer Portal (**HCP**), identifier CSC-SYS-001.

## 2. System Overview
The HCP is everything the company uses to run and reach customer workloads. Customers use it to order, start, stop, and reboot their virtual machines (VMs), open the VM console, manage tickets, and pay invoices. Company engineers use its management layer to run the hypervisor cluster, back up VMs, change customer DNS zones, and patch managed customer servers through the RMM tool.

**Users:**
- About 180 customer portal users from about 70 business customers, including 2 community banks. 72 are customer administrators.
- 7 employees. Privileged users are the Lead Systems Engineer, the 2 Systems Engineers, the 2 Support Engineers (portal and RMM technician rights), and the Owner (standing administrator, see section 10).

At this size the "control plane" is not company-built code. It is a commercial hosting automation and billing product, the hypervisor manager, and a SaaS RMM tool, held together by service accounts. Most of the platform underneath belongs to vendors: the colocation provider, the public cloud provider, and the SaaS vendors. For each control, this plan says what the company does itself, what an outside provider does for it, and what it inherits.

**Major components** (IDs from `../00_company-facts.md` section 3):
- **SYS-01:** customer portal and billing (commercial software on one cloud VM)
- **SYS-02:** hypervisor manager and host baseboard management controllers (BMCs) on the DC-1 management network
- **SYS-03 (management interfaces only):** 6 hypervisor hosts, 1 storage array, 2 switches, 2 firewalls, 1 backup appliance
- **SYS-04:** public cloud tenant (IaaS) with the portal VM, its managed database, and the off-site backup copy
- **SYS-05:** backup service (backup appliance at DC-1 with a nightly cloud copy)
- **SYS-06:** RMM tool (SaaS), with agents on about 310 customer servers
- **SYS-07:** workforce identity provider and productivity suite (SaaS)
- **SYS-08 (administration only):** the company's account at the SaaS DNS provider
- **SYS-09:** PSA ticketing and documentation vault (SaaS)
- **SYS-10:** 9 company laptops used for administration
- **SYS-11 (supporting):** the MDR provider's monitoring platform

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | Status for the HCP |
|---|---|---|---|
| C-IT-R05 | Bank service provider notification rule | 12 CFR 53.4 (OCC, for Bank A); 12 CFR 304.24 (FDIC, for Bank B); 12 CFR 225.303 (FRB, same text, no FRB-supervised customer today) | **Applies.** The company performs covered services for 2 banks (P03, P08) |
| Contract | Interagency Guidelines Establishing Information Security Standards, flowed down by both bank contracts | 12 CFR Part 30, App. B and Supplement A (OCC); 12 CFR Part 364, App. B (FDIC); III.D.2 requires banks to bind service providers by contract | **Applies by contract.** Bank examiners can also review the company's services under 12 U.S.C. 1867(c). Cited in the control table as "Interagency Guidelines" with the paragraph number |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2) (reasonable measures), (6) (third-party agent notice within 10 days), (8) (disposal) | **Applies** when the company maintains or processes customers' personal information, as it does for Bank A |
| Contract | Master services agreement (MSA) | 99.9% monthly availability; confidentiality; incident notice within 72 hours of confirmation | Applies to every customer |
| C-IT-R06 | CIRCIA (pending rule) | 6 U.S.C. 681b; proposed 6 CFR Part 226 | Not in force. No final rule as of 2026-09-25. Tracked only |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | Approved 2026-09-15, effective 2026-10-01 |

**Not applicable, with reasons:**
- **C-IT-R01 (FedRAMP):** no federal agency uses the service, and the Owner declined the only federal inquiry (P03 section 1).
- **C-IT-R02 (CMMC) and C-IT-R03 (DFARS 252.204-7012):** the MSA prohibits CUI and covered defense information, and no DoD clauses have been flowed down.
- **C-IT-R04 (DOJ Data Security Program, 28 CFR Part 202):** no covered data transaction with a country of concern or covered person. The Operations Manager rechecks at each new vendor contract.
- **HIPAA:** the MSA prohibits PHI and the company signs no business associate agreements.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner on 2026-09-15.

### 4.2 System Authorization Decision
There is no federal authorization. The equivalent internal decision: on 2026-09-15 the Owner accepted continued operation of the HCP, on the condition that the POA&M items in P07 close by their dates and the Very High and High risks in P01 follow their dated treatment plans. R-001 (RMM compromise) is tolerated only until its first milestone on 2026-10-15 (shared RMM accounts removed).

### 4.3 System Operational Status
**Operational.** Planned changes:
- Named RMM accounts with sign-in restrictions and two-person script approval (P01 R-001), due 2026-11-30
- Immutable backup copy in a separate cloud account (R-002), due 2026-12-31
- Named, MFA-protected hypervisor and BMC administration (R-003), due 2026-12-31
- Degraded-mode recovery into the cloud tenant for a DC-1 loss (R-009), tested by 2027-05-31

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner | Overall accountability; accepts Moderate, High, and Very High risks with a treatment plan; approves this plan, policies, and spending |
| Information Security Lead | Lead Systems Engineer (about 20% of the role) | Day-to-day security; maintains this plan and the risk register; owns the cluster, network, VPN, identity provider, and the MDR relationship |
| Compliance Coordinator | Operations Manager | Policies, vendor contracts, bank contact lists, customer notices, training records, onboarding and terminations |
| Technical owners | Systems Engineers | Backup service, cloud tenant, portal, DNS, RMM scripts |
| Support desk and first response | Support Engineers | Customer requests, portal administration, routine RMM patching |
| Outside monitoring | MDR provider | 24x7 monitoring of laptops, identity provider, and firewalls; first-line containment on laptops and identity accounts |
| Independent assessor | IT security consultant | Yearly control assessment (P07) |

**Overlap.** The Lead Systems Engineer runs the systems and also judges their security. That is normal at 7 people. The checks on that overlap are the MDR's independent view of activity, the independent consultant's yearly assessment, the Owner's monthly review of the security report, and two-person approval for the riskiest actions once POAM-004 and POAM-006 close.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 and adjusted for a hosting provider. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Hosted customer data (VM contents, including Bank A's loan documents; customer DNS zones) | Moderate | Moderate | Moderate | The MSA prohibits PHI, CUI, and card data. Bank customer information is nonpublic personal information; disclosure would cause serious harm to the bank and its customers |
| IT infrastructure management (hypervisor and RMM credentials, customer server passwords, configurations) | Moderate | Moderate | Moderate | One stolen credential can affect every customer at once. That concentration is rated Very High impact in the risk register (P01) but does not change the FIPS 199 level |
| Information security (logs, MDR alerts) | Moderate | Moderate | Low | Needed for investigations; a day without monitoring is tolerable (P05 BP-07) |
| Customer account and billing contacts | Moderate | Low | Low | Personal contact data of customer staff |
| **HCP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Availability is Moderate.** The BIA (P05) sets a 4-hour MTD for hosting and DNS, driven by SLA credits and the bank 4-hour notice test. An outage causes serious, not severe, harm to customers.

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person provider. The plan documents **46 controls** that carry the bank contract measures, the bank notice rule, and basic cyber hygiene (`control-implementation.csv`). Other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the colocation provider (facility power, fire, environment, visitors), the public cloud provider (infrastructure below the tenant), and the SaaS vendors (their platforms), with the colocation SOC 2 report as the main evidence (P09).
- **Tailored out** at this tier where the control assumes a federal program or a larger staff (for example, a configuration control board or a separate development environment). These are tailoring decisions, not gaps.

## 7. Authorization Boundary Description
**Inside the boundary:**
- The customer portal VM, its database, and the backup copy in the cloud tenant
- The hypervisor manager, BMCs, management network, VPN, and the management interfaces of the hosts, storage array, switches, firewalls, and backup appliance at DC-1
- The company's RMM tenant and its technician accounts, the DNS provider account, the PSA tenant and vault, and the identity provider tenant
- The 9 company laptops

**Outside the boundary (interconnected or supporting):**
- **Customer VMs and customer servers.** These are customer systems. The company runs the platform and the tools that reach them, not the guest operating systems (P04 section 2).
- The colocation facility (physical controls inherited), the public cloud provider's infrastructure below the tenant, the SaaS vendors' platforms, and the MDR provider's platform (SYS-11)
- Payroll, the payment processor's hosted page, and the colocation provider's remote hands

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Customers (portal and API) | Bidirectional | Orders, VM actions, console sessions, tickets, invoices | MSA |
| Customer servers (RMM agents) | Bidirectional | Monitoring data, patch jobs, scripts | Managed services addendum. **No script-approval terms (gap)** |
| Bank A and Bank B | Outbound notices; inbound due diligence questionnaires | Incident notices (12 CFR 53.4); security answers | Bank vendor contracts with a security exhibit. **Bank-designated contacts not current (gap)** |
| Public cloud provider | Hosting | Portal, database, backup copy | Provider customer agreement |
| RMM vendor | Hosting | Technician sessions, agent commands, audit logs | Vendor terms. **No incident notice terms (gap)** |
| MDR provider | Inbound logs; outbound escalations and automated actions | EDR, identity, and firewall events | MDR contract; 12-month log retention. **Telemetry-use clause under review (P10)** |
| SaaS DNS provider | Hosting | Customer zones | Reseller terms |
| Colocation provider | Physical hosting; remote hands | None (physical) | Colocation contract with a SOC 2 Type 2 report |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Customer portal and billing (SYS-01) | Commercial web application on a VM | Public cloud tenant | Systems Engineer |
| Portal database and backup copy (SYS-04) | Managed database and object storage | Public cloud tenant (same account, **gap**) | Systems Engineer |
| Hypervisor manager and 6 host BMCs (SYS-02) | Virtual appliance and firmware interfaces | DC-1 management network | Lead Systems Engineer |
| Storage array, 2 switches, 2 firewalls (SYS-03) | Appliances | DC-1, 2 racks | Lead Systems Engineer |
| Backup appliance (SYS-05) | Appliance with backup software | DC-1 management network | Systems Engineer |
| RMM tenant (SYS-06) | SaaS | RMM vendor | Lead Systems Engineer |
| Identity provider and suite (SYS-07) | SaaS | Identity and suite vendor | Lead Systems Engineer |
| DNS provider account (SYS-08) | SaaS | DNS provider | Systems Engineer |
| PSA and documentation vault (SYS-09) | SaaS | PSA vendor | Operations Manager |
| Laptops (9) (SYS-10) | Endpoints with EDR and full-disk encryption | Office and home | Lead Systems Engineer |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 46 controls:
- Implemented: 10
- Partially implemented: 28
- Planned: 8
- Not applicable: 0

By responsibility: 21 system-specific (the company), 24 hybrid (the company with a vendor or the MDR provider), and 1 common/inherited (PE-3, from the colocation provider).

### 10.2 Inherited and provider-supplied controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Colocation provider | Physical entry, cameras, visitors (PE-3); power, cooling, fire suppression; upstream DDoS filtering (SC-5) | SOC 2 Type 2 report reviewed 2026-08-26 (P09) | Complementary user entity controls: keep the authorized-person list current (PE-2), lock its racks, review the access report |
| Public cloud provider | Infrastructure security below the tenant; encryption of storage and the managed database by default (SC-28) | Provider's published shared responsibility model and its audit reports | Account and role setup, MFA, logging retention, backup immutability, network rules |
| MDR provider | 24x7 monitoring and first containment on laptops and identity (SI-3, SI-4, IR-4) | MDR contract; monthly MDR report | Add missing log sources; review what the AI triage closes (P10); act on escalations |
| RMM, PSA, DNS, identity vendors | Platform security, sign-in, lockout, MFA features (AC-7, IA-2(1)) | Vendor documentation; no reports reviewed yet (POAM-012) | Named accounts, roles, MFA settings, log export, contract terms |

**Inherited does not mean done.** The colocation report expects the company to keep its authorized-person list current. The company did not, so a former employee stayed on the list for five months (PE-2; P07 AC-2 finding).

### 10.3 Control assessment status
Assessed 2026-08-17 to 2026-08-19 by an independent IT security consultant. Results are in P07 `assessment-results.csv`; weaknesses are tracked in P07 `poam.csv`.

## 11. Digital Identity Acceptance Statement
Assurance levels follow NIST SP 800-63.
- **Workforce:** named identity provider accounts with push-approval MFA for the suite, PSA, MDR console, and VPN. That is a multi-factor authenticator but not a phishing-resistant one. **Gaps:** shared RMM support accounts, a shared hypervisor administrator account, and no MFA at the hypervisor and BMC layer (P01 R-001, R-003). Target: hardware security keys for all 7 staff and named, MFA-protected administration of every system by 2026-12-31.
- **Customer users:** password with optional MFA; 15 of 72 customer administrators have enrolled. Customer administrators can delete VMs, so the target is required MFA for customer administrator roles by 2027-01-31 (R-005), and a call-back check before the support desk resets a password or opens a console.
- **Identity proofing:** workforce identities are verified by the Operations Manager at hire with background checks. New customer administrators are confirmed by the account owner named in the customer's contract.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), regulatory gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and colocation report review (P09), AI risk assessment (P10).

## 13. Acronym List and Glossary
- **BMC:** baseboard management controller (out-of-band hardware management interface)
- **EDR:** endpoint detection and response
- **HCP:** Hosting Control Plane and Customer Portal
- **MDR:** managed detection and response
- **MSA:** master services agreement
- **POA&M:** plan of action and milestones
- **PSA:** professional services automation (ticketing and documentation)
- **RMM:** remote monitoring and management
- **VM:** virtual machine

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.1 | 2026-07-31 | Draft from the gap analysis fieldwork | Lead Systems Engineer |
| 1.0 | 2026-09-15 | Updated for P06 policies and P07 results; approved | Lead Systems Engineer |
