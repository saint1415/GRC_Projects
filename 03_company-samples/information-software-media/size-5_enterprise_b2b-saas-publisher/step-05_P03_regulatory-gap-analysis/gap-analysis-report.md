# Regulatory Gap Analysis: Cris Santos Company | Information | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded B2B SaaS software publisher; headquartered in Florida; customers in every state) |
| Tier / Vertical | Enterprise / Information |
| Regulations analyzed | FTC Act Section 5 (reasonable security under the FTC's business guidance, and the company's own security, privacy, and AI representations); SEC Form 8-K Item 1.05 and Reg S-K Item 106; CCPA and CPPA regulations (service provider duties, cybersecurity audit, risk assessments, ADMT); state comprehensive privacy laws as a processor (generic); Fla. Stat. 501.171 (worked example) and other state breach laws (generic); FedRAMP for the Government Edition; bank service provider notification (12 CFR 53.4, 225.303, 304.24); DOJ Data Security Program (28 CFR Part 202); applicability checks for COPPA, CPNI, PADFA, HIPAA, and CIRCIA |
| Not repeated here | SOC 2 criterion-level readiness for the three service lines (P09, which reuses the `related_tsc_criteria` column); SOX Section 404 IT general controls (separate program) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the Chief Privacy Officer; outside privacy counsel reviewed sections 1 and 6; sampling reperformed by Internal Audit for 8 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the cybersecurity and risk committee of the board, 2026-09-10 |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| FTC Act Section 5 (N51-R01) | **Yes** | For-profit company in commerce, not in a 45(a)(2) carve-out; no size threshold. Unfairness (15 U.S.C. 45(n)) reaches unreasonable security; deception reaches untrue security, privacy, and AI statements |
| SEC Item 1.05 and Item 106 (N51-R08) | **Yes** | Exchange Act registrant, not a smaller reporting company |
| CCPA and CPPA regulations (N51-R03) | **Yes** | Revenue far above $26,625,000 (Cal. Civ. Code 1798.140(d)); a business for its own data and a service provider for customer data. The cybersecurity audit applies under Cal. Code Regs. tit. 11, 7120(b)(2)(A) because the company processed personal information of about 420,000 California marketing contacts in 2025; with 2026 revenue over $100 million, the first audit covers 2027-01-01 to 2028-01-01 and the report is due 2028-04-01 (7121(a)(1)) |
| State comprehensive privacy laws | **Yes, as a processor** | Customers are controllers under these laws in many states. Treated generically. Florida's Digital Bill of Rights does not apply: its controller definition (Fla. Stat. 501.702) requires more than $1 billion in revenue **and** one of three business models (online advertising revenue, a consumer smart speaker service, or a large app store), none of which the company has |
| Fla. Stat. 501.171 and other state breach laws | **Yes** | Covered entity for its own data; third-party agent for customers' data (501.171(6)). Other states handled generically |
| FedRAMP (N51-R07) | **Yes, Government Edition only** | 45 federal civilian agencies use the Government Edition under its FedRAMP Moderate authorization. The commercial OCP is not used as a federal information system and is not claimed as authorized |
| Bank service provider notification | **Yes** | About 140 banking organization customers receive covered services subject to the Bank Service Company Act (12 CFR 53.2(b)(2), (b)(5)) |
| DOJ Data Security Program (N51-R04) | **Screening duty** | Customer data likely exceeds bulk thresholds for some categories (28 CFR 202.205). Note that contact data linked only to other contact data is excluded from covered personal identifiers (202.212(b)(1)). No vendor, employment, or investment agreements give countries of concern or covered persons access today, so 202.1001 compliance program duties do not apply; screening confirms this each year |
| COPPA (N51-R02), CPNI (N51-R06), PADFA (N51-R05), HIPAA | **No** | Not directed to children; not a carrier; not a data broker; no business associate agreements and PHI prohibited by contract (rows G-078 to G-081) |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25; reporting to CISA is voluntary. The company would likely be covered when final (above the SBA size standard, IT sector) |
| SOX Section 404 | Separate program | IT general controls over ERP and billing are tested by the SOX program |

## 2. Method
1. **Decompose.** FTC guidance practices became one row each, cited by guide, lesson, and practice heading (FTC guidance is a U.S. government work, so headings are quoted). Every security, privacy, or AI statement the company makes publicly or by contract became one deception row. Regulations were broken into citation-level duties from primary text: 17 CFR 229.106 (eCFR, 2026-09-23 version); SEC Release 33-11216 for Item 1.05; Cal. Code Regs. tit. 11, 7050, 7051, 7120 to 7124, 7150, 7157, and 7200 (CPPA text of regulations); Fla. Stat. 501.171 and 501.702 (2026 Florida Statutes); 12 CFR Part 53 (eCFR, 2026-09-23); 28 CFR Part 202 (eCFR, 2026-09-23); 44 U.S.C. 3607 to 3616 (U.S. Code); and the FedRAMP Consolidated Rules for 2026 definitions page (fedramp.gov, retrieved 2026-10-04).
2. **Crosswalk.** Each row maps to CSF 2.0, SP 800-53 Rev. 5, and related SOC 2 criterion IDs. This is an **author mapping**: no official NIST, FTC, or AICPA mapping exists for these requirements. SOC 2 criteria are listed by ID only.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls used 25 items; configuration and account data were checked in full with analytics. Selections were random. **31 rows were tested by sampling or full-population analytics; 23 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| FTC Act Section 5: reasonable security (FTC Start with Security guide) (N51-R01) | 12 | 16 | 0 | 0 | 28 |
| FTC Act Section 5: reasonable security (FTC Protecting Personal Information guide) (N51-R01) | 0 | 2 | 0 | 0 | 2 |
| FTC Act Section 5: breach response (FTC Data Breach Response guide) (N51-R01) | 0 | 1 | 0 | 0 | 1 |
| FTC Act Section 5: deception (security, privacy, and AI representations) (N51-R01) | 3 | 5 | 5 | 0 | 13 |
| SEC Form 8-K Item 1.05 (N51-R08) | 2 | 2 | 0 | 0 | 4 |
| SEC Regulation S-K Item 106 (N51-R08) | 5 | 0 | 0 | 0 | 5 |
| CCPA and CPPA regulations (N51-R03) | 3 | 5 | 2 | 0 | 10 |
| State comprehensive privacy laws (processor duties) | 0 | 1 | 0 | 0 | 1 |
| Fla. Stat. 501.171 (Florida worked example) | 2 | 2 | 0 | 0 | 4 |
| State breach notification laws (generic) | 0 | 1 | 0 | 0 | 1 |
| FedRAMP, Government Edition only (N51-R07) | 1 | 2 | 0 | 0 | 3 |
| DOJ Data Security Program (N51-R04) | 1 | 1 | 0 | 1 | 3 |
| Bank service provider notification (12 CFR 53.4; 225.303; 304.24) | 0 | 2 | 0 | 0 | 2 |
| Not applicable at this company | 0 | 0 | 0 | 5 | 5 |
| **Total** | **29** | **40** | **7** | **6** | **82** |

**FTC reasonable security (guidance rows):** 12 Met, 19 Partially met, 0 Not met (31 rows). The program meets the guidance where the FTC looks first (authentication, encryption, endpoint security, vendor contracts). The gaps sit in credentials and secrets, the AQ-01 export path, monitoring of data leaving the platform, and retention.

**Deception rows:** 3 Met, 5 Partially met, 5 Not met (13 rows). **This is the most important finding.** Five statements the company makes today are not true as written: two trust page claims about support access and recording (G-032, G-033), the no-cross-customer-training claim for AQ-01 customers (G-034), and the two deletion commitments (G-037, G-040). The FTC treats broken security and data-use promises as deception regardless of company size.

**Gap risk levels across all regulations:** High 20, Moderate 22, Low 5.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-002 | Start with Security, 1: Hold on to information only as long as you have a ... | The offboarding job failed silently for 23 terminated tenants (see G-037); Data Cloud snapshots kept 13 months (see G-040) | Delete the 23 tenants; alert and reconcile monthly (POAM-011); snapshot lifecycle (POAM-022) | Chief Privacy Officer | 2027-01-31 |
| G-004 | Start with Security, 2: Restrict access to sensitive data | 7 of 60 sampled sessions had no linked customer ticket; customer approval only for about 9% of tenants | Ticket link enforced; customer approval by default for Enterprise tenants (POAM-004) | Vice President, Customer Support | 2027-01-31 |
| G-007 | Start with Security, 3: Store passwords securely | 212 live secrets found in repositories in 2026 H1; long-lived keys in 9 OCP pipelines and 31 AQ-01 pipelines (POAM-002) | Remove long-lived keys; automated revocation | Director of Product Security | 2027-01-31 |
| G-010 | Start with Security, 4: Keep sensitive information secure throughout its ... | The nightly AQ-01 export copies full transcripts for 1,150 customers into a bucket outside the landing zone (POAM-001) | Minimized, tenant-scoped export with an interconnection agreement | Vice President, Integration Management Office | 2026-12-15 |
| G-012 | Start with Security, 4: Ensure proper configuration | AQ-01 is outside the guardrails; its CI build logs were publicly readable (POAM-019) | Apply guardrails to the AQ-01 organization | Vice President, Integration Management Office | 2026-11-15 |
| G-014 | Start with Security, 5: Monitor activity on your network | No bulk-read alert on exports; AQ-01 logs not in the SIEM; cross-tenant anomaly detection on 2 of 5 data stores (POAM-003) | Export and bulk-read detections; AQ-01 log onboarding | Director of Security Operations | 2026-12-15 |
| G-030 | Protecting Personal Information, 5. Plan ahead | Plan lacks the bank service provider and FedRAMP communication steps (POAM-012) | Update the plan; tabletop 2026-11-12 | Director of Security Operations | 2026-11-30 |
| G-031 | Data Breach Response: Notify Appropriate Parties; Fix Vulnerabilities | Customer notice terms (24, 48, 72 hours) are not in a searchable register (see G-035) | Obligations register (POAM-012) | General Counsel | 2026-11-30 |
| G-032 | Trust page: "customer data is never accessed by our staff without customer ... | The statement is not true for about 91% of tenants | Correct the statement now; restore only when customer approval is the default (POAM-021, POAM-004) | General Counsel | 2026-10-30 |
| G-033 | Trust page: "all administrative access is logged and recorded" | The recording claim is not true for the legacy console path | Correct the statement; retire the legacy path (POAM-021, POAM-004) | General Counsel | 2026-10-30 |
| G-034 | Trust page and AI terms: "we never use your data to train AI models for other ... | Statement is untrue for customers who also use the Conversational AI service (POAM-020) | Stop pooled training; retrain or delete affected models; align terms and notify customers | Chief Data and AI Officer | 2026-11-30 |
| G-035 | DPA: notice of a security incident affecting customer data without undue delay ... | 9 of 60 sampled contracts had non-standard notice terms not visible to the incident team | Obligations register extracted from contracts and linked to the runbook (POAM-012) | General Counsel | 2026-11-30 |
| G-037 | DPA: deletion of customer data from production within 30 days after termination | 23 terminated tenants were still present 41 to 212 days after termination | Delete the 23 tenants; failure alerts; monthly reconciliation (POAM-011) | Chief Privacy Officer | 2026-11-30 |
| G-038 | DPA and CCPA service provider terms: customer data used only to provide the ... | AQ-01 pooled training breaks the use limit for shared customers (POAM-020) | As G-034 | Chief Data and AI Officer | 2026-11-30 |
| G-040 | DPA: deletion of customer data from backups within 90 days after termination | Data Cloud keeps terminated tenants' data up to 13 months in snapshots | 90-day snapshot lifecycle or tenant-level deletion (POAM-022) | Vice President, Data Cloud | 2027-01-31 |
| G-045 | Form 8-K Item 1.05: materiality determination | Three new committee members not briefed; playbook does not show how bank, FedRAMP, and customer notices interact with the determination (POAM-012) | Update the playbook; tabletop 2026-11-12 | General Counsel | 2026-11-30 |
| G-047 | Form 8-K Item 1.05: filing deadline | Escalation timing from severity-1 declaration to the committee has not been tested end to end with current members | Tabletop 2026-11-12 (POAM-012) | General Counsel | 2026-11-30 |
| G-055 | Cal. Code Regs. tit. 11, 7050(a)(3): internal use to build or improve services | Pooled training uses one customer's data to serve others (POAM-020) | As G-034 | Chief Data and AI Officer | 2026-11-30 |
| G-065 | Fla. Stat. 501.171(2) | Same gaps as G-007, G-010, G-014 | See those rows | CISO | 2027-01-31 |
| G-067 | Fla. Stat. 501.171(8) | As G-037 and G-040 | POAM-011; POAM-022 | Chief Privacy Officer | 2027-01-31 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Trust page and questionnaire corrections (POAM-021); AQ-01 guardrails (POAM-019); stop AQ-01 pooled training (POAM-020); obligations register, bank contacts, FedRAMP step, and disclosure tabletop 2026-11-12 (POAM-012); delete 23 terminated tenants (POAM-011); minimized AQ-01 export and bulk-read detections (POAM-001, POAM-003); overdue sub-processor reviews and DSP screening (POAM-010); CCPA audit readiness and external auditor (POAM-024); FedRAMP overdue items (POAM-023); AI documentation pack (POAM-018) | FTC Section 5 (deception and unfairness); SEC Item 1.05; 12 CFR 53.4; CCPA 7050, 7122; Fla. Stat. 501.171(8); 28 CFR 202; FedRAMP | Corrected pages; tabletop report; register; deletion certificates; screening records; auditor engagement letter |
| 2027 Q1 | Long-lived keys removed (POAM-002); tenant access tool rebuilt with customer approval by default (POAM-004); Data Cloud snapshot lifecycle (POAM-022); Cell 4 split and retest (POAM-007); secondary DNS; AQ-01 into the landing zone | FTC Section 5; DPA commitments; MSA availability | Key inventory; recording coverage; DR retest report |
| 2027 Q1 to Q4 | **CCPA cybersecurity audit period 2027-01-01 to 2028-01-01**; CPPA risk assessments in the 7150 format (by 2027-06-30); ADMT support for customers (from 2027-01-01) | CCPA 7120 to 7124, 7150, 7200 | Audit evidence; assessments |
| 2028 Q1 | Cybersecurity audit report and executive certification by 2028-04-01; risk assessment submission by 2028-04-01 | CCPA 7121, 7124, 7157 | Audit report; certification |

## 6. Pending regulatory changes and watch items
- **FTC proposed AI-accuracy policy statement** (Docket FTC-2026-0727; comments closed 2026-07-31): **not final** as of 2026-09-25. Flagged on G-034 and G-043; not treated as a current obligation.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.
- **CIRCIA:** final rule not published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect.
- **FedRAMP:** the FedRAMP Authorization Act sections (44 U.S.C. 3607 to 3616) are scheduled for repeal 5 years after 2022-12-23 under Pub. L. 117-263 sec. 5921(d)(1) unless Congress extends them; FedRAMP's Consolidated Rules for 2026 launched 2026-06-24. The Government Edition team tracks both; timing of incident reports is confirmed in the current FedRAMP rules before each update of the runbook.
- **Colorado SB26-189** (developer documentation duties for ADMT, effective 2027-01-01) and the **CPPA ADMT rules** (compliance by 2027-01-01): handled in P10 and G-062.
- **State comprehensive privacy laws:** new laws and threshold changes take effect in 2027 (for example, Delaware's lower thresholds and new laws in Oklahoma and Louisiana, per the cross-sector register). Processor duties are reviewed each January.
- **OMB secure software attestation:** OMB M-26-05 (2026-01-23) rescinded M-22-18 and M-23-16; agencies may still request the CISA attestation form at their discretion, so the Government Edition keeps a current form ready.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to an FTC civil investigative demand, a CPPA or state attorney general inquiry, an agency or FedRAMP request, a banking customer's examiner request, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 readiness, and P10 AI assessment;
- dated captures of the trust page, sub-processor page, AI product pages, and questionnaire library, with the evidence behind each statement;
- contract obligations register (from 2026-11-30);
- records retained at least 7 years (POL-01 4.11).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the cybersecurity and risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.
