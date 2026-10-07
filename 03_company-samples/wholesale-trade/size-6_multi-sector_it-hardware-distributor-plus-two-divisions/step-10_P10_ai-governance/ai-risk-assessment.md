# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (IT Distribution, Logistics, Online Retail, corporate) |
| Tier / Vertical | Multi-Sector / Wholesale Trade |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the rules that apply to the priority use cases: demand forecasting and automated reordering (AI-001, registry default), DC labor management (AI-005), and the Online Retail customer-facing models (AI-002, AI-004) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1) for AI-004 and AI-009, and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27; presented to the board audit and risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (10 use cases: 1 High, 7 Medium, 2 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board audit and risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Group supply chain risk director, Group HR director, and one leader from each division. Approves High-tier use cases, the approved-tools list, and automation thresholds |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (prompt injection, model and data supply chain, data leakage) |
| Group Chief Privacy Officer | Personal information, CCPA risk assessments and ADMT rules |
| Group CMMC program director | Keeps CUI out of AI tools; FCI only in tools whose terms meet FAR 52.204-21 |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-05, under POL-01 4.16)
1. **Register before use.** Every AI use case that makes or influences purchasing, pricing, customer, worker, or seller decisions, or that processes CUI, FCI, cardholder data, or personal information, is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: the council approves, a pre-deployment impact assessment and bias testing are required, and monitoring is reported quarterly.
3. **Data rules.** No CUI in any AI tool; FCI only in tools whose terms carry FAR 52.204-21 safeguards; no cardholder data; personal information only in tools approved for it (POL-04 4.11).
4. **Supply chain rules apply to machines too.** Automated purchasing must follow the same sourcing order, covered-manufacturer block, and supplier risk status as a buyer (POL-01 4.10, 4.11).
5. **Automation thresholds.** Any decision an AI system makes without human review needs a council-approved threshold, a kill switch, and monitoring.
6. **Change gate.** A new model, new data source, new decision role, or raised threshold triggers re-assessment before release.
7. **Approved tools only** for workforce generative AI (POL-05 4.7).

**Where the program fell short in 2026.** The standard was adopted after AI-001's automatic release went live (2026-02-02) and after Logistics expanded AI-005's task allocation. Neither had been assessed. Both are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Demand forecasting and automated reordering | IT Distribution (buys for Online Retail too) | Medium | In production with conditions |
| AI-002 | Checkout fraud screening | Online Retail | Medium | In production |
| AI-003 | Recommendations and personalized promotions | Online Retail | Medium | In production |
| AI-004 | Customer service generative AI assistant | Online Retail | Medium | In production |
| AI-005 | DC labor management (productivity scores, task allocation) | Logistics | High | In production; expansion paused |
| AI-006 | Route and load optimization | Logistics | Medium | In production |
| AI-007 | Marketplace seller risk and counterfeit listing detection | Online Retail | Medium | In production |
| AI-008 | Receiving packaging inspection (computer vision) | Logistics | Medium | Pilot at DC-1 |
| AI-009 | Enterprise generative AI assistant | Group | Low | Pilot (3,000 users) |
| AI-010 | Coding assistant | Online Retail | Low | Approved |

### 2.1 AI-001 demand forecasting and automated reordering (priority use case)
| Item | Description |
|---|---|
| Purpose | Forecast weekly demand for about 310,000 SKUs and release purchase orders so buyers keep fill rates high without overstock. One purchasing team buys for IT Distribution and Online Retail |
| Users | About 260 buyers; the data science team maintains the models |
| Automation | Since 2026-02-02, orders under $250,000 to suppliers flagged as authorized sources release automatically. About 14,300 orders (about $610 million) released this way through 2026-07-31 |
| Data | Three years of order history **including DoD orders (FCI)**; supplier lead times, prices, and approved-supplier status; demand from both selling divisions. No personal information about individuals |
| Build or buy | Build: models on the group data platform (SYS-G6), releasing through the ERP |
| Not intended | Customer pricing, allocation of scarce stock among customers, sourcing for federal integration jobs, and orders to non-authorized sources. Enabling any of these requires re-assessment |

| Rule | Applies? | What it means for AI-001 |
|---|---|---|
| FAR 52.204-21 (N42-R04) | **Yes** | The training feed holds FCI from DoD orders. The group data platform meets the safeguards, but model artifacts are exported to a vendor-hosted experiment tracker without FAR 52.204-21 terms. Fix: remove DoD orders from the feed, or keep all artifacts inside the platform (ID-021) |
| FAR 52.204-25 (N42-R05) | **Yes** for federal-eligible stock | Automated orders for SKUs sold to federal customers must not buy covered equipment. The block keys on the manufacturer of record, which is blank for about 1,900 SKUs (POAM-009) |
| DFARS 252.246-7008 (prime subcontracts) | **Yes** for stock that may go to integration jobs | The authorized-source filter is the machine version of the sourcing order. It must also read supplier risk status, not only authorization status (see the Supplier K finding below) |
| FTC Act Section 5 (N42-R01) | Indirectly | Applies to claims the group makes about availability to customers and to vendor claims relied on |
| CCPA ADMT rules and Colorado SB26-189 | No | AI-001 makes no decision about an individual and no decision in a covered category |
| SEC Reg S-K Item 106 | Indirectly | AI governance is part of the cyber risk management description in the annual report |

### 2.2 AI-005 DC labor management (High)
| Rule | What it means |
|---|---|
| Repository rubric | Scores and task allocation are a substantial factor in employment decisions (coaching, discipline, work assignment), so the tier is **High** regardless of which laws apply |
| Title VII disparate impact | Liability exists by statute even though EEOC enforcement is deprioritized (cross-sector file). The Uniform Guidelines treat a selection rate below four-fifths of the highest group's rate as general evidence of adverse impact (29 CFR 1607.4(D)); the group uses that as a screening threshold for coaching flags |
| CCPA ADMT rules | "Allocation or assignment of work" is a significant decision under the CPPA definition. They would apply to California employees; no DC workers are in California today. Re-check before any California site |
| Colorado SB26-189 (effective 2027-01-01) | Covers ADMT that materially influences employment decisions. No workers are in Colorado today; re-check before any Colorado site. Its status is unsettled (litigation and federal preemption efforts; see `00_universal-framework/cross-sector/us-cross-sector-obligations.md`) |
| State warehouse quota and labor laws | Some states regulate productivity quotas in warehouses. They were **not analyzed in this sample**; Group HR and counsel must review each DC state before quotas are tied to scores |

### 2.3 Online Retail customer-facing models (AI-002, AI-003, AI-004, AI-007)
| Rule | Use cases | Implication |
|---|---|---|
| FTC Act Section 5 (N44-45-R02) | All | No deceptive AI claims; disclose that the assistant is AI; fraud declines must not rest on unfair practices |
| CCPA risk assessments (Cal. Code Regs. tit. 11, 7150(b)(1)-(2)) | AI-003 | Sharing for cross-context behavioral advertising and precise geolocation in the app require risk assessments (pre-existing processing by 2027-12-31) |
| CCPA ADMT rules | AI-002 | Counsel concluded on 2026-07-28 that order fraud screening is not a "significant decision" (the defined categories are financial or lending services, housing, education, employment, and health care). Re-check if the division ever offers credit or payment plans |
| INFORM Consumers Act (N44-45-R08) | AI-007 | Model scores may prioritize review, but suspension follows the Act's notice and 10-day opportunity (15 U.S.C. 45f(a)(1)(C)); data collected only for the Act may not feed other models (45f(a)(3)) |
| PCI DSS (N44-45-R01) | AI-004 | No card data in chat; the assistant cannot take payments |

## 3. Risk tiers (repository rubric)
- **High:** AI-005 (substantial factor in employment decisions about DC workers).
- **Medium:** AI-001, AI-002, AI-003, AI-004, AI-006, AI-007, AI-008. They influence business decisions or interact with customers, and a human makes, or can stop, final decisions about individuals.
- **Low:** AI-009, AI-010.

**Why AI-001 is Medium even though some orders release without review.** The rubric's High criteria concern consequential decisions about people and safety or critical infrastructure. AI-001 makes neither. Because orders release without a human, the council added the controls of section 1.2 item 5 (threshold, kill switch, monitoring) and treats any raise of the threshold as a change requiring re-assessment.

**Re-tier triggers:** using AI-001 for federal integration sourcing (to High, given supply chain integrity for DoD systems); using AI-005 scores as the sole basis for discipline (prohibited); letting AI-002 decide credit or payment plans (to High); letting AI-004 change addresses or issue large refunds.

## 4. MEASURE
Results are from monitoring and audits between 2026-03 and 2026-08.

### 4.1 AI-001 demand forecasting and automated reordering
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Weighted absolute percentage error (WAPE) at a 4-week horizon for A-class SKUs; threshold 30% overall and per product line | Overall 21%; video surveillance 37%; consumer networking 33% | **No** for two lines |
| Safe (supply chain integrity) | Share of automatically released lines to suppliers that are suspended, under investigation, or not authorized; threshold 0% | 0 to non-authorized sources, but 31 orders were released to Supplier K after the OEM's first channel warning, because the filter checks authorization status only (P08) | **No** |
| Secure and resilient | Service identity limited to order creation; SSO and MFA for model consoles | Service role scoped (P04); 2 shared notebook accounts found | Partial |
| Accountable and transparent | Every released order traceable to the model version and inputs; buyer override reasons recorded | Model version logged; override reasons free text, 40% blank | Partial |
| Explainable and interpretable | Buyers see forecast drivers per SKU | Available and used | Yes |
| Privacy-enhanced and data protection | No FCI outside systems that meet FAR 52.204-21 | DoD orders in the feed; artifacts exported to a tracker without those terms | **No** |
| Fair, with harmful bias managed | Fill rate by customer segment: top-100 resellers, small resellers (under $250,000 a year), DoD primes, and Online Retail. Flag if a segment is more than 3 points below the best segment | Top-100 97%; small resellers 92%; DoD primes 96%; Online Retail 95% | **No** (small resellers 5 points below) |
| Financial drift | Excess inventory created by automatic releases | About $14 million excess on 3 product lines after an OEM price change in 2026-05 | **No** |

### 4.2 AI-005 DC labor management
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Fair, with harmful bias managed | Coaching-flag rate by sex and age band (40 and over vs under 40), compared using the four-fifths screening threshold on the "not flagged" rate | Sex within threshold; workers 40 and over not-flagged rate 0.78 of the under-40 rate | **Flagged.** Review whether task mix explains it (older workers assigned more heavy-pick zones) by 2026-11-30 |
| Valid and reliable | Share of flags overturned by supervisors after review | 22% | **No** (target under 10%) |
| Accountable and transparent | Workers can see their scores and contest them | Visible at 6 of 9 DCs; contest process informal | Partial |
| Safe | Productivity targets adjusted for heat and heavy-pick zones | Adjusted at 4 DCs | Partial |

### 4.3 Online Retail models
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-002 fraud screening | Automatic decline rate by shipping-region proxy; flag a region more than 2 times the overall rate without a fraud-loss explanation | Two rural regions at 2.4 times the overall rate | **Flagged** |
| AI-002 fraud screening | False declines reversed on consumer call | 1.1% of declines | Yes (target under 2%) |
| AI-004 assistant (AI 600-1: data privacy, confabulation, information security) | Order details disclosed after weak identity check in red-team tests; fabricated policy answers in 200 sampled chats; prompt-injection test | 3 of 40 red-team attempts obtained order details; 2.5% fabricated answers; injection blocked | **No** for disclosure; **No** for confabulation (target under 1%) |
| AI-007 seller risk | Suspensions without the Act's notice step | 0 in sampled cases; INFORM data used in a marketing test (POAM-020) | Partial |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** automatic release only under $250,000, only to authorized sources, only for SKUs with a manufacturer of record, and (new) only to suppliers with no open risk flag. Buyers sample 2% of released orders weekly. A kill switch in the ERP stops all automatic releases; the Group supply chain risk director can use it during any supplier incident (P08).
- **AI-005:** supervisors review every flag before coaching; scores are never the sole basis for discipline; workers can see and contest scores at every DC.
- **AI-002:** automatic declines only above a high threshold; held orders go to analysts; consumers can request review.
- **AI-004:** disclosed as AI; one-time code to the account's email or phone before order details; hand-off to an agent on request.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board audit and risk committee; P01 risks GR-09, ID-008, ID-021, LW-010, OR-011, and OR-012.

**Incident handling:** an automatically released order to a suspended or compromised supplier is a supply chain incident under P08; an AI disclosure of customer data follows POL-03.

**Decommissioning:** each use case has an off switch and a fallback the BIA already covers (P05): manual reorder reports for AI-001, supervisor-only assignment for AI-005, manual review queues for AI-002, and agents for AI-004.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 demand forecasting and automated reordering | **Continue with conditions** (council, 2026-08-27; board audit and risk committee informed 2026-09-15) | Supplier risk flags added to the release filter by 2026-10-15; DoD orders removed from the feed and artifacts kept inside the platform by 2026-11-30; automatic release limited to SKUs with a manufacturer of record by 2026-11-30; drift and excess-inventory monitoring with a 2-week threshold review by 2026-12-31; small-reseller fill-rate gap 3 points or less by 2027-03-31; no threshold increase until all are met (POAM-025) |
| AI-005 DC labor management | **Continue; expansion of automated task allocation paused** | Task-mix analysis for the age finding by 2026-11-30; contest process at every DC by 2026-12-31; counsel review of state quota laws for each DC state before any new quota; scores never the sole basis for discipline |
| AI-002 fraud screening | **Continue** | Regional decline analysis and threshold adjustment by 2026-12-31 |
| AI-004 customer service assistant | **Continue with conditions** | One-time code before order details by 2026-12-31; confabulation under 1% in monthly samples; red-team test each quarter |
| AI-003, AI-006, AI-007 | **Continue** | AI-003 CCPA risk assessment by 2027-06-30; AI-007 stops using INFORM data outside compliance (POAM-020) |
| AI-008 receiving vision | **Pilot continues** | Validation against OEM serial checks at DC-1 before any expansion |
| AI-009, AI-010 | **Approved** | Standard monitoring; AI-009 prohibited for decisions about people and for CUI, FCI, or cardholder data |
