# Enterprise Risk Register Report: Cris Santos Company | Management of Companies and Enterprises | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company: Building Products, Home Services, Manufacturing, Finance, and Global Business Services; six states) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Management of Companies and Enterprises |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | Finance's written risk assessment inputs (16 CFR 314.4(b)); the basis for the Reg S-K Item 106(b) description of risk management processes; risk input to the SOX scoping of IT general controls |
| Prepared | 2026-05-04 to 2026-07-17 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-14; reviewed by the joint audit and risk committee session of the board, 2026-09-17 |

## 1. Scope and risk framing
**Scope.** The holding company, GBS, and all four subsidiaries: the Shared Corporate Services Platform (SCSP, P02), subsidiary systems, plant OT at 3 plants, the two clouds and two data centers (P04), the acquired businesses AQ-01 and AQ-02, and about 2,300 vendors (420 with access to sensitive data or systems). Business processes and impact values come from the group BIA (P05).

**Three lines.** Risk owners in GBS and the subsidiaries (first line) own and treat risks; each subsidiary's business information security officer (BISO) coordinates for its President. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line), with its co-source firm, tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Financial reporting and disclosure:** very low appetite for misstatement, late or inaccurate SEC disclosure, or an ICFR deficiency caused by technology.
- **Money movement:** very low appetite for fraudulent payments.
- **Plant safety:** very low appetite for technology events that could injure workers.
- **Personal and customer information:** low appetite for unauthorized disclosure, with the lowest appetite for Finance customer information.
- **Continuity of shared services:** low appetite for disruption that stops more than one subsidiary.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Disruption of shared services and subsidiary operations | Moderate |
| ER-02 Financial reporting integrity and SEC disclosure | Low |
| ER-03 Payment fraud and treasury loss | Low |
| ER-04 Compromise of personal and customer information | Moderate |
| ER-05 Third-party and concentration risk | Moderate |
| ER-06 Integration of acquired businesses | Moderate |
| ER-07 Plant operations and safety (OT) | Low |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive (for a subsidiary risk, that subsidiary's President) |
| High | Executive risk committee (Chief Risk Officer, CFO, CIO, CISO, General Counsel), reported to the board risk committee |
| Very High | CEO and CFO jointly, reported to the board risk committee at its next meeting |

Plant-safety risks (ER-07) at High or above cannot be accepted without a dated treatment plan. Risks to Finance customer information are also reported to Finance's Qualified Individual. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E; the holding-company threat picture (shared-services compromise, help desk social engineering, payment fraud, acquisition integration, OT ransomware); the BIA (P05); the gap analysis (P03); and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - **Holding-company rule:** a risk that can stop more than one subsidiary is always assigned to ER-01, whichever subsidiary it starts in, so the board sees concentration in shared services.
   - The enterprise risk profile (section 4) is what the board risk committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 13 |
| Moderate | 38 |
| Low | 13 |
| **Total** | **65** |

By threat source type: Adversarial 30, Structural 21, Accidental 11, Environmental 3.
By treatment: Mitigate 50, Accept 12, Avoid 2, Share/Transfer 1.
By status: In progress 45, Open 8, Closed (accepted) 12.
**23 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Disruption of shared services and subsidiary operations | Operational | 17 | 1 | 4 | 10 | 2 | **Very High** | Moderate | 5 |
| ER-02 | Financial reporting integrity and SEC disclosure | Compliance and financial | 7 | 0 | 1 | 4 | 2 | **High** | Low | 5 |
| ER-03 | Payment fraud and treasury loss | Financial | 6 | 0 | 2 | 3 | 1 | **High** | Low | 5 |
| ER-04 | Compromise of personal and customer information | Compliance and reputational | 11 | 0 | 1 | 5 | 5 | **High** | Moderate | 1 |
| ER-05 | Third-party and concentration risk | Operational | 6 | 0 | 2 | 4 | 0 | **High** | Moderate | 2 |
| ER-06 | Integration of acquired businesses | Strategic | 5 | 0 | 1 | 4 | 0 | **High** | Moderate | 1 |
| ER-07 | Plant operations and safety (OT) | Operational and safety | 5 | 0 | 2 | 2 | 1 | **High** | Low | 4 |
| ER-08 | Responsible use of AI | Strategic and compliance | 8 | 0 | 0 | 6 | 2 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (shared services)** carries the only Very High risk, group-wide ransomware (R-001), and four High risks that share one root: the group identity platform. Help desk social engineering (R-002), unvaulted service accounts (R-018), lateral movement between subsidiaries through the shared directory (R-046), and slow directory recovery (R-061) are all ways one identity failure becomes a failure of every subsidiary.
- **ER-02 (financial reporting and disclosure)** has a Low tolerance, so even Moderate risks are outside it. The High risk is the materiality process (R-008), which does not yet cover incidents that start in a subsidiary or at a vendor.
- **ER-03 (payment fraud)** is outside tolerance mainly because of Home Services branch payables (R-003, R-050) and the chance that the same identity attack reaches both payment approvers (R-004).
- **ER-07 (plant OT)** has two High risks at Plants 2 and 3 (R-011, R-014): a flat network and unmanaged vendor remote access.
- **ER-08 (AI)** is within tolerance today, but the AI assistant data exposure (R-015) and the credit model fairness testing (R-016) depend on work due by 2027-03-31.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Ransomware encrypts shared virtualization, the SCSP, and subsidiary systems at the same time | Very High | ER-01 | Verified identity proofing at the service desk (POAM-001); directory tiering (POAM-005); AQ integration (POAM-003); ERP RTO fix (POAM-010); enterprise exercise with the disclosure committee (POAM-011) | CISO | 2027-03-31 |
| R-002 | Attacker social-engineers the outsourced service desk into resetting MFA for a GBS identity administrator and takes over the group identity platform | High | ER-01 | Verified identity proofing for every reset (POAM-001); phishing-resistant MFA for all privileged accounts (POAM-002); contract standard for the provider (POAM-012) | Director of Identity and Access Management | 2027-03-31 |
| R-003 | A vendor payment is redirected after a fraudulent bank-detail change at a Home Services branch | High | ER-03 | Move branch payables into GBS accounts payable and remove the conflicts (POAM-007); payment-fraud training (POAM-019) | Vice President, Global Business Services | 2026-12-31 |
| R-004 | A compromised treasury user releases a fraudulent wire through the payment hub | High | ER-03 | Payee allow-lists and anomaly rules at the primary bank | Treasurer | 2027-03-31 |
| R-005 | Theft of Finance customer information (about 520,000 consumers) | High | ER-04 | Data minimization and retention enforcement (POAM-022); egress analytics on the warehouse | Finance Information Security Officer | 2027-03-31 |
| R-007 | Attacker enters through an AQ-01 or AQ-02 legacy directory or site VPN and reaches the SCSP integration platform | High | ER-06 | Restrict AQ VPNs to named hosts (POAM-015); federate identities and migrate ERPs (POAM-003) | Vice President, Integration Management Office | 2027-03-31 |
| R-008 | A material incident is disclosed late or incompletely because the playbook does not cover incidents that start in a subsidiary or at a vendor | High | ER-02 | Update the playbook and run a full tabletop on 2026-11-19 (POAM-011) | General Counsel | 2026-11-30 |
| R-011 | Ransomware or an attacker in plant OT stops a plant or forces an unsafe machine state | High | ER-07 | Segment Plant 3 (POAM-015); complete the OT inventory (POAM-014); vendor access through PAM (POAM-016) | Director of OT Security | 2027-03-31 |
| R-013 | The outsourced service desk provider is breached or fails | High | ER-05 | Contract amendment and quarterly verification audits (POAM-012) | Director of Third-Party Risk Management | 2026-12-31 |
| R-014 | An attacker uses a vendor's unmanaged remote access tool to reach plant controllers | High | ER-07 | Route all OT vendor access through the OT PAM gateway (POAM-016) | Director of OT Security | 2026-12-31 |
| R-018 | An attacker uses a service account with a non-expiring password to move across the directory | High | ER-01 | Vault or convert to managed identities (POAM-004); remove domain admin rights (POAM-005) | Director of Identity and Access Management | 2027-03-31 |
| R-026 | Malicious code arrives in a trusted vendor software update | High | ER-05 | Staged rollout for all tier-1 software; SBOM requests for tier-1 vendors | CISO | 2027-06-30 |
| R-046 | A compromise in one subsidiary spreads to the others through shared directory trust | High | ER-01 | Directory tiering and per-subsidiary administration boundaries (POAM-005) | Director of Identity and Access Management | 2026-12-31 |
| R-061 | The directory takes longer to restore than planned after a full directory compromise | High | ER-01 | Annual full forest recovery exercise | Director of Identity and Access Management | 2027-04-30 |

## 6. Themes from the 2026 analysis
1. **Identity is the shared-services single point of failure (ER-01).** One directory and one identity provider serve every subsidiary, and the outsourced service desk can reset any credential after knowledge-based checks. The P08 scenario follows exactly this path. Treatment: verified identity proofing by 2026-12-15, phishing-resistant MFA for all 1,180 privileged accounts by 2027-03-31, and directory tiering by 2026-12-31.
2. **Payment fraud at the edges (ER-03).** The payment hub is well controlled; the exposure is in Home Services branch payables and the three local bank portals outside the hub (R-003, R-050; P07 AC-5, SI-7).
3. **Disclosure readiness for a group, not just a company (ER-02).** The materiality playbook and the quarterly sub-certifications do not yet capture incidents that start in a subsidiary, in plant OT, or at a vendor, or a series of related incidents across subsidiaries (R-008, R-065).
4. **Acquisitions (ER-06).** AQ-01 and AQ-02 keep their own directories and ERPs until 2027, with manual consolidation uploads, nightly-only backups, and site VPNs that reach the integration platform (R-007, R-010, R-012, R-020). Going forward, deal approvals must include technical cyber diligence and an integration budget (R-060).
5. **Plant OT (ER-07).** Inventory is 72% complete, Plant 3 is flat, and two plants allow unmanaged vendor remote access (R-011, R-014, R-039).
6. **AI (ER-08).** 14 use cases; 8 reviewed. The assistant's reach across subsidiaries (R-015) and the credit model (R-016) are the two that matter most. Unapproved public AI tools are blocked (R-041, Avoid) and the resume ranking feature stays off (R-042, Avoid).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $7.4 million:** phishing-resistant keys and identity proofing service ($1.1M), directory tiering and service account vaulting ($0.9M), AQ-01 and AQ-02 identity federation and ERP migration ($2.6M, from the integration budget), Plant 3 segmentation and OT PAM gateway ($1.3M), OT asset discovery ($0.4M), integration middleware upgrade ($0.5M), SIEM onboarding for AQ, OT, and integration logs ($0.4M), and outside counsel for the disclosure tabletop ($0.04M). Two IT auditor positions are in the 2027 Internal Audit budget. Items map to the POA&M in P07.
- **Accepted (12):** R-021, R-030, R-036, R-038, R-044, R-048, R-049, R-054, R-055, R-058, R-062, R-064. Each is Low or Moderate residual and within tolerance, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-041 (unapproved AI tools blocked) and R-042 (AI resume ranking disabled until review).
- **Shared (1):** R-035 (processor-hosted payment fields and cyber insurance for card brand assessments).
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of High on 2026-09-14; the board risk committee reviewed it on 2026-09-17.

## 8. Board reporting
**Risk committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-17 joint session received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-009, R-032), disclosure controls (R-008, R-053, R-065), and the draft Item 106 disclosure, which describes this process.
**Finance board (annually):** the Qualified Individual's report includes every risk tagged to Finance customer information (16 CFR 314.4(i)).
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-14.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-14.
- Joint audit and risk committee session of the board: reviewed the enterprise risk profile, 2026-09-17.
- Next full review: May to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
