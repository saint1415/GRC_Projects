# AI Use Assessment: Generative AI Assistant Across the Three LLCs (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (sole proprietorship) and its LLCs: Storage, Rentals, Laundry |
| Tier / Vertical | Sole Proprietorship / Management of Companies and Enterprises |
| AI use case | AI-001: the generative AI assistant add-on to the productivity suite (SYS-10), turned on 2026-06-01 for the owner's account only |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 for generative AI risks |
| Assessor and decision | Owner-manager, 2026-07-30 (with the P01 risk assessment); decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does and what it can reach (Map)
The assistant drafts and summarizes email and documents, and answers questions about anything in the owner's mailbox and files. Because the owner's account is the back office for all four entities, **the assistant can read every LLC's mail and files at once**: rental applications with SSNs and screening reports, Storage driver license scans, new-hire forms, leases, and the books. It is a business-plan add-on from the suite vendor; the vendor's business terms say prompts and files are not used to train its models (a contract term the owner has read, not tested). Uses so far (the owner's own account of six weeks):
- drafting Storage delinquency reminders, laundromat signs, and rental listings;
- summarizing leases and vendor contracts;
- **on 2026-07-14, summarizing six rental applications for unit 4B, including their screening reports, and asking which applicant to choose.** The owner chose an applicant two days later.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| Fair Housing Act, 42 U.S.C. 3604 | **Yes** (Rentals) | It is unlawful to refuse to rent or to discriminate in terms because of race, color, religion, sex, handicap, familial status, or national origin (3604(a)-(b), (f)), or to publish a listing that indicates such a preference (3604(c)). The statute applies to the decision whatever tool helped make it. Neither 3603(b) exemption fits Rentals |
| FCRA, 15 U.S.C. 1681b(f) and 1681m(a) | **Yes** (Rentals) | Screening reports may be used only for the permissible purpose (the application). If a decline rests in whole or in part on a report, the applicant gets an adverse action notice, whatever tool was involved |
| FTC Disposal Rule, 16 CFR 682.3 | **Yes** (Rentals) | Copies of screening reports created by prompts or downloads are consumer information that must be disposed of properly |
| Fla. Stat. 501.171(2) | **Yes** (each LLC) | Putting Restricted data into a tool the owner has not assessed is not a "reasonable measure." The suite vendor already holds this data under the same contract, so this is a handling issue, not a new disclosure |
| State AI laws (for example Colorado SB26-189) | **No** | The LLCs operate only in Florida; no Florida statute on private-sector AI use was identified. Recheck each July |

## 3. Risk screen (repository rubric)
**As it was used on 2026-07-14: High.** Choosing a tenant is a housing decision, a consequential decision under the rubric, and the assistant was asked to be a factor in it.
**As it will be used under the conditions below: Medium.** It drafts messages that reach tenants and customers, but makes and influences no decision about a person, and every output is read before use.

**Unit 4B check (2026-07-30).** The owner wrote tenant selection criteria (income, rental history, screening result) and re-checked the 4B decision against them. The chosen applicant met all three; the two declined applicants each failed the screening criterion and received the platform's adverse action notice on 2026-07-16. The owner saved the assistant's answer to the unit 4B file in the property management platform, to be kept with the declined applications for 2 years (POL-01 8.7). **No evidence of a prohibited basis was found, but the practice stops now.**

### Generative AI risks (NIST AI 600-1) that apply
| Risk | How it shows up here | Control |
|---|---|---|
| Data Privacy | One prompt can pull another LLC's Restricted data (an applicant's SSN into a Storage draft) | Restricted folders excluded from the assistant (POL-01 8.2) |
| Harmful Bias and Homogenization | A ranking of applicants could reflect a protected trait or a proxy for one | No AI in applicant, tenant, customer, or employee decisions (POL-01 9.5) |
| Confabulation | A wrong lease date or fee in a drafted notice | Owner checks every date, amount, and name against the source |
| Information Integrity | A listing that "prefers" a type of tenant (42 U.S.C. 3604(c)) | Owner reads every listing word for word |

## 4. Data-sharing rules (Govern)
1. Only the suite's assistant (SYS-10) is approved. No other AI tool may be used with business data (POL-01 9.5).
2. No Restricted data (SSNs, license numbers, screening reports, bank details, passwords) in prompts, and Restricted files live only in folders the assistant cannot read, one per LLC.
3. One LLC's Confidential data is not used in another LLC's drafts.
4. Agent features that send mail or change files stay off.

## 5. Human review of outputs (Measure and Manage)
The owner reads every output before it is sent or saved; checks every name, date, amount, and address against the source; reads every rental listing against 3604(c); and never pastes an output into a tenant selection, adverse action, or employment record. Once a month, during the POL-01 7.7 review, the owner opens the assistant's activity history and checks that no prompt contained Restricted data. A slip is logged as an incident under POL-01 10.2.

## 6. Decision: approve with conditions (2026-08-31)
Keep the assistant for drafting and summarizing, **on these conditions** (P01 R-009, due 2026-09-30):
1. Move the application folder, license scans, and new-hire forms into restricted folders excluded from the assistant, then delete what the retention schedule says to delete (POL-01 8.7).
2. Never use it to rank, screen, or choose any applicant, tenant, customer, or employee.
3. Re-run this assessment before turning on any new AI feature, connecting it to an LLC system, or letting LLC staff use it.

**Related action (AI-002):** by 2026-11-30, ask the screening partner what its accept, decline, or conditional recommendation is based on, record the answer, and confirm the written criteria, not the recommendation alone, decide every application.
