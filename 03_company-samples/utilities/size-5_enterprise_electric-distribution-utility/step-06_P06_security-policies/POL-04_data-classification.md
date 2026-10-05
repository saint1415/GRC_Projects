# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer (BCSI statements jointly with the Director, NERC Compliance) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-3, MP-6, SC-8, SC-28, SI-12, AC-3, PM-5(1) |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10 |
| Regulatory | CIP-011-3 R1 and R2; CIP-004-7 R6; 16 CFR 681.1 and 682.3; Fla. Stat. 501.171(2) and (8) worked example; FERC CEII rules (18 CFR 388.113) for information submitted to FERC |

## 1. Purpose
Classify company information by the harm its disclosure, alteration, or loss could cause, and set handling, retention, and disposal rules for each class, so the company protects grid information, customer information, and business records consistently.

## 2. Scope
All information the company creates, receives, stores, or transmits, in any form, including information held by vendors and information the company handles for SL-1 and SL-2 clients.

## 3. Classification levels
| Level | Examples | Key handling rules |
|---|---|---|
| **Restricted: BCSI** | EMS network diagrams, ESP and EAP configurations, BES Cyber Asset lists, security settings of high and medium impact systems | Approved BCSI repositories only; provisioned access authorized and verified (CIP-004-7 R6); BCSI labels; no cloud storage until a cloud BCSI repository is approved |
| **Restricted: customer** | SSNs, driver license numbers, bank account numbers, consumer reports, portal credentials | Field-level encryption; minimum necessary; retention limits; secure disposal |
| **Confidential** | OT diagrams and settings for the ADMS and distribution substations, interval usage data, customer contact data, client utilities' data, unreleased financial results | Encryption at rest and in transit; access by role |
| **Internal** | Procedures, organization charts, most email | Company systems only |
| **Public** | Published outage map, tariffs, press releases | Approved for release |

Information submitted to FERC that qualifies as Critical Energy/Electric Infrastructure Information is marked under 18 CFR 388.113 and handled as Restricted.

## 4. Policy statements
4.1 Every system owner must record the highest classification of data in the system and the information location in the GRC platform. (RA-2; CM-12; ID.AM-07)
4.2 BES Cyber System Information must be identified using the BCSI guide (STD-04.3), labeled, and stored only in approved BCSI repositories; storing BCSI in email, collaboration sites, or cloud storage that is not an approved repository is prohibited. (MP-3; AC-3; PR.DS-01)
4.3 Restricted and Confidential data must be encrypted in transit and at rest using approved algorithms (STD-04.1), except where an OT device cannot support encryption and an approved exception records compensating controls. (SC-8; SC-28; PR.DS-01; PR.DS-02)
4.4 SSNs, driver license numbers, and bank account numbers must be collected only where needed for credit, identity verification, or payment, and SSNs for closed accounts must be purged 2 years after the final bill unless a legal hold applies. (SI-12; PM-5(1); PR.DS-01)
4.5 Bulk extracts of customer data must be registered (PRC-04.1), masked where possible, and stored only in the restricted zone of the data platform. (AC-3; SI-12; PR.DS-01)
4.6 Media and devices holding Restricted or Confidential data, including consumer information, must be sanitized or destroyed under NIST SP 800-88 before reuse or disposal, with a record of each action. (MP-6; PR.DS-01)
4.7 Records must be kept for the period in the records retention schedule and disposed of securely when no longer to be retained. (SI-12; MP-6; PR.DS-01)
4.8 Restricted or Confidential data must not be entered into AI tools unless the tool is on the approved AI tools list (STD-05.2) for that class; BCSI must never be entered into any AI tool. (AC-20; SA-9; PR.DS-01)
4.9 Client utilities' data (SL-1) and fleet clients' data (SL-2) must be kept logically separate from company data and used only as the client agreement allows. (AC-3; AC-4; PR.DS-01)
4.10 Data loss prevention must scan email, collaboration sites, and cloud storage at least quarterly for BCSI and customer Restricted data outside approved locations. (SI-4; CM-12(1); DE.CM-01)

## 5. Standards and procedures under this policy
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection, Retention, and Disposal Standard
- STD-04.3 BES Cyber System Information Handling Standard
- PRC-04.1 Data Extract Registration Procedure

## 6. Compliance and enforcement
Compliance is monitored through DLP reports, BCSI access verifications, retention job reports, disposal certificates, and the annual Internal Audit assessment (P07). Violations are handled under PRC-01.1.

## 7. Exceptions
Exceptions follow POL-01 section 7. CIP-011-3 requirements cannot be excepted.

## 8. Related documents
POL-01; POL-02; POL-05; STD-04.1 to STD-04.3; CIP information protection program v5; Identity Theft Prevention Program; records retention schedule; P03 gap analysis.
