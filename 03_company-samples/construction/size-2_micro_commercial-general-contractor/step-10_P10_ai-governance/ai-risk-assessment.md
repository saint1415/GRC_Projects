# AI Risk Assessment: AI Estimating and Bid Assistant

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor) |
| Tier / Vertical | Micro / Construction |
| AI use case | AI-001: AI estimating and bid assistant, a trial by the Project Manager and Estimator since 2026-06-01 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | Office Manager (security and compliance lead) with the Project Manager and Estimator, 2026-08-26; counsel consulted on FAR 52.203-2 |
| Decision | Owner and President, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner:** Project Manager and Estimator. **Decision authority:** the Owner, who also signs every bid.
- **Policies that apply:**
  - POL-02 A.5: a vendor that holds FCI or Restricted information needs a security check and terms that bar training on company data
  - POL-04 4.3 and 4.6: FCI stays on approved systems; no FCI, Restricted, or Confidential information in unapproved AI tools
  - POL-02 C.3: no company data in public AI chatbots
- **Approved-tools list:** kept by the Office Manager with the inventory. Today it lists AI-001 only, only for the Project Manager, and only under the conditions in section 6.
- **Scale for a Micro company:** there is no AI committee. The Owner, the Office Manager, and the Project Manager review AI use at the monthly POA&M meeting and re-assess AI-001 every quarter.
- **How it started.** The Project Manager signed up on a company credit card after a trade show. No one checked the terms. That is the first finding: a new tool that holds company data must go through POL-02 A.5 before use.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Speed up estimating for a one-estimator company: (1) quantity takeoff from drawing PDFs; (2) unit pricing from the vendor's market data and the company's past estimates; (3) comparison of subcontractor quotes (normalizing scope and flagging exclusions); (4) drafting bid narratives and qualifications |
| Users / operators | The Project Manager and Estimator; the Owner reviews and signs every bid |
| Affected parties | Owners (the price they pay), subcontractors and suppliers (whether they are selected; many are themselves small or sole-proprietor firms), the company (fixed-price exposure) |
| Data | Inputs: drawings and specifications, past estimates and the company's labor and material prices, subcontractor quotes. Outputs: quantities, unit prices, quote comparisons, draft text. **The click-through terms allow customer data to be used to improve the vendor's models** |
| Build or buy | Buy: vendor SaaS; files uploaded by hand |
| Not intended | Submitting bids; selecting subcontractors without the Project Manager's recorded reason; any hiring, discipline, or crew-assignment use; structural, fire protection, or other life-safety quantities |

**Is the data FCI?** It depends on the stage.
- Public solicitation documents posted for all bidders are *not* FCI. FAR 52.204-21(a) excludes "information provided by the Government to the public". The DoD solicitation, when issued, can be estimated in the tool before award.
- Drawings and change-order packages on an **awarded** federal contract *are* FCI. The Project Manager uploaded FC-1 change-order drawings in June and July 2026. That put FCI on an external system the company does not control (P03 G-003, G-024).

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FAR 52.204-21(b)(1)(iii) | **Yes** for FCI | The company must "verify and control/limit connections to and use of external information systems". Uploading FCI under click-through terms fails this |
| DFARS 252.204-7021(d)(2) | **Yes** once a DoD contract with the clause is awarded | FCI may be processed only on systems with the required CMMC status. The tool must either be in the Level 1 scope or never receive FCI |
| FAR 52.203-2, Certificate of Independent Price Determination | **Yes** on federal bids that include it | The offeror certifies that its prices were arrived at independently, without "any consultation, communication, or agreement with any other offeror or competitor" about prices or "the methods or factors used to calculate the prices", and that its prices have not been "knowingly disclosed" to another offeror or competitor before bid opening or award. A vendor feature that pools customers' pricing into shared market suggestions puts that certification at risk |
| FAR 15.403-4 (certified cost or pricing data) | No at this size | The threshold is at least $2.5 million (15.403-4(a)(1)); FC-1 and the DoD job are far below it. Recheck if the company ever negotiates a larger action |
| Owner contract confidentiality clauses | **Yes** | The medical office owner's contract limits sharing of its drawings to parties working on the project. The hospital system's questionnaire asks whether drawings go to AI services |
| Sherman Act Section 1 (15 U.S.C. 1) | Indirectly | Bid rigging and price-fixing are illegal. Counsel reviews any vendor feature that shares or aggregates pricing across contractors |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. The claims the company relied on are kept in the procurement file |
| State AI laws (for example Colorado SB26-189) | No | The company operates in Florida, and AI-001 does not make consequential decisions about individuals |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why not High:** AI-001 does not make, and is not a substantial factor in, a consequential decision about a person, and it does not affect physical safety. The Project Manager decides every quantity used in a bid and every subcontractor selection, and the Owner approves every bid.

**Why not Low:** it influences fixed-price bids worth a large share of the year's revenue, it holds FCI and owners' confidential drawings, and its quote comparison affects which small firms get work.

**Escalation triggers (re-tier to High and re-assess):**
- automatic bid submission or automatic subcontract award
- use for hiring, discipline, or crew assignment (employment)
- use for structural, fire protection, or other life-safety quantities
- turning on any feature that pools pricing across the vendor's customers

## 4. MEASURE
Trial evidence: a back-test on 5 completed past bids (3 renovations, 2 new tenant improvements) and live monitoring of 12 bids from June to August 2026, including 14 bid packages with 61 subcontractor quotes.

| Trustworthy characteristic | Test / metric | Result (trial) | Pass? |
|---|---|---|---|
| Valid and reliable | Takeoff quantity error by trade versus the Project Manager's final takeoff. Threshold: within 5% for framing, drywall, doors and hardware, and ceilings; within 10% for other trades | Framing 3%, drywall 4%, doors and hardware 2%, ceilings 6%; MEP fixture counts 18%; demolition 15%. Renovations averaged 11% error against 4% for new tenant improvements, because the tool counts new work but misses existing conditions | **No** for ceilings, MEP, demolition, and renovations |
| Safe | No bid leaves without the Project Manager's verification and the Owner's approval | 12 of 12 bids reviewed; one missed ceiling demolition in an occupied clinic was caught at the Owner's review | Yes |
| Secure and resilient | Vendor security evidence; MFA; access limited to the enrolled user | Vendor has a SOC 2 Type 1 report only (design, not operating effectiveness); local account with a password; MFA available but off | **Partial** |
| Accountable and transparent | Each AI-derived figure in an estimate is tagged with its source (AI takeoff, past estimate, vendor market data) | No tagging; figures are pasted into the estimate spreadsheet | **No** |
| Explainable and interpretable | The estimator can see what the model counted on each sheet | Takeoff overlays show counted items; pricing suggestions do not show their basis | Partial |
| Privacy-enhanced (confidentiality) | No training on company data; deletion within 30 days of request; US data location; no cross-customer pricing features | Click-through terms allow model improvement; no deletion commitment; a "market pricing insights" feature is on by default | **No** |
| Fair, with harmful bias managed | Quote comparison recommendation rate for each subcontractor group divided by the rate for all others, among quotes within 5% of the low price. Groups: firms not on the vendor's subcontractor network, certified small disadvantaged and women-owned firms (where known), and firms new to the company. Flag any ratio below 0.8. This heuristic is borrowed from employment selection practice; it is not a legal threshold for subcontracting | **Firms not on the vendor's network: 0.58.** Firms new to the company: 0.74. Certified groups: only 9 quotes, too few to measure | **No.** Disparity flagged |

**Bias finding.** The quote comparison weights a "network reliability score" built from the vendor's own subcontractor network. Firms that are not on the network get no score, and the model treats that as a poor score. Most of the company's local subcontractors are small firms that never joined the network, so the tool steadily pushes them down. That narrows the company's subcontractor base and works against the small local firms the company relies on. It is a data problem (missing values), not a certification-status input. The fix is to turn the score off or treat missing scores as neutral, and to show the price-and-scope comparison on its own.

## 5. MANAGE
**Human-in-the-loop design:**
- The tool produces drafts only.
- The Project Manager verifies every takeoff for the 5 largest cost items against the drawings. MEP, demolition, and existing-conditions work are taken off manually until the tool meets the accuracy threshold for two quarters.
- Quote comparison is advisory. The Project Manager records the reason for each subcontractor selection in the bid file.
- The Owner approves every bid and, on a federal bid, signs the price certification only after confirming that no pooled market pricing was used.
- The Owner can stop use of the tool at any time; the Project Manager can always estimate without it (P05 BP-04 workaround).

**Monitoring:**
- Quarterly accuracy review by trade and project type, tracked in the risk register (R-010).
- Quarterly bias check of recommendation ratios, until enough quotes exist for each group.
- Wrong outputs are noted in the bid file and reviewed at the monthly POA&M meeting.

**Incident handling:**
- A vendor security incident or a change in data use follows P08 and the notice terms once signed.
- A material estimating error in a submitted bid goes to the Owner and counsel before award.

**Decommissioning:**
- If enterprise terms are not signed by 2026-10-15, stop federal uploads for good, ask the vendor in writing to delete FC-1 files, and keep the vendor's confirmation.
- Stop use if the accuracy thresholds are still missed after two quarters.
- Stop use if the vendor enables cross-customer pricing features that cannot be turned off.

## 6. Decision
**Approve with conditions.** Owner and President, 2026-08-31. The trial may continue for the Project Manager **only if** these conditions are met:
1. **Now:** no uploads of documents from awarded federal contracts (FCI) until enterprise terms are signed (POAM-003). The terms must bar training on company data, require deletion within 30 days of request, keep data in the US, and support MFA. Due 2026-10-15. The vendor is asked in writing to delete the FC-1 files already uploaded.
2. **Now:** the "market pricing insights" feature is turned off, and counsel confirms in writing before the DoD bid that no pooled competitor pricing reaches a federal bid (FAR 52.203-2; P01 R-023).
3. **Now:** manual takeoffs for MEP, demolition, and existing conditions on every renovation.
4. By 2026-09-15: MFA on the tool account.
5. By 2026-10-31: the network reliability score is turned off or treated as neutral, and the bias check is rerun.
6. By 2026-11-30: source tagging for AI-derived figures in estimates.
7. Owners' drawings are uploaded only where the owner's contract allows sharing with service providers. Nothing from the hospital system is uploaded without its written agreement.
8. Before any DoD award with DFARS 252.204-7021: the tool is either inside the CMMC Level 1 scope with evidence, or it never receives FCI.

Any second user, or any use beyond the 4 purposes in section 2, requires a new assessment and two consecutive quarters meeting the accuracy thresholds with no open bias flag.

**AI-002 (public chatbots).** Prohibited for FCI, Restricted, and Confidential information (POL-04 4.6). The Office Manager will check whether the productivity suite's built-in AI assistant can be enabled under the suite's existing terms as the approved alternative, and will assess it before anyone uses it.
