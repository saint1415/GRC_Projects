# Risk Register Report: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent radiation safety consultant) |
| Size tier | Sole Proprietorship (owner only, 0 employees) |
| Vertical | Nuclear Reactors, Materials, and Waste |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Prepared | 2026-07-24 by the owner-consultant, with the on-call IT technician (under NDA since 2026-07-14) |
| Risk owner and approver | Owner-consultant (owner, security lead, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-08, the USB drive, paper in the home office, the owner's access to the two client portals, and the people around the business (per-diem technician, IT technician, tax accountant). Processes come from the BIA (P05).

**What is different about this business.** The consultancy has no plant, no license, and almost no personal data. Its risk comes from what its clients trust it with: Client B's Part 37 security information, and a path (people and portable media) into Client A's nuclear power plant. The worst outcome is not the loss of the business's own data. It is helping someone plan an attack on a client, or carrying malware to a plant.

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. Any risk that could put a client's security information or plant systems at risk is never accepted above Low.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the client terms (CSR-A, CSIA-B), the gap analysis (P03), and a walk through the laptops, phone, media, and SaaS accounts with the IT technician.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories, including harm to the client and to workers whose dose depends on the owner's data.
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 2 |
| Moderate | 10 |
| Low | 3 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Info-stealing malware on the laptop used to reach Client A's portal and the email suite | High | Standard daily account; password manager; authenticator MFA; training; runbook | Owner-consultant | 2026-10-09 |
| R-002 | Client B Part 37 security information opened by someone who should not see it | High | Client B's share only; named-person sharing; no client text in AI tools | Owner-consultant | 2026-09-30 |
| R-004 | Malware carried to Client A's plant on the owner's USB drive (attempted pivot) | Moderate | Encrypted Client A-only drive; offline field laptop; kiosk scans | Owner-consultant | 2026-10-09 |
| R-003 | Email takeover through a phished text code or SIM swap | Moderate | Authenticator MFA; carrier PIN; monthly sign-in review | Owner-consultant | 2026-09-15 |
| R-013 | Missed 8-hour Client A or 24-hour Client B notice | Moderate | P08 runbook and printed contacts | Owner-consultant | 2026-10-09 |
| R-010 | Owner unavailable during an outage (single point of failure) | Moderate | Peer coverage; sealed recovery codes | Owner-consultant | 2026-12-31 |

The two High risks share one cause: **client information was handled like the business's own files.** Client B's security information sat in a general-purpose suite behind an open link, and the laptop that reaches Client A's portal is used for everything in an administrator account with saved passwords. R-004 rates Moderate only because Client A's kiosk scan works; its impact is the highest in the register (Very High), so the owner treats it before the fall outage instead of relying on the client's control.

## 4. Treatment summary
- **Free or low-cost fixes first (by 2026-09-30):** authenticator MFA on email, MFA on accounting and calibration-tracking, standard daily account, carrier PIN, Client B information moved back to Client B's share, the 2025 Client A packages returned or destroyed, photo sync off, site tags removed from the drift prediction data.
- **Before the fall outage starts on 2026-10-19 (by 2026-10-09):** encrypted Client A-only USB drive, field laptop offline, runbook walkthrough with the IT technician, printed contacts.
- **Budgeted (about $700 a year plus a one-time field laptop replacement of about $1,200):** password manager, encrypted drives, security course, replacement field laptop or supported operating system.
- **Accepted (Low):** R-008 (accidental SGI receipt; POL-01 8.4 rule in place) and R-014 (hurricane; work continues from anywhere).

## 5. Approval
Owner-consultant, 2026-08-31: approved all treatment plans and the two acceptances. Next full review July 2027, or sooner after a new client, a new system, a change in Client A's or Client B's terms, or an incident.
