# Risk Register Report: Cris Santos Company Holdings | Admin and Support Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 core employees plus about 230,000 temporary associates a week; Administrative and Support Services, Professional Services, Health Care) |
| Focus division | Staffing (NAICS 561320) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A), for Home Health (covered entity) and for Consulting and corporate as business associates; the CSF 2.0 ID.RA outcomes used as the Staffing benchmark (P03) |
| Registers | `risk-register.csv` (group), `risk-register-staffing.csv`, `risk-register-consulting.csv`, `risk-register-home-health.csv` |
| Fieldwork | 2026-05-01 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-10 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that holds worker, candidate, client, or patient data in the three divisions, plus the corporate shared services they depend on: the group identity platform (SYS-G1), the group SOC (SYS-G2), the group cloud platform and network (SYS-G3), and the Group Workforce Platform (SYS-G4). Division systems are SYS-D1 to SYS-D3 (`../00_company-facts.md` sections 3 and 7).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. Staffing, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact. They are not simply the highest division rating.

**Risk tolerance and who can accept risk** (recorded in `../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Patient-safety risks at High may not be accepted, and neither may risks that leave workers unpaid. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), the 2025 payroll fraud record, and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Group impact reflects enterprise consequences: workers in many states at once, several regulators, client loss, and SEC disclosure.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 5 | 12 | 3 | 0 | 20 | n/a |
| Staffing | 0 | 3 | 16 | 7 | 0 | 26 | 15 |
| Consulting | 0 | 2 | 7 | 5 | 0 | 14 | 7 |
| Home Health | 0 | 2 | 13 | 3 | 0 | 18 | 10 |
| **All registers** | **0** | **12** | **48** | **18** | **0** | **78** | **32** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Theft of worker PII and Home Health patient data from the GWP | ST-001 | Remove patient identifiers from visit-pay data; retention purge; role tightening; SaaS export alerts | Group CISO | 2027-03-31 |
| GR-02 | Ransomware on the payroll engine or shared services halts pay for every division | ST-005, HH-002 | Isolated recovery test; exercise the repeat-payroll procedure; cross-division tabletop | Group payroll director | 2027-03-31 |
| GR-04 | AI hiring and decision tools produce discriminatory outcomes or breach state AI laws | ST-003, ST-009, ST-023, CN-007, CN-008, HH-010, HH-011 | Group AI governance program (P10) | Group Chief Risk Officer | 2027-01-31 |
| GR-05 | Payroll diversion at scale through self-service and the associate service center | ST-002, ST-016 | Passkey or app authenticator; out-of-band confirmation and hold on first-time bank changes | Group payroll director | 2027-03-31 |
| GR-10 | Home Health patient data disclosed to corporate payroll without BAA coverage or minimum-necessary limits | HH-001 | Anonymous visit IDs; purge; BAA amendment | Group Chief Privacy Officer | 2026-12-31 |

### Staffing (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| ST-001 | Bulk export of associate and candidate PII through a compromised recruiter or payroll account | Export limits per role; SaaS export alerts; session token protection | Staffing security and compliance lead | 2027-03-31 |
| ST-002 | Fraudulent direct deposit changes divert associate pay (690 cases, about $1.9 million, in 2025) | Passkey or app authenticator; 3-day hold and out-of-band confirmation | Group payroll director | 2027-03-31 |
| ST-003 | AI ranking add-on screens out protected groups at higher rates | Group-wide adverse impact monitoring; turn off auto-advance; candidate notices | Staffing talent acquisition vice president | 2026-12-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| CN-001 | Consulting | Client-issued EHR accounts left active after consultant roll-off are used to access PHI | Consulting HIPAA compliance officer | 2027-03-31 |
| CN-002 | Consulting | Client PHI in the engagement repository and on laptops exposed through sharing links or loss | Consulting security and compliance lead | 2027-03-31 |
| HH-001 | Home Health | Patient names and addresses disclosed to corporate payroll beyond what pay needs | Home Health HIPAA Privacy Officer | 2026-12-31 |
| HH-002 | Home Health | Ransomware enters through an unprotected field tablet and spreads to agency offices | Home Health security and compliance lead | 2027-03-31 |

### What the results say
The program is sound where the group has invested longest: identity, the SOC, backups, and tokenization in the payroll engine. There are no Very High risks. The High risks cluster around **what the group shares** and **what it acquired**:
1. **The Group Workforce Platform** (GR-01, GR-02, GR-05, GR-10) concentrates every division's worker data and pay. Its two sharpest problems are patient data that should never have entered payroll (scenario gap 1) and a phishable SMS code that guards bank changes for 1.1 million people (gap 2).
2. **AI in hiring** (GR-04) now touches every division's recruiting, and the 2027-01-01 Colorado and California dates turn a fairness risk into a compliance deadline (gap 4).
3. **Consulting's business associate access** (CN-001, CN-002) is a client-trust risk: the group would be the source of a hospital client's breach (gap 7).
4. **Home Health** (HH-002, and the Moderate group risk GR-06) is still being brought into group controls three years after acquisition (gaps 3 and 6).

Shared-incident notification (GR-03) is Moderate at group level, but it is the risk the P08 runbook addresses most directly, because a GWP breach would set E-Verify, state, HIPAA, client, and SEC clocks running at once (gap 5).

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** visit-pay redesign and purge (GR-10, GR-01); self-service authentication upgrade (GR-05); isolated payroll recovery testing (GR-02); group AI governance program (GR-04); Home Health endpoint migration and SIEM onboarding (GR-06, GR-12); kiosk segmentation at 61 branches (GR-13); retention automation (GR-14); MSP SOC 2 program (GR-15).
- **Accepted (all Low):** ST-020 (encrypted recruiter device loss), CN-012 (encrypted consultant laptop loss), HH-014 (paper downtime forms).
- **Contract actions:** amend the Home Health intercompany BAA (GR-10); subcontractor BAAs for Consulting's independent consultants (CN-009); breach notice terms in every tier 1 vendor contract (GR-08).
- **Treatment status:** 57 risks are In progress, 18 are Open (treatment approved, work not started), and 3 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The five High group risks were presented on 2026-09-10. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight, the Group CISO's reporting line, and the use of an independent internal audit function).

## 6. Approval
- Board risk committee: approved the group register, the five High group treatment plans, and the funding request, 2026-09-10.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the seven High division risks, 2026-09-10.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-08 to 2026-09-10.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
