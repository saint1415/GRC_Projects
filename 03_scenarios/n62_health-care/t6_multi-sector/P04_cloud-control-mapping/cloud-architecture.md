# Cloud Architecture and Control Placement: Cris Santos Company Holdings | Health Care | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector | **Providers:** two public cloud providers, called provider A and provider B (vendor-agnostic; see section 4)
**Scope:** the shared corporate cloud platform (SYS-G3 landing zones and the Group Data Platform) plus the division workloads that run on it. The SSP system (P02) is the Group Data Platform.

## 1. Design in one paragraph
Corporate runs one **landing zone** per provider: identity federation from SYS-G1, a hub network, guardrail policies, a central log archive, key management, EDR, and an immutable backup vault. Divisions get their own **accounts** (subscriptions or projects) inside the landing zone and inherit these guardrails. Provider A hosts the corporate hub, the Group Data Platform (GDP), Care Delivery's patient-app platform (SYS-D4) and interface engines, and the Health Plan's UM platform and portals. Provider B hosts the SaaS production service (SYS-D3), the GDP disaster recovery replica, and the backup vault. Two division systems sit outside the cloud platform: the Care Delivery EHR (SYS-D1, hosted by the EHR vendor) and the Health Plan claims core (SYS-D2, in a group colocation data center, linked privately).

## 2. Diagrams
### 2.1 Group landing zone and division workloads

```mermaid
flowchart TB
  subgraph Common["Common controls (corporate; inherited by all divisions)"]
    IDP["Group identity platform SYS-G1<br/>IA-2(1), AC-2, AC-6(5), AC-7"]
    IAM["Cloud IAM, providers A and B<br/>AC-3"]
    HUB["Landing-zone hub network<br/>SC-7, SC-7(5), SC-8"]
    PRIV["Private connectivity to colocation and sites<br/>SC-8(1)"]
    GRD["Guardrail policy service<br/>CM-6, CM-7"]
    LOG[("Central log archive account<br/>AU-9, AU-11")]
    SOC["Group SIEM and SOC SYS-G2<br/>SI-4, AU-6"]
    EDR["Workload protection (EDR)<br/>SI-3"]
    KMS["Key management<br/>SC-12, SC-28(1)"]
    BK[("Immutable backup vault, provider B<br/>CP-9, CP-6")]
    DC["Provider data centers<br/>PE-3, MP-6 (inherited)"]
  end
  subgraph CD["Care Delivery accounts (provider A)"]
    APP["SYS-D4 patient-app platform<br/>containers and API gateway<br/>SA-11, SC-5"]
    PID["SYS-D4 patient identity<br/>IA-2"]
    PDB[("SYS-D4 managed database<br/>SC-28")]
    IE["Care Delivery interface engines<br/>SI-2"]
  end
  EHR["SYS-D1 EHR (vendor-hosted SaaS)<br/>CP-9 provider, AU-6 customer"]
  subgraph HP["Health Plan accounts (provider A)"]
    UM["UM platform and AI UM model serving<br/>CM-3, AU-12"]
    POR["Member and broker portals<br/>IA-2(1), SC-7"]
  end
  CLAIMS["SYS-D2 claims core<br/>(group colocation data center)"]
  subgraph SAAS["Health-Tech SaaS accounts (provider B)"]
    K8S["SYS-D3 container platform<br/>SC-4, CM-3"]
    SDB[("SYS-D3 managed database<br/>SC-28, CP-10")]
    TEN["SYS-D3 customer tenants<br/>IA-2(1) (customer control)"]
    AIF["Care summary assist<br/>SA-9, AU-3"]
    DEX["De-identified export to GDP<br/>AC-21"]
  end
  LLM["Third-party model provider<br/>(subcontractor BAA)"]
  GDP["Group Data Platform<br/>(see 2.2)"]
  IDP --> IAM
  IAM --> CD
  IAM --> HP
  IAM --> SAAS
  HUB --> CD
  HUB --> HP
  HUB --> GDP
  PRIV --> CLAIMS
  CLAIMS -->|approved nightly extracts, AC-4| GDP
  EHR -->|interfaces over TLS| IE
  IE --> GDP
  UM <-->|training data and monitoring| GDP
  TEN --> K8S
  K8S --> SDB
  K8S --> AIF
  AIF -->|private egress, TLS| LLM
  SDB --> DEX
  DEX -->|de-identified sets| GDP
  CD --> LOG
  HP --> LOG
  SAAS --> LOG
  GDP --> LOG
  LOG --> SOC
  CD --> BK
  HP --> BK
  GDP --> BK
  GRD -.-> CD
  GRD -.-> HP
  GRD -.-> SAAS
  KMS -.-> PDB
  KMS -.-> SDB
  EDR -.-> K8S
  EDR -.-> IE
  DC -.-> HUB
```

### 2.2 Group Data Platform (SSP boundary)

```mermaid
flowchart LR
  subgraph GDPB["Group Data Platform boundary (provider A)"]
    ING["Ingestion and workflow services<br/>AC-4, IA-5"]
    subgraph Lake["Data lake zones (SC-28, per-zone keys)"]
      ZCD[("Care Delivery PHI zone")]
      ZHP[("Health Plan PHI zone")]
      ZDI[("De-identified zone")]
      ZST[("Staging<br/>gap: identifiable SaaS data lands here")]
    end
    CAT["Catalog and policy engine<br/>PT-3, CM-8, AC-3"]
    DW["Data warehouse<br/>AC-6, AU-3"]
    WS["Data science workspace<br/>CM-11, AC-12"]
  end
  DR[("DR replica, provider B<br/>CP-7")]
  SRC1["SYS-D1 exports"] --> ING
  SRC2["SYS-D2 extracts"] --> ING
  SRC3["SYS-D3 de-identified exports"] --> ING
  ING --> ZST
  ZST --> ZCD
  ZST --> ZHP
  ZST --> ZDI
  CAT -.->|purpose tags, 61% coverage| ZCD
  CAT -.-> ZHP
  CAT -.-> ZDI
  ZCD --> DW
  ZHP --> DW
  ZDI --> DW
  DW --> WS
  ZCD --> DR
  ZHP --> DR
  ZDI --> DR
```

**Target state (POAM-006 and POAM-007, due 2027-03-31):** the Care Delivery and Health Plan zones move to separate accounts with separate keys; every table carries a covered entity and purpose tag enforced by the policy engine; SaaS data is de-identified inside SYS-D3 before export, so identifiable SaaS data never reaches staging; cross-division analysis uses approved, minimum-necessary views only.

## 3. Common versus division-specific controls
`cloud-control-map.csv` has 53 rows across 30 components. The `control_scope` column shows who owns each placement:

| Scope | Rows | What it means |
|---|---|---|
| Common (group) | 22 | Provided once by corporate (SYS-G1, SYS-G2, SYS-G3) and inherited by every division account. Listed in the P02 common control catalog |
| Shared system (Group Data Platform) | 11 | Controls of the shared corporate system documented in the P02 SSP |
| Division-specific (Care Delivery) | 7 | Patient-app platform, interface engines, EHR customer duties |
| Division-specific (Health Plan) | 5 | UM model, portals, claims link |
| Division-specific (Health-Tech SaaS) | 8 | Multi-tenant service, AI feature, de-identified export |

| Responsibility | Rows |
|---|---|
| Customer (the group or a division) | 41 |
| Shared (provider and group) | 8 |
| Provider | 4 |

**Rule of thumb.** Identity, network guardrails, logging, keys, backups, and EDR are **common**. A division cannot opt out of them, only request an exception through POL-01. Application behavior, data access within the application, and customer-facing identity are **division-specific**, because they depend on each division's regulators and customers.

## 4. Layers
| Layer | Common components | Division components | Key controls | Responsibility |
|---|---|---|---|---|
| Identity | SYS-G1, cloud IAM | Patient identity (SYS-D4), member and broker portals, SaaS customer tenants | AC-2, AC-3, AC-6(5), IA-2, IA-2(1) | Customer (configuration); vendor (service) |
| Network | Hub network, private links | API gateways, WAF | SC-7, SC-7(5), SC-8, SC-8(1), SC-5 | Customer, with provider DDoS protection shared |
| Compute | EDR on all hosts | Containers, interface engines, UM serving, GDP workspace | SI-2, SI-3, CM-3, CM-11, SC-4 | Customer (guest OS, containers, code) |
| Data | Keys, backup vault | GDP zones, division databases | SC-12, SC-28, SC-28(1), CP-9, CP-6, AC-4, PT-3 | Shared: provider encrypts; group owns keys, zoning, and retention |
| Logging and monitoring | Log archive, SIEM | Application and model decision logs | AU-3, AU-6, AU-9, AU-11, AU-12, SI-4 | Shared: providers generate platform logs; group retains and reviews |
| SaaS dependencies | Identity and SIEM vendors | EHR vendor, model provider | SA-9, CP-9, AU-6 | Provider for the service; customer for use and oversight |
| Physical | Provider data centers | none | PE-3, MP-6 | Provider (inherited) |

## 5. Service categories and provider equivalents
The design does not depend on a provider. This table gives each provider's name for each service category, for reading its shared responsibility documentation.

| Service category | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|
| Account structure and guardrails | AWS Organizations with service control policies | Management groups with Azure Policy | Resource hierarchy with Organization Policy |
| Object storage (data lake) | Amazon S3 | Azure Blob Storage / Data Lake Storage | Cloud Storage |
| Managed analytical database | Amazon Redshift | Azure Synapse Analytics | BigQuery |
| Managed containers | Amazon EKS | Azure Kubernetes Service | Google Kubernetes Engine |
| Key management | AWS KMS | Azure Key Vault | Cloud KMS |
| Audit logging | AWS CloudTrail | Azure Monitor activity log | Cloud Audit Logs |
| Backup with immutability | AWS Backup (vault lock) | Azure Backup (immutable vault) | Backup and DR Service |
| Private connectivity | AWS Direct Connect / PrivateLink | Azure ExpressRoute / Private Link | Cloud Interconnect / Private Service Connect |

Shared responsibility sources: SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal/sources/source-register.csv`. All three agree on the split used here: for IaaS the provider owns facilities, hosts, and virtualization; for PaaS the provider also owns the runtime; for SaaS the provider owns the application. The customer always keeps identities, access decisions, data classification, and data.

## 6. Findings from the mapping
1. **Zoning, not encryption, is the GDP's weak point.** Encryption and keys are sound (SC-28, SC-12). The gap is that two covered entities' PHI share storage areas and the policy engine enforces purpose on only 61% of tables (AC-3, PT-3; P01 GR-01; POAM-006).
2. **The staging area breaks the de-identification promise** (AC-4). Identifiable SaaS data can land before de-identification runs. Moving de-identification into SYS-D3 removes the problem at the source (POAM-007).
3. **The model provider is a new external dependency** outside both landing zones (SA-9). It needs monitoring and per-patient request logging (AU-3) to support 164.410(c)(1) notices (POAM-018).
4. **Common controls are strong and reused.** One identity platform, one SIEM, one backup design. This is what lets group internal audit assess them once (P07). The weak link is documentation of inheritance for the Health Plan (P02, POAM-015), not the controls themselves.
5. **Two systems sit outside the platform.** The EHR relies on the vendor's SOC 2 report and contract (CP-9 provider), and the claims core relies on the colocation link and nightly extracts (AC-4). Both are covered by division-specific rows.
