# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Hotels, Attractions, Vacation Ownership and the finance subsidiary, corporate) |
| Tier / Vertical | Multi-Sector / Accommodation and Food Services (focus division: Hotels) |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the regulator-specific rules for the priority use cases. The registry default, **revenue-management pricing and the guest chatbot** (AI-001, AI-002), is kept as the Hotels priority because both run at scale across 88 hotels. Division priorities add the credit model (AI-006) and the inventory forecasting model (AI-007), which carry regulator-specific rules |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), review 2026-08-17 to 2026-08-28, council decision 2026-08-26; presented to the board risk committee 2026-09-10 |
| Inventory | `ai-use-case-inventory.csv` (11 use cases: 2 High, 8 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of enterprise risk; receives the High-tier list and condition status quarterly (P01 GR-04) |
| Group AI council (formed 2026-03) | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Group HR director, the three division presidents' delegates, and the Qualified Individual. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring and report monthly |
| Finance subsidiary model risk function | Validates the credit model; reports to the finance subsidiary president |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) |
| Group Chief Privacy Officer | Data use and purpose rules, notices, retention |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-03, under POL-01 4.13)
1. **Register before use.** Every AI use case that sets prices, talks to guests, makes or supports decisions about credit, employment, or access, or processes Restricted data is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: the council approves; a pre-deployment impact assessment, bias testing, notice to affected people, and quarterly monitoring are required.
3. **Price integrity.** Any AI that quotes or sets a price must show the total price including mandatory fees (16 CFR 464.2) and must respect the emergency pricing guardrail (Fla. Stat. 501.160 as the worked example).
4. **Regulator overlays.** Each division supplement adds its regulator's rules: Regulation B and the Safeguards Rule for the finance subsidiary, Fla. Stat. 721.13 for inventory reservations, COPPA for anything touching the kids' club (no kids' club data in any AI use case without council approval).
5. **Change gate.** A material change (new model, new vendor feature, new data source, new decision role) triggers re-assessment before release.
6. **Approved tools only** for workforce generative AI (POL-05 4.7).

**Where the program fell short in 2026** (scenario gap 10). Most use cases went live before the council existed. Before this review the council had looked at 6 of 11 use cases (AI-001, AI-002, AI-005, AI-006, AI-007, AI-010). Three live use cases had concrete legal gaps: the chatbot omits the resort fee, the credit model's reasons are not always specific, and the inventory model keeps no records. This assessment covered all 11 at inventory level and the four priority use cases in depth. The other five have council review dates by 2026-12-31.

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Revenue-management pricing | Hotels | Medium | In production; conditions |
| AI-002 | Guest chatbot (generative) | Hotels | Medium | In production; conditions |
| AI-003 | Dynamic ticket pricing | Attractions | Medium | In production; review due 2026-11-30 |
| AI-004 | Ticket bot detection | Attractions | Medium | In production; review due 2026-11-30 |
| AI-005 | Seasonal applicant screening | Attractions (Group HR) | High | Proposed; not approved |
| AI-006 | Credit model for timeshare loans | Vacation Ownership (finance subsidiary) | High | In production; conditions |
| AI-007 | Inventory forecasting and rental model | Vacation Ownership | Medium | In production; conditions |
| AI-008 | Finger-scan gate matching | Attractions | Medium | In production; review due 2026-10-31 |
| AI-009 | Payment fraud scoring | Group | Medium | In production; review due 2026-12-31 |
| AI-010 | Enterprise generative AI assistant | Group | Low | Approved pilot (1,500 users) |
| AI-011 | Tour lead scoring | Vacation Ownership | Medium | In production; review due 2026-10-31 |

### 2.1 Hotels: revenue-management pricing (AI-001) and guest chatbot (AI-002)
| Rule | What it requires | What it means here |
|---|---|---|
| 16 CFR 464.2(a)-(b) | Any offer, display, or advertisement of a price for short-term lodging must disclose the total price, including mandatory fees, more prominently than other pricing | AI-002 quotes nightly rates, so every rate answer must lead with the total price. **Gap:** at 6 resort hotels the chatbot quoted rates without the mandatory resort fee (P03 G-079). AI-001 publishes rates to the CRS, which displays total price correctly (G-078) |
| 16 CFR 464.2(c); 464.3 | Excluded government charges and the final amount before the guest pays; fees not misrepresented | The chatbot must not describe the resort fee inaccurately or call it optional; it hands off to the booking engine for the final amount |
| Fla. Stat. 501.160 (worked example) | During a declared state of emergency, no unconscionable prices for dwelling units and essential commodities; a gross disparity from the 30-day pre-declaration average is prima facie evidence | The statute names dwelling units rather than hotels; the group treats room rates as covered (P03 G-086). AI-001 has run an emergency freeze at the 30 owned hotels since 2025, but the 49 managed hotels that use automatic publishing have no emergency rule. Other states' price gouging laws are applied the same way |
| Antitrust (counsel review) | Using competitors' non-public data to set prices can raise antitrust risk | The vendor offers a feature that pools non-public occupancy data from other client hotels. It was switched off in 2026-08 on counsel's advice; the vendor contract does not yet bar the vendor from pooling group data (P01 HTL-17) |
| FTC Act Section 5 (N72-R02) | Claims must be truthful; unfair practices prohibited | Chatbot answers about policies and prices are company statements |
| PCI DSS (N72-R01) | No card data outside the CDE | The chatbot must never accept card numbers; the input filter masks them |

### 2.2 Vacation Ownership: credit model (AI-006)
| Rule | What it requires | What it means here |
|---|---|---|
| 12 CFR 1002.9(a)(1) | Notify the applicant of action taken within 30 days after a completed application | Met: 0 late in a sample of 60 |
| 12 CFR 1002.9(b)(2) | A statement of specific principal reasons; saying the applicant failed to achieve a qualifying score is insufficient | **Gap:** 9 of 60 sampled notices gave a reason that described the score band, not the underlying factor (P03 V-030) |
| ECOA and Regulation B (general) | No discrimination on a prohibited basis | Fair lending analysis of approval rates and pricing is required for a model this consequential |
| 16 CFR 314.4 (N53-R01) | Customer information protected; access limited | Training data stays in the finance subsidiary's environment; no export to the guest profile hub |
| CFPB Circular 2022-03 | Withdrawn on 2025-05-12 | The Regulation B duty to give specific reasons is unchanged |
| Colorado SB26-189 (effective 2027-01-01) | Deployer notice, explanation after an adverse outcome, correction and human review rights for automated decisions that materially influence lending | Applies to decisions about Colorado consumers made on or after 2027-01-01. Its status is unsettled (federal preemption efforts; see `00_universal-framework/cross-sector/us-cross-sector-obligations.md`); counsel tracks it |

### 2.3 Vacation Ownership: inventory forecasting and rental model (AI-007)
| Rule | What it requires | What it means here |
|---|---|---|
| Fla. Stat. 721.13(12)(a) | The managing entity may forecast reservation and use and reserve accommodations for rental in the best interests of the owners as a whole | Authorizes the model's purpose for Florida plans |
| Fla. Stat. 721.13(12)(b) | A conspicuous statement of that right in the public offering statement | Confirm the statement is in each Florida plan's public offering statement (counsel check) |
| Fla. Stat. 721.13(12)(c) | Keep copies of all records, data, and information supporting each reservation determination for 5 years; make them available to the state division on investigation | **Gap:** no decision records kept (P03 V-031) |
| Fla. Stat. 721.071 | Material filed with the division with an affidavit of confidentiality is protected as a trade secret | Model records produced to the division are filed with an affidavit |
| 16 CFR 464.2 | Total price for vacation rentals | Rentals are sold through the CRS, which shows total price (P03 V-042) |

### 2.4 Attractions and group use cases (summary)
- **AI-005 applicant screening:** employment is a consequential decision. Title VII disparate-impact liability and ADA accommodation duties remain by statute even though the EEOC's 2023 technical assistance page was removed. The tool would be used only for park seasonal hiring in Florida, Texas, Georgia, Tennessee, and Ohio, so Colorado SB26-189 does not apply unless use expands.
- **AI-008 gate matching:** finger-scan templates are biometric data and therefore personal information under Fla. Stat. 501.171; retention is the issue (POAM-017), not matching accuracy.
- **AI-011 tour lead scoring:** uses hotel and park guest data for vacation ownership offers. The privacy notices must disclose this use (P03 G-087). Kids' club data is excluded by design.
- **AI-003, AI-004, AI-009:** standard Medium-tier controls; reviews scheduled.

## 3. Risk tiers (repository rubric)
- **High:** AI-005 (employment) and AI-006 (credit). Both are, or would be, a substantial factor in a consequential decision about a person.
- **Medium:** AI-001, AI-002, AI-003, AI-004, AI-007, AI-008, AI-009, AI-011. They interact with guests or influence business decisions that affect people (prices, access, offers, declined payments), but a human sets the rules or makes final decisions about individuals.
- **Low:** AI-010.

**Re-tier triggers:** letting AI-001 publish rates during a declared emergency without approval (to High, because of legal exposure); letting AI-002 change or cancel reservations or take payments; using AI-008 to refuse entry without staff review; using AI-011 to set financing terms or to target households with children.

## 4. MEASURE
Results are from tests and monitoring between 2026-05 and 2026-08.

### 4.1 Revenue-management pricing (AI-001)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Forecast error on 30-day occupancy (target under 5 points) | 3.8 points | Yes |
| Safe (emergency pricing) | Replay of the 2025 hurricane declaration period: maximum automated rate increase over the 30-day pre-declaration average | Owned hotels held by the freeze; 38% within 48 hours at 4 managed Florida hotels | **No.** No guardrail at managed hotels |
| Accountable and transparent | Share of rate changes above the band approved by a revenue manager (target 100%) | 100% | Yes |
| Privacy-enhanced | Personal data used | None | Yes |
| Fair, harmful bias managed | Not applicable to individual guests (rates are set by date and room type, not by person) | n/a | n/a |
| Governance (antitrust) | Pooled non-public competitor data feature | Switched off 2026-08; contract terms not yet amended | Partial |

### 4.2 Guest chatbot (AI-002), using AI 600-1 risk areas
| AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Confabulation | 60 scripted prompts on policies and prices: answers with a wrong fact (target 0 on prices, under 2% on policies) | Resort fee missing in 14 of 60 price answers (all at the 6 resort hotels); 3 wrong policy answers | **No** |
| Information integrity | Answers cite brand content or live rates | 57 of 60 | Partial |
| Information security (prompt injection) | Red-team test with crafted prompts to reveal other guests' reservations or system prompts | Not done | **No** |
| Data privacy | Card numbers masked before storage; transcripts kept 30 days | Masking worked in 20 of 20 tests; retention set | Yes |
| Human-AI configuration | AI disclosed at chat start; handoff to an agent | Handoff works; disclosure only in the footer | Partial |
| Value chain and component integration | Vendor model and retrieval changes go through the change gate | Vendor changed the model version in 2026-06 without notice | **No** |

### 4.3 Credit model (AI-006)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Default-rate calibration by score band (2025 originations) | Within tolerance in all bands | Yes |
| Explainable and interpretable | Adverse action notices with specific principal reasons (target 100%, 12 CFR 1002.9(b)(2)) | 51 of 60 (85%) | **No** |
| Fair, harmful bias managed | Approval-rate and pricing differences across demographic estimates and age bands; flag differences above 5 points without a documented business justification | Two flags (applicants aged 62 and over; one geographic cluster) | **Flagged.** Fair lending counsel review due 2026-11-30 |
| Accountable and transparent | Independent model validation within 24 months | Last validated 2024-05, before the acquisition | **Due.** Validation by 2027-01-31 |
| Secure and privacy-enhanced | Training data access limited to the model team; MFA | Legacy directory without MFA (POAM-020) | Partial |

### 4.4 Inventory forecasting model (AI-007)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Share of reserved inventory later requested by owners within 14 days of arrival (target under 3%) | 2.1% | Yes |
| Accountable and transparent | Records of each reservation determination kept 5 years (Fla. Stat. 721.13(12)(c)) | None kept | **No** |
| Fair to owners as a whole | Owner booking success rate in peak weeks before and after model releases | No significant change | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** revenue managers set bands; changes above 25% need approval. Extended to all hotels (with owner consent for managed hotels): when a state of emergency is declared for an area, rates for hotels in that area freeze at the 30-day pre-declaration average plus documented cost increases until a revenue manager and counsel approve otherwise.
- **AI-002:** price answers come only from the live rate service with total price; the bot hands off to an agent for any booking change, complaint, or low-confidence answer; AI disclosure at the start of each chat.
- **AI-006:** processors review every refer decision; any applicant can ask for reconsideration by a person; reason codes map to specific factors before notices are generated.
- **AI-007:** the revenue team approves releases above thresholds; every decision is logged with its inputs.

**Monitoring:** monthly metrics to division owners; quarterly High-tier and condition report to the council and the board risk committee; P01 risks GR-04, HTL-15, HTL-16, HTL-17, ATT-10, ATT-14, VO-06, VO-07, VO-11.

**Incident handling:** AI failures that misprice offers, disclose personal data, or produce unlawful decisions follow P08 and POL-03. A chatbot pricing error that reaches guests is handled as a consumer protection incident with counsel.

**Decommissioning:** each use case has an off switch and a fallback (manual rate setting, contact center, manual underwriting, manual inventory release) covered by the BIA (P05 BP-H06, BP-H05, BP-V03, BP-V06).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 revenue-management pricing | **Continue with conditions** (council, 2026-08-26) | Emergency freeze extended to the 49 managed hotels with automatic publishing by 2026-11-30 (owner consent); vendor contract amended to bar pooling of group data by 2026-12-31; quarterly replay test |
| AI-002 guest chatbot | **Continue with conditions** | Total price in every rate answer by 2026-10-31 (POAM-031); prompt-injection red-team test and AI disclosure at chat start by 2026-11-30; vendor must give notice of model changes (contract amendment by 2026-12-31) |
| AI-006 credit model | **Continue with conditions** | Reason code mapping by 2026-11-15 and monthly second-line notice review (POAM-028); fair lending review of the two flags by 2026-11-30; independent validation by 2027-01-31; Colorado SB26-189 readiness by 2026-12-31 |
| AI-007 inventory model | **Continue with conditions** | Decision log with inputs kept 5 years by 2026-11-30 (POAM-032); public offering statement check by 2026-12-31 |
| AI-005 applicant screening | **Not approved** | Impact assessment, adverse impact testing, accommodation process, and vendor documentation before any pilot |
| AI-010 enterprise assistant | **Approved (pilot)** | No Restricted data; no decisions about people |
| AI-003, AI-004, AI-008, AI-009, AI-011 | **Continue pending council review** | Reviews by 2026-10-31 (AI-008, AI-011), 2026-11-30 (AI-003, AI-004), and 2026-12-31 (AI-009) |
