# Risk Register Report: Cris Santos Company | Food and Agriculture | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (custom-exempt meat processing shop) |
| Size tier | Sole Proprietorship (owner-operator only, 0 employees) |
| Vertical | Food and Agriculture |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Prepared | 2026-07-31 by the owner-operator, with the on-call IT technician. This is the shop's first risk assessment |
| Risk owner and approver | Owner-operator (owner, security lead, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-10, the walk-in cooler and freezer, the smokehouse, paper records in the shop, and the people and vendors the shop depends on. Processes and impact levels come from the BIA (P05).

**What makes this shop different from an office.** Two systems act on food. A changed alarm set point or a silenced alert can let customers' meat spoil unnoticed, and a changed cook program or cure amount can make product unsafe. Impact is therefore rated on product safety and customers' property, not only on data.

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. A risk that could put unsafe product in a customer's home is never accepted at High.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the P03 gap analysis, and a walkthrough of the shop, the devices, and each SaaS account with the IT technician on 2026-07-28 and 2026-07-29.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale, combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories.
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 5 |
| Low | 6 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware on the shop laptop, with theft of saved passwords | High | Standard account; password manager; versioned files and encrypted backups; training | Owner-operator | 2026-10-15 |
| R-002 | Takeover of the cold-chain and smokehouse accounts through the shared password | High | Unique passphrases; MFA on SYS-01; monthly log and program checks | Owner-operator | 2026-09-15 |
| R-003 | Cooler failure overnight with no alert | High | Offline notice; battery backup; second alert contact; hourly manual readings | Owner-operator | 2026-10-15 |
| R-010 | Hurricane or long power outage | High | Storm procedure; generator transfer switch; emergency cooler space | Owner-operator | 2027-05-31 |
| R-004 | Loss of custom records, cook programs, cure sheet, or label templates | Moderate | Versioned file plan; monthly encrypted export; printed programs | Owner-operator | 2026-10-15 |
| R-005 | Unchecked AI chatbot cure calculation exceeds 9 CFR 424.21(c) limits | Moderate | Supplier chart is the only source; check recorded on each batch sheet (P10) | Owner-operator | 2026-09-30 |
| R-009 | Owner unavailable (single point of failure) | Moderate | Reciprocal agreement with a neighboring processor; sealed emergency sheet | Owner-operator | 2026-10-15 |

**The common thread.** Three of the four High risks (R-002, R-003, R-010) end the same way: customers' meat warms or is cooked wrongly and nobody notices in time. The fixes are mostly settings and agreements, not equipment: turning on MFA and the offline notice, adding a second alert contact, and writing down what the owner already does by habit. R-005 is Moderate only because the owner usually catches a wrong number by eye; its impact is Very High, which is why it has a short due date.

## 4. Treatment summary
- **Free fixes first (by 2026-09-15):** MFA on SYS-01 and the booking form, unique passphrases, clearing the browser password store, and the smokehouse program list check. The default router and panel passwords were already changed on 2026-07-29.
- **Before the busy season (by 2026-10-15, about $350 one-time and $140 a year):** battery backup for the gateway and router (about $120), encrypted backup drive (about $80), guest and device networks with the IT technician (about $150), password manager and business file plan with version history (about $140 a year together), and the reciprocal agreement with a neighboring custom processor (no cost).
- **Before the 2027 hurricane season (by 2027-05-31):** generator transfer switch for the condensing units (quote first; cost not yet known) and the written storm procedure.
- **Accepted (Low):** R-011 (vendor outage), R-012 (chatbot data use, with the POL-01 9.5 input rule), R-014 (label printing outage, covered by the preprinted roll), and R-015 (device theft, covered by encryption).

## 5. Approval
Owner-operator, 2026-08-31: approved all treatment plans and the four acceptances. Next full review July 2027, or sooner after a new system or vendor, a hire, a change to the custom exemption status, or an incident.
