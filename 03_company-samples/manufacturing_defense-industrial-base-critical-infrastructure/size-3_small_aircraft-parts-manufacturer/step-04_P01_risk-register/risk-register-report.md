# Risk Register Report: Cris Santos Company | Defense Industrial Base | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts manufacturer, DoD subcontractor) |
| Size tier | Small (250 employees) |
| Vertical | Defense Industrial Base |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | SP 800-171 Rev. 2 requirement 3.11.1 (periodic risk assessment), CMMC RA.L2-3.11.1 |
| Prepared | 2026-07-24 by the IT Manager; R-032 added 2026-08-07 |
| Approved | 2026-08-31 by the Vice President of Operations (Moderate and below) and the President (High and Very High) |

## 1. Scope and risk framing
**Scope.** The CUI Engineering Enclave (CEE) defined in the SSP (P02), the printed CUI on the shop floor, the business processes in the BIA (P05), and the systems outside the enclave that could affect it or the company's defense contracts (corporate network, ERP, MSP). See `../00_company-facts.md` sections 3 and 4.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the Vice President of Operations may accept, with a treatment plan or a documented reason.
- High and Very High: only the President may accept, and only temporarily with a dated treatment plan.
- Not acceptable at any level: a known failure to meet a DFARS 252.204-7012 duty (reporting, flowdown, adequate security), or an unauthorized ITAR release. These are treated, not accepted.

This is the company's first documented risk assessment since the 2024 SSP.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, interviews with the Plant Manager, Quality Manager, Director of Engineering, and Contracts Manager, the plant walkthrough, and the gap analysis (P03). Threats to aerospace suppliers from foreign intelligence services and contracted actors were included because the company holds controlled technical information for military aircraft.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3), including flight safety and export control harm.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 6 |
| Moderate | 18 |
| Low | 7 |
| Very Low | 0 |
| **Total** | **32** |

By threat source type: 16 Adversarial, 9 Accidental, 6 Structural, 1 Environmental.

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Cannot show the CMMC status Prime A flows down or SP 800-171 Rev. 2 compliance under DFARS 252.204-7012 | Very High | Remediation roadmap (P03); voluntary C3PAO assessment 2027-02 | Vice President of Operations | 2027-02-26 |
| R-002 | Phishing steals an engineer's session token; CAD models bulk-synced from the enclave | High | Phishing-resistant MFA; download alerts; log review; 24x7 detection | IT Manager | 2027-01-31 |
| R-003 | SPRS score of 96 overstates implementation (recalculated -65) | High | Corrected score and date-to-110 in SPRS | Contracts Manager | 2026-09-30 |
| R-005 | Visitor or foreign person sees ITAR drawings on the shop floor | High | Escort and log every visitor; cell drawing cabinets | Plant Manager | 2026-10-31 |
| R-008 | Cyber incident not reported to DoD within 72 hours | High | Medium assurance certificates; DIBNet drill | Contracts Manager | 2026-11-30 |
| R-011 | Ransomware destroys MES, DNC, and their local backups | High | Daily cloud backups of MES and DNC; close remote desktop; restore test | Manufacturing Systems Engineer | 2026-12-31 |
| R-014 | CUI pasted into public AI chatbots or file-sharing sites | High | Block categories at the enclave firewall; approved-tools list; training | IT Manager | 2026-10-31 |

The High and Very High risks share one theme: **the company's contract eligibility depends on proving controls it has not yet evidenced.** R-001 and R-003 are compliance risks with direct revenue impact: Prime A is about 40% of revenue. R-002, R-005, and R-014 are the ways CUI is most likely to leave the company today, and R-008 means that if it did, the company could not meet its DFARS reporting duty. Fixing R-002 and R-016 (log review) also reduces R-015 and R-032.

R-032 was added on 2026-08-07 after control assessment testing (P07) found two departed employees' enclave accounts still enabled, 19 and 45 days after departure.

## 4. Treatment summary
- **Mitigate (25 risks).** Funded in the 2026 Q4 and 2027 Q1 budget ($185,000 approved by the President on 2026-08-31):
  - Phishing-resistant security keys for all enclave users and 24x7 managed detection for the enclave (R-002, R-016)
  - Vulnerability scanning service (R-013)
  - FIPS-validated firewall firmware and SFTP configuration (R-004)
  - DNC serial gateway for the 6 legacy CNC machines (R-012)
  - Cell drawing cabinets and locked shred bins (R-005, R-020)
  - Forensic retainer (R-009)
  - C3PAO assessment fee (R-001)
  - MES and DNC cloud backups (R-011)
- **Avoid (1 risk).** R-029: the enclave suite's AI assistant stays off until the P10 conditions are met.
- **Share or transfer (1 risk).** R-025: property and business interruption insurance for hurricanes, plus preparation steps in the contingency plan.
- **Accept (5 risks, all Low).** The IT Manager may accept Low risks; the Vice President of Operations confirmed all five on 2026-08-31:
  - R-023: cloud provider regional outage; the shop floor keeps running
  - R-024: single plant internet circuit; to be revisited in the contingency plan
  - R-026: MSP compromise; the MSP has no enclave access
  - R-027: vendor remote support, already controlled
  - R-028: lost or stolen laptop; full-disk encryption and remote wipe
- **Contract actions:** DFARS 252.204-7012 and 252.204-7020 flowdown to the 3 outside processors (R-010) and a written ERP scoping position from Prime A (R-019), both by 2026-10-31.

## 5. Approval
- Vice President of Operations: approved Moderate and Low treatments and acceptances, 2026-08-31.
- President (majority owner and CMMC Affirming Official): approved the Very High and High treatment plans and the budget, 2026-08-31. No High or Very High risk was accepted.
- Next full review: July 2027, or sooner after a major change, an incident, or the C3PAO assessment.
