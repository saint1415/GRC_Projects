# Enterprise Risk Register Report: Cris Santos Company | Other Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded national electronics and device repair chain: 1,120 stores in 44 states and DC, 3 depots, a national data recovery lab) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Other Services (except Public Administration) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | PCI DSS v4.0.1 12.3.1 targeted risk analyses (input); the HIPAA risk analysis for SL-2 ePHI (45 CFR 164.308(a)(1)(ii)(A)); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk and technology committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** All systems that store, process, or transmit customer, card, client, or employee data, or that support tier-1 processes, across the 1,120 stores (including the 160 AC stores), the three depots, the data recovery lab, the contact center, two clouds and two colocation sites, and about 1,300 vendors. Business processes and impact values come from the enterprise BIA (P05). The STPP is also covered at system level in the SSP (P02).

**Three lines.** Risk owners in the business and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Customer trust:** low appetite for unauthorized access to customer personal data or the contents of devices in the company's custody. Customers hand over their phones; the business depends on that trust.
- **Payments:** low appetite for card data compromise or loss of PCI DSS standing.
- **Regulatory, contractual, and disclosure:** low appetite for noncompliance with the FTC Act, state privacy and breach laws, SEC disclosure rules, the merchant agreement, manufacturer program agreements, or client contracts.
- **Service continuity:** moderate appetite for disruption of store, depot, and SL-1 services, within the BIA tolerances.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Store, depot, and service disruption from cyber and technology events | Moderate |
| ER-02 Compromise of customer personal data and device contents | Low |
| ER-03 Payment card compromise and PCI DSS standing | Low |
| ER-04 Third-party, manufacturer, and client dependency | Moderate |
| ER-05 Integration of the acquired chain | Moderate |
| ER-06 Regulatory, contractual, and disclosure compliance | Low |
| ER-07 Financial reporting integrity and fraud | Low |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, CIO, COO, CISO, General Counsel), reported to the risk and technology committee |
| Very High | CEO and CFO jointly, reported to the risk and technology committee at its next meeting |

Risks under ER-02 and ER-03 at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the repair and retail threat picture (POS malware, e-skimming, insider access to customer devices, ransomware), the BIA (P05), the gap analysis (P03), and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3).
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each system-level cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category (operational, strategic, compliance, financial).
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the risk and technology committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 11 |
| Moderate | 30 |
| Low | 22 |
| **Total** | **64** |

By threat source type: Adversarial 33, Structural 20, Accidental 9, Environmental 2.
By treatment: Mitigate 53, Accept 9, Avoid 2.
By status: In progress 42, Open 11, Closed (accepted) 9, Closed (avoided) 2.
**25 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Store, depot, and service disruption from cyber and technology events | Operational | 10 | 0 | 2 | 3 | 5 | **High** | Moderate | 2 |
| ER-02 | Compromise of customer personal data and device contents | Compliance and reputational | 19 | 0 | 4 | 5 | 10 | **High** | Low | 9 |
| ER-03 | Payment card compromise and PCI DSS standing | Compliance and financial | 6 | 1 | 1 | 3 | 1 | **Very High** | Low | 5 |
| ER-04 | Third-party, manufacturer, and client dependency | Operational | 11 | 0 | 1 | 6 | 4 | **High** | Moderate | 1 |
| ER-05 | Integration of the acquired chain | Strategic | 5 | 0 | 1 | 4 | 0 | **High** | Moderate | 1 |
| ER-06 | Regulatory, contractual, and disclosure compliance | Compliance | 4 | 0 | 1 | 3 | 0 | **High** | Low | 4 |
| ER-07 | Financial reporting integrity and fraud | Financial | 3 | 0 | 0 | 2 | 1 | **Moderate** | Low | 2 |
| ER-08 | Responsible use of AI | Strategic | 6 | 0 | 1 | 4 | 1 | **High** | Moderate | 1 |

**Reading the profile:**
- **ER-03 (payments)** carries the only Very High risk: POS malware at the AC stores, where card data is still in clear text (R-001). It also holds the ROC timing risk (R-013). Both fall when the AC stores convert to P2PE.
- **ER-02 (customer data and device contents)** has the most risks and the most outside tolerance (9), because the board set a Low tolerance. The four High risks are the ones a repair business uniquely carries: passcodes in records (R-002, R-007), technician access to devices (R-005), and devices resold or recycled with data (R-006).
- **ER-05 (acquired chain)** has only five risks of its own, but AC conditions also drive R-001, R-007, and R-013. Integration is the single largest driver of the board-level exposure.
- **ER-06 (compliance)** is outside tolerance because the materiality process has not been exercised for this incident type (R-009), and because two new obligations (California cybersecurity audit, SL-2 business associate duties) are not yet operational.

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Memory-scraping malware on AC legacy POS captures card data at the 160 AC stores | Very High | ER-03 | Convert AC stores to P2PE and the STPP in two waves; interim EDR, card data VLAN, and SIEM feed; remove the legacy remote tool (POAM-001; POAM-002; POAM-012) | Vice President, Integration Management Office | 2027-03-31 |
| R-002 | Bulk export of STPP customer records including passcode-like strings in notes | High | ER-02 | Purge and block passcode and card-number strings (POAM-003); atypical-use analytics (POAM-005) | Chief Digital Officer | 2026-11-30 |
| R-003 | Ransomware across stores, depots, and enterprise systems | High | ER-01 | Close AC gaps; EDR on remaining bench workstations; ransomware exercise with the disclosure committee (POAM-005; POAM-008) | CISO | 2027-03-31 |
| R-004 | Attacker enters through AC flat networks or the legacy remote tool and reaches enterprise systems | High | ER-05 | PAM-brokered support; segmentation; SD-WAN conversion (POAM-002) | Director of Network Engineering | 2026-12-15 |
| R-005 | Technician views or copies personal content from a customer device | High | ER-02 | New image with cache wipe; log review; agreements; atypical-use analytics (POAM-005) | Senior Vice President, Store Operations | 2027-01-31 |
| R-006 | Device resold or recycled with customer or client data | High | ER-02 | Per-device verification at Depot West; store drop-off chain of custody (POAM-006) | Director of Sanitization and Asset Recovery | 2026-12-31 |
| R-007 | Theft of AC legacy ticketing data with passcodes and account passwords | High | ER-02 | Purge; named accounts with MFA; migrate and decommission (POAM-004) | Vice President, Integration Management Office | 2026-12-15 |
| R-009 | Material incident disclosed late or inaccurately | High | ER-06 | Playbook update; tabletop 2026-11-12 (POAM-008) | General Counsel | 2026-11-30 |
| R-011 | AI applicant screening produces discriminatory outcomes or misses required notices and audits | High | ER-08 | Independent bias audit; notices; disable ranking where requirements are not met (POAM-009) | Chief Human Resources Officer | 2026-12-31 |
| R-013 | 2026 ROC cannot be completed as compliant because of the AC stores | High | ER-03 | Agree the assessment approach with the acquirer and the QSA; deliver wave 1 (POAM-001) | Vice President, Payments | 2026-12-15 |
| R-014 | Zero-day in an internet-facing edge device is exploited | High | ER-01 | 72-hour emergency patch SLA; retire AC firewalls (POAM-019) | Director of Network Engineering | 2027-03-31 |
| R-015 | Malicious code in a trusted vendor software update | High | ER-04 | Staged rollout for tier-1 software; SBOM from tier-1 vendors | CISO | 2027-06-30 |

## 6. Themes from the 2026 analysis
1. **The acquired chain (ER-05, ER-03, ER-02).** The 160 AC stores still take cards on legacy POS without encryption at the PIN pad, keep passcodes and account passwords in a legacy ticketing service, and run flat networks reachable by a legacy remote support tool. These conditions create the only Very High risk (R-001) and three High risks (R-004, R-007, R-013). Treatment: conversion in two waves (2026-12-15 and 2027-03-31) with interim controls now.
2. **Customer devices in custody (ER-02).** The company holds about 37,000 customer devices a day. Three of 37 access complaints in 2026 were substantiated (R-005), bench caches survive on older images (R-022), and a sanitized laptop was resold with client data in 2026-05 (R-006). Testing also found default passwords on sanitization stations (R-057, new from P07).
3. **Passcodes in records (ER-02).** The restricted passcode field works, but free-text habits put passcodes back into notes (R-002) and the AC legacy service was built around a free-text passcode field (R-007).
4. **Payments beyond the stores (ER-03).** The mobile web deposit page lacks script controls (R-008), phone payments are only 62% masked (R-016), and 7 TPSP AOCs are expired (R-024).
5. **New obligations (ER-06, ER-08).** The California cybersecurity audit period starts 2027-01-01 (R-027); SL-2 business associate duties are not yet mapped (R-026); state AI hiring laws apply to the applicant screening tool now (R-011). The technician productivity scoring feature was switched off pending review (R-042, treatment Avoid).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $9.1 million:** AC conversion acceleration and interim controls ($4.2M), NAC for the remaining 320 core stores ($1.3M), bench workstation image and atypical-use analytics ($0.9M), DTMF masking for all phone payments ($0.8M), Depot West sanitization verification ($0.6M), California cybersecurity audit readiness ($0.45M), notes purge and pattern blocking ($0.35M), payment page script tooling for the mobile deposit page ($0.25M), independent AI bias audit ($0.18M), and outside counsel for the disclosure tabletop ($0.04M). Items map to the POA&M in P07.
- **Accepted (9):** R-030, R-031, R-036, R-039, R-046, R-047, R-049, R-051, R-062. Each is Low or Moderate residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-041, R-042. Unapproved generative AI domains are blocked, and the technician productivity scoring feature is disabled until review.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and the residual target of Moderate on 2026-09-08; the risk and technology committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk and technology committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-031), PCI DSS ROC status (R-013), and disclosure controls (R-009). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk and technology committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.
