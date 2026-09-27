# Security Assessment Plan and Summary: Cris Santos Company | Finance and Insurance | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Community Federal Credit Union (member-owned federal credit union) |
| System assessed | Core and Digital Banking Platform (CDBP), per the SSP (P02) |
| Tier / Vertical | Micro / Finance and Insurance |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent IT audit consultant engaged by the Supervisory Committee under a fixed-fee letter. Took no part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the ISO; MSP lead technician on call |
| Assessment window | 2026-08-04 to 2026-08-06 (on site 2026-08-05) |
| Also satisfies | Independent testing of key controls, 12 CFR Part 748, Appendix A III.C.3 (N52-R01) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 86 determination statements.** Controls were chosen because they support the four High risks in P01 (BEC wire fraud, theft of member information from the shared mailbox, core processor incident notice, MSP compromise), cover High gaps in P03, or test what the MSP does on the credit union's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | No access reviews; shared password survived a departure (P01 R-004; P03 G-023) | Focused | Comprehensive (all 7 staff in the core, admin console, wire portal, LOS, and suite) |
| AC-5 | Wire dual control is the main fraud barrier (P03 G-029) | Focused | Comprehensive (all wire portal users and tokens) |
| IA-2(1), IA-2(2) | Password-only shared mailbox and MSP-held logins (R-001, R-002, R-010) | Focused | Focused (every administrator login; the shared mailbox) |
| AT-2(3) | BEC relies on staff being fooled (R-001, R-018; G-025, G-033) | Basic | Focused (5 of 7 staff interviewed) |
| AU-6 | No log review (G-030; R-003, R-009) | Basic | Basic |
| CP-9, CP-4 | Imaging snapshots in one account; nothing ever tested (R-010, R-015) | Focused | Focused |
| IR-6, IR-8 | No NCUA 72-hour step or member notice (G-010, G-043; R-007) | Basic | Basic |
| RA-3 | Risk assessment outdated since 2019 (R-017) | Basic | Basic |
| SA-9 | Vendor contracts and SOC reports (R-006, R-008, R-014; G-037, G-038, G-041) | Focused | Comprehensive (all 8 vendors that hold or reach member information) |

## 2. Methods and objects
- **Examine:** user lists from the core, admin console, wire portal, LOS, and suite; core role profiles; the wire portal administrator report and token list; the 2019 wire procedure and incident plan; vendor contracts and the SOC report folder; the P01 register and the 2019 questionnaire; training sign-in sheets; the MSP evidence listed below.
- **Interview:** President and CEO, ISO, Accounting and Compliance Officer, Lending Manager, 5 of 7 staff (training and incident reporting), and the MSP lead technician.
- **Test:**
  - user lists compared against the staff roster in each system
  - sign-in to the cloud console and the Member Services mailbox without a second factor (with the MSP present and the MSR who normally signs in)
  - portal role check: can one user both add a maker and approve (checked in the portal's role screen, not by sending a wire)
  - a review of 10 wire files from July 2026 for callback evidence (supports P03 G-025)

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-07-28 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch and antivirus report (July 2026) | SI-2, SI-3 (context) | Yes, 2026-08-03 |
| Device encryption report | SC-28 (context) | Yes, 2026-08-03 |
| Cloud snapshot policy and console user list | CP-9, IA-2(1) | Yes, 2026-08-04 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Suite MFA and sign-in settings | IA-2(2) | Yes, 2026-08-03 |
| Technician list with access, and MFA on the remote management platform | SA-9, AC-17 | Not received by fieldwork end; follow-up in POAM-013 |

## 3. Rules of engagement
- No test could move money or change member data. The portal role check was done on screen; no wire was keyed.
- Member information stayed on credit union systems. Screenshots were redacted before they went into the evidence folder. The SAR log was viewed by the ISO for the assessor; its contents were not copied (748.1(d)(5)).
- The assessor would stop and tell the ISO at once about any critical exposure. The shared mailbox and cloud console findings were reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 26 |
| Other than satisfied | 60 |
| **Total** | **86** |

**Fully other than satisfied:** IA-2(1), IA-2(2), AT-2(3), AU-6, CP-4, IR-6. No process or technology met the objective.
**Largely satisfied:** RA-3 (the 2026 register meets every objective except review, dissemination, and the update cycle, none of which had run by fieldwork) and IR-8 (the 2019 plan has a sound skeleton but none of the credit union-specific content).

**New findings from testing:**
1. The former MSR's core account was still enabled 5 months after her departure (AC-02f.[04], AC-02i.01). Core sign-in logs showed no use after her last day. Disabled on 2026-08-05. P01 R-004 updated; POAM-001.
2. The Member Services mailbox and the MSP's cloud console accepted a password alone (IA-02(02), IA-02(01)). The mailbox was converted to delegated access on 2026-08-12 (POAM-004); the cloud console is POAM-003.
3. The Operations Manager can administer the wire portal and approve wires (AC-05b.). POAM-002.
4. Of 10 July 2026 wire files, 6 were requested by email and 1 of those had a callback note. This confirms P03 G-025.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`: 4 High (POAM-004, POAM-006, POAM-010, POAM-013), 7 Moderate, and 2 Low. The High items match the P01 themes: trust in email and trust in vendors.

## 5. Deliverables
`assessment-results.csv` (86 rows), `poam.csv` (13 items), and this plan and summary. The Supervisory Committee received the results on 2026-08-25; the President and CEO accepted them on 2026-08-31.
