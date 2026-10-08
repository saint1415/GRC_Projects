# Cloud Architecture and Control Placement: Cris Santos Company | Agriculture | Micro

**Organization:** Cris Santos Company, LLC (precision-agriculture row crop and watermelon farm) | **Tier:** Micro | **Provider:** Vendor-agnostic SaaS (see section 3)
**System:** Farm Management and Irrigation Control Platform (FMICP), as defined in the SSP (P02) | **Prepared:** 2026-07-31 by the Office Manager (Security Coordinator) with the MSP technician and the Irrigation and Equipment Technician | **Approved:** Owner and General Manager, 2026-08-31

## 1. Diagram
The farm runs no servers and no IaaS tenant. Its "cloud" is a set of SaaS services plus one cloud workload that the MSP operates for it: the cloud backup of the productivity suite (SYS-08). The components come from the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv); the `evidence_source` column in `cloud-control-map.csv` cites the evidence ID behind each placement. The diagram shows the environment **as found in July 2026**. Items marked "gap" are on the POA&M (P07). The dashed line from the irrigation dealer is the always-on remote access path that POAM-002 replaces.

```mermaid
flowchart LR
  subgraph Shop["Shop and farm office (on-premises, one flat network today)"]
    EP["Office desktop + 2 laptops<br/>SI-2, SI-3, SC-28 (desktop gap)"]
    TAB["Field tablet + 3 phones<br/>AC-11 (gap), IA-2 (shared login)"]
    FW["MSP-managed firewall + shop Wi-Fi<br/>SC-7, AC-18 (gap: flat, shared password)"]
  end
  subgraph Pump["Pump station (Home Farm)"]
    PLC["Pump station controller<br/>VFD pump, fertigation, drip valves<br/>IA-5 (default PIN), CP-9 (gap)"]
    GW["Dealer cellular gateway<br/>MA-4, AC-17, IA-5 (gaps)"]
  end
  subgraph Field["Fields (Home Farm and River Tract)"]
    PIV["5 pivot panels with cellular modems<br/>PE-3 (River Tract gap)"]
    SEN["Soil probes, flow meters,<br/>weather station"]
  end
  subgraph SaaS["Vendor SaaS (provider-operated)"]
    FMIS["FMIS: records, hours, food safety,<br/>irrigation module<br/>AC-3, AU-2, CP-9, SI-4 (alerts off)"]
    PCS["Pivot connectivity service<br/>(FMIS subservice, carved out)"]
    SUITE["Productivity suite<br/>email + Office folder<br/>IA-2(1), AC-3 (gap)"]
    TEL["Telematics portal (SYS-06)<br/>AC-2 (dealer access gap)"]
    AIV["Agronomy analytics (SYS-09)<br/>SA-9 (terms gap)"]
  end
  subgraph Workload["Cloud workload (MSP-operated)"]
    BK[("Cloud backup (SYS-08)<br/>30 days, not immutable<br/>CP-9, CP-4, IA-2(1) (gaps)")]
  end
  RMM["MSP remote management<br/>AC-17"]
  DEALER["Irrigation dealer"]
  EP --> FW
  TAB --> FW
  FW ---|wireless bridge| PLC
  PLC --- GW
  DEALER -.->|always-on shared login (gap)| GW
  FW -->|TLS + MFA| SUITE
  FW -->|TLS| FMIS
  TAB -->|cellular| FMIS
  FMIS <--> PCS
  PCS <-->|carrier private network| PIV
  SEN -->|cellular telemetry| FMIS
  EP <-->|sync client| SUITE
  SUITE -->|nightly copy| BK
  RMM --> EP
  TEL --> FMIS
  TAB -.->|drone imagery upload| AIV
```

## 2. Layers and who is responsible
| Layer | Components | Key controls | Customer (farm) | MSP or dealer (on the farm's behalf) | Provider (SaaS vendor) |
|---|---|---|---|---|---|
| Identity | SYS-01, suite, backup, telematics, and gateway accounts | AC-2, IA-2, IA-2(1), IA-5 | Decides who gets access; enforces MFA in SYS-01; removes departed users | MSP creates and disables suite accounts and holds the backup login; dealer holds the gateway login | Runs the sign-in and MFA service |
| Network | Firewall, Wi-Fi, pump station bridge, internet line | SC-7, AC-18 | Approves changes; decides separation | MSP configures and patches the firewall and Wi-Fi | Carrier runs the private cellular network for the pivots |
| OT | Pump station controller, gateway, pivot panels, probes | MA-4, IA-5, CP-9, CM-3 | Owns the OT; approves every dealer session and change; holds the program copy | Dealer programs and maintains | No cloud shared responsibility model covers OT (SP 800-82r3) |
| Endpoints | Desktop, laptops, tablets, phones | SC-28, SI-2, SI-3, AC-11 | Keeps the inventory; manages tablets and phones (gap) | MSP encrypts, patches, and runs antivirus on 3 computers | Not applicable |
| SaaS applications | FMIS, suite, telematics, agronomy analytics | AC-3, AU-2, SI-4 | Users, roles, sharing, alert settings | MSP administers the suite on request | Application, platform, data centers |
| Data | SYS-01 records, the Office folder, backup copies, controller program | CP-9, CP-4, SC-28 | Decides retention, exports, and restore testing | MSP runs the backup and restore tests | Encrypts and backs up its own platform |
| Logging | SYS-01 audit trail, suite logs, firewall logs | AU-2, AU-6 | **Reviews logs monthly (gap today)** | MSP keeps firewall logs | Generates and stores logs |
| Vendor governance | Contracts, SOC 2 review, supplier terms | SA-9 | Signs terms; reviews SOC 2 reports and MSP evidence | Not applicable | Provides SOC 2 reports |

**The MSP and the irrigation dealer are not cloud providers in the shared responsibility sense.** They perform customer-side duties for the farm. Anything marked "Customer (performed by MSP)" in `cloud-control-map.csv` remains the farm's responsibility: the farm must direct the work, receive evidence, and check it (SA-9; CSF 2.0 GV.SC-07).

## 3. Service categories and provider equivalents
The design is vendor-agnostic. The shared responsibility split for SaaS is the same in all three major cloud providers' models: the provider runs the application, platform, and infrastructure; the customer keeps identities, access, data, configuration, and devices (SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal-framework/sources/source-register.csv`). For the farm's vendors, a SOC 2 report or vendor security documentation is the evidence of the provider side.

| Service category used | What it is here | Equivalent category in the large cloud providers (for reading their documentation) |
|---|---|---|
| Line-of-business SaaS | FMIS with irrigation module; telematics portal; agronomy analytics | Industry SaaS built on any provider |
| Productivity suite | Email, calendar, file storage, sync client | Productivity and collaboration SaaS |
| SaaS-to-SaaS backup | Cloud backup of mailboxes and the Office folder | Backup service or third-party SaaS backup |
| IoT connectivity | Pivot and probe telemetry over cellular | IoT device connectivity and messaging service |
| Remote monitoring and management | MSP device management | Device management SaaS |

**OT is always the farm's.** No cloud shared responsibility model covers the pump station controller, the gateway, or the pivot panels. NIST SP 800-82 Rev. 3 is the reference for those rows.

## 4. Findings from the mapping
1. **The dealer's gateway is a second, unmanaged internet path into irrigation (SC-7, MA-4, IA-5).** The cellular gateway bypasses the firewall, uses one shared dealer login without MFA (EV-020), and its admin page was reachable from the internet with the manufacturer's default password until 2026-08-14 (P07 test, EV-IA-5; fix confirmed in EV-050). Fix: gateway powered on only for approved sessions, named dealer accounts with MFA through the gateway vendor's remote access service, and no internet-facing administration. Tracked as P01 R-002 and R-023 and POAM-002, POAM-007, POAM-009.
2. **Sync is not backup (CP-9, CP-4).** The office desktop syncs the Office folder. If ransomware encrypts the synced copy, the encrypted files sync to the suite and then to SYS-08. Only the 30 days of versions protect the farm, the backup console has a password-only login, and nobody has tried a restore. SYS-01 records and the pump station program have no farm-held copy at all. Fix: 90-day immutable versions, MFA on the console, a restore test by 2026-09-30, a monthly SYS-01 export, and a copy of the controller program kept offline. Tracked as R-004 and POAM-003, POAM-004.
3. **SaaS configuration is the farm's job (SI-4, AU-6, IA-2(1)).** SYS-01 can alert on every pivot start, stop, and schedule change, and can require MFA for every user, but both are switched off. Turning them on costs nothing. Tracked as R-003 and POAM-008.
4. **Inherited controls rely on the FMIS vendor's SOC 2 report, with one carve-out.** The connectivity service that carries pivot commands is a subservice organization carved out of the report (P09). That is the path an attacker would use to start or stop pivots through SYS-01.
5. **Personal data sits in more places than the farm knew.** H-2A passport and visa copies are in the Office folder (shared with four users and synced to an unencrypted desktop), and operator location history sits in the telematics portal with standing dealer access. Tracked as R-005, R-014, and R-015.
