# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | IT Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-25 |
| Review cycle | Annually (next review 2027-09-24), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-3, MP-5, MP-6, SC-8, SC-12, SC-13, SC-28, CP-6, CP-9, AC-21, CM-12, SI-12, AU-11 |
| CSF 2.0 | ID.AM-05, ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| Regulatory drivers | C-IT-R01 (FedRAMP readiness: CMU-CSO-CMD, MAS-CSO-FLO); Fla. Stat. 501.171(2) and (8); MSA confidentiality clause |

## 1. Purpose
Classify company and customer information and set handling rules for each class, so the strongest protection goes to the data and secrets that could harm customers.

## 2. Scope
All information the company creates, receives, stores, or processes. This includes customer data in VMs, snapshots, and backups; tenant metadata; secrets; source code; logs; and business records. It applies in all locations: DC-1, DC-2, the public cloud tenant, SaaS tools, and laptops.

## 3. Classification levels
| Class | Examples | Minimum handling |
|---|---|---|
| **Restricted** | Customer VM contents, snapshots, and backups; customer credentials and API keys; control plane service credentials; code and template signing keys; BMC and root credentials; any federal customer data if hosted | Encrypted in transit and at rest; access by named role with ticket reference; never copied off the platform |
| **Confidential** | Tenant metadata, DNS zone data, tickets, security logs, vulnerability reports, source code, bank contact lists, employee records | Encrypted in transit; access by role; shared outside the company only under contract |
| **Internal** | Procedures, internal guides, network diagrams without secrets | Company systems only |
| **Public** | Marketing site, status page, published documentation | Approved for publication |

Unlabeled information is treated as Confidential.

## 4. Policy statements
4.1 System owners must classify the data their systems hold and record where it is stored (DC-1, DC-2, cloud region, SaaS vendor) in the SSP data inventory. (RA-2; CM-12; ID.AM-07)

4.2 **Encryption.**
- Restricted and Confidential data must be encrypted in transit with TLS 1.2 or higher (or IPsec between sites).
- Restricted data must be encrypted at rest.
- New customer VM volumes must be encrypted by default from 2027-06-30.
- The Engineering Manager (Control Plane) must keep an inventory of the cryptographic modules that protect customer data and whether each one is FIPS 140 validated. Agency tenants must use validated modules.
(SC-8; SC-13; SC-28; PR.DS-01; PR.DS-02)

4.3 **Customer data access.**
- Staff may access customer VM contents or snapshots only at the customer's request or during an incident, with a ticket reference.
- Staff must never copy customer data to laptops or to any location outside the platform.
(AC-3; PR.DS-01)

4.4 **Sharing.** Customer data and tenant metadata may be shared with third parties only as the MSA allows or the law requires. The COO decides each case with outside counsel and records the decision. (AC-21)

4.5 **Keys.** Encryption and signing keys must be generated and stored in the cloud key management service or a hardware security module. Rotation periods must be documented. Keys must never be exported in plain text. (SC-12)

4.6 **Media.**
- Failed or retired drives must be cryptographically erased, then destroyed by a certified vendor that issues certificates.
- Drives moving between sites must travel in sealed containers and be logged.
(MP-5; MP-6; ID.AM-08)

4.7 **Backups.** Control plane backups must be immutable, stored in a separate account and a second region, taken at least hourly for the tenant database, and restore-tested every quarter. (CP-9; CP-6; PR.DS-11)

4.8 **Retention.**
- Security logs: 1 year online and 3 years in archive.
- Incident records: at least 3 years.
- Customer data: deleted within 30 days after contract end unless the MSA says otherwise.
- Records containing personal information: destroyed so they cannot be read or reconstructed (Fla. Stat. 501.171(8)).
(SI-12; AU-11)

4.9 **AI tools.** Restricted and Confidential data must not be entered into AI tools unless the Information Security Officer has approved the tool and its contract restricts use of company data. The SIEM's AI-assisted triage is approved for security logs, with conditions (P10). (PL-4; SA-9)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the right authority, and expire within 12 months.

## 7. Related documents
POL-01; POL-02; POL-05; P04 cloud control map; P05 BIA (RPO targets); P10 AI risk assessment; Fla. Stat. 501.171
