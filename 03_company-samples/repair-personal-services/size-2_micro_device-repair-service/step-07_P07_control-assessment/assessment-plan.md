# Security Assessment Plan and Summary: Cris Santos Company | Other Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent electronics and device repair shop) |
| System assessed | Service Ticketing and Point-of-Sale System (STPS), per the SSP (P02) |
| Tier / Vertical | Micro / Other Services (except Public Administration) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Shop Manager; MSP lead technician on call; the Senior Technician present for bench tests |
| Assessment window | 2026-08-10 to 2026-08-12 (on site 2026-08-11, before opening) |
| Also supports | NIST CSF 2.0 ID.IM-01 (improvements from evaluations); evidence for the business account questionnaire (P09) and the 2026 SAQ P2PE |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **14 controls, 80 determination statements.** Controls were chosen because they support the three High risks in P01 (technician access to customer devices, the shared Counter login and ticket notes, ransomware), cover High gaps in P03, or test what the MSP does on the shop's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2 | Shared Counter login; leaver not processed (P01 R-002, R-003; P03 G-053) | Focused | Comprehensive (every SYS-01 and suite account against the roster) |
| AC-6, MP-7, PS-6 | Technician access to customer devices (R-001; G-016, G-057) | Focused | Focused (3 technicians; all 4 bench workstations) |
| IA-2(1) | MFA on administrator access, including MSP-held logins (R-010, R-013) | Focused | Comprehensive (every admin console) |
| AT-2, IR-6 | No training; no reporting rule (R-007, R-023) | Basic | Focused (5 of 7 staff interviewed) |
| AU-6 | No log review (G-077) | Basic | Basic |
| CM-7 | Bench tools and the flat network (R-006, R-020) | Focused | Focused (4 bench workstations; one scan of the staff Wi-Fi) |
| CP-4, CP-9 | Backup never tested (R-010; G-064, G-101) | Focused | Focused |
| MP-6 | No sanitization standard (R-005; G-038, G-115) | Focused | Focused (3 of 41 devices in the recycling cage) |
| SA-9 | No vendor terms (R-012, R-018; G-026) | Focused | Comprehensive (all 9 vendors that hold or touch customer data) |
| SI-12 | Retention of passcodes, card numbers, and customer data (R-002, R-004, R-008; G-061) | Focused | Comprehensive (SYS-01 field searches repeated; full bench storage listing) |

## 2. Methods and objects
- **Examine:** SYS-01 and suite user and role lists; the staff roster; SYS-01 audit log and alert settings; bench PC software lists and USB settings; firewall rule export; contract folder, merchant agreement, MSP contract, and the AI add-on terms; recycler certificates; personnel files; the MSP evidence listed below.
- **Interview:** Owner, Shop Manager, Senior Technician, 2 Repair Technicians or Counter Associates (5 of 7 staff in total), and the MSP lead technician.
- **Test:**
  - user lists compared with the staff roster in SYS-01 and the suite
  - a customer export attempted with a technician account
  - sign-in attempts to the backup console, firewall management page, and bench storage console without a second factor (with the MSP present)
  - a scan of the staff Wi-Fi from a test laptop placed where a customer device would sit
  - 3 devices marked as wiped in the recycling cage powered on and checked
  - the bench drawer's removable media checked for labels and contents (file names only; no files opened)

### MSP evidence requested
The MSP operates most technical controls on the office side, so evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 (context for CM-7) | Yes, 2026-08-07 |
| Antivirus console export (office endpoints) | SI-3 (context) | Yes, 2026-08-07 |
| Encryption report | SC-28 (context) | Yes, 2026-08-07 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-10 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Firewall rule export | CM-7 | Yes, 2026-08-07 |
| Technician list with access to the shop, and MFA on the remote management platform | SA-9 | Not received by fieldwork end; follow-up in POAM-014 |
| Any work on the bench workstations or bench storage | CM-7, SI-12 | None: outside the MSP contract (confirmed) |

## 3. Rules of engagement
- No testing that could disrupt customers or touch customer content. On-site tests ran before opening on 2026-08-11. No customer file was opened; only file names and sizes were recorded.
- No customer data left the shop. Screenshots were redacted before they went into the evidence folder.
- The assessor would stop and tell the Shop Manager at once about any critical exposure. The bench storage label and the unreset recycling device were reported the same morning.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 8 |
| Other than satisfied | 72 |
| **Total** | **80** |

**Fully other than satisfied (10 of 14 controls):** AC-6, IA-2(1), AT-2, AU-6, CP-4, IR-6, MP-6, MP-7, PS-6, and SI-12. AC-2 is close behind: only 3 of its 26 objectives (account managers, role membership, and intended use) are satisfied. For a shop that wrote its first policies on 2026-08-31 this is expected: most of these objectives need a written rule that did not exist at fieldwork.
**Partly satisfied:** CP-9 (backups run nightly and are encrypted, but are neither immutable nor protected by MFA), CM-7 (the firewall blocks inbound ports, but nothing is restricted inside the shop), and SA-9 (provider roles are in the MSP contract and merchant agreement, but nothing is required or monitored).

**New findings from testing:**
1. The bench storage console accepted the default administrator account, and its password was on a label on the device. The console was reachable from the staff Wi-Fi, where customer devices connect (IA-02(01), CM-07b.[05]). The label was removed and the password changed on 2026-08-12. Added to the risk register as R-024 and to POAM-003.
2. SYS-01 still listed an active named account for a Repair Technician who left in November 2025. Its sign-in log showed no use after the departure date. Disabled on 2026-08-11 (AC-02f.[04]).
3. One of 3 devices marked as wiped in the recycling cage had not been reset and opened to the customer's home screen (MP-06a.[02]). The Senior Technician re-checked all 41 devices in the cage that day; no other device held data. The device never left the shop, so no customer data was disclosed; it was logged as the shop's first incident record.
4. Three unlabeled USB drives were in the bench drawer; one held a customer's photo library from a June 2026 transfer job (MP-07b., SI-12[03]). The drives never left the shop and nobody outside the workforce had access. After the Senior Technician confirmed that the customer had received the data, the drives were wiped on 2026-08-12 and the event was logged.
5. A technician account exported the full customer list (AC-06), confirming the manager-role finding from P03.

Every control has at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-001 to POAM-004, POAM-006 to POAM-008, and POAM-010 to POAM-012: shared and over-privileged access, customer data handling at the bench, and backups.

## 5. Deliverables
`assessment-results.csv` (80 rows), `poam.csv` (14 items), and this plan and summary. The Owner accepted the results on 2026-08-31.
