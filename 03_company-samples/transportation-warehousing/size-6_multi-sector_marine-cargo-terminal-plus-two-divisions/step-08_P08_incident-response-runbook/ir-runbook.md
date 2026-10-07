# Incident Response Runbook: Ransomware Through the Integration Hub Disrupting the TOS at All Terminals

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Transportation and Warehousing |
| Incident type | Ransomware with data theft (double extortion) that starts in the group B2B integration hub (SYS-G4), disrupts the TOS at all 9 terminals and steals data from all three divisions |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06). For Marine Terminals this runbook is part of each facility's Cyber Incident Response Plan (33 CFR 101.650(g)(2)) |
| Runbook owner | Group CISO; Coast Guard reporting owned by the Division CySO; all other notifications owned by the Group General Counsel |
| Approved | 2026-09-15 by the Group CISO, the Group General Counsel and the Division CySO |
| Last tested | Technical playbooks tested quarterly; terminal cyber drills at T1 to T6 in 2026. **The multi-regulator notification matrix has not been exercised** (scenario gap 7); the first cross-division tabletop, using this scenario, is due 2026-12-15 (POAM-004, POAM-022) |
| Handling | SSI once terminal contacts and network details are added (POL-04 5.2) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** an attacker exploits a newly disclosed flaw in the managed file transfer software on SYS-G4 before the patch is applied, and takes over the hub service account that can write to every division's inbound folders (P07 CA-3 finding).
- **Spread:** from the hub the attacker uses the static passwords of the TOS EDI adapter service accounts (P07 IA-5 finding) to reach the TOS application and database in provider A, and the hub's file drop to the Gulf terminals to reach SYS-T1L servers on the flat T7 to T9 networks (P01 MT-002).
- **Dwell:** 5 days. The attacker copies the TOS gate transaction history (truck driver names and license numbers), customer cargo and booking data for all 9 terminals, Freight Trading supplier and customer EDI files (including DoD order messages, which are FCI), and tenant rent remittance files.
- **Impact on Day 0 (Sunday, 02:00):** SYS-G4, the SYS-T1 application servers and the SYS-T1L servers and gate servers at T7 to T9 are encrypted; the T8 PACS server is also encrypted. All 9 terminals lose the TOS. The T5 automated stack stops. Freight Trading and Port Real Estate SaaS systems keep running but lose partner and bank files. An extortion note names all three divisions.
- **Forensic estimate at Day 4:** about 210,000 truck drivers' names and license numbers (about 95,000 Florida residents; the rest mostly in Georgia, Louisiana and Texas); cargo and booking data for about 2,300 customers; EDI files of about 400 trading partners; remittance files for about 180 tenants, about 40 of them sole proprietors. No CUI or covered defense information was on any affected system (the 2026-06-18 drawings were quarantined elsewhere).

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Group incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Coast Guard reporting and terminal incident command | Division CySO | Alternate CySO at each terminal (T1 to T6); Gulf terminals general manager for T7 to T9 until alternates are designated | Terminal radio and the bridge |
| Terminal safety and security | FSO at each terminal | Security supervisor on duty | Security office radio |
| OT safety | Marine Terminals director of engineering | Terminal OT leads | Bridge; crane and ASC vendor 24x7 lines |
| Technical response | Group SOC, cloud and integration teams | Forensic firm on retainer (through the insurer's panel) | SOC bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division general counsels | Out-of-band bridge |
| DoD clause decisions | Freight Trading federal contracts compliance manager | Freight Trading general counsel | Division bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Partners and communications | Group communications lead | Division customer services leads | Out-of-band bridge |
| Law enforcement | FBI field offices; CISA | n/a | Contacts in the offline incident binders |

**Out-of-band first.** Assume the attacker can read corporate email and chat. Use the crisis line, radios and managed mobile devices. The printed binder at each terminal security office and at each division command center holds contacts, this runbook, the notification matrix and manual operating forms.

## 2. Preparation checks (Identify / Protect)
- [x] Immutable backups of SYS-T1 and SYS-G4 configuration in the provider B vault, with a separate backup identity (CP-9; P07 satisfied)
- [x] 24x7 SOC with EDR on all IT servers and workstations, including the Gulf terminals (SI-3, SI-4)
- [x] Break-glass accounts per critical system held by each FSO; tested quarterly
- [ ] Hub routes and service accounts separated by division (**gap until POAM-014 closes**)
- [ ] EDI adapter service accounts on certificates (**gap until POAM-006 closes**)
- [ ] Gulf terminals segmented, logged to the SIEM and backed up to the vault (**gap until POAM-011 to POAM-013 close**)
- [ ] Alternate CySOs at T7 to T9 (**gap until POAM-025 closes**)
- [ ] Notification matrix complete and exercised (**gap until POAM-004 closes**); DFARS medium assurance certificate held (**POAM-016**)
- [x] Printed dangerous cargo list at every shift change at T1 to T6 (T7 to T9 from 2026-10-01)
- [x] Forensic retainer and insurer panel confirmed; disclosure committee charter covers cybersecurity

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Encryption on hub, TOS or gate servers; ransom note | EDR, cloud audit logs, terminal staff | Declare Severity 1; open the bridge; call the CySO |
| Hub service account reaching TOS or Gulf servers outside its normal routes | SIEM, hub logs | Disable the account; start triage |
| Bulk reads of TOS gate transactions or customer data by a service account | SIEM, database audit | Disable the account; preserve logs |
| TOS down at several terminals at once | Planners, gate clerks | Treat as possible ransomware until ruled out |
| Crane, ASC or RTG behaves unexpectedly, or HMI settings changed | Operators, engineers | **Stop the equipment in a safe state** (POL-03 4.7); call the director of engineering and the CySO |
| Extortion email or leak-site post naming any division | Email, threat intelligence, law enforcement | Declare Severity 1; preserve the message |

**Severity 1** (group scale, POL-03 4.2): encryption or theft in a shared service, any regulated facility affected, or more than one division involved.

**Clocks start at evidence, not certainty.** The Coast Guard report under 33 CFR 6.16-1 is due **immediately** on evidence of an actual or threatened cyber incident. The DFARS clock (72 hours) runs from discovery. State clocks run from determination of the breach. The SEC materiality determination must be made without unreasonable delay after discovery; the 4-business-day filing clock runs from the determination. Record each of these times in the incident log.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Safety first.** Stop crane, ASC and RTG moves where OT integrity is in doubt (all of T7 to T9; the T5 automated block); hold vessel work that depends on TOS hazardous cargo data; issue the printed dangerous cargo lists | Terminal operations leads with the director of engineering; FSOs | Equipment in a safe state; lists at each security office |
| 2. **Report under 33 CFR 6.16-1:** the CySO calls the COTP for each of the 4 COTP zones, the FBI and CISA, naming each affected facility. Do not wait for forensics | Division CySO (alternates if unreachable) | Report references recorded |
| 3. Isolate: shut the hub's partner interfaces; block hub-to-division routes at the provider A hub; drop the WAN links to T7 to T9; disconnect Gulf OT from IT; keep T1 to T6 OT zones closed except the equipment interface, then close that too | Group network and cloud directors; Gulf terminals general manager | Links down; vault unreachable from compromised identities |
| 4. Disable the hub service account and all EDI adapter service accounts; revoke sessions; rotate privileged credentials from clean devices (break-glass if needed) | Group identity director | Accounts disabled |
| 5. Snapshot affected cloud servers and image Gulf servers for forensics before rebuilding; legal hold on logs | SOC; forensic firm | Evidence list signed |
| 6. Start manual working at every terminal: manual gate on reduced lanes with printed release lists (imports only if confirmed released), radio dispatch, paper tally; T5 vessels moved to T6 where berth space allows | Terminal operations leads; FSOs | Manual procedures running (P05) |
| 7. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 8. FSO at T8 reports the PACS outage as a breach of security to the NRC if the FSP measure was circumvented (101.305(b)); all FSOs assess with their COTP whether a TSI is developing | FSOs | Reports recorded |
| 9. Tell carriers, port authorities, port community systems, the customs data exchange service and trucking companies that EDI and gates are suspended and that messages after the declaration time are not trusted until verified | Division customer services leads | Partners called from the printed list |
| 10. Brief the Group CISO; convene the disclosure committee within 24 hours (POL-03 4.6) | Group CISO | Committee convened |

## 5. Analysis (RS.AN)
1. **Scope by system and division.** Hub logs (AU-12) show which partner folders and routes the attacker used; database audit logs show which TOS tables were read; EDR shows which hosts were touched. Map each data set to its division and owner.
2. **Personal information by state.** Count drivers, employees and sole-proprietor tenants by state of residence. These counts drive Florida and other state notices.
3. **DoD clause check (first 24 hours).** The federal contracts compliance manager confirms whether any covered defense information was on an affected system. DoD order EDI messages are FCI, not covered defense information, and FAR 52.204-21 has no reporting duty. In this scenario no covered defense information was affected, so no DFARS report is due; the decision and its evidence are recorded. If any were found, the 72-hour DFARS report, malware submission and 90-day preservation in the matrix apply.
4. **OT check.** With crane and ASC vendors, compare PLC programs and HMI settings at T7 to T9 and the T5 equipment control system with the approved versions held in the OT repository (or vendor copies for the Gulf terminals). **No equipment returns to TOS-directed work until signed off.**
5. **Commercial data.** Customer cargo and booking data is confidential under terminal services agreements; trading partner files and tenant remittance files under their agreements. Counsel decides customer and partner notices.
6. **Root cause:** the unpatched hub software, the hub service account's cross-division reach, static EDI adapter passwords, and the flat Gulf networks. Feed to P01 GR-01, GR-11, GR-16 and MT-001, MT-002.

## 6. Containment and eradication (RS.MI)
1. Rebuild SYS-G4 from code in a clean account, patched, with **separate routes and service accounts per division** and one credential per partner (accelerates POAM-014). Retire the 2 FTP partners at the same time.
2. Move EDI adapters to certificates before reconnecting them to the TOS (accelerates POAM-006).
3. Rebuild TOS application servers from code; do not reuse encrypted hosts.
4. Rebuild SYS-T1L and gate servers at T7 to T9 from clean media, behind the interim IT/OT firewalls (accelerates POAM-011). If rebuild of the legacy TOS would take longer than moving T7 to T9 onto SYS-T1 under the migration plan, the Gulf terminals general manager and the CySO decide which is faster and safer.
5. Confirm with forensics that no persistence remains in SYS-G1, the landing zone or division accounts before reconnecting anything.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (28 rows).** Counsel approves every notice except the Coast Guard report, which does not wait for counsel. The matrix has three layers:
1. **Facility duties (Marine Terminals):** immediate reports for each facility under 6.16-1, MTSA reports under 101.305 decided by each FSO, and incident records kept 2 years (101.640).
2. **Group and division duties:** SEC materiality and Form 8-K; the DFARS check for Freight Trading; state breach notices for each state where affected individuals reside.
3. **Contract duties:** carriers, port authorities, port community systems, the customs data exchange service, trading partners, tenants and banks, and the insurer.

| When (from Day 0 discovery) | Action | Owner |
|---|---|---|
| Immediately (first hour) | Report to each COTP, the FBI and CISA under 6.16-1; this also meets the NRC duty (101.620(b)(7)) | Division CySO |
| Without delay | NRC breach of security report for T8 (101.305(b)); TSI reports to the COTP if the FSOs and COTPs conclude one occurred (101.305(c)(1)) | FSOs |
| Day 0 | Insurer, counsel and forensics engaged; carriers, port authorities, the customs data exchange and port community systems told operationally | Group Chief Risk Officer; customer services leads |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Within 24 hours | DFARS check recorded (no covered defense information affected in this scenario; if there were, report to DoD within 72 hours of discovery) | Federal contracts compliance manager |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| As facts develop | Updates to the COTPs and the FBI; answer COTP questions on terminal status and hazardous cargo | Division CySO; FSOs |
| As soon as known | Decide whether personal information was acquired and determine the breach; record the determination date | Group General Counsel |
| Within 30 days of determination | Florida individual notices to about 95,000 drivers; Department of Legal Affairs (500 or more Floridians); consumer reporting agencies (more than 1,000). Apply each other state's law to drivers and tenants who live there | Group General Counsel with Marine Terminals and Port Real Estate |
| Per contract | Customer, trading partner, tenant and bank notices about commercial data | Division general counsels |
| Throughout, kept 2 years | Incident records for each facility (101.640; 33 CFR 105.225(b)(3)) | FSOs |

**Plan to the shortest clock.** Here the order is: Coast Guard (immediately), MTSA reports (without delay), the DFARS check (72-hour clock, here not triggered), SEC (4 business days after the materiality determination), then state notices (30 days in the Florida example).

**Materiality factors for the disclosure committee:** all 9 terminals on manual working (about $9.3 million of division revenue a day at risk and about 55 vessel calls a week affected); carrier diversions and contract penalties; theft of customer commercial data and driver personal information; regulator attention (Coast Guard, state attorneys general, and the Federal Maritime Commission if customers complain); recovery and notification cost; and the effect on Freight Trading and Port Real Estate, which kept operating.

**Ransom decision:** board risk committee chair, Group General Counsel, insurer, an OFAC sanctions check and notice to law enforcement (POL-03 4.9). Paying does not remove any reporting or notice duty when data was taken. **CIRCIA is not in effect** (final rule not published as of 2026-09-25); there is no CIRCIA 72-hour or 24-hour report today.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7):
1. SYS-G1 identity and break-glass access confirmed clean
2. Landing zones, WAN and the provider A hub, with OT zones isolated
3. SOC visibility (SIEM and EDR)
4. Facility security: PACS at T8 rebuilt; TWIC checked visually until then; dangerous cargo lists confirmed
5. Crane, ASC and yard OT checked and signed off; cranes run in local mode meanwhile
6. to 7. SYS-T1 restored from the provider B vault (last clean point before the attacker's first database read), then vessel and yard operations at T1 to T6
8. SYS-G4 rebuilt clean, partner by partner, starting with the customs data exchange and carriers with vessels due
9. to 11. Truck gates, the Gulf terminals and customs status and carrier EDI
12. to 26. Port Real Estate building access, Freight Trading partner EDI, then the remaining processes in BIA order

**Validate before resuming normal operations:**
- **Reconcile the TOS with reality.** Compare restored inventory with yard checks, paper gate interchanges and carrier bay plans; key in all manual moves before automated dispatch restarts.
- **Customs holds first.** Refresh release and hold status from the customs data exchange before any import container leaves by an automated gate.
- **Hazardous cargo.** Each FSO confirms that TOS dangerous cargo locations match the printed list and a yard check.
- **T5 last among operations.** The automated stack restarts only after the equipment control system and its link to the TOS are signed off, and with the optimization service in advisory mode (P10).

Tell staff, the COTPs, carriers and other partners when each service is back (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.12).
- Update P01 (GR-01, GR-03, GR-11, GR-16, MT-001, MT-002), the POA&M (POAM-004, POAM-006, POAM-011 to POAM-014), the notification matrix, this runbook and each terminal's Cybersecurity Plan (101.650(g)(3)).
- Count the incident response toward the drill and exercise requirements only if goals are documented for the COTP (101.635(a)(2)).
- Consider the Reg S-K Item 106 description for the next annual report.
- Keep incident records at least 2 years for facility records (101.640) and 6 years for group records (POL-01 4.13).
