# Security Assessment Plan and Summary: Cris Santos Company | Commercial Facilities | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial office and retail property owner-operator) |
| System assessed | Building Automation and Access Control System (BAACS), per the SSP (P02) |
| Tier / Vertical | Small / Commercial Facilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content); OT test limits from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Contracted independent assessor with OT experience. Not involved in operating or designing the controls. Escorted by the IT Manager; the Director of Engineering and the BAS integrator attended all OT tests |
| Assessment window | 2026-08-03 to 2026-08-07 (Property B walkthrough and OT tests 2026-08-05, after retail hours) |
| Also supports | CISA CPG 2.0 goal 2.C (independent validation of controls, voluntary) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 167 determination statements.** Controls were chosen because they support the three High risks in P01, cover the CPG 2.0 goals with High or Moderate gaps in P03, or underpin recovery and incident response.

| Control | Why selected | Statements | Depth | Coverage |
|---|---|---|---|---|
| AC-17, MA-4, IA-2(1) | Integrator remote access; P01 R-001 (High); P03 G-005, G-016 (CPG 1.E, 3.F) | 13 | Focused | Comprehensive (every remote path) |
| SC-7, AC-4 | OT segmentation; R-003 (High); G-019 (CPG 3.I) | 7 | Focused | Focused (all three properties) |
| CP-9, CP-4, CP-2 | BAS recovery; R-002 (High), R-021; G-025, G-034 (CPG 3.O, 6.A) | 35 | Focused | Focused |
| AC-2, AC-6, IA-2, IA-5 | Shared, default, and stale credentials; R-005 to R-008; G-011 to G-014, G-018 (CPG 3.A-3.D, 3.H) | 39 | Focused | Focused |
| CM-8, CM-3 | OT inventory and change control; R-031, R-034; G-006, G-024 | 16 | Basic | Focused (Property B device count) |
| SI-2, RA-5 | Unsupported BAS server and OT vulnerabilities; R-009; G-007 | 19 | Focused | Basic |
| AU-6 | No log review; R-020; G-027 (CPG 3.Q) | 3 | Basic | Basic |
| IR-4, IR-6 | Incident handling and reporting; R-021, R-028; G-003, G-033 | 15 | Focused | Basic |
| SA-9 | Vendor security; R-015, R-016; G-004 | 6 | Focused | Focused (7 contracts) |
| AT-2 | Awareness; R-010; G-020 | 10 | Basic | Focused (10 staff interviews) |
| MP-6 | Disposal of card data on paper and NVR drives; R-013 | 4 | Basic | Basic |

## 2. Methods and objects
- **Examine:** identity provider, access control platform, and BAS user exports; firewall rule exports for all three properties; backup job reports and vault settings; the remote-support tool console; integrator, MSP, guard, visitor management, and parking contracts; the MSP external scan reports of 2026-07-16 and 2026-07-20; training roster; the BIA and draft runbook; the booking binder at the Property A events desk.
- **Interview:** COO, IT Manager, Director of Engineering, 2 chief engineers, Security Manager, 2 security console operators, Controller, HR Manager, the MSP lead technician, the BAS integrator's service lead, and 10 randomly selected staff.
- **Test:**
  - sign-in tests, including an administrator sign-in with a hardware key and an attempt to reach the BAS without MFA
  - reachability tests from a corporate laptop to BAS, door controller, and NVR addresses at Properties A and B
  - default-credential test on BAS field controllers and NVRs at Property B, read-only login attempts only, with the integrator present
  - a device count at Property B compared with the integrator's lists
  - a review of 90 days of remote-support tool session history

## 3. Rules of engagement
- **No active scanning of OT devices.** Following SP 800-82 Rev. 3, the assessor did not run vulnerability scans against field controllers or door controllers. Default-credential checks used a single read-only login per device, one device at a time.
- **No changes to building systems.** No setpoint, schedule, door mode, or program was changed. The chief engineer could stop any test at any time.
- **Timing.** OT tests ran after retail hours at Property B, with the security console informed in advance.
- **Life-safety systems were out of bounds.** No test touched fire alarm, elevator, or emergency voice systems.
- **Data handling.** No personal data left company systems. Screenshots of badge and visitor records were redacted.
- **Critical findings.** The assessor stopped and told the IT Manager and Director of Engineering at once about any critical exposure. The default passwords were reported on 2026-08-05, and the Director of Engineering started changing them the next day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 41 |
| Other than satisfied | 126 |
| **Total** | **167** |

**Fully other than satisfied (10 controls):** AC-17, MA-4, IA-2(1), AC-4, AC-6, IA-2, CP-4, AU-6, IR-6, SA-9. No plan, process, or technical control existed for these, or the one control that exists (MFA) stops at the edge of the BAS.

**Largely or partly satisfied:**
- AC-2 (16 of 26): corporate account creation and approval work; removal, reviews, and shared accounts do not.
- RA-5 (5 of 9) and SC-7 (3 of 6): the external boundary is controlled and the July scan was acted on; internal and OT boundaries are not.
- IA-5 (4 of 10): the identity provider's password rules are sound; OT passwords are not.

**New finding:** manufacturer default passwords on 12 BACnet field controllers at Property B and on 2 NVRs (IA-05e.). This was not known before testing. It was added to the risk register (R-007, updated 2026-08-07) and to POAM-009, with defaults to be changed by 2026-09-30.

**Other findings not known before:** 31 of 144 field controllers counted at Property B were missing from the integrator's list (CM-8), and 2 failed NVR drives had been returned to the integrator without wiping (MP-6).

All 22 controls have at least one weakness, and each has a POA&M item in `poam.csv`: 7 High (POAM-001 to POAM-007) and 15 Moderate (POAM-008 to POAM-022). 15 items are in progress and 7 are open.

## 5. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and rules of engagement agreed with the COO and Director of Engineering |
| 2026-08-03 to 2026-08-07 | Fieldwork |
| 2026-08-14 | Draft results to control owners for factual review |
| 2026-08-31 | Results and POA&M accepted by the COO |

Deliverables: `assessment-results.csv` (167 rows), `poam.csv` (22 items), and this plan and summary. The next assessment is due by 2027-08-31 (POL-01 4.9).
