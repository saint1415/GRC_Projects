# Risk Register Report: Cris Santos Company Holdings | Accommodation and Food Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; Hotels, Attractions and Entertainment, and Resort Real Estate and Vacation Ownership divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Accommodation and Food Services, Arts, Entertainment, and Recreation, and Real Estate and Rental and Leasing) |
| Focus division | Hotels (NAICS 721110): 88 hotels, 30 owned or leased and 58 managed for third-party owners |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | PCI DSS v4.0.1 Requirement 12.3 risk management for each merchant and service provider validation (N72-R01, N71-R04, N53-R04); the written risk assessment the finance subsidiary needs under 16 CFR 314.4(b)(1) (N53-R01); the annual children's data risk assessment under 16 CFR 312.8(b)(2) (N71-R06) |
| Registers | `risk-register.csv` (group), `risk-register-hotels.csv`, `risk-register-attractions.csv`, `risk-register-vacation-ownership.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses), last reviewed 2026-07-31 |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-10 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments and the finance subsidiary board approved the Safeguards Rule remediation plan the same week |

## 1. Scope and risk framing
**Scope.** Every system that stores, processes, or transmits card data, guest, visitor, or owner personal information, children's information, or loan customer information in the three divisions, plus the corporate shared services they depend on: identity (SYS-G1), the SOC (SYS-G2), the cloud platform and network (SYS-G3), group payment services (SYS-G4), the guest identity and loyalty platform (SYS-G5), and ERP and HR (SYS-G6). Division systems are SYS-H1 to SYS-H5, SYS-A1 to SYS-A4, and SYS-V1 to SYS-V4 (`../00_company-facts.md` section 3). Ride and show control (SYS-A4) is in scope for safety as well as security.

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Hotels, the focus division, has the most detailed register (26 risks).
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not on the highest division rating. Four group risks (GR-11, GR-12, GR-16, GR-17) have no division counterpart because they exist only at group level.

**Risk tolerance and who can accept risk** (added to `../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead (Group CISO for group risks) |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Two kinds of risk at High may not be accepted at all and must be treated: **guest, visitor, or rider safety** (ride control, door locks) and **card data compromise** (the acquirer agreements do not allow the group to carry a known card data exposure). For the finance subsidiary, the Qualified Individual must also report every High risk to the finance subsidiary board in the annual written report (16 CFR 314.4(i)).

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the 2026 penetration and segmentation tests (2026-04-27 to 2026-05-08), the gap analyses (P03), the common control assessment (P07), and interviews with each division's leadership, the Qualified Individual, and the Group Director of Payments and PCI Compliance.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05: cost, operations, regulatory and contractual, safety, reputation). Group impact reflects enterprise consequences: card brand action across three acquirers, several regulators at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads proposed roll-ups. The Group Chief Risk Officer decided which risks become group risks with three tests: the risk crosses divisions, sits in a shared service, or needs a group decision or group funding.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 6 | 10 | 2 | 0 | 18 | n/a |
| Hotels | 0 | 3 | 15 | 8 | 0 | 26 | 15 |
| Attractions | 0 | 1 | 7 | 8 | 0 | 16 | 7 |
| Vacation Ownership | 0 | 3 | 12 | 3 | 0 | 18 | 12 |
| **All registers** | **0** | **13** | **44** | **21** | **0** | **78** | **34** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Card-capturing malware spreads to hotel and park POS through the shared legacy POS vendor's remote support | HTL-01, HTL-10, HTL-22, ATT-01 | Vendor access through PAM with named accounts by 2026-12-31; compensating monitoring on legacy segments; P2PE replacement by 2027-06-30 | Group CISO | 2027-06-30 |
| GR-02 | Guest profile hub data, including owners' bank account numbers, read in bulk through an over-broad integration credential | HTL-03, VO-03 | Restrict the service account to loyalty fields; rotate keys every 90 days; move bank data out of the hub and keep it tokenized in SYS-V3 | Group Chief Privacy Officer | 2026-12-31 |
| GR-04 | AI systems set prices or credit terms without adequate governance | HTL-15, HTL-16, HTL-17, ATT-10, ATT-14, VO-06, VO-07, VO-11 | Group AI governance program (P10) with conditions on AI-001, AI-002, AI-006, and AI-007 | Group Chief Risk Officer | 2027-03-31 |
| GR-05 | Ransomware spreads through shared identity and network services into several divisions | HTL-08, VO-15 | Move Vacation Ownership to SYS-G1 and group EDR; segment the legacy data center; quarterly restore tests | Group CISO | 2027-03-31 |
| GR-06 | A breach of loan and owner data in the acquired division exposes the group to FTC Safeguards Rule enforcement | VO-01, VO-02, VO-05 | Safeguards Rule remediation plan approved by the finance subsidiary board; the Qualified Individual reports progress monthly | Vacation Ownership security and compliance lead | 2027-03-31 |
| GR-09 | An attacker reaches ride and show control from the park business network and affects a ride | ATT-02, ATT-15 | Remove the jump host bridge; one-way maintenance path with PAM and engineering approval | Attractions vice president of ride engineering | 2026-11-30 |

### Hotels (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| HTL-01 | Memory-scraping malware on legacy POS servers captures card data at 72 outlets | Vendor through PAM; compensating segment monitoring; P2PE replacement (GR-01) | Hotels security and compliance lead | 2027-06-30 |
| HTL-03 | The CRS integration service account is used to read guest and owner data from the profile hub | Restrict scope; rotate; remove the credential from legacy POS servers (GR-02) | Hotels division payments and systems director | 2026-11-30 |
| HTL-04 | An attacker uses the lock vendor's default administrator password to encode room keys | Change all lock server passwords; add lock servers to the hardening scan; vendor access through PAM | Hotels vice president of engineering | 2026-10-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| ATT-02 | Attractions | An attacker crosses the maintenance jump host into ride control (GR-09) | Attractions vice president of ride engineering | 2026-11-30 |
| VO-01 | Vacation Ownership | The unencrypted loan document archive is stolen (16 CFR 314.4(c)(3)) | Vacation Ownership security and compliance lead | 2026-12-31 |
| VO-02 | Vacation Ownership | A loan processing account without MFA is taken over (16 CFR 314.4(c)(5)) | Vacation Ownership security and compliance lead | 2026-11-30 |
| VO-03 | Vacation Ownership | Owners' bank account numbers in the guest profile hub are exposed (GR-02) | Vacation Ownership vice president of owner services | 2026-12-31 |

### What the results say
There are no Very High risks. The group's shared controls are strong: one identity platform with PAM, a 24x7 SOC, tokenization in one card vault, immutable backups, and annual QSA Reports on Compliance for Hotels and Attractions. The High risks cluster in three places:
1. **What the divisions share** (GR-01, GR-02, GR-05). The same legacy POS vendor reaches hotel and park POS (scenario gap 1), and the guest profile hub holds all three divisions' customers behind one over-broad credential (gap 2). One incident in either place would trigger card brand, FTC, state, owner, and SEC duties at once. That is the P08 scenario.
2. **The acquired division** (GR-06, VO-01, VO-02, VO-03). Vacation Ownership has not reached the group baseline two years after the acquisition. Its gaps map directly to named Safeguards Rule elements: encryption at rest, MFA, and service provider oversight (gap 3).
3. **Safety and building systems** (GR-09, ATT-02, HTL-04). A ride control bridge (gap 9) and a default door lock password are rated High because the impact is physical harm or unsecured rooms, not data loss. Neither may be accepted.

AI governance (GR-04, gap 10) is High at group level even though no single division AI risk is High. Eight division risks, from chatbot fee quotes to credit model reasons, share one cause: AI use cases went live before the Group AI council existed.

The kids' club (ATT-03, ATT-04) and biometric gate data (ATT-05) are Moderate. Their likelihood is low because both sit with vendors that have not had incidents, but they carry concrete regulatory gaps (16 CFR 312.8(b), 312.5(a)(2), 312.10; gap 4) that P03 rates High as compliance gaps.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** legacy POS vendor access through PAM and P2PE replacement (GR-01; POAM-001); guest profile hub least privilege and bank data removal (GR-02; POAM-013); Vacation Ownership migration to SYS-G1, group EDR, and SIEM (GR-05, GR-06; POAM-006, POAM-020); ride control bridge removal (GR-09; POAM-016); group AI governance program (GR-04; P10).
- **Contract actions:** re-paper the 31 pre-2020 management agreements and send every owner a PCI DSS responsibility matrix (GR-18; POAM-026); written assurances from the kids' club analytics vendor and the gate vendor (POAM-018).
- **Accepted (all Low):** GR-16 (privileged administrator misuse, covered by PAM and session recording), HTL-18 (guest Wi-Fi and IPTV compromise; vendor-managed guest networks are separated from staff and payment segments), ATT-16 (stored-value and gift card fraud, covered by velocity checks), and VO-12 (single ACH bank, until the 2027 bank review).
- **Avoided:** ATT-14. The seasonal applicant screening tool was not approved; it needs a full assessment before any pilot (P10 AI-005).
- **Treatment status:** 54 risks are In progress, 20 are Open (treatment approved, work not started), and 4 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The six High group risks were presented on 2026-09-10, together with the audit committee's review of the assessment results (P07). Three other reporting lines draw on the same registers:
- the **Qualified Individual's annual written report** to the finance subsidiary board (16 CFR 314.4(i)), which uses the Vacation Ownership register and GR-06;
- the **PCI DSS targeted risk analyses** that the Group Director of Payments and PCI Compliance keeps for each validation (Requirement 12.3.1);
- the **Reg S-K Item 106** disclosure in the next annual report, which describes how cyber risk is integrated into enterprise risk management and how the board oversees it.

## 6. Approval
- Board risk committee: approved the group register, the six High group treatment plans, and the funding request, 2026-09-10.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the seven High division risks, 2026-09-10.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-08 to 2026-09-10.
- Finance subsidiary board: approved the Safeguards Rule remediation plan (GR-06) on the Qualified Individual's report, 2026-09-10.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
