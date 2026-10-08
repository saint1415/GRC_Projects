# Regulatory Gap Analysis: Cris Santos Company Holdings | Chemical | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Chemical (focus division: Specialty Chemicals, NAICS 325998) |
| Primary benchmark | CFATS RBPS 8 (Cyber), 6 CFR 27.230(a)(8), with CISA's RBPS 8 security measures and the OT benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3). **Voluntary** (CFATS authority lapsed) |
| Binding regulations by division | Specialty Chemicals: EPA RMP Program 3 at Plant C1 and Program 2 at 4 ammonia plants (40 CFR Part 68), OSHA PSM, CERCLA and EPCRA release reporting, the DOT hazmat security plan as an offeror. Distribution: **USCG 33 CFR Part 101 Subpart F at Terminal T1**, the DOT security plan as an offeror. Hazmat Transport: the DOT security plan and training as a carrier, DOT incident reporting, FMCSA ELD and driver record rules. Group: SEC disclosure, state breach laws |
| Gap tables | `gap-analysis.csv` (Specialty Chemicals, 82 rows); `gap-analysis-distribution.csv` (53 rows); `gap-analysis-hazmat-transport.csv` (22 rows); `gap-analysis-group.csv` (16 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from P07 (to 2026-08-28; Terminal T1 OT test 2026-08-19) |
| Assessors | Division security and compliance leads, the Plant C1 Process Safety Manager, the Terminal T1 CySO, and the Hazmat Transport Vice President of Safety and Compliance, coordinated by the Group Chief Risk Officer; reviewed by group internal audit |
| Regulatory status checked | 2026-10-05 (eCFR point-in-time 2026-09-23; Federal Register search; the vertical registry) |

## 1. Applicability
Applicability was decided first, from each division's chemicals, quantities, sites, and operations. Citations reused from the Chemical Small sample were re-checked for this size.

**1. CFATS (6 CFR Part 27): would apply to 7 plants, but cannot be enforced.**
- Plant C1 holds up to 360,000 lb of chlorine (a release-toxic chemical of interest with an STQ of 2,500 lb) and about 170,000 lb of hydrogen peroxide in 50% solution (a theft and diversion chemical of interest at 35% or more, STQ 400 lb). Six other plants were also tiered before the lapse.
- **Status on 2026-10-05:** CFATS authority expired on 2023-07-28. The vertical registry confirmed on 2026-09-25 that it has not been reauthorized, and a Federal Register search on 2026-10-05 found no CFATS document since June 2025.
- **Decision:** RBPS 8 is a **voluntary benchmark** for all 16 plants, because it is still the only chemical-sector federal cyber performance standard and 7 plants would be back in scope on reauthorization. Legacy CVI is still protected (G-025).

**2. EPA RMP (40 CFR Part 68): Program 3 at Plant C1; Program 2 at 4 plants.**
- Plant C1's chlorine process exceeds the 2,500 lb TQ by a wide margin. Connected rail cars count as part of the stationary source (68.3). The process is subject to OSHA PSM (chlorine TQ 1,500 lb), so it is **Program 3** under 68.10(l)(2). Plant C1 is a **responding stationary source** (68.90(a), 68.95).
- Four plants hold more than 20,000 lb of ammonia in 29% aqueous ammonia (listing "Ammonia (conc 20% or greater)", TQ 20,000 lb). They are not PSM-covered (29% is below the PSM listing for ammonia solutions above 44%), so they are **Program 2**, as in the Small sample's math.
- **2024 amendments with 2027 compliance dates** (68.10(g)) are assessed as current obligations: standby power for monitoring equipment, safer technology and alternatives analysis for NAICS 325 Program 3 processes, root cause analysis, and employee participation. An EPA proposal (91 FR 8970, 2026-02-24; comment period extended to 2026-05-11, 91 FR 16621) would revise several of them; until a final rule is published, the current text governs.
- RMP is not a cyber rule. It is in scope because PHA, MOC, safe work practices, contractor oversight, and emergency notification all depend on the control system (G-041 to G-073).

**3. USCG MTSA cybersecurity rule (33 CFR Part 101 Subpart F): applies to Terminal T1 only.**
- Terminal T1 transfers hazardous materials in bulk to and from vessels of 250 barrels or more, so 33 CFR Part 154 applies (154.100(a)), which brings Part 105 (105.105(a)(1)) and therefore Subpart F (101.605(a)). Plant C1 and the other plants have no marine transfer.
- Key dates: training by 2026-01-12 and annually (101.650(d)(4)); Cybersecurity Assessment and Plan submission by 2027-07-16 (101.650(e)(1); 101.655).

**4. DOT Hazardous Materials Regulations: all three divisions.**
- Specialty Chemicals and Distribution **offer**, and Hazmat Transport **transports**, large bulk quantities (more than 3,000 liters in one packaging) of 50% hydrogen peroxide (Division 5.1, PG II) and Class 3 PG II solvents, so each needs a security plan (172.800(b)(6) and (b)(10)) with security training (172.704(a)(4)-(5)).
- Chlorine arrives at Plant C1 by rail from the supplier; the supplier is the offeror and the railroad the carrier for that movement.
- **FMCSA safety permit** (49 CFR 385.403) does not apply: Hazmat Transport hauls none of the listed materials.

**5. Group-wide and screened-out items.**
- **SEC:** Reg S-K Item 106 and Form 8-K Item 1.05 apply (publicly traded).
- **State breach laws:** each state where affected individuals reside, with Florida (Fla. Stat. 501.171) as the worked example.
- **CIRCIA** (proposed 6 CFR Part 226): no final rule as of 2026-10-05, so no obligation. Unlike the Small sample, this group would be covered as proposed: it exceeds the SBA size standard (650 employees for NAICS 325998), and Terminal T1 is an MTSA facility.
- **CCPA:** applies to the group's California workforce data (about 110 drivers live in California). Below the cyber audit volume triggers (GG-09).
- **Not applicable:** TSA surface Security Directives (designated rail and pipeline operators only), FAR clauses and CMMC (no federal contracts), EAR (no controlled technology found, 2026-03), DEA List I (none distributed), PCI DSS (no card payments).

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Regulation-by-division matrix
| Requirement | Specialty Chemicals | Distribution | Hazmat Transport | Group (corporate) |
|---|---|---|---|---|
| C-CHEMICAL-R01 CFATS RBPS 8 | **Primary benchmark** (voluntary; 7 formerly tiered plants) | Voluntary practice at branches holding hydrogen peroxide | Not applicable | OT security standard carries the intent |
| OT benchmark (CSF 2.0 with SP 800-82 Rev. 3) | Applies (voluntary) | Applies at Terminal T1 and repackaging lines (voluntary) | Not applicable (no plant OT) | Group OT standard |
| EPA RMP, 40 CFR Part 68 | **Binding:** Program 3 at Plant C1; Program 2 at 4 plants | Not applicable (no process above a TQ, 2026-03 screen) | Not applicable (transportation is excluded from the stationary source) | Process safety center of excellence |
| OSHA PSM, 29 CFR 1910.119 | **Binding** (Plant C1 chlorine) | Not applicable | Not applicable | |
| CERCLA 40 CFR 302.6 and EPCRA 40 CFR 355.40 to 355.43 | **Binding** (all plants) | **Binding** (branches and terminals) | Applies to releases in transport (355.42(b): 911 notice) | ERC backup caller |
| C-CHEMICAL-R02 USCG Subpart F | Not applicable (no marine transfer) | **Binding at Terminal T1** | Not applicable | Gateway, SOC, and identity support it |
| HMR security plan and training, 49 CFR 172.800 to 172.804 and 172.704 | **Binding** (offeror) | **Binding** (offeror) | **Binding** (carrier) | Group ERC (172.604) |
| HMR incident reports, 49 CFR 171.15 and 171.16 | When in physical possession during loading | When in physical possession during loading | **Binding** (carrier) | |
| FMCSA ELD and driver records, 49 CFR Parts 382, 391, 395 | Not applicable | Not applicable | **Binding** | |
| N42-R07 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Binding** (registrant) |
| State breach laws (Florida worked example) | Employees | Employees; customer contacts | Drivers and employees | Coordinates notices |
| C-CHEMICAL-R03 CIRCIA | Tracked only (proposed) | Tracked only | Tracked only | Tracked only |
| SOC 2 (contractual) | Not in scope (P09) | **In scope for the managed inventory service** (P09) | Not in scope (P09) | Group services carved in |

## 3. Method
1. **Requirements.** RBPS 8 rows come from the text of 6 CFR 27.230(a)(8) and related RBPS items, and CISA's published RBPS 8 security measures (reused from the Small sample, re-read 2026-10-05). RMP, Subpart F, HMR, FMCSA, CERCLA, and EPCRA rows follow each rule's section structure, read from eCFR (point in time 2026-09-23). Group rows use the vertical and wholesale registries.
2. **Crosswalk.** OT benchmark rows use the official CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). All other rows carry an **author mapping**, labeled as such, because NIST publishes no mapping for 6 CFR Part 27, 40 CFR Part 68, 33 CFR Part 101, or 49 CFR.
3. **Evidence.** Interviews, document review, configuration exports, the Plant C1 PHA and compliance audit, and P07 test results (Plant C1 on 2026-08-12, Terminal T1 on 2026-08-19, two Hazmat Transport terminals on 2026-08-25).
4. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale. Where a row applies a process safety rule to a cyber condition, the row says "author interpretation".

## 4. Results
### 4.1 Specialty Chemicals (`gap-analysis.csv`)
| Source | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| CFATS RBPS text, 6 CFR 27.110 to 27.400 (voluntary) | 5 | 5 | 0 | 1 | 11 |
| CISA RBPS 8 security measures (voluntary guidance) | 4 | 10 | 0 | 0 | 14 |
| OT benchmark: CSF 2.0 with SP 800-82 Rev. 3 (voluntary) | 4 | 11 | 0 | 0 | 15 |
| EPA RMP Program 3, Plant C1 (binding) | 19 | 13 | 0 | 0 | 32 |
| EPA RMP Program 2, 4 ammonia plants (binding) | 0 | 1 | 0 | 0 | 1 |
| CERCLA, EPCRA, and OSHA PSM (binding) | 3 | 0 | 0 | 0 | 3 |
| DOT HMR as offeror: security plan, training, emergency number (binding) | 5 | 1 | 0 | 0 | 6 |
| **Total** | **40** | **41** | **0** | **1** | **82** |

Of the 41 gaps, **9 are High**, 30 Moderate, and 2 Low.

**Reading the results.** Unlike the Small sample, there are no Not met rows: the group OT standard and the Plant C1 program give every benchmark row at least a partial answer. The pattern is **Plant C1 strong, legacy plants weak, and the seams between process safety and cyber open**. Six of the 9 High gaps are about change and access paths that reach every plant (remote access, MOC, segmentation, monitoring). The other 3 are RMP rows where a cyber condition breaks an assumption the process safety program makes: the PHA treats DCS alarms and the SIS as independent (G-046), remote integrator work is not covered by safe work practices (G-052), and two change paths reach the DCS outside MOC (G-056).

### 4.2 Distribution (`gap-analysis-distribution.csv`)
| Source | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| USCG Subpart F, Terminal T1 (binding) | 13 | 24 | 10 | 2 | 49 |
| USCG MTSA reporting, 33 CFR 101.305 (binding) | 1 | 0 | 0 | 0 | 1 |
| DOT HMR as offeror: security plan, training, emergency number (binding) | 2 | 1 | 0 | 0 | 3 |
| **Total** | **16** | **25** | **10** | **2** | **53** |

Of the 35 gaps, **5 are High**, 22 Moderate, and 8 Low. The 10 Not met rows split into two groups:
- **Overdue now:** contractor training and supervision (DS-G31, DS-G32, DS-G34, DS-G35). The 2026-01-12 deadline passed with 23 contractor personnel untrained, unaccompanied, and unmonitored.
- **Not started, not yet due:** the Plan and Assessment (DS-G02, DS-G10, DS-G12, DS-G36), the approved hardware and software list (DS-G25), and IT/OT segmentation for the loading rack and tank gauging PLCs (DS-G46, High). They are Not met today, and the Plan cannot be approved with them open.

### 4.3 Hazmat Transport (`gap-analysis-hazmat-transport.csv`)
| Source | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| DOT HMR as carrier: security plan, training, incident reports, emergency number | 9 | 4 | 0 | 0 | 13 |
| FMCSA ELD, driver qualification, and drug and alcohol records | 3 | 2 | 1 | 0 | 6 |
| Screened out (FMCSA safety permit, TSA Security Directives, CMMC) | 0 | 0 | 0 | 3 | 3 |
| **Total** | **12** | **6** | **1** | **3** | **22** |

Hazmat Transport's regulatory basics are in place. Its 7 gaps are where its rules meet its technology: the security plan does not assess cyber threats to dispatch and telematics (HT-G02, HT-G05 High, HT-G07), ELD support accounts are shared (HT-G16, Not met under 395.22(b)(2)(ii)), and there is no plan for a fleet-wide ELD outage (HT-G18).

### 4.4 Group (`gap-analysis-group.csv`)
| Source | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| SEC disclosure | 2 | 1 | 0 | 0 | 3 |
| State breach laws (Florida worked example and other states) | 1 | 4 | 0 | 0 | 5 |
| CCPA, FTC Act, OFAC, OSHA injury reporting | 3 | 1 | 0 | 0 | 4 |
| Screened out or not in effect (CIRCIA, CFATS, EAR, FAR) | 0 | 0 | 0 | 4 | 4 |
| **Total** | **6** | **6** | **0** | **4** | **16** |

The group gaps are about the untested notification matrix (scenario gap 8) and two missing pieces: OT and safety factors in the SEC materiality checklist (GG-03) and vendor breach notice terms (GG-07).

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Contractor training and supervision overdue at Terminal T1 (4) | Distribution | 101.650(d)(1)-(4) | High | Train or escort all 23; onboarding gate | Distribution CySO for Terminal T1 | 2026-10-31 |
| 2 | Always-on integrator tools at 2 legacy plants (2) | Specialty Chemicals | RBPS 8 (voluntary) | High | Remove; move to the gateway | Specialty Chemicals Vice President of Manufacturing Technology | 2026-11-30 |
| 3 | Combined cyber and RMP tabletop (8) | All | 68.96(b)(2) (before 2026-12-21); 101.635(c); POL-03 | Moderate | Tabletop on 2026-12-08 with county responders | Group General Counsel; Specialty Chemicals EHS director | 2026-12-15 |
| 4 | AI-001 and other change paths outside MOC (3, 9) | Specialty Chemicals | 68.75(a)-(b); 68.65(c)(1)(iv) | High | MOC for hub pushes and AI changes; staging share; cyber screen | Plant C1 Process Safety Manager | 2027-03-31 |
| 5 | Shared OT remote access (1) | Specialty Chemicals; Distribution | RBPS 8; 68.69(d); 101.650(a)(4), (f)(3) | High | Named accounts, per-session approval, recording everywhere | Group OT Security Director | 2027-03-31 |
| 6 | Terminal T1 segmentation (4) | Distribution | 101.650(h)(1) | High | Rack and gauging PLCs behind the OT firewall | Distribution CySO for Terminal T1 | 2027-03-31 |
| 7 | Terminal T1 Assessment and Plan (4) | Distribution | 101.650(e)(1); 101.630; 101.655 | Moderate | Assessment by 2027-03-31; submit by 2027-05-31 | Distribution CySO for Terminal T1 | 2027-05-31 |
| 8 | Cyber causes in PHAs and hazard reviews (3) | Specialty Chemicals | 68.67(c)(4); 68.50 | High | Interim PHA update at Plant C1; Program 2 hazard reviews | Group Process Safety Director | 2027-06-30 |
| 9 | Security plans miss cyber threats (5) | All | 172.802(a), (a)(3), (b)(2) | High (carrier) | Revise all three plans at the 2026 annual reviews | Each senior official under 172.802(b)(1) | 2026-12-31 |
| 10 | ELD shared support accounts (5) | Hazmat Transport | 395.22(b)(2)(ii) | Moderate | Unique accounts | Hazmat Transport Director of Fleet Technology | 2026-11-30 |
| 11 | Legacy plant segmentation, monitoring, and backups (2) | Specialty Chemicals | RBPS 8; OT benchmark | High | OT standard migration | Specialty Chemicals Vice President of Manufacturing Technology | 2027-12-31 |

High and Moderate gaps are carried into the risk registers (P01) and the POA&M (P07). POAM-003, POAM-004, POAM-009 to POAM-016, and POAM-022 trace directly to this analysis.

## 6. Pending regulatory changes
None of these is treated as a current obligation.
- **CFATS reauthorization.** If Congress reauthorizes CFATS, RBPS 8 becomes enforceable again for tiered facilities, and the 7 formerly tiered plants would need Site Security Plan updates. Rows G-001 to G-025 would be the starting point.
- **EPA RMP proposal (91 FR 8970, 2026-02-24; comment period extended to 2026-05-11).** EPA proposes changes to the 2024 rule, including safer technology and alternatives analyses, third-party audits, employee participation, community and emergency responder notification, natural hazards, power loss, emergency response exercises, and process safety information. Rows G-044, G-045, G-047, G-059, G-062, G-064, G-067 to G-069, and G-073 are flagged. Until a final rule is published, the current Part 68 text governs, including the 2027-05-10 compliance dates in 68.10(g).
- **CIRCIA final rule (proposed 6 CFR Part 226; NPRM 89 FR 23644, 2024-04-04).** As proposed, covered entities would report covered cyber incidents within 72 hours and ransom payments within 24 hours. Not in effect; the group would be covered as proposed (GG-13).
- **NIST SP 800-82 Rev. 4 (initial public draft).** The benchmark stays on Rev. 3 until Rev. 4 is final; then the section references in G-026 to G-040 should be rechecked.
