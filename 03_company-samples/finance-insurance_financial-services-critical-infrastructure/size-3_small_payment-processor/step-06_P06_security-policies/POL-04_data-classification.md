# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Compliance and Risk Manager |
| Approved by | COO |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after significant changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-6, SC-8, SC-12, SC-28, SI-12, CP-9, SA-9, CM-8 |
| CSF 2.0 | ID.AM-05, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| PCI DSS v4.0.1 | Requirements 3 and 4; 9.4.7; 12.5 |
| FTC Safeguards Rule | 16 CFR 314.4(c)(2), (c)(3), (c)(6) |

## 1. Purpose
Classify company information by sensitivity and set handling rules, so protection matches the harm a disclosure would cause. Card data must stay inside the CDE.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors), all company information in any form, and all systems and service providers that store, process, or transmit it.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Compliance and Risk Manager | Owns classification and the retention schedule; approves new uses of Restricted data |
| Platform Engineering Lead | Encryption, key management, PAN discovery, backup, and deletion controls in the cloud tenant |
| IT Manager | Discovery scans in SaaS systems; media disposal |
| Data owners (CTO, CFO, Settlement Operations Manager, Risk and Fraud Manager) | Approve access to and extracts of their data |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Core rules |
|---|---|---|
| **Restricted** | Account data (PAN, cardholder name and expiry with PAN), sensitive authentication data during authorization, cryptographic keys, merchant owner SSNs and bank account numbers | CDE or approved system only; encrypted; MFA; access logged |
| **Confidential** | Tokens, transaction records without PAN, merchant contracts, settlement reports, fraud model features, security configurations | Company systems only; need-to-know access |
| **Internal** | Policies, procedures, internal communications | Company systems; no public posting |
| **Public** | Marketing, published integration guides | No restrictions |

(RA-2; ID.AM-05)

4.2 Sensitive authentication data must never be stored after authorization, even if encrypted. That covers full track data, card verification codes, and PINs or PIN blocks. (SC-28; SI-12; PR.DS-01; PCI DSS 3.3.1)

4.3 PAN may be stored only in the token vault, encrypted with keys held in the payment HSM service. PAN must never be stored in email, chat, tickets, spreadsheets, logs, the data warehouse, or any other system outside the CDE. (SC-28; PR.DS-01; PCI DSS 3.5.1; 16 CFR 314.4(c)(3))

4.4 When displayed, PAN must be masked to no more than the BIN and last four digits, unless a role has a documented business need to see the full PAN. (AC-3; PR.DS-01; PCI DSS 3.4.1)

4.5 Restricted and Confidential data sent over external networks must use TLS 1.2 or higher. PAN must never be sent by email, chat, or other end-user messaging. (SC-8; PR.DS-02; PCI DSS 4.2.1, 4.2.2; 16 CFR 314.4(c)(3))

4.6 **Retention and disposal.**
- Account data must be kept only as long as the retention schedule allows. A quarterly process must find and securely delete stored account data that has passed its retention period.
- Customer information must be disposed of no later than two years after its last use to serve the customer, unless it is needed for business operations, required by law, or cannot feasibly be deleted on its own.
- The retention schedule must be reviewed every year.

(SI-12; PR.DS-01; PCI DSS 3.2.1; 16 CFR 314.4(c)(6))

4.7 **PAN discovery.** Automated PAN discovery must run on these schedules:
- the data warehouse: monthly
- ticketing, email, and file storage: quarterly

Results must support the six-month scope confirmation (POL-01 4.6). PAN found must be handled under POL-03 4.9. (CM-8; RA-2; ID.AM-07; PCI DSS 12.5.2, 12.10.7; 16 CFR 314.4(c)(2))

4.8 **Data extracts.** Extracts that leave the CDE, including fraud model training extracts, must contain tokens, never PAN. They must include only the fields the data owner approves, and an automated check must block PAN before loading. Extracts sent to a service provider must be covered by a contract that limits their use and requires deletion with a certificate. (SA-9; SI-12; GV.SC-05; 16 CFR 314.4(f))

4.9 **Key management.**
- Cryptographic keys must be managed under documented procedures that cover generation, distribution, storage, rotation, retirement, and replacement.
- Manual cleartext key operations need split knowledge and dual control.
- Key custodians must acknowledge their duties in writing each year.

(SC-12; PR.DS-01; PCI DSS 3.6.1, 3.7, 3.6.1.1)

4.10 Media that held Restricted data must be destroyed or sanitized before disposal or reuse. For cloud storage, this is inherited from the provider, and the evidence is its AOC. (MP-6; ID.AM-08; PCI DSS 9.4.7)

4.11 Backups of Restricted data must be encrypted, stored in a second region, and restore-tested every quarter. (CP-9; PR.DS-11)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.14. Compliance is checked through PAN discovery results (4.7), the six-month scope confirmation, and the annual control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.13. They must be written, risk-rated, approved by the policy owner (or by the majority owner and CEO for High risk), and expire within 12 months. No exception may allow storage of sensitive authentication data after authorization.

## 7. Related documents
POL-01; POL-03; POL-05; retention schedule; key-management procedures; PCI DSS Requirements 3 and 4; 16 CFR 314.4(c)
