# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | EHS Manager (CVI and process safety information) with the IT Manager (technical controls) |
| Approved by | VP Operations |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-6, MP-3, MP-4, MP-6, MP-7, SC-8, SC-28, CP-9, SI-12 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-05 |
| Benchmarks and rules | C-CHEMICAL-R01 (6 CFR 27.400 CVI, legacy; 27.230(a)(8), voluntary benchmark); 40 CFR 68.48 (process safety information); Fla. Stat. 501.171 (employee personal information) |

## 1. Purpose
Define how company information is classified, and how each class must be protected, stored, shared, backed up, and destroyed.

## 2. Scope
All company information in any form, including OT configurations and recipes, in all systems, including those operated by vendors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Information owners (Process Engineer, Quality Manager, EHS Manager, HR Manager, Controller) | Classify their information; approve access |
| EHS Manager | Custodian of legacy CVI and the old Site Security Plan |
| IT Manager and Controls Engineer | Implement technical controls |
| Workforce | Label and handle information as classified |

## 4. Policy statements
4.1 **Classes.**
| Class | Examples | Handling |
|---|---|---|
| **Restricted-Security** | Legacy CVI (Top-Screen, SVA, Site Security Plan), OT network diagrams, firewall rules, remote access credentials | Named access only (maximum 6 users); access logged; no email outside the company; paper locked |
| **Restricted** | Master recipes and formulations, DCS and SIS configurations, employee PII, background check results | Role-based access; encrypted at rest and in transit; no personal devices |
| **Internal** | Operating procedures, production schedules, QC results, customer orders | Workforce only; share with vendors under agreement |
| **Public** | Safety data sheets, marketing materials, the public RMP summary | No restriction |

(RA-2; ID.AM-05)
4.2 **Legacy CVI.** CVI must stay in the locked cabinet or the restricted CVI library, labeled, and limited to people with a need to know. CFATS is lapsed and whether CVI duties are still enforceable was not verified, so the company keeps protecting CVI as if the rules applied. (AC-3; MP-4; 27.400)
4.3 Restricted and Restricted-Security data must be encrypted at rest and in transit wherever the system supports it. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.4 Restricted-Security and Restricted data must not be kept in folders open to more than the owner's approved group. Access is reviewed quarterly. (AC-6)
4.5 **Removable media in OT.** Only company-owned, approved USB drives may be used on OT workstations. Every drive must be scanned at the media scanning station before each use. Personal and vendor-supplied media are prohibited. (MP-7; PR.PS-05)
4.6 **Backups.** DCS and SIS configurations, master recipes, the LIMS, and file shares must be backed up. At least one copy must be offline or immutable and stored away from the system it protects. Restores must be tested quarterly. The SIS program copy must be compared with the running logic after each proof test. (CP-9; PR.DS-11)
4.7 Media and devices must be sanitized or destroyed before disposal or return, with a record. That includes failed DCS disks and replaced HMIs. (MP-6)
4.8 Restricted or Restricted-Security data must not be entered in AI tools unless the tool is on the approved list for that class (POL-05 4.8). (AC-3)
4.9 Security records, assessments, and POA&Ms are kept for at least 5 years, matching RMP record retention (40 CFR 68.200). (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Compliance is checked through the annual control assessment (P07) and quarterly access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.6.

## 7. Related documents
POL-01; POL-02; POL-05; CVI handling procedure; backup and restore procedure (due 2026-12-31); 6 CFR 27.400
