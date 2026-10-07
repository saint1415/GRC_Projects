# Risk Register Report: Cris Santos Company Holdings | Financial Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Financial Services, Information, Professional Services) |
| Focus division | Payment Processing (NAICS 522320), a PCI DSS Level 1 service provider and bank service provider |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | The written risk assessment in the FTC Safeguards Rule, 16 CFR 314.4(b), for the Payment Processing and Software divisions; the PCI DSS targeted risk analyses draw on it (12.3.1) |
| Registers | `risk-register.csv` (group), `risk-register-payment-processing.csv`, `risk-register-software.csv`, `risk-register-consulting.csv` |
| Fieldwork | 2026-05-01 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-10 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that stores, processes, or transmits cardholder data or other customer information in the three divisions, the systems that can affect their security, and the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 data centers and landing zones, SYS-G4 data platform, and SYS-G5 email (`../00_company-facts.md` section 3).

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. Each division security and compliance lead keeps one. Payment Processing, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not copied from the highest division rating.

**Written criteria (16 CFR 314.4(b)(1)).** The likelihood and impact scales, the tables below, and the acceptance rules are the evaluation and categorization criteria the Safeguards Rule asks for. Impact is scaled to the P05 BIA categories.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

A High risk of cardholder data compromise may not be accepted. It must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the BIA (P05), the gap analyses (P03), the control assessment (P07), card brand and sector threat intelligence, and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories. Group impact reflects enterprise consequences: card brand and sponsor bank actions, several regulators at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results
| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 12 | 2 | 0 | 18 | n/a |
| Payment Processing | 0 | 2 | 17 | 11 | 0 | 30 | 16 |
| Payments Software Platform | 0 | 3 | 10 | 5 | 0 | 18 | 9 |
| Merchant Consulting | 0 | 1 | 8 | 5 | 0 | 14 | 7 |
| **All registers** | **0** | **10** | **47** | **23** | **0** | **80** | **32** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | E-commerce skimming on storefront pages or around the hosted payment fields | SW-001, SW-002, PP-003 | Script inventory and tamper-detection for all themes; marketplace script review; content security policy defaults | Software division CISO | 2027-03-31 |
| GR-02 | A cross-division access path (consulting identity provider, ISV support console) reaches cardholder data | PP-001, PP-002, MC-001, MC-002, MC-011, SW-003 | Block SMS for CDE access; migrate consulting users to SYS-G1; remove bulk export; SIEM onboarding; mask ISV keys | Group CISO | 2027-03-31 |
| GR-06 | Ransomware through shared services halts authorization or settlement | PP-021 | Separate administration tiers per data center; settlement restore tests; ransomware tabletop | Group CISO | 2027-03-31 |
| GR-08 | Gateway or cloud region outage stops e-commerce authorizations for more than 4 hours | SW-004, PP-026 | Gateway failover test, then active-active | Software division chief technology officer | 2027-06-30 |

### Payment Processing (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| PP-001 | Federated consulting account taken over through SMS code relay and used to bulk export dispute case files with PAN | Block SMS for CDE access; remove bulk export; SIEM detection (GR-02) | Payment Processing division CISO | 2026-12-31 |
| PP-010 | PAN in dispute evidence held in consulting mailboxes is exposed | Evidence upload portal; mailbox purge; PAN blocking on consulting mail (GR-09) | Merchant Consulting dispute services director | 2027-01-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| SW-001 | Software | Malicious script in a merchant-customized storefront theme | Software division CISO | 2027-03-31 |
| SW-002 | Software | Compromised marketplace app injects scripts into many storefronts | Software division marketplace director | 2027-03-31 |
| SW-004 | Software | Gateway region failure longer than 4 hours with untested failover | Software division chief technology officer | 2027-06-30 |
| MC-001 | Merchant Consulting | Dispute analyst's SMS code relayed and the session used inside the CDE | Merchant Consulting security and compliance lead | 2027-03-31 |

### What the results say
The program is mature where the group built it: there are no Very High risks, and the processor's own technical core (segmentation, tokenization, HSM key management, active-active recovery) produces only Moderate and Low risks. The High risks sit at **the edges between divisions**:
1. **The browser around the payment fields** (GR-01). The processor protects the fields; the Software division owns the storefront page around them and covers only the standard template (scenario gap 3).
2. **People and pages from other divisions inside the CDE** (GR-02). The acquired consulting firm's identity provider, with SMS codes, is federated into the CDE, and every dispute analyst can bulk export case files (gap 1).
3. **Shared infrastructure** (GR-06, GR-08). The data centers and the gateway serve more than one division, so one failure or one ransomware event hits several revenue lines and several notice duties at once (gaps 7 and 8).

Notification (GR-03), AI governance (GR-04), supplement drift (GR-05), and PAN outside the CDE (GR-09) are Moderate at group level. They matter because each one would turn a contained incident into a regulatory, card brand, or sponsor bank problem, which is why the P07 assessment sampled Merchant Consulting and the notification controls more heavily.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** consulting identity migration and SMS removal (GR-02); storefront script control and marketplace review (GR-01); gateway failover and active-active design (GR-08); administration tiering per data center (GR-06); evidence upload portal and PAN purge (GR-09); group AI governance program (GR-04).
- **Before the ROC fieldwork starts on 2026-11-02:** remove the bulk export permission (PP-002), record all four sponsor banks' contacts (PP-007), and agree compensating controls with the QSA for anything still open (GR-10, PP-019).
- **Accepted (all Low):** GR-15 (hurricane, covered by the second data center and remote work), PP-028 and MC-013 (encrypted laptop theft), SW-016 (engineer production access, covered by PAM).
- **Contract actions:** intercompany responsibility matrix between the processor, the gateway, and consulting (SA-9); ISV responsibility matrix (PCI DSS 12.9.2; SW-011); group engagement letter template for consulting (MC-012).
- **Treatment status:** 50 risks are In progress, 26 are Open (treatment approved, work not started), and 4 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks were presented on 2026-09-10. The Group CISO's annual written report to the board as Qualified Individual (16 CFR 314.4(i)) draws on the same register, and the Reg S-K Item 106 disclosure in the next annual report describes this risk management process and the board risk committee's oversight.

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, and the funding request, 2026-09-10.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the six High division risks, 2026-09-10.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-08 to 2026-09-10.
- Next full review: May to July 2027, or sooner after a significant change, acquisition, or incident (16 CFR 314.4(b)(2); PCI DSS 12.5.3).
