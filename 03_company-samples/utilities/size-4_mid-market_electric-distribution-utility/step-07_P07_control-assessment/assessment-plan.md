# Security Assessment Plan and Summary: Cris Santos Company | Utilities | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (investor-owned electric distribution utility, NERC-registered Distribution Provider) |
| System assessed | Distribution Operations Platform (DOP, CSC-DOP-01), per the SSP (P02), plus the company-wide controls that protect customer and client utility data in the CIS, AMI head-end, and CIS export (AC-5, MP-6, SI-12, SA-9, SR-6) |
| Tier / Vertical | Mid-Market / Utilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors) with an OT specialist subcontractor, reporting to the board audit committee. Neither firm designs or operates any assessed control. The Information Security Manager and the OT Engineering Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-10 to 2026-08-28 (substation testing 2026-08-18 to 2026-08-20, coordinated with the DCC) |
| Also supports | NERC CIP-003-9 internal compliance checks (CIP rows in P03); SOC 2 readiness evidence (P09); annual internal IT audit |
| Results accepted | Chief Operating Officer (system owner and CIP Senior Manager), 2026-09-17; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **34 controls, 236 determination statements** (every determination statement for each selected control). Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- carry CIP-003-9 low impact requirements with gaps in the gap analysis (P03);
- cover the voluntary OT benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3) for the SCADA, OMS, and field network;
- support SOC 2 readiness for Utility Services (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | OT account lifecycle and shared administrator accounts; R-001 (Very High), R-041 | Focused | Focused (samples of 25) |
| AC-5, AC-6 | AMI bulk disconnect and SCADA privilege; R-014, R-001 | Comprehensive | Comprehensive (all 22 AMI bulk users; all SCADA server accounts) |
| AC-17, MA-4 | Vendor remote access; CIP-003-9 Att. 1 Sec. 6; R-001, R-005 | Comprehensive | Focused (25 sessions; all 4 BES substations surveyed) |
| AC-3, AC-4, SC-7 | IT/OT boundary and gateway access lists; CIP-003-9 Att. 1 Sec. 3.1; R-004, R-005 | Comprehensive | Comprehensive (all IT/OT rules; all 4 BES gateways) |
| IA-2(1), IA-5 | MFA and authenticators; R-036, R-052 | Focused | Focused (25 of 61 privileged accounts; 30 of about 180 routers) |
| AT-2 | Awareness; CIP-003-9 Att. 1 Sec. 1; gap 15; R-018 | Basic | Focused (15 interviews) |
| AU-6, SI-4 | Monitoring and detection; CIP-003-9 Att. 1 Sec. 6.3; R-011 | Focused | Focused |
| CM-2, CM-3, CM-6, CM-8 | Baselines, change, inventory; gaps 1 and 8; R-006, R-013, R-051 | Focused | Focused |
| CP-2, CP-4, CP-9 | SCADA recovery; gap 7; R-007, R-016, R-017 | Comprehensive | Comprehensive |
| IR-6, IR-8 | Incident reporting and plan; CIP-003-9 Att. 1 Sec. 4; R-042 | Focused | Basic |
| MP-6, MP-7, SI-12 | Disposal, removable media, retention; CIP-003-9 Att. 1 Sec. 5.3; 16 CFR 682.3; R-003, R-024, R-025 | Focused | Focused (all 5 sites) |
| PE-2, PE-3 | Substation physical access; CIP-003-9 Att. 1 Sec. 2; R-009 | Focused | Comprehensive (all 4 BES substations) |
| RA-2 | Categorization; CIP-002-5.1a | Basic | Basic |
| RA-5, SI-2, SI-3 | Vulnerabilities, patching, malicious code; R-012, R-013 | Focused | Focused |
| SA-9, SR-6 | Vendor oversight; gap 9; R-015, R-026 | Focused | Focused (20 of about 85 vendors; all 14 OT remote access vendors) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items. Assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers | 58 | 25 | AC-2 |
| New OT and OMS accounts | 74 | 25 | AC-2 |
| Privileged accounts (IdP, cloud, OMS, jump hosts) | 61 | 25 for MFA tests | IA-2(1) |
| Jump host vendor sessions (2026-04-01 to 2026-07-31) | 412 | 25 | AC-17, MA-4 |
| Private LTE routers | about 180 | 30 (credential test) | CM-6, IA-5 |
| Substation gateways | 74 | 8 (credential test), 6 (configuration comparison) | CM-2, CM-6, IA-5 |
| BES substations | 4 | 4 (remote path survey, physical, passive capture) | AC-17, PE-2, PE-3, SC-7 |
| Field devices for firmware check | about 1,900 | 40 | SI-2 |
| Change board meetings (2026-02 to 2026-07) | 22 | 10 | CM-3 |
| DCC vendor access log review days | 104 | 10 | AU-6 |
| Vendor contracts | about 85 | 20 | SA-9 |
| Destruction certificates (2025-2026) | 41 | 10 | MP-6 |
| Staff for awareness and reporting interviews | 850 | 15 (including 6 field and 4 DCC) | AT-2, IR-6 |

## 3. Methods and objects
- **Examine:**
  - POL-01 to POL-05 (2025 versions and 2026 drafts), the CIP low impact policy and plan, the SSP draft
  - OT domain, SCADA, IdP, AMI, OMS, and jump host account exports
  - IT/OT firewall, OT DMZ, and substation gateway configurations
  - the OT asset inventory, change board minutes, PRC-005 test logs
  - SCADA and OMS recovery test reports, backup logs, the offline media register
  - vendor register and contracts; SOC 2 reports of the SCADA and ADMS vendor, AMI vendor, CIS vendor, and MSSP
  - records schedule, CIS data profile, CIS export share inventory
- **Interview:**
  - vCISO, Information Security Manager, the OT-focused security analyst
  - OT Engineering Manager and 2 SCADA engineers
  - Director of System Operations and 2 shift supervisors
  - Director of Engineering and Protection and the relay testing contractor's lead technician
  - Vice President of Customer Operations, Director of Utility Services, Procurement Manager, HR Director
  - the MSSP service lead; 15 randomly selected staff
- **Test:**
  - remote access path survey and passive network capture at Substations N, E, L, and H
  - reachability test from the corporate server administration subnet to the historian and engineering workstations
  - credential tests on 30 private LTE routers and 8 substation gateways (vendor-approved, read-only, DCC coordinated)
  - MFA sign-in tests on 25 privileged accounts and an OT domain administrator logon test
  - a simulated vendor session with a known-bad signature through a jump host, to test IDS detection and MSSP escalation
  - EICAR test files on 1 engineering workstation and 2 jump hosts (vendor-approved)
  - a 60-meter disconnect batch on the AMI test tenant
  - a restore of one SCADA display file from the weekly offline backup
  - firmware version reads on 40 field devices

## 4. Rules of engagement
- **No testing that could change grid state.** No active scanning of SCADA servers, HMIs, relays, RTUs, or field devices. Substation work was read-only, scheduled with the DCC, with a protection technician present. The DCC could stop any test at any time.
- No customer data left company systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system. OT diagrams and settings were viewed on site only.
- **Stop-and-notify rule:** any critical exposure is reported to the Information Security Manager, the OT Engineering Manager, and the NERC Compliance Manager the same day. **Used twice:**
  - 2026-08-19: the cellular modem at Substation H, installed by the relay testing contractor, giving routable access to the relays outside the gateway. The company disconnected it on 2026-08-20, updated P01 R-005 on 2026-08-21, and added it to the planned SERC self-report (P03).
  - 2026-08-19: vendor default passwords on 12 of 30 sampled private LTE routers. Logged as P01 R-052 on 2026-08-21; password changes began the same week.
- The CIP compliance implications of findings were referred to the NERC Compliance Manager and General Counsel; the assessors did not make compliance determinations.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 165 |
| Other than satisfied | 71 |
| **Total** | **236** |

Other than satisfied statements by risk: 22 High, 41 Moderate, 8 Low.

| Control | Satisfied | Other than satisfied | Highest risk | POA&M |
|---|---|---|---|---|
| AC-2 | 19 | 7 | High | POAM-001; POAM-002 |
| AC-3 | 1 | 0 | n/a | n/a |
| AC-4 | 0 | 1 | High | POAM-003 |
| AC-5 | 1 | 1 | High | POAM-013 |
| AC-6 | 0 | 1 | High | POAM-001 |
| AC-17 | 3 | 1 | High | POAM-004 |
| AT-2 | 8 | 2 | Moderate | POAM-010 |
| AU-6 | 2 | 1 | Moderate | POAM-009 |
| CM-2 | 2 | 3 | Moderate | POAM-005; POAM-008 |
| CM-3 | 8 | 2 | High | POAM-014; POAM-017 |
| CM-6 | 2 | 4 | Moderate | POAM-005; POAM-008 |
| CM-8 | 1 | 5 | Moderate | POAM-008 |
| CP-2 | 19 | 5 | High | POAM-007 |
| CP-4 | 2 | 3 | High | POAM-007 |
| CP-9 | 5 | 1 | Moderate | POAM-007 |
| IA-2(1) | 0 | 1 | Moderate | POAM-001 |
| IA-5 | 7 | 3 | High | POAM-001; POAM-005 |
| IR-6 | 1 | 1 | Low | POAM-016 |
| IR-8 | 15 | 2 | Low | POAM-016 |
| MA-4 | 6 | 2 | High | POAM-001; POAM-004 |
| MP-6 | 2 | 2 | Moderate | POAM-012 |
| MP-7 | 1 | 1 | Low | POAM-018 |
| PE-2 | 4 | 2 | Moderate | POAM-006 |
| PE-3 | 9 | 3 | Moderate | POAM-006 |
| PS-4 | 4 | 1 | Moderate | POAM-002 |
| RA-2 | 3 | 0 | n/a | n/a |
| RA-5 | 6 | 3 | Moderate | POAM-015 |
| SA-9 | 3 | 3 | Moderate | POAM-011 |
| SC-7 | 3 | 3 | High | POAM-003; POAM-004; POAM-009 |
| SI-2 | 8 | 2 | Moderate | POAM-015 |
| SI-3 | 8 | 0 | n/a | n/a |
| SI-4 | 10 | 2 | High | POAM-004; POAM-009 |
| SI-12 | 2 | 2 | High | POAM-012 |
| SR-6 | 0 | 1 | Moderate | POAM-011 |

**Fully satisfied (3 controls):** AC-3 (SCADA and OMS roles enforced as designed), RA-2 (FIPS 199 and CIP-002 categorizations documented and approved), and SI-3 (EDR detected and quarantined every test file within 4 minutes, and the kiosks blocked the test file on media). Strong partial results also confirm the strengths in the scenario facts: jump host sessions (25 of 25 named, MFA, DCC-enabled, and ended on time), IDS detection of the simulated malicious vendor session in 6 minutes, write-once cloud backups, and the incident response plan content.

**Fully other than satisfied (4 controls):** AC-4, AC-6, IA-2(1), and SR-6.

**Themes:**
1. **Paths around good controls.** The jump hosts work as designed, but the shared SCADA administrator accounts, the legacy IT/OT rules, a contractor modem, and default router passwords bypass them (AC-4, AC-6, AC-17, IA-5, SC-7).
2. **Recovery is not proven.** SCADA restore and failover do not meet the BIA (CP-2, CP-4).
3. **The field is less visible and less managed than the DCC** (CM-2, CM-8, RA-5, SI-4).
4. **Customer data is kept longer than needed** (SI-12, MP-6).

**POA&M:** 31 controls had at least one Other than satisfied statement. They map to 18 POA&M items (POAM-001 to POAM-018), because related controls share an item; POAM-017 also covers the ADMS row from the gap analysis. Four more items come from the gap analysis, the SOC 2 readiness assessment, and the AI assessment (POAM-019 Identity Theft Prevention Program, POAM-020 contractor laptops at L and H, POAM-021 AI governance, POAM-022 SOC 2 readiness). The total is 22 items: 8 High, 12 Moderate, and 2 Low. 15 are In progress and 7 are Open. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-31 | Plan, rules of engagement, and sample requests issued; DCC coordination agreed |
| 2026-08-10 to 2026-08-14 | Document examination and interviews |
| 2026-08-17 to 2026-08-21 | Technical tests (substation testing 2026-08-18 to 2026-08-20) |
| 2026-08-24 to 2026-08-28 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M accepted by the Chief Operating Officer and presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (236 rows); `poam.csv` (22 items).
