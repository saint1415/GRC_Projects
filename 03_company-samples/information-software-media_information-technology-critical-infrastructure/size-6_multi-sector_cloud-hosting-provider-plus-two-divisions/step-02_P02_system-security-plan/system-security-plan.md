# System Security Plan: Hosting Control Plane and Customer Portal (HCP)

**Organization:** Cris Santos Company Holdings, Inc., Cloud Hosting division (serving its customers and the Managed IT and Payment Processing divisions) | **Tier:** Multi-Sector | **Vertical:** Information Technology
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17
**Control baseline:** NIST SP 800-53B High baseline, tailored. The G1 partition is also the control plane of the FedRAMP Rev5 Class C Government Cloud offering; every Class C control in scope is covered here.

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **HCP**, the registry default, because it is both: it is the focus division's primary system, and it is the platform the other two divisions run on. The Payment Processing cardholder data environment and the corporate landing zone sit in SL-1 accounts, and the Managed IT DoD CUI enclave sits in a G1 tenant, all controlled through the HCP, and about 1,900 Managed IT engineers act on customer servers through the HCP partner-operator path. The HCP carries the group's top risk (P01 GR-01). Each other division keeps its own security documentation (the Payment Processing PCI DSS documentation for SYS-P1; the Managed IT system documentation for SYS-M1 and the SYS-M2 enclave SSP required by NIST SP 800-171 Rev. 2, 3.12.4), all inheriting from the same common control catalog.

## 1. System Name and Identifier
Hosting Control Plane and Customer Portal (**HCP**), identifier CSCH-SYS-H1. It corresponds to SYS-H1 in `../00_company-facts.md`, in two partitions: commercial (HCP-C, serving regions R1 to R5) and Government (HCP-G, serving region G1).

## 2. System Overview
The HCP is the set of services through which customers and operators create, change, and observe cloud resources. It supports:
- **SL-1 Commercial Cloud:** about 38,000 business customers and about 290,000 customer console identities, including about 260 banking organizations and about 900 health care customers under business associate agreements.
- **SL-2 Government Cloud (G1):** 27 federal agencies and about 140 defense industrial base (DIB) companies that store controlled unclassified information (CUI).
- **SL-3 Managed Hosting:** about 4,100 tenants operated by the Managed IT division through the partner-operator path.
- **The group itself:** the Payment Processing CDE (dedicated accounts in R1 and R3), the Managed IT ticketing and access broker, the SYS-M2 CUI enclave (a G1 tenant), and corporate landing-zone accounts.

**Users:**
- Customer users (through the console, the public API, and customer IAM).
- About 6,400 Cloud Hosting workforce members with HCP roles, of whom about 2,300 can request privileged access through PAM.
- About 1,900 Managed IT engineers with the partner-operator role.
- Agency administrators in G1, who sign in through agency federation.

**Major components:**
- **Console and public API:** web console, API gateway, and command-line endpoints (behind SYS-H4 DDoS protection).
- **Customer identity and access management:** tenant accounts, users, roles, policies, and API keys.
- **Policy engine:** authorizes every request against tenant policies.
- **Orchestration and provisioning:** schedulers, placement, and the job system that acts on SYS-H2 hosts and storage.
- **Run-command service:** executes customer-approved or operator commands inside customer virtual machines through the guest agent.
- **Support tooling:** case-linked, customer-approved access for support engineers.
- **Partner-operator access path:** federation for Managed IT engineers into managed-hosting tenants.
- **Metering capture:** usage records for billing.
- **Control plane data stores:** managed databases, queues, and the secrets store.
- **Management interfaces of SYS-H2:** hypervisor managers, BMC access through bastions.
- **Fleet automation of SYS-H3:** the guest-agent update service, which acts through the HCP job system.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the HCP |
|---|---|---|---|
| C-IT-R01 | FedRAMP | 44 U.S.C. 3607-3616; FedRAMP Consolidated Rules for 2026 | **Applies to the G1 partition.** G1 holds a Rev5 Class C certification (originally a legacy FedRAMP Moderate agency authorization, 2023-03-15). The 2026 rules must be followed to maintain it, on ruleset dates from 2026-12-07 to 2028-02-01 (P03) |
| C-IT-R03 | DFARS Safeguarding CDI and Cyber Incident Reporting | 48 CFR 252.204-7012(b)(2)(ii)(D) | **Applies by contract to G1.** DIB customers that store covered defense information must ensure their cloud provider meets security requirements equivalent to the FedRAMP Moderate baseline and complies with paragraphs (c) through (g) (incident reporting, malicious software, media preservation, access, damage assessment). A DFARS addendum flows this down to the Cloud Hosting division |
| C-IT-R05 | Bank service provider notification rule | 12 CFR 53.4 (OCC); 12 CFR 225.303 (FRB); 12 CFR 304.24 (FDIC) | **Applies.** About 260 banking organizations run covered services on SL-1 |
| C-IT-R04 | DOJ Data Security Program | 28 CFR Part 202 | **Applies.** G1 holds government-related data (no volume threshold), and SL-1 holds bulk U.S. sensitive personal data for customers. The issue is vendor screening (scenario gap 10) |
| C-IT-R06 | CIRCIA (pending rule) | 6 U.S.C. 681b; proposed 6 CFR Part 226 | Not in force. No final rule as of 2026-09-25. Tracked only |
| N54-R06 | HIPAA (as business associate) | 45 CFR 164.302-164.318, 164.410, 164.504(e) | **Applies** to the HIPAA-eligible SL-1 services offered under BAAs. The HCP can reach customer data (snapshots, run-command), so its safeguards are part of the division's business associate duties |
| N52-R03 and PCI DSS | FTC Safeguards Rule (for Payment Processing); PCI DSS v4.0.1 Requirements 12.8 and 12.9 (contractual) | 16 CFR 314.4(f) | The CDE relies on HCP controls, so the Cloud Hosting division is an **affiliate service provider** to Payment Processing. No intercompany agreement carries these terms yet (scenario gap 6) |
| N52-R08 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | An HCP incident could be material to the group (P08) |
| FAR | Federal contract clauses for G1 | 48 CFR 52.204-21, 52.204-23, 52.204-25, 52.204-30 | Agencies order G1 under federal contracts that include these clauses (section 7 of `../00_company-facts.md`) |
| State | Florida Information Protection Act (worked example) | Fla. Stat. 501.171(6) | The division is a third-party agent for customer personal information it maintains; it must notify the customer within 10 days of a breach determination. Other states are handled generically |
| Contract | Customer agreement and SLA | Security incident notice within 72 hours of confirmation; 99.99% multi-zone and 99.9% console and API availability | Every customer |
| Internal | Group policies POL-01 to POL-05 and the Cloud Hosting supplement | P06 | |

**Not applicable:** CMMC (32 CFR Part 170) does not bind the division as a cloud provider; DIB customers that use G1 rely on its FedRAMP status for their own CMMC scope (32 CFR 170.19(c)(2)). NYDFS Part 500 (no New York license in the group).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Cloud Hosting chief technology officer (system owner) and the Cloud Hosting division CISO on 2026-09-17, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency. G1 holds a FedRAMP certification, and each agency that uses G1 issues its own authorization to operate. The internal decision for the whole HCP:
- **Decision:** authorized to operate with conditions, 2026-09-17, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks), with the Cloud Hosting division president.
- **Conditions:**
  1. Partner-operator sessions limited to 1 hour from 2026-10-15, a run-command volume alert by 2026-10-31 (POAM-002), and partner-operator access moved into SYS-G1 PAM with phishing-resistant MFA and per-client scoping by 2026-12-31 (POAM-001).
  2. G1 follows the FedRAMP VDR and VER rules by 2026-12-07 (POAM-006), and the PAIN-rated incident procedure is exercised at the 2026-12-09 tabletop (POAM-004, POAM-005).
  3. From 2026-10-15, the AI triage service may not run containment actions in G1 or the CDE without analyst approval until its accuracy is validated (POAM-003).
- **Reauthorization:** annually, or at completion of the partner-operator rebuild.

### 4.3 System Operational Status
**Operational.** Major modifications planned:
- Partner-operator access rebuilt on SYS-G1 PAM (P01 GR-01), due 2026-12-31.
- FedRAMP 2026 rules adoption for G1 (P03), on ruleset dates through 2027-08-01.
- Shared failure mode exercise for the CDE regions (POAM-012), due 2027-03-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Cloud Hosting chief technology officer | Accountable for the HCP and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Division security lead | Cloud Hosting division CISO | Security of the HCP; FedRAMP senior security official (receives Emergency messages from the FedRAMP Security Inbox) |
| FedRAMP program | Government Cloud compliance director | Certification package, Ongoing Certification, 2026 rules transition |
| Technical owners | Control plane engineering director; release engineering director; Cloud Hosting data center operations director | HCP services; signing and the pipeline; SYS-H2 management interfaces |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group HR director, Cloud Hosting data center operations director | Operate inherited controls (`common-control-catalog.csv`) |
| Partner-operator owner (consumer) | Managed IT managed hosting director | Requests and uses partner-operator access; accountable for engineers' conduct in tenants |
| Independent assessors | Group internal audit; FedRAMP Recognized independent assessment service (G1) | Assess common controls once and sample HCP controls (P07); annual FedRAMP assessment |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 and adjusted for a cloud provider. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Tenant configuration and metadata (inventory, IAM policies, network configuration) | **High** | **High** | Moderate | Aggregation across about 38,000 customers; an integrity failure (for example, a changed IAM policy) exposes customer data at scale |
| Customer data reachable through HCP functions (snapshots, images, run-command output, console sessions) | **High** | **High** | Moderate | The HCP can read or change any tenant's data through these functions; customers include banks, health care organizations under BAAs, and the group's own CDE |
| Federal customer data and metadata in G1 | Moderate | Moderate | Moderate | Agencies categorize their own systems; G1 is certified at Class C, which FedRAMP aligns with Moderate. G1 is inside this High-categorized system, so it inherits the stronger internal baseline |
| IT infrastructure management (service credentials, signing keys, hypervisor and BMC configuration) | **High** | **High** | Moderate | Compromise would let an attacker act on every customer |
| Information security (audit logs, alerts) | Moderate | **High** | Moderate | Log integrity is essential for incident facts and every notice clock |
| Customer account and billing contacts | Moderate | Low | Low | Contact data of customer staff |
| **HCP category (high-water mark)** | **High** | **High** | **Moderate** | Overall **High** |

**Availability is Moderate** because running customer workloads continue when the control plane is unavailable (P05: BP-H02 MTD 4 hours). The data plane (BP-H01, 2-hour MTD) is outside the HCP boundary.

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **130 controls** in `control-implementation.csv`:
- 125 from the High baseline, of which 124 are also on the FedRAMP Rev5 Class C control list (all except CA-5);
- 1 control that is on the Class C list but not in the High baseline: CA-8(2) red team exercises;
- 4 program management controls not in any baseline (PM-1, PM-2, PM-9, PM-10).

CA-5 (Plan of Action and Milestones) is kept although it is not on the Class C list, because the group still manages weaknesses through a POA&M, and the FedRAMP accepted-vulnerability model replaces it only for G1 reporting (P03).

Other High-baseline controls are tracked in the division's tailoring register: most PE and MA controls are provided by Cloud Hosting data center operations and listed only where the HCP depends on them, and controls for components the HCP does not have (for example wireless access) are tailored out with a reason.

## 7. Authorization Boundary Description
**Inside:**
- Both HCP partitions: console, API gateway, customer IAM, policy engine, orchestration, run-command, support tooling, partner-operator federation, metering capture, and control plane data stores.
- The management interfaces of SYS-H2 (hypervisor managers; BMC bastions) and the SYS-H3 fleet automation service as it acts through the HCP job system.

**Outside, inherited (common control providers):**
- SYS-G1 identity platform and PAM.
- SYS-G2 SOC, SIEM, SOAR, EDR, and the AI triage service.
- SYS-G3 log archive, key management guardrails, and the backup vault at external provider X.
- Cloud Hosting data center operations (physical and environmental controls for 17 data centers).

**Outside, interconnected:**
- SYS-H2 hosts and storage (data plane).
- SYS-H4 edge services.
- The Managed IT legacy identity tenant (partner-operator federation).
- SYS-M1 RMM integrations.
- Customer tenants, including the Payment Processing CDE accounts.
- The third-party model service used by the AI triage service.

**For FedRAMP, G1's boundary is wider than this plan's view of it.** The 2026 Minimum Assessment Scope rules require G1 to list every information resource likely to handle federal customer data or affect it, including metadata (MAS-CSO-IIR, MAS-CSO-MDI). SYS-G1, SYS-G2, and the model service handle G1 identities and logs, so they must be documented as part of the G1 offering or as third-party information resources (MAS-CSO-TPR). That documentation is due before the 2027-02-08 annual assessment (POAM-008).

The diagrams are in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Customers (console, API) | Bidirectional | Resource requests, configuration, console sessions | Customer agreement; acceptable use terms |
| G1 agencies and DIB customers | Bidirectional | Same, in G1 | Agency contracts; DFARS addendum |
| SYS-H2 hosts and storage | Outbound commands; inbound status | Provisioning, run-command, telemetry | Internal design documentation |
| Managed IT legacy identity tenant | Inbound federation | Partner-operator sign-ins | **No documented interconnection terms (gap; CA-3)** |
| SYS-M1 RMM | Bidirectional (API) | Ticket links, inventory | Internal integration record |
| Payment Processing CDE accounts | Hosting | Card data stays inside the CDE accounts; the HCP holds account metadata | **No intercompany agreement with 314.4(f) and PCI DSS 12.8 and 12.9 terms (scenario gap 6)** |
| SYS-G2 SIEM | Outbound | Audit logs (G1 logs over a dedicated path) | Group logging standard |
| Third-party model service (through SYS-G2 AI triage) | Outbound | Alert context, which can include G1 resource metadata and customer IP addresses | **Not documented as a FedRAMP third-party information resource (POAM-008)** |
| External provider X | Outbound | Immutable backups | Provider agreement |

## 9. System Component Inventory
| Component | Type | Location | Owner |
|---|---|---|---|
| Console and API gateway | Company-built services on control plane clusters | R1, R3, R4; G1-A, G1-B | Control plane engineering director |
| Customer IAM and policy engine | Company-built services | Same | Control plane engineering director |
| Orchestration, job system, run-command | Company-built services | Same | Control plane engineering director |
| Support tooling and partner-operator federation | Company-built services | Commercial partition only (G1 has no partner-operator path) | Control plane engineering director |
| Control plane databases, queues, secrets store | Managed services on SL-1 (G1 copies in G1) | Same | Control plane engineering director |
| Hypervisor managers and BMC bastions | Virtual appliances and hardened hosts | All 17 data centers | Cloud Hosting data center operations director |
| Fleet automation and signing service | Company-built service with HSMs | R1, R3; G1 has its own signing domain | Release engineering director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (130 controls) and `common-control-catalog.csv` (83 group common controls).

| Status | Controls |
|---|---|
| Implemented | 107 |
| Partially implemented | 23 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **130** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or Cloud Hosting data center operations) | 54 |
| Hybrid (a common provider supplies the mechanism; the HCP configures or operates part) | 29 |
| System-specific | 47 |

**The 23 partially implemented controls** cluster in four places:
- **The partner-operator path** (scenario gap 1): AC-2, AC-2(12), AC-6, AC-6(5), AC-6(7), AC-12, IA-2(1), and AU-6 (shared with the AI triage gap).
- **The FedRAMP 2026 rules transition for G1** (gap 3): CA-5, CA-7, CM-3, CM-8, PL-2, RA-5, SA-9, and SC-13.
- **The SOC's AI triage service** (gap 4): SI-4 and IR-4.
- **Cross-division governance** (gaps 7 and 10, and the CDE design): IR-3, IR-6, CA-3, PS-7, and CP-4.

### 10.2 Common control inheritance by division
The catalog lists 83 controls provided by group functions or by Cloud Hosting data center operations and the edge service.
- **Cloud Hosting:** inheritance is documented in the G1 FedRAMP package and the SL-1 SOC 2 system description.
- **Payment Processing:** documented in its PCI DSS responsibility matrix for group services, **but not for the SL-1 platform controls it relies on** (physical security, data center media handling, and DDoS protection; 5 controls in the catalog). That is scenario gap 6 (POAM-018).
- **Managed IT:** **not documented at all** (scenario gap 9; POAM-017). P07 found the CA-2 statements other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and HCP and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit (P07 `assessment-results.csv` and `poam.csv`). The G1 partition's annual FedRAMP independent assessment was completed on 2026-03-20; the next starts on 2027-02-08 and will be the first under the 2026 rules.

## 11. Digital Identity Acceptance Statement
Assurance levels follow NIST SP 800-63.
- **Cloud Hosting workforce:** SYS-G1 single sign-on with phishing-resistant hardware keys for privileged users, and just-in-time PAM elevation. This meets the intent of authenticator assurance level 3 for administrators.
- **Partner operators (gap):** push MFA through the Managed IT legacy tenant, with 12-hour sessions that are not bound to a device. That is not phishing-resistant and is below the level required for an account that can act on thousands of tenants. Target: SYS-G1 hardware keys, PAM, and per-client scoping by 2026-12-31 (POAM-001).
- **Customer users:** password plus MFA, required for tenant root owners and available to all; about 61% of customer administrator users have MFA enabled. Customers control their own users (a complementary user entity control in the SOC 2 report).
- **G1 agency administrators:** agency federation with PIV-based credentials (IA-2(12)).
- **Service identities:** short-lived workload identities with mutual TLS.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **BMC:** baseboard management controller (out-of-band hardware management)
- **CDE:** cardholder data environment (PCI DSS)
- **Common control:** a control provided once by a group function and inherited by several systems
- **G1:** the Government Cloud region
- **HCP:** Hosting Control Plane and Customer Portal
- **HSM:** hardware security module
- **PAIN:** Potential Agency Impact N-rating (FedRAMP 2026 rules)
- **PAM:** privileged access management
- **Partner operator:** a Managed IT engineer allowed to act inside a managed-hosting tenant
- **Run-command:** an HCP function that executes commands inside a customer virtual machine through the guest agent
- **SDR:** Security Decision Record (FedRAMP 2026 rules)
- **SOAR:** security orchestration, automation, and response

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | Cloud Hosting division CISO |
| 1.0 | 2026-09-17 | Approved with authorization conditions | Cloud Hosting chief technology officer |
