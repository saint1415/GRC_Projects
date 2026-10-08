# Security Assessment Plan and Summary: Cris Santos Company Holdings | Agriculture | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the Farm Management and Irrigation Control Platform (FMICP, P02 SSP system), and samples of Food Processing and Farm Supply controls |
| Tier / Vertical | Multi-Sector / Agriculture, Forestry, Fishing and Hunting (focus division: Crop Farming) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`); OT test methods follow NIST SP 800-82 Rev. 3 (passive first, active checks only in maintenance windows) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls, co-sourced with an independent OT assessment firm. Division security and compliance leads and OT security managers acted as liaisons only |
| Assessment window | 2026-07-01 to 2026-08-31 (off-season; OT tests ran outside irrigation run windows) |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers, so:
1. **Common controls** in the P02 common control catalog were assessed **once**, with samples drawn from every division (for example, the joiner-mover-leaver sample took 20 of its 60 events from seasonal starts and ends in Crop Farming).
2. **The FMICP's** system-specific controls were assessed in depth because it is the SSP system and carries the only Very High risk (CF-001).
3. **Division samples** covered controls Food Processing and Farm Supply operate themselves, chosen from their High risks and P03 gaps. Division findings are reported to that division, not averaged into the group.

## 2. Controls selected
**37 control assessments** (33 distinct controls; AC-3, CP-9, SA-9, SC-7 were assessed in two scopes), **237 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1) | AC-2, AC-2(3), AC-6(5), IA-2(1), IA-5 | 42 | Every division access control; GR-01, GR-05, GR-12 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1) | PS-4, AT-2 | 15 | Terminations and training for about 45,000 users including seasonal workers | Focused / Focused |
| Common control (SYS-G2) | SI-4, IR-4, IR-6, IR-8, RA-5 | 53 | GR-03, GR-04; EV-008, EV-012, EV-018 | Focused / Comprehensive |
| Common control (SYS-G3) | CP-9, SC-7, SC-8, SC-28 | 14 | GR-01; immutable backups and the hub network | Focused / Focused |
| FMICP (Crop Farming SSP system) | AC-17, MA-4, AC-3, IA-2, CM-3, CM-8, CP-2, CP-4, SC-7, SI-17, SC-24 | 68 | SSP system; CF-001 (Very High), CF-002 to CF-004; EV-020, EV-037, EV-039, EV-044 | Comprehensive / Comprehensive (3 ROCs; 6 legacy and 3 acquired farms) |
| Division sample: Food Processing | CM-5, SI-7, SA-9, AU-9, CP-9 | 26 | FP-001, FP-002, FP-003; EV-057, EV-058, EV-061 | Focused / Focused (3 of 11 facilities) |
| Division sample: Farm Supply | AC-3, CM-4, SA-11, SA-9, AC-6 | 19 | FS-004, FS-005; EV-070, EV-092 | Focused / Focused |
| **Total** | **37** | **237** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, the farm operations directory, SIEM and OT sensor coverage, landing-zone routes and firewall rules, backup vault settings, remote access inventories and remote tool configurations, change tickets and the FMIS change log, contingency plans and freeze procedures, food defense and food safety plans, historian settings, contractor agreements, the portal release record, and file share permissions.
- **Interview:** group identity, SOC, and cloud platform directors; the Crop Farming VP Irrigation and Field Technology, OT security manager, ROC leads at all 3 ROCs, and irrigation technicians at 9 farms; Food Processing food defense and preventive controls qualified individuals and the plant OT security manager; the Farm Supply portal general manager and credit director; the Group General Counsel.
- **Test:**
  - a joiner-mover-leaver sample of 60 events and 55 terminations (25 year-round, 30 seasonal);
  - a credential check of 60 pivot panel modems and 20 LoRaWAN gateways (read-only login attempts with the vendor default, outside run windows);
  - connection tests from the farm data hub account toward ROC networks, with ROC approval;
  - a simulated unexpected PLC logic download on the ROC-2 test bench and a remote tool session at an acquired farm, to test detection;
  - a loss-of-communication test on one test pivot at a legacy farm and one at an acquired farm;
  - restores of 3 data sets from the immutable vault and of 1 PLC program to a test controller at a plant;
  - a setpoint change test on a blanching line test recipe; cross-tenant access attempts in portal test tenants.

### What each test could show
The group policies v2026 (P06) were drafts during fieldwork; the board risk committee and the Group CISO approved them on 2026-09-10, effective 2026-10-01, and the Crop Farming supplement v2026-09 was re-issued after fieldwork, on 2026-09-08. The draft policies were reviewed as drafts, for design only, and no determination statement in `assessment-results.csv` rests on them: every statement was tested against the controls in force under the 2024 group policies, the division supplements on file at intake (EV-017) and the IR plan v5. The `test_type` column says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control existed before fieldwork and was tested on samples, configurations, interviews, or live systems | 228 |
| Design | The statement rests on a draft whose design was reviewed; operation is tested at the 2027-04 follow-up | 0 |
| Not implemented | Nothing existed to test: documented connection requirements for the integrator remote tool (AC-17), a manual freeze start procedure at the acquired ROC-1 farms (SI-17), integrity checks on plant historian data (SI-7, 2 statements), review of refrigeration contractor session recordings (SA-9), security and privacy impact analyses for the AI prescription launch (CM-4, 2 statements), and a portal privacy assessment plan and AI prescription validation testing (SA-11, 2 statements) | 9 |
| **Total** | | **237** |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-C-AC2 and so on), with the population each sample was drawn from (for example, the 60 joiner-mover-leaver events and 55 terminations come from the HR roster and identity governance records in EV-002 and EV-005, the modem and gateway sample from the OT asset inventory in EV-043, and the acquired farm remote access tests from the remote access inventory in EV-037).

## 4. Rules of engagement (OT)
- No active scanning of live PLCs or field controllers. Credential checks used single read-only attempts on modems and gateways outside irrigation run windows; any device that misbehaved would be power-cycled by the irrigation technician on site (none did).
- Every OT test had the ROC lead or plant manager on the call and a stop word. No test ran on freeze protection, fertigation, or ammonia refrigeration equipment in operation.
- No personal data left group systems; screenshots were redacted. The assessor would stop and notify the Group CISO on any critical exposure. One was found and escalated the same day: the integrator remote tool (it fed the board's interim measure for CF-001).

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls (SYS-G1, Group HR, SYS-G2, SYS-G3) | 100 | 24 | 124 |
| FMICP (Crop Farming SSP system) | 41 | 27 | 68 |
| Division sample: Food Processing | 21 | 5 | 26 |
| Division sample: Farm Supply | 14 | 5 | 19 |
| **Total** | **176** | **61** | **237** |

**Common controls are mostly strong.** 100 of 124 common statements were satisfied. CP-9, SC-8, SC-28 had no findings. The common findings concern **what the corporate controls do not reach in Crop Farming**: the farm operations directory (AC-6(5), IA-2(1), AC-2), seasonal accounts (AC-2, AC-2(3), PS-4), default credentials on field devices (IA-5), OT monitoring and scanning (SI-4, RA-5), and incident handling and notice for OT and cross-division duties (IR-4, IR-6, IR-8).

**The FMICP is where the risk is.** Integrator remote access failed 7 of 12 statements across AC-17 and MA-4 (no per-session authorization, approval, monitoring, strong authentication, or session end). Shared crew and integrator accounts failed identification (IA-2) and access enforcement (AC-3). OT change control (CM-3), recovery planning and testing (CP-2, CP-4), the manual freeze procedure (SI-17), and the loss-of-communication test at the acquired farm (SC-24) all had findings. The connection test confirmed that the farm data hub account can reach ROC networks (SC-7 in both the common and FMICP scopes).

**Division samples:**
- *Food Processing:* shared operator logins let anyone on 9 lines change setpoints (CM-5), historian data used as monitoring records has no integrity check (SI-7), and refrigeration contractor sessions are recorded but never reviewed (SA-9). Plant OT backups (CP-9) and record locking in the quality service (AU-9) passed.
- *Farm Supply:* the AI prescription feature skipped security and privacy impact analysis (CM-4) and validation testing (SA-11), and grower credit files are readable by 340 accounts (AC-6). Tenant isolation (AC-3) and subservice provider oversight (SA-9) passed.

**Controls fully other than satisfied** (every statement failed): AC-6(5) (common, SYS-G1), IA-2(1) (common, SYS-G1), AC-3 (FMICP), IA-2 (FMICP), SI-17 (FMICP), SC-24 (FMICP), CM-4 (Farm Supply), AC-6 (Farm Supply). Each has one or two determination statements.

30 of the 37 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **24 items**: 15 from this assessment and 9 from the P02 SSP review, the P03 gap analyses, the P09 readiness review, and the P10 AI assessment. By risk: 12 High (POAM-001, POAM-002, POAM-003, POAM-004, POAM-005, POAM-006, POAM-008, POAM-011, POAM-015, POAM-017, POAM-019, POAM-022), 11 Moderate, and 1 Low. Status: 15 In progress, 8 Open, and 1 Closed (POAM-014, the H-2A exports purged from the farm data hub and verified by internal audit). Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (237 rows, with an `assessment_scope` column), `poam.csv` (24 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-10. Division presidents accepted their division findings the same week.
