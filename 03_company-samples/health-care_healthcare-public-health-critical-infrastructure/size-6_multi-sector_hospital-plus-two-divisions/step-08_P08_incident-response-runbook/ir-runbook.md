# Incident Response Runbook: Ransomware Forcing EHR Downtime and Ambulance Diversion (Cross-Division)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Healthcare and Public Health |
| Incident type | Ransomware with data theft (double extortion) that starts at one hospital, spreads through the shared directory into both group data centers, encrypts the EHR and ancillary systems, the Health Plan claims core, and the group file service, and forces EHR downtime and ambulance diversion decisions at all 9 hospitals |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Emergency plan link | This runbook is the cyber annex of the hospitals' unified emergency preparedness plan (42 CFR 482.15(a)(2), (f)); clinical, diversion, and community communication steps use the plan's incident command and communication plan (482.15(c)) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel; clinical operations owned by the system emergency management director |
| Approved | 2026-09-15 by the Group CISO, the Group General Counsel, and the Hospital System president |
| Last tested | Technical playbooks tested quarterly. **The cross-division scenario, the notification matrix, and the diversion steps have not been exercised** (group gaps 2 and 8; EV-011, EV-012). The first tabletop is due 2026-12-15 and will count as the hospitals' additional annual exercise (POAM-005, POAM-023) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** an attacker uses stolen credentials for one of the 37 device vendor remote support connections that bypass PAM (P01 HS-005) to reach an imaging workstation at a community hospital with a flat network (HS-006).
- **Spread:** from that workstation the attacker harvests a cached administrator credential, takes control of the group directory forest, and moves into DC1 and DC2, which trust the same directory (GR-01).
- **Theft:** over 9 days the attacker copies EHR reporting extracts, Health Plan reporting shares, and College financial aid and registrar shares from the group file service (GR-11).
- **Impact (Day 0, 02:40):** the attacker encrypts EHR application and database servers in both data centers, the ancillary clinical servers, the Health Plan claims core, and the group file service, then emails an extortion demand naming all three divisions.
- **Forensic estimate at Day 6:** about 1.1 million hospital patients (about 780,000 in Florida), including about 40,000 patients of 12 community-connect practices; about 260,000 Health Plan members (about 190,000 in Florida), including members of 22 ASO employer plans; about 70,000 people appear in both sets; about 14,000 current and former College students' financial aid records (about 9,000 in Florida), including Social Security numbers.
- **What still works:** College SaaS systems (separate directory and vendors), the Health Plan UM platform and portals at provider A (no directory trust), the immutable vault at provider B, analog phones and EMS radios, and downtime workstations, whose last reports printed at 02:00.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander (technical) | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| System clinical command | System emergency management director, with the System CNO and system chief medical officer | Flagship hospital chief executive | System command center (flagship); radio and analog lines |
| Hospital incident command (each of 9) | Hospital chief executive or delegate | House supervisor on duty | Hospital command center; analog lines |
| ED medical lead (each ED) | ED physician on duty | ED medical director | ED analog line; EMS radio |
| Technical response | Group SOC, infrastructure, and identity teams; HCIS system owner | Forensic firm on retainer (insurer panel); EHR vendor's recovery team | SOC bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division general counsels | Out-of-band bridge |
| Hospital System breach decisions | Hospital System Privacy Officer | Hospital System security and compliance lead | Division bridge |
| Health Plan breach and insurance notices | Health Plan Privacy Officer; Health Plan compliance officer | Health Plan security and compliance lead | Division bridge |
| College notices (FSA, FTC, students) | College IT director (Qualified Individual) with the financial aid director | College president | Division bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division and hospital communications leads | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker controls the directory, email, chat, VoIP, and the file service. Use the crisis line, managed mobile devices, analog lines, EMS radios, and the printed binders in every hospital command center, ED, and division office. The binder holds contacts, this runbook, the notification matrix, the diversion script, and the downtime procedures.

## 2. Preparation checks (Identify / Protect)
- [x] Immutable vault at provider B with a separate backup identity, not reachable with directory credentials (CP-9; P07 satisfied)
- [x] 24x7 SOC with EDR on data center servers and workstations (SI-3, SI-4)
- [x] Downtime workstations on every unit and in every ED; paper downtime kits
- [x] Forensic retainer, insurer panel, and EHR vendor recovery services confirmed
- [x] Disclosure committee charter covers cybersecurity materiality
- [ ] Clean recovery environment for rebuilding the directory and the EHR (**gap until POAM-012 closes**; interim plan in section 8)
- [ ] Data center zones and the highest-privilege directory tier separated (**gap until POAM-007 closes**)
- [ ] All device vendor connections through PAM (**gap until POAM-013 closes**)
- [ ] Downtime workstations tested at all 9 hospitals in the last quarter (**3 hospitals overdue; POAM-009**)
- [ ] Notification matrix complete with insurance commissioner, FSA, and FTC contacts, and exercised (**gap until POAM-005 and POAM-021 close**)
- [ ] Cyber annex with system-level diversion criteria adopted into the unified emergency plan (**gap until POAM-023 closes**)

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| EHR unavailable at several hospitals at once, or ransom notes on servers | Nursing units, EDs, EDR, monitoring | Declare Severity 1; open the out-of-band bridge; start downtime everywhere |
| Mass encryption or deletion on data center servers or the file service | EDR, storage alerts | Declare Severity 1 |
| Unusual directory changes (new domain administrators, policy changes) | SIEM, directory monitoring | Isolate the accounts; escalate |
| Large outbound transfers from the file service or EHR reporting servers | Network detection at the data center edge | Block the destination; open an incident |
| Device vendor connection active at night or from a new location | Clinical engineering, firewall logs | Disconnect the vendor path; open an incident |
| Extortion email or leak-site post naming any division | Email, threat intelligence, law enforcement | Declare Severity 1; preserve the message |

**Severity 1** (group scale, POL-03 4.2): confirmed encryption or theft in a shared service, or any incident that stops clinical systems at more than one hospital.

**Record the discovery date for each entity** (POL-03 4.3). For each covered entity it is the first day the breach is known, or by reasonable diligence would have been known, to any workforce member (164.404(a)(2)); for a business associate, to any employee or agent (164.410(a)(2)); for the College's FTC notice, the first day known to any employee, officer, or other agent other than the attacker (16 CFR 314.4(j)(2)). Because the group SOC is corporate, **this runbook treats the day the SOC knew as the discovery date for every division**. Counsel may refine this, but no clock is planned from a later date.

## 4. First hours: two tracks (RS.MA, RS.MI, and patient safety)
The **technical track** (incident commander) and the **clinical track** (system clinical command) start together. The Group CISO and the system emergency management director join each other's briefings every hour.

| Step | Track | Who | Done when |
|---|---|---|---|
| 1. Start downtime procedures on every unit, ED, pharmacy, laboratory, imaging, and registration desk in all 9 hospitals; collect the last downtime reports | Clinical | Hospital incident command; charge nurses | Paper workflows running; report times logged |
| 2. Activate hospital incident command at all 9 hospitals and the system command center under the unified emergency plan | Clinical | System emergency management director | Command centers staffed |
| 3. Disconnect the WAN links between hospitals and the data centers, the device vendor connections, and the links to provider A; keep EMS radios and analog lines in service | Technical | Group network director | Links down; isolation confirmed |
| 4. Isolate affected servers from the network but leave them powered on for memory evidence | Technical | SOC; forensic firm | Servers isolated |
| 5. Confirm the vault at provider B is intact and unreachable from the compromised directory; rotate the vault's own credentials from a clean device | Technical | Group infrastructure director | Vault integrity report |
| 6. Patient safety checks: infusion pumps keep their last drug library; dispensing cabinets on override with pharmacist double-check; monitors on bedside alarms with more frequent rounds; blood bank on paper log | Clinical | System CNO; system chief pharmacy officer; clinical engineering | Safety checks logged at each hospital |
| 7. Call the cyber insurer; engage breach counsel, forensics, and the EHR vendor's recovery team through the panel | Technical | Group Chief Risk Officer | Claim number issued |
| 8. Tell division privacy officers, the Health Plan compliance officer, and the College Qualified Individual **on the bridge** (this starts corporate's business associate and service provider notices) | Technical | Incident commander | Each acknowledges |
| 9. Each hospital assesses whether it can safely accept ambulances (section 5) | Clinical | Hospital incident command with the ED medical lead | Decision recorded with time |
| 10. Escalate to the disclosure committee within 24 hours of declaration (POL-03 4.7) | Technical | Group CISO | Committee convened |
| 11. Start the paper incident log at the bridge and at each command center: timeline, actions, who, when | Both | Incident commander; each hospital incident command | Logs open |

## 5. Clinical operations and ambulance diversion (RS.MA, RC.RP)
**What diversion means.** EMTALA lets a hospital direct an ambulance that is not yet on its property to another facility when it is in "diversionary status" because it does not have the staff or facilities to accept any additional emergency patients (42 CFR 489.24(b), definition of "comes to the emergency department"). It does **not** change the duty to screen and stabilize anyone who arrives: walk-ins, and any ambulance that comes onto hospital property anyway, are still screened and stabilized.

**Hospital decision rule (from the P05 MTDs).** Each hospital's incident command decides with the ED medical lead. Consider diversion when any of these is true and not expected to recover within its MTD:
- The ED cannot document, order, and give medications safely on paper (BP-H01, MTD 4 h).
- Laboratory or blood bank results cannot be produced or reported (BP-H04, MTD 4 h).
- CT or the reading of imaging is down (BP-H05, MTD 8 h). Divert CT-dependent traffic (suspected stroke, major trauma) first.
- Clinical communications or transfer coordination are not working (BP-H09, BP-H08, MTD 2 h).

**System coordination rule (the multi-hospital problem).** In this scenario all 9 hospitals lose the EHR at once. If every ED diverts, a region can be left with no open ED. So:
1. Hospitals send their status to the system command center before telling EMS, unless a patient is in immediate danger.
2. The system command center, with county EMS and the regional health care coalition, keeps at least one ED open in each region (the flagship trauma center does not divert trauma unless its trauma capability itself is lost) and uses **partial diversion** (CT-dependent or specific services) before full diversion.
3. Transfers out go first to non-group hospitals that are not affected (482.15(b)(7)); the transfer center works from analog lines and the regional EMS radio.

**Diversion steps:**
1. Notify county EMS dispatch by radio or analog line using the script in the binder: scope (full or partial), reason ("IT systems outage"), and next update time. Do not say "cyberattack" on open radio.
2. Notify county emergency management, the regional health care coalition, and receiving hospitals, and report occupancy and capability to the authority having jurisdiction (482.15(c)(7)).
3. Record every diversion decision and status change with the time.
4. Review diversion status at least every 2 hours, and end it as soon as the affected process is back within its RTO or a safe paper workaround is running.

**Patients already in the hospitals.** Continue care on paper. Reprint medication administration records from the last downtime reports and reconcile them with pharmacy every shift. Move patients who need services a hospital cannot provide without its systems, using paper transfer packets and a copy log (482.15(c)(4)). Health information management at each hospital tracks every paper record created (POL-04 4.8). The sepsis model is down with the EHR; nurses continue manual sepsis screening at triage and every shift (P10).

**If downtime lasts more than 24 hours** (expected here, because the EHR rebuild estimate is 5 to 7 days): add a second paper MAR reconciliation per day, set up runners for laboratory and imaging results at every hospital, postpone elective surgery after the 8-hour MTD for perioperative services (BP-H03), and plan staffing for paper workloads.

## 6. Analysis (RS.AN)
1. **Scope by system and division.** Use EDR, directory, firewall, and storage logs to list encrypted and accessed systems. Map each to its division and covered entity.
2. **Initial access and spread:** confirm the vendor connection and the imaging workstation; identify the administrator credential used and every directory change the attacker made. Treat the whole directory forest as compromised.
3. **Data taken:** use file service and network logs to list the shares and extracts read and sent out. Map each file set to its owner: hospital patients (including community-connect practice patients), Health Plan members (including ASO plan members), and College students.
4. **Individuals by state:** for each covered entity, business associate customer, and the College, produce counts of affected individuals by state of residence. These drive HHS, media, state attorney general, consumer reporting agency, and FTC notices.
5. **Overlap:** identify people who are both patients and members. Each covered entity still owes its own notice.
6. **Four-factor assessment (164.402)** for each covered entity: nature and extent of the PHI, who obtained it, whether it was actually acquired or viewed, and the extent the risk has been mitigated. With confirmed theft by a criminal group, expect a breach finding.
7. **College determination:** whether unencrypted customer information of 500 or more consumers was acquired without authorization (16 CFR 314.4(j)); for FSA, report on suspicion, not on determination.
8. **Part 2 check:** confirm whether any Part 2 records received from outside programs were in the stolen extracts (none expected).

## 7. Containment and eradication (RS.MI)
1. Keep the data centers isolated from hospitals, the cloud, and the internet until the directory is rebuilt.
2. Disable every vendor remote connection; reconnect device vendors only through PAM with named accounts and MFA (accelerates POAM-013).
3. Rebuild the directory from a known-good state in an isolated network, reset every privileged and service credential, and rotate the vaulted interface credentials (accelerates POAM-002).
4. Rebuild servers from clean images; do not decrypt and reuse them.
5. Re-image the entry workstation and isolate the community hospital's device network (accelerates POAM-015).
6. Confirm with forensics that no persistence remains before any system is reconnected. The EHR vendor will require this confirmation before it supports the restore.

## 8. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (36 rows).** Counsel approves every notice. The matrix has four layers:
1. **Inside the group:** corporate notifies the Hospital System and the Health Plan as their business associate (164.410 and intercompany BAAs), and the College as its service provider; corporate also owes each division the Florida third-party agent notice (10 days after determination).
2. **Each covered entity's own duties:** the Hospital System and the Health Plan each notify their individuals, HHS, and media (164.404-164.408). They are separate covered entities (no affiliated covered entity designation, P03), so there are **two** HHS reports and two sets of letters. Coordinated letters to people in both populations must identify both entities.
3. **Business associate duties outward:** the Hospital System notifies 12 community-connect practices and the Health Plan notifies 22 ASO employer plans (164.410 and their BAAs), with each affected individual identified (164.410(c)).
4. **Regulators and investors:** state insurance commissioners in adopting states (72 hours after determination); Federal Student Aid (immediately) and the FTC (30 days after discovery) for the College; state attorneys general and consumer reporting agencies under each state's law (Florida worked example); the SEC if material.

| When (from SOC discovery, Day 0) | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer, counsel, forensics, and EHR vendor engaged; internal notices to all three divisions on the bridge | Group Chief Risk Officer; incident commander |
| Hour 1 and each change | County EMS, emergency management, and coalition informed of diversion and capability | Each hospital incident command; system command center |
| Day 0 | FSA breach report (actual or suspected breach of financial aid information) | College financial aid director with the Qualified Individual |
| Day 0-1 | Voluntary report to FBI or IC3 and CISA (supports OFAC mitigation if payment is considered) | Group CISO |
| Day 0-1 | Staff briefings at shift huddles; community statement that hospitals are open with service limits | Hospital chief executives; group communications |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts (POL-03 4.7) | Group General Counsel |
| Within 72 hours of determination | State insurance commissioners in adopting states (generic; Health Plan list) | Health Plan compliance officer |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 10 days of determination | Florida third-party agent notices from corporate to each division | Group General Counsel |
| Within 30 days of discovery | FTC Safeguards Rule notice (about 14,000 consumers) | College Qualified Individual |
| Within 30 days of determination | Florida individual notices (or HIPAA notice with a copy to the Department of Legal Affairs under the deemed-compliance path); Department notice (500 or more Floridians); consumer reporting agencies (more than 1,000). Apply each other state's law the same way | Each division with counsel |
| Within 60 days of discovery | HIPAA individual notices; HHS notice (500 or more, contemporaneous); media in each state with more than 500 affected residents; business associate notices to practices and ASO plans (sooner if their BAAs say so) | Hospital System and Health Plan Privacy Officers |
| Confirm before use | CMS notification under the MA contract (**unverified** in this sample) | Health Plan compliance officer |

**Plan to the shortest clock.** In this scenario the order is: EMS and emergency management (at each decision), FSA (immediately), state insurance commissioners (72 hours), SEC (if material), Florida third-party agent notices (10 days), the FTC and Florida 30-day notices, then the HIPAA 60-day outer limit.

**Materiality factors for the disclosure committee:** the number of people affected across both covered entities and the College; the length of EHR downtime and diversion at 9 hospitals; lost revenue (about $28.8 million a day of Hospital System revenue at risk, plus claims delays); regulatory exposure (OCR, state attorneys general and insurance departments, FSA, the FTC, CMS); recovery and notification costs; and reputation in the communities the hospitals serve. Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

**Ransom decision:** board risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not remove any notice duty when data was taken, and it does not shorten a safe rebuild.

**CIRCIA.** Not in effect as of 2026-09-25. If finalized as proposed, it would require a report to CISA within 72 hours of a covered incident and within 24 hours of a ransom payment, covering all 9 hospitals and the College. Recheck the matrix when the rule changes.

## 9. Recovery (RC.RP, RC.CO)
Restore in the BIA priority order (P05 section 7), with patient safety first:
1. Identity: rebuild the directory in an isolated network; restore SYS-G1 federation and break-glass access (BP-G01)
2. WAN and voice: reconnect hospitals one at a time after their endpoints are cleared (BP-G04)
3. Data center compute and storage, using clean images (BP-G03)
4. Vault restores, starting with the EHR database (BP-G05)
5. SOC visibility on everything reconnected (BP-G02)
6. Clinical communications and the transfer center (BP-H09, BP-H08)
7. EHR access for EDs, inpatient units, pharmacy, and laboratory, in that order (BP-H01, BP-H02, BP-H06, BP-H04), after the EHR vendor confirms the restored database is consistent
8. Device integration, perioperative systems, and imaging (BP-H07, BP-H03, BP-H05)
9. Health Plan UM (already running at provider A; reconnect the provider portal), community-connect practices, eligibility, and registration (BP-P01, BP-H13, BP-P03, BP-H10)
10. File service, portals, College shares, claims core, ASO claims, revenue cycle, public health feeds, financial aid files, financial close, sepsis alerting, payroll, and the rest of the BIA list

**Interim clean recovery approach (until POAM-012 closes).** There is no prepared clean environment, so the directory and the EHR are rebuilt in a quarantined segment of DC2 with new hardware credentials, using the vault copies and the EHR vendor's recovery team. The estimate is 5 to 7 days for EHR access and longer for full ancillary integration. This is why the clinical track plans for multi-day downtime from the first hours.

**Validate before reconnecting:** EDR clean, credentials rotated, systems patched, vendor connections in PAM, the device network at the entry hospital isolated. **Back-entry:** each unit enters or scans its downtime records on a documented schedule, starting with medication administration, allergies, and results (POL-04 4.8). End diversion and tell EMS, emergency management, staff, practices, members, students, and the community when services are restored (RC.CO).

## 10. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.11).
- File the after-action report in the emergency program records. An actual emergency that requires activating the emergency plan exempts a hospital from its next required full-scale community-based or facility-based functional exercise, and the response must be analyzed and documented (482.15(d)(2)(i)(B), (d)(2)(iii)).
- Update P01 (GR-01, GR-02, GR-03, GR-07, GR-11, HS-001, HS-002, HS-005, HS-011, HP-001, ED-004), the POA&M (POAM-005, POAM-007, POAM-009, POAM-012, POAM-013, POAM-023), the notification matrix, and this runbook.
- The College Qualified Individual includes the event and the response in the next written report to the board (16 CFR 314.4(i)).
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain all incident records for 6 years (POL-01 4.11).
