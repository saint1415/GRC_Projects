# Security Assessment Plan and Summary: Cris Santos Company | Defense Industrial Base | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts machine shop, DoD subcontractor) |
| System assessed | CUI Machining Enclave (CME), per the SSP (P02) |
| Tier / Vertical | Micro / Defense Industrial Base |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent consultant experienced in NIST SP 800-171A assessments, under a fixed-fee engagement. Not a C3PAO. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager; MSP lead technician on site for testing |
| Assessment window | 2026-08-10 to 2026-08-12 (on site 2026-08-11) |
| Purpose | Readiness assessment of selected controls before the CMMC Level 2 (Self) self-assessment (target 2027-03-15). It supports SP 800-171 3.12.1 but is not a CMMC assessment and produces no score |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 77 determination statements.** Controls were chosen because they support the High and Very High risks in P01 (CUI outside the enclave, DoD reporting, MSP compromise), carry 5-point SP 800-171 requirements with gaps in P03, or test what the MSP does on the company's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Former programmer's access lasted 110 days; shared accounts (P01 R-013, R-007; P03 3.1.1, 3.9.2) | Focused | Comprehensive (every account in SYS-01, SYS-02, ERP, Prime A portal, and MSP admin) |
| IA-2(1) | MFA on privileged access, including MSP-held logins (3.5.3); R-023 | Focused | Comprehensive (every administrator login) |
| AT-2 | No training after hire (3.2.1, 3.2.3); R-002, R-016 | Basic | Focused (5 of 7 employees interviewed) |
| AU-6 | No log review (3.3.5); R-022 | Basic | Basic |
| CP-9 | CUI in a commercial backup cloud (3.8.9; DFARS 252.204-7012(b)(2)(ii)(D)); R-003 | Focused | Focused |
| IR-6 | Cannot report to DoD (3.6.2; 252.204-7012(c)); R-006 | Focused | Focused |
| MP-7 | USB loading of older CNC machines (3.8.7, 3.8.8); R-012 | Focused | Comprehensive (all drives and both older machines) |
| PE-8 | Visitors and the foreign-national service visit (3.10.3, 3.10.4); R-009 | Basic | Comprehensive (June to August 2026 log) |
| SA-9 | MSP as External Service Provider; cloud provider CRM (32 CFR 170.19(c)(2)); R-007, R-003 | Focused | Comprehensive (cloud provider, MSP, backup subcontractor) |
| SC-7 | Flat network (3.13.1, 3.13.6); R-008 | Focused | Focused (one test path from staff Wi-Fi to a machine) |
| SC-28 | Unencrypted shop PCs (3.13.16); R-008 | Basic | Focused (3 devices) |
| CM-8 | Asset inventory and CMMC asset categories (3.4.1; 170.19(c)(1)) | Basic | Comprehensive (walkthrough of the whole unit) |

## 2. Methods and objects
- **Examine:** SYS-01, SYS-02, ERP, and Prime A portal user lists; staff roster; termination record; MSP contract and SOC 2 report; FedRAMP Marketplace listing; backup job report and settings; firewall rules; RMM device list and session log; visitor log; hire orientation checklist; draft POL-02 and POL-03.
- **Interview:** President, Office Manager, CNC Programmer, Quality Inspector, Lead Machinist, and 2 machinists (5 of 7 for training), and the MSP lead technician.
- **Test:**
  - account lists compared against the staff roster in every system
  - sign-in attempts without a second factor to the firewall, RMM console, and local administrator on SYS-03 (with the MSP present)
  - encryption status on SYS-03, SYS-04, and one laptop
  - a laptop on staff Wi-Fi trying to reach a networked CNC machine's file share
  - USB drives found at the older machines inserted on SYS-03 (scanned first) to check whether USB storage is blocked

### MSP evidence requested
The MSP operates most technical controls, so much of the evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Backup job report (July 2026), retention settings, and backup provider name and authorization status | CP-9, SA-9 | Yes, 2026-08-07. Provider confirmed as commercial, not FedRAMP authorized |
| Firewall rule export and firmware record | SC-7 | Yes, 2026-08-07 |
| RMM device list and session log (July 2026) | CM-8, AC-17 | Yes, 2026-08-07 |
| List of technicians with access, and MFA status for each | AC-2, IA-2(1) | Yes, 2026-08-10. Showed one technician without MFA |
| Encryption status report | SC-28 | Yes, 2026-08-07 |
| SOC 2 Type 2 report | SA-9 | Yes, 2026-08-05 (reviewed in P09) |
| U.S.-person confirmation for technicians | SA-9, PS-3 | Not received by fieldwork end; follow-up in POAM-009 |
| Responsibility matrix for CMMC | SA-9 (32 CFR 170.19(c)(2)(ii)) | Does not exist; follow-up in POAM-009 |

## 3. Rules of engagement
- No testing that could stop a machine or change a program. Machine shares were only listed, not written to. The MSP stayed on site for all tests.
- No CUI left the building. Screenshots showing file names of controlled drawings were redacted before they went into the evidence folder.
- The assessor would stop and tell the Office Manager at once about any critical exposure. The shared MSP administrator password (unchanged since a technician left the MSP in May 2026) and the RMM login without MFA were reported the same day, and the MSP fixed both on 2026-08-12.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 15 |
| Other than satisfied | 62 |
| **Total** | **77** |

**Fully other than satisfied:** AT-2, AU-6, IA-2(1), IR-6, MP-7, PE-8, SC-28. No process or technology met the objective.
**Partly satisfied:** CP-9 (backups run nightly and are verified, but in the wrong place and never restored), SC-7 (the external boundary is controlled; the inside is flat), AC-2 (users are approved and match the roster; the process around them is missing), PS-4 (property returned; access not), CM-8 (the 4 computers are tracked well; nothing else is), and SA-9 (only the confidentiality clause meets the objective).

**New findings from testing:**
1. One MSP technician's RMM console login had no MFA (IA-02(01)). Added to the risk register as R-023 and to POAM-002. The MSP enabled MFA on 2026-08-12.
2. The shared MSP administrator password had not been changed since a technician left the MSP in May 2026 (AC-02k.[02]). Changed on 2026-08-12; named accounts follow in POAM-001.
3. A laptop on staff Wi-Fi could open the file share on a networked CNC machine (SC-07a.[04]). POAM-004.
4. 4 of 5 employees interviewed could not say what CUI is (AT-02b.). POAM-011.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The 6 High items are POAM-002, POAM-007, POAM-008, POAM-009, POAM-010, and POAM-011. Their common theme is the one in P01: CUI and administrator access reach further than the enclave, and nobody is watching.

**Link to CMMC.** A determination of "Other than satisfied" here means the matching SP 800-171 requirement would be NOT MET in a CMMC self-assessment. None of the 13 controls would pass today.

## 5. Deliverables
`assessment-results.csv` (77 rows), `poam.csv` (13 items), and this plan and summary. The President accepted the results on 2026-08-31. The next independent check is a readiness re-check in January 2027, before the Level 2 self-assessment.
