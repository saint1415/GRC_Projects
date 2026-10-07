# Risk Register Report: Cris Santos Company Holdings | Government Services and Facilities | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Government Services and Facilities, Construction, Administrative and Support Services) |
| Focus division | Government Facilities Support (NAICS 561210) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | The risk assessment (RA-3) that state agency contract exhibits require under the SP 800-53 Rev. 5 Moderate baseline; the risk inputs to the Construction division's SP 800-171 assessment |
| Registers | `risk-register.csv` (group), `risk-register-facilities-support.csv`, `risk-register-construction.csv`, `risk-register-janitorial-security.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses; customer site walkthroughs 2026-06-08 to 2026-06-19) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-15 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that operates customers' building systems or holds customer, workforce, or government information in the three divisions, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and network, SYS-G4 ERP and payroll, and SYS-G5, the Integrated Building Operations Platform (IBOP). Division systems are SYS-F1 and SYS-F2, SYS-C1 to SYS-C3, and SYS-J1 to SYS-J3 (`../00_company-facts.md` sections 3 and 7). Physical consequences at customer buildings (doors, environmental conditions) are in scope because they are the main impact of a building systems intrusion.

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. Facilities Support, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services (above all the IBOP), or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not simply the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Life-safety and physical-security risks rated High at a customer building may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), customer site walkthroughs, and interviews with each division's leadership. OT threat events use the building automation and access control scenarios in NIST SP 800-82 Rev. 3.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Group impact reflects enterprise consequences: many customers and regulators at once, loss of federal or DoD award eligibility, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 5 | 14 | 1 | 0 | 20 | n/a |
| Facilities Support | 0 | 2 | 20 | 8 | 0 | 30 | 23 |
| Construction | 0 | 3 | 9 | 6 | 0 | 18 | 11 |
| Janitorial and Security | 0 | 2 | 14 | 2 | 0 | 18 | 15 |
| **All registers** | **0** | **12** | **57** | **17** | **0** | **86** | **49** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Intruder gains IBOP administrator access and changes doors, schedules, and setpoints at many customer buildings | FS-001, FS-002, FS-003, FS-017, FS-030, CN-006, JS-010 | Retire legacy remote access; per-customer just-in-time administration; OT log onboarding | Group CISO | 2027-03-31 |
| GR-02 | Ransomware spreads through shared services into the IBOP and division systems | FS-007, FS-010, FS-020, CN-008, JS-012 | Segment flat sites; replace unsupported workstations; restore tests | Group CISO | 2027-03-31 |
| GR-04 | AI in physical security, building control, and hiring causes unfair, unsafe, or unlawful outcomes | FS-005, FS-006, CN-012, JS-004, JS-005, JS-014, JS-016 | Group AI program conditions (P10) | Group Chief Risk Officer | 2027-03-31 |
| GR-05 | Covered defense information mishandled; loss of DoD award eligibility | FS-015, CN-001, CN-002, CN-003, CN-018 | Enclave migration; SPRS score above 88; C3PAO assessment | Construction division president | 2027-03-31 |
| GR-06 | Covered telecommunications or video equipment found in use | FS-016, CN-010, JS-001 | Confirm the 4 NVRs; extend screening to the installation business | Group procurement director | 2026-11-30 |

### Facilities Support (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| FS-001 | Intruder uses a vendor remote-support tool at an acquired site to change door schedules and setpoints | Remove tools; jump service with MFA and approval at all 37 sites | Group building technology director | 2026-12-15 |
| FS-003 | Stolen or misused global administrator account unlocks doors across many customer tenants | Per-customer roles with just-in-time elevation | Facilities Support security systems director | 2027-03-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| CN-001 | Construction | CUI drawings in the commercial project collaboration SaaS are breached or found by DoD | Construction CUI program manager | 2026-12-31 |
| CN-002 | Construction | No CMMC Level 2 (C3PAO) status for DoD bids after 2026-11-10 | Construction division president | 2027-03-31 |
| CN-018 | Construction | SPRS score overstates implementation | Group General Counsel | 2026-12-31 |
| JS-001 | Janitorial and Security | Covered video equipment at the central monitoring station or in installed systems | Janitorial and Security technology services director | 2026-12-31 |
| JS-009 | Janitorial and Security | Former workers keep customer-site badges and keys | Janitorial and Security operations director | 2026-12-31 |

### What the results say
The program is defined and mostly sound. There are no Very High risks. Identity, the SOC, cloud guardrails, and backups are strong common controls. The High risks cluster around **what the group shares and what it acquired**, not around corporate basics:
1. **The IBOP** (GR-01) is where one weakness reaches hundreds of government buildings. The 37 acquired sites (scenario gap 1) and the standing cross-tenant administrator role (gap 2) are the two paths that turn a single stolen credential into a group-level event.
2. **The newer divisions carry federal contract risks** that the focus division already manages: CUI and CMMC in Construction (GR-05, gap 5) and Section 889 screening in the acquired installation business (GR-06, gap 6).
3. **AI governance** (GR-04) has fallen behind deployment in two divisions (gap 11).
4. **A shared incident** would trigger customer, GSA, DoD, state, and SEC duties at once (GR-03, rated Moderate, gap 10). P08 builds the runbook around this.

Governance gaps 8 and 9 (policy drift and undocumented inheritance) are Moderate at group level (GR-11). They matter because they hide whether Construction and Janitorial and Security controls actually operate, which is why P07 sampled those divisions directly.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q1):** retirement of legacy remote access at the 37 acquired sites and per-customer administration (GR-01); OT segmentation and log onboarding (GR-02, GR-12); the Construction CUI enclave and CMMC Level 2 program (GR-05); the group AI program (GR-04); extension of supply chain screening (GR-06).
- **Accepted (all Low):** FS-025 (PIV sponsorship lapses), FS-029 (CMMS outage), CN-017 (jobsite trailer loss), JS-015 (lost guard tour phone).
- **Avoided:** JS-014. The Group AI council declined 1:N face identification of the public (P10 AI-002).
- **Shared or transferred:** GR-08 and FS-009 (access control vendor dependency), through contract recovery terms and cyber insurance.
- **Treatment status:** 51 risks are In progress, 30 are Open (treatment approved, work not started), and 5 are Closed (the 4 accepted risks and the avoided one).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The five High group risks were presented on 2026-09-15. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight and the Group CISO's reporting line).

## 6. Approval
- Board risk committee: approved the group register, the five High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the seven High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-16.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
