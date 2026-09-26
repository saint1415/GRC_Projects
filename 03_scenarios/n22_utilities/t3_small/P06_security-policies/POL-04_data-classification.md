# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | IT Manager |
| Approved by | President and CEO |
| Effective date | 2026-09-08 |
| Review cycle | Annually (next review by 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-6, SC-8, SC-28, SI-12, CP-9 |
| CSF 2.0 | ID.AM-05, ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| NERC and other | Fla. Stat. 501.171 (customer personal information); CIP-003-9 Compliance 1.2 (evidence retention) |

## 1. Purpose
Classify company information by the harm its loss, change, or disclosure could cause, and set handling rules to match. Grid configuration data and customer personal information need the most protection.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at every company site, including substations and crew yards. Covers all company systems and data: corporate IT, the Distribution Operations Platform, the low impact BES Cyber Systems at Substation N and Substation E, the cloud tenant, and systems that vendors operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Owns classification; implements encryption, backup, and disposal controls |
| Customer Service Manager | Owner of customer data in the CIS and AMI |
| Manager of Engineering and Protection | Owner of relay settings, substation diagrams, and access lists |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer SSNs and bank account numbers; relay settings; substation network diagrams and gateway access lists; SCADA configuration and backups; passwords and keys; Critical Energy/Electric Infrastructure Information (CEII) received from FERC or the transmission owner | Encrypted at rest and in transit; need-to-know; approved systems only; never emailed outside the company |
| **Confidential** | Outage records with customer contact details; usage data; payroll; contracts; security reports | Encrypted in transit; need-to-know |
| **Internal** | Procedures, schedules, maps without device details | Workforce only |
| **Public** | Outage map, rates, website | No restriction |

(RA-2; ID.AM-05)

4.2 Restricted data must be encrypted at rest and in transit. It must be shared outside the company only through the approved secure file transfer, and only with a need to know. CEII must also be handled under the terms the sender set. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 Restricted and Confidential data may be stored only in approved systems: the CIS, the AMI head-end, the OMS, the engineering file server, the SCADA servers, and the backup vaults. It must never be kept on personal devices or personal cloud accounts. (AC-3)

4.4 The IT Manager must keep an inventory of where Restricted data is stored and which vendors receive it. (ID.AM-07; CM-8)

4.5 Customer SSNs must be deleted from the CIS once the credit or deposit decision is made, and no later than 90 days after an account closes. (SI-12; Fla. Stat. 501.171)

4.6 Media and devices holding Restricted data must be wiped (for reuse) or destroyed by a certified vendor that provides a certificate of destruction (for disposal). This includes retired relays, gateways, and HMI drives. (MP-6; ID.AM-08)

4.7 Backups of the SCADA database and configuration must include an offline or immutable copy, kept apart from the OT network and its credentials, and must be restore-tested every quarter. Cloud backups must stay in the separate backup account with immutable retention. (CP-9; PR.DS-11)

4.8 CIP evidence must be kept for at least three calendar years in the CIP evidence repository (POL-01 4.11). (SI-12; CIP-003-9 Compliance 1.2)

4.9 Restricted or Confidential data must not be entered into AI tools unless the tool is on the approved list (see P10 and POL-05). (SA-9)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 4.8). Compliance is checked through the annual control assessment (P07) and the data inventory review.

## 6. Exceptions
Exceptions follow POL-01 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; P10 AI approved-tools list; records retention schedule; CIP evidence repository procedure
