# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Crude Oil Production, Power Generation, Crude Logistics) and corporate shared services |
| Policy ID | POL-04 |
| Owner | Group CISO, with the Group General Counsel |
| Approved by | Group CISO, under authority of POL-01 (2026-09-17) |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, SC-28, SC-8, MP-6, SI-12, CM-12, AC-3 |
| CSF 2.0 | ID.AM-07, ID.AM-05, PR.DS-01, PR.DS-02 |
| Regulatory and benchmark drivers | Fla. Stat. 501.171(2) and (8) as the worked example for state law; HMR 172.802(c) (security plan access); trade secret protection |
| Division supplements | Production: royalty owner data and seismic data. Power Generation: CIP-related plans and network diagrams. Crude Logistics: shipper data, hazmat security plan, driver location and video |

## 1. Purpose
Classify group information so that each type gets protection that matches the harm its disclosure, alteration, or loss would cause, including OT information that could help an attacker.

## 2. Scope
All information the group creates, receives, or holds in any form, including OT configurations and data in supplier systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Data owners | Classify their data and approve access |
| Group General Counsel | Defines legal holds, retention, and personal information categories |
| Group data platform director | Applies classification tags on SYS-G6 |
| All workforce | Label and handle data by its class |

## 4. Policy statements
4.1 All information must be classified as **Restricted**, **Confidential**, **Internal**, or **Public**. Restricted: personal information as defined by state breach laws (for example, royalty owner and employee Social Security or taxpayer numbers, bank accounts, driver license numbers), and authentication secrets. Confidential: OT network diagrams, firewall rules, SCADA and controller backups, setpoints and logic, vendor remote access details, seismic and reservoir data, shipper volumes and statements, the hazmat security plan, and driver location and video. Internal: other business information. Public: approved for release. (RA-2; ID.AM-05; driver: Fla. Stat. 501.171(1))

4.2 Each division must keep an inventory of where Restricted and Confidential data is stored, including exports and copies. (CM-12; ID.AM-07; driver: N21-BM (SP 800-82r3 6.1.1))

4.3 **Restricted data must stay in approved systems.** It must not be exported to file shares, email, or personal storage. Bulk transfers to third parties must use approved secure transfer. (AC-3; SC-28; PR.DS-01; driver: Fla. Stat. 501.171(2))

4.4 Restricted and Confidential data must be encrypted at rest and in transit wherever the system supports it. Where OT links cannot be encrypted, the network must be isolated and the exception recorded. (SC-28; SC-8; PR.DS-01; PR.DS-02; driver: N21-BM (SP 800-82r3 6.2.3))

4.5 OT Confidential data (diagrams, rules, backups, vendor access details) may be shared with suppliers only under contract and need to know, and must not be posted in tickets or chat outside the OT workspace. (AC-3; PR.DS-01; driver: N21-BM (SP 800-82r3 6.2.3))

4.6 The hazmat security plan may be shared only with employees who implement it and with authorized DOT or DHS officials on request. (AC-3; PR.DS-01; driver: HMR 172.802(c), (d))

4.7 Media and records containing Restricted or Confidential data must be destroyed by shredding or erasure that makes the data unreadable (NIST SP 800-88 methods), including media from SCADA servers and HMIs. (MP-6; PR.DS-01; driver: Fla. Stat. 501.171(8) (applied as group practice))

4.8 Data must be retained under the group retention schedule and any longer regulatory period, and disposed of at the end of it unless on legal hold. (SI-12; ID.AM-08; driver: N21-BM)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.14. Compliance is checked through the P07 assessment of common controls and division samples, the annual supplement attestations, and division access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may weaken a safety function or extend a legal notice deadline.

## 7. Related documents
POL-01; POL-02; POL-05; group retention schedule; data inventories.
