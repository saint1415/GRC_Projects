# Security Assessment Plan and Summary: Cris Santos Company | Accommodation and Food Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Florida hotel owner and operator: 2 independent resorts and 4 franchised select-service hotels) |
| System assessed | Property Management and Point-of-Sale Platform (PMPS: SYS-01, SYS-03, SYS-04, SYS-06 to SYS-10, SYS-12), per the SSP (P02), including the company-managed property side of Hotels 3 to 6 |
| Tier / Vertical | Mid-Market / Accommodation and Food Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (objective labels and determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead and 2 IT auditors), reporting to the board audit committee. The firm does not design or operate any assessed control, and it is neither the QSA firm engaged for the 2026 SAQ D nor the planned SOC 2 service auditor. The Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (site walkthroughs 2026-08-10 to 2026-08-13; vendor remote tool test 2026-08-11; after-hours device and network tests 2026-08-12; lock server restore test in a lab 2026-08-13) |
| Also satisfies | Annual independent assessment under POL-01 4.11; annual internal IT audit; evidence input to the QSA-supported 2026 SAQ D (not a substitute for it) and to SOC 2 readiness (P09) |
| Results accepted | Chief Operating Officer (system owner), 2026-09-15; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **32 controls, 206 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01), above all the POS and reservation system compromise (R-001) and ransomware (R-002) scenarios used in P08;
- test the PCI DSS v4.0.1 requirements with High gaps in the gap analysis (P03), so the CFO knows which SAQ D answers are supported by evidence;
- cover the controls the SOC 2 examination for the REIT management agreement will rely on (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Account lifecycle across SYS-01 and the brand PMS; R-010; P03 G-031, G-073 (PCI 8.2, 7.2.4) | Focused | Focused (samples of 25) |
| AC-6, IA-2, IA-5 | Card display rights, shared night-audit logins, default and interface credentials; R-007, R-011, R-049; G-069, G-074, G-007 | Comprehensive | Comprehensive (all 162 SYS-01 users, all 64 brand PMS accounts) |
| AC-17, IA-2(1), MA-4 | Vendor remote access into the CDE; R-001, R-005; G-033, G-077 (PCI 8.4.3) | Comprehensive | Comprehensive (all 7 remote access paths) |
| AC-4, SC-7 | CDE isolation at Resort 2 and Hotels 3 to 6; R-001, R-006, R-013; G-003 (PCI 1.3) | Focused | Focused (4 of 7 sites) |
| AT-2 | Phone social engineering and device tampering awareness; G-059, G-080 | Basic | Focused |
| AU-2, AU-6, AU-11 | Logging coverage, daily review, retention; R-041; G-042, G-044, G-081, G-082 (PCI 10.2, 10.4.1, 10.5.1) | Focused | Focused |
| CM-6, CM-8 | Configuration baselines and the payment device inventory; R-012, R-050; G-002, G-078 (PCI 2.2, 9.5.1.1) | Focused | Focused (10 of 34 servers; 120 of 120 payment devices) |
| CP-4, CP-9 | Recovery of lock servers and cloud workloads; R-002, R-015, R-017; P05 finding 3 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident capability and notice clocks; R-040, R-052; G-063 (PCI 12.10) | Focused | Basic (10 of 43 incidents) |
| MP-6 | Media and leased device disposal; G-039, G-095 | Basic | Focused |
| RA-3, RA-5, SI-2 | Risk assessment, scanning, patching; R-027; G-024, G-050, G-071 (PCI 6.3.3, 11.3) | Focused | Focused |
| SA-9 | Vendor and franchisor oversight; R-006, R-020, R-021; G-061, G-087 (PCI 12.8, 12.8.5) | Focused | Comprehensive (31 of 31 card and guest-data vendors) |
| SA-22 | Unsupported Resort 2 POS server and lock server; R-030; G-071 | Focused | Comprehensive |
| SC-28 | Card data stored outside the vault; R-003, R-004; G-010, G-011, G-067, G-068 (PCI 3.2, 3.3.1) | Focused | Focused (60 recordings; mailbox discovery scan) |
| SI-3, SI-4 | Malware protection and monitoring; R-001, R-013; G-019, G-052 (PCI 5.2, 11.5) | Focused | Focused (30 PCs; 5 EICAR tests) |
| SI-7 | Payment page script integrity and terminal firmware; R-008; G-072, G-085 (PCI 6.4.3, 11.6.1) | Focused | Comprehensive (23 of 23 scripts) |
| SR-10 | Payment device inspection; R-012; G-079 (PCI 9.5.1.2) | Focused | Focused (30 devices; 13 weeks of logs) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for a control that operates many times a year at moderate risk; 5 to 10 items for weekly or monthly controls; the whole population where it is small or the risk is High. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 212 | 25 | AC-2, PS-4 |
| Transfers | 70 | 25 | AC-2 |
| New SYS-01 accounts | 96 | 25 | AC-2 |
| SYS-01 users with permissions | 162 | All 162 | AC-6 |
| Brand PMS company accounts | 64 | All 64 | AC-2, IA-2 |
| Privileged accounts (company) | 38 | 25 for MFA test | IA-2(1) |
| Remote access paths (VPN, broker, vendor tools) | 7 | All 7 | AC-17, MA-4 |
| Vendor-managed systems for default-credential test | 6 | All 6 | IA-5 |
| Interface credentials (POS to PMS, PMS to lock server, and others) | 11 | All 11 | IA-5 |
| Servers for configuration benchmark scans | 34 | 10 | CM-6 |
| Payment devices | 120 | 120 reconciled to lists; 30 physically inspected | CM-8, SR-10 |
| PCs | 520 | 30 (EDR status); 5 (EICAR test) | SI-3 |
| Backup job days (July 2026) | 31 | 31 | CP-9 |
| Incidents (2025-01-01 to 2026-07-31) | 43 | 10 | IR-4, IR-6 |
| Critical and high vulnerability findings (Q1-Q2 2026) | 46 | 46 | RA-5 |
| Critical patches for in-scope systems (last 12 months) | 14 | 14 | SI-2 |
| CRO call recordings (July 2026) | about 11,400 | 60 | SC-28 |
| Card and guest-data vendors | 31 | 31 | SA-9 |
| Scripts on booking pages | 23 | 23 | SI-7 |
| Staff for awareness and reporting interviews | 600 | 20 (4 sites) | AT-2, IR-6 |
| Sites for walkthroughs | 7 | 4 (Resort 1, Resort 2, Hotel 4, corporate office with the CRO) | AC-4, SC-7, CM-8 |

## 3. Methods and objects
- **Examine:**
  - policies (the 2024 set and the 2026 drafts) and the standards index
  - the SSP draft, the P03 scope tables, and the 2025 SAQ D
  - identity provider, SYS-01, brand PMS, and cloud exports
  - firewall rule exports for 7 sites
  - backup, patch, scan, ASV, and EDR reports
  - vendor AOCs, SOC 2 reports, contracts, and the franchise agreements
  - the incident log, the 2025 tabletop report, and the P08 drafts
  - device lists, inspection logs, destruction certificates, and lease return records
- **Interview:**
  - vCISO, IT Director, Security Manager, security analyst, and GRC Analyst
  - Chief Financial Officer and Director of Finance
  - General Counsel
  - Director of Central Reservations, both Resort Directors of Food and Beverage, both Resort Chief Engineers, and 3 General Managers
  - the MSSP service lead and the franchisor's regional IT contact
  - 20 randomly selected staff (front desk, night audit, CRO, outlets)
- **Test:**
  - MFA sign-in tests on 25 privileged accounts
  - connection test of the Resort 2 POS vendor and lock vendor remote tools (2026-08-11)
  - default-credential tests on 6 vendor-managed systems (after hours, vendor and Chief Engineer present, 2026-08-12)
  - reachability test from the Resort 2 POS VLAN to corporate networks (2026-08-12)
  - benchmark configuration scans of 10 servers
  - EICAR test files on 5 PCs
  - a simulated impossible-travel sign-in to test MSSP escalation
  - a lab restore of the Resort 2 lock server backup (2026-08-13)
  - physical inspection of 30 payment devices against the device list
  - browser capture of the booking pages to list scripts

## 4. Rules of engagement
- **Guests first.** No test that could stop check-in, key issue, or payments. Lock server, POS, and network tests ran after hours with the Resort Chief Engineer or the Resort Director of Food and Beverage present. Lock servers were not restarted; the restore test used a copy of the backup on lab hardware.
- **No real card data leaves company systems.** Screenshots were masked to the first 6 and last 4 digits at most. The 60 recordings were sampled inside the contact center system; no audio was exported. Evidence was kept in the firm's encrypted workpaper system.
- **Payment devices** were inspected, not opened. P2PE devices were not tested beyond inspection.
- **Franchisor systems are off-limits** for active testing. Brand firewalls and the brand PMS were reviewed only through company-side observation, account lists, and the franchisor's written answers.
- **Stop-and-notify rule:** any critical exposure is reported to the IT Director and the vCISO the same day. **Used once:** on 2026-08-12 the assessors found that the Resort 2 lock server still accepted the lock vendor's default administrator password. The password was changed that evening, and the company logged the finding as P01 R-050 on 2026-08-14.
- **Suspected incidents are not investigated by the assessors.** The 2026-03 suspected skimmer at Hotel 5, found unreported to the acquirer during the IR-6 test, was referred to the General Counsel and the CFO.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 121 |
| Other than satisfied | 85 |
| **Total** | **206** |

Other than satisfied statements by risk: 26 High, 48 Moderate, 11 Low.

| Control | Satisfied | Other than satisfied | Highest risk | POA&M |
|---|---|---|---|---|
| AC-2 | 20 | 6 | Moderate | POAM-001, POAM-002, POAM-005 |
| AC-4 | 0 | 1 | High | POAM-003 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 2 | 2 | High | POAM-004 |
| AT-2 | 8 | 2 | Low | POAM-008 |
| AU-2 | 2 | 4 | High | POAM-005 |
| AU-6 | 2 | 1 | High | POAM-005 |
| AU-11 | 0 | 1 | Moderate | POAM-005 |
| CM-6 | 2 | 4 | Moderate | POAM-006 |
| CM-8 | 2 | 4 | Moderate | POAM-007 |
| CP-4 | 2 | 3 | High | POAM-011 |
| CP-9 | 3 | 3 | High | POAM-011 |
| IA-2 | 1 | 1 | Moderate | POAM-002 |
| IA-2(1) | 0 | 1 | High | POAM-004 |
| IA-5 | 6 | 4 | High | POAM-002, POAM-006 |
| IR-4 | 10 | 3 | Moderate | POAM-009 |
| IR-6 | 1 | 1 | Moderate | POAM-009 |
| IR-8 | 13 | 4 | Moderate | POAM-009 |
| MA-4 | 1 | 7 | High | POAM-004 |
| MP-6 | 3 | 1 | Moderate | POAM-013 |
| PS-4 | 3 | 2 | Moderate | POAM-001, POAM-002 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 6 | 3 | High | POAM-010 |
| SA-9 | 1 | 5 | High | POAM-012 |
| SA-22 | 0 | 2 | High | POAM-010 |
| SC-7 | 4 | 2 | High | POAM-003 |
| SC-28 | 0 | 1 | High | POAM-013 |
| SI-2 | 7 | 3 | High | POAM-010 |
| SI-3 | 5 | 3 | High | POAM-014 |
| SI-4 | 7 | 5 | High | POAM-005, POAM-014 |
| SI-7 | 2 | 4 | Moderate | POAM-015 |
| SR-10 | 0 | 1 | Moderate | POAM-007 |

**Fully satisfied (1 control):** RA-3. The 2026 risk assessment follows SP 800-30, covers every business unit, and was approved under the risk acceptance authority in POL-01 4.4.

**Strengths confirmed inside partly satisfied controls:**
- MFA on all 25 sampled company privileged accounts (IA-2(1) fails only because of the 2 vendor tools).
- Identity provider accounts removed on the termination date for 25 of 25 leavers (AC-2).
- EDR quarantined all 5 test files within 5 minutes, and the MSSP escalated the simulated sign-in in 22 minutes, inside its 30-minute target (SI-3, SI-4).
- Daily backups of the workloads account ran on 31 of 31 days into the separate write-once backup account (CP-9).
- 30 of 30 inspected payment devices showed no sign of tampering (SR-10).

**Fully other than satisfied (7 controls):** AC-4, AC-6, AU-11, IA-2(1), SA-22, SC-28, and SR-10.

**Themes:**
1. **The cardholder data environment is wider than it needs to be.** Card data sits in mailboxes and recordings (SC-28), 46 users can display full card numbers (AC-6), and the Resort 2 POS and Hotels 3 to 6 networks are not isolated (AC-4, SC-7). These are the same conditions that let the R-001 attack path work.
2. **Vendors and the franchisor hold access the company cannot see.** Always-on vendor tools without MFA (AC-17, MA-4, IA-2(1)), a vendor default password (IA-5), and no responsibility matrix or current AOCs for 9 vendors (SA-9). These match the practices alleged in *FTC v. Wyndham* (P03 section 1.1).
3. **Visibility stops at the systems most likely to be attacked.** The Resort 2 POS, the lock servers, and Hotels 3 to 6 are outside logging, scanning, and EDR (AU-2, RA-5, SI-3, SI-4).
4. **Recovery of guest-safety systems is unproven.** The only lock server restore attempted failed (CP-4, CP-9).

**Effect on the 2026 SAQ D.** The CFO should not answer "In Place" for PCI DSS 1.3, 3.2 and 3.3.1, 3.4.1, 8.4.3, 10.4.1, 11.3, 11.4.5, or 12.8.5 until the linked POA&M items close. The CFO is agreeing the reporting approach for those requirements with the acquirer and the QSA firm (P03 section 4).

**POA&M:** 31 controls had at least one Other than satisfied statement. They map to 15 POA&M items (POAM-001 to POAM-015), because related controls share an item. Six more items come from other deliverables: POAM-016 PCI DSS scope and scope reduction (P03), POAM-017 retention schedule (P03), POAM-018 price displays and privacy notice (P03), POAM-019 AI governance conditions (P10), POAM-020 continuity and hurricane IT planning (P05), and POAM-021 SOC 2 readiness (P09). The total is **21 items: 12 High, 8 Moderate, and 1 Low** (16 In progress, 5 Open). See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Site walkthroughs and technical tests |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M accepted by the COO and presented to the audit committee |
| Each quarter | POA&M status to the audit committee (POL-01 4.5) |
| 2027 Q3 | Next annual assessment, with the High POA&M items retested |

Deliverables: this plan and summary; `assessment-results.csv` (206 rows); `poam.csv` (21 items).
