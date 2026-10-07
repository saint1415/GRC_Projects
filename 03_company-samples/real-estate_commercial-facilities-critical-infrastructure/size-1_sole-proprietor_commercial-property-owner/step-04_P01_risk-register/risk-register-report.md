# Risk Register Report: Cris Santos Company | Commercial Facilities | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operator of one mixed-use commercial building) |
| Size tier | Sole Proprietorship (owner only, 0 employees) |
| Vertical | Commercial Facilities |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | "Reasonable measures" under Fla. Stat. 501.171(2) and CISA CPG 2.0 goals 1.B and 2.B (voluntary). This is the business's first risk assessment |
| Prepared | 2026-07-24 by the owner, with the on-call IT consultant |
| Risk owner and approver | Owner (owner, security lead, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-09, the paper lease files, and the contracted services that touch them (installer, HVAC contractor, IT consultant, janitorial contractor, CPA). Processes come from the BIA (P05).

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. Any risk that could leave the building open to unauthorized entry and is rated High is never accepted.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the CPG 2.0 gap analysis (P03), and a walkthrough of the building, the router, the portals, and the laptop with the IT consultant on 2026-07-21.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (cost, operations, regulatory, safety, reputation).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 9 |
| Low | 3 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware or an infostealer on the laptop harvests saved passwords and reaches the building portals | High | MFA on building portals, password manager, backups, training | Owner | 2026-10-31 |
| R-002 | Takeover of the access control, video, or thermostat portal (no MFA) | High | MFA by app for every administrator; unique passphrases | Owner | 2026-09-15 |
| R-004 | Guarantor files exposed through the public folder link or email takeover | High | Remove the link; restricted folder; retention; app-based MFA | Owner | 2026-09-15 |
| R-003 | Installer's standing administrator accounts misused or taken over | Moderate | Time-limited accounts per visit; written terms | Owner | 2026-10-31 |
| R-006 | Former credential holders still able to enter | Moderate | Departure reporting; monthly review | Owner | 2026-10-31 |
| R-009 | Owner unavailable (single point of failure) | Moderate | Manual procedures; sealed envelope; contractor fallback | Owner | 2026-12-31 |

The three High risks share one cause: **the accounts that control the building and hold guarantor data are protected by passwords alone, and those passwords sit in the laptop's browser.** Turning on MFA in the three building portals costs nothing and takes an afternoon. A password manager (about $40 a year) removes the saved-password path that makes R-001 so damaging.

**What the building's design already gets right.** Egress is mechanical and always free, so no cyber event can trap anyone inside. The door controllers and thermostats keep working offline, and the fire alarm and elevator are on their own cellular communicators. That is why outages (R-008, R-015) are Low, while compromise of the portals (R-002) is High.

## 4. Treatment summary
- **Free fixes first (by 2026-09-15):** MFA on all building portals, a separate HVAC contractor login, changing the router password, and removing the public folder link (done 2026-08-05).
- **Budgeted (about $400 a year plus about $300 once):** password manager, SaaS backup for email and files, an encrypted external drive, and a business router with separate building-device and guest networks (2026-12-31).
- **Contract actions by 2026-10-31:** one-page security terms with 72-hour incident notice for the installer, HVAC contractor, IT consultant, and janitorial contractor (R-003); a rules letter asking tenants to report departures within 1 business day (R-006).
- **Avoided:** face recognition retired and audio kept off (R-010; P10).
- **Accepted (Low):** R-008 (internet or cloud outage; devices run offline) and R-015 (hurricane; doors fail secure with free egress).

## 5. Approval
Owner, 2026-08-31: approved all treatment plans, the avoidance decision, and the two acceptances. Next full review July 2027, or sooner after a new building system, a new contractor with system access, a hire, or an incident.
