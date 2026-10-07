# Data Classification and CUI Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | President (data owner); CNC Programmer (CUI data custodian) |
| Approved by | President, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and when a customer's marking or handling rules change |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-2, MP-3, MP-4, MP-5, MP-6, MP-7, SC-28, AC-4, AC-20, SA-9, CP-9 |
| CSF 2.0 | ID.AM-05, ID.AM-07, PR.DS-01, PR.DS-02, PR.PS-03, GV.SC-05 |
| SP 800-171 Rev. 2 | 3.1.3, 3.1.20, 3.1.21, 3.8.1 to 3.8.9, 3.13.16 |
| Other rules | 32 CFR Part 2002 (CUI program); ITAR 22 CFR 120.56; EAR 15 CFR 734 |

## 1. Purpose
Tell everyone how to recognize CUI and other company information, where each kind may be kept, and how to print, move, and destroy it.

## 2. Scope
All company information in any form: files, email, programs, printed drawings, USB drives, and anything typed into a tool.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| President | Data owner; decides classification questions; export control decisions |
| CNC Programmer | CUI custodian: job folders, CAM and NC programs, setup sheet templates, approved AI tools list (with the President) |
| Lead Machinist | Printed CUI and USB drives on the floor |
| Office Manager | Shred bin, media log, ERP attachment check |
| All workforce | Handle information by its class |

## 4. Policy statements
4.1 **Classes.**
| Class | What it is here | Examples |
|---|---|---|
| CUI | Controlled technical information from Prime A or Supplier B and anything made from it. Includes ITAR technical data and EAR-controlled technology | Drawings, 3D models, specifications, CAM files, NC programs, setup sheets, CMM programs, inspection data tied to a drawing |
| FCI | Information about a DoD contract that is not public and is not CUI | DoD purchase orders, delivery schedules, prices |
| Internal | Business information | Payroll, HR files, quotes for commercial work, Customer C drawings that are not export controlled |
| Public | Approved for release | Website text, capability sheet |

4.2 **How to recognize CUI.** Treat as CUI anything from a defense customer that carries a CUI banner, a distribution statement, or an export control notice, and everything made from it. When in doubt, treat it as CUI and ask the President. (RA-2; ID.AM-05)

4.3 **Where CUI may be stored.** Only in the CUI suite job folders and on the CUI Assets listed in POL-02 A.4. Never in the commercial suite, the ERP, the commercial backup, personal devices, or personal accounts. The ERP may hold drawing numbers and revision letters only, never the drawing itself. (AC-4; 3.1.3; 3.1.20)

4.4 **How CUI may be sent.** Only through the CUI suite (to approved customer domains) or the Prime A portal. Customers that email CUI to the commercial suite must be asked to resend to the CUI suite, and the commercial copy is deleted. (AC-4; SC-8)

4.5 **Marking.** Customer markings must never be removed. Setup sheets, CAM printouts, and inspection reports made from CUI carry a "CUI" banner from the template. Company USB drives carry an owner label. (MP-3; 3.8.4)

4.6 **AI tools.** CUI and FCI may be entered only into AI tools on the approved tools list, which is kept by the CNC Programmer and the President. On 2026-09-01 the list has **no** approved AI tool for CUI. A tool can be added only after a P10 assessment confirms it runs inside a FedRAMP Moderate-or-higher authorized boundary listed in the SSP. Public chatbots are never approved for CUI or FCI. AI output is never the source for a dimension, tolerance, NC program, or inspection criterion. (AC-20; SA-9; 3.1.20)

4.7 **Paper.** Print CUI only on the shop printer. Drawings go out with the job folder and come back to the locked cabinet at the end of the shift. Do not take CUI home. (MP-2; MP-4; 3.8.1; 3.8.2)

4.8 **USB drives.** Only the 2 company-owned encrypted USB drives may be used, and only to load the 2 older CNC machines. They are kept in a locked drawer, logged when taken, scanned on the CAM workstation, and wiped after each transfer. Any other drive found is handed to the Office Manager and destroyed. USB storage is blocked on other computers. (MP-7; 3.8.6 to 3.8.8)

4.9 **Destruction.** Paper CUI goes in the locked shred bin and is cross-cut shredded. Computers and drives are wiped by the MSP, with a certificate, before disposal, repair, or reuse. (MP-6; 3.8.3; 3.7.3)

4.10 **Outside processors.** Send outside processors a process sheet without the drawing where possible. If a drawing must go, the purchase order must carry DFARS 252.204-7012 and 252.204-7020, the processor's SPRS score must be checked, and the drawing is logged out and back. (MP-5; SR-3; 3.8.5)

4.11 **Export control.** Only U.S. persons (22 CFR 120.62) may access ITAR technical data. Showing a drawing to a foreign person, including a visitor, is a release that may be an export (22 CFR 120.56). Questions go to the President as Empowered Official before access is given. (AC-3; 3.1.2)

4.12 **Encryption at rest.** Every computer and USB drive that holds CUI uses full-disk encryption with a FIPS-validated module. (SC-28; 3.13.16; 3.13.11)

4.13 **Backups.** CUI is backed up only by a service inside a FedRAMP Moderate-or-higher authorized boundary listed in the SSP. Backups are tested by a restore at least twice a year. A backup of a computer that syncs CUI is treated as CUI. (CP-9; 3.8.9)

## 5. Compliance and enforcement
The Office Manager runs a quarterly ERP attachment report and a commercial suite search for drawing files, and checks the USB log and shred bin service monthly. Violations are handled under POL-02 A.9.

## 6. Exceptions
None for 4.3, 4.6, or 4.11. Others under POL-02 A.10.

## 7. Related documents
POL-02, POL-03, the SSP (P02), the gap analysis (P03), the AI risk assessment (P10).
