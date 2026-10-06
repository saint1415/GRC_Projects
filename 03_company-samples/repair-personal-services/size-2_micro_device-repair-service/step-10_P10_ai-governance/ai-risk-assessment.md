# AI Risk Assessment: Ticketing Platform AI Assistant (Customer Chat and Diagnostic Suggestions)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent electronics and device repair shop) |
| Tier / Vertical | Micro / Other Services (except Public Administration) |
| AI use case | AI-001: the AI assistant built into the ticketing and POS platform (SYS-10), turned on 2026-05-04. Two functions: **(a) customer chat** on the website and by text; **(b) diagnostic suggestions** to technicians |
| Why one use case covers both | The registry default for this vertical is "AI-assisted diagnostics and customer chatbot". At this size both come from one vendor feature, one contract, and one data flow, so they are assessed together, with separate tests and conditions for each function |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessors / date | Shop Manager (owner of the chat function) and Senior Technician (owner of the diagnostic function) with the independent consultant, 2026-08-17 to 2026-08-21 |
| Decision | Owner, 2026-08-31 (section 6) |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owners:** the Shop Manager for customer chat; the Senior Technician for diagnostic suggestions. **Decision authority:** the Owner.
- **Policies that apply:**
  - POL-02 A.5: no terms, no customer data. This covers new features inside existing SaaS.
  - POL-02 A.9: any new tool or feature that touches customer data needs approval.
  - POL-04 4.3: passcodes only in the restricted field; never in notes that other tools read.
  - POL-04 4.8: approved AI tools list; no customer data in public chatbots (AI-002).
- **Approved-tools list:** kept by the Shop Manager in POL-04 4.8. It has one entry, AI-001, approved with the conditions in section 6.
- **Marketing claims:** any public statement about AI performance must be approved by the Owner and backed by the measurements in section 4.
- **Scale for a Micro shop:** there is no AI committee. The Owner, Shop Manager, and Senior Technician review AI use at the monthly security check-in, and before any new AI feature is turned on.

**How the feature started.** The vendor offered the AI assistant as an add-on in April 2026. The Shop Manager accepted the add-on terms in the SYS-01 admin screen on 2026-05-04 and turned on both functions. Nobody read the terms or tested it. That broke the "no terms, no customer data" rule the shop has now written down (P01 R-012; P03 G-026, G-027).

## 2. MAP
| Item | (a) Customer chat | (b) Diagnostic suggestions |
|---|---|---|
| Purpose and intended use | Answer common questions day and night: hours, price ranges from the published price list, booking, and ticket status | Suggest the likely fault and parts from the symptoms and notes on a ticket, to speed up triage |
| Users | Customers on the website and by text; Counter Associates take over conversations | 3 technicians |
| Affected people | About 900 customers a month who chat or text | About 22 tickets a business day, and their owners |
| Data sent to the vendor and its model provider | Customer messages, and the first name and status of a ticket once the customer gives the ticket number and the phone number on file | **The full ticket: symptoms and the free-text notes, which still hold device passcodes and sometimes account passwords (P01 R-002)** |
| What the review found in the data | A sample of 200 conversations (May to August 2026) held 6 device passcodes and 1 full card number typed by customers | Every diagnostic request since 2026-05-04 sent the ticket notes; about 1 in 3 notes held a passcode |
| Vendor terms | The add-on terms let the vendor and its model provider use conversations and ticket content "to improve the service". Retention is not stated. The model provider is not named. The SOC 2 report does not cover the feature (P09) | Same |
| Build or buy | Buy: vendor model, configured with the shop's FAQ and price list | Buy: vendor model; the shop cannot inspect or retrain it |
| Not intended | Approving refunds or warranty claims, quoting outside the price list, diagnosing faults, giving repair-at-home advice, collecting payment details or passcodes. Enabling any of these requires a new assessment | Final diagnosis, automatic quotes, or deciding a device is not worth repairing. A technician always decides |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45(a)(1) (deception) | **Yes** | The website says "AI diagnosis in minutes, right every time" with no test data. The FTC's "Operation AI Comply" (September 2024 onward) and the 2025 Workado order targeted unsupported AI claims (per `00_universal-framework/cross-sector/us-cross-sector-obligations.md`). Customers must also not be misled into thinking they are texting a person |
| FTC Act Section 5, 15 U.S.C. 45(n) (unfairness) | **Yes** | Sending customers' passcodes to an unnamed model provider that may use them "to improve the service", or steering customers to repairs they do not need, can cause injury customers cannot reasonably avoid |
| Fla. Stat. 501.171(2) and (6) | **Yes** | Chat transcripts and ticket notes can hold personal information (an email with a password; a name with a card number). The vendor and its model provider maintain or process it for the shop, so they are third-party agents with a 10-day breach notice duty to the shop. The shop must take reasonable measures to protect that data |
| PCI DSS v4.0.1 (SAQ P2PE eligibility) | **Yes, indirectly** | A SAQ P2PE merchant must not receive account data electronically. A card number typed into the chat is received electronically, which threatens eligibility (P03 G-118) |
| State AI laws (for example Colorado's and Utah's) | **Not today** | Neither function makes or is a substantial factor in a consequential decision (employment, credit, housing, insurance, education, health care, legal, or government services). The shop operates only in Florida. The chat will disclose that it is AI at the start of every conversation regardless. Other states' chatbot disclosure laws were not analyzed |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why not High:** neither function makes or is a substantial factor in a consequential decision about a person, and neither controls anything physical. A technician confirms every diagnosis and the customer approves every quote; staff take over any chat about money beyond the price list.
- **Why not Low:** the chat talks to customers directly and can reveal ticket information; the diagnostic function sends passcodes to an outside model provider; and both influence what customers pay.

**Re-tier to High and reassess if:** the chat starts approving refunds, warranties, or payment plans, or takes payment details; diagnostic suggestions produce quotes without technician confirmation or declare devices not worth repairing; the vendor starts training on shop data under new terms; or the shop uses it for business accounts' devices without the account's written consent.

## 4. MEASURE
Tests ran 2026-08-19 to 2026-08-21: 60 scripted customer questions, 10 prompt-injection attempts, a review of 200 real conversations, and 100 diagnostic suggestions compared with the technician's confirmed fault.

**(a) Customer chat:**
| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Correct answers to 60 scripted questions; prices must match the price list | 88% correct; 4 answers quoted prices not on the list | **No.** Target 95% and zero off-list prices |
| Safe | No advice that could damage a device or hurt someone | 1 answer told a customer to charge a swollen phone "to check if it still works" | **No.** Block battery and repair-at-home advice |
| Secure and resilient | Status only after ticket number and phone number match; 10 prompt-injection attempts | 1 of 10 attempts (posing as staff) got the status and first name for a ticket number without the phone check | **No.** Vendor fix and retest required |
| Accountable and transparent | AI disclosed at the start; a person on request | Website says "Chat with us" with no AI disclosure; text replies carry none; handover works when asked | **No** |
| Explainable and interpretable | Answers point to the FAQ or price list entry used | Not shown | Partial (acceptable for this use if prices are locked to the list) |
| Privacy-enhanced | Passcodes and card numbers masked before they reach the vendor; no training on shop data; 30-day retention | No masking; training allowed; retention unknown | **No** |
| Fair, with harmful bias managed | Compare correct-answer rates for English and Spanish questions; flag a gap over 5 percentage points | English 91% (45 questions); Spanish 80% (15 questions). Small sample, but flagged | **No (flagged)** |

**(b) Diagnostic suggestions:**
| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | First suggestion matches the technician's confirmed fault | 71% of 100 tickets | **No** for the website claim ("right every time"). Acceptable as a triage aid with technician confirmation |
| Safe | Safety-relevant faults (swollen battery, liquid damage) not missed | 2 swollen batteries not flagged; both caught by technicians at physical inspection | Partial: keep the mandatory physical inspection |
| Secure and resilient | Only symptoms needed for diagnosis are sent | The whole ticket, including notes with passcodes, is sent | **No** |
| Accountable and transparent | Technician's name on every diagnosis; customers told an AI tool assisted triage | Technician named; customers not told | Partial |
| Explainable and interpretable | Suggestion shows which symptoms it used | Symptoms shown; whether notes were used is not shown | Partial |
| Privacy-enhanced | No passcodes or account passwords sent; no training on shop data | Passcodes sent with every request; training allowed by the terms | **No** |
| Fair, with harmful bias managed | Compare agreement for devices 4 or more years old against newer devices; flag a gap over 5 points. Watch the upsell rate (AI suggested a costlier repair than the confirmed one) | Older devices 58% vs newer 76%; upsell rate 7% | **No (flagged)** |

**Bias finding.** Older devices belong disproportionately to price-sensitive customers, and many of the shop's customers prefer Spanish. A worse result for either group means more wrong quotes or wrong answers for the people least able to absorb them. The samples are small, so the shop treats both gaps as real until larger samples or vendor data show otherwise. The shop does not collect customers' race, ethnicity, or income and will not start; device age and language are used as imperfect proxies only to look for patterns worth fixing.

## 5. MANAGE
**Data protection:**
- **Turn off diagnostic suggestions now.** They stay off until the restricted passcode field is in use and the historical notes are purged (POAM-011), so no passcode can reach the model provider, and until the vendor confirms in writing that the feature sends symptoms only.
- Data-use addendum with the vendor: no training or service improvement using shop data, including in de-identified form; 30-day retention of conversations, then deletion; the model provider named and bound to the same terms; breach notice to the shop within 72 hours (well within the 10 days in Fla. Stat. 501.171(6)); deletion of all shop data held so far (POL-02 A.5; POAM-014).
- Mask anything that looks like a card number or passcode before a chat message reaches the vendor, if the vendor setting allows; otherwise show a warning and a staff handover when a customer starts typing one (POL-04 4.3 and 4.5).

**Human in the loop:**
- The chat cannot change tickets, approve anything, or take payment. Customers can type "person" at any time; staff also take over any chat about a complaint, a refund, a price not on the list, a battery, or liquid damage.
- Diagnostic suggestions (once back on) are suggestions only. The technician must physically inspect the device, confirm the fault, and record their own diagnosis before any quote. The quote screen shows the technician's diagnosis, not the AI's.

**Claims:**
- Remove "AI diagnosis in minutes, right every time" from the website now. Any future claim must state what was measured (for example "our technicians confirm every diagnosis; the AI's first suggestion matched in 71% of 100 repairs in August 2026") and be refreshed quarterly.

**Monitoring:**
- Monthly: 30 random conversations reviewed for wrong prices, unsafe advice, and typed passcodes or card numbers; once diagnostics resume, 30 suggestions compared with confirmed faults.
- Quarterly: the English and Spanish comparison and the device-age comparison, reported at the security check-in with P01 R-012.
- Customer complaints mentioning the chat or AI diagnosis go to the Shop Manager.

**Incident handling:** a chat that reveals another customer's ticket, or a vendor security incident, is handled under POL-03 and the P08 runbook (route B). A card number found in a chat transcript is handled under POL-04 4.5.

**Decommissioning:** turn off the whole add-on if the vendor will not sign the data-use addendum by 2026-10-31, if the phone-number check fails a retest, if a bias flag stays open two quarters in a row, or if the vendor changes its data-use terms. Ask the vendor and model provider to confirm deletion of all shop data.

## 6. Decision
**Approve customer chat with conditions; suspend diagnostic suggestions.** Owner, 2026-08-31.

Diagnostic suggestions were turned off on 2026-08-31. Customer chat may stay on **only if** these are done by 2026-10-31; if not, it is turned off that day:
1. AI disclosure at the start of every conversation, on the website and by text.
2. The vendor fixes and the shop retests the phone-number check (10 of 10 prompt-injection attempts refused).
3. Price answers come only from the price list; battery, liquid-damage, and repair-at-home questions hand over to staff.
4. Passcode and card-number masking or warning (this also protects SAQ P2PE eligibility before the SAQ is signed on 2026-12-15).
5. The data-use addendum signed (R-012; POAM-014).
6. The website claim removed (by 2026-09-30).
7. Spanish answers reviewed and the FAQ translated; Spanish retested.

Diagnostic suggestions may be turned back on only after POAM-011 closes, the vendor confirms symptoms-only processing in writing, the addendum is signed, and a 30-ticket retest shows at least 75% agreement with no missed safety faults. The older-device gap must be raised with the vendor, with a written response by 2026-11-30.
