# Incident Response Runbook: CAD Outage from Ransomware

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensed private ambulance service) |
| Tier / Vertical | Small / Emergency Services |
| Incident type | Ransomware encrypts the CAD application server and dispatch consoles, forcing manual dispatch (possible theft of PHI) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager (Security Officer) |
| Approved | 2026-09-04 by the COO |
| Last tested | Not yet. First tabletop due 2026-11-30 (POAM-015); first manual dispatch drill due 2026-10-31 (POAM-005) |

**Two tracks run at once.** Track A keeps ambulances moving (dispatch continuity). Track B handles the security incident. Track A never waits for Track B.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Dispatch continuity (Track A lead) | On-duty dispatch supervisor | Communications Center Supervisor | Dispatch room; supervisor cell |
| Incident commander (Track B lead) | IT Manager | COO | Incident line (cell), then the out-of-band group chat on personal phones |
| Technical response | MSP incident team; CAD vendor support | Forensic firm on retainer (through the insurer's panel) | MSP 24x7 line; CAD vendor support line |
| Clinical safety | Medical Director | Clinical Services Coordinator | Cell |
| Breach and privacy decisions | Billing and Compliance Manager (Privacy Officer) | COO | Cell |
| County liaison | COO | Communications Center Supervisor | County PSAP supervisor line; county EMS contract manager |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Via insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and anything on the headquarters network are compromised. Coordinate on personal phones, the county P25 radio talkgroup, and the printed contact list in the incident binder in the dispatch room and at Station 2.

## 1. Preparation checks (Identify / Protect)
- [ ] Manual dispatch binder in the dispatch room and at Station 2: paper incident cards, unit status board, run cards by zone, radio procedure, county PSAP numbers
- [ ] Manual dispatch drilled in the last 90 days (CP-4). **Gap until POAM-005 closes**
- [ ] Immutable CAD database and integration engine backups in a separate account, with a restore test in the last 90 days (CP-9, CP-4). **Gap until POAM-004 and POAM-005 close**
- [ ] EDR on consoles and cloud VMs with 24x7 alerting (SI-3, SI-4). **Gap until POAM-006 closes**
- [ ] 3 pre-imaged spare dispatch laptops kept offline (P05 priority 4)
- [ ] Two break-glass accounts and the sealed CAD admin credential tested (POL-02 4.7)
- [ ] Paper patient care record kits in every ambulance (P05 BP-03)
- [ ] Forensic retainer and insurer panel confirmed (POAM-015)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| CAD client freezes or shows errors on several consoles at once | Dispatcher | Supervisor starts Track A (manual mode) at once; calls the IT Manager |
| Ransom note on a console, or files renamed with an unknown extension | Dispatcher, EDR alert | **Do not power off.** Unplug the console's network cable. Start Track A. Call the incident line |
| CAD server or database unreachable; unusual admin activity in the cloud tenant | MSP, cloud audit log | IT Manager opens the incident |
| MDCs lose CAD but radio works | Crews | Crews switch to radio status reports; dispatch confirms manual mode |
| Extortion email or leak-site post naming the company | Email, threat intelligence, law enforcement | Declare the incident; preserve the message |

**Declare a ransomware incident when** encryption or a ransom note is confirmed on any console or server, or an extortion claim names company data.
**Record the time of discovery.** Under 45 CFR 164.404(a)(2), a breach counts as discovered on the first day it is known, or by reasonable diligence would have been known, to any workforce member. The Florida 30-day clock starts at determination of the breach or reason to believe one occurred (Fla. Stat. 501.171(4)).

## 3. Track A: keep dispatching (RC.RP, CP-2)
| Step | Who | Done when |
|---|---|---|
| A1. Announce "manual dispatch" to all units on the company talkgroup. Units report location and status by radio | Dispatch supervisor | All staffed units acknowledged |
| A2. Call the county PSAP supervisor: CAD-to-CAD is down; ask the PSAP to voice-announce new county calls on the P25 system and transfer callers by phone | Dispatch supervisor | PSAP confirms |
| A3. Start paper incident cards and the unit status board. One dispatcher takes calls, one tracks units, the supervisor assigns | Dispatchers | Board matches radio roll call |
| A4. Forward request lines to supervisor cell phones if console phones are affected | Communications Center Supervisor | Test call answered |
| A5. Tell hospitals and nursing facilities that non-urgent interfacility trips may be delayed; defer scheduled non-urgent trips | Communications Center Supervisor | Facility call list done |
| A6. Crews switch to paper patient care records if tablets cannot sync | Operations Manager | Crews confirm |
| A7. **At 2 hours in manual mode (P05 MTD)**, or sooner if the Medical Director judges it unsafe, ask the county PSAP to route new 911 calls in the zone to the mutual-aid provider | COO with the Medical Director | County confirms routing |
| A8. Log every Track A decision with the time | Dispatch supervisor | Log kept |

## 4. Track B: first hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| B1. Isolate affected consoles (cable out). Leave them powered on for memory evidence | Dispatchers with IT on the phone | Consoles offline |
| B2. Disable the site-to-site and vehicle VPN tunnels into the cloud tenant if the CAD server may be affected; block the MSP remote tool until it is cleared | IT Manager | Tunnels and tool blocked |
| B3. Call the cyber insurer's breach hotline. Engage counsel and forensics through the insurer | COO | Claim number issued |
| B4. Revoke all identity provider sessions; reset administrator credentials using break-glass accounts; change the cloud root and CAD admin credentials | IT Manager | Sessions revoked; credentials changed |
| B5. Snapshot the CAD server and database for evidence before any restore | MSP | Snapshots taken and tagged |
| B6. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

## 5. Analysis (RS.AN)
1. **Scope:** which consoles, VMs, cloud accounts, and user accounts are affected? Check EDR (once deployed), identity sign-in logs, cloud audit logs, firewall logs, and the MSP tool's session history.
2. **Initial access:** likely paths are phishing, the MSP remote tool (P01 R-021), an unpatched console (R-004), or a vehicle router (R-007). Identify the first compromised host.
3. **Preserve evidence:** forensics images affected hosts and exports logs before they roll over (default retention can be as short as 30 days; POAM-009). Maintain chain of custody with a signed evidence log.
4. **Exfiltration:** determine whether CAD database records (patient names, addresses, chief complaints) or call recordings were accessed or taken. Check database query logs, storage access logs, and egress. **This drives the breach determination.**
5. **Backups and SaaS:** confirm the backup vault and database snapshots are intact before any restore. Check the ePCR and billing platforms separately; they are SaaS and may be unaffected, but confirm no stolen credentials were used there.

## 6. Containment and eradication (RS.MI)
1. Block attacker infrastructure (IPs, domains) at both firewalls and in the cloud network rules.
2. Disable compromised accounts. Rotate CAD service accounts, integration engine credentials, and the county interface credentials (tell the county PSAP first).
3. Rebuild consoles from the standard image, or deploy the 3 spare laptops. **Do not decrypt and reuse encrypted machines.**
4. Rebuild the CAD server from a clean image with the CAD vendor, and patch before reconnecting.
5. Confirm with forensics that persistence is removed, including in the MSP tool, before recovery.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Legal counsel confirms every notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Hour 0 | County PSAP told that dispatch is manual (A2) | Dispatch supervisor |
| Day 0 | Insurer notified; counsel engaged; county EMS contract manager informed | COO |
| Day 0-2 | Voluntary report to FBI (IC3) and CISA. Supports the OFAC mitigating factor if a payment is ever considered | IT Manager |
| Day 0-5 | Staff briefing script: what happened, manual mode steps, do not discuss outside the company | COO |
| As soon as known | Four-factor breach risk assessment (45 CFR 164.402) documented | Privacy Officer |
| Within 30 days of determination | Florida individual notice, or HIPAA notice with a copy to the Department of Legal Affairs under the deemed-compliance path; Department notice if 500 or more Floridians | Privacy Officer and counsel |
| Within 60 days of discovery | HIPAA individual notices; HHS notice if 500 or more (contemporaneous); media notice if more than 500 Florida residents | Privacy Officer and counsel |
| Within 60 days after year end | HHS breach log submission if fewer than 500 | Privacy Officer |

**Plan to the shorter clock.** Florida's 30-day deadline (from determination) can arrive before HIPAA's 60-day outer limit (from discovery). Counsel should confirm the deemed-compliance path early.

**CIRCIA is not yet in force.** If the final rule is published and matches the proposal, this incident would also need a CISA report within 72 hours, and a ransom payment report within 24 hours. Recheck the rule's status at each annual review.

**Ransom decision:** requires the majority owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Manual dispatch and county help must be sustained while the decision is made. Paying does not remove breach notification duties if data was taken.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Items 1 and 2 are already running from Track A:
1. County P25 radio and manual dispatch mode
2. Phone lines (forwarded to supervisor cell phones if needed)
3. Identity provider and administrator access (break-glass if needed)
4. Headquarters network and clean dispatch consoles (3 spare laptops first)
5. CAD server and database: restore the database to a point in time before the compromise, verify integrity with the CAD vendor, then reconnect consoles
6. Vehicle routers and MDCs: re-enroll and reconnect
7. Integration engine: restore, rotate credentials, and reconnect the county CAD-to-CAD link and the ePCR push, testing each with the county
8. ePCR sync; back-enter paper patient care records within 48 hours so hospitals can get them (Rule 64J-1.014, F.A.C.)
9. Billing: import the backlog of trips
10. Scheduling and payroll

**Validate before leaving manual mode:** EDR shows clean hosts, credentials are rotated, systems are patched, and a test incident runs end to end (entry, unit recommendation, MDC, CAD-to-CAD). The dispatch supervisor, not IT, decides when to switch back, and announces it on the radio and to the county PSAP (RC.CO). Reconcile the paper incident cards into CAD so response-time reports and state data are complete.

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days), including the county PSAP and the Medical Director.
- Medical Director reviews every call handled in manual mode for delays that affected patients.
- Update the risk register (P01, especially R-001, R-002, R-009, R-021), the POA&M (P07), the BIA's MTD assumptions, and this runbook.
- Retain all incident documentation for 6 years (POL-01 4.10).
