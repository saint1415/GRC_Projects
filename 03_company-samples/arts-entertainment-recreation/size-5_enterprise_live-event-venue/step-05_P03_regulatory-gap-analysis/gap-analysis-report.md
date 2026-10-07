# Regulatory Gap Analysis: Cris Santos Company | Arts, Entertainment, and Recreation | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded live entertainment company; 36 venues in 8 states; in-house ticketing platform for own events and about 340 client venues) |
| Tier / Vertical | Enterprise / Arts, Entertainment, and Recreation |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, June 2024), as a **Level 1 merchant** and a **Level 1 service provider**. A contractual standard enforced through the acquirer and card brands, **not law** (N71-R04) |
| Other rules analyzed | SEC Form 8-K Item 1.05 and Reg S-K Item 106; FTC Act Section 5 and the FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (N71-R05); ADA Title III ticketing rules, 28 CFR 36.302(f); BOTS Act, 15 U.S.C. 45c; state breach notification and consumer privacy laws (Florida worked example); applicability checks for the gaming rules (N71-R01 to R03) and COPPA (N71-R06) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team and the Director of Payments and PCI Compliance (second line) with the Chief Compliance Officer; sampling reperformed by Internal Audit for 8 rows. This is a pre-assessment; the QSA's Reports on Compliance are separate (fieldwork 2026-10-19 to 2026-11-25) |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |

## 1. Applicability
### 1.1 PCI DSS: two roles, two validations
PCI SSC sets no size tiers; validation levels come from the card brands and the acquirer. Visa's Account Information Security program page (checked 2026-10-06) and *What To Do If Compromised* v10.0 (effective 2026-06-25) define the levels used here.

| Role | Basis | Visa level | 2026 validation |
|---|---|---|---|
| **Merchant** (own events, venue box offices, stands) | About 25 million Visa transactions a year across all channels | **Level 1** (more than 6 million Visa transactions a year) | Annual Report on Compliance (ROC) by a QSA, or an internal resource if signed by an officer, plus an attestation of compliance (AOC). The company uses a QSA. Passing quarterly ASV scans (Requirement 11.3.2) |
| **Service provider** (payment service and checkout for about 340 client venues) | Transmits about 7.8 million Visa transactions a year for clients | **Level 1** (more than 300,000 Visa transactions a year) | Annual on-site assessment and an AOC signed by the company and the QSA, submitted to Visa. Visa requires QSA validation before a service provider can be listed on its Global Registry of Service Providers, where client venues check the company's status. Service provider-only requirements apply (for example 11.4.6, 12.4.2, 12.5.2.1, 12.9) |

Other brands' level definitions were not verified; the acquirer applies them. The 2025 merchant and service provider ROCs were both Compliant. The 2026 ROCs and AOCs are due 2026-12-31 (fictional acquirer date).

**Scope reduction already in place.** Tokenization means the platform stores no card numbers by design, and validated P2PE devices reduce 30 venues' box offices and stands to the P2PE device controls. **Scope this analysis added:** the AV-01 to AV-06 venues (in full scope since 2026-02-02) and the contact center platform and outsourced overflow center, where card data was found (G-010, G-011, G-062).

**Requirements checked.** All 12 principal requirements were taken to the requirement-group level, the payment page requirements to the defined-requirement level (6.4.1, 6.4.2, 6.4.3, 11.6.1), and the service provider-only requirements that carry the most risk (11.4.6, 12.4.2, 12.5.2.1) as separate rows. All requirements that were future-dated in v4.0 have been effective since 2025-03-31, and 6.4.1 was superseded by 6.4.2 on that date. Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted. No newer PCI DSS version was found on the PCI SSC standards page on 2026-09-26.

### 1.2 Other rules
| Rule | Applies? | Basis |
|---|---|---|
| SEC Form 8-K Item 1.05 and Reg S-K Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| FTC Act Section 5, 15 U.S.C. 45(a), (n) (N71-R05) | **Yes** | For-profit corporation; no size threshold |
| FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (N71-R05) | **Yes** | "Covered good or service" includes live-event tickets (464.1); effective 2025-05-12 (90 FR 2066, rule text at 2166). Applies to every display the company makes, including client templates it renders |
| ADA Title III ticketing, 28 CFR 36.302(f) | **Yes** | Concert halls, stadiums, and other places of exhibition or entertainment are places of public accommodation (28 CFR 36.104); the rules reach pricing, sale stages, and purchase limits that AI-001 and AI-002 enforce |
| BOTS Act, 15 U.S.C. 45c | **No compliance duty** | The company is a ticket issuer the Act protects; its bot defense records are evidence for FTC or state attorney general cases |
| State breach notification laws | **Yes** | Patrons in all 50 states. The company is a covered entity for its own patrons and a third-party agent for client venues (Florida worked example: Fla. Stat. 501.171(6)) |
| State comprehensive consumer privacy laws | **Yes, where thresholds are met** | 19 laws in effect as of 2026-09-25 (cross-sector file); counsel keeps the state list. Florida's Digital Bill of Rights does not apply: the company exceeds $1 billion in revenue but meets none of the three additional tests (G-098) |
| Gaming rules (N71-R01 to R03) | **No** | No gaming license, wagering, or casino operations |
| COPPA (N71-R06) | **No** | General-audience sites and app; accounts require age 18 or older |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25; reporting is voluntary. Under the proposed rule, an entity in a critical infrastructure sector above its SBA size standard would be covered; the company is above the standard and in the Commercial Facilities Sector, so it is tracked as a watch item |
| SOX Section 404 | Separate program | IT general controls over ERP and payroll are tested by the SOX program and not repeated here |

## 2. Method
1. **Decompose.** PCI DSS as described in section 1.1. Other rules were broken into citation-level duties from the primary text: 16 CFR Part 464 and 28 CFR 36.302 (eCFR, versions of 2026-09-23), 17 CFR 229.106 (eCFR), 15 U.S.C. 45c (govinfo), the SEC's Item 1.05 compliance guide and Release 33-11216, and Fla. Stat. 501.171 (Florida Legislature site).
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. **All mappings are author mappings**; no official NIST mapping exists from PCI DSS v4.0.1, the FTC rules, or the ADA rules to CSF 2.0 or SP 800-53.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls and populations under 250 used 25 to 40 items; configuration and account data were checked in full with analytics; recurring reviews used 5 weekly or 2 quarterly occurrences. Selections were random. **38 rows were tested by sampling or full-population analytics; 22 found exceptions.**
4. **Browser and data evidence.** Browser captures of 212 client checkout templates (2026-07-20 to 2026-07-24), a card-number discovery scan of the contact center platform and case notes (2026-07-08), and a listening sample of 60 overflow center recordings.
5. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. Very High and High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 2 | 3 | 0 | 0 | 5 |
| PCI Req 2 Secure configurations | 2 | 1 | 0 | 0 | 3 |
| PCI Req 3 Stored account data | 2 | 2 | 1 | 2 | 7 |
| PCI Req 4 Transmission | 2 | 0 | 0 | 0 | 2 |
| PCI Req 5 Malware and phishing | 3 | 1 | 0 | 0 | 4 |
| PCI Req 6 Secure systems and software | 3 | 3 | 0 | 1 | 7 |
| PCI Req 7 Restrict access | 2 | 1 | 0 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 5 | 1 | 0 | 0 | 6 |
| PCI Req 9 Physical access and card readers | 3 | 2 | 0 | 0 | 5 |
| PCI Req 10 Logging | 6 | 1 | 0 | 0 | 7 |
| PCI Req 11 Security testing (incl. 11.4.6, 11.6.1) | 6 | 1 | 0 | 0 | 7 |
| PCI Req 12 Policies and programs (incl. 12.4.2, 12.5.2.1) | 5 | 6 | 1 | 0 | 12 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **41** | **22** | **2** | **6** | **71** |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| FTC Act Section 5 | 1 | 3 | 0 | 0 | 4 |
| FTC Rule on Unfair or Deceptive Fees | 1 | 3 | 0 | 0 | 4 |
| ADA Title III ticketing (28 CFR 36.302(f)) | 3 | 2 | 0 | 0 | 5 |
| BOTS Act (applicability) | 0 | 0 | 0 | 1 | 1 |
| State breach notification laws | 0 | 3 | 0 | 0 | 3 |
| State consumer privacy laws | 0 | 1 | 0 | 1 | 2 |
| Gaming rules and COPPA (applicability) | 0 | 0 | 0 | 4 | 4 |
| **Total** | **52** | **36** | **2** | **12** | **102** |

**PCI DSS:** 41 Met, 22 Partially met, 2 Not met, 6 Not applicable (71 rows). The two Not met rows are security codes retained in overflow center recordings (3.3, G-011) and the missed 6-month service provider scope confirmation (12.5.2.1, G-063). Most partial rows trace to four root causes: the acquired venues, client checkout templates, card data in the contact center, and third-party assurance.

**Gap risk levels across all rules (38 gaps):** Very High 2, High 13, Moderate 22, Low 1.

## 4. Priority gaps (Very High and High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-027 | PCI DSS 6.4.3 | Script authorization and integrity controls do not cover client templates (14 unauthorized scripts on 37 templates) | Remove client tag containers from the checkout page shell; allow-list and integrity hashes on all templates (POAM-002) | Chief Technology Officer | 2026-12-15 |
| G-056 | PCI DSS 11.6.1 | No change or tamper detection on client checkout templates | Extend detection to all templates with SOC alerting (POAM-002) | Chief Technology Officer | 2026-12-15 |
| G-003 | PCI DSS 1.3 | AV-01 to AV-06 POS terminals not segmented | P2PE devices and SD-WAN segments; interim access lists (POAM-001) | Vice President, Integration Management Office | 2027-03-31 |
| G-010 | PCI DSS 3.2 | About 41,000 card numbers in case notes; card numbers in overflow recordings | Purge; masking in notes; quarterly discovery of the contact center platform (POAM-003) | Director of Payments and PCI Compliance | 2026-12-15 |
| G-011 | PCI DSS 3.3 | Security codes retained in 22 of 60 sampled recordings | Keypad masking or pause-and-resume; purge (POAM-003) | Director of Payments and PCI Compliance | 2026-12-15 |
| G-013 | PCI DSS 3.5 | Card numbers in notes and recordings not rendered unreadable | Purge and masking (POAM-003) | Director of Payments and PCI Compliance | 2026-12-15 |
| G-041 | PCI DSS 9.4 | Electronic media with card data not destroyed | Purge (POAM-003) | Director of Payments and PCI Compliance | 2026-12-15 |
| G-062 | PCI DSS 12.5 | Scope missed the contact center platform | Add to scope or remove the data (POAM-003) | Director of Payments and PCI Compliance | 2026-12-15 |
| G-066 | PCI DSS 12.8 | Overflow center AOC expired; tag vendors not managed as service providers | Renew the AOC or move seats in-house; add tag vendors (POAM-009) | Director of Third-Party Risk Management | 2027-03-31 |
| G-068 | PCI DSS 12.10 | PAN-in-unexpected-location procedure not triggered; no client notification path | Runbook update (P08); 12.10.7 training; tabletop (POAM-008) | Director of Security Operations | 2026-11-30 |
| G-073 | Form 8-K Item 1.05 (materiality determination) | Escalation and materiality factors for service-provider and card breach incidents untested | Update the playbook; tabletop on 2026-11-12 (POAM-008) | General Counsel | 2026-11-30 |
| G-080 | 15 U.S.C. 45(n) | Client MFA optional; warehouse service accounts with passwords; long-lived API keys | POAM-004; POAM-005 | CISO | 2027-01-31 |
| G-084 | 16 CFR 464.2(a) | Base-price displays on 41 client templates and in 9 of 30 sampled emails | Lock total-price display; email template change (POAM-021) | Chief Marketing Officer | 2026-11-30 |
| G-090 | 28 CFR 36.302(f)(3) | 2 accessible seating parity breaches in 40 sampled events | Remove accessible levels from automation; automated parity check; refunds (POAM-020) | Vice President, Pricing and Revenue Management | 2026-11-30 |
| G-095 | Fla. Stat. 501.171(2) | Same gaps as G-080 (reasonable measures) | POAM-004; POAM-005 | CISO | 2027-01-31 |

**Before the QSA fieldwork closes (2026-11-25):** close G-027, G-056, G-010, G-011, G-013, G-041, and G-062 (all within POAM-002 and POAM-003), and confirm service provider scope (G-063). AV-01 to AV-06 cannot be migrated by then; the QSA will assess their interim controls, and any requirement not in place will need a compensating control worksheet or a dated action plan in the AOC.

## 5. Compliance roadmap
| Quarter | Milestones | Rules served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Service provider scope confirmation (G-063); client template redesign and tamper detection (POAM-002); keypad masking and purge (POAM-003); total-price lock on templates and emails (POAM-021); accessible seating parity automation (POAM-020); materiality playbook and tabletop on 2026-11-12 (POAM-008); data warehouse service accounts (POAM-005); AV reader inventory and inspections (G-042) | PCI DSS 3.2, 3.3, 3.5, 6.4.3, 9.4, 9.5, 11.6.1, 12.5, 12.5.2.1, 12.10; Item 1.05; 16 CFR 464.2; 28 CFR 36.302(f)(3); 15 U.S.C. 45(n) | Browser captures; discovery scans; destruction certificates; tabletop report; parity reports |
| 2027 Q1 | AV-01 to AV-06 on P2PE and SD-WAN (POAM-001); client MFA and API credentials (POAM-004); third-party reassessments and tag vendors (POAM-009); opt-out signals on client templates (POAM-025); retention purge (POAM-022); 2026 responsibility matrix for clients (G-067) | PCI DSS 1.2, 1.3, 1.5, 2.2, 5.2, 8.2, 12.8, 12.9; state privacy and breach laws; 15 U.S.C. 45(n) | Segmentation test; MFA reports; AOC register; purge logs |
| 2027 Q2 | OT segmentation at 14 venues (POAM-006, a P01 safety item); second-region restore tests; SBOM for all services | FTC Section 5 reasonable security; CISA Commercial Facilities guidance (voluntary) | Network test reports |
| 2027 Q3 | Annual risk analysis and gap reassessment; 6-month service provider scope confirmation | All | Updated P01 and P03 |

## 6. Pending changes and watch items
- **PCI DSS.** v4.0.1 is the version in effect. The analysis will be updated when PCI SSC publishes a new version.
- **CIRCIA.** The final rule had not been published as of 2026-09-25; reporting to CISA is voluntary until it takes effect.
- **SEC.** A 2025 petition asks the SEC to rescind Item 1.05 (File No. 4-856). No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.
- **TICKET Act (H.R. 1402, 119th Congress).** Not law; it would add statutory all-in pricing and speculative-ticket rules. Not treated as a current obligation.
- **State privacy and AI laws** change often. Counsel refreshes the state list quarterly; P10 tracks state AI laws for the AI portfolio.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to the QSA, the acquirer, a card brand, the FTC, a state attorney general, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the PCI DSS scope document, responsibility matrices, targeted risk analyses, and the 2025 ROCs and AOCs;
- the P01 risk register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- browser captures of checkout templates, discovery scan results, and destruction certificates;
- fee display reviews and accessible seating parity reports (from P10);
- retention of assessment evidence for at least 3 years under the company's retention schedule, and of SEC disclosure records as counsel directs.

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, with service provider scope confirmations every 6 months.
