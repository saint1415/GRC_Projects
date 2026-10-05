# Security Assessment Plan and Summary: Cris Santos Company | Water and Wastewater Systems | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (privately held community water system, 2,850 population served) |
| System assessed | Water Treatment SCADA System (WTSS), per the SSP (P02) |
| Tier / Vertical | Micro / Water and Wastewater Systems |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content), with OT considerations from NIST SP 800-82 Rev. 3 |
| Assessor and independence | Independent OT security consultant under a fixed-fee engagement. Did not take part in the risk or gap analysis (P01, P03), operates no control, and is independent of the SCADA integrator and the MSP. Escorted by the Chief Operator at the plant and remote sites; Office Manager for office evidence; MSP lead technician on call |
| Assessment window | 2026-08-10 to 2026-08-12 (site visit to the plant, Well 3, and the elevated tank on 2026-08-11) |
| Not a regulatory requirement | No federal rule requires a control assessment from a system serving 2,850 persons (P03). The company commissioned it for its own risk decisions and for the cyber insurer's renewal (P09) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 117 determination statements.** Controls were chosen because they are the controls an attacker would defeat in the P08 scenario (remote access to the HMI), because they support the 4 High risks in P01, or because they cover the 8 High gaps in P03. Each control also tests something a contractor does, or should do, for the company.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, IA-5 | Shared HMI login and remote desktop password; former operator knew the password (P01 R-002; P03 G-034) | Focused | Comprehensive (every WTSS account and credential) |
| AC-17, IA-2(1) | Always-on remote desktop tool with no MFA (P01 R-001, High; P03 G-035, G-036) | Focused | Comprehensive (every remote path) |
| SC-7, CM-7 | Flat network; exposed devices (P01 R-003, High; P03 G-040, G-043) | Focused | Focused |
| CP-9 | No company copy of the PLC program (P01 R-004, High; P03 G-039) | Focused | Focused |
| IR-8 | No cyber incident plan (P03 G-045, High) | Basic | Basic |
| CM-8, RA-5 | No inventory; no vulnerability identification (P03 G-029, G-031) | Focused | Comprehensive (all 3 sites) |
| SI-2 | HMI computer not updated since May 2024 (P01 R-005; P03 G-041) | Basic | Focused |
| SA-9 | No security terms with the integrator, MSP, or remote monitoring vendor (P01 R-014, R-016; P03 G-027) | Basic | Comprehensive (all 4 providers that reach the WTSS) |
| AT-2 | No training (P01 R-007; P03 G-038) | Basic | Comprehensive (all 7 staff interviewed) |

**Not selected, with reasons.** SC-24 (engineered safeguards) was observed during the site visit and is recorded as implemented in the SSP; it was not tested by forcing an overfeed. CP-2 and CP-4 are covered by the gap analysis and the first exercise due 2026-11-30.

## 2. Methods and objects
- **Examine:** HMI user list and security settings; remote desktop tool console, settings, and 90-day connection history; remote monitoring user list and audit log; the password spreadsheet and its sharing settings; firewall rule export; 2018 as-builts; HMI computer update history and installed software; MSP backup report and retention settings; the three contracts and the remote monitoring terms; the 2023 emergency plan and plant binder; training and orientation records.
- **Interview:** Owner and General Manager, Office Manager, Chief Operator, both Operators, Utility Field Technician, Customer Service and Billing Clerk, the MSP lead technician, and the integrator's technician (by phone on 2026-08-11).
- **Test:**
  - a connection to the remote desktop tool from an unregistered device with the shared password (Chief Operator present; no action taken on the HMI)
  - sign-in attempts without a second factor on the remote desktop tool, the remote monitoring service, and the firewall management login
  - a passive network trace from a switch mirror port to see which devices can reach the PLC and HMI computer
  - an external exposure check of the plant broadband address and the 2 modem addresses
  - a physical check of every device at the 3 sites against the 2018 as-built list

### MSP and vendor evidence requested
The MSP operates the office firewall, Wi-Fi, and backup, so evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Firewall rule export and firmware record | SC-7, CM-7, SI-2 | Yes, 2026-08-07 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-07 |
| Record of any restore test | CP-9 | No record exists (confirmed by the MSP) |
| Monthly patch and antivirus report (July 2026) | SI-2 | Yes, 2026-08-07 (office computers only; the HMI computer is excluded by contract) |
| Technician list and MFA on the MSP's remote management platform | SA-9 | Not received by fieldwork end; follow-up in POAM-011 |
| Remote monitoring vendor's SOC 2 report (requested from the vendor) | SA-9 | Received 2026-08-14, after fieldwork; reviewed in P09 |
| Integrator's copy date of the PLC program (requested from the integrator) | CP-9 | The integrator could not confirm it |

## 3. Rules of engagement
- **No active scanning or testing inside the plant network.** OT devices can fail when scanned, so the assessor used only configuration review, a passive trace, and physical inspection, as SP 800-82 Rev. 3 advises. No change to any setpoint, PLC, HMI setting, or alarm.
- A licensed operator was present for every action in the control room and at the remote sites.
- The external check covered only the company's broadband address and the 2 modem addresses on the company's carrier plan, with the Owner's written permission.
- The assessor would stop and tell the Chief Operator and the Owner at once about any critical exposure. **One was found** (section 4) and fixed the next day.
- No customer data left the office. Screenshots of credentials were redacted before they went into the evidence folder.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 11 |
| Other than satisfied | 106 |
| **Total** | **117** |

Of the 106 statements other than satisfied, 28 are rated High, 44 Moderate, and 34 Low.

**Fully other than satisfied (6 controls):** AC-17, IA-2(1), IR-8, SI-2, RA-5, AT-2. No documented process or working technology existed for these at fieldwork. POL-02, POL-03, POL-04, and the P08 runbook were approved on 2026-08-31, after fieldwork, so they could not be credited.

**What works:** process data is copied to the remote monitoring service with 2 years of history (CP-09a.); the office firewall blocks unsolicited inbound traffic (SC-07a.[02]); the gateway cannot write to the PLC (CM-07b.[05]); account managers are known and the departed operator's remote monitoring account was removed promptly (AC-02b., AC-02h.02). The engineered safeguards observed on site (stroke limit, analyzer relays to the alarm dialer, hand-off-auto switches) are outside the selected controls but explain why no WTSS risk in P01 is Very High.

**New findings from testing:**
1. **Critical exposure.** The external check on 2026-08-11 found the elevated tank modem's web administration reachable from the internet with the default password (IA-05e., CM-07b.[02], SC-07b.). The modem had been replaced after a 2022 lightning strike and never hardened. The integrator turned off web administration and changed the password on 2026-08-12. Added to the risk register as R-023, and to POAM-003, POAM-006, and POAM-007.
2. The test connection from an unregistered device reached the HMI desktop with the shared password alone (AC-17b.). POAM-002.
3. The passive trace showed office computers and a visitor Wi-Fi device able to reach the PLC programming port (SC-07a.[04]). POAM-006.

All 13 controls have at least one weakness and a POA&M item in `poam.csv` (13 items: 8 High, 5 Moderate). The High items are POAM-001 to POAM-006, POAM-009, and POAM-012: remote access, credentials, the PLC backup, the flat network, vulnerability identification, and the missing incident plan, the same theme as the High risks in P01.

## 5. Deliverables
`assessment-results.csv` (117 rows), `poam.csv` (13 items), and this plan and summary. The Owner and General Manager accepted the results on 2026-08-31. The Office Manager tracks the POA&M at the monthly 30-minute meeting with the Owner. The next independent assessment is due by August 2028 (POL-02 A.6), with a self-review in August 2027.
