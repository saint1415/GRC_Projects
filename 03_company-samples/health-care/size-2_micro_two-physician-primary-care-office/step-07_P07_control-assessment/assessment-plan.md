# Security Assessment Plan and Summary: Cris Santos Company | Health Care | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (primary care office, two physicians) |
| System assessed | Office Clinical Platform (OCP), per the SSP (P02) |
| Tier / Vertical | Micro / Health Care and Social Assistance |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent HIPAA security consultant under a fixed-fee engagement. Did not take part in the risk analysis (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager; MSP lead technician on call |
| Assessment window | 2026-08-10 to 2026-08-12 (on site 2026-08-11) |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 91 determination statements.** Controls were chosen because they support the three High risks in P01 (ransomware, PHI exfiltration, MSP compromise), cover Required HIPAA implementation specifications with gaps in P03, or test what the MSP does on the practice's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Former MA account active 3 months (P01 R-004; P03 164.308(a)(3)(ii)(C)) | Focused | Comprehensive (all 7 users in EHR, suite, fax) |
| IA-2(1) | MFA on administrator access, including MSP-held logins (164.312(d)); R-013 | Focused | Focused |
| AT-2, IR-6 | No training after hire; no incident reporting (164.308(a)(5), (a)(6)); R-001, R-015 | Basic | Focused (5 of 7 staff interviewed) |
| AU-6 | No log review (164.308(a)(1)(ii)(D)); R-008 | Basic | Basic |
| CP-4, CP-9 | Backup never tested (164.308(a)(7)(ii)(A), (D)); R-005 | Focused | Focused |
| RA-3 | Risk analysis (164.308(a)(1)(ii)(A)); R-014 | Basic | Basic |
| SA-9 | Missing BAAs and no vendor oversight (164.308(b)); R-006, R-011, R-013 | Focused | Comprehensive (all 7 vendors that handle ePHI or administer systems) |
| SC-28 | Unencrypted desktops (164.312(a)(2)(iv)); R-007 | Basic | Focused (3 devices tested) |
| SI-2, SI-3 | MSP patching and antivirus; R-001, R-017 | Focused | Focused (3 computers; alert routing test) |

## 2. Methods and objects
- **Examine:** EHR, suite, and fax user lists; EHR role list; suite security settings; BAA folder; MSP contract; EHR vendor SOC 2 report; P01 risk register and 2019 checklist; new-hire video sign-in sheet; the MSP evidence listed below.
- **Interview:** owner physician, Office Manager, Billing Specialist, 5 of 7 staff (training and incident reporting), and the MSP lead technician.
- **Test:**
  - user lists compared against the staff roster in the EHR, suite, and fax portal
  - sign-in attempts to the backup console and firewall management page without a second factor (with the MSP present)
  - encryption status on 2 desktops and 1 laptop
  - patch status on 3 computers, including the procedure-room workstation
  - an industry-standard harmless antivirus test file on 1 desktop, and an after-hours test alert to check routing

### What each test could show
The new policies (P06) were drafts during fieldwork; they were approved on 2026-08-31, after fieldwork ended. The drafts were therefore reviewed for design only. A control that a draft policy introduces has not operated yet, so it cannot be tested for operation. The `test_type` column in `assessment-results.csv` says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control existed before 2026 and was tested on samples or live systems | 43 |
| Design | The control is new (the 2026 risk analysis, or a draft policy); its design was reviewed. Operation is tested at the next annual review (risk analysis) or the 2027-02 follow-up (draft policy) | 9 |
| Not implemented | Nothing existed to test | 39 |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-AC-2 and so on), with the population each test was drawn from (for example, the user lists were compared with the 7 staff and the April 2026 termination in EV-001, and the 10 computers come from the MSP device list in EV-009).

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-08-07 |
| Antivirus console export (all devices) | SI-3 | Yes, 2026-08-07 |
| Device encryption report | SC-28 | Yes, 2026-08-07 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-10 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Firewall rule export and firmware record | SC-7, SI-2 | Yes, 2026-08-07 |
| Technician list with access to the practice, and MFA on the remote management platform | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-009 |
| Subcontractor list and confirmation of the backup vendor BAA | SA-9 (164.314(a)(2)(iii)) | Not received by fieldwork end; follow-up in POAM-009 |

## 3. Rules of engagement
- No testing that could disrupt patient care. On-site tests ran over the lunch break on 2026-08-11. The procedure-room workstation was checked but not changed.
- No ePHI left the office. Screenshots were redacted before they went into the evidence folder.
- The assessor would stop and tell the Office Manager at once about any critical exposure. The patching exclusion on the procedure-room workstation was reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 35 |
| Other than satisfied | 56 |
| **Total** | **91** |

**Fully other than satisfied:** IA-2(1), AU-6, CP-4, IR-6, SC-28. No process or technology met the objective.
**Largely satisfied:** RA-3 (the 2026 risk analysis meets every objective except the annual update, which has never happened), SI-3 (detection and quarantine work; alerting after hours does not), and SI-2 (patching works, except for the excluded workstation and undefined time limits).

**New findings from testing:**
1. The MSP had excluded the procedure-room workstation from patching since April 2026 at the device vendor's request, without telling the practice (SI-02a.[03], SI-02d.). Added to the risk register as R-023 and to POAM-011.
2. The fax portal still listed the former MA's account after the EHR and suite accounts were disabled (AC-02i.01). Its log showed no sign-ins after termination. Removed on 2026-08-12.
3. The backup console and firewall management login accept a password alone (IA-02(01)). POAM-002.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-003, POAM-004, and POAM-005: backups and malware detection, the same ransomware theme as P01.

## 5. Deliverables
`assessment-results.csv` (91 rows), `poam.csv` (13 items), and this plan and summary. The owner physician accepted the results on 2026-08-31.
