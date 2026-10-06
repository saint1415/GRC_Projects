# Risk Register Report: Cris Santos Company | Professional, Scientific, and Technical Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed CPA, tax, and advisory firm, with its attest affiliate) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Professional, Scientific, and Technical Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, and the Appendix I semi-quantitative values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | FTC Safeguards Rule written risk assessment, 16 CFR 314.4(b)(1) (criteria in section 2); HIPAA risk analysis input for the business associate ePHI, 45 CFR 164.308(a)(1)(ii)(A) (completed by the enclave-specific analysis due 2027-03-31) |
| Prepared | 2026-07-31 by the GRC Manager and the Director of Information Security (Qualified Individual); R-051 added 2026-08-14 from P07 testing |
| Approved | 2026-09-22: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High, and the risk appetite); presented to the audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (tax practice, tax operations, the Attest Firm, CAS, advisory, and enterprise functions), the Tax and Client Data Platform (TCDP, SSP in P02), the CAS platform (SYS-08), the audit and SOC engagement platform (SYS-09), about 85 service providers including the offshore preparation support vendor, and the AI tools (P10). Processes and impact values come from the BIA (P05). Vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-22.

| Area | Appetite | Statement and measure |
|---|---|---|
| Confidentiality of client tax data | **Low** | The Company will not accept a risk of a breach affecting 500 or more consumers (the FTC notification threshold) above Moderate. Measure: risks above Moderate with that potential (6 today: R-001, R-004, R-005, R-006, R-007, R-013; target 0 by 2027-06-30) |
| IRC 7216 compliance | **Very low** | No known practice that discloses tax return information without a permission or a signed consent is tolerated, because section 7216 is a criminal statute. Measure: R-011, R-033, R-039 at Low by 2027-01-15 |
| Filing deadlines | **Low** | Recovery must meet the BIA RTOs for every High-criticality process (P05) in peak season. Measure: every High process has a passed recovery test or exercise in the last 12 months |
| CAS client funds | **Very low** | No path by which one person or one forged request can move client money is accepted. Measure: R-020 and R-051 at Moderate or lower by 2026-12-31 |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no vendor receives customer information without security terms in its contract (314.4(f)(2)), and every Tier 1 vendor is reviewed each year (P09) |
| Innovation and AI | **Moderate** | The Company wants AI in data entry, research, and audit analytics, but only through the P10 review. No AI tool receives client data without a confirmed IRC 7216 basis, and no AI tool materially influences a hiring decision without adverse impact testing |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that lowers likelihood, not only insurance |

## 2. Method and 16 CFR 314.4(b)(1) criteria
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the IRS Security Summit warnings in Pub. 4557 (phishing, account takeover, fraudulent returns), the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood that the event causes adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, client harm, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range built from the BIA values and the notification population, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are for prioritizing, not actuarial figures.

How this method meets the written risk assessment content in 314.4(b)(1):

| 314.4(b)(1) requires | Where it is met |
|---|---|
| (i) Criteria for evaluating and categorizing identified risks or threats | Steps 2 to 4: the SP 800-30 likelihood and impact scales and Tables G-5 and I-2 |
| (ii) Criteria for assessing the confidentiality, integrity, and availability of systems and customer information, including the adequacy of existing controls | The FIPS 199 categorization in the SSP (P02 section 6), the BIA impact categories (P05), and the `existing_controls` column, rated against the P03 and P07 results |
| (iii) How identified risks will be mitigated or accepted, and how the program will address them | The acceptance authorities and appetite in section 1, the `treatment` and `treatment_plan` columns, and the POA&M (P07) |

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 10 |
| Moderate | 31 |
| Low | 10 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 51 Mitigate, 1 Accept (R-026). Status: 36 Open, 15 In progress, 1 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-001, R-004, and R-005. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to clients.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-004 | Ransomware with data theft in filing season | Very High | Privileged access management for directory and SaaS admins; vault service accounts; quarterly restore tests; ransomware runbook and executive tabletop | Chief Information Officer | 2027-01-15 |
| R-001 | Business email compromise by session token theft | High | Security keys for partners, admins, finance, and CAS payroll; compliant devices for mail; inbox-rule alerts restored | Director of Information Security | 2027-01-15 |
| R-005 | Bulk export of client files without detection | High | DMS and tax software logs in the SIEM with bulk-download alerts; egress alerting; team-based DMS permissions | Director of Information Security | 2027-01-15 |
| R-006 | Client portal account takeover | High | Mandatory client MFA; identity check at enrollment | Director of Tax Operations | 2027-01-15 |
| R-007 | Privileged account takeover with standing admin rights | High | Separate admin accounts with security keys; just-in-time elevation; break-glass accounts | Director of Information Security | 2026-12-31 |
| R-011 | Offshore staff see unmasked SSNs (26 CFR 301.7216-3(b)(4)) | High | Masked-image DMS view for the offshore pool; consent gate before routing | Director of Tax Operations | 2026-12-15 |
| R-013 | Service provider breach with no contract security terms | High | Vendor tiering; contract amendments; annual Tier 1 reviews | GRC Manager | 2027-03-31 |
| R-017 | Tax software vendor outage before a deadline | High | Deadline-week outage procedure; early-extension triggers; contract terms | National Tax Practice Leader | 2027-01-15 |
| R-020 | Fraudulent bank change diverts CAS client funds | High | Call-back on every bank change; second approver; hold on first payments | CAS Practice Leader | 2026-12-31 |
| R-035 | AI resume screening with adverse impact | High | Suspend auto-ranking; adverse impact testing; Colorado notices and human review from 2027-01-01 | Chief People Officer | 2026-12-31 |
| R-051 | Former CAS staff accounts outside SSO (found in P07) | High | Federate payroll and bill pay to SSO; monthly reconciliation | CAS Practice Leader | 2026-12-31 |

**Themes.**
- **Identity is the front door (R-001, R-006, R-007, R-050, R-051).** MFA is everywhere, but the methods in use do not stop token theft, help desk impersonation, or accounts that live outside SSO.
- **The Company cannot see what happens inside its SaaS applications (R-003, R-005, R-030).** It detects attacks on endpoints and identities well. Bulk exports from the tax software or DMS would go unnoticed.
- **IRC 7216 is a design constraint, not a paperwork item (R-011, R-033, R-038, R-039).** The offshore program and the AI drafting feature were set up for capacity, and the 7216 conditions were not built into the workflow.
- **Money moves through CAS (R-019, R-020, R-051).** CAS turns a data-security program into a payments program, which is why the appetite for client funds is Very low.
- **AI adopted without governance (R-032 to R-037).** P10 covers them.

**Change from the July 2025 assessment.** The 2025 register had 34 risks. New this year: R-011 (offshore SSNs), R-020 and R-051 (CAS funds), R-033 to R-037 (AI), R-046 (acquisitions), and R-050 (help desk impersonation). R-001 rose from Moderate to High because number matching does not stop session token theft and because the MSSP suppressed inbox-rule alerts during the 2026 filing season.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO on 2026-09-22): $815,000 one-time, including $210,000 for SOC 2 readiness and the Type 2 examination (P09), and $360,000 a year:**
- Security keys for about 220 users and device compliance for mail ($45,000)
- Privileged access management for directory and SaaS administrators ($140,000 one-time, $60,000 a year)
- SIEM onboarding of tax software, portal, DMS, and CAS activity, and data loss prevention rules ($95,000 a year through the MSSP)
- DMS redaction module and offshore consent gate ($120,000)
- SSO federation and bank-change controls for the CAS platform ($60,000)
- Recovery testing program, including the workpaper server and CAS fallback ($80,000)
- Retention and disposal project ($90,000)
- AI governance: adverse impact testing and counsel review ($70,000)
- One additional security engineer ($165,000 a year) and a wider penetration test scope ($40,000 a year)

Each funded item maps to a P07 POA&M entry.

**Accepted (1):** R-026 (Low; laptops and phones are encrypted and can be wiped), accepted by the Director of Information Security.

**Contract actions:** security terms for 31 service providers (R-013), vendor remote access through the broker (R-014), offshore vendor turnover reporting and audit (R-012), tax software deadline commitments (R-017), and AI vendor terms (R-033, R-035), due 2026-11-30 to 2027-03-31.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the Company's enterprise risk register as one line, "Cybersecurity, data protection, and technology resilience", owned by the Chief Operating Officer and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file kept by each owner, not separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Tax and Client Data Platform (TCDP; SSP in P02) | National Tax Practice Leader with the Director of Information Security | 38 risks whose affected assets include SYS-01 to SYS-06 or SYS-10 to SYS-12 (filter the `affected_asset_or_process` column) |
| CAS service (P09 SOC 2 scope) | CAS Practice Leader | R-013, R-018, R-019, R-020, R-051 |
| Offshore preparation program | Director of Tax Operations | R-011, R-012, R-038, R-039 |
| Business associate ePHI | Director of Information Security (HIPAA Security Officer) | R-004, R-005, R-022 |
| AI portfolio (P10) | General Counsel (chair of the AI review group) | R-032, R-033, R-034, R-035, R-036, R-037 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments, 2026-09-22.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-22.
- Audit committee: received the results on 2026-09-22. They will also go to the board in the Qualified Individual's written report on 2026-10-27 (314.4(i)).
- Next full risk assessment: July 2027, or sooner after a material change such as an acquisition (R-046) or a significant security event (314.4(b)(2) and (g)).
