# Incident Response Runbook: Ransomware Disrupting Production of Grid Equipment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (power and distribution transformer manufacturer, Florida) |
| Tier / Vertical | Small / Critical Manufacturing |
| Incident type | Ransomware that encrypts the ERP, the file and PLM servers, the dual-homed MES server, and plant HMIs, stopping transformer production during hurricane season |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 section 6.4 |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager, with the Controls Engineer for the OT sections |
| Approved | 2026-09-04 by the VP Operations |
| Last tested | Not yet. First tabletop with the Plant Manager and MSP due 2026-11-30 (POAM-008) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | VP Operations | Incident line (cell), then the out-of-band group chat on personal phones |
| OT incident lead | Controls Engineer | Maintenance Manager with a controls technician | Cell; plant radio channel 2 |
| Plant safety and operations decisions | Plant Manager | Shift supervisor on duty | Cell; plant radio |
| Technical response (IT) | MSP incident team | Forensic firm from the insurer's panel | MSP 24x7 line |
| Technical response (OT) | OT-capable incident response firm on retainer (contract due 2026-10-31, POAM-008) | Plant equipment OEMs (drying oven, winders, core line) | Retainer hotline; OEM support numbers in the binder |
| Insurer, breach coach, counsel | Controller calls the carrier breach hotline | President | Policy card in the incident binder |
| Customer and government notices | Contracts and Compliance Manager | VP Operations | Cell |
| Utility access notices and storm crews | Field Service Manager | Contracts and Compliance Manager | Cell |
| Product integrity (test data, TMU firmware) | Quality Manager; VP Engineering | Engineering manager on duty | Cell |
| Manual scheduling | Production Planning Manager | Shift supervisors | Cell |
| Ransom and shutdown decisions | President with the VP Operations | n/a | Cell |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and the identity provider may be compromised. Coordinate on personal phones and the printed contact list in the incident binders (plant office, HQ reception, and the Controls Engineer's truck).

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder in three places: this runbook, contacts, the notification matrix, the 12 utility security contacts, the paper traveler kit, and oven safe-state procedures
- [ ] Immutable ERP backups in a separate account and region, restore-tested within 90 days (CP-9, CP-4). **Gap until POAM-002 and POAM-007 close**
- [ ] Offline, verified copies of PLC, HMI, and CNC programs and winding recipes (POL-04 4.9). **Gap: last ad hoc copy 2026-02 (P01 R-021)**
- [ ] Known-good TMU firmware images with supplier hashes on an offline drive held by the VP Engineering (POL-01 4.8)
- [ ] 24x7 managed detection on endpoints and firewalls (SI-4). **Gap until POAM-006 closes**
- [ ] Documented isolation points: IT/OT firewall, MES office interface, cloud VPN, OEM routers, historian connector (POAM-001 milestone 2026-11-30)
- [ ] Two break-glass administrator accounts sealed and tested (POL-02 4.10)
- [ ] OT-capable retainer confirmed and insurer panel contacts current (POAM-008)
- [ ] Printed 5-day production schedule refreshed daily during storm season (P05 BP-01)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or files renamed with an unknown extension, on any server or PC | Staff report; EDR alert | Call the incident line. **Do not power off.** Unplug the network cable |
| HMI screen locked, showing a ransom note, or behaving on its own (setpoints or recipes changing) | Operator; shift supervisor | Operator steps back and calls the shift supervisor, who calls the Controls Engineer and the Plant Manager. **Do not touch the controls** |
| Kiosks or the MES stop responding across a bay | Shift supervisor | Call the incident line; switch to paper travelers |
| Many files changing at once on the file server or PLM vault | EDR; backup job failure | IT Manager opens the incident |
| New administrator accounts, or backups deleted in the cloud tenant | Cloud audit log; backup alert | IT Manager opens the incident and disables the cloud VPN |
| Unexpected session on an OEM router or remote access gateway | Router or gateway log (once recorded) | Controls Engineer powers the router off and opens the incident |

**Declare a ransomware incident when** encryption or a ransom note is confirmed on any system, or when any plant controller or HMI shows unauthorized changes. The IT Manager declares for IT and the Controls Engineer for OT (POL-03 4.3).

**Record the time of declaration.** Two clocks can start from it:
- the 48-hour utility addendum notice, which runs from **confirmation** of an incident related to products or services supplied to a utility (see section 6);
- the Florida 30-day notice, which runs from **determination** of a breach of employee personal information.

## 3. First hour: safety, isolation, and calls (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Safe state.** Plant Manager decides for each area: <br>- *Drying ovens:* if the local PLC is running normally, let the cycle finish under operator watch at the panel; otherwise follow the oven safe-shutdown procedure. <br>- *Oil fill station:* stop. <br>- *Test bay:* stop tests and de-energize. <br>- *Winders and core lines:* stop at the end of the current operation | Plant Manager, Controls Engineer, oven operators | Every area in a known safe state, logged with times |
| 2. **Isolate IT from OT.** <br>- Block all rules on the IT/OT firewall. <br>- Unplug the MES server's office network interface. <br>- Power off the 3 OEM cellular routers. <br>- Disconnect the historian's outbound connector to the AI-002 service | Controls Engineer | Plant network has no path to the office or the internet |
| 3. **Isolate the office and cloud.** <br>- Unplug affected servers and PCs, leaving them powered on for memory evidence. <br>- Disable the site-to-site VPN to the cloud tenant. <br>- Suspend the MSP's RMM tool | IT Manager with the MSP | Spread stopped; cloud tenant cut off |
| 4. **Call the insurer's breach hotline.** Engage counsel, forensics, and the OT-capable firm through the insurer | Controller | Claim number issued |
| 5. **Protect identity.** <br>- Revoke all sessions in the identity provider. <br>- Reset administrator credentials with the break-glass accounts. <br>- Check that the hardware-key policy is intact | IT Manager | Sessions revoked; admin credentials rotated |
| 6. **Go manual.** <br>- Switch to paper travelers and the printed schedule. <br>- Hold new work order release | Production Planning Manager, shift supervisors | Paper workflow running |
| 7. **Start the incident log:** timeline, decisions, who, and when | IT Manager | Log open (paper if needed) |

## 4. Analysis (RS.AN)
1. **Scope.** Which servers, PCs, HMIs, controllers, and cloud workloads are affected? Sources: EDR, identity provider sign-in logs, cloud audit logs, firewall logs, and a walk-down of every HMI and engineering workstation. Cloud logs keep 90 days and identity logs only 30 days (POAM-015), so export them now.
2. **Controllers.** Did the attacker reach the PLCs or only the HMIs? The Controls Engineer compares controller programs and recipes with the most recent offline copies. The OT firm assists. **No controller is trusted until checked.**
3. **Initial access.** Check phishing, the VPN, the MSP's RMM tool, OEM routers, and the historian connector.
4. **Preserve evidence** before any wipe (POL-03 4.10): memory and disk images of key servers, HMI images, controller program uploads, and firewall, VPN, and router logs. Keep chain of custody.
5. **Exfiltration.** Were designs, customer substation drawings, FCI, or employee personal information taken? Check egress logs and cloud storage access. **This drives the Florida and customer decisions.**
6. **Products and customers.** Was the TMU firmware library (on the engineering file share) or the configuration tool touched? Were field laptops or saved utility credentials exposed? **This decides whether the incident is "related to products or services supplied" under the addenda.**
7. **Backups.** Confirm that backups are intact before any restore. Today they sit in the same cloud account (POAM-002), so check them for deletion or encryption first.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure (IP addresses, domains) at the edge firewall and in the cloud network rules.
2. Disable compromised accounts. Rotate service accounts, the integration service credentials, EDI credentials, and every shared HMI and test PC password (POAM-004).
3. **Rebuild, do not decrypt and reuse.**
   - Office PCs and servers: rebuild from standard images.
   - Cloud VMs: rebuild from clean templates and patch before reconnecting.
   - MES: rebuild as a single-homed server on the plant side, with no office interface (POAM-001 design).
4. **HMIs and engineering workstations:** reimage from OEM media with OEM help, then load verified project files. Unsupported operating systems (11 of 18) may need OEM media or replacement units (P01 R-009).
5. The forensic and OT firms confirm that persistence is removed from IT, cloud, and OT before recovery starts.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Legal counsel reviews every external notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Hour 0-2 | Insurer notified; counsel and response firms engaged | Controller |
| Hour 0-4 | Staff briefing by shift: what happened, manual procedures, report anything odd, do not post online | Plant Manager; HR Manager |
| Day 0-1 | Voluntary report to the FBI (IC3 or field office) and CISA. Supports OFAC mitigation if payment is considered; also the path CIRCIA would formalize | IT Manager |
| **Within 48 hours of confirmation** | **Incident notice to each of the 12 addendum utilities** if the incident relates to supplied products or services (section 4 step 6). If in doubt, counsel decides early. The deadline is a contract term | Contracts and Compliance Manager |
| Within 1 business day | Access-revocation notice to each utility where an exposed field technician credential exists | Field Service Manager |
| Day 1-3, then daily | Delivery-impact updates to utilities with storm-restoration orders and other affected customers; update to the federal contracting officer on delivery impact | Contracts and Compliance Manager; VP Operations |
| As needed | FAR 52.204-25(d) report within 1 business day if covered equipment is identified during the rebuild | Contracts and Compliance Manager |
| Within 30 days of determination | Florida notice to affected current and former employees; Department of Legal Affairs if 500 or more; consumer reporting agencies if more than 1,000 | HR Manager and counsel |
| Within 30 days of knowing | Disclosure to addendum utilities of any vulnerability found in supplied firmware or software | VP Engineering |
| Ongoing | Coordinate response with affected utilities (addendum sec. 2); share indicators | IT Manager; Contracts and Compliance Manager |

**Not required:**
- **No CIRCIA report is required.** The rule is proposed only; report voluntarily instead.
- **No DFARS report.** The company has no DoD work.
- **No FAR 52.204-21 incident report.** The clause has no reporting paragraph.

**Ransom decision:** requires the President, counsel, the insurer, and an OFAC sanctions check (POL-03 4.9). Paying does not remove any notice duty.

**Storm season.** If a hurricane watch covers a utility customer's service area during the incident, the VP Operations tells that utility the realistic ship dates for its reserved storm units within 24 hours. This is a business commitment, not a legal deadline.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 6). **No plant equipment restarts until the Controls Engineer has verified its programs and settings (POL-03 4.4).**
1. **Drying ovens and oil fill (BP-03, RTO 12 h).**
   - Verify the PLC program and recipes against the offline copy.
   - Restore the HMI.
   - Plant Manager approves the restart.
2. **Identity provider and administrator access** (break-glass if needed), 2 h.
3. **Internet, firewalls, and the cloud VPN**, 4 h. Rebuild the IT/OT firewall rules as deny-by-default with only the flows needed now.
4. **Test bay PCs (BP-05, RTO 24 h).**
   - Rebuild with unique administrator accounts.
   - The Quality Manager checks raw test data against printouts before any certified test report is signed.
   - Retest where data integrity is in doubt.
5. **ERP and APS (BP-01, RTO 24 h).**
   - Restore from the most recent clean backup.
   - Reconcile orders, receipts, and shipments made on paper since the incident.
6. **MES and kiosks, 24 h.**
   - Bring up the rebuilt single-homed MES.
   - Re-enter paper traveler confirmations.
7. **Integration service**, 24 h. Reconnect to the MES only through the new restricted path.
8. **TMU firmware library and field laptops (BP-09), 24 h.**
   - Rebuild the library from the known-good offline images.
   - Re-verify every hash against the supplier's signatures before any firmware is loaded at final test (addendum sec. 5).
9. **Winding and core line HMIs (BP-02), 48 h.** Until then, run manual recipe entry from printed winding sheets with an engineering double-check.
10. **PLM vault (BP-06), 48 h.** Restore from the nightly backup or the weekly cloud copy; verify design files against release records.
11. **EDI (BP-07, BP-08), 48 h.**
12. **Tank shop (BP-04), 72 h.**
13. **Payroll and finance (BP-10), 72 h.**

**Validate before reconnecting:**
- EDR is clean;
- credentials are rotated;
- systems are patched;
- the OT firm agrees the plant network is clean.

**Communicate restoration (RC.CO):**
- Tell staff by shift.
- Tell utilities and the contracting officer when production and deliveries resume.
- Send a final addendum update to utilities that received the 48-hour notice.

## 8. Post-incident (ID.IM)
- Hold a lessons-learned meeting within 14 days of recovery. POL-03 4.12 requires documentation within 30 days.
- Update the risk register (P01, especially R-001, R-002, R-003, R-006, R-021), the POA&M (P07), the BIA recovery times (P05), and this runbook.
- Retain incident records, notices, and evidence for at least as long as counsel and the insurer require. Keep export records for 5 years (15 CFR 762.6).
