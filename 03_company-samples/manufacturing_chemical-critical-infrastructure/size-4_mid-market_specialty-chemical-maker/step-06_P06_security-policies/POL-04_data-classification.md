# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Information Security Manager (CySO) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (new; there was no classification scheme before) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-4, MP-2, MP-6, MP-7, SC-8, SC-28, CP-9, SI-12 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory drivers | 49 CFR Part 1520 (SSI); C-CHEMICAL-R02 (33 CFR 101.630(b), 101.650(c), 101.650(g)(4), 101.650(i)(2)); 6 CFR 27.400 (legacy CVI, voluntary); Fla. Stat. 501.171 |
| Supporting standards | STD-05 Backup and Recovery; STD-08 |

## 1. Purpose
Classify company information by the harm its disclosure, alteration, or loss could cause, and set handling rules for each class.

## 2. Scope
All information in any form, on any system, at any site, including OT configurations, logic, and recipes.

## 3. Classes
| Class | Examples | Handling minimums |
|---|---|---|
| **SSI** (legally controlled) | FSP, Facility Security Assessment, Cybersecurity Plan, critical systems lists, OT network maps once in the plan | 49 CFR 1520.9 rules: named need-to-know list; SSI marking; restricted share; no public AI tools; destruction when no longer needed |
| **Restricted** | Master recipes and formulations; DCS, SIS, and PLC configurations and logic; legacy CVI; vulnerability reports; employee SSNs and background checks | Named-user access; encrypted at rest and in transit; integrity checks for configurations and logic; offline backup copies; export alerts |
| **Confidential** | Customer data and TTRS tank data; prices; contracts; process history | Role-based access; encrypted at rest; shared outside the company only under contract |
| **Internal** | Procedures, general business documents | Company accounts only |
| **Public** | Published SDSs, marketing | Approved for release |

## 4. Policy statements
4.1 Every information asset must have an owner and a class. Data owners must classify new repositories when they are created. (RA-2; ID.AM-05)
4.2 SSI must be handled under 49 CFR Part 1520: it is disclosed only to covered persons with a need to know, marked, and stored only in the restricted SSI repository. (AC-3; MP-2; 49 CFR 1520.9; 33 CFR 101.630(b))
4.3 Restricted and SSI information must not be stored in general file shares, sent to personal accounts, or entered into AI tools other than those approved for that class (STD-07). (AC-3; AC-4)
4.4 Restricted and Confidential data must be encrypted at rest and in transit where technically feasible. For OT traffic that cannot be encrypted, zone and physical controls must be documented as compensating controls. (SC-8; SC-28; 33 CFR 101.650(c)(2))
4.5 Logs are Restricted. They must be captured and protected so that only privileged users can read them. (AU-9; 33 CFR 101.650(c)(1))
4.6 Configurations and logic for critical OT systems must be backed up at least weekly to offline media and nightly online, protected from alteration, and test-restored on the schedule in STD-05. (CP-9; 33 CFR 101.650(g)(4))
4.7 Removable media may be used on OT only after scanning at the media kiosk, and only by exception. Unused ports must be disabled. (MP-7; 33 CFR 101.650(i)(2))
4.8 Media and devices holding Restricted or SSI information must be sanitized before reuse or disposal, with a record kept. (MP-6)
4.9 Records must be kept for the periods in STD-03 and then destroyed. (SI-12)

## 5. Compliance and enforcement
Checked through quarterly share permission reports, data loss prevention alerts (from 2027), and the P07 assessment.

## 6. Exceptions
Under POL-01 4.7. No exceptions to 4.2.

## 7. Related documents
POL-01; POL-02; POL-05; STD-05; STD-07; FSP; 49 CFR Part 1520
