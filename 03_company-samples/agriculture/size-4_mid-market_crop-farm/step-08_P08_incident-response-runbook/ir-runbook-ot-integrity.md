# Incident Response Runbook: OT Integrity Incident with Possible Product Safety Impact

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed diversified precision-agriculture crop farm with a central packinghouse and a Grower Services unit) |
| Tier / Vertical | Mid-Market / Agriculture, Forestry, Fishing and Hunting |
| Incident type | Unauthorized or unexplained change to fertigation, irrigation, ethylene ripening, or cold-chain controls (SYS-07), by an attacker, a vendor, an insider, or a faulty automatic action, where product safety, worker safety, or crops may be affected |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); NIST SP 800-82 Rev. 3 sections 6.3 to 6.5; the food safety recall plan |
| Policy basis | POL-03 Incident Response Policy (4.4, 4.5, 4.7, 4.10) |
| Companion documents | `ir-runbook.md` (ransomware); `notification-matrix.csv`; BIA (P05 BP-01, BP-04, BP-05, BP-07); risk register (P01 R-006, R-022, R-030, R-050); food defense plan; food safety recall plan |
| Runbook owner | Director of Irrigation and Water Resources (operations lead) with the Security Manager (security lead) and the Director of Food Safety and Quality (product lead) |
| Approved | 2026-09-15 by the Chief Operating Officer; effective 2026-10-01 |
| Last tested | Not yet. OT integrity tabletop with the SCADA integrator, the refrigeration contractor, and a retail customer's food safety contact scheduled 2027-01-20 (POAM-014) |

## 0. Why this runbook exists
The company's OT doses fertilizer into irrigation water through 14 injection skids, runs 12 ethylene ripening rooms, and keeps about 120 truckloads of produce cold. Today these controls have default credentials (packinghouse controllers, P01 R-050), standing vendor access (R-002), no change control (R-006), and no monitoring (R-021). An unauthorized or mistaken change could burn a crop, exceed label or permit rates, expose workers to concentrated chemicals, or let temperature-abused produce ship. The first question is never "who did it" but **"is anything unsafe, and where did it go?"** This runbook also covers a faulty automatic action by AI-002 (automatic irrigation scheduling at Farm 3, P10).

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Operations lead | Director of Irrigation and Water Resources (field OT) or Packinghouse Manager (packinghouse OT) | Farm Manager of the affected farm | Safe state, manual operation, setpoint and program verification, safe restart |
| Product lead | Director of Food Safety and Quality | Food Safety Coordinator | Product hold, lot scoping, customer notice, recall recommendation |
| Security lead | Security Manager | IT Director | Evidence, access cut-off, investigation, decision whether `ir-runbook.md` also applies |
| CMT chair (if escalated) | Chief Operating Officer | CEO | Declares severity 1; recall decision with the CEO; external statements |
| Worker safety | HR Director with the Farm Manager | n/a | Restricted-entry decisions, medical referral, worker communication |
| Vendors | SCADA integrator; refrigeration contractor; pivot manufacturer; FMIS vendor | n/a | On-site support only; program and setting histories |
| Legal | Outside general counsel; breach counsel if data is involved | n/a | Customer contract notices, recall communications, law enforcement |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Fertigation injection rate, recipe, or EC/pH reading outside the approved recipe | IOC operator; Irrigation Technician at the skid; flow and EC sensors | **Stop injection at the skid**; record the reading and time; call the operations lead |
| Irrigation schedule, valve, pump, or pivot behavior that nobody scheduled | IOC operator; SYS-01 irrigation module; Farm 3 pivot app | Switch to Hand at the panel; call the operations lead |
| Ripening room ethylene, temperature, or timing differs from the approved program | Packinghouse shift lead; room gas detector | Stop the cycle; ventilate per the room's safety procedure; call the Packinghouse Manager |
| Cold room or trailer temperature excursion, or an alarm service that went silent | Cold-chain alarm service; hourly rounds | Move product or start manual control; call the Packinghouse Manager |
| PLC program, HMI screen, or setpoint changed with no change record | Change log (STD-04); OT monitoring alerts (from 2027-03-31, POAM-020) | Call the security lead |
| AI-002 automatic schedule outside its plausibility limits | SYS-01 alert; daily approval check | Return Farm 3 to manual approval mode; call the operations lead |
| Vendor or insider admits a change made without approval | Report | Treat as an OT integrity event until verified |

**Severity:**
- **Severity 1:** any confirmed change to fertigation, ripening, or cold-chain controls by someone not authorized, or any event where product that may be unsafe could have shipped, or a worker may have been exposed. CMT within 2 hours (POL-03 4.4).
- **Severity 2:** an unexplained change with no product or worker exposure (for example, an irrigation schedule change caught before it ran).
- **Severity 3:** a known operator error corrected within the shift, with no exposure.

**Record the time of discovery** and the time each affected setting was last known to be correct. That window scopes the product hold.

## 3. First 2 hours (RS.MA, RS.MI): make it safe
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | **Safe state.** Stop fertigation injection and close injection valves at the affected skids; put affected pumps, valves, and pivots in Hand; stop affected ripening cycles and ventilate; move product out of an affected cold room if needed | Operations lead | Equipment in a known safe state |
| 0-30 min | **Worker safety.** Keep workers out of blocks that may have received excess fertilizer or chemical until the operations lead and the Farm Manager clear them; check gas detectors in ripening rooms; send anyone with symptoms for medical care | Farm Manager; Packinghouse Manager; HR Director | Areas controlled; people safe |
| 0-30 min | **Product hold.** Place on hold all product harvested from affected blocks, or ripened or stored in affected rooms, since the last known-good time; tag lots in SYS-01 and the ERP; stop shipping those lots | Director of Food Safety and Quality | Hold list issued; shipping stopped |
| 0-60 min | **Cut access.** Disable vendor remote access (integrator tool, pivot manufacturer support, refrigeration contractor connection); change the credentials on the affected controllers from a clean device; isolate the affected OT segment at the firewall only after the equipment is in manual operation | Security lead with the operations lead | Access off; segment isolated |
| 0-60 min | **Preserve evidence before restoring.** Photograph HMI screens; export SCADA, historian, controller, and pivot cloud event logs; download the current PLC programs and recipes **without overwriting them**; keep the injection skid and flow meter readings | Security lead; integrator on site | Evidence saved with chain of custody |
| 1-2 h | Decide severity; convene the CMT for severity 1; decide whether `ir-runbook.md` also applies (malware or ransomware found) | Security lead; COO | Severity recorded |

## 4. Analysis (RS.AN)
1. **What changed, when, and by whom.** Compare current PLC programs, HMI configurations, fertigation recipes, ripening programs, and cold storage setpoints with the approved copies (STD-04; hash comparison where POAM-010 copies exist). Use the SCADA event log, the historian trend, the pivot cloud audit log, the SYS-01 irrigation module history, vendor remote session records, and badge and key records for pump stations.
2. **Exposure window and scope.** From the last known-good time to the safe state: which blocks received irrigation or fertigation, how much product was applied compared with the recipe and label rates, which ripening rooms and cold rooms were affected, and for how long.
3. **Product trace (with the food safety team).** List every lot harvested from affected blocks or held in affected rooms during the window, using SYS-01 harvest records, packing line lot codes, and ERP shipments. Include contract growers' lots packed or stored in affected rooms. Use the mock recall procedure; the target is a complete lot list within 4 hours.
4. **Safety assessment.** The Director of Food Safety and Quality, with the agronomist and, where needed, the fertilizer supplier and an outside laboratory, decides whether affected product is safe, needs testing, or must be destroyed. Over-application of fertilizer is mainly a crop and worker risk; a temperature excursion or an ethylene program fault is mainly a quality and spoilage risk; a change that introduced a non-approved substance, or tampering with packinghouse water, is a potential adulteration and food defense event (the food defense plan uses 21 CFR Part 121 as a voluntary checklist, N11-R01).
5. **Cause.** Attack (follow `ir-runbook.md` as well), vendor error, insider action, operator error, sensor fault, or a faulty AI-002 schedule. If an AI system acted, record the model version, inputs, and the plausibility limits in force (P10).

## 5. Containment, correction, and safe restart (RS.MI, RC.RP)
1. Reload the approved PLC programs, recipes, ripening programs, and setpoints from verified copies. Where no verified copy exists, the integrator rebuilds from documentation on site and the operations lead approves line by line.
2. Rotate all credentials on the affected controllers and SCADA; remove any vendor access path that was used without approval.
3. **Restart one element at a time** with the operations lead watching a full cycle: one pump and its valves, then one injection skid at a low test rate with EC and pH checked by hand, then normal rates; one ripening room through a full program; one cold room through a full cooling cycle.
4. For AI-002: Farm 3 stays in manual approval mode until the P10 owner and the Director of Irrigation sign off on the cause and the plausibility limits.
5. The Director of Food Safety and Quality releases held product lot by lot, with the reason, or orders destruction. Released and destroyed lots are recorded in SYS-01 and the ERP.

## 6. Customers, growers, regulators, and the public (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms external notices.

| When | Action | Owner |
|---|---|---|
| Within 24 hours of awareness | **Retail customers** that received or are due to receive affected lots: notice of any event that could affect product safety, traceability, or committed volumes (supplier agreements), with the lot list as it stands | Director of Food Safety and Quality with the Director of Sales |
| Within 24 hours | **Foodservice and terminal market buyers** of affected lots: same information, so each can assess its own duties (including any Reportable Food Registry duty that falls on a registered facility; the company registers none) | Director of Food Safety and Quality |
| Same day | **Contract growers** whose lots are held, and the effect on their settlement | Vice President of Grower Services |
| If the company decides to remove or correct distributed product it believes violative | **FDA** is requested to be notified immediately (firm-initiated recall, 21 CFR 7.46(a)); follow the food safety recall plan and FDA's requests for product, reason, risk, quantities, distribution, and recall strategy | CEO and Director of Food Safety and Quality, with counsel |
| On request | Produce Safety records (21 CFR 112.166(a)) and traceability records for the affected lots | Director of Food Safety and Quality |
| If pesticide or chemical exposure of workers is suspected | Medical referral; application and hazard information given to treating medical personnel promptly (40 CFR 170.311(b)(8)) | HR Director; Food Safety Coordinator |
| If tampering or an attack is suspected | Voluntary report to the FBI and CISA; cyber insurer hotline | Security Manager; COO |
| If water use exceeded permit conditions | Report under the water use permit conditions in the next monthly report, with the explanation | Director of Irrigation and Water Resources |

**Recall decision.** The CEO decides with the Director of Food Safety and Quality and counsel, using the safety assessment in section 4 step 4. Holding product costs less than a recall, so the default is to hold first and decide with evidence. Customer and FDA communications come only from the people named above.

## 7. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days; written report within 30 days (POL-03 4.12), shared with the food safety team for the food defense plan review.
- Update the risk register (P01: R-006, R-022, R-030, R-050), the POA&M (P07), STD-04, the food defense plan, and this runbook.
- If AI-002 was involved, the P10 owner re-assesses the use case before automatic application resumes.
- Keep the incident record, hold and release decisions, and customer notices for at least 3 years (POL-01 4.12), and food safety records for their legal retention periods (POL-04 4.7).
