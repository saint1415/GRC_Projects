# Security Assessment Plan and Summary: Cris Santos Company | Wholesale Trade | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed IT hardware and software wholesale distributor) |
| System assessed | Distribution Operations Platform (DOP, SYS-01 to SYS-14), per the SSP (P02), including the purchasing and receiving processes that apply the SR controls |
| Tier / Vertical | Mid-Market / Wholesale Trade |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead and 2 IT auditors), reporting to the board audit committee. The firm does not design or operate any assessed control. The Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (site walkthroughs 2026-08-10 to 2026-08-13; OT and FIL tests after hours on 2026-08-12) |
| Also supports | SP 800-171 Rev. 2 requirement 3.12.1 (periodic assessment); readiness for the 2027-03 CMMC Level 2 (C3PAO) assessment; annual internal IT audit |
| Results accepted | Chief Operating Officer, 2026-09-17; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **34 controls, 194 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- implement SP 800-171 requirements and clause duties with High gaps in the gap analysis (P03), especially those that cannot be placed on a CMMC POA&M;
- test the supply chain controls behind the P08 supplier compromise runbook;
- support inherited-control reliance and SOC 2 readiness (P09).

This is an SP 800-53A assessment of SP 800-53 controls in the SSP. It is **not** a CMMC assessment: a C3PAO will assess the 110 SP 800-171 requirements against SP 800-171A objectives in 2027-03.

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Access lifecycle; 3.5.6, 3.9.2; R-019 | Focused | Focused (samples of 25; all 12 enclave leavers) |
| AC-3, AC-4 | CUI outside the enclave; 3.1.1, 3.1.3; R-004 (High) | Focused | Focused |
| AC-6 | Standing administrators; 3.1.5; R-017 (High) | Comprehensive | Comprehensive (all 61 privileged accounts) |
| AC-17, MA-4 | Integrator remote access; R-005 (High) | Focused | Focused |
| AT-2, AT-3 | Training gaps; 3.2.2, 3.2.3; R-018, R-025 | Basic | Focused |
| AU-6, AU-11, SI-4 | Monitoring and retention; 3.3.1; 252.204-7012(e); R-020, R-021 | Focused | Focused |
| CM-6, CM-7, CM-8 | Configuration, least functionality, inventory; 3.4.1; R-005, R-038 | Focused | Focused |
| CP-4, CP-9, CP-10 | Recovery; R-001 (Very High), R-013 | Comprehensive | Comprehensive |
| IA-2(1), IA-2(2), IA-5 | Authentication; 3.5.3; R-017 | Focused | Focused |
| IR-4, IR-6 | Incident handling and reporting; 252.204-7012(c); 52.204-25(d); 52.204-30(c); R-022 | Focused | Basic |
| MP-7, SC-13 | FIL media control and FIPS mode; 3.8.7, 3.13.11 | Focused | Comprehensive (all 22 FIL workstations; FIL VPN) |
| PE-3 | Visitor control; 3.10.3; 52.204-21(b)(1)(ix); R-043 | Focused | Focused (4 locations) |
| RA-5 | Scanning; 3.11.2; R-036 | Focused | Focused |
| SA-9 | Cloud and service providers; 252.204-7012(b)(2)(ii)(D); R-012, R-039 | Focused | Focused (22 Tier 1 vendor files) |
| SC-7 | Boundaries, OT exposure; R-001, R-005 | Focused | Focused |
| SI-3 | Malware protection (inherited reliance on EDR) | Basic | Focused |
| SR-5, SR-6, SR-10, SR-11 | Counterfeit, tampered, and covered products; 252.246-7007, 252.246-7008, 52.204-25, 52.204-30; R-003 (Very High), R-006 | Focused | Focused (purchasing, DC-1 and DC-2 receiving, FIL) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items; small populations were tested in full. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 214 | 25 | AC-2, PS-4 |
| Enclave leavers | 12 | 12 | AC-2, PS-4 |
| Transfers | 96 | 25 | AC-2 |
| Privileged accounts (all planes) | 61 | 61 for rights review; 25 for MFA test | AC-6, IA-2(1) |
| DC automation controllers | 6 | 6 (default-credential test) | IA-5 |
| FIL workstations | 22 | 22 (policy report); 4 (USB test) | MP-7 |
| Endpoints for EDR test | about 1,300 | 5, including 1 FIL workstation | SI-3 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| Tier 1 vendors | 22 | 22 | SA-9 |
| Broker purchase orders (2026) | about 410 | 20 | SR-5 |
| Federal drop-ship orders (2026) | 310 | 20 | SR-5 |
| Inbound receipts observed | about 180 a day | 10 at DC-1, 8 at DC-2 | SR-10 |
| Incidents (12 months) | 41 | 10 | IR-4 |
| Critical vulnerability findings | 50 corporate; 12 enclave | 50; 12 | RA-5 |
| Servers for configuration scan | 46 | 10 | CM-6 |
| Staff for reporting-awareness interviews | 850 | 15 | IR-6, AT-2 |
| Locations for walkthroughs | 5 | 4 (DC-1, DC-2, the Integration Center, the FIL cage) | PE-3, SC-7, CM-8 |

## 3. Methods and objects
- **Examine:** the 2024 policies and the 2026 drafts; the SSP draft and enclave SSP 1.0; IdP, ERP, WMS, enclave, and cloud exports; backup, patch, scan, and EDR reports; vendor files and contracts; the approved supplier list and broker files; procedure QP-14 and inspection records; the incident register; training records; badge and visitor logs.
- **Interview:** vCISO, Director of Information Technology, Security Manager and both analysts, Director of Federal Programs, Federal Integration Lab Manager, Vice President of Supply Chain, Director of Quality and Product Compliance, Director of Distribution Operations, HR Director, the MSSP service lead, the integrator's field engineer, and 15 randomly selected staff.
- **Test and observe:**
  - access to a CUI-attached ERP order with a customer service test account
  - reachability from a corporate VLAN to the OT and FIL networks
  - port scan of the DC-1 OT subnet and FIL subnet
  - security-key sign-in tests on 25 privileged accounts
  - default-credential tests on 6 DC automation controllers (after hours, integrator present)
  - unregistered USB drive on 4 FIL workstations
  - EICAR test files on 5 endpoints
  - restore of one file-share folder from the backup account
  - observation of 18 inbound receipts at DC-1 and DC-2
  - query of broker-sourced SKUs received at DC-2 since 2026-01, with OEM serial validation of a sample

## 4. Rules of engagement
- No testing that could disrupt shipping. Network and OT tests ran after the last carrier cutoff, with the Director of Distribution Operations and the integrator present.
- CUI was viewed only inside enclave sessions and the FIL cage by assessors who are U.S. persons. No CUI or FCI left company systems; screenshots were redacted, and workpapers are kept in the firm's encrypted system.
- Stop-and-notify rule: any critical exposure is reported to the Director of Information Technology and the vCISO the same day. **Used once:** on 2026-08-13 the assessors reported that 64 broker optical transceivers had been received at DC-2 without inspection and that the OEM could not validate 23 of the sampled serial numbers. Quality quarantined the remaining stock the same day, and the company logged the finding as P01 R-051 on 2026-08-14. The P08 supplier compromise runbook uses this case as its worked example.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 121 |
| Other than satisfied | 73 |
| **Total** | **194** |

Other than satisfied statements by risk: 36 High, 36 Moderate, 1 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 20 | 6 | Moderate | POAM-002 |
| AC-3 | 0 | 1 | High | POAM-001 |
| AC-4 | 0 | 1 | High | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-003 |
| AC-17 | 2 | 2 | High | POAM-004 |
| AT-2 | 8 | 2 | Moderate | POAM-006 |
| AT-3 | 5 | 4 | Moderate | POAM-006 |
| AU-6 | 2 | 1 | Moderate | POAM-007 |
| AU-11 | 0 | 1 | Moderate | POAM-008 |
| CM-6 | 3 | 3 | Moderate | POAM-009 |
| CM-7 | 3 | 3 | High | POAM-005 |
| CM-8 | 3 | 3 | Moderate | POAM-010 |
| CP-4 | 2 | 3 | High | POAM-011 |
| CP-9 | 5 | 1 | Low | POAM-012 |
| CP-10 | 0 | 2 | High | POAM-011 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-2(2) | 0 | 1 | Moderate | POAM-013 |
| IA-5 | 7 | 3 | Moderate | POAM-014 |
| IR-4 | 9 | 4 | High | POAM-015 |
| IR-6 | 1 | 1 | High | POAM-015 |
| MA-4 | 2 | 6 | High | POAM-004 |
| MP-7 | 1 | 1 | Moderate | POAM-016 |
| PE-3 | 9 | 3 | Moderate | POAM-017 |
| PS-4 | 3 | 2 | Moderate | POAM-002 |
| RA-5 | 7 | 2 | Moderate | POAM-018 |
| SA-9 | 3 | 3 | High | POAM-019 |
| SC-7 | 4 | 2 | High | POAM-005 |
| SC-13 | 1 | 1 | Moderate | POAM-020 |
| SI-3 | 8 | 0 | n/a | n/a |
| SI-4 | 9 | 3 | Moderate | POAM-007 |
| SR-5 | 1 | 2 | High | POAM-021 |
| SR-6 | 0 | 1 | High | POAM-021 |
| SR-10 | 0 | 1 | High | POAM-022 |
| SR-11 | 2 | 3 | High | POAM-022 |

**Fully satisfied (2 controls):** IA-2(1) (security keys on all 25 sampled privileged accounts) and SI-3 (EDR quarantined every test file within 4 minutes and alerted the MSSP). CP-9 was satisfied except for one statement (DC automation configurations), and the backup restore took 40 minutes.

**Fully other than satisfied (8 controls):** AC-3, AC-4, AC-6, AU-11, CP-10, IA-2(2), SR-6, and SR-10.

**Themes:**
1. **The enclave works; the business processes around it leak.** CUI reached the ERP, the commercial email tenant, and Integration Center benches (AC-3, AC-4).
2. **OT and vendor access are the largest technical exposure** (SC-7, CM-7, AC-17, MA-4, IA-5).
3. **Product integrity depends on which dock receives the goods.** DC-1 inspects broker receipts; DC-2 does not, and the transceiver finding shows the result (SR-10, SR-11).
4. **Recovery is designed but not proven** (CP-4, CP-10).

**POA&M:** 32 controls had at least one Other than satisfied statement. They map to 22 POA&M items (POAM-001 to POAM-022), because related controls share an item. Four more items come from other deliverables: POAM-023 (C-SCRM plan, P03), POAM-024 (SPRS correction and CMMC readiness, P03), POAM-025 (AI governance, P10), and POAM-026 (reseller portal MFA, P01 and P09). The total is 26 items: 11 High, 14 Moderate, and 1 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Site walkthroughs and technical tests |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (194 rows); `poam.csv` (26 items).
