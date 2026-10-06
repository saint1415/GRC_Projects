# Risk Register Report: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed staffing and temporary help firm, NAICS 561320) |
| Size tier | Mid-Market (600 internal staff; about 3,600 associates on assignment in an average week) |
| Vertical | Administrative and Support and Waste Management and Remediation Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also supports | "Reasonable measures" under Fla. Stat. 501.171(2); the records security program for electronic Forms I-9 (8 CFR 274a.2(g)); NIST CSF 2.0 ID.RA (P03 benchmark); the SOC 2 risk assessment criteria CC3.1 to CC3.4 (P09) |
| Prepared | 2026-08-07 by the Security Manager and the vCISO; R-052 added 2026-08-26 from P07 testing |
| Approved | 2026-09-22: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High, and the risk appetite); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (Light Industrial with the 6 on-site programs, Office and Professional, Healthcare Staffing, Managed Workforce Solutions) and HQ shared services; the Associate Payroll and Applicant Tracking Platform (APATP) and the systems around it (`../00_company-facts.md` section 3); and the vendors that hold firm data. Processes and impact values come from the BIA (P05); vulnerabilities come from the SSP (P02), the cloud mapping (P04), the gap analysis (P03), and the control assessment (P07).

**What the firm is protecting.** About 168,000 associate records with SSNs and bank accounts, about 610,000 candidate profiles, about 10,900 consumer reports a year, Form I-9 records and document images since 2012, medical information for about 2,600 clinicians, finger templates for about 1,300 associates, and a weekly payroll of about $1.45 million.

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
| Pay continuity | **Very low** | No risk that could stop associates being paid on the regular payday is accepted above Moderate. Measure: R-001 and R-005 at Moderate or lower by 2026-12-31 |
| Worker personal information | **Low** | No risk of a breach affecting 1,000 or more associates or candidates is accepted above Moderate. Measure: R-002, R-003, and R-052 at Moderate or lower by 2027-03-31 (R-052 by 2026-10-15) |
| Clinician placement safety | **Very low** | No clinician starts a shift without verified credentials; no risk to that control is accepted above Low. Measure: credential verification exceptions per month (0 today, tracked by the Credentialing Manager) |
| Regulatory compliance | **Low** | No binding Form I-9, E-Verify, FCRA, ADA medical file, or Florida requirement may stay Not met beyond 2027-06-30 (P03) |
| Fair hiring and AI | **Low** | No AI tool may make, or be a substantial factor in, an employment decision without bias testing, candidate notice, and human review (P10). Measure: R-015 at Low by 2027-03-31 |
| Client commitments | **Low** | MSP availability, notice, and SOC 2 commitments are met. Measure: SOC 2 Type 2 report issued by 2027-11-30 (R-032) |
| Third parties | **Moderate**, with conditions | SaaS is used widely, but no vendor receives Restricted data without security terms, and every Tier 1 vendor is reviewed each year (P09) |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $100,000 insurance retention are tolerable. Scenarios above $1 million need a treatment that lowers likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the vertical overlay, the BIA, interviews with every process owner and 3 Branch Managers, the 2026 H1 incident log (including 41 pay diversion cases), the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (P05 section 3).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 6 |
| Moderate | 34 |
| Low | 11 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 48 Mitigate, 4 Accept (R-037, R-039, R-040, R-041, all Low). Status: 33 Open, 15 In progress, 4 Accepted.

Cyber insurance ($5 million limit, $100,000 retention) and the crime policy's $250,000 social engineering sublimit transfer part of the financial exposure for R-001 to R-004 and R-052. Insurance is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to associates or operations.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-004 | Ransomware with data theft halts dispatch and the integration platform before payroll | Very High | Kiosk segmentation; restore tests of the integration platform and archive; separate backup administrators; tabletop | IT Director | 2027-03-31 |
| R-001 | Associate portal takeover and pay diversion at scale | High | App-based codes or passkeys; hold or call-back on new bank accounts; device-change alerts | Director of Payroll and Billing | 2026-12-31 |
| R-002 | Payroll specialist account takeover by push-relay phishing; register exported and pay diverted | High | Phishing-resistant authenticators; payroll export and bank-change alerts; fraud training | Security Manager | 2027-03-31 |
| R-003 | Bulk theft of SSNs and bank accounts from the data warehouse | High | Last-4 masking; 6 named analysts; query logging | Security Manager | 2026-12-31 |
| R-005 | Payroll platform outage on payroll day | High | Off-cycle manual payroll procedure; tested pay card and ACH path; payroll outage tabletop | Director of Payroll and Billing | 2026-12-31 |
| R-015 | AI ranking auto-advance disadvantages a protected group | High | Sort-only mode; bias testing and monitoring; notice and accommodation path (P10) | Director of Recruiting Operations | 2026-11-30 |
| R-052 | Exposed payroll API key (found in P07) | High | Rotate; secrets service; split keys by job; secret scanning | IT Director | 2026-10-15 |

**Themes.**
- **Money and identity flow through SaaS sign-ins (R-001, R-002, R-035, R-052).** The firm's MFA for staff is good, but associates still use SMS codes, push approvals can be relayed, and one integration key bypasses sign-in altogether. The 41 diversion cases in 2026 H1 show this is already happening.
- **Too much data, kept too long, in too many places (R-003, R-006, R-007, R-014, R-034).** Full SSNs are copied to the warehouse, I-9 images are visible to 262 users, and nothing has been purged since 2012. Every breach scenario above costs 3 to 4 times more because of it.
- **Detection stops at the SaaS boundary (R-021, R-042).** Endpoints and the cloud are watched 24x7; payroll exports, bank changes, and ATS downloads are not.
- **Payday is the firm's hardest deadline (R-004, R-005, R-025).** No manual payroll procedure exists, so a vendor outage or ransomware in payroll week would turn into missed wages.
- **AI adopted without governance (R-015 to R-018).** Two tools affect who gets work. P10 addresses them.

R-052 was added on 2026-08-26 after the co-sourced internal audit firm found the payroll API key in the integration platform's container image during P07 testing.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-22, $410,000 one-time and $257,000 a year):**
- Associate portal authentication upgrade and bank-change hold ($60,000 a year)
- Phishing-resistant authenticators for 40 payroll, billing, and administrator users ($25,000 one-time)
- SaaS log connectors and MSSP payroll fraud use cases ($85,000 a year)
- Data warehouse masking and access redesign ($40,000 one-time)
- Kiosk segmentation at Branches 6-14 ($70,000 one-time)
- Archive backups and restore testing ($30,000 one-time; $12,000 a year in cloud cost)
- Vendor risk program, including contract terms and SOC 2 reviews ($45,000 a year)
- AI bias testing with an independent statistician ($35,000 a year; P10)
- Secrets management and code scanning for the integration platform ($20,000 a year)
- Records purge project and certified destruction ($25,000 one-time)
- Outside counsel review of biometric, AI, and recording notices and breach notice templates ($30,000 one-time)
- SOC 2 Type 1 and Type 2 examinations by an independent CPA firm ($190,000 across 2027; P09)

Each funded item maps to a P07 POA&M entry.

**Accepted (4, all Low, by the risk owner):** R-037, R-039, and R-040 (IT Director); R-041 (Director of Recruiting Operations).

**Contract actions:** AI vendor data use addendum (R-017, 2026-12-31); timekeeping vendor biometric and breach terms (R-008, 2027-03-31); credentialing vendor questionnaire and SOC 2 commitment (R-030, 2027-03-31); ATS recovery and data-return terms at renewal (R-012, R-023).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the firm's enterprise risk register as one line, "Cybersecurity, data protection, and payroll resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system or program owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| APATP (SSP in P02) | Security Manager | 38 risks whose affected assets include SYS-01 to SYS-06, SYS-10, SYS-13, or SYS-14 (filter the `affected_asset_or_process` column) |
| Payroll (BP-01, BP-02, BP-12) | Director of Payroll and Billing | R-001, R-002, R-005, R-009, R-027, R-052 |
| Healthcare Staffing | Vice President, Healthcare Staffing | R-007, R-024, R-030, R-049, R-050 |
| Managed Workforce Solutions (SOC 2 system, P09) | Vice President, Managed Workforce Solutions | R-020, R-027, R-031, R-032, R-045 |
| AI portfolio (P10) | Director of Recruiting Operations | R-015, R-016, R-017, R-018 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments, 2026-09-22.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-22.
- Board audit committee: received the results on 2026-09-22. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example an acquisition, R-048, or a new AI tool that ranks candidates) or a significant incident.
