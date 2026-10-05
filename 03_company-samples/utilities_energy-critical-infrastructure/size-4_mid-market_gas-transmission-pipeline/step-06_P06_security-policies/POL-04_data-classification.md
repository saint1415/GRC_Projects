# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-2, MP-3, MP-4, MP-6, SC-8, SC-28, SI-12, CP-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| Regulatory basis | TSA SD Pipeline-2021-02G Sections III.F.1.c and IV.B; 49 CFR 1520.9, 1520.13, 1520.19; 18 CFR 388.113; 49 CFR 192.631(j) |
| Supporting standards | STD-07 Contingency and recovery standard; STD-08 Encryption standard; STD-10 SSI and CEII handling standard |

## 1. Purpose
Classify company information by the harm its disclosure, alteration, or loss could cause, and set handling rules so protection matches that harm. For a TSA-designated pipeline, the most sensitive information is what would help someone attack the pipeline, and some of it is regulated as Sensitive Security Information (SSI).

## 2. Scope
All employees, contractors, authorized representatives, and managed service providers, at all sites, for information in any form.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Owns classification and the SSI repository; approves sharing of SSI and Restricted information |
| SCADA and OT Engineering Manager | Protects OT configurations, backups, PLC logic, and network information |
| Director of Regulatory Affairs | CEII requests for FERC filings |
| General Counsel | SSI and CEII questions; requests from outside parties |
| All personnel | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of five levels:

| Level | Examples | Handling |
|---|---|---|
| **SSI** | TSA Cybersecurity Implementation, Incident Response, and Assessment Plans; assessment results and reports submitted to TSA; reports to CISA under SD 01G | Part 1520 rules (4.7); SSI repository only |
| **Restricted** | SCADA configurations, backups, and PLC logic; OT network diagrams and firewall rules; OT passwords; detailed pipeline design data (CEII if filed); this policy set's evidence; employee Social Security and bank numbers | Encrypted at rest and in transit; need-to-know; approved systems only; never in public AI tools |
| **Confidential** | Shipper contracts, nominations, measurement data, OSA customer data, payroll | Encrypted in transit; need-to-know |
| **Internal** | Procedures, schedules, training material | Employees and approved contractors |
| **Public** | Website, Informational Postings, public awareness material | No restriction |

(RA-2; ID.AM-07)
4.2 SSI and Restricted information must be encrypted at rest and in transit wherever the technology supports it. Where an OT device or protocol cannot encrypt, the data must stay inside OT or the private telecommunications network. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.3 SSI and Restricted information may be stored only in approved locations: the SSI repository, the OT network, the restricted security folder, and the backup locations in 4.5. It must never be kept on personal devices or personal cloud accounts, or sent to suppliers without the Security Manager's approval. (AC-3; MP-4)
4.4 The Security Manager must keep an inventory of where SSI and Restricted information are stored and which suppliers receive them, and scan general file shares for SSI markings each quarter. (ID.AM-07; CM-8)
4.5 **Backups.**
- SCADA servers must be backed up weekly and after every configuration change; PLC logic at every station after every change.
- At least one copy must be offline and stored at the BCC, away from the GCC.
- Backups must be hash-checked and scanned for malicious code when made and before restore, and a full rebuild must be tested at least annually.
- Business workload backups must be write-once for at least 35 days in the separate backup account.

(CP-9; PR.DS-11; SD 02G III.F.1.c)
4.6 Media and devices holding SSI or Restricted information, including replaced HMIs, SCADA servers, and field devices, must be wiped or destroyed with a certificate of destruction before disposal. (MP-6; ID.AM-08; 49 CFR 1520.19)
4.7 **Sensitive Security Information.** SSI must be:
- marked with the protective marking SENSITIVE SECURITY INFORMATION and the distribution limitation statement in 49 CFR 1520.13, on paper and electronic records, including exports;
- disclosed only to covered persons with a need to know, unless TSA authorizes otherwise in writing;
- stored in the SSI repository or a locked container when not in use;
- destroyed completely when no longer needed.

Requests for SSI from anyone else go to the Cybersecurity Coordinator, who refers them to TSA. Unmarked SSI received must be marked and the sender told. Any release of SSI to unauthorized persons must be reported to the Security Manager the same day and to TSA promptly. (MP-3; MP-4; AC-3; 49 CFR 1520.9; SD 02G IV.B)
4.8 **CEII.** When the company files CEII with FERC (for example Form No. 567 system flow diagrams), the filing must follow 18 CFR 388.113(d), including the justification, labeling in bold capital letters that the pages contain CEII and are marked "DO NOT RELEASE," segregation of the CEII portions, and a public version with the CEII redacted where practicable. The company's own copies are handled as Restricted. (MP-3)
4.9 Records that show compliance with 49 CFR 192.631 and the TSA directives must be kept in the compliance records system and protected from alteration. (SI-12; 192.631(j); SD 02G IV.C)

## 5. Compliance and enforcement
Violations may lead to retraining, written warning, loss of access, or termination, depending on intent and impact. Mishandling of SSI may also expose the company and the individual to TSA civil penalties. Compliance is checked through the quarterly SSI scan and the control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may relax the Part 1520 duties in 4.7.

## 7. Related documents
POL-01; POL-05; STD-07; STD-08; STD-10; P10 approved-tools list; records retention schedule; 49 CFR Part 1520; 18 CFR 388.113
