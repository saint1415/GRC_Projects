# AI Use Assessment: Generative AI Assistant (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (specialty chemical distributor, broker) |
| Tier / Vertical | Sole Proprietorship / Chemical |
| AI use case | The generative AI assistant (SYS-08, paid individual plan), used since 2026-03. **AI-001:** office drafting (customer and supplier emails, quote letters, summaries of supplier notices). **AI-002:** drafting hazmat shipping descriptions for BOLs and reading hazard classes from SDS text |
| Why not the registry default | The registry default, a process-optimization model, needs a process. This business runs none. The assistant is the one AI tool the owner uses, and its hazmat-description use is the safety-relevant case |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 (Generative AI Profile) for the generative AI risks |
| Assessor and decision | Owner, 2026-09-18 (the model-improvement setting was turned off that day); decision adopted 2026-10-05 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases, one tool) |

## 1. What it does (Map)
The owner types or pastes text into the vendor's chat service and copies the answer into an email, a quote, or, until this assessment, the BOL. The vendor's general-purpose model runs in the vendor's cloud. The owner accepted click-through terms. Until 2026-09-18 the setting that lets the vendor use chats to improve its models was **on**, so chats with customer names, prices, and SDS text may already have been used. That cannot be undone. A review of the chat history on 2026-09-18 found **no** driver license numbers, pickup numbers, schedules, or bank details.

**Relevant AI 600-1 risks:** confabulation (a confident but wrong packing group), data privacy (business data kept by the vendor), human-AI configuration (trusting a fluent draft), information security (the AI account itself), and value chain (the vendor can change its terms). CBRN information risk is not engaged: the owner does not ask the assistant about reactivity, mixing, or hazards beyond the SDS, and this assessment keeps it that way.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| DOT HMR shipping papers, 49 CFR 172.201, 172.202, 172.204 | **Yes (AI-002)** | The BOL must show the identification number, proper shipping name, hazard class with any subsidiary class, and packing group from the 172.101 table (172.202(a)). The owner signs the shipper's certification that the material is "properly classified, described" (172.204(a)(1)). A tool cannot take on that duty |
| DOT HMR training, 49 CFR 172.702(b) | **Yes** | A hazmat employee may not perform a function "unless instructed in the requirements" for it. Classifying and describing is the owner's trained function, not the tool's (P03 G-014) |
| Fla. Stat. 501.171(2) and (1)(g) | **Yes, as a data rule** | Driver names with license numbers are personal information. They must never go into the assistant. The chats held business names and prices, not personal information, so no breach notice duty arose |
| Supplier distribution agreements | Contract | Supplier prices and terms are business confidential. They stay out of any tool whose terms let the vendor train on them (POL-01 9.4) |
| CFATS RBPS 27.230(a)(8) (C-CHEMICAL-R01) | Voluntary benchmark | Release and shipment data (pickup numbers, schedules, tracking links) stay out of external services that are not needed to move the load |
| State AI laws (Colorado SB26-189, California CPPA ADMT rules, Texas HB 149) | No | No AI use makes or influences a consequential decision about a person, and the business sells only in Florida and south Georgia |
| FTC Act Section 5 | No (today) | The business makes no claims about AI to customers |

## 3. Risk screen (repository rubric)
- **AI-002, hazmat descriptions: High.** The rubric puts AI that "can affect physical safety or critical infrastructure operations" in the High tier. A wrong description misleads carriers and emergency responders about a Division 5.1 or Class 8 load. It already happened once: in 2026-05 an AI-drafted ferric chloride entry showed Packing Group II instead of III, and only the supplier's shipping clerk caught it (P01 R-005, Moderate after the supplier's check).
- **AI-001, office drafting: Medium.** Drafts go to customers and suppliers and can carry product facts they rely on, and the prompts hold confidential prices. The owner makes every final decision and nothing is decided about a person (P01 R-012, Low).

## 4. Tests on 2026-09-18 (Measure)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | All 7 hazmat descriptions the assistant drafted from 2026-03 to 2026-08, checked against the 172.101 table; the UN2014 description requested in 5 new chats | 1 of 7 wrong (ferric chloride PG II). In 1 of 5 new chats the UN2014 entry left out the subsidiary class (8) | **No** for AI-002 |
| Safe | Acceptable error rate for a shipping description: zero, without relying on a supplier's catch | 2 errors in 12 outputs | **No** for AI-002 |
| Secure and resilient | Account protection; data settings | Password only; model-improvement setting on until 2026-09-18 | Partial |
| Accountable and transparent | One accountable person signs every email and BOL | Owner | Yes |
| Explainable and interpretable | Every product fact in a draft can be traced to the SDS or the product description sheet | Not done before this assessment | Partial |
| Privacy-enhanced | Chat history review for Restricted data (POL-01 8.1) | None found; customer prices and SDS text found | Partial |
| Fair, with harmful bias managed | Is the tool used in any choice about a person or a customer (credit, new-customer checks, carrier choice)? | No. Kept out of those uses by rule 4 below, so there is no group to compare | Not applicable |

## 5. Data-sharing rules (Govern)
These rules apply POL-01 9.4 to this tool.
1. **Never in the assistant:** driver names or license numbers, pickup numbers, load schedules, tracking links, bank details, credentials, HSP-01 content, or end-use statements.
2. **Customer prices and supplier terms:** not until the account is on a plan whose terms bar the vendor from training on business data (by 2026-10-31, R-012). If no such plan is available, the ban stays.
3. **Public SDS text and product brochures** may be used to draft a cover email. The customer always gets the manufacturer's SDS itself, never an AI summary in its place.
4. **Not used** for hazmat descriptions, hazard classes, or packing groups (AI-002), new-customer or ship-to verification, credit decisions, or carrier choice.
5. The model-improvement setting stays off. The owner checks the data settings each quarter and whenever the vendor announces new terms.

## 6. Human review of outputs (Manage)
- The owner reads every draft in full before it is sent. Any concentration, hazard, handling, or compatibility statement is replaced with text copied from the manufacturer's SDS or the product description sheet.
- BOL descriptions come only from the locked product description sheet, checked against the 172.101 table (POL-01 8.2; due 2026-10-31).
- **Incidents.** An AI-caused error found on a BOL is corrected with the supplier before pickup. If the load has left, the owner calls the carrier and the ERI provider and logs the event (POL-01 10.2). A suspected takeover of the AI account follows the P08 runbook's steps for other accounts.
- **Stop using the tool** if the vendor's terms no longer let the owner turn off training, if an AI error reaches a customer or a shipping paper again, or at the end of the plan. When stopping, export what is needed and delete the chat history.

## 7. Decision (adopted by the owner 2026-10-05)
- **AI-002: prohibited** from 2026-10-05 (POL-01 9.4). It is not to be reconsidered for hazmat descriptions.
- **AI-001: approved with conditions:**
  1. rules 1 to 5 above;
  2. a unique passphrase in the password manager, with MFA if the plan offers it, by 2026-10-15;
  3. the move to a plan with no-training terms by 2026-10-31.

Re-assess each September with the POL-01 review, or sooner if the tool, plan, terms, or use changes.
