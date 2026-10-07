# Risk Register Report: Cris Santos Company Holdings | Water and Wastewater Systems | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Utilities, Construction, and Waste Management and Remediation Services) |
| Focus division | Water Utility (NAICS 221310): 58 community water systems serving about 3.37 million people |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also supports | The RRA of each covered water system (42 U.S.C. 300i-2(a)(1)(A)(i)-(vi)), especially the automated-systems element; Construction's NIST SP 800-171 risk assessment requirement (3.11.1); the Environmental Services hazardous materials security plan risk assessment (49 CFR 172.802(a)) |
| Registers | `risk-register.csv` (group), `risk-register-water-utility.csv`, `risk-register-construction.csv`, `risk-register-environmental-services.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads and the Group OT Security Director |
| Approved | 2026-09-15 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** The OT and IT systems of the three divisions and the corporate shared services they depend on: the group identity platform (SYS-G1), the group SOC and OT monitoring (SYS-G2), the cloud and data platform (SYS-G3), and the OT remote access gateway (SYS-G4). Division systems are SYS-W1 to SYS-W4, SYS-C1 to SYS-C4, and SYS-E1 and SYS-E2 (`../00_company-facts.md` section 3).

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. The Water Utility, the focus division, has the most detailed register (28 risks), with RS1-SCADA (the P02 SSP system) and the 19 acquired systems as its main subjects.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not on the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Risks to public health or worker safety rated High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment and division samples (P07), CISA water sector advisories, and interviews with each division's leadership and RS-1 operators.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**. Engineered safeguards that do not depend on SCADA (hardwired stroke limits, independent analyzer alarms, manual operation) lower the likelihood of adverse impact for chemical-feed events at the 15 largest systems' plants.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA categories (P05), with public health as its own category. Group impact reflects enterprise consequences: several regulators at once, public notices in more than one system, DoD contract exposure, and SEC disclosure.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 11 | 3 | 0 | 18 | n/a |
| Water Utility | 0 | 2 | 18 | 8 | 0 | 28 | 15 |
| Infrastructure Construction | 0 | 3 | 7 | 6 | 0 | 16 | 10 |
| Environmental Services | 0 | 1 | 10 | 5 | 0 | 16 | 6 |
| **All registers** | **0** | **10** | **46** | **22** | **0** | **78** | **31** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Misuse of the shared OT remote access gateway changes treatment at a large water system | WU-001, WU-003, CN-004 | Revoke the commissioning exception; per-session approval for all; recording review; interconnection agreement and contract security terms for Construction | Group OT Security Director | 2026-12-31 |
| GR-02 | Ransomware spreads through shared IT services into OT DMZs and division systems | WU-010, CN-006, ES-005 | Segment acquired systems; quarterly restore tests; cross-division tabletop | Group CISO | 2027-03-31 |
| GR-04 | Attackers exploit the weak OT of the 19 acquired water systems | WU-002, WU-004, WU-005, WU-006, WU-016 | Integration program: gateway, named accounts, segmentation, backups, monitoring | Water Utility security and compliance lead | 2027-06-30 |
| GR-06 | Covered defense information is compromised or the CMMC affirmation is inaccurate | CN-001, CN-002, CN-005, CN-007 | CUI discovery and purge; correct the assessment before the 2026-12-12 affirmation; C3PAO readiness | Construction president | 2026-12-12 |

### Water Utility (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| WU-001 | Attacker uses a commissioning engineer's gateway session to change chemical feed at WTP-A | Revoke the exception (POAM-002); quarterly OT account certification (POAM-001); recording review (POAM-006) | RS-1 Director of Operations | 2026-10-31 |
| WU-002 | Attacker reaches an acquired system's HMI through a legacy vendor remote tool | Remove vendor tools; move behind SYS-G4 (POAM-013) | Water Utility security and compliance lead | 2027-06-30 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| CN-001 | Construction | Covered defense information on commissioning laptops and SYS-C1 is stolen | Construction security and compliance lead | 2026-11-30 |
| CN-002 | Construction | The CMMC annual affirmation repeats a self-assessment that records unmet requirements as MET | Construction president | 2026-12-12 |
| CN-004 | Construction | A compromised commissioning account or laptop is used to reach client or Water Utility OT | Construction commissioning and controls integration director | 2026-12-31 |
| ES-001 | Environmental Services | Attacker uses default gateway credentials to alter client data or reach client controls | Environmental Services remote monitoring general manager | 2026-11-30 |

### What the results say
The program is defined and its common controls are sound: a 24x7 SOC, a remote access gateway with MFA and recording, PAM, immutable backups, and plants that can run without SCADA. There are no Very High risks, because the engineered safeguards at the large plants limit what a remote attacker can do to water quality before operators intervene. The High risks cluster in three places:
1. **The paths between divisions** (GR-01, WU-001, CN-004). The gateway is a common control, but an exception for Construction's commissioning team and an unmanaged laptop connection turned a sister division into the easiest route into RS-1 (scenario gap 1).
2. **What the group bought but has not integrated** (GR-04, WU-002). The 19 acquired water systems carry the remote access, credential, segmentation, and backup weaknesses that the regional SCADA systems fixed years ago (gap 2).
3. **Construction's defense work** (GR-06, CN-001, CN-002). CUI outside the enclave and an inaccurate self-assessment create contract, legal, and national security exposure with a hard date: the 2026-12-12 affirmation (gap 4).

Environmental Services has one High risk (ES-001, default credentials on client site gateways). Its other risks are Moderate and center on the monitoring service's commitments to clients (gap 5), which P09 addresses. Governance gaps 3, 6, and 7 (RRA consistency, the unexercised notification matrix, and undocumented inheritance) are Moderate at group level (GR-05, GR-03, GR-09), and the AI gap (8) is GR-07.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** acquired-system integration (GR-04); OT monitoring expansion (GR-12); commissioning access controls (GR-01); CUI discovery and CMMC readiness (GR-06); group AI governance (GR-07); cross-division tabletop and notification matrix (GR-03).
- **Accepted (all Low):** WU-014 (unalarmed booster stations until the 2027 capital program), WU-023 (loss of the ROC, covered by the tested backup control room), CN-015 (equipment telematics tampering), ES-015 (driver location data retention until contract renewal).
- **Transferred in part:** GR-14 and WU-019 (vendor breach of customer data: contract notice terms and insurance), GR-18 (insurance coverage for OT and public notice costs).
- **Treatment status:** 54 risks are In progress, 20 are Open (treatment approved, work not started), and 4 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks were presented on 2026-09-15. The Reg S-K Item 106 disclosure in the next annual report draws on this governance (GR-15 adds an OT review of the draft). Each covered water system's RRA cyber addendum cites the Water Utility register rows that apply to it, so the register and the 42 RRAs stay consistent (GR-05).

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the six High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-16.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
