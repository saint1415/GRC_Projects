# Risk Register Report: Cris Santos Company | Arts, Entertainment, and Recreation | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (live event venue operator with ticketing; private equity-backed; three Florida venues) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Arts, Entertainment, and Recreation |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2; Appendix I semi-quantitative values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also supports | PCI DSS v4.0.1 Requirement 12.3.1 (targeted risk analysis inputs) and FTC Act Section 5 reasonable security (N71-R04, N71-R05); Fla. Stat. 501.171(2) reasonable measures |
| Prepared | 2026-07-31 by the GRC Analyst and the Security Manager with the vCISO; R-029 added 2026-08-14 from P07 testing |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High, and the risk appetite); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (the three venues, ticketing and the call center, food and beverage, premium seating and group sales, marketing and digital, booking, finance, HR, and the County PAC services that start in 2027), the Ticketing and Venue Operations Platform (TVOP, P02), both merchant accounts (MID-T and MID-F), and the vendors and agencies that hold patron or card data, as listed in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv). Processes and impact values come from the BIA (P05); vulnerabilities come from the intake evidence, the gap analysis (P03) and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-15.

| Area | Appetite | Statement and measure |
|---|---|---|
| Attendee safety | **Very low** | No technology risk that could contribute to crowd harm is accepted above Low. Any such risk rated Moderate or higher must have a funded treatment plan within 90 days. Measure: safety-linked risks above Low (6 today: R-018, R-020, R-028, R-029, R-030, R-050; target 0 by 2027-06-30) |
| Card data | **Low** | No risk of a card data compromise is accepted above Moderate, and the company will not hold card data it does not need. Measure: R-001, R-002, R-004, and R-005 at Low or Moderate before the 2026 ROC fieldwork (2026-11-02) |
| Patron data | **Low** | No risk of a breach affecting more than 10,000 patrons is accepted above Moderate. Measure: R-002, R-003, and R-010 at Moderate or lower by 2026-12-31 |
| Pricing and consumer protection | **Very low** | Every advertised ticket price shows the total price, and pricing tools never set accessible seating above parity. Measure: zero fee-display or parity exceptions in the monthly marketing and pricing checks |
| Availability of event-day operations | **Low** | Every venue can admit attendees and sell food and beverage through a written, drilled fallback within the BIA MTDs (P05). Measure: a passed drill at each venue in the last 12 months |
| Third parties and agencies | **Moderate**, with conditions | Vendors and agencies are used widely, but none touches the payment page, card data, or patron data without a contract with security terms and a current AOC or SOC 2 report where applicable (P09) |
| Innovation and AI | **Moderate** | The company wants the benefits of AI in pricing, bot defense, guest service, and safety, but only through the P10 governance process |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $250,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, the intake evidence, risk interviews with the process owners, the three venue General Managers, the IT Director, the Security Manager and the MSSP service lead (EV-064), observation of a high-demand on-sale (2026-07-15, EV-065) and an Amphitheater show night (2026-07-18, EV-066), the gap analysis (P03), and the control assessment (P07). The gap analysis ran in the same fieldwork window, and the two shared findings. The control assessment added one risk in a second pass.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood that the event causes adverse impact were each rated, then combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the incident queue (EV-033), scan results (EV-020, EV-021), phishing results (EV-036), configuration exports, the walk-throughs, the gap analysis samples and the interviews. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, contractual and regulatory, attendee safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 9 |
| Moderate | 32 |
| Low | 10 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 44 Mitigate, 3 Avoid (R-004, R-005, R-031), 3 Accept (R-023, R-040, R-046), 2 Share/Transfer (R-021, R-052). Status: 30 Open, 19 In progress, 3 Accepted.

Cyber insurance ($10 million limit, $250,000 retention, $1 million sublimit for card brand assessments) transfers part of the financial exposure for R-001, R-002, R-008, and R-009. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to patrons or operations.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Skimming script on website event pages that embed the checkout form | Very High | Script inventory and authorization; tag manager on SSO with two-person publishing; payment page tamper detection | Vice President of Marketing and Digital | 2026-10-30 |
| R-002 | Takeover of a local ticketing account, then patron export and setting changes | High | Local accounts to SSO or app-based MFA; admins cut to 6; alerts on exports and setting changes | Vice President of Ticketing | 2026-10-31 |
| R-006 | 2026 ROC finds requirements Not in Place; Non-Compliant AOC | High | Scope document; virtual terminal scope reduction; close High P03 rows before fieldwork | Chief Financial Officer | 2026-12-15 |
| R-007 | Phishing with session theft takes over an employee identity | High | Security keys for administrators; token theft detections | Security Manager | 2027-03-31 |
| R-008 | Business email compromise redirects an artist or County PAC payment | High | Callback verification; dual approval over $50,000 | Controller | 2026-10-31 |
| R-009 | Ransomware on corporate, venue office, and cloud workloads | High | Segmentation; privileged access management; restore tests | IT Director | 2027-03-31 |
| R-014 | Advertised ticket prices omit mandatory fees (16 CFR 464.2) | High | Total price in every listing and email; pre-publication check | Vice President of Marketing and Digital | 2026-09-30 |
| R-018 | Ticketing or scanning lost during doors at the Music Hall or the Club with no manual procedure | High | Write and drill the manual entry procedure at both venues | Vice President of Venue Operations | 2026-11-30 |
| R-029 | Default administrator credentials on the Music Hall crowd analytics server (found in P07) | High | Password changed 2026-08-14; check all integrator devices | Vice President of Venue Operations | 2026-10-31 |
| R-034 | Attacks on the ticketing tenant, website, or virtual terminal go undetected (logs not collected) | High | Ticketing, tag manager, CMS, and partner portal logs to the SIEM with alerts | Security Manager | 2026-12-31 |

**Themes.**
- **The company's own edge of the vendor platform is the weak point (R-001 to R-005, R-034).** The ticketing vendor's PCI DSS and SOC 2 controls do not stop a skimming script on the company's own pages, a phished agency account, an over-privileged API key, or card numbers typed into CRM notes. R-001 and R-002 together are the first P08 scenario.
- **Scale outgrew the 2025 validation (R-004, R-006, R-037).** The Amphitheater moved the company to Visa Level 2 and a ROC, and the virtual terminal channel and website pages were never in scope before.
- **Event-day resilience is uneven (R-018 to R-020, R-050).** The Amphitheater has a drilled manual entry procedure; the Music Hall and the Club do not. This is the second P08 scenario.
- **Consumer protection rules reach the pricing stack (R-014 to R-017).** Fee display, accessible seating parity, and posted limits are pricing and marketing risks with security-style controls (change control, monitoring). P10 covers them.
- **New finding from testing (R-029).** The control assessment found the integrator's default administrator password on the crowd analytics server installed in April 2026. The password was changed on 2026-08-14 and the risk was added the same day.

**Two passes.** Pass 1 was completed on 2026-07-31 from intake and fieldwork evidence. Pass 2 followed the control assessment (P07): R-029 was added on 2026-08-14 after testing found the integrator's default administrator password on the Music Hall crowd analytics server, reachable from the corporate segment (EV-IA-5, EV-SC-7). The `assessment_pass` column shows which pass produced each risk.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15, $584,000 one-time and $255,000 a year, fictional):**
- Validated P2PE devices for the 26 virtual terminal users ($14,000) and QSA support for the scope document ($25,000)
- Payment page script monitoring and change detection service ($45,000 a year)
- SIEM onboarding of ticketing, tag manager, CMS, and payment partner logs ($60,000 a year through the MSSP)
- Privileged access management extension and security keys for administrators ($120,000 one-time, $40,000 a year)
- Segmentation of physical security and production segments at the three venues ($140,000)
- Internal and segmentation penetration testing ($45,000 a year)
- Second ISP at the Club and battery coverage for Amphitheater network closets ($60,000 one-time, $18,000 a year)
- SOC 2 readiness, Type 1, and Type 2 examination for the County PAC agreement ($190,000 across 2027)
- Card data discovery and email data loss prevention ($35,000 one-time, $22,000 a year)
- Vendor risk program tooling ($25,000 a year)

Smaller items (key logs for network closets, exercise facilitation, contract amendments) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**No-cost actions due by 2026-09-30:** purge card data from the CRM and mailboxes (R-005), total-price displays (R-014), accessible seating parity (R-015), and disabling the 2 departed agency accounts (R-002).

**Accepted (3):** R-023 (Low; backups already isolated and write-once), R-040 (Low; vendor and edge protections), R-046 (Low; until the corporate segment leaves the CDE).

**Avoided (3):** R-004 (no card number reaches a laptop after the P2PE change), R-005 (card data purged and blocked), R-031 (face matching stays off).

**Shared or transferred (2):** R-021 through the ticketing vendor contract (recovery terms and service credits at the 2027 renewal) and R-052 through the vendor's fraud screening.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity, payments, and event technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Ticketing and Venue Operations Platform (TVOP; SSP in P02) | Security Manager | 40 risks whose affected assets include SYS-01, SYS-02, SYS-04, SYS-05, SYS-06, SYS-08, SYS-09, or SYS-16 (filter the `affected_asset_or_process` column) |
| PCI DSS cardholder data environment (feeds the 12.3.1 targeted risk analyses and the ROC) | Chief Financial Officer with the Security Manager | R-001, R-002, R-004, R-005, R-006, R-034, R-037, R-041, R-042, R-052 |
| Event-day operations (all three venues) | Vice President of Venue Operations | R-018, R-019, R-020, R-021, R-028, R-029, R-030, R-050 |
| AI portfolio (P10) | Vice President of Ticketing with the vCISO | R-015, R-016, R-017, R-030, R-031, R-032, R-033 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and acceptances, 2026-09-15.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-15.
- Board audit committee: received the results on 2026-09-15. Next report: December 2026 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example the County PAC onboarding or the end of the virtual terminal channel) or a significant incident.
