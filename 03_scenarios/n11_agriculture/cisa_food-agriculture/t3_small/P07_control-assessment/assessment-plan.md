# Security Assessment Plan and Summary: Cris Santos Company | Food and Agriculture | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (meat processing plant with a smoked seafood room) |
| System assessed | Plant Production and Cold-Chain Monitoring System (PPCM), per the SSP (P02) |
| Tier / Vertical | Small / Food and Agriculture |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content), with OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Contracted independent assessor with OT experience. Not involved in designing or operating the controls. Escorted by the IT Manager and, on the floor, the Controls Engineer |
| Assessment window | 2026-08-10 to 2026-08-15 (OT testing in the sanitation window on 2026-08-14 and 2026-08-15) |
| Also supports | Food defense verification under 21 CFR 121.150(a)(3)(ii) for the cyber-physical mitigation strategies, and the integrity of electronic CCP records under 9 CFR 417.5(d) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 182 determination statements.** Controls were chosen because they support the High and Very High risks in P01, the High gaps in P03 (food defense measures and electronic record integrity), or the OT benchmark rows most tied to those gaps.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| SC-7, AC-17 | Segmentation and OT remote access; R-001 (Very High), R-002, R-006 | Focused | Focused |
| AC-2, AC-6, IA-2, IA-5 | Shared OT accounts; R-003, R-019; 121.305(f); 9 CFR 417.5(b) | Focused | Focused |
| CM-3, SI-7 | Formulation and setpoint change control; R-003, R-025; 121.135(a), 121.157(b)(1) | Focused | Focused |
| AU-6, AU-9 | Record integrity and log review; 9 CFR 417.5(d); 21 CFR 123.9(f) | Focused | Basic |
| CM-8 | OT inventory; CSF ID.AM-01 | Basic | Focused |
| CP-2, CP-4, CP-9 | OT recovery; R-007; P05 key findings | Focused | Focused |
| IR-4, IR-6 | Incident handling and reporting, including food safety decisions; 9 CFR 417.3(b), 418.2 | Focused | Basic |
| SI-3, SI-4 | OT malware protection and monitoring; R-001, R-013, R-014 | Focused | Focused |
| AT-2 | Floor-level awareness; 121.4(b)(2) | Basic | Focused |
| PE-3 | Physical mitigation strategies in the food defense plan | Basic | Focused |
| RA-3 | Risk assessment feeding the food defense reanalysis | Basic | Basic |
| SA-9 | Vendors with OT remote access; cold-chain SaaS | Focused | Basic |

## 2. Methods and objects
- **Examine:** firewall rules, VPN and modem configuration, identity provider export, HMI and recipe-system account lists, historian and records application configuration, backup job reports, change history, maintenance work orders, vendor contracts, training rosters, the 2023 food defense plan, and the P01 risk register.
- **Interview:** General Manager, FSQA Manager, IT Manager, Controls Engineer, Maintenance and Refrigeration Manager, Operations Manager, Sanitation Supervisor, and 8 randomly selected production and sanitation staff (reporting awareness).
- **Test:**
  - HMI sign-in on 6 HMIs and the recipe system
  - comparison of 15 sampled formulations in the recipe system with the signed formulation master
  - edit test on a sample CCP record in the records application's test environment
  - network reachability scan from a corporate host to the control network (sanitation window, read-only, rate-limited)
  - default-credential test on the refrigeration controller and 6 HMIs (sanitation window, with vendor approval and the refrigeration contractor present)
  - remote access test to the integrator VPN from an external network (with approval)
  - malware detection test (EICAR) on 2 office endpoints only

## 3. Rules of engagement
- **No active testing of live process controls.** OT tests ran only during the sanitation window with lines stopped, product cleared from affected areas, and the Controls Engineer present. No PLC logic was downloaded or changed. Scans were read-only and rate-limited, following SP 800-82 Rev. 3 cautions on active scanning in OT.
- **Refrigeration stays on.** The refrigeration controller was tested for sign-in only, with the refrigeration contractor present and the engine room staffed. No setpoint was changed.
- **Stop condition.** The assessor was to stop and notify the IT Manager and the Maintenance and Refrigeration Manager on finding any exposure that could affect product safety or ammonia containment. **This happened once** (section 4).
- No formulations, food defense plan content, or employee data left the site. Screenshots of formulations were redacted.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 52 |
| Other than satisfied | 130 |

**Fully other than satisfied (12 controls):** AC-6, AC-17, IA-2, AU-6, AU-9, CM-3, CM-8, CP-2, CP-4, IR-4, SI-4, and SI-7. For these, no documented process or technical mechanism existed in OT at the time of fieldwork.

**Fully or largely satisfied:**
- RA-3 (fully satisfied: the 2026 risk assessment exists and covers OT and food defense scenarios)
- PE-3 (one exception: engine room keys not changed after a departure)
- IR-6 (incident information goes to FSIS through the recall procedure; the gap is floor-level reporting)
- IA-5 for identity provider accounts
- CP-9 for the routine backups themselves

**New finding (stop condition triggered on 2026-08-14):** the refrigeration controller's web interface accepted the manufacturer default administrator password (IA-05e.), and the controller is reachable from the corporate network. The assessor stopped and notified the IT Manager and the Maintenance and Refrigeration Manager. The contractor was asked to change the password; it is scheduled for change by 2026-09-30 (POAM-005). The finding was added to the risk register as R-032.

**What the test results mean for food defense.** The formulation comparison matched 15 of 15 samples to the signed master. That is good news about today, but it says nothing about tomorrow: nothing would have detected a change (SI-7), and nothing ties a change to a person (IA-2). The cyber-physical mitigation strategies the food defense reanalysis will depend on do not exist yet, so there is nothing for 121.150 verification to verify.

All 21 controls with weaknesses have POA&M items in `poam.csv`: 1 Very High (POAM-001), 9 High, 10 Moderate, and 1 Low. RA-3 has none.

## 5. Deliverables
`assessment-results.csv` (182 rows), `poam.csv` (21 items), and this plan and summary. The results were accepted by the General Manager on 2026-09-04.
