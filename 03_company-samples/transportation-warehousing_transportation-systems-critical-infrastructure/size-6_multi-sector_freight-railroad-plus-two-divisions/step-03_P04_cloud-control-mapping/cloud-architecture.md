# Cloud Architecture and Control Placement: Cris Santos Company Holdings | Transportation Systems | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector | **Providers:** two public cloud providers, called provider A and provider B (vendor-agnostic; see section 5), plus company data centers DC-1 and DC-2
**Scope:** the shared corporate cloud platform (SYS-G3 landing zones, the SYS-G5 integration platform, logging, keys, and backups) and the division workloads that run on it or depend on it. The SSP system (P02, TDPB) is on premises; its cloud dependencies are shown separately.

## 1. Design in one paragraph
Corporate runs one **landing zone** per provider: identity federation from SYS-G1, a hub network, guardrail policies, a central log archive, key management, EDR, and an immutable backup vault. Divisions get their own **accounts** (subscriptions or projects) inside the landing zone and inherit these guardrails. Provider A hosts the hub, the SYS-G5 integration platform, the rail TMS and crew system, the terminal operating system, and the wholesale portal and federal contracts workspace. Provider B hosts the SIEM data lake and log archive, the AI services (SYS-G6), the immutable backup vault, and the TDPB clean-room recovery account. **The train dispatching and PTC back office platform stays on premises** in DC-1 and DC-2 for latency and availability; it reaches the cloud only through the industrial DMZ. Many division systems are SaaS (ERP, property management, fleet telematics, building OT consoles), where the group's duties are identity, configuration, and vendor oversight.

## 2. Diagrams
### 2.1 Group landing zone and division workloads

```mermaid
flowchart TB
  subgraph Common["Common controls (corporate; inherited by all divisions)"]
    IDP["Group identity platform SYS-G1<br/>IA-2(1), AC-2, AC-6(5)"]
    IAM["Cloud IAM, providers A and B<br/>AC-3"]
    HUB["Hub network, provider A<br/>SC-7, SC-7(5)"]
    PRIV["Private circuits to DC-1, DC-2, NOCs<br/>SC-8(1)"]
    GRD["Guardrail policy service<br/>CM-6, CM-7"]
    LOG[("Central log archive, provider B<br/>AU-9, AU-11")]
    SOC["Group SIEM and SOC SYS-G2<br/>SI-4, AU-6"]
    EDR["Workload protection (EDR)<br/>SI-3"]
    KMS["Key management<br/>SC-12, SC-28(1)"]
    BK[("Immutable backup vault, provider B<br/>CP-9, CP-6")]
    INT["Integration platform SYS-G5<br/>AC-4, IA-5, SI-2, SI-12"]
  end
  subgraph RR["Freight Railroad accounts (provider A)"]
    TMS["Rail TMS SYS-R4<br/>CM-3, CP-10, AC-3"]
    CREW["Crew system SYS-R5<br/>SC-28"]
  end
  subgraph TW["Transload and Wholesale accounts (provider A)"]
    TOS["Terminal operating system SYS-W1<br/>IA-2(1), CP-9"]
    FCI["Federal contracts workspace SYS-W3<br/>AC-3, SC-7"]
    PORT["Customer portal and EDI<br/>SC-8"]
  end
  subgraph AIB["AI services (provider B)"]
    AI1["AI-001 defect detection<br/>SA-11, AU-3"]
  end
  subgraph SAAS["SaaS used by divisions"]
    ERP["Group ERP SYS-G4"]
    PMS["Property management SYS-E1<br/>IA-2(1), AC-3"]
    BAS["Building OT vendor consoles SYS-E2<br/>SA-9"]
    TEL["Fleet telematics SYS-W4<br/>SA-9"]
    ROW["Right-of-way portal SYS-E3<br/>AC-21"]
  end
  DMZ["Industrial DMZ (DC-1, DC-2)<br/>TMS interface server, SC-7"]
  TDPB["TDPB on premises<br/>(see 2.2)"]
  IDP --> IAM
  IAM --> RR
  IAM --> TW
  IAM --> AIB
  HUB --> RR
  HUB --> TW
  PRIV --> DMZ
  TMS <-->|consists and car lists| DMZ
  DMZ --> TDPB
  TOS <-->|car orders and placements| INT
  INT <-->|gap 1: not in the CIP flow list| TMS
  INT <--> ERP
  INT <--> PMS
  PORT --> INT
  RR --> LOG
  TW --> LOG
  AIB --> LOG
  INT --> LOG
  LOG --> SOC
  RR --> BK
  TW --> BK
  GRD -.-> RR
  GRD -.-> TW
  GRD -.-> AIB
  KMS -.-> CREW
  EDR -.-> TOS
```

### 2.2 TDPB (SSP boundary) and its cloud dependencies

```mermaid
flowchart LR
  subgraph TDPBB["TDPB boundary (DC-1 primary, DC-2 standby, both NOCs)"]
    CAD["CAD cluster<br/>AC-3, SI-10, CP-10"]
    PTCB["PTC back office<br/>SI-2 (gap 2), CP-7"]
    KEY["PTC key management enclave<br/>SC-12, SC-7(21)"]
    CTC["CTC office code servers<br/>AC-2 (shared admin accounts, gap 4)"]
    CON["156 dispatch consoles<br/>IA-2(1) compensating controls, CM-7(5)"]
  end
  DMZ2["Industrial DMZ<br/>PAM jump hosts, TMS interface server"]
  CORP["Corporate network and SYS-G1"]
  FIELD["Field code units, wayside interface units, radio"]
  ONB["Onboard PTC apparatus (330 locomotives)"]
  MSG["Interoperable messaging network<br/>(Class I, Amtrak, commuter operator)"]
  VAULT[("Provider B vault and clean-room recovery account<br/>CP-9, CP-9(1), CP-10")]
  SIEM["SIEM SYS-G2<br/>AU-12 partial: CTC and PTC logs missing"]
  CORP -->|PAM only, AC-17| DMZ2
  DMZ2 --> CAD
  DMZ2 --> PTCB
  CAD --> CTC
  CTC --> FIELD
  PTCB <--> KEY
  PTCB <-->|236.1033 message integrity| ONB
  PTCB <--> MSG
  CON --> CAD
  CAD --> VAULT
  PTCB --> VAULT
  CAD --> SIEM
```

**Target state (POAM-001, POAM-003, POAM-004, POAM-005):** the SYS-G5 route into the TMS interface server is described in an amended CIP with its own inspected DMZ rule; CTC and PTC logs reach the SIEM with 1-year retention; the PTC back office standby is rebuilt to match production and meets its 4-hour RTO; unpatched PTC servers have documented compensating measures until the vendor certifies patches.

## 3. Common versus division-specific controls
`cloud-control-map.csv` has 46 rows across 28 components. The `control_scope` column shows who owns each placement:

| Scope | Rows | What it means |
|---|---|---|
| Common (group) | 25 | Provided once by corporate (SYS-G1 to SYS-G5) and inherited by every division account. Listed in the P02 common control catalog |
| SSP system (TDPB cloud dependencies) | 4 | Cloud and DMZ placements that the on-premises TDPB relies on, documented in the P02 SSP |
| Division-specific (Freight Railroad) | 7 | TMS, crew system, crew telephony, and the AI defect detection services |
| Division-specific (Transload and Wholesale) | 6 | Terminal operating system, federal contracts workspace, customer portal, fleet telematics |
| Division-specific (Real Estate) | 4 | Property management, building OT vendor consoles, right-of-way portal |

| Responsibility | Rows |
|---|---|
| Customer (the group or a division) | 37 |
| Shared (provider and group) | 6 |
| Provider | 3 |

**Rule of thumb.** Identity, network guardrails, logging, keys, backups, EDR, and the integration platform are **common**. A division cannot opt out, only request an exception through POL-01. Application behavior, operational technology, and customer-facing identity are **division-specific**, because they depend on each division's regulators and customers: TSA and FRA for the railroads, FAR clauses and hazmat rules for terminals and wholesale, lease and vendor terms for buildings.

## 4. Layers
| Layer | Common components | Division components | Key controls | Responsibility |
|---|---|---|---|---|
| Identity | SYS-G1, cloud IAM | TMS roles, TOS kiosks, property portal users, CDS customer users | AC-2, AC-3, AC-6(5), IA-2(1), IA-5 | Customer (configuration); vendor (service) |
| Network | Hub, private circuits, edge protection | Industrial DMZ (on premises), federal contracts workspace | SC-7, SC-7(5), SC-8, SC-8(1), SC-5 | Customer, with provider DDoS protection shared |
| Compute | EDR, guardrails, integration platform | TMS, TOS, AI services | SI-2, SI-3, CM-3, CM-6, CM-7, SA-11 | Customer (guest OS, containers, code) |
| Data | Keys, backup vault | TMS RSSM extract, crew records, FCI, guarantor records | SC-12, SC-28, SC-28(1), CP-9, CP-6, CP-10, AC-21, SI-12 | Shared: provider encrypts; group owns keys, retention, and access |
| Logging and monitoring | Log archive, SIEM | TDPB forwarding, AI alert logs | AU-3, AU-6, AU-9, AU-11, AU-12, SI-4 | Shared: providers generate platform logs; group retains and reviews |
| SaaS dependencies | Identity, SIEM, and EDR vendors | Crew telephony, telematics, building OT vendors, property and right-of-way systems | SA-9 | Provider for the service; customer for use and oversight |
| Physical | Provider data centers (DC-1 and DC-2 are company-run and covered in P02) | none | PE-3, MP-6 | Provider (inherited) |

## 5. Service categories and provider equivalents
The design does not depend on a provider. This table gives each provider's name for each service category, for reading its shared responsibility documentation.

| Service category | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|
| Account structure and guardrails | AWS Organizations with service control policies | Management groups with Azure Policy | Resource hierarchy with Organization Policy |
| Hub network and firewalls | Transit Gateway with AWS Network Firewall | Virtual WAN hub with Azure Firewall | Network Connectivity Center with Cloud NGFW |
| Managed integration and file transfer | AWS Transfer Family; Amazon EventBridge | Azure Logic Apps; Azure Service Bus | Application Integration; Pub/Sub |
| Managed relational database | Amazon RDS | Azure SQL Database | Cloud SQL |
| Key management | AWS KMS | Azure Key Vault | Cloud KMS |
| Audit logging | AWS CloudTrail | Azure Monitor activity log | Cloud Audit Logs |
| Backup with immutability | AWS Backup (vault lock) | Azure Backup (immutable vault) | Backup and DR Service |
| Private connectivity | AWS Direct Connect | Azure ExpressRoute | Cloud Interconnect |

Shared responsibility sources: SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal-framework/sources/source-register.csv`. All three agree on the split used here: for IaaS the provider owns facilities, hosts, and virtualization; for PaaS the provider also owns the runtime; for SaaS the provider owns the application. The customer always keeps identities, access decisions, data classification, and data.

## 6. Findings from the mapping
1. **The integration platform is the group's hidden Critical Cyber System dependency** (AC-4). It is common, cloud-hosted, and connects every division, and it feeds the TMS interface server that sits next to dispatch. It must be named in the CIP and given its own DMZ rule (gap 1; P01 GR-01; POAM-001).
2. **The integration platform also holds personal information it does not need** (SI-12). HR export files for all divisions sit in the transfer store with no purge. In a breach they would turn an operational incident into a multi-state notification event (P08).
3. **TDPB's cloud dependencies are recovery and monitoring, not operations.** The vault and the clean-room recovery account are sound (CP-9, CP-9(1), CP-10); the weak link is log forwarding from CTC and PTC servers (AU-12; POAM-003).
4. **Common controls are strong and reused.** One identity platform, one SIEM, one backup design. This is what lets group internal audit assess them once (P07). The weak links are where divisions sit outside the platform: 21 acquired terminals with local accounts and no EDR (gap 5), and building OT consoles run by vendors under contracts without security terms (gap 7).
5. **The federal contracts workspace is a small, clean enclave** (AC-3, SC-7). Keeping FCI there limits the reach of FAR 52.204-21 to 23 users and one workspace.
