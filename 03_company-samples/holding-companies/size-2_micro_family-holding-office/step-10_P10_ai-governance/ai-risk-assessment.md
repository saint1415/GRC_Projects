# AI Risk Assessment: Generative AI Assistant in the Shared Tenant

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (family holding company and single-family office) |
| Tier / Vertical | Micro / Management of Companies and Enterprises |
| AI use case | AI-001: generative AI assistant add-on in the productivity suite (SYS-10), 4-user pilot since 2026-06-15, paused on 2026-07-23 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | Family Office Director (Qualified Individual) with the Investment Director and the Office Manager, 2026-09-08 |
| Decision | Principal, 2026-09-18 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## Why this use case
This is the registry's "enterprise generative AI assistant across subsidiaries" at Micro size. The assistant is licensed only to office staff, but it works inside the one tenant that holds the subsidiaries' board packs and monthly financial packages and every family's records. Whatever a user can open, the assistant can read, summarize, and repeat. So the question is less about the model and more about what each user can reach.

## 1. GOVERN
- **Accountable owner:** the Family Office Director. **Decision authority:** the Principal.
- **Policies that apply:**
  - POL-04 4.6: no new tool, including AI, receives office information until it passes the new-tool checklist and is on the approved-tools list. The assistant is approved only under the conditions in section 6.
  - POL-02 B.2 and POL-04 4.3: need-to-know access by family branch and subsidiary; Restricted family documents only in the vault. These are what keep the assistant's reach small.
  - POL-02 C.2: no office information in unapproved AI tools, including free public chatbots (AI-003).
- **Scale for a Micro office:** there is no AI committee. The Family Office Director, Investment Director, and Office Manager review AI use at the monthly security meeting, and the Principal decides.
- **Safeguards Rule hooks.** The assistant is an externally developed application that accesses customer information, so the office must have a procedure to evaluate its security (16 CFR 314.4(c)(4)). Its vendor is a service provider the office must oversee (314.4(f)). Access to customer information must be limited to what each user needs (314.4(c)(1)(ii)).

**How the pilot started and stopped.** The Office Manager turned on the add-on for 4 users on 2026-06-15 after a vendor promotion. Nobody reviewed what the users could reach. On 2026-07-22 the Executive Assistant asked it to "summarize this week's family updates", and the answer included a trust distribution memo for one adult child that the Executive Assistant had no need to see. The memo was in the Family site, which every staff member can open. The Family Office Director paused the pilot on 2026-07-23 (P01 R-004).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Summarize subsidiary monthly packages and board packs; draft letters, meeting notes, and first drafts of investment memos; find documents in the Office and Subsidiaries sites |
| Users | 4 pilot users: Family Office Director, Controller, Investment Director, Executive Assistant |
| Affected people | Family members (their records may be read and summarized), subsidiary managers and employees (named in board packs), household and office employees (payroll data in reach of some users) |
| Data | Inputs: prompts and any file or email the user can open in SYS-02. Outputs: summaries and drafts saved in the user's mailbox or files. The enterprise add-on's terms say prompts and files are not used to train the vendor's models and stay within the tenant's service boundary |
| Build or buy | Buy: an add-on to the existing productivity suite; no plugins, connectors, or agents enabled |
| Not intended | Investment decisions or recommendations to family members; anything about employment of subsidiary or household staff; tax positions; drafting payment instructions. These are prohibited uses; enabling any of them requires a new assessment |

**Applicable rules:**
| Rule | Applies? | Why |
|---|---|---|
| FTC Safeguards Rule, 16 CFR 314.4(c)(1)(ii), (c)(4), (f) | **Yes** | The assistant reaches customer information; access must be need-to-know, the application must be evaluated, and the vendor overseen |
| Florida Information Protection Act, Fla. Stat. 501.171(2) | **Yes** | Reasonable measures for personal information the assistant can read. Good-faith access by an employee is not a breach when the information is not misused (501.171(1)(a)), which is why the July 2026 event needed no notice; misuse or disclosure outside the office could be |
| Advisers Act family office exclusion, 17 CFR 275.202(a)(11)(G)-1 | **Watch** | Drafts of investment memos must go only to family clients. Sending AI-drafted investment material to a subsidiary manager or other non-family person could weaken the exclusion (POL-02 A.10, C.6) |
| Federal or state AI laws on consequential decisions | **No today** | The assistant makes no decision about employment, credit, housing, insurance, or similar matters. No federal AI rule specific to holding companies was identified. Recheck if any employment or tenant-related use is ever proposed |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why not High:** the assistant does not make, and is not a substantial factor in, a consequential decision about a person. Staff decide, and investment and employment uses are prohibited.
- **Why not Low:** it reaches regulated data (customer information and Florida personal information) and influences business decisions (subsidiary oversight and investment memos).

**Re-tier to High and reassess if:** it is used for any decision about subsidiary or household employees; it drafts recommendations sent to family members without review; agents or connectors are enabled to act (send email, move files, touch bill pay); or it is extended to subsidiary guests.

## 4. MEASURE
The Family Office Director and the Investment Director ran 24 test prompts on 2026-09-04 in a test account set up with the planned need-to-know permissions, and compared results with the same prompts from a pilot account with the old, broad permissions. Results map to the AI 600-1 risk categories.

| Trustworthy characteristic (AI 600-1 risk) | Test or metric | Result | Pass? |
|---|---|---|---|
| Privacy-enhanced (Data Privacy) | 8 prompts seeking SSNs, passport numbers, trust terms, or medical bills of a family branch the test user does not serve; target 0 disclosures | Old permissions: 6 of 8 returned Restricted content. New permissions: 0 of 8 | **No** with old permissions; Yes with new |
| Valid and reliable (Confabulation) | 6 summaries of subsidiary monthly packages checked against the source figures; target 0 wrong figures | 2 of 6 summaries misstated a figure (one gross margin, one debt covenant ratio) | **No** |
| Secure and resilient (Information Security) | Prompt-injection test: a document with hidden instructions placed in the Subsidiaries site | The assistant repeated the hidden text in a summary but took no action (no agents enabled) | Partial |
| Accountable and transparent (Human-AI Configuration) | Drafts labeled as AI-assisted; a named person reviews before anything leaves the office | No labeling; one AI-drafted letter to a family member was sent in July without review | **No** |
| Information integrity | Summaries cite the source document | Summaries link the source files | Yes |
| Value chain (Value Chain and Component Integration) | Vendor terms on training use, retention, and subprocessors reviewed | Enterprise terms: no training on customer data; prompts kept with the mailbox; subprocessors listed by the vendor | Yes |
| Fair, with harmful bias managed (Harmful Bias or Homogenization) | Not material for the intended uses (no decisions about people); prohibited uses would need a bias test first | Not tested | Not applicable while uses are limited |

**Key finding.** The privacy failures came from permissions, not from the model. With need-to-know permissions the assistant returned nothing it should not. The confabulation rate on financial figures means every number in an AI summary must be checked against the source before it reaches the Principal, a Board, or a lender.

## 5. MANAGE
**Data protection:**
- **Permissions first.** The pilot may restart only after the Family site is split by family branch, Restricted family documents are moved to the vault (which the assistant cannot reach), and each subsidiary's folder is limited to its own guests and the staff who oversee it (POAM-005).
- Sensitivity labels on estate, tax, medical, and payroll folders that block the assistant from reading them, as a second layer.
- No plugins, connectors, web grounding on internal content, or agents. Any change requires a new assessment.
- The Executive Assistant's pilot license is not renewed: the role does not need summaries of family financial matters.

**Human in the loop:**
- The assistant produces drafts only. A named staff member reviews every output before it is used, and checks every figure against the source.
- Nothing AI-drafted goes to a family member, a subsidiary, a custodian, or a lender without that review, and drafts carry a short "prepared with AI assistance" footer until sent.
- The assistant is never used to draft or approve payment instructions.

**Monitoring:**
- Monthly: 5 sampled summaries checked for wrong figures and for Restricted content; results logged against P01 R-004.
- Quarterly: the prompt-leakage test from section 4 repeated after any permission change.
- The SYS-02 audit log of assistant use is part of the monthly log review (POL-02 B.11).

**Incident handling:** an AI output that discloses Restricted information to someone without a need to know is an incident under POL-03 and is logged; if it leaves the office, the breach decision in P08 applies.

**Decommissioning:** turn off the add-on if the need-to-know restructure slips past 2026-12-31, if a Restricted disclosure recurs after restart, or if the vendor changes its data-use terms. Ask the vendor to confirm deletion of prompts and outputs on exit.

## 6. Decision
**Approve with conditions.** Principal, 2026-09-18.

The pilot stays paused and may restart for 3 users (Family Office Director, Controller, Investment Director) only when all of these are met:
1. The need-to-know restructure of the Family and Subsidiaries sites is complete and the leakage test passes with 0 disclosures (target 2026-10-31; POAM-005).
2. Sensitivity labels block the assistant from estate, tax, medical, and payroll folders.
3. The prohibited uses and the review rule are written into the approved-tools list (POL-04 4.6) and acknowledged by the 3 users.
4. The monthly sampling in section 5 is assigned to the Family Office Director.

Extension to more users or to subsidiary guests requires three consecutive months with no Restricted disclosure and no unreviewed external output, plus a new assessment.

**Related action for AI-002.** The investment platform's AI-drafted commentary stays off until the Investment Director tests it on two quarters of reports and confirms it never states figures that differ from the platform's own numbers. Due before the 2027 Q1 reports.
