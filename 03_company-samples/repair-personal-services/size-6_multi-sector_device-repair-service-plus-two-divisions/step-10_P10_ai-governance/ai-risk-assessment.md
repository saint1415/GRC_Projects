# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Device Repair, Electronics Retail, IT Support Services, corporate) |
| Tier / Vertical | Multi-Sector / Other Services (except Public Administration) (focus division: Device Repair) |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the rules that apply to three priority use cases: AI-assisted diagnostics (AI-002, Device Repair), the group customer chatbot (AI-001, shared by all divisions), and the AI remediation agent (AI-008, IT Support) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), fieldwork 2026-08-17 to 2026-08-28; presented to the board risk committee 2026-09-10 |
| Inventory | `ai-use-case-inventory.csv` (11 use cases: 1 High, 8 Medium, 2 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Device Repair chief operating officer, Electronics Retail chief digital officer, IT Support managed services director. Approves High-tier use cases, the approved-tools list, and any AI that acts on customer systems |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage, agent permissions) |
| Group Chief Privacy Officer | Data use, retention, vendor no-training terms, IT Support's business associate duties with the IT Support Privacy Official |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026, under POL-01 4.12)
1. **Register before use.** Every AI use case that touches customer data or device data, interacts with customers, or acts on customer systems is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: the council approves; a pre-deployment impact assessment, bias testing, notice to affected people, and quarterly monitoring are required.
3. **No terms, no data** (POL-01 4.8; POL-04 4.10). AI vendors sign terms that prohibit training on group or customer data and limit retention. Vendors that handle ePHI for IT Support sign a subcontractor business associate agreement first. Free-text ticket notes never go to an AI service.
4. **Claims follow evidence.** No marketing claim about an AI feature's accuracy or capability unless the council has the measurements behind it (FTC Act Section 5).
5. **Agents need a leash.** AI that acts on systems (not just advises) runs under a scoped role, an allow list, human approval for anything beyond read-only checks, and a tested kill switch (POL-02 4.8).
6. **Change gate.** A material change (new model, new provider, new decision role, new action type) triggers re-assessment before release, including the SOC 2 system description impact for IT Support.
7. **Approved tools only** for workforce generative AI (POL-05 4.6). **No facial recognition anywhere in the group.**

**Where the program fell short in 2026.** The standard was adopted after AI-001 and AI-002 were already live. The diagnostics marketing claim was never reviewed, the chatbot keeps passcodes customers paste, and the AI agent started without the change gate (scenario gap 7). All three are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Group customer chatbot | Group (all divisions) | Medium | In production; conditions |
| AI-002 | AI-assisted diagnostics (liquid damage flags) | Device Repair | High | In production; conditions |
| AI-003 | Trade-in condition grading | Electronics Retail | Medium | In production |
| AI-004 | Parts demand forecasting | Device Repair | Low | In production |
| AI-005 | Return fraud scoring | Electronics Retail | Medium | In production; condition |
| AI-006 | Personalized recommendations and offers | Electronics Retail | Medium | In production |
| AI-007 | Contact center agent assist | Group | Medium | In production |
| AI-008 | AI remediation agent | IT Support | Medium | Pilot (40 customers); expansion paused |
| AI-009 | Technician knowledge assistant | IT Support | Low | Approved |
| AI-010 | Enterprise generative AI assistant | Group | Medium | Pilot (3,000 users) |
| AI-011 | Ticket note summarization | Device Repair | Medium | Proposed; not approved |

### 2.1 AI-assisted diagnostics (AI-002): consumer protection and partner rules
| Rule or commitment | What it means for the model |
|---|---|
| FTC Act Section 5, deception (15 U.S.C. 45(a)(1)) | "AI-verified diagnostics" on the website and in stores is a claim the group cannot substantiate (P03 G-108). Withdrawn by 2026-10-15; any future claim must rest on section 4.1 measurements. The FTC's proposed AI accuracy policy statement (Docket FTC-2026-0727, July 2026) is not final and is tracked only |
| FTC Act Section 5, unfairness (15 U.S.C. 45(n)) | A wrong liquid damage flag shifts the cost of a repair to a customer who cannot see or avoid the error. The 9.5% overturn rate in section 4.1 makes this a live risk, not a theoretical one |
| TPA repair network agreement (contract) | Claim coverage decisions must rest on the technician's documented findings. A model flag accepted without photo evidence does not meet that standard |
| Manufacturer A and B program terms (contract) | Warranty voids for liquid damage must follow the manufacturers' indicator rules; the model is an aid, not the basis |
| Fla. Stat. 501.171(2) (worked example) | The model's payload includes free-text notes that can contain passcodes and account passwords (POAM-018) |
| State AI decision laws | The repository rubric treats insurance-like coverage decisions as consequential, so the group tiers AI-002 High as a precaution. The group operates in no state whose comprehensive AI decision law it has identified as applying (it has no operations in Colorado); counsel reviews each year |

### 2.2 Group customer chatbot (AI-001): one bot, three divisions
| Rule or commitment | Implication |
|---|---|
| FTC Act Section 5 | Answers about repair status, returns, warranties, and subscriptions must be accurate; the bot must not claim abilities it does not have |
| Fla. Stat. 501.171(2) and (1)(g)1.b. (worked example) | Transcripts that hold a passcode with an email, or an account password, are personal information under the statute and need reasonable security; better not to keep them at all |
| Division duties | Repair status answers draw on the STPP; order answers on retail systems; subscription answers on IT Support systems. Each division owns the accuracy of its content, and the group owns the bot |
| Disclosure | The bot says it is automated at the start of every chat and offers a human; this meets the repository rubric for Medium tier and the bot disclosure laws some states have |

### 2.3 AI remediation agent (AI-008): business associate and customer commitments
| Rule or commitment | Implication |
|---|---|
| 45 CFR 164.308(a)(1)(ii)(A) | The agent must be in IT Support's risk analysis before it touches any practice system (P03 IT-G01) |
| 45 CFR 164.308(b)(1); 164.314(a)(2)(iii); 164.504(e)(2)(ii)(D) | The model provider sees endpoint telemetry and script output, which can include ePHI at practices. It needs a subcontractor business associate agreement with the same restrictions (IT-G13, IT-G26) |
| SOC 2 commitments (CC2.3, CC3.4, CC8.1, CC9.2) | The agent runs inside the current SOC 2 period (it started 2026-07-06); it must be described, and its changes and its model provider controlled (P09) |
| 16 CFR 314.4(f) (customers' duty) | Accounting and tax firm customers must oversee their service providers; they will ask what the agent does on their systems |
| Managed services contracts | Changes to customer systems follow the agreed change process; an agent action is a change |

## 3. Risk tiers (repository rubric)
- **High:** AI-002 (a substantial factor in protection plan coverage and warranty decisions; tiered High as a precaution because the outcome works like an insurance decision for the customer).
- **Medium:** AI-001, AI-003, AI-005, AI-006, AI-007, AI-008, AI-010, AI-011. They interact with customers, use customer data, or act on customer systems, but a human makes or can reverse the final decision.
- **Low:** AI-004, AI-009.

**Re-tier triggers:** letting AI-001 approve refunds or claims (to High); letting AI-005 block returns without review (to High); letting AI-008 act without human approval beyond read-only checks or on practice clinical systems (to High); any use of AI for employment decisions about the workforce (to High, and a new assessment).

## 4. MEASURE
Results are from monitoring and audits between 2026-05 and 2026-08.

### 4.1 AI-assisted diagnostics (AI-002)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Suggested diagnosis matches the technician's final diagnosis (2,400 tickets; target 90%) | 86% overall; 71% for devices more than 4 years old | **No** |
| Valid and reliable | Liquid damage flags overturned on second review with indicator photos (1,200 flags; target under 3%) | 9.5% | **No** |
| Safe (automation bias) | Share of flags accepted without photo evidence (target 0%) | 97% | **No** |
| Fair, harmful bias managed | Overturn rate by device age band; flag if a band is more than 3 points above the overall rate | Devices more than 4 years old: 14.1% vs 9.5% overall | **Flagged.** Older devices are more often owned by customers who cannot easily absorb a voided claim |
| Accountable and transparent | Customers told that AI assists diagnostics, and offered an appeal | Not told; no appeal path | **No** |
| Secure and privacy-enhanced | Payload limited to logs and photos | Notes included (POAM-018) | **No** |

**Impact estimate.** About 41,000 protection plan claims were denied for liquid damage in the 12 months to 2026-07-31. At a 9.5% overturn rate, about 3,900 customers may have been wrongly denied coverage. The council treats this as a customer harm to remediate, not only a model metric.

### 4.2 Group customer chatbot (AI-001), using AI 600-1 risk areas
| AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Confabulation | Incorrect answers in 400 sampled transcripts (target under 2%) | 4.5% (mostly warranty and return policy answers) | **No** |
| Data privacy | Share of chats where customers pasted a passcode or password; retention | 1.8% of chats; transcripts kept 2 years | **No** |
| Information security (prompt injection and data access) | Red-team test of status lookups (2026-08) | Lookups require the ticket or order number and the phone number on file; no cross-customer disclosure found | Yes |
| Human-AI configuration | Handoff to a human on request; disclosure at chat start | In place | Yes |
| Value chain and component integration | Vendor terms: no training on transcripts; retention limits | No-training term in place; retention not limited | **Partial** |

### 4.3 AI remediation agent (AI-008)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Safe | Actions that caused a service disruption (1,900 actions in 6 weeks; target under 0.1%) | 0.4% (8 disruptions, 2 of them at accounting firms; all rolled back within 1 hour). No practice is in the pilot | **No** |
| Accountable and transparent | Every action logged with customer, endpoint, script, and outcome | In place | Yes |
| Secure and resilient | Agent role limited to allow-listed script types; kill switch | Scoped role in place; kill switch not yet tested | **Partial** |
| Human oversight | Human approval for actions beyond read-only checks | None today | **No** |
| Privacy-enhanced | Subcontractor agreement with the model provider | Not signed | **No** |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-002:** a liquid damage flag that affects coverage needs indicator photos in the ticket and a second technician's sign-off; the model's flag is shown after the technician records their own finding. Customers are told AI assists diagnostics and can ask for a review at any store.
- **AI-001:** the bot never asks for passcodes or passwords and tells customers not to share them; passcode patterns are redacted before storage; policy answers come only from approved content; customers can reach a human at any point.
- **AI-008:** read-only checks run automatically; any change needs technician approval in the RMM; scripts on practice systems need the practice's change window; the kill switch is tested each quarter.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-10, DR-012, DR-013, DR-027, ER-010, IT-005.

**Incident handling:** AI failures that harm customers, expose customer data, or disrupt customer systems follow P08 and POL-03. A model provider incident is handled as a vendor incident under the matrix (third-party agent and business associate rows).

**Decommissioning:** each use case has an off switch and a fallback (manual diagnostics with manufacturer tools, human agents, technician-run scripts) that the BIA already covers (P05 BP-DR09, BP-IT05).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-002 AI-assisted diagnostics | **Continue with conditions** (council, 2026-08-28; board risk committee informed 2026-09-10) | Claim withdrawn by 2026-10-15 (POAM-021); photo evidence and second sign-off for coverage-affecting flags by 2026-10-31; re-review with the TPA of the 41,000 liquid damage denials from the last 12 months, and remediation for customers wrongly denied, by 2027-03-31; customer notice and appeal path by 2026-11-30; notes removed from the payload by 2026-10-31 and vendor terms amended by 2026-12-31 (POAM-018); monthly accuracy by device model and age band from 2026-11 |
| AI-001 group customer chatbot | **Continue with conditions** | Passcode redaction and 90-day retention by 2026-11-30 (POAM-018); policy answers limited to approved content by 2026-12-31; monthly accuracy sampling with a 2% target |
| AI-008 AI remediation agent | **Continue the pilot for 40 customers; pause expansion** | Human approval beyond read-only checks by 2026-10-31; no practice enrolled until the subcontractor agreement is signed and the risk analysis updated (POAM-024); kill switch test by 2026-11-30; SOC 2 description and customer notice (POAM-025) |
| AI-005 return fraud scoring | **Continue with a condition** | Manager review of every blocked return at all stores by 2026-12-31 (ER-010) |
| AI-011 ticket note summarization | **Not approved** | Revisit after the notes purge (POAM-002) |
| AI-003, AI-004, AI-006, AI-007, AI-009, AI-010 | **Approved** | Standard monitoring; AI-010 prohibited for decisions about customers or employees |
