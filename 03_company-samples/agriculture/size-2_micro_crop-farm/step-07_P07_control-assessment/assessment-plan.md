# Security Assessment Plan and Summary: Cris Santos Company | Agriculture | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (precision-agriculture row crop and watermelon farm) |
| System assessed | Farm Management and Irrigation Control Platform (FMICP), per the SSP (P02) |
| Tier / Vertical | Micro / Agriculture, Forestry, Fishing and Hunting |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content); OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor and independence | Independent consultant with OT experience under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager (Security Coordinator); OT tests run with the Irrigation and Equipment Technician and the irrigation dealer present; MSP technician on call |
| Assessment window | 2026-08-10 to 2026-08-13 (on site 2026-08-11 and 2026-08-12; OT tests on 2026-08-12) |
| Benchmark | CSF 2.0 (P03). Results also feed the Produce Safety and H-2A record findings in P03 |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 102 determination statements.** Controls were chosen because they support the three High risks in P01 (ransomware, backups, and the exposed pump station gateway), cover the High gaps in P03, or test what the MSP and the irrigation dealer do on the farm's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2 | Shared field login, stale bookkeeper mailbox (P03 G-053, G-057; 21 CFR 112.161(a)(4); 20 CFR 655.122(j)(1)); R-009, R-010 | Focused | Comprehensive (every account in SYS-01, the suite, the telematics portal, and the backup console) |
| AC-17, MA-4 | Dealer's always-on remote access to the pump station (P03 G-071, G-078); R-002 | Focused | Focused |
| IA-2(1), IA-5 | MFA gaps and default credentials (P03 G-053, G-055); R-003, R-020 | Focused | Focused (all accounts that can control irrigation or delete backups; every OT device with a sign-in page) |
| CP-4, CP-9 | Backups never tested; controller program held by the dealer (P03 G-064, G-101); R-004 (High), R-007 | Focused | Focused |
| SC-7 | Flat network and the gateway path (P03 G-071); R-020 | Focused | Focused (tested from the shop Wi-Fi and against the gateway's public address) |
| SI-2, SI-3 | MSP patching and antivirus; OT firmware; R-001 (High) | Focused | Focused (3 office computers; gateway and controller firmware; after-hours alert routing) |
| AT-2, IR-6 | No training or reporting rule (P03 G-059, G-087); R-016 | Basic | Comprehensive (all 5 year-round staff interviewed, 2 in Spanish) |
| SA-9 | No supplier terms or oversight (P03 G-026, G-028); R-014, R-018, R-021 | Focused | Comprehensive (all 7 providers that run or reach farm systems) |

## 2. Methods and objects
- **Examine:** SYS-01, suite, telematics portal, and backup console user lists; the SYS-01 role list and security settings; the suite sharing report; the SYS-08 job report and retention settings; the firewall rule export; the irrigation dealer's 2026 invoices and the gateway connection history; the contract folder; the FMIS vendor SOC 2 report; training records; the P01 risk register and the draft SSP; the MSP evidence listed below.
- **Interview:** Owner and General Manager, Office Manager, Irrigation and Equipment Technician, Field Supervisor, Equipment Operator, the MSP technician, and the irrigation dealer's service technician.
- **Test:**
  - user lists compared with the staff list in SYS-01, the suite, the telematics portal, and the backup console
  - sign-in attempts without a second factor to the Technician's SYS-01 account, the backup console, and the gateway (with the MSP and dealer present)
  - reachability of the pump station touchscreen's web interface from a laptop on the shop Wi-Fi (one connection attempt, no scanning)
  - a check of the gateway's public address for an administration page, with the dealer's written consent
  - patch status on the 3 office computers and firmware versions on the gateway and controller
  - an industry-standard harmless antivirus test file on 1 laptop, and an after-hours test alert to check routing

### What each test could show
The new policies (P06) were drafted from 2026-08-03 to 2026-08-07 and approved on 2026-08-31, after fieldwork ended. During fieldwork they were drafts, so they were reviewed for design only. A control that a draft policy or the draft SSP introduces has not operated yet, so it cannot be tested for operation. The `test_type` column in `assessment-results.csv` says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control or condition existed before 2026 and was tested on samples, settings, or live systems | 46 |
| Design | The control is new (a draft policy or the draft SSP); its design was reviewed. Operation is tested at the 2027-02 follow-up | 5 |
| Not implemented | Nothing existed to test | 51 |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-AC-2 and so on), with the population each test was drawn from (for example, the user lists were compared with the 7 employees and the January 2026 termination in EV-001, the SYS-01 and suite accounts in EV-003 and EV-007, and the telematics accounts in EV-021; the 3 office computers come from the MSP device list in EV-009).

### MSP and dealer evidence requested
The MSP and the irrigation dealer operate most technical controls, so evidence came from them. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-08-07 (MSP) |
| Antivirus console export | SI-3 | Yes, 2026-08-07 (MSP) |
| SYS-08 job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-07 (MSP) |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Firewall rule export | SC-7 | Yes, 2026-08-07 (MSP) |
| List of MSP technicians with access and their MFA status | AC-17, SA-9 | MSP statement only (technicians use MFA); no list by fieldwork end; follow-up in POAM-010 |
| Gateway connection history and 2026 service invoices | MA-4 | Yes, 2026-08-10 (dealer) |
| Copy of the current controller program | CP-9 | Not received by fieldwork end; dealer agreed to hand it over by 2026-09-30 (POAM-003) |
| FMIS vendor SOC 2 Type 2 report | SA-9 | Yes, 2026-08-18, after fieldwork (EV-052; requested from the vendor 2026-08-03; reviewed in P09 on 2026-08-20) |

## 3. Rules of engagement (OT safety first)
- **No active scanning of the pump station controller, the VFD, the gateway, or the pivot panels.** SP 800-82 Rev. 3 warns that active scans can disrupt OT. Reachability was shown with a single connection attempt from the shop Wi-Fi.
- OT tests ran on 2026-08-12 between 06:00 and 09:00, outside irrigation run times, with the Technician present, pumps in local control, and fertigation off.
- No settings were changed on any OT device. The default-password test on the gateway stopped at the sign-in success page.
- No personal data left the farm. Screenshots of the Office folder and SYS-01 hours records were redacted.
- The assessor would stop and tell the Owner and General Manager at once about any critical exposure. One was found (below) and reported the same morning.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 19 |
| Other than satisfied | 83 |
| **Total** | **102** |

**Fully other than satisfied (6 controls):** AC-17, AT-2, CP-4, IA-2(1), IR-6, SC-7. No plan, process, or technology met the objective.
**Largely satisfied:** SI-3 (6 of 8: detection and quarantine work; after-hours alerting does not).
**Mostly other than satisfied:** AC-2 (4 of 26 satisfied), CP-9 (2 of 6), IA-5 (2 of 10), MA-4 (1 of 8), SA-9 (1 of 6), SI-2 (3 of 10).

**What the tests showed:**
- From the shop Wi-Fi, a laptop reached the pump station touchscreen's web interface (SC-07a.[04]). Anyone who knows the Wi-Fi password, including former contractors, could reach irrigation control.
- The Technician's SYS-01 administrator account, the backup console, and the gateway each accepted a password alone (IA-02(01)).
- The gateway connection history and invoices show 9 dealer remote sessions in 2026 that the farm did not approve or record (MA-04a.[01]).
- Two dealer technician accounts in the telematics portal belonged to people who no longer work for the dealer (AC-02f.[05]). They were removed on 2026-08-14 (EV-051).

**New finding (critical exposure, reported 2026-08-12):** the gateway's administration page was reachable from the internet and accepted the manufacturer's default password (IA-05e.). This was not known before testing. It was added to the risk register as R-023 (High) and to POAM-007. The dealer changed the password and turned off internet-facing administration on 2026-08-14 (EV-050); a firmware update and retest are due 2026-09-30.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The six High items are POAM-002 to POAM-007: remote access, backups, recovery testing, malware detection, network separation, and default credentials. They match the P01 theme: irrigation and records sit behind a few unmanaged passwords and an unproven backup.

## 5. Deliverables
`assessment-results.csv` (102 rows), `poam.csv` (13 items), and this plan and summary. The Owner and General Manager accepted the results on 2026-08-31.
