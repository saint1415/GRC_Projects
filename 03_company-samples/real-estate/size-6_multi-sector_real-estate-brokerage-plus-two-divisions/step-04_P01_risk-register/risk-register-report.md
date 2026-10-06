# Risk Register Report: Cris Santos Company Holdings | Real Estate | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Real Estate, Finance and Insurance, Construction) |
| Focus division | Residential Brokerage (NAICS 531210) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | The written risk assessment that Home Loans and Title each need under the FTC Safeguards Rule (16 CFR 314.4(b) and (b)(1)): criteria for rating risks, criteria for assessing confidentiality, integrity, and availability, and how each risk is mitigated or accepted |
| Registers | `risk-register.csv` (group), `risk-register-brokerage.csv`, `risk-register-mortgage-title.csv`, `risk-register-homebuilding.csv` |
| Fieldwork | 2026-05-04 to 2026-07-24 (group and division risk analyses) |
| Prepared | 2026-07-24 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-17 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments and acceptances the same week |

## 1. Scope and risk framing
**Scope.** Every system that holds customer information, client data, or payment instructions in the three divisions, plus the corporate shared services they depend on: identity (SYS-G1), the SOC (SYS-G2), the cloud platform and Group Data Platform (SYS-G3), email (SYS-G4), and the treasury and payments hub (SYS-G5). Division systems are SYS-B1 to SYS-B4, SYS-M1 and SYS-M2, and SYS-H1 to SYS-H3 (`../00_company-facts.md` section 3).

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. Each division security and compliance lead maintains one. The Residential Brokerage, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not as the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason (for group risks, the Group Chief Risk Officer) |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Risks to customer funds rated High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the BIA (P05), the gap analyses (P03), the common control assessment (P07), the 12-month fraud history (412 stopped payee-change attempts; 11 loss events), and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**. Existing controls lower the likelihood of adverse impact: for example, Title's callback and dual approval make a diverted title disbursement less likely to succeed than a buyer wire sent from a hijacked agent mailbox.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). Group impact reflects enterprise consequences: two financial institutions' FTC duties, state notices in up to 8 states, SEC disclosure, lender and investor relationships, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 5 | 11 | 3 | 0 | 19 | n/a |
| Residential Brokerage | 0 | 3 | 17 | 6 | 0 | 26 | 21 |
| Mortgage and Title | 0 | 2 | 12 | 4 | 0 | 18 | 18 |
| Homebuilding | 0 | 3 | 8 | 5 | 0 | 16 | 13 |
| **All registers** | **0** | **13** | **48** | **18** | **0** | **79** | **52** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Business email compromise diverts closing, escrow, payout, or trade partner funds in any division | BR-001, BR-002, BR-006, BR-007, BR-008, BR-022, MT-001, MT-002, MT-003, HB-001, HB-006 | Agent MFA; group payee verification for every payment type through SYS-G5; payee-change alerts | Group CISO | 2027-01-31 |
| GR-02 | Contractor agent identities compromised or kept after departure | BR-003, BR-004, BR-005, BR-010 | MFA enforcement; automated removal; app protection; transaction-team visibility | Group identity director | 2027-03-31 |
| GR-03 | Ransomware spreads through shared services and halts closings in all divisions | BR-015, MT-010, HB-008 | Segmentation; legacy tenant migration; cross-division tabletop | Group CISO | 2027-03-31 |
| GR-07 | AI in housing and credit decisions produces unlawful disparities or unreliable valuations | BR-016, BR-017, BR-019, BR-021, MT-004, MT-005, MT-016 | Group AI governance program (P10) | Group Chief Risk Officer | 2027-03-31 |
| GR-13 | Smart-home access rights let unauthorized people unlock or control homes | HB-003, HB-004 | Remove builder roles; rotate passcodes; enforce handover | Homebuilding chief operating officer | 2026-12-31 |

### Residential Brokerage (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| BR-001 | A buyer wires deposit or cash to close to a fraudster after spoofed instructions from a compromised agent mailbox | Agent MFA; block instruction-like content from agent mail to buyers; buyer warnings at every milestone | Residential Brokerage security and compliance lead | 2026-12-31 |
| BR-003 | Password-only contractor agent accounts taken over | Enforce MFA and disable non-compliant accounts; block legacy protocols | Group identity director | 2026-12-31 |
| BR-016 | Tenant screening recommendations deny or condition applicants unlawfully or on wrong records (AI-001) | Disparity testing, individualized review, configuration changes (P10) | Residential Brokerage president of property management | 2027-01-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| MT-001 | Mortgage and Title | A title disbursement is diverted by a spoofed payoff letter or changed proceeds instructions | President, Title | 2027-01-31 |
| MT-004 | Mortgage and Title | AVM estimates used in credit decisions lack the quality control 12 CFR 1026.42(i) requires | President, Mortgage | 2027-01-31 |
| HB-001 | Homebuilding | Spoofed trade partner email changes bank details and payments are diverted | Homebuilding chief financial officer | 2026-11-30 |
| HB-003 | Homebuilding | Builder administrator access kept on about 3,100 closed homes is misused | Homebuilding chief operating officer | 2026-11-30 |
| HB-004 | Homebuilding | A shared installer passcode lets someone take over hubs installed in 2023 and 2024 | Homebuilding chief operating officer | 2026-12-31 |

### What the results say
The program is defined and mostly sound. There are no Very High risks, and the group already runs a 24x7 SOC, PAM, quarterly access certification, immutable backups, and strong title wire controls. The High risks cluster where **money and identities cross division lines**:
1. **Business email compromise** (GR-01) is the group's top risk. Title's controls work: the portal, callback, dual approval, and hardware-key release. But an attacker picks the weakest door: a password-only agent mailbox (scenario gap 1), a brokerage refund, an owner payout, or a trade partner bank change with no callback (gap 2). The 12-month history (11 losses, $3.0 million, $1.3 million recovered) shows the attempts are constant.
2. **Contractor agent identities** (GR-02) are the largest population the group does not employ: about 52,000 people on personal devices, of whom about 9,900 still have no MFA and departures are removed late.
3. **AI in consequential decisions** (GR-07) has outrun its testing: tenant screening, the pre-qualification model, and the AVM are in production without disparity or sample testing (gap 6).
4. **Homebuilding's physical-world risk** (GR-13) is new to the group: smart-home access is a safety issue, not only a data issue (gap 8).

Shared-service governance gaps are Moderate at group level: undocumented affiliate data flows (GR-05, gap 4), Homebuilding outside common controls (GR-06, gap 5), unmonitored application logs (GR-09, gap 3), the untested notification matrix (GR-04, gap 7), the intercompany agreement (GR-11), and retention (GR-12, gap 9). They matter because they hide whether division controls actually operate, which is why P07 sampled Homebuilding governance and the brokerage's payment controls most heavily.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** agent MFA enforcement and automated agent removal (GR-02); group payee verification for every division payment type (GR-01); application log onboarding to the SIEM (GR-09); Homebuilding migration to group identity and email (GR-06); group AI governance program (GR-07); smart-home remediation (GR-13).
- **Accepted (6 risks):** GR-15 (hurricane, Moderate, accepted by the Group Chief Risk Officer with existing remote work); BR-025 (encrypted laptop theft, Low); BR-026 and HB-011 (processor-hosted payment pages, Low); HB-013 (hurricane at sites, Moderate, accepted by the Homebuilding president); HB-014 (schedule optimization AI with superintendent approval, Low).
- **Transferred in part:** GR-19 (funds transfer fraud beyond the $10 million insurance sublimit) is shared through insurance and reviewed at renewal.
- **Contract actions:** amend the intercompany services agreement (GR-11, MT-013); align the title production vendor RTO (MT-008); vendor access through PAM (MT-015).
- **Treatment status:** 43 risks are In progress, 30 are Open (treatment approved, work not started), and 6 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The five High group risks were presented on 2026-09-17, together with the Qualified Individual's annual written reports to the boards of Home Loans and Title (16 CFR 314.4(i)), which draw on the Mortgage and Title register and the group risks that affect both institutions. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here: the board risk committee's oversight and the Group CISO's reporting line.

## 6. Approval
- Board risk committee: approved the group register, the five High group treatment plans, and the funding request, 2026-09-17.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the eight High division risks, 2026-09-17.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-17.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident (16 CFR 314.4(b)(2)).
