# Security Assessment Plan and Summary: Cris Santos Company | Educational Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (K-12 tutoring and learning center) |
| System assessed | Tutoring Operations Platform (TOP), per the SSP (P02), plus contractor tutors' use of their own computers (SYS-07) |
| Tier / Vertical | Micro / Educational Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Center Director; MSP lead technician on call |
| Assessment window | 2026-08-03 to 2026-08-05 (on site 2026-08-04, before the center opened) |
| Also satisfies | Testing and monitoring of safeguards under the COPPA Rule, 16 CFR 312.8(b)(4) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 87 determination statements.** Controls were chosen because they support the three High risks in P01 (ransomware, theft of the "Student files" folder, platform account takeover), cover High and Moderate COPPA gaps in P03, test what the MSP does on the company's behalf, or test the contractor tutor model that no vendor covers.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Former contractor tutors with active accounts (P01 R-004); trial child accounts before consent (P03 G-017) | Focused | Comprehensive (all 21 tutor and staff users in the platform, scheduling platform, suite, and website) |
| IA-2(1) | No MFA in the platform or on MSP-held logins (312.8(b)(3)); R-003 | Focused | Focused |
| AC-20, PS-7 | Contractor tutors' personal computers and district rosters (99.31(a)(1)(i)(B)); R-005 | Focused | Focused (3 of 14 contractor tutors interviewed; email search) |
| AT-2, IR-6 | No training; nobody knew the district's 48-hour term; R-001, R-015 | Basic | Focused (4 staff and 3 contractor tutors interviewed) |
| CP-4, CP-9 | Backup never tested (312.8(b)(3)-(4)); R-010 | Focused | Focused |
| RA-3 | Risk assessment (312.8(b)(2)) | Basic | Basic |
| SA-9 | No written assurances from vendors (312.8(c)); AI module terms; R-008, R-013 | Focused | Comprehensive (all 5 vendors that hold children's information or administer systems) |
| SC-7 | Shared Wi-Fi segment; R-014 | Focused | Focused (external scan and guest Wi-Fi test) |
| SI-12 | Indefinite retention (312.10); R-007 | Basic | Comprehensive (platform record counts) |

## 2. Methods and objects
- **Examine:** platform, scheduling platform, suite, and website user lists; staff and contractor roster; offboarding records; platform settings and record counts; vendor terms and the platform SOC 2 report; MSP contract; contractor agreement template; P01 risk register; training records; the MSP evidence listed below.
- **Interview:** Owner, Center Director, Director of Tutoring, Enrollment and Billing Coordinator, 1 Lead Tutor, 3 contractor tutors, and the MSP lead technician.
- **Test:**
  - user lists compared against the staff and contractor roster
  - sign-in attempts to platform administrator accounts, the scheduling administrator, the backup console, and the firewall management page without a second factor (with the MSP present)
  - an external scan of the center's public internet address
  - a test laptop on the student and guest Wi-Fi, checking what it can reach
  - a search of the company mailbox for outgoing roster attachments since January 2026

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-07-27 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-07-31 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Firewall rule and Wi-Fi configuration export | SC-7 | Yes, 2026-07-31 |
| Monthly patch and antivirus report (July 2026) | Context for SI-2 and SI-3 (not assessed) | Yes, 2026-07-31 |
| Technician list with access to the company, and MFA on the remote management platform | SA-9, PS-7 | Not received by fieldwork end; follow-up in POAM-007 |
| Name of the backup subcontractor and its security terms | SA-9 (312.8(c)) | Not received by fieldwork end; follow-up in POAM-007 |

## 3. Rules of engagement
- No testing that could disrupt sessions. On-site tests ran on 2026-08-04 before the center opened at 2:30 pm. No configuration was changed by the assessor.
- No student information left the company. Screenshots were redacted before they went into the evidence folder, and contractor tutors showed their downloads folders on screen; no files were copied.
- The assessor would stop and tell the Center Director at once about any critical exposure. The internet-facing firewall management page was reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 19 |
| Other than satisfied | 68 |
| **Total** | **87** |

**Fully other than satisfied:** IA-2(1), AT-2, CP-4, SI-12, AC-20, IR-6. No process or technology met the objective.
**Largely satisfied:** RA-3 (the 2026 risk assessment meets every objective except review and update, which have never happened). **Partly satisfied:** CP-9 (backups run and are encrypted, but are not protected from deletion) and PS-4 (property is collected; access is not removed).

**New findings from testing:**
1. The firewall management page was reachable from the internet with a password only (SC-07c.). Added to the risk register as R-024; the MSP turned it off on 2026-08-06 and the assessor verified it. POAM-011.
2. A former temporary front-desk worker's account was still active in the scheduling platform, last used in May 2026 (AC-02f.[05]). Its log showed no sign-ins after the worker left. Disabled on 2026-08-04.
3. Two of the 3 contractor tutors interviewed still had district roster spreadsheets in their downloads folders (AC-20a.02). Both deleted them on screen; all contractor tutors will attest (POAM-008).
4. A test laptop on the guest Wi-Fi could reach a staff laptop's file-sharing prompt (SC-07a.[04]). POAM-011.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-002 (MFA), POAM-004 (backups), and POAM-005 (restore testing): the same account takeover and ransomware themes as P01.

## 5. Deliverables
`assessment-results.csv` (87 rows), `poam.csv` (13 items: 3 High, 9 Moderate, 1 Low; 8 In progress, 5 Open), and this plan and summary. The Owner accepted the results on 2026-08-28.
