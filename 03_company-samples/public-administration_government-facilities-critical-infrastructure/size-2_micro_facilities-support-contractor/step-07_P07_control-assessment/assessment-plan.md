# Security Assessment Plan and Summary: Cris Santos Company | Government Services and Facilities | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (facilities support contractor operating government buildings) |
| System assessed | Building Systems Operations Platform (BSOP), per the SSP (P02) |
| Tier / Vertical | Micro / Government Services and Facilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent building systems security consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office and Compliance Manager; Lead Controls Technician present for gateway tests; MSP lead technician on call |
| Assessment window | 2026-08-03 to 2026-08-06 (gateway tests on the evening of 2026-08-05 with the county facilities director's approval) |
| Also satisfies | CA-2 Control Assessments and the annual independent assessment clause of the county security exhibit |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 88 determination statements.** Controls were chosen because they support the 4 High risks in P01 (shared remote write access, SYS-01 administrator takeover, ransomware on engineering laptops, MSP compromise), carry the county exhibit's named requirements (MFA, incident notice), cover the FAR clauses the company must meet, or test what the MSP does on the company's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Shared "oncall" account; former technician's SYS-01 access for 3 months (P01 R-001, R-003; P03 G-002, G-117) | Focused | Comprehensive (all user lists on 5 platforms and 7 gateways) |
| IA-2(1), IA-5 | MFA and passwords on the paths into buildings (R-001, R-004, R-023) | Focused | Focused (2 gateways and the "oncall" account tested; all 7 gateway logins checked for defaults) |
| AC-17 | Gateway VPN, city VPN, and the MSP RMM (R-004, R-010) | Basic | Focused |
| AU-6 | No log review (R-014) | Basic | Basic |
| CM-8 | No component inventory (P03 G-047) | Focused | Focused (one city building walked down) |
| CP-9 | Engineering records only on laptops (R-005, R-006) | Focused | Focused (3 laptops; SYS-08 report) |
| SI-2 | Gateway firmware; MSP patching (R-004) | Focused | Comprehensive for gateways (7 of 7) |
| IR-6 | Customer notice clocks not known (R-009) | Basic | Focused (5 of 7 staff interviewed) |
| MP-4 | CUI drawings (R-007; FAR and 32 CFR Part 2002 through CT-F) | Focused | Focused (office, 2 vans, 3 laptops) |
| SA-9 | MSP and SYS-02 vendor oversight (R-010) | Focused | Comprehensive (all 6 providers that hold data or administer systems) |
| SR-3 | FAR 52.204-23, -25, -30 screening (R-008) | Focused | Comprehensive (all 6 items supplied to the federal building in 2026) |

## 2. Methods and objects
- **Examine:** SYS-01, SYS-02, suite, CMMS, and gateway user lists; role lists; MFA settings; gateway configuration exports and firmware list; MSP contract, patch policy, and reports; SYS-08 job report; contracts and the subcontract; purchase records; the SYS-01 vendor's SOC 2 report; P01 risk register; termination record.
- **Interview:** owner, Office and Compliance Manager, Lead Controls Technician, Security Systems Technician, Controls Technician, Building Engineer, Service Coordinator, and the MSP lead technician.
- **Test:**
  - user lists compared with the staff roster on SYS-01, SYS-02, the suite, the CMMS, and the gateways
  - sign-in attempts without a second factor on 2 gateways and the SYS-02 "oncall" account (with the Lead Controls Technician present)
  - default password check on all 7 gateways
  - gateway firmware versions compared with the manufacturer's current releases
  - walk-down of the city community center BAS compared with the CMMS asset list
  - search of 3 laptops' downloads folders and the shared folder for CUI markings
  - trace of all 6 items supplied to the federal building in 2026 to their manufacturers

### MSP and vendor evidence requested
The MSP operates the laptop and office controls, so evidence came from it. Requested on 2026-07-27 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-07-31 |
| Antivirus console export (all laptops) | SI-3 (context) | Yes, 2026-07-31 |
| Laptop encryption report | SC-28 (context) | Yes, 2026-07-31 |
| SYS-08 job report and retention settings | CP-9 | Yes, 2026-08-03 |
| Record of any SYS-08 restore test | CP-9 | No record exists (confirmed by the MSP) |
| Technician list with access, and MFA on the RMM and backup console | AC-17, IA-2(1), SA-9 | Not received by fieldwork end; follow-up in POAM-002 and POAM-005 |
| SYS-02 vendor security documentation | SA-9 | Service terms only; no SOC report exists |

## 3. Rules of engagement
- No test could change a building system. Gateway tests were sign-in attempts and read-only configuration views, done in the evening of 2026-08-05 after the county facilities director approved them, with the Lead Controls Technician present.
- No cardholder data or CUI left the company. Screenshots were redacted before they went into the evidence folder.
- The assessor would stop and tell the owner at once about any critical exposure. The default gateway password was reported the same evening and changed before the assessor left.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 16 |
| Other than satisfied | 72 |
| **Total** | **88** |

**Fully other than satisfied:** IA-2(1), AU-6, IR-6, SA-9, and SR-3. No process or technology met the objective.
**Partly satisfied:** SI-2 (the MSP patches and tests laptop updates; nobody maintains gateways), CP-9 (the suite and its documentation are backed up and encrypted; engineering records are not), MP-4 (paper is well controlled; electronic CUI is not), and PS-4 (property was recovered; access was not).

**New findings from testing:**
1. The parks operations building gateway still had the manufacturer default administrator password (IA-05e.). Changed on 2026-08-05; added to the risk register as R-023 and to POAM-007.
2. The SYS-02 "oncall" account signed in from 4 different home internet addresses in July 2026, none attributable to a person (AC-02g.). The sign-ins matched on-call nights, but nobody can prove who made each change. POAM-001.
3. 11 BACnet controllers at the city community center were missing from the CMMS asset list (CM-08a.02). Added to the CMMS by 2026-09-15. POAM-009.
4. CUI drawings were in the downloads folders of 2 laptops (MP-04a.[03]). Deleted by 2026-09-15. POAM-012.
5. All 6 items supplied to the federal building in 2026 traced to manufacturers that are not named covered entities; one network switch had no recorded manufacturer until the purchase record was found (SR-03a.[01]). No FAR report was required. POAM-013.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The 5 High items are POAM-001 to POAM-005: shared and password-only access into buildings, broad remote access, missing backups, and unmanaged providers. They are the same remote-reach theme as P01.

## 5. Deliverables
`assessment-results.csv` (88 rows), `poam.csv` (13 items), and this plan and summary. The owner accepted the results on 2026-08-31.
