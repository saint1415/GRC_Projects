# AI Risk Assessment: AI Estimating and Bid Assistant

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor) |
| Tier / Vertical | Small / Construction |
| AI use case | AI-001: AI estimating and bid assistant, pilot with 4 estimators since May 2026 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | Director of Preconstruction with the IT Manager and Contracts Administrator, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** Director of Preconstruction. **Decision authority:** CFO (Medium tier); the President if re-tiered High.
- **Policies that apply:**
  - POL-01 4.8: vendors that hold FCI or Restricted data need a security review and terms that bar training on company data
  - POL-04 4.3 and 4.7: FCI stays inside the assessed boundary; no FCI, Restricted, or Confidential data in unapproved AI tools
  - POL-05 4.9: approved tools only
- **Approved-tools list:** kept by the IT Manager. Today it lists AI-001 only, only for the 4 enrolled estimators, and only under the conditions in section 6.
- **Scale for a Small company:** there is no AI committee. The Director of Preconstruction, IT Manager, Contracts Administrator, and CFO review AI use cases quarterly.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Speed up estimating: (1) quantity takeoff from drawings; (2) unit pricing from the company's historical cost database and the vendor's market data; (3) subcontractor bid leveling (normalizing scope, flagging exclusions, ranking bids); (4) drafting proposal narratives |
| Users / operators | 4 estimators; the Director of Preconstruction reviews output |
| Affected parties | Owners (the price they pay), subcontractors (whether they are selected, including small and disadvantaged businesses), the company (fixed-price exposure) |
| Data | Inputs: drawings and specifications, historical costs, subcontractor bid forms. Outputs: quantities, unit prices, leveled bid tables, recommendations, draft text. **Standard vendor terms allow customer data to be used to improve models** |
| Build or buy | Buy: vendor SaaS with a connector to the estimating database (read-only) |
| Not intended | Submitting bids automatically; selecting subcontractors without an estimator's documented decision; producing certified cost or pricing data without human verification; any hiring, discipline, or crew-assignment use; structural or life-safety quantities |

**Is the data FCI?** It depends on the stage.
- Public solicitation documents posted for all bidders are *not* FCI. FAR 52.204-21(a) excludes "information provided by the Government to the public".
- Drawings and change-order packages on an **awarded** federal contract *are* FCI. Estimators uploaded FC-2 change-order drawings in June and July 2026. That put FCI on an external system the company does not control (P03 G-003, G-024).

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FAR 52.204-21(b)(1)(iii) | **Yes** for FCI | The company must "verify and control/limit connections to and use of external information systems". Uploading FCI under consumer-style terms fails this |
| DFARS 252.204-7021(d)(2) | **Yes** once a DoD contract with the clause is awarded | FCI may be processed only on systems with the required CMMC status. The tool must either be in the Level 1 scope or never receive FCI |
| FAR 52.203-2, Certificate of Independent Price Determination | **Yes** on federal bids | The offeror certifies prices were arrived at "without ... any consultation, communication, or agreement with any other offeror or competitor" about prices or "the methods or factors used to calculate the prices". A vendor feature that pools competitors' pricing into shared "market" suggestions puts that certification at risk |
| FAR 15.403-4 (certified cost or pricing data) | **When required** | For negotiated actions above the threshold in FAR 15.403-4, the company certifies that data are accurate, complete, and current. AI-derived figures need traceable sources |
| FAR 52.219-8, Utilization of Small Business Concerns | **Yes** on federal jobs | It is federal policy that small, veteran-owned, service-disabled veteran-owned, HUBZone, small disadvantaged, and women-owned small businesses have "the maximum practicable opportunity" to participate in subcontracts. The contractor agrees to carry out this policy (52.219-8(b), (d)). A ranking model that disfavors such firms works against that commitment |
| Sherman Act Section 1 (15 U.S.C. 1) | Indirectly | Bid rigging and price-fixing are illegal. Counsel reviews any vendor feature that shares or aggregates pricing across contractors |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. The claims the company relied on are kept in the procurement file |
| State AI laws (e.g., Colorado SB26-189) | No | The company operates in Florida, and AI-001 does not make consequential decisions about individuals. Out of scope by decision (`../00_company-facts.md`) |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why not High:** AI-001 does not make, and is not a substantial factor in, a consequential decision about a person, and it does not affect physical safety. An estimator decides every quantity used in a bid and every subcontractor selection, and the Director of Preconstruction approves every bid.

**Why not Low:** it influences multi-million-dollar business decisions and subcontractor selection. It processes FCI and third parties' confidential pricing, and its errors can lock the company into a losing fixed price.

**Escalation triggers (re-tier to High and re-assess):**
- automatic bid submission or automatic subcontract award
- use for hiring, discipline, or crew assignment (employment)
- use for structural, fire protection, or other life-safety quantities
- enabling any feature that pools pricing across the vendor's customers

## 4. MEASURE
Pilot test: back-test on 10 completed bids (5 public federal solicitations, 5 private), plus live monitoring of 38 bid packages (212 subcontractor bids) from May to August 2026.

| Trustworthy characteristic | Test / metric | Result (pilot) | Pass? |
|---|---|---|---|
| Valid and reliable | Takeoff quantity error by trade versus the estimator's final takeoff. Threshold: within 5% for concrete, steel, and drywall; within 10% for other trades | Concrete 3%, drywall 4%, steel 5%; MEP fixture counts 14%, sitework 11%. Renovation projects averaged 12% error against 4% for new construction | **No** for MEP, sitework, and renovations |
| Safe | No bid leaves without estimator verification and Director approval | 100% of pilot bids reviewed; one sitework quantity error caught at review | Yes |
| Secure and resilient | Vendor security report; single sign-on and MFA; access limited to enrolled users | Vendor has a SOC 2 Type 1 report only (design, not operating effectiveness); local accounts, MFA optional and off; estimators hold administrator rights | **Partial** |
| Accountable and transparent | Each AI-derived figure in an estimate is tagged with its source (AI takeoff, cost database, vendor market data) | No tagging today; figures are pasted into the estimate spreadsheet | **No** |
| Explainable and interpretable | Estimator can see what the model counted on each sheet | Takeoff overlays show counted items; pricing suggestions do not show their basis | Partial |
| Privacy-enhanced (confidentiality) | No training on company data; deletion within 30 days; US data location; no cross-customer pricing features | Standard terms allow model improvement; no deletion commitment; a "market pricing insights" feature is on by default | **No** |
| Fair, with harmful bias managed | Bid leveling recommendation rate for each subcontractor group divided by the rate for all others, among bids within 5% of the low price. Groups: certified small disadvantaged, women-owned, HUBZone, service-disabled veteran-owned, and first-time bidders to the company. Flag any ratio below 0.8. This heuristic is borrowed from employment selection practice; it is not a legal threshold for subcontracting | Certified small business groups: 0.88 to 0.95. **First-time bidders: 0.55** | **No.** Disparity flagged |

**Bias finding.** The ranking weights the company's "historical performance" score. First-time bidders have no history, and the model treats missing history as poor history. That systematically pushes new firms down, and many new firms are small or disadvantaged businesses. This works against the FAR 52.219-8 policy on federal jobs and narrows the company's subcontractor base on every job. It is a data problem (missing values), not a certification-status input. The fix is to score missing history as neutral and to show estimators the price-only ranking beside the model's ranking.

## 5. MANAGE
**Human-in-the-loop design:**
- The tool produces drafts only.
- An estimator must verify every takeoff for concrete, steel, drywall, MEP, and sitework against the drawings. MEP and sitework must be taken off manually until the tool meets the accuracy threshold for two quarters.
- Bid leveling is advisory. The estimator records the reason for each subcontractor selection in the bid file.
- The Director of Preconstruction approves every bid and signs the federal price certification only after confirming that no pooled market pricing was used.
- AI-derived figures used in federal change-order pricing must be tagged with their source records before submission (FAR 15.403-4 where applicable).

**Monitoring:**
- Quarterly accuracy review by trade and project type, tracked in the risk register (R-012).
- Quarterly bias check of recommendation ratios.
- Estimators report wrong outputs to the Director through the estimating issue log.

**Incident handling:**
- A vendor security incident or a data-use change follows P08 and the contract notice terms.
- A material estimating error in a submitted bid is escalated to the CFO and counsel before award.

**Decommissioning:**
- Stop federal-contract uploads permanently and export or delete company data if enterprise terms are not signed by 2026-10-15.
- Stop use if the accuracy thresholds are still missed after two quarters.
- Stop use if the vendor enables cross-customer pricing features that cannot be turned off.

## 6. Decision
**Approve with conditions.** CFO, 2026-08-31. The pilot may continue for the 4 enrolled estimators **only if** these conditions are met:
1. **Now:** no uploads of documents from awarded federal contracts (FCI) until enterprise terms are signed (POAM-010). The terms must bar training on company data, require deletion within 30 days of request, keep data in the US, and support single sign-on with MFA. Due 2026-10-15.
2. **Now:** the "market pricing insights" feature is turned off, and counsel confirms in writing that no pooled competitor pricing reaches federal bids (FAR 52.203-2).
3. **Now:** manual takeoffs for MEP and sitework, and for all renovation projects.
4. By 2026-10-31: missing performance history is scored as neutral, and the bias check is rerun.
5. By 2026-11-30: source tagging for AI-derived figures in estimates.
6. Before any DoD award with DFARS 252.204-7021: the tool is either inside the CMMC Level 1 scope with evidence, or technically blocked from receiving FCI.

Expansion beyond 4 estimators requires two consecutive quarters meeting the accuracy thresholds and no unresolved bias flag.

**Related action for AI-003.** The jobsite camera vendor's PPE detection feature stays off. If operations wants it, it needs its own assessment first. Used for discipline, it would be an employment use and rate High.
