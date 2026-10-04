# Risk Register Report: Cris Santos Company | Educational Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (tutoring and educational support service) |
| Size tier | Sole Proprietorship (owner-tutor only, 0 employees) |
| Vertical | Educational Services |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also satisfies | The COPPA Rule's risk assessment, 16 CFR 312.8(b)(2): internal and external risks to the confidentiality, security, and integrity of personal information collected from children, and whether the safeguards are sufficient. This is the business's first one; it must be repeated at least annually |
| Prepared | 2026-07-17 by the owner-tutor, with the on-call IT technician (under a confidentiality and data-handling agreement since 2026-07-08) |
| Risk owner and approver | Owner-tutor (owner, security program coordinator, and risk acceptor for every risk) |
| Approved | 2026-07-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-09, paper worksheets and notes at home, the old laptop in storage, and the contracted helpers (IT technician, tax preparer). Processes come from the BIA (P05). The register covers all student and parent information, not only what COPPA reaches: records parents hand over (report cards, IEP and 504 plans, evaluations) are protected under Fla. Stat. 501.171(2) and the enrollment agreement.

**Risk tolerance.** The owner-tutor owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules (POL-01 4.4):
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Never accepted as they are. Any risk that exposes children's information and is rated High must have its free fixes in place before the next term starts.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the COPPA requirements (P03), and a walk through the laptop, phone, router, and each SaaS account with the IT technician on 2026-07-14 and 2026-07-15.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale, combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (P05 section 3). Harm to children (exposure of disability information, contact by a stranger) counts at the Regulatory and Reputation levels.
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
| R-001 | Ransomware on the laptop; synced student folders and portal passwords stolen | High | Separate family account, disk encryption, MFA, independent backup, runbook | Owner-tutor | 2026-09-30 |
| R-002 | Takeover of the email and files suite | High | MFA now; password manager; named-parent sharing | Owner-tutor | 2026-08-14 |
| R-003 | Takeover of the website-builder administrator (children's portal) | High | MFA; close inactive accounts; vendor assurances | Owner-tutor | 2026-08-14 |
| R-004 | Theft or loss of the unencrypted laptop | High | Built-in full-disk encryption | Owner-tutor | 2026-08-14 |
| R-005 | FTC COPPA finding: no notice, uninformed consent, no retention policy | Moderate | Online notice, new direct notice and fresh consent, retention schedule | Owner-tutor | 2026-08-14 |
| R-006 | Student information in a consumer AI assistant | Moderate | Stop; deletion request; narrowed use (P10) | Owner-tutor | 2026-08-14 |
| R-007 | Over-retention widens any breach | Moderate | Retention schedule and first purge | Owner-tutor | 2026-09-30 |

The four High risks share one cause: **children's information sits in three SaaS accounts protected only by passwords and on an unencrypted laptop the family also uses.** Four settings that cost nothing (MFA on three accounts and disk encryption) and one separate family account reduce R-001 to R-004 before the fall term starts on 2026-08-17. Deleting what is no longer needed (R-007) then shrinks every breach scenario: today a laptop theft would reach about 265 children, while under the retention schedule it would reach about 55 current students and those in their first year after stopping.

## 4. Treatment summary
- **Free fixes before the fall term (by 2026-08-14):** MFA on the email suite, website builder, and video platform; laptop encryption and a 5-minute lock; a separate family account; password manager and deletion of the portal password spreadsheet; router admin password; stopping student data in the AI assistant; the children's privacy notice and fresh parent consent.
- **Budgeted (about $400 a year):** password manager, a backup service that desktop sync cannot overwrite, and a business-tier AI assistant with no-training terms. A cyber insurance quote is requested (R-013).
- **By 2026-09-30:** first retention purge and old-laptop wipe (R-007); P08 walkthrough (R-013); independent backup (R-001).
- **Accepted (Low):** R-014 (client-management SaaS outage; vendor commitments meet the BIA) and R-015 (hurricane; data is in SaaS). R-009 (home network) is Low but is still treated because the fix is free.

## 5. Approval
Owner-tutor, 2026-07-31: approved all treatment plans and the two acceptances. Next full review July 2027 (16 CFR 312.8(b)(2) requires at least annually), or sooner after a new system, a new vendor, a hire, or an incident.
