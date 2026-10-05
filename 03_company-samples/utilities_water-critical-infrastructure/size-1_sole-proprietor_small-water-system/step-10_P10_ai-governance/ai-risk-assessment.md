# AI Use Assessment: Portal Anomaly Alerts for Water Quality (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (small community water system) |
| Tier / Vertical | Sole Proprietorship / Water and Wastewater Systems |
| AI use case | AI-001: the remote access portal's anomaly alert feature (SYS-08), a third-party machine-learning model that flags unusual residual, flow, tank level, and pump run-time patterns. Free trial, turned on 2026-06-01 without review |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form. AI 600-1 applies only to AI-002 (generative) |
| Assessor and decision | Owner-operator, 2026-08-24; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
The portal already collects process data from the panel every few minutes. The feature learns the plant's normal daily pattern and sends a push alert to the owner's phone when a reading drifts, for example a chlorine residual falling while flow is steady, or a pump running longer than usual. It **reads** data only; it cannot change a setpoint. It uses no personal information. The click-through terms let the vendor use customer data to improve its models.

In its first 12 weeks it sent 9 alerts: 6 were normal events (well rotation, a hydrant flushing day), 2 were real (a weak hypochlorite batch and a sticking check valve, both already caught on the daily visit), and 1 was a dropped cellular signal.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| 40 CFR 141.403(b)(3)(i)(B) | **Yes, as a limit** | Compliance monitoring is the daily grab sample at peak flow. An alert, or the absence of one, never replaces it |
| 40 CFR 141.404(c) and 141.405(a)(1) | **Yes, as a limit** | The 4-hour clocks start when the operator determines the residual or 4-log treatment is not being maintained. An alert is a prompt to check, not a determination |
| SDWA section 1433 | Voluntary only | The monitoring-practices element (300i-2(a)(1)(A)(iii)) is used as a checklist; it does not bind this system (P03 G-020) |
| Consequential-decision AI laws | No | The tool makes no decision about any person |

## 3. Risk screen (repository rubric)
**Tier: High.** The rubric puts any AI that "can affect physical safety or critical infrastructure operations" in the High tier. The feature is advisory and read-only, but its output steers when the owner goes to the well house. The real risk is **over-reliance**: skipping a check because no alert came (P01 R-010). The minimum High-tier controls are applied in proportion: human review before any action (section 5), a validation period before trust grows (section 5), this assessment as the impact assessment, and ongoing monitoring of alert quality. Notice to affected people is not needed, because no decision is made about a person. Bias testing across groups of people does not apply to process data; it is replaced by the validity check in section 5.

**AI-002** (consumer chat assistant for letters) is **Low**: internal drafting, no decisions, and no customer data entered. Its AI 600-1 risks (confabulated facts, wrong health-effects language) are handled by the rule that public notices come only from the primacy agency's templates.

## 4. Data-sharing rules (Govern)
1. The feature receives process data only. No customer data, credentials, or network details go to any AI tool (POL-01 9.5).
2. Opt out of model training if the vendor allows it; otherwise record the terms in the vendor list and recheck at each renewal (POL-01 6.5).
3. The feature must never be given write access to the panel. If the vendor offers "auto-correct" or setpoint suggestions that apply themselves, they stay off.

## 5. Human review of outputs (Measure and Manage)
- **Every alert is checked** at the panel or with the field test kit, and the check is written in the operating log with the alert time.
- **No alert means nothing.** The daily site visit and grab sample happen whether or not the feature is quiet.
- **Validity check for 90 days (to 2026-11-30):** compare each alert with what the owner found, and each daily grab sample with whether an alert fired. Keep the feature only if it catches real problems the owner would otherwise have found later, at a false-alarm rate the owner can live with.
- **Stop rule:** if the feature misses a residual drop that the grab sample finds, or the vendor changes the terms to need write access, turn it off and re-run this assessment.

## 6. Decision: keep, advisory only (approved 2026-08-31)
**Keep AI-001 as an advisory tool**, with these conditions, by 2026-09-30 (P01 R-010):
1. Opt out of model training if offered, or record the terms.
2. Start the alert log in the operating log and run the 90-day validity check.
3. Add the stop rule and "no alert means nothing" to the manual-operation sheet so the relief operator follows them too.

**AI-002:** continue for non-regulatory letters only. Public notices come from the primacy agency's templates, and no customer data goes into the tool.
