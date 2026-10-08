# Cloud Architecture and Control Placement: Cris Santos Company Holdings | Utilities | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector | **Providers:** two public cloud providers, called provider A and provider B (vendor-agnostic; see section 6)
**Scope:** the shared corporate cloud platform (SYS-G3 landing zones), the cloud-hosted part of the shared OT remote access platform (SYS-G4), and the division workloads that run in the cloud or as SaaS. The SSP system (P02) is the Distribution Operations Platform, which is **on premises**; this document shows where it touches the cloud.

## 1. Design in one paragraph
Corporate runs one **landing zone** per provider: identity federation from SYS-G1, a hub network, guardrail policies, a central log archive, key management, EDR, and an immutable backup vault. Divisions get their own **accounts** inside the landing zone and inherit these guardrails. Provider A hosts the corporate hub, the group data platform, the Electric Utility's load-forecasting workload (SYS-E6) and customer outage map, Gas Production's production data, and the **SYS-G4 broker and policy engine**. Provider B hosts Engineering Services' client project platform (SYS-S1) and the backup vault. Several division systems are vendor SaaS (the AMI head-end SYS-E4, the CIS SYS-E5, Gas Production's accounting system SYS-N2). **No OT control system runs in the cloud.** The DOP, the TCC EMS, substations, and the Gas Production field SCADA stay on premises; the only cloud-to-OT path is SYS-G4, whose on-premises connectors make outbound-only connections to the broker.

## 2. Diagrams
### 2.1 Group landing zone, shared OT access, and division workloads

```mermaid
flowchart TB
  subgraph Common["Common controls (corporate; inherited by all divisions)"]
    IDP["Group identity platform SYS-G1<br/>IA-2(1), AC-2, AC-6(5), AC-7"]
    IAM["Cloud IAM, providers A and B<br/>AC-3"]
    HUB["Landing-zone hub network<br/>SC-7, SC-7(5), SC-8"]
    GRD["Guardrail policy service<br/>CM-6, CM-7"]
    LOG[("Central log archive<br/>AU-9, AU-11")]
    SOC["Group SIEM and SOC SYS-G2<br/>SI-4, AU-6"]
    EDR["Workload protection (EDR)<br/>SI-3"]
    KMS["Key management<br/>SC-12, SC-28"]
    BK[("Immutable backup vault, provider B<br/>CP-9, CP-6")]
    DC["Provider data centers<br/>PE-3 (inherited)"]
  end
  subgraph G4["Shared OT remote access SYS-G4"]
    BRK["Broker and policy engine (provider A)<br/>AC-17, AC-17(1), AC-17(2), MA-4, AU-12"]
  end
  subgraph EUC["Electric Utility accounts (provider A)"]
    LF["Load-forecasting workload SYS-E6<br/>CM-3, SI-10, AC-6"]
    MAP["Customer outage map<br/>AC-22, SC-5"]
  end
  AMI["AMI head-end SYS-E4 (vendor SaaS)<br/>SA-9 provider, AC-6 customer"]
  CIS["CIS and portal SYS-E5 (vendor SaaS)<br/>SC-28 provider, IA-2 shared"]
  subgraph GPC["Gas Production"]
    PDATA["Production data (provider A)<br/>AC-3"]
    ACCT["Accounting and royalty SYS-N2 (vendor SaaS)<br/>SA-9, IA-2(1), AC-4"]
  end
  subgraph ESC["Engineering Services accounts (provider B)"]
    S1["Client project platform SYS-S1<br/>AC-3, AC-6, SC-28, CP-9, AU-12, AC-4, CM-6"]
  end
  GAI["Generative AI design assistant (third-party SaaS, pilot)<br/>SA-9, AC-4"]
  subgraph OT["On premises OT (not in the cloud)"]
    DOP["Distribution Operations Platform SYS-E1<br/>(see 2.2)"]
    SUB["74 transmission substations SYS-E3<br/>(low impact BES Cyber Systems)"]
    POC["Gas Production POC SYS-N1"]
    TCC["TCC EMS SYS-E2 (medium impact)<br/>own CIP-005 Intermediate System"]
  end
  IDP --> IAM
  IDP -->|MFA for remote users| BRK
  IAM --> EUC
  IAM --> GPC
  IAM --> ESC
  HUB --> EUC
  HUB --> ESC
  BRK <-->|outbound-only connectors, AC-17(3)| DOP
  BRK <-->|vendor access, CIP-003-9 Sec. 6| SUB
  BRK <-->|support sessions| POC
  DOP -->|outage feed (gap: bypasses DMZ)| MAP
  AMI -->|outage events via DMZ| DOP
  CIS <-->|premise and call data via DMZ| DOP
  S1 -.->|client documents (gap: no client consent)| GAI
  EUC --> LOG
  ESC --> LOG
  GPC --> LOG
  BRK --> LOG
  LOG --> SOC
  ESC --> BK
  EUC --> BK
  GRD -.-> EUC
  GRD -.-> GPC
  GRD -.-> ESC
  KMS -.-> S1
  EDR -.-> LF
  DC -.-> HUB
```

### 2.2 Distribution Operations Platform boundary (SSP system) and its outside connections

```mermaid
flowchart LR
  subgraph DOPB["DOP boundary (DCC and backup DCC, on premises)"]
    ADMS["ADMS clusters: SCADA, DMS, OMS<br/>AC-3, AU-3, CP-9 (gap: backups not isolated)"]
    CON["64 operator consoles<br/>IA-2, SA-22 (gap: 22 unsupported)"]
    FEP["8 front-end processors<br/>SC-8, CM-7"]
    subgraph DMZ["OT DMZ"]
      JH["SYS-G4 jump hosts<br/>AC-17(3), AU-12"]
      INT["AMI and CIS integration servers<br/>AC-4"]
      HR["Historian replica"]
    end
    FW["IT/OT firewalls<br/>SC-7 (gap: 37 broad rules)"]
    DSUB["446 distribution substation gateways<br/>CM-8 (gap: inventory)"]
  end
  SUB["74 transmission substation gateways<br/>(low impact BES Cyber Systems)<br/>CIP-003-9 Sec. 3.1"]
  EMS["TCC EMS SYS-E2<br/>(medium impact ESP)"]
  CORP["Corporate network"]
  BRK["SYS-G4 broker (provider A)"]
  CON --> ADMS
  ADMS --> FEP
  FEP -->|DNP3, private LTE and fiber| DSUB
  FEP -->|DNP3 (gap: any protocol allowed)| SUB
  EMS -->|one-way data diode| HR
  JH --> ADMS
  BRK --> JH
  INT --> ADMS
  CORP --> FW
  FW --> DMZ
  ADMS -.->|gap: OMS feeds bypass the DMZ| CORP
```

**Target state (POAM-001, POAM-005, POAM-003, POAM-009):** every SYS-G4 session to the DOP needs DCC approval and a work order, with separate entitlements per OT environment; all DOP traffic to and from the corporate network passes through the OT DMZ under deny-by-default rules; network sensors in both DCC networks feed the group SOC; DOP backups get an offline, immutable copy. Gateway rules at the 74 transmission substations allow only DNP3 from the FEPs (POAM-014).

## 3. Tenancy and identity decision
- **Decision.** SYS-G1 holds the IT identities of all three divisions, and divisions get their own accounts inside the landing zone. SYS-G1 is not used inside the CIP Electronic Security Perimeters.
- **Separate OT identity.** The DOP has its own OT domain, separate from SYS-G1. Gas Production's field SCADA has a separate OT domain. The TCC EMS has its own CIP-005 Intermediate System. Remote users authenticate at the SYS-G4 gateway through SYS-G1 with MFA, then to the jump host with their OT domain account.
- **Why.** No OT control system runs in the cloud, and the only cloud-to-OT path is SYS-G4. OT access is a shared system, but each OT owner decides who may reach its environment.
- **What limits blast radius.** SYS-G4 connectors make outbound-only connections, every session is recorded, and vendors connect only through SYS-G4 with MFA. Just-in-time PAM elevation for cloud and IT administration. The backup vault uses a separate backup identity and holds no OT backups. The load-forecasting workspace has no access from the DOP.
- **Known gaps.** 230 Engineering Services accounts have standing access to all three OT environments (GR-01, POAM-001). The DOP has 14 broad OT domain administrator accounts (GR-10). Malicious-communication detection on vendor sessions covers 31 of 74 substations (POAM-013).
- **Cross-division risks:** GR-01, GR-07, GR-08, GR-10 in [risk-register.csv](../step-04_P01_risk-register/risk-register.csv).

## 4. Common versus division-specific controls
`cloud-control-map.csv` has 50 rows across 21 components. The `control_scope` column shows who owns each placement:

| Scope | Rows | What it means |
|---|---|---|
| Common (group) | 20 | Provided once by corporate (SYS-G1, SYS-G2, SYS-G3) and inherited by every division account. Listed in the P02 common control catalog |
| Shared system (SYS-G4 OT remote access) | 7 | One corporate system that reaches three divisions' OT environments |
| Division-specific (Electric Utility) | 10 | Load forecasting, outage map, AMI and CIS SaaS, the DOP-to-cloud interface |
| Division-specific (Gas Production) | 4 | Accounting SaaS and production data |
| Division-specific (Engineering Services) | 9 | Client project platform and the AI design assistant pilot |

| Responsibility | Rows |
|---|---|
| Customer (the group or a division) | 38 |
| Shared (provider and group) | 7 |
| Provider | 5 |

**Rule of thumb.** Identity, network guardrails, logging, keys, backups, and EDR are **common**. A division cannot opt out of them, only request an exception through POL-01. **OT access is a shared system, not a common control:** it is operated centrally, but each OT owner decides who may reach its environment and when. Application behavior and data access inside each application are **division-specific**, because they depend on each division's regulators and clients.

## 5. Layers
| Layer | Common components | Division components | Key controls | Responsibility |
|---|---|---|---|---|
| Identity | SYS-G1, cloud IAM, SYS-G4 broker | AMI and CIS roles, SYS-S1 permissions, SYS-N2 federation | AC-2, AC-3, AC-6, AC-17, IA-2, IA-2(1) | Customer (configuration); vendor (service) |
| Network | Hub network; SYS-G4 outbound-only connectors | Outage map front end; DOP-to-cloud interface | SC-7, SC-7(5), SC-8, AC-17(3), AC-4, SC-5 | Customer, with provider DDoS protection shared |
| Compute | EDR, guardrails | Forecasting workspace; SYS-S1 | SI-3, CM-3, CM-6, CM-7 | Customer (guest OS, containers, code) |
| Data | Keys, backup vault | SYS-S1 CEII and BCSI; CIS customer data; royalty exports | SC-12, SC-28, CP-9, CP-6, AC-4 | Shared: provider encrypts; group owns keys, access, and retention |
| Logging and monitoring | Log archive, SIEM | SYS-G4 session records; SYS-S1 file events | AU-6, AU-9, AU-11, AU-12, SI-4 | Shared: providers generate platform logs; group retains and reviews |
| SaaS dependencies | Identity, SIEM, and EDR vendors | AMI, CIS, accounting, AI assistant vendors | SA-9 | Provider for the service; customer for use and oversight |
| Physical | Provider data centers | None in the cloud; OT facilities are covered in P02 | PE-3 | Provider (inherited) |

## 6. Service categories and provider equivalents
The design does not depend on a provider. This table gives each provider's name for each service category, for reading its shared responsibility documentation.

| Service category | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|
| Account structure and guardrails | AWS Organizations with service control policies | Management groups with Azure Policy | Resource hierarchy with Organization Policy |
| Managed containers (SYS-G4 broker) | Amazon EKS | Azure Kubernetes Service | Google Kubernetes Engine |
| Data science workspace (SYS-E6) | Amazon SageMaker | Azure Machine Learning | Vertex AI |
| Object storage | Amazon S3 | Azure Blob Storage | Cloud Storage |
| Key management | AWS KMS | Azure Key Vault | Cloud KMS |
| Audit logging | AWS CloudTrail | Azure Monitor activity log | Cloud Audit Logs |
| Backup with immutability | AWS Backup (vault lock) | Azure Backup (immutable vault) | Backup and DR Service |
| DDoS protection | AWS Shield | Azure DDoS Protection | Cloud Armor |

Shared responsibility sources: SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal-framework/sources/source-register.csv`. All three agree on the split used here: for IaaS the provider owns facilities, hosts, and virtualization; for PaaS the provider also owns the runtime; for SaaS the provider owns the application. The customer always keeps identities, access decisions, data classification, and data.

## 7. Findings from the mapping
1. **The riskiest cloud component is the one that touches OT.** The SYS-G4 broker is well built (MFA, encryption, recording, outbound-only connectors), but one Engineering Services role reaches the DOP, the substations, and the Gas Production POC (AC-6, AC-17; P01 GR-01; POAM-001).
2. **The DOP leaks to the cloud outside its DMZ.** The outage map feed leaves the DOP directly (AC-4). It carries only aggregate counts, but the path is a way in (POAM-005).
3. **Client CEII and BCSI need their own access model** on SYS-S1 (AC-3, AC-6). Encryption and backups are sound; inherited project-wide permissions are not (POAM-020). The same platform holds the Electric Utility's own TCC BCSI, which brings CIP-004-7 R6 into a cloud document platform (P03; POAM-015).
4. **Provider B guardrails are incomplete** for two non-production SYS-S1 accounts (CM-6; P01 GR-19).
5. **Common controls are strong and reused.** One identity platform, one SIEM, one backup design, one key service. This is what lets group internal audit assess them once (P07). The weak links are where a division's regulator or clients add requirements the common controls were not designed for.
