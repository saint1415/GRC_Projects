# Risk Register Report: Cris Santos Company Holdings | Health Care | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Health Care, Finance and Insurance, Information) |
| Focus division | Care Delivery (NAICS 621111), a HIPAA covered entity |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A), for each covered entity (Care Delivery and the Health Plan) and for the SaaS as a business associate |
| Registers | `risk-register.csv` (group), `risk-register-care-delivery.csv`, `risk-register-health-plan.csv`, `risk-register-saas.csv` |
| Fieldwork | 2026-05-01 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-10 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that creates, receives, maintains, or transmits ePHI or customer PHI in the three divisions, plus the corporate shared services they depend on: the group identity platform (SYS-G1), the group SOC (SYS-G2), and the group cloud and data platform (SYS-G3). Division systems are SYS-D1 to SYS-D4 (`../scenario-facts.md` sections 3 and 7).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. Care Delivery, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact. They are not simply the highest division rating.

**Risk tolerance and who can accept risk** (added to `../scenario-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Patient-safety and member-harm risks at High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Group impact reflects enterprise consequences: several regulators at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 15 | 2 | 0 | 21 | n/a |
| Care Delivery | 0 | 3 | 18 | 9 | 0 | 30 | 18 |
| Health Plan | 0 | 2 | 11 | 5 | 0 | 18 | 14 |
| Health-Tech SaaS | 0 | 2 | 11 | 5 | 0 | 18 | 11 |
| **All registers** | **0** | **11** | **55** | **21** | **0** | **87** | **43** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Cross-division PHI exposure or misuse on the Group Data Platform | CD-002, HP-002, HP-016, HT-008 | Zone separation by covered entity; purpose tags; minimum-necessary protocols; de-identify before landing | Group Chief Privacy Officer | 2027-03-31 |
| GR-02 | Ransomware spreads through shared services and exfiltrates data from several divisions | CD-001, CD-028, HP-003 | Legacy segmentation; quarterly restore tests; cross-division tabletop | Group CISO | 2027-03-31 |
| GR-04 | AI in regulated decisions or products without adequate governance | CD-004, CD-019, HP-001, HT-002, HT-003 | Group AI governance program (P10) | Group Chief Risk Officer | 2027-03-31 |
| GR-08 | Critical third-party outage or breach across divisions | CD-020, HP-009 | Second clearinghouse; continuous monitoring of tier 1 vendors | Group Chief Risk Officer | 2027-03-31 |

### Care Delivery (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| CD-001 | Ransomware halts LIS, PACS, and clinic servers at 23 legacy sites | Segment legacy sites; quarterly LIS and PACS restore tests | Care Delivery security and compliance lead | 2027-03-31 |
| CD-002 | Care Delivery PHI on the Group Data Platform used or exposed beyond its purpose | Zone separation and purpose tags (GR-01) | Care Delivery Privacy Officer | 2027-03-31 |
| CD-020 | Clearinghouse ransomware halts claims and eligibility for weeks | Second clearinghouse connection; cash contingency | Care Delivery revenue cycle director | 2027-03-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| HP-001 | Health Plan | UM model recommendation drives an adverse outcome without documented individualized review (42 CFR 422.101(c)(1)(i)) | Health Plan medical director | 2026-12-31 |
| HP-002 | Health Plan | Health Plan PHI on the Group Data Platform used beyond its purpose | Health Plan Privacy Officer | 2027-03-31 |
| HT-001 | Health-Tech SaaS | Tenant isolation defect exposes one customer's data to another | SaaS chief technology officer | 2027-03-31 |
| HT-003 | Health-Tech SaaS | AI feature launched without updated SOC 2 system description or customer BAAs | SaaS general manager | 2026-11-30 |

### What the results say
The program is mostly sound. There are no Very High risks, and most control families are in place: a 24x7 SOC, PAM, quarterly access certification, and immutable backups. The High risks cluster around **what the group shares**, not around any one division's basics:
1. **The Group Data Platform** (GR-01) holds PHI for two covered entities in mixed zones. Purpose-based access is inconsistent, and minimum-necessary enforcement between divisions has not been verified (scenario gap 1).
2. **AI governance** (GR-04) has fallen behind deployment in all three divisions (gaps 3 and 4).
3. **Shared-service incidents** (GR-02, and the Moderate risk GR-03) would trigger two covered entities' breach duties, SaaS customer notices, state insurance notices, and an SEC materiality decision at once (gap 5).

Governance gaps 2 and 6 (policy drift and undocumented Health Plan inheritance) are Moderate at group level (GR-05, GR-06). They matter because they hide whether Health Plan controls actually operate, which is why the P07 assessment sampled the Health Plan more heavily.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** Group Data Platform zone separation and purpose-based access (GR-01); legacy segmentation at Care Delivery and the Health Plan (GR-02, GR-13); group AI governance program (GR-04); second clearinghouse (GR-08); SIEM onboarding of remaining ePHI systems (GR-12).
- **Accepted (all Low):** CD-016 (encrypted laptop theft), CD-027 (patient-app denial of service), HP-018 (hurricane at the claims center, covered by remote work), HT-013 (engineer production access, covered by PAM).
- **Contract actions:** re-paper the Health Plan intercompany BAA and amend SaaS customer BAAs (GR-17, HT-009); customer notice and system description update for the SaaS AI feature (HT-003).
- **Treatment status:** 55 risks are In progress, 28 are Open (treatment approved, work not started), and 4 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks were presented on 2026-09-10. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight and the Group CISO's reporting line).

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, and the funding request, 2026-09-10.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the seven High division risks, 2026-09-10.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-08 to 2026-09-10.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
