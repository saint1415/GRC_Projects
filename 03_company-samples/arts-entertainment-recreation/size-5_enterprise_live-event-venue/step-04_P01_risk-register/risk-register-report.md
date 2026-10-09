# Enterprise Risk Register Report: Cris Santos Company | Arts, Entertainment, and Recreation | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded live entertainment company: 36 venues in 8 states, 3 festivals, in-house ticketing platform for own events and about 340 client venues) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Arts, Entertainment, and Recreation |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | PCI DSS v4.0.1 Requirement 12.3 risk analysis inputs (N71-R04); input to the Reg S-K Item 106 description of risk management processes; reasonable security under FTC Act Section 5 (N71-R05) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that store, process, or transmit card or patron data or support tier-1 processes: the ticketing platform and payment service, 36 venues and 3 festivals, the two cloud estates and two colocation data centers, the six acquired venues (AV-01 to AV-06), the two contact centers, and about 1,450 vendors (230 with patron, card, or employee data). Business processes and impact values come from the enterprise BIA (P05). The Ticketing and Venue Operations Platform is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business and technology (first line) own and treat risks. The GRC team, the Director of Payments and PCI Compliance, and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Attendee safety:** very low appetite for technology-related harm to attendees and staff.
- **Payment card data:** very low appetite for compromise of card data or loss of PCI DSS validation.
- **Regulatory and disclosure:** very low appetite for noncompliance with SEC disclosure rules, the FTC fee rule, ADA ticketing rules, or state breach laws.
- **Ticketing and event continuity:** low appetite for disruption of on-sales, payments, or gate entry.
- **Patron and client data:** low appetite for unauthorized disclosure.
- **Growth and innovation (acquisitions, AI pricing):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Disruption of ticketing, payments, and event operations | Moderate |
| ER-02 Compromise of payment card data | Low |
| ER-03 Compromise of patron and client data | Moderate |
| ER-04 Third-party and concentration risk | Moderate |
| ER-05 Integration of acquired venues | Moderate |
| ER-06 Venue safety and operational technology | Low |
| ER-07 Regulatory, contractual, disclosure, and financial reporting compliance | Low |
| ER-08 Responsible AI and fair access to tickets | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, Chief Operating Officer, CTO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Safety risks (ER-06) and card data risks (ER-02) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the live entertainment threat picture (e-skimming, ticket bots, account takeover, data warehouse credential theft, ransomware) in the SOC's threat intelligence (EV-071), the BIA (P05), the intake evidence, the 2025 risk analysis (EV-025), and risk workshops with the SOC, Platform, Payments and Data Engineering, the Integration Management Office, Venue Security and Safety, Third-Party Risk Management, Ticketing Operations, Pricing and Revenue Management, Finance and Payroll, and the Privacy Office (EV-080). The gap analysis and PCI DSS pre-assessment (P03) ran in the same fieldwork window, and the two shared findings. The Internal Audit assessment (P07) fed the second pass.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: threat intelligence, the SOC case history (EV-021), coverage and configuration exports from the enterprise systems of record, contract and vendor records, the workshops, the P03 samples, and, for risks updated in the second pass, the P07 test results. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

**Two passes.** Pass 1 was completed on 2026-07-31 from the intake evidence and the June and July fieldwork. Pass 2 followed the Internal Audit assessment (P07): R-014 was added on 2026-08-28 after testing found vendor default credentials on turnstile controllers at 2 venues and a building management interface at a third (EV-IA-5), and the risks that P07 tested were updated with the results (their `last_reviewed` date is 2026-08-28; their `likelihood_basis` cites the P07 evidence ID). The `assessment_pass` column shows which pass produced each risk.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 13 |
| Moderate | 37 |
| Low | 14 |
| **Total** | **65** |

By threat source type: Adversarial 31, Structural 26, Accidental 7, Environmental 1.
By treatment: Mitigate 52, Accept 11, Avoid 2.
By status: In progress 52, Open 2, Closed (accepted) 11.
**24 risks are outside tolerance**, and each has a dated treatment plan. All 24 are board-reported.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Disruption of ticketing, payments, and event operations | Operational | 9 | 0 | 1 | 5 | 3 | **High** | Moderate | 1 |
| ER-02 | Compromise of payment card data | Compliance and financial | 7 | 1 | 1 | 3 | 2 | **Very High** | Low | 5 |
| ER-03 | Compromise of patron and client data | Compliance and reputational | 11 | 0 | 2 | 8 | 1 | **High** | Moderate | 2 |
| ER-04 | Third-party and concentration risk | Operational | 6 | 0 | 3 | 2 | 1 | **High** | Moderate | 3 |
| ER-05 | Integration of acquired venues | Strategic | 6 | 0 | 1 | 5 | 0 | **High** | Moderate | 1 |
| ER-06 | Venue safety and operational technology | Safety and operational | 8 | 0 | 3 | 2 | 3 | **High** | Low | 5 |
| ER-07 | Regulatory, contractual, disclosure, and financial reporting compliance | Compliance | 11 | 0 | 2 | 5 | 4 | **High** | Low | 7 |
| ER-08 | Responsible AI and fair access to tickets | Strategic and compliance | 7 | 0 | 0 | 7 | 0 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-02 (card data)** carries the only Very High risk, e-skimming on checkout pages (R-001), because client templates can load scripts the company does not control. Its tolerance is Low, so five constituent risks sit outside it.
- **ER-06 (venue safety and OT)** has three High risks: OT on shared networks (R-013), default credentials found during testing (R-014), and gate entry if offline scanning fails (R-015).
- **ER-07 (compliance)** has the most risks outside tolerance (7), led by the 2026 PCI DSS validation (R-019) and the untested materiality process for service-provider incidents (R-018).
- **ER-08 (AI and fair access)** is within tolerance today, but 5 of 13 AI use cases lack committee review (R-045), and accessible seating parity (R-016) and bot challenge accessibility (R-043) depend on conditions due by 2026-12-31 (P10).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | E-skimming script injected into checkout pages captures card data from own-brand or client checkouts | Very High | ER-02 | Remove client tag containers from the checkout page shell; script allow-list and tamper detection on all client templates; tag vendors into third-party risk (POAM-002; POAM-009) | Chief Technology Officer | 2026-12-15 |
| R-002 | Ransomware encrypts ticketing platform workloads and venue systems across regions | High | ER-01 | Close acquired-venue gaps (POAM-001); EDR on AV terminals; failover automation (POAM-010); ransomware exercise with the disclosure committee (POAM-008) | CISO | 2027-03-31 |
| R-003 | Patron data exported from the data warehouse with a stolen service account credential | High | ER-03 | Key-pair authentication, network policies, and vaulted secrets for all service accounts; export volume alerts (POAM-005) | Director of Data Engineering | 2026-11-30 |
| R-004 | Card data captured from legacy POS at an acquired venue, or lateral movement from its flat network | High | ER-05 | P2PE and SD-WAN segments at AV venues; retire legacy terminals; federate identities (POAM-001; POAM-011) | Vice President, Integration Management Office | 2027-03-31 |
| R-005 | Client user account taken over and used to issue tickets, refunds, or bulk exports | High | ER-03 | Enforce client MFA; disable inactive accounts; atypical-use alerts (POAM-004) | President, Ticketing | 2027-01-31 |
| R-007 | Card numbers in call recordings and case notes are accessed and misused | High | ER-02 | Keypad masking at the overflow center; purge; automated detection (POAM-003) | Director of Payments and PCI Compliance | 2026-12-15 |
| R-008 | A major on-sale fails because the edge and bot management provider is down | High | ER-04 | Test the fallback runbook; second bot detection option for on-sales (POAM-014) | Director of Platform Engineering | 2027-03-31 |
| R-013 | Venue OT compromised through shared network segments | High | ER-06 | Segment OT at 14 venues; integrator access through PAM; complete OT inventory (POAM-006; POAM-019) | Vice President, Venue Security and Safety | 2027-06-30 |
| R-014 | Default credentials on turnstile controllers or building management interfaces | High | ER-06 | Change all default credentials; commissioning checks (POAM-007) | Vice President, Venue Security and Safety | 2026-11-15 |
| R-015 | Gate entry stops and offline mode fails, causing crowding at gates | High | ER-06 | Offline drills at 15 untested venues; carrier redundancy at AV venues (POAM-013) | President, Venue Operations | 2026-12-15 |
| R-018 | Material incident disclosed late or inaccurately (service-provider incidents not covered) | High | ER-07 | Update the playbook; tabletop with the disclosure committee on 2026-11-12 (POAM-008) | General Counsel | 2026-11-30 |
| R-019 | 2026 PCI DSS Reports on Compliance late or not Compliant | High | ER-07 | Close POAM-002 and POAM-003 before QSA fieldwork; compensating controls or a dated action plan for AV venues | Director of Payments and PCI Compliance | 2026-12-31 |
| R-021 | A third party with patron or card data suffers a breach | High | ER-04 | Clear overdue reassessments; renew the outsourced center AOC; continuous monitoring (POAM-009) | Director of Third-Party Risk Management | 2027-03-31 |
| R-023 | Malicious code in a third-party library or SDK | High | ER-04 | SBOM and version pinning for all services; staged SDK rollout | Chief Technology Officer | 2027-06-30 |

## 6. Themes from the 2026 analysis
1. **The payment page is the main target (ER-02).** The payment service itself is well isolated, but the page around the payment fields is not under full control on client templates (R-001, R-022; EV-030, EV-084). Payment page script attacks are the risk that PCI DSS Requirements 6.4.3 and 11.6.1 address.
2. **Identities outside the workforce (ER-03).** Workforce identity is strong, but client users, client API keys, and data warehouse service accounts are not held to the same standard (R-003, R-005, R-024; EV-007, EV-008, EV-034).
3. **Acquisition integration (ER-05).** AV-01 to AV-06 brought non-P2PE POS, flat networks, and a legacy directory into the merchant CDE on day one (R-004, R-031, R-057, R-060; EV-053, EV-029). Going forward, deal approvals must include security due diligence and funding (R-061).
4. **Venue safety depends on OT and offline modes (ER-06).** Gate entry and venue OT are where a cyber event becomes a safety event (R-013 to R-015). Testing found default credentials on OT devices at 3 venues (R-014; EV-IA-5).
5. **Concentration (ER-04).** One edge and bot management provider and one tokenization provider sit under every online sale (R-008, R-011).
6. **AI and fair access (ER-08).** Dynamic pricing and bot detection affect what patrons pay and whether they can buy at all; accessible seating parity and challenge accessibility are the open issues (R-016, R-043, R-045).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $7.2 million:** AV venue P2PE and network migration ($2.1M), OT segmentation at 14 venues ($1.6M), checkout template redesign and client-template script controls ($1.2M), regional failover automation ($0.6M), client MFA enforcement and API credential migration ($0.5M), third-party reassessment surge ($0.4M), keypad masking at the outsourced contact center ($0.3M), AI testing and the accessible bot challenge ($0.3M), data warehouse service account hardening ($0.2M), and outside counsel for the disclosure tabletop ($40K). Items map to the POA&M in P07.
- **Accepted (11):** R-012, R-026, R-033, R-038, R-039, R-048, R-050, R-051, R-052, R-059, R-062. Each is Low residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-041 and R-042. Unapproved generative AI domains are blocked, and the facial recognition express entry pilot (AI-005) is paused pending counsel's state-by-state review.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and a residual target of Moderate on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, PCI DSS validation status (R-019), SOX IT general control status (R-051), and disclosure controls (R-018). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
