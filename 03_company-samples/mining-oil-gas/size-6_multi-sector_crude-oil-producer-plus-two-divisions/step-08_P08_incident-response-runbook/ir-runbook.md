# Incident Response Runbook: Ransomware Spreading from Business IT toward Field SCADA

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Mining, Quarrying, and Oil and Gas Extraction |
| Incident type | Ransomware that starts in business IT, spreads through shared services toward the OT of all three divisions, encrypts the Mid-Continent legacy SCADA HMIs, and steals royalty owner data (double extortion) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response practices from NIST SP 800-82 Rev. 3 section 6.4 |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06), including the Power Generation CIP-003-9 incident response plan and the Crude Logistics emergency procedures under 49 CFR 195.402 |
| Runbook owner | Group CISO; OT response led by the Group OT Security Director; notifications owned by the Group General Counsel |
| Approved | 2026-09-17 by the Group CISO and the Group General Counsel |
| Last tested | SOC technical playbooks tested quarterly. **The multi-regulator notification matrix has not been exercised** (scenario gap 7); the first cross-division tabletop is due 2026-12-15 (POAM-010) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry (Day -9):** an attacker phishes a corporate finance analyst with an adversary-in-the-middle page, steals a session token, and signs in to the corporate virtual desktop pool.
- **Spread toward OT (Day -8 to Day -1):** from the virtual desktop the attacker can route to the five shared OT support jump servers (P07 AC-17 finding). PAM blocks sign-in, but one jump server carries a known exploited vulnerability from the OT backlog (POAM-004), which the attacker uses to gain a foothold. In parallel, the attacker finds the SYS-G6 historian connector secret in a data platform pipeline and uses it to **write** to historian brokers in all three OT DMZs (P07 AC-04 finding). From the Production OT DMZ the attacker reaches the Mid-Continent legacy SCADA (SYS-P5), which has no EDR and no SIEM feed.
- **Theft (Day -2):** the attacker copies monthly royalty owner exports from the finance file share: about 168,000 owners in all 50 states (about 19,000 in Florida), with names, taxpayer numbers, and bank accounts.
- **Impact (Day 0, a Saturday, 02:10):** ransomware runs on corporate file servers and some ERP application servers (EDR stops it on most hosts) and encrypts 14 HMIs and both SCADA servers of SYS-P5. A ransom note names the group and threatens to publish owner data.
- **OT reactions (Day 0):** the OT sensors at the PCC and GCC alert on new sessions from a jump server. The PCC and GCC shift leads **isolate their control rooms from corporate networks as a precaution**; control continues on their own OT networks. Mid-Continent controllers lose sight of about 2,900 wells; field crews start manual rounds and shut in remote wells.
- **Forensic picture at Day 5:** no commands were sent to field devices, plants, or pipeline equipment; the attacker wrote junk tags to historian brokers and reached the GCC OT DMZ landing host, but no evidence shows access to a BES Cyber System; owner data was taken.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| OT technical lead | Group OT Security Director | OT security engineering lead | OT bridge |
| Production operations decisions | IOC shift lead; Mid-Continent operations manager | Production Vice President of Operations Technology | IOC console phone; radio |
| Power Generation operations decisions | GCC shift lead; plant shift supervisors | Vice President of Generation (CIP Senior Manager) | GCC phone; P1 control room |
| Crude Logistics operations decisions | PCC shift lead | Pipeline Control Center Manager | PCC phone; backup PCC |
| Notifications and legal | Group General Counsel with outside breach counsel | Division counsel | Out-of-band bridge |
| Regulator notice owners | Production HSE director (EPA); Pipeline Compliance Manager (PHMSA); CIP Senior Manager and NERC Compliance Manager (E-ISAC, EOP-004); Fleet Safety Director (hazmat) | Division compliance leads | Division bridges |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline binders |

**Out-of-band first.** Assume the attacker can read corporate email and chat. Use the crisis line and managed mobile devices. Printed binders at the IOC, BCC, GCC, PCC, and backup PCC hold contacts, this runbook, and the notification matrix (POL-03 4.6).

**Operations decide on operations.** Only the control room shift lead may isolate a control room, switch to manual operation, or shut in or shut down (POL-03 4.3). The SOC and the OT desk advise. Safety and environmental protection come before evidence collection.

## 2. Preparation checks (Identify / Protect)
- [x] Immutable backups of cloud workloads and SCADA server images in the provider B vault (CP-9; P07 satisfied)
- [x] 24x7 SOC with an OT desk and passive OT sensors at the IOC, BCC, PCC, and GCC (SI-4)
- [x] Hardwired shutdowns and relief systems that act without SCADA at central facilities, compressor and pump stations, and plants
- [x] Local logons and break-glass accounts at every control room, so control works without SYS-G1
- [ ] Jump servers reachable only from privileged access workstations and split by division (**gap until POAM-002 closes**)
- [ ] Historian connector read-only and outbound only (**gap until POAM-001 closes**)
- [ ] SYS-P5 with EDR, SIEM logging, offline backups, and integrator access through PAM (**gap until POAM-012 closes**)
- [ ] Notification matrix exercised, with offline copies at all five control centers (**gap until POAM-010 closes**)
- [ ] Royalty owner data kept inside SYS-P3, not on file shares (**gap until POAM-023 closes**)
- [x] Forensic retainer with OT capability and the insurer's panel confirmed

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Encryption, mass file changes, or a ransom note on any host | EDR, file server alerts | Declare Severity 1; open the bridge |
| New session into an OT DMZ from a jump server or connector outside an approved PAM session | OT sensors at the IOC, BCC, PCC, GCC | Call the affected shift leads; consider isolation |
| Writes to a historian broker by the SYS-G6 service account | Historian audit log; SIEM | Disable the account; treat as an OT intrusion |
| Loss of view at a control room (HMIs encrypted or frozen) | Control room staff | Shift lead starts manual operations; call the OT desk |
| Extortion email or leak-site post naming the group | Email, threat intelligence, law enforcement | Declare Severity 1; preserve the message |

**Severity 1** (group scale, POL-03 4.2): confirmed encryption or exfiltration in a shared service, or any unauthorized activity in an OT network.

**Record each clock's start (POL-03 4.4).** Each regulator uses a different trigger: confirmed discovery of a release (PHMSA), knowledge of a discharge (EPA), determination of a Reportable Cyber Security Incident (NERC), the materiality determination (SEC), and determination of a breach (state laws, Florida 501.171). The incident log records each one separately; nothing is planned from a later date than the rule allows.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Each shift lead confirms safe state: hardwired shutdowns healthy, alarms visible or rounds started, no abnormal pressures | IOC, Mid-Continent, PCC, GCC shift leads | Safe-state checklist signed |
| 2. Isolate control rooms from corporate networks where the shift lead decides it is safer (PCC and GCC did so in the scenario) | Shift leads with the OT desk | Isolation logged with time |
| 3. Mid-Continent: manual rounds; shut in remote wells; gauging rounds at batteries that use the SPCC high-level alarm option, within 4 hours | Mid-Continent operations manager; Production HSE director | Rounds staffed; shut-in list recorded |
| 4. Block all jump server and historian connector paths into every OT DMZ at the OT DMZ firewalls; disable the SYS-G6 service account | Group OT Security Director | Rules applied; account disabled |
| 5. Revoke the analyst's sessions; disable the compromised accounts; force reset for the finance group | Group identity director | Sessions revoked |
| 6. Snapshot affected IT hosts and image one encrypted SYS-P5 HMI for forensics before rebuilding; put logs on legal hold | SOC; forensic firm | Evidence list signed |
| 7. Confirm the provider B vault and SCADA image backups are intact and unreachable from compromised identities | Group cloud platform director | Vault integrity report |
| 8. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 9. Tell the Balancing Authorities and market operators that the GCC is operating isolated and plants are following dispatch | GCC shift lead | Calls logged |
| 10. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.7) | Group CISO | Committee convened |

## 5. Analysis (RS.AN)
1. **OT first.** For each division, confirm with controller logs and OT sensor data whether any command reached field devices, pipeline equipment, or plant controls, and whether any historian value used by operators was altered. Controllers compare key values with field readings before trusting displays.
2. **Power Generation determination.** The CIP Senior Manager decides whether the incident compromised or disrupted a low impact BES Cyber System at P1, P2, P3, or the GCC (the NERC Glossary test for a Reportable Cyber Security Incident). In the scenario the attacker reached the GCC OT DMZ landing host only, and the precautionary isolation did not disrupt any BES Cyber System, so the determination is "not reportable"; the reasoning is documented, and the E-ISAC is informed voluntarily. If evidence changes, the determination is redone and the E-ISAC notified.
3. **EOP-004 check.** No GO or GOP event type was met: there was no damage to a Facility and no physical threat. Loss of monitoring or control at a BES control center is a reporting event only for RC, BA, and TOP entities.
4. **Releases.** Confirm with the PCC and HSE whether any release occurred during the loss of view. A release would start the PHMSA one-hour clock (trunk line and regulated rural gathering lines) and the EPA immediate notice if oil reached water. None occurred in the scenario.
5. **Personal data.** Identify which exports were taken, the owners in each, and each owner's state of residence (P03 GG-04). These counts drive the state notices.
6. **Root cause:** the phishing path, the virtual desktop route to the jump servers (POAM-002), the unpatched jump server (POAM-004), the writable historian connector (POAM-001), the unmonitored SYS-P5 (POAM-012), and the owner exports on a file share (POAM-023). Feed these to P01 GR-01, GR-02, GR-03, GR-10, and PD-002.

## 6. Containment and eradication (RS.MI)
1. Keep the PCC and GCC isolated until the reconnection criteria in step 8.4 are met.
2. Rebuild all five jump servers from known-good images into the division split design (accelerates POAM-002). Patch before any reconnection.
3. Replace the historian connector with an outbound, read-only push before re-enabling any historian replication (accelerates POAM-001). Clean junk tags from the historian brokers.
4. Rebuild SYS-P5 SCADA servers and HMIs from vendor media and the last verified configuration, not from the local backup device that sat on the same network. Disable the integrator's always-on path permanently.
5. Rebuild encrypted corporate servers from infrastructure code and the vault.
6. Confirm with forensics that no persistence remains in SYS-G1, the jump servers, the data platform, or any OT DMZ before reconnecting.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (32 rows; 25 apply to this group, 7 are recorded as not applicable, and 5 rows that depend on state or market rules or contracts are marked unverified and must be confirmed before use).** Counsel approves every notice, except safety and environmental notices that a rule requires within hours: the named owner makes those first and then reports to counsel (POL-03 4.5).

| When | Action | Owner |
|---|---|---|
| Within 1 hour of confirmed discovery of a reportable release (only if one occurs) | PHMSA telephonic notice to the National Response Center (trunk line, regulated rural gathering lines); update within 48 hours | Pipeline Compliance Manager |
| Immediately on knowledge of a harmful oil discharge (only if one occurs) | EPA notice to the National Response Center (40 CFR 110.6) | Production HSE director or the division where it occurs |
| Day 0 | Insurer, counsel, forensics; voluntary report to the FBI or IC3 and CISA; Balancing Authorities and market operators informed of GCC status | Group Chief Risk Officer; Group CISO; GCC shift lead |
| Day 0 to 1 | CIP Senior Manager's Reportable Cyber Security Incident determination; E-ISAC notified after a "reportable" determination (company target within 1 hour of it) | CIP Senior Manager; NERC Compliance Manager |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 30 days of the breach determination | Florida individual notices and the Department of Legal Affairs notice (about 19,000 Floridians, so 500 or more); consumer reporting agencies (more than 1,000). Apply each other state's law the same way for owners in the other 49 states | Group General Counsel with Production Accounting |
| Within 30 days of discovery (only if an accident or hazmat incident occurred) | PHMSA Form 7000-1; DOT Form F 5800.1 | Pipeline Compliance Manager; Fleet Safety Director |

**Plan to the shortest clock.** Safety and environmental notices come first and do not wait for the bridge. The NERC determination comes next because it depends on facts the OT desk is already gathering. The SEC clock starts only at the materiality determination, which must be made without unreasonable delay. State notices follow the state with the shortest deadline among the owners' states of residence, with Florida's 30 days as the worked example.

**Materiality factors for the disclosure committee:** lost production at the Mid-Continent fields (about 22% of production; about $8.5 million per day at the BIA revenue rate, P05), recovery cost, regulatory exposure (state attorneys general, the NERC Regional Entity, PHMSA and the state pipeline agency), the number of royalty owners affected in all 50 states, and reputational effects with shippers and partners. Materiality is decided without unreasonable delay; the 4-business-day clock starts at the determination, not at discovery.

**Ransom decision:** board risk committee, counsel, the insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not remove any notice duty when data was taken, and decryption tools are not used on OT hosts; they are rebuilt.

## 8. Recovery (RC.RP, RC.CO)
Recovery follows the P05 BIA order, adjusted for this incident:
1. SYS-G1 identity and break-glass access confirmed clean (BP-G01)
2. Landing zones, WAN, and site connectivity (BP-G03), without OT paths
3. SOC visibility, including new sensors at the SYS-P5 field offices (BP-G02)
4. **Reconnection criteria for each isolated control room:** paths into its OT DMZ are rebuilt or removed; the OT desk confirms no attacker activity for 72 hours; the shift lead agrees; controllers verify key values against field readings (POL-03 4.10). The PCC and GCC reconnect first because they kept control
5. Safety and environmental alarming and field control for the Mid-Continent fields (BP-PD02, BP-PD06), with SYS-P5 rebuilt clean; wells brought back in a controlled order
6. Historian replication through the new outbound path only
7. Business systems: dispatch and run ticket links (BP-ML04), field data capture (BP-PD04), market systems (BP-PG03), financial close (BP-G06), then hydrocarbon accounting with owner payments on the normal cycle where possible (BP-PD05)

Tell division staff, shippers, market operators, and royalty owners when services are restored (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.12). Power Generation updates its CIP-003-9 plan if needed within 180 days (Attachment 1 Section 4.6).
- Update P01 (GR-01, GR-02, GR-03, GR-10, PD-001, PD-002, PG-004, ML-001), the POA&M (POAM-001, 002, 004, 010, 012, 023), the notification matrix, and this runbook.
- Crude Logistics reviews whether control room actions during the loss of corporate connectivity need changes to its control room procedures (195.446(g) applies to reportable accidents; the review is done here as good practice).
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain all incident records for at least 6 years (POL-01 4.12).
