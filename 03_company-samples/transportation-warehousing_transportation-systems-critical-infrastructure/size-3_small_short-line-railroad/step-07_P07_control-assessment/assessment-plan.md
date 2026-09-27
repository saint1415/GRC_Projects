# Security Assessment Plan and Summary: Cris Santos Company | Transportation Systems | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (Class III short line freight railroad) |
| System assessed | Train Dispatch and PTC Operations Platform (TDPO), per the SSP (P02) |
| Tier / Vertical | Small / Transportation Systems |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor with OT experience. Not involved in operating or designing the controls. Escorted by the IT Manager; OT work escorted by the Signal and Communications Supervisor |
| Assessment window | 2026-08-03 to 2026-08-07 (dispatch center and Central Yard walkthrough 2026-08-05; tower site and detector visit 2026-08-06) |
| Benchmark | NIST CSF 2.0 with SP 800-82 Rev. 3 (C-TRANSPORTATION-BM); TSA duties under 49 CFR 1570.203 (C-TRANSPORTATION-S01) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 184 determination statements.** Controls were chosen because they support the Very High and High risks in P01, cover the High gaps in P03, or support the one binding cyber duty (TSA reporting under 1570.203).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-17, MA-4, SC-7 | Vendor remote access and the flat network: P01 R-001 (Very High), R-002; P03 G-057, G-060 | Focused | Focused |
| AC-2, AC-6, IA-2, IA-2(1), IA-5 | Access gaps: R-004 (High), R-010, R-011, R-012, R-014; P03 G-044 to G-046 | Focused | Focused |
| CP-2, CP-4, CP-9 | Recovery and manual dispatch: R-003 and R-005 (High); P03 G-043, G-052, G-066 | Focused | Focused |
| IR-4, IR-6 | No incident capability; TSA reporting: R-006; P03 G-007, G-008, G-063 | Focused | Basic |
| SI-2, SI-3, SI-4, AU-6, RA-5 | Patching, malware, monitoring: R-008, R-009, R-021; P03 G-054, G-055, G-059 | Focused | Focused |
| CM-8 | No OT inventory: P03 G-035 | Basic | Focused (one tower site sampled) |
| AT-2 | Training gap: R-025; P03 G-048 | Basic | Focused |
| SA-9 | Vendor terms: R-013, R-022; P03 G-033, G-034 | Focused | Basic |
| PE-3 | HQ, dispatch, tower sites: R-020 | Basic | Focused |

## 2. Methods and objects
- **Examine:** identity provider and CAD user exports, dispatch server local accounts, firewall and VPN configurations, the vendor VPN appliance configuration, backup job reports and vault settings, patch reports, the MSP asset report and 2021 network diagram, contracts and SOC 2 reports, the training roster, the TSOC report log, the 2025 mailbox compromise ticket, and the 2019 manual dispatch procedure.
- **Interview:** President and General Manager, Vice President of Operations, Chief Dispatcher and 2 dispatchers, Manager of Safety and Security, Signal and Communications Supervisor, IT Manager, MSP lead technician, the dispatch system vendor's support lead, and 8 randomly selected employees (incident reporting awareness).
- **Test:**
  - sign-in to the staff VPN and a dispatch server administrator account without a second factor
  - reachability from one office workstation to the dispatch VLAN (read-only port check)
  - console log-on check on all 6 dispatch consoles
  - default-credential test on the 3 wayside detector modems
  - antivirus response to a harmless test file on 3 endpoints
  - badge and key checks at HQ, the dispatch center, and one tower site

## 3. Rules of engagement
- **Safety first.** No test may touch the CAD application, the radio consoles, or wayside equipment while it is in service without the Chief Dispatcher's approval. Detector modem tests happened in a 2-hour window with no trains scheduled over the detectors and the Signal and Communications Supervisor present.
- **No active scanning of the dispatch VLAN** during this assessment. The reachability test was one read-only port check in a window agreed with the dispatch vendor.
- **No change to onboard PTC units or the PTC back office.** They were examined through documents and the vendor's SOC 2 report only.
- **SSI and data handling.** Screenshots were redacted. Network diagrams and findings about OT exposures are Restricted (POL-04). The results were not taken off site.
- **Stop rule.** The assessor stopped and notified the IT Manager on finding any critical exposure. One was found: the default modem credentials (below).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 49 |
| Other than satisfied | 135 |
| **Total** | **184** |

**Fully other than satisfied (11 controls):** AC-6, AC-17, AU-6, CP-2, CP-4, IA-2, IA-2(1), IR-4, IR-6, RA-5, SI-4. No plan, process, or technology existed for these.
**Largely satisfied:** PE-3 (badge access at HQ and dispatch; 9 of 12), SI-3 (signature antivirus detects and quarantines; 6 of 8), AC-2 (account creation and role assignment work; 16 of 26).

**Key observations:**
- The vendor VPN appliance terminates **inside** the dispatch VLAN and bypasses the firewall (SC-07c.). Together with the always-on shared vendor account (MA-4) and the unfiltered office LAN (SC-07a.[04]), this is the path in P01 R-001.
- 5 of the 8 employees interviewed did not know where to report a cyber event (IR-06a.).
- **New finding:** manufacturer default credentials worked on all 3 wayside detector modems (IA-05e.). This was not known before testing. The stop rule was invoked. It was added to the risk register as R-010 and to POAM-013. The credentials are scheduled to be changed by 2026-09-30.

All 22 controls have at least one weakness and a POA&M item in `poam.csv`: 11 High, 10 Moderate, and 1 Low. The High items are POAM-002 to POAM-012.

## 5. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and rules of engagement approved by the Vice President of Operations and IT Manager |
| 2026-08-03 to 2026-08-07 | Fieldwork |
| 2026-08-14 | Draft results to the IT Manager for factual review |
| 2026-08-31 | Results and POA&M accepted by the President and General Manager |

Deliverables: `assessment-results.csv` (184 rows), `poam.csv` (22 items), and this plan and summary.
