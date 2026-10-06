# Cloud Architecture and Control Placement: Cris Santos Company | Commercial Facilities | Mid-Market

**Organization:** Cris Santos Company, Inc. | **Tier:** Mid-Market | **Provider:** Vendor-agnostic public cloud (see section 4), plus SaaS
**System:** Building Automation and Access Control System (BAACS), as defined in the SSP (P02), with the rest of the landing zone it shares | **Prepared:** 2026-07-31 by the IT Director and the Security Manager; updated 2026-09-15 with P07 results
**Control map:** `cloud-control-map.csv` (49 rows, 22 components)

## 1. Diagram
The diagram shows today's design. Items marked "gap" or "planned" are POA&M items (P07).

```mermaid
flowchart LR
  subgraph Towers["Towers 1-4 (OT zones in place)"]
    FWT["Property firewalls<br/>SC-7, AC-4, SC-7(5)"]
    BASA["Platform A BAS server VM (Tower 1)<br/>CM-6, SI-3, CP-9 (gap: any-any rule found in P07)"]
    OTA["Platform A controllers, door controllers, cameras, NVRs<br/>CM-8, IA-5"]
    SCC["SCC console PCs (Tower 1; backup at Tower 3)<br/>SI-3, AC-11, CP-7"]
  end
  subgraph Flat["Mixed-Use 1-2 (partial), Parks 1-2 and Retail 1-6 (flat)"]
    FWF["Property firewalls<br/>SC-7 (gap: no OT zones)"]
    BASB["8 Platform B site servers<br/>SA-22 (gap: unsupported OS, no backups)"]
    OTB["Platform B controllers, door controllers, NVRs<br/>IA-5 (gap: default passwords), CM-8 (gap)"]
  end
  subgraph SaaS["SaaS (provider-operated)"]
    IDP["Identity provider<br/>IA-2, IA-2(1), AC-7"]
    PACS["Access control and video platform<br/>AC-3, AC-6, AU-2, CP-9, SI-12"]
    APP["Tenant experience app<br/>AC-2 (mobile credentials)"]
    VMS["Visitor management<br/>SI-12 (gap: no retention limit)"]
    SIEM["MSSP SIEM<br/>SI-4, AU-6 (gap: no OT sources)"]
  end
  subgraph Org["Cloud organization (4 accounts)"]
    subgraph IdA["Identity and security account"]
      FED["Cloud identity federation<br/>IA-2, AC-2, AC-6(5)"]
      GR["Organization guardrails<br/>CM-6, AC-3"]
      POST["Posture and threat detection<br/>CA-7, RA-5"]
    end
    subgraph SSA["Shared services account"]
      HUB["Network hub and cloud firewall<br/>SC-7, SC-7(5), AC-4"]
      VPN["Site-to-cloud VPN<br/>SC-8"]
      RAG["Remote access gateway<br/>AC-17, MA-4, IA-2(1), AU-2"]
      LOG["Log pipeline and write-once bucket<br/>AU-9, AU-11"]
    end
    subgraph WLA["Workloads account"]
      HIS["BAS historian and energy analytics<br/>CM-6, SI-2, SC-28"]
      CON["Energy optimization connector (AI-004)<br/>AC-4, CA-3 (gap: no terms)"]
      FS[("File storage: drawings<br/>AC-3, SC-28")]
      DW[("Data warehouse: JV reporting<br/>AC-6")]
      KMS["Key management<br/>SC-12"]
    end
    subgraph BKA["Backup account (second region)"]
      BK[("Backup vault, write-once 35 days<br/>CP-9, CP-6 (gap: no restore test)")]
    end
  end
  INTA["BAS Integrator A; access control integrator"] -->|MFA, approval, recording| RAG
  INTB["BAS Integrator B"] -.->|today: always-on tool, shared account (gap)| BASB
  INTB -->|planned 2026-11-30| RAG
  RAG --> BASA
  RAG -.->|planned| BASB
  FWT -->|IPsec| VPN
  FWF -->|IPsec| VPN
  VPN --> HUB
  HUB --> HIS
  BASA -->|trend data| HIS
  BASB -->|trend data| HIS
  VEND["Energy optimization vendor"] -->|setpoint writes| CON
  CON --> BASA
  OTA -->|TLS| PACS
  OTB -->|TLS| PACS
  APP -->|mobile credentials| PACS
  VMS -->|visitor passes| PACS
  SCC -->|SSO and MFA| IDP
  IDP --> PACS
  IDP --> FED
  BASA --> BK
  HIS --> BK
  FS --> BK
  DW --> BK
  LOG --> SIEM
  IDP --> SIEM
  POST --> SIEM
  LS["Life-safety systems (separate networks)"] -.->|read-only hardwired relays| OTA
```

## 2. Landing zone design
The landing zone separates duties across 4 accounts (subscriptions or projects, depending on the provider) under one cloud organization. Each account limits what an attacker can do from any other.

| Account | Purpose | Who administers | Key design decisions |
|---|---|---|---|
| **Identity and security** | Organization root, cloud identity federation to the identity provider, organization guardrails, posture management and threat detection | Security Manager and the OT security analyst | No workloads. Root credentials sealed. Guardrails apply to every other account and cannot be disabled from them |
| **Shared services** | Network hub, cloud firewall, site-to-cloud VPN for 14 sites, DNS and time, the integrators' remote access gateway, log pipeline and write-once log bucket | IT Director's infrastructure team | All traffic between sites, workloads, the gateway, and the internet passes the hub. OT sites reach only the historian and gateway subnets |
| **Workloads** | BAS historian and energy analytics, the energy optimization connector (AI-004), file storage for building drawings, the data warehouse for JV and lender reporting, key management | Infrastructure team; Integrator A for the historian application | Separate subnets per workload. No internet ingress. Company-managed keys |
| **Backup** | Backup vault with 35-day write-once retention in a second region | 2 named backup administrators | Separate administrator credentials, not federated to everyday accounts. Backups are written by a cross-account role that cannot delete |

**Where OT meets the cloud.** The BAACS is mostly on-premises. Its cloud footprint is the historian, the gateway, the backups, and the vendor SaaS platform for access control and video. The design rule is that the cloud may **receive** OT data (trends, logs, backups) and **broker** vetted remote sessions, but nothing in the cloud writes to OT without a named, approved path. The energy optimization connector (AI-004) is today's only exception, and P10 sets conditions on it.

## 3. Layers and shared responsibility per service
| Layer | Components | Key controls | Service model | Responsibility |
|---|---|---|---|---|
| Identity | Cloud federation, break-glass accounts, guardrails, identity provider, backup administrators | IA-2, IA-2(1), AC-2, AC-6(5), AC-7, IA-5 | PaaS / SaaS | Customer configures identities, roles, MFA, and reviews; providers run the identity services |
| Network | Hub, cloud firewall, VPN, DNS and time, remote access gateway, SD-WAN, energy optimization connector | SC-7, SC-7(5), AC-4, SC-8, AC-17, MA-4, CA-3 | IaaS / PaaS / SaaS | Customer designs routes, rules, and segmentation; providers run the gateway, VPN, and SD-WAN services |
| Compute | Historian and analytics virtual machines | CM-6, SI-2, SI-3, CP-10 | IaaS | Customer (guest OS, applications, EDR); Integrator A for the historian application under contract; provider for hosts and hypervisor |
| Data | File storage, managed database, data warehouse, keys, backups | SC-28, SC-12, CP-9, CP-6, CP-4, AC-3, AC-6 | PaaS | Shared: provider encrypts and runs storage; customer controls keys, access, retention, isolation, and restore testing |
| Logging and monitoring | Log pipeline, posture service, SIEM | AU-2, AU-6, AU-8, AU-9, AU-11, CA-7, RA-5 | PaaS / SaaS | Shared: providers generate logs and findings; customer enables, retains, forwards, and acts on them; MSSP monitors |
| SaaS applications | Identity provider, access control and video platform, tenant app, visitor management | AC-3, AC-6, AU-2, CP-9, SI-12, AC-2 | SaaS | Provider runs the application; customer keeps users, roles, retention settings, and audit review |
| Physical | Provider data centers | PE-3, PE-13 | All | Provider (inherited, evidenced by SOC 2 reports) |

**Responsibility counts in `cloud-control-map.csv`:** 28 Customer, 15 Shared, 6 Provider. By service model: 16 IaaS, 22 PaaS, 11 SaaS rows. The customer side is always identity, data protection, retention, and logging, which is what the three major providers' shared responsibility models say.

## 4. Service categories and provider equivalents
The design is independent of the provider. This table gives each provider's name for each service category, for reading its shared responsibility documentation (SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal-framework/sources/source-register.csv`).

| Service category | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|
| Multi-account organization and guardrails | AWS Organizations, service control policies | Management groups, Azure Policy | Resource Manager folders, organization policies |
| Account, subscription, or project | Account | Subscription | Project |
| Cloud identity federation | IAM Identity Center | Microsoft Entra ID with Azure RBAC | Cloud Identity with IAM |
| Network hub | Transit Gateway | Virtual WAN hub or hub virtual network | Network Connectivity Center or shared VPC |
| Cloud firewall | AWS Network Firewall | Azure Firewall | Cloud NGFW |
| Site-to-cloud VPN | Site-to-Site VPN | VPN Gateway | Cloud VPN |
| Virtual machines (historian, gateway, connector) | EC2 | Virtual Machines | Compute Engine |
| Object storage with write-once retention | S3 with Object Lock | Blob Storage with immutability policies | Cloud Storage with bucket lock |
| Managed database and warehouse | Amazon RDS or Redshift | Azure SQL or Azure Synapse | Cloud SQL or BigQuery |
| Backup service | AWS Backup (vault lock) | Azure Backup (immutable vault) | Backup and DR Service |
| Key management | AWS KMS | Azure Key Vault | Cloud KMS |
| Audit logging | CloudTrail | Azure Monitor activity log | Cloud Audit Logs |
| Posture and threat detection | Security Hub, GuardDuty | Microsoft Defender for Cloud | Security Command Center |

**Service model split used here (all three providers agree):**
- **IaaS** (virtual machines, networks): the provider owns facilities, hosts, and virtualization. The customer owns the guest OS, applications, network configuration, identities, and data.
- **PaaS** (managed database, storage, backup, key service, VPN): the provider also owns the platform software and its patching. The customer owns access, keys, data, retention, and configuration.
- **SaaS** (identity provider, access control and video platform, tenant app, visitor management, SD-WAN orchestration): the provider also owns the application. The customer keeps identities, roles, retention settings, audit review, and data.

## 5. Findings from the mapping
1. **The remote access gateway is the strongest OT control, but it covers only half the portfolio.** Integrator A and the access control integrator connect only through it, with MFA, approval, and recording. Integrator B bypasses it at 8 properties (POAM-003; P01 R-002). Fix: move Integrator B by 2026-11-30 and block its tool at the property firewalls.
2. **The cloud receives OT data but OT logs do not reach the SIEM.** The log pipeline is ready, but BAS servers and access control administrator events are not forwarded (POAM-006; P01 R-029). Fix: forward Platform A, gateway, and platform audit logs first (2026-12-31), then Platform B after the upgrade.
3. **Backups are isolated but incomplete and untested.** The backup account (separate credentials, second region, write-once) is well designed. It does not hold Platform B servers or field controller programs, and nothing has been restored (POAM-010; P01 R-004). Fix: add Platform B images and controller program exports; quarterly restore tests starting 2026-10-27.
4. **The energy optimization connector is a write path into OT.** A vendor service in the cloud changes setpoints on Platform A at Towers 1-2. Bounds are enforced by the vendor, and there are no written interconnection terms (CA-3; P01 R-011). P10 requires company-enforced write limits on the connector and a contract addendum.
5. **SaaS retention is the customer's job.** The access control and video platform and the visitor management service keep data as long as the company configures them to. Today visitor ID scans are kept indefinitely and analytics clips for 1 year (POAM-017; P01 R-016).
6. **Boundary check.** Every in-scope component in the SSP (P02 section 9) appears in the diagram. Every cloud component has at least one row in the control map, and each account has controls from at least 2 of the AC, AU, CM, IA, SC, and SI families or inherits them.
7. **Inherited controls rely on SOC 2 reports.** Controls marked Provider or Shared for the identity provider, the access control and video platform, the cloud provider, and the MSSP depend on their SOC 2 Type 2 reports and complementary user entity controls, reviewed each year in P09 `vendor-soc2-review.csv`.
