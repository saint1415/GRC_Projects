# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, AC-21, MP-6, PT-2, PT-3, SC-8, SC-28, SC-28(1), SI-12, AU-2 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02 |
| Regulatory anchors | FTC Start with Security 1 and 4 (N51-R01); 16 CFR 314.4(c)(2), (c)(3), (c)(6) (N52-R03); 48 CFR 52.204-21(b)(1)(vii) (N54-R04); 45 CFR 164.504(e)(2)(ii)(J) (N54-R06); PCI DSS 3; customer DPAs |
| Division supplements | Cloud Software: export and handoff channels. Technology Consulting: client data at project close; federal project area. Payments and Payroll: account data and payroll records retention |

## 1. Purpose
Make sure every data set has a classification, an owner, a permitted purpose, a storage location, and a retention period, and that the protection follows the data when it moves between divisions.

## 2. Scope
All data the group creates, receives, stores, or transmits, in any division and any format.

## 3. Classes
| Class | Examples | Minimum handling |
|---|---|---|
| **Restricted** | Social Security numbers, bank account and routing numbers, payroll handoff files, cardholder data, PHI, federal contract information, credentials and keys | Customer-managed keys; read logging; named-owner access; no email; shortest retention |
| **Confidential** | Customer worker data in tenants, HR case notes, client project data, merchant records | Encryption; role-based access; DPA or contract use limits |
| **Internal** | Policies, internal reports | Workforce only |
| **Public** | Published documents | Approved for release |

## 4. Policy statements
4.1 Every data set must be recorded in the data inventory with its class, owner, and permitted purposes. **The owner is the division with the legal duty for the data**, even when another division stores it (for example, Payments and Payroll owns the payroll handoff files stored in the WCP). (RA-2; ID.AM-07; 16 CFR 314.4(c)(2))

4.2 Restricted data must be encrypted at rest with keys controlled by the owning division or the group key service on its behalf, and in transit with TLS 1.2 or higher. Read access to Restricted data must be logged at the object level. (SC-28(1); SC-8; AU-2; 16 CFR 314.4(c)(3))

4.3 **Moving Restricted data between divisions** requires a documented flow with a single recipient, a written intercompany agreement (POL-01 4.8), and deletion at the source once receipt is confirmed. Shared storage locations for Restricted data are prohibited. (AC-4; AC-21)

4.4 Customer data must be used only for the purposes the customer's agreement allows. Any new use, including AI training or tuning on aggregated or de-identified data, requires a privacy impact assessment and confirmation that the affected agreements permit it. (PT-2; PT-3; RA-8)

4.5 **Retention.** Payroll handoff files: 7 days after receipt is confirmed. Customer-requested exports: 30 days. Terminated customers' tenant data: deleted within 90 days of termination. Client project data in consulting systems: deleted or returned at project close, unless the contract says otherwise. Payroll and tax records: as tax law requires, and no longer than two years after last use unless required or necessary (16 CFR 314.4(c)(6)). (SI-12)

4.6 Media and devices that held Restricted or Confidential data must be sanitized with a certificate before disposal or reuse. (MP-6; 48 CFR 52.204-21(b)(1)(vii))

4.7 Federal contract information must be stored only in the federal project area of the collaboration workspace, with membership limited to the named project team. (AC-3; 48 CFR 52.204-21(b)(1)(i))

4.8 PHI received as a business associate must not be used in test environments; synthetic data must be used instead. PHI must be returned or destroyed at the end of the engagement. (45 CFR 164.504(e)(2)(ii)(J))

4.9 Cardholder data must stay inside the cardholder data environment; outside it, only tokens may be stored. (PCI DSS 3)

## 5. Compliance and enforcement
Compliance is checked through the data inventory review each quarter, P07 sampling of SI-12 and AC-4, and the PCI DSS scope review.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may permit shared storage of Restricted data.

## 7. Related documents
POL-01; POL-02; division supplements; P02 SSP; P04 cloud control map.
