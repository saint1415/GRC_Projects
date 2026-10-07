# Risk Register Report: Cris Santos Company | Defense Industrial Base | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (engineering subcontractor handling CUI drawings) |
| Size tier | Sole Proprietorship (owner only, 0 employees) |
| Vertical | Defense Industrial Base |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also satisfies | NIST SP 800-171 Rev. 2 requirement 3.11.1 (periodic risk assessment). This is the business's first evidence-based one |
| Prepared | 2026-07-24 by the owner; R-015 added 2026-08-05 from P07 testing |
| Risk owner and approver | Owner (every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: the Engineering Office Systems (SYS-01 to SYS-08, planned SYS-10), the home office and printed CUI, the commercial AI chatbot (SYS-09), and the outside parties (Prime A, the IT consultant, SaaS providers). Processes come from the BIA (P05).

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, three fixed rules apply (POL-01 4.4):
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Never accepted as they are. Any risk that could make an SPRS entry or CMMC affirmation untrue is treated as High or above.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the gap analysis (P03), and a walk through the laptop, phone, router, and SaaS accounts.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3). Loss of the Prime A relationship, or personal liability for a false statement, is rated Very High because either could end the business.
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 4 |
| Moderate | 8 |
| Low | 2 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-003 | SPRS score of 110 overstates implementation; a false affirmation would follow | Very High | Post the corrected score and date-to-110; affirm only with evidence | Owner | 2026-09-15 |
| R-001 | Phishing steals the SYS-01 session and the attacker syncs CUI drawings | High | SYS-10 with hardware keys; password manager; log review; training | Owner | 2026-11-30 |
| R-002 | CUI held in a commercial cloud suite that is not FedRAMP Moderate equivalent | High | Migrate to SYS-10 and delete CUI from SYS-01 | Owner | 2026-11-30 |
| R-004 | No CMMC Level 2 (Self) status before the follow-on award | High | P03 roadmap; self-assessment and affirmation | Owner | 2027-01-15 |
| R-006 | Cyber incident not reported to DoD within 72 hours | High | Medium assurance certificate; P08 runbook; forensics on call | Owner | 2026-10-31 |
| R-007 | CUI pasted into a commercial AI chatbot | Moderate | Avoid: no CUI in the chatbot; incident decision with counsel and Prime A (P10) | Owner | 2026-09-30 |

The High and Very High risks share one cause: **the business took on a DFARS 252.204-7012 subcontract with the IT setup of an ordinary home office, and then reported full compliance.** The cheapest and most urgent fix is honesty: correct the SPRS score (R-003), which costs nothing. The most important technical fix is moving CUI to a FedRAMP-authorized service (R-002), which also removes most of R-001 and R-010.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** corrected SPRS score; MFA on the accounting SaaS; password manager; standard user account; office locking and visitor log; router firmware and settings; encrypted backup drive; stop CUI in the chatbot.
- **Budgeted (about $3,600 in the first year, fictional):** SYS-10 licenses through a reseller (about $1,800 a year), two hardware security keys, a FIPS-validated encrypted backup drive, a second router for the business network, a password manager, a vulnerability scanner license, the medium assurance certificate, and about 10 hours of CMMC consultant time.
- **Business decision:** if Level 2 (Self) cannot be reached by 2027-01-15, the owner tells Prime A before the solicitation closes rather than affirming without evidence (R-003, R-004).
- **Accepted (Low):** R-014 (hurricane; files are in the cloud and the laptop leaves with the owner).
- **Added after testing:** R-015 (router default administrator password, found in P07 on 2026-08-05 and changed that day).

## 5. Approval
Owner, 2026-08-31: approved all treatment plans and the one acceptance. Next full review July 2027, or sooner after the SYS-10 migration, a new customer or contract clause, a hire, or an incident.
