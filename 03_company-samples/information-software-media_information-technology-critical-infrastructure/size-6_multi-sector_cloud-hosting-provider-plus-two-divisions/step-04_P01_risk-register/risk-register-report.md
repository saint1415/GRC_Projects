# Risk Register Report: Cris Santos Company Holdings | Information Technology | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Information, Professional Services, and Finance and Insurance) |
| Focus division | Cloud Hosting (NAICS 518210) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | FTC Safeguards Rule written risk assessment for Payment Processing (16 CFR 314.4(b)); NIST SP 800-171 Rev. 2 risk assessment (3.11.1) for the Managed IT CUI enclave; HIPAA risk analysis (45 CFR 164.308(a)(1)(ii)(A)) for both divisions' business associate work; PCI DSS v4.0.1 targeted risk analyses are kept separately by Payment Processing |
| Registers | `risk-register.csv` (group), `risk-register-cloud-hosting.csv`, `risk-register-managed-it.csv`, `risk-register-payment-processing.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security leads |
| Approved | 2026-09-17 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments and acceptances the same week |

## 1. Scope and risk framing
**Scope.** Every system that holds or can reach customer, client, agency, merchant, or consumer data in the three divisions, plus the corporate shared services they depend on: SYS-G1 (identity), SYS-G2 (SOC and the AI triage service), SYS-G3 (landing zone and backup vault), and SYS-G4 (corporate SaaS). Division systems are SYS-H1 to SYS-H4, SYS-M1 and SYS-M2, and SYS-P1 and SYS-P2 (`../00_company-facts.md` section 3).

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. Cloud Hosting, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each of those division risks points back to it. Group risks are rated on their own group-level likelihood and impact, not copied from the highest division rating.

**Who can accept risk** (POL-01 section 4.4; `../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security lead (division CISO where one exists) |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

A High risk to a federal agency's data, a bank's covered services, or cardholder data may not be accepted. It must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the BIA (P05), the gap analyses (P03), the common control assessment (P07), threat intelligence on attacks against cloud and managed service providers, and interviews with each division's leadership.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) is combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). Group impact reflects enterprise consequences: several regulators at once, loss of a certification, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 11 | 5 | 0 | 20 | n/a |
| Cloud Hosting | 0 | 2 | 15 | 11 | 0 | 28 | 15 |
| Managed IT | 0 | 2 | 11 | 5 | 0 | 18 | 14 |
| Payment Processing | 0 | 1 | 12 | 5 | 0 | 18 | 10 |
| **All registers** | **0** | **9** | **49** | **26** | **0** | **84** | **39** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Stolen partner-operator session used to run commands across managed-hosting tenants | CH-001, CH-002, CH-003, MS-002 | SYS-G1 PAM with hardware keys and per-client scope; 1-hour device-bound sessions; run-command volume alert | Group CISO | 2026-12-31 |
| GR-02 | Malicious script through the single RMM tenant reaches client servers, Payment Processing connected-to servers, and the CUI enclave | MS-001, MS-003, PY-001 | Two-person approval for multi-client scripts; separate internal tooling; RMM logs to the SIEM | Managed IT division president | 2027-01-31 |
| GR-04 | AI triage service auto-closes a true positive or runs a disruptive containment action in another division | CH-020 | Human approval for containment in G1 and the CDE; per-division validation (P10) | Group SOC director | 2026-12-31 |
| GR-05 | G1 loses its FedRAMP certification because the 2026 rules are not adopted by their grace dates | CH-004, CH-006 | Funded transition program by ruleset date (P03) | Cloud Hosting division president | 2027-08-01 |

### Cloud Hosting (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| CH-001 | Stolen partner-operator session used to run commands in managed-hosting tenants | PAM, hardware keys, per-client scope, 1-hour device-bound sessions (POAM-001) | Cloud Hosting division CISO | 2026-12-31 |
| CH-004 | G1 misses the VDR and VER maintain date (2026-12-07) and the grace end (2027-03-07) | VDR and VER adoption program (POAM-006) | Government Cloud compliance director | 2026-12-07 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| MS-001 | Managed IT | Stolen technician session sends a malicious script through the RMM to many clients | Managed IT chief operating officer | 2026-12-31 |
| MS-002 | Managed IT | Technician and partner-operator identities phished through the legacy identity tenant | Managed IT division security and compliance lead | 2027-03-31 |
| PY-001 | Payment Processing | Attacker uses RMM-managed settlement-support servers to pivot into the CDE | Payment Processing division CISO (Qualified Individual) | 2027-01-31 |

### What the results say
The program is defined and mostly effective. There are no Very High risks, and the controls that most divisions share (identity, the SOC, EDR, immutable backups, HSM signing) are strong. The High risks cluster around **the paths that connect the divisions**, not around any one division's basics:
1. **Tooling that reaches across divisions** (GR-01, GR-02). Two privileged paths cross division lines: the HCP partner-operator role and the single RMM tenant. Both rely on the Managed IT legacy identity tenant, so one phished engineer could reach thousands of customer systems, Payment Processing's connected-to servers, and the CUI enclave (scenario gaps 1 and 2). This is also the P08 scenario.
2. **Automation the group cannot yet vouch for** (GR-04). The SOC's AI triage service decides which alerts a human sees and can contain hosts in every division, but its accuracy has never been validated by division (scenario gap 4).
3. **A certification with dated rules** (GR-05). The FedRAMP 2026 rules have fixed maintain and grace dates. Missing them means losing the G1 certification, which 27 agencies and about 140 DIB customers depend on (scenario gap 3).

Governance gaps 7, 8, 9, and 10 (notification matrix, supplement drift, Managed IT inheritance, vendor screening) are Moderate or Low at group level (GR-03, GR-12, GR-13, GR-14). They matter because they decide whether the High risks would be reported on time, which is why P07 sampled Managed IT governance controls more heavily.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q3):** partner-operator rebuild on SYS-G1 PAM (GR-01); RMM separation and two-person approval (GR-02); AI triage validation and limits (GR-04); FedRAMP 2026 transition (GR-05); CMMC Level 2 readiness (GR-06); intercompany agreements for Payment Processing (GR-08).
- **Accepted (4 Low, 1 Moderate):** GR-18 and CH-024 (hurricane in R1, covered by the multi-region design), CH-027 (metering records), MS-018 (encrypted laptop loss), and PY-012 (sponsor bank concentration, accepted by the Payment Processing division president as a commercial decision reviewed each year).
- **Contract actions:** intercompany agreements carrying 16 CFR 314.4(f) terms and a PCI DSS responsibility matrix (GR-08); an ESP responsibility matrix for DIB clients (MS-006); 24-hour incident notice terms for tier 1 vendors (GR-17).
- **Treatment status:** 65 risks are In progress, 14 are Open (treatment approved, work not started), and 5 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks were presented on 2026-09-17 with their funding requests. The Reg S-K Item 106 description in the next annual report draws on this governance: the board risk committee's oversight, the Group CISO's reporting line, and the use of independent assessors (group internal audit, the FedRAMP assessment service, and the PCI QSA).

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, and the funding requests, 2026-09-17.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the five High division risks, 2026-09-17.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-17.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
