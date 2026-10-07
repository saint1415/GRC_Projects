# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (managed cloud hosting provider) |
| Policy ID | POL-04 |
| Owner | Operations Manager (Compliance Coordinator), with the Lead Systems Engineer (Information Security Lead) for technical content |
| Approved by | Owner, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually each September (next review 2027-09-30), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, AC-3, SC-8, SC-28, SA-9, PL-4, CP-9, CP-4, MP-6, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-02, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05 |
| Regulatory drivers | Interagency Guidelines II.B, III.C.1.c, III.C.1.h, III.C.4 (bank contracts); Fla. Stat. 501.171(2), (8); MSA confidentiality clause |

## 1. Purpose
Sort the information the company holds or can reach by the harm its loss or disclosure would cause, and set handling rules for each level.

## 2. Scope
All workforce members and all information the company holds, processes, or can reach, in any form. That includes:
- customer VM contents and backups;
- customer servers reached through the RMM tool;
- customer DNS zones;
- credentials and configuration;
- the company's own business records.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Manager | Owns this policy; keeps the system and data inventory with the Lead Systems Engineer; approves new vendors under POL-02 A.5 |
| Lead Systems Engineer | Encryption, backup design, and restore testing; the technical side of the inventory |
| Systems Engineers | Run backups, restore tests, zone exports, and disposal, with records |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 The company uses three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer VM contents and backups (including Bank A's loan documents); anything on customer servers; bank customer information; credentials of every kind (administrator and service passwords, BMC passwords, MFA seeds, API tokens, break-glass seals, customer server passwords) | Only in approved locations (4.3); encrypted at rest and in transit; opened only to work a ticket for that customer (POL-02 C.1); never in personal accounts or public AI tools |
| **Internal** | Customer contact and billing data, DNS zone data, configurations and network diagrams, tickets, contracts, security documents, employee records | Workforce and approved vendors only; encrypted in transit |
| **Public** | Website, published service descriptions and status notices | No restriction |

When unsure, treat information as Restricted. Customer data is always Restricted, because the company cannot see what each customer keeps in its VMs. (RA-2; ID.AM-07)

4.2 **Encryption.** Restricted information must be encrypted in transit (TLS 1.2 or higher, or the VPN) and at rest. New storage array volumes and the backup repository must be encrypted at rest by 2026-12-31, and existing volumes as they are migrated. Laptops must use full-disk encryption. (SC-8; SC-28; PR.DS-01; PR.DS-02; Interagency Guidelines III.C.1.c)

4.3 **Approved locations for Restricted information:**
- customer VMs on the DC-1 platform and their backups (appliance and cloud copy);
- the RMM tool, for data in transit to customer servers;
- the business password manager, for credentials;
- the PSA vault, only in folders restricted by role.

Bank server passwords are kept only in the business password manager, with per-person access. (AC-3; PR.DS-01)

4.4 **Inventory.** The Lead Systems Engineer and the Operations Manager must keep one inventory of hardware, SaaS services, cloud resources, and every place bank customer information is stored or can be reached (Bank A's VMs, backups, RMM agents on bank servers, vault entries), by 2026-10-31, and update it when anything changes. (CM-8; ID.AM-01; ID.AM-02; ID.AM-07; Interagency Guidelines I.C.2)

4.5 **New vendors and tools.** No vendor, SaaS tool, or integration may receive Restricted information until it passes the vendor review in POL-02 A.5 and is added to the inventory. (SA-9; GV.SC-05)

4.6 **AI tools.** Restricted or Internal information may be processed only by AI tools on the approved list:
- the MDR provider's AI alert triage, approved with conditions on 2026-09-15 (P10 AI-001);
- no other AI tool is approved today.

Public or personal AI chatbots must never receive customer data, credentials, configurations, or tickets. AI features in existing SaaS tools stay turned off until assessed (P10 AI-003). (SA-9; PL-4)

4.7 **Backups.**
- The backup add-on VMs, the hypervisor manager configuration, and the portal database must be backed up nightly.
- The cloud copy must sit in a separate cloud account with object lock for at least 30 days, by 2026-12-31.
- Customer DNS zones must be exported nightly to the backup copy, by 2026-10-31.
- A sample restore (at least one add-on VM, the portal database, and one DNS zone) must be tested and recorded every quarter, starting in 2026 Q4.
- Customers not on the backup add-on are told in the MSA that they back up their own VMs.

(CP-9; CP-4; PR.DS-11; Interagency Guidelines III.C.1.h)

4.8 **Disposal.**
- Media that held Restricted information must be wiped with a verified method before reuse, or destroyed by a vendor that gives a certificate of destruction.
- Failed array drives stay with the company under the keep-the-drive warranty option.
- The Systems Engineer records every wipe and destruction.
- Customer VMs and their backups are deleted within 30 days after a customer leaves, unless the customer asks for an export first.

(MP-6; ID.AM-08; Interagency Guidelines III.C.4; Fla. Stat. 501.171(8))

4.9 **Retention.** Customer data is kept only as the MSA and the customer's instructions require. Security records follow POL-02 A.7. (SI-12)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through quarterly restore records, the monthly MDR report, disposal records, and the yearly assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; system and data inventory; P04 cloud control map; P05 BIA; P10 AI risk assessment; MSA; P03 gap rows G-007, G-009, G-012, G-020, G-025, G-028, G-042
