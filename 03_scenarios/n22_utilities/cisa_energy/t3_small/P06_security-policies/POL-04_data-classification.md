# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | IT Manager |
| Approved by | President |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-3, MP-6, SC-8, SC-28, SI-12, CP-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| Pipeline safety link | 49 CFR 192.631(j) (records) |

## 1. Purpose
Classify company information by the harm its disclosure, alteration, or loss could cause, and set handling rules so protection matches that harm. For a pipeline, information that would help someone attack the pipeline is the most sensitive.

## 2. Scope
All Cris Santos Company employees, contractors, and suppliers with access to company systems, at HQ and the Gas Control Center, Compressor Station 1, the field offices, and all field sites. It covers business IT, OT (SCADA, field devices, telecommunications, and the IT/OT DMZ), the cloud tenant, and SaaS services, including systems that suppliers operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Owns classification; approves new uses of Restricted information |
| SCADA Engineer | Protects OT configurations, backups, and network information |
| All personnel | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | SCADA configurations and backups, OT network diagrams and firewall rules, OT passwords, security assessments and this policy set's evidence, employee Social Security and bank numbers | Encrypted at rest and in transit; need-to-know; approved systems only; never in public AI tools |
| **Confidential** | Customer contracts, nominations, measurement data, pipeline maps below public detail, payroll | Encrypted in transit; need-to-know |
| **Internal** | Procedures, schedules, training material | Employees and approved contractors |
| **Public** | Website, public awareness material, emergency contact information for the public | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted information must be encrypted at rest and in transit wherever the technology supports it. Where an OT device or protocol cannot encrypt, it must stay inside the OT network or the carrier private network. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.3 Restricted information may be stored only in approved locations: the OT network, the restricted security folder in the productivity suite, and the backup locations in 4.5. It must never be kept on personal devices or personal cloud accounts, or sent to suppliers without the IT Manager's approval. (AC-3; MP-3)
4.4 The IT Manager must keep an inventory of where Restricted information is stored and which suppliers receive it. (ID.AM-07; CM-8)
4.5 **Backups.**
- SCADA servers must be backed up weekly and after every configuration change.
- At least one copy must be offline or immutable and stored away from the Gas Control Center.
- Backups must be checked for malware before restore and restore-tested at least annually.
- Business IT backups must be immutable for at least 30 days.

(CP-9; PR.DS-11)
4.6 Media and devices holding Restricted information, including replaced HMIs, SCADA servers, and field devices, must be wiped or destroyed with a certificate of destruction before disposal. (MP-6; ID.AM-08)
4.7 Records that show compliance with 49 CFR 192.631 must be kept in the compliance records system and protected from alteration. (SI-12; 192.631(j))
4.8 **Sensitive Security Information (activated on TSA designation).** If TSA designates the pipeline, plans, reports, and assessment results submitted to TSA are SSI under 49 CFR Part 1520. They must be marked, shared only with covered persons who have a need to know, and stored and sent as Restricted. The IT Manager must issue an SSI handling procedure within 30 days of designation. (MP-3; AC-3)

## 5. Compliance and enforcement
Violations may lead to retraining, written warning, loss of access, or termination, depending on intent and impact. For contractors, violations may lead to removal of access and contract action. Compliance is checked through the annual control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; P10 approved-tools list; records retention schedule; 49 CFR Part 1520 (on designation)
