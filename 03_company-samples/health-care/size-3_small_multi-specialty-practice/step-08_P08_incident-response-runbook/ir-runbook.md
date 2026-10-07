# Incident Response Runbook: Ransomware with PHI Exfiltration

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (multi-specialty physician practice) |
| Tier / Vertical | Small / Health Care and Social Assistance |
| Incident type | Ransomware with PHI exfiltration (double extortion), starting from a phishing email |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager (Security Officer) |
| Approved | 2026-08-31 by the Practice Administrator |
| Last tested | Not yet. First tabletop exercise due 2026-11-30 (POAM-014) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | Practice Administrator | Incident line (cell), then the out-of-band group chat on personal phones |
| Technical response | MSP incident team | Forensic firm on retainer (engaged through the insurer's panel) | MSP 24x7 line |
| Breach and privacy decisions | Medical Director (Privacy Officer) | Practice Administrator | Cell |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Via insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Clinical operations | Clinic A and Clinic B Managers | Medical Director | Cell |
| Communications | Practice Administrator | Outside PR (via counsel) | Cell |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email and chat are compromised. Coordinate on personal phones and the printed contact list in the incident binder at each clinic.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at both clinics: this runbook, contacts, downtime forms, and the notification matrix
- [ ] Immutable backups in a separate account, with a restore test within the last 90 days (CP-9, CP-4). **Gap until POAM-003 and POAM-004 close**
- [ ] EDR deployed with 24x7 alerting (SI-4). **Gap until POAM-005 closes**
- [ ] Two break-glass accounts sealed and tested (POL-02 4.7)
- [ ] Downtime kits (paper forms, printed schedules) at each front desk (P05)
- [ ] Forensic retainer and insurer panel confirmed (POAM-014)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or files renamed with an unknown extension | Staff report, EDR alert | Call the incident line. **Do not power off.** Unplug the network cable or turn off Wi-Fi |
| Many files changing at once on a share or VM | EDR, backup job failure | IT Manager opens the incident |
| Staff report clicking a phishing link and entering credentials | Staff report | Reset password, revoke sessions, review sign-ins; escalate if there is lateral activity |
| Large outbound transfer to an unknown destination | Firewall alert | Block the destination; open an incident |
| Extortion email or leak-site post naming the practice | Email, threat intelligence, law enforcement | Declare the incident; preserve the message |

**Declare a ransomware incident when** encryption or a ransom note is confirmed on any system, or an extortion claim names practice data.
**Record the time of discovery.** Under 45 CFR 164.404(a)(2), a breach counts as discovered on the first day it is known, or by reasonable diligence would have been known, to any workforce member.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Isolate affected endpoints from the network (cable out, Wi-Fi off). Leave them powered on for memory evidence | Staff with IT on phone | Devices are offline |
| 2. Disable site-to-site VPN tunnels to the cloud tenant if the cloud workloads may be affected | IT Manager | Tunnels down |
| 3. Call the cyber insurer's breach hotline. Engage counsel and forensics through the insurer | Practice Administrator | Claim number issued |
| 4. Reset credentials for all administrators with break-glass accounts; revoke all sessions in the identity provider | IT Manager | Sessions revoked |
| 5. Activate downtime procedures at both clinics | Clinic Managers | Paper workflow running |
| 6. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** which endpoints, servers, cloud workloads, and accounts are affected? Check EDR, identity provider sign-in logs, cloud audit logs, and firewall logs.
2. **Initial access:** identify the phishing email, the credential used, and the first compromised host.
3. **Preserve evidence:** forensics images affected hosts and exports logs before they roll over (default retention can be as short as 30 days; POAM-008). Maintain chain of custody.
4. **Exfiltration:** determine whether PHI was accessed or taken. Check for archive or transfer tools, firewall egress, and cloud storage access logs. **This drives the breach determination.**
5. **Backups:** confirm the backup vault is intact before any restoration. Check the EHR vendor's status separately; the EHR is SaaS and may be unaffected.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure (IPs, domains) at both firewalls and in the cloud network rules.
2. Disable compromised accounts. Rotate service account and interface credentials (interface engine, lab, clearinghouse).
3. Rebuild affected endpoints from the standard image. **Do not decrypt and reuse them.**
4. Rebuild affected cloud VMs from clean images, and patch before reconnecting.
5. Confirm with forensics that persistence mechanisms are removed before recovery.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Legal counsel confirms every notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Day 0 | Insurer notified; counsel engaged | Practice Administrator |
| Day 0-2 | Voluntary report to FBI (IC3) and/or CISA. Supports OFAC mitigation if payment is considered | IT Manager |
| Day 0-5 | Staff briefing script: what happened, downtime steps, do not discuss outside the practice | Practice Administrator |
| As soon as known | Four-factor breach risk assessment (45 CFR 164.402) documented | Privacy Officer |
| Within 30 days of determination | Florida individual notice, or HIPAA notice with a copy to the Department of Legal Affairs under the deemed-compliance path; Department notice if 500+ Floridians | Privacy Officer and counsel |
| Within 60 days of discovery | HIPAA individual notices; HHS notice if 500+ (contemporaneous); media notice if more than 500 Florida residents | Privacy Officer and counsel |
| Within 60 days after year end | HHS breach log submission if fewer than 500 | Privacy Officer |

**Plan to the shorter clock.** Florida's 30-day deadline (from determination) can arrive before HIPAA's 60-day outer limit (from discovery). Counsel should confirm the deemed-compliance path early.

**Ransom decision:** requires the majority owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.6). Paying does not remove breach notification duties if data was taken.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Identity provider and administrator access (break-glass if needed)
2. Clinic internet and network (cellular backup if needed)
3. Clean endpoints for front desk and providers: 4 pre-imaged spares per clinic
4. EHR/PM access (vendor-hosted; confirm the vendor's integrity statement)
5. Interface engine: restore from immutable backup, verify integrity, reconnect the lab and clearinghouse
6. Imaging archive: restore and verify studies against the modality's local cache
7. Clearinghouse connectivity and the claims backlog
8. Payroll

**Validate before reconnecting:** EDR is clean, credentials are rotated, and the system is patched. Tell staff and patients when services are restored (RC.CO). Keep downtime forms until each process is back on its RTO (P05).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-005), the POA&M (P07), and this runbook.
- Retain all incident documentation for 6 years (POL-01 4.10).
