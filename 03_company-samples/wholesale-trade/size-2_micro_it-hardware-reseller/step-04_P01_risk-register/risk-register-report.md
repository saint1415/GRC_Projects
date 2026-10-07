# Risk Register Report: Cris Santos Company | Wholesale Trade | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (IT hardware and software reseller) |
| Size tier | Micro (7 employees) |
| Vertical | Wholesale Trade |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); supply chain threats from NIST SP 800-161 Rev. 1 |
| Prepared | 2026-07-24 by the Operations Manager (security and compliance lead) with the Owner and the MSP lead technician |
| Updated | 2026-08-12 (R-024 added from P07 testing); 2026-08-25 (R-020 to R-022 from the AI assessment, P10); 2026-08-31 (R-013 and R-016 accepted and closed) |
| Approved | 2026-08-31 by the Owner |

## 1. Scope and risk framing
**Scope.** The whole company and its key vendors and suppliers. That covers every system in `../00_company-facts.md` section 3 (SYS-01 to SYS-10), the stockroom, and the outside parties the business depends on: the ERP and suite vendors, the MSP, the 16 suppliers (including 4 brokers), the bank, and the ERP's AI subprocessor. The register covers three kinds of harm:
- harm to the company's own systems and data (FCI, orders, payments);
- harm to customers from the **products** it resells (counterfeit, tampered, or covered equipment);
- loss of DoD business through FAR, DFARS, Section 889, or CMMC failures.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Operations Manager may accept.
- Moderate: only the Owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead. A risk that could put counterfeit, tampered, or covered equipment on a DoD order is never accepted.

**Overlapping roles.** The Owner is risk acceptor, Affirming Official, and a risk owner. Government contracts counsel reviews the High risks that involve federal filings (R-004, R-024), and the independent assessor's P07 results are the outside check on this register.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the supply chain threat examples in SP 800-161 Rev. 1, the BIA (P05), the gap analysis (P03), the April 2026 payment diversion, and interviews with all 7 staff and the MSP lead technician (2026-07-13 to 2026-07-24).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3). For a company with about $920 of gross profit per business day, a $50,000 loss or the loss of DoD eligibility (about 22% of revenue) is rated High or Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 5 |
| Moderate | 15 |
| Low | 4 |
| Very Low | 0 |
| **Total** | **25** |

Treatment: 23 Mitigate, 2 Accept (R-013 and R-016, both Low). Status: 12 Open, 11 In progress, 2 Closed.

### Very High and High risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-004 | Unsupported CMMC Level 1 result and affirmation in SPRS | Very High | Correct the SPRS entry on counsel's advice; no new setup orders until a documented self-assessment shows all 15 requirements MET | Owner | 2026-10-31 |
| R-001 | Counterfeit or tampered equipment from a broker sold to a customer | High | Written sourcing order; authorized sources only for DoD orders; broker assessment; receiving checklist | Purchasing and Inventory Coordinator | 2026-11-30 |
| R-002 | Covered (Section 889) equipment delivered on a DoD order | High | Manufacturer of record for every SKU; screening list; hard block on DoD quotes | Federal Account Manager | 2026-10-31 |
| R-003 | Supplier email compromise diverts a payment | High | Call-back on the number in the ERP; Owner approves the first payment to new details; 5-day hold | Bookkeeper | 2026-09-30 |
| R-010 | MSP RMM tool compromise reaches every computer | High | Annual MSP security review; 24-hour incident notice and a recovery commitment at renewal | Owner | 2026-12-31 |
| R-024 | The company's own camera recorder was covered equipment; the SAM representation may be inaccurate | High | Replaced 2026-08-20; counsel reviews the representation and any report; screen all company equipment | Owner | 2026-09-30 |

**The common theme is "the company cannot yet vouch for what it says or sells."** It affirmed CMMC Level 1 without an assessment (R-004), represented in SAM that it uses no covered equipment without checking its own stockroom (R-024), and sells products without screening or inspection (R-001, R-002). These four share one fix: a written supplier and screening process (C-SCRM plan) plus documented checks before anything is affirmed. The same work lowers R-011 (setup bench), R-019 (missed reports), and R-021 (AI subprocessor).

**Risks found or changed during the work:**
- R-009: the former setup technician's ERP account was found active on 2026-07-15 and disabled that day. The ERP sign-in log showed no use after the termination date. The process gap remains open.
- R-024: added on 2026-08-12 after P07 testing found the stockroom camera recorder and cameras are white-label units of a manufacturer named in the FAR 52.204-25 covered definition.
- R-020 to R-022: added on 2026-08-25 from the AI assessment (P10).

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner on 2026-08-31; about $8,800 one-time and $3,150 a year):**
  - Independent assessment (P07) and policy work: about $3,500 one-time
  - Government contracts counsel for the SPRS correction and the Section 889 representation review: about $2,500 one-time (R-004, R-024)
  - Replacement cameras and recorder from a non-covered manufacturer: about $1,200 one-time (R-024)
  - Setup bench rebuild and a separate bench network segment by the MSP: about $900 one-time (R-011)
  - Visitor log, individual alarm codes, and a key log: about $400 one-time (R-014)
  - Receiving inspection supplies and OEM serial lookups: about $300 one-time (R-001)
  - MSP-managed endpoint detection and response with after-hours alerting on 9 computers: about $1,600 a year (R-006)
  - Vulnerability scanning by the MSP: about $600 a year (R-025)
  - Security awareness training with phishing simulations for 7 people: about $500 a year (R-003, R-005)
  - Backup upgrade to 1-year immutable versions: about $450 a year (R-007)
- **Accepted:** R-013 (Low; laptops encrypted) and R-016 (Low; staff can work from home on laptops).
- **Contract actions:** supplier purchase order terms (Section 889 and DFARS 252.246-7008 flowdown, notice of suspect items) by 2026-10-31; ERP vendor AI terms by 2026-10-31 (R-021); MSP contract amendment at renewal by 2026-12-31 (R-010).
- **Business decision:** no new DoD setup orders after 2026-10-31 until the Level 1 self-assessment is documented and all 15 requirements are MET (R-004). COTS-only DoD orders, which carry no FAR 52.204-21 or CMMC requirement, continue.

## 5. Approval
- Owner: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example accepting CUI, adding a broker, or turning on AI auto-submit again), an incident, or a change in FAR or CMMC rules.
