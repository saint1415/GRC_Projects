# Security Assessment Plan and Summary: Cris Santos Company Holdings | Government Services and Facilities | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (corporate shared services and three divisions) |
| Scope | Group common controls (SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and network, group HR), the Integrated Building Operations Platform (IBOP, the P02 SSP system), and samples of Facilities Support, Construction, and Janitorial and Security controls |
| Tier / Vertical | Multi-Sector / Government Services and Facilities (focus division: Government Facilities Support) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`); OT test limits from NIST SP 800-82 Rev. 3 |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls it assessed. Division security and compliance leads and the Construction CUI program manager acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 (customer site visits during the P03 walkthroughs, 2026-06-08 to 2026-06-19, supplied part of the evidence) |
| Also satisfies | The annual independent assessment that state agency contract exhibits require for contractor-managed systems (SP 800-53 Rev. 5 Moderate); evidence for the 2026 SOC 2 Type 2 period (P09) and the GovRAMP readiness plan (POAM-030) |

## 1. Approach: assess common controls once, then sample the IBOP and the divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and give three slightly different answers. So:
1. **Common controls** marked for the 2026 cycle in the P02 common control catalog (`common-control-catalog.csv`, `assessed_in_P07` = Yes) were assessed **once**, with samples drawn from every division. For example, the joiner-mover-leaver sample took 75 events from all three divisions and corporate, and the termination sample included Janitorial and Security separations at customer sites. Findings are reported to the division where they were found, but the fix belongs to the control provider.
2. **The IBOP's** system-specific and hybrid controls were assessed because it is the SSP system and carries the top group risk (P01 GR-01).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Catalog controls marked "No (2027 cycle)" were not re-tested as common controls this year; where a division or the IBOP operates part of one (for example AT-3, AC-6, SR-3, and SR-5), that part was sampled. Division findings are reported to that division, not averaged into the group.

Construction was sampled on assessment and CUI location controls because its SPRS score rests on a self-assessment that did not test inherited controls (scenario gaps 5 and 9). Janitorial and Security was sampled on its own policy set, supply chain screening, and site training because its 2022 policy set has drifted (gap 8) and its acquired installation business sits outside group screening (gap 6).

## 2. Controls selected
**36 control assessments** (34 distinct controls; AC-6 and AT-3 were assessed in two scopes), **265 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, IA-2, IA-2(1), IA-5 | 39 | Every division's access; GR-07; scenario gap 1 (integrator accounts) | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR) | PS-3, PS-4, AT-2 | 18 | 45,000 users and 58% turnover in Janitorial and Security; GR-10 | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, RA-5, IR-4, IR-6, IR-8 | 53 | GR-03, GR-12; scenario gaps 4 and 10 | Focused / Comprehensive |
| Common control (SYS-G3 cloud and network) | CP-9, SC-7, SC-28, CM-6 | 19 | GR-02; immutable backups, guardrails, and site boundaries | Focused / Focused |
| IBOP (SSP system) | AC-6, AC-17, MA-4, AU-6, AU-12, CM-8, CP-4 | 30 | GR-01 (High); scenario gaps 1 to 4; FS-001, FS-003 | Comprehensive / Focused (12 sites, 4 of them acquired) |
| Division sample: Facilities Support | CP-2, AT-3, PS-7 | 38 | FS-013, FS-026; building recovery procedures (GSA BTTRG v3.0 section 1.6.2) | Focused / Focused |
| Division sample: Construction (including the IBOP commissioning workspace) | CA-2, CA-5, CM-12, MP-3, PE-3 | 34 | CN-001, CN-002, CN-018 (High); DFARS 252.204-7012 and CMMC | Focused / Focused (6 DoD projects) |
| Division sample: Janitorial and Security | AC-6, AT-3, SR-3, SR-5, PL-1 | 34 | JS-001 (High), JS-003, JS-008, JS-017; gaps 6 to 8 | Focused / Focused (6 branches) |
| **Total** | **36** | **265** | | |

## 3. Methods and objects
- **Examine:** identity governance, PAM, and conditional access configuration; the integrator account list; SIEM data sources and detection rules; OT sensor coverage; scan and passive discovery reports; the group incident response plan and playbooks; landing-zone, backup, and edge gateway configuration; access control SaaS role exports for 188 tenants; jump service logs; the OT asset inventory and program repository; contingency plans and building recovery procedures; integrator subcontracts; the SPRS workpapers and CMMC system security plan; the CUI data map; drawing samples; screening logs and purchase records; the Janitorial and Security 2022 policy set; training records.
- **Interview:** the Group identity, SOC, cloud platform, and HR directors; the Group General Counsel and contracts compliance director; the IBOP security lead; the Facilities Support controls engineering, security systems, and operations directors; the Construction CUI program manager; the Janitorial and Security monitoring, operations, and talent directors; 6 branch managers.
- **Test:**
  - a joiner-mover-leaver sample of 75 events and 40 terminations across divisions; 25 customer-site separations and 31 PIV card returns;
  - a hardware-key administrator sign-in and federation checks on 48 applications;
  - controller credential tests and workstation scans at 12 sites (4 acquired);
  - passive OT discovery at 3 sites, compared with the inventory;
  - a simulated setpoint change at the controls engineering training lab to test OT detection;
  - restores of 3 IBOP databases and the program repository from the provider B vault;
  - an external exposure scan of the landing zones and site gateways;
  - searches for controlled markings in SYS-C1 and the commissioning workspace, and plan room walkthroughs at 6 DoD jobsites.

## 4. Rules of engagement
- **Building safety first.** No test could change a door state, schedule, setpoint, or controller program at an occupied customer building. OT discovery at customer sites was passive only (NIST SP 800-82 Rev. 3). The detection test used the training lab.
- No CUI, consumer report content, or cardholder data left group systems. CUI findings were recorded by file name and project only; consumer report access was tested with role exports and access logs, not by opening reports.
- Customer approval was obtained before any work at a customer site; customer security staff escorted the assessors at criminal justice and FTI buildings.
- The assessor would stop and notify the Group CISO on any critical exposure. **One was found:** on 2026-07-21 a vendor remote-support tool at an acquired school site was reachable from the internet with a default password. It was disabled within 24 hours; the remaining tools are in POAM-009.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 103 | 26 | 129 |
| IBOP (SSP system) | 15 | 15 | 30 |
| Division sample: Facilities Support | 30 | 8 | 38 |
| Division sample: Construction | 21 | 13 | 34 |
| Division sample: Janitorial and Security | 23 | 11 | 34 |
| **Total** | **192** | **73** | **265** |

By risk, the 73 statements other than satisfied are 35 High, 36 Moderate, and 2 Low.

**Common controls are mostly strong.** 103 of 129 common statements were satisfied. Backups (CP-9), encryption at rest (SC-28), and configuration settings (CM-6) had no findings, and all four restores from the provider B vault completed and matched their source hashes. Workforce identity is sound: every sampled workforce account was approved, certified, and disabled within 4 hours of termination. The common findings sit at the **edges of the group**: integrator accounts and acquired-site credentials (AC-2, IA-2, IA-2(1), IA-5), OT monitoring and scanning coverage (SI-4, RA-5), frontline training and customer-site credentials in Janitorial and Security (AT-2, PS-3, PS-4), flat networks and bypass connections at customer sites (SC-7), and inconsistent incident handling and notification across divisions (IR-4, IR-6, IR-8; scenario gap 10).

**The IBOP is where the risk is.** Half of its statements failed. AC-6 (the standing cross-tenant global administrator role) failed outright, and 6 of 8 MA-4 statements failed because integrator maintenance at the 37 acquired sites is neither approved, recorded, nor strongly authenticated. The test also found 312 unlisted BACnet devices at 3 sites (CM-8) and confirmed that the monitoring module failover has never been tested (CP-4).

**Division samples:**
- *Facilities Support:* building recovery procedures missing at 26% of state, local, and education sites (CP-2), OT and customer-required training gaps (AT-3), and inherited integrator subcontracts without security terms (PS-7).
- *Construction:* the SPRS self-assessment was not independent and did not test inherited controls or CUI outside the enclave (CA-2), the CMMC POA&M is a spreadsheet (CA-5), CUI sits in four undocumented places (CM-12), derivative drawings are unmarked (MP-3), and 3 of 6 plan rooms were unlocked (PE-3). Several of these are SP 800-171 requirements that may not be placed on a CMMC POA&M.
- *Janitorial and Security:* about 310 users can open consumer reports (AC-6), screening does not cover the installation business and 4 monitoring station NVRs have an unconfirmed manufacturer (SR-3, SR-5), staff at FTI and criminal justice buildings lack customer-required topics (AT-3), and the 2022 policy set conflicts with group policy (PL-1).

**Controls fully other than satisfied** (every statement failed): IA-2(1) (common), AC-6 (IBOP), CA-5 (Construction), and AC-6 and SR-5 (Janitorial and Security).

33 of the 36 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **30 items**: 27 trace to this assessment (most also appear in the P03 gap analyses) and 3 come from the P03 gap analyses only (POAM-026 consumer report disposal, POAM-029 Colorado SB26-189 deployer duties, POAM-030 GovRAMP readiness). By risk: 14 High, 14 Moderate, and 2 Low. Status: 27 In progress and 3 Open. Each item names its scope and the related P01 risks, and its owner and dates match the P01 registers and P03 gap tables.

The SSP authorization conditions (P02 section 4.2) depend on POAM-003, POAM-009, POAM-010 (due 2026-12-15), POAM-011 (2027-03-31), and POAM-019 (CUI out of the commissioning workspace).

## 7. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-06-30 | Assessment plan approved by the Group CISO and the board audit committee chair |
| 2026-07-06 to 2026-07-31 | Common controls (identity, HR, SOC, cloud) |
| 2026-08-03 to 2026-08-21 | IBOP and division samples |
| 2026-08-28 | Fieldwork closed; draft results to control owners |
| 2026-09-15 | Results presented to the board risk committee; accepted by the Group CISO and the Group Chief Risk Officer; division presidents accepted their division findings the same week |

Deliverables: `assessment-results.csv` (265 rows, with an `assessment_scope` column), `poam.csv` (30 items), and this plan and summary. The next cycle (2027) assesses the catalog controls marked "No (2027 cycle)" and re-tests every High item.
