# Security Assessment Plan and Summary: Cris Santos Company | Arts, Entertainment, and Recreation | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing) |
| System assessed | Ticketing and Venue Operations Platform (TVOP), per the SSP (P02) |
| Tier / Vertical | Small / Arts, Entertainment, and Recreation |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in operating or designing the controls, and not the company's future ASV or penetration tester. Escorted by the IT Manager |
| Assessment window | 2026-08-03 to 2026-08-07 (on-site testing 2026-08-04 and 2026-08-05; box office observed at a Lounge show on 2026-08-05) |
| Also supports | Evidence for the 2026 SAQs (PCI DSS v4.0.1, N71-R04) and FTC reasonable security (N71-R05) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **21 controls, 140 determination statements.** Controls were chosen because they support the five High risks in P01, cover the High gaps in P03, or underpin the P08 incident scenario (ticketing account takeover and checkout skimming).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-6, IA-2, IA-2(1), IA-5 | Ticketing account gaps (P03 8.2, 8.4, 8.6); R-001 (High) | Focused | Focused (all 34 venue users) |
| AC-17 | Integrator remote access (P03 8.4); R-022 | Basic | Focused |
| CM-7, SI-7, CM-8, CM-3 | Checkout scripts and change control (P03 6.4.3, 11.6.1, 6.5, 9.5); R-002 (High) | Focused | Focused |
| AU-6, AU-11 | No log review or retention (P03 10.4, 10.5) | Basic | Basic |
| RA-5 | No scanning (P03 11.3) | Basic | Basic |
| SC-7, SI-3 | Box office PCs on a shared segment (P03 1.3, 5.2-5.3); R-003, R-009 | Focused | Focused |
| MP-6 | Paper card data (P03 3.3, 9.4); R-004 | Basic | Focused |
| CP-9 | Backups (P04 finding 3); R-010 | Focused | Basic |
| IR-4, IR-6 | No incident capability (P03 12.10); R-026 | Focused | Basic |
| AT-2 | No training (P03 12.6); R-021 (High) | Basic | Basic |
| SA-9 | Service provider oversight (P03 12.8); R-033 | Focused | Focused |

## 2. Methods and objects
- **Examine:** ticketing user, role, and security settings exports; identity provider and cloud IAM exports; firewall export; backup reports; anti-malware console; vendor contracts, AOCs, and the SOC 2 report; the phone-order binder; checkout page captures of 2026-07-21 and 2026-08-05.
- **Interview:** General Manager, Controller, IT Manager, Director of Ticketing, Marketing Director, Food and Beverage Manager, the integrator's lead technician, and 8 staff (box office, bar leads, finance) on incident reporting and card handling.
- **Test:**
  - admin sign-in to the ticketing platform with a test account (MFA prompt or not)
  - reconciliation of ticketing accounts against the HR termination list
  - traffic tests from a production-segment laptop and a box office PC
  - default-credential test on the CCTV recorder and the door access controller, with the integrator present
  - an anti-malware test file on 2 box office PCs
  - log retention on 3 box office PCs
  - a second capture of the checkout page to compare scripts

## 3. Rules of engagement
- No testing during an on-sale or during doors. Network tests ran on a dark day (2026-08-04).
- No real card data was entered, copied, or photographed. The phone-order slips were photographed with card numbers covered, then locked in the Controller's safe pending shredding.
- The CCTV and door tests were run with the integrator present and the Operations Director's approval.
- The assessor stopped and notified the IT Manager on finding a critical exposure. **One was found:** default passwords on the CCTV recorder and door controller (see section 4).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 27 |
| Other than satisfied | 113 |

**Fully other than satisfied (no statement satisfied):** AC-6, AT-2, AU-6, AU-11, CM-3, IA-2(1), IR-4, IR-6, RA-5, SI-7. For these no plan, process, or technology existed.
**Largely satisfied:** SI-3 (6 of 8: detection and quarantine work; alerting does not), SC-7 at the external boundary, CP-9 backup creation (but not isolation).

**Findings that change the picture:**
- **Checkout content changed during the assessment.** A tenth script appeared on the checkout page between the captures of 2026-07-21 and 2026-08-05 (added by the agency for a sponsor campaign). Nobody at the company knew. This confirms that SI-7 and CM-3 are the controls that would have caught the P08 scenario, and neither exists. The Marketing Director removed the new script on 2026-08-06. Removal of the other 9 is scheduled with the agency by 2026-09-30 because two sponsor campaigns report through them (POAM-007).
- **New finding:** integrator default admin passwords on the CCTV recorder and door access controller (IA-05e.), both reachable from the corporate segment. This was not known before testing. It was added to the risk register as R-019 and to POAM-005, and the passwords are scheduled to be changed by 2026-09-30.
- **MFA test:** the ticketing admin test account signed in with a password alone (IA-02(01)), confirming P01 R-001.

All 21 controls have weaknesses and have POA&M items in `poam.csv`: 8 High (POAM-001, 003, 007, 008, 011, 013, 014, 016) and 13 Moderate.

## 5. Deliverables
`assessment-results.csv` (140 rows), `poam.csv` (21 items), this plan and summary. The results were accepted by the General Manager on 2026-08-31.
