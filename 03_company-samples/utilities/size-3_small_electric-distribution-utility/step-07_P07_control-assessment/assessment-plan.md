# Security Assessment Plan and Summary: Cris Santos Company | Utilities | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (electric distribution utility, NERC-registered Distribution Provider) |
| System assessed | Distribution Operations Platform (DOP), per the SSP (P02), including the low impact BES Cyber Systems at Substation N and Substation E |
| Tier / Vertical | Small / Utilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent OT security assessor. Not involved in operating or designing the controls. Escorted by the SCADA/OT Administrator in the DCC and by a protection technician at substations |
| Assessment window | 2026-08-10 to 2026-08-14 (substation testing 2026-08-12) |
| Also supports | CIP-003-9 internal compliance review before the SERC self-report; voluntary SP 800-82 Rev. 3 benchmark for the SCADA outside CIP scope |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 154 determination statements.** Controls were chosen because they:
- support the four High risks in P01 (R-001, R-002, R-006, R-009), or
- carry a CIP-003-9 Attachment 1 requirement with a gap in P03 (Sections 2, 3.1, 4.2, 4.5, 5, 6).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, IA-2(1), IA-5 | Shared OT accounts, no OT MFA, relay passwords; R-008, R-009 | Focused | Focused |
| AC-17, MA-4 | Vendor remote access (CIP Att. 1 Sec. 6); R-001 (High) | Focused | Comprehensive (all vendor sessions for 30 days) |
| AC-4, SC-7, CM-6 | IT/OT boundary and substation access lists (CIP Att. 1 Sec. 3.1); R-002 (High) | Focused | Focused (both BES substations, IT/OT firewall) |
| SI-4, AU-6 | No OT monitoring (CIP Att. 1 Sec. 6.3); R-020 | Basic | Basic |
| CP-9, CP-4 | SCADA recovery; R-006 (High) | Focused | Focused |
| IR-3, IR-6 | Plan test and notifications (CIP Att. 1 Sec. 4.2, 4.5); R-022 | Focused | Basic |
| SI-3, MP-7 | Transient Cyber Assets and removable media (CIP Att. 1 Sec. 5); R-005 | Focused | Focused |
| PE-3 | Substation keys (CIP Att. 1 Sec. 2); R-013 | Basic | Focused (both BES substations and the DCC) |
| AT-2 | Awareness (CIP Att. 1 Sec. 1) and phishing; R-011 | Basic | Basic |
| SI-2, RA-5, CM-8 | Unsupported OS, no OT vulnerability process, incomplete inventory; R-007 | Basic | Focused |
| SA-9 | Vendor contracts and oversight; R-010, R-021 | Basic | Focused |

## 2. Methods and objects
- **Examine:**
  - account exports (OT domain, jump host, identity provider)
  - firewall and gateway configurations and backup job logs
  - jump host session logs, contracts, and SOC 2 reports
  - the low impact plan and its 2023 test report, and the EOP-004 Operating Plan
  - training records, the OT inventory, and walkthrough notes
- **Interview:** the CIP Senior Manager, the Manager of System Operations, the Manager of Engineering and Protection, the NERC Compliance Coordinator, the IT Manager, the SCADA/OT Administrator, 2 system operators, 2 protection technicians, and 4 randomly selected field staff (incident reporting and USB practices).
- **Test:**
  - HMI and jump host sign-in tests, including a jump host sign-in from the VPN pool
  - a traffic test from a corporate VLAN toward the historian
  - access list tests at the Substation N and E gateways from an OT network test laptop
  - a default-credential test on relays and gateways at both BES substations
  - an EICAR antivirus test on an engineering workstation
  - a permission test on the SCADA backup share

## 3. Rules of engagement
- Safety and reliability come first. **No test touched relay protection functions or sent any control command.**
- Substation tests were read-only, run on 2026-08-12 with the DCC informed and a protection technician present, and paused during a storm watch.
- Test traffic toward SCADA was limited to connection attempts with no payload, and was coordinated with the shift supervisor.
- No customer data was copied off-site. Screenshots were redacted.
- The assessor was to stop and notify the SCADA/OT Administrator and the NERC Compliance Coordinator on finding any exposure of a low impact BES Cyber System. **This happened once** (below).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 59 |
| Other than satisfied | 95 |

**Fully other than satisfied:** AC-4, AU-6, CP-4, IA-2(1), IR-3, RA-5, SI-4. No plan, process, or technology existed for these.
**Largely satisfied:** PE-3 at the DCC (badge control, visitor escort, door alarms), IA-5 basics (the default-credential test passed on all 8 relays and both gateways), SI-3 detection and quarantine on SCADA servers, AC-2 account creation from HR tickets.

**New finding:** the Substation E gateway access list permitted any routable traffic from the OT network to the relays (CM-06b.). It was left that way after the 2025 commissioning. The assessor stopped testing and notified the NERC Compliance Coordinator on 2026-08-12. Protection staff corrected the list on 2026-08-13, and the assessor retested it the same day.

The finding was:
- added to the risk register as R-031
- rated Partially met in P03 row G-020 (Attachment 1 Section 3.1)
- tracked as POAM-013
- included in the SERC self-report

All 22 controls with weaknesses have POA&M items in `poam.csv`. The High items are POAM-002 to POAM-008.

## 5. Deliverables
`assessment-results.csv` (154 rows), `poam.csv` (22 items), and this plan and summary. The results were accepted by the President and CEO and the CIP Senior Manager on 2026-09-04.
