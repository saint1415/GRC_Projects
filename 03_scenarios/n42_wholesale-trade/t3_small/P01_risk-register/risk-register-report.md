# Risk Register Report: Cris Santos Company | Wholesale Trade | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (IT hardware and software wholesale distributor) |
| Size tier | Small (62 employees) |
| Vertical | Wholesale Trade |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); supply chain threats per NIST SP 800-161 Rev. 1 |
| Also supports | SP 800-171 Rev. 2 requirement 3.11.1 (periodic risk assessment); C-SCRM plan (SR-2) |
| Prepared | 2026-07-24 by the IT Manager with the Purchasing and Supplier Manager and Government Contracts Manager; updated 2026-08-07 (R-035) and 2026-08-25 (AI risks) |
| Approved | 2026-08-31 by the Chief Operating Officer (Moderate and below) and the Chief Executive Officer (High) |

## 1. Scope and risk framing
**Scope.** The Order-to-Fulfillment Platform (OFP) and the business processes in the BIA (P05), plus the supply chain that feeds them: 47 suppliers (35 authorized sources and 12 brokers), the MSP, and the SaaS vendors in `../scenario-facts.md` section 3. The register covers three kinds of harm:
- harm to the company's own systems and data (CUI, FCI, orders, payments);
- harm to customers from the **products** the company distributes (counterfeit, tampered, or covered equipment);
- loss of DoD business through CMMC, DFARS, or Section 889 failures.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the Chief Operating Officer may accept, with a treatment plan or a documented reason.
- High and Very High: only the Chief Executive Officer may accept, and only temporarily with a dated treatment plan. Risks that could put counterfeit, tampered, or covered equipment into a DoD system are not accepted at High.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events were identified from SP 800-30 Appendices D and E, the supply chain threat examples in SP 800-161 Rev. 1, the BIA, interviews with purchasing, receiving, the lab, and finance, the May 2026 payment fraud near miss, and the gap analysis (P03).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3). Harm to DoD missions from distributed products counts as Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables with a script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 0 |
| High | 9 |
| Moderate | 20 |
| Low | 6 |
| Very Low | 0 |
| **Total** | **35** |

Treatment: 33 Mitigate, 2 Accept (R-031 and R-034, both Low).

### High risks
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| R-001 | Counterfeit or tampered equipment from a broker ships to a customer | C-SCRM plan; authorized sources only for DoD jobs; broker assessments; receiving inspection | Purchasing and Supplier Manager | 2026-12-15 |
| R-002 | Covered (Section 889) equipment delivered on a federal order | Mandatory manufacturer of record; screening list with a hard block on federal orders | Government Contracts Manager | 2026-11-30 |
| R-003 | Supplier email compromise diverts a supplier payment | Call-back verification; second approver; 5-day hold after bank changes | Controller | 2026-10-15 |
| R-004 | CUI disclosed from the open file share or ERP attachments | CUI enclave project; purge ERP attachments | IT Manager | 2026-12-15 |
| R-005 | CMMC Level 2 not achieved in time; Prime B option lost | Monthly POA&M review; close 5-point items first; C3PAO booked for 2027-02 | Chief Operating Officer | 2027-01-31 |
| R-006 | Unsupported SPRS score and Level 1 affirmation | Corrected SPRS entries on counsel's advice | Chief Executive Officer | 2026-10-31 |
| R-007 | Ransomware encrypts WMS, file server, and endpoints | 24x7 managed detection; immutable backups; segmentation | IT Manager | 2027-01-15 |
| R-010 | MSP RMM tool compromise reaches every device | Customer responsibility matrix; session approval; source restrictions | Chief Operating Officer | 2026-12-15 |
| R-035 | Broker supplies rebranded covered video products | Block the 3 SKUs; quarantine; suspend the broker; screen broker SKUs | Government Contracts Manager | 2026-09-30 |

The High risks share two themes:
- **The company cannot vouch for what it sells** (R-001, R-002, R-035). There is no written sourcing order, no receiving inspection, and no Section 889 screening. The P07 finding of 3 white-label video SKUs (R-035) shows the risk is real, not theoretical. Fixing these also lowers R-009 (firmware tampering), R-015 (single-source lines), and R-027 (automated reordering from brokers).
- **The company cannot prove what it has affirmed** (R-004, R-005, R-006). CUI is widely exposed, and the posted SPRS score and Level 1 affirmation are not supported. The CUI enclave project and corrected SPRS entries come first, because several of these requirements cannot be placed on a CMMC POA&M (32 CFR 170.21).

R-035 was added on 2026-08-07 after control assessment testing (P07) found 3 IP camera and video recorder SKUs from one broker with a blank OEM of record that match rebranded units of a covered manufacturer. None had shipped on a DoD order. R-026 to R-029 were added on 2026-08-25 from the AI assessment (P10).

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1 budget, $118,000, approved 2026-08-31):**
  - Managed detection and response with 24x7 alerting through the MSP: $30,000 per year
  - Replacement of 40 handheld scanners: $36,000
  - C3PAO readiness consultant hours: $15,000
  - CUI enclave (CUI share, lab VLAN, USB control, FIPS mode): $8,000
  - Immutable backup account and 4-hourly WMS backups: $6,000 per year
  - Central log store with 1-year retention: $5,000 per year
  - Outside counsel for SPRS and CMMC corrections: $5,000
  - Vulnerability scanning by the MSP: $4,000 per year
  - Training platform with phishing and role-based modules: $3,000 per year
  - Electronic visitor log and 1-year badge log retention: $2,500
  - Receiving inspection station and OEM serial validation tools: $2,000
  - Cellular failover router: $1,500
- **Accepted:** R-031 (Low, EDI outage with a working fallback) and R-034 (Low, label service outage with carrier portals as fallback).
- **Contract actions:** Section 889 and DFARS 252.246-7008 flowdown in purchase order terms, supplier notification terms, and FCI filtering for the forecasting vendor, all by 2026-10-31.
- **Not funded in this budget:** the C3PAO assessment fee (2027 budget) and a second source for the two single-source lines (R-015, sourcing effort only).

## 5. Approval
- Chief Operating Officer: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Chief Executive Officer: approved the High-risk treatment plans and the budget, 2026-08-31.
- Next full review: July 2027, or sooner after a major change, an incident, or a change in CMMC or FAR rules (see P03 section 5).
