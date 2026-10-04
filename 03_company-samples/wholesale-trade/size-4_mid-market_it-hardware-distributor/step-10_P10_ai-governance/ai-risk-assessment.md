# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed IT hardware and software wholesale distributor) |
| Tier / Vertical | Mid-Market / Wholesale Trade |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. AI-001, demand forecasting and automated reordering, is assessed in depth |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook, with the Generative AI Profile (NIST AI 600-1) for AI-002 and AI-003 |
| Assessors / date | vCISO and Security Manager (security), Director of Inventory Planning and Vice President of Supply Chain (AI-001), HR Director with General Counsel (AI-005), 2026-08-24 to 2026-09-10 |
| Decision | Chief Operating Officer, 2026-09-17; the High-tier decision on AI-005 noted by the CEO |

## 1. Summary
Four of the five tools were adopted by departments without a security, legal, or data review (gap 10). None is out of control, but three need conditions now:
- **AI-001 forecasting and automated reordering** has released purchase orders automatically since 2026-02. Its supplier choice can pick brokers, and the Section 889 and FASCSA screens do not apply to the orders it creates.
- **AI-005 resume screening** rejects applicants automatically. A preliminary check found a knockout question with adverse impact by sex.
- **AI-003 portal chatbot** was never tested for leaks of one reseller's data to another.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Demand forecasting and automated reordering | Medium, with elevated controls | Approve with conditions; auto-release narrowed |
| AI-002 | Enterprise generative AI assistant | Low | Approve with data rules |
| AI-003 | Reseller portal chatbot | Medium | Approve with conditions |
| AI-004 | Invoice capture and payment anomaly scoring | Medium | Approve with conditions (advisory only) |
| AI-005 | Resume screening for hourly DC roles | High | Screen-out suspended; ranking continues with human review |

Tiers: 1 High, 3 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** the vCISO, with a business owner for each use case (inventory).
- **Policies:** POL-01 4.16 (approval before use); POL-04 4.2 and 4.8 (no CUI in AI tools; Confidential data only in approved tools); POL-05 4.8 (approved tools, output checks); STD-05 AI use standard (due 2026-12-31).
- **Approved-tools list:** kept by the Security Manager; lists AI-001 to AI-005 with their conditions. Public chatbots are blocked on company devices and the enclave.

### 2.1 Lightweight governance process for a mid-market company
A company of 850 people does not need a standing AI committee with a large charter. It needs a short gate and a monthly rhythm that reuse existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | One-page request for any AI tool or AI feature turned on in an existing tool: purpose, users, data, vendor, decisions affected | Business owner | 15 minutes |
| 2. Triage | Provisional tier with the repository rubric; purchasing gate (no purchase order or feature activation without approval) | Security Manager | 2 business days |
| 3. Review | Low: security checklist. Medium: security, data and contract terms, business reviewer. High: full MAP and MEASURE assessment with counsel and a bias testing plan | Security Manager; General Counsel; business reviewer | 1, 2, or 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the AI review group (vCISO, General Counsel, Vice President of Supply Chain or the relevant business leader), 30 minutes monthly. High: the group recommends; the COO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owners report agreed metrics monthly; High tier gets a quarterly deep dive; incidents follow P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type, new population, or an incident | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. The rubric is defined by this repository, not by any regulation.

## 3. MAP
### 3.1 AI-001 Demand forecasting and automated reordering (in depth)
| Item | Description |
|---|---|
| Purpose | Forecast weekly demand for about 68,000 SKUs and create purchase orders (quantity, date, supplier). Replenishment lines up to $25,000 are released to suppliers automatically; larger lines go to buyers |
| Users and operators | About 30 buyers; the Director of Inventory Planning tunes settings |
| Affected parties | Resellers (fill rates and back orders), suppliers, federal channel customers, and, through the products, DoD programs. No decisions about individual people |
| Data | 3 years of ERP order history **including federal channel orders (FCI)**; reseller account identifiers; inventory; supplier lead times and prices; the approved supplier list **including the 31 brokers** |
| Build or buy | Buy (SaaS connected to the ERP, SYS-15); the vendor trains a model per customer |
| Not intended | Customer pricing, allocation of scarce stock among customers, and FIL or DoD job sourcing. Enabling any of these requires re-assessment |

### 3.2 Other use cases
| Item | AI-002 Assistant | AI-003 Portal chatbot | AI-004 AP anomaly scoring | AI-005 Resume screening |
|---|---|---|---|---|
| Purpose | Drafting and summarizing | Order status, product and compatibility answers | Extract invoice data; score payment risk | Rank and screen applicants for hourly DC roles |
| Users | All staff after training | About 9,600 reseller users | 8 AP staff | 3 recruiters |
| Affected people | None directly | Reseller staff | Suppliers (businesses) | About 4,300 applicants since 2026-01 |
| Data | Internal and Confidential | Catalog; the signed-in account's orders | Invoices; bank details | Resumes; knockout answers |
| Generative AI? | Yes | Yes | No | No (ranking model and rules) |

### 3.3 Applicable laws and rules
| Rule | Applies to | Why |
|---|---|---|
| FAR 52.204-21 and CMMC Level 1 (N42-R04, N42-R02) | AI-001 | The vendor processes FCI from federal channel orders without FAR 52.204-21 terms. Fix: filter federal orders from the feed by 2026-10-15 (also P03 G-113) |
| FAR 52.204-25 (N42-R05), FAR 52.204-30, DFARS 252.246-7008 | AI-001 | Auto-released purchase orders choose suppliers. The sourcing order and covered-equipment screening must apply to every order the platform creates |
| DFARS 252.204-7012 and SP 800-171 (N42-R03) | AI-002, AI-003 | CUI must never enter an AI tool; the enclave blocks external AI services |
| FTC Act Section 5 (N42-R01) | AI-002, AI-003, AI-001 vendor claims | Product and compatibility statements to resellers must be accurate; vendor accuracy claims relied on in procurement are kept on file |
| Title VII (42 U.S.C. 2000e-2(k)) and the Uniform Guidelines on Employee Selection Procedures (29 CFR 1607) | AI-005 | A selection procedure with adverse impact must be job related and consistent with business necessity. Under 29 CFR 1607.4(D), a selection rate for a race, sex, or ethnic group below four-fifths of the highest group's rate is generally regarded as evidence of adverse impact |
| ADA reasonable accommodation in the application process | AI-005 | Applicants must have a way to request an accommodation, for example for online knockout questions |
| State AI laws in `00_universal-framework/cross-sector/` (for example Colorado SB26-189) | None today | The company has no employees or applicants in Colorado; warehouse hiring is in Florida, and this assessment found no Florida AI hiring statute. Revisit if hiring expands to other states |
| CCPA/CPRA automated decision-making rules (N42-R08) | None today | No California business (facts section 1); revisit with the West Coast expansion (R-048) |

## 4. Risk tier
- **AI-001: Medium, with elevated controls.** Under the rubric it is Medium: it makes business decisions, not decisions about people. But auto-release removes the human from purchase decisions that can route spend to brokers or covered manufacturers, so the company applies controls normally reserved for High tier: pre-release testing, monthly monitoring, and a kill switch. **Re-tier to High** if it is used for FIL or DoD job sourcing.
- **AI-002: Low** with the approved enterprise tool and the data rules.
- **AI-003: Medium.** It interacts directly with customers; a human answers anything it cannot.
- **AI-004: Medium.** It influences payment decisions; humans approve every payment.
- **AI-005: High.** It is a substantial factor in an employment decision.

## 5. MEASURE
### 5.1 AI-001 (production data 2026-03 to 2026-08)
| Trustworthy characteristic | Test / metric and threshold | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Weighted absolute percentage error (WAPE) at a 4-week horizon for A-class SKUs; 30% or less overall and per product line | Overall 21%; networking 17%; **video surveillance 38%** | **No** (one line) |
| Safe (supply chain integrity) | Auto-released lines that name a supplier outside authorized sources: 0 | 312 of 41,200 auto-released lines (0.8%) went to brokers, including 4 to BRK-17 (R-051) | **No** |
| Safe (covered equipment) | Auto-released lines for SKUs without a manufacturer of record: 0 | 9 lines (none on federal orders) | **No** |
| Secure and resilient | SSO with MFA; vendor SOC 2 | 6 local accounts without MFA; vendor SOC 2 Type 2 unqualified (P09 VEN-08) | Partial |
| Accountable and transparent | Every auto-release logged with the model version and the rule that allowed it | Logged; model version not recorded | Partial |
| Explainable and interpretable | Buyers can see forecast drivers per SKU | Available | Yes |
| Privacy-enhanced (data protection) | No FCI in the feed; vendor uses data only for the company's model | Federal orders in the feed; vendor terms allow "service improvement" use | **No** |
| Fair, with harmful bias managed | Fill rate by customer segment (top-50 resellers, small resellers under $250,000 a year, federal channel); flag a gap of more than 3 points from the best segment | Top-50 97%; federal 96%; **small resellers 92%** | **No** |

**Bias finding.** The model learns from order volume, so SKUs bought mostly by small resellers are under-forecast and stock out more often, even though commercial terms treat small resellers the same. Fix: minimum safety stock for sparse-history SKUs and monthly fill-rate reporting by segment; target gap of 3 points or less by 2027-03-31.

### 5.2 Other use cases
| Use case | Characteristic | Test and threshold | Result | Pass? |
|---|---|---|---|---|
| AI-002 | Valid and reliable (confabulation, AI 600-1) | 20 AI-drafted product descriptions against OEM spec sheets; 0 errors published | 3 drafts had wrong specifications; all caught in review | Yes (with review) |
| AI-003 | Privacy-enhanced | Cross-account leakage red-team test: 0 leaks | Not yet run (due 2026-11-15) | **Not tested** |
| AI-003 | Valid and reliable | 50 scripted compatibility questions; 0 wrong answers without a handoff | 2 wrong answers without handoff | **No** |
| AI-004 | Valid and reliable | Duplicate and altered-invoice detection on a seeded test set | 18 of 20 detected; the 2026-02 spoofed bank change was not flagged (call-back stopped it) | Advisory only |
| AI-005 | Fair, harmful bias managed | Four-fifths comparison of selection rates by sex and by race and ethnicity from voluntary self-identification (29 CFR 1607.4(D)) | The "available for all shifts" knockout gives women a selection rate 0.76 of men's; race and ethnicity results inconclusive (incomplete self-identification) | **No** |
| AI-005 | Accountable and transparent | Every screen-out reviewed by a recruiter; accommodation route on the application | No review of screen-outs; no accommodation route | **No** |

## 6. MANAGE
**Human-in-the-loop design:**
- **AI-001:** auto-release is limited, from 2026-10-31, to authorized-source suppliers and SKUs that pass manufacturer-of-record, Section 889, and FASCSA screening; brokers are removed from the supplier pool the platform can pick. Buyers review all other suggestions and sample 50 auto-released lines a month. Auto-release is never used for FIL or DoD job stock.
- **AI-002:** users check every output; product claims are checked against OEM spec sheets.
- **AI-003:** account-scoped retrieval; pricing answers link to the portal price; handoff to customer service on request or low confidence.
- **AI-004:** advisory only; call-back and dual approval stay mandatory (R-010, R-031).
- **AI-005:** no automatic rejection; a recruiter reviews every screen-out and every ranked list; the shift-availability knockout is replaced by a scheduling conversation; an accommodation request link is added.

**Monitoring:** owners report section 5 metrics monthly to the AI review group; AI-001 and AI-005 also get a quarterly deep dive. Results feed the risk register (P01 R-026 to R-032).

**Incident handling:**
- An auto-released order to a blocked supplier, or for a covered or unscreened SKU, is a supply chain incident under the P08 supplier compromise runbook.
- A vendor security incident follows P08 and the vendor's notice terms.
- A chatbot disclosure of another reseller's data is a security incident under POL-03 and a reseller contract notice event.

**Decommissioning criteria:**
- AI-001: turn off auto-release if any order to a blocked supplier is released, if WAPE exceeds 40% for two months, or if the vendor changes its data-use terms; fall back to the ERP reorder report.
- AI-003: switch off if the red-team test finds any cross-account leak.
- AI-005: keep screen-out off unless the adverse impact analysis and job-relatedness review support it.

## 7. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | Approve with conditions | Federal orders filtered from the feed by 2026-10-15; auto-release limited to authorized sources and screened SKUs by 2026-10-31; SSO with MFA by 2026-11-30; model version logging by 2026-12-31; small-reseller fill-rate gap 3 points or less by 2027-03-31 | Chief Operating Officer, 2026-09-17 |
| AI-002 | Approve | Training before access; no CUI or FCI; Confidential data only in this tool | Chief Operating Officer, 2026-09-17 |
| AI-003 | Approve with conditions | Red-team test by 2026-11-15; handoff fix for compatibility answers by 2026-10-31 | Chief Operating Officer, 2026-09-17 |
| AI-004 | Approve with conditions | Documented as advisory; AP procedure updated by 2026-10-31 | Chief Operating Officer, 2026-09-17 |
| AI-005 | Screen-out suspended 2026-09-10; ranking continues with human review | Adverse impact analysis and job-relatedness review with counsel by 2026-11-30; accommodation route by 2026-10-15; re-decision by the COO after the analysis | Chief Operating Officer, 2026-09-17 (noted by the CEO) |

These conditions are tracked as POAM-025 in P07.
