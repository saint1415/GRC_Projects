# Enterprise Risk Register Report: Cris Santos Company | Construction | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded commercial and institutional building general contractor; about 300 projects in 8 states) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Construction |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | SP 800-171 R2 3.11.1 periodic risk assessment for the FPCE scope (P03 G-081); input to the Reg S-K Item 106 description of risk management processes (17 CFR 229.106(b)) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that hold FCI, CUI, payment data, or personal information, or that support tier-1 processes across about 140 jobsites, 10 offices, 2 yards, the two cloud estates, the government community cloud enclave, two colocation data centers, the two acquired businesses (AQ-1 and AQ-2), and about 7,500 subcontractors and suppliers plus 1,300 IT and service vendors. Business processes and impact values come from the enterprise BIA (P05). The Project Delivery and Payment Platform (PDPP) is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business and IT (first line) own and treat risks. The GRC team, the CMMC Program Office, and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Payments and cash:** very low appetite for funds diverted by fraud.
- **Federal eligibility:** very low appetite for anything that could cost the company its CMMC status or its standing as a federal contractor, including inaccurate representations to the Government.
- **Safety:** very low appetite for technology-related harm to workers or to clients' building occupants.
- **Disclosure and financial reporting:** very low appetite for noncompliance with SEC disclosure rules or SOX.
- **Project delivery continuity:** low appetite for disruption of field execution and billing.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Payment fraud and funds diversion | Moderate |
| ER-02 Project delivery disruption from cyber and technology events | Moderate |
| ER-03 Federal contract eligibility and CUI protection | Moderate |
| ER-04 Compromise of sensitive data | Moderate |
| ER-05 Third-party and subcontractor risk | Moderate |
| ER-06 Integration of acquired businesses | Moderate |
| ER-07 Client building systems and safety | Low |
| ER-08 Regulatory, disclosure, and financial reporting | Low |
| ER-09 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CFO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Risks to federal eligibility (ER-03) and safety (ER-07) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the construction threat picture (business email compromise and payment fraud, ransomware, supply chain, insider fraud), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3). A single diverted payment above $1 million, or loss of federal award eligibility, is Very High.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **9 enterprise risks (ER-01 to ER-09)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 13 |
| Moderate | 39 |
| Low | 12 |
| **Total** | **65** |

By threat source type: Adversarial 27, Structural 25, Accidental 11, Environmental 2.
By treatment: Mitigate 52, Accept 11, Avoid 2.
By status: In progress 52, Closed (accepted) 11, Open 2.
**18 risks are outside tolerance** and each has a dated treatment plan. All 18 are board reported.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Payment fraud and funds diversion | Financial | 9 | 0 | 4 | 5 | 0 | **High** | Moderate | 4 |
| ER-02 | Project delivery disruption from cyber and technology events | Operational | 12 | 1 | 0 | 7 | 4 | **Very High** | Moderate | 1 |
| ER-03 | Federal contract eligibility and CUI protection | Compliance | 10 | 0 | 4 | 5 | 1 | **High** | Moderate | 4 |
| ER-04 | Compromise of sensitive data | Compliance and reputational | 7 | 0 | 1 | 5 | 1 | **High** | Moderate | 1 |
| ER-05 | Third-party and subcontractor risk | Operational | 7 | 0 | 0 | 5 | 2 | **Moderate** | Moderate | 0 |
| ER-06 | Integration of acquired businesses | Strategic | 4 | 0 | 1 | 3 | 0 | **High** | Moderate | 1 |
| ER-07 | Client building systems and safety | Operational and safety | 5 | 0 | 1 | 2 | 2 | **High** | Low | 3 |
| ER-08 | Regulatory, disclosure, and financial reporting | Compliance | 5 | 0 | 1 | 2 | 2 | **High** | Low | 3 |
| ER-09 | Responsible use of AI | Strategic | 6 | 0 | 1 | 5 | 0 | **High** | Moderate | 1 |

**Reading the profile:**
- **ER-01 (payment fraud)** has the most High risks. The 2026-04 loss at AQ-1 (R-003) and the adversary-in-the-middle phishing path that bypasses push MFA (R-002) are the drivers.
- **ER-02 (project delivery)** carries the only Very High risk, enterprise ransomware during the pay app window (R-009). The AQ-1 network (R-042, ER-06) is the main reason its likelihood is not lower.
- **ER-03 (federal eligibility)** is outside tolerance because CUI was found on the commercial project management platform (R-018) and because the enclave drifted before its C3PAO assessment (R-019, R-020). Several drifted requirements cannot be placed on a CMMC POA&M (32 CFR 170.21(a)(2)), so they must be fixed, not planned.
- **ER-07 (client building systems)** has the lowest tolerance because BTS controls access and cameras in about 420 client buildings (R-046).
- **ER-08 (disclosure)** is outside tolerance because the materiality playbook has no payment fraud scenario and no rule for related occurrences (R-051). 17 CFR 229.106(a) defines a cybersecurity incident to include "a series of related unauthorized occurrences", so repeated small frauds must be considered together.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-009 | Ransomware encrypts the ERP, integration platform, and file systems during the pay app window | Very High | ER-02 | Close AQ-1 gaps (POAM-016; POAM-004); SYS-01 export restore (POAM-008); ransomware tabletop with the disclosure committee (POAM-009) | CISO | 2027-01-31 |
| R-001 | BEC redirects an owner progress payment | High | ER-01 | Phishing-resistant MFA for project managers (POAM-017); payment fraud training (POAM-011); materiality scenario (POAM-009); owner remittance letters | Vice President, Treasury | 2027-03-31 |
| R-002 | Adversary-in-the-middle phishing bypasses push MFA | High | ER-01 | FIDO2 or device-bound passkeys for project management staff (POAM-017) | Director of Identity and Access Management | 2027-03-31 |
| R-003 | Fraudulent subcontractor bank change processed | High | ER-01 | All AQ-1 payee changes through Payment Operations; structured call-back records (POAM-003) | Director of Payment Operations | 2026-11-30 |
| R-006 | Payment files altered between the ERP and a bank | High | ER-01 | Signed files or hash verification for bank 3 (POAM-006) | Vice President, Treasury | 2027-01-31 |
| R-018 | CUI uploaded to the commercial project management platform | High | ER-03 | Purge and attest; CUI marking detection; designers routed to the FPCE gateway (POAM-019) | Director, CMMC Program Office | 2026-10-31 |
| R-019 | FPCE fails the C3PAO assessment | High | ER-03 | Remediate 8 drifted requirements; update the FPCE SSP; mock assessment (POAM-020) | President, Federal Group | 2026-12-15 |
| R-020 | Affirmation or SPRS entry overstates compliance | High | ER-03 | Remediate and post an updated self-assessment before relying on the status (POAM-020; POAM-024) | General Counsel | 2026-12-31 |
| R-022 | Subcontractor without required CMMC status receives CUI or FCI | High | ER-03 | SPRS and CMMC status check before award (POAM-021) | Vice President, Procurement and Subcontracts | 2026-12-31 |
| R-030 | Client facility security details leak from BTS | High | ER-04 | Credential rotation; quarterly vault review | Vice President, Building Technology Services | 2027-01-31 |
| R-042 | Lateral movement from AQ-1 into enterprise systems | High | ER-06 | Restrict VPN; SD-WAN migration; identity federation (POAM-016; POAM-014) | Vice President, Integration Management Office | 2026-12-15 |
| R-046 | BTS remote access abused to disable client access control or cameras | High | ER-07 | Retire vendor-specific remote tools; just-in-time access per client | Vice President, Building Technology Services | 2027-03-31 |
| R-051 | Materiality process misses payment fraud or related occurrences | High | ER-08 | Payment fraud scenario and related-occurrence rule; tabletop 2026-11-19 (POAM-009) | General Counsel | 2026-12-15 |
| R-056 | AI bid assistant feeds pooled competitor pricing into federal bids | High | ER-09 | Contract terms bar pooling; quarterly configuration check (P10) | Vice President, Preconstruction | 2026-12-31 |

## 6. Themes from the 2026 analysis
1. **Payment fraud (ER-01).** The company moves about $700 million a month through owner receipts and subcontractor payments. The 2026-04 AQ-1 loss ($612,000 paid, $157,000 net after recall) came from a path the enterprise controls did not cover: AQ-1 payees changed in the AQ-1 ERP and sent through the enterprise payment hub (R-003). Treatment: one payee verification process for the whole company by 2026-11-30.
2. **CUI outside the enclave (ER-03).** Design firms and subcontractors uploaded CUI-marked drawings to the commercial project management platform on 2 DoD projects (R-018). The platform is not FedRAMP authorized, so this is a DFARS 252.204-7012(b)(2)(ii)(D) and 252.204-7021(d)(2) issue, not just a policy breach (P03).
3. **CMMC drift (ER-03).** The FPCE achieved Final Level 2 (Self) on 2026-02-27, but the July readiness check found 8 requirements no longer fully met, mostly in the jobsite plan rooms that the SSP never described (R-019, R-021). With the voluntary C3PAO assessment on 2027-01-25 and the annual affirmation due 2027-02-27, the window is short, even though CMMC Phase 2 is suspended.
4. **Acquisitions (ER-06).** AQ-1 is still on its own ERP, email, directory, and VPN (R-042 to R-044). AQ-2 holds FCI under its own Level 1 status (R-025).
5. **Disclosure (ER-08).** The disclosure committee reviewed EV-2026-04 and recorded it as not material, but without a written rule for related occurrences (R-051).
6. **AI (ER-09).** The AI bid assistant's pooled pricing feature (R-056) and takeoff errors (R-057) are the main AI risks; computer vision for discipline was avoided (R-059).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $5.4 million:** AQ-1 ERP and email migration brought forward ($2.1M), phishing-resistant authenticators for about 3,300 users ($640K), SD-WAN migration of AQ-1 sites ($520K), plan room hardening at 16 installation jobsites ($410K), CUI marking detection and SaaS log streaming ($380K), bank 3 file signing and payment hub changes ($260K), C3PAO assessment and mock assessment ($310K), subcontractor CMMC verification service ($240K), tablet enrollment ($180K), payment fraud training content ($90K), and outside counsel for the disclosure tabletop ($45K). Items map to the POA&M in P07.
- **Accepted (11):** R-011, R-012, R-014, R-016, R-026, R-038, R-041, R-048, R-049, R-055, R-063. Each is Low or Moderate residual and within tolerance, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-033 and R-059. Unapproved generative AI domains are blocked, and jobsite computer vision may not be used for discipline.
- **Very High risk R-009:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-08; the board risk committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), the regulatory roadmap (P03), and a CMMC readiness briefing from the President, Federal Group.
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-052), payment fraud events and recoveries, and the disclosure controls topics (R-051, R-054). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-009, 2026-09-08.
- Risk committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
