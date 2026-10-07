# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | General Counsel, with the CISO |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 (version 2026.1) |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after changes to SSI or CEII rules |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-3, MP-6, AC-3, SC-8, SC-28, CP-9, SI-12, SA-9, PL-4 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08, GV.SC-05 |
| Regulatory drivers | 49 CFR Part 1520 (SSI); SD Pipeline-2021-02G Sections III.B.2.b, III.F.1.c, and IV (C-ENERGY-R03); 18 CFR 388.113 (CEII); 49 CFR 192.631(j) (C-ENERGY-R04); state data security laws (Fla. Stat. 501.171 as the worked example) |

## 1. Purpose
Classify company information by the harm its disclosure, alteration, or loss could cause, and set handling rules, including the legal handling rules for SSI and CEII.

## 2. Scope
All information the company creates, receives, or holds, in any form, in IT, OT, cloud, SaaS, and supplier systems, including information held for JV owners (SL-2) and shippers (SL-1).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| General Counsel | SSI and CEII determinations; this policy |
| Director of Regulatory Affairs | CEII filings with FERC |
| CISO | Encryption, backup, and technical handling standards |
| Data owners (vice presidents) | Classify their data and approve access |
| All workers | Label and handle information by its class |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information must be classified as **Restricted** (SSI, CEII, SCADA and station control configurations and backups, OT network diagrams and firewall rules, credentials, security assessment results, employee Social Security and bank numbers), **Confidential** (shipper commercial data, JV owner data, measurement data, material nonpublic information, payroll), **Internal**, or **Public**, and labeled where systems allow. (RA-2; ID.AM-07)
4.2 SSI must be marked as 49 CFR 1520.13 requires, disclosed only to covered persons with a need to know, stored in the SSI library or locked containers, and destroyed as 1520.19 requires. Unmarked SSI received from others must be marked and the sender told. Any release of SSI to an unauthorized person must be reported to the General Counsel at once so TSA can be informed promptly. (MP-3; AC-3; PR.DS-01)
4.3 Information submitted to FERC that qualifies as CEII must be filed under the CEII procedure (PRC-04.2), with a justification, the required labels, and a redacted public version. (MP-3; PR.DS-01)
4.4 Restricted information must be encrypted at rest and in transit under STD-04.1. OT traffic that crosses any network shared with business IT must be encrypted. Where an OT device or protocol cannot encrypt, it must stay inside the OT network or a dedicated carrier path. (SC-8; SC-28; PR.DS-01; PR.DS-02)
4.5 Information belonging to one shipper or JV owner must not be disclosed to another; access must be granted by owner group. (AC-3; PR.DS-01)
4.6 Backups must be protected and tested: IT backups immutable in separate accounts; SCADA backups taken weekly and after every configuration change, with an offline copy at the other gas control center; all backups scanned for malicious code when made and before restore; restores tested at least annually. (CP-9; PR.DS-11)
4.7 Media holding Restricted or Confidential information, including replaced HMIs, PLCs, and SCADA servers, must be sanitized before reuse and destroyed by a certified vendor with a certificate before disposal. (MP-6; ID.AM-08)
4.8 Records that show compliance with 49 CFR 192.631, and the records TSA may inspect under the security directives, must be kept in the compliance records system, protected from alteration, and retained per the records schedule. (SI-12; PR.DS-11)
4.9 Restricted information must not be entered into any AI tool unless the AI governance committee has approved the use case and the terms prohibit training on company data. (SA-9; PL-4; GV.SC-05)

## 5. Standards and procedures under this policy
- STD-04.1 Encryption Standard
- STD-04.2 Media Protection and Disposal Standard (includes SSI and CEII marking and storage)
- STD-04.3 Backup Standard
- PRC-04.1 SSI Handling Procedure
- PRC-04.2 CEII Filing Procedure

## 6. Compliance and enforcement
Compliance is monitored through quarterly SSI marking checks (added in 2026 after P03 G-060 and G-116), data loss prevention alerts, backup reports, and the annual Internal Audit assessment (P07). Violations are handled under PRC-01.1 (POL-01 statement 4.16). Unauthorized SSI disclosure can also lead to TSA enforcement.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2. SSI handling rules in 49 CFR Part 1520 cannot be excepted.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; records schedule; P02 SSP; P03 rows G-113 to G-121; P04 cloud control map.
