# Incident Response Runbook: Ransomware on Dispatch and Train Control Back-Office Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Transportation Systems |
| Incident type | Ransomware with data theft, entering through the shared integration platform (SYS-G5) and reaching the dispatch (CAD) and PTC back office servers of the Train Dispatching and PTC Back Office Platform (TDPB), with effects in all three divisions |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; Freight Railroad supplement; the Covered Railroads' Cybersecurity Incident Response Plan (CIRP, SSI, SD 1580-21-01E II.D) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel; rail operations decisions by the Director, Network Operations Center |
| Approved | 2026-09-10 by the Group CISO, the Group General Counsel, and the Chief Operating Officer, Freight Railroad |
| Last tested | Technical CIRP objectives tested 2026-02 (isolation, backups). **The multi-regulator notification matrix has not been exercised** (scenario gap 8); the first cross-division tabletop is due 2026-12-15 (POAM-008) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry (Day minus 9):** an attacker exploits a vulnerability in the managed file transfer component of SYS-G5, reads the platform's partner credentials (14 of them older than 1 year, P07 IA-05f.), and copies HR export files waiting in the transfer store (P04 finding 2).
- **Pivot (Day minus 9 to Day minus 1):** through the broad DMZ rule that lets SYS-G5 reach the TMS interface server (gap 1; P07 AC-04), the attacker lands in the industrial DMZ, harvests a cached corporate administrator credential, and uses the unreviewed one-way trust from the rail OT directory to the corporate directory (gap 4) to log on to CAD application servers and PTC back office management servers. It also finds an old copy of the CIP on a DMZ server.
- **Impact (Day 0, 02:10 local):** ransomware encrypts CAD application and reporting servers in DC-1 and, through the same credentials, the DC-2 hot standby; it encrypts the PTC back office management servers and the SYS-G5 cluster. Vital field logic, onboard PTC apparatus, and wayside interface units are not affected. An extortion note names the group and threatens to publish employee data and "railroad security plans."
- **Effects by division:** Freight Railroad: no CAD for 72 railroads and 11 CDS customers; PTC back office down on CR-11 to CR-14. Transload and Wholesale: no car orders or placements between terminals and the railroads; driver records in the stolen HR exports. Real Estate: the property system feed stops; its employees' records are in the stolen exports.
- **Forensic estimate at Day 4:** HR export files with personal information of about 52,000 current and former employees in 28 states (about 19,000 in Florida), including about 2,100 drivers' license numbers; one superseded CIP copy (SSI).

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC Director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead and TSA Cybersecurity Coordinator | Group CISO | Director, Rail OT Security | Out-of-band bridge |
| Rail operations (manual dispatch, PTC failure procedures) | Director, Network Operations Center | Chief Operating Officer, Freight Railroad | NOC radio and voice network |
| TSA Security Coordinator (1570.203, RSSM requests, SSI) | Vice President, Rail Security | Director, NOC | TSOC line; out-of-band bridge |
| PTC and FRA | PTC Program Director | Chief Safety Officer, Freight Railroad | Out-of-band bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division counsel | Out-of-band bridge |
| Terminal operations and hazmat | Vice President, Terminal Operations | Hazmat compliance manager, Transload and Wholesale | Division bridge |
| Federal contracts | Federal contracts compliance manager | Director, Security and Compliance (Transload and Wholesale) | Division bridge |
| Real Estate | Manager, Security and Compliance (Real Estate) | Director, Property Management | Division bridge |
| SEC materiality | Disclosure committee | Chief Financial Officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email, chat, and the SOC case system. Use the crisis line, managed mobile devices, and the rail radio network for operations. Printed binders at both NOCs hold contacts, this runbook, the notification matrix, the RSSM fallback procedure, and the manual dispatch forms.

## 2. Preparation checks (Identify / Protect)
- [x] Immutable backups of CAD and PTC databases and configurations in the provider B vault, with a separate backup identity, scanned when made and restored (CP-9; SD 1580-21-01E II.D.1.b; P07 satisfied)
- [x] Clean-room recovery account in provider B for rebuilding images before they return to DC-1 or DC-2
- [x] Manual dispatch forms and procedures at both NOCs; PTC failure procedures in the PTCSP and operating rules
- [x] RSSM fallback: printed car list every 4 hours and offline extract on a standby laptop (tested 2026-03 and 2026-06)
- [ ] SYS-G5 flow approved, inspected, and in the CIP (**gap until POAM-001 closes**)
- [ ] Directory trust removed or restricted (**gap until POAM-018 closes**)
- [ ] CTC and PTC logs in the SIEM with 1-year retention (**gap until POAM-003 closes**)
- [ ] Group notification matrix exercised, TSOC procedure for all 72 railroads (**gap until POAM-008 closes**)
- [ ] HR exports purged from SYS-G5 after delivery (**gap until POAM-019 closes**)
- [x] Forensic retainer through the insurer panel; CAD and PTC vendors' emergency contacts
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| EDR alert for encryption behavior on a CAD or PTC server, or CAD consoles lose the application | EDR; NOC | Declare Severity 1; open the bridge; NOC starts manual dispatch |
| PTC back office loses messaging with onboard units or partners | PTC monitoring; Amtrak, commuter, or Class I dispatchers | Treat as Severity 1 if any cyber indicator exists; PTC failure procedures |
| Unusual reads or transfers on SYS-G5, or logons from SYS-G5 into the DMZ | SIEM | Disable the accounts; start triage |
| Corporate administrator account used on OT servers | Directory logs; SIEM | Disable the account; review the trust |
| Extortion note or leak-site post naming the group | Email, threat intelligence, law enforcement | Declare Severity 1; preserve the message |

**Severity 1** (group scale, POL-03 4.2): confirmed encryption or exfiltration in a shared service, any compromise of a Critical Cyber System, or effects in more than one division.

**Record the identification time.** The CISA clock runs from when the group *identifies* a cybersecurity incident (SD 1580-21-01E II.C.2), and the definition includes events still under investigation (IV.C). The TSA clock under 1570.203 runs from *initial discovery*. In this scenario both are Day 0, 02:30, when the SOC confirmed encryption on a CAD server. The breach notice clocks under state law run later, from determination of a breach.

## 4. First hours (RS.MA, RS.MI): safety first
| Step | Who | Done when |
|---|---|---|
| 1. Stop new movement authorities from the CAD; switch every railroad and CDS customer to manual dispatch (paper track warrants by radio; manual block procedures in CTC territory). Hold trains that cannot be given authority | Director, NOC | All dispatchers working from paper; every train accounted for |
| 2. Apply PTC failure procedures on CR-11 to CR-14 (49 CFR 236.1029 restrictions) and tell Amtrak, the commuter operator, and Class I hosts by voice | PTC Program Director; Director, NOC | Partners acknowledge |
| 3. Isolate the NOC operations zone and the industrial DMZ from the corporate network at the DMZ firewalls; block all SYS-G5 routes (SD 1580/82-2022-01E III.D.4; SD 1580-21-01E II.D.1.c) | Director, Rail OT Security | Isolation rules confirmed |
| 4. Disable the compromised administrator and service accounts; remove the directory trust; revoke SYS-G5 partner credentials | Group identity director | Accounts disabled; trust removed |
| 5. Snapshot affected servers for forensics before rebuilding; place logs on legal hold | SOC; forensic firm | Evidence list signed |
| 6. Confirm the provider B vault and clean-room account are intact and unreachable from the compromised identities | Group CIO | Vault integrity report |
| 7. Activate the RSSM fallback: printed list and offline extract on the standby laptop at both NOCs | NOC on-duty manager | Ready to answer TSA within 30 minutes |
| 8. Stop SYS-G5-dependent work at terminals: car orders by phone and email; hazmat loading continues only where rack controls and shipping papers are unaffected | Vice President, Terminal Operations | Terminal managers confirm |
| 9. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 10. CISA report and TSOC call (section 7) | Group CISO; Vice President, Rail Security | Report confirmation numbers logged |
| 11. Brief the disclosure committee within 24 hours (POL-03 4.6) | Group General Counsel | Committee convened |

## 5. Analysis (RS.AN)
1. **Scope by system and by railroad.** Which Critical Cyber Systems were touched, for which of the 14 Covered Railroads, and whether any field device, onboard unit, or PTC key was reached. The PTC key management enclave must be checked before any PTC restart; if key compromise cannot be ruled out, revoke and reissue keys (49 CFR 236.1033(b)(3)).
2. **Integrity of movement data.** Before CAD returns, compare restored track data, bulletins, and speed restrictions against the paper records kept during manual dispatch and the field (CP-10(2)). A wrong bulletin is a safety risk, not just a data error.
3. **Data theft.** List the stolen HR export files and the people in them by state of residence; identify drivers' license numbers and any medical or certification data. These counts drive the state notices.
4. **SSI.** Confirm whether the stolen CIP copy is SSI; if so, inform TSA promptly (49 CFR 1520.9(c)).
5. **Covered telecommunications and Kaspersky checks.** If forensics finds covered equipment or software in any system, the FAR reports start (section 7).
6. **Root cause:** the SYS-G5 vulnerability, the broad DMZ rule, the stale credentials, and the directory trust. Feed these to P01 GR-01, GR-02, RR-002, and RR-006.

## 6. Containment and eradication (RS.MI)
1. Rebuild CAD and PTC back office servers from known-good images in the clean-room account; do not reuse encrypted hosts. The DC-2 standby is rebuilt too, because it shared the compromised credentials.
2. Reset every OT directory credential; keep the directory trust removed (accelerates POAM-018).
3. Rebuild SYS-G5 with current patches; rotate all partner credentials; purge stored HR exports (POAM-019).
4. Replace the broad DMZ rule with a single inspected flow (POAM-001).
5. Confirm with forensics that no persistence remains in the DMZ, the operations zone, SYS-G1, or the landing zone before reconnecting.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (29 rows).** Counsel approves every notice; TSA and CISA reports are SSI. The matrix has three layers:
1. **Rail regulators (TSA, CISA, FRA):** CISA report for the Covered Railroads, TSOC reports for every affected railroad, SSI release report, RSSM requests during the outage, and FRA reports only if their triggers are met.
2. **Group-level duties:** SEC materiality; state breach notices for employees and drivers in each state of residence, with Florida as the worked example; FAR reports only if covered equipment is found.
3. **Contracts:** passenger operators and Class I hosts, CDS customers, tenants, the insurer.

| When (from identification, Day 0 02:30) | Action | Owner |
|---|---|---|
| Day 0, first hour | Manual dispatch; PTC failure procedures; voice notice to Amtrak, the commuter operator, and Class I hosts | Director, NOC; PTC Program Director |
| Day 0, by 14:30 (within 12 hours) | TSOC call for all affected railroads (IC Surface-2025-01 recommendation) | Vice President, Rail Security |
| Day 0, by 14:30 | CDS customers told by phone; written notice follows within 24 hours | Director, Rail Technology Services |
| Day 1, by 02:30 (within 24 hours) | CISA report under SD 1580-21-01E naming CR-01 to CR-14 and stating it is made under the directive (also satisfies 1570.203 for them); TSOC report for the 58 other railroads (1570.203) | Group CISO; Vice President, Rail Security |
| Day 1 | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Within 24 hours of new information | Supplemental CISA reports (II.C.4.f) | Group CISO |
| Promptly after confirming the CIP copy was taken | SSI release report to TSA (1520.9(c)) | Vice President, Rail Security |
| Within 30 minutes of any TSA request | RSSM car location answer from the fallback | NOC on-duty manager |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 10 days of determining the breach | Florida third-party agent notices from corporate (and from any vendor involved) to the employing subsidiaries | Group General Counsel |
| Within 30 days of determining the breach | Florida individual notices; Department of Legal Affairs (500 or more Floridians); consumer reporting agencies (more than 1,000). Apply each other state's law the same way, planning to the shortest clock | Group General Counsel with outside counsel |
| Within 50 days of a permanent change | CIP amendment request for rebuilt or changed Critical Cyber Systems (SD 1580/82-2022-01E VI.B-D) | Vice President, Rail Cybersecurity |

**Plan to the shortest clock.** In this scenario the order is: operational notices, TSOC (12-hour recommendation), CISA and 1570.203 (24 hours), SEC (if material), Florida third-party agent notices, then state notices to individuals.

**Materiality factors for the disclosure committee:** days of manual dispatch and lost carloads across 72 railroads; effects on passenger service on hosted lines; terminal throughput; regulator attention (TSA, FRA); the number of people whose data was taken; recovery cost; and customer contracts. Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

**Ransom decision:** board safety, security, and risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove any notice duty when data was taken, and it does not restore trust in systems that issue movement authority; the group plans to rebuild either way.

## 8. Recovery (RC.RP, RC.CO)
Restore in the P05 recovery order:
1. Identity (SYS-G1) and break-glass access confirmed clean (BP-G01)
2. Network, data centers, and landing zones (BP-G03)
3. SOC visibility, including new CTC and PTC log forwarding (BP-G02)
4. CAD rebuilt from clean images; track data, bulletins, and speed restrictions verified against field records before the first electronic authority (BP-R01; RTO 2 hours is not achievable after a ransomware rebuild, so manual dispatch carries the load)
5. CTC office code servers (BP-R03)
6. PTC back office after key checks; partners told before PTC returns on host territory (BP-R02)
7. CDS customers (BP-R09), crossing and detector monitoring (BP-R07), crew calling (BP-R06)
8. SYS-G5 with the single inspected flow (BP-G04), then the TMS link and terminal car orders (BP-R05, BP-W01)

Tell dispatchers, partners, CDS customers, terminals, and employees when each service returns (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10).
- Update P01 (GR-01, GR-02, GR-03, RR-001, RR-002, RR-006), the POA&M (POAM-001, POAM-003, POAM-008, POAM-018, POAM-019), the notification matrix, the CIRP, and this runbook.
- File CIP amendment requests for permanent changes within 50 days.
- Consider the Reg S-K Item 106 description for the next Form 10-K.
- Retain incident records for at least 6 years (POL-01 4.13).
