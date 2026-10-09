# Risk Register Report: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent recruiter: contract staffing and direct-hire placement) |
| Size tier | Sole Proprietorship (owner-recruiter only, 0 employees) |
| Vertical | Administrative and Support and Waste Management and Remediation Services |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | The "reasonable measures" duty in Fla. Stat. 501.171(2): a documented risk assessment is the basis for deciding what is reasonable for this business |
| Prepared | 2026-07-24 by the owner-recruiter, with the on-call IT support technician (confidentiality agreement since 2026-07-17) |
| Risk owner and approver | Owner-recruiter (owner, security lead, privacy contact, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-10, paper in the home office, and the contracted services (back-office partner, outside bookkeeper, IT support technician), as listed in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv). Processes come from the BIA (P05). The partner's own payroll, I-9, and background check operations are outside the scope; the risk the owner carries from them is captured as supplier risk (R-003, R-008).

**Risk tolerance.** The owner-recruiter owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as they are. A risk that could lead to unlawful discrimination against candidates is never accepted, whatever its level.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the intake evidence ([evidence register](../step-00_P00_intake/evidence-register.csv)), the BIA, the gap analysis (P03), and a walk through the mailbox, the ATS, the partner portal, the laptop, the phone, and the router with the IT technician on 2026-07-21 (EV-029). The gap analysis ran in the same self-assessment week, and the two shared findings.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the account and device reviews (EV-001, EV-008, EV-020, EV-021), the mailbox review (EV-009), the vendor records (EV-013, EV-032), the AI records (EV-005, EV-027), and the owner's self-review (EV-030). A one-person business keeps no ticket or incident log to count, so a rating with no evidence behind it would be a guess, and none was made.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories.
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

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
| R-001 | Email takeover through phishing that defeats SMS codes | High | Authenticator-app MFA, sign-in alerts, monthly review, training | Owner-recruiter | 2026-09-15 |
| R-002 | ATS takeover and export of about 3,400 candidate records | High | ATS MFA; unique passphrase in a password manager | Owner-recruiter | 2026-09-15 |
| R-004 | SSNs, dates of birth, and ID images for 77 people kept with no purpose | High | Delete after the partner confirms its copies; SSNs only in the portal or by phone | Owner-recruiter | 2026-10-31 |
| R-003 | Contractor pay diverted through a forwarded bank-change form | Moderate | Partner accepts bank changes only through contractor self-service or a call-back | Owner-recruiter | 2026-09-30 |
| R-005 | AI match add-on screens out qualified applicants unfairly | Moderate | Score as a sort aid only; human review; notice and accommodation (P10) | Owner-recruiter | 2026-10-31 |
| R-009 | Owner-recruiter unavailable (single point of failure) | Moderate | Continuity sheet; sealed recovery codes; partner coverage | Owner-recruiter | 2026-12-31 |

**One pass.** The register was completed on 2026-07-24 from intake and self-assessment evidence. The control tests ran on 2026-07-23, inside the same week, so this pass already reflects them: R-004 uses the counts from the mailbox and device search (EV-SI-12), and R-013 the router's default password (EV-IA-5). No risk was added after P07 testing. The `assessment_pass` column records the pass for each risk.

The three High risks share one cause: **sensitive data the business no longer needs sits behind accounts protected by phishable codes or by a reused password.** Two settings (authenticator-app MFA on email and MFA on the ATS) and one clean-up (deleting the SSNs and IDs) cut all three. The clean-up matters most: under Fla. Stat. 501.171, a mailbox with no SSNs or ID numbers in it turns most email incidents from a notifiable breach into a non-event.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** authenticator-app MFA on email, ATS MFA, a password manager, deleting the two background reports, deleting chatbot history, the bank-change request to the partner, and adopting the P08 runbook.
- **Budgeted (about $300 a year):** a password manager and a small security course; a router that supports a separate work network if the provider's router cannot (about $150 once).
- **Contract actions by 2026-11-30:** security addendum with the partner (R-008); AI add-on training opt-out and feature list from the ATS vendor (R-005).
- **Accepted (Low):** R-011 (laptop theft; disk encryption takes the data out of 501.171) and R-015 (hurricane; all systems are SaaS and contractors are paid by the partner).

## 5. Approval
Owner-recruiter, 2026-08-31: approved all treatment plans and the two acceptances. Next full review July 2027, or sooner after a new system, a new vendor or AI tool, a first hire, or an incident.
