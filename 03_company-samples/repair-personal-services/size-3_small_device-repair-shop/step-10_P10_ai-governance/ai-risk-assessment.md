# AI Risk Assessment: AI-Assisted Diagnostics and Customer Chatbot

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (electronics and device repair service) |
| Tier / Vertical | Small / Other Services (except Public Administration) |
| AI use cases | AI-001: customer chatbot (live since 2026-03). AI-002: AI-assisted diagnostics (pilot at the Depot and Store A since 2026-06) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) for AI-001 |
| Assessors / date | Customer Experience Manager (AI-001) and Operations Manager (AI-002) with the IT Manager, 2026-08-17 to 2026-08-21 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |
| Decision | General Manager, 2026-09-04 (section 6) |

## 1. GOVERN
- **Accountable owners:** Customer Experience Manager (AI-001), Operations Manager (AI-002). **Decision authority:** General Manager for Medium-tier use cases; majority owner if any use case is re-tiered High.
- **Policies that apply:**
  - POL-04 4.9: no Restricted or Confidential data in AI tools without approval and signed data-use terms
  - POL-05 4.9: approved tools only; never paste customer data, passcodes, or device photos into unapproved tools
  - POL-01 4.8: vendor review and contract terms (including no model training on company data) before any vendor receives customer data
- **Approved-tools list:** kept by the IT Manager. Today it lists AI-001 and AI-002 only, both conditionally (section 6).
- **Marketing claims:** any public statement about AI performance must be approved by the Customer Experience Manager and backed by the measurements in section 4.
- **Scale for a Small company:** no AI committee. The two owners, the IT Manager, and the General Manager review AI use cases quarterly, and before any new AI feature is turned on.

## 2. MAP
| Item | AI-001 Customer chatbot | AI-002 AI-assisted diagnostics |
|---|---|---|
| Purpose and intended use | Answer common questions, give ticket status, book appointments, and give price ranges from the published price list, day and night | Suggest the likely fault and repair from device diagnostic logs and damage photos, to speed up triage |
| Users / operators | Customers on the website and by text; counter staff take over conversations | Technicians at the Depot and Store A (12) |
| Affected people | About 1,900 customers a month who chat | About 140 devices a week in the pilot, and their owners |
| Data | Customer questions; first name and ticket status returned by the connector function. **A sample of 500 chats found 9 device passcodes and 2 full card numbers typed by customers.** Vendor terms allow use of transcripts "to improve the service"; transcripts are kept indefinitely | Diagnostic logs (can include device name, account identifiers, and installed app names) and photos. Vendor terms are silent on retention and training |
| Build or buy | Buy: vendor model, configured with the company's FAQ and price list | Buy: vendor model; the company cannot inspect or retrain it |
| Not intended | Approving refunds or warranty claims, quoting outside the price list, diagnosing faults, collecting payment details or passcodes. Enabling any of these requires re-assessment | Final diagnosis, automatic quotes, or deciding whether a device is "not repairable". A technician always decides |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45(a)(1) (deception) | **Yes** | The website says "AI-powered diagnosis, 99% accurate" with no test data. The FTC's "Operation AI Comply" (September 2024 onward) targeted deceptive AI claims (per `00_universal-framework/cross-sector/`). Customers must also not be misled into thinking they are chatting with a person |
| FTC Act Section 5, 15 U.S.C. 45(n) (unfairness) | **Yes** | Recommending unneeded or more expensive repairs, or keeping chat transcripts with passcodes, can cause injury customers cannot reasonably avoid |
| Fla. Stat. 501.171(2) and (6) | **Yes** | Chat transcripts can hold personal information (for example an email with a password). Both vendors maintain or process personal information for the company, so they are third-party agents with a 10-day breach notice duty to the company |
| PCI DSS v4.0.1 (SAQ P2PE eligibility) | **Yes, indirectly** | A SAQ P2PE merchant must not receive account data electronically. Card numbers typed into the chat are received electronically, which threatens eligibility (P03 G-118) |
| State AI laws (for example Colorado SB26-189, Texas TRAIGA, Utah AI disclosure rules) | **Not today** | Neither use case makes or materially influences a consequential decision (employment, credit, housing, insurance, education, health care, government services). The company operates in Florida; some mail-in customers live elsewhere, so the chatbot discloses that it is AI at the start of every chat regardless. Other states' chatbot disclosure laws were not analyzed |

## 3. Risk tier
**Both use cases: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why not High:** neither makes or is a substantial factor in a consequential decision about a person, and neither affects physical safety. A technician confirms every diagnosis and the customer approves every quote; staff take over any chat about money beyond the price list.

**Why not Low:** both interact with customers or influence what they pay, and both handle customer data through outside vendors.

**Escalation triggers (re-tier and re-assess):**
- AI-001 approves refunds, warranty claims, or payment plans, or collects payment details
- AI-002 produces quotes without technician confirmation, or declares devices unrepairable
- Either vendor starts training on company data
- Use for business accounts' devices without the account's written consent

## 4. MEASURE
**AI-001 chatbot (scripted test of 200 questions plus review of 500 real chats, August 2026):**
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Correct answers on 200 scripted questions; price ranges must match the price list | 91% correct; 6 answers quoted prices not on the list | **No.** Target 95% and zero off-list prices |
| Safe | No instructions that could damage a device or cause battery harm | 1 answer suggested heating a phone to remove a screen at home | **No.** Block repair-at-home instructions |
| Secure and resilient | Prompt-injection tests (10); connector returns status only | Connector returned status only; 2 of 10 injection prompts made the bot reveal its internal instructions | Partial |
| Accountable and transparent | Chat discloses AI at the start; handover to a person on request | Disclosure present on the website, missing on text messages | **No** |
| Explainable and interpretable | Answers cite the FAQ or price list entry used | Citations shown on the website only | Partial |
| Privacy-enhanced | Passcodes and card numbers masked before storage; no vendor training on company data; 30-day transcript retention | No masking; training allowed by vendor terms; indefinite retention | **No** |
| Fair, with harmful bias managed | Compare correct-answer rates for English and Spanish chats; flag a gap over 5 percentage points | English 93%, Spanish 84% | **No.** Gap flagged |

**AI-002 diagnostics (pilot data, June to August 2026, 1,640 devices):**
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Agreement between the AI's suggested fault and the technician's confirmed fault | 78% overall | **No** for the website claim of 99%. Acceptable as a triage aid with technician confirmation |
| Safe | Missed battery swelling or liquid damage (safety-relevant) | 4 missed cases, all caught by technicians | Partial: keep mandatory physical inspection |
| Secure and resilient | Logs sent over TLS; vendor account uses company SSO | TLS confirmed; local vendor accounts without SSO | Partial |
| Accountable and transparent | Customer told that an AI tool assisted triage; technician name on every diagnosis | Not disclosed to customers | **No** |
| Explainable and interpretable | Suggestion shows the log entries and photo areas it used | Log entries shown; photo areas not shown | Partial |
| Privacy-enhanced | Account identifiers stripped from logs before upload; vendor retention limited | Not stripped; vendor terms silent | **No** |
| Fair, with harmful bias managed | See the bias testing plan below | Devices over 4 years old: 64% agreement vs 81% for newer devices. Manufacturer B laptops: 69%. Upsell rate (AI suggested a costlier repair than the confirmed one) 6% overall | **No.** Two gaps flagged |

**Bias testing plan (both use cases, quarterly):**
| Group compared | Metric | Threshold | Why this group |
|---|---|---|---|
| Device age (4 years or older vs newer) | AI-002 agreement rate; upsell rate | Flag a gap over 5 percentage points | Older devices belong disproportionately to price-sensitive customers; a worse model for them means more wrong quotes for those who can least absorb them |
| Device brand (Manufacturer A, Manufacturer B, others) | AI-002 agreement rate | Flag a gap over 5 points | The vendor's training data may favor some brands |
| Customer language (English vs Spanish) | AI-001 correct-answer rate; handover rate | Flag a gap over 5 points | A large share of the company's Florida customers prefer Spanish |
| Store (by the median household income of the store's ZIP code, as a proxy) | AI-002 upsell rate; final repair price relative to the AI suggestion | Flag a gap over 3 points in upsell rate | Detect whether AI-influenced quotes land harder on some neighborhoods |

The company does not collect customers' race, ethnicity, or income, and will not start collecting them for this test. The proxies above are imperfect and are used only to look for patterns worth investigating.

## 5. MANAGE
**Human-in-the-loop design:**
- AI-001 cannot change tickets, approve anything, or collect payment. Customers can type "person" at any time; staff also take over any chat that mentions a complaint, refund, or a price not on the list.
- AI-002 produces a suggestion only. The technician must physically inspect the device, confirm the fault, and record their own diagnosis before any quote. The quote screen shows the technician's diagnosis, not the AI's.

**Data protection:**
- Mask passcodes and card numbers in chat before they reach the vendor; show a warning when a customer starts typing a number that looks like either (links to POL-04 4.3 and 4.5).
- Contract addenda for both vendors: no training on company data, 30-day retention, deletion on request, breach notice within 72 hours (POL-01 4.8; POAM-017).
- Strip account identifiers from diagnostic logs before upload (vendor setting).

**Claims:**
- Remove "99% accurate" from the website now. Any future accuracy claim must state what was measured (for example "the tool's first suggestion matched our technicians' diagnosis in 78% of devices in our 2026 pilot") and be refreshed quarterly.

**Monitoring:**
- Monthly: 50 random chats reviewed; 100 diagnostics compared with confirmed faults.
- Quarterly: the bias testing plan above, reported to the General Manager with the risk register (P01 R-011, R-012, R-028).
- Customer complaints mentioning the chatbot or AI diagnosis are routed to the use-case owner.

**Incident handling:** a vendor security incident, or a chat that exposes another customer's data, follows P08 and the vendor's notice terms.

**Decommissioning:** turn AI-001 off (website banner and phone number) and stop AI-002 if the vendor will not sign data-use terms by 2026-11-30, if a bias flag stays open two quarters in a row, or if the vendor changes its data-use terms.

## 6. Decision
**Approve both with conditions.** General Manager, 2026-09-04.

AI-001 may stay live **only if** these are done by 2026-10-31:
1. AI disclosure at the start of every chat, including text messages.
2. Passcode and card-number masking and the warning prompt (also closes a SAQ P2PE eligibility risk before the SAQ is signed).
3. Off-list price answers blocked and at-home repair instructions removed.
4. Spanish answers reviewed and the FAQ translated; the Spanish gap retested.

AI-002 may continue the pilot at the Depot and Store A **only if**:
1. The "99% accurate" claim is removed by 2026-09-30.
2. Technician confirmation before quoting is enforced in the workflow.
3. Account identifiers are stripped from uploads.

Expansion of AI-002 to Stores B to D requires the vendor addendum signed (POAM-017), two consecutive months at or above 80% agreement, and no open bias flag. The older-device and Manufacturer B gaps must be raised with the vendor, with a written response by 2026-11-30.
