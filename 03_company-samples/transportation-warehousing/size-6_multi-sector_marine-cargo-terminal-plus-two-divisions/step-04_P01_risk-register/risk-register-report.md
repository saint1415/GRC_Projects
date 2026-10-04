# Risk Register Report: Cris Santos Company Holdings | Transportation and Warehousing | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded port logistics group; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Transportation and Warehousing, Wholesale Trade, Real Estate) |
| Focus division | Marine Terminals (NAICS 488320): 9 facilities regulated under 33 CFR Part 105 |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also feeds | The Cybersecurity Assessment each terminal must complete by 2027-07-16 (33 CFR 101.650(e)(1)); the risk factors and Item 106 risk management disclosure in the annual report |
| Registers | `risk-register.csv` (group), `risk-register-marine-terminals.csv`, `risk-register-freight-trading.csv`, `risk-register-port-real-estate.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses); MT-024 added on 2026-08-28 from the P07 assessment |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads and the Division CySO |
| Approved | 2026-09-15 by the board risk committee (group register, the Very High risk and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that supports terminal operations, trading or property operations, plus the corporate shared services they depend on: identity (SYS-G1), the SOC (SYS-G2), the cloud platform, WAN and vault (SYS-G3), the B2B integration hub (SYS-G4), ERP and payroll (SYS-G5) and the productivity suite (SYS-G6). Division systems are SYS-T1 to SYS-T6 and SYS-T1L, SYS-F1 to SYS-F3, and SYS-R1 and SYS-R2 (`../00_company-facts.md` section 3).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one; for Marine Terminals the Division CySO co-owns it, because the same analysis feeds the Subpart F Cybersecurity Assessments. Marine Terminals, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not simply copied from the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead (Group CISO for group risks) |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Safety risks (crane, ASC and hazardous cargo) rated High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), and interviews with each division's leadership, the FSOs and the hiring halls' dispatch staff.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). Group impact reflects enterprise consequences: several regulators at once, SEC disclosure, effects on more than one division, and safety at the terminals.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision or group funding.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 9 | 8 | 1 | 0 | 18 | n/a |
| Marine Terminals | 1 | 6 | 19 | 6 | 0 | 32 | 19 |
| Freight Trading | 0 | 4 | 7 | 5 | 0 | 16 | 9 |
| Port Real Estate | 0 | 2 | 8 | 4 | 0 | 14 | 9 |
| **All registers** | **1** | **21** | **42** | **16** | **0** | **80** | **37** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Ransomware enters through the B2B integration hub and spreads to all three divisions | MT-001, MT-002, FT-006, RE-012 | Separate hub flows and accounts per division; retire shared credentials and FTP; cross-division tabletop | Group CISO | 2027-03-31 |
| GR-02 | Terminal customer data shared with the trading affiliate; affiliate truckers preferred | MT-006, MT-007, FT-007 | Remove the group logistics role; neutral appointment rules; affiliate data-sharing standard | Group General Counsel | 2026-11-30 |
| GR-04 | A terminal is found not compliant with Subpart F, or a Plan is late | MT-008, MT-009, MT-010 | Alternates and Plans for T7 to T9; longshore and OT training; Assessments for all 9 | Division CySO | 2027-04-30 |
| GR-06 | Third-party remote access into OT and building systems | MT-003, RE-001, RE-002, RE-014 | All vendor and integrator access through the group jump host; SOC monitoring | Group CISO | 2027-03-31 |
| GR-07 | Business email compromise redirects a large payment | FT-004, RE-003 | Payment change verification in SYS-G5 for all divisions | Group chief financial officer | 2026-12-31 |
| GR-08 | DoD contract noncompliance (CUI and FCI scope) | FT-001, FT-002, FT-003, FT-013 | Re-scope Level 1; CUI decision; DFARS reporting procedure | Freight Trading federal contracts compliance manager | 2026-12-31 |
| GR-09 | AI drives operational and legal decisions without governance | MT-011, FT-005 | Group AI governance program (P10) | Group Chief Risk Officer | 2027-03-31 |
| GR-10 | Compromise of the group identity platform | MT-016 | Tiered administration; identity threat detection | Group identity director | 2027-03-31 |
| GR-11 | Gulf terminals remain on legacy systems | MT-002, MT-004, MT-005, MT-031 | Group-funded migration; interim immutable backups and SIEM forwarding | Gulf terminals general manager | 2027-06-30 |

### Marine Terminals (focus division): risks rated Very High and High
| Risk ID | Level | Risk | Treatment | Owner | Due |
|---|---|---|---|---|---|
| MT-002 | **Very High** | Ransomware at a Gulf terminal spreads from IT to crane and yard OT on the flat network | Interim IT/OT firewall at each Gulf terminal by 2026-12-31; standard OT zones by 2027-06-30 | Gulf terminals general manager | 2027-06-30 |
| MT-001 | High | Ransomware encrypts TOS servers, gate servers and operations workstations at T1 to T6 | Certificates for EDI adapters; isolate hub flows | Director of terminal systems | 2027-01-31 |
| MT-003 | High | Always-on crane vendor remote access at T7 to T9 | Disconnect modems; group jump host | Gulf terminals general manager | 2026-11-30 |
| MT-004 | High | Gulf legacy TOS backups destroyed or too old to meet the RPO | Offsite immutable copy; quarterly restore test | Gulf terminals general manager | 2026-12-31 |
| MT-006 | High | Freight Trading staff use terminal data about competing importers | Remove the group logistics role; review 12 months of access logs | Director of terminal systems | 2026-11-30 |
| MT-007 | High | Reserved appointment slots for affiliate truckers at T3 and T5 | Remove or offer equal terms to all; legal review | Director of customer services | 2026-10-31 |
| MT-011 | High (safety) | Optimization service sends an unsafe or wrong ASC job sequence at T5 | Advisory mode; safety case; AI council review (P10) | Director of planning | 2026-10-31 |

MT-002 is the only Very High risk in the group. The board risk committee reviewed it on 2026-09-15 and did **not** accept it; it approved the interim firewall budget and asked for monthly status until the risk falls to Moderate.

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| FT-001 | Freight Trading | CUI drawings handled in systems that do not meet NIST SP 800-171 | Federal contracts compliance manager | 2026-12-31 |
| FT-002 | Freight Trading | SPRS Level 1 affirmation inaccurate: FCI in SYS-F2 outside the scope | Federal contracts compliance manager | 2026-11-30 |
| FT-004 | Freight Trading | Supplier bank-detail change redirects a large payment | Freight Trading chief financial officer | 2026-12-31 |
| FT-007 | Freight Trading | Trading desks gain an advantage from competitors' terminal data | Freight Trading chief compliance officer | 2026-11-30 |
| RE-001 | Port Real Estate | Building access control or CCTV taken over through internet-exposed remote access | Director of building technology | 2027-03-31 |
| RE-003 | Port Real Estate | Closing wire or construction draw redirected by email fraud | Port Real Estate general counsel | 2026-12-31 |

### What the results say
The program is defined and its common controls are sound: a 24x7 SOC, EDR on every IT host, phishing-resistant MFA and just-in-time PAM for administrators, immutable backups and quarterly TOS restore tests. The High risks cluster at **the seams of the group**, not in any one division's basics:
1. **Between divisions.** The trading affiliate sees terminal customers' data and gets preferred appointments (GR-02; scenario gap 1). This is a cyber access problem with a Shipping Act and contract consequence, so it is owned by the Group General Counsel, not by IT.
2. **Acquired and outsourced estates.** The Gulf terminals (GR-11, MT-002 to MT-005; gap 2) and the building systems run by integrators (GR-06, RE-001, RE-002; gap 5) sit outside the controls that protect the rest of the group.
3. **Shared services as a path.** The integration hub joins all three divisions' partners (GR-01, GR-16). The P08 runbook uses it as the starting point of the incident for that reason.
4. **Regulatory programs behind schedule.** Subpart F at three terminals and for longshore labor (GR-04; gap 3) and the DoD contract scope (GR-08; gap 4).
5. **AI ahead of governance** at T5 and in trading legal (GR-09; gap 8).

Governance gaps 6 and 7 (undocumented inheritance for Port Real Estate and the unexercised notification matrix) are Moderate at group level (GR-05, GR-03). They matter because they hide whether Port Real Estate controls operate and whether notices would go out on time, which is why P07 sampled Port Real Estate governance and P08 exercises the matrix.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** Gulf terminal migration and interim protections (GR-11); integration hub separation by division (GR-01, GR-16); third-party access through the jump host for OT and building systems (GR-06); Subpart F completion at all 9 terminals (GR-04); group AI governance (GR-09); payment change verification (GR-07).
- **Legal and commercial actions:** remove the group logistics role and neutralize appointment rules (GR-02); legal review of Shipping Act and contract exposure; Level 1 re-scope and corrected SPRS affirmation, and a decision on CUI work (GR-08).
- **Accepted (all Low):** GR-15, MT-025, MT-028, MT-029, MT-032, FT-009, FT-012, FT-014, FT-016, RE-009, RE-012 and RE-013. Each was accepted by the owner allowed by the table in section 1.
- **Treatment status:** 52 risks are In progress, 16 are Open (treatment approved, work not started), and 12 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The nine High group risks and the Very High division risk were presented on 2026-09-15. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (board risk committee oversight, the Group CISO's reporting line, and the use of the register in the group's risk management processes). The Marine Terminals register is also the starting point for each terminal's Cybersecurity Assessment, which must analyze all networks and the risk posed by each digital asset (101.650(e)(1)(i)); the CySO will extend it terminal by terminal before 2027-03-31.

## 6. Approval
- Board risk committee: approved the group register, the nine High group treatment plans, the MT-002 treatment and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the twelve High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-15.
- Next full review: May to July 2027, or sooner after a major change (for example the Gulf cutover), an acquisition or an incident.
