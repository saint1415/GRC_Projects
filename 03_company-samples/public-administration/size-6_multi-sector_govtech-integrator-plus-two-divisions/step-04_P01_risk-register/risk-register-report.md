# Risk Register Report: Cris Santos Company Holdings | Public Administration | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Public Administration, Professional Services, Information) |
| Focus division | GovTech Integration (NAICS 541512), a private contractor hosting systems for state and local agencies |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | SP 800-53 RA-3 required by agency contracts; the risk assessment inputs agencies expect under CJISSECPOL v6.1 RA-3 and Pub. 1075; the risk assessment the IT Consulting CUI enclave needs for SP 800-171 Rev. 2 3.11.1; the risk analysis for the IEP's HIPAA business associate work (45 CFR 164.308(a)(1)(ii)(A)) |
| Registers | `risk-register.csv` (group), `risk-register-govtech.csv`, `risk-register-it-consulting.csv`, `risk-register-govsoftware.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-15 by the board risk committee (group register, all High risks, and the Very High risk); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that holds or processes agency, federal, or customer data in the three divisions, plus the corporate shared services they depend on: the group identity platform (SYS-G1), the group SOC (SYS-G2), the group cloud platform (SYS-G3), and corporate SaaS (SYS-G4). Division systems are SYS-D1 to SYS-D8 (`../00_company-facts.md` section 3). It also covers contract risk: for a government contractor, a failed CJIS audit or IRS review can end a contract as surely as an outage.

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. GovTech Integration, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to it. Group risks are rated on their own group-level likelihood and impact, not copied from the highest division rating. For example, IC-004 (no CMMC status at Phase 2) is High for IT Consulting, but GR-06 is Moderate for the group, because DoD work is about 10% of one division's revenue.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

A risk that would breach a CJIS Security Addendum, Pub. 1075 Exhibit 7, or DFARS 252.204-7012 term may not be accepted at any level. It must be treated, or the regulated data removed.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), agency audit and review letters, and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). Impact on agencies and on the people in their records counts, not only impact on the group. Group impact reflects enterprise consequences: several agencies and regulators at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 6 | 11 | 3 | 0 | 20 | n/a |
| GovTech Integration | 0 | 6 | 18 | 6 | 0 | 30 | 17 |
| IT Consulting | 1 | 2 | 10 | 5 | 0 | 18 | 8 |
| Government Software Products | 0 | 3 | 8 | 7 | 0 | 18 | 11 |
| **All registers** | **1** | **17** | **47** | **21** | **0** | **86** | **36** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Ransomware spreads through shared services and exfiltrates CJI and FTI from several divisions | GT-001, GT-002, IC-001, SW-002 | Retire the directory trust; full-scale restore exercise; bulk-read alerts; cross-division tabletop | Group CISO | 2027-03-31 |
| GR-02 | Unscreened shared-service or subcontractor staff with CJI or FTI access found in a CSA audit or IRS review | GT-004, GT-005, GT-022, SW-004 | One group screening register; suspend unscreened access by 2026-10-31 | Group CISO | 2026-12-31 |
| GR-03 | A cross-division incident misses an agency, DoD, or SEC notice clock | GT-006, GT-019, IC-005, SW-006 | Complete and exercise the group notification matrix (P08) | Group General Counsel | 2026-12-15 |
| GR-04 | AI in public benefit and criminal justice work shapes decisions about people without adequate governance | GT-008, GT-009, GT-025, IC-007, SW-003, SW-013 | Group AI program (P10) | Group Chief Risk Officer | 2027-03-31 |
| GR-05 | Attackers use the acquired consulting firm's estate to reach group systems | IC-001, IC-003, IC-013 | Phishing-resistant VPN MFA; EDR; retire the trust at migration | IT Consulting president | 2027-03-31 |
| GR-07 | A full ACMP restore takes far longer than the 8-hour contract RTO | GT-003, SW-005 | Parallel restore automation; full-scale exercise | GovTech division president | 2027-03-31 |

### GovTech Integration (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| GT-001 | Ransomware through a stolen cloud administrator credential encrypts ACMP databases | Session binding for PAM; snapshot-deletion alerts; full-scale restore exercise | ACMP platform director | 2027-03-31 |
| GT-002 | Theft of FTI and CJI from the ACMP followed by extortion | Bulk-read alerts; service accounts in identity governance | GovTech division CISO | 2026-12-31 |
| GT-003 | Full ACMP restore exceeds the 8-hour RTO | Parallel restore automation (POAM-011) | ACMP platform director | 2027-03-31 |
| GT-004 | Unscreened corporate staff with CJI or FTI access | Suspend access; group register (POAM-001) | GovTech personnel security manager | 2026-12-31 |
| GT-005 | Subcontractor staff without Security Addendum or IRS-approved terms | Suspend access; flowdown checklist (POAM-012) | Group public sector compliance director | 2026-11-30 |
| GT-008 | AI eligibility recommendations lead to wrong denials or delays | Review-first design; deterministic rules; monthly QC (P10; POAM-016) | GovTech Data and AI director | 2026-12-31 |

### Other division risks rated High or Very High
| Risk ID | Division | Level | Risk | Owner | Due |
|---|---|---|---|---|---|
| IC-001 | IT Consulting | **Very High** | Ransomware through the acquired firm's VPN (password and SMS codes) and the directory trust | IT Consulting security and compliance lead | 2026-12-31 |
| IC-002 | IT Consulting | High | DoD CUI on the acquired firm's file shares outside the enclave | IT Consulting defense programs director | 2026-12-31 |
| IC-004 | IT Consulting | High | No CMMC Level 2 (C3PAO) status when Phase 2 solicitations require it | IT Consulting president | 2027-03-31 |
| SW-001 | Software | High | RMS connectors still on FIPS 140-2 modules after the CJIS deadline | Software division RMS general manager | 2026-12-31 |
| SW-002 | Software | High | Intrusion in the RMS exposes CJI of about 620 agencies | Government Software Products security and compliance lead | 2027-03-31 |
| SW-003 | Software | High | RMS AI assist adds or omits facts in police narratives | Software division RMS general manager | 2026-12-31 |

### What the results say
The program is defined and mostly effective. The one Very High risk and most of the High risks cluster around **what the group shares and what it bought**, not around any division's basics:
1. **The acquired consulting firm** (IC-001, GR-05) is the only Very High risk. Its VPN accepts SMS codes, its endpoints are outside group EDR, and a migration trust links its directory to the group's. It is the entry path in the P08 scenario. The board risk committee was told on 2026-09-15 that the risk is being treated, not accepted: phishing-resistant MFA on the VPN by 2026-10-31 and EDR by 2026-12-31.
2. **Shared services touch the most sensitive data.** About 860 corporate staff can reach CJI and FTI environments, and screening was never extended to them (GR-02; scenario gap 1). Shared admin paths and one restore team also mean one ransomware event can hit several divisions (GR-01, GR-07, GR-08).
3. **Notification across divisions** (GR-03) has never been exercised, and its shortest clock is 1 hour.
4. **AI is ahead of governance** in two divisions (GR-04; scenario gap 6).

Scenario gaps 2, 3, and 9 (log retention, enclave inheritance, and the RMS FIPS deadline) are Moderate at group level (GR-09, GR-10, GR-11) because each has a dated fix in progress, but SW-001 is High in its division because the 41 connectors cannot be upgraded before the CJIS date of 2026-09-21.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** acquired firm security uplift and migration (GR-05); group screening register and checks (GR-02); full-scale restore automation and exercise (GR-07); notification matrix and tabletop (GR-03); group AI program (GR-04); 7-year log retention (GR-09); CMMC Level 2 assessment (GR-06).
- **Accepted (12 risks, all Low):** GR-15, GR-17, GT-024, GT-026, GT-027, GT-029, IC-014, IC-016, IC-018, SW-009, SW-014, SW-017. Each was accepted by the authority for its level and is reviewed at the next cycle.
- **Agency and customer disclosures:** the group public sector compliance director tells each affected agency about the screening gap (GT-004), the subcontractor gap (GT-005), and the IRS notification gap (GT-015) by 2026-10-31, so each agency can decide its own reporting duties. The Software division tells each CSA with connector agencies about the FIPS schedule (SW-001).
- **Treatment status:** 46 risks are In progress, 28 are Open (treatment approved, work not started), and 12 are Accepted.

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The six High group risks and the Very High division risk were presented on 2026-09-15. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here: board risk committee oversight, the Group CISO's reporting line, and the use of group internal audit and outside assessors (state CSAs, the IRS Office of Safeguards through the agencies, the SOC 2 service auditors, and the FedRAMP and GovRAMP assessors).

## 6. Approval
- Board risk committee: approved the group register, the six High group treatment plans, the IC-001 treatment plan, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the 11 High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-10 to 2026-09-15.
- Next full review: May to July 2027, or sooner after a major change, an acquisition, an incident, or a new CJISSECPOL version.
