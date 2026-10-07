# Risk Register Report: Cris Santos Company | Financial Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed payment processor serving merchants) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Financial Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | FTC Safeguards Rule written risk assessment, 16 CFR 314.4(b); PCI DSS 12.3.1 inputs (the targeted risk analyses themselves are tracked in P03) |
| Prepared | 2026-07-31 by the Director of Information Security (Qualified Individual) and the vCISO; R-050 added 2026-08-14 from P07 testing |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High, and the risk appetite); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (Merchant Processing, Integrated Payments, Settlement and Treasury Operations, Risk, Fraud, and Compliance, Merchant Services, and Corporate), the Payment Processing Platform (PPP; SSP in P02) across Cloud A, Cloud B, and both colocation cages, the 34 PCI DSS service providers and the 41 vendors inherited from the acquisition, and the AI portfolio (P10). Processes and impact values come from the BIA (P05); vulnerabilities come from the cloud mapping (P04), the gap analysis (P03), and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |
| Any level | No one | A risk that would leave a PCI DSS requirement "not in place" at the annual ROC cannot be accepted, because the AOC and both sponsor relationships depend on it |

**Why the Safeguards Rule matters here.** 16 CFR 314.4(b)(1) requires the risk assessment to be written and to include criteria for evaluating and categorizing risks, criteria for assessing confidentiality, integrity, and availability, and requirements for how risks will be mitigated or accepted. Sections 1 and 2 of this report are those criteria.

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-15. They were written for the first time this year (gap 14 in `../00_company-facts.md`).

| Area | Appetite | Statement and measure |
|---|---|---|
| Card data confidentiality | **Very low** | No risk of a card data compromise affecting either platform is accepted above Moderate. Measure: R-001 to R-003 at Moderate or lower by 2026-12-31 |
| PCI DSS and sponsor bank standing | **Very low** | The company will not carry a requirement into the ROC that would be "not in place" without an interim measure. Measure: High P03 gaps open at ROC fieldwork (2026-11-09); target 0 |
| Availability of authorization | **Low** | Recovery must meet the BIA RTOs for every High-criticality process (P05). Measure: every High process has a passed recovery test in the last 12 months (today 0 of 7) |
| Integrity of settlement and funding | **Very low** | No unreconciled break or unsigned funding file is tolerated as normal operation. Measure: R-052 treated by 2027-03-31; daily reconciliation breaks cleared within 1 business day |
| Regulatory notices | **Very low** | Every notice owed to card brands, sponsor banks, the FTC, merchants, and states goes out on time. Measure: designated contacts for both banks confirmed each quarter |
| Third parties | **Moderate**, with conditions | Service providers are used widely, but none touches account data without a current AOC or inclusion in the ROC and a responsibility matrix |
| Innovation and AI | **Moderate** | AI is welcome in fraud, underwriting, disputes, support, and engineering, but only through the AI and model risk process in P10. No model makes a decision about a merchant or cardholder without validation |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $5 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the cloud mapping (P04), interviews with every process owner, the gap analysis (P03), the control assessment (P07), Visa's What To Do If Compromised guidance on common compromise patterns, and the two P08 scenarios.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, merchant operations, regulatory and card brand, reputation). A card data compromise on either platform is rated Very High: card brand assessments, forensic costs, notices across many states, and possible loss of a sponsor bank.
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 12 |
| Moderate | 27 |
| Low | 12 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 47 Mitigate, 5 Accept (R-013, R-031, R-034, R-041, R-044). Status: 20 Open, 27 In progress, 5 Accepted.

Cyber insurance ($20 million limit, $500,000 retention) transfers part of the financial exposure for R-001 to R-005. It is not recorded as the treatment for any risk, because it does not lower the likelihood of a compromise or an outage.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Gateway compromise through a phished engineer with standing Cloud B administrator rights (P08 scenario 1) | Very High | PAM and security keys for Cloud B; remove standing roles; SIEM and MSSP onboarding; egress allow list | Director of Integrated Payments Engineering | 2026-11-06 |
| R-002 | E-skimming through the Integrated Payments hosted payment fields | High | Script inventory, integrity checks, tamper-detection | Director of Integrated Payments Engineering | 2026-10-30 |
| R-003 | Gateway exfiltration undetected because Cloud B is not monitored | High | Cloud B logs to the SIEM; MSSP use cases; DNS and egress monitoring | Director of Information Security | 2026-11-06 |
| R-004 | Integrated Payments portal account takeover | High | MFA and dynamic risk analysis; step-up for funding account changes | Director of Integrated Payments Engineering | 2026-10-30 |
| R-005 | Ransomware in the settlement environment delays funding (P08 scenario 2) | High | Replace unsupported servers; isolate management network; offline backup copy; tabletop with both banks | Director of Settlement and Treasury Operations | 2027-06-30 |
| R-006 | Authorization failover longer than the 2-hour MTD | High | Automated failover; semiannual tests | VP Platform Engineering | 2027-03-31 |
| R-007 | Settlement DR misses the funding cutoff | High | Fix the DR runbook; test with both sponsor banks | Director of Settlement and Treasury Operations | 2027-02-28 |
| R-016 | Combined 2026 ROC finds requirements not in place | High | Close P03 High gaps or interim measures before 2026-11-09 | COO | 2026-11-06 |
| R-017 | Key misuse, or stale keys at the DR cage block decryption after failover | High | Replicate keys after every rotation; custodian review | VP Platform Engineering | 2026-11-30 |
| R-019 | Full PAN kept 7 years in the settlement archive enlarges any breach | High | Retention set to business need; purge or truncate older records before the ROC | Director of Settlement and Treasury Operations | 2026-11-06 |
| R-043 | A sponsor bank restricts or exits the relationship after a compliance failure | High | Monthly compliance status to both banks; SOC 2 Type 2 (P09) | CEO | 2027-06-30 |
| R-050 | Default credentials on settlement server management interfaces (found in P07) | High | Dedicated management network behind PAM; credential checks | VP Platform Engineering | 2026-10-15 |
| R-052 | Funding file altered before transmission | High | HSM signing; bank signature verification | Director of Settlement and Treasury Operations | 2027-03-31 |

**Themes.**
- **The acquisition created a second, weaker CDE (R-001 to R-004, R-008, R-011, R-038 to R-040, R-051).** The core platform is mature. The acquired gateway in Cloud B lacks PAM, monitoring, script controls, and MFA for portal users, and its 2026 validation is part of the combined ROC (R-016). This chain is the P08 gateway scenario.
- **Settlement is the legacy heart of the business (R-005, R-007, R-009, R-010, R-017, R-019, R-028, R-050, R-052).** Unsupported servers, a segmentation change that was not retested, default credentials, slow DR, unsigned funding files, and long PAN retention all sit in the colocation cages. These risks matter to both sponsor banks, because settlement and funding are covered services under 12 CFR 53.4 and 304.24.
- **Recovery is designed but not proven (R-006 to R-008).** Every High-criticality process in the BIA either missed its RTO in testing or has never been tested.
- **AI and models grew without governance (R-020 to R-025, R-046).** P10 addresses them.

Fixing R-001 to R-003 also reduces R-011, R-036, R-040, and R-051. Fixing R-050 and R-009 reduces R-005.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15, $1.6 million one-time and $640,000 a year):**
- Cloud B onboarding to the SIEM, MSSP, and PAM, and Cloud B guardrails ($220,000 one-time; $160,000 a year)
- Hosted payment field script monitoring and portal MFA for Integrated Payments ($60,000 one-time; $40,000 a year)
- Replacement of the 4 unsupported settlement servers and a dedicated management network ($520,000)
- Automated authorization failover and settlement DR improvements, including a test with both sponsor banks ($310,000)
- Funding file signing with HSM-held keys ($90,000)
- Two cloud security engineers ($330,000 a year)
- Contact center automatic pause-and-resume ($45,000 one-time; $30,000 a year)
- Model validation and AI governance support from an outside model risk firm ($120,000 one-time; $80,000 a year)
- SOC 2 readiness and Type 2 examination ($235,000 across 2027)

Smaller items (segmentation retest, archive truncation, chatbot PAN masking) come from the operating budget. Each funded item maps to a P07 POA&M entry.

**Migration.** Moving the gateway into the Cloud A landing zone (due 2027-09-30) is a separate capital project ($1.9 million) that retires most of the Integrated Payments risks. The interim controls above are required whether or not the migration stays on schedule.

**Accepted (5):** R-013 (Low, COO), R-031 (Low, COO), R-034 (Low, Director of Information Security), R-041 (Low, Director of Information Security), R-044 (Low, COO).

**Contract actions:** current AOCs and responsibility matrices for 7 service providers (R-014), due 2026-10-31; security schedules for the 20 largest ISV partners (CA-3 gap), due 2027-03-31; Bank B's designated contacts for 12 CFR 304.24 notices recorded (R-015), due 2026-10-15.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity, payment data, and processing resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks. The enterprise register also holds credit, liquidity, and merchant default risks owned by the CFO and the CRCO; R-043 is shared with those lines.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Core platform (Cloud A: SYS-01, SYS-04, SYS-05) | VP Platform Engineering | R-006, R-012, R-013, R-027, R-029, R-031, R-035, R-044, R-045 |
| Integrated Payments gateway (Cloud B: SYS-06) | Director of Integrated Payments Engineering | R-001, R-002, R-003, R-004, R-008, R-011, R-038, R-040, R-051 |
| Settlement and funding (colocation: SYS-02, SYS-03, SYS-16) | Director of Settlement and Treasury Operations | R-005, R-007, R-009, R-010, R-017, R-019, R-028, R-032, R-033, R-050, R-052 |
| AI and model portfolio (P10) | Chief Risk and Compliance Officer | R-020, R-021, R-022, R-023, R-024, R-025, R-046 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-013, R-031, and R-044, 2026-09-15.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-15. No High or Very High risk is accepted; all are under treatment.
- Board audit committee: received the results on 2026-09-15. Next report: 2026-12 quarterly meeting, together with the Qualified Individual's annual report (16 CFR 314.4(i)).
- Next full risk assessment: July 2027, or sooner after a significant change (for example the gateway migration) or a significant incident. The six-month PCI DSS scope confirmation (12.5.2.1) triggers a review of R-001 to R-005 each time.
