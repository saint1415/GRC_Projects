# Risk Register Report: Cris Santos Company | Health Care and Social Assistance | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (multi-specialty physician practice) |
| Size tier | Small (60 employees) |
| Vertical | Health Care and Social Assistance |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A) |
| Prepared | 2026-07-24 by the IT Manager (Security Officer) |
| Approved | 2026-08-31 by the Practice Administrator (Moderate and below) and the majority owner (High) |

## 1. Scope and risk framing
**Scope.** The Clinical and Revenue Cycle Platform (CRCP) and the business processes in the BIA (P05). That covers every system that creates, receives, maintains, or transmits ePHI at both clinics, plus the vendors that handle ePHI for the practice ([asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv)).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the Practice Administrator may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. Patient-safety risks at High are not acceptable.

This is the practice's first documented risk analysis since 2021.

## 2. Method
1. **Identify.** Threat sources and events were identified from SP 800-30 Appendices D and E, the BIA, the intake evidence, and interviews with the Clinic Managers and Billing Manager (EV-033). The gap analysis (P03) ran in the same fieldwork window, as is usual for a HIPAA risk analysis, and the two shared findings.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the ticket history (EV-017), configuration exports, walk-throughs and interviews. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 18 |
| Low | 10 |
| **Total** | **31** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware via phishing encrypts endpoints and cloud workloads | High | EDR with 24x7 alerting; phishing training; segmentation | IT Manager | 2027-01-31 |
| R-005 | Backups destroyed along with production | High | Immutable, separate-account, second-region backups; quarterly restore tests | IT Manager | 2026-12-31 |
| R-022 | MSP remote tool compromise reaches every endpoint | High | MFA and IP restrictions on MSP tooling; annual MSP security review | Practice Administrator | 2026-12-31 |
| R-013 | Unpatched firewall firmware exploited | Moderate | Quarterly firmware updates; vulnerability scanning | IT Manager | 2026-11-30 |
| R-006 | Workforce snooping in patient records | Moderate | Monthly access report review; sanctions policy | Privacy Officer | 2026-11-30 |
| R-028 | AI scribe error in a clinical note | Moderate | Provider review attestation; monthly sampling | Medical Director | 2026-11-30 |

The three High risks share one theme: **the practice could not recover from a ransomware attack today.** Detection is weak (R-001), the backups are exposed (R-005), and a trusted vendor has broad access (R-022). Fixing these three also reduces six related Moderate risks (R-002, R-007, R-013, R-017, R-019, R-021) and one Low risk (R-026).

**Two passes.** Pass 1 was completed on 2026-07-24 from intake and fieldwork evidence. Pass 2 followed the control assessment (P07): R-031 was added on 2026-08-07 after testing found manufacturer default passwords on four vital-sign monitors (EV-IA-5). The `assessment_pass` column shows which pass produced each risk.

## 4. Treatment summary
- **Funded (2026 Q4 budget, $48,000):**
  - EDR and 24x7 monitoring through the MSP
  - Backup redesign
  - Full-disk encryption on desktops
  - Cellular failover for Clinic B
  - A badge reader at Clinic B (deferred to 2027 Q1)
- **Accepted:**
  - R-014: hardware keys already reduce it to Low
  - R-020: Low
  - R-023: Moderate, covered by a line of credit
  - R-027: Low, vendor-managed
- **Contract actions:** BAAs for the fax, telehealth, and AI scribe vendors (R-011, R-012), due by 2026-10-31.

## 5. Approval
- Practice Administrator: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Majority owner: approved the High-risk treatment plans and the budget, 2026-08-31.
- Next full review: July 2027, or sooner after a major change or incident.
