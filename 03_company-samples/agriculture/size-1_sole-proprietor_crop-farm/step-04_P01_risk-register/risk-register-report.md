# Risk Register Report: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (precision-agriculture crop farm) |
| Size tier | Sole Proprietorship (owner-operator only, 0 employees) |
| Vertical | Agriculture, Forestry, Fishing and Hunting |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | CSF 2.0 ID.RA (benchmark); "reasonable measures" under Fla. Stat. 501.171(2). This is the farm's first risk assessment |
| Prepared | 2026-07-17 by the owner-operator, with the on-call IT technician |
| Risk owner and approver | Owner-operator (owner, security lead, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole farm as one system: SYS-01 to SYS-10, the irrigation equipment at both parcels, paper program documents, and the outside parties (irrigation dealer, FMIS vendor, booking vendor, AI yield vendor, custom harvest operator), as listed in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv). Processes come from the BIA (P05).

**What the farm cares about most.** Losing a crop in one night (freeze protection), losing the season's sales, and losing the records that keep the farm out of the full Produce Safety Rule. A breach notice would be small (personal information of 2 individuals is held by the farm itself), but the irrigation and records risks are large.

**Risk tolerance.** The owner-operator owns and accepts every risk. Because the same person proposes and approves, three fixed rules apply:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan, never accepted as they are. Any risk that can cost a crop must be treated before freeze season (2026-11-30).

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the intake evidence, the BIA, the SaaS control map (P04), and a walk through the laptop, router, pump house, and SaaS accounts with the IT technician on 2026-07-15 (EV-035). The gap analysis (P03) ran in the same self-assessment week, and the two shared findings. SP 800-82 Rev. 3 section 4.1 (Managing OT Security Risk) was used for the irrigation risks.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the account, device and router reviews (EV-002, EV-011, EV-020, EV-022), the dealer records (EV-001, EV-008), the alarm settings (EV-004), the document search (EV-030), and the owner's self-reviews (EV-034, EV-036). A one-person farm keeps no ticket or incident log to count, so a rating with no evidence behind it would be a guess, and none was made.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (a lost crop block is Severe cost; P05 section 3).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.
5. **Feedback from testing.** R-005 includes the default password found on the pump controller in P07 testing on 2026-07-16 (EV-IA-5, EV-SC-7).

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 8 |
| Low | 4 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware on the shared laptop, with theft of saved passwords | High | Separate accounts, password manager, backups, training | Owner-operator | 2026-10-31 |
| R-002 | Takeover of the SYS-01 irrigation control account | High | MFA, unique passphrase, activity log review | Owner-operator | 2026-09-15 |
| R-005 | Customer Wi-Fi reaches the pump controller with its default password | High | Change defaults; isolate customer Wi-Fi; separate pump house network | Owner-operator | 2026-11-15 |
| R-003 | Freeze alarm does not arrive | Moderate | Standalone alarm; written freeze-night procedure | Owner-operator | 2026-11-15 |
| R-004 | Dealer's always-on technician account misused | Moderate | Viewer role; service windows; contract terms | Owner-operator | 2026-09-30 |
| R-006 | Owner unavailable (single point of failure) | Moderate | Mutual-aid neighbor; sealed recovery codes | Owner-operator | 2026-11-30 |
| R-007 | Records lost, so the qualified exemption cannot be shown | Moderate | Monthly exports; annual eligibility review | Owner-operator | 2026-10-31 |

**One pass.** The register was completed on 2026-07-17 from intake and self-assessment evidence. The control tests ran on 2026-07-16, inside the same week, so this pass already reflects them: R-005 was identified from the intake router and walk-through evidence (EV-022, EV-009) and cites the pump controller test result (EV-IA-5, EV-SC-7). No risk was added after P07 testing. The `assessment_pass` column records the pass for each risk.

The three High risks share one theme: **anyone who gets one password, or onto the farm-stand Wi-Fi, can reach the irrigation.** The fixes cost almost nothing: MFA on SYS-01 and the booking platform, a password manager, changing two default passwords, and turning on the router's guest isolation. All three must be done before the strawberries go in the ground for the December freeze season.

## 4. Treatment summary
- **Free fixes first (by 2026-09-15):** MFA on SYS-01 and the booking platform; unique passphrases in a password manager; change the router and pump controller default passwords (with the dealer).
- **Before freeze season (by 2026-11-30):** separate networks for customer Wi-Fi and the pump house; standalone cellular freeze alarm (about $300 plus a monthly plan); written freeze-night procedure; mutual-aid arrangement with a neighbor; sealed recovery codes.
- **Budgeted (about $400 a year):** business-grade file plan with version history, password manager, encrypted backup drive.
- **Contract actions:** dealer security terms (R-004, at renewal, interim viewer role by 2026-09-30); AI yield vendor data terms or stop (R-011, by 2026-10-31).
- **Accepted (Low):** R-012 (USB sticks; antivirus scans them), R-013 (lightning or hurricane; manual pumping and insurance), and R-014 (SYS-01 outage; manual operation and exports).

## 5. Approval
Owner-operator, 2026-08-31: approved all treatment plans and the three acceptances. Next full review July 2027, or sooner after a new system, a new vendor, the first hire, a change in sales mix that affects the qualified exemption, or an incident.
