# AI Use Assessment: AI Estimating and Bid Assistant (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (commercial and institutional building general contractor) |
| Tier / Vertical | Sole Proprietorship / Construction |
| AI use case | AI-001: AI estimating and bid assistant, an individual subscription (SYS-09) used since March 2026 for about 20 bids and change orders |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; AI 600-1 for generative AI risks |
| Assessor and decision | Owner, 2026-08-24; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (1 use case) |

## 1. What it does (Map)
The owner uploads drawings and specifications. The tool counts quantities (doors, fixtures, wall area, flooring), suggests unit prices from its own market data, and drafts the proposal letter. The owner copies the results into the estimate spreadsheet. It is an individual plan accepted by click-through. Until 2026-07-17 the setting "use my content to improve the service" was on (the default). In June 2026 the owner uploaded **FC-1 change-order drawings**, which are FCI.

**Is the data FCI?** Public solicitation documents are not FCI: FAR 52.204-21(a) excludes "information provided by the Government to the public". Drawings and change-order packages on the **awarded** FC-1 contract are FCI. Private clients' drawings are not FCI, but most client contracts make them confidential.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| FAR 52.204-21(b)(1)(iii) | **Yes** for FCI | The owner must "verify and control/limit connections to and use of external information systems". Uploading FCI under terms that allow model training fails this (P03 G-003) |
| DFARS 252.204-7021(d)(2) | **Yes** once the DoD subcontract is signed | FCI may be processed only on systems with the required CMMC status. The tool will not be in the Level 1 scope, so it must never receive DoD FCI (P03 G-024) |
| Client contract confidentiality clauses | Yes | Private drawings were uploaded under the same terms |
| State AI laws on consequential decisions | No | The tool makes no decision about a person (employment, credit, housing, and similar). The company works only in Florida |

## 3. Risk screen (repository rubric)
**Tier: Medium.** The tool influences business decisions (what the company bids and at what price), and it handles regulated data (FCI). It is not High: it makes no decision about a person and does not affect physical safety, because the owner decides every quantity and price. It is not Low, because it touches FCI and a bad quantity can lock the company into a losing fixed price.

**Re-tier to High and re-assess if** the tool is used for structural, fire protection, or other life-safety quantities, or to choose subcontractors automatically.

## 4. Data-sharing rules (Govern)
1. No FCI and no private client drawings go to the tool unless its business terms bar training on company data, allow deletion on request, and support MFA (POL-01 6.1, 9.6).
2. Never upload anything from the DoD subcontract, whatever the terms.
3. Public solicitation documents and the owner's own past prices may be used now, with model improvement turned off.

## 5. Accuracy check and human review (Measure and Manage)
Back-test on 3 completed jobs (dental build-out, church hall, one retail repair), comparing the tool's takeoff with the owner's final takeoff:

| Item | Result | Acceptable? |
|---|---|---|
| Drywall, paint, and flooring areas | Within 4% | Yes (threshold 5%) |
| Doors, hardware, and plumbing fixture counts | 9% off on average; missed items on revised sheets | **No** |
| Renovation demolition quantities | 18% off | **No** |
| Suggested unit prices vs local subcontractor quotes | 12% to 20% below quotes | **No** for pricing; use only as a sanity check |
| Proposal letter drafts | Two drafts listed exclusions the owner had not chosen | Usable only after a full read |

**Human review rules:** the owner checks every count against the drawings and every price against a real subcontractor quote; demolition and fixture counts are done by hand; the owner reads the whole proposal letter before it goes out. The tool never submits a bid. No fairness test is needed today because the tool makes no decision about people; one would be needed before any use to rank subcontractors.

## 6. Decision: approve with conditions (2026-08-31)
1. **Done 2026-07-17:** model improvement turned off.
2. **By 2026-09-15:** written request to the vendor to delete the FC-1 change-order drawings and all private client drawings; keep the reply (POAM-004, P01 R-009).
3. **Until business terms are in place:** public bid documents and the owner's own data only.
4. **By 2026-10-31:** decide whether to move to the vendor's business plan (no training, deletion on request, MFA) or stop using the tool for client drawings.
5. Accuracy re-checked on the next 3 bids; if counts are still more than 5% off, use the tool for area takeoffs only.
