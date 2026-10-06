# AI Governance Risk Assessment: Enterprise AI Portfolio, Revenue-Management Pricing, and Guest Chatbot

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded hotel franchisor, manager, and owner: 750 hotels in 33 states and DC) |
| Tier / Vertical | Enterprise / Accommodation and Food Services |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with full assessments of AI-001 revenue-management pricing (section 6) and AI-002 guest chatbot (section 7) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1) for generative use cases; repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Risk Officer), meeting of 2026-08-19; GRC team prepared the portfolio review (2026-08-17 to 2026-08-28) |
| Decision | Executive risk committee, 2026-09-10 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 2, Medium 9, Low 1 |
| Status | In production 10, Pilot 1, Suspended 1 |
| Generative AI use cases | 5 (AI-002, AI-003, AI-009, AI-010, AI-012) |
| Committee review complete | 8 of 12 |
| Not yet reviewed | 4: AI-006, AI-008, AI-010, AI-011 (all due 2026-11-30, POAM-020) |
| Use cases offered to franchisees or clients | 2: AI-001 (franchise pricing service, 212 franchised hotels) and AI-002 (also on SL-2 client booking pages) |

**Main findings:**
1. **Pooled pricing data (AI-001).** The revenue-management vendor pools non-public rate and occupancy data from the company's hotels and the 212 independently owned franchised hotels that subscribe to the franchise pricing service. This is the fact pattern the Third Circuit found plausible in *Cornish-Adebiyi v. Caesars Entertainment, Inc.* (P01 R-012, High).
2. **Emergency pricing (AI-001).** No automatic cap stops rate increases in a declared state of emergency; revenue managers freeze rates by hand (P01 R-057).
3. **Total price (AI-002).** 9 of 20 sampled chatbot quotes for resort collection hotels omitted the mandatory resort fee (P03 G-081; 16 CFR 464.2).
4. **Unreviewed AI.** 4 use cases run without committee review, including a High-tier employment tool (AI-006, ranking now disabled) that a hotel group switched on inside a vendor product.
5. **Biometric accuracy (AI-005).** Face matching has only vendor accuracy data; no local testing by age or skin tone.

## 2. GOVERN: AI governance committee operating model
**Charter.** Formed in 2025 under POL-01; reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee reviews quarterly.

**Members:** Chief Risk Officer (chair); Chief Commercial Officer; Chief Privacy Officer; CISO; General Counsel's delegate (with antitrust counsel for pricing use cases); Chief Human Resources Officer (for workforce tools); Executive Vice President, Hotel Operations; Vice President, Digital and Loyalty; Director of Franchise Technology Compliance (for services offered to franchisees); the data science lead. Internal Audit observes. **Recusal:** the Chief Commercial Officer is the executive owner of AI-001 and AI-002 and does not vote on them; the chair records the recusal.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Impact assessment; pre-deployment bias testing on the company's own population; human review design; notice to affected people; monitoring plan; legal review of state laws where it will be used |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy, security, and (for pricing) competition and fee-display review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.7; STD-05.3). From 2026-10-31, procurement and IT change management block AI features without an inventory ID (POAM-020). The GRC team owns the inventory.

**Policies:** POL-04 4.5 (no sharing or pooling of non-public rate and occupancy data without General Counsel approval); POL-04 4.9 (no Restricted or Confidential data in AI tools without committee approval and no-training terms); POL-05 4.7 (approved AI tools only); POL-01 4.14 (public statements and price displays reviewed and tested quarterly); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier use case and for AI-001 and AI-002; annual re-review of every use case.

**Why 4 use cases lack review.** All four entered as features switched on in existing vendor products (applicant tracking, workforce management, SIEM, building management) before the procurement block existed. AI-006 was switched on by one hotel group in 2026-04 without telling HR; the ranking feature was disabled on 2026-08-20 when the committee's intake sweep found it.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45(a) and (n) | Yes, all customer-facing use cases | Chatbot answers and price displays are the company's representations; unfair practices that cause substantial, unavoidable injury are prohibited |
| FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (effective 2025-05-12) | Yes, AI-001 and AI-002 | Short-term lodging is covered (464.1). Any offer, display, or advertisement of a price must show the total price, including mandatory resort and destination fees, more prominently than other pricing (464.2(a)-(b)); fees must not be misrepresented (464.3) |
| Sherman Act Section 1, 15 U.S.C. 1 (algorithmic pricing) | Litigation risk, AI-001 | *Cornish-Adebiyi v. Caesars Entertainment, Inc.*, No. 24-3006 (3d Cir. July 29, 2026), reversed the dismissal of claims that casino-hotels sent non-public pricing and occupancy data to a shared pricing algorithm that generated rates for competitors. *Gibson v. Cendyn Group, LLC*, No. 24-3576 (9th Cir. Aug. 15, 2025), affirmed dismissal where competing hotels only licensed the same software. The franchise pricing service adds a franchisor-specific risk: the company could itself be seen as the hub that collects franchisees' non-public data |
| Fla. Stat. 501.160 and other state price gouging laws | Yes, AI-001 | During a Governor-declared state of emergency, offering at an unconscionable price in the declared area is unlawful; a gross disparity from the average price in the 30 days before the declaration is prima facie evidence unless explained by added costs or market trends. The prohibition runs up to 60 days under the initial declaration and can be extended. The statute names dwelling units rather than hotels; the company treats room rates as covered (cautious reading). Other states are handled the same way through counsel's matrix |
| PCI DSS v4.0.1 | Yes, AI-002 and AI-003 | Card numbers typed into chat or spoken on calls must not be stored outside the vault |
| State breach notification laws (Florida worked example, Fla. Stat. 501.171) | Yes, AI-002, AI-005 | Transcripts and verification data hold personal information. Florida's definition includes biometric data as defined in 501.702 (501.171(1)(g)1.a.(VI)) |
| Florida biometric definition (Fla. Stat. 501.702) | Unsettled, AI-005 | 501.702 defines biometric data as automatic measurements of biological characteristics used to identify a person and excludes physical or digital photographs and data generated from video or audio recordings. Whether face templates computed from a selfie and an ID photo fall inside the definition is unsettled; counsel to confirm. The company treats them as biometric data. (The Florida Digital Bill of Rights itself does not apply: the company is not a "controller", P03 G-096) |
| Illinois BIPA (740 ILCS 14) | Avoided by design, AI-005 | Face matching is disabled at Illinois hotels. The statute text was not re-verified |
| Employment AI laws | Yes, AI-006 (and possibly AI-008) | The 22 hotels that used AI-006 include 2 in Illinois and 3 in California. Illinois HB 3773 (775 ILCS 5/2-102, effective 2026-01-01) makes it a civil rights violation to use AI with a discriminatory effect in employment decisions and requires notice (rules pending; text confirmed only through official search snippets). The CPPA ADMT regulations (11 CCR 7200 et seq.) cover employment significant decisions, with ADMT compliance by 2027-01-01. Colorado SB26-189 (effective 2027-01-01) and NYC Local Law 144 would apply if the tool were used for Colorado or New York City hiring; it was not. Federal equal employment opportunity laws apply everywhere; counsel reviews adverse impact |
| Connecticut PA 26-64 (surveillance pricing, from 2026-10-01) | Watch, AI-001 | Limits and disclosures for surveillance pricing (per the Connecticut AG; act text not read). The personalized pricing feature is off; enabling it requires counsel review of this and similar laws |
| FTC proposed AI accuracy policy statement (July 2026) | Watch only | Proposed, not final |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person (here, employment) or able to affect physical safety.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | Revenue-management pricing and the franchise pricing service | Medium (High during a declared emergency) | In production | Reviewed 2025-11-12; re-reviewed 2026-08-19 |
| AI-002 | Guest chatbot | Medium | In production | Reviewed 2026-01-21; re-reviewed 2026-08-19 |
| AI-003 | Contact center agent assist | Medium | In production | Reviewed 2026-05-20 |
| AI-004 | Booking fraud and card-testing detection | Medium | In production | Reviewed 2026-03-18 |
| AI-005 | Mobile check-in face matching | High | In production (disabled in Illinois) | Reviewed 2026-02-11 |
| AI-006 | Applicant screening and ranking | High | Suspended (ranking disabled) | Not reviewed (due 2026-11-30) |
| AI-007 | Loyalty personalization | Medium | In production | Reviewed 2025-12-10 |
| AI-008 | Labor demand forecasting and scheduling suggestions | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-009 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-01-14 |
| AI-010 | SOC alert triage assistant | Low | In production | Not reviewed (due 2026-11-30) |
| AI-011 | Predictive maintenance for building systems | Medium | Pilot (12 hotels) | Not reviewed (due 2026-11-30) |
| AI-012 | Guest review response drafting | Medium | In production | Reviewed 2026-04-15 |

**Tiering notes:** AI-005 is High because it decides whether a digital room key is issued, which affects guests' physical security; a failed match only sends the guest to the front desk, so no one is refused a stay. AI-006 is High because ranking is a substantial factor in hiring. AI-001 stays Medium because room prices are not one of the rubric's consequential decisions and are not individualized; it is treated as High for the duration of any declared state of emergency in a hotel's area, and its enterprise risk (R-012) is High because of the competition exposure. AI-008 may move to High if counsel concludes that schedule suggestions are employment decisions in any state where it runs.

## 5. Pricing, competition, and fee display controls (AI-001 and AI-002)
| Duty | What the company does | Status |
|---|---|---|
| No pooling of non-public competitor data | Opt out of the vendor's pooled benchmark; contract amendment confirming past pooled data will not be used; recommendations use only each hotel's own data plus public market data | Not met: pooling active for all 322 subscribing hotels (110 company-operated, 212 franchised). Due 2026-12-31 (POAM-020) |
| Independent pricing by franchisees | Franchisees keep full rate authority; the franchise pricing service gives recommendations only; an information barrier keeps franchisees' non-public data away from the company's own revenue managers | Partially met: franchisees approve rates, but revenue strategy staff supporting the service can see franchised hotels' data in the vendor tool. Barrier due 2026-12-31 |
| Emergency pricing | Automatic cap at the 30-day pre-declaration average in declared areas, with human approval and a written cost reason for any increase | Not met: manual freeze only. Due 2026-11-30 (POAM-020) |
| Total price in feeds and chatbot answers | Mandatory fees loaded as fee codes in every feed; chatbot states the total price first | Partially met: 14 hotels missing fee codes in one feed; chatbot errors for resort collection hotels. Due 2026-11-30 (POAM-021) |
| No individualized pricing | Personalized pricing feature off; quarterly quote parity test | Met |

These rows match P03 G-079, G-081, G-082, G-085, and G-094, and POAM-020 and POAM-021.

## 6. Full assessment: AI-001 revenue-management pricing
### 6.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Forecast demand by room type and date and recommend daily rates, to raise revenue per available room |
| Users / operators | Revenue managers for the 110 company-operated hotels (under the Vice President, Revenue Strategy); revenue staff at 212 franchised hotels that subscribe to the franchise pricing service |
| Affected people | Guests who book at 322 hotels; franchisees whose pricing depends on the service |
| Data | Aggregated bookings, stay history, and rates from the CRS and PMS (no guest identities); public competitor rates; events calendar. **The vendor pools non-public rate and occupancy data from all its client hotels into a benchmark** |
| Build or buy | Buy: vendor SaaS configured by the revenue strategy team |
| Automation | At company-operated hotels, recommendations publish automatically within floor, ceiling, and a 15% daily change limit; anything outside needs revenue manager approval. Franchised hotels choose automatic or manual publishing |
| Not intended | Personalized prices based on guest profile, location, device, or browsing (feature exists and is **off**) |

### 6.2 Risk tier
Medium (section 4). **Escalation triggers:** a declared state of emergency covering a hotel's area (High for its duration); enabling personalized pricing; any feature that shares one hotel's non-public data with another.

### 6.3 MEASURE (back-test June 2025 to July 2026, and August 2026 tests)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 14-day occupancy forecast error under 10% | 7.8% average error across company-operated hotels | Yes |
| Valid and reliable | Published rate changes outside floor, ceiling, or daily limit without approval | 0 at company-operated hotels (guardrails enforced by the tool) | Yes |
| Safe (emergency pricing) | No increase above the 30-day pre-declaration average in a declared area without approval | Back-test of 2025 Florida hurricane declarations: auto-published rates at 9 company-operated hotels rose up to 31% above the 30-day average before revenue managers froze them by hand (median 26 hours) | **No** |
| Secure and resilient | Vendor assurance; SSO with MFA; settings change log | Vendor SOC 2 Type 2 reviewed; SSO with MFA; changes logged | Yes |
| Accountable and transparent | Every automatic change logged with drivers; daily exception review | Logged; reviewed daily by revenue managers | Yes |
| Explainable and interpretable | Revenue managers can see why a rate was recommended | Driver breakdown in the vendor dashboard | Yes |
| Privacy-enhanced | No guest identities sent to the vendor | Extract carries aggregated data only | Yes |
| Fair, with harmful bias managed | Same room type and dates quoted from 6 locations, 3 device types, 2 languages, member and non-member: prices identical apart from disclosed member rates | 120 quotes; no unexplained differences | Yes |
| Competition safeguards | No non-public data from one hotel used to price another; information barrier for franchise data | Pooling active for 322 hotels; franchise data visible to company revenue strategy staff | **No** |

**Bias and fairness plan (ongoing):** repeat the 120-quote parity test each quarter and after any vendor model update; any unexplained difference between locations, devices, languages, or member status is a stop-and-investigate event.

### 6.4 MANAGE
- **Human in the loop:** automatic publishing only inside guardrails; revenue manager approval outside them. **Emergency mode:** when a state of emergency is declared for a hotel's area, the tool caps rates at the 30-day pre-declaration average; any increase needs approval by the Vice President, Revenue Strategy with a written cost reason, for as long as the price gouging prohibition runs (Florida worked example: up to 60 days under the initial declaration, unless extended).
- **Competition:** opt out of pooling, amend the contract, build the information barrier, and have antitrust counsel review the franchise pricing service terms (franchisees keep full rate authority; recommendations use only their own data and public data).
- **Monitoring:** daily exception report; monthly guardrail and emergency-mode report to the committee; quarterly parity test.
- **Incidents:** a pricing error at scale, an emergency-mode failure, or a data-sharing breach is logged under POL-03 and reviewed by the committee.
- **Decommissioning:** switch to manual rates (P05 BP-11 tolerates 72 hours) if the vendor will not remove pooling by 2026-12-31 or emergency mode fails a test.

## 7. Full assessment: AI-002 guest chatbot
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Answer common questions, quote availability and rates, show a signed-in member's own reservations, and link to the booking engine |
| Users / operators | Guests on the brand website, app, and messaging, and on SL-2 client booking pages; the digital team maintains answer sources |
| Affected people | About 1.9 million conversations a year |
| Data | Questions, names, contact details, transcripts (kept 90 days); availability and rates from the CRS; member reservations. Card numbers are redacted before storage since 2026-07; older transcripts with card numbers are being purged (R-054) |
| Build or buy | Build: company integration on Cloud provider B's managed generative AI service, with retrieval from approved brand content; the model provider may not train on company data (contract) |
| Not intended | Taking payments, changing reservations, legal, medical, or accessibility advice, or evacuation instructions (hand off to staff) |

### 7.2 Risk tier
Medium. **Escalation triggers:** taking payments or reservation changes in chat; answering accessibility or emergency questions without handoff; using transcripts for marketing profiles.

### 7.3 MEASURE (August 2026)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Monthly 200-question test set (policies, amenities, hours); 95% correct | 93% correct (pet fees and cancellation windows at resort collection hotels wrong) | **No** |
| Valid and reliable (fee rule) | Every rate answer states the total price including mandatory fees, before other pricing | 9 of 20 quotes for resort collection hotels omitted the resort fee; 20 of 20 correct for other hotels | **No** (16 CFR 464.2) |
| Safe | Accessibility, medical, and emergency questions handed to staff | 18 of 20 handed off; 2 answered from general knowledge | **No** |
| Secure and resilient | 30 prompt-injection attempts to reveal other guests' data or system instructions | No guest data exposed (the integration reads only the signed-in member's reservations); system instructions partly revealed in 2 attempts | Partial |
| Accountable and transparent | States it is an AI assistant at the start and offers a human | Yes, every conversation | Yes |
| Explainable and interpretable | Answers link to the brand page they come from | 182 of 200 answers linked a source | Yes |
| Privacy-enhanced | Card numbers redacted before storage; transcripts kept 90 days | Redaction live; historical transcripts with card numbers not yet purged | Partial |
| Fair, with harmful bias managed | Same 200 questions in English and Spanish; flag a gap above 5 percentage points | English 94%, Spanish 87% | **No** (7-point gap) |

**Bias and fairness plan (ongoing):** repeat the English and Spanish test sets monthly; Spanish answers show a handoff offer on every reply until the gap is 5 points or less for two months in a row. Add French and Portuguese test sets in 2027 for the resort collection markets.

### 7.4 MANAGE
- **Human in the loop:** staff take over booking changes, complaints, accessibility, medical, and emergency questions; 100 transcripts reviewed each week.
- **Total price:** fee rules loaded from the same fee table the booking engine uses, so every quote states the total first (POAM-021, 2026-10-15); monthly 20-quote test by the Vice President, Distribution and Reservations.
- **Data protection:** finish the purge of historical transcripts by 2026-12-31; keep redaction and 90-day retention.
- **Monitoring:** monthly report to the committee on accuracy, fee compliance, handoffs, language gap, and prompt-injection tests.
- **Incidents:** a wrong price at scale, a fee-rule failure, or data exposure through the chatbot is logged under POL-03; card data exposure follows P08.
- **Decommissioning:** turn off rate quoting for resort collection hotels if the fee rule is not live by 2026-10-15; turn the chatbot off if a guest-data exposure is found until fixed.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier use case and AI-001 and AI-002 report quarterly metrics (inventory column `monitoring`) to the committee; threshold breaches trigger re-review.
- **Third parties:** AI vendors are tier-1 in the vendor program when they handle Restricted or Confidential data; contracts require notice of material model changes and prohibit training on company data.
- **Franchise and client services:** any AI offered to franchisees or SL-2 clients needs Director of Franchise Technology Compliance sign-off and counsel review of the service terms.
- **Incident handling:** AI incidents (unsafe output, bias finding, pricing error, data misuse) are logged as SOC or operations events and follow P08 where security or personal data is involved.
- **Decommissioning:** use cases are retired if they fail monitoring thresholds twice or a vendor changes data-use terms; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the AI governance committee's recommendation of 2026-08-19 (the Chief Commercial Officer recused on AI-001 and AI-002):
1. **AI-001:** approved to continue with conditions: emergency cap live by 2026-11-30; pooled benchmarking opt-out, contract amendment, information barrier, and antitrust counsel review of the franchise pricing service by 2026-12-31 (POAM-020). If the vendor will not remove pooling, the company moves to manual or single-hotel recommendations.
2. **AI-002:** approved to continue with conditions: total price rule live by 2026-10-15 or rate quoting off for resort collection hotels (POAM-021); emergency, medical, and accessibility handoff fixed by 2026-10-31; Spanish handoff offer until the language gap closes; historical transcript purge by 2026-12-31.
3. **AI-005:** continue; local accuracy testing by age band and skin tone by 2027-03-31 (POAM-020); remains disabled in Illinois; counsel to confirm the Florida 501.702 question and other states' biometric laws.
4. **AI-006:** ranking stays disabled until committee review, an adverse impact analysis, and counsel's review of the Illinois and California rules are complete; no re-enable after 2027-01-01 without a CPPA ADMT compliance check.
5. **AI-008, AI-010, AI-011:** may continue in current scope until committee review by 2026-11-30; no expansion.
6. **Procurement block** on AI features without an inventory ID live by 2026-10-31.
