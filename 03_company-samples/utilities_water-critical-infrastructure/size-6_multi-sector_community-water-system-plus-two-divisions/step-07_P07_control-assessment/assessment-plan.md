# Security Assessment Plan and Summary: Cris Santos Company Holdings | Water and Wastewater Systems | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, SYS-G4, the group OT security office, group HR), the SSP system RS1-SCADA (P02), and samples of Water Utility, Construction, and Environmental Services controls |
| Tier / Vertical | Multi-Sector / Water and Wastewater Systems (focus division: Water Utility) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`), with OT test methods from NIST SP 800-82 Rev. 3 |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls, with an outside OT assessment firm for site testing. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28, with site visits to the RS-1 ROC, WTP-A, WTP-C, 6 RS-1 remote sites, and 4 acquired water systems |
| Also supports | The automated-systems element of the RRAs (42 U.S.C. 300i-2(a)(1)(A)(ii)); Construction's periodic assessment of NIST SP 800-171 requirements (3.12.1) |

## 1. Approach: assess common controls once, then sample divisions
Most identity, monitoring, remote access, and backup safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and give three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three, and the gateway session sample included Water Utility, integrator, and Construction commissioning sessions).
2. **RS1-SCADA's** system-specific controls were assessed because it is the SSP system and is where the top group risk lands (GR-01).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

The Water Utility sample focused on the 19 acquired systems (scenario gap 2). The Construction sample focused on the CUI enclave and where CUI actually was (gap 4). The Environmental Services sample focused on client site gateways, client notices, and control inheritance (gaps 5 and 7).

## 2. Controls selected
**36 control assessments** (30 distinct controls; AC-17, AU-6, CA-2, CP-9, IR-6, and SC-7 were assessed in two scopes), **243 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-6(5), IA-2(1), IA-5 | 38 | GR-01, GR-10; every division's access | Focused / Comprehensive (all divisions sampled) |
| Common control (SYS-G4 OT remote access) | AC-17, MA-4 | 12 | GR-01 (High); scenario gap 1 | Comprehensive / Comprehensive |
| Common control (SYS-G2 SOC and OT monitoring) | SI-4, AU-6, IR-3, IR-4, IR-6, IR-8 | 48 | GR-03, GR-12; scenario gap 6 | Focused / Comprehensive |
| Common control (Group OT security office) | RA-5 | 9 | GR-04, GR-16 | Focused / Focused |
| Common control (SYS-G3 cloud) | CP-9 | 6 | GR-02; immutable backups | Focused / Focused |
| Common control (Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| SSP system (RS1-SCADA) | CM-3, CM-8, CP-4, SI-2, AC-6, SC-7, SI-7, SA-4 | 60 | WU-001, WU-003, WU-011; the WTP-A expansion | Comprehensive / Focused (3 plants, 6 remote sites) |
| Division sample: Water Utility acquired systems | AC-17, IA-2, CP-9, SC-7 | 18 | GR-04, WU-002 (High) | Focused / Focused (4 of 19 systems) |
| Division sample: Construction CUI enclave | AC-4, CA-2, SC-13, AU-6 | 17 | GR-06, CN-001, CN-002 (High) | Comprehensive / Focused (enclave, SYS-C1, 40 laptops) |
| Division sample: Environmental Services monitoring service | CM-6, IR-6, AC-3, CA-2 | 20 | ES-001 (High); P09 readiness | Focused / Comprehensive (all gateways audited) |
| **Total** | **36** | **243** | | |

## 3. Methods and objects
- **Examine:** identity governance, OT directory, and PAM configuration; gateway policy, approval logs, and recordings; SIEM sources and OT sensor coverage; RS-1 MOC records and the Construction commissioning log; OT asset inventory; patch and backup records; firewall rule bases; ERPs and the group IR plan; the CMMC self-assessment package and SPRS record; contracts (intercompany, integrator, client).
- **Interview:** group identity, SOC, cloud, and OT security leaders; the RS-1 Director of Operations and SCADA engineering lead; control room supervisors at the ROC and WTP-C; operators at 4 acquired systems; the Construction CMMC program owner and commissioning director; the Environmental Services remote monitoring general manager.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations;
  - a gateway session sample of 50 (20 commissioning sessions) traced to approvals and recordings;
  - privileged sign-in tests to 20 systems, including RS-1 engineering workstations;
  - a field check of 60 WTP-A devices against the inventory and 40 RS-1 RTU credentials;
  - PLC logic comparison on 5 RS-1 PLCs against offline copies (read-only, during a planned window);
  - network walk-downs and an external exposure scan of 4 acquired systems;
  - a CUI discovery scan of SYS-C1 and 40 commissioning laptops;
  - an audit of every Environmental Services client site gateway, and cross-tenant access attempts in test tenants;
  - restores of 3 data platform datasets and 1 SYS-E1 tenant from the immutable vault.

## 4. Rules of engagement
- **No active scanning or writes to live OT.** PLC comparisons were read-only and scheduled with operations; the RS-1 Director of Operations could stop any test. Water safety overrode every test plan.
- No CUI left the enclave during testing; discovery scan results listed file locations, not contents.
- No client data left SYS-E1; gateway audits used the platform's management interface.
- The assessor would stop and notify the Group CISO on any critical exposure. One was found: internet-reachable modem administration at 3 acquired systems. It was reported to the Group CISO on the day it was found (2026-08-11), the default passwords on those modems were changed that week as an interim step, and the move to a private APN and the segmentation work are tracked in POAM-017.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 108 | 20 | 128 |
| SSP system (RS1-SCADA) | 48 | 12 | 60 |
| Division sample: Water Utility acquired systems | 12 | 6 | 18 |
| Division sample: Construction CUI enclave | 12 | 5 | 17 |
| Division sample: Environmental Services monitoring service | 15 | 5 | 20 |
| **Total** | **195** | **48** | **243** |

**Common controls are mostly strong.** 108 of 128 common statements were satisfied. Privileged access (AC-6(5), IA-2(1)), cloud backups (CP-9), terminations (PS-4), and training (AT-2) had no findings. The common findings are about **one exception and its side effects** (AC-2, AC-17, MA-4, AU-6: the commissioning team's standing, unapproved, unreviewed access), **monitoring coverage** (SI-4: 6 of 58 systems), **OT vulnerability depth** (RA-5), and **cross-division incident readiness** (IR-3, IR-4, IR-6, IR-8; scenario gap 6).

**RS1-SCADA is well run, with a supplier-shaped hole.** Boundary protection (SC-7) and integrity checking of PLC logic (SI-7) had no findings. The findings trace to the WTP-A expansion (CM-3, CM-8, AC-6, SA-4) and to WTP-C's end-of-support HMIs and untested restores (SI-2, CP-4).

**Division samples:**
- *Water Utility acquired systems:* always-on vendor tools and undocumented remote access (AC-17), shared HMI logins (IA-2), no offline controller backups (CP-9), and flat networks with exposed modems (SC-7). Every acquired-system control assessed had a finding.
- *Construction:* CUI outside the enclave (AC-4), a self-assessment whose scope missed the real CUI locations and recorded 7 unmet requirements as MET (CA-2), a non-validated transfer tool (SC-13), and a lapsed weekly log review (AU-6).
- *Environmental Services:* default credentials on 23 client gateways (CM-6), no client incident notice terms (IR-6), and undocumented inheritance (CA-2). Tenant isolation (AC-3) passed.

**Controls fully other than satisfied** (every statement failed): IR-3 (common), AC-6 (RS1-SCADA), and AC-4 (Construction). Each has only one determination statement.

28 of the 36 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **29 items**: 24 from this assessment, 4 from the P03 gap analyses (POAM-024 to POAM-027), and 1 from the P01 register confirmed in P10 (POAM-028, AI-001 validation). By risk: 8 High (POAM-002 commissioning access, POAM-013, POAM-016, and POAM-017 for the acquired systems, POAM-018 and POAM-020 for CUI and the CMMC record, POAM-022 client gateways, POAM-024 RRA cyber element and ERPs), 19 Moderate, and 2 Low. Status: 23 In progress, 6 Open. Each item names the related P01 risks and its scope.

## 7. Deliverables and acceptance
`assessment-results.csv` (243 rows, with an `assessment_scope` column), `poam.csv` (29 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-15. Division presidents accepted their division findings the same week. The Construction findings were also shared with Group General Counsel because they bear on the 2026-12-12 CMMC affirmation.
