# Risk Register Report: Cris Santos Company Holdings | Finance and Insurance | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded bank holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Finance and Insurance, Information, Real Estate) |
| Focus division | Banking: Cris Santos Bank, N.A., an OCC-supervised national bank and a covered bank under 12 CFR 30 App. D |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | The risk assessment the bank must perform under 12 CFR 30 App. B III.B, and the holding company's under 12 CFR 225 App. F III.B for its nonbank subsidiaries; input to the bank's risk profile under App. D II.C.2(b) |
| Registers | `risk-register.csv` (group), `risk-register-banking.csv`, `risk-register-financial-software.csv`, `risk-register-commercial-real-estate.csv` |
| Fieldwork | 2026-05-01 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads; challenged by the Head of Technology and Cyber Risk (second line) |
| Approved | 2026-09-10 by the holding company board risk committee (group register and all High risks) and the bank board risk committee (bank register); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that holds or processes customer information, payment instructions, or client institution data in the three divisions, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 hybrid infrastructure, and SYS-G4 email and collaboration. Division systems are SYS-B1 to SYS-B4, SYS-S1 and SYS-S2, and SYS-R1 and SYS-R2 (`../00_company-facts.md` sections 3 and 7).

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. Each division security and compliance lead maintains one. Banking, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back. Group risks are rated on their own group-level likelihood and impact, not by copying the highest division rating.

**Three lines.** Risk owners are first-line executives. The Head of Technology and Cyber Risk (second line, reporting to the Group Chief Risk Officer) challenged every High rating and every acceptance. Group internal audit (third line) did not rate risks; its P07 findings were inputs.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the holding company board risk committee (and the bank board risk committee for bank risks); temporary only, with a dated plan |
| Very High | Board risk committee only |

The bank's risk appetite statement (12 CFR 30 App. D II.E) sets two cyber limits that this register is measured against: no High cyber risk may remain untreated for more than two quarters, and annual fraud losses from payment-instruction fraud must stay under $25 million. Customer-harm and payment-integrity risks rated High may not be accepted; they must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), and interviews with each division's leadership. Sector threats come from the vertical overlay: business email compromise and payment fraud lead the list.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Group impact reflects enterprise consequences: several regulators at once, client institutions, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 5 | 11 | 4 | 0 | 20 | n/a |
| Banking | 0 | 2 | 15 | 11 | 0 | 28 | 15 |
| Financial Software | 0 | 3 | 10 | 5 | 0 | 18 | 13 |
| Commercial Real Estate | 0 | 1 | 6 | 7 | 0 | 14 | 9 |
| **All registers** | **0** | **11** | **42** | **27** | **0** | **80** | **37** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Payment-instruction fraud succeeds in one or more divisions | BR-002, BR-028, FS-003, FS-006, RR-001, RR-002, RR-011 | One group callback standard; CRE funding through the bank's verified-instruction service; mandatory business payment MFA; vendor-impersonation training | Group Chief Risk Officer | 2027-03-31 |
| GR-02 | Stolen workforce session tokens move an attacker across shared identity and email | BR-018, FS-001, FS-016, RR-003 | Device-bound sessions of 8 hours or less; step-up for sensitive console actions; token-replay detection | Group CISO | 2026-12-31 |
| GR-04 | The digital banking platform is compromised or down, hitting the bank and 310 client institutions at once | BR-003, BR-004, FS-001, FS-002, FS-004 | Tenant-scoped support access; hot gateway standby; failover tests | Financial Software division president | 2027-03-31 |
| GR-05 | AI used in credit decisions produces unexplained or unfair outcomes | BR-010, BR-011, FS-008, FS-009 | Group AI program conditions (P10) | Group Chief Risk Officer | 2027-03-31 |
| GR-06 | Ransomware halts core and payments in the group data centers | BR-001 | Isolated recovery environment; quarterly core restore tests | Group CISO | 2027-06-30 |

### Banking (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| BR-001 | Ransomware encrypts core and payments servers | Isolated recovery environment; quarterly core restore test | Group CISO | 2027-06-30 |
| BR-010 | AI credit model adverse action reasons do not match its cash-flow drivers (12 CFR 1002.9(b)(2)) | Remap reason codes; corrected notices; validation re-test | Bank consumer and small business lending executive | 2026-11-30 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| FS-001 | Financial Software | A stolen support session reads every tenant's configuration through the support console | Head of Digital Banking Platform | 2026-12-31 |
| FS-002 | Financial Software | A tenant isolation defect exposes one client's customers to another | Financial Software chief technology officer | 2027-03-31 |
| FS-008 | Financial Software | The cash-flow data service drives client credit decisions without developer documentation or fairness testing | Financial Software data services lead | 2026-12-31 |
| RR-001 | Commercial Real Estate | A loan is funded to an attacker's account on spoofed or compromised-mailbox instructions | Director of loan closing and funding | 2026-11-30 |

### What the results say
The bank's own program is mature. It has only 2 High risks, and its payment controls (dual control, callbacks to independently verified numbers, a fraud model) are strong. The High risks cluster around **what the group shares and what the newer divisions do differently**:
1. **Shared identity and email** (GR-02). One stolen session reaches every division's systems for up to 12 hours, including a support console that can read every platform tenant (FS-001).
2. **Payment-instruction fraud outside the bank's controls** (GR-01). The bank's callback standard does not bind CRE Lending, an affiliate that funds loans on emailed instructions (RR-001, scenario gap 1). When CRE Lending is fooled, the bank's controls see a legitimate customer request.
3. **Concentration in one platform** (GR-04). The bank and 310 client institutions share SYS-S1, so a platform event is both a bank notification incident question and a bank service provider notice event (scenario gaps 3 and 6).
4. **AI in credit decisions** (GR-05). The bank's model and the data service sold to client banks share the same cash-flow attributes and the same weakness: reason codes and documentation lag the model (scenario gap 4).

Governance gaps (division drift, affiliate oversight, cross-division notification) are Moderate at group level (GR-03, GR-08, GR-09). They matter because they hide whether controls in the newer divisions actually operate, which is why P07 sampled Commercial Real Estate even though it has not been assessed before.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** session binding and token-replay detection (GR-02); one callback standard and the verified-instruction service for CRE funding (GR-01); support console redesign and hot gateway standby (GR-04); group AI program conditions (GR-05); isolated recovery environment for core (GR-06).
- **Accepted (all Low):** BR-020 (encrypted laptop loss), BR-027 (ATM skimming with processor monitoring), FS-012 (engineer production access under PAM), FS-013 (coding assistant under enterprise terms), RR-012 (single alarm monitoring vendor with two monitoring centers).
- **Contract actions:** amend the 2021 intercompany services agreement and treat affiliates as critical vendors (GR-09, BR-013); offer credit unions the same notice terms as banks (FS-014).
- **Treatment status:** 68 risks are In progress, 7 are Open (treatment approved, work not started), and 5 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the holding company board risk committee each quarter. Bank risks also feed the bank's risk profile, which independent risk management compares to the risk appetite statement and reports to the bank board risk committee at least quarterly (12 CFR 30 App. D II.G.3). The five High group risks were presented to both committees on 2026-09-10. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (both board risk committees' oversight and the Group CISO's reporting lines).

## 6. Approval
- Holding company board risk committee: approved the group register, the five High group treatment plans, and the funding request, 2026-09-10.
- Bank board risk committee: approved the bank register and the bank's High treatment plans, 2026-09-10.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the six High division risks, 2026-09-10.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-08 to 2026-09-10.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
