# Cloud Architecture and Control Placement: Cris Santos Company | Construction | Small

**Organization:** Cris Santos Company, LLC (commercial and institutional building general contractor) | **Tier:** Small | **Provider:** Vendor-agnostic (see section 3)
**System:** Project Delivery and Payment Platform (PDPP), as defined in the SSP (P02). This is also the FCI boundary for CMMC Level 1.

## 1. Diagram

```mermaid
flowchart LR
  subgraph Field["Main office, yard, and 8 jobsites"]
    EP["Managed laptops and desktops<br/>SC-28, SI-3, AC-11"]
    TAB["Rugged tablets and commissioning laptops<br/>AC-19, IA-5 (gaps)"]
    FW["Main office firewall<br/>SC-7, SI-2"]
    RTR["Jobsite cellular routers<br/>CM-6 (gap)"]
  end
  subgraph SaaS["SaaS (provider-operated)"]
    IDP["Identity provider<br/>IA-2, IA-2(1), IA-2(2), AC-7"]
    MAIL["Productivity suite (email, files)<br/>SI-8, AU-2, AU-6"]
    PM["Project management platform<br/>AC-3, AC-2, CP-9"]
    ERP["ERP and accounting<br/>AC-5, AU-2"]
  end
  subgraph Tenant["Public cloud tenant (IaaS/PaaS)"]
    VPN["VPN gateway<br/>SC-8, AC-17"]
    subgraph Internal["Internal subnet"]
      FS["BIM/CAD file server + virtual desktops<br/>SI-3, CM-6, AC-3"]
      EST["Estimating database<br/>AC-3, SI-2"]
      FTP["File-transfer portal (internet-facing)<br/>SC-7, RA-5 (gap: wrong subnet)"]
    end
    BK[("Backup vault<br/>CP-9 (gap: same account)")]
    LOG["Cloud audit logging<br/>AU-2, AU-11"]
  end
  BANK["Bank portal (ACH, wire)"]
  AI["AI bid assistant (outside boundary)"]
  EP --> FW
  EP -->|SSO + MFA| IDP
  TAB --> RTR
  RTR -->|internet| PM
  IDP --> MAIL
  IDP --> PM
  IDP --> ERP
  FW -->|IPsec| VPN
  VPN --> FS
  VPN --> EST
  DES["Design teams and subcontractors"] -->|HTTPS| FTP
  FTP --- FS
  ERP -->|ACH file| BANK
  EST -.->|bid documents (FCI, gap)| AI
  FS --> BK
  EST --> BK
  FS --> LOG
```

## 2. Layers
| Layer | Components | Key controls | Responsibility |
|---|---|---|---|
| Identity | Identity provider, cloud IAM roles | AC-2, IA-2, IA-2(1), IA-2(2), IA-2(8), AC-7, AC-6 | Customer (configuration), provider (service) |
| Network / edge | Main office firewall, jobsite routers, site-to-site VPN, cloud subnets and rules | SC-7, SC-8, AC-17, CM-6 | Customer |
| Compute / application | File server and virtual desktops, estimating database, file-transfer portal | CM-6, SI-2, SI-3, RA-5, AC-3 | Customer (guest OS and application) |
| Data | Cloud disks and object storage, backup vault | SC-28, CP-9, CP-4 | Shared: provider encrypts; customer configures keys, retention, and isolation |
| Logging / monitoring | Cloud audit logs, identity sign-in logs, mailbox audit logs, ERP change log | AU-2, AU-6, AU-11 | Shared: provider generates; customer enables, retains, and reviews |
| SaaS applications | Productivity suite, project management platform, ERP | AC-3, AC-5, SI-8, CP-9 | Provider (application and infrastructure); customer (users, roles, data, mail policy) |
| Physical / hypervisor | Provider data centers | PE family | Provider (inherited) |

## 3. Service categories and provider equivalents
The company's design is independent of the provider. This table gives each provider's name for each service category, to use when reading its shared responsibility documentation.

| Service category | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|
| Virtual machines (including GPU) | Amazon EC2 | Azure Virtual Machines | Compute Engine |
| Object storage | Amazon S3 | Azure Blob Storage | Cloud Storage |
| Backup service | AWS Backup | Azure Backup | Backup and DR Service |
| Identity and access management | AWS IAM | Azure role-based access control with Microsoft Entra ID | Cloud IAM |
| Network segmentation | VPC subnets and security groups | Virtual network subnets and network security groups | VPC subnets and firewall rules |
| Audit logging | AWS CloudTrail | Azure Monitor activity log | Cloud Audit Logs |
| Site-to-site VPN | AWS Site-to-Site VPN | Azure VPN Gateway | Cloud VPN |

Shared responsibility sources: SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal/sources/source-register.csv`. All three models agree on the split used here:
- **IaaS:** the provider owns physical facilities, hosts, and the virtualization layer. The customer owns the guest operating system, applications, network configuration, identities, and data.
- **SaaS:** the provider also owns the application. The customer keeps identities, access, data, devices, and tenant settings such as mail authentication policy.

**FCI and cloud providers.** FAR 52.204-21 and CMMC Level 1 do not require FedRAMP-authorized services. That requirement applies to covered defense information under DFARS 252.204-7012(b)(2)(ii)(D), which does not apply today (P03 G-034). The company must still control which external systems hold FCI (52.204-21(b)(1)(iii)).

## 4. Findings from the mapping
1. **Public component on the internal subnet (SC-7; FAR 52.204-21(b)(1)(xi)).** The file-transfer portal accepts connections from the internet and sits in the same subnet as the BIM/CAD file server and estimating database. This is a CMMC Level 1 blocker. Fix: move it to its own public subnet. Allow only its one sync path to the file server, and deny everything else. Tracked as P03 G-013, P01 R-020, and P07 POAM-008.
2. **Business email compromise leaves few traces today (AU-2, AU-6, AU-11).** The identity provider and productivity suite record sign-ins, inbox rules, and forwarding changes. Nobody reviews them, and they roll off after 30 to 90 days. For a business email compromise, those logs are the main evidence. Fix: enable mailbox auditing for all users, export to a 1-year log workspace in the tenant, and run a weekly MSP review with alerts for new forwarding rules. Tracked as P07 POAM-005.
3. **Backup isolation (CP-9).** The backup vault shares the production account, region, and administrator roles. Fix: separate account, immutable retention, second region. Tracked as P01 R-006 and P07 POAM-017.
4. **FCI leaves the boundary (AC-20).** Bid documents flow from the estimating database to the AI bid assistant under standard terms (dotted line in the diagram), and email can auto-forward to personal accounts. Both put FCI on systems outside the CMMC scope. Tracked as P03 G-003 and G-024.
5. **Inherited controls rely on vendor SOC 2 reports.** Controls marked "Provider" or "Shared" for the project management platform depend on its SOC 2 Type 2 report, reviewed in P09. That report lists controls the company must run. One of them, removing users promptly, is an open gap (212 stale external accounts).
