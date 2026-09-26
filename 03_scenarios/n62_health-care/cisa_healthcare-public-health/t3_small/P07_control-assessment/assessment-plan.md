# Security Assessment Plan and Summary: Cris Santos Company | Healthcare and Public Health | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural critical access hospital) |
| System assessed | Hospital Clinical Information System (HCIS), per the SSP (P02) |
| Tier / Vertical | Small / Healthcare and Public Health |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor with health care experience. Not involved in operating or designing the controls. Escorted by the IT Manager; clinical areas with the Director of Nursing's approval |
| Assessment window | 2026-08-03 to 2026-08-07 (after-hours device and network tests 2026-08-05) |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 186 determination statements.** Controls were chosen because they address the Very High and High risks in P01 (vendor access, backups, monitoring, segmentation, device patching), the Required HIPAA implementation specifications with gaps in P03, or the contingency elements that the CMS emergency preparedness condition depends on (485.625(b)(5)).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-17, SI-4, SC-7 | Initial access and spread in a ransomware attack; P01 R-001 (Very High), R-002 | Focused | Focused |
| CP-2, CP-4, CP-9, CP-10 | Contingency gaps (164.308(a)(7)); P01 R-003, R-004; 485.625(b)(5) | Focused | Focused |
| SI-2, CM-8 | Device and firmware patching, device inventory; P01 R-006, R-007 | Focused | Focused (all networked devices on the walkthrough) |
| AC-2, PS-4, IA-2, IA-2(1), IA-5 | Access and identity gaps (164.308(a)(3)-(4), 164.312(a), (d)); P01 R-009, R-011, R-026 | Focused | Focused |
| AT-2 | Training gaps for contracted and agency staff (164.308(a)(5)) | Basic | Focused |
| AU-6 | No log or access report review (164.308(a)(1)(ii)(D)); P01 R-010 | Basic | Basic |
| IR-4, IR-8 | No incident capability or plan (164.308(a)(6)) | Focused | Basic |
| RA-3, RA-5 | Risk analysis and vulnerability management (164.308(a)(1)(ii)(A)-(B)) | Focused | Basic |
| SA-9 | Missing BAAs and vendor oversight (164.308(b)); P01 R-018, R-019 | Focused | Focused |
| SC-28 | Unencrypted desktops and workstations on wheels (164.312(a)(2)(iv)) | Basic | Focused |

## 2. Methods and objects
- **Examine:** identity provider and EHR exports, VPN and firewall configurations, backup reports and vault settings, patch and firmware records, BAAs and contracts, the training roster, the 2023 and 2026 risk analyses, the 2025 emergency preparedness plan, the 2019 downtime binder, and walkthrough notes.
- **Interview:** CEO, IT Manager, IT Support Specialist, MSP lead technician, Director of Nursing, Facilities Manager, Quality and Compliance Manager, HR Manager, CFO, and 11 randomly selected staff and contracted clinicians (incident reporting and training awareness).
- **Test:**
  - idle-lock on 10 workstations, the tracking board, and the nursing station workstation
  - administrator sign-in with a hardware key
  - local administrator password comparison on 10 workstations
  - a test sign-in to the teleradiology VPN profile, with the vendor's approval
  - a restore of one file-server folder from backup
  - an internal reachability scan from a workstation to the device, OT, and phone addresses
  - default-credential checks on networked medical devices, after hours, with the manufacturer's field engineer present
  - an after-hours EDR alert routing test (21:40)

## 3. Rules of engagement
- No testing that could disrupt patient care. Device tests ran after hours on devices not in use, with the Director of Nursing's approval and the manufacturer's field engineer present. No infusion pump was tested while connected to a patient.
- No ePHI was copied off site. Screenshots were redacted.
- The assessor was to stop and notify the IT Manager on finding any critical exposure. **One was found:** the teleradiology support VPN account (shared, no MFA, enabled 24x7). The IT Manager restricted it to approved support windows on 2026-08-10 as an interim step (POAM-008).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 53 |
| Other than satisfied | 133 |
| **Total** | **186** |

**Fully other than satisfied (7 controls):** AC-17, AU-6, CP-4, CP-10, IR-8, RA-5, SC-28. No plan, process, or technology existed for these at fieldwork.
**Fully satisfied (1 control):** IA-2(1), hardware-key MFA for administrators.
**Largely satisfied:** RA-3 (the 2026 analysis exists), IA-5 password strength and issuance, CP-9 backup execution (a test restore worked; the problem is isolation, not whether backups run).

**New finding:** a manufacturer default administrator password on the patient monitor central station (IA-05e.). It was not known before testing. It was added to the risk register as R-026 and to POAM-012, and the manufacturer's field engineer is scheduled to change it by 2026-09-30.

**Notable test results:**
- From an ordinary workstation, the assessor reached the CT workstation, the infusion pump drug-library server, OT controllers, and the phone system (SC-07a.[04]). That is the path a ransomware operator would use.
- The 21:40 test alert was not seen until 08:15 the next morning (SI-04d.[01]).
- 11 accounts of former agency and contracted staff were enabled at fieldwork (AC-02f.[04]); they were disabled on 2026-08-14.

## 5. POA&M
All 21 controls with weaknesses have POA&M items in `poam.csv` (21 items): 1 Very High, 6 High, 13 Moderate, 1 Low; 11 in progress and 10 open. The Very High item is POAM-008 (vendor remote access). The High items are POAM-002 to POAM-006 and POAM-017.

Resources: the P01 funded list ($93,000) covers POAM-003, POAM-005, POAM-006, and POAM-009. The other costed items (scanning $5,000 per year, badge readers $6,000, legal review $4,000, downtime kits $1,500, forensic retainer $5,000) come from the IT operating budget.

## 6. Deliverables
`assessment-results.csv` (186 rows), `poam.csv` (21 items), and this plan and summary. The CEO accepted the results on 2026-08-31.
