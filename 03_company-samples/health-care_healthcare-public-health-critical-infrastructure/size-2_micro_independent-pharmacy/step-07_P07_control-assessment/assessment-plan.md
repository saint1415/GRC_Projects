# Security Assessment Plan and Summary: Cris Santos Company | Healthcare and Public Health | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent community pharmacy) |
| System assessed | Pharmacy Core SaaS Stack (PCSS), per the SSP (P02) |
| Tier / Vertical | Micro / Healthcare and Public Health |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent HIPAA security consultant under a fixed-fee engagement. Did not take part in the risk analysis (P01) or the gap analysis (P03) and operates no control. Accompanied by the Store Manager; MSP lead technician present for the tests |
| Assessment window | 2026-08-04 to 2026-08-06 (on-site tests 2026-08-05 after the 7:00 p.m. closing) |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **15 controls, 102 determination statements.** Controls were chosen because they support the four High risks in P01 (ransomware, data theft, the packaging workstation, MSP compromise), cover Required HIPAA specifications or DEA duties with gaps in P03, or test what the MSP does on the pharmacy's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Former technician's accounts active about 11 weeks; shared logins (P01 R-004, R-012; P03 164.308(a)(3)(ii)(C)) | Focused | Comprehensive (all 7 users in the PMS, suite, fax portal, and delivery app) |
| AC-6 | Controlled substance alteration permission fixed during the gap analysis (21 CFR 1311.200(e); R-006); shared desktop rights (R-003) | Focused | Comprehensive (all PMS roles) |
| AU-6 | Daily EPCS audit report never read (21 CFR 1311.215(c); 164.308(a)(1)(ii)(D); R-011) | Focused | Focused (EPCS review log and 90 retained reports) |
| IA-2(1) | MFA on administrator access, including MSP-held logins (164.312(d); R-003, R-013) | Focused | Focused |
| SI-3, SI-2 | MSP antivirus and patching; unsupported packaging workstation (R-001, R-008) | Focused | Focused (3 computers including the packaging workstation; alert routing test) |
| CP-9, CP-4 | Backups never tested (164.308(a)(7)(ii)(A), (D); R-005) | Focused | Focused |
| AT-2, IR-6 | No security training; no incident reporting (164.308(a)(5), (a)(6); R-001, R-016) | Basic | Focused (5 of 7 staff interviewed) |
| SA-9 | Missing BAAs and no vendor oversight (164.308(b); R-008, R-012, R-013) | Focused | Comprehensive (all 7 vendors that handle ePHI or administer systems) |
| SC-28 | Unencrypted desktops (164.312(a)(2)(iv); R-007) | Basic | Focused (3 devices tested) |
| RA-3 | Risk analysis (164.308(a)(1)(ii)(A); R-015) | Basic | Basic |
| IA-5 | Password and CSOS key handling (164.308(a)(5)(ii)(D); 21 CFR 1311.30; R-014) | Focused | Focused (3 computers; owner laptop) |

## 2. Methods and objects
- **Examine:** PMS, suite, fax portal, and delivery app user lists; PMS role and permission reports; the EPCS audit report screen and review log; suite security settings; the BAA folder; the MSP contract; the PMS vendor SOC 2 and EPCS audit reports; the P01 risk register (draft) and the 2022 vendor checklist; the video sign-in sheet; the MSP evidence listed below.
- **Interview:** pharmacist-owner, Staff Pharmacist, Store Manager, Lead Pharmacy Technician, 5 of 7 staff (training and incident reporting), and the MSP lead technician.
- **Test (2026-08-05, after closing):**
  - user lists compared against the staff roster in the PMS, suite, fax portal, and delivery app
  - sign-in attempts to the backup console and to the PMS administrator role inside the store without a second factor (with the MSP present)
  - encryption status on 2 desktops and 1 laptop
  - patch status on 3 computers, including the packaging workstation
  - the local administrator password tried on 3 computers (with the MSP present)
  - an industry-standard harmless antivirus test file on the back-office desktop, and an after-hours test alert to check routing

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-07-28 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-08-03 |
| Antivirus console export (all devices) | SI-3 | Yes, 2026-08-03 |
| Device encryption report | SC-28 | Yes, 2026-08-03 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-04 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Firewall rule export and firmware record | SC-7, SI-2 | Yes, 2026-08-03 |
| Device policy report (screen lock, local accounts) | AC-6, IA-5 | Yes, 2026-08-03 |
| Technician list with access to the pharmacy, and MFA on the remote management platform | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-010 |
| Subcontractor list and confirmation of the backup vendor BAA | SA-9 (164.314(a)(2)(iii)) | Not received by fieldwork end; follow-up in POAM-010 |

## 3. Rules of engagement
- No testing during store hours or anything that could stop dispensing. Tests ran after closing on 2026-08-05. The packaging workstation was checked but not changed, and the strip packager was not used.
- No ePHI left the store. Screenshots were redacted before they went into the evidence folder. The assessor did not open any patient profile.
- The assessor would stop and tell the Store Manager and the pharmacist-owner at once about any critical exposure. The shared local administrator password was reported the same evening.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 34 |
| Other than satisfied | 68 |
| **Total** | **102** |

**Fully other than satisfied:** AC-6, AU-6, IA-2(1), CP-4, SC-28, IR-6. No process or technology met the objective.
**Largely satisfied:** RA-3 (the 2026 risk analysis meets every objective except an update, which has never happened) and SI-3 (detection and quarantine work on the 7 computers; there is no protection on the packaging workstation and no after-hours alerting).

**New findings from testing:**
1. The same local administrator password works on every desktop and on the packaging workstation; it was set by the MSP in 2021 (IA-05g.). Added to the risk register as R-023 and to POAM-015.
2. The shared counter desktop account has local administrator rights (AC-06). POAM-003.
3. The backup console and the in-store PMS administrator sign-in accept a password alone (IA-02(01)). POAM-005.
4. An after-hours antivirus alert was not seen until the next morning (SI-03c.02[02]). POAM-006.

**Controlled substance findings.** The PMS permission report confirmed that only the pharmacist role can now alter dispensed controlled substance records (fixed 2026-07-17). The daily EPCS audit report is now opened, but not every business day and with no log (AU-06a.); the DEA reporting path is missing (AU-06b.). Both are in POAM-004.

All 15 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-006, POAM-007, POAM-008, and POAM-014: malware detection, backups, and the packaging workstation, the same ransomware theme as P01.

## 5. Deliverables
`assessment-results.csv` (102 rows), `poam.csv` (15 items), and this plan and summary. The pharmacist-owner accepted the results on 2026-08-28.
