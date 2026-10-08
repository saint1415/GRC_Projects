# Security Assessment Plan and Results Memo: Cris Santos Company | Health Care | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (solo primary care physician practice) |
| System assessed | Practice Systems Profile (PSP), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Health Care and Social Assistance |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The physician-owner (self-assessment), assisted by the on-call IT consultant after the consultant signed a BAA on 2026-07-17. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant helped run the tests and read the settings but is also the person who supports the laptop |
| Assessment window | 2026-07-20 to 2026-07-24 (tests on 2026-07-23) |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 38 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-004) or a Required HIPAA specification with a gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1), IA-2(2) | MFA on the EHR and email (R-002; 164.312(d)) | Basic / all accounts |
| SC-28 | Laptop encryption (R-004; 164.312(a)(2)(iv)) | Basic / all 3 devices |
| SI-3 | Ransomware defense on the laptop (R-001) | Focused / laptop |
| CP-9 | Backups (R-012; 164.308(a)(7)(ii)(A)) | Basic / EHR and local data |
| AC-11 | Device lock (164.312(a)(2)(iii)) | Basic / laptop and tablet |
| SA-9 | Vendors and BAAs (R-003, R-007, R-008, R-009; 164.308(b)) | Focused / all 7 vendors |
| AU-6 | Activity review (Required, 164.308(a)(1)(ii)(D)) | Basic |
| IR-6 | Incident reporting (Required, 164.308(a)(6)(ii)) | Basic |
| RA-3 | Risk analysis (Required, 164.308(a)(1)(ii)(A)) | Basic |

## 2. Methods and objects
- **Examine:** EHR security and user settings, email and fax account security pages, device encryption and lock settings, antivirus status, the BAA folder, the EHR vendor's SOC 2 report, P01 and P05.
- **Test (2026-07-23):** sign-ins to the EHR, email, and cloud fax from a new browser; idle-lock timing on the laptop and tablet; download of a standard antivirus test file; encryption status on each device; review of the remote-support tool's settings.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT consultant challenged each answer against what was on screen.

### What each test could show
No written policy existed during fieldwork. POL-01 was drafted afterward from these results and the gaps, and adopted on 2026-08-31, so none of its new rules had operated yet and none was tested here. The first risk analysis (P01) was completed on 2026-07-24, inside the assessment window, so it could be reviewed for design only. The `test_type` column in `assessment-results.csv` says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control existed before the assessment and was tested on the live accounts, devices and vendor records | 20 |
| Design | The control is new (the 2026 risk analysis); its design was reviewed. Operation is checked at the July 2027 annual review | 6 |
| Not implemented | Nothing existed to test | 12 |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-RA-3 and so on), with the population each test covered: the EHR, email and fax accounts (EV-001, EV-004, EV-006), the 3 devices (EV-007, EV-008), and the 7 vendors that handle PHI (EV-013). Controls that POL-01 introduces are tested for operation at the 2027-02 follow-up, after at least one quarter of use.

## 3. Rules of engagement
- No testing during clinic hours. No patient data copied off the devices; screenshots were cropped to settings only.
- The IT consultant worked only under the BAA signed 2026-07-17, in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 21 |
| Other than satisfied | 17 |
| **Total** | **38** |

**Fully satisfied:** IA-2(1) (the EHR vendor enforces MFA) and SI-3 (built-in antivirus detected and quarantined the test file).
**Fully other than satisfied:** IA-2(2), SC-28, AU-6, IR-6.
**Partly satisfied:** RA-3 (the analysis exists; no review cycle yet), CP-9 (EHR backups inherited; local data not backed up), AC-11 (15-minute laptop lock), SA-9 (only the EHR vendor is overseen).

**New finding:** the IT consultant's remote-support tool on the laptop still had unattended access turned on (SA-09a.[03]). The owner turned it off during the session on 2026-07-23, and the rule is now POL-01 6.4. P01 R-008 and POAM-003 track the remaining steps (consultant MFA, removing the tool when not needed). The cloud fax MFA gap found in P04 was confirmed by test (IA-02(02)).

The 8 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-008). The High items are POAM-001 (MFA) and POAM-002 (disk encryption), both due 2026-09-15.

## 5. Deliverables
`assessment-results.csv` (38 rows), `poam.csv` (8 items), and this memo. Accepted by the physician-owner on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.
