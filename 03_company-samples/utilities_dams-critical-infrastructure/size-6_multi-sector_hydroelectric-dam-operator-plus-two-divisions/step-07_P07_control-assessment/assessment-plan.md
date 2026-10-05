# Security Assessment Plan and Summary: Cris Santos Company Holdings | Dams | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1 identity, Group HR and training, SYS-G2 SOC and the General Counsel's notification process, SYS-G3 cloud, group procurement), the Hydro Plant Control and Dam Monitoring System (P02 SSP), and samples of Constructors (Federal Projects Enclave and jobsites) and Engineering (DSMS) controls |
| Tier / Vertical | Multi-Sector / Dams (focus division: Cris Santos Hydro) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit with a co-sourced OT specialist firm. Internal audit reports to the board audit committee; neither team designs nor operates the controls. Division security and compliance leads, the NERC Compliance Director, and the Federal Programs Compliance Director acted as liaisons only |
| Assessment window | 2026-07-01 to 2026-08-31 (site walkthroughs at HOC-A, DEV-02, DEV-05, and 2 Constructors jobsites, 2026-07-13 to 2026-07-17) |
| Also supports | FERC Security Program Form 3 Q24b (independent assessment) and Q31 (outsourced vulnerability assessment input); evidence for the CIP compliance program; the Constructors pre-assessment ahead of the CMMC Level 2 (C3PAO) assessment |

## 1. Approach: assess common controls once, then the SSP system and division samples
Most IT safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three divisions and corporate, and the termination sample included craft workers).
2. **The HPCDMS** (the P02 system) was assessed on the controls that carry the top group risk (GR-01) and the Section 9 and CIP-003-9 gaps found in P03.
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Constructors was sampled on the controls behind its CMMC score (AC-3, AT-3, PE-3, SI-3) and its supplement drift (PL-1). Engineering was sampled on the DSMS controls Hydro and 61 clients rely on (CA-3, CM-3, SA-11) and two that its SOC 2 report will need (AC-3, CP-10).

## 2. Controls selected
**36 control assessments** (33 distinct controls; AC-3, CM-3, and SC-7 were assessed in two scopes), **256 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-6(5), IA-2(1) | 28 | Every division's IT access; GR-02, GR-18 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR; training platform) | PS-3, PS-4, AT-2 | 18 | Personnel risk assessments for CIP access; terminations; training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC; General Counsel) | SI-4, AU-6, IR-3, IR-4, IR-6, IR-8, RA-5 | 57 | GR-04, HY-006; scenario gaps 2 and 8 | Focused / Comprehensive |
| Common control (SYS-G3 cloud; group procurement) | CP-9, SC-7, SR-6 | 13 | GR-02, GR-08; immutable backups and guardrails | Focused / Focused |
| HPCDMS (Hydro, P02 system) | AC-4, AC-17, AC-20, CM-3, CM-8, CP-4, IA-5, MA-4, SC-7, SI-2 | 63 | GR-01, GR-03, HY-001, HY-004, HY-005, HY-018; scenario gaps 1 to 4 | Comprehensive / Comprehensive (HOC-A, DEV-02, DEV-05, and records for all 41 plants) |
| Division sample: Constructors (FPE and jobsites) | AC-3, AT-3, PE-3, PL-1, SI-3 | 47 | CN-001, CN-002, CN-003; gaps 5 and 7 | Focused / Focused (20 USACE folders; 2 jobsites; 10 kits) |
| Division sample: Engineering (DSMS) | AC-3, CA-3, CM-3, CP-10, SA-11 | 30 | GR-03, GR-05, EN-003; gaps 3 and 6 | Focused / Focused |
| **Total** | **36** | **256** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration; OT remote access standard and Intermediate System configuration; firewall rule sets at the HOC ESPs and 6 plant gateways; the Section 9 asset inventory; change records (Hydro and Constructors) for 2 rehabilitation sites; the failover test report and CIP-009 lessons learned; SOC use cases and sensor coverage; the notification matrix draft; the Constructors supplement; FPE SSP, DLP, and folder permissions; DSMS threshold change history, release pipeline, and model validation records; supplier assessments and the OEM contract.
- **Interview:** the Group CISO; the group identity, SOC, and cloud platform directors; the Senior Vice President, Hydro Operations; the Director, OT Security; the HOC Managers; the Chief Dam Safety Engineer; the NERC Compliance Director; the Federal Programs Compliance Director; 2 Constructors project managers and 4 commissioning engineers; the DSMS General Manager and the Director of Data Science; the General Counsel.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations including craft workers;
  - a phishing-resistant administrator sign-in and a privileged checkout in PAM;
  - a passive test laptop placed on the DEV-02 plant control network for 2 hours, with HOC approval, to test detection;
  - password checks on 30 field devices at DEV-02 and DEV-05;
  - network discovery at DEV-05 and inspection and imaging of the DEV-05 commissioning kit (removed 2026-07-16);
  - a traffic capture on the DSMS replication link at DEV-02;
  - restores of 2 DSMS datasets and 1 FPE share from the immutable vault;
  - cross-tenant access attempts in DSMS test tenants;
  - a walkthrough of 2 jobsite trailers that print CUI drawings.

## 4. Rules of engagement
- **No test may move a gate, change a unit setpoint, or load anything onto a controller.** All OT tests were passive and approved by the HOC shift supervisor, with the plant in a stable state and no flood operations under way.
- No active scanning of plant control networks; discovery at DEV-05 used passive capture and the controllers' own diagnostic pages under engineer supervision.
- No CUI or client CEII left its approved system; evidence screenshots were redacted and stored in the restricted library as BCSI or CEII.
- The assessor would stop and notify the Group CISO and the Senior Vice President, Hydro Operations on any finding of active compromise or immediate danger. The DEV-05 commissioning kit (found 2026-07-15) triggered this rule: it was disconnected the same day and the interim rule issued on 2026-07-16. Forensic review of its image found no sign of malicious use.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 103 | 13 | 116 |
| HPCDMS (Hydro, P02 system) | 42 | 21 | 63 |
| Division sample: Constructors | 33 | 14 | 47 |
| Division sample: Engineering | 17 | 13 | 30 |
| **Total** | **195** | **61** | **256** |

Of the 61 statements other than satisfied, 40 are rated High and 21 Moderate.

**Common controls are mostly strong.** 103 of 116 common statements were satisfied. Privileged access (AC-6(5)), MFA (IA-2(1)), screening (PS-3), training (AT-2), log review (AU-6), cloud backups (CP-9), and landing zone boundaries (SC-7) had no findings. The common findings are about **craft worker terminations** (AC-2), **OT monitoring coverage below the HOCs** (SI-4) and **overdue plant vulnerability assessments** (RA-5), **cross-division incident handling and notification** (IR-3, IR-4, IR-6, IR-8; scenario gap 8), and **supplier assessments** (SR-6).

**The HPCDMS is where the top risk shows.** 21 of 63 statements failed, and they trace to two causes:
- **Construction connectivity (gap 1):** AC-17, AC-20, MA-4, CM-3, IA-5, and SC-7 findings all describe the DEV-05 commissioning kit, which connected the gate control network to a cellular network for 41 days, with a remote support tool, a default router password, and no Hydro authorization.
- **Scale below the HOC (gaps 2 to 4):** the two-way DSMS path (AC-4), unmonitored plant interfaces (SC-7), unsupported hosts and old firmware (SI-2), an incomplete inventory (CM-8), and a failover that missed its RTO (CP-4).
The HOC Electronic Security Perimeters and Intermediate Systems themselves passed every applicable statement.

**Division samples:**
- *Constructors:* CUI on the commercial project platform (AC-3), untrained federal project teams (AT-3), trailers that print CUI drawings without physical controls (PE-3; these correspond to CMMC requirements that cannot be placed on a POA&M), commissioning kits without malicious code protection (SI-3), and a 2023 supplement that conflicts with group policy and DFARS (PL-1).
- *Engineering:* no agreement for the Hydro data exchange (CA-3), no change control or testing for alert thresholds and AI-001 models (CM-3, SA-11). Tenant isolation (AC-3) and recovery (CP-10) passed.

**Controls fully other than satisfied** (every statement failed): IR-3 and SR-6 (common), AC-4 (HPCDMS), and AC-3 (Constructors). Each has only one determination statement.

27 of the 36 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **26 items**: 18 from this assessment and 8 from the P03 gap analyses, the P02 SSP, and the P10 decision (POAM-010, POAM-011, POAM-015, POAM-016, and POAM-023 to POAM-026). By risk: 13 High and 13 Moderate. Status: 21 In progress, 5 Open. Each item names the related P01 risks.

The **FERC plan and schedule** for negative Form 3 answers (Rev. 3A 9.1.1.3) is this POA&M filtered to the Section 9 items (POAM-001, POAM-003 to POAM-008, POAM-010, POAM-011, POAM-019, POAM-020, POAM-024). The **SERC mitigation plan** for the CIP-003-9 Attachment 1 Sections 3, 5, and 6 gap is POAM-001 with POAM-002. The **CMMC remediation plan** is POAM-014, POAM-021, POAM-022, and POAM-023.

## 7. Deliverables and acceptance
`assessment-results.csv` (256 rows, with an `assessment_scope` column), `poam.csv` (26 items), and this plan and summary. Results were presented to the board audit committee and the safety, risk, and reliability committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-10. Division presidents accepted their division findings the same week.
