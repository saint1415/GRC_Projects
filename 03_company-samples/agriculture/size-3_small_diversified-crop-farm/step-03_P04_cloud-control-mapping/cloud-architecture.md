# Cloud Architecture and Control Placement: Cris Santos Company | Agriculture | Small

**Organization:** Cris Santos Company, LLC (diversified precision-agriculture crop farm) | **Tier:** Small | **Provider:** Vendor-agnostic (see section 3)
**System:** Farm Management and Irrigation Control Platform (FMICP), as defined in the SSP (P02)

## 1. Diagram
The diagram shows the environment **as found in July 2026**. Items marked "gap" are on the POA&M (P07). The dashed line from the integrator is the always-on remote access path that the redesign removes.

```mermaid
flowchart LR
  subgraph HQ["Headquarters and pump house (on-premises, one flat network today)"]
    EP["Office laptops and desktops, tablets<br/>AC-11, SC-28, SI-3, CM-6"]
    FW["Headquarters firewall<br/>SC-7, AC-4 (gap: no internal zones)"]
    HMI["SCADA HMI workstation + data collector<br/>IA-2, SI-2, CM-7 (gaps)"]
    PLC["PLC: 3 well pumps, 2 fertigation pumps<br/>CM-3, CM-5, CP-9 (gaps)"]
    LW["LoRaWAN gateway<br/>IA-5 (gap: default password)"]
    WIFI["Packing shed Wi-Fi<br/>AC-18"]
  end
  subgraph Field["Fields (North Block and Home Block)"]
    PIV["5 pivot panels with cellular modems<br/>IA-5, PE-3 (gaps)"]
    SEN["Probes, flow meters, weather stations,<br/>valve controllers"]
  end
  subgraph SaaS["SaaS (provider-operated)"]
    IDP["Identity provider<br/>IA-2, IA-2(1), AC-7"]
    FMIS["FMIS: farm records, tally,<br/>irrigation module<br/>AC-3, AU-3, CP-9, SI-7"]
    OFF["Productivity suite<br/>AC-3, SC-28"]
  end
  subgraph Tenant["Public cloud tenant (IaaS/PaaS)"]
    HUB["Farm data hub VM<br/>CM-6, SI-2, SC-7"]
    IMG[("Imagery object storage<br/>SC-28, AC-3")]
    BK[("Backup vault<br/>CP-9 (gap: same account and region)")]
    LOG["Cloud audit logging<br/>AU-2, AU-11"]
  end
  INT["Irrigation integrator<br/>(remote support)"]
  AIV["Agronomy analytics SaaS<br/>(AI-001)"]
  EP --> FW
  HMI --- PLC
  WIFI --- FW
  HMI --- FW
  SEN --> LW --> FW
  EP -->|SSO + MFA| IDP
  IDP --> FMIS
  IDP --> OFF
  PIV <-->|carrier private network| FMIS
  FW -->|collector data, unencrypted (gap)| HUB
  HUB -->|API over TLS| FMIS
  INT -.->|always-on remote tool, shared account (gap)| HMI
  IMG -->|orthomosaics| AIV
  HUB --> BK
  HUB --> LOG
```

## 2. Layers
| Layer | Components | Key controls | Responsibility |
|---|---|---|---|
| Identity | Identity provider, SYS-01 accounts, cloud IAM roles, HMI and remote tool accounts | AC-2, IA-2, IA-2(1), IA-5, IA-8, AC-7 | Customer (configuration and accounts); provider (service) |
| Network / edge | Headquarters firewall, internal network, packing shed Wi-Fi, LoRaWAN gateway, pivot modems, cloud network rules | SC-7, AC-4, AC-18, SC-8 | Customer (farm network and cloud rules); carrier (private cellular network) |
| OT | PLC, HMI, pivot panels, valve controllers, sensors | CM-3, CM-5, SI-2, MA-4, CP-9 | Customer, with the integrator as maintainer (SP 800-82 Rev. 3) |
| Compute / application | Farm data hub VM | CM-6, SI-2, SI-3 | Customer (guest operating system and application) |
| Data | Imagery object storage, VM disks, backup vault | SC-28, CP-9, SC-13 | Shared: provider encrypts; customer configures keys, retention, and isolation |
| Logging / monitoring | Cloud audit logs, identity provider sign-in logs, SYS-01 audit trail | AU-2, AU-6, AU-11, AU-12, SI-4 | Shared: provider generates; customer retains and reviews |
| SaaS applications | FMIS (SYS-01), productivity suite | AC-3, AU-3, CP-9, SI-7 | Provider (application and infrastructure); customer (users, roles, data, configuration such as irrigation alerts) |
| Physical / hypervisor | Provider data centers | PE family | Provider (inherited) |

## 3. Service categories and provider equivalents
The farm's design is independent of the provider. This table gives each provider's name for each service category, to use when reading its shared responsibility documentation.

| Service category | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|
| Virtual machines | Amazon EC2 | Azure Virtual Machines | Compute Engine |
| Object storage | Amazon S3 | Azure Blob Storage | Cloud Storage |
| Backup service | AWS Backup | Azure Backup | Backup and DR Service |
| Identity and access management | AWS IAM | Azure role-based access control with Microsoft Entra ID | Cloud IAM |
| Key management | AWS KMS | Azure Key Vault | Cloud KMS |
| Audit logging | AWS CloudTrail | Azure Monitor activity log | Cloud Audit Logs |
| Site-to-site VPN (planned) | AWS Site-to-Site VPN | Azure VPN Gateway | Cloud VPN |
| Network filtering | Security groups | Network security groups | VPC firewall rules |

Shared responsibility sources: SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal-framework/sources/source-register.csv`. All three models agree on the split used here:
- **IaaS:** the provider owns physical facilities, hosts, and the virtualization layer. The customer owns the guest operating system, applications, network configuration, identities, and data.
- **SaaS:** the provider also owns the application. The customer keeps identities, access, data, configuration, and devices.
- **OT is always the farm's.** No cloud shared responsibility model covers the PLC, HMI, or field devices. SP 800-82 Rev. 3 (SRC-800-82) is the reference for those rows.

## 4. Findings from the mapping
1. **The cloud edge is the OT edge (SC-7, SC-8).** The data collector on the HMI sends pump, flow, and weather data to the data hub VM over the internet without encryption. The VM accepts that traffic only from the farm's public IP address (confirmed in the network rule export), which limits exposure, but the data is readable in transit and the HMI needs an internet path. Fix: site-to-site VPN from the headquarters firewall to the tenant, and move the collector to a small OT gateway on the segmented OT network so the HMI itself has no internet route. Tracked as P01 R-022 and POAM-006.
2. **Backup isolation (CP-9).** The backup vault shares the production account, region, and administrators. Fix: a separate backup account with immutable retention in a second region, plus a monthly SYS-01 record export and versioned PLC and HMI program backups. Tracked as P01 R-003 and R-015, and POAM-003.
3. **SaaS configuration is the farm's job (SI-4, AU-6).** SYS-01 can alert on irrigation schedule and setpoint changes, but the alerts are switched off. Turning them on is a customer responsibility and costs nothing. Tracked as POAM-011.
4. **Inherited controls rely on vendor SOC 2 reports.** Rows marked "Provider" for SYS-01 depend on the FMIS vendor's SOC 2 Type 2 report, reviewed in P09. Its complementary user entity controls (MFA, user removal, audit review) are open gaps at the farm.
5. **Imagery storage (AC-3).** The bucket holding drone orthomosaics is private and shared with the AI vendor through a time-limited signed link per upload (confirmed). Keep it that way; do not make the bucket public for convenience.
