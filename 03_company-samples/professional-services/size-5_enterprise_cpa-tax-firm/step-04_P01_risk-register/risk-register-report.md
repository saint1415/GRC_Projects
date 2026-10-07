# Enterprise Risk Register Report: Cris Santos Company | Professional, Scientific, and Technical Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLP (national CPA and tax firm; 64 offices in 14 states; privately owned by its partners) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Professional, Scientific, and Technical Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | The written risk assessment in 16 CFR 314.4(b)(1)(i)-(iii) and the periodic reassessment in 314.4(b)(2); the business associate risk analysis input for 45 CFR 164.308(a)(1)(ii)(A) (completed separately for PHI repositories under POAM-021) |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO (Qualified Individual); updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the Audit and Risk Committee of the Partnership Board, 2026-09-15 |

## 1. Scope and risk framing
**Scope.** All systems that create, receive, maintain, or transmit customer information, tax return information, PHI held as a business associate, or Federal Contract Information, or that support tier-1 processes: the 64 offices and 12 processing hubs, both cloud estates and both colocation data centers, the six acquired firms (AF-01 to AF-06), the offshore tax outsourcing provider, and the roughly 1,400 vendors (about 260 with client data). Business processes and impact values come from the enterprise BIA (P05). The Tax Engagement Platform is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the service lines and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (approved by the Partnership Board, 2026-02).** Qualitative statements:
- **Client confidentiality:** low appetite for unauthorized disclosure of taxpayer and client information. Confidentiality is the firm's license to operate.
- **Regulatory and professional standards:** very low appetite for noncompliance with the FTC Safeguards Rule, IRC 7216, IRS e-file rules, HIPAA business associate duties, or professional standards.
- **Fraud against clients:** very low appetite for refund, payroll, or payment diversion that starts in firm systems or processes.
- **Filing season continuity:** low appetite for disruption that causes missed client deadlines.
- **Growth and innovation (acquisitions, AI, offshore delivery):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Tax season and service disruption from cyber and technology events | Moderate |
| ER-02 Compromise of taxpayer and client confidential information | Moderate |
| ER-03 Third-party and concentration risk | Moderate |
| ER-04 Integration of acquired firms | Moderate |
| ER-05 Fraud against clients and the firm (refund, payroll, and payment diversion) | Low |
| ER-06 Regulatory and professional standards compliance | Low |
| ER-07 Service line commitments to clients (SL-1, SL-2, SEC-registrant clients) | Moderate |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (director or managing principal) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, Chief Operating Officer, CIO, CISO, General Counsel, National Tax Leader), reported to the Audit and Risk Committee |
| Very High | CEO and Managing Partner with the CFO jointly, reported to the Audit and Risk Committee at its next meeting |

Risks under ER-05 (fraud) and ER-06 (regulatory) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the tax professional threat picture (business email compromise, refund diversion, filing-season phishing described in IRS Pub. 4557), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category (strategic, operational, financial, compliance).
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. One severe risk is never averaged away.
   - The enterprise risk profile (section 4) is what the Audit and Risk Committee sees each quarter.

**How this meets 16 CFR 314.4(b)(1).** The likelihood and impact scales are the criteria for evaluating and categorizing risks ((b)(1)(i)); the BIA impact categories and the FIPS 199 categorization in P02 are the criteria for confidentiality, integrity, and availability, and each row rates existing controls ((b)(1)(ii)); the treatment, acceptance authority, and tolerance rules describe how risks are mitigated or accepted ((b)(1)(iii)).

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 12 |
| Moderate | 33 |
| Low | 18 |
| **Total** | **64** |

By threat source type: Adversarial 30, Structural 20, Accidental 12, Environmental 2.
By treatment: Mitigate 50, Accept 12, Avoid 2.
By status: In progress 43, Open 7, Closed (accepted) 12, Closed (avoided) 2.
**22 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Tax season and service disruption from cyber and technology events | Operational | 9 | 1 | 0 | 4 | 4 | **Very High** | Moderate | 1 |
| ER-02 | Compromise of taxpayer and client confidential information | Compliance and reputational | 18 | 0 | 4 | 8 | 6 | **High** | Moderate | 4 |
| ER-03 | Third-party and concentration risk | Operational | 6 | 0 | 3 | 1 | 2 | **High** | Moderate | 3 |
| ER-04 | Integration of acquired firms | Strategic | 6 | 0 | 2 | 4 | 0 | **High** | Moderate | 2 |
| ER-05 | Fraud against clients and the firm | Financial | 5 | 0 | 1 | 4 | 0 | **High** | Low | 5 |
| ER-06 | Regulatory and professional standards compliance | Compliance | 9 | 0 | 2 | 5 | 2 | **High** | Low | 7 |
| ER-07 | Service line commitments to clients | Operational | 6 | 0 | 0 | 4 | 2 | **Moderate** | Moderate | 0 |
| ER-08 | Responsible use of AI | Strategic | 5 | 0 | 0 | 3 | 2 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (service disruption)** carries the only Very High risk: ransomware with data theft during peak filing season (R-002). The acquired firms (R-003) and the unproven 8-hour RTO (R-031) are why its likelihood is not lower.
- **ER-02 (confidentiality)** holds the most risks (18). Four are High, all tied to identity: business email compromise through adversary-in-the-middle phishing (R-001), client portal account takeover (R-006), insider browsing in open DMS repositories (R-007), and undetected session token replay (R-009).
- **ER-05 (fraud)** and **ER-06 (regulatory)** have the lowest tolerance, so every Moderate risk in them sits outside tolerance. ER-06 includes the offshore IRC 7216 exceptions (R-008) and the untested business email compromise playbook (R-016).
- **ER-07 (service lines)** and **ER-08 (AI)** are within tolerance today, but ER-08 depends on the AI reviews and IRC 7216 memos due 2027-01-08 (R-014).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-002 | Ransomware encrypts the Tax Engagement Platform and steals taxpayer data during peak filing season | Very High | ER-01 | Integrate AF-05 and AF-06 (POAM-005); prove the 8-hour RTO (POAM-011); exercise the incident plan with the Incident Disclosure Committee (POAM-010) | CISO | 2027-01-15 |
| R-001 | Business email compromise through adversary-in-the-middle phishing, then theft of client tax documents | High | ER-02 | Phishing-resistant MFA and device-bound sessions; block unmanaged-device email; token replay detection (POAM-001; POAM-004) | Director of Identity and Access Management | 2027-01-15 |
| R-003 | Attacker enters through an acquired firm's legacy tenant or network | High | ER-04 | Migrate AF-05 by 2026-12-15 and AF-06 by 2027-03-31 (POAM-005) | Chief Integration Officer | 2027-03-31 |
| R-004 | Refund diversion through a changed direct deposit account before e-file | High | ER-05 | Call-back at AF-05 and AF-06; step-up authentication for portal bank changes; reviewer training (POAM-014) | Director of e-file Operations | 2027-01-15 |
| R-005 | E-file transmitter down more than 8 hours before a deadline | High | ER-03 | Contract RTO of 8 hours; tested early-extension plan; second transmission path evaluated (POAM-019) | Director of e-file Operations | 2027-09-01 |
| R-006 | Client portal account takeover by credential stuffing | High | ER-02 | Mandatory client MFA; disable dormant accounts (POAM-002) | Director of Tax Technology | 2027-01-15 |
| R-007 | Insider browses or exports returns beyond need-to-know | High | ER-02 | Engagement-based DMS permissions; role-tuned analytics (POAM-003; POAM-004) | National Tax Leader | 2027-03-31 |
| R-008 | Offshore disclosure without consent, or unmasked SSNs of Form 1040 filers | High | ER-06 | Automated consent gate; K-1 masking; monthly sampling (POAM-008) | National Tax Leader | 2026-12-31 |
| R-009 | Stolen session tokens replayed without detection | High | ER-02 | Token replay and device-binding detections (POAM-004) | Director of Security Operations | 2026-12-31 |
| R-016 | Late or wrong notices because the business email compromise playbook was never exercised | High | ER-06 | Tabletop with the Incident Disclosure Committee on 2026-11-19 (POAM-010) | General Counsel | 2026-12-15 |
| R-030 | Malicious code in a trusted tax software or vendor update | High | ER-03 | Staged rollout; software bills of materials from tier-1 vendors | CISO | 2027-06-30 |
| R-038 | A third party holding client data is breached | High | ER-03 | Clear overdue vendor reviews; continuous monitoring (POAM-015) | Director of Third-Party Risk Management | 2027-03-31 |
| R-048 | Zero-day in a legacy edge device at AF-05 or AF-06 | High | ER-04 | Retire legacy edge devices with migration (POAM-005); 72-hour emergency patch target | Director of Network Engineering | 2027-03-31 |

## 6. Themes from the 2026 analysis
1. **Identity is the battleground (ER-02, ER-05).** Business email compromise is the leading attack on tax professionals, and push MFA no longer stops it: adversary-in-the-middle kits steal the session after the user approves the prompt (R-001, R-009). The same identity weaknesses drive refund diversion (R-004) and client portal takeover (R-006). Treatment: phishing-resistant authenticators and device-bound sessions for all tax staff and mandatory client MFA before the 2027 filing season.
2. **Acquired firms (ER-04).** AF-05 and AF-06 still run their own email, tax software, and EFINs, outside SOC monitoring and enterprise patching (R-003, R-015, R-048, R-051, R-060). Future deals must include security due diligence and funded integration (R-061).
3. **IRC 7216 at scale (ER-06, ER-08).** Offshore delivery (R-008) and AI features (R-012, R-013, R-014, R-043) both create disclosures of tax return information that need a permission or a prior written consent. Sampling found consent and masking exceptions; AI memos are incomplete.
4. **Concentration (ER-03).** One transmitter carries every e-file (R-005), and one identity verification service supports every electronic Form 8879 (R-037).
5. **Readiness to notify (ER-06, ER-07).** The business email compromise playbook, with its three clocks (FTC discovery, IRS confirmation, state determination) and its client-notice step for SEC-registrant clients, has never been exercised (R-016, R-017, R-018, R-019).
6. **Over-retention (ER-06).** About 2.1 million former-client records sit past the 7-year schedule (R-011, R-054). Every breach scenario gets bigger because of them.

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $4.4 million:** phishing-resistant authenticators and device management for about 9,000 staff ($1.1M), AF-05 and AF-06 integration ($1.6M), DMS permission redesign ($420K), token replay and behavior analytics content ($380K), client MFA rollout and support ($310K), records disposal program ($240K), offshore consent automation and masking ($180K), transmitter contract amendment and second-path evaluation ($150K), and outside counsel for the tabletop and state law matrix ($60K). Items map to the POA&M in P07.
- **Accepted (12):** R-021, R-022, R-023, R-029, R-032, R-044, R-045, R-050, R-052, R-055, R-062, R-063. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-041 and R-043. Public generative AI domains are blocked, and the AI drafting-suggestion feature stays off.
- **Very High risk R-002:** not accepted as is. The CEO and Managing Partner and the CFO approved the treatment plan and the residual target of High on 2026-09-08; the Audit and Risk Committee reviewed it on 2026-09-15.

## 8. Board reporting
**Audit and Risk Committee of the Partnership Board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and acceptances made. The 2026-09-15 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Partnership Board (annual):** the Qualified Individual's written report under 16 CFR 314.4(i), presented on 2026-09-17. It covers the overall status of the information security program and compliance with Part 314, and material matters: this risk assessment, risk management and control decisions, service provider arrangements (including the offshore provider and the transmitter), testing results (P07 and the 2026 penetration test), security events and management's responses, and recommended program changes.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and Managing Partner with the CFO: approved the treatment plan and residual target for Very High risk R-002, 2026-09-08.
- Audit and Risk Committee of the Partnership Board: reviewed the enterprise risk profile, 2026-09-15.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition (16 CFR 314.4(b)(2)). KRIs are refreshed quarterly.
