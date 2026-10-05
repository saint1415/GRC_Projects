# AI Use Assessment: Vibration Analytics with AI Fault Diagnosis (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated industrial equipment repair service) |
| Tier / Vertical | Sole Proprietorship / Critical Manufacturing |
| AI use case | AI-001: vibration analytics SaaS with AI fault diagnosis (SYS-08), trial since 2026-05-04. Adapted from the registry default "Demand forecasting and predictive maintenance": a one-person service business has no demand to forecast with a model; predictive maintenance is the AI use it actually has |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form |
| Assessor and decision | Owner-technician, 2026-09-02; decision 2026-09-11 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases; AI-002 is a consumer generative AI assistant, restricted to Public information) |

## 1. What it does (Map)
Wireless sensors on customer motors send vibration and temperature readings to the vendor's cloud. A vendor-trained model flags likely faults (bearing wear, misalignment, imbalance) on a dashboard and phone app. In the trial, sensors sit on 6 motors at Customer A's plant (winding line and drying oven vacuum pumps) and 4 motors at one local plant. The owner uses the alerts to plan visits and recommend repairs; the customer decides. The model makes no decision about any person and touches no machine control.

The owner accepted click-through trial terms without reading them. They let the vendor **use uploaded data to improve its service**. Uploads include machine and plant names, which Customer A's exhibit treats as Customer A information. **Customer A did not give written consent** (exhibit S1).

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| Customer A exhibit S1 | **Yes** | No Customer A information to a third party, including cloud and AI services other than the owner's email and file storage, without written consent (P03 G-036) |
| Local plant (no written terms) | Courtesy | Ask before continuing; it owns the machines |
| Sector AI rules | No | None identified for critical manufacturing (vertical profile) |
| State AI laws on consequential decisions (for example Colorado SB26-189) | No | No decisions about people in employment, credit, housing, insurance, education, health care, or government services |
| FTC Act Section 5 | Vendor's duty | Applies to the vendor's accuracy claims, not to the owner's use |

## 3. Risk screen (repository rubric)
**Tier: Medium.** The output influences maintenance advice at plants that build grid equipment, but a person makes every decision and the tool cannot act on machines. **Escalation triggers (re-tier to High and reassess):** using a "healthy" prediction to skip or extend scheduled maintenance; connecting the tool to a machine controller or alarm; offering its predictions to customers as a service they rely on.

## 4. Data-sharing rules (Govern)
1. No Customer A data in AI-001 until Customer A consents in writing, and only under the vendor's business plan data addendum that bars using customer data to train or improve models and deletes data within 30 days of a request (POL-01 12.4).
2. Sensor and dashboard names use machine tag numbers, not plant names, where the customer prefers.
3. No program files, drawings, network lists, or passwords go into AI-001 or AI-002.

## 5. Human review of outputs (Measure and Manage)
- **Trial results:** 3 alerts in 4 months. 2 were confirmed with handheld readings (bearing wear on a vacuum pump motor; motor misalignment on the winding line); 1 was a false positive after a sensor came loose. No missed fault is known, but 4 months is too short to judge.
- **Every alert is checked** with a handheld vibration reading or thermal image before the owner recommends work, and the check is noted on the job ticket.
- **A quiet dashboard proves nothing.** Scheduled inspections continue as before.
- **Monitoring:** each quarter, compare alerts with what was found on site; a missed fault or two false positives in a row trigger a review with the vendor.
- **Decommissioning:** on exit, remove the sensors and get written confirmation that the vendor deleted the data.

## 6. Decision: continue with conditions (approved 2026-09-11)
1. Customer A uploads stopped on 2026-09-02 (sensors paused). By 2026-09-30, ask Customer A in writing for consent under the business plan's no-training addendum (P01 R-007).
2. If Customer A consents, move to the business plan before resuming. If it declines or has not answered by 2026-10-31, remove the sensors at Customer A and request deletion of its data, keeping the vendor's confirmation.
3. Ask the local plant whether it agrees to continue.
4. Re-run this assessment before adding sensors at another site or if any escalation trigger occurs.
