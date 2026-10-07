# Cloud Architecture and Control Placement: Cris Santos Company | Wholesale Trade | Micro

**Organization:** Cris Santos Company, LLC (IT hardware and software reseller) | **Tier:** Micro | **Provider:** Vendor-agnostic SaaS (see section 3)
**System:** Reseller Operations Platform (ROP), as defined in the SSP (P02) | **Prepared:** 2026-07-24 by the Operations Manager with the MSP lead technician | **Approved:** Owner, 2026-08-31

## 1. Diagram
The company runs no servers and no IaaS tenant. Its "cloud" is a set of SaaS services plus one cloud workload that the MSP operates for it: the SaaS-to-SaaS backup of the productivity suite (SYS-05). FCI flows are marked; there is no CUI.

```mermaid
flowchart LR
  subgraph Office["Office and stockroom (on-premises, MSP-managed)"]
    EP["8 laptops<br/>SC-28, SI-3, AC-11"]
    BE["Setup bench desktop<br/>customer devices connect here<br/>SC-28 gap, IA-2 gap"]
    CAM["Cameras and recorder<br/>CM-8 (covered unit replaced)"]
    FW["Firewall, staff Wi-Fi,<br/>separate guest Wi-Fi<br/>SC-7, SI-2, IA-2(1)"]
  end
  subgraph SaaS["Vendor SaaS (provider-operated)"]
    ERP["ERP + customer portal<br/>orders, inventory, serials<br/>AC-2, AC-3, AU-2, CP-9"]
    SUITE["Productivity suite<br/>email + Orders folder (FCI)<br/>AC-3, IA-2(1), AC-20"]
  end
  subgraph Workload["Cloud workload (MSP-operated)"]
    BK[("Suite backup<br/>30 days of versions<br/>CP-9, CP-4, IA-2(1)")]
  end
  subgraph MSP["MSP"]
    RMM["RMM platform<br/>AC-17, SI-2, SI-3"]
  end
  subgraph Ext["External services (outside the boundary)"]
    SP["Distributor and OEM portals<br/>IA-2 gap, SR-3"]
    BANK["Business banking"]
    AISUB["ERP AI subprocessor<br/>SA-9 (see P10)"]
  end
  DOD["DoD contracting offices<br/>and the Federal Prime"]
  EP --> FW
  BE --> FW
  CAM --> FW
  FW -->|TLS + MFA| ERP
  FW -->|TLS + MFA| SUITE
  DOD -->|POs and equipment lists (FCI)| SUITE
  SUITE -->|nightly copy| BK
  RMM -->|agent on every computer| EP
  RMM --> BE
  ERP -->|order history incl. DoD orders| AISUB
  EP -->|orders, drop-ship| SP
  EP -->|supplier payments| BANK
```

## 2. Layers and who is responsible
| Layer | Components | Key controls | Customer (company) | MSP (on the company's behalf) | Provider (SaaS vendor) |
|---|---|---|---|---|---|
| Identity | ERP, suite, backup, firewall, and supplier portal logins | AC-2, IA-2, IA-2(1), IA-5 | Decides who gets access; removes it; ends shared logins | Creates and disables suite and laptop accounts; holds backup and firewall admin logins | Runs the sign-in and MFA services |
| Network | Firewall, Wi-Fi, internet line, bench port | SC-7, SI-2 | Approves changes; decides on the bench segment | Configures, patches, and monitors | Not applicable |
| Endpoints | 8 laptops, setup bench, scanners | SC-28, SI-3, SI-2, AC-11 | Approves exceptions (bench lock); keeps the inventory | Encryption, endpoint protection, patching, screen lock | Not applicable |
| SaaS applications | ERP and customer portal, suite | AC-3, AU-2, SC-8 | Users, roles, folder permissions, forwarding rules | Suite administration on request | Application, platform, data centers |
| Data | Orders folder (FCI), ERP data, backup copies, bench files | CP-9, CP-4, SC-28, AC-3 | Decides who sees FCI, retention, and restore testing | Operates the backup and runs restore tests | Encrypts and backs up its own platform |
| Logging | ERP and suite logs, firewall logs | AU-2, AU-6 | **Reviews logs monthly (gap today)** | Keeps firewall logs; forwards alerts | Generates and stores logs |
| Vendor and supply chain governance | Contracts, SOC 2 review, MSP review, supplier terms | SA-9, SR-3 | Reviews SOC 2 and MSP evidence; sets FCI terms and supplier flowdown | Supplies evidence about itself and the backup vendor | Provides SOC 2 reports and subprocessor lists |

**The MSP is not a cloud provider in the shared responsibility sense.** It performs customer-side duties for the company. Anything marked "Customer (performed by MSP)" in `cloud-control-map.csv` stays the company's responsibility under FAR 52.204-21 and in the CMMC Level 1 self-assessment. The company must direct the work, receive evidence, and check it (SA-9).

**SaaS vendors that hold FCI are part of the Level 1 scope.** 32 CFR 170.19(b)(3) tells the company to consider the people, technology, facilities, and External Service Providers that process, store, or transmit FCI. The ERP and suite vendors hold FCI, so their side of each control must be evidenced (SOC 2 report or vendor documentation) in the Level 1 self-assessment.

## 3. Service categories and provider equivalents
The design is vendor-agnostic. The shared responsibility split for SaaS is the same in all three major cloud providers' models: the provider runs the application, platform, and infrastructure; the customer keeps identities, access, data, and devices (SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal-framework/sources/source-register.csv`). For the company's vendors, the SOC 2 report or vendor security documentation is the evidence of the provider side.

| Service category used | What it is here | Equivalent category in the large cloud providers (for reading their documentation) |
|---|---|---|
| Line-of-business SaaS | ERP for small distributors with a customer portal | Industry SaaS built on any provider |
| Productivity suite | Email, file storage, chat, sync | Productivity and collaboration SaaS |
| SaaS-to-SaaS backup | Nightly backup of mail and files | Backup service or third-party SaaS backup |
| Remote monitoring and management | MSP device management | Device management SaaS |
| AI service (subprocessor) | Forecasting model behind the ERP reorder feature | Managed machine learning or AI platform services |

## 4. Findings from the mapping
1. **FCI sits wherever email puts it (AC-3, AC-20).** Equipment lists arrive by email, land in the Orders folder that all 7 staff can open, and get downloaded to laptops and the unencrypted setup bench. Fix: a restricted FCI folder for the 4 people who work DoD orders, no downloads to the bench except the active job, and a rule against personal email. Tracked as P01 R-012.
2. **The setup bench is the weak point (SC-7, SC-28, IA-2).** It connects customer devices, including DoD laptops being configured, to the staff network, has a shared administrator account, and is not encrypted. Fix: separate bench network segment, named accounts, and encryption by 2026-10-31 (R-011).
3. **MSP-held administrator logins have no MFA (IA-2(1)).** The backup console and the firewall management login use passwords only. One stolen MSP password could delete the backups. Fix: MFA on both by 2026-09-30 (P07 POAM-003).
4. **Sync is not backup (CP-9, CP-4).** Laptops sync the suite's files; ransomware that encrypts a synced folder pushes the damage to the suite and then into the backup. Only 30 days of versions protect the company, and nobody has tried a restore. Fix: immutable versions and a restore test (R-007; POAM-006).
5. **Order history leaves through the AI feature (SA-9).** The ERP sends order history, including DoD orders, to a third-party AI service listed as a subprocessor. The company never reviewed those terms. P10 decides the conditions.
6. **A camera recorder on the staff network was covered equipment (CM-8).** It was not on any inventory, so nobody checked it against Section 889 before the P07 test. It was replaced on 2026-08-20 (R-024).
