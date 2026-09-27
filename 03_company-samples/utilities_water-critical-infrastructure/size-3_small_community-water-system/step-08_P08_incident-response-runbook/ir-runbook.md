# Incident Response Runbook: Remote-Access Compromise of a Treatment-Plant HMI

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (investor-owned community water system, 46,200 population served) |
| Tier / Vertical | Small / Water and Wastewater Systems |
| Incident type | An unauthorized person uses a remote access path (the integrator's remote desktop agent, or the on-call VPN) to control an HMI at WTP-1 or WTP-2, for example by changing the sodium hydroxide (caustic) dose setpoint |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 (sections 6.4 and 6.5) |
| Policy basis | POL-03 Incident Response Policy; ERP (42 U.S.C. 300i-2(b)(2)) |
| Runbook owner | IT Manager (security lead), with the Operations Manager for all process decisions |
| Approved | 2026-08-31 by the General Manager. Becomes the cyber annex of the ERP when the ERP is certified (target 2026-12-11) |
| Last tested | Not yet. First OT tabletop with the integrator due 2026-11-30 (POAM-009) |

**The rule that overrides everything else in this runbook: keep the water safe first, then investigate.** Operators may take any process safety action at any time without waiting for IT, management, or forensics.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Process safety lead (first 60 minutes) | Chief Plant Operator on duty | Operations Manager | Control room phone; radio |
| Incident commander | IT Manager | Operations Manager | Incident line (cell), then the out-of-band group on personal phones |
| OT technical response | SCADA and Instrumentation Technicians | SCADA integrator (only through an approved, observed session or on site) | Cell; integrator 24x7 line |
| Water quality and public notice | Water Quality Supervisor | General Manager | Cell |
| Executive decisions and external communications | General Manager | Operations Manager | Cell |
| Legal counsel and forensics | Outside counsel and forensic firm through the cyber insurer's panel | n/a | Insurer breach hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the ERP binder |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the ERP binder |
| Regulator | State drinking water primacy agency (after-hours line) | n/a | PN SOP contact sheet |

**Out-of-band first.** Assume the attacker can see business email and chat. Coordinate on personal phones and the printed ERP binder in the WTP-1 control room, at WTP-2, and in the Operations Manager's truck.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed ERP binder at WTP-1, WTP-2, and the administration office: this runbook, contacts, the notification matrix, manual-mode procedures, and Tier 1 notice templates
- [ ] Offline, encrypted copies of PLC logic and HMI projects less than 30 days old, in two locations (CP-9). **Gap until POAM-006 closes (2026-10-15)**
- [ ] Remote access only through the gateway with MFA, approval, and recording (AC-17, MA-4). **Gap until POAM-002 and POAM-003 close (2026-10-31)**
- [ ] OT and firewall logs retained at least 1 year (AU-11). **Gap until POAM-012 closes (2027-03-31); today firewall logs roll over in 7 days**
- [ ] Written manual-mode procedure for each chemical feed; manual drill within the last 6 months (CP-3). Drill done 2026-05; procedures incomplete (P01 R-018)
- [ ] Offline export of customer contact lists and media contacts less than 31 days old (P03 G-048)
- [ ] Known-good rebuild media for the HMIs and engineering workstation from the integrator (CP-10). **Gap until the OT recovery procedure is done (2026-12-11)**
- [ ] Insurer panel forensic firm with OT experience confirmed (POAM-009)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| The HMI cursor moves or screens change when no one on site is using it | Operator | **Go to section 3 now.** Then call the Chief Plant Operator and the incident line |
| A chemical feed setpoint, pump mode, or alarm limit changed that no one on shift changed | Operator; HMI event list; analyzer alarm | Section 3. Treat as an incident until the change is explained |
| pH or chlorine analyzer high/low alarm (hardwired) with no process cause | Hardwired alarm panel | Section 3; verify with a grab sample |
| A remote session or VPN login outside an approved window | Gateway or VPN alert (after POAM-002); integrator call | Disconnect the session (section 3 step 3); call the incident line |
| Integrator reports its own compromise, or CISA or the FBI warns about the remote tool | Phone or email | IT Manager disables the path; declare if any session happened in the exposure window |
| OT monitoring alert (after POAM-011) | Sensor | IT Manager triages with a SCADA technician |

**Declare an HMI compromise incident when** any control action on the WTSS cannot be traced to an authorized person, or an unapproved remote session reached an HMI or the engineering workstation.

**Record the time the company learned of the situation.** For public notice, the 24-hour clocks run from when the system learns of the situation (40 CFR 141.202(b)).

## 3. First 60 minutes: process safety and containment (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Put the affected chemical feed (and any process that looks changed) in **local/manual** control at the pump panel. Return the dose to the normal rate. The hardwired stroke limits cap the pump in the meantime | Operator on duty | Feed on local control at the normal rate |
| 2. Take grab samples at the plant clearwell and high-service discharge for pH and chlorine. Repeat every 30 minutes until stable | Operator; lab if on site | Two results in range, 30 minutes apart |
| 3. **Cut every remote path:** unplug the engineering workstation's network cable (do not power it off); IT Manager disables the VPN and blocks the integrator tool at the IT/OT firewall | Chief Plant Operator; IT Manager | No remote session possible (confirmed on the firewall) |
| 4. Decide the operating mode: (a) keep SCADA islanded from the business network with operators watching every change, or (b) full manual operation of the plant. **If a PLC or HMI integrity is in doubt, choose manual** | Operations Manager | Mode recorded in the incident log |
| 5. Check whether off-spec water reached the distribution system: clearwell and storage levels, time off-spec, flows | Water Quality Supervisor; Operations Manager | Yes/no with evidence |
| 6. Call the cyber insurer's hotline; engage counsel and forensics through the insurer | General Manager | Claim number issued |
| 7. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

If the change could affect public health and cannot be reversed quickly, the Water Quality Supervisor starts the Tier 1 decision (section 6) **at the same time**, not after the investigation.

## 4. Analysis (RS.AN)
1. **Scope:** which HMIs, servers, PLCs, and accounts were touched. Sources: HMI event and alarm history, the remote desktop agent's connection history (request the vendor's relay logs through the integrator), VPN logs, IT/OT firewall logs (export now; they roll over in 7 days), and the engineering workstation.
2. **Initial access:** which path and which credential. Check whether the integrator's account or an on-call operator's VPN account was used, and whether the password was reused elsewhere.
3. **PLC integrity:** compare the running logic in every PLC with the offline known-good copy (once POAM-006 exists; until then, with the integrator's copy, which must itself be verified). Check PLC key switch positions.
4. **Lateral movement:** did the attacker reach the historian, the business network, or the cloud tenant? If the business network or the CIS was reached, customer personal information may be involved (Fla. Stat. 501.171 rows in the matrix).
5. **Preserve evidence:** forensics images the engineering workstation and affected HMIs before rebuild, where this does not delay safety actions. Keep chain of custody. Photograph HMI screens and panel states.

## 5. Containment and eradication (RS.MI)
1. Keep all remote paths closed until the gateway with MFA and session approval is in place. The integrator works on site, observed, until then.
2. Change every credential the attacker could have seen: HMI and engineering accounts, device passwords, VPN accounts, the integrator's accounts, and any passwords in the device spreadsheet.
3. Remove the remote desktop agent. Rebuild the engineering workstation and any affected HMI from known-good media. **Do not clean and reuse them.**
4. Reload PLC logic from the verified known-good copy if any difference is found. Set key switches to RUN.
5. Confirm with forensics that no persistence remains on the historian or business network before reconnecting anything.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every legally required notice. The Water Quality Supervisor owns the public notice clock.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer notified; counsel engaged | General Manager |
| Hour 0-4 | Decide whether this is a failure or significant interruption in key treatment processes (Tier 1 trigger, 40 CFR 141.202(a) Table 1 item (7)). If yes, draft the notice from the template | Water Quality Supervisor with the General Manager |
| No later than 24 h after learning of the situation | If Tier 1: deliver the notice to all persons served (broadcast media, posting, hand delivery, or another approved method) and start consultation with the primacy agency | Water Quality Supervisor; Customer Service and Billing Manager |
| Within 24 h of declaration | Report to the FBI (tampering, 42 U.S.C. 300i-1) and to CISA (voluntary) | IT Manager |
| Within 48 h | If a drinking water regulation was violated (including missed monitoring), report it to the state (40 CFR 141.31(b)) | Water Quality Supervisor |
| Within 10 days of completing notices | Public notice certification with copies to the primacy agency (40 CFR 141.31(d)(1)) | Water Quality Supervisor |
| Within 30 days of determination | Only if customer personal information was accessed: Florida individual notice, and Department of Legal Affairs notice if 500 or more (Fla. Stat. 501.171) | Customer Service and Billing Manager with counsel |
| Day 0-2 | Staff briefing: what happened, operating mode, do not discuss outside the company | General Manager |

**The shortest clock is public health, not data.** For this incident type, the 24-hour Tier 1 notice and primacy agency consultation will almost always come due before any data breach clock. The CIS or email may be unavailable if the attacker reached the business network, so use the offline contact export and broadcast media.

**CIRCIA is not in effect.** If the final rule is published, add the 72-hour CISA report to this table. The company would be covered through the water-sector criterion.

**Ransom decision** (if the incident becomes extortion): requires the majority owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). SCADA comes back **after** safe water and communications are stable.
1. Manual operation of the affected plant with extra staffing (WARN mutual aid if the outage lasts beyond 24 hours)
2. Booster stations and tank levels on local control
3. Grab sampling every 4 hours at the plant outlets and 8 distribution stations
4. Public notice capability (offline contact list, media)
5. Field dispatch with printed map books
6. Customer service phones and CIS (confirm not affected)
7. SCADA servers and HMIs rebuilt from known-good media, then reconnected **one process at a time** with an operator watching each loop in manual before switching it back to automatic
8. Historian and the cloud replica; the anomaly detection model (P10) stays off until the replica is verified

**Validate before returning to automatic control:** credentials changed, PLC logic verified against the known-good copy, remote paths closed or behind the gateway, and 24 hours of stable manual-to-auto operation on the first process. Tell customers when any notice is lifted (RC.CO), using the same channels as the notice.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, including the integrator and the primacy agency contact if a notice was issued. POL-03 requires documentation within 30 days.
- Update the risk register (P01, especially R-001, R-002, R-006, R-008), the POA&M (P07), the RRA cyber addendum, and the ERP. A real incident is a reason to revise the ERP.
- Retain all incident documentation for at least 5 years (POL-01 4.10) and public notices and certifications for 3 years (40 CFR 141.33(e)).
