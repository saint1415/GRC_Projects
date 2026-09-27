# Incident Response Runbook: Ransomware Forcing EHR Downtime and Ambulance Diversion

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural critical access hospital, 12 beds, 24-hour ED) |
| Tier / Vertical | Small / Healthcare and Public Health |
| Incident type | Ransomware that encrypts hospital-managed systems, forces disconnection from the hosted EHR, and may require ambulance diversion. Likely initial access: the teleradiology vendor's shared VPN account (P01 R-001) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Emergency plan link | This runbook is the cyber annex to the emergency preparedness plan (42 CFR 485.625(a)(2)); the diversion and communications steps use that plan's incident command and communication plan (485.625(c)) |
| Runbook owner | IT Manager (Security Officer) |
| Approved | 2026-08-31 by the CEO |
| Last tested | Not yet. First tabletop by 2026-11-30, filed as the emergency program's additional exercise (POAM-014) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (technical) | IT Manager | IT Support Specialist, then MSP incident lead | Incident line (cell), then the out-of-band group on personal phones |
| Hospital incident command | CEO | Director of Nursing | Cell; command post in the administration conference room |
| Clinical safety and downtime lead | Director of Nursing | House supervisor on duty | Cell; overhead page if phones work |
| ED medical lead | ED physician on duty (emergency physician group) | Chief of Medical Staff | ED analog line |
| Technical response | MSP incident team | Forensic firm on retainer (through the insurer's panel) | MSP 24x7 line (after POAM-005; business hours only today) |
| Breach and privacy decisions | Quality and Compliance Manager (Privacy Officer) | CEO | Cell |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Via insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Emergency preparedness liaison | Facilities Manager | CEO | Cell; county emergency management line |
| County EMS dispatch | Dispatch supervisor | County EMS director | EMS radio in the ED; analog line |
| Receiving hospitals | Regional hospital transfer center | Second transfer partner | Numbers in the incident binder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, the VoIP phones, and the file server are compromised or unavailable. Coordinate on the analog lines in the ED and at the nursing station, the EMS radio, personal cell phones, and the printed contact list in the incident binder at the nursing station, the ED, and the administration office.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder in three places: this runbook, the contact list, the downtime procedures, the notification matrix, and the diversion request script
- [ ] Downtime PCs in the ED and at the nursing station tested this month, with printed census and MAR reports less than 2 hours old (P05)
- [ ] Downtime kits (paper ED records, MARs, order sheets, laboratory and imaging requisitions, registration forms) on each unit
- [ ] Immutable backups in a separate account with a restore test in the last 90 days (CP-9, CP-4). **Gap until POAM-003 and POAM-004 close**
- [ ] 24x7 alert monitoring (SI-4). **Gap until POAM-005 closes**
- [ ] Named vendor accounts with MFA (AC-17). **Gap until POAM-008 closes; interim: shared account enabled only in support windows**
- [ ] Two break-glass accounts sealed and tested (POL-02 4.7)
- [ ] Forensic retainer and insurer panel confirmed (POAM-014)
- [ ] Six pre-imaged spare laptops for the ED, nursing station, pharmacy, and laboratory (P05)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note on a screen, or files renamed with an unknown extension | Staff report, EDR alert | Call the incident line. **Do not power off.** Unplug the network cable or turn off Wi-Fi |
| Several workstations, the dispensing cabinets, or the analyzer middleware stop at once | Nursing, pharmacy, laboratory | Charge nurse calls the incident line and starts downtime on the unit |
| EHR vendor calls to say it has cut the hospital's connection because of malicious traffic | EHR vendor | IT Manager opens the incident; Director of Nursing starts downtime |
| Many files changing at once on the file server or cloud workloads; backup jobs failing | EDR, backup reports | IT Manager opens the incident |
| Unusual VPN sign-in (vendor account at night, new country) | Firewall or identity provider alert | Disable the account; open the incident |
| Extortion email or leak-site post naming the hospital | Email, threat intelligence, law enforcement | Declare the incident; preserve the message |

**Declare a ransomware incident when** encryption or a ransom note is confirmed on any system, or an extortion claim names hospital data.
**Record the time of discovery.** Under 45 CFR 164.404(a)(2), a breach counts as discovered on the first day it is known, or by reasonable diligence would have been known, to any workforce member. Night-shift reports count.

## 3. First hour (RS.MA, RS.MI, and patient safety)
Two tracks start together: the **technical track** (IT Manager) and the **clinical track** (Director of Nursing). The CEO opens hospital incident command and joins them every 30 minutes.

| Step | Who | Done when |
|---|---|---|
| 1. Start downtime procedures on every unit, the ED, pharmacy, laboratory, imaging, and registration | Director of Nursing; charge nurses | Paper workflow running; last downtime PC print collected |
| 2. Isolate affected endpoints (cable out, Wi-Fi off). Leave them powered on for memory evidence | Staff with IT on phone | Devices offline |
| 3. Disable the teleradiology and MSP remote access paths, and the site-to-site VPN tunnels to the cloud tenant and EHR vendor if they may be affected | IT Manager | Tunnels and vendor accounts down |
| 4. Check infusion pumps, monitors, and dispensing cabinets: pumps keep their last drug library; switch cabinets to override with nurse double-check | Director of Nursing; pharmacy technician | Safety checks logged |
| 5. Call the cyber insurer's breach hotline; engage counsel and forensics through the insurer | CEO | Claim number issued |
| 6. Revoke all identity provider sessions; reset administrator credentials with break-glass accounts | IT Manager | Sessions revoked |
| 7. Assess whether the ED can safely accept ambulances (section 4) | CEO, Director of Nursing, ED physician | Decision recorded with time |
| 8. Start the incident log: timeline, actions, who, and when (on paper) | IT Manager | Log open |

## 4. Clinical operations and ambulance diversion (RS.MA, RC.RP)
**What diversion means here.** EMTALA lets a hospital direct an ambulance that is not yet on its property to another facility when it is in "diversionary status" because it lacks the staff or facilities to accept more emergency patients (42 CFR 489.24(b), definition of "comes to the emergency department"). It does **not** change the duty to screen and stabilize anyone who arrives: walk-ins, and any ambulance that comes onto hospital property anyway, are still screened and stabilized. The next hospital is about 45 miles away, so diversion carries its own risk.

**Decision rule (from the P05 MTDs).** The CEO (or delegate), the Director of Nursing, and the ED physician on duty decide together. Consider diversion when any of these is true and not expected to recover within the BIA MTD:
- CT, or the route to teleradiology reads, is down (BP-05, MTD 8 h). Divert CT-dependent ambulance traffic (suspected stroke, major trauma) first.
- Laboratory results cannot be produced or reported (BP-04, MTD 4 h).
- Phones and alternate communications are not working (BP-12, MTD 2 h).
- The ED cannot document, order, or give medications safely on paper (BP-01, MTD 4 h).

**Diversion steps:**
1. Notify county EMS dispatch by radio or analog line, using the script in the binder: scope (full or CT-dependent only), reason ("IT systems outage"), and next update time. Do not say "cyberattack" on open radio.
2. Notify county emergency management and the regional receiving hospitals (485.625(c)(7) and (b)(7)).
3. Record every diversion decision and status change with the time.
4. Review diversion status at least every 2 hours, and end it as soon as the affected process is back within its RTO or a safe workaround is running.

**Patients already in the hospital.** Continue care on paper. Transfer patients who need services the hospital cannot provide without its systems, using the paper transfer packet and a copy log (485.625(c)(4)). The HIM Manager tracks every paper record created (POL-04 4.7).

## 5. Analysis (RS.AN)
1. **Scope:** which endpoints, servers, cloud workloads, medical device workstations, OT controllers, and accounts are affected? Check EDR, identity provider sign-in logs, VPN logs, cloud audit logs, and firewall logs.
2. **Initial access:** check the teleradiology VPN account and the MSP tool first, then phishing. Identify the first compromised host and account.
3. **Preserve evidence:** forensics images affected hosts and exports logs before they roll over (some default retention is as short as 30 days; POAM-005). Maintain chain of custody.
4. **Exfiltration:** determine whether PHI was accessed or taken. Check for archive or transfer tools, firewall egress volumes, file server access, and cloud storage access logs. **This drives the breach determination.**
5. **Backups:** confirm that backup copies are intact and clean before any restore. Today the appliance and the cloud vault may both be reachable by the attacker (POAM-003).
6. **EHR:** ask the EHR vendor for its written statement on whether its platform and the hospital's data were affected, and what it needs before it will reconnect the hospital.
7. **Devices and OT:** with the manufacturers, check the CT workstation, pump drug-library server, dispensing cabinet server, and OT controllers for tampering. Verify the pump drug library against the pharmacist's last approved version before pumps receive any update.

## 6. Containment and eradication (RS.MI)
1. Block attacker infrastructure (IPs, domains) at the firewall and in the cloud network rules.
2. Disable compromised accounts. Rotate service account and interface credentials (interface engine, reference laboratory, HIE, clearinghouse, teleradiology route).
3. Replace the shared teleradiology account with named accounts and MFA before reconnecting the vendor.
4. Rebuild affected endpoints and servers from clean images. **Do not decrypt and reuse them.**
5. Rebuild affected cloud VMs from clean images, and patch before reconnecting.
6. Confirm with forensics that persistence is removed before recovery. The EHR vendor will usually require this confirmation before reconnecting.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Legal counsel confirms every notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer notified; counsel engaged | CEO |
| Hour 1 | County EMS and emergency management informed of any diversion or capability limits | CEO or Facilities Manager |
| Day 0-1 | Voluntary report to the FBI (IC3) and CISA. Supports the OFAC mitigating factor if payment is considered | IT Manager |
| Day 0-1 | Staff briefing (in person at shift huddles): what happened, downtime steps, do not discuss outside the hospital | Director of Nursing |
| Day 1-2 | Community statement that the hospital is open and caring for patients, with any service limits | CEO (with counsel) |
| As soon as facts allow | Four-factor breach risk assessment (45 CFR 164.402) documented | Privacy Officer |
| Within 30 days of determination | Florida individual notice, or HIPAA notice with a copy to the Department of Legal Affairs under the deemed-compliance path; Department notice if 500 or more Floridians | Privacy Officer and counsel |
| Within 60 days of discovery | HIPAA individual notices; HHS notice if 500 or more (contemporaneous); media notice if more than 500 residents of a state | Privacy Officer and counsel |
| Within 60 days after year end | HHS breach log if fewer than 500 | Privacy Officer |

**Plan to the shorter clock.** Florida's 30-day deadline (from determination) can arrive before HIPAA's 60-day outer limit (from discovery). Counsel should confirm the deemed-compliance path early.

**CIRCIA.** Not in effect as of 2026-09-26. If finalized as proposed, this hospital would have to report a covered incident to CISA within 72 hours and a ransom payment within 24 hours. Recheck the matrix whenever the rule changes.

**Ransom decision:** requires the governing body, counsel, the insurer, and an OFAC sanctions check (POL-03 4.6). Paying does not remove breach notification duties if data was taken, and it does not guarantee working decryption.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7):
1. Phones: analog lines, radio, and cellular phones first; VoIP after the network is clean
2. Identity provider and administrator access (break-glass if needed)
3. Firewall, core network, and internet (cellular backup for EHR traffic only)
4. Clean endpoints for the ED, nursing station, pharmacy, and laboratory (pre-imaged spares)
5. EHR access, after the vendor's reconnection conditions are met
6. Dispensing cabinet server and analyzer middleware
7. OT monitoring
8. Imaging archive and the route to teleradiology: restore, verify study counts against the CT's local cache
9. Interface engine: reference laboratory, HIE, and public health feeds; resend queued reportable results
10. File and print servers
11. Clearinghouse connectivity and the claims backlog
12. Payroll

**Validate before reconnecting:** EDR clean, credentials rotated, systems patched, vendor accounts named with MFA. **Back-entry:** each unit enters or scans its downtime records within 24 hours of recovery, starting with medication administration and results (POL-04 4.7). End diversion and tell EMS, emergency management, staff, and the community when services are restored (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days).
- File the after-action report in the emergency preparedness binder; an actual emergency that requires activating the emergency plan exempts the hospital from its next required full-scale or functional exercise, and the response must be analyzed and documented (485.625(d)(2)(i)(B) and (d)(2)(iii)).
- Update the risk register (P01, especially R-001, R-003, R-004, R-005, R-016), the POA&M (P07), and this runbook.
- Retain all incident documentation for 6 years (POL-01 4.11).
