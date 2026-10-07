# AI Governance Risk Assessment: Enterprise AI Portfolio, AI-Assisted Diagnostics, and Customer Chatbot

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded national electronics and device repair chain; 1,120 stores in 44 states and DC) |
| Tier / Vertical | Enterprise / Other Services (except Public Administration) |
| Scope | Enterprise AI portfolio (11 use cases in `ai-use-case-inventory.csv`), with full assessments of AI-001 AI-assisted diagnostics and AI-002 customer chatbot in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1) for AI-002 and AI-003; repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Data and Analytics Officer), meeting of 2026-08-26; GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-10 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 11 |
| Risk tier | High 2, Medium 7, Low 2 |
| Status | In production 8, Pilot 2, Suspended 1 |
| Committee review complete | 6 of 11 |
| Not yet reviewed | 5: AI-004, AI-005, AI-008, AI-010, AI-011 (all due 2026-11-30, POAM-024) |
| Use cases in employment decisions (state AI hiring and ADMT laws) | 2 High-tier (AI-004 applicant screening, in production; AI-011 technician scoring, suspended); 2 to watch (AI-005 fraud flags, AI-008 scheduling) |
| Customer-facing use cases with local bias testing | 2 of 2 assessed in section 7 (AI-001, AI-002); both have open gaps |

**Main findings:** both High-tier use cases are employment tools that arrived as vendor features and were never reviewed. One (AI-004) is ranking about 38,000 applicants a year without the bias audit, notices, or ADMT process that state and local laws require. The other (AI-011) was switched off on 2026-08-27 after the inventory scan found it. The two customer-facing use cases in the registry scenario work as designed but have measured gaps: diagnostics accuracy is lower for older devices and Manufacturer C consoles, with a small upsell gap by store income area; the chatbot receives passcodes and card numbers and answers Spanish questions less accurately.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the risk and technology committee of the board reviews quarterly.

**Members:** Chief Data and Analytics Officer (chair); Chief Privacy Officer; CISO; Chief Compliance Officer; General Counsel's delegate; Chief Human Resources Officer (for workforce tools); Senior Vice President, Store Operations; Vice President, Customer Experience; Chief Marketing Officer; the data science lead. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Local validation and bias testing on the company's own data; independent bias audit where law requires; impact or risk assessment (including CCPA risk assessment for California); human review design; notices to affected people; monitoring plan; counsel sign-off on state AI and employment laws |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review; claims review for anything said publicly |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.5; STD-05.3). From 2026-10-31, procurement and IT change management block AI features without an inventory ID (POAM-024). The GRC team owns the inventory and runs a quarterly scan of vendor release notes for new AI features.

**Policies:** POL-04 4.9 (no Restricted data in AI tools without committee approval and no-training terms); POL-05 4.5 (approved tools only; register new AI features); POL-01 4.8 (vendor contracts with data-use terms); POL-04 4.3 and 4.5 (passcodes and card numbers never in chat); STD-05.3 (approved AI tools list).

**Claims.** Any public statement about AI performance must be approved by the Chief Marketing Officer and Legal and must rest on the measurements in section 7. The "near perfect" diagnosis wording was removed from signage and the website on 2026-08-21 (P01 R-019).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High and Medium tool; annual re-review of every use case.

**Why 5 use cases lack review.** AI-004, AI-008, AI-010, and AI-011 arrived as vendor features or vendor pilots before the intake block existed; AI-005 predates the committee. The committee set review dates for all five (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45(a)(1) (deception) | **Yes** | AI accuracy claims (AI-001), AI disclosure in chat (AI-002), and add-on suggestions (AI-010) must not mislead. The FTC's "Operation AI Comply" (September 2024 onward) targeted deceptive AI claims (per the cross-sector reference) |
| FTC Act Section 5, 15 U.S.C. 45(n) (unfairness) | **Yes** | Recommending unneeded repairs (AI-001, AI-010) or keeping chat transcripts with passcodes (AI-002) can cause injury customers cannot reasonably avoid |
| State breach and privacy laws (Florida worked example Fla. Stat. 501.171(2), (6)) | **Yes** | Chat transcripts and diagnostic logs can hold personal information; AI vendors that maintain it are third-party agents with a breach notice duty to the company |
| PCI DSS v4.0.1 (contractual) | **Yes, for AI-002 and AI-003** | Card numbers typed into chat or spoken on recorded calls are account data the company must not store (3.2.1, 3.3.1); a chatbot vendor holding them would come into PCI DSS scope |
| Illinois Public Act 103-0804 | **Yes, for AI-004** | Notice to applicants and employees when AI is used; AI with a discriminatory effect, or zip codes used as a proxy, is a civil rights violation. Effective 2026-01-01. Content confirmed only from ilga.gov search snippets (cross-sector reference); counsel confirms |
| NYC Local Law 144 | **Yes, for AI-004 in New York City** | Bias audit within 1 year before use, public summary, and candidate notice 10 business days before use. Ranking has been paused for NYC roles since 2026-07 |
| California CPPA ADMT regulations (11 CCR 7200 and following) | **Yes, for AI-004 from 2027-01-01** | ADMT used for significant decisions, including employment, needs a pre-use notice, opt-out with exceptions, access rights, and a risk assessment; businesses already using it must comply by 2027-01-01. AI-011 would also be covered if re-enabled |
| California Civil Rights Council ADS regulations (2 CCR 11008 and following) | **Yes, for AI-004** | Using an automated-decision system that discriminates is unlawful; anti-bias testing is relevant to defenses; 4-year record retention |
| Colorado SB26-189 | **Yes, from 2027-01-01** | Covers deployers whose ADMT materially influences consequential decisions, including employment, with point-of-interaction notice, post-adverse-outcome explanation, and human review rights. No small-business exemption. Applies to AI-004 for Colorado roles (41 stores, 14 of them AC) and possibly AI-005 and AI-008; counsel decides by 2026-11-30 |
| Title VII of the Civil Rights Act | **Yes, for AI-004 and AI-011** | Disparate-impact liability remains in the statute even though the EEOC's 2023 technical assistance page was removed (cross-sector reference) |
| Texas TRAIGA (Tex. Bus. & Com. Code ch. 551-554) | **Yes, as prohibitions only** | Intent-based prohibitions (for example AI developed with intent to discriminate unlawfully); disclosure duties fall on government agencies and health care service providers, not on the company. No use case is near a prohibition |
| Utah AI Policy Act (Utah Code 13-72 and 13-75, as amended) | **Yes, for AI-002** | Generative AI used with consumers must disclose when clearly asked; disclosure at the outset gives a safe harbor. AI-002 discloses at the start of every chat. The Act's repeal date is 2027-07-01 |
| State recording consent laws | **Yes, for AI-003** | The company applies all-party prior consent for recorded calls everywhere. Florida worked example: interception is lawful when all parties have given prior consent (Fla. Stat. 934.03(2)(d)) |
| Connecticut Public Act 26-15 | **Watch** | Reported to require written notice when AI is used in employment decisions from 2026-10-01; only the attorney general's release was read (cross-sector reference). Counsel confirms before 2026-11-30 |
| FTC AI accuracy policy statement | **Not final** | Proposed 2026-07; tracked only |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person (here, employment) or able to affect physical safety.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | AI-assisted diagnostics (fault and repair suggestions) | Medium | In production at 960 core stores | Reviewed 2026-01-21; re-reviewed 2026-08-26 |
| AI-002 | Customer chatbot (web, app, text) | Medium | In production (about 310,000 chats a month) | Reviewed 2025-08-20; re-reviewed 2026-08-26 |
| AI-003 | Contact center call summarization and agent assist | Medium | In production | Reviewed 2026-03-18 |
| AI-004 | Applicant screening and ranking | High | In production except New York City | Not reviewed (due 2026-11-30) |
| AI-005 | Refund and warranty claim fraud detection | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-006 | Parts demand forecasting | Low | In production | Reviewed 2025-11-12 |
| AI-007 | Device grading and resale pricing for ITAD | Low | In production at Depot Central | Reviewed 2026-05-20 |
| AI-008 | Store workforce scheduling optimization | Medium | Pilot at 120 stores (no Colorado stores) | Not reviewed (due 2026-11-30) |
| AI-009 | Enterprise generative AI assistant (approved tenant) | Medium | In production | Reviewed 2026-04-15 |
| AI-010 | Upsell recommendations at the POS | Medium | Pilot at 80 stores | Not reviewed (due 2026-11-30) |
| AI-011 | Technician productivity scoring | High | Suspended (disabled 2026-08-27) | Not reviewed (due 2026-11-30) |

**Tiering notes:** AI-001 stays Medium because a technician confirms every diagnosis and the customer approves every quote; it would move to High if it produced quotes or declared devices unrepairable without a technician. AI-005 stays Medium only while investigators decide; if flags were used alone for discipline it would be High. AI-008 is Medium pending counsel's view on whether scheduling is a consequential employment decision. AI-009 is Medium rather than Low because Confidential data is allowed in its tenant. AI-007 is Low because it grades sanitized devices with no personal data.

## 5. Employment AI: what must happen before AI-004 continues
| Duty | Source | Status | Action (POAM-009) |
|---|---|---|---|
| Independent bias audit within 1 year before use; public summary | NYC Local Law 144 | Not done; NYC ranking paused | Audit engaged by 2026-10-31; NYC stays paused until the audit summary is published |
| Notice to candidates 10 business days before use (NYC); notice to applicants (Illinois) | NYC Local Law 144; Illinois Public Act 103-0804 | Not given | Notices live in the applicant flow by 2026-11-30 |
| No zip codes as a proxy for protected classes | Illinois Public Act 103-0804 | Vendor confirms the ranking does not use zip codes; not independently tested | Audit to confirm inputs |
| Pre-use notice, opt-out, access, and a risk assessment | California ADMT regulations, from 2027-01-01 | Not ready (P03 G-190) | Build the process or disable ranking for California roles by 2026-12-31 |
| Notice, adverse-outcome explanation, human review | Colorado SB26-189, from 2027-01-01 | Not ready | Same decision as California for Colorado roles by 2026-12-31 |
| Adverse impact analysis | Title VII; California ADS regulations | Not done | Selection-rate ratios by sex and race or ethnicity (where self-reported) in the audit; 4-year records |

## 6. MEASURE: portfolio testing gaps
Local testing exists only for AI-001, AI-002, and AI-003. AI-004, AI-005, AI-008, AI-010, and AI-011 have none. The committee's minimum before any of them stays in production after 2026-11-30: a test plan with metrics, groups, and thresholds, approved at review.

## 7. Full assessments: AI-001 AI-assisted diagnostics and AI-002 customer chatbot
### 7.1 MAP
| Item | AI-001 AI-assisted diagnostics | AI-002 Customer chatbot |
|---|---|---|
| Purpose and intended use | Suggest the likely fault and repair from device diagnostic logs and damage photos, to speed triage | Answer common questions, give ticket status, book appointments, and give price ranges from the published price list |
| Users / operators | About 4,300 store technicians at 960 core stores | Customers on the website, app, and text; contact center agents take over |
| Affected people | About 420,000 devices a month and their owners | About 310,000 chats a month |
| Data | Diagnostic logs (account identifiers stripped since 2026-05) and damage photos | Customer questions; first name and ticket status from the connector; whatever customers type. A 2,000-chat sample found 41 device passcodes and 6 full card numbers |
| Build or buy | Buy: vendor model; contract (2026-01) forbids training on company data and limits retention to 30 days | Buy: vendor model configured with the FAQ and price list; vendor terms still allow use of transcripts "to improve the service" (POAM-017) |
| Not intended | Final diagnosis, automatic quotes, or declaring a device not repairable; use on SL-2 client devices without the client's written consent | Approving refunds, warranty claims, or payment plans; quoting outside the price list; collecting passcodes or payment details |

### 7.2 Risk tier
Both Medium (section 4). Escalation triggers: AI-001 producing quotes without technician confirmation, or use on SL-2 devices without consent; AI-002 approving anything about money or collecting payment details; either vendor starting to train on company data.

### 7.3 MEASURE
**AI-001 diagnostics (6,000 devices sampled, 2026-06 to 2026-08):**
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Agreement between the AI's suggested fault and the technician's confirmed fault; target 85% | 84% overall | **No** (narrowly); acceptable as a triage aid with technician confirmation |
| Safe | Missed battery swelling or liquid damage (safety-relevant) | 11 missed cases, all caught by the mandatory physical inspection | Partial: keep the physical inspection mandatory |
| Secure and resilient | Logs over TLS; vendor access through company SSO | Both in place | Yes |
| Accountable and transparent | Intake screen tells customers that an AI tool assists triage; technician named on every diagnosis | In place at core stores | Yes |
| Explainable and interpretable | Suggestion shows the log entries and photo areas used | Shown | Yes |
| Privacy-enhanced | Account identifiers stripped; no vendor training; 30-day retention | In place since 2026-05 | Yes |
| Fair, with harmful bias managed | Bias plan in 7.4 | Older devices 76% vs 87% for newer; Manufacturer C consoles 71%; upsell rate 6.9% in stores in the lowest-income areas vs 3.9% in the highest (3.0 points) | **No.** Three gaps flagged |

**AI-002 chatbot (400 scripted questions plus a 2,000-chat review, 2026-08):**
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Correct answers on scripted questions (target 95%); zero off-list prices | 94% correct; 3 off-list prices | **No** |
| Safe | No at-home repair instructions that could cause battery or device harm | None found (blocked since 2025-12) | Yes |
| Secure and resilient | Prompt-injection tests (25); connector returns status only | 1 of 25 revealed system instructions; connector returned status only | Partial |
| Accountable and transparent | AI disclosed at the start of every chat; handover to a person on request | Disclosed on web, app, and text (since 2026-05) | Yes |
| Explainable and interpretable | Answers cite the FAQ or price list entry | Citations shown on web and app; not in text messages | Partial |
| Privacy-enhanced | Passcodes and card numbers masked before storage; no vendor training; 30-day retention | No masking; vendor terms allow transcript use; 90-day retention | **No** |
| Fair, with harmful bias managed | Correct-answer rate by language; flag a gap over 5 percentage points | English 95%, Spanish 89% | **No.** Gap flagged |

### 7.4 Bias testing plan (both use cases, quarterly)
| Group compared | Metric | Threshold | Why this group |
|---|---|---|---|
| Device age (4 years or older vs newer) | AI-001 agreement rate; upsell rate | Flag a gap over 5 percentage points | Older devices belong disproportionately to price-sensitive customers; a worse model for them means more wrong quotes for those least able to absorb them |
| Device brand (Manufacturers A, B, C, others) | AI-001 agreement rate | Flag a gap over 5 points | The vendor's training data may favor some brands |
| Store income area (median household income of the store's ZIP code, in quintiles, as a proxy) | AI-001 upsell rate; final price relative to the AI suggestion | Flag a gap over 3 points in upsell rate | Detect whether AI-influenced quotes land harder on some neighborhoods. ZIP code is used only to group stores for testing, never as a model input |
| Customer language (English vs Spanish) | AI-002 correct-answer rate; handover rate | Flag a gap over 5 points | A large share of customers in several states prefer Spanish |

The company does not collect customers' race, ethnicity, or income and will not start collecting them for this test. The proxies are imperfect and are used only to find patterns worth investigating.

### 7.5 MANAGE
**Human in the loop:**
- AI-001 produces a suggestion only. The technician must physically inspect the device, confirm the fault, and record their own diagnosis before any quote. The quote screen shows the technician's diagnosis, not the AI's.
- AI-002 cannot change tickets, approve anything, or collect payment. Customers can ask for a person at any time; staff take over any chat about a complaint, refund, or price not on the list.

**Fixes for the measured gaps:**
- AI-001: the vendor retrains with older-device and Manufacturer C data by 2027-01-31; until then, suggestions for devices 4 or more years old and for Manufacturer C consoles show a low-confidence label. Upsell gap: quotes above the AI suggestion need a store manager's review in the affected stores for one quarter, then retest.
- AI-002: masking of passcodes and card numbers before transcripts reach the vendor, with a warning prompt, by 2026-10-31; contract addendum with no training and 30-day retention by 2026-11-30 (POAM-017); off-list prices blocked; Spanish FAQ reviewed and retested by 2026-12-31.

**Monitoring:** monthly 500-device sample for AI-001 and 300-chat review for AI-002; the quarterly bias plan above, reported to the committee and to the executive risk committee with ER-08 (P01 R-018, R-019, R-063).

**Incidents:** a chat that exposes another customer's data, or a vendor security incident, follows P08 and the vendor's notice terms. A safety-relevant miss by AI-001 is logged and reviewed by store operations.

**Decommissioning:** turn AI-002 off (banner and phone number) and pause AI-001 if a vendor will not sign the data-use terms, if a bias flag stays open two quarters in a row, or if a vendor changes its data-use terms.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High and Medium tool has quarterly performance and fairness metrics (inventory column `monitoring`) reported to the committee; threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse) are logged as SOC or operations events and follow P08 where security or personal data is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts require no training on company data, retention limits, notice of material model changes, and breach notice to the company.
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice, cannot meet legal requirements in time, or change data-use terms; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the committee's recommendation of 2026-08-26:
1. **AI-001:** approved to continue with conditions: low-confidence labels and manager review in affected stores now; vendor retraining by 2027-01-31; retest next quarter.
2. **AI-002:** approved to continue only if masking and the warning prompt are live by 2026-10-31 and the contract addendum is signed by 2026-11-30 (POAM-017). If not, it is switched off.
3. **AI-004:** may continue outside New York City only until 2026-11-30 unless notices are live and the bias audit is under way; ranking for California and Colorado roles is disabled on 2026-12-31 unless the ADMT and SB26-189 processes are ready (POAM-009).
4. **AI-005, AI-008, AI-010:** may continue in current scope until committee review by 2026-11-30; no expansion; AI-008 stays out of Colorado stores until counsel decides.
5. **AI-011:** stays disabled until committee review and an adverse impact analysis are complete.
6. **Intake block:** procurement and change management block AI features without an inventory ID from 2026-10-31 (POAM-024).
