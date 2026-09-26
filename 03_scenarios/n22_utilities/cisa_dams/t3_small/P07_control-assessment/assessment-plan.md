# Security Assessment Plan and Summary: Cris Santos Company | Dams | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensee of the fictional Cypress Fork Hydroelectric Project) |
| System assessed | Plant Control and Dam Monitoring System (PCDMS), per the SSP (P02) |
| Tier / Vertical | Small / Dams |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content), with OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Contracted independent assessor with OT experience. Not involved in designing or operating the controls. Escorted by the Controls Engineer; all OT tests approved by the Plant Manager |
| Assessment window | 2026-08-03 to 2026-08-07 (site walkthrough 2026-08-05) |
| Also supports | FERC Security Program Rev. 3A Form 3: this assessment provides the evidence behind the answers to Questions 5-33 and the plan and schedule for negative answers (9.1.1.3) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 176 determination statements.** Controls were chosen because they support the five High risks in P01, answer the Form 3 questions with the largest gaps in P03, or test FERC duties that were certified but not evidenced.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, IA-2, IA-2(1), IA-5 | Shared operator account, no MFA, default passwords (P03 G-054, G-055; Form 3 Q21); R-001, R-014 | Focused | Focused (all HMIs; 4 gate panels; 2 modems) |
| AC-17, MA-4 | Remote operation and vendor access (Form 3 Q12); R-001, R-003, R-004 | Focused | Comprehensive (every remote path) |
| SC-7 | IT/OT segregation (Form 3 Q11, Q22); R-005 | Focused | Comprehensive (all firewall rules) |
| AU-6, SI-4 | No OT logging or monitoring (Form 3 Q14); R-007 | Basic | Focused |
| CM-3, CM-8 | Change control and inventory (Section 9.2; Table 9.3a system lifecycle) | Focused | Focused |
| CP-9, CP-4 | OT backup and recovery (Form 3 Q16); R-009 | Focused | Comprehensive (all PLCs and HMIs) |
| RA-5, SI-2 | Vulnerability assessment and patching (Table 9.3b; Form 3 Q15, Q18i); R-008 | Basic | Focused |
| MP-7 | Removable media (Form 3 Q17); R-010 | Basic | Focused |
| IR-4, IR-6 | OT incident handling and 18 CFR 12.10 reporting; R-016 | Focused | Basic |
| AT-3 | Role-based OT training (Table 9.3a training) | Basic | Focused |
| PE-3 | Physical protection of cyber assets (Table 9.3a general; Form 1 Q6) | Basic | Comprehensive (all OT locations) |
| AC-3 | CEII access (Form 1 Q22); R-017 | Basic | Focused |
| PL-2 | Security Plan currency (Rev. 3A 7.5, 8.0); R-015 | Focused | Focused |

**Tailoring of statements.** Privacy-plan statements in PL-2 and privacy-training statements in AT-3 were not assessed: the PCDMS processes no personal information. The privacy risk assessment statement (PL-02a.08[01]) was excluded for the same reason.

## 2. Methods and objects
- **Examine:** HMI, SCADA, and OT VPN user lists; OT firewall rule export (2026-07-20); SCADA event journal (July 2026); backup NAS listing; vendor contracts and connection list; the 2022 Security Plan and 2017 Security Assessment; the ODSP; training rosters; key register and card access logs; file share permissions.
- **Interview:** Plant Manager, Controls Engineer, 2 I&C technicians, all 3 Operations Supervisors, 8 randomly selected operators and security officers (incident reporting), Chief Dam Safety Engineer, Compliance and Security Coordinator, IT Manager, and the SCADA integrator and governor vendor by phone.
- **Test** (all OT tests approved by the Plant Manager, with an operator at the local panels):
  - sign-in tests on 2 HMIs and the OT VPN
  - default-credential test on the 4 gate panel web interfaces (gates placed in local lockout first) and the 2 gauge modems
  - passive network discovery on the control LAN (no active scanning of PLCs, governors, or exciters)
  - a test laptop connected to a spare control LAN switch port for 2 hours to see whether anything detected it
  - USB mount test on 2 HMIs and the engineering workstation
  - reachability test from the corporate network into the control LAN
  - CEII access test with a seasonal staff account

## 3. Rules of engagement
- **Safety first.** No active scanning or fuzzing of PLCs, governors, exciters, or the gate controller. No test while a gate was moving or during a flood watch. Gates were in local lockout during panel tests, with an operator present.
- **Stop rule.** The assessor had to stop and tell the Plant Manager at once on finding anything that could allow uncontrolled gate operation. One finding triggered this rule: the default passwords on 2 gate panel web interfaces (2026-08-05). The Plant Manager ordered the passwords changed; they are due by 2026-09-30 and the web interfaces are disabled when not in use until then.
- No CEII or configuration data left the site. Screenshots were redacted, and the working papers are marked "Privileged - Security Sensitive Material".

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 46 |
| Other than satisfied | 130 |
| **Total** | **176** |

**Fully other than satisfied (every statement):** AC-3, AC-17, IA-2, IA-2(1), MA-4, AU-6, SI-4, CM-8, CP-4, RA-5, SI-2, MP-7, IR-6, AT-3. For these there was no plan, process, or technology for the OT environment.
**Largely satisfied:** PE-3 (10 of 12: physical protection is strong), PL-2 (17 of 22: the new PCDMS SSP covers most plan content; the FERC Security Plan is the weak part), IR-4 preparation and containment (operators isolated the network and ran gates locally during a 2025 SCADA server failure), CM-3 review and oversight in the weekly operations meeting.

**New findings not known before testing:**
- Manufacturer default passwords on 2 of 4 gate panel web interfaces and both upstream gauge modems (IA-05e.). Added to the risk register as R-011 and R-012 on 2026-08-07 and tracked in POAM-014.
- A laptop plugged into the control LAN for 2 hours was not detected (SI-4).
- 11 of 38 control network devices found by passive discovery are missing from the 2018 drawings (CM-8).
- 3 unlabeled USB drives in a control room drawer (MP-07b.).

All 22 controls have weaknesses and are tracked in `poam.csv` (21 items; the IA-2(1) findings share POAM-001 with AC-17). The High items are POAM-001 to POAM-007, POAM-009 to POAM-011, POAM-014, POAM-015, POAM-019, and POAM-020. POA&M costs are within the $265,000 budget approved in P01, except about $24,600 of training, kiosk, retainer, outside review, and carrier costs, which come from the 2027 operating budget.

**Use for FERC.** Filtered to the Section 9 rows, `poam.csv` is the plan and schedule that Section 9.1.1.3 requires for every negative Form 3 answer. It goes to the Regional Engineer with the corrected statement by 2026-09-30.

## 5. Deliverables
`assessment-results.csv` (176 rows), `poam.csv` (21 items), and this plan and summary. The Vice President of Operations accepted the results on 2026-08-31.
