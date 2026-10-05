# Risk Register Report: Cris Santos Company Holdings | Utilities | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded utility holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Utilities, Mining, Quarrying, and Oil and Gas Extraction, and Professional Services) |
| Focus division | Electric Utility (NAICS 221122), a NERC-registered DP, TO, and TOP |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Registers | `risk-register.csv` (group), `risk-register-electric-utility.csv`, `risk-register-gas-production.csv`, `risk-register-engineering-services.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-15 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** All systems of the three divisions and the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and data platform, SYS-G4 OT secure remote access, and SYS-G5 ERP and HR. Division systems are SYS-E1 to SYS-E6, SYS-N1 and SYS-N2, and SYS-S1 and SYS-S2 (`../00_company-facts.md` section 3). OT risks are rated on safety and reliability consequences, not only on data loss.

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. The Electric Utility, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact; they are not simply the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

High risks to public or crew safety may not be accepted; they must be treated. Potential NERC noncompliance is never accepted; it is self-reported and mitigated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), E-ISAC and CISA advisories on energy-sector threats, and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). For the Electric Utility, impacts on public and crew safety and on BES reliability drive Very High ratings. Group impact reflects enterprise consequences: several regulators at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads proposed roll-ups. The Group Chief Risk Officer decided which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results
| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 6 | 12 | 2 | 0 | 20 | n/a |
| Electric Utility | 0 | 6 | 12 | 12 | 0 | 30 | 21 |
| Gas Production | 0 | 2 | 9 | 7 | 0 | 18 | 11 |
| Engineering Services | 0 | 2 | 9 | 7 | 0 | 18 | 10 |
| **All registers** | **0** | **16** | **42** | **28** | **0** | **86** | **42** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Attacker uses the shared OT remote access platform (SYS-G4) to reach the DOP, transmission substations, and the Gas Production POC | EU-001, GP-002, GP-016, ES-003 | Remove standing access; per-session approval by each OT owner; separate entitlements per environment; detection on every vendor and engineer session | Group OT security director | 2027-03-31 |
| GR-02 | Destructive or manipulative attack on the DOP opens feeders and slows restoration | EU-002, EU-003, EU-006, EU-007 | Firewall rebuild; DCC network sensors; offline DOP backups with a full restore test; console replacement | Electric Utility distribution operations director | 2027-06-30 |
| GR-03 | A cross-division incident is reported late or inconsistently (NERC, E-ISAC, CISA, DOE, clients, states, SEC) | EU-010, GP-018, ES-006 | Complete the matrix; cross-division tabletop; DCC reporting checklist; client notice register | Group General Counsel | 2026-12-15 |
| GR-06 | Client CEII and BCSI at Engineering Services exposed, including the Electric Utility's own BCSI | ES-001, EU-008 | Per-project restricted folders with client-approved access; block personal storage; bring Electric Utility BCSI into its CIP-004 R6 program | Engineering Services security and compliance lead | 2026-12-31 |
| GR-07 | Compromised vendor software or firmware reaches OT in several divisions | EU-009, GP-008 | Extend CIP-013-style integrity and vendor notice processes to the DOP and field SCADA; group OT vendor tiering | Group procurement director | 2027-03-31 |
| GR-14 | Major hurricane damages control centers and IT during grid restoration | EU-018 | Hot standby at the backup DCC; satellite communications | Electric Utility distribution operations director | 2027-05-31 |

### Electric Utility (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| EU-001 | Standing SYS-G4 access used to command the DOP or reach low impact substation gateways | Per-session DCC approval; remove standing access; detection on vendor sessions (POAM-001, POAM-013) | Electric Utility distribution operations director | 2027-03-31 |
| EU-002 | Undetected intruder in the DCC networks | DCC network sensors and DOP logs to the SIEM (POAM-003, POAM-008) | Group SOC director | 2027-03-31 |
| EU-003 | Pivot from the corporate network through broad firewall rules or DMZ bypasses | Rule review; deny by default; route OMS feeds through the DMZ (POAM-005) | Electric Utility OT engineering manager | 2026-12-31 |
| EU-006 | DOP cannot be restored within its RTO after a destructive attack | Offline immutable backups; full restore test twice a year (POAM-009) | Electric Utility OT engineering manager | 2026-12-31 |
| EU-007 | Unauthorized or erroneous switching command de-energizes feeders where crews are working | Tag-change integrity alerts; quarterly interlock testing | Electric Utility distribution operations director | 2027-03-31 |
| EU-008 | Electric Utility BCSI on the Engineering Services platform accessed without authorization | Designated BCSI folders with authorized access lists; self-report (POAM-015) | Electric Utility NERC compliance director | 2026-11-30 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| GP-001 | Gas Production | Attacker reaches field SCADA through internet-exposed well pad modems | Gas Production SCADA and automation manager | 2026-12-31 |
| GP-002 | Gas Production | SYS-G4 standing access used to reach the POC | Gas Production SCADA and automation manager | 2026-12-31 |
| ES-001 | Engineering Services | Client CEII or BCSI on the project platform accessed without a need to know | Engineering Services security and compliance lead | 2026-12-31 |
| ES-003 | Engineering Services | Engineer credentials stolen and used on SYS-G4 to reach client or affiliate OT | Engineering Services security and compliance lead | 2026-12-31 |

### What the results say
There are no Very High risks, and the Electric Utility's medium impact CIP program for the TCC carries no High risk at all. The High risks cluster around **what the group shares and where the CIP perimeter ends**:
1. **One remote access platform reaches three OT environments** (GR-01). The platform itself is well built; the entitlements on it are not (scenario gap 1).
2. **The DOP is the most consequential system outside CIP scope** (GR-02). It controls distribution for 2.4 million meters but has broad firewall rules, no internal monitoring, and untested restores (gap 2).
3. **An affiliate holds sensitive grid information** (GR-06). Engineering Services stores client CEII and the Electric Utility's own BCSI on a platform built for collaboration, not need-to-know (gap 5).
4. **Reporting duties stack up in an OT incident** (GR-03): CIP-008-6 and DOE-417 within an hour, EOP-004, client notices within 24 to 72 hours, state notices, and an SEC decision (gap 9).

Governance gaps 6 and 7 (Gas Production drift and undocumented inheritance) are Moderate at group level (GR-05). They matter because they hide whether Gas Production controls actually operate, which is why P07 sampled Gas Production governance controls.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** SYS-G4 entitlement redesign and vendor-session detection (GR-01); DOP firewall rebuild, DCC sensors, and offline backups (GR-02); project platform access model (GR-06); group OT vendor process (GR-07); backup DCC hot standby (GR-14).
- **Accepted (6 risks; 5 Low and 1 Moderate):** EU-019 (fuel interruption at supplying plants, covered by replacement purchases), EU-027 (single EMS vendor team), EU-029 (field network storm damage), GP-015 (field communications in floods, Moderate, accepted by the Gas Production president), ES-016 (single-region project platform), ES-017 (stolen encrypted laptop).
- **Regulatory actions:** self-report six potential CIP noncompliance rows (four issues) to SERC by 2026-09-30 with mitigation plans (GR-09; P03).
- **Contract actions:** OT security schedule in the intercompany agreement; client notice register at Engineering Services; group OT schedule at ADMS and SCADA integrator renewals.
- **Treatment status:** 52 risks are In progress, 28 are Open (treatment approved, work not started), and 6 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The six High group risks were presented on 2026-09-15. Grid reliability and public safety are separate enterprise risk categories, so GR-01, GR-02, and GR-14 also appear in the operational risk profile, not only the cyber profile. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight and the Group CISO's reporting line).

## 6. Approval
- Board risk committee: approved the group register, the six High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the ten High division risks and the temporary acceptance of GR-01 and GR-02 pending treatment (P02 authorization conditions), 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-16.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
