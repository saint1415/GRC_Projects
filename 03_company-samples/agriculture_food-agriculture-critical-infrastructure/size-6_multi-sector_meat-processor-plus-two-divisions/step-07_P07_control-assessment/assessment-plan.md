# Security Assessment Plan and Summary: Cris Santos Company Holdings | Food and Agriculture | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, SYS-G5, SYS-G6, group HR), the PPCM (P02 SSP system), and samples of Meat Processing, Food Distribution, and Grocery Retail controls |
| Tier / Vertical | Multi-Sector / Food and Agriculture (focus division: Meat Processing) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`), with NIST SP 800-82 Rev. 3 rules for testing OT safely |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. An OT specialist from the group's assurance firm joined for plant testing. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 (OT testing at Plants 2, 5, and 6 during weekend sanitation windows, 2026-08-08 to 2026-08-23) |
| Also supports | Verification evidence for the Plant 6 food defense plan (21 CFR 121.150) and the Grocery Retail PCI DSS program; it does not replace the QSA's ROC |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three divisions and corporate, and the termination sample included agency workers).
2. **The PPCM's** system-specific controls were assessed because it is the SSP system and carries the group's food defense risk (GR-09). Plants 2 and 5 were tested in depth because they sit below the OT reference architecture; Plant 6 was tested because it is the FDA-registered plant.
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Food Distribution was sampled on governance controls (PL-1, CA-2) because its inheritance is undocumented and its standards have drifted (scenario gap 7). Grocery Retail was sampled on the controls its 2026 PCI DSS testing flagged, so that group internal audit could confirm the findings independently of the QSA.

## 2. Controls selected
**39 control assessments** (33 distinct controls; SC-7 was assessed in three scopes, and CP-9, SA-9, and CM-8 in two), **290 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2(1), IA-5 | 42 | Every division's access; GR-01 (privileged service accounts) | Focused / Comprehensive (all divisions sampled; OT credential tests at three plants) |
| Common control (Group HR with SYS-G1; Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users including agency workers | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-4, IR-6, IR-8, RA-5 | 53 | GR-01, GR-03, GR-15; scenario gap 6 | Focused / Comprehensive |
| Common control (SYS-G3 cloud and colocation) | CP-9, SC-7, SC-28, CM-6 | 19 | Immutable backups and guardrails that every division inherits | Focused / Focused |
| Common control (SYS-G5 OT security services) | AC-17, MA-4 | 12 | GR-12 (High); scenario gap 1 | Comprehensive / Comprehensive (every remote path at every plant and DC) |
| Common control (SYS-G6 cold-chain platform) | CP-4, SA-9 | 11 | GR-02 (High); scenario gap 2 | Focused / Focused |
| PPCM (system-specific) | AC-3, IA-2, AU-9, AU-12, CM-3, CM-8, SC-7, CP-9 | 36 | GR-09 (High); scenario gaps 1, 3, and 4 | Comprehensive / Comprehensive at Plants 2, 5, and 6 |
| Division sample: Meat Processing | SI-2, CP-2, SA-9, AT-3 | 49 | MT-006, MT-010, MT-014; contingency for a multi-plant outage | Focused / Focused (all six plans; three plants on site) |
| Division sample: Food Distribution | PL-1, CA-2, CP-9, AU-11 | 35 | Gap 7; FD-001, FD-007, FD-008, FD-011 | Focused / Focused (DC-1 and DC-3) |
| Division sample: Grocery Retail | SC-7, SI-7, CM-8 | 18 | RT-001, RT-002, RT-003 (two High) | Focused / Focused (2 stores re-tested; 40 stores' inspection records) |
| **Total** | **39** | **290** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, SIEM data sources and OT monitoring coverage, landing-zone policies, backup settings, SYS-G5 configuration and the remote path inventory, the cold-chain DR runbook and vendor file, HMI and MES account lists, historian and SYS-M5 audit settings, OT change records, inventories, contingency plans, supplier contracts, division standards, store network templates, payment page script inventory, and POI device records.
- **Interview:** group identity, SOC, infrastructure, and OT security directors; the group cold-chain services manager; plant managers, FSQA managers, and controls engineers at Plants 2, 5, and 6; the integrator and refrigeration contractor; DC general managers; the Food Distribution and Grocery Retail security and compliance leads; the digital commerce director.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions and a termination sample of 25 (8 agency workers);
  - hardware-key administrator sign-in and federation checks on 45 applications;
  - credential tests on 60 OT devices at Plants 2, 5, and 6 (read-only checks of web and HMI sign-in pages, during sanitation windows);
  - a simulated remote connection over the Plant 5 integrator VPN, with SOC approval, to test detection;
  - test sign-ins on HMIs and MES at Plants 2, 5, and 6;
  - a walkdown of two production lines at Plant 2 against the inventory;
  - a traffic capture between business and control networks at Plants 2, 5, and 6;
  - restores of a SCADA server image at Plant 6 and of three cloud datasets from the provider B vault;
  - segmentation re-tests in 2 stores of the affected design.

## 4. Rules of engagement
- **Safety first in OT.** No active scanning of PLCs or HMIs; no changes to setpoints or logic; testing only while lines were down for sanitation, with the plant controls engineer and the refrigeration manager present. Refrigeration controllers were observed, never operated.
- **Food safety.** Any test that could affect product or CCP monitoring needed prior FSQA approval. None affected product.
- **No card data or personal data left group systems.** Screenshots were redacted.
- **Stop rule.** The assessor would stop and notify the Group CISO on any critical exposure. One was found: default passwords on OT devices (IA-05e.). The Plant 2 HMI passwords were changed the next day; the Plant 5 controller password needed the refrigeration contractor and was changed by 2026-09-30 (POAM-027).

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 127 | 25 | 152 |
| PPCM | 21 | 15 | 36 |
| Division sample: Meat Processing | 38 | 11 | 49 |
| Division sample: Food Distribution | 26 | 9 | 35 |
| Division sample: Grocery Retail | 13 | 5 | 18 |
| **Total** | **225** | **65** | **290** |

**Common controls are mostly strong.** 127 of 152 common statements were satisfied. Cloud protection (CP-9, SC-7, SC-28, CM-6 in SYS-G3), privileged access (AC-6(5), IA-2(1)), automatic disabling (AC-2(3)), and terminations (PS-4) had no findings. The common findings sit in four places: **privileged service accounts** in the directory (AC-2, IA-5), **OT coverage** of the SOC and the OT gateway at the acquired plants (SI-4, RA-5, AC-17, MA-4), **the cold-chain platform** (CP-4 failover never tested; SA-9 vendor assurance lapsed), and **cross-division incident handling and notification** (IR-4, IR-6, IR-8, scenario gap 6).

**The PPCM is where the food safety risk is.** 15 of 36 statements were other than satisfied, all traceable to Plants 2 and 5 or to shared HMI logins, plus the Plant 6 change that skipped a food defense check (CM-03b.[02]). The traffic capture confirmed that business and control traffic at Plants 2 and 5 is neither controlled nor monitored (SC-7).

**One Very High finding.** Manufacturer default passwords on 3 packaging HMIs at Plant 2 and on the Plant 5 refrigeration controller (IA-05e.; P01 MT-030; POAM-027).

**Division samples:**
- *Meat Processing:* unsupported HMIs and late patches at Plants 2 and 5 (SI-2), contingency plans that assume a single-plant outage (CP-2), OT suppliers without security terms (SA-9), and engineers given OT access before training (AT-3).
- *Food Distribution:* drifted standards (PL-1) and no inheritance matrix (CA-2), both scenario gap 7; untested DC automation backups (CP-9); 30-day log retention (AU-11).
- *Grocery Retail:* the store Wi-Fi management path to POS lanes (SC-7), payment page integrity (SI-7), and POI inventory gaps (CM-8). These confirm the division's own PCI DSS findings; the rest of its control set was not re-tested.

**Controls fully other than satisfied** (every statement failed): AC-3 and AU-9 (PPCM) and AU-11 (Food Distribution). AC-3 and AU-11 each have only one determination statement; AU-9 has two.

31 of the 39 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **28 items**: 24 from this assessment (POAM-020 and POAM-021 also trace to P03 PCI DSS gaps), 3 from the P03 gap analysis (POAM-023 to POAM-025), and 1 from the P10 AI risk assessment (POAM-026). By risk: 1 Very High (POAM-027 default OT passwords), 9 High (POAM-001 to POAM-005, POAM-007, POAM-009, POAM-020, POAM-023), and 18 Moderate. Status: 19 In progress, 9 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (290 rows, with an `assessment_scope` column), `poam.csv` (28 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-15, with the Group Chief Food Safety and Quality Officer concurring on the PPCM findings. Division presidents accepted their division findings the same week.
