# Risk Register Report: Cris Santos Company | Management of Companies and Enterprises | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (the owner's management business for three wholly owned LLCs: Storage, Rentals, Laundry) |
| Size tier | Sole Proprietorship (owner only, 0 employees; the LLCs employ 3 part-time workers) |
| Vertical | Management of Companies and Enterprises |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also supports | The "reasonable measures" duty of each LLC and of the sole proprietorship as third-party agent (Fla. Stat. 501.171(2)); the CSF 2.0 portfolio profile outcomes ID.RA-03 to ID.RA-06 (P03) |
| Prepared | 2026-07-31 by the owner-manager, with the on-call IT technician (under a confidentiality and security agreement since 2026-07-24) |
| Risk owner and approver | Owner-manager (risk owner and risk acceptor for every risk, for every entity) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The four entities as one system: the Shared Back-Office Platform (SYS-01 to SYS-04, SYS-08, SYS-10), the owner's administrator access to each LLC's system (SYS-05 to SYS-07), the site devices (SYS-09), paper move-in forms, and the contracted services (bookkeeper, IT technician, CPA firm, maintenance contractor). Processes come from the BIA (P05).

**Why one register for four entities.** The LLCs are legally separate, but they share one identity, one owner, one bookkeeper, and one set of habits. Every High risk below hits all three LLCs at once. The register names the affected LLC where a risk is local (for example R-005 Storage, R-006 Laundry, R-003 Rentals).

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. A risk that could stop payroll or lock tenants out for longer than the BIA allows is never accepted.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the gap analysis (P03), and a walk through each system's settings and both sites with the IT technician (2026-07-28 to 2026-07-30).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (scaled to the LLCs' combined revenue of about $750,000).
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
| R-001 | Takeover of the owner's email account, the recovery address for every system | High | App-based MFA and hardware key; separate administrator account; monthly sign-in review | Owner-manager | 2026-10-31 |
| R-002 | Payment redirection through a fake bank-change request | High | Callback rule; payee changes by the owner only; bookkeeper role reduced | Owner-manager | 2026-09-30 |
| R-010 | Owner unavailable: nobody can run four entities | High | Sealed access sheet with the attorney; limited Storage authority; bank signer question | Owner-manager | 2026-12-31 |
| R-008 | Email and files lost with no backup | Moderate | Backup service; monthly exports; restore test | Owner-manager | 2026-10-31 |
| R-009 | AI assistant used on rental applications and applicant choice | Moderate | POL-01 9.5 rules; Restricted folder excluded (P10) | Owner-manager | 2026-09-30 |
| R-015 | Reused passwords and no MFA on LLC administrator accounts | Moderate | Password manager; MFA | Owner-manager | 2026-09-15 |

**The pattern.** Two of the three High risks have the same root: **one email account, protected by a text-message code, controls four businesses and their money.** R-001 is the entry point, R-002 is how the attacker gets paid, and R-008 is why recovery would be slow. The third High risk, R-010, is the same concentration seen from the other side: the one person who holds that account is also the only way back in. The holding structure separates liability, not technology.

## 4. Treatment summary
- **Free or low-cost fixes first (by 2026-09-30):** app-based MFA everywhere, a password manager (about $40 a year), the callback rule for payment changes, individual Laundry PINs, the Storage desktop sign-in and encryption, the gate password, AI use rules, and adopting the P08 runbook.
- **Budgeted (about $500 a year):** a backup service for the suite (about $150), two hardware security keys (about $100 once), and the password manager.
- **Contract actions by 2026-10-31:** confidentiality and security terms with the bookkeeper and a vendor list with notice contacts (R-011).
- **By 2026-12-31:** the successor access envelope and bank signer arrangements (R-010).
- **Accepted (Low):** R-013 (LLC system outage; manual fallbacks meet the BIA) and R-014 (hurricane; every system is reachable from the owner's phone). R-006 (laundromat Wi-Fi) is Low but still treated, because the fix is a free router setting.
- **Cyber insurance:** none today. The owner will get quotes for one policy covering the sole proprietorship and all three LLCs by 2026-12-31 (Share/Transfer is considered for R-001 and R-002 at the next review).

## 5. Approval
Owner-manager, 2026-08-31: approved all treatment plans and the two acceptances, for the sole proprietorship and, as sole member and manager, for each LLC. Next full review July 2027, or sooner after buying or selling an LLC, a new system or vendor, a new employee at any LLC, or an incident.
