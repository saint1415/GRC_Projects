# AI Risk Assessment: Predictive Maintenance for Well Equipment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer, one field) |
| Tier / Vertical | Micro / Mining, Quarrying, and Oil and Gas Extraction |
| AI use case | AI-001: the SCADA vendor's predictive maintenance add-on for rod pumps, in pilot on 8 of the 16 producing wells since May 2026 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook. The Generative AI Profile (AI 600-1) is not used for AI-001, which is not generative; it informs the rules for AI-002 |
| Assessor / date | Office Manager (Security Coordinator) with the Owner and the Field Superintendent, 2026-08-25 |
| Decision | Owner, 2026-08-31, with the Field Superintendent's agreement |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

**Adapted to this size.** The registry default for this vertical is a predictive maintenance model for well equipment. A 7-person producer does not build models, so here the same use case is a **vendor add-on** to the SCADA cloud service the company already uses (SYS-08). The questions change from "is our model good" to "what does the vendor's model see, what can it do, and what did we agree to".

## 1. GOVERN
- **Accountable owner and decision authority:** the Owner, who started the pilot. The Field Superintendent must agree to anything that affects field operations.
- **How the pilot started:** in May 2026 the Owner accepted the SCADA vendor's offer of a free 6-month trial of the add-on for 8 wells, in the vendor's web portal, with no review and no change to the subscription terms (gap 13 in `../00_company-facts.md`). During this review, on 2026-08-25, the Owner found that the vendor had also enabled its "auto-optimize idle time" feature on 2 of the 8 wells. The feature changed pump-off idle-time setpoints 11 times in July, within limits the vendor set, through the connector on the SCADA host. Nobody at the company had approved it. The Owner turned it off on 2026-08-26.
- **Policies that apply:**
  - POL-02 A.5: no security terms, no vendor access or Restricted data
  - POL-02 B.10: no cloud service may send commands or setpoints to field controllers
  - POL-04 4.6: approved AI tools only; this add-on is approved for pump-off controller data in advisory mode
  - POL-02 C.2: no Restricted data in public AI chatbots (AI-002)
- **Approved-tools list:** kept by the Office Manager in POL-04 4.6. Today it lists AI-001 (advisory only). An enterprise generative AI tool for AI-002 will be added once chosen.
- **Scale for a Micro company:** there is no AI committee. The Owner, Office Manager, and Field Superintendent review AI use at the monthly security meeting and whenever the vendor announces a feature change.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Flag rod pumps likely to fail within about 2 weeks (rod parts, worn pumps, gas interference) so the Owner can book the contract pulling unit before the well stops, and point the Lease Operators to wells that need a closer look |
| Users | The Owner and the Field Superintendent read the alert list in the vendor portal |
| Affected parties | Field operations (pulling unit bookings, route priorities); royalty owners and partners indirectly (production). No decisions about individuals |
| Data | Dynamometer cards, motor load, run time, and pump-off events from the 8 pilot wells, sent by the SYS-08 connector. **No personal information.** The vendor's standard terms let it use customer data, in aggregated form, to improve its models across customers; well performance data is commercially sensitive to the partners |
| Build or buy | Buy: the vendor trains and runs the models. The company cannot inspect them; the vendor provides a short model description and per-alert explanations |
| Connection to OT | **Was two-way, now one-way.** Until 2026-08-26 the connector accepted setpoint writes from the cloud for 2 wells. It is now send-only, and the Field Technician checks the setting monthly |
| Not intended | Changing controller settings; deciding shut-ins; deferring checks of safety equipment (H2S monitors, high-level switches, SWD high-pressure shutdown); judging Lease Operators' work. Each requires a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Sector AI rules (oil and gas) | No | None identified for this vertical (`02_industry-rules/mining-oil-gas/overlay.md`) |
| State AI laws on consequential decisions | No | The add-on makes no decision about a person. No Florida AI statute applicable to this use was identified in the repository's cross-sector research |
| Fla. Stat. 501.171 | Not today | No personal information is used. It would apply if staff names, phone locations, or other personal data were added |
| FTC Act Section 5 | Indirectly | Applies only to claims the company makes about the tool, for example to partners. Describe it honestly as a vendor's advisory tool |
| Joint operating agreements and the vendor's subscription terms | Yes | The partners' well data goes to the vendor; the terms on data use, feature changes, and deletion **are not yet negotiated** (P03 GV.SC-06) |

## 3. Risk tier
**Tier: Medium, on condition that write-back stays off** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why it was High until 2026-08-26.** The rubric puts AI that "can affect physical safety or critical infrastructure operations" at High. With write-back on, the vendor's model was changing pump-off settings on live wells. Pump-off settings are not safety settings, and the hardwired shutdowns were unaffected, but the model was acting on field equipment with no human approval. That is the High case.

**Why Medium now.** With the connector send-only, the add-on only reorders a list that a person reads. If it misses a failure, the result is the same as before the pilot: the pump fails, the Lease Operator finds the well down on the next daily visit, and the pulling unit is booked. It makes no decision about any person.

**Why not Low.** It shapes how a very small crew spends its time, its data is OT data that also belongs to the partners, and the vendor has already shown it will change features without asking.

**Escalation triggers (re-tier to High and re-assess):**
- any write-back to controllers, including "suggested setpoint" features that apply themselves
- use to defer or skip checks of safety-critical equipment
- use of alerts to rank, evaluate, or discipline Lease Operators
- adding personal information (for example phone locations of field staff)

## 4. MEASURE
| Trustworthy characteristic | Test or metric | Result (pilot, May-August 2026) | Pass? |
|---|---|---|---|
| Valid and reliable | Failures flagged at least 3 days ahead; alerts that turned out to be real problems | 5 pump failures on pilot wells; 3 flagged ahead. 9 alerts; 4 were real problems (3 failures and 1 gas-locked pump) | Partial: sample too small to judge; keep measuring |
| Safe | No write path to controllers; no change to safety checks | Write-back was on for 2 wells until 2026-08-26; now off and verified by the Field Technician; safety check schedule unchanged | **Yes, since 2026-08-26** |
| Secure and resilient | Vendor accounts with MFA; connector send-only; contract security terms | MFA not enabled on the portal; **no security or change-notice terms** | **No** |
| Accountable and transparent | Named owner; staff told what the add-on does and does not see | Owner named; field staff not yet briefed | Partial |
| Explainable and interpretable | Each alert shows the card pattern or load trend behind it | Shown in the vendor portal | Yes |
| Privacy-enhanced | No personal information sent | Confirmed: controller data only | Yes |
| Fair, with harmful bias managed | Compare missed failures and false alerts across well groups (plan below) | Too few events to compare; the 2 cellular sites in the pilot send data every 15 minutes instead of every minute, and both of their failures were missed | **Watch**: flagged as a likely blind spot |

**Representativeness and bias plan (scaled to 8 wells).** Here "harmful bias" means the tool serves some wells worse than others, so those wells fail more often and wait longer for the pulling unit.
- **Groups watched:** radio sites vs the cellular sites (less data per hour); the 3 deepest wells (different pump size) vs the rest; wells in sour service vs sweet.
- **Method:** with so few wells, no statistics are computed. The Owner keeps a simple log of every failure and every alert and reviews it each quarter by group.
- **Trigger:** if 2 or more failures in one group are missed in a quarter while the other groups are caught, that group goes back to "no reliance" (Lease Operators check those wells as if the tool did not exist), and the vendor is asked whether more data or a different model would help.
- **Workforce check:** the tool must not be used to judge the Lease Operators. Alerts are about pumps, not routes or people.

## 5. MANAGE
**Human-in-the-loop design:**
- The add-on produces a ranked alert list in the vendor portal. It does nothing else.
- The Owner or the Field Superintendent reads each alert and its explanation and decides whether to send a Lease Operator, book the pulling unit, or dismiss it with a reason.
- Lease Operators keep their daily visits to every well. The tool adds attention; it never removes a visit.

**Monitoring:**
- Monthly: the Field Technician confirms the connector is send-only and the vendor portal shows no write-back features enabled; the Owner updates the failure and alert log.
- Quarterly: group review (section 4) and a check of the vendor's release notes for feature changes.
- Any vendor feature change that touches controller settings stops use of the add-on until it is reviewed.

**Security:**
- The connector stays send-only (POL-02 B.10). Turning write-back on needs a new assessment and the Owner's and Field Superintendent's written approval.
- MFA on the vendor portal by 2026-09-30 (POAM-007).

**Incident handling:** a security incident affecting the vendor's cloud or the connector follows P08. An unexplained setting change on a controller is reported under POL-03 4.2.

**Decommissioning:** stop and export the alert log if the vendor will not agree to the conditions below by 2026-11-30, or if the trial ends without a paid agreement. Ask the vendor in writing to delete the company's pilot data, and record the answer.

## 6. Decision
**Approve with conditions.** Owner, with the Field Superintendent's agreement, 2026-08-31. The pilot may continue on the 8 wells in advisory mode **only if** these conditions are met by 2026-11-30:
1. Write-back stays off, checked monthly and recorded (done 2026-08-26; first check 2026-09-30).
2. The subscription terms are amended: no write-back without the company's written request; 30 days' notice of feature changes; no use of the company's or partners' well data to train models for other customers unless the company opts in; deletion on request (POL-02 A.5).
3. MFA is enabled on the vendor portal for all users.
4. Field staff are briefed on what the add-on does and that daily visits continue.

Expansion to all 16 producing wells requires two quarters with no group flagged in section 4 and the amended terms in place.

**Related action for AI-002.** Choose an enterprise generative AI tool with data protections and add it to the approved list, so staff stop using public chatbots. Until then, public tools may be used only for Public and Internal information (POL-02 C.2; POL-04 4.6). Due 2026-11-30 (P01 R-023).
