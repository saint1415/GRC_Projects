# System Security Plan: Agency Case Management Platform (ACMP)

**Organization:** Cris Santos Company Holdings, Inc. (GovTech Integration division, inheriting corporate shared services) | **Tier:** Multi-Sector | **Vertical:** Public Administration
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **ACMP**, the focus division's main hosted system, because it holds the most sensitive data the group handles for agencies (FTI for 7 revenue agencies and CJI for 212 criminal justice agencies), it carries the group's top risks (P01 GR-01 and GR-02), and it inherits most of its controls from corporate (SYS-G1 to SYS-G3). The common controls are documented once in `common-control-catalog.csv`, which the other division systems (IEP, MVSP, RMS, Civic Suite, Grants Management, and the CUI enclave) inherit through their own plans.

## 1. System Name and Identifier
Agency Case Management Platform (**ACMP**), identifier CSCH-GT-SYS-D1. SYS-D1 in `../00_company-facts.md`.

## 2. System Overview
The ACMP is a multi-tenant case management service that the GovTech Integration division builds, hosts, and supports for about 430 state and local agency tenants in 29 states. About 61,000 agency users work in it, and about 27.7 million individuals have records in it.

| Module | Customer group | Tenants | Data |
|---|---|---|---|
| Tax compliance | CG-REV: 7 state revenue agencies | 7 dedicated tenants, each with its own database instance and customer-managed key | FTI and state tax data; about 14.0 million taxpayer case records |
| Supervision and court | CG-CJ: 212 criminal justice agencies under 11 state CSAs | Tenants in the CJI cluster (separate database cluster and accounts) | CJI including CHRI; about 4.6 million case records |
| Constituent services | CG-LOC: 211 counties and cities | Tenants in the shared cluster | Constituent and code enforcement data; about 9.1 million records |

**Major components** (all in provider A's government-community landing zone, U.S. regions; backups in provider B):
- **Web and application tier:** managed container service across 3 availability zones
- **Databases:** 7 dedicated FTI database instances; the CJI cluster; the shared cluster
- **Document storage:** object storage per cluster, encrypted with group-managed keys (customer-managed keys for FTI tenants)
- **Integration gateway:** secure file transfer from revenue agencies, API links to 11 state message switches, agency API links
- **Agency sign-in:** federation with agency identity providers (all CJI and FTI tenants); ACMP-local accounts with required MFA for local governments
- **Non-production:** development, test, and staging accounts with synthetic data only (technical block on production data since 2025)
- **Backups and logging:** point-in-time recovery, hourly snapshots copied to the provider B vault, and application audit logs to the group log archive

The ACMP has no AI features. The IEP's AI eligibility assistant is a separate system (SYS-D2, P10).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it reaches the ACMP |
|---|---|---|---|
| Contract | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline | SP 800-53B Moderate baseline | Almost every agency contract |
| N92-R02 | FBI CJIS Security Policy | CJISSECPOL v6.1 (06/25/2026); 28 CFR 20.33(a)(7) | CJIS Security Addendum in each CG-CJ contract; audits by 11 state CSAs |
| N92-R01 | IRS Publication 1075 (FTI safeguards) | 26 U.S.C. 6103(p)(4); 26 CFR 301.6103(n)-1; Pub. 1075 (Rev. 11-2021) | Exhibit 7 language in each CG-REV contract; IRS Office of Safeguards reviews of the agencies |
| State | State IT security standards for agency contracts (Florida worked example: Rule 60GG-2, F.A.C.; Fla. Stat. 282.318(4)(h)) | State law in each customer state | Security terms in state agency contracts |
| State | State breach and data security laws (Florida worked example: Fla. Stat. 501.171(2) and (6)) | Each state where affected individuals reside | Directly, as a third-party agent or service provider of each agency |
| State | Agency ransomware and incident reporting (Florida worked example: Fla. Stat. 282.318, 282.3185, 282.3186) | State law | Agency duties; the group must give agencies the facts in time (P08) |
| N92-R08 | GovRAMP (formerly StateRAMP) | GovRAMP program (not law) | Requested by agencies in several states (P09) |
| SEC | Form 8-K Item 1.05; Reg S-K Item 106 | 17 CFR 229.106 | An ACMP incident may be material to the group (P08) |
| Internal | Group policies POL-01 to POL-05 and the GovTech supplement | P06 | Group policy |

Not applicable to the ACMP (they apply elsewhere in the group; see the P03 regulation-by-division matrix):
- HIPAA Security Rule (N92-R03): no ACMP customer has designated the group a business associate. It applies to the IEP for 2 Medicaid agencies.
- Medicaid and SNAP confidentiality (N92-R04): no benefits data in the ACMP. It applies to the IEP.
- Driver's Privacy Protection Act (N92-R05): no motor vehicle records in the ACMP. It applies to the MVSP.
- CIRCIA (N92-R07): proposed rule only. SLCGP (N92-R06): no grant funds pay for the ACMP.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the ACMP platform director (system owner) and the GovTech division CISO on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no federal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the GovTech division president with the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:**
  1. Corporate shared-service staff without the required CJIS or Pub. 1075 screening lose access to the CJI cluster and FTI tenants by 2026-10-31, and the group screening register is complete by 2026-12-31 (POAM-001).
  2. Subcontractor staff without documented Security Addendum certifications or IRS-approved subcontract terms lose access by 2026-10-31 (POAM-012).
  3. A full-scale restore exercise of the CJI cluster and 2 FTI tenants is completed by 2027-03-31 (POAM-011).
  4. Common control logs for FTI-relevant accounts are kept 7 years by 2027-03-31 (POAM-002).
- **Agency sharing:** each agency receives this SSP's summary, the P07 results for common and ACMP controls, and the POA&M on request, and with each CSA audit or IRS review.
- **Reauthorization:** annually, or after a major change.

### 4.3 System Operational Status
Operational. Major modifications planned: parallel tenant restore automation (POAM-011) and the move of the remaining service accounts into identity governance (POAM-005).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | ACMP platform director | Accountable for the ACMP and this SSP |
| Authorizing official equivalent | GovTech division president, with the Group CISO and Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Division security lead | GovTech division CISO | Day-to-day security program; CSA and IRS review liaison |
| Personnel screening | GovTech personnel security manager | CJIS and Pub. 1075 screening before access |
| Agency contract obligations | Group public sector compliance director | Security Addendum, Exhibit 7, and state contract terms |
| Development | GovTech chief technology officer | Code, pipeline, change management |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3), Group HR director, Group CISO (governance), Group General Counsel (procurement and legal) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once and samples ACMP and division controls (P07) |
| Agency counterparts | Revenue agency disclosure officers; criminal justice agency LASOs; state CSOs | Receive notices; approve agency users; hold Security Addendum certifications |

## 6. System Information Types and System Categorization
Information types were modeled on the mission-based categories in NIST SP 800-60 Vol. 2 Rev. 1. Impact levels are the group's FIPS 199 determinations, agreed with the revenue agencies and the CSAs.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Criminal justice supervision and court records (CJI, including CHRI) | Moderate | Moderate | Moderate | Disclosure harms supervisees and is restricted by 28 CFR Part 20; wrong conditions could lead to wrongful arrest; agencies can run one shift on paper (P05 MTD 12 h) |
| Taxation management records with FTI | Moderate | Moderate | Low | Unauthorized disclosure carries criminal and civil penalties (IRC 7213, 7213A, 7431); agency tax systems keep collections running (P05 MTD 48 h) |
| Constituent service records | Low | Low | Low | Names, addresses, some driver license numbers; paper workaround for 3 days |
| System and security information (credentials, logs, keys) | Moderate | Moderate | Moderate | Compromise gives access to every tenant |
| **ACMP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Aggregation.** The group considered raising confidentiality to High because the ACMP aggregates about 27.7 million individuals' records. It kept Moderate because each agency's own categorization of the data is Moderate, the CJIS and Pub. 1075 requirements are written for that level, and the aggregation risk is handled by design: FTI tenants have dedicated databases and keys, CJI tenants sit in a separate cluster, no administrator has standing access, and exports are role-restricted. The aggregation risk is carried in the group register (GR-01) and reviewed at each reauthorization.

**Baseline:** the NIST SP 800-53B **Moderate** baseline, as agency contracts require: 177 base controls with 110 enhancements. `control-implementation.csv` has one row per base control, and each statement covers the control's Moderate enhancements. Tailoring:
- **Not applicable (4):** AC-18, MA-3, MP-5, and SC-15, with reasons in each row.
- **Inherited:** physical and environmental controls and parts of media, maintenance, and supply chain controls are inherited from the FedRAMP authorized cloud providers; identity, monitoring, cloud, governance, personnel, and procurement controls are inherited from corporate common control providers.
- **Overlay values:** where CJISSECPOL v6.1 or Pub. 1075 sets a stricter value (5 failed logons in 15 minutes for AC-7; 1-year and 7-year log retention for AU-11; FIPS 140-3 for SC-13; a 1-hour internal report for IR-6), the stricter value is the organization-defined value (PL-11).

## 7. Authorization Boundary Description
- **Inside:** the ACMP production accounts in provider A (application tier, the three database groups, document storage, integration gateway, agency sign-in configuration), the non-production accounts, the ACMP's backup copies in the provider B vault, and the ACMP application audit logs.
- **Outside, inherited (common control providers):** SYS-G1 identity platform, SYS-G2 SOC, SIEM, and EDR, and the SYS-G3 landing zones (hub networks, guardrails, key management, log archive account, backup vault account, CI/CD).
- **Outside, interconnected:** revenue agency tax systems, 11 state message switches, agency identity providers, and the IT service management system (SYS-G4) used for support tickets.

The diagram is in P04 `cloud-architecture.md` (section 2.2).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| 7 revenue agency tax systems | Inbound nightly file transfer; outbound case status | FTI and state tax data | Contract with Exhibit 7; each agency's IRS 45-day notification. **Gap:** 2 of 7 notifications predate the 2025 move of backups to provider B (P03 PB-16; POAM-027) |
| 11 state message switches | Inbound criminal history summaries; outbound supervision status | CJI including CHRI | CJIS Security Addendum; interface agreements with each CSA |
| Agency identity providers (all CJI and FTI tenants) | Inbound assertions | User identity and roles | Federation agreements in contracts |
| Group SIEM (SYS-G2) | Outbound logs | Audit records, which can include record identifiers | Common control (catalog); SIEM in provider A's government-community region |
| IT service management system (SYS-G4) | Inbound tickets from agencies | Ticket text and screenshots (**FTI and CJI observed in 14 of 300 sampled tickets; gap, SA-9; POAM-015**) | Group contract; FedRAMP authorized service |
| Provider B backup vault | Outbound copies | Encrypted backups of all tenants | Common control (CP-6, CP-9) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Web and application containers | Managed container service (PaaS) | Provider A, U.S. region 1, 3 zones | ACMP platform director |
| FTI database instances (7) with customer-managed keys | Managed relational database | Provider A | ACMP platform director |
| CJI cluster | Managed relational database cluster | Provider A, separate accounts | ACMP platform director |
| Shared cluster (local governments) | Managed relational database cluster | Provider A | ACMP platform director |
| Document storage | Object storage | Provider A | ACMP platform director |
| Integration gateway | Containers, file transfer service, API gateway | Provider A | GovTech chief technology officer |
| Non-production environments | Separate accounts, synthetic data | Provider A | GovTech chief technology officer |
| Backup copies | Immutable vault with deletion lock | Provider B, U.S. region | Group cloud platform director |
| Application audit logs | Write-once log archive account | Provider A | Group SOC director |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (177 base controls) and `common-control-catalog.csv` (99 controls provided by corporate).

| Status | Controls |
|---|---|
| Implemented | 156 |
| Partially implemented | 17 |
| Planned | 0 |
| Not applicable | 4 |
| **Total** | **177** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or the cloud providers) | 97 |
| Hybrid (corporate provides the mechanism; the ACMP configures or operates part) | 33 |
| System-specific | 47 |

**The 17 partially implemented controls** cluster in four places:
- **People with access to agency data** (scenario gaps 1 and 10): PS-3, PS-7, AT-2.
- **Incident notification across divisions** (gap 5): IR-3, IR-4, IR-6, IR-8.
- **Recovery and retention at scale** (gaps 2 and 8): CP-4, CP-10, AU-11.
- **Operational hygiene:** AC-2, AC-8, CM-3, IA-5, RA-5, SA-9, SI-4.

### 10.2 Common control inheritance by division
The common control catalog lists 99 controls provided by corporate: 26 by the group security governance office, 19 by SYS-G3, 19 by SYS-G2, 15 by SYS-G1, 13 by group HR and personnel security, and 7 by group procurement and legal. Controls inherited only from the cloud providers (for example the PE family) are not in the catalog; they are evidenced by each provider's FedRAMP package and SOC 2 report.

Inheritance is **documented** for GovTech (this plan, and the IEP and MVSP inheritance matrices from 2025) and for Government Software Products (its FedRAMP, GovRAMP, and SOC 2 packages). It is **not documented** for the IT Consulting CUI enclave or delivery environment (scenario gap 3). Until POAM-019 closes, IT Consulting cannot show a CMMC assessor which of its SP 800-171 requirements are met by group controls.

### 10.3 Control assessment status
Common controls were assessed once, and ACMP and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`. The P03 gap analysis rated all 177 controls plus the CJIS and Pub. 1075 overlays.

## 11. Digital Identity Acceptance Statement
- **Workforce:** every user signs in through SYS-G1 with MFA (number matching); administrators use phishing-resistant hardware keys and just-in-time PAM elevation. This meets CJISSECPOL v6.1 IA-2(1) and IA-2(2) ([Priority 1]) and the Pub. 1075 multi-factor requirements.
- **Agency users:** CJI and FTI tenant users are authenticated by their agencies' identity providers, which enforce MFA; agencies own identity proofing. Local government tenants use ACMP-local accounts with required MFA since 2026-03.
- **Service accounts:** 41 ACMP service accounts are still managed by script outside identity governance (AC-2; POAM-005).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **ACMP:** Agency Case Management Platform
- **CHRI:** criminal history record information
- **CJI:** criminal justice information
- **CJISSECPOL:** FBI CJIS Security Policy
- **Common control:** a control provided once by corporate and inherited by several systems
- **CSA / CSO:** CJIS Systems Agency / CJIS Systems Officer
- **FTI:** federal tax information
- **LASO:** local agency security officer
- **PAM:** privileged access management
- **TIGTA:** Treasury Inspector General for Tax Administration

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | ACMP platform director |
| 1.0 | 2026-09-15 | Approved with authorization conditions | GovTech division CISO |
