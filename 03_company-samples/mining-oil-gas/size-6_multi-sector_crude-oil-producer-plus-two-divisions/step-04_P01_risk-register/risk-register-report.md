# Risk Register Report: Cris Santos Company Holdings | Mining, Quarrying, and Oil and Gas Extraction | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; sectors 21, 22, and 48-49) |
| Focus division | Crude Oil Production (NAICS 211120) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1; OT risk framing per NIST SP 800-82 Rev. 3 section 4 |
| Registers | `risk-register.csv` (group), `risk-register-crude-oil-production.csv`, `risk-register-power-generation.csv`, `risk-register-crude-logistics.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads and the Group OT Security Director |
| Approved | 2026-09-17 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** The corporate shared services (SYS-G1 to SYS-G6) and every division system in `../00_company-facts.md` section 3: the Production field SCADA, field devices, accounting, and legacy Mid-Continent SCADA (SYS-P1 to SYS-P6); the Power Generation plant control systems, Generation Control Center, and market systems (SYS-E1 to SYS-E3); and the Crude Logistics pipeline SCADA, measurement, shipper platform, and fleet systems (SYS-M1 to SYS-M4).

**OT changes what "impact" means.** In these divisions the worst outcomes are physical: an uncontrolled release, H2S exposure, an overpressured pipeline, or a tripped unit during a grid emergency. Impact ratings therefore weigh safety and environmental harm first, then reliability obligations, then money (P05 section 3). Hardwired shutdowns and relief systems that act without SCADA are treated as existing controls that cap the worst case; they do not lower the likelihood of an attack.

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. Each division security and compliance lead maintains one. Crude Oil Production, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not copied from the highest division rating.

**Risk tolerance and who can accept risk** (recorded in `../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Safety and environmental risks rated High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), OT threat advisories tracked by the SOC OT desk, and interviews with each division's operations and compliance leaders.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA categories (P05). Group impact reflects enterprise consequences: harm in more than one division, several regulators at once, and SEC disclosure.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads proposed roll-ups. The Group Chief Risk Officer decided which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 6 | 9 | 1 | 0 | 16 | n/a |
| Crude Oil Production (`risk-register-crude-oil-production.csv`) | 0 | 4 | 15 | 5 | 0 | 24 | 11 |
| Power Generation (`risk-register-power-generation.csv`) | 0 | 2 | 5 | 5 | 0 | 12 | 8 |
| Crude Logistics (`risk-register-crude-logistics.csv`) | 0 | 2 | 11 | 1 | 0 | 14 | 6 |
| **All registers** | **0** | **14** | **40** | **12** | **0** | **66** | **25** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Attacker uses the group data platform historian connector to move from corporate IT into the OT DMZs of all three divisions and write to historian brokers | PD-007; PG-004; ML-001 | Replace the shared account with one read-only account per division; push historian data outward from each OT DMZ (no inbound pull); write an interconnection agreement per division | Group data platform director | 2027-03-31 |
| GR-02 | Attacker who compromises a corporate virtual desktop reaches the shared OT support jump servers and from them the OT DMZs of all three divisions | PD-001; PG-004; ML-001 | Split the jump servers by division; reach them only from hardened privileged access workstations; remove routes from the virtual desktop pool | Group OT Security Director | 2026-12-31 |
| GR-03 | Ransomware that starts with a phished corporate user encrypts shared business systems in all divisions and steals personal data before encryption | PD-002; PD-021; PG-004; ML-006 | Cross-division ransomware tabletop with the notification matrix (P08); block lateral paths into OT (GR-01, GR-02); remove owner exports from file shares (GR-10) | Group CISO | 2027-03-31 |
| GR-05 | AI models change physical operations or decisions about people without safety review or approval | PD-009; PG-007; ML-008 | Inventory every AI use case; council approval before any model acts on equipment; safety management of change for models that write setpoints; human review of camera scores (P10) | Group Chief Risk Officer | 2026-12-31 |
| GR-10 | Royalty owner and employee personal data is stolen from shared corporate storage | PD-010 | Stop exports to file shares; deliver owner decks through SYS-P3 reports only; data loss prevention on taxpayer and bank numbers | Production Accounting Vice President | 2026-12-31 |
| GR-13 | A nation-state actor pre-positions in OT networks using legitimate tools and waits for a crisis to disrupt operations | PD-001; PD-003; PD-007; PD-014; ML-001 | Extend OT sensors to SYS-P5 and all plants; threat hunts in OT twice a year; complete OT asset inventory | Group OT Security Director | 2027-06-30 |

### Crude Oil Production (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| PD-001 | Attacker uses the integrator's always-on remote access to the Mid-Continent legacy SCADA and issues unauthorized commands | Disable the always-on path; integrator access only through group PAM with named accounts; segment the field offices; forward logs to the SIEM (POAM-012) | Production Vice President of Operations Technology | 2026-12-31 |
| PD-002 | Ransomware encrypts the Mid-Continent legacy SCADA servers and HMIs | Offline and immutable copies of SYS-P5 images; quarterly restore test; accelerate migration to SYS-P1 (due 2027-09-30) | Mid-Continent operations manager | 2027-03-31 |
| PD-007 | Attacker exploits a known exploited vulnerability on an OT DMZ server or SCADA server | Clear the backlog; monthly OT patch window for DMZ servers; compensating rules where patching must wait (POAM-004) | Group OT Security Director | 2026-12-31 |
| PD-009 | The predictive maintenance model lowers rod pump speeds wrongly or acts on bad data, causing equipment damage, lost production, or unsafe conditions | Return the model to advisory mode; safety management of change and council approval before any automatic action (P10; POAM-021) | Production Vice President of Operations Technology | 2026-12-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Treatment | Owner | Due |
|---|---|---|---|---|---|
| PG-001 | Power Generation | Attacker uses the turbine vendor's standing remote access path at Plant P3 to reach the turbine control system | Move vendor access to group PAM with session approval; OT sensor rules for vendor sessions; self-report and mitigation plan (POAM-013) | Power Generation CIP Senior Manager | 2026-12-31 |
| PG-004 | Power Generation | Ransomware in corporate IT forces the GCC and plants to isolate from corporate networks, or reaches their OT DMZs | Division-only jump servers and read-only historian push (GR-01, GR-02); isolation drill with the market operator | Power Generation security and compliance lead | 2027-03-31 |
| ML-001 | Crude Logistics | Attacker manipulates pipeline SCADA to change pressures or valve positions on the trunk line | Division-only access paths (GR-01, GR-02); SCADA manipulation as an abnormal operating condition in controller training (ML-003) | Pipeline Control Center Manager | 2027-03-31 |
| ML-002 | Crude Logistics | The backup PCC does not work when the main PCC is lost | Test the backup SCADA system by 2026-10-31 and then every calendar year within 15 months (POAM-015) | Pipeline Control Center Manager | 2026-10-31 |

### What the results say
There are no Very High risks. Each division's own basics are mostly in place: a 24x7 SOC with an OT desk, PAM with MFA, immutable cloud backups, a clean NERC CIP audit, and written control room procedures. The High risks cluster in three places:
1. **The seams between shared IT and division OT** (GR-01, GR-02, GR-13, PG-004, ML-001). Two shared paths, the data platform historian connector and the shared OT jump servers, reach all three divisions' OT DMZs (scenario gap 1). One compromised corporate identity could touch field SCADA, the Generation Control Center, and the Pipeline Control Center. This is the top group risk and the subject of the P08 runbook.
2. **Legacy and acquired OT** (PD-001, PD-002, PD-007, GR-16). The Mid-Continent legacy SCADA carries about 22% of production with always-on integrator access, no logging, and untested backups (scenario gap 2).
3. **Rules that apply to only one division** (PG-001, ML-002). Plant P3's vendor remote access does not meet CIP-003-9 Attachment 1 Section 6.3 (gap 3), and the backup PCC test is past the 195.446(c)(4) interval (gap 4). Both are compliance failures as well as security risks, so their treatment dates are the earliest in the register.

AI governance (GR-05, PD-009) is High because the predictive maintenance model was already changing rod pump speeds in the field before anyone reviewed it (scenario gap 8). Royalty owner data on file shares (GR-10) is High because about 190,000 owners in all 50 states would need notices.

Governance gaps 6, 7, and 9 (inheritance, the unexercised notification matrix, and the stale Crude Logistics supplement) are Moderate (GR-04, GR-06, GR-07). They matter because they hide whether Crude Logistics controls actually operate, which is why P07 sampled Crude Logistics most heavily.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** split the shared OT jump servers by division and replace the historian connector with one-way, read-only pushes (GR-01, GR-02); extend OT monitoring to the Mid-Continent fields and all plants (GR-13); accelerate the Mid-Continent SCADA migration (PD-001, PD-002); group AI governance program (GR-05); remove royalty owner exports from file shares (GR-10).
- **Compliance-driven treatments:** Plant P3 vendor access and the self-report decision (PG-001, PG-006; see P03); backup PCC test by 2026-10-31 (ML-002); controller training and point-to-point verification (ML-003, ML-004); hazmat security plan cyber update (ML-007).
- **Accepted (all Low):** PD-018 (someone tampers with an RTU or controller at a remote well p...), PD-023 (a hurricane disables the Florida control room and field comm...), PG-008 (an unauthorized person enters a plant control room...). Each was accepted by the division security and compliance lead under the tolerance table.
- **Treatment status:** 38 risks are In progress, 25 are Open (treatment approved, work not started), and 3 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The six High group risks were presented on 2026-09-17. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here: the board risk committee's oversight, the Group CISO's reporting line, and the use of internal audit to assess common controls.

## 6. Approval
- Board risk committee: approved the group register, the six High group treatment plans, and the funding request, 2026-09-17.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the eight High division risks, 2026-09-17.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-17.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
