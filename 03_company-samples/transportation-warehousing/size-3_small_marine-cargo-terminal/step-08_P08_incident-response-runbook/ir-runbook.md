# Incident Response Runbook: Ransomware Disrupting the Terminal Operating System

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (marine cargo terminal operator, NAICS 488320) |
| Tier / Vertical | Small / Transportation and Warehousing |
| Incident type | Ransomware that encrypts the TOS application servers and TOS gate servers and stops vessel, yard and gate operations. Assumed entry: a stolen password for a staff VPN account (no MFA). The crane and RTG controllers (OT) are at risk because they share a flat network with the gate servers |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy. This runbook is the first part of the Cyber Incident Response Plan required by 33 CFR 101.650(g)(2) |
| Runbook owner | IT Manager (proposed Cybersecurity Officer) |
| Approved | 2026-09-04 by the General Manager |
| Last tested | Not yet. First tabletop exercise, with key personnel, due 2026-11-30 (POAM-015) |
| Handling | SSI once contacts and network details are added (POL-04 4.2) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander and Coast Guard reporting | IT Manager (proposed CySO) | Security and Safety Manager (FSO, proposed alternate CySO) | CySO line (cell), then the out-of-band group on personal phones |
| Terminal operations (manual working) | Operations Manager | Shift superintendent on duty | Radio channel 1 and cell |
| OT safety and crane vendor | Maintenance Manager | Senior crane electrician | Cell; crane vendor 24x7 service line |
| Security, TWIC access and MTSA reporting | Security and Safety Manager (FSO) | Security supervisor on duty | Security office radio and cell |
| Technical response | MSP incident team | Forensic firm on retainer (engaged through the insurer's panel) | MSP 24x7 line |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Through the insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Decisions and communications | General Manager | Finance and Administration Manager | Cell |
| Ransom decision | Majority owner, with counsel and the insurer | n/a | Cell |
| Port partners | Operations Manager | Customer service lead | Printed partner contact sheet |

**Out-of-band first.** Assume email, chat and the identity provider may be compromised. Coordinate on personal phones, radios and the printed contact list in the incident binders (security office, gate complex and operations office).

## 1. Preparation checks (Identify / Protect)
- [ ] Incident binders at the security office, gate complex and operations office: this runbook, the notification matrix, partner contacts, the Coast Guard Sector, FBI field office and CISA contact details, and manual gate and vessel forms
- [ ] MFA on the staff VPN and all TOS users (IA-2(2)). **Gap until POAM-001 closes (2026-11-30)**
- [ ] Isolated, immutable TOS backups, gate server images and PLC programs held by the company, with a restore test in the last 90 days (CP-9, CP-4). **Gap until POAM-004 and POAM-005 close**
- [ ] EDR with 24x7 alerting on servers and endpoints (SI-4). **Gap until POAM-008 closes**
- [ ] Central logs kept for 1 year, which local administrators cannot delete (AU-9, AU-11). **Gap until POAM-023 closes.** Until then, local logs roll over in 7 to 30 days, so export them in the first hour
- [ ] Crane vendor appliance off except for approved sessions (AC-17). **Gap until POAM-002 closes**
- [ ] Two break-glass administrator accounts sealed in the FSO safe (POL-02 4.8)
- [ ] A printed dangerous cargo location list at the security office at every shift change (P01 R-030)
- [ ] Forensic retainer and insurer panel confirmed (POAM-015)
- [ ] Staff and longshore supervisors know to report to the CySO line (POL-03 4.2; POAM-016)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note on a gate server, workstation or TOS server; files renamed with an unknown extension | Gate clerk, planner, MSP | Call the CySO line. **Do not power off.** Pull the network cable or turn off Wi-Fi |
| TOS unavailable, or the TOS database stops accepting transactions | Planners, gate clerks, TOS vendor | IT Manager checks the cloud console and the TOS vendor status; open an incident if encryption or unknown admin activity is seen |
| VPN sign-in at an unusual time or from an unusual location; several accounts locked out at once | Identity provider or VPN logs, MSP | Disable the account, revoke sessions, review activity; escalate if servers were accessed |
| OCR portals or kiosks fail on all lanes at once | Gate supervisor | Treat as possible ransomware until the IT Manager rules it out |
| HMI shows changed settings, a crane or RTG behaves unexpectedly, or PLC faults appear together | Crane operator, mechanic | **Stop the equipment in a safe state** (POL-03 4.7); call the Maintenance Manager and the CySO line |
| A partner reports odd EDI messages, or the customs data exchange reports failed connections | Carrier, customs data exchange, port community system | Suspend outbound EDI; verify with the partner by phone |
| An extortion email, or a leak site post naming the company | Email, insurer, law enforcement | Declare the incident; preserve the message |

**Declare a ransomware incident when** encryption or a ransom note is confirmed on any system, or an extortion claim names company data. The incident commander declares it and records the **time of declaration**.

**Clocks start at evidence, not certainty.** 33 CFR 6.16-1 requires evidence of an actual or threatened cyber incident to be reported **immediately**. Do not wait for forensics. Florida's 30-day clock for personal information starts when the breach is determined (Fla. Stat. 501.171).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Safety first.** Stop crane and RTG moves if OT integrity is in doubt; hold any vessel work that depends on TOS data for hazardous cargo | Operations Manager with the Maintenance Manager | Equipment in a safe state; superintendents informed by radio |
| 2. Isolate: disable the staff VPN; drop the site-to-site VPN to the cloud tenant; disconnect the gate and yard switch from the office LAN; power off the crane vendor appliance. Leave affected servers powered on for memory evidence | IT Manager with the MSP | Links down; OT has no path to IT |
| 3. **Report under 33 CFR 6.16-1:** call the Captain of the Port (Sector command center), the FBI field office and CISA. Give what is known now and update later | IT Manager (CySO); FSO if the CySO cannot be reached | Report reference numbers recorded in the log |
| 4. Call the cyber insurer's breach hotline; engage counsel and forensics through the insurer | General Manager | Claim number issued |
| 5. Disable the compromised VPN account; revoke all identity provider sessions; reset administrator passwords from a clean device (break-glass accounts if needed) | IT Manager | Sessions revoked |
| 6. Start manual working: manual gate on one lane with the printed release list; radio dispatch; paper tally; printed dangerous cargo list to the security office and the port fire department contact | Operations Manager; FSO | Manual procedures running (P05) |
| 7. Tell port partners that EDI and the gate are suspended and that messages received after the declaration time are not trusted until verified | Operations Manager | Partners called from the printed list |
| 8. Start the incident log: timeline, actions, who, when, and every report made (101.640) | FSO | Log open |

## 4. Analysis (RS.AN)
1. **Scope.** Which TOS servers, gate servers, OCR servers, workstations, cloud workloads and accounts are affected? Check the cloud audit logs, identity provider and VPN logs, antivirus console and firewall logs.
2. **Initial access.** Confirm the VPN account used, when it was first used, and the first server reached. Check for other VPN accounts used from the same source.
3. **Preserve evidence.** Export VPN, firewall, gate server and TOS logs before they roll over (7 to 30 days today). Forensics images affected servers and takes memory captures. Keep chain of custody. Keep cloud snapshots of affected disks.
4. **OT check.** With the crane vendor, compare PLC programs and HMI settings on each STS crane and RTG with the vendor's known-good copies. Look for new connections to controllers from the gate and yard network. **No crane returns to TOS-directed work until this check is signed off.**
5. **Data taken?** Check for archive tools, large outbound transfers and cloud storage access. The data that drives notices:
   - truck driver names and driver license numbers in the TOS gate module (Fla. Stat. 501.171)
   - employee records on the file share
   - SSI, such as FSP extracts or network diagrams (report to the COTP; POL-04)
   - cargo and customs data (commercial harm; tell affected carriers)
6. **Backups.** Before restoring anything, confirm that the snapshots and the weekly export are intact, and identify the last clean restore point.
7. **Security impact.** The FSO decides whether any FSP security measure was circumvented (a breach of security) and whether the disruption could become a TSI (33 CFR 101.305).

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at the firewall and in the cloud network rules.
2. Disable compromised accounts. Rotate all administrator, service and integration credentials, including:
   - EDI partner credentials
   - API keys for the port community system, the customs data exchange and the scheduling service
   - the TOS vendor support account
3. **Enforce MFA on the VPN before it is turned back on.** Keep the VPN off until then.
4. Rebuild gate servers, OCR servers and affected workstations from clean media and patch them. **Do not decrypt and reuse them.**
5. Rebuild TOS application servers from clean images. Restore the database to the last clean point in a clean environment.
6. Keep OT disconnected from IT until the OT check (4.4) is signed off and a temporary firewall rule allows only the TOS equipment interface.
7. Forensics confirms that persistence has been removed before recovery starts.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms personal information notices. Coast Guard reporting does not wait for counsel.

| When | Action | Owner |
|---|---|---|
| Immediately (first hour) | Report to the COTP, FBI and CISA under 33 CFR 6.16-1. This also satisfies the Subpart F NRC reporting duty (101.620(b)(7)) | CySO (FSO as backup) |
| Without delay, if applicable | NRC report of a breach of security or suspicious activity, and a TSI report to the COTP, per the FSP (101.305) | FSO |
| Day 0 | Insurer notified; counsel engaged; staff briefing script: what happened, manual procedures, no discussion outside the company | General Manager |
| Day 0, then twice daily | Port partner updates: port authority, carriers with vessels due, port community system, customs data exchange, trucking companies (portal banner or email from a clean account) | Operations Manager |
| As facts develop | Update the Coast Guard and FBI; answer COTP questions about terminal status and hazardous cargo | CySO; FSO |
| As soon as known | Decide whether personal information was accessed; document the decision | Finance and Administration Manager with counsel |
| Within 30 days of determination | Florida individual notices; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000; other states as applicable | Finance and Administration Manager with counsel |
| Throughout, kept 2 years | Incident record (101.640; 105.225(b)(3)) | FSO |

**Ransom decision:** requires the majority owner, counsel, the insurer and an OFAC sanctions check (POL-03 4.6). Paying does not remove any reporting or notice duty. **CIRCIA is not in effect** (final rule not published as of 2026-09-25), so there is no 72-hour or 24-hour CIRCIA report today. Recheck when the final rule is published.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 6):
1. Identity provider and administrator access (break-glass if needed)
2. Firewall, internet and core network, with OT isolated
3. PACS and TWIC readers, and the dangerous cargo list (security officers check TWICs manually until then)
4. TOS database and application servers, from the last clean restore point
5. Clean operations endpoints and gate booth workstations
6. Crane and RTG controllers, signed off by the Maintenance Manager and crane vendor before reconnecting to the TOS
7. Gate automation: gate servers, OCR and kiosks
8. EDI gateway and customs data exchange feed
9. The TOS vendor's hosted truck appointment and customer portal
10. Finance, payroll and billing
11. Scheduling optimization service: last, and only after a security review (P10)

**Validate before resuming normal operations:**
- **Reconcile the TOS with reality.** Compare the restored container inventory with a physical yard check, paper gate interchanges and carrier bay plans. Moves made during manual working must be keyed in before automated dispatch restarts.
- **Customs holds first.** Refresh release and hold status from the customs data exchange before any import container leaves by the automated gate.
- **Hazardous cargo.** The FSO confirms that the TOS dangerous cargo locations match the printed list and a yard check.
- **Clean systems only.** EDR or antivirus is clean, credentials are rotated, systems are patched, and the VPN has MFA.

Tell staff, the COTP and port partners when each service is back (RC.CO). Keep manual procedures running until each process is within its RTO (P05).

## 8. Post-incident (ID.IM)
- Hold a lessons-learned meeting within 14 days of recovery. POL-03 4.10 requires documentation within 30 days.
- Update the risk register (P01, especially R-001, R-002, R-004 and R-005), the POA&M (P07), this runbook and the Cybersecurity Plan (101.650(g)(3)).
- Keep all incident records for at least 2 years (POL-01 4.10; 101.640).
- Add the incident to the next annual cyber training and the next exercise (101.635).
