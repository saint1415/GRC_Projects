# Incident Response Runbook: Ransomware Disrupting Production of Grid Equipment

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Critical Manufacturing (focus division: Transformer Manufacturing) |
| Incident type | Ransomware with data theft that starts at the acquired plant (P8), spreads through shared IT, stops work order release to all 8 plants, encrypts the TMU firmware build servers, and probes the Electric Utility's TCC |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT steps follow NIST SP 800-82 Rev. 3 |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06). The Electric Utility's CIP-008-6 plan governs its own determinations and reports |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel; reliability reports owned by the Electric Utility NERC compliance director |
| Approved | 2026-09-15 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The multi-party notification matrix has not been exercised** (scenario gap 7); the first cross-division tabletop is due 2026-12-15 (POAM-005) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative. It is set in September, during hurricane season.
- **Entry (Day -9):** an attacker logs in to one of the 4 always-on OEM cellular routers at P8 with its shared vendor password (P07 AC-17 finding) and reaches the flat P8 network.
- **Spread (Day -9 to Day 0):** from P8 the attacker takes over a legacy domain administrator account and crosses the two-way trust into the corporate domain (GR-07). On a GEPS integration hub server it reads one of the 6 static hub keys from a configuration file (P07 IA-5 finding).
- **Theft (Day -3 to Day -1):** about 210 GB is copied from legacy group file servers: HR exports with Social Security numbers (about 31,000 current and former employees and applicants, about 14,000 in Florida), and Grid Engineering closed-project archives for about 120 clients, including client BCSI and CEII for 17 clients with CIP flow-down terms and 2021 TCC design documents from a closed affiliate project.
- **Impact (Day 0, 02:10):** the attacker encrypts the GEPS application servers and integration hub in provider A, group file servers, the P8 MES server and 23 P8 HMIs and engineering workstations, and the TMU firmware build servers in the group data center. From a compromised corporate server it scans and tries to log in to the TCC Electronic Access Point, which blocks it. An extortion note names the company and threatens to publish the files.
- **What keeps running:** plants P1 to P7 keep producing from their MES queues (about 48 hours of released work orders); the Electric Utility's TCC and DCC run normally on their own networks; the FMS and the Grid Engineering project platform in provider B are not encrypted; the immutable backup vault is intact.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| OT response | Group OT security director with the Director of OT engineering | OT-capable firm from the insurer's panel | Plant bridge |
| Plant safety and production | VP manufacturing operations; each plant manager | Plant shift supervisors | Plant bridge |
| GEPS recovery | Group ERP platform director | Group cloud platform director | SOC bridge |
| Product security and utility notices | Chief product security officer (PSIRT) | Director of reliability engineering | Out-of-band bridge |
| Electric Utility determinations and reports | Electric Utility NERC compliance director | CIP Senior Manager | Utility reporting desk line |
| Grid Engineering client notices | Grid Engineering contracts director | Grid Engineering security and compliance lead | Out-of-band bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division counsel | Out-of-band bridge |
| State breach decisions | Group Chief Privacy Officer | Group HR director | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Federal contracts | Director of federal contracts | Grid Engineering federal programs manager | Out-of-band bridge |
| Law enforcement | FBI field office; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email, chat, and file shares. Use the crisis line and managed mobile devices. A printed binder at each plant, the TCC, the storm desk, and the group command center holds contacts, this runbook, the notification matrix, the customer security terms register, and plant shutdown procedures.

## 2. Preparation checks (Identify / Protect)
- [x] Immutable backups in provider B with a separate backup identity (CP-9; P07 satisfied)
- [x] 24x7 SOC with EDR on IT endpoints and servers; OT sensors at P1 to P7 and the TCC (SI-4)
- [x] OT DMZs and a central OEM gateway at P1 to P7; manual shutdown procedures at every plant
- [x] The Electric Utility's CIP-008-6 plan and DOE-417 procedure at the TCC; precautionary Normal Report rule agreed (P03 EU-G47)
- [ ] P8 isolation switch and OT DMZ (**gap until POAM-007 closes**); OEM cellular routers removed (**gap until POAM-008 closes**)
- [ ] P8 legacy domain trust removed (**gap until POAM-020 closes**)
- [ ] One hub account per plant with vaulted keys (**gap until POAM-002 closes**)
- [ ] GEPS scheduling recovery runbook and tested restore of APS and the hub (**gap until POAM-004 closes**)
- [ ] Firmware signing key in a hardware security module (**gap until POAM-010 closes**)
- [ ] Notification matrix adopted and exercised; Grid Engineering client terms register (**gap until POAM-005 and POAM-012 close**)
- [x] Forensic and OT incident response retainers through the insurer's panel; disclosure committee charter covers cybersecurity

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Encryption on GEPS, file servers, or build servers; ransom note | EDR, cloud audit logs, file server alerts | Declare Severity 1; open the bridge |
| Work order release to the plants fails or the hub sends unexpected messages | Integration hub monitoring; plant MES alarms; planners | Stop the hub; check every plant's MES queue |
| HMIs or engineering workstations at any plant show a ransom screen or stop responding | Plant operators | Plant manager puts affected lines into a safe state; call the OT bridge |
| Scans or failed logins at a TCC Electronic Access Point from a corporate address | TCC EAP sensors to the SOC | Tell the utility reporting desk at once (POL-03 4.5) |
| Large outbound transfers from file servers | SIEM, firewall | Block at the hub; preserve logs |
| Extortion email or leak-site post naming any division | Email, threat intelligence, law enforcement | Declare Severity 1; preserve the message |

**Severity 1** (group scale, POL-03 4.2): confirmed encryption in a shared service, any OT impact, or data from more than one division involved.

**Record the clock-start facts for each duty** in the incident log: when the SOC confirmed the incident, when the PSIRT confirmed that it related to supplied products, when Grid Engineering identified affected client data, when the utility determined an attempt to compromise, and when a breach of personal information was determined. The notification matrix says which fact starts each clock.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Safety first.** Plant managers put any line whose HMIs are encrypted or untrusted into a safe state using the manual procedures (drying ovens, vacuum oil processing, test labs). Nobody restarts a process from an untrusted HMI | Plant managers; VP manufacturing operations | Every plant reports a safe state or normal operation |
| 2. Stop the GEPS integration hub and cut every hub-to-plant connection at the OT DMZs (P1 to P7) and the P8 firewall. Plants P1 to P7 keep running from their MES queues | Group ERP platform director; Director of OT engineering | Hub stopped; DMZ rules applied |
| 3. Cut P8 from the WAN and power off the 4 cellular routers | Director of OT engineering; P8 plant manager | P8 isolated |
| 4. Disable the stolen hub key and the compromised domain accounts; break the P8 domain trust; reset the krbtgt and all privileged credentials in order | Group identity director | Accounts disabled; trust removed |
| 5. The Electric Utility decides whether to isolate its networks from group IT. In the exercise it closed the corporate links to the TCC and DCC at 03:05, which triggers the precautionary DOE-417 Normal Report rule | Electric Utility system operations director; NERC compliance director | Isolation logged with the time |
| 6. Snapshot affected servers for forensics before rebuilding; collect OT evidence only with plant approval; put logs on legal hold | SOC; forensic and OT firms | Evidence list signed |
| 7. Confirm the provider B vault and GEPS replica are intact and unreachable from the compromised identities | Group cloud platform director | Vault integrity report |
| 8. Call the cyber insurer; engage breach counsel and the forensic and OT firms through the panel | Group Chief Risk Officer | Claim number issued |
| 9. **PSIRT decision on the signing key.** The build servers held the firmware signing key, so treat it as stolen: freeze all firmware releases, revoke the key, and decide the utility notice (matrix rows 1 to 5) | Chief product security officer | Decision recorded with the time |
| 10. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.6) | Group CISO | Committee convened |

## 5. Analysis (RS.AN)
1. **Path and scope.** Rebuild the attacker's path: cellular router, P8 network, legacy domain, trust, corporate domain, hub key, encryption. Confirm whether any plant controller (PLC) program was changed, not just HMIs. Compare P1 to P7 controller programs against their last backups before any restart.
2. **Firmware integrity.** List every firmware release signed since the earliest attacker activity (Day -9). Compare each release with its build record and published hash. Tell utilities which releases are known-good (addendum sec. 5).
3. **Data taken.** From file server and firewall logs, list the folders copied. Map HR files to individuals by state of residence. Map Grid Engineering archives to clients, and flag client BCSI, CEII, and affiliate files.
4. **The TCC probe.** The Electric Utility applies its CIP-008-6 criteria. In the exercise it determined an **attempt to compromise** its EACMS (not a Reportable Cyber Security Incident), and separately reviewed whether the 2021 TCC design documents in the stolen archives call for configuration changes.
5. **Utility impact of the product side.** Ask the 140 addendum utilities and the affiliate whether any TMU received firmware signed after Day -9. The TMU is under utility control at customer sites, so only the utility can confirm.
6. **Root cause** feeds P01 GR-01, GR-02, GR-04, GR-07, and MF-001.

## 6. Containment and eradication (RS.MI)
1. Remove the 4 cellular routers permanently; move the OEMs to the central gateway (accelerates POAM-008).
2. Keep P8 isolated until its MES and HMIs are rebuilt behind a temporary firewall zone (interim step toward POAM-007).
3. Rebuild the integration hub with one service account per plant and keys in the secret store before reconnecting any plant (accelerates POAM-002).
4. Rebuild the build servers in an isolated network; sign new releases only with a new key held in a hardware security module (accelerates POAM-010).
5. Confirm with forensics that no persistence remains in SYS-G1, the landing zones, the P8 domain, or any plant OT DMZ before reconnecting.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (34 rows).** The matrix has four layers:
1. **Customers and clients, by contract:** 140 utility addenda (24 or 48 hours), the affiliated Electric Utility as a vendor customer, about 120 Grid Engineering clients (24 to 72 hours for the 17 with CIP flow-down terms), customers whose deliveries slip, and federal contracting officers for delayed deliveries.
2. **The Electric Utility's reliability reports:** CIP-008-6 R4 attempt notice, DOE-417 Normal Report (criterion 11, precautionary) and criterion 14, the DOE-417 final report, and EOP-004-4 if a threshold is met. The reporting desk files these **without waiting** for group legal review (POL-03 4.5).
3. **People whose data was taken:** state breach notices to individuals, regulators, and consumer reporting agencies, with Florida as the worked example, and the third-party agent notice from corporate to each employing subsidiary.
4. **Investors and others:** the SEC materiality decision, OFAC, law enforcement and CISA, and the insurer.

| When (from Day 0, 02:10) | Action | Owner |
|---|---|---|
| Day 0, 03:05 | Utility isolates group IT from the TCC and DCC; Normal Report clock (6 hours) starts | Electric Utility |
| Day 0, by 09:05 | DOE-417 Normal Report (criterion 11, precautionary), with criterion 14 checked once the attempt is determined | Electric Utility NERC compliance director |
| Day 0 | Insurer, counsel, forensics engaged; voluntary report to the FBI and CISA; corporate tells each employing subsidiary on the bridge (third-party agent duty) | Group Chief Risk Officer; Group CISO; Group General Counsel |
| Day 0, 11:00 | PSIRT confirms the incident relates to supplied products (signing key exposure); addendum clocks start | Chief product security officer |
| By end of Day 1 | CIP-008-6 attempt notice to the E-ISAC and CISA (the utility determined the attempt on Day 0) | Electric Utility NERC compliance director |
| Within 24 hours of Day 0, 11:00 | Notices to all 140 addendum utilities (the 45 with 24-hour terms first) and to the affiliate utility, with a firmware hold and the known-good release list | PSIRT |
| Within 24 hours of identification | Grid Engineering notices to the clients with 24-hour terms; 48- and 72-hour clients follow in order from the register | Grid Engineering contracts director |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Within 72 hours of Day 0 | DOE-417 final report | Electric Utility |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 7 calendar days of new information | CIP-008-6 updates to the E-ISAC and CISA | Electric Utility |
| Within 30 days of the breach determination | Florida individual notices and the Department of Legal Affairs notice (500 or more Floridians); consumer reporting agencies (more than 1,000). Apply each other state's law the same way | Group Chief Privacy Officer |

**Plan to the shortest clock.** In this scenario the order is: the utility's DOE-417 Normal Report (6 hours), the 24-hour addendum and client notices, the CIP-008-6 attempt notice and DOE-417 criterion 14 (end of the next calendar day), the 48- and 72-hour notices, the DOE-417 final report (72 hours), the Form 8-K (4 business days after the determination, if material), then state breach notices (30 days in Florida).

**Not triggered, recorded so the decision is visible:** DFARS 252.204-7012 (no DoD contracts); CIRCIA (proposed only; the voluntary CISA report is made instead); FAR 52.204-25, 52.204-23, and 52.204-30 reports (only if covered equipment or articles are found during the rebuild); FMS subscriber notices (the FMS was not affected); CIP-008-6 Reportable Cyber Security Incident and DOE-417 Emergency Alert (no compromise of the TCC and no interruption of electrical system operations).

**Materiality factors for the disclosure committee:** lost output at all 8 plants (about $26.3 million a day once the MES buffers run out) and late storm-season deliveries; the possible signing key theft and its effect on about 700 utility customers' trust in the TMU; regulatory exposure across divisions (SERC, state attorneys general); data theft and extortion; and cost of recovery. Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

**Ransom decision:** board risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove any notice duty when data was taken, and does not make the stolen signing key safe again.

## 8. Recovery (RC.RP, RC.CO)
Restore in the BIA order (P05 section 7). The Electric Utility recovers on its own track and reconnects to group IT only when its CIP Senior Manager approves.
1. **Identity, landing zones, and SOC visibility** confirmed clean (BP-G01, BP-G03, BP-G02; 1 to 4 hours).
2. **Plant process control** (BP-MF04): verify controller programs at every plant against backups; restart lines with plant engineering sign-off. P8 restarts last, from rebuilt HMIs and verified programs (RTO 12 hours for P1 to P7; P8 longer until POAM-023 closes).
3. **GEPS** (BP-G04, RTO 12 hours) from the provider B replica: ERP first, then APS and the integration hub. Because restoring APS and the hub has never been tested (POAM-004), plan for longer than the 24-hour scheduling RTO (BP-MF02) and start paper travelers at P1 to P7 if the MES buffers will run out.
4. **Re-synchronize each plant MES** against the restored schedule before releasing new work orders; reconnect plants one at a time.
5. **Storm orders and spare release** (BP-MF07, RTO 8 hours) from the restored GEPS, with the Electric Utility storm desk on the bridge.
6. **Testing, shipping, order entry, export screening** (BP-MF05, MF06, MF01). Use the manual export screening fallback until the GEPS is verified.
7. **Firmware** (BP-MF08): new key in the HSM, rebuilt releases, new hashes published to utilities.
8. **File services** rebuilt without the legacy HR exports and closed-project archives, which are purged or moved per POL-04 4.10.

Tell customers, the affiliate, and plant staff when production and deliveries resume (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.12).
- Update P01 (GR-01, GR-02, GR-03, GR-04, GR-07, MF-001, MF-002, MF-005), the POA&M, the notification matrix, the customer security terms register, and this runbook.
- The Electric Utility reviews its CIP-008-6 plan and records the response as a plan test if it qualifies.
- Consider the Reg S-K Item 106 description for the next annual report.
- Keep all incident records for at least the group retention period (POL-01 4.11), and longer for the Electric Utility's CIP evidence.
