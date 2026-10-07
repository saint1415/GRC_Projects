# AI Governance Risk Assessment: Enterprise AI Portfolio and Automated Reordering

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded IT hardware and software distributor) |
| Tier / Vertical | Enterprise / Wholesale Trade |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001 demand forecasting and automated reordering in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1) for AI-006, AI-007, and AI-011; repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Data and Analytics Officer), meeting of 2026-08-19; GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-10 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 4, Medium 7, Low 1 |
| Status | In production 10, Pilot 2 |
| Committee review complete | 8 of 12 |
| Not yet reviewed | 4: AI-005, AI-008, AI-011, AI-012 (all due 2026-11-30, POAM-021) |
| High-tier use cases | AI-003 trade credit (credit), AI-004 resume screening (employment), AI-008 robotics path planning (safety), AI-012 labor scoring (employment) |
| High-tier use cases with company-run bias or safety testing | 1 of 4 (AI-003); AI-004 relies on the vendor's adverse impact report; AI-008 and AI-012 not yet tested |

**Main findings:** two High-tier use cases (AI-008 and AI-012) entered through vendor software upgrades without committee review. The resume screening tool (AI-004) is not ready for the CCPA ADMT compliance date of 2027-01-01 and was suspended for California requisitions. Automated reorder release (AI-001), the largest financial exposure in the portfolio, has run since 2026-02 without formal drift monitoring and over-ordered after an OEM price change in 2026-06.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-09 (P01), which the board risk committee reviews quarterly.

**Members:** Chief Data and Analytics Officer (chair); CISO; Chief Privacy Officer; Chief Compliance Officer; General Counsel's delegate; Chief Human Resources Officer (workforce tools); Chief Supply Chain Officer (supply chain tools); Vice President, Credit and Collections (credit tools); Director, OT Engineering (safety); Director, Government Contracts (federal data). Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Impact assessment; company-run bias or safety testing on company data; notice to affected people where the law requires it; human review design; monitoring plan; legal review (ECOA, employment, CCPA, Colorado) |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; security and data review (no CUI; FCI only in approved tools) |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on in existing vendor products, must be registered before use (POL-05 4.6; STD-05.3). After AI-008 and AI-012 arrived through vendor upgrades, procurement and change management now require an inventory ID before an AI feature is enabled, and OT vendor release notes are reviewed for AI features.

**Policies:** POL-04 4.8 (no Restricted data in AI tools outside the FSCE; Confidential data only in approved tools); POL-04 4.3 (FCI only with vendors bound by FAR 52.204-21 terms); POL-05 4.6 (approved tools and registration); POL-01 4.13 and 4.14 (sourcing order and Section 889 screening apply to every purchase order, including automatically released ones).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier use case and for AI-001; annual re-review of every use case.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| ECOA and Regulation B (12 CFR Part 1002) | Yes, for AI-003 | Trade credit to resellers is credit. For trade credit the company must notify the applicant of action taken within a reasonable time and, on a written request within 60 days, give a written statement of specific reasons (1002.9(a)(3)(ii)); "failed to achieve a qualifying score" is not a sufficient reason (1002.9(b)(2)). Intentional discrimination and prohibited bases still apply; since the 2026 amendment, 1002.6(a) states that ECOA does not provide for the effects test, but Title VII-style disparate impact is still tested internally as good practice |
| CCPA ADMT and risk assessment rules | Yes, for AI-004 (California applicants) | Employment decisions are significant decisions; businesses already using ADMT must comply by 2027-01-01 (pre-use notice, opt-out with exceptions, access). Risk assessments for 2026-2027 are submitted by 2028-04-01 |
| Colorado SB26-189 | From 2027-01-01, for Colorado applicants (AI-004) and possibly AI-003 | Covers ADMT that materially influences consequential decisions, including employment and lending, with no small-business exemption. The company hires remote inside sales staff nationwide; counsel is confirming whether trade credit to businesses is a covered lending decision |
| Title VII disparate impact; Uniform Guidelines | Yes, for AI-004 and AI-012 | Disparate impact liability exists by statute; the four-fifths rule (29 CFR 1607.4(D)) is the screening threshold for adverse impact in selection rates |
| Illinois HB 3773; NYC Local Law 144 | No today | The company has no sites in Illinois or New York City; remote requisitions in those places are excluded from AI-004 until reviewed |
| FAR 52.204-21, FAR 52.204-25, DFARS 252.246-7008 | Yes, for AI-001 and AI-011 | AI-001 processes FCI and releases purchase orders that must follow the sourcing order and covered-manufacturer block; AI-011 reads federal contracts (FCI) |
| DFARS 252.204-7012 | Yes, as a prohibition | No AI tool outside the FSCE may process CUI (POL-04 4.8) |
| FTC Act Section 5 | Yes, for AI-006 and AI-007 | Accurate statements to resellers; AI-drafted product claims checked against OEM specifications |
| Texas TRAIGA | Reviewed | The company does business in Texas; none of its use cases falls under the Act's intent-based prohibitions |
| Workplace safety obligations | Yes, for AI-008 | Not analyzed here; the Director, OT Engineering and the safety team review AI-008 with the committee |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person, or able to affect physical safety or critical operations.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | Demand forecasting and automated reordering | Medium | In production (auto-release since 2026-02) | Reviewed 2025-11-12; re-reviewed 2026-08-19 |
| AI-002 | Quote and price recommendations for sales representatives | Medium | In production | Reviewed 2026-03-11 |
| AI-003 | Reseller trade credit limit recommendations | High | In production | Reviewed 2026-05-20 |
| AI-004 | Applicant resume screening and ranking | High | In production (suspended for California requisitions) | Reviewed 2026-02-18; re-reviewed 2026-08-19 |
| AI-005 | Receiving image inspection for counterfeit indicators | Medium | Pilot | Not reviewed (due 2026-11-30) |
| AI-006 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-01-21 |
| AI-007 | Reseller-facing support assistant | Medium | In production | Reviewed 2026-06-17 |
| AI-008 | Robotics path planning and slotting in automated storage | High | In production | Not reviewed (due 2026-11-30) |
| AI-009 | Order fraud detection model | Medium | In production | Reviewed 2026-08-19 |
| AI-010 | SOC alert triage assistant | Low | In production | Reviewed 2026-04-08 |
| AI-011 | Contract clause extraction for federal flowdowns | Medium | Pilot | Not reviewed (due 2026-11-30) |
| AI-012 | Warehouse labor scheduling and productivity scoring | High | In production (scheduling; scoring for coaching only) | Not reviewed (due 2026-11-30) |

**Tiering notes:** AI-001 stays Medium because it makes no decision about a person, but it is the highest financial exposure and is governed with High-tier monitoring (section 7). AI-003 is High because some resellers are sole proprietors and the model is a substantial factor in credit decisions. AI-005 stays Medium because it can only add inspections. AI-009 is Medium because an analyst reviews every hold. AI-012 becomes a consequential employment use if scores are used for discipline, which is why that use is blocked until review.

## 5. MEASURE: testing plan for High-tier use cases
| Use case | Metric | Groups compared | Threshold for action | Status |
|---|---|---|---|---|
| AI-003 trade credit | Approval, limit, and decrease rates; reason-code coverage | Business size band; years in business; region (ZIP code reviewed as a proxy) | Any group's approval rate below 80% of the highest group at similar payment history; any adverse action without a specific mapped reason | Tested 2026-05: no group below threshold; reason codes mapped for 71% of decisions (target 100% by 2026-12-31) |
| AI-004 resume screening | Selection rate into the "qualified" pool | Sex; race or ethnicity (voluntary self-identification); age band | Selection rate below four-fifths of the highest group (29 CFR 1607.4(D)), or a statistically significant gap | Vendor report only; company analysis due 2026-11-30 |
| AI-008 robotics | Near misses and safety stops per 10,000 robot hours | Before and after the 2026-04 upgrade; site | Any increase over the pre-upgrade baseline | Data collected; review due 2026-11-30 |
| AI-012 labor scoring | Score distribution and coaching referrals | Shift; age band; disability accommodation status; agency versus employee | Referral rate ratio above 1.25 for any group | Not started |

**Data limits:** demographic data comes only from voluntary self-identification, kept separate from the models and used only for testing. Small reseller businesses have no demographic data, so AI-003 testing uses business characteristics and proxy review.

## 6. Portfolio risks in the P01 register
- R-029: AI-004 not ready for CCPA ADMT (Moderate).
- R-030: AI-001 drift (Moderate).
- R-055: AI-003 reasons cannot be stated on request (Moderate).
- R-063: AI pricing chat leaking contract prices (avoided; feature not enabled).
- R-065: AI-005 false assurance at receiving (Moderate, in ER-02).
- R-032: unapproved generative AI use (avoided; domains blocked).

## 7. Full assessment: AI-001 demand forecasting and automated reordering
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Forecast weekly demand for about 180,000 active SKUs and replenish stock across 6 distribution centers, keeping fill rates high without excess inventory |
| Users / operators | About 380 purchasing staff; the supply chain planning team tunes the models |
| Affected parties | Resellers and DoD customers (fill rates and back orders), OEMs and authorized sources (order volumes), and the company's balance sheet (inventory). No decisions are made about individual people |
| Data | 3 years of ERP order history, **including DoD orders (FCI)** under a FAR 52.204-21 safeguarding schedule in the vendor contract (2026-03); inventory; supplier lead times and prices; the approved supplier list. The vendor trains a model per customer and may not use company data for other customers |
| Build or buy | Buy: vendor SaaS connected to the ERP |
| Automation | Since 2026-02, replenishment purchase orders release automatically when the supplier is the OEM or an authorized source, the order is $250,000 or less, and the quantity is within 20% of the forecast. About 38% of purchase order lines released automatically from 2026-03 to 2026-08 |
| Not intended | Open-market (broker) purchases, federal configuration job sourcing, allocation of scarce stock among customers, and customer pricing |

### 7.2 Risk tier
Medium (section 4), governed with High-tier monitoring because of its financial exposure. Escalation triggers: raising the auto-release limit; allowing broker sources; using it for allocation among customers.

### 7.3 MEASURE (2026-03 to 2026-08)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Weighted absolute percentage error (WAPE) at a 4-week horizon for A-class SKUs; threshold 25% for each product category | Overall 19%; networking 16%; servers 21%; **video surveillance 33%** | **No** (one category) |
| Safe (supply chain integrity) | Auto-released lines to a non-authorized source or a covered manufacturer; threshold 0 | 0 of about 212,000 auto-released lines (rules enforced in the ERP) | Yes |
| Secure and resilient | SSO with MFA; vendor SOC 2 Type 2 report reviewed; FCI schedule in the contract | All in place | Yes |
| Accountable and transparent | Override reasons recorded when buyers change a suggestion by more than 20% | 92% recorded (target 100%) | Partial |
| Explainable and interpretable | Buyers can see the drivers of each forecast (trend, seasonality, promotions, lead time) | Available on the SKU screen | Yes |
| Privacy-enhanced (data protection) | No personal information; FCI only under contract terms; no cross-customer use | Met | Yes |
| Fair, with harmful bias managed | Fill rate and forecast bias by customer segment (top-20 resellers, small resellers under $250,000 a year, DoD customers); flag a fill-rate gap above 3 points or bias beyond 10% | Small resellers 93% vs top-20 resellers 97% (4-point gap); DoD customers 96%; small-reseller-heavy SKUs under-forecast by 9% | **No** (fill-rate gap) |
| Drift (added for automation) | Detection of shifts after demand or price shocks | None in place; after an OEM price change in 2026-06 the model over-ordered for 2 weeks, about $3.1 million of excess inventory | **No** |

### 7.4 MANAGE
- **Human in the loop:** buyers review every suggestion outside the auto-release limits; the auto-release rules allow only OEM and authorized sources and apply the covered-manufacturer block (POL-01 4.13, 4.14).
- **Video surveillance category** removed from auto-release until its WAPE stays under 25% for 3 months.
- **Drift monitoring (POAM-021):** weekly WAPE by category with automatic suspension of auto-release for a category when WAPE exceeds 30% for 2 weeks in a row; event-triggered review after OEM price changes and allocation notices.
- **Fill-rate gap:** minimum safety stock for sparse-history SKUs; monthly fill-rate reporting by segment; target gap of 3 points or less by 2027-03-31.
- **Override reasons:** made mandatory in the ERP by 2026-11-30.
- **Incidents:** an auto-released order to a blocked supplier would be a supply chain incident under P08; a vendor security incident follows P08 and the contract notice terms.
- **Decommissioning:** return to ERP reorder reports if WAPE exceeds 35% overall for 2 months, if any auto-released order breaks the sourcing rules, or if the vendor changes its data-use terms.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier use case and AI-001 have quarterly metrics (inventory column `monitoring`) reported to the committee; threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse, wrong automated order) are logged as SOC, safety, or supply chain events and follow P08 where security or product integrity is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts require notice of material model changes, which would have caught AI-008 and AI-012.
- **Decommissioning:** use cases are retired if they fail monitoring thresholds twice or the vendor changes data-use terms; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the committee's recommendation of 2026-08-19:
1. **AI-001:** approved to continue with conditions: video surveillance removed from auto-release now; drift monitoring with automatic suspension by 2026-12-31; mandatory override reasons by 2026-11-30; fill-rate gap of 3 points or less by 2027-03-31. The auto-release limit stays at $250,000 until three months meet every threshold.
2. **AI-003:** continue; reason-code mapping to 100% by 2026-12-31 (POAM-021); counsel opinion on Colorado SB26-189 by 2026-11-30.
3. **AI-004:** stays suspended for California requisitions until the ADMT notice, opt-out, access, and human review workflow and the CCPA risk assessment are complete (target 2026-12-15); company selection-rate analysis by 2026-11-30; Colorado requisitions follow the same workflow from 2027-01-01.
4. **AI-008 and AI-012:** committee review by 2026-11-30; AI-012 scores may not be used for discipline until then; AI-008 keeps hardware safety interlocks and the fixed-path fallback.
5. **AI-005 and AI-011:** remain pilots until review; AI-005 may only add inspections; AI-011 is blocked from any document with CUI markings.
6. **Intake:** AI features in vendor upgrades need an inventory ID before they are enabled.
