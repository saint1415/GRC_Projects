# Security Assessment Plan and Summary: Cris Santos Company | Health Care | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (multi-specialty physician practice) |
| System assessed | Clinical and Revenue Cycle Platform (CRCP), per the SSP (P02) |
| Tier / Vertical | Small / Health Care and Social Assistance |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in operating or designing the controls. Escorted by the IT Manager |
| Assessment window | 2026-08-03 to 2026-08-07 (walkthrough of both clinics 2026-08-05) |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 164 determination statements.** Controls were chosen because they support the three High risks in P01, cover the Required HIPAA implementation specifications with gaps in P03, or support Required implementation specifications (risk analysis, access, audit, contingency).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-6, AC-11, IA-2, IA-2(1), IA-5 | Access control gaps (P03 164.308(a)(3)-(4), 164.312(a), (d)); R-004, R-021 | Focused | Focused |
| AT-2 | Training gap (164.308(a)(5)); R-001 | Basic | Focused |
| AU-6 | No log review (164.308(a)(1)(ii)(D)); R-006 | Basic | Basic |
| CP-2, CP-4, CP-9 | Contingency gaps (164.308(a)(7)); R-005 (High) | Focused | Focused |
| IR-4, IR-6 | No incident capability (164.308(a)(6)) | Focused | Basic |
| MP-6, PE-3 | Physical gaps (164.310) | Basic | Focused (both clinics) |
| RA-3, RA-5 | Risk analysis and vulnerability management | Focused | Basic |
| SA-9 | Missing BAAs (164.308(b)); R-022 (High) | Focused | Focused |
| SC-8, SC-28 | Encryption (164.312(a)(2)(iv), (e)) | Basic | Focused |
| SI-2, SI-3 | Patching and malware; R-001, R-013 | Focused | Focused |

## 2. Methods and objects
- **Examine:** identity provider and EHR exports, backup and patch reports, BAAs and contracts, training roster, the 2021 and 2026 risk assessments, clinic walkthrough notes.
- **Interview:** Practice Administrator, IT Manager, MSP lead technician, Privacy Officer, HR and Payroll Specialist, both Clinic Managers, and 8 randomly selected staff (incident reporting awareness).
- **Test:**
  - idle-lock on 10 workstations and the modality
  - sign-in tests, including an administrator sign-in with a hardware key
  - local admin password comparison on 10 workstations
  - default-credential test on networked medical devices, with vendor approval and outside clinic hours
  - antivirus alert routing
  - a TLS scan of external services

### What each test could show
The new policies (P06) were drafts during fieldwork; they were approved on 2026-08-31. A control that a draft policy introduces has not operated yet, so it can only be reviewed for design. The `test_type` column in `assessment-results.csv` says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control existed before 2026 and was tested on samples or live systems | 75 |
| Design | The control is new (the 2026 risk analysis, or a draft policy); its design was reviewed. Operation is tested at the 2027-02 follow-up | 9 |
| Not implemented | Nothing existed to test | 80 |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-AC-2 and so on), with the population each sample was drawn from (for example, the 5 sampled terminations come from the 7 in EV-003 and EV-004).

## 3. Rules of engagement
- No testing that could disrupt patient care. Medical device tests happened after hours, with the Clinic A Manager present.
- No ePHI was copied off-site. Screenshots were redacted.
- The assessor stopped and notified the IT Manager on finding any critical exposure. None was found.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 57 |
| Other than satisfied | 107 |

**Fully other than satisfied:** CP-2, CP-4, RA-5, AU-6, SC-28, SC-8, AC-6, IR-6. No plan, process, or technology existed for these.
**Largely satisfied:** IA-2(1) (hardware-key MFA for administrators), PE-3 at Clinic A, SI-3 detection and quarantine, RA-3 (now that the 2026 analysis exists).

**New finding:** default manufacturer admin passwords on 4 networked vital-sign monitors (IA-05e.). This was not known before testing. It was added to the risk register as R-031 and to POAM-012. The passwords are scheduled to be changed by 2026-09-30.

All 21 controls with weaknesses have POA&M items in `poam.csv`. The High items are POAM-002 to POAM-005.

## 5. Deliverables
`assessment-results.csv` (164 rows), `poam.csv` (21 items), this plan and summary. The results were accepted by the Practice Administrator on 2026-08-31.
