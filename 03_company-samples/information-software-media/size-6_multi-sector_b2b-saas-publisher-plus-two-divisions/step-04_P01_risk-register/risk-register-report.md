# Risk Register Report: Cris Santos Company Holdings | Information | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Information, Professional Services, Finance and Insurance) |
| Focus division | Cloud Software (NAICS 513210), publisher of Workforce Cloud |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | The written risk assessment of the FTC Safeguards Rule for Payments and Payroll (16 CFR 314.4(b)); the HIPAA risk analysis for consulting's business associate work (45 CFR 164.308(a)(1)(ii)(A)); PCI DSS 12.3 targeted risk analyses draw on it; SOC 2 CC3.2 for Workforce Cloud |
| Registers | `risk-register.csv` (group), `risk-register-cloud-software.csv`, `risk-register-technology-consulting.csv`, `risk-register-payments-and-payroll.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-17 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that holds customer, worker, client, cardholder, or payroll data in the three divisions, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud platform and CI/CD, and SYS-G4 corporate SaaS. Division systems are SYS-D1 (WCP), SYS-D2 (consulting delivery systems), SYS-D3 (payroll engine), and SYS-D4 (payments platform) (`../00_company-facts.md` sections 3 and 7).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. Cloud Software, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not simply the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead (division CISO where one exists) |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Risks that could leave workers unpaid or expose payroll data (Social Security numbers and bank details) at High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), the cloud mapping (P04), and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Group impact reflects enterprise consequences: several regulators and contract counterparties at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 3 | 13 | 4 | 0 | 20 | n/a |
| Cloud Software | 0 | 4 | 16 | 8 | 0 | 28 | 16 |
| Technology Consulting | 0 | 2 | 9 | 7 | 0 | 18 | 13 |
| Payments and Payroll | 0 | 2 | 10 | 8 | 0 | 20 | 15 |
| **All registers** | **0** | **11** | **48** | **27** | **0** | **86** | **44** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | A leaked static machine credential lets an attacker read customer exports and payroll handoff files across divisions | SW-001, SW-003, IC-003, PY-001 | Workload identity and a guardrail against new static keys; dedicated handoff channel with 7-day retention, customer-managed keys, and read logging; bulk-read detection | Group CISO | 2026-12-31 |
| GR-02 | Ransomware or a destructive attack spreads through shared identity, CI/CD, or the consulting access gateway | SW-010, IC-008, PY-012 | Acquired firm onto group EDR and identity; isolate the access gateway; cross-division restore exercise | Group CISO | 2027-03-31 |
| GR-04 | AI in products and group HR produces unfair, inaccurate, or undisclosed outcomes | SW-005, SW-006, SW-007, SW-025, SW-028, IC-012, PY-014 | Group AI governance program conditions (P10) | Group Chief Risk Officer | 2027-03-31 |

### Cloud Software (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| SW-001 | Leaked static key used to read payroll handoff files and customer exports | Revoke static keys; workload identity; read logging and bulk-read alerts | Cloud Software division CISO | 2026-11-30 |
| SW-002 | Tenant isolation defect exposes one customer's worker data to another | Canary-stage isolation checks; annual third-party isolation test | Cloud Software chief technology officer | 2027-03-31 |
| SW-003 | Handoff files kept far beyond need multiply the size of any breach | 7-day retention; move the channel to the payroll engine | Cloud Software integrations director | 2026-12-31 |
| SW-006 | Attrition-risk scores disadvantage protected groups in customers' employment decisions | Bias testing; developer documentation; usage guidance | Cloud Software chief product officer | 2026-12-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| IC-003 | Technology Consulting | Static migration key leaks from a laptop or personal repository and is used against customer exports | Technology Consulting security and compliance lead | 2026-11-30 |
| IC-008 | Technology Consulting | Ransomware spreads through the client access gateway into client systems | Technology Consulting managed services director | 2027-03-31 |
| PY-001 | Payments and Payroll | Payroll handoff data for up to 2.4 million workers copied from the affiliate's export bucket | Payments and Payroll division CISO | 2026-12-31 |
| PY-002 | Payments and Payroll | Malicious script on a hosted checkout page skims card data | Payments platform director | 2026-11-30 |

### What the results say
The program is defined and mostly effective. There are no Very High risks, and the basics are in place: single sign-on with MFA, PAM, a 24x7 SOC, immutable backups, signed builds, and independent assurance (SOC 2, SOC 1, PCI DSS, ISO/IEC 27001). The High risks cluster around **where the divisions meet**, not around any one division's basics:
1. **The payroll handoff and the keys that can read it** (GR-01; SW-001, SW-003, IC-003, PY-001). One division stores another division's most sensitive data, and a third division holds keys that can read it (gaps 1 and 2). This is also the P08 scenario.
2. **AI governance** (GR-04) has fallen behind deployment in the product and in group HR (gap 4).
3. **Shared paths for destructive attacks** (GR-02), made worse by the acquired consulting firm's separate stack (gap 9).

Governance gaps 5, 7, 8, 10, and 11 (affiliate oversight, notification matrix, CCPA audit readiness, consulting inheritance, and federal contract information) are Moderate or Low at group level (GR-09, GR-03, GR-15, GR-18, GR-16). They matter because they decide whether the group can prove its controls to regulators, banks, and clients, which is why the P07 assessment sampled consulting and payments governance controls.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q1):** workload identity and the static key guardrail (GR-01); handoff channel redesign (GR-01, GR-09); acquired firm EDR and identity migration (GR-02, GR-10); group AI governance program (GR-04); multi-division notification matrix and tabletop (GR-03); CCPA audit readiness (GR-15).
- **Accepted (both Low):** SW-024 and IC-016 (encrypted laptop loss).
- **Contract and legal actions:** intercompany agreement for the handoff (GR-09); DPA amendments for aggregated data use (SW-007); subcontract flowdown for federal work (IC-007); money transmission licensing analysis (GR-11, PY-010).
- **Treatment status:** 74 risks are In progress, 10 are Open (treatment approved, work not started), and 2 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The three High group risks were presented on 2026-09-17. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight and the Group CISO's reporting line). The Payments and Payroll Qualified Individual's annual written report to its board (16 CFR 314.4(i)) uses the payments register and the group risks it rolls up to.

## 6. Approval
- Board risk committee: approved the group register, the three High group treatment plans, and the funding request, 2026-09-17.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the eight High division risks, 2026-09-17.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-17.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
