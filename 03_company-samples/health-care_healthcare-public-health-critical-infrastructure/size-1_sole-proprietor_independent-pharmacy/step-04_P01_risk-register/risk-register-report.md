# Risk Register Report: Cris Santos Company | Healthcare and Public Health | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent community pharmacy) |
| Size tier | Sole Proprietorship (pharmacist-owner only, 0 employees; one relief pharmacist as a contractor) |
| Vertical | Healthcare and Public Health |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also satisfies | HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A). This is the pharmacy's first one |
| Prepared | 2026-08-07 by the pharmacist-owner, with the on-call IT consultant (under BAA since 2026-07-31) |
| Risk owner and approver | Pharmacist-owner (owner, Privacy Officer, Security Officer, and risk acceptor for every risk) |
| Approved | 2026-09-04 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-08, the CSOS certificate, paper prescriptions and logs in the store, the relief pharmacist, and the contracted services (PMS vendor, cloud fax vendor, email and file suite vendor, IT consultant). Processes come from the BIA (P05).

**Risk tolerance.** The pharmacist-owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as they are. A risk to patient safety is never accepted above Low.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the gap analysis (P03), the DEA EPCS and CSOS duties, and a walk through the counter desktop, PMS settings, store network, and SaaS accounts with the IT consultant on 2026-08-04 and 2026-08-06.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 10 |
| Low | 2 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware at the PMS vendor takes the PMS offline for days | High | P08 runbook; paper downtime kit; transfer arrangement; ask about cyber coverage | Pharmacist-owner | 2026-10-31 |
| R-002 | Ransomware or remote attacker enters the counter desktop through the vendor's remote-support agent or phishing | High | Attended remote support only; own standard accounts; encryption; guest network; training | Pharmacist-owner | 2026-10-31 |
| R-005 | Burglary takes the unencrypted counter desktop | High | Built-in full-disk encryption; delete the mailing-list export | Pharmacist-owner | 2026-09-15 |
| R-003 | Relief pharmacist dispenses under the owner's PMS account | Moderate | Own PMS account and pharmacist role | Pharmacist-owner | 2026-09-30 |
| R-008 | Altered controlled substance records go unnoticed; DEA one-business-day report missed | Moderate | Daily EPCS report review; written decision steps | Pharmacist-owner | 2026-09-30 |
| R-006 | Email and file suite holds PHI with no BAA in effect | Moderate | Accept the vendor's BAA | Pharmacist-owner | 2026-09-15 |
| R-011 | Pharmacist-owner unavailable (single point of failure) | Moderate | Own accounts; CSOS power of attorney decision; sealed recovery codes; transfer arrangement | Pharmacist-owner | 2026-12-31 |

The three High risks share one theme: **the pharmacy depends on one vendor's system and one shared, always-open desktop.** The desktop fixes cost nothing (encryption, own accounts, attended remote support) and close most of R-002 and R-005 within weeks of adoption. The vendor outage (R-001) cannot be prevented by the pharmacy, only survived: its treatment is the paper downtime kit and the P08 runbook.

**Pharmacy-specific risks.** Three risks exist only because this is a pharmacy: shared-account dispensing that breaks the DEA rule that each controlled substance record name the person who dispensed (R-003), unread EPCS audit reports with a one-business-day DEA clock (R-008), and the CSOS key on a shared desktop (R-012). None of them appears in a generic small-business risk list.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** desktop encryption, accept the email suite BAA, cloud fax MFA, own PMS and desktop accounts with a screen lock, MFA for the PMS administrator role in the store, CSOS key moved to the owner's account, daily EPCS report review, and adopting the P08 runbook.
- **Budgeted (about $500 a year):** a password manager, the IT consultant's time to split the store network, and an annual HIPAA security course for the owner and the relief pharmacist.
- **Contract and process actions by 2026-12-31:** a transfer arrangement with a nearby pharmacy; the CSOS power of attorney decision; sealed recovery codes; a quote for cyber insurance.
- **Avoided:** R-009 and R-010 (no PHI in the AI chatbot and no AI use for calculations; stopped 2026-08-07, rule adopted 2026-09-04; R-010 closed).
- **Accepted (Low):** R-015 (hurricane or long power outage; the PMS is reachable from the laptop and Florida law allows emergency supplies under a declared emergency).

## 5. Approval
Pharmacist-owner, 2026-09-04: approved all treatment plans and the one acceptance. Next full review August 2027, or sooner after a new system or vendor, a change of PMS, a hire, or an incident.
