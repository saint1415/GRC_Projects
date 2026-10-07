# Risk Register Report: Cris Santos Company Holdings | Professional Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services; the CPA Partners attest firm is included under the administrative services agreement) |
| Size tier | Multi-Sector (45,000 employees; Professional Services, Finance and Insurance, Information) |
| Focus division | CPA and Tax Services (NAICS 541211): Tax and Advisory and the CPA Partners attest practice |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | Tax and Advisory's written risk assessment under 16 CFR 314.4(b)(1) (criteria in section 2; mitigation and acceptance rules in section 1); input to Wealth's Regulation S-P program review and Practice Cloud's SOC 2 risk assessment (CC3.2) |
| Registers | `risk-register.csv` (group), `risk-register-tax.csv`, `risk-register-wealth.csv`, `risk-register-practice-cloud.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses, after the filing season) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the division security and compliance leads |
| Approved | 2026-09-10 by the board risk committee (group register and all High risks); division presidents and the CPA Partners managing partner approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that creates, receives, maintains, or transmits tax return information, customer information, client funds instructions, or customer firms' data, in the three divisions and CPA Partners, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and network, and SYS-G4 email. Division systems are SYS-T1 to SYS-T3, SYS-W1, and SYS-S1 (`../00_company-facts.md` sections 3 and 7).

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. CPA and Tax Services, the focus division, has the most detailed register; CPA Partners' risks are in it (TX-023 to TX-025).
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back. Group risks are rated on their own group-level likelihood and impact, not simply the highest division rating.

**Risk tolerance and who can accept risk** (also in `../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president (for CPA Partners, its managing partner), with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Risks that could cause direct financial loss to clients (refund diversion, fraudulent transfers) may not be accepted at High. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), IRS security alerts for tax professionals, and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Group impact reflects enterprise consequences: several regulators at once (FTC, IRS, SEC, states), customer firms, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

These scales are the "criteria for the evaluation and categorization of identified security risks or threats" and for assessing confidentiality, integrity, and availability that 16 CFR 314.4(b)(1)(i) and (ii) require; section 1 and the treatment columns meet (b)(1)(iii).

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 13 | 3 | 0 | 20 | n/a |
| CPA and Tax Services | 0 | 4 | 18 | 8 | 0 | 30 | 22 |
| Wealth Management | 0 | 1 | 10 | 7 | 0 | 18 | 10 |
| Practice Management Software | 0 | 2 | 7 | 9 | 0 | 18 | 10 |
| **All registers** | **0** | **11** | **48** | **27** | **0** | **86** | **42** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Tax return information disclosed to or used by Wealth without a valid IRC 7216 consent | TX-003, TX-004, WM-005 | Consent register enforced by the referral interface; specific consent template; stop statistical compilations; re-consent | Group Chief Privacy Officer | 2027-03-31 |
| GR-02 | Business email compromise through the shared email tenant: taxpayer data theft, refund diversion, and fraudulent transfer requests across divisions | TX-001, TX-002, TX-013, TX-016, WM-001, WM-002 | Block legacy authentication; remove forwarding exceptions; tax office inbox-rule alerts; enforced call-backs; cross-division tabletop | Group CISO | 2027-01-04 |
| GR-04 | Generative AI in tax preparation and in the Practice Cloud product without adequate governance | TX-008, TX-009, WM-006, SW-002, SW-009, SW-018 | Group AI governance program (P10) | Group Chief Risk Officer | 2027-03-31 |
| GR-06 | Ransomware spreads through shared services during the filing season | TX-011, WM-012 | Office segmentation; season-volume restore test; ransomware exercise | Group CISO | 2027-01-15 |

### CPA and Tax Services (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| TX-001 | Phishing of tax office staff leads to mailbox takeover and theft of client documents | Block legacy authentication; tax office inbox-rule alerts; portal upload instead of intake mailboxes | Tax division security and compliance lead | 2027-01-04 |
| TX-002 | A fraudulent refund bank-account change diverts a client's refund | SYS-T1 blocks release until the call-back is recorded; weekly bank-field review | Chief Tax Officer | 2027-01-04 |
| TX-004 | Consents do not cover the products solicited, and Wealth uses statistical compilations of tax return information | New template naming each type of product or service; re-consent; stop compilations | Chief Tax Officer | 2027-03-31 |
| TX-011 | Ransomware encrypts SYS-T1 in the filing season | Season-volume restore test; office segmentation | Tax division technology director | 2027-01-15 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| WM-001 | Wealth | A fraudulent money-movement request from a hijacked or spoofed email is processed | Wealth operations director | 2026-12-31 |
| SW-001 | Practice Cloud | A tenant isolation defect exposes one customer firm's client documents to another | Practice Cloud chief technology officer | 2027-03-31 |
| SW-002 | Practice Cloud | The AI document intake feature runs without SOC 2, sub-processor, contract, and IRC 7216 updates | Practice Cloud division president | 2026-12-31 |

### What the results say
The program is defined and mostly sound. There are no Very High risks, and the common platforms are strong: one identity platform with phishing-resistant administrator MFA, a 24x7 SOC, PAM, immutable backups, and annual penetration tests. The High risks cluster where **divisions meet**:
1. **Data moving from tax to wealth** (GR-01). IRC 7216 makes the preparer's disclosure or use of tax return information a crime unless a permission or a specific, prior, written consent covers it. The referral interface does not check consent, and the consent itself is too general (scenario gap 1).
2. **One email tenant for every division** (GR-02). Business email compromise is the leading threat to tax professionals, and a hijacked tax office mailbox sends trusted internal mail to Wealth advisers (gaps 3 and 6).
3. **AI deployed faster than governance** (GR-04) in two divisions (gaps 4 and 5).
4. **Ransomware in the filing season** (GR-06), when an outage costs about $92 million of tax work per business day.

Seasonal identity (GR-05, gap 2), cross-division notification (GR-03, gap 6), and the attest practice's undocumented services (GR-09, gap 7) are Moderate at group level. They matter because each turns a contained incident into a multi-regulator one.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q1):** consent enforcement and re-consent (GR-01); email hardening before the 2027 filing season (GR-02); group AI governance program (GR-04); office segmentation and season-volume restore testing (GR-06); seasonal identity gating (GR-05); SIEM onboarding of tax office mailboxes and Practice Cloud alerts (GR-11).
- **Accepted (all Low):** TX-019 (single e-file transmitter; returns queue), TX-026 (encrypted laptop theft), WM-014 (archive gaps found within a day), SW-015 (engineer production access under PAM).
- **Contract actions:** amend the integrated planning agreement for the Regulation S-P 72-hour notice and the administrative services agreement for security and HIPAA subcontractor terms (GR-13, WM-003, TX-024); Practice Cloud customer contract and sub-processor updates (SW-002).
- **Treatment status:** 71 risks are In progress, 11 are Open (treatment approved, work not started), and 4 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks were presented on 2026-09-10. Two other reporting lines use the same registers:
- **FTC Safeguards Rule:** the Qualified Individual's written report to the Tax and Advisory board of managers (16 CFR 314.4(i)), due 2026-10-15, draws on the group and CPA and Tax Services registers.
- **SEC:** the Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (board risk committee oversight; the Group CISO's reporting line).

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, and the funding request, 2026-09-10.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the seven High division risks, 2026-09-10.
- Division presidents and the CPA Partners managing partner: approved Moderate and Low treatments and acceptances for their units, 2026-09-08 to 2026-09-10.
- Next full review: May to July 2027 (after the filing season), or sooner after a major change, acquisition, or incident.
