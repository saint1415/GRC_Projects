# Risk Register Report: Cris Santos Company Holdings | Chemical | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Chemical manufacturing, Wholesale Trade, Transportation and Warehousing) |
| Focus division | Specialty Chemicals (NAICS 325998), with Plant C1 (RMP Program 3 chlorine process) in detail |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also supports | The USCG Cybersecurity Assessment for Terminal T1 (33 CFR 101.650(e)(1), due 2027-07-16; P03), the transportation security risk assessments in the three hazmat security plans (49 CFR 172.802(a)), and the RMP process hazard analyses where cyber causes are added (40 CFR 68.67) |
| Registers | `risk-register.csv` (group), `risk-register-specialty-chemicals.csv`, `risk-register-distribution.csv`, `risk-register-hazmat-transport.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads and the Group Process Safety Director |
| Approved | 2026-09-17 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system in the three divisions that controls a chemical process, stores or moves hazardous materials, produces shipping papers, or holds sensitive data, plus the corporate shared services they depend on: SYS-G1 (identity and the OT remote access gateway), SYS-G2 (SOC and OT desk), SYS-G3 (cloud and WAN), SYS-G4 (ERP), and SYS-G6 and SYS-G7. Division systems are SYS-C1 to SYS-C9, SYS-D1 to SYS-D4, and SYS-T1 to SYS-T4 (`../00_company-facts.md` sections 3 and 7).

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. Specialty Chemicals, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not copied from the highest division rating.

**Safety consequences set the impact scale.** For OT risks, impact was rated on the worst credible physical consequence with the existing safeguards, as the PHA would, not on the IT asset. A manipulated chlorine feed setpoint is Very High impact even though the SIS lowers the likelihood that the attack causes harm. That is why several OT risks show Moderate likelihood of adverse impact and still rate High.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Process safety and public safety risks rated High must be treated, not accepted.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the BIAs (P05), the gap analyses (P03), the common control assessment and OT tests (P07), the Plant C1 PHA (2024) and RMP compliance audit (2025-05-14), and interviews with plant, terminal, and fleet leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05), including the safety category.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 6 | 10 | 2 | 0 | 18 | n/a |
| Specialty Chemicals | 0 | 6 | 11 | 11 | 0 | 28 | 17 |
| Distribution | 0 | 2 | 10 | 6 | 0 | 18 | 10 |
| Hazmat Transport | 0 | 2 | 8 | 6 | 0 | 16 | 9 |
| **All registers** | **0** | **16** | **39** | **25** | **0** | **80** | **36** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Stolen or shared integrator credential on the OT remote access gateway reaches control systems at several plants and Terminal T1 | SC-001, SC-002, SC-006, DS-002 | Named integrator accounts; per-session site approval; recording at all sites; remove standing hub connections | Group OT Security Director | 2027-03-31 |
| GR-02 | Cyber-initiated loss of control causes a toxic release or fire at an RMP-covered plant | SC-001, SC-003, SC-008, SC-009 | Cyber causes in PHA revalidations; all DCS, SIS, and recipe changes through plant MOC | Group Process Safety Director | 2027-06-30 |
| GR-03 | ERP ransomware stops order release and hazmat shipping papers in all three divisions | HT-004, DS-009 | Segment ERP integration; extend the shipping paper fallback; cross-division tabletop | Group ERP director | 2027-03-31 |
| GR-04 | AI changes process setpoints without MOC, safety review, or governance | SC-007, SC-022, HT-006 | Group AI Standard change gate; AI-001 conditions (P10) | Group Chief Risk Officer | 2026-12-31 |
| GR-05 | Ransomware spreads through flat networks at the 7 legacy plants | SC-004, SC-005, SC-006, SC-014 | OT standard migration by 2027-12-31; remove always-on tools now | Specialty Chemicals Vice President of Manufacturing Technology | 2027-12-31 |
| GR-08 | Telemetry vendor portal compromise disrupts deliveries to water utilities | DS-006, DS-007 | MFA on the portal; two approvers for firmware; daily reconciliation for utilities | Distribution managed inventory service director | 2026-12-31 |

### Specialty Chemicals (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| SC-001 | Intruder on a gateway session to the Plant C1 EWS changes reactor alarm limits and a chlorine feed setpoint | Shift superintendent phone approval now; named accounts and per-session approval; DCS journal to the SIEM | Plant C1 Controls Engineering Manager | 2027-03-31 |
| SC-002 | Central engineering hub compromise pushes malicious logic or recipes to many plants | Remove standing connections; staging share and plant MOC for every push | Specialty Chemicals Director of Process Control Engineering | 2027-03-31 |
| SC-003 | A cyber-initiated deviation defeats safeguards the PHA treats as independent | Add control system compromise as a PHA cause; check credited safeguards for common failure with the DCS | Plant C1 Process Safety Manager | 2027-06-30 |
| SC-005 | Malware moves into legacy plant control systems through flat networks | OT standard migration | Specialty Chemicals Vice President of Manufacturing Technology | 2027-12-31 |
| SC-006 | Always-on integrator remote desktop tools at two legacy plants | Remove the tools; move integrators to the gateway | Specialty Chemicals Vice President of Manufacturing Technology | 2026-11-30 |
| SC-007 | AI-001 writes a setpoint that drives a hypochlorite reactor toward an unsafe condition | Remove the write rule; MOC and AI council review before any automatic mode | Specialty Chemicals Process Engineering Director | 2026-12-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| DS-001 | Distribution | Attacker on the Terminal T1 office network changes tank gauging or loading rack logic | Distribution Cybersecurity Officer (CySO) for Terminal T1 | 2027-03-31 |
| DS-006 | Distribution | Telemetry vendor portal without MFA is used to push bad configuration to customer gateways | Distribution managed inventory service director | 2026-12-31 |
| HT-001 | Hazmat Transport | Attacker in dispatch changes routes or consignees to divert hazmat loads | Hazmat Transport dispatch director | 2026-12-31 |
| HT-004 | Hazmat Transport | Ransomware stops electronic shipping papers and dispatch | Hazmat Transport dispatch director | 2027-03-31 |

### What the results say
The program has a mature core: a 24x7 SOC with an OT desk, PAM, an OT security standard at 9 plants and Terminal T1, independent SIS on every RMP-covered process, and immutable backups. There are no Very High risks. The High risks cluster around **what connects the divisions and the plants**, not around any one site's basics:
1. **Shared paths into OT** (GR-01, GR-05). The gateway and the engineering hub reach every plant. A single weakness (shared integrator accounts, standing connections) repeats at 17 sites (scenario gap 1). The 7 legacy plants add flat networks and always-on remote tools (gap 2).
2. **Process safety does not yet see cyber** (GR-02, GR-04). PHAs do not treat control system compromise as a cause, recipe pushes skip the plant MOC screen (gap 3), and an AI model wrote setpoints for three months without MOC (gap 9).
3. **Shared IT drives every division's hazmat shipping** (GR-03). One ERP outage stops shipping papers for all three divisions.
4. **Customers' public health depends on a vendor portal** (GR-08; gap 6).

Terminal T1's USCG gaps (GR-06, gap 4) are Moderate at group level because the rule's main deadlines are in 2027 and the terminal already has a Facility Security Plan and OT monitoring. The overdue contractor training is the exception and is treated first (POAM-010). Governance gaps 7 and 10 (Hazmat Transport inheritance and supplement drift) are Moderate (GR-09, GR-10). They matter because they hide whether Hazmat Transport controls actually operate, which is why P07 sampled Hazmat Transport on governance controls.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q4):** gateway redesign (GR-01); legacy plant migration (GR-05); ERP segmentation and shipping paper fallback (GR-03); Terminal T1 USCG compliance (GR-06); group AI governance (GR-04).
- **Process safety actions (not acceptable to defer):** cyber causes in PHA revalidations and MOC coverage of DCS, SIS, and recipe changes at every plant (GR-02, SC-003, SC-008).
- **Accepted (7, all Low):** GR-16 (ERC outage, covered by a tested backup site), SC-015 (unauthenticated controller protocols until the 2027 DCS upgrade), SC-017 (LIMS outage), DS-015 (portal business contact data), DS-017 (no ship-to-shore connection), HT-010 (tablet loss, remote wipe), HT-015 (fuel card fraud).
- **Treatment status:** 51 risks are In progress, 22 are Open (treatment approved, work not started), and 7 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The six High group risks were presented on 2026-09-17. Process safety and cyber are reported together because GR-02 and GR-04 are both. The Reg S-K Item 106 description in the next annual report draws on the governance described here (the board risk committee's oversight and the Group CISO's reporting line).

## 6. Approval
- Board risk committee: approved the group register, the six High group treatment plans, and the funding request, 2026-09-17.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the ten High division risks, 2026-09-17. The Plant C1 Plant Manager, as RMP qualified person, confirmed the interim measures for SC-001, SC-003, and SC-007.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-17.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
