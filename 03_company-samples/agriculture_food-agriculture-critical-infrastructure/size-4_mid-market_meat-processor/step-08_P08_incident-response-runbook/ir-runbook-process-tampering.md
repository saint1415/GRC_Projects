# Incident Response Runbook: Suspected Tampering with Process Setpoints or Formulations

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed meat processor with two USDA-inspected plants) |
| Tier / Vertical | Mid-Market / Food and Agriculture |
| Incident type | An unexplained or unauthorized change to a value that controls food safety (cure, brine, or antimicrobial dosing; injector rates; smokehouse, oven, or chill setpoints; CIP valve logic; Plant 2 blend recipes and fat targets; x-ray or metal detector sensitivity) or to the refrigeration controllers, whether by an insider, a vendor account, or an outside attacker through the control system |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); NIST SP 800-82 Rev. 3; the company's voluntary food defense plans (Part 121 method as a benchmark, C-FOOD-AG-R01) |
| Policy basis | POL-03 Incident Response Policy (4.2, 4.5, 4.6, 4.10); POL-02 4.3 (two-person rule) |
| Companion documents | `ir-runbook.md` (ransomware); `notification-matrix.csv`; HACCP plans and corrective action procedures; recall procedures; food defense plans; PSM and RMP emergency plans; P01 R-003, R-004, R-005, R-031, R-052 |
| Runbook owner | VP FSQA (business lead) with the Security Manager (security lead) and the Controls Engineering Manager (OT lead) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. Tampering tabletop scheduled 2027-02-18 (POAM-012) |

## 0. Why this runbook exists
A meat plant can be attacked without anyone touching the food. Shared HMI logins, setpoints without range limits, blend recipes that live only in HMIs, an always-on vendor VPN, and a modem on a refrigeration controller (P01 R-002 to R-005, R-031) all let a person change how food is made or how ammonia is handled. Most unexplained changes turn out to be mistakes. This runbook treats each one as possible intentional adulteration **until the VP FSQA rules it out**, because the cost of the opposite error is product in commerce that could hurt consumers.

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Business lead | VP FSQA | Plant FSQA Manager | Product holds, acceptability review, FSIS and customer notices, food defense corrective action |
| Security lead | Security Manager | OT security engineer | Access and log review, account containment, forensics through counsel |
| OT lead | Controls Engineering Manager | Senior controls engineer | Compare running values with approved versions; safe state; reload verified logic |
| Refrigeration lead (controller variant) | Director of Engineering and Maintenance | Plant PSM coordinator | Manual operation; PSM and RMP investigation |
| CMT chair (if escalated) | Chief Operating Officer | CEO | Declares severity 1; approves external statements and recall costs |
| Legal | General Counsel; outside counsel through the insurer | n/a | Law enforcement contact, employment actions, privilege, notices |
| HR (insider variant) | HR Director | Plant HR lead | Interviews and employment actions with counsel; staffing agency coordination |
| Plant | Plant Manager | Production manager | Line stops and restarts |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A setpoint, recipe, or blend value differs from the approved version and nobody can explain it | Operator, QA technician, monthly comparison (POL-04 4.7), MES checksum alert | Stop the affected step; call the Plant FSQA Manager and the incident line |
| Out-of-range product results (residual nitrite, cook temperatures, fat percentage, foreign material complaints) with no process explanation | QA laboratory; customer complaint | Plant FSQA Manager opens a deviation and asks the OT lead to compare values |
| Engineering download, controller login, or remote session outside an approved change | Plant 1 OT sensor; gateway log; Plant 2 integrator report | Security lead disables the account or session; declare |
| x-ray or metal detector fails its test piece, or its sensitivity setting changed | Scheduled test-piece check | Hold product since the last good check; compare the device configuration with the approved record |
| CIP valve opened on a brine system in production mode | Valve state alarm (Injector 2 alarm due 2026-12-31) | Stop injection; hold product; declare |
| Unknown person at a control panel, dosing skid room, or engine room; a tip from a worker | Supervisor; CCTV; hotline | Security lead and Plant Manager respond; preserve CCTV |

**Severity 1 (declare immediately, POL-03 4.4):** any unexplained change to a value that controls a CCP, a formulation, CIP valve logic, or refrigeration safety, or any evidence that someone accessed those values without authorization.

**Record the times:** when the change was made (from logs, if any exist), when it was found, the last time the value was verified as correct, and every lot produced in between. **That window defines the product at risk.**

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | Stop the affected step or line and put it in a safe state; do not "fix" the value yet | Plant Manager with the OT lead | Step stopped; screen photographed |
| 0-30 min | **Hold all product** made under the suspect value since it was last verified correct, including product in coolers and on trailers not yet shipped | Plant FSQA Manager | Hold list started; trailers stopped at the gate |
| 0-30 min | Preserve evidence: photograph HMI screens; export historian trends, MES audit logs, gateway session logs, and CCTV for the window; record who held each shared login during the window | Security lead with the OT lead | Evidence list started with chain of custody |
| 0-60 min | Contain access: disable vendor accounts and any account seen in the window; rotate the shared passwords for the affected line or blender; confirm the Plant 2 modem and VPN are off | Security lead | Accounts disabled; passwords rotated |
| 0-60 min | Compare every CCP setpoint, formulation, blend recipe, and inspection device setting at the affected plant with the repository and signed masters (not only the one found) | OT lead with the Plant FSQA Manager | Comparison sheet signed by both |
| 1-2 h | Convene the CMT if severity 1 is confirmed; call the insurer hotline if an outside attacker or vendor account is suspected | COO; CFO | CMT meeting held |
| 1-4 h | Decide whether already-shipped product is affected (section 6, D1) | VP FSQA | Decision recorded |
| 2-4 h | If insider involvement is possible, counsel and HR plan interviews; staffing agency contacted if a temporary worker is involved. Do not confront anyone before evidence is preserved | General Counsel; HR Director | Plan documented |

**Refrigeration controller variant.** If the changed value is on a refrigeration controller (setpoints, alarm thresholds, interlocks), the engine room switches to the manual operation procedure at once, the Director of Engineering and Maintenance confirms ammonia detection is working, and the decision on a PSM and RMP incident investigation is made within 48 hours (1910.119(m); 68.81). Any release follows the release reporting rows in `notification-matrix.csv`.

## 4. Analysis (RS.AN)
1. **What changed, when, and how?** Use MES audit logs, the Plant 1 historian audit trail, gateway session recordings, the Plant 1 OT sensor, and engineering workstation logs. At Plant 2 the historian audit trail was disabled until POAM-006 closes, so analysis may rely on interviews, CCTV, and integrator records.
2. **Who could have made it?** List everyone who held the shared login for that line or blender during the window, every vendor account active in the window, and every remote session. Shared logins make this list long; record that fact for the lessons learned.
3. **Mistake or malice?** Check change tickets, maintenance logs, and recent recipe releases. An approved change that was entered wrongly is still a deviation for food safety purposes, but not a security incident; the security lead decides, with the VP FSQA, whether to downgrade.
4. **Is anything else changed?** Extend the comparison to the other plant if any shared vendor, account, or engineering laptop could reach it.
5. **Is it still happening?** Watch for repeat changes after passwords are rotated; if a change recurs, treat the access path as still open.

## 5. Containment, eradication, and verified restart (RS.MI, RC.RP)
1. Reload PLC logic, recipes, and inspection device settings from the repository or signed masters. At Plant 2, re-enter blend recipes from signed sheets with a two-person check.
2. Rotate every shared credential at the affected plant; keep vendor access off until the security lead clears it.
3. Add temporary compensating controls until named accounts are live (POAM-002): a supervisor present at affected HMIs, hourly value checks by QA, and CCTV review.
4. **Verified restart (POL-03 4.10):** the OT lead confirms values match the approved versions; the Plant FSQA Manager signs the restart checklist; the first batch is verified against critical limits and, for cured products, residual nitrite.

## 6. Food safety decisions, notifications, and law enforcement (RS.CO)
**Follow `notification-matrix.csv`.** The VP FSQA decides every food safety question; the General Counsel confirms legal notices.

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Did product made under the suspect value leave the plant? If evaluation shows it is adulterated or misbranded, notify the FSIS District Office within 24 hours of learning or determining (9 CFR 418.2) and start the recall procedure (418.3) | VP FSQA | Decision log; traceability export |
| D2 | For product still on hold: is it acceptable, reworkable, or to be destroyed? Document the review as an unforeseen deviation (417.3(b)(1)-(3)) and the reassessment decision (417.3(b)(4)) | Plant FSQA Manager; VP FSQA | Hold and disposition records |
| D3 | Is this a criminal act? Intentional adulteration is reported to the FBI; counsel makes the call and coordinates any request to delay customer or public communication | General Counsel | Decision log |
| D4 | Customer notices within 24 hours under supply agreements (any hold affecting committed volumes; any recall) | VP of Sales and Customer Service with the VP FSQA | Notice log |
| D5 | Food defense: corrective action and reanalysis of the affected plant's plan (company plan follows the Part 121 method as a benchmark: corrective actions and reanalysis after a mitigation strategy fails) | VP FSQA | Food defense plan revision |
| D6 | Refrigeration variant: PSM and RMP incident investigation; release reports if any release occurred | Director of Engineering and Maintenance | Investigation record |

**Speed matters more than certainty.** The 24-hour FSIS clock starts when the company learns or determines that adulterated or misbranded product entered commerce. Do not wait for the forensic report to decide D1. Hold, evaluate, and decide with the information available; record why.

**Communications.** No public statement about suspected tampering without counsel. FSIS inspection personnel on site are told about holds and the reason (deviation under review). Staff are told only what they need to keep the line safe, so evidence and any investigation are not compromised.

## 7. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days with FSQA, OT, security, HR, and the Plant Manager; written report within 30 days (POL-03 4.12).
- Update the risk register (P01: R-003, R-004, R-005, R-031, R-052), the POA&M (P07), the HACCP hazard analysis (control-system causes, P03 G-019), and the food defense plan for the affected plant.
- If shared logins limited the investigation, record it as evidence for POAM-002 and POAM-003 priority.
- Retain the evidence, decision log, hold and disposition records, and any FSIS correspondence with the HACCP records and for at least 3 years (POL-01 4.13).
