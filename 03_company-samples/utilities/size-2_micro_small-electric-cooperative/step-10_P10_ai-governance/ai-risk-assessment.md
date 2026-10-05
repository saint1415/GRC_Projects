# AI Risk Assessment: Peak Forecasting for Load Management

| Field | Value |
|---|---|
| Organization | Cris Santos Electric Cooperative, Inc. (member-owned electric distribution cooperative) |
| Tier / Vertical | Micro / Utilities |
| AI use case | AI-001: the AMI vendor's machine-learning peak-forecasting add-on, on trial since 2026-06-01 |
| Why not the registry default | The registry names an "electric load-forecasting model". A 7-person cooperative builds no models, and system load forecasting for wholesale planning is done by the G&T. The cooperative's own AI use is this vendor add-on, which forecasts the G&T's monthly coincident peak so the cooperative can cut its demand charge. Recorded in `../00_company-facts.md` section 5 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook. AI 600-1 (Generative AI Profile) does not apply because the model is not generative; it is used only for AI-003 |
| Assessor / date | General Manager with the Office and Finance Manager (Security Coordinator) and the Meter and Service Technician, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner and decision authority:** General Manager. **Technical owner:** Meter and Service Technician (AMI administrator). **Oversight:** the Board of Trustees receives the decision in section 6 with the yearly security report (POL-02 A.10).
- **Policies that apply:**
  - POL-04 4.5: no new add-on receives member data before approval and vendor terms. **The trial started before this rule existed and without a review of the vendor's data-use terms** (P01 R-017).
  - POL-04 4.6: approved AI tools only. AI-001 is approved for aggregated and member interval data only under the conditions in section 6.
  - POL-02 C.2: no member data or SCADA details in public chatbots (AI-003).
  - POL-02 A.2: AI risks are in the risk register (R-017, R-018, R-021).
- **Approved-tools list:** kept by the Security Coordinator in the information inventory (POL-04 4.4). It lists AI-001 (conditional) and AI-002. Public chatbots (AI-003) are approved for Public information only.
- **Scale for a micro cooperative:** there is no AI committee. The General Manager reviews AI use cases with the Security Coordinator at the July risk register update and before any new AI feature is switched on.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Predict, for each summer and winter month, the days and hour most likely to be the G&T's monthly coincident peak. The G&T bills a demand charge of about $18 per kW-month on the cooperative's load at that hour |
| How the output is used | (1) The General Manager decides whether to call a load-control event: 310 enrolled water heaters are switched off for up to 4 hours (about 0.35 MW). A well-timed event saves about $6,300 in a month. (2) A peak alert by text and email asks all members to cut use during the window |
| Users / operators | General Manager (decides); Meter and Service Technician (sets up the event in the AMI head-end); Member Services Representative (answers member questions) |
| Affected people | 310 members enrolled in the voluntary water-heater program (comfort; they can opt out); all about 820 members receive alerts; all members indirectly through wholesale costs |
| Data | **Member-level 15-minute interval usage from every meter**, load-control switch status, weather, and the G&T's peak advisories. The add-on runs inside the AMI vendor's service. The standard AMI terms allow the vendor to use customer data for "product improvement", which could include training its model on member data |
| Build or buy | Bought: a vendor add-on enabled in the cooperative's AMI tenant. The cooperative cannot see or change the model, only its outputs and settings |
| Not intended | Automatic dispatch of load control, operating any field device other than the load-control switches, remote disconnects, or any decision about an individual member's account. These uses would require a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Federal or Florida AI-specific law | None identified | The repository's cross-sector file lists no federal AI statute that governs this use. State AI laws such as Colorado SB26-189 cover consequential decisions about individuals in listed categories, and the cooperative operates only in Florida |
| Fla. Stat. 501.171 | Indirectly | Interval usage is not one of the listed personal information elements in 501.171(1)(g), but it is linked to account numbers in the AMI service and POL-04 classifies it Internal. If the vendor were breached, member names linked to accounts would be checked against the statute |
| Wholesale power contract | Yes (contract) | Sets the coincident peak demand charge; forecast accuracy has direct cost |
| Load-control program terms | Yes (member agreement) | Limits events to 4 hours and lets members opt out |
| 7 CFR 1730.27(c)(8) | Yes | Vendor use of member data is an "other threat" the VRA update records (P03 G-024) |
| NIST guidance | Voluntary | AI RMF 1.0 |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why not High.** The rubric's High tier covers AI that makes or is a substantial factor in a consequential decision about a person, or that can affect physical safety or critical infrastructure operations. The add-on does neither in its current use. Its output decides only whether 310 water heaters pause for up to 4 hours, a comfort effect the member agreed to, and a person approves every event. It does not touch protection, switching, or SCADA, and it cannot disconnect anyone.

**Why not Low.** It processes member-level usage data under unreviewed vendor terms, and it triggers communications to every member.

**Minimum controls for the Medium tier and how they are met:**
| Rubric control | Status |
|---|---|
| Human oversight | In place: the General Manager checks the G&T peak advisory and approves every event and alert |
| Output quality monitoring | **Started 2026-08** (monthly comparison with the G&T's actual peak hour); not yet a written procedure |
| Disclosure of AI interaction | Not applicable to members today (they receive an alert, not an AI conversation). The program page will say that a forecasting tool helps pick event days |

**Escalation triggers (re-assess, likely as High, before any of these):**
- letting the add-on dispatch load control or alerts without a person's approval
- linking it to SCADA, regulators, or any switching device
- using it for voltage reduction, remote disconnects, or decisions about an individual member
- sharing forecasts or member data with any third party other than the AMI vendor

## 4. MEASURE
| Trustworthy characteristic | Test / metric | Result (trial, June to August 2026) | Pass? |
|---|---|---|---|
| Valid and reliable | Each month, the G&T's actual coincident peak hour falls inside a called event window | 3 of 3 months | Yes |
| Valid and reliable (precision) | Predicted peak hour equals the G&T's actual peak hour on flagged days | In August the add-on placed the peak 1 hour early on 2 of 6 flagged days; events still covered the actual hour because they run 4 hours | **Partly.** Watch for a pattern; start events 1 hour later on hot days if it repeats |
| Safe | Medical-needs members excluded from load control; events capped at 4 hours | No medical-needs member is enrolled in the program today, but nothing stops one from enrolling; 4-hour cap set in the head-end | **Partly.** Add an enrollment check |
| Secure and resilient | MFA on the AMI head-end; event commands limited to approved users; fallback when the add-on fails | No MFA (POAM-002); 4 users can send load-control commands (POAM-009); fallback is the G&T advisory alone | **No** |
| Accountable and transparent | Event log with who approved, forecast shown, and actual peak hour | Head-end log records the command and user only | **No.** Approval not recorded |
| Explainable and interpretable | Vendor shows the drivers of each forecast (temperature, day type) | Vendor screen shows the top drivers | Yes |
| Privacy-enhanced | Vendor contract bars training on, or sharing, member data outside the service, and requires deletion at exit | Standard terms allow "product improvement" use (P01 R-017) | **No** |
| Fair, with harmful bias managed | Test below | No differences found in the trial | Yes, with monitoring |

**Bias and fairness testing plan.** The forecast makes no decision about a person, but the events it triggers fall on people. The test:
- **Groups compared:** enrolled members by feeder (3 feeders), and members who rely on electric medical equipment (medical-needs list) against all others.
- **Metrics:** event hours per enrolled member per month; opt-out requests and complaints per feeder; any enrollment of a medical-needs member.
- **Threshold:** flag any feeder whose event hours or opt-out rate differs from the average by more than 25%, and any enrollment of a medical-needs member without a documented check.
- **Frequency:** every month during the trial, then quarterly.

**Bias finding.** All 310 switches are controlled together, so event hours were identical across feeders in the trial. Opt-out requests (2 in July) came from different feeders. No medical-needs member is enrolled. The plan stays in place because a future change, such as calling events by feeder, would create differences.

## 5. MANAGE
**Human-in-the-loop design:**
- The add-on forecasts; the General Manager decides. Before each event the General Manager checks the G&T's peak advisory email and, on close calls, phones the G&T control center.
- The Meter and Service Technician sets up the event in the head-end only after the General Manager's approval, which is logged with the forecast shown.
- The General Manager can cancel an event at any time; members can opt out of a single event by calling the office.
- If the add-on fails or is switched off, the fallback is the G&T's peak advisory alone, which is how the program ran before June 2026.

**Monitoring:**
- Monthly: predicted versus actual peak hour, event hours, savings, opt-outs (P01 R-018).
- Quarterly: the fairness test in section 4.
- At the July risk register update: whether to keep, change, or end the add-on.

**Security:**
- MFA on the AMI head-end and load-control commands limited to the Meter and Service Technician and the General Manager (POAM-002, POAM-009).
- The add-on has no path to SCADA or field devices other than the load-control switches managed by the AMI head-end.

**Incident handling:** an event sent without approval, a mass switch failure, or a vendor data incident is handled under POL-03. A vendor breach of member data is checked against Fla. Stat. 501.171 (P08 matrix).

**Decommissioning:** switch off the add-on if the actual peak falls outside the event window in 2 of any 6 months, if the vendor will not sign the data-use addendum, or if the cost exceeds the savings. On exit, the vendor must delete any member data used by the add-on and confirm in writing.

## 6. Decision
**Continue the trial with conditions.** General Manager, 2026-08-31. A decision on production use is due by 2026-11-30, **only if** these conditions are met by then:
1. A signed data-use addendum: no training on, or sharing of, member data outside the cooperative's service, and deletion on exit (P01 R-017).
2. A written monthly accuracy check, with the General Manager's approval of each event recorded (R-018).
3. MFA on the AMI head-end and load-control rights limited to two people (POAM-002, POAM-009).
4. An enrollment check that keeps medical-needs members out of the load-control program unless they ask to join after a call with the Member Services Representative.

If condition 1 is not met by 2026-11-30, the add-on is switched off and events return to the G&T advisory alone. The use case must be re-assessed before any escalation trigger in section 3, and at least every year.

**Related actions:**
- **AI-002 (AMI tamper analytics):** review flag accuracy every quarter. Keep the rule that the Meter and Service Technician inspects every flagged meter before any action, and that no disconnect is ever sent from a flag. Due 2026-12-31.
- **AI-003 (public chatbots):** allowed only for Public information (POL-04 4.6). Covered in the yearly training (POAM-012). No enterprise tool is planned at this size.
