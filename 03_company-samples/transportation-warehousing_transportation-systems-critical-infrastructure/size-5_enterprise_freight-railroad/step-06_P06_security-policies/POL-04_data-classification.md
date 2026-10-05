# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Assistant Vice President, Rail Security (with the CISO for technical standards) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-3, MP-4, MP-6, SC-8, SC-12, SC-13, SC-28, SI-7, SI-12 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-11 |
| TSA / regulatory basis | 49 CFR part 1520 (1520.9, 1520.13, 1520.19); SD 1580/82-2022-01E Sec. III.B.2.b, IV.B; 49 CFR 236.1033; state breach laws |

## 1. Purpose
Classify company information so that SSI, personal information, customer data, and train control data get protection that matches the harm their disclosure or alteration could cause.

## 2. Scope
All information the company creates, receives, or holds, in any form, on any system, including OT data in the TDPB, PTC keys, data held for SL-1 and SL-2 customers, and information held by vendors for the company.

## 3. Classification levels
| Level | Examples | Key handling rules |
|---|---|---|
| **SSI** | CIP and CAP, assessment results, incident reports to TSA and CISA, zone designs, RSSM routing and security plans | 49 CFR part 1520: covered persons with a need to know; marked; stored in the SSI library; destroyed completely |
| **Restricted** | Personal information (employee, crew certification, medical), PTC cryptographic keys, credentials, customer operating data | Encryption at rest and in transit; named access; DLP |
| **Operational integrity** | Territory tables, authority records, PTC configuration, consists | Change control; integrity checks; backups with zero or 15-minute RPO as set in P05 |
| **Internal** | Policies, procedures, timetables, bulletins | Company staff only |
| **Public** | Press releases, public tariffs | Approved for release |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every information asset must have an owner and a classification recorded in the inventory or data catalog. (RA-2; ID.AM-05)
4.2 SSI must be disclosed only to covered persons with a need to know, kept in the SSI library or an approved SSI system, marked with the protective marking and limited distribution statement, and requests from others referred to TSA. (MP-3; MP-4; PR.DS-01)
4.3 Unauthorized release of SSI must be reported to the Assistant Vice President, Rail Security at once, who informs TSA promptly. (IR-6; RS.CO-02)
4.4 Restricted and SSI data must be encrypted at rest and in transit with NIST-approved algorithms. OT traffic that crosses IT or carrier networks must be encrypted or otherwise protected for integrity. (SC-8; SC-28; SC-13; PR.DS-01; PR.DS-02)
4.5 PTC cryptographic keys must be generated and held in hardware security modules, distributed and revoked under the key management procedure, and never exposed in cleartext outside key entry. (SC-12; PR.DS-01)
4.6 Integrity of territory tables, authority records, and PTC configuration must be verified at load and continuously monitored, with alerts to the SOC and the system owner. (SI-7; PR.DS-01)
4.7 Media holding SSI or Restricted data must be sanitized to NIST SP 800-88 or destroyed with a certificate before disposal or reuse. (MP-6; PR.DS-01)
4.8 Records must be retained for the periods in the records schedule, including PTC records (236.1037), RSSM custody records (1580.205(h)), training records (1570.121), and security documentation (POL-01 4.11). (SI-12; PR.DS-11)
4.9 SSI and Restricted data must not be entered into AI tools unless the AI governance committee has approved the tool and the contract prohibits training on company data. (AC-20; PR.DS-01)

## 5. Standards and procedures under this policy
- STD-04.1 Encryption and Key Management Standard
- STD-04.2 Media Protection, Marking, and Disposal Standard (including SSI)
- STD-04.3 Backup Standard
- STD-04.4 Operational Data Integrity Standard
- PRC-04.1 SSI Handling Procedure

## 6. Compliance and enforcement
Compliance is monitored through DLP and SSI content scans, SSI library access reviews, and the annual Internal Audit assessment (P07). Violations are handled under PRC-01.1 (POL-01 statement 4.7).

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2. No exception may permit disclosure of SSI to a person who is not a covered person with a need to know.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P02 TDPB SSP; P04 cloud control map; P10 AI governance; applicable regulations listed in P03.
