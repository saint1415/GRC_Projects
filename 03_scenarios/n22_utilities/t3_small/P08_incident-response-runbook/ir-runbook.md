# Incident Response Runbook: Intrusion into Distribution Control Systems (OT)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (electric distribution utility, NERC-registered Distribution Provider) |
| Tier / Vertical | Small / Utilities |
| Incident type | Unauthorized access to the distribution SCADA or substation networks. Example: an attacker uses the shared vendor account on the OT jump host, sends open commands to feeder breakers, and probes the Substation E relay network |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT practices from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy. This runbook is part of the CIP-003-9 low impact Cyber Security Incident response plan (Attachment 1 Section 4) |
| Runbook owner | IT Manager, with the Manager of System Operations for operational steps |
| Approved | 2026-09-04 by the President and CEO and the CIP Senior Manager |
| Last tested | Low impact plan last tested 2023-06-14. Tabletop of this runbook scheduled 2026-10-20 (POAM-008) |

**Safety first.** The grid must stay safe for the public and for crews. The shift supervisor on duty decides every isolation step that affects operations. Crews working under clearances are protected before anything else.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Operational incident commander | Shift supervisor, then the Manager of System Operations | Vice President of Operations | DCC console phone; radio |
| Technical incident lead | IT Manager | SCADA/OT Administrator | Cell; out-of-band group on personal phones |
| OT systems | SCADA/OT Administrator | SCADA vendor emergency line (by phone, **not** through the jump host) | Cell |
| Protection and substations | Manager of Engineering and Protection | On-call protection technician | Cell; radio |
| CIP determination and reports | NERC Compliance Coordinator | IT Manager | Cell |
| CIP Senior Manager | Vice President of Operations | President and CEO | Cell |
| Legal, insurer, communications | President and CEO | Chief Financial Officer | Insurer hotline; outside counsel via insurer |
| Customer communications | Customer Service Manager | Communications lead | Cell |
| External | Transmission owner control center, Balancing Authority, Reliability Coordinator; DOE Operations Center; E-ISAC; CISA; FBI field office | | Numbers in the DCC incident binder |

**Out-of-band first.** Assume the corporate network, email, and chat may be compromised. Coordinate by DCC phone, radio, and personal phones, using the printed contact list in the DCC incident binder.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed DCC incident binder: this runbook, the notification matrix, contacts, and switching procedures for manual operation
- [ ] Vendor remote access off by default and enabled per session (POL-02 4.6). **Gap until POAM-002 closes**
- [ ] OT monitoring with alerts to the DCC and the IT Manager (SI-4). **Gap until POAM-004 closes**
- [ ] Offline, immutable SCADA backups with a restore test in the last 90 days (CP-9, CP-4). **Gap until POAM-005 and POAM-006 close**
- [ ] Approved relay settings files for Substation N and E stored offline (BP-03 recovery point)
- [ ] Sealed break-glass OT administrator credentials in the DCC safe (P01 R-029)
- [ ] DOE-417 filing agreed with the Balancing Authority; E-ISAC contacts current (POAM-017)
- [ ] OT-capable incident response firm confirmed through the insurer panel

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A breaker, recloser, or capacitor operates and no operator or automatic scheme did it | SCADA event log; operator | Shift supervisor treats it as a possible intrusion. Confirm no crew or automatic scheme caused it. Call the IT Manager |
| Unknown or off-hours login on an HMI, the jump host, or the OT domain | Jump host log; operator; OT monitoring (planned) | Disable the account and call the IT Manager |
| Vendor session the DCC did not enable | Jump host session list | Disable vendor access at once (POL-02 4.6) |
| Relay or gateway alarm, settings change, or unexpected reboot at Substation N or E | SCADA alarm; protection staff | Notify the Manager of Engineering and Protection; start the relay integrity check (section 5) |
| Scans or new connections on the OT network | OT monitoring (planned); firewall logs | IT Manager triages |
| Tip from the SCADA vendor, E-ISAC, CISA, or the FBI | External | Declare and investigate |

**Declare an OT intrusion when** any control action, login, or connection in the OT network cannot be explained by staff, a vendor session that the DCC enabled, or an automatic scheme.

**Record the times:**
- when the incident occurred or was first seen (DOE-417 clocks run from the incident)
- when a Cyber Security Incident was identified
- when it was determined to be Reportable (the E-ISAC step follows this determination)

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Make the grid safe: confirm the status of every crew clearance; put affected feeders and devices in local or manual control where possible; send crews to key substations | Shift supervisor | All crews confirmed safe; manual control in place |
| 2. Cut the attacker's path: disable vendor access and the shared vendor account on the jump host; block the VPN pool at the IT/OT firewall | IT Manager with SCADA/OT Administrator | Sessions ended; rules applied |
| 3. Isolate, do not power off: disconnect the OT DMZ from the corporate network and the cloud VPN. Keep SCADA running if it is still trusted for monitoring. Otherwise switch to manual operation | IT Manager; shift supervisor decides | OT isolated; operating mode recorded |
| 4. Notify the transmission owner and the Reliability Coordinator if Substation N or E, or the 115 kV lines, could be affected | Shift supervisor | Call logged |
| 5. **DOE-417 Emergency Alert within 1 hour** if unauthorized commands interrupted electrical system operations (criterion 3) or a Reportable Cyber Security Incident is confirmed (criterion 2) | Manager of System Operations | Form submitted or phoned to the DOE Operations Center |
| 6. Call the insurer hotline; engage counsel and an OT-capable response firm | President and CEO | Claim number issued |
| 7. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** which HMIs, servers, gateways, and accounts were used? Check the SCADA event log, jump host logs, OT domain logs, and IT/OT firewall logs. Check whether the path came through the corporate network or the cloud VPN (P04 finding 1).
2. **Initial access:** identify the account and source. Check the shared vendor account first, then VPN accounts.
3. **Low impact systems:** decide whether any relay at Substation N or E (the low impact BES Cyber Systems) was compromised or disrupted. That decides whether this is a **Reportable Cyber Security Incident** (NERC Glossary). A compromised gateway is treated as a likely path to the relays and triggers the relay integrity check. An attempt that did not compromise or disrupt a relay may still be a Cyber Security Incident, but it is not Reportable. Attempt-to-compromise reporting (CIP-008-6 R4, DOE-417 criterion 14) covers only high and medium impact systems. Record the decision and who approved it (CIP Senior Manager).
4. **Preserve evidence:**
   - Export jump host, SCADA, and firewall logs before they roll over (jump host logs keep only 30 days).
   - Image the jump host and any affected HMI.
   - Keep chain of custody.
5. **Customer data:** confirm whether the OMS, the CIS, or the AMI head-end was touched. That drives the Florida breach analysis.
6. **Backups:** confirm the SCADA backups and the standby server are intact before any restore.

## 5. Containment and eradication (RS.MI)
1. Keep vendor access disabled until the vendor confirms its own environment is clean. Re-enable only through named accounts with MFA.
2. Reset all OT domain, HMI, jump host, and gateway passwords from a clean workstation. Rotate relay passwords at Substation N and E.
3. **Relay integrity check:** protection staff compare the relay settings at Substation N and E with the approved offline files, reload them if they differ, and test. The transmission owner decides whether the 115 kV lines stay in service meanwhile (BP-03, RTO 8 h).
4. Rebuild the jump host and any affected HMI from vendor media. **Do not reuse compromised systems.**
5. Remove the legacy any rules the attacker used (POAM-003) before reconnecting the OT DMZ.
6. Confirm with the response firm that persistence is removed.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** The NERC Compliance Coordinator tracks every clock. Counsel reviews customer and regulator notices.

| When | Action | Owner |
|---|---|---|
| Immediately | Transmission owner, BA, and RC by phone if BES facilities or BES-connected load are affected | Shift supervisor |
| Within 1 hour of the incident | DOE-417 Emergency Alert if criterion 2 or 3 is met | Manager of System Operations |
| Within 1 hour of a Reportable determination (company target) | E-ISAC notice (CIP-003-9 Attachment 1 Section 4.2). DOE-417 can also share its form with the E-ISAC. Its instructions say that sharing satisfies CIP-008, not CIP-003, so notify the E-ISAC directly as well | NERC Compliance Coordinator |
| Within 6 hours of the incident | DOE-417 Normal Report if only criterion 11 applies, or if more than 50,000 customers lose service for 1 hour or more (criterion 12) | Manager of System Operations |
| Later of 24 hours or end of next business day | EOP-004-4 report to NERC if a Facility was damaged by intentional action or 200 MW or more of firm load was lost for 15 minutes or more | NERC Compliance Coordinator |
| Same day | Voluntary report to CISA and the FBI | IT Manager |
| Within 72 hours of the incident | DOE-417 final report (unless an interim update has been provided) | NERC Compliance Coordinator |
| As needed | Customer outage updates through the IVR, outage map, and media; no attack details without counsel | Customer Service Manager |
| Within 30 days of determination | Florida breach notices, only if CIS or other personal information was accessed | Customer Service Manager and counsel |

**Extortion or ransom demand:** requires the majority owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7).

**Proposed rule watch:** if the CIRCIA final rule takes effect as proposed, this company would have to report covered incidents to CISA within 72 hours. It is not in effect as of 2026-09-25.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Manual operation by crews and radio dispatch (already running from step 1)
2. SCADA on a trusted server: the standby if clean, otherwise a rebuild from offline backups (target 2 h; unproven until POAM-006)
3. Substation communications, one substation at a time, after gateway access lists are verified
4. OMS feeds from SCADA and the AMI through the OT DMZ integration server only
5. Relay integrity confirmed at Substation N and E; the transmission owner returns lines to normal
6. CIS, IVR, and portal (vendor-hosted; confirm they were not affected)
7. Email and chat, load forecast, AMI operations, and back-office systems

**Validate before reconnecting:** credentials are rotated, systems are rebuilt or verified, monitoring is in place, and vendor access stays off. Tell customers when service is restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days).
- Update this runbook and the low impact plan within 90 days (company rule; CIP-003-9 allows 180 calendar days after an actual Reportable Cyber Security Incident).
- Update the risk register (P01, especially R-001, R-002, R-003, R-020) and the POA&M (P07).
- Consider whether the event shows a noncompliance to self-report to SERC (POL-01 4.10).
- Retain all incident records as CIP evidence for at least three calendar years (POL-01 4.11).
