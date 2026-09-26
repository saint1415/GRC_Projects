# Cloud Architecture and Control Placement: Cris Santos Company | Information | Small

**Organization:** Cris Santos Company, LLC (B2B SaaS software publisher) | **Tier:** Small | **Provider:** Vendor-agnostic (see section 3)
**System:** Workforce Scheduling Platform (WSP), as defined in the SSP (P02) | **Control map:** `cloud-control-map.csv` (39 rows, 18 components)

## 1. Diagram

```mermaid
flowchart LR
  subgraph Users["Users"]
    W["Workers: mobile app, kiosks<br/>IA-8, AC-7"]
    M["Customer managers and admins<br/>IA-8 (MFA for admins)"]
    E["Company staff on managed laptops<br/>SC-28, SI-3"]
  end
  subgraph SaaSCorp["Company SaaS"]
    IDP["Workforce identity provider<br/>IA-2(1), AC-2"]
    REPO["Source repository and CI/CD<br/>CM-3, SR-3 (gap: static keys)"]
    OBS["Logging and monitoring SaaS<br/>SI-12 (gap: PII in logs)"]
  end
  subgraph Prod["Production cloud account (IaaS/PaaS)"]
    EDGE["WAF and load balancer<br/>SC-7, SC-5, SC-8"]
    APP["Container service: web, API, workers, AI service<br/>AC-3, CM-6, SI-10"]
    DB[("Multi-tenant database<br/>SC-28, SC-4, CP-9")]
    OBJ[("Payroll export storage<br/>AC-3 (gap: no object access logs)")]
    KMS["Key management and secrets<br/>SC-12, IA-5"]
    LOG["Cloud audit logging<br/>AU-12 (gap: 90 days, no alerts)"]
    SNAP[("Snapshots and cross-region copies<br/>CP-9 (gap: same account)")]
    ADM["Internal admin console<br/>AC-6, AU-6 (gap: view-as-tenant)"]
  end
  subgraph Stg["Staging account"]
    STG[("Staging copy of production data<br/>SA-3(2) (gap)")]
  end
  subgraph Sub["Sub-processors"]
    NOTIF["Email and SMS delivery<br/>SA-9"]
    LLM["AI model provider API<br/>SA-9 (gap: no DPA)"]
  end
  W --> EDGE
  M --> EDGE
  EDGE --> APP
  APP --> DB
  APP --> OBJ
  APP --> KMS
  APP --> NOTIF
  APP --> LLM
  APP --> OBS
  E -->|SSO + MFA| IDP
  IDP --> REPO
  IDP -->|console, read-only roles| Prod
  E -->|break-glass role (gap)| DB
  ADM --> DB
  REPO -->|static access keys (gap)| APP
  DB --> SNAP
  SNAP -->|monthly unmasked refresh (gap)| STG
  APP --> LOG
```

## 2. Layers
| Layer | Components | Key controls | Responsibility |
|---|---|---|---|
| Identity | Workforce identity provider, production and staging cloud IAM, CI credentials | AC-2, AC-6, IA-2(1), IA-5, AC-6(9) | Customer (the company) for all identities, roles, and keys; provider runs the IAM service |
| Network / edge | WAF, load balancer, private subnets, network rules | SC-7, SC-5, SC-8 | Shared: provider runs edge services and DDoS protection; the company writes rules and egress limits |
| Compute / application | Container service, container registry, internal admin console | AC-3, CM-6, SI-2, SI-10, RA-5 | Shared for the platform layer (provider patches the managed control plane); customer for images, code, and tenant isolation |
| Data | Managed database, payroll export storage, snapshots, key management, staging copy | SC-28, SC-4, SC-12, CP-9, SA-3(2) | Shared: provider encrypts and runs backups; the company decides retention, isolation, copy locations, and who can delete |
| Logging / monitoring | Cloud audit logging, logging and monitoring SaaS | AU-2, AU-11, AU-12, SI-4, SI-12 | Shared: provider generates events; the company must turn on data-level logging, retain, alert, and review |
| SaaS and sub-processors | Source repository and CI/CD, notification providers, AI model provider | CM-3, SR-3, SA-9 | Provider runs the service; the company owns configuration, contracts, and oversight |
| Physical / hypervisor | Provider data centers | PE-3 | Provider (inherited) |

**What the company must always own, whatever the service model:** who has access (identity), what is logged and reviewed, where copies of customer data go, and whether sub-processors are checked. Every High risk in P01 sits in one of those four areas.

## 3. Service categories and provider equivalents
The design is independent of the provider. This table gives each provider's name for each category, for reading its shared responsibility documentation.

| Service category | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|
| Managed containers | Amazon EKS or Amazon ECS | Azure Kubernetes Service or Azure Container Apps | Google Kubernetes Engine or Cloud Run |
| Managed relational database | Amazon RDS | Azure Database for PostgreSQL | Cloud SQL |
| Object storage | Amazon S3 | Azure Blob Storage | Cloud Storage |
| Key management | AWS KMS | Azure Key Vault | Cloud KMS |
| Secrets manager | AWS Secrets Manager | Azure Key Vault | Secret Manager |
| Audit logging | AWS CloudTrail | Azure Monitor activity log | Cloud Audit Logs |
| Threat detection | Amazon GuardDuty | Microsoft Defender for Cloud | Security Command Center |
| Web application firewall | AWS WAF | Azure Web Application Firewall | Cloud Armor |
| Container registry | Amazon ECR | Azure Container Registry | Artifact Registry |
| Federated workload credentials for CI | IAM OIDC identity provider with IAM roles | Microsoft Entra workload identity federation | Workload Identity Federation |

Shared responsibility sources: SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM in `00_universal/sources/source-register.csv`. All three models agree on the split used here:
- **IaaS:** the provider owns facilities, hosts, and the virtualization layer. The company owns operating systems, applications, network configuration, identities, and data.
- **PaaS (managed containers and database):** the provider also runs the platform software and its patching. The company still owns images, code, access, configuration, retention, and data.
- **SaaS:** the provider also owns the application. The company keeps identities, access, configuration, and data.

## 4. Findings from the mapping
1. **Static CI keys reach everything (IA-5, AC-6).** The CI/CD pipeline holds two long-lived keys with broad read and write permissions over production, including the payroll export bucket and snapshots. This is the entry point in the P08 scenario. Fix: federated short-lived credentials scoped per pipeline job (P01 R-001, P07 POAM-005).
2. **Data-level activity is invisible (AU-2, AU-11, SI-4).** Management events are logged for 90 days, but object reads, database queries, and snapshot sharing are not logged or alerted on. After a key leak the company could not tell customers which files were taken. Fix: object access logs, provider threat detection, and a 1-year archive in a separate log account (R-031, POAM-006 to POAM-008).
3. **Backups share a blast radius with production (CP-9).** Snapshots and cross-region copies live in the production account, so a compromised administrator could delete them. Fix: separate backup account with write-once retention (R-007).
4. **Production data leaves production (SA-3(2)).** Monthly unmasked refreshes put all customer data in a less protected account. Fix: stop refreshes and purge (R-003, POAM-010).
5. **Tenant isolation has one layer (AC-3, SC-4).** Isolation is enforced only in application code. Fix: database-level row security as a second layer (R-005).
6. **Sub-processor controls rely on unreviewed reports (SA-9).** Rows marked Provider or Shared for SaaS vendors depend on SOC 2 reports that nobody has reviewed. P09 `vendor-soc2-review.csv` starts that review.
