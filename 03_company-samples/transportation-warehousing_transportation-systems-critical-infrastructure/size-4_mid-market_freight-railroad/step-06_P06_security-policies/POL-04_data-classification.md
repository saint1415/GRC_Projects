# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Director of Safety, Security, and Hazmat (SSI) with the Cybersecurity Manager (technical protections) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, incidents, or changes to 49 CFR part 1520 |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, IR-6, MP-3, MP-4, MP-6, SC-8, SC-12, SC-13, SC-28, CP-9, SI-12 |
| CSF 2.0 | ID.AM-05, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-01 |
| Regulatory basis | C-TRANSPORTATION-S03 (1520.9, 1520.13, 1520.19; 1570.121(c)); C-TRANSPORTATION-R01 (SD 1580/82-2022-01E IV.B, III.B.2.b; SD 1580-21-01E II.D.1.b); C-TRANSPORTATION-S02 (1580.205(h)); C-TRANSPORTATION-S06 (172.802); C-TRANSPORTATION-S07 (Fla. Stat. 501.171) |
| Supporting standards | STD-10 SSI handling standard; STD-08 Encryption and key management standard; STD-07 Contingency and recovery standard; STD-01 Configuration standard |

## 1. Purpose
Classify company information by sensitivity and set handling rules for each class, including the federal rules for Sensitive Security Information (SSI), so that plans and data an attacker could use against train operations stay protected.

## 2. Scope
All information the company creates, receives, or holds, in any form, at any location, including information held for the company by vendors (for example the TMS, the MSSP, and cloud providers) and the car data the company holds for the affiliated and contracted short lines.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Safety, Security, and Hazmat | Decides what is SSI; keeps the SSI access list and the restricted SSI library; reports unauthorized SSI release to TSA |
| Cybersecurity Manager | Technical protections (encryption, access, backups); configuration baselines |
| Department heads | Classify the information their departments create; approve need-to-know |
| General Counsel | SSI disclosure questions and requests from third parties |
| All workforce | Label and handle information by its class |

## 4. Policy statements
4.1 Company information has four classes:

| Class | Examples | Handling minimums |
|---|---|---|
| **SSI (federal)** | The CIP, the CAP, CAP annual reports and drafts, assessment and test results on Critical Cyber Systems, the 2022 vulnerability assessment and remediation plan, CISA incident reports made under the directive, TSA-marked documents, the security training program | 49 CFR part 1520 rules in 4.2 to 4.4; restricted SSI library only; named need-to-know access |
| **Restricted** | OT network diagrams and configurations; CAD/CTC, BOS, and field controller configurations; RSSM car location data; credentials and keys; the hazmat security plan; employee personal information, engineer and conductor certification and medical records; track, bridge, and signal imagery (AI-001) | Need-to-know access; encrypted at rest and in transit; no personal email, removable media, or unapproved AI tools |
| **Internal** | Train schedules, bulletins, shipper contracts and rates, operating procedures, the shared service agreements | Employees and approved contractors |
| **Public** | Website content, published tariffs | No restriction |

(RA-2; ID.AM-05)

4.2 **SSI access.** SSI must be kept in the restricted SSI library (or a locked container for paper), disclosed only to covered persons with a need to know, and never copied to general file shares, email folders, or chat. Requests for SSI from anyone without a need to know must be referred to TSA. Vendors (for example the MSSP or an assessor) get SSI only after a written need-to-know record. Access to the library is reviewed quarterly. (AC-3; MP-4; 1520.9(a); 1570.121(c))
4.3 **SSI marking and destruction.** SSI must carry the protective marking and limited distribution statement in 49 CFR 1520.13, including drafts of CAP reports, and be destroyed as 1520.19 requires when no longer needed. Unmarked SSI received from others must be marked and the sender told (1520.9(b)). Each CAP and CIP submission to TSA gets a marking check before filing. (MP-3; MP-6; ID.AM-08)
4.4 If SSI may have been released to unauthorized persons, including through a cyber incident, the Director of Safety, Security, and Hazmat must promptly inform TSA (1520.9(c); POL-03 4.6). (IR-6)
4.5 The hazmat security plan is available only to employees who implement it, on a need-to-know basis (49 CFR 172.802). (AC-3)
4.6 **Encryption.** Restricted data and SSI must be encrypted at rest and in transit with algorithms in STD-08. OT traffic that crosses IT networks or leased circuits must be encrypted or otherwise protected (SD III.B.2.b). The 2 leased code line circuits and 6 legacy tower links must move to encrypted paths by 2027-06-30. (SC-8; SC-28; PR.DS-01; PR.DS-02)
4.7 **Backups.** CAD/CTC, BOS, crew management, and file services data must be backed up daily to the write-once vault in the separate backup account with at least 35 days retention, with credentials separate from production. Backups are scanned for malicious artifacts when made and when restored in testing. Restores of each TDPO component must be tested quarterly (STD-07). (CP-9; PR.DS-11; SD 1580-21-01E II.D.1.b)
4.8 **Retention.** Records are kept as the retention schedule sets, at least: chain-of-custody records for RSSM transfers 60 days (1580.205(h); company practice 1 year); TSA security training records 5 years (1570.121(a)(2)); CAD/CTC train sheets, warrants, and dispatcher log 3 years; security logs as STD-02 sets. (SI-12)
4.9 **Media sanitization.** Media holding Restricted data or SSI, including retired consoles, field controllers, onboard units, and crew tablets, must be wiped or destroyed by a method that prevents recovery, with a destruction record. (MP-6)
4.10 **Data held for others.** Car and customer data the company holds for the affiliated and contracted short lines is Restricted. It is used only to provide the shared service, segregated by railroad in the TMS and CAD/CTC, and returned or deleted as each service agreement requires. (AC-3; PR.DS-01)
4.11 Restricted data, SSI, and infrastructure imagery must not be entered into any AI tool that is not on the approved-tools list for that class of data (POL-05 4.8; STD-05). (AC-3)

## 5. Compliance and enforcement
Violations are handled under POL-01 statement 4.11. SSI violations may also be reported to TSA as 1520.9(c) requires. Compliance is checked through the annual control assessment (P07) and quarterly SSI library reviews.

## 6. Exceptions
Exceptions follow POL-01 statement 4.9. No exception may permit handling SSI in a way that part 1520 prohibits.

## 7. Related documents
POL-01; POL-02; POL-05; STD-07; STD-08; STD-10; 49 CFR part 1520; 49 CFR 1570.121; 49 CFR 172.800 and 172.802; SD 1580/82-2022-01E IV.B; retention schedule
