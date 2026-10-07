# Cloud Architecture and Control Placement: Cris Santos Company | Public Administration | Micro

**Organization:** Cris Santos Company, LLC (GovTech systems integrator) | **Tier:** Micro | **Provider:** Vendor-agnostic (see section 3)
**System:** Hosted Case Management Service (HCMS), as defined in the SSP (P02) | **Prepared:** 2026-08-07 by the Lead Platform Engineer with the Operations Manager and the MSP lead technician; updated 2026-08-19 with P07 test results | **Approved:** owner, 2026-08-31

## 1. Diagram
The company runs no servers of its own except one. Its cloud is a licensed low-code platform (SaaS/PaaS) that hosts the agency applications, plus one cloud workload it operates itself: the integration virtual machine and its export bucket (SYS-02) in a government-community IaaS region.

```mermaid
flowchart LR
  subgraph Agencies["Agency side (outside the boundary)"]
    SHF["Sheriff file drop + identity provider<br/>(AC-01, CJI)"]
    AU["Agency users<br/>AC-01 to AC-04"]
  end
  subgraph Platform["Low-code platform tenant (SYS-01), vendor-operated"]
    WS["4 agency workspaces + sandbox<br/>AC-3, AC-7, IA-2(2), AU-2, CP-9"]
    AI["AI add-on (SYS-09, pilot)<br/>SA-9 (outside vendor FedRAMP scope)"]
  end
  subgraph IaaS["IaaS account (SYS-02), company-operated"]
    VM["Integration virtual machine<br/>SC-13, SI-2, IA-2(1), AU-11"]
    BK[("Export bucket<br/>30 days, same account<br/>CP-9, AC-3")]
  end
  subgraph Office["Company (MSP-managed)"]
    LT["8 laptops<br/>SC-28, SI-3, AC-11"]
    FW["Office firewall, Wi-Fi<br/>SC-7"]
  end
  subgraph SaaS["Business SaaS"]
    SU["Productivity suite + identity<br/>IA-2(1)"]
    HD["Helpdesk (CJI screenshots)<br/>SA-9"]
    RP["Repository<br/>IA-5"]
  end
  RMM["MSP remote management (SYS-08)<br/>AC-17"]
  VDI["Revenue agency virtual desktop (SYS-10)<br/>FTI stays here"]
  SHF -->|SFTP nightly, CJI| VM
  VM -->|platform API, TLS| WS
  VM -->|nightly export| BK
  AU -->|TLS + MFA (not AC-04)| WS
  WS --> AI
  LT -->|SSH keys| VM
  LT -->|TLS + MFA| WS
  LT --> SU
  AU -.->|email tickets| HD
  RMM -->|agent on every laptop| LT
  LT -->|2 approved laptops, agency MFA| VDI
  RP -.->|scripts| VM
```

## 2. Layers and who is responsible
| Layer | Components | Key controls | Customer (company) | MSP (on the company's behalf) | Provider (platform vendor or IaaS provider) |
|---|---|---|---|---|---|
| Identity | Platform staff and agency accounts; SSH keys; suite accounts | AC-2, AC-6, IA-2(1), IA-2(2), IA-5 | Decides who gets access; sets MFA and lockout; holds SSH keys | Creates and disables suite accounts | Runs the sign-in and MFA services |
| Application | Workspaces, roles, workflows, AI add-on settings | AC-3, CM-3, SA-9 | Designs and promotes configurations; decides on the AI add-on | Not applicable | Runs the platform and enforces workspace separation |
| Compute | Integration virtual machine | SI-2, SI-3, CM-2 | Patches, hardens, and monitors the server | Not applicable (not in the MSP contract) | Hypervisor and hardware |
| Network | Security group, SFTP and API links, office firewall | SC-7, SC-8, SC-13 | Security group rules; FIPS mode for the SFTP pull | Office firewall and Wi-Fi | Network isolation; platform TLS |
| Data | Workspace data, CHRI working files, nightly exports | CP-9, SC-28, MP-6 | Export copies, retention, restore tests, deletion of working files | Not applicable | Platform backups; default disk and bucket encryption |
| Logging | Tenant audit log, server logs, bucket access logs | AU-2, AU-6, AU-11 | Exports, keeps 1 year, reviews monthly (**gap today**) | Keeps laptop and firewall logs | Generates platform and account logs |
| Endpoints | 8 laptops | SC-28, SI-3, AC-11 | Approves exceptions; keeps the inventory | Encryption, antivirus, patching, screen lock | Not applicable |
| Vendor governance | Platform vendor, MSP, helpdesk, AI add-on | SA-9, SR-6 | Reviews SOC 2 reports and contract terms | Not applicable | Provides SOC 2 report, FedRAMP package, and letters |

**The MSP is not a cloud provider in the shared responsibility sense.** It performs customer-side duties for the company on laptops and the suite. Anything marked "Customer (performed by MSP)" in `cloud-control-map.csv` stays the company's responsibility under its agency contracts. The MSP has no role on the platform tenant or SYS-02, which makes the Lead Platform Engineer the only operator of the one server that holds CHRI files.

## 3. Service categories and provider equivalents
The design is vendor-agnostic. For SaaS, all three major providers' shared responsibility models put the application, platform, and infrastructure with the provider and keep identities, access, data, and devices with the customer. For IaaS, the customer also owns the operating system, network rules, and everything installed on the server (SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal-framework/sources/source-register.csv`).

| Service category used | What it is here | Equivalent category in the large cloud providers (for reading their documentation) |
|---|---|---|
| Low-code case management platform (SaaS/PaaS) | SYS-01 tenant | No single equivalent: low-code application platforms are sold through each provider's marketplace and run on its government regions |
| Government-community IaaS virtual machine | SYS-02 server | AWS EC2 in GovCloud (US), Azure Virtual Machines in Azure Government, Google Compute Engine with Assured Workloads |
| Object storage | SYS-02 export bucket | Amazon S3, Azure Blob Storage, Google Cloud Storage |
| Managed generative AI feature | SYS-09 add-on | Amazon Bedrock, Azure OpenAI Service, Vertex AI (here supplied by the platform vendor, not bought directly) |
| Productivity suite, helpdesk, repository | SYS-03 to SYS-05 | Productivity, service desk, and code hosting SaaS |
| Remote monitoring and management | SYS-08 | Device management SaaS |

## 4. Findings from the mapping
1. **The backup sits next to the thing it backs up (CP-9).** The nightly exports are in the same IaaS account as SYS-02, under an access key stored on SYS-02, with no versioning or object lock. An attacker who reaches the server can delete both. The vendor's tenant restore is the only other copy, and it takes up to 48 hours. Fix: write-once copies in a separate account by 2026-11-30 and a first restore test by 2026-10-31 (P01 R-001, R-004).
2. **The one server is the weakest layer (IA-2(1), SI-2, SC-13).** SYS-02 is administered with SSH keys only, patched by hand, has no malware protection, and pulls CJI with a library not confirmed to run a FIPS 140-3 certified module. The CJIS cutoff for FIPS 140-2 certificates is 2026-09-21. P07 testing also found a security group rule allowing SSH from any internet address (P01 R-024).
3. **CJI leaks out of the boundary through support.** Sheriff users email screenshots to the helpdesk, whose vendor has no CJIS Security Addendum, and the MSP's remote tool can reach laptops that cache those screenshots (SA-9, AC-17; P01 R-012, R-013).
4. **The platform side is strong and evidenced.** The vendor's FedRAMP Moderate authorization and SOC 2 report cover the data centers, platform patching, encryption, and backups. The gaps are on the company's side: access reviews, log export and review, AC-04 MFA, and lockout values for CJIS.
5. **The AI add-on is outside the vendor's FedRAMP scope.** The vendor confirmed in August 2026 that the add-on is not yet in its authorization, so applicant data has been going to a service no one has assessed since 2026-06-01. It is mapped here to show the SA-9 gap; P10 sets the conditions.
6. **FTI is not in this architecture, by design.** The revenue agency's virtual desktop is drawn only to show that 2 laptops connect to it. The FTI spill found on 2026-07-29 (a defect log in the suite) shows what happens when that design is not enforced on people (P01 R-006).
