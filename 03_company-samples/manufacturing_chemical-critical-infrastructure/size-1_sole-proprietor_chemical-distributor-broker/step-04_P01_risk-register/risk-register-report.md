# Risk Register Report: Cris Santos Company | Chemical | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (specialty chemical distributor, broker) |
| Size tier | Sole Proprietorship (owner only, 0 employees) |
| Vertical | Chemical |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also serves as | The cyber and information part of the transportation security risk assessment that 49 CFR 172.802(a) requires in the hazmat security plan (HSP-01, P06) |
| Prepared | 2026-09-11 by the owner, with the on-call IT technician |
| Risk owner and approver | Owner (owner, security officer, and risk acceptor for every risk) |
| Approved | 2026-10-05 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-08, paper in the home office, and the contracted services that touch shipments (suppliers' shipping offices, carriers, the ERI provider). Processes come from the BIA (P05). Physical risks at the suppliers' docks and on the road belong to the suppliers' and carriers' own plans; this register covers the part the broker controls: **the information that releases, describes, and pays for each shipment.**

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, three fixed rules apply:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan and are never accepted as they are. Any risk that could put hazmat in the wrong hands is treated, whatever its rating.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the two 2026 near misses (the lookalike-domain request and the AI-drafted packing group), the gap analysis (P03), and a walk through every account and device with the IT technician on 2026-09-10.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories. A diverted hydrogen peroxide load is rated Very High because it combines safety, regulatory, and business harm.
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 2 |
| Moderate | 8 |
| Low | 4 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Forged pickup authorization from a taken-over email account diverts a bulk hydrogen peroxide load | Very High | Email MFA; HSP-01 call-back and pickup-number rule; supplier hold-release instruction | Owner | 2026-10-31 |
| R-002 | Business email compromise redirects a customer or supplier payment | High | Email MFA; call-back before any bank-detail change; payee-change alerts | Owner | 2026-10-31 |
| R-004 | Bulk hydrogen peroxide offered with no security plan and lapsed training | High | Adopt HSP-01; recurrent and in-depth security training | Owner | 2026-11-30 |
| R-003 | Impostor or fictitious customer orders hydrogen peroxide (as on 2026-06-17) | Moderate | Know-your-customer steps in HSP-01; record and report suspicious orders | Owner | 2026-10-31 |
| R-005 | Wrong hazmat description on a BOL | Moderate | Locked product description sheet; no AI-drafted descriptions | Owner | 2026-10-31 |
| R-006 | ERI provider lacks a product's emergency information | Moderate | New-product checklist; annual reconciliation | Owner | 2026-10-31 |
| R-011 | Owner unavailable while loads are in transit | Moderate | Hold-release instruction; coverage arrangement; sealed recovery codes | Owner | 2026-12-31 |

The three highest risks share one cause: **the email account can release hazmat and move money, and it is protected only by a reused password.** Turning on MFA costs nothing and reduces R-001, R-002, R-007, and R-008 at once. The second cause is regulatory: the business never wrote the security plan the HMR requires for bulk hydrogen peroxide (R-004). HSP-01 (P06) closes the plan gap and puts the call-back controls for R-001 and R-003 in writing.

## 4. Treatment summary
- **Free fixes first (by 2026-10-15):** email MFA and a unique passphrase, password manager, standard laptop account, end of family use of the laptop (R-001, R-002, R-009).
- **Process changes in force from 2026-10-05:** HSP-01 call-back verification for pickups, ship-to changes, new customers, and bank details; a locked product description sheet for BOLs; no AI-drafted hazmat descriptions (R-001, R-003, R-005).
- **Budgeted (about $400 a year):** password manager, a third-party backup for the email and file suite, a new router, and the recurrent HMR course with an in-depth security module.
- **By 2026-12-31:** driver data purge, coverage arrangement, sealed recovery codes (R-008, R-011).
- **Accepted (Low):** R-014 (email suite outage; provider commitments and the phone fallback meet the BIA) and R-015 (hurricane; bulk releases are held under a warning).

## 5. Approval
Owner, 2026-10-05: approved all treatment plans and the two acceptances. Next full review in September 2027 with the annual HSP-01 review (172.802(c)), or sooner after a new product, a new supplier or carrier relationship, a hire, or an incident.
