# Incident Response Runbook: Intrusion into Distribution Control Systems (OT)

| Field | Value |
|---|---|
| Organization | Cris Santos Electric Cooperative, Inc. (member-owned electric distribution cooperative; not NERC-registered) |
| Tier / Vertical | Micro / Utilities |
| Incident type | Unauthorized operation of field devices through SCADA. Scenario: at 23:40 an attacker signs in to the hosted SCADA web HMI with the shared operator password and opens the 3 feeder reclosers at Substation 1, dropping all about 820 meters, including the county water plant, the fire station, and 26 members on the medical-needs list |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT practices from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy. This runbook is the cyber annex to the Emergency Restoration Plan (7 CFR 1730.28(c)(6)) |
| Runbook owner | Line Superintendent (operational steps), with the Office and Finance Manager (Security Coordinator) for notices and records |
| Approved | 2026-08-31 by the General Manager |
| Last tested | Never. One-hour tabletop with the MSP and the SCADA vendor scheduled 2026-11-18; full exercise in the May 2027 ERP exercise (7 CFR 1730.28(f)) |

**Safety first.** People come before evidence. Before anything is re-closed, the Line Superintendent confirms that no crew is working on an affected line and that each feeder has been checked for a real fault. Medical-needs members get a call as soon as an outage will last more than 1 hour.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Operational incident commander | Line Superintendent | On-call Journeyman Lineworker until the Line Superintendent arrives | Cell; truck radio |
| Decision maker (money, notices, insurer, law enforcement) | General Manager | Office and Finance Manager | Cell |
| Notices, log, vendors, members | Office and Finance Manager (Security Coordinator) | Member Services Representative | Cell |
| SCADA service | SCADA vendor 24x7 support line (by phone, **not** through the HMI) | SCADA vendor account manager | Number on the printed contact sheet |
| Office IT and backup vault | MSP | MSP after-hours line | Cell |
| AMI | AMI vendor support | Meter and Service Technician | Phone |
| Insurer and response firm | Insurer 24x7 hotline (panel counsel and an OT-capable forensic firm) | | Policy number on the contact sheet |
| External | G&T control center (24x7); DOE Operations Center; CISA; FBI field office; county emergency management; water plant operator | | Printed contact sheet |

**Out-of-band first.** Assume the attacker can see SCADA screens and may read email. Coordinate by cell phone and truck radio, using the printed contact sheet in the ERP binder and in every truck.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed runbook, contact sheet, notification matrix, and feeder switching sheets in the ERP binder, in every truck, and at the General Manager's and Line Superintendent's homes (POL-03 4.1)
- [ ] Named SCADA accounts with MFA; shared login disabled. **Gap until POAM-001 and POAM-002 close (2026-10-31)**
- [ ] SCADA vendor able to lock every cooperative account on one phone call; procedure agreed in writing. **Agree by 2026-10-31**
- [ ] Each feeder recloser control's "remote control disabled" switch labeled, and every field staff member trained to use it
- [ ] Approved settings for every recloser, regulator, and RTU in the vault and printed in the ERP binder (POL-04 4.7). **Gap until POAM-007 closes**
- [ ] DOE-417 filing arrangement with the G&T and the Balancing Authority signed, and the cooperative's DOE-417 online account set up. **Gap until POAM-011 closes (2026-10-31)**
- [ ] Printed medical-needs list with phone numbers, by feeder, in the ERP binder
- [ ] Insurer hotline and policy number on the contact sheet; OT-capable firm confirmed on the panel

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A recloser opens with no fault targets, no storm, and no one switching | SCADA alarm text to the on-call lineworker; outage calls | On-call lineworker calls the Line Superintendent at once and treats it as a possible intrusion |
| Recloser or regulator settings change that no one made | SCADA event log; device display | Line Superintendent declares; do not re-close remotely |
| SCADA sign-in alert from an unknown location or at an odd hour (once alerts exist) | SCADA vendor alert | Line Superintendent asks the vendor to lock the account |
| Many AMI meters disconnect or load-control switches operate with no scheduled event | AMI head-end; member calls | Meter and Service Technician calls the Line Superintendent |
| Tip from the SCADA vendor, the G&T, CISA, or the FBI | External | Declare and investigate |

**Declare an OT intrusion when** any device operation, setting change, or sign-in cannot be explained by staff, a scheduled event, an automatic protection action, or a vendor session the Line Superintendent approved.

**Record the times** on the incident log: when the reclosers opened (DOE-417 clocks run from the incident), when the event was declared, and each call made.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Stop remote control.** Call the SCADA vendor support line and ask it to lock all cooperative SCADA accounts. At the same time, send the nearest lineworker to Substation 1 to set each feeder recloser control to "remote control disabled" | Line Superintendent | Vendor confirms lock; switches set and photographed |
| 2. **Make it safe.** Confirm that no crew is working on any feeder. Patrol each feeder's first section for faults before closing | Line Superintendent | All crews accounted for |
| 3. **Restore by local control.** Close feeder reclosers at the device, one feeder at a time, starting with the feeder that serves the water plant and the fire station. Leave remote control disabled | Line Superintendent and lineworkers | Each feeder closed and holding |
| 4. **Tell the G&T control center** that load at the delivery point dropped and is being restored, and that the cause is a suspected cyber intrusion | Line Superintendent | Call logged |
| 5. **DOE-417 Emergency Alert within 1 hour** of the reclosers opening: criterion 3 (cyber event interrupting operations) and criterion 4 (complete shut-down of the distribution system). Under the filing arrangement, confirm with the G&T who files; if in doubt, the cooperative files or phones the DOE Operations Center | Line Superintendent, with the General Manager | Form submitted or phoned; confirmation number logged |
| 6. **Call the insurer hotline**; engage panel counsel and the OT-capable forensic firm | General Manager | Claim number issued |
| 7. **Medical-needs calls** for members on affected feeders if the outage will pass 1 hour; tell the water plant operator and county emergency management | Office and Finance Manager; Member Services Representative | Calls logged |
| 8. **Start the incident log**: timeline, actions, who, and when; photographs of device displays before any setting is changed | Office and Finance Manager | Log open |

## 4. Analysis (RS.AN)
1. **How did they get in?** Ask the SCADA vendor for the sign-in and command history for the last 90 days: account, source address, time, and every command. With one shared login, the log cannot say which person used it, so check each field staff member's whereabouts and devices.
2. **What else did they touch?** Check whether any settings changed on the recloser, regulator, and RTU controls (compare with the approved settings files), whether vendor support sessions were open, and whether the 6 line recloser modems show sign-ins.
3. **Other systems.** Ask the AMI vendor for disconnect and load-control commands in the same window. Ask the MSP to check the operations workstation, the truck tablets, and the office computers for malware that could have captured the password (P01 R-016). Check whether the outage module (medical-needs list) or the business suite was accessed. That decides the Florida breach analysis.
4. **Preserve evidence.** Get written confirmation from the SCADA vendor that it has preserved logs beyond the 90-day window. Do not wipe the operations workstation or tablets until the forensic firm has imaged them. Keep chain of custody.
5. **Scope decision.** The General Manager records whether the incident is contained to SCADA, whether member data was involved, and whether the forensic firm recommends further containment.

## 5. Containment and eradication (RS.MI)
1. Keep remote control disabled at the devices until step 4 below is done and the Line Superintendent approves.
2. Have the SCADA vendor create named accounts with MFA for the 4 field staff and the Line Superintendent (POAM-001, POAM-002), and delete the shared operator login. Disable vendor standing access; re-enable only on request (POL-02 B.6).
3. Change every device password (recloser, regulator, RTU, gateway, modems) from a clean laptop (POL-02 B.7).
4. **Settings integrity check.** Compare every device's settings with the approved files in the vault and the printed copies. Reload any that differ, and test before returning the device to remote control.
5. Reimage the operations workstation and any tablet the forensic firm flags; enroll them in MSP management before reconnecting.
6. Confirm with the forensic firm and the SCADA vendor that the attacker's access path is closed.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** The Office and Finance Manager tracks every clock on the incident log. Counsel reviews member and regulator notices.

| When | Action | Owner |
|---|---|---|
| Immediately | G&T control center by phone | Line Superintendent |
| Within 1 hour of the incident | DOE-417 Emergency Alert (criteria 3 and 4), by the cooperative or the G&T under the filing arrangement | Line Superintendent |
| Within 6 hours of the incident | DOE-417 Normal Report instead, if the event was stopped before it interrupted service (criterion 11) | Line Superintendent |
| Same day | Voluntary report to CISA and the FBI | General Manager |
| Within 72 hours of the incident | DOE-417 final report (unless an interim update has been provided) | Office and Finance Manager |
| During the outage | Outage updates on the outage map, IVR, and social media; no attack details without counsel | Office and Finance Manager |
| Within 30 days of a breach determination | Florida notices to members (and the Department of Legal Affairs if 500 or more, consumer reporting agencies if more than 1,000), only if member personal information was accessed | Office and Finance Manager with counsel |
| Next Board meeting | Report to the Board of Trustees (POL-02 A.10) | General Manager |

**Extortion or ransom demand:** requires the General Manager and the Board chair, counsel, the insurer, and an OFAC sanctions check (POL-03 4.8).

**Not applicable:** NERC CIP-008 and EOP-004 reports (not registered). **Proposed rule watch:** the CIRCIA final rule had not been published as of 2026-09-25 and is not a current obligation.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Field restoration by local control (already running from step 3)
2. Outage calls and the outage module (business suite; confirm it was not affected)
3. SCADA monitoring with view-only access, after the vendor confirms its own service is clean
4. SCADA remote control, feeder by feeder, only after named accounts with MFA are live and settings are verified (target 8 hours, BP-02 RTO; a lineworker stays at Substation 1 until then)
5. Line reclosers, one at a time, after their modem passwords are changed and their management ports are confirmed closed
6. AMI remote disconnect and load control, after the AMI command history is cleared and the two-person rule is on
7. Peak management, billing, and back-office systems

**Validate before reconnecting:** credentials are changed, MFA is on, settings match the approved files, and vendor access is off. Tell members when service is fully restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery with the MSP, the SCADA vendor, and the G&T (POL-03 4.11 requires a written report within 30 days).
- Update this runbook, the ERP, and the VRA (7 CFR 1730.27(a): significant changes call for an additional VRA).
- Update the risk register (P01, especially R-001, R-002, R-008, R-014) and the POA&M (P07).
- Report to the Board of Trustees.
- Keep the incident records under POL-02 A.7.
