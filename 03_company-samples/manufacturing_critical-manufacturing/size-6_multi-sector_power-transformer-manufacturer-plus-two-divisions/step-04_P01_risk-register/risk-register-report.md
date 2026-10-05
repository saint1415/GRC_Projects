# Risk Register Report: Cris Santos Company Holdings | Critical Manufacturing | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Critical Manufacturing, Utilities, Professional Services) |
| Focus division | Transformer Manufacturing (NAICS 335311) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also supports | The Electric Utility's CIP-013-2 R1 supply chain risk assessment (vendor risks EU-003, EU-008, EU-010) and the voluntary benchmark outcomes ID.RA-05 and GV.RM in the gap analysis (P03) |
| Registers | `risk-register.csv` (group), `risk-register-manufacturing.csv`, `risk-register-electric-utility.csv`, `risk-register-engineering.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-15 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system and process in the group and division BIAs (P05): the corporate shared services (SYS-G1 to SYS-G6, including the GEPS), the 8 plants and their OT, the TMU product and FMS, the Electric Utility's control centers, substations, and customer systems, and Grid Engineering's project platform and field laptops (`../00_company-facts.md` section 3).

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. Each division security and compliance lead maintains one. Transformer Manufacturing, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact. They are not simply the highest division rating.

**Risk tolerance and who can accept risk** (recorded in `../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Risks rated High that could harm workers, crews, or the public (plant process safety, unsafe units on the grid, prolonged outages) may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the BIA (P05), the gap analyses (P03), the common control assessment (P07), CISA ICS advisories for transformer plant equipment, and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). Group impact reflects enterprise consequences: several plants or divisions at once, several regulators and customers, and SEC disclosure.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 10 | 2 | 0 | 16 | n/a |
| Transformer Manufacturing | 0 | 3 | 17 | 8 | 0 | 28 | 11 |
| Electric Utility | 0 | 2 | 9 | 3 | 0 | 14 | 9 |
| Grid Engineering | 0 | 2 | 7 | 3 | 0 | 12 | 7 |
| **All registers** | **0** | **11** | **43** | **16** | **0** | **70** | **27** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Ransomware spreads through shared IT services and halts production at all plants and the Electric Utility storm logistics | MF-001; MF-002; MF-003; MF-006; EU-004; ES-006 | Remove the P8 domain trust; P8 behind an OT DMZ; full GEPS restore test; cross-division ransomware tabletop (P08) | Group CISO | 2027-03-31 |
| GR-02 | GEPS integration hub compromise or failed recovery stops work order release to all 8 plants beyond the 48-hour MES buffer | MF-002; MF-004; EU-007 | One service account per plant with vaulted rotating keys; hub logs to the SIEM; full restore test in provider B | Group ERP platform director | 2027-03-31 |
| GR-04 | Tampered TMU firmware signed with a stolen key is distributed to utility substations, including the affiliate | MF-005; EU-010 | Move signing to a hardware security module with split control; isolate build servers; reproducible builds for the top 3 firmware lines | Chief product security officer | 2026-12-31 |
| GR-07 | An attacker moves from the acquired plant into corporate identity through the legacy domain trust | MF-001 | Break the trust; migrate P8 users to SYS-G1; EDR on all P8 servers | Group identity director | 2026-12-31 |

### Transformer Manufacturing (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| MF-001 | Ransomware spreads from IT into P8 plant OT through the dual-homed MES, the flat network, or the legacy domain trust and encrypts HMIs | OT DMZ and zoning at P8; remove dual-homing; EDR on P8 servers; OT sensors | Director of OT engineering | 2027-03-31 |
| MF-002 | Ransomware or outage stops GEPS scheduling for all 8 plants beyond the MES buffer | Full GEPS restore test; plant re-synchronization procedure; paper procedure at P8 | VP manufacturing operations | 2027-03-31 |
| MF-005 | Firmware signing key stolen from the build server and malicious TMU firmware signed and released | Hardware security module with split control; isolated build environment | Chief product security officer | 2026-12-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| EU-001 | Electric Utility | Malicious communications through vendor remote access to a low impact substation go undetected | Electric Utility NERC compliance director | 2026-12-31 |
| EU-007 | Electric Utility | Storm restoration delayed because the GEPS and the affiliate storm desk are down together | Electric Utility director of supply chain | 2027-05-31 |
| ES-001 | Grid Engineering | Client CEII or BCSI exposed through project-wide permissions or personal cloud storage | Grid Engineering project platform director | 2026-12-31 |
| ES-003 | Grid Engineering | Commissioning laptop carries malware into a client substation | Grid Engineering chief operating officer | 2026-12-31 |

### What the results say
The program is defined and mostly sound. There are no Very High risks: the 24x7 SOC, PAM, immutable backups, OT DMZs at 7 of 8 plants, and the Electric Utility's mature medium impact CIP program all hold. The High risks cluster around **what the group shares and what it bought or built most recently**:
1. **Shared IT reaches the plants** (GR-01, GR-02, GR-07). One identity domain, one GEPS, and one integration hub serve every plant. The acquired plant P8 is the weak entry point, and the GEPS scheduling recovery has never been tested (scenario gaps 1 and 2).
2. **The product reaches the grid** (GR-04). The TMU firmware signing key is in software on a build server. A stolen key would let an attacker sign firmware that about 700 utilities, including the affiliate, would trust (gap 3).
3. **Affiliates are vendors** (GR-05, Moderate, and the High division risks EU-001 and ES-001). The Electric Utility's CIP duties depend on how its affiliates handle its information and access (gaps 4 and 5).

Notification consistency (GR-03), AI governance (GR-06), and Grid Engineering inheritance (GR-10) are Moderate at group level. They matter because a single incident would test all three at once (P08), which is why the P07 assessment sampled the incident controls across divisions.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** P8 integration (OT DMZ, domain trust removal, EDR, OEM gateway: GR-01, GR-07); GEPS hub least privilege and full restore test (GR-02); hardware security module signing and isolated build environment (GR-04); intercompany security schedules and BCSI relocation (GR-05); AI validation and storm allocation rule (GR-06).
- **Accepted (all Low):** GR-16 (loss of key OT security and NERC compliance staff), MF-027 (theft of an encrypted laptop), EU-013 (single-source dependency on the affiliate for large power transformer spares), ES-008 (fCI exposed on federal contract projects).
- **Regulatory actions:** the Electric Utility's self-reports to SERC by 2026-09-30 for the CIP-003-9 and CIP-012-2 gaps and the BCSI handling issue (GR-08, EU-001, EU-002, EU-003; P03).
- **Treatment status:** 48 risks are In progress, 18 are Open (treatment approved, work not started), and 4 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The 4 High group risks were presented on 2026-09-15. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight and the Group CISO's reporting line).

## 6. Approval
- Board risk committee: approved the group register, the High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the 7 High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-16.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
