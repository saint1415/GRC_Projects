# Risk Register Report: Cris Santos Company | Other Services (except Public Administration) | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (electronics and device repair service) |
| Size tier | Sole Proprietorship (owner-technician only, 0 employees) |
| Vertical | Other Services (except Public Administration) |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | "Reasonable measures" under Fla. Stat. 501.171(2); CSF 2.0 ID.RA and GV.RM outcomes (P03). This is the shop's first risk assessment |
| Prepared | 2026-07-24 by the owner-technician, with the independent security consultant (on site 2026-07-20) |
| Risk owner and approver | Owner-technician (owner, security and privacy lead, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-12, paper intake forms and tags, the customer devices in the shop's custody, and the contracted help (fill-in technician, recycler, payment processor, SaaS vendors). Processes come from the BIA (P05).

**Risk tolerance.** The owner-technician owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as they are. Any risk that exposes customers' device contents or account passwords and is rated High is never accepted.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the gap analysis (P03), and a walkthrough of the counter, bench, router, and SaaS accounts with the security consultant on 2026-07-20.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 2 |
| Moderate | 9 |
| Low | 4 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Takeover of the shared ticketing login; export of passcodes, account passwords, and card numbers in notes | High | Named fill-in account, MFA, restricted passcode field, purge of old notes | Owner-technician | 2026-10-31 |
| R-002 | Customer device data on the unprotected bench PC and drives | High | Password, encryption, 14-day deletion rule, backlog purge | Owner-technician | 2026-10-31 |
| R-006 | Card numbers recorded outside the P2PE terminal | Moderate | Key phone payments directly; shred notes; purge tickets | Owner-technician | 2026-09-15 |
| R-004 | Fill-in technician misuse of customer data | Moderate | Written agreement, named account, access rules | Owner-technician | 2026-09-30 |
| R-009 | Customer data in a consumer AI assistant | Moderate | Training off, no personal data in prompts, business terms (P10) | Owner-technician | 2026-09-30 |
| R-010 | Owner unavailable (single point of failure) | Moderate | Emergency access sheet, device-return procedure | Owner-technician | 2026-12-31 |

**The two High risks share one cause: the shop keeps customers' secrets long after the repair is done.** Passcodes stay in ticket notes and full device copies stay on the bench forever. Collecting less and deleting on a schedule reduces both risks more than any product purchase. Turning on MFA, which costs nothing, becomes possible once the fill-in technician has a named account.

**What is specific to a repair shop.** Five of the 15 risks (R-001, R-002, R-004, R-005, R-008) exist only because customers hand over their devices and passcodes. A good technician needs some access to test a repair. The line between good-faith access and a breach is drawn by Fla. Stat. 501.171(1)(a): access by an agent is not a breach "provided that the information is not used for a purpose unrelated to the business." POL-01 8.4 turns that line into rules.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** bench PC password and lock, phone-payment rule and shredding the old notes (R-006), AI training setting off (R-009), camera MFA (R-013), rewritten intake notice (R-008), the fill-in agreement and named account (R-004), and the P08 runbook (R-012).
- **Budgeted (about $450 one-time):** two hardware-encrypted transfer drives (about $350) and an hour of the consultant's time to set up separate Wi-Fi networks (about $100). Recurring: an AI business plan (about $25 a month) if it is kept, and a SYS-01 user fee for the fill-in account in cover months (about $20 a month).
- **Data clean-up by 2026-10-31:** purge passcodes, account passwords, and card numbers from SYS-01 notes, and delete or sanitize the 1.6 TB bench backlog (R-001, R-002, R-005).
- **Accepted (Low):** R-011 (ticketing outage; the vendor's commitments meet the BIA) and R-014 (hurricane; storm procedure in the register).

## 5. Approval
Owner-technician, 2026-08-31: approved all treatment plans and the two acceptances. Next full review July 2027, or sooner after a new system, a new contractor or hire, a new service line, or an incident.
