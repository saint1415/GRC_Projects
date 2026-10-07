# Risk Register Report: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated oilfield services contractor, NAICS 213112) |
| Size tier | Sole Proprietorship (owner-operator only, 0 employees) |
| Vertical | Mining, Quarrying, and Oil and Gas Extraction |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also answers | Customer A's annual security questionnaire (risk assessment question) and CSF 2.0 ID.RA in the voluntary benchmark (P03). This is the business's first risk assessment |
| Prepared | 2026-07-24 by the owner-operator, with the on-call IT technician |
| Risk owner and approver | Owner-operator (owner, security lead, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: the Field Service Business Systems (SYS-01 to SYS-08), the paper gauge book, and the business's touch points with customer field equipment (remote sessions, cables, USB drives). Customer SCADA and controllers are in scope only as **assets the owner can harm**, not as systems the owner runs. Functions come from the BIA (P05).

**Risk tolerance.** The owner-operator owns and accepts every risk. Because the same person proposes and approves, three fixed rules apply:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. A risk that could cause a release or unsafe condition at a customer site is never accepted above Low.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the gap analysis (P03), Customer A's security schedule, and a walkthrough of the laptop, phone, truck, home office, and SaaS accounts with the IT technician (2026-07-21 and 2026-07-22).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (cost, operations, contract, safety and environment, reputation).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 8 |
| Low | 3 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware on the field laptop spreading toward customer SCADA | High | Standard daily account, password manager, offline backups, training, P08 runbook | Owner-operator | 2026-11-30 |
| R-002 | Takeover of the business email account | High | Authenticator-app MFA, delete the password spreadsheet, sign-in review | Owner-operator | 2026-09-30 |
| R-003 | Attacker uses Customer B's shared remote-desktop login | High | Named accounts and MFA requested from Customer B; session log; remote access terms | Owner-operator | 2026-10-31 |
| R-008 | Customer A ends the MSA over the security schedule | High | Meet items (3) to (5); cyber coverage of at least $1 million | Owner-operator | 2026-10-31 |
| R-006 | Wrong or unapproved program or setpoint loaded | Moderate | Email approval and change log | Owner-operator | 2026-09-15 |
| R-009 | Customer data in AI tools without consent | Moderate | Consent or no-training tier; well codes (P10) | Owner-operator | 2026-09-30 |

**The common cause.** Three of the four High risks share one condition: **a laptop that is both a business computer and a customer engineering workstation, run from one administrator account, with every customer password in a plain spreadsheet.** The cheapest fixes are settings and habits: a standard daily account, a password manager, authenticator-app MFA, and deleting the spreadsheet. They cost under $100 a year and reduce R-001, R-002, R-003, and R-004 within a month. The fourth High risk, R-008, is commercial: the largest customer's contract already requires most of these controls, so meeting the schedule and the controls are the same work.

**Shared risk with the customers.** R-003 and R-005 sit mostly on customer equipment. The owner cannot fix Customer B's remote-desktop tool alone, so the treatment is a written request (sent 2026-07-24) and, until Customer B acts, the owner's own session log and password hygiene. This follows the SP 800-82 Rev. 3 point that third-party remote access into OT must be controlled by the asset owner (section 6.2.10, author mapping).

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** accounting MFA, authenticator-app MFA for email, standard laptop account, password manager, dedicated USB drives, change approval by email, the P08 runbook, and the AI consent decision.
- **Budgeted (about $1,900 in the first year):** password manager (about $40), an encrypted offline drive (about $100, one time), a new router (about $150, one time), the dynamometer no-training tier if consent is refused (about $300 a year more), and cyber liability coverage of at least $1 million (insurance agent's estimate about $1,300 a year).
- **Contract actions:** Customer B named accounts and MFA (R-003, requested 2026-07-24); written remote access terms at the next Customer B renewal; mutual coverage agreement (R-010).
- **Accepted (Low):** R-012 (laptop loss; encrypted and rebuildable within the BP-02 MTD) and R-015 (hurricane; customers shut in wells and records are in SaaS).

## 5. Approval
Owner-operator, 2026-08-31: approved all treatment plans and the two acceptances. Next full review July 2027, or sooner before an MSA renewal, after a new customer remote access path, a new system, a hire, or an incident.
