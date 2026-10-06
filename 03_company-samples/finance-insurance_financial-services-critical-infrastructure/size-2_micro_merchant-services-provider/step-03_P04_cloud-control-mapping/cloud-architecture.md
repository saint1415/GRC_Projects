# Cloud Architecture and Control Placement: Cris Santos Company | Financial Services | Micro

**Organization:** Cris Santos Company, LLC (merchant services provider, an ISO) | **Tier:** Micro | **Provider:** Vendor-agnostic SaaS plus one cloud workload (see section 3)
**System:** Merchant Payments Platform (MPP), as defined in the SSP (P02) | **Prepared:** 2026-07-24 by the Operations Manager with the MSP lead technician | **Approved:** Owner, 2026-08-31

## 1. Diagram
The company runs no servers of its own except one: the website and application intake (SYS-08), a small cloud workload built by a freelance web developer. Everything else is SaaS, the processor partner's platform, or MSP-managed devices.

```mermaid
flowchart LR
  subgraph Office["Office or home (MSP-managed)"]
    SUP["2 support laptops<br/>keyed entry (CDE)<br/>SC-28, SI-3, SI-2"]
    LAP["5 other laptops + 2 spares<br/>SC-28, SI-3"]
    FW["Firewall, staff Wi-Fi,<br/>guest Wi-Fi<br/>SC-7, AC-18, RA-5 (ASV)"]
    POI["About 40 spare terminals<br/>locked cabinet<br/>CM-8"]
  end
  subgraph PP["Processor partner (provider-operated)"]
    GW["Gateway reseller console<br/>log in as merchant, payment page<br/>settings, fraud filters<br/>IA-2(1), AC-2, AU-6, SI-7, CM-3"]
    PORTAL["Partner portal<br/>boarding, residuals, chargebacks<br/>IA-2(1), IA-8"]
    PROC[("Authorization, settlement,<br/>hosted payment pages")]
  end
  subgraph SaaS["Vendor SaaS"]
    CRM["CRM and merchant files<br/>IA-2(1), SC-28, SI-12"]
    SUITE["Productivity suite<br/>SC-8, AU-11"]
    PHONE["Cloud phone + recording<br/>IA-2, SC-28, SC-8"]
    BK[("Suite backup (MSP)<br/>CP-9")]
  end
  subgraph Workload["Cloud workload (company-owned)"]
    WEB["Website + application form<br/>SI-2, AC-2, IA-5"]
    BUCKET[("Upload bucket<br/>SC-28, SI-12, AU-2")]
  end
  RMM["MSP remote management<br/>AC-17"]
  MER["Merchant (phone)"] -->|card details spoken| PHONE
  SUP -->|TLS| GW
  SUP --> FW
  LAP --> FW
  FW -->|TLS + MFA| SUITE
  FW -->|TLS + MFA| CRM
  FW -->|TLS| GW
  FW -->|TLS + MFA| PORTAL
  GW --> PROC
  SUITE -->|daily copy| BK
  AGT["Outside agents"] -.->|applications by email (gap)| SUITE
  AGT -->|MFA| CRM
  APP["Merchant applicants"] -->|upload| WEB
  WEB --> BUCKET
  RMM -->|agent on every laptop| SUP
  RMM --> LAP
```

## 2. Layers and who is responsible
| Layer | Components | Key controls | Customer (company) | MSP (on the company's behalf) | Provider |
|---|---|---|---|---|---|
| Identity | Console, portal, CRM, suite, phone, hosting accounts | AC-2, IA-2, IA-2(1), IA-5 | Decides who gets access; enrolls MFA; removes leavers and agents; owns the hosting login | Creates suite accounts; holds firewall admin | Runs sign-in and MFA services |
| Payment settings | Hosted payment page content, merchant users, fraud filters (SYS-01) | SI-7, CM-3, AC-6 | Decides and records every change it makes for a merchant | None | Hosts and protects the page and platform |
| Network | Firewall, Wi-Fi, internet | SC-7, AC-18, RA-5 | Approves changes; buys the ASV scan | Configures, patches, and monitors | Not applicable |
| Endpoints | 9 laptops | SC-28, SI-2, SI-3, AC-11 | Approves patch exceptions; keeps the inventory | Encryption, antivirus, patching, screen lock | Not applicable |
| SaaS applications | CRM, suite, phone | SC-8, SC-28, AU-2 | Users, sharing, recording, mail rules, retention | Suite administration on request | Application, platform, data centers |
| Cloud workload | Web server and upload bucket (SYS-08) | SI-2, IA-5, SC-28, SI-12, AU-2 | **Everything above the platform**: plugins, keys, bucket settings, retention, logging | None today | Physical hosts, hypervisor, storage service |
| Data | Merchant files, recordings, backups | SC-28, SI-12, CP-9 | Retention and restore testing | Operates the backup and runs restore tests | Encrypts and backs up its own platform |
| Logging | Console audit log, suite logs, bucket logs | AU-2, AU-6, AU-11 | **Reviews logs weekly (gap today)** | Keeps firewall and antivirus logs | Generates and stores logs |
| Vendor governance | ISO agreement, vendor terms, AOCs | SA-9 | Keeps the service provider list, AOCs, and responsibility matrix | None | Provides AOCs and SOC 2 reports |

**The MSP is not a cloud provider in the shared responsibility sense.** It performs customer-side duties for the company. Anything marked "Customer" and performed by the MSP in `cloud-control-map.csv` remains the company's responsibility under PCI DSS (12.8) and the Safeguards Rule (16 CFR 314.4(f)). The company must direct the work, receive evidence, and check it.

**The processor partner is both a provider and the company's customer.** It provides the gateway and portal, and its PCI DSS AOC covers its platform. But it also relies on the company, under the ISO agreement, to keep console access and payment page content safe. If an attacker changes a hosted payment page through a company console account, the processor partner's controls did their job and the company's did not.

## 3. Service categories and provider equivalents
The design is vendor-agnostic. For SaaS, all three major cloud providers' shared responsibility models put the application and platform on the provider and keep identities, access, data, and devices with the customer. For the website, which runs on infrastructure-level hosting (one virtual server and object storage), the customer also owns the operating system, application, plugins, keys, and storage settings (SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal-framework/sources/source-register.csv`).

| Service category used | What it is here | Equivalent category in the large cloud providers (for reading their documentation) |
|---|---|---|
| Payment gateway (provider SaaS) | Processor partner's console, portal, hosted payment pages | Third-party payment service integrated with any provider |
| Line-of-business SaaS | CRM, cloud phone | Industry SaaS built on any provider |
| Productivity suite | Email, files, chat | Productivity and collaboration SaaS |
| SaaS-to-SaaS backup | Suite backup | Backup service or third-party SaaS backup |
| Virtual server | Website and form | Virtual machine or compute instance |
| Object storage | Upload bucket | Object storage service |
| Remote monitoring and management | MSP laptop management | Device management SaaS |

## 4. Findings from the mapping
1. **The weakest layer is identity on the payment console.** The console is the one place where the company can change what about 120 merchants' customers see when they pay, and 4 of 6 accounts have no MFA (IA-2(1)). This is the entry point in the P08 scenario. Fix: MFA required for every console account by 2026-09-15 (P01 R-001, R-002; POAM-002).
2. **The company has no record of what it puts on payment pages (SI-7, CM-3).** The processor partner protects its hosted payment page, but the custom header field accepts whatever the company types into it. P07 found third-party analytics scripts on 2 merchants' pages that nobody approved (R-022). Fix: script inventory, approval, and monthly comparison; confirm with the processor partner whether its change-detection covers custom header content.
3. **The one cloud workload is fully the company's responsibility and nobody owns it.** The web developer holds the only login, the bucket access key has full rights and sits in a configuration file, the form plugin is out of date, bucket logging is off, and about 610 files with Social Security numbers have piled up since 2023 (R-005). Fix: move applications to the CRM's secure upload link, delete the bucket contents after export to the CRM, transfer the hosting login to the company, and rotate the key.
4. **Keyed entry pulls the office into PCI DSS scope.** Because the support laptops sit on the flat staff network, the firewall, Wi-Fi, and every device on it are in scope (SC-7). Stopping keyed entry (R-003) is cheaper than segmenting the network for 160 calls a month.
5. **The MSP's reach is total (AC-17).** Its remote tool can run commands on the keyed-entry laptops. The company has no evidence of how the MSP protects it. Fix: MSP security terms, technician list, and MFA evidence (R-011).
