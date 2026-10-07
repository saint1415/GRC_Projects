# Cloud Architecture and Control Placement: Cris Santos Company | Retail Trade | Small

**Organization:** Cris Santos Company, LLC (independent grocery retailer) | **Tier:** Small | **Provider:** Vendor-agnostic (see section 3)
**System:** E-commerce and Loyalty Platform (ELP), as defined in the SSP (P02) | **Prepared:** 2026-07-31 by the IT Manager; updated 2026-08-14 after P07 testing | **Approved:** General Manager, 2026-09-04

## 1. Diagram

```mermaid
flowchart LR
  subgraph Store["Store office (on-premises)"]
    ADM["Administrator PCs and laptops (5)<br/>SI-3, AC-11, SC-28<br/>SC-7 gap: flat network with IoT"]
    POS["POS system (SYS-05)<br/>outside the ELP boundary"]
  end
  subgraph SaaS["SaaS (provider-operated)"]
    IDP["Identity provider<br/>IA-2, IA-2(1), AC-7, AC-2"]
    SF["Storefront admin console, theme, apps<br/>AC-3, AC-6, AC-12, CM-3, AU-2"]
    CO["Checkout page and tag manager<br/>CM-7, CM-8, SI-7, SI-4<br/>(PCI DSS 6.4.3, 11.6.1)"]
    PE["Pricing and offers engine<br/>SA-9, SI-10"]
    OFF["Productivity suite<br/>SC-8, SI-8"]
  end
  subgraph TPSP["Payment processor (TPSP, outside boundary)"]
    PF["Embedded payment form (inline frame)<br/>SC-8, SA-9"]
  end
  subgraph Tenant["Public cloud tenant (PaaS/IaaS)"]
    API["Loyalty API (application service)<br/>SC-7, IA-5, SI-2, SI-10"]
    DB[("Loyalty database (managed)<br/>SC-28, AC-3, AU-2")]
    OS[("Export storage (object storage)<br/>CM-6, SI-12")]
    BK[("Backup vault<br/>CP-9, CP-4 (gap: same account)")]
    LOG["Cloud audit logging<br/>AU-2, AU-6, AU-11"]
    IAM["Cloud IAM and key management<br/>AC-6, IA-2(1), SC-12"]
  end
  CUST["Customer browser"] -->|HTTPS| CO
  CO -->|hosts| PF
  CUST -->|card data over TLS| PF
  PF -->|token only| SF
  ADM -->|SSO + MFA| IDP
  IDP --> SF
  IDP --> IAM
  IDP --> OFF
  SF --> CO
  SF <-->|loyalty lookups| API
  POS -->|loyalty lookups over TLS| API
  API --> DB
  DB --> BK
  DB -->|monthly export| OS
  OS -.->|emailed export (gap)| OFF
  SF <-->|purchase history, prices| PE
  API --> LOG
  IAM --> LOG
```

## 2. Layers
| Layer | Components | Key controls | Responsibility |
|---|---|---|---|
| Identity | Identity provider, cloud IAM roles, storefront staff accounts | AC-2, AC-6, AC-7, IA-2, IA-2(1), IA-5 | Customer (configuration and accounts); provider (the service) |
| Network / edge | Access restrictions on the loyalty API, store firewall for administrator PCs, storefront web application firewall | SC-7, SC-5 | Customer (API rules, store network); provider (storefront edge) |
| Compute / application | Loyalty API on a managed application service; administrator PCs | SI-2, SI-3, SI-10, IA-5 | Shared: provider patches the runtime; the company owns the code, keys, and PCs |
| Data | Managed database, object storage for exports, backup vault, key management | SC-28, SC-12, CP-9, CP-4, CM-6, SI-12 | Shared: provider encrypts; the company configures access, retention, and backup isolation |
| Logging / monitoring | Cloud audit log, identity provider sign-in log, storefront admin log, payment page monitoring | AU-2, AU-6, AU-11, SI-4 | Shared: providers generate logs; the company keeps and reviews them |
| SaaS applications | Storefront and checkout page, pricing engine, productivity suite | AC-3, AC-12, CM-3, CM-7, CM-8, SI-7, SC-8, SA-9 | Provider (application and infrastructure); customer (users, settings, scripts, data) |
| Payment processing | Processor's embedded payment form | SC-8, SA-9 | Processor (card data, under its AOC); company (the page that hosts the form) |
| Physical / hypervisor | Provider data centers | PE-3 | Provider (inherited) |

## 3. Service categories and provider equivalents
The design does not depend on one provider. This table gives each provider's name for each category, for use when reading its shared responsibility documentation.

| Service category | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|
| Managed application service (loyalty API) | AWS App Runner or Elastic Beanstalk | Azure App Service | Cloud Run |
| Managed relational database | Amazon RDS | Azure SQL Database | Cloud SQL |
| Object storage | Amazon S3 | Azure Blob Storage | Cloud Storage |
| Account-level public access block | S3 Block Public Access | Storage account setting that disallows anonymous blob access | Public access prevention |
| Backup service | AWS Backup | Azure Backup | Backup and DR Service |
| Identity and access management | AWS IAM | Azure role-based access control with Microsoft Entra ID | Cloud IAM |
| Key management and secrets | AWS KMS; AWS Secrets Manager | Azure Key Vault | Cloud KMS; Secret Manager |
| Audit logging | AWS CloudTrail | Azure Monitor activity log | Cloud Audit Logs |

Shared responsibility sources: SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal-framework/sources/source-register.csv`. All three models agree on the split used here:
- **IaaS (storage, backup vault):** the provider owns facilities, hosts, and the storage service. The customer owns access policies, retention, isolation, identities, and data.
- **PaaS (application service, managed database):** the provider also patches the operating system and runtime. The customer owns application code, keys, network rules, and data.
- **SaaS (storefront, identity provider, pricing engine, productivity suite):** the provider owns the application. The customer keeps users, roles, settings, **scripts added to its pages**, and data.

For the storefront and the payment processor, the evidence is the vendor's SOC 2 Type 2 report and PCI DSS AOC (P09), not a cloud shared responsibility model.

## 4. Findings from the mapping
1. **The checkout page is a customer responsibility on a vendor platform.** The storefront vendor's AOC covers its platform, and the processor's AOC covers the payment form. **Neither covers the scripts the company and its contractor add to the page that hosts the form.** Those belong to the company under PCI DSS 6.4.3 and 11.6.1. Tracked as P01 R-001 and POAM-003, POAM-004, POAM-008, and POAM-009.
2. **Backup isolation (CP-9).** The backup vault shares the production account and administrator roles. Someone with cloud administrator rights could delete both. Fix: copy backups to a separate account with immutable retention, and test restores quarterly. Tracked as P01 R-013, POAM-011, and POAM-012.
3. **Log retention and review (AU-6, AU-11).** Cloud, identity provider, and storefront logs use default retention, and nobody reviews them. After an e-skimming incident, the storefront admin log is the main record of who changed the theme or tags (P08). Fix: export to 1-year storage and review weekly (POAM-010).
4. **Export storage (CM-6, SI-12).** Old exports sit in object storage without an account-level public access block. Fix: enforce the block, alert on policy changes, and delete exports older than 90 days (P01 R-014).
5. **Administrator PCs on the flat store network (SC-7).** The PCs that administer the storefront and cloud share a network with refrigeration IoT devices. Fix: a separate office VLAN (POAM-020, P01 R-004).
6. **Inherited controls depend on vendor reports.** Controls marked "Provider" or "Common/Inherited" in P02 depend on the storefront, identity, productivity, and cloud providers' SOC 2 reports and AOCs, reviewed in P09. The pricing engine vendor has provided no assurance report (POAM-013).

## 5. Validation against the SSP
Every component inside the P02 boundary appears in the diagram and in `cloud-control-map.csv`. Each has at least one control from the AC, AU, CM, IA, SC, or SI families, implemented or inherited. The POS system and payment processor are drawn only as interfaces, because they are outside the ELP boundary.
