# Risk Register Report: Cris Santos Company | Emergency Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensed private ambulance service) |
| Size tier | Small (60 employees) |
| Vertical | Emergency Services (CISA sector; NAICS 621910 Ambulance Services) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A) (C-EMERGENCY-R04) |
| Prepared | 2026-07-31 by the IT Manager (Security Officer); R-007 added 2026-08-12 |
| Approved | 2026-09-04 by the COO (Moderate and below) and the majority owner (High and Very High) |

## 1. Scope and risk framing
**Scope.** The Dispatch and Patient Care Platform (DPCP) and every business process in the BIA (P05). That covers each system that creates, receives, maintains, or transmits ePHI (CAD, ePCR, billing, phone recordings, fleet mobile systems) and the vendors that handle it (`../00_company-facts.md` section 3).

**What makes this business different.** A dispatch outage is a patient safety event, not only an IT event. Every minute that a 911 or urgent interfacility call waits for manual handling can delay care. Impact ratings therefore use the BIA safety category (P05) first.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the COO may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. Risks that can delay emergency response at High or above are never accepted without treatment.

This is the company's first documented security risk analysis.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, interviews with the Communications Center Supervisor, Operations Manager, and Billing and Compliance Manager, the gap analysis (P03), and CISA's Emergency Services Sector context.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (safety, operations, regulatory, cost, reputation).
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 4 |
| Moderate | 17 |
| Low | 11 |
| **Total** | **33** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware encrypts the CAD server and dispatch consoles, forcing manual dispatch | Very High | EDR with 24x7 alerting; monthly console patching; dispatch segment; quarterly manual dispatch drills | IT Manager | 2026-12-31 |
| R-002 | Backups destroyed along with production | High | Immutable, separate-account, second-region backups; quarterly restore tests | IT Manager | 2026-11-30 |
| R-007 | Internet-exposed vehicle routers with default passwords | High | Remote admin disabled and passwords changed 2026-08-14; central router management | IT Manager | 2026-10-31 |
| R-009 | Dispatch center unusable after a hurricane or fire, with no alternate site | High | Alternate dispatch position at Station 2; county PSAP overflow agreement; annual relocation drill | Communications Center Supervisor | 2027-05-31 |
| R-021 | MSP remote tool compromise reaches every endpoint and the cloud tenant | High | MFA and source restrictions on MSP tooling; annual MSP security review | COO | 2026-12-31 |
| R-014 | AI triage under-prioritizes a critical call once it leaves shadow mode | Moderate | Go-live gate with validation and bias thresholds (P10) | Medical Director | 2026-12-31 |
| R-005 | Shared CAD logins prevent attribution of misuse | Moderate | Named, federated CAD accounts; monthly CAD query review | Communications Center Supervisor | 2026-12-31 |

The five High and Very High risks share one theme: **the company could not keep dispatching reliably through a ransomware attack or a site loss today.** Detection is weak (R-001), backups are exposed (R-002), two routes lead straight into the environment (R-007 and R-021), and there is nowhere else to dispatch from (R-009). Fixing them also reduces seven related Moderate risks (R-003, R-004, R-008, R-010, R-022, R-031, R-032) and one Low risk (R-023).

R-007 was added on 2026-08-12 after control assessment testing (P07) found three vehicle routers with internet-exposed administration and default passwords. The IT Manager closed the exposure on 2026-08-14. The risk stays open until every router is under central management.

## 4. Treatment summary
- **Funded (2026 Q4 budget, $55,000):**
  - EDR and 24x7 monitoring through the MSP
  - Backup redesign (separate account, immutable retention, second region)
  - Network segmentation at headquarters (dispatch, office, guest)
  - Vehicle router management platform
  - Hardware security keys for administrators
  - Monthly authenticated vulnerability scanning
  - Alternate dispatch position at Station 2 (2027 Q2, before hurricane season)
- **Accepted:**
  - R-015: Low, because tablets are encrypted and can be wiped remotely
  - R-025: Low, because crews can phone ECG findings to the hospital
  - R-026: Low, because tablets work offline
- **Avoided:** R-033. The company will not accept criminal justice information feeds from the county unless a CJIS compliance program and agreement are in place first.
- **Contract actions:** BAA amendment covering the AI triage service (R-013) by 2026-10-15; BAA with the hosted phone vendor or a replacement vendor (R-012) by 2026-10-31.

## 5. Approval
- COO: approved Moderate and Low treatments and acceptances, 2026-09-04.
- Majority owner: approved the High and Very High treatment plans and the budget, 2026-09-04.
- Next full review: July 2027, or sooner after a major change (for example, moving the AI triage pilot out of shadow mode) or an incident.
