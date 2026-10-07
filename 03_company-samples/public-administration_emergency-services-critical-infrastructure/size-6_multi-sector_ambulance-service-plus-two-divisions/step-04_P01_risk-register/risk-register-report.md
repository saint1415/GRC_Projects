# Risk Register Report: Cris Santos Company Holdings | Emergency Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Emergency Services, Health Care, Administrative and Support Services) |
| Focus division | Ambulance Services (NAICS 621910), a HIPAA covered entity |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A), for each covered entity (Ambulance Services and Urgent Care) and for BDS and corporate as business associates |
| Registers | `risk-register.csv` (group), `risk-register-ambulance.csv`, `risk-register-urgent-care.csv`, `risk-register-bds.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses); P07 findings added 2026-08-28 |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-16 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that creates, receives, maintains, or transmits ePHI in the three divisions, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and network, and SYS-G4 corporate SaaS. Division systems are SYS-D1 to SYS-D4 (`../00_company-facts.md` section 3). The dispatch risks also cover safety: a dispatch failure can delay an emergency response even when no data is lost.

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. Each division security and compliance lead maintains one. Ambulance Services, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to it. Group risks are rated on their own group-level likelihood and impact, not copied from the highest division rating.

**Risk tolerance and who can accept risk** (also in `../00_company-facts.md` section 7 and POL-01 4.4):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Risks that could delay an emergency response or harm a patient may not be accepted at High. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the cloud mapping (P04), the gap analyses (P03), the common control assessment (P07), and interviews with each division's leadership and the communications center supervisors.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Group impact reflects enterprise consequences: several regulators and clients at once, county agreements, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 13 | 1 | 0 | 18 | n/a |
| Ambulance Services | 0 | 2 | 14 | 12 | 0 | 28 | 15 |
| Urgent Care | 0 | 2 | 7 | 6 | 0 | 15 | 6 |
| Billing and Dispatch Services | 0 | 4 | 8 | 6 | 0 | 18 | 14 |
| **All registers** | **0** | **12** | **42** | **25** | **0** | **79** | **35** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Prolonged loss of the single CAD instance halts dispatch for the Ambulance division and 14 client agencies | AMB-001, BDS-001 | Warm CAD standby in provider B; failover tests twice a year; multi-day manual dispatch drills | Group dispatch and clinical platforms director | 2027-06-30 |
| GR-02 | Ransomware spreads between the CAD and the revenue cycle file transfer servers and steals data from several divisions and clients | AMB-004, BDS-003 | Move both into separate landing-zone accounts; remove the shared subnet | Group cloud platform director | 2027-01-31 |
| GR-04 | AI used in dispatch, clinical, and billing decisions without adequate governance | AMB-011, AMB-012, UC-004, UC-005, BDS-004, BDS-010 | Group AI governance program (P10) | Group Chief Risk Officer | 2027-03-31 |
| GR-05 | Attacker uses the CAD vendor support path to gain CAD administrator access | BDS-002 | Remove standing vendor accounts; vendor access only through PAM | Group identity director | 2026-11-30 |

### Ambulance Services (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| AMB-001 | CAD is unavailable for days and crews run on radio and paper, delaying responses | Multi-day manual dispatch drill with counties; CAD standby (GR-01) | Ambulance Services chief operating officer | 2027-06-30 |
| AMB-002 | Attacker takes over vehicle routers through exposed remote administration and reaches the CAD tunnel (**new from P07**: 41 routers with the factory default password) | Close remote administration fleet-wide; configuration baseline; per-device certificates | Ambulance Services fleet technology director | 2026-12-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| UC-001 | Urgent Care | A breach at the 46 acquired clinics goes undetected for months | Urgent Care chief information officer | 2027-06-30 |
| UC-005 | Urgent Care | The proposed symptom checker sends a patient with an emergency to urgent care (treatment: avoid, do not deploy until P10 conditions are met) | Urgent Care chief medical officer | 2027-03-31 |
| BDS-001 | BDS | CAD outage stops dispatch for 14 client agencies at once | BDS vice president of communications operations | 2027-06-30 |
| BDS-002 | BDS | CAD vendor support accounts are used to take over the CAD | BDS security and compliance lead | 2026-11-30 |
| BDS-003 | BDS | Attacker steals client claim files from the revenue cycle file transfer servers | BDS revenue cycle president | 2027-01-31 |
| BDS-004 | BDS | AI triage processes client agencies' caller audio without authorization and under-triages some callers | BDS vice president of communications operations | 2026-11-30 |

### What the results say
The program is mostly sound. There are no Very High risks, and most control families work: a 24x7 SOC, PAM for cloud administrators, MFA, quarterly access certification, and immutable backups. The High risks cluster around **the dispatch platform the divisions share**, not around any one division's basics:
1. **One CAD, one provider, one legacy account** (GR-01, GR-02). The CAD is the group's tightest recovery requirement (P05: MTD 2 hours), and it sits in the one cloud account that never moved into the landing zone (scenario gaps 1 and 3).
2. **Access paths outside group identity** (GR-05, AMB-002). The CAD vendor's standing accounts and the vehicle routers bypass the controls that protect everything else (gaps 2 and 4).
3. **AI governance** (GR-04) has fallen behind deployment in two divisions (gap 6).

Gaps 5, 7, 8, and 9 (possible CJI, multi-party notification, Urgent Care drift, and card payments) are Moderate at group level (GR-06, GR-03, GR-10 and GR-11, GR-14). They matter because each involves a third party's rules: a county's CJIS Systems Agency, clients' BAAs, or card brand rules.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** CAD move into the landing zone and separation from billing servers (GR-02); provider B CAD standby (GR-01); vendor access through PAM (GR-05); fleet device management (GR-09); group AI governance program (GR-04); legacy clinic migration (GR-11); tone-masked card payments (GR-14).
- **Accepted (all Low):** AMB-006 (encrypted tablet loss), AMB-027 (printed face sheets), UC-012 (encrypted laptop theft).
- **Avoided:** UC-005 (the symptom checker is not deployed until its conditions are met).
- **Contract actions:** amend the CAD vendor BAA for client agencies and notify clients (BDS-004, GR-17); client and county notice register (GR-03, BDS-007, AMB-013).
- **Treatment status:** 62 risks are In progress, 14 are Open (treatment approved, work not started), and 3 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks were presented on 2026-09-16. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight and the Group CISO's reporting line).

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, and the funding request, 2026-09-16.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the eight High division risks, 2026-09-16.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-16.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
