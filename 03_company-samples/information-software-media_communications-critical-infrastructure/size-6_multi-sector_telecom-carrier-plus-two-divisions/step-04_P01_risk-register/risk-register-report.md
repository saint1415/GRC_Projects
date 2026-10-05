# Risk Register Report: Cris Santos Company Holdings | Communications | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Information, Professional Services, and Real Estate sectors) |
| Focus division | Telecom Carrier (NAICS 517111) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Regulatory link | Supports the CPNI duty to take "reasonable measures to discover and protect against attempts to gain unauthorized access to CPNI" (47 CFR 64.2010(a)); outage and 911 duties (47 CFR Part 4); CALEA SSI (47 CFR 1.20003); antenna structure lighting (47 CFR 17.47-17.49); and the risk management description in Reg S-K Item 106 |
| Registers | `risk-register.csv` (group), `risk-register-carrier.csv`, `risk-register-engineering.csv`, `risk-register-tower.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses); TF-014 added 2026-08-31 after P07 testing |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-17 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that holds CPNI, subscriber or landowner personal information, federal contract information, or network and lighting control functions in the three divisions, plus the corporate shared services they depend on (SYS-G1 to SYS-G4). Division systems are SYS-C1 to SYS-C10, SYS-E1 and SYS-E2, and SYS-T1 to SYS-T3 (`../00_company-facts.md` section 3). Business processes are those in the BIA (P05).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. The Carrier, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services (including the Carrier-owned service assurance platform that all three divisions use), or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to it. Group risks are rated on their own group-level likelihood and impact, not simply copied from the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Risks to 911 call completion, tower obstruction lighting, or lawful-intercept confidentiality rated High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), interviews with each division's leadership, and public reporting on intrusions into U.S. carriers. The FCC's 2025 order on reconsideration describes the "Salt Typhoon" campaign that "exploited publicly known common vulnerabilities and exposures" (90 FR 58006). That pattern shaped GR-01 and the P08 scenario.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (cost, operations, regulatory, safety, reputation). Group impact reflects enterprise consequences: several regulators at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 5 | 10 | 1 | 0 | 16 | n/a |
| Telecom Carrier | 0 | 5 | 20 | 5 | 0 | 30 | 22 |
| Network Engineering Services | 0 | 1 | 9 | 4 | 0 | 14 | 10 |
| Tower and Fiber Infrastructure | 0 | 3 | 9 | 2 | 0 | 14 | 10 |
| **All registers** | **0** | **14** | **48** | **12** | **0** | **74** | **42** |

No risk is rated Very High. Thirteen risks have a Very High impact (for example, GR-01, TC-002, TF-001), but none has an overall likelihood above Moderate, so Table I-2 gives High for twelve of them and Moderate for GR-15 (Low likelihood).

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Nation-state intrusion into network management planes across divisions | TC-001, TC-002, TC-003, NE-001, NE-002, TF-001, TF-014 | Named AAA accounts with MFA in the acquired regions; SBC replacement; brokered SYS-E1 access; SIEM onboarding | Group CISO | 2027-03-31 |
| GR-02 | Shared service assurance platform exposes CPNI to affiliates and fails for three divisions at once | TC-004, TC-005, TC-018, NE-005, TF-002 | Remove the legacy role; tenant partitioning; intercompany CPNI and tenant agreements; three-tenant failover test | Carrier OSS/BSS platform vice president | 2027-03-31 |
| GR-03 | Ransomware through shared services halts OSS/BSS, ERP, and division systems | TC-008, TC-009, NE-008, TF-008 | Offline configuration backups in every region; failover test; tabletop | Group CISO | 2027-03-31 |
| GR-05 | AI in customer-facing or consequential decisions without adequate governance | TC-006, TC-020, NE-012, NE-014, TF-011 | Group AI program conditions (P10) | Group Chief Risk Officer | 2027-03-31 |
| GR-06 | Lawful-intercept compromise or unauthorized activation | TC-013, TC-014 | Isolated SYS-C8 management path; SSI refiling | Carrier Vice President, Network Security and Lawful Intercept | 2026-12-31 |

### Telecom Carrier (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| TC-001 | Known vulnerability in an internet-facing SBC or edge router exploited | Replace or isolate the 9 unsupported SBCs; authenticated scanning; weekly patch tracking | Carrier network engineering vice president | 2027-01-31 |
| TC-002 | Shared local accounts used to reconfigure or wipe access elements, causing an outage including 911 | Named TACACS+ accounts with MFA on every element class | Carrier network engineering vice president | 2027-03-31 |
| TC-003 | Theft of call detail records from mediation and the CDR store | Object-level read logging; collector isolation; exfiltration alerts | Carrier OSS/BSS platform vice president | 2026-12-31 |
| TC-009 | Ransomware encrypts OSS/BSS workloads and regional NOC servers | Offline configuration copies; NOC server hardening; tabletop | Carrier OSS/BSS platform vice president | 2027-03-31 |
| TC-013 | Lawful-intercept system reached through shared management segments in the acquired regions | Isolated management path and jump host for SYS-C8 | Carrier Vice President, Network Security and Lawful Intercept | 2026-12-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| NE-001 | Engineering | Known vulnerability in an SYS-E1 remote access gateway exploited to reach customer networks and the Carrier | Engineering MNO general manager | 2027-03-31 |
| TF-001 | Tower | Lighting alarms disabled or falsified through legacy RMUs | Tower site operations director | 2027-03-31 |
| TF-002 | Tower | Lighting alarms lost when the shared platform is down or isolated, with no written fallback | Tower site operations director | 2026-11-30 |
| TF-014 | Tower | Legacy RMUs that accept the default password taken over (found in P07 testing) | Tower site operations director | 2026-12-31 |

### What the results say
The program is mature where the group built it once: identity, the SOC, the cloud landing zones, and backups. The High risks cluster around **what the divisions share and what the group acquired**, not around any one division's basics:
1. **The management planes** (GR-01). The acquired regions, the Engineering gateways, and the legacy RMUs all expose network control functions through shared credentials or unpatched internet-facing devices, which is the pattern used against U.S. carriers in 2024 and 2025.
2. **The shared service assurance platform** (GR-02). One Carrier-owned platform carries CPNI, Engineering's customer alarms, and tower lighting alarms, with a legacy role that crosses tenants and a disaster recovery path never tested with all three.
3. **AI governance** (GR-05) has fallen behind deployment: the chatbot account recovery pilot and the deposit model's adverse action notices.
4. **Lawful intercept in the acquired regions** (GR-06): a shared management path and stale SSI filings.

Governance gaps (policy drift and undocumented Tower inheritance, GR-10; notification coordination, GR-04) are Moderate at group level. They matter because they hide whether Tower controls actually operate, which is why P07 sampled the Tower division on governance controls.

**New finding from testing.** TF-014 was added on 2026-08-31 after P07 testing on 2026-08-19 found 212 legacy RMUs that accept the manufacturer's default web password. Passwords on all 212 were changed by 2026-09-30 under POAM-022; the risk stays open until web administration is blocked from the internet and the units are replaced.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** management plane remediation in the acquired regions and SBC replacement (GR-01); tenant partitioning of the service assurance platform (GR-02); offline configuration backups (GR-03); group AI program conditions (GR-05); SYS-C8 isolation (GR-06); SIEM onboarding of network elements, gateways, and RMUs (GR-09); legacy RMU replacement (TF-001, TF-014).
- **Accepted (all Low):** TC-026 (encrypted technician tablets), TC-030 (bill print vendor), NE-013 (subcontracted crews), TF-013 (fiber route maps under role-based access).
- **Shared:** TC-023 (DDoS), through the cloud provider's protection and transit scrubbing contracts.
- **Contract actions:** intercompany CPNI and tenant agreements (GR-02); 24-hour incident notice terms for the outsourced contact center and lease management vendors (TC-012, TF-009).
- **Treatment status:** 58 risks are In progress, 12 are Open (treatment approved, work not started), and 4 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The five High group risks were presented on 2026-09-17. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight, the Group CISO's reporting line, and the use of an independent internal audit function).

## 6. Approval
- Board risk committee: approved the group register, the five High group treatment plans, and the funding request, 2026-09-17.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the nine High division risks, 2026-09-17.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-17.
- Next full review: May to July 2027, or sooner after a major change (management plane migration, legacy billing retirement, RMU replacement), an acquisition, or an incident.
