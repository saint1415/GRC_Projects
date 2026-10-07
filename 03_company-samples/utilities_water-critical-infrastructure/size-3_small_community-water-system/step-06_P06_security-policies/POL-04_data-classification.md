# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, SC-8, SC-28, MP-6, CP-9, CM-8, SI-12 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| Regulatory basis | RRA and ERP retention, 42 U.S.C. 300i-2(d); customer personal information, Fla. Stat. 501.171(2) and (8) |

## 1. Purpose
Classify company information by sensitivity and set handling rules so protection matches the harm a disclosure or alteration would cause, including harm to the water system.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and interns) at WTP-1, WTP-2, the administration office, and remote sites. Covers all systems and data, including operational technology (the Water Treatment SCADA System, PLCs, RTUs, and telemetry) and systems that service providers operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Owns classification; implements encryption, backup, and disposal controls |
| Operations Manager | Decides who may see RRA, ERP, and SCADA information |
| Customer Service and Billing Manager | Owner of customer personal information |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | RRA and ERP contents; SCADA network diagrams, IP plans, and device credentials; PLC logic and HMI projects; vulnerability findings | Named-role access only; encrypted at rest and in transit; never emailed outside the company except to the integrator through approved channels |
| **Confidential** | Customer personal information and online account credentials; payroll; contracts; water quality data before release | Encrypted in transit; need-to-know |
| **Internal** | Procedures, schedules, maps without critical facility layers | Workforce only |
| **Public** | Consumer confidence report, public notices, website | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted and Confidential data must be encrypted at rest on every device and service, and in transit. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.3 Restricted data may be stored only in approved locations: the Restricted folder in the productivity suite (access limited to 6 named roles), the engineering workstation, and the offline backup media. (AC-3)
4.4 The IT Manager must keep an inventory of where Restricted and Confidential data is stored and which vendors receive it. (ID.AM-07; CM-8)
4.5 Media and devices holding Restricted or Confidential data must be wiped or destroyed so the data is unreadable, with a certificate of destruction for disposal. Customer records must be disposed of by shredding, erasing, or otherwise making them unreadable (Fla. Stat. 501.171(8)). (MP-6; ID.AM-08)
4.6 **OT backups.** PLC logic and HMI projects must be exported monthly and after every change, encrypted, stored offline in two locations, and compared quarterly with the running logic. Business backups must be kept apart from production and restore-tested quarterly. (CP-9; PR.DS-11)
4.7 Restricted or Confidential data must not be entered into AI tools or other third-party services unless the tool is on the approved list (POL-05 4.8). (SA-9)
4.8 The RRA, the ERP, and their certifications must be kept at least 5 years after each certification (42 U.S.C. 300i-2(d)); copies of public notices and certifications at least 3 years (40 CFR 141.33(e)). (SI-12)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; P10 AI approved-tools list; records retention schedule
