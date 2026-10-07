# AI Use Assessment: Face Verification Add-on at City Hall (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (facilities support contractor operating government buildings) |
| Tier / Vertical | Sole Proprietorship / Government Services and Facilities |
| AI use case | AI-001: face verification (1:1) add-on in the city's cloud access control tenant, at the city hall staff entrance (facial recognition for facility access, the registry default). The city facilities manager asked the owner by email on 2026-08-03 to configure it and to enroll staff from their existing badge photos. Vendor trial on in the tenant from 2026-07-27 to 2026-10-31; no one enrolled |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form. AI 600-1 applies only to AI-002 |
| Assessor and decision | Owner, 2026-08-28; decision 2026-09-04 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases; AI-002 is the consumer chatbot) |

## 1. Who decides (Govern)
The **city** owns the building, the access control system, the vendor contract, and the decision to use face recognition on its employees. At this size the owner builds nothing. **The owner's decision is narrower: whether the owner will configure and operate a third-party AI feature in a customer's system.** POL-01 9.6 requires this assessment and the city's written decision first. A request from the facilities manager by email is not that decision.

## 2. What it does and what it touches (Map)
Two loaned camera readers at the staff entrance would capture a face when a badge is presented and compare it with that badge holder's enrolled template. About 85 city hall staff use the entrance. The request was to **create templates from the badge photos already in the tenant**, without asking staff. Templates would be held in the vendor's platform; the trial terms say nothing about model training, retention, or deletion.

| Rule | Applies? | Why |
|---|---|---|
| Fla. Stat. 501.171 | **Yes, to plan for** | "Personal information" includes a name with "biometric data as defined in s. 501.702" (501.171(1)(g)1.a.(VI)). Section 501.702 covers automatic measurements of biological characteristics used to identify a person but excludes "physical or digital photographs" and data generated from video recordings. Whether templates computed from badge photos or reader camera images are biometric data is **unsettled; counsel to confirm.** The owner treats them as biometric data and itself as a third-party agent (reasonable security, 10-day breach notice to the city) |
| Florida Digital Bill of Rights | **No** | A "controller" under Fla. Stat. 501.702 must have more than $1 billion in global gross annual revenue and also either earn 50% or more of it from online advertising, operate a consumer smart speaker and voice command service, or operate an app store with at least 250,000 applications. The owner meets none of these, and the city is a government |
| Florida public records law | **Yes, for the city attorney** | The biometric exemption covers only friction ridge detail, fingerprints, palm prints, and footprints (Fla. Stat. 119.071(5)(g)); it does not name face templates. Whether another exemption protects them is for the city attorney. As a contractor the owner must keep exempt records confidential and route any request to the city's custodian (119.0701(2)(b)3.; POL-01 8.8) |
| City contract security exhibit | Yes | Templates and match logs are city data: Moderate safeguards, 24-hour incident notice |
| Colorado SB26-189 and other state AI laws | No | Florida only |

## 3. Risk screen
**Tier: High** (repository rubric): it controls physical access to a government facility, it processes data the owner treats as biometric, and repeated false rejections fall on people trying to get to work. It is also P01 **R-014** (Moderate, treatment Avoid).

Main harms the owner would be responsible for as the person configuring it:
- **Uneven false rejections.** Face matching accuracy can differ by age, sex, and race; NIST's face recognition vendor test on demographic effects (NISTIR 8280, December 2019) documented such differences across algorithms. Badge photos taken years ago make this worse.
- **No consent and no notice** if templates are built from badge photos.
- **Unclear retention and vendor use** of templates under trial terms.
- **Possible public disclosure** of templates if no exemption applies.

## 4. Data-sharing rules
1. No templates are created from existing badge photos. Enrollment, if any, is live, voluntary, and after written notice and signed consent collected by the city.
2. The vendor terms must bar training on city templates, encrypt templates, delete each template within 30 days after withdrawal or departure, and give 24-hour incident notice.
3. Match scores and face images stay in the city tenant. The owner keeps no copies on the laptop or in the suite.

## 5. Human review and measurement (Measure, Manage)
If the city decides to go ahead: the badge is always required and the face match is a second factor only; a failed match falls back to badge plus PIN or the reception desk; no match result alone leads to refusal, discipline, or a report to police. Before any staff are enrolled, the city and the vendor agree a measurement plan: false rejection rate overall and by age band, sex, and voluntary self-reported race (reported to the owner only in aggregate), a local impostor test, and a stop rule if any group's false rejection rate is more than 1.5 times the overall rate. The owner reviews the monthly rejection report with the city facilities manager.

## 6. Decision: not configured now (owner, 2026-09-04)
The owner **will not configure AI-001** until all of these are in hand: (1) a written decision from the city manager or a designee, not only the facilities manager; (2) the city attorney's view on 501.171 and the public records status of templates; (3) the vendor terms in section 4; (4) the consent and notice process; (5) the measurement plan in section 5; and (6) a re-run of this assessment. The owner's letter to the city facilities manager setting out these conditions is due 2026-09-15. If the conditions are not met by 2026-10-31, the owner asks the vendor, through the city IT manager, to end the trial and confirm in writing that no templates exist.

**AI-002 (consumer chatbot): allowed with limits.** Tier Low only because no customer data may be entered (POL-01 9.6). The June to August 2026 use with city point lists and a door schedule excerpt broke that rule before it existed; the owner turned off the model-improvement setting, deleted the chat history on 2026-08-12, and reported it to the city IT manager on 2026-08-13 (P01 R-013). Every suggestion is checked against the manufacturer documentation and the city's sequence of operations before any change, and every change still needs the city's approval.
