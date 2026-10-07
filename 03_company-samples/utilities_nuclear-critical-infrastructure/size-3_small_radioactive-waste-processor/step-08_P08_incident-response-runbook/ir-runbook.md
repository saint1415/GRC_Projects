# Incident Response Runbook: Business Network Intrusion with Attempted Pivot to OT and Security Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (radioactive and hazardous waste processor) |
| Tier / Vertical | Small / Nuclear Reactors, Materials, and Waste |
| Incident type | Cyber attack on the site business network (phished credentials, then hands-on-keyboard activity) with an attempted pivot to the plant OT network and the physical security systems that protect the category 2 sealed source vault |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with NIST SP 800-82 Rev. 3 sections 3.3.8 and 6.4 for OT |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager, with the Radiation Safety Officer for all Part 37 steps |
| Approved | 2026-08-31 by the General Manager |
| Last tested | Not yet. First tabletop, with the controls integrator and alarm monitoring company, due 2026-11-30 (POAM-011) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (cyber) | IT Manager | General Manager | Incident line (cell), then the out-of-band group chat on personal phones |
| Part 37 decisions and regulator contact | Radiation Safety Officer | General Manager (second reviewing official) | Cell |
| Vault security (direct control) | Shift lead on duty (approved individual) | Any approved individual on the call list | Radio and cell |
| Plant safe state | Operations Manager | Maintenance and Controls Supervisor | Radio and cell |
| Technical response (IT) | MSP incident team | Forensic firm on retainer (through the insurer's panel) | MSP 24x7 line |
| Technical response (OT) | Controls integrator (on-call engineer) | Maintenance and Controls Supervisor | Integrator hotline |
| Alarm monitoring | Central station operator | Security system vendor | Central station line |
| Law enforcement | County sheriff (LLEA for the vault); FBI field office or IC3 | CISA | Numbers in the incident binder |
| Regulator | Florida Bureau of Radiation Control (address and telephone from license condition E.2) | n/a | Numbers in the incident binder |
| Legal and insurance | Outside counsel (insurer panel); carrier breach hotline | n/a | Policy card in the incident binder |
| Communications | General Manager | Customer Service Manager for customer notices | Cell |

**Out-of-band first.** Assume email, chat, and the file library are compromised. Coordinate on personal phones and radios, and use the printed incident binder kept in the RSO office and the shift lead office.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at both locations: this runbook, contacts, the notification matrix, the Florida contact sheet, and the vault direct-control roster
- [ ] Security VLAN in place, so PACS, NVR, and cameras survive a business network shutdown (SC-7). **Gap until POAM-002 closes**
- [ ] Historian no longer dual-homed (P03 G-080). **Gap until POAM-002 closes**
- [ ] Vendor remote access appliance off by default (P03 G-074). **Gap until POAM-019 closes**
- [ ] Immutable backups in a separate account, with a restore test in the last 90 days (CP-9, CP-4). **Gap until POAM-003 and POAM-004 close**
- [ ] Current PLC and HMI program backups stored offline (P03 G-077)
- [ ] Procedures SEC-05 and TR-06 corrected to name the Florida Bureau of Radiation Control (POAM-012)
- [ ] Two break-glass accounts sealed and tested (POL-02 4.9)
- [ ] Forensic retainer confirmed, and the integrator's on-call terms in its contract (POAM-011, POAM-016)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| EDR alert for credential theft, remote tools, or lateral movement on an office endpoint | MSP | MSP isolates the host and calls the IT Manager |
| Staff report entering credentials on a phishing page | Staff | Reset password, revoke sessions, review sign-ins; escalate if there is other activity |
| Sign-in to the Part 37 restricted library by someone not on the information access list | Library access alert (after POAM-010) | **Call the RSO immediately** (POL-03 4.3) |
| Unexpected connections from the business network to the historian, PACS server, NVR, or cameras | Firewall or EDR | Block at the firewall; open an incident |
| A camera or the NVR goes offline, unknown badges appear, or PACS settings change | Shift lead, alarm company, or PACS log | **Call the RSO and put the vault under direct control** |
| Vendor remote access session nobody approved | Appliance log | Disable the appliance; call the Maintenance and Controls Supervisor |
| HMI shows unexpected setpoint or mode changes | Operator | Put the line in local hand control; call the Operations Manager |

**Declare an incident** when an attacker is confirmed on any business system, or any trigger in the table involves the OT network, the security systems, or Part 37 information.
**Record the time of discovery.** It starts the clocks in `notification-matrix.csv`, including the Part 37 4-hour clocks.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Protect the vault first.** Post an approved individual at the vault for direct control (37.47(c)(2)). Stop all source receipts and shipments. Ask the central station to confirm both IDS paths are up | Shift lead with the RSO | Direct control log started; central station confirms |
| 2. **Cut the pivot paths.** Block all business-to-OT and business-to-security-system traffic at the firewall; unplug the historian's business network cable; disable the vendor remote access appliance. **Do not power off** PACS, NVR, IDS, PLCs, or radiation monitors | IT Manager with the Maintenance and Controls Supervisor | Paths blocked; devices still running |
| 3. **Put the Plant in a safe state.** Stop open waste handling. Keep exhaust ventilation running in local hand control. Confirm radiation monitors are reading. Check the vault inventory against the last printed export | Operations Manager and a health physics technician | Safe-state checklist signed; inventory confirmed |
| 4. Isolate affected office endpoints through EDR; revoke all sessions; reset administrator credentials with break-glass accounts if needed | IT Manager and the MSP | Sessions revoked |
| 5. Call the cyber insurer's breach hotline. Engage counsel and forensics through the insurer | General Manager | Claim number issued |
| 6. **Start the Part 37 assessment.** The RSO decides whether this is suspicious activity related to possible theft, sabotage, or diversion (37.57(b)). If yes, notify the LLEA as appropriate, and note the time: the Florida notice is due no later than 4 hours after that | Radiation Safety Officer | Decision and time recorded |
| 7. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

**Why step 1 comes first.** Part 37 treats deliberate damage to "the components of the security system" as sabotage (37.5). If an attacker is working toward the PACS or cameras, the company must be able to detect and respond at the vault whatever happens to the network. The IDS runs independently, and people provide the rest. Treating cyber tampering with security systems as possible sabotage or suspicious activity under 37.57 is the company's reading of the rule. The RSO will confirm it with the Florida Bureau of Radiation Control at the next inspection, and until then will notify rather than wait.

## 4. Analysis (RS.AN)
1. **Scope:** which accounts, endpoints, cloud workloads, and SaaS tenants are affected? Check EDR, identity provider sign-in logs, cloud audit logs, SYS-01 file access logs (especially the Radiation Safety and HR libraries), and firewall logs.
2. **Pivot attempt:** did the attacker reach the historian, PACS server, NVR, cameras, or the vendor appliance? Pull their logs **before** making changes. OT forensics must be passive (SP 800-82 Rev. 3 Appendix E.2.3 warns against active scanning of operational OT).
3. **Security-related information:** was the security plan, procedures, approved list, or DOT security plan opened, downloaded, or shared? If yes, the RSO treats it as suspicious activity under 37.57(b), assesses whether security measures must change, and informs the LLEA.
4. **Personal information:** were background investigation files, HR records, or payroll data accessed? This drives the Fla. Stat. 501.171 determination.
5. **Integrity of regulated records:** compare the source inventory application and open manifests with the physical count and paper copies. Any unexplained change is treated as possible sabotage or diversion and goes to the RSO.
6. **Preserve evidence:** forensics images affected hosts and exports logs before they roll over (default retention can be as short as 30 days; POAM-010). Keep chain of custody.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure (IPs, domains) at the firewall and in the cloud network rules.
2. Disable compromised accounts. Rotate service account, PACS, NVR, camera, and vendor appliance credentials, and replace any default passwords found.
3. Rebuild affected office endpoints from the standard image.
4. **OT:** if the attacker reached the historian or any HMI, rebuild it from known-good media and restore PLC programs only after comparing them with the offline backups. Keep processing in hand control until the controls integrator signs off.
5. **Security systems:** if the PACS server or NVR was reached, restore them from vendor media on the security VLAN (or an isolated switch until the VLAN exists). Re-enroll badges from the RSO's approved list, not from the old database. Keep direct control of the vault until the RSO confirms the systems are trustworthy.
6. Confirm with forensics that persistence is removed before reconnecting any network path.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** The RSO owns every Part 37 and Chapter 64E-5 notice. Counsel confirms breach notices.

| When | Action | Owner |
|---|---|---|
| Immediately | LLEA notice if actual or attempted theft, sabotage, or diversion is determined (37.57(a)) | RSO |
| As appropriate, and start the clock | LLEA notice for suspicious activity (37.57(b)) | RSO |
| **No later than 4 hours** after discovery (37.57(a)) or after notifying the LLEA (37.57(b)) | Florida Bureau of Radiation Control by telephone, using the license condition contact, **not** the NRC Operations Center | RSO |
| Within 4 hours of determining a category 2 shipment is lost or missing | Florida Bureau of Radiation Control (37.81(b)) | Compliance and Transportation Manager with the RSO |
| Day 0 | Insurer notified; counsel engaged | General Manager |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA. Supports OFAC mitigation if payment is considered | IT Manager |
| Within 24 hours of confirmation | Reactor customers, per contract, if their data or site work is affected | General Manager |
| Within 30 days | Written Part 37 report to the State, if an initial telephone notice under 37.57(a) or 37.81 was made | RSO |
| Within 30 days of determining a breach | Fla. Stat. 501.171 notice to affected individuals; Department of Legal Affairs if 500 or more Floridians. If counsel concludes no likely harm, document the determination in writing, keep it 5 years, and send it to the Department within 30 days (501.171(4)(c)) | General Manager and counsel |

**Plan to the shortest clock.** In this incident, the shortest clock is the 4-hour Part 37 notice to the State. It can start within the first hour, long before the cyber investigation is finished. The RSO should notify on suspicion and update later, rather than wait for certainty.

**Ransom decision:** requires the President, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove any Part 37 or breach notice duty.

**Not applicable here:** NRC 10 CFR 73.77 cyber notifications (the company is not a 73.54 licensee) and CIRCIA (not in effect).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Security systems: IDS paths confirmed; PACS server and NVR restored and trusted by the RSO. Direct control of the vault ends only then
2. Identity provider and administrator access (break-glass if needed)
3. Radiation monitoring workstation and data
4. Site internet and business network (clean endpoints first for the dock and dispatcher)
5. Waste tracking access on clean tablets; enter paper receiving logs
6. Source inventory application: restore, then reconcile with the physical count
7. Records archive and e-Manifest access
8. Fleet telematics
9. Plant OT network: restore the historian as a DMZ replica, not dual-homed; release lines from hand control with integrator sign-off
10. Accounting and billing
11. HR and payroll

**Validate before reconnecting:** EDR is clean, credentials are rotated, systems are patched, and the security VLAN and OT firewall rules are in place. Tell staff and customers when services are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Hold a lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days).
- Update the risk register (P01, especially R-001 to R-004 and R-006), the POA&M (P07), this runbook, and the Part 37 security plan if security measures changed (37.43(a)(3)).
- Feed the results into the annual Part 37 security program review (37.55) and re-coordinate with the LLEA if the incident changed the vault's vulnerability (37.45(d)).
- Retain incident documentation for at least 3 years, and Part 37 event records per the license (POL-01 4.11).
