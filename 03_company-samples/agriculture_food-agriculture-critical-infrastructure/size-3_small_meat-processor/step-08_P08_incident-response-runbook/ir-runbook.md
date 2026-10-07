# Incident Response Runbook: Ransomware Halting Processing Lines and Cold-Chain Monitoring

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (meat processing plant with a smoked seafood room) |
| Tier / Vertical | Small / Food and Agriculture |
| Incident type | Ransomware that starts on the corporate network, spreads to SCADA and the recipe and batch system (MES), stops the processing lines, and cuts cold-chain monitoring |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager, with the Controls Engineer (OT) and FSQA Manager (food safety) |
| Approved | 2026-09-04 by the General Manager |
| Last tested | Not yet. First tabletop exercise due 2026-12-15 (POAM-017) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | General Manager | Incident line (cell), then the out-of-band group chat on personal phones |
| OT lead (safe state, containment, recovery) | Controls Engineer | Controls integrator (on-site only during the incident) | Cell |
| Food safety lead (product hold, FSIS and FDA notices) | FSQA Manager | Senior QA technician | Cell |
| Refrigeration and ammonia safety | Maintenance and Refrigeration Manager | Refrigeration contractor (on-site) | Cell; PSM emergency response plan |
| Production | Operations Manager | Line supervisors | Radio and cell |
| Cold storage and shipping | Warehouse and Logistics Manager | Shift lead | Cell |
| Legal counsel and forensics | Outside breach counsel and an OT-capable forensic firm (insurer panel) | n/a | Via insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Communications | General Manager | Outside PR (via counsel) | Cell |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and the identity provider are compromised. Coordinate on personal phones and plant radios, using the printed contact list in the incident binders in the FSQA office, the engine room, and the shipping office.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binders: this runbook, contacts, the notification matrix, manual CCP forms, the manual temperature log, and signed formulation sheets
- [ ] Controlled printed copy of the food defense plan in the FSQA office safe (21 CFR 121.315(c))
- [ ] Offline and immutable backups of SCADA, historian, and MES; PLC programs in the repository; a restore test within the last 90 days (CP-9, CP-4). **Gap until POAM-006 and POAM-007 close**
- [ ] OT DMZ in place and MES no longer dual-homed (SC-7). **Gap until POAM-001 closes**
- [ ] OT monitoring with alerts on setpoint and recipe changes (SI-4). **Gap until POAM-013 closes**
- [ ] Escalating cold-chain alerts to three roles, cellular path for the gateway (P01 R-005)
- [ ] Two break-glass administrator accounts sealed and tested (planned)
- [ ] Forensic retainer with OT capability confirmed (POAM-017)
- [ ] List of FSIS District Office and FDA RFR portal access holders current (FSQA Manager)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note or encrypted files on an office PC, the SCADA server, the historian, or the MES | Staff report, EDR alert | Call the incident line. **Do not power off** SCADA or MES. Pull the network cable |
| HMIs show "communication lost," or the recipe system will not load formulations | Operators | Line supervisor calls the Controls Engineer and the incident line |
| Cold-chain dashboard stops updating, or no alerts arrive during a known excursion | Warehouse shift lead | Start the manual temperature log at once; call the incident line |
| Setpoint or formulation values that nobody approved | Operators, QA, FSQA review | Treat as possible tampering: stop the affected step and call the FSQA Manager and the incident line |
| Extortion email or a leak-site post naming the company | Email, law enforcement | Declare the incident; preserve the message |

**Declare a ransomware incident when** encryption or a ransom note is confirmed on any system, or when HMIs, SCADA, or MES lose function with signs of malicious activity.
**Record the time** of discovery and of every product-affecting event (last good CCP reading, start of manual monitoring). These times drive product decisions and notification clocks.

## 3. First hour: make the plant safe (RS.MA, RS.MI)
**Order matters.** Protect people, then product in process, then evidence and systems.

| Step | Who | Done when |
|---|---|---|
| 1. Confirm refrigeration is running on its local controller and ammonia detection is normal. If the refrigeration controller shows signs of tampering, switch to manual operation under the PSM procedures | Maintenance and Refrigeration Manager | Engine room reports stable; no ammonia alarm |
| 2. Start manual temperature logging for every cooler, freezer, the seafood room, and loaded trailers, at least hourly | Warehouse and Logistics Manager | First manual log entries recorded |
| 3. Put lines in a safe state: let smokehouse cycles finish on local controllers where the cycle is intact, or abort and hold the product; stop brine injection and dosing; close CIP valves manually | Operations Manager with the Controls Engineer | Every line stopped or finishing a verified cycle |
| 4. **Hold all product** made, cooked, chilled, or stored since the last trusted CCP record, plus any product dosed from the recipe system since the last verified formulation | FSQA Manager | Hold tags on product; hold list started |
| 5. Isolate: disconnect the corporate-to-OT firewall link, the site-to-cloud VPN, the integrator VPN, and the refrigeration modem. Leave affected hosts powered on for memory evidence | IT Manager and Controls Engineer | Links down; photos of cable positions taken |
| 6. Call the cyber insurer's breach hotline; engage counsel and an OT-capable forensic firm | General Manager | Claim number issued |
| 7. Revoke all sessions and reset administrator credentials in the identity provider and cloud tenant, using break-glass accounts if needed | IT Manager | Sessions revoked |
| 8. Brief the FSIS inspection program personnel on site that electronic CCP monitoring is down and manual monitoring and holds are in place | FSQA Manager | Briefing time recorded |
| 9. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** which office hosts, OT servers, HMIs, and accounts are affected? Check EDR, identity provider sign-ins, firewall logs, VPN logs, and cloud audit logs (default retention can be as short as 30 days; POAM-012).
2. **Initial access:** phishing, the integrator VPN account, or the refrigeration modem? These three paths are the likely ones (P01 R-001, R-002, R-006).
3. **Did the attacker touch the process?** With the Controls Engineer, compare PLC programs, smokehouse cycles, and every formulation in the recipe system with the repository and the signed formulation master. Check CIP valve logic on the seafood brine tank and the dosing skid. **Any unexplained difference is treated as possible intentional adulteration** (POL-03 4.5).
4. **Preserve evidence:** the forensic firm images affected servers and exports logs. Chain of custody for every drive and export.
5. **Exfiltration:** did the attacker take employee data (HR files), online customer accounts, formulations, or the food defense plan? This drives the Florida breach decision and the food defense reanalysis.
6. **Backups:** confirm OT and cloud backups are intact and clean before any restore.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at the internet firewall and in cloud network rules.
2. Disable compromised accounts. Rotate every shared OT password, the integrator VPN credentials, and service accounts between MES, ERP, and the cloud tenant.
3. Rebuild affected office endpoints and OT Windows hosts (SCADA, historian, MES, engineering workstation) from clean media. **Do not decrypt and reuse them.**
4. Reload PLC programs from the repository if any comparison in section 4 step 3 failed or could not be completed.
5. Keep the integrator VPN and the refrigeration modem disconnected. Vendors work on site under escort until the OT remote access gateway is live.
6. Confirm with forensics that persistence is removed before reconnecting anything.

## 6. Food safety decisions and reporting (RS.CO)
**Food safety decisions come first, and they are the FSQA Manager's.** Follow `notification-matrix.csv`; legal counsel confirms personal-data notices.

**Product on hold.** For each held lot, the FSQA Manager documents the review required for unforeseen deviations (9 CFR 417.3(b)): segregate and hold, determine acceptability using manual records, chart recorders, and product testing where needed, and dispose of anything that cannot be shown safe. Product may not ship until its records are complete (9 CFR 417.5(c)).

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer notified; counsel engaged; FSIS personnel on site briefed | General Manager; FSQA Manager |
| Hour 0-24 | Decide whether any **already-shipped** meat product may be adulterated or misbranded (for example, shipped after monitoring stopped or after an unexplained formulation change). If so, notify the FSIS District Office **within 24 hours** of that determination (9 CFR 418.2) and start the recall procedure (9 CFR 418.3) | FSQA Manager |
| Hour 0-24 | Same question for shipped **seafood**. If it is a reportable food, report to FDA's Reportable Food Registry **within 24 hours** of the determination (21 U.S.C. 350f(d)). No report is needed if the problem originated here, was caught before any transfer, and the food was corrected or destroyed (350f(d)(2)) | FSQA Manager |
| Day 0-2 | Voluntary report to FBI (IC3) and CISA. Supports OFAC mitigation if payment is considered | IT Manager |
| Day 0-2 | Customer notices under supply agreements (delivery impact, any recall) | General Manager with the FSQA Manager |
| As soon as known | Decide whether personal information (employee data, online customer accounts) was accessed or acquired | Controller with counsel |
| Within 30 days of determination | Florida individual notice; Department of Legal Affairs notice if 500+ Floridians; consumer reporting agencies if more than 1,000 (Fla. Stat. 501.171) | Controller and counsel |
| After containment | Food defense corrective action record and reanalysis decision if any tampering was found or cannot be ruled out (21 CFR 121.145, 121.157(b)(3)) | FSQA Manager |

**Plan to the shortest clock.** The 24-hour FSIS and FDA clocks start at *determination*, not discovery, but the determination must be made with reasonable speed. Do not delay the product question while IT work continues.

**Ransom decision:** requires the majority owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not make held product safe or remove any notification duty.

**CIRCIA:** not in effect. As proposed, the company would be below the size criterion. Recheck when the final rule is published.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Refrigeration running and temperatures recorded (manual log until the cold-chain gateway is back on a clean network)
2. Safe state for in-process product; held product evaluated
3. SCADA and historian from a verified clean backup; historian gap covered by manual records
4. Recipe system restored, then **every formulation compared with the signed master** before any dosing (POL-03 4.8)
5. Packaging, labeling, and lot coding (manual labels with second-person check until MES is back)
6. Identity provider and corporate network
7. Food safety records application and traceability database; enter manual records
8. ERP and WMS for shipping
9. Seafood room
10. Finance, payroll, outlet and online store

**Validate before restart:** each line restarts only after the Controls Engineer confirms PLC programs and formulations match the approved versions, the FSQA Manager signs a restart checklist, and the first batch on each line is verified against critical limits. Tell staff, customers, and the FSIS personnel on site when normal monitoring resumes (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the FSQA Manager and the Controls Engineer (POL-03 requires documentation within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-003, R-005, R-007), the POA&M (P07), this runbook, the HACCP plans (reassessment under 9 CFR 417.3(b)(4) if the deviation was unforeseen), and the food defense plan if tampering was found or suspected.
- Retain incident records for at least 3 years (POL-01 4.12), and product hold and disposition records with the HACCP records.
