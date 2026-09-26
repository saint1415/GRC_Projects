# Cloud Architecture and Control Placement: Cris Santos Company | Healthcare and Public Health | Small

**Organization:** Cris Santos Company, LLC (rural critical access hospital) | **Tier:** Small | **Provider:** Vendor-agnostic (see section 3)
**System:** Hospital Clinical Information System (HCIS), as defined in the SSP (P02)

## 1. Diagram
Every component in the diagram has at least one row in `cloud-control-map.csv` (40 rows, 18 components). Dashed boxes are planned.

```mermaid
flowchart LR
  subgraph Hospital["Hospital campus (on-premises, one flat network today)"]
    EP["Endpoints and downtime PCs<br/>SC-28, SI-3"]
    MD["Medical devices: CT, pumps, monitors, analyzers<br/>SA-22 (CT workstation)"]
    MDN["Medical device network (planned)<br/>SC-7"]
    OT["Building OT: nurse call, HVAC, med gas, generator<br/>CM-8"]
    FW["Hospital firewall and VPN<br/>SC-7, AC-17, SI-2"]
  end
  subgraph SaaS["SaaS (provider-operated)"]
    IDP["Identity provider<br/>IA-2, IA-2(1), IA-2(2), AC-2, AC-7"]
    EHR["Hosted EHR with sepsis model<br/>AC-3, AC-12, AU-3, AU-6, CP-9, SI-7"]
    OFF["Productivity suite<br/>SI-8, SC-8"]
  end
  subgraph Tenant["Public cloud tenant (IaaS/PaaS)"]
    IAM["Cloud IAM<br/>AC-2, AC-6"]
    VPN["VPN gateway<br/>SC-8"]
    NET["Cloud network rules<br/>SC-7"]
    IAV["Imaging archive VMs<br/>CM-6, SI-2, SI-3"]
    IAS[("Imaging archive storage<br/>SC-28, AC-3")]
    IE["Interface engine VM<br/>SC-8, SI-4, AU-12"]
    BK[("Backup vault<br/>CP-9, CP-4 (gap: same account)")]
    KMS["Key management<br/>SC-13"]
    LOG["Cloud audit logging<br/>AU-2, AU-6, AU-11"]
    DC["Provider data centers<br/>PE-3 (inherited)"]
  end
  EP --> FW
  MD -.-> MDN
  MDN -.-> FW
  OT --> FW
  EP -->|SSO + MFA| IDP
  IDP --> EHR
  IDP --> OFF
  IDP --> IAM
  FW -->|IPsec to EHR vendor| EHR
  FW -->|IPsec| VPN
  VPN --> NET
  NET --> IAV
  NET --> IE
  IAV --> IAS
  IAS --> KMS
  IE -->|HL7| EXT["Reference lab, HIE, state health department"]
  IAV -->|image route| TR["Teleradiology group (BA)"]
  TR -.->|shared support VPN, no MFA (gap)| FW
  EHR <-->|interfaces| IE
  IAV --> BK
  IE --> BK
  IAV --> LOG
  IE --> LOG
```

## 2. Layers
| Layer | Components | Key controls | Responsibility |
|---|---|---|---|
| Identity | Identity provider, cloud IAM | AC-2, AC-6, AC-7, IA-2, IA-2(1), IA-2(2) | Customer configures; provider runs the service |
| Network / edge | Hospital firewall and VPN, cloud VPN gateway, cloud network rules, planned medical device network | SC-7, SC-8, AC-17, SI-2 | Customer (the cloud gateway service itself is provider-run) |
| Compute / application | Imaging archive VMs, interface engine VM, endpoints, CT workstation | CM-6, SI-2, SI-3, SI-4, SA-22 | Customer (guest OS and applications) |
| Data | Imaging archive storage, backup vault, key management | SC-28, SC-13, AC-3, CP-9, CP-4 | Shared: provider encrypts and stores; customer sets keys, access, retention, and isolation |
| Logging / monitoring | Cloud audit logs, identity sign-in logs, EHR audit trail, interface engine logs | AU-2, AU-3, AU-6, AU-11, AU-12 | Shared: provider generates; customer retains and reviews |
| SaaS applications | Hosted EHR (with the sepsis model), productivity suite | AC-3, AC-12, AU-3, CP-9, SI-7, SI-8, SC-8 | Provider (application and infrastructure); customer (users, roles, data, review) |
| Building OT | Nurse call, HVAC, medical gas alarms, generator monitoring | CM-8 (inventory first) | Customer (Facilities Manager with OT vendors) |
| Physical / hypervisor | Provider data centers | PE family | Provider (inherited) |

## 3. Service categories and provider equivalents
The hospital's design does not depend on one provider. This table gives each provider's name for each service category, for use when reading its shared responsibility documentation.

| Service category | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|
| Virtual machines | Amazon EC2 | Azure Virtual Machines | Compute Engine |
| Object storage | Amazon S3 | Azure Blob Storage | Cloud Storage |
| Backup service | AWS Backup | Azure Backup | Backup and DR Service |
| Identity and access management | AWS IAM | Azure role-based access control with Microsoft Entra ID | Cloud IAM |
| Key management | AWS KMS | Azure Key Vault | Cloud KMS |
| Audit logging | AWS CloudTrail | Azure Monitor activity log | Cloud Audit Logs |
| Site-to-site VPN | AWS Site-to-Site VPN | Azure VPN Gateway | Cloud VPN |
| Network filtering | Security groups | Network security groups | VPC firewall rules |

Shared responsibility sources: SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal/sources/source-register.csv`. All three models agree on the split used here:
- **IaaS:** the provider owns physical facilities, hosts, and the virtualization layer. The customer owns the guest operating system, applications, network configuration, identities, and data.
- **SaaS:** the provider also owns the application. The customer keeps identities, access, data, and devices. For the EHR, the vendor's SOC 2 report lists the controls the hospital must run for the vendor's controls to work (P09).

## 4. Findings from the mapping
1. **Backup isolation (CP-9).** The backup vault shares the production account, region, and administrator roles, and the local backup appliance is joined to the hospital directory. A ransomware actor with domain or cloud administrator rights could delete both copies. Fix: a separate backup account with immutable retention in a second region, and take the appliance off the directory. Tracked as P01 R-003 and P07 POAM-003.
2. **The EHR's recovery time is the vendor's, and it is too long (CP-9).** The vendor states an RTO of 8 hours; the ED and inpatient processes need 2 hours (P05). No hospital control can shorten the vendor's recovery. The hospital closes the gap with downtime procedures and a contract discussion (P09 follow-up).
3. **Vendor access is the weakest edge (AC-17).** The teleradiology group's support connection enters through the hospital firewall on a shared account without MFA, then reaches the flat network, the archive route, and everything else. This is the initial access path in the P08 scenario. Fix: named vendor accounts through the identity provider with MFA, limited to the imaging segment. Tracked as P01 R-001 and POAM-008.
4. **One flat network (SC-7).** Medical devices, OT, servers, phones, and workstations share one network. The planned medical device network and OT segment are drawn dashed. Tracked as P01 R-001, R-007, R-008, R-033 and POAM-006.
5. **Log retention and review (AU-6, AU-11).** Cloud, identity, and interface engine logs use default retention and nobody reviews them. Fix: export to a central log workspace with 1-year retention and weekly review.
6. **Inherited controls rely on vendor SOC 2 reports.** Rows marked Provider depend on the EHR, identity, productivity, and cloud providers' reports. The EHR report is reviewed in P09.
