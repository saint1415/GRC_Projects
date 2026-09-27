# Incident Response Runbook: Ransomware on Farm-Management and Irrigation Control Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (diversified precision-agriculture crop farm) |
| Tier / Vertical | Small / Agriculture, Forestry, Fishing and Hunting |
| Incident type | Ransomware on the farm management and irrigation control systems, entering through the irrigation integrator's remote access account, with theft of payroll and H-2A files (double extortion) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT response steps follow NIST SP 800-82 Rev. 3 sections 6.4 and 6.5 |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Operations and Technology Manager (security lead) |
| Approved | 2026-08-31 by the majority owner and General Manager |
| Last tested | Not yet. First tabletop due 2026-11-30 and first manual irrigation drill due 2026-11-15 (POAM-005) |

**Scenario used to write this runbook.** A weekday in March, at peak strawberry harvest, 8 days into a dry spell. At 05:40 the Irrigation Technician finds the HMI screen replaced by a ransom note. Pumps are still running on the PLC's last schedule. The office file share and two laptops are encrypted, the farm data hub VM will not start, and an email to the majority owner claims the attackers hold "all your worker files." Later analysis finds the attacker signed in through the integrator's always-on remote tool with the shared account (P01 R-002), then moved across the flat network (R-022).

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Operations and Technology Manager | Farm Manager | Incident phone, then the out-of-band group text on personal phones |
| Safety and OT lead | Irrigation Technician | Farm Manager | Radio channel 2 and cell |
| Field and packing operations | Farm Manager | Crew Leads | Cell and radio |
| Executive, insurer, counsel, notices | Majority owner and General Manager | Farm Manager | Cell |
| Workers, payroll, H-2A records | Office and HR Manager | Majority owner | Cell |
| Technical response | MSP incident team; forensic firm through the insurer panel | Integrator field engineer (OT only, on site, not remote) | MSP after-hours line; insurer hotline |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Via insurer hotline |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and the integrator's remote tool are compromised. Use personal phones, radios, and the printed contact list in the incident binders in the office and the pump house.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder in the office and the pump house: this runbook, contacts, the notification matrix, paper tally cards, paper Produce Safety forms, and the manual irrigation procedure
- [ ] Manual irrigation and freeze procedure written and drilled (POAM-004). **Gap until 2026-11-15**
- [ ] Farm-held PLC program and HMI project backups, versioned and stored offline (POAM-003). **Gap until 2026-10-15**
- [ ] Immutable backups in a separate account with a restore test in the last 90 days (POAM-003, POAM-005). **Gap until 2026-11-30**
- [ ] Integrator remote access on request only through the jump host (POAM-002). **Gap until 2026-10-31**
- [ ] EDR with after-hours alerting (POAM-007). **Gap until 2027-01-31**
- [ ] Two break-glass accounts sealed and tested (POL-02 4.10)
- [ ] Insurer panel process confirmed and policy number in the binder (POAM-018)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note on the HMI, an office computer, or the data hub | Staff report | Call the incident phone. **Do not power off.** Unplug the network cable. Tell the Irrigation Technician at once |
| A pump, pivot, valve, or fertigation pump runs, stops, or changes rate when nobody scheduled it | Irrigation Technician; SYS-01 alert (once enabled) | Put the equipment in local or manual control; call the incident phone |
| Files renamed with an unknown extension; many files changing at once | Staff report; backup job failure | Security lead opens the incident |
| Remote tool shows a session nobody requested | Irrigation Technician | End the session; disable the tool; open the incident |
| Extortion email or leak-site post naming the farm | Email; law enforcement | Declare the incident; preserve the message |

**Declare a ransomware incident when** encryption or a ransom note is confirmed on any farm system, an unexplained OT command is confirmed, or an extortion claim names farm data.
**Record two times:** when the incident was discovered, and when the farm determined (or had reason to believe) that personal information was accessed. Florida's 30-day notice clock runs from the determination (Fla. Stat. 501.171(3)-(4)).

## 3. First hour (RS.MA, RS.MI): safety first
| Step | Who | Done when |
|---|---|---|
| 1. **Put irrigation in a safe state.** Switch each well pump and pivot to local or Hand control at its panel; turn fertigation injection off and close the injection valves; confirm pressures and flows at the meter faces. The PLC keeps running its last logic; do not rely on it until step 4 of section 5 | Irrigation Technician | All pumps and pivots in local control; fertigation off |
| 2. Unplug the HMI and all office computers from the network. **Leave them powered on** for memory evidence. Unplug the uplink from the pump house to the headquarters switch | Security lead with the Irrigation Technician | Devices and the pump house offline |
| 3. Disable the integrator's remote tool account at the vendor portal and change the account password. Tell the integrator by phone: **no remote connections until further notice** | Security lead | Tool disabled; integrator acknowledged |
| 4. Call the cyber insurer's breach hotline. Engage counsel and forensics through the insurer | Majority owner | Claim number issued |
| 5. Revoke all identity provider sessions; reset administrator credentials using a break-glass account from a clean device | Security lead | Sessions revoked |
| 6. Start paper operations: tally cards to crew leads, paper Produce Safety forms to the packing shed, hourly cooler checks, a staffed irrigation schedule | Farm Manager; Food Safety and Packing Lead | Paper workflow running |
| 7. Start the incident log: timeline, actions, who, and when | Security lead | Log open |

**Freeze nights (December to February).** If the incident happens in freeze season, the Farm Manager staffs the overhead system on site each night with two people, and starts it by hand at the trigger temperature from a thermometer reading. The automation is not trusted until section 5 is complete.

## 4. Analysis (RS.AN)
1. **Scope:** which endpoints, the HMI, the data hub VM, the backup vault, SYS-01 accounts, and the identity provider are affected? Use the remote tool history, identity provider sign-in logs, cloud activity logs, and SYS-01 audit trail. **Export logs now**; default retention can be as short as 30 days (POAM-010).
2. **Initial access:** confirm how the attacker got in (the remote tool account, a phished credential, or another path) and the first compromised host.
3. **OT integrity:** did the attacker change PLC logic, setpoints, schedules, or fertigation limits? Compare the PLC program with the farm-held approved backup (hash comparison), and review the SYS-01 irrigation change log. **If any fertigation setting changed, treat affected blocks as a possible food safety issue** and go to section 6 (distributor row).
4. **Exfiltration:** determine whether personnel, payroll, or H-2A files were taken (file access logs in the productivity suite; firewall egress). **This drives the Florida breach determination.**
5. **Backups:** confirm the backup vault and the SYS-01 vendor data are intact before any restore. SYS-01 is SaaS and may be unaffected; check with the vendor.
6. **Preserve evidence:** forensics images affected hosts and collects exported logs, with chain of custody.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure (IP addresses, domains) at the headquarters firewall and in the cloud network rules.
2. Remove the integrator remote tool from the HMI. Future access only through the jump host (POAM-002).
3. Rotate all shared and service passwords: HMI, SYS-01 integration keys, modems, the LoRaWAN gateway, and the dealer portal.
4. **Rebuild the HMI** from a clean image with the integrator on site, then load the farm-held HMI project. **Reload the PLC** from the farm-held approved program if the integrity check in section 4 step 3 fails or cannot be done. Record the program version.
5. Rebuild affected office computers and the data hub VM from clean images; patch before reconnecting.
6. Confirm with forensics that persistence is removed before any system goes back on the network.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Day 0 | Insurer notified; counsel engaged | Majority owner |
| Day 0, within 24 hours of awareness | Distributor food safety contact told of any event that could affect product safety, lot traceability, or volumes (supplier agreement). If fertigation may have been tampered with, say which blocks and lots | Farm Manager |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA. Supports the OFAC mitigation factors if payment is ever considered | Security lead |
| Day 0-2 | Crew meeting in English and Spanish: what happened, paper procedures, whom to call, do not discuss outside the farm | Farm Manager with Crew Leads |
| As soon as known | Breach determination under Fla. Stat. 501.171 documented, including the date of determination | Majority owner with counsel |
| Within 30 days of determination | Notice to affected individuals in Florida (English and Spanish templates); notice to the Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 are notified | Majority owner, Office and HR Manager, counsel |
| Same period | Notices for people outside Florida under their states' laws; H-2A workers now at home-country addresses notified by farm policy | Office and HR Manager, counsel |
| Each payday | H-2A earnings statements issued on time from paper tally and the payroll provider (20 CFR 655.122(k)) | Office and HR Manager |
| On request | Produce Safety records to FDA (paper forms and the latest monthly export; 21 CFR 112.166(a)); H-2A records to DOL within 72 hours (655.122(j)(2)) | Food Safety and Packing Lead; Office and HR Manager |

**Plan to the 30-day clock.** Florida's deadline runs from the determination, not from the end of the investigation. Counsel should set the determination date early and in writing.

**Not triggered for this farm (see the matrix for reasons):** the Reportable Food Registry (the farm is not a responsible party), CIRCIA (not final, and the farm is below the proposed size criterion), and FAR 52.204-25 (no federal contracts).

**Ransom decision:** requires the majority owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove notice duties if data was taken, and it does not make the PLC or HMI trustworthy again.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Manual irrigation stays in place throughout (people first, not systems)
2. Identity provider and administrator access (break-glass if needed)
3. Cooler alarm path and headquarters network, on the new segmented design if it exists, or with the pump house left disconnected
4. **PLC and HMI:** rebuilt and verified (section 5 step 4). Return to automatic control one pump and one pivot at a time with the Irrigation Technician watching a full cycle. Fertigation returns last, after a supervised test at low rate
5. SYS-01 irrigation module and harvest tally (vendor-hosted; confirm with the vendor that the farm's tenant was not accessed)
6. Clean laptops and tablets for crew leads and the office
7. Payroll (repeat prior payroll through the payroll provider if needed, then correct from the paper tally)
8. Farm data hub from immutable backup; re-sync flow history
9. Sales, telematics, imagery, and the AI pilot

**Validate before reconnecting:** EDR clean (once deployed), credentials rotated, systems patched, PLC program matches the approved version. Tell crews, the distributor, and the insurer when each process is back (RC.CO). Keep paper procedures until each process is back within its RTO (P05).

**End of recovery:** declared by the incident commander when all BP-01 to BP-03 processes run on automation for 72 hours without anomalies and the paper tally for the incident period has been keyed and reviewed.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires a written record within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-003, R-005, R-011, R-022), the POA&M (P07), the contingency plan, and this runbook.
- Keep all incident records for at least 3 years (POL-01 4.11), and any Florida no-harm determination for at least 5 years (Fla. Stat. 501.171(4)(c)).
