# Risk Register Report: Cris Santos Company Holdings | Transportation Systems | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Transportation, Wholesale Trade, Real Estate) |
| Focus division | Freight Railroad (NAICS 482112): 72 railroads, 14 of them Covered Railroads under 49 CFR 1580.101 |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | The risk assessment that informs the Covered Railroads' CIP and the remediation plan from the TSA vulnerability assessment (SD 1580-21-01E II.E.2) |
| Registers | `risk-register.csv` (group), `risk-register-freight-railroad.csv`, `risk-register-transload-wholesale.csv`, `risk-register-real-estate.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group Chief Risk Officer's GRC team with the Group CISO and the three division security and compliance leads |
| Approved | 2026-09-10 by the board safety, security, and risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that supports train movement, terminal operations, building operations, or holds personal information or SSI in the three divisions, plus the corporate shared services they depend on: identity (SYS-G1), the SOC (SYS-G2), network, data centers, and cloud (SYS-G3), the ERP (SYS-G4), and the integration platform (SYS-G5). Division systems are listed in `../00_company-facts.md` section 3.

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. Each division security and compliance lead keeps one. The Freight Railroad register, for the focus division, is the most detailed.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not by copying the highest division rating.

**Risk tolerance and who can accept risk:**
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board safety, security, and risk committee; temporary only, with a dated plan |
| Very High | Board safety, security, and risk committee only |

Risks to train movement safety, hosted passenger trains, or hazmat loading rated High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the CAP results, the 2026-05 architecture design review, the common control assessment (P07), and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Group impact reflects enterprise consequences: several regulators at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 3 | 12 | 3 | 0 | 18 | n/a |
| Freight Railroad (`risk-register-freight-railroad.csv`) | 0 | 4 | 16 | 8 | 0 | 28 | 17 |
| Transload and Wholesale (`risk-register-transload-wholesale.csv`) | 0 | 2 | 7 | 7 | 0 | 16 | 11 |
| Real Estate (`risk-register-real-estate.csv`) | 0 | 0 | 6 | 6 | 0 | 12 | 9 |
| **All registers** | **0** | **9** | **41** | **24** | **0** | **74** | **37** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Compromise of the shared integration platform reaches rail Critical Cyber Systems and exposes personal information of all divisions | RR-002; TW-013 | File a CIP amendment request with the SYS-G5 flows; dedicated DMZ rule and inspection; purge HR exports after transfer; rotate partner credentials | Group CISO | 2026-12-31 |
| GR-02 | Ransomware spreads through shared services into the dispatch back office, terminals, and corporate systems at once | RR-001; TW-001; TW-010 | Segment and onboard the acquired terminals; review and remove the OT directory trust; cross-division ransomware tabletop (P08) | Group CISO | 2027-03-31 |
| GR-14 | A state-sponsored actor pre-positions in rail OT to disrupt operations during a crisis | RR-006; RR-007 | Forward CTC and PTC logs with 1-year retention; OT threat hunts twice a year; remove the directory trust | Director, Rail OT Security | 2027-03-31 |

### Freight Railroad (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| RR-001 | Ransomware encrypts CAD reporting and application servers and halts dispatching | Remove the directory trust; retire shared accounts; quarterly CAD restores to the clean-room account | Director, Rail OT Security | 2027-03-31 |
| RR-002 | Attacker uses the integration platform route to reach the TMS interface server in the industrial DMZ | CIP amendment request; dedicated DMZ rule with inspection; interconnection record | Director, Rail OT Security | 2026-11-30 |
| RR-004 | Known vulnerability in unpatched PTC back office servers is exploited | Document compensating measures and timeline; contract patch certification timeline with the PTC vendor | PTC Program Director | 2026-10-31 |
| RR-006 | Attacker moves from the corporate directory into the rail OT directory through the unreviewed trust | Review the trust; remove it or restrict it to named services; schedule reviews | Director, Rail OT Security | 2026-12-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| TW-001 | Transload and Wholesale | Ransomware spreads across acquired terminals and into the TOS | Director, Security and Compliance (Transload and Wholesale) | 2027-03-31 |
| TW-002 | Transload and Wholesale | Loading rack controllers are manipulated through always-on vendor remote access | Vice President, Terminal Operations | 2026-12-31 |

### What the results say
There are no Very High risks. The railroads' program is defined and TSA-driven: segmentation through an industrial DMZ, PAM, MFA for remote and privileged access, immutable backups, and a 24x7 SOC. The High risks cluster around **what the group shares** and **where divisions sit outside the platform**:
1. **The integration platform** (GR-01, RR-002) quietly links the terminals and the ERP to the server next to dispatch. Nobody owned it as a rail dependency, so it never entered the CIP (scenario gap 1).
2. **Ransomware across shared services** (GR-02, RR-001, TW-001) would hit dispatch back office systems and the 21 acquired terminals, which still run flat networks without EDR (gaps 4 and 5).
3. **OT pre-positioning** (GR-14, RR-006) is hard to see: CTC and PTC server logs are not in the SIEM and the OT directory trust has never been reviewed (gaps 3 and 4).
4. **PTC back office patching** (RR-004) is a TSA directive gap in its own right (SD III.E.3) as well as a risk.

Governance gaps 9 and 10 (no supplements and undocumented inheritance in two divisions) are Moderate at group level (GR-06, GR-07). They matter because they hide whether terminal and building controls operate at all, which is why P07 sampled those divisions on governance as well as technical controls.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** integration platform hardening and CIP amendment (GR-01); terminal segmentation and EDR (GR-02, TW-001, TW-010); OT logging and directory trust removal (GR-14); PTC back office standby rebuild (RR-003); OT inventory for terminals and buildings (GR-10); payment fraud controls in the ERP (GR-05).
- **Accepted (16, all Low):** GR-17, GR-18, RR-010, RR-016, RR-018, RR-022, RR-024, RR-025, RR-026, TW-004, TW-005, TW-008, TW-016, RE-009, RE-011, RE-012.
- **Contract actions:** PTC vendor patch certification timeline (RR-004); building OT vendor security terms (RE-007); second crew calling telephony provider (RR-019).
- **Treatment status:** 33 risks are In progress, 25 are Open (treatment approved, work not started), and 16 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board safety, security, and risk committee each quarter. The 3 High group risks were presented on 2026-09-10. The Reg S-K Item 106 disclosure in the next Form 10-K draws on the governance described here (the committee's oversight and the Group CISO's reporting line), and the Covered Railroads' TSA remediation plan draws on the Freight Railroad register.

## 6. Approval
- Board safety, security, and risk committee: approved the group register, the 3 High group treatment plans, and the funding request, 2026-09-10.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the 6 High division risks, 2026-09-10.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-08 to 2026-09-10.
- Next full review: May to July 2027, or sooner after a major change, acquisition, CIP amendment, or incident.
