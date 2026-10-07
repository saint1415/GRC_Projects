# AI Use Assessment: Dynamometer Card Analysis Service with Failure Prediction (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated oilfield services contractor) |
| Tier / Vertical | Sole Proprietorship / Mining, Quarrying, and Oil and Gas Extraction |
| AI use case | AI-001: predictive maintenance for customers' rod-pumped wells through a third-party cloud dynamometer card analysis service (SYS-08). In use since March 2026 for 14 wells of Customers A and B |
| Why this tool | The registry's default use case is a predictive maintenance model for well equipment. A one-person contractor cannot build one, so this assessment covers the third-party predictive maintenance tool the owner actually uses |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form |
| Assessor and decision | Owner-operator, 2026-08-25; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
The owner downloads dynamometer cards (load against position for each pump stroke) and run times from customers' rod pump controllers, by cable on site or through Customer A's SCADA exports, and uploads them to the service. A machine learning model classifies each card (for example fluid pound, gas interference, worn pump, rod part) and scores the chance of a pump failure in the next 30 days. The owner uses the results to recommend pump changes or well servicing; the customer decides whether to send a pulling unit, which costs the customer thousands of dollars per job. The service also offers an **automatic optimization feature** that can push setpoint changes (for example pump-off idle time) to the controllers from the cloud. It has never been turned on.

The inputs are customer production data, confidential under the MSAs. The provider's standard terms allow it to use uploaded data to improve its models; a paid tier offers a no-training option. **Customer A never gave written consent** for the uploads, which its MSA requires (MSA-A (5)).

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| Customer A MSA security schedule item (5) | **Yes** | No disclosure of Customer A data to third parties, including software services, without written consent |
| Customer B MSA confidentiality clause | **Yes** | Customer information is confidential; the clause does not mention service providers, so the owner asks Customer B too |
| Federal or Florida AI rules | None identified | The vertical research found no sector AI rules, and the tool makes no decision about a person, so state consequential-decision laws on AI do not reach it |
| Safety and environmental duties | Indirectly | A wrong recommendation or an automatic setpoint change could upset a well or tank battery; customers keep their safety and spill duties (P08 matrix) |

## 3. Risk screen (repository rubric)
**Tier: Medium as used.** The tool influences business decisions (which wells get serviced), but a human makes every decision and the tool cannot act on equipment. **The automatic optimization feature would make it High**, because the AI could then change critical infrastructure operations directly. That feature stays off and is prohibited (POL-01 9.6). Main risks, rated with the P01 method in R-009 (Moderate): disclosure of customer data and use for model training; wrong classifications leading to needless or missed well work; and over-reliance on scores on wells whose conditions the model has not seen (high-water-cut, gassy wells).

## 4. Data-sharing rules (Govern)
1. No upload of Customer A or Customer B data until that customer gives written consent, or the account is on the no-training tier and the customer is told (POL-01 6.3).
2. Wells are uploaded under owner-assigned codes, not lease or well names; the code list stays in the password manager notes.
3. MFA on the account (available on the paid tier) and deletion of all data on request when a customer's MSA ends (POL-01 8.7).
4. **AI-002 (free chatbot):** no customer names, well names, or numbers. Summaries are drafted with placeholders and filled in by the owner.

## 5. Human review of outputs (Measure and Manage)
- **Every flagged well** is checked against the raw card and on the next round (fluid level, sound, stroke counter) before the owner recommends work. The recommendation to the customer states that it is based on the tool plus the owner's check.
- **No setpoint change** follows from a tool output without the customer approver's email approval and a change log entry (POL-01 8.4).
- **Accuracy tracking:** for each well serviced, the owner records whether the pulled pump matched the tool's classification. After 10 jobs, if fewer than 7 match, the owner stops recommending work on the tool's score alone and tells the customers. No testing was done before adoption.
- **Bias and fairness testing** in the AI RMF sense does not apply: the tool makes no decision about people. The equivalent check is whether it performs worse on some well types; the tracking log records well type for that reason.

## 6. Decision: continue with conditions (approved 2026-08-31)
By 2026-09-30 (P01 R-009):
1. Ask Customers A and B in writing for consent to the uploads, explaining the provider's terms. If either declines, move to the no-training tier (about $300 a year more) or stop that customer's uploads and ask the provider to delete them.
2. Switch to well codes and turn on MFA.
3. Keep the automatic optimization feature off; re-run this assessment before any change to that.
4. AI-002: no customer data, ever. The owner reviewed the chatbot account's settings on 2026-07-24, turned off chat history, and deleted the earlier chats.
