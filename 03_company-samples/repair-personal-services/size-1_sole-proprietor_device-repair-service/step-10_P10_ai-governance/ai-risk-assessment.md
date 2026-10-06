# AI Use Assessment: Generative AI Assistant at the Repair Bench (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (electronics and device repair service) |
| Tier / Vertical | Sole Proprietorship / Other Services (except Public Administration) |
| AI use case | AI-001: a general-purpose generative AI assistant (SYS-12, consumer plan) used since 2026-02 to suggest likely faults and to draft customer messages. This adapts the registry default ("AI-assisted diagnostics and customer chatbot") to the one AI tool a one-person shop actually uses. The vendor chatbot add-on (AI-002) was trialed and not adopted; it is in the inventory only |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 for generative AI risks |
| Assessor and decision | Owner-technician, 2026-08-03; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
At the bench, the owner types symptoms, pastes device error logs, and uploads photos of screens or boards, and the assistant suggests likely faults and test steps. At the counter, it drafts text messages explaining a quote or a delay. The owner reviewed the chat history on 2026-08-03: **212 chats; 31 included customer first names, 9 included ticket notes copied with device passcodes, and 14 included screen photos, 3 of them showing a customer's notifications.** The consumer terms let the vendor use chats to train its models, and that setting was on. The vendor offers a business plan whose terms exclude training on customer content.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45(n) (unfairness) | **Yes** | Sending customers' passcodes and personal content to a vendor that may train on them, and recommending repairs on an unchecked AI suggestion, can cause injury customers cannot avoid or see |
| FTC Act Section 5, 15 U.S.C. 45(a)(1) (deception) | **Yes, if the shop makes claims** | The website does not mention AI today. Any future "AI diagnosis" claim must be true and measured (POL-01 9.8) |
| Fla. Stat. 501.171(2) | **Yes** | Reasonable measures for personal information the shop holds; pasting it into a consumer tool is not one |
| State AI laws (for example Colorado SB26-189) | **Not today** | No consequential decision (employment, credit, housing, insurance, education, health care, government services). The owner makes every repair decision |

## 3. Risk screen (repository rubric)
**Tier: Medium.** The assistant influences what repair and price a customer is quoted and drafts messages customers read, but the owner makes every decision and sends every message. It would be Low only if no customer data went in and no customer saw its output. **No tier allows customer personal data in a tool that trains on it** (POL-01 9.7).

## 4. Data-sharing rules (Govern)
1. Training setting off (done 2026-08-03) and chat history deleted (requested 2026-08-03).
2. No customer names, contact details, passcodes, account details, or ticket notes in prompts. Use the device model and symptoms only.
3. Photos are cropped to the fault area; never a screen showing messages, photos, or notifications.
4. By 2026-09-30, move to the business plan with no-training terms and a retention limit, or stop using the tool for shop work (P01 R-009; POAM-008).

## 5. Human review of outputs (Measure and Manage)
The owner compared the assistant's first suggestion with the confirmed fault on 40 recent tickets: **27 matched (68%)**. Two suggestions were unsafe (heating a swollen battery to remove it; bypassing a charging protection circuit). So:
- **Every suggestion is a hypothesis.** The owner inspects and tests the device and confirms the fault before quoting; the quote names the confirmed fault, not the AI's.
- **Safety rule:** for batteries, charging circuits, and liquid damage, follow the device maker's repair documents, never an AI instruction.
- **Messages:** the owner reads, edits, and sends every customer message personally; no AI message goes out unedited, and prices come only from the shop's price list.
- **Monitoring:** each month, compare 10 suggestions with confirmed faults and log the match rate and any unsafe suggestion. Stop using it for diagnosis if the match rate falls below 60% for two months or an unsafe suggestion is followed.
- **Fairness check (scaled to one person):** no data on customers' characteristics is collected or used. The monthly sample includes older devices, where wrong suggestions would cost price-sensitive customers most; if older devices match noticeably worse, the owner relies on the assistant less for them.

## 6. Decision: continue with conditions (approved 2026-08-31)
AI-001 may be used only under section 4 and section 5. If the business plan is not in place by 2026-09-30, use stops and the account is closed with a deletion request (POL-01 6.4). Any incident involving AI chat data follows P08.

**AI-002 (vendor chatbot add-on):** not adopted. The 14-day trial (2026-05-05 to 2026-05-19, 41 chats) quoted prices not on the price list in 5 chats, received device passcodes in 3, and never told customers they were chatting with AI. Transcript deletion was requested from the vendor on 2026-08-03. Re-assess before any future use.
