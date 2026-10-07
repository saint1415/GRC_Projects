# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group General Counsel (group privacy office), with the Group CISO |
| Approved by | Group CISO, under authority of POL-01, 2026-09-22 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-21, MP-3, MP-4, MP-6, SC-8, SC-28, CP-9, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory drivers | SSI 1520.9, 1520.11, 1520.13, 1520.19; C-ENERGY-R03 (SD 02G IV.B); CEII 388.113; State breach (Florida worked example: Fla. Stat. 501.171(2), (8)) |
| Division supplements | Gas Transmission: TSA plan documents and CEII filings. Gathering and Production: royalty owner data. Integrity Services: client SSI, CEII, and assessment evidence |

## 1. Purpose
Classify group information by sensitivity and by whose information it is, and set handling rules, including the legal rules for SSI.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including information clients and affiliates share with a division and copies on shared platforms.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group General Counsel | Owns the classes, the SSI and CEII rules, and the retention schedule |
| Division SSI owners (Director of Pipeline Cybersecurity; Integrity Services Client Security Officer) | Run the SSI register, need-to-know groups, marking, and destruction for their division |
| Data owners | Classify and label datasets; approve access and sharing |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (SSI, CEII, OT configurations and network diagrams, credentials and keys, Social Security and taxpayer numbers, bank account data), **Confidential** (client integrity data, measurement and commercial data, other personal information), **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 **SSI.** Records containing SSI, including TSA plans, reports, and assessment results and the same material received from clients, must:
- be marked with the protective marking SENSITIVE SECURITY INFORMATION and the distribution limitation statement, conspicuously on electronic records (1520.13);
- be shared only with covered persons who have a need to know (1520.9(a)(2), 1520.11), through named need-to-know groups;
- be stored only in an approved SSI store or a locked container (1520.9(a)(1));
- be marked on receipt if they arrive unmarked, with the sender informed (1520.9(b));
- be destroyed completely when no longer needed (1520.19(b));
- have requests from other persons referred to TSA (1520.9(a)(3)).
(MP-3; MP-4; AC-3; AC-21; MP-6; PR.DS-01; SD 02G IV.B)

4.3 **SSI disclosure.** Anyone who learns that SSI has been released to unauthorized persons must report it to the group SOC at once, and the division SSI owner must inform TSA promptly. (IR-6; 1520.9(c))

4.4 **Sharing between divisions.** A division may share its SSI or CEII with another division only for a defined project, only the excerpts needed, and only into the receiving division's SSI store. The receiving division must apply 4.2 in full. (AC-21; PR.DS-10)

4.5 **CEII.** CEII filed with FERC must be submitted with a request for CEII treatment under 18 CFR 388.113. CEII received from clients must be handled as the client agreement requires and at least as Restricted. (MP-3; AC-3)

4.6 Restricted information must be encrypted at rest and in transit with approved algorithms and group-managed keys. OT traffic that crosses IT networks must be encrypted. (SC-28; SC-8; PR.DS-01; PR.DS-02; SD 02G III.B.2.b)

4.7 **Engagement evidence.** Client network captures, firewall rules, diagrams, and configurations collected by the OT Assessment Practice must be kept only in the assessment evidence store, removed from toolkits at engagement close, and deleted 30 days after close unless the client contract requires otherwise, with a deletion certificate. (MP-6; SI-12; ID.AM-08)

4.8 **Personal information.** Royalty owner and employee personal information must stay in its system of record. Bulk exports to file shares are prohibited unless the data owner approves a purpose and a deletion date. Records no longer retained must be disposed of so they are unreadable (Fla. Stat. 501.171(8) as the worked example; each state's law applies to its residents). (SI-12; MP-6; PR.DS-01)

4.9 Backups of Restricted and Critical Cyber System data must be held separately from production (offline or immutable), checked for known malicious code, and restore-tested at least annually. (CP-9; PR.DS-11; SD 02G III.F.1.c)

4.10 Restricted information must not be entered into any AI tool unless the tool is approved under the Group AI Standard for that class. SSI and OT configurations must never be entered into a generative AI tool. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.12. Compliance is checked through the P07 assessment (AC-3, MP-3, MP-6), SSI register reviews, and the P09 SOC 2 readiness work.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may relax a Part 1520 duty.

## 7. Related documents
POL-01; POL-02; POL-03; `division-supplements.md`; P04 cloud control map; P10 Group AI Standard.
