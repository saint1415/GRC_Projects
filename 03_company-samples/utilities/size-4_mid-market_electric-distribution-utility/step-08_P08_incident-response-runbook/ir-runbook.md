# Incident Response Runbook A: Intrusion into Distribution Control Systems (OT)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (investor-owned electric distribution utility, NERC-registered Distribution Provider) |
| Tier / Vertical | Mid-Market / Utilities |
| Incident type | Unauthorized access to the distribution SCADA, OT DMZ, substation, or field networks. Scenario: an attacker who has compromised the SCADA and ADMS vendor's support environment uses a vendor jump host session and the shared SCADA administrator accounts to send open commands to feeder breakers, then probes the relay network at Substation H |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions; OT practices from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy. This runbook is part of the CIP-003-9 low impact Cyber Security Incident response plan (Attachment 1 Section 4) |
| Companion documents | `ir-runbook-ransomware-customer-data.md` (runbook B); `notification-matrix.csv`; BIA (P05); storm restoration plan; crisis management plan |
| Runbook owner | Information Security Manager (technical lead), with the Director of System Operations for operational steps |
| Approved | 2026-09-17 by the Chief Operating Officer (CIP Senior Manager) |
| Last tested | Low impact plan tested by tabletop 2024-10-08. Combined storm and SCADA intrusion tabletop scheduled 2027-02-17 (POAM-016) |

**Safety first.** The grid must stay safe for the public and for crews. The shift supervisor on duty decides every isolation step that affects operations. Crews working under clearances are protected before anything else, and a known safe manual state comes before forensic completeness.

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers so that grid, technical, and business and legal decisions each have one owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer (CIP Senior Manager). President and CEO, Chief Financial Officer, General Counsel, vCISO, Vice President of Operations and Field Services, Vice President of Customer Operations, Director of Corporate Communications, Director of Utility Services | Business continuity, external statements, regulator and client contact, Reportable determination approval, CIP Exceptional Circumstances, ransom decision (recommendation to the CEO) |
| **Grid operations command** | Shift supervisor, then the Director of System Operations; Director of Engineering and Protection; storm restoration plan section chiefs | Manual operations, crew dispatch, switching and clearances, coordination with transmission owners, BA, and RC |
| **Incident response team (IRT)** | Technical lead: Information Security Manager. OT Engineering Manager and the OT engineering team, OT-focused security analyst, MSSP, the insurer panel OT-capable forensic firm (through counsel), SCADA and ADMS vendor emergency contact | Containment, investigation, eradication, clean rebuild, recovery sequence |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Operational incident commander | Shift supervisor on duty, then the Director of System Operations | Vice President of Operations and Field Services | DCC console phone; radio |
| Technical lead | Information Security Manager | OT Engineering Manager | Out-of-band group on personal phones; printed call tree |
| OT systems | OT Engineering Manager | SCADA and ADMS vendor emergency line (by phone, **not** through the jump hosts) | Cell |
| Protection and substations | Director of Engineering and Protection | On-call protection technician | Cell; radio |
| CIP determination and reports | NERC Compliance Manager | GRC analyst | Cell |
| CIP Senior Manager and CMT chair | Chief Operating Officer | President and CEO | Out-of-band group |
| Legal and privilege | General Counsel | Outside breach counsel (insurer panel) | Insurer hotline, then direct |
| Cyber insurer | Carrier hotline ($25 million limit, $500,000 retention) | Broker | Policy card in the DCC binder |
| Monitoring | MSSP 24x7 security operations center | n/a | MSSP hotline |
| Communications | Director of Corporate Communications | Outside crisis PR (through counsel) | Out-of-band group |
| Board | President and CEO informs the audit committee chair | General Counsel | Phone |
| External | Transmission Owners A and B control centers; BA and RC; DOE Operations Center; E-ISAC; CISA; FBI field office | | Numbers in the DCC incident binder |

**Out-of-band first.** Assume the corporate network, email, and chat may be compromised. Coordinate by DCC phone, radio, satellite phones at both DCCs, and the pre-provisioned messaging group on personal phones.

**Legal privilege protocol.** General Counsel engages the forensic firm through the insurer panel and directs the investigation. Facts (timeline, logs) are kept separate from legal conclusions. Nobody speculates in email or chat.

## 1. Preparation checks (Identify / Protect)
- [x] Printed DCC incident binder at both DCCs: this runbook, the notification matrix, contacts, one-line diagrams, and switching procedures for manual operation
- [x] Vendor remote access off by default, enabled per session by the DCC, with MFA and IDS monitoring (CIP-003-9 Att. 1 Sec. 6; P07 jump host sample 25 of 25)
- [ ] Shared SCADA administrator accounts replaced by named, vaulted accounts (POL-02 4.1). **Gap until POAM-001 closes (2026-12-31)**
- [ ] Legacy IT/OT rules removed (POL-02 4.9). **Gap until POAM-003 closes (2026-11-30)**
- [ ] OT monitoring at substations (SI-4). **Gap until POAM-004 and POAM-009 close**
- [ ] SCADA restorable within 2 hours, with a spare server and gold images at the backup DCC (CP-4). **Gap until POAM-007 closes**
- [ ] Offline, hash-verified approved relay settings for Substations N, E, L, and H (BP-03 recovery point). **Due 2026-12-31 (POAM-007)**
- [x] Sealed break-glass OT administrator credentials in the DCC and backup DCC safes
- [ ] DOE-417 filing agreed in writing with the Balancing Authority (POAM-016). E-ISAC contact current (verified 2026-09-17)
- [x] OT-capable incident response firm confirmed through the insurer panel
- [ ] DCC role cards issued to all 6 shift supervisors (POAM-016, due 2026-10-31)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A breaker, recloser, or capacitor operates and no operator, crew, FLISR, or protection scheme did it | SCADA event log; operator | Shift supervisor treats it as a possible intrusion; confirms no crew or scheme caused it; calls the technical lead |
| Unknown or off-hours login on an HMI, jump host, SCADA server, or the OT domain | Jump host logs; OT sensors; operator | Disable the account; call the technical lead |
| Vendor session the DCC did not enable, or a session past its end time | Jump host session list; DCC access log | Disable all vendor access at once (POL-02 4.6) |
| IDS alert on vendor traffic, or new connections or scans in the OT network | OT DMZ firewall IDS; OT sensors; MSSP | MSSP calls the technical lead within 30 minutes |
| Relay or gateway alarm, settings change, or unexpected reboot at Substation N, E, L, or H | SCADA alarm; protection staff | Notify the Director of Engineering and Protection; start the relay integrity check (section 5) |
| Unknown device or modem found at a substation | Crew or protection staff; survey (POAM-004) | Photograph; do not unplug until protection staff confirm it is safe; call the technical lead |
| Tip from the SCADA and ADMS vendor, E-ISAC, CISA, or the FBI | External | Declare and investigate |

**Declare an OT intrusion when** any control action, login, or connection in the OT network cannot be explained by staff, a DCC-enabled vendor session, or an automatic scheme. Severity: **High** if any unauthorized control action occurred or any BES substation is involved; otherwise Medium.

**Record the times** in the incident log:
- when the incident occurred or was first seen (DOE-417 clocks run from the incident);
- when a Cyber Security Incident was identified;
- when it was determined to be Reportable (the E-ISAC step follows this determination);
- when any customer or client data access was suspected and determined (runbook B clocks).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Make the grid safe: confirm the status of every crew clearance from the printed clearance log; put affected feeders in local or manual control; switch off FLISR on the 40 pilot feeders; send crews to the 20 largest substations (storm plan staffing list) | Shift supervisor | All crews confirmed safe; manual operations state declared (POL-03 4.5) |
| 2. Cut the attacker's path: disable all vendor access on both jump hosts; disable the 3 shared SCADA administrator accounts (break-glass accounts take over); block the corporate administration subnet and the site-to-cloud VPN at the IT/OT firewall | Technical lead with the OT Engineering Manager | Sessions ended; rules applied; times logged |
| 3. Isolate, do not power off: disconnect the OT DMZ from the corporate network and the cloud. Keep SCADA running for monitoring if it is still trusted; otherwise operate by crews and radio | Technical lead; shift supervisor decides | OT isolated; operating mode recorded |
| 4. Call Transmission Owners A and B and the Reliability Coordinator if Substations N, E, L, or H, the BES lines, or UFLS availability could be affected | Shift supervisor | Call logged |
| 5. **DOE-417 Emergency Alert within 1 hour of the incident** if unauthorized commands interrupted electrical system operations (criterion 3) or a Reportable Cyber Security Incident is confirmed (criterion 2) | Director of System Operations | Form submitted or phoned to the DOE Operations Center |
| 6. Convene the CMT; call the insurer hotline; General Counsel engages breach counsel and the OT-capable forensic firm | Chief Operating Officer; General Counsel | Claim number; engagement letters |
| 7. Activate the storm restoration plan structure if more than 10 feeders are affected or crews are needed at more than 5 substations | Director of System Operations | Section chiefs assigned |
| 8. Start the incident log: timeline, actions, who, and when | Technical lead | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** which HMIs, servers, gateways, routers, and accounts were used. Sources: SCADA event log, jump host session recordings, OT domain logs, OT sensor data, IT/OT firewall and IDS logs, MSSP SIEM. Check paths through the corporate network (legacy rules, gap 4), the cloud VPN, private LTE routers (default passwords, R-052), and any unmanaged device at substations.
2. **Initial access:** identify the account and source. Check the vendor's jump host account and the shared SCADA administrator accounts first. Ask the vendor (by phone) whether its environment is compromised.
3. **Low impact systems:** decide whether any relay or gateway at Substations N, E, L, or H was compromised or disrupted. That decides whether this is a **Reportable Cyber Security Incident** (NERC Glossary). A compromised gateway is treated as a likely path to the relays and triggers the relay integrity check. An attempt that did not compromise or disrupt a relay may still be a Cyber Security Incident, but it is not Reportable. Attempt-to-compromise reporting (CIP-008-6 R4) covers only high and medium impact systems. The NERC Compliance Manager and the technical lead recommend; the CIP Senior Manager approves and the decision is logged.
4. **Preserve evidence:** export jump host, SCADA, gateway, and firewall logs before they roll over; image the jump hosts and any affected HMI or engineering workstation; keep chain of custody under counsel's direction.
5. **Customer and client data:** confirm whether the OMS (names, addresses, premise locations), the CIS, the AMI head-end, or the CIS export was touched. If yes, open runbook B section 4 for the breach analysis.
6. **Backups:** confirm the weekly offline SCADA backups and the hot standby are intact and that no malicious change replicated to the standby before any restore.

## 5. Containment and eradication (RS.MI)
1. Keep vendor access disabled until the vendor confirms in writing that its environment is clean. Re-enable only through named accounts with MFA.
2. Reset all OT domain, HMI, jump host, gateway, router, and relay passwords from a clean workstation. Vault the new credentials.
3. **Relay integrity check:** protection staff compare relay settings at Substations N, E, L, and H with the approved offline files, reload them if they differ, and test. The transmission owner decides whether the 230 kV or 115 kV lines stay in service meanwhile (P05 BP-03, about 8 hours per substation).
4. Rebuild the jump hosts and any affected HMI, engineering workstation, or SCADA server from vendor media and gold images. **Do not reuse compromised systems.**
5. Remove any IT/OT rule or remote path the attacker used before reconnecting the OT DMZ.
6. Survey affected substations for unmanaged remote devices; remove any found.
7. Confirm with the forensic firm that persistence is removed, and with the MSSP that detections for the attacker's indicators are in place.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** The NERC Compliance Manager tracks every clock on a whiteboard in the DCC. General Counsel reviews every external notice.

| When | Action | Owner |
|---|---|---|
| Immediately | Transmission owners, BA, and RC by phone if BES facilities, BES-connected load, or UFLS could be affected | Shift supervisor |
| Within 1 hour of the incident | DOE-417 Emergency Alert if criterion 2 or 3 is met | Director of System Operations |
| Within 1 hour of a Reportable determination (company target) | E-ISAC notice (CIP-003-9 Attachment 1 Section 4.2). Sharing the DOE-417 form with the E-ISAC is not relied on for CIP-003; notify the E-ISAC directly | NERC Compliance Manager |
| Within 6 hours of the incident | DOE-417 Normal Report if only criterion 11 applies, or if more than 50,000 customers lose service for 1 hour or more (criterion 12) | Director of System Operations |
| Later of 24 hours or end of next business day | EOP-004-4 report if a Facility was damaged by intentional action, there was a physical threat or suspicious device at a Facility, or a BES Emergency caused an uncontrolled loss of 200 MW or more of firm load for 15 minutes or more | NERC Compliance Manager |
| Within 48 hours of awareness | Client utilities, if client AMI meters, outage calls, or client data were affected (contract) | Director of Utility Services |
| Same day | Voluntary report to CISA and the FBI | Information Security Manager |
| Within 72 hours of the incident | DOE-417 final report (unless an interim update has been provided) | NERC Compliance Manager |
| Before the next board meeting, or within 24 hours for High severity | Audit committee chair briefed | President and CEO |
| As needed | Customer outage updates through the IVR, outage map, and media; no attack details without counsel; staff briefing | Director of Corporate Communications |
| Within 30 days of determination | Breach notices, only if personal information was accessed (runbook B) | Vice President of Customer Operations and General Counsel |

**Extortion or ransom demand:** requires the President and CEO, General Counsel, and the insurer, an OFAC sanctions check, and a board briefing before payment (POL-03 4.9).

**Self-report check.** After containment, the NERC Compliance Manager decides with General Counsel whether the event revealed a potential noncompliance (for example, an unmanaged remote path) to self-report to SERC.

**Proposed rule watch:** if the CIRCIA final rule takes effect as proposed, covered incidents would be reported to CISA within 72 hours. It is not in effect as of 2026-09-25.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 8):
1. Manual operation by crews and radio dispatch (running from step 1)
2. Identity provider and OT break-glass accounts verified
3. SCADA on a trusted server: the hot standby if verified clean, otherwise a rebuild from the weekly offline backup (target 2 hours; 6 hours demonstrated until POAM-007 closes)
4. Substation and field communications, one substation at a time, after gateway access lists and router credentials are verified
5. OMS switching and clearance module, then outage prediction and dispatch; OMS feeds from SCADA only through the OT DMZ integration server
6. OT DMZ (integration server, historian replica); vendor access stays disabled
7. Relay integrity confirmed at Substations N, E, L, and H; the transmission owners return lines to normal
8. ADMS FLISR pilot re-enabled only after the ADMS Program Manager and OT Engineering Manager sign off
9. CIS, IVR, portal, AMI, load forecast, and back-office systems (confirm they were not affected)

**Validate before reconnecting:** credentials rotated, systems rebuilt or verified, monitoring for the attacker's indicators in place, vendor access off, and the CMT chair's approval to leave the manual operations state. Tell customers when service is restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- Update this runbook and the low impact plan within 90 days (company rule; CIP-003-9 allows 180 calendar days after an actual Reportable Cyber Security Incident).
- Update the risk register (P01: R-001, R-004, R-005, R-007, R-011) and the POA&M (P07).
- Keep all incident records as CIP evidence for at least 3 years (POL-01 4.15).
- Review the SCADA and ADMS vendor relationship and contract terms (R-015).
