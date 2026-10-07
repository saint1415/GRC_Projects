# Risk Register Report: Cris Santos Company Holdings | Management of Companies and Enterprises | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; two operating divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Management of Companies and Enterprises, Finance and Insurance, Health Care) |
| Focus | The holding company and its corporate shared services (NAICS 551112) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | The insurers' risk assessment under state laws based on NAIC Model #668 sec. 4C (Alabama, South Carolina, Tennessee); Health Care Services' HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A); the processes described under Reg S-K Item 106(b) |
| Registers | `risk-register.csv` (group, focus), `risk-register-insurance.csv`, `risk-register-health-care-services.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group Chief Risk Officer and the Group CISO, with the Insurance information security officer and the Health Care Services HIPAA Security Officer |
| Approved | 2026-09-15 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** The Shared Corporate Services Platform (SCSP: SYS-G1, SYS-G4, SYS-G5, SYS-G6), the common infrastructure (SYS-G2, SYS-G3), the productivity suite and board systems (SYS-G7, SYS-G8), the group health plan, and the division systems SYS-I1 to SYS-I4 and SYS-H1 to SYS-H3 (`../00_company-facts.md` sections 3 and 7).

**Why the group register is the focus.** For a holding company, the group register is not a summary of the divisions. It is the register of the holding company's own business: the shared services every subsidiary depends on, the duties it carries as a public registrant, plan sponsor, insurance holding company, and service provider to its subsidiaries, and the risks that cross division lines.

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself.
- **The group register** holds risks that sit in shared services, cross divisions, or need a group decision or group funding. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back. Group risks are rated on their own group-level likelihood and impact, not copied from the highest division rating. For example, HCS-001 (adjusters reading non-work visits) is High for Health Care Services, while its group counterpart GR-24 is Moderate, because at group level the fix is a role change that both divisions already agreed.

**Risk tolerance and who may accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead; for group risks, the group security governance director |
| Moderate | Division president; for group risks, the Group CIO |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Patient-safety risks and risks to claimants' benefit payments rated High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the BIA (P05), the SSP and cloud mapping (P02, P04), the gap analyses (P03), the control assessment (P07), and interviews with division leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). Group impact reflects enterprise consequences: several regulators at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all three registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk sits in a shared service, crosses divisions, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 5 | 15 | 4 | 0 | 24 | n/a |
| Insurance | 0 | 1 | 10 | 7 | 0 | 18 | 10 |
| Health Care Services | 0 | 3 | 13 | 2 | 0 | 18 | 6 |
| **All registers** | **0** | **9** | **38** | **13** | **0** | **60** | **16** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Help desk MFA reset leads to takeover of the shared identity platform | INS-005, HCS-004, HCS-018 | Division-scoped help desk roles; identity verification for every reset; tiered administration | Group identity director | 2026-11-30 (tiering 2027-03-31) |
| GR-02 | Ransomware spreads through shared identity and network across divisions | INS-004, HCS-002, HCS-004 | Close legacy trust; segment colocation; quarterly restores; cross-division tabletop | Group CISO | 2027-03-31 |
| GR-03 | Fraudulent bank-detail change redirects claims or vendor payments | INS-001, INS-016 | Out-of-band verification; hold on first payment to a changed account | Group Treasurer | 2026-12-31 |
| GR-08 | Pivot from an acquired clinic through the legacy directory trust | HCS-004, HCS-009, HCS-018 | Selective authentication now; remove trust at migration; SIEM onboarding | Group identity director | 2026-12-31 |
| GR-10 | Enterprise AI assistant surfaces PHI, consumer nonpublic information, or MNPI across divisions | INS-018, HCS-016 | Group AI Standard conditions (P10) | Group Chief Risk Officer | 2026-12-31 |

### Division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| INS-001 | Insurance | Bank-detail change by phone redirects claim payments | Insurance claims vice president | 2026-12-31 |
| HCS-001 | Health Care Services | Adjusters read non-work-related visits in the clinic EHR | Health Care Services HIPAA Privacy Officer | 2026-12-31 |
| HCS-002 | Health Care Services | Ransomware halts clinic registration and documentation | Health Care Services HIPAA Security Officer | 2027-03-31 |
| HCS-004 | Health Care Services | Acquired clinics' legacy EHR compromised or loses a day of records undetected | Health Care Services division president | 2027-03-31 |

### What the results say
The group program is defined and most common controls work: a 24x7 SOC, PAM, hardware keys for administrators, immutable backups, and tested SOX controls. There are no Very High risks. **Four of the five High group risks sit in what the holding company provides to everyone else:**
1. **The shared identity platform** (GR-01, GR-08). Sign-in is strong; recovery and trust are weak. A help desk reset or the legacy directory trust bypasses the hardware keys (scenario gap 1).
2. **The payment path** (GR-03). Controls protect a payment once it exists, but not the bank-detail change that comes before it (gap 5).
3. **Shared infrastructure as a ransomware path** (GR-02). One identity platform and one hub connect all three divisions.
4. **The AI assistant** (GR-10) amplifies every existing over-sharing problem across three regulated divisions at once (gap 9).

The group's **governance duties** are Moderate but matter for regulators: the insurers cannot yet show oversight of the holding company as their service provider (GR-06, gap 2), the plan sponsor firewall leaks (GR-05, gap 3), and the notification matrix is incomplete (GR-07, gap 7).

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** identity administration redesign (GR-01, GR-08); payment-change verification across Insurance and payables (GR-03); legacy clinic migration and SIEM onboarding (GR-08, GR-18); Group AI Standard conditions (GR-10); integration standby automation (GR-09).
- **Accepted (Low or Very Low target):** INS-017 (unencrypted reinsurance email, with TLS enforced for the top 5 reinsurers), HCS-013 (encrypted laptop loss), and HCS-014 (check-in app takeover with limited data).
- **Avoided:** GR-22 (resume screening turned off) and INS-014 (aerial-imagery pricing model not deployed).
- **Contract and governance actions:** security schedule in the 2017 intercompany agreement (GR-06); plan document amendment (GR-05); 2026 Form 10-K Item 106 narrative aligned with these results (GR-16); cyber risks added to the 2027 enterprise risk report under Fla. Stat. 628.801(2) (GR-21).
- **Treatment status:** 36 risks are In progress, 19 are Open (treatment approved, work not started), and 5 are Closed (the 3 accepted and 2 avoided risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The five High group risks were presented on 2026-09-15. Two other reports draw on this register:
- **Reg S-K Item 106** in the 2026 Form 10-K describes how these processes are integrated into enterprise risk management and how the board risk committee oversees them (106(b)(1)(i), 106(c)(1)).
- **The annual enterprise risk report** the holding company files as ultimate controlling person of the insurers (Fla. Stat. 628.801(2), due April 1) will include GR-01, GR-02, GR-03, and GR-06, which could affect the insurers.

## 6. Approval
- Board risk committee: approved the group register, the five High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the four High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-10 to 2026-09-15.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
