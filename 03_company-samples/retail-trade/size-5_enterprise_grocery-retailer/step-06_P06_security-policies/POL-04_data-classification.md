# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-3, AC-4, MP-1, MP-6, PT-1, PT-2, PT-4, RA-2, RA-8, SA-9, SC-1, SC-8, SC-12, SC-13, SC-28, SI-12 |
| CSF 2.0 | GV.OC-03, GV.SC-05, ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10 |
| PCI DSS v4.0.1 (N44-45-R01) | 3.2.1, 3.3.1, 3.4.1, 4.2.1, 4.2.2, 9.4.6, 12.5.2 (requirement numbers only; read the text in the company's licensed copy) |

## 1. Purpose
Classify company information and set handling rules so that card data, customer personal information, and other sensitive data are protected in proportion to their risk and used only for disclosed purposes.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at the 112 stores in Florida, Georgia, Alabama, South Carolina, and Tennessee, the 2 distribution centers, and headquarters, including the acquired banner (AB) stores from their acquisition date. Covers all systems and data, including stores, colocation, cloud, SaaS, store operational technology, and systems that third parties operate for the company, and the services the company offers to external business clients (SL-1 retail media and SL-2 supplier collaboration).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns classification and handling rules; privacy reviews; Tennessee data protection assessments |
| Data owners (vice presidents) | Classify data and approve access |
| Chief Data and Analytics Officer | CDP, analytics, and clean room data controls |
| Vice President, Retail Media | Clean room outputs and client data use |
| All workforce | Handle data according to its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).
**Classes.** **Restricted:** card data and sensitive authentication data, precise geolocation, biometric data, authentication secrets. **Confidential:** customer and loyalty personal information, employee data, supplier commercial data, non-public financial results. **Internal:** operating procedures and internal reports. **Public:** published content.

4.1 Every data set must have an owner and a class (Restricted, Confidential, Internal, Public) recorded in the data inventory. (RA-2; ID.AM-05)
4.2 Full card numbers must not be stored after authorization, sensitive authentication data must never be stored, and card numbers must be masked to the last 4 digits wherever displayed. (SI-12; AC-3; PR.DS-01)
4.3 Card numbers must never be sent or accepted through end-user messaging (email, chat, text); data loss prevention must detect and mask them. (SC-8; SI-12; PR.DS-02)
4.4 Restricted and Confidential data must be encrypted in transit over open networks with TLS 1.2 or higher. (SC-8; SC-13; PR.DS-02)
4.5 Restricted and Confidential data must be encrypted at rest with customer-managed keys under STD-04.1. (SC-28; SC-12; PR.DS-01)
4.6 Payment fields (card numbers, tokens, and card brand transaction data) must be kept out of loyalty, CDP, retail media, and analytics data sets. (AC-4; PR.DS-01)
4.7 Customer data may be used only for purposes described in the privacy notice. A new use needs a privacy review and, where the Tennessee Act requires, a documented data protection assessment before launch. (RA-8; PT-2; GV.OC-03)
4.8 Sensitive data, including precise geolocation, may be processed only with recorded consent. Facial recognition and other biometric identification of customers are prohibited. (PT-4; GV.OC-03)
4.9 Data must be kept only as long as the retention schedule allows and then destroyed so it cannot be read or reconstructed. (SI-12; MP-6; PR.DS-01)
4.10 Clean room outputs to clients must be aggregated with minimum audience thresholds enforced by the platform, and client contracts must prohibit re-identification. (AC-4; AC-3; PR.DS-10)
4.11 Restricted or Confidential data may be entered into an AI tool only if the AI governance committee has approved the tool with no-training and deletion terms. (SA-9; GV.SC-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard
- STD-04.3 Backup Standard
- STD-04.4 Customer Data Use and Clean Room Standard
- PRC-04.1 Data Extract Registration Procedure
- PRC-04.2 Data Protection Assessment Procedure

## 6. Compliance and enforcement
Compliance is measured through data discovery scans (card numbers outside the CDE, payment fields in Cloud B data sets), data loss prevention alerts, the data inventory review, Tennessee data protection assessment status, and the annual Internal Audit assessment (P07). Violations follow PRC-01.1.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2. A deviation from a PCI DSS requirement also needs the PCI Program Manager's review, because internal exceptions do not change what the QSA must validate.

## 8. Related documents
POL-01; STD-04.1 to STD-04.4; PRC-04.1 and PRC-04.2; P03 Tennessee Act and Visa rows; P09 SL-1 confidentiality criteria; P10 AI governance; POAM-019, POAM-020.
