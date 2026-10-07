# Security Assessment Plan and Results Memo: Cris Santos Company | Government Services and Facilities | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (facilities support contractor operating government buildings) |
| System assessed | Building Systems Support Environment (BSSE), per the system profile (P02), including the owner's access paths into the city's building systems |
| Tier / Vertical | Sole Proprietorship / Government Services and Facilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner (self-assessment), assisted by the on-call IT technician under NDA (signed 2026-08-03). **Independence is limited**: the owner designed, operates, and assessed these controls. The technician helped run the tests and read the settings but also supports the laptop. The city facilities manager witnessed the library controller test |
| Assessment window | 2026-08-18 to 2026-08-20 (library controller comparison on the evening of 2026-08-19) |
| Also satisfies | CA-2 of the Moderate baseline required by the city security exhibit |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 37 determination statements.** Controls were chosen because they carry a High risk in P01 (R-001, R-002, R-006 via backups) or a High or Moderate gap in P03, or because a contract clause depends on them (FAR supply chain, CUI, incident notice).

| Control | Why selected | Depth / coverage |
|---|---|---|
| AC-17 | Remote-desktop path into the city BAS (R-001; G-012) | Focused / every remote path into city systems |
| IA-2(1) | MFA on privileged accounts, including city systems (R-001, R-002; city exhibit MFA term) | Basic / all 6 privileged accounts |
| IA-5 | Shared BAS administrator password (R-002; G-065) | Focused / all authenticators |
| AC-6 | Daily administrator use of the laptop (R-004; FAR 52.204-21(b)(1)(ii)) | Basic / laptop |
| CP-9 | Controller program backups; BIA RPO (R-005; G-059) | Focused / library building (11 controllers) |
| AU-6 | Log review never done (R-001, R-002; G-027) | Basic / 3 log sources |
| IR-6 | Contract and statutory notice clocks (R-010; GSA-01) | Basic |
| MP-4 | CUI storage (R-008; CUI-01) | Basic / paper and digital CUI |
| SC-28 | Encryption of the devices that hold customer data (R-004, R-009) | Basic / laptop and phone |
| SR-3 | Parts for the federal building (R-011; FAR-18) | Focused / 14 purchases in 12 months |

## 2. Methods and objects
- **Examine:** remote-desktop agent and account settings, laptop accounts, phone notes and password storage, router administrator page, sync settings and the engineering folder, suite folder structure, van cabinet and home office, the two contracts, purchase records, the incident log.
- **Test:** sign-ins from a new browser to each service and city system (2026-08-18); an unattended connection attempt through the agent (2026-08-18, before it was turned off); an installer run under the daily account (2026-08-18); encryption status on both devices (2026-08-18); a comparison of the laptop's copies of the 11 library controller programs with the running programs, uploaded read-only from each controller (2026-08-19, evening, city facilities manager present, no program was written to any controller); a SAM.gov "FASCSA order" search and manufacturer check of 14 purchases (2026-08-20).
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- No test changed a city system. Controller programs were read, never written. The unattended connection test was done once, with the city hall BAS workstation idle and the owner on site watching its screen.
- No customer data was copied off the devices; screenshots were cropped to settings only.
- Findings that touched a customer were reported under the contracts: the remote-desktop agent was disclosed to the city IT manager on 2026-08-21, and the unverified switch was reported to the prime on 2026-08-20.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 9 |
| Other than satisfied | 28 |
| **Total** | **37** |

**Fully satisfied:** SC-28 (laptop and phone encrypted).
**Fully other than satisfied:** AC-17, IA-2(1), AC-6, AU-6, IR-6, SR-3.
**Partly satisfied:** IA-5 (3 of 10; the issue is the shared BAS password and the missing password manager), CP-9 (2 of 6; documents are versioned but controller programs have one stale copy), MP-4 (3 of 5; paper is controlled, digital CUI is not).

**Findings that changed something during the test:**
- **Remote-desktop agent (AC-17, IA-2(1)).** The unattended connection worked with a password alone. The owner turned on MFA and turned off unattended access the same day (2026-08-18) and told the city IT manager on 2026-08-21. The city asked for the agent to be removed by 2026-09-30.
- **Stale controller programs (CP-9).** 4 of the 11 library program copies on the laptop were older than the programs running in the controllers. A controller failure in those 4 air handlers would have restored an old sequence.
- **Switch with an unconfirmed manufacturer (SR-3).** One of 14 parts supplied for the federal building came from an online marketplace. It is not known to be covered equipment; the owner told the prime, and it will be confirmed or replaced by 2026-09-30.
- **First log review (AU-6).** All 37 remote sessions in the 90 days of history came from the owner's devices, and the access control audit trail showed no unexplained administrator change. Nothing suggested an intrusion, so no incident notice was needed.

The 9 controls with weaknesses are tracked in 8 POA&M items in `poam.csv` (the IA-2(1) finding shares POAM-001 with AC-17). The High items are POAM-001 (remote-desktop agent, due 2026-09-30) and POAM-002 (shared BAS password, due 2026-10-31).

## 5. Deliverables
`assessment-results.csv` (37 rows), `poam.csv` (8 items), and this memo. Accepted by the owner on 2026-09-04. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year. A summary of the POA&M goes to the city IT manager with the account list by 2026-09-30.
