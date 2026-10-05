# Incident Response Runbook: Unauthorized Remote Command of Field Equipment through a Third-Party Access Path

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed independent crude oil producer with a Panhandle gathering system) |
| Tier / Vertical | Mid-Market / Mining, Quarrying, and Oil and Gas Extraction |
| Incident type | Someone uses a vendor's remote access path to send commands to field equipment: variant A, the compressor packager's cellular gateways at the 4 compression stations; variant B, the flow computer vendor's support modem at the Panhandle Central Facility (LACT units and gathering pump station); variant C, a vendor's jump host account used with stolen credentials. The worst case is a manipulated pump station setpoint or valve command that causes or hides a release from the gathering system |
| Why this runbook exists | P07 found 2 of 4 packager gateways reachable from the internet with a shared password, and one could reach a station PLC (P01 R-052). Vendor paths are the company's largest exposure (P01 R-004, R-006, R-020) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); NIST SP 800-82 Rev. 3 sections 6.2.10 (remote access), 6.4, and 6.5; CSF GV.SC-08 (suppliers in incident planning) |
| Policy basis | POL-03 Incident Response Policy (4.4, 4.6, 4.8); POL-02 4.11 (vendor remote access); STD-04 Remote and third-party access standard |
| Companion documents | `ir-runbook.md` (ransomware); `notification-matrix.csv`; pipeline emergency procedures; emergency response plan; BIA (P05 BP-04, BP-05, BP-07) |
| Runbook owner | OT Security Engineer (OT incident lead) with the Pipeline Compliance Manager (pipeline lead) |
| Approved | 2026-09-16 by the Chief Operating Officer, with the VP Operations agreeing to the field steps |
| Last tested | Not yet. Panhandle OT and pipeline tabletop with the Pipeline Compliance Manager 2026-11-18 (POAM-016) |

**Safety and the pipeline come first.** If a command could have changed pressure, flow, or valve position on the gathering system, the pipeline emergency procedures start at once, in parallel with this runbook. The hardwired high-pressure shutdown switches at the pump station keep the trunk line below MOP without SCADA; never bypass them. Production Controllers do not wait for the cyber investigation to stop a pump, close a valve, or send a station operator.

## 0. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| OT incident lead | OT Security Engineer | SCADA and Automation Manager | Cut the vendor path, preserve OT evidence, verify controller logic and setpoints |
| Pipeline lead | Pipeline Compliance Manager | VP Operations | Pipeline emergency procedures; 195.52 notice decision within 1 hour of confirmed discovery; safety-related condition decision |
| Control room | OCC shift lead | Control Room Manager | Put affected stations in local or safe state; dispatch operators; record times |
| Field lead | Field Superintendent (Panhandle or Alabama) | VP Operations | Station operators, line riders, shut-in decisions |
| Incident commander (if severity 1) | Security Manager | VP IT | Overall coordination; MDR and forensics |
| CMT chair (if escalated) | Chief Operating Officer | CEO | Declares severity 1; approves external statements |
| Measurement lead (variant B) | Measurement Supervisor | Production Accounting Director | LACT configuration and volume integrity; shipper statements |
| Vendor management and legal | General Counsel | Outside counsel | Vendor contract rights and cooperation, insurer, evidence |
| Spill notices | HSE Director | HSE on-call | 40 CFR 110.6 and state notices |

## 1. Preparation checks (Identify / Protect)
- [x] Inbound internet access blocked on all 4 packager gateways and their passwords changed (2026-08-13)
- [ ] Packager gateways removed and packager support moved to the jump host. **Due 2026-10-31 (POAM-002)**
- [ ] Flow computer vendor modem removed. **Due 2026-11-30 (POAM-002)**; until then it stays powered off and is powered on only by the Measurement Supervisor for a scheduled call
- [x] Jump host with named vendor accounts, MFA, per-session approval, and recording (25 of 25 sampled sessions compliant in P07)
- [ ] Alarm on every write to pump station setpoints, with a second reviewer for changes (POAM-008, due 2027-01-31). Until then the OCC shift lead compares pump station setpoints with the MOP record at each shift change
- [ ] Flow computer configuration captured nightly (POAM-007, due 2026-12-31)
- [x] Hardwired high-pressure shutdown switches at the pump station and compressor emergency shutdowns tested on their normal schedule
- [x] Vendor emergency contacts for the packager, the flow computer vendor, and the integrator in the binders at the OCC, the BCC, and the Central Facility
- [ ] Manual release estimate tables at the OCC, BCC, and pump station (POAM-020, due 2026-11-30)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A setpoint, valve position, or compressor start or stop that nobody on shift ordered | HMI event list; Production Controller | OCC shift lead puts the station in a safe state (section 3) and calls the OT Security Engineer and the Pipeline Compliance Manager |
| Pump station discharge pressure rising toward the MOP alarm, or an unexplained drop in trunk line pressure or flow | SCADA pressure and flow alarms; leak analytics (AI-003, advisory only) | Start the pipeline emergency procedures; the analytics tool never clears an alarm |
| New connection to a station PLC or the Central Facility network from a gateway or modem | OT sensor at the Central Facility; gateway logs from the packager | OT Security Engineer opens an OT incident |
| LACT meter factor, configuration, or totals change without a work order | Measurement Supervisor review; measurement data service | Treat as variant B; check the pump station too |
| A vendor reports that its remote access platform or a shared credential was compromised | Vendor notice; CISA advisory | Cut that vendor's paths at once (section 3, step 2) |
| Jump host session from a vendor account at an unusual time or without an approval record | Jump host logs; weekly session review | Variant C; disable the account and start this runbook |

**Declare an OT incident** on any of the triggers above. **Declare severity 1 and convene the CMT within 2 hours** (POL-03 4.5) if a command was confirmed as unauthorized, if gathering system pressure or flow was affected, or if a release is suspected.

**Record two times:** the time the trigger was first seen, and the time a release (if any) was confirmed. The 1-hour telephone notice runs from confirmed discovery of the accident (49 CFR 195.52(a)).

## 3. First hour (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-10 min | Put the affected station in a safe state from the OCC if the HMI is trusted: stop the pump or compressor, or hold the valve; if the HMI is not trusted, call the station operator to do it at the local panel | OCC shift lead | Station safe; time logged |
| 0-15 min | **Cut the vendor path physically:** power off or pull the SIM from the gateway (variant A), power off the modem (variant B), or disable the vendor account at the jump host and end its sessions (variant C) | Station operator or automation technician, directed by the OT Security Engineer | Path cut; photo of the device taken before and after |
| 0-15 min | If any gathering system pressure, flow, or valve change was involved: start the pipeline emergency procedures, send a station operator to the pump station, and send line riders to the 14-mile regulated trunk line | Control Room Manager; Field Superintendent (Panhandle) | Operator on the way; patrol started |
| 0-60 min | **Release decision.** If a release is confirmed and meets 195.52(a) (death or hospitalization, unintended fire or explosion, estimated damage over $50,000, water pollution as in 195.52(a)(4), or significant in the operator's judgment), call the National Response Center no later than 1 hour after confirmed discovery. If oil reached water, the HSE Director calls under 40 CFR 110.6 immediately | Pipeline Compliance Manager; HSE Director | Call made and logged, or decision not to call recorded with reasons |
| 0-60 min | Disable all other vendor paths and vendor accounts until the source is known; block the gateway and modem address ranges at the Central Facility firewall | OT Security Engineer | All vendor access off |
| 0-60 min | Call the insurer hotline if severity 1; General Counsel engages counsel and the OT-capable forensic firm | CFO; General Counsel | Claim number |
| 1-2 h | Convene the CMT if severity 1; first situation report: what moved, safety status, pipeline status, notices made | COO | CMT meeting held |

**Do not restart** the affected station, pump, or compressor until section 7 is complete, unless the Field Superintendent and the Pipeline Compliance Manager agree that local manual operation with an operator on site is safe.

## 4. Analysis (RS.AN)
1. **What moved and when.** Pull the HMI event list, historian trends (pressure, flow, valve position, compressor status), and controller event buffers for the affected station and the pump station. Export them at once, before the 30-day rollover.
2. **Which path.** Collect the gateway or modem logs (from the device and from the vendor), jump host recordings, Central Facility firewall logs, and OT sensor captures. Determine whether the access came from the internet, the vendor's network, or a stolen company account.
3. **Controller and setpoint integrity.** Upload the running logic from the affected PLCs and compare it with the repository copy. The Pipeline Compliance Manager compares pump station setpoints with the MOP record. The Measurement Supervisor compares LACT flow computer configuration with the approved record (variant B).
4. **Release estimate.** If there is a release, estimate the volume under the written procedure (195.52(c)). If SCADA data is untrusted, use the manual fallback (LACT tickets, tank gauges, line pack tables), and revise or confirm within 48 hours (195.52(d)).
5. **Spread.** Check whether the same path reached other stations, the SCADA network, or corporate systems. Ask the vendor whether other customers using the same shared credential were affected.
6. **Preserve evidence** with chain of custody: the gateway or modem itself (bagged and labeled), exported logs with hashes, HMI screenshots, and controller uploads.

## 5. Containment and eradication (RS.MI)
1. Keep every vendor path off until the source is found and fixed.
2. Change every controller, gateway, and station password the vendor knew; rotate jump host credentials for all vendor accounts.
3. Reload controller logic only from verified repository copies, and re-enter pump station setpoints from the MOP record with a second reviewer.
4. If the access came from a stolen company or vendor account (variant C), follow the identity steps in `ir-runbook.md` section 3.2 and check for spread toward IT.
5. Do not reconnect any vendor except through the jump host with a named account and MFA (POL-02 4.11).

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Pipeline and spill telephone notices are never delayed for legal review. General Counsel keeps the decision log (`ir-runbook.md` section 6, decision points D1 to D6).

| When | Action | Owner |
|---|---|---|
| Immediately, if oil reaches water | National Response Center under 40 CFR 110.6; state notices per the emergency response plan | HSE Director |
| No later than 1 hour after confirmed discovery | National Response Center telephone notice for a regulated trunk line accident meeting 195.52(a) | Pipeline Compliance Manager |
| Within 48 hours after confirmed discovery | Revise or confirm the telephone notice (195.52(d)) | Pipeline Compliance Manager |
| Within 5 working days after determination | Safety-related condition report if pressure rose above 110% of MOP because of a malfunction or operating error and no 195.55(b) exception applies (195.55(a)(4); 195.56) | Pipeline Compliance Manager |
| Within 30 days after discovery | PHMSA accident report for any accident meeting 195.50, on the regulated line or a reporting-regulated line (195.54; 195.15) | Pipeline Compliance Manager |
| Hour 0-2 | Transmission pipeline control center, if LACT deliveries stop or receipt-point pressure changes | Control Room Manager |
| Within 24 hours of confirmed impact | Shippers, if gathering is curtailed or measurement may be affected (variant B) | Measurement Supervisor |
| Day 0-1 | Written notice to the vendor whose path was used, invoking its contract cooperation duties; request its logs | General Counsel |
| Day 0-1 | Voluntary report to CISA and the FBI through counsel | Security Manager |
| Before the next renewal | Confirm to the cyber insurer how remote access is now controlled; the policy requires MFA on all remote access (P01 R-036) | CFO |

Personal information is not usually involved in this incident type. If the investigation shows that an attacker also reached corporate systems or personal information, the breach steps in `ir-runbook.md` section 6 apply.

## 7. Recovery (RC.RP, RC.CO)
1. Station runs in local manual mode with an operator on site until verification is complete.
2. Verification before returning to remote control: controller logic matches the repository; pump station setpoints match the MOP record (signed by the Pipeline Compliance Manager); LACT configuration matches the approved record (signed by the Measurement Supervisor); the hardwired high-pressure shutdown switches are confirmed in service.
3. Restart in BIA order (P05): pump station and trunk line monitoring first (BP-04, RTO 4 hours), then custody transfer measurement (BP-05, RTO 24 hours), then compression (BP-07, RTO 12 hours).
4. Increase line rider patrols of the regulated trunk line to every 4 hours for 72 hours after restart.
5. Re-enable vendor support only through the jump host.
6. Tell the transmission pipeline, shippers, and the gas gathering company when normal operations resume (RC.CO). Reconcile shipper statements for the affected period with LACT tickets before republishing.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days with field operations, the Pipeline Compliance Manager, the HSE Director, and the vendor; written report within 30 days (POL-03 4.12).
- Update the risk register (P01: R-004, R-006, R-007, R-020, R-036, R-052), the POA&M (P07), the vendor's tier and assessment (STD-03), the pipeline emergency procedures, and this runbook.
- Retain the decision log, pipeline notice records, and evidence for at least 6 years (POL-01 4.14), and accident records as Part 195 requires.
