# Incident Response Runbook: CAD Outage from Ransomware Across Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Emergency Services |
| Incident type | Ransomware takes down the computer-aided dispatch (CAD) system at all 4 communications centers, with data theft from the CAD database and the revenue cycle file transfer servers (double extortion). Registry scenario: computer-aided dispatch outage from ransomware |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; dispatch continuity owned by the BDS vice president of communications operations; notifications owned by the Group General Counsel |
| Approved | 2026-09-16 by the Group CISO, the Group General Counsel, and the BDS vice president of communications operations |
| Last tested | Technical playbooks tested quarterly. **The multi-party notification matrix and a multi-day manual dispatch have not been exercised** (scenario gaps 1 and 7); the first cross-division tabletop is due 2026-12-15 (POAM-004) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** an attacker buys a CAD vendor engineer's stolen credentials and connects over the vendor's persistent VPN into the legacy cloud account with one of the 6 standing CAD administrator accounts (P01 GR-05; P07 AC-06(05)).
- **Dwell:** over 9 days the attacker moves across the shared management subnet (P07 SC-07a.[04]), copies the CAD database, and copies 90 days of claim files from the revenue cycle file transfer servers.
- **Impact:** at 02:10 on Day 0 the attacker encrypts the CAD servers and the integration engine. All 4 communications centers lose the CAD at once. An extortion note names the group, its "ambulance customers," and "billing clients."
- **Forensic estimate at Day 5:** CAD records for about 8.9 million Ambulance Services patients in 7 states (about 4.1 million Florida residents) and about 1.2 million patients of 9 client agencies in 4 states (about 600,000 in Florida); claim files for about 410,000 Urgent Care patients (about 190,000 in Florida) and about 340,000 patients of 23 billing clients in 9 states (about 45,000 in Florida). The premise notes received from one county were in the copied database (P03 BD-G28).

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander (technical) | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Dispatch continuity commander | BDS vice president of communications operations | Senior center supervisor on duty | Center supervisor radio talkgroup and crisis line |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC and cloud platform teams | Forensic firm on retainer (through the insurer's panel) | SOC bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division counsel | Out-of-band bridge |
| Ambulance Services breach decisions | Ambulance Services Privacy Officer | Ambulance Services HIPAA Security Officer | Division bridge |
| Urgent Care breach decisions | Urgent Care Privacy Officer | Urgent Care HIPAA Security Officer | Division bridge |
| Client notices (dispatch and billing) | BDS security and compliance lead | BDS client services director | Division bridge |
| County notices | Ambulance Services contract compliance director | Regional operations directors | Phone from the county notice register |
| Clinical oversight | Ambulance Services chief medical officer | State medical directors | Division bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email and chat. Use the crisis line, managed mobile devices, and radio. The printed binder at each communications center holds this runbook, the manual dispatch procedure, the county and client call trees, and the notification matrix.

## 2. Preparation checks (Identify / Protect)
- [x] Manual dispatch binders, paper incident cards, and status boards at all 4 centers (CP-2; P07 satisfied for content, not for duration)
- [x] County P25 radio at every console and in every ambulance
- [x] Immutable hourly copies of the CAD database in the provider B vault, with a separate backup identity (CP-9; P07 satisfied)
- [x] 24x7 SOC with EDR on CAD and file transfer servers (SI-3, SI-4)
- [ ] CAD standby in provider B (**gap until POAM-013 closes**; until then recovery means rebuilding in provider A)
- [ ] CAD vendor access only through PAM (**gap until POAM-003 closes**)
- [ ] CAD and billing servers separated (**gap until POAM-012 closes**)
- [ ] Notification matrix with the client and county notice register, exercised (**gap until POAM-004 closes**)
- [x] Forensic retainer and insurer panel confirmed
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| CAD consoles freeze or show errors at more than one center | Telecommunicators; center supervisors | Supervisors switch to manual dispatch at once (POL-03 4.3) and call the SOC |
| EDR alert for mass encryption on CAD or integration servers | EDR, SIEM | Declare Severity 1; open the bridge |
| Vendor account sign-in at an unusual time or from a new location | VPN and CAD logs (once in the SIEM) | Disable the account; start triage |
| Extortion note or leak-site post naming the group, its clients, or counties | Email, threat intelligence, law enforcement | Declare Severity 1; preserve the message |
| A client agency or county reports CAD-to-CAD failures | Client duty officers; PSAP supervisors | Treat as a possible CAD incident; confirm with the SOC |

**Severity 1** (group scale, POL-03 4.2): loss of the CAD at any center, confirmed encryption or exfiltration in a shared service, or data of more than one division or any client involved.

**Record the discovery date for each entity.** For a covered entity, a breach is discovered on the first day it is known, or by reasonable diligence would have been known, to any workforce member or agent (164.404(a)(2)). For a business associate, to any employee or agent (164.410(a)(2)). Because the group SOC is corporate, **this runbook conservatively treats the day the SOC knew as the discovery date for Ambulance Services, Urgent Care, and BDS.** Counsel may refine this, but no clock is planned from a later date.

## 4. First hour: keep dispatching (RS.MA, RS.MI, RC.RP)
Dispatch continuity runs in parallel with the technical response. Neither waits for the other.

| Step | Who | Done when |
|---|---|---|
| 1. Declare manual dispatch at all 4 centers; start paper incident cards and status boards; announce on radio | BDS vice president of communications operations | Every center confirms manual mode |
| 2. Within 15 minutes: call each of the 14 client agency duty officers and each affected county PSAP supervisor from the binder call trees | Center supervisors; Ambulance contract compliance director | Calls logged with time and name |
| 3. Ask PSAPs to voice-transfer EMS calls and to stop CAD-to-CAD sends; ask neighboring providers to stand by for mutual aid | Center supervisors | PSAPs confirm |
| 4. Crews report status and location by radio; supervisors post units by map; ePCR tablets keep working offline | Ambulance Services regional operations | Status board matches the radio roster each hour |
| 5. Disable all CAD vendor accounts and the vendor VPN; revoke CAD administrator sessions | Group identity director | VPN down; accounts disabled |
| 6. Isolate the legacy account from the hub and the internet; keep the ePCR, EHR, and revenue cycle platform running | Group network director | Peering removed; egress blocked |
| 7. Snapshot affected servers and storage for forensics before rebuilding; place logs on legal hold | SOC; forensic firm | Evidence list signed |
| 8. Confirm the provider B vault copies are intact and unreachable from compromised identities | Group cloud platform director | Vault integrity report |
| 9. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 10. Tell the division privacy officers and the BDS lead on the bridge (this starts BDS's and corporate's internal 164.410 notices) | Incident commander | Each acknowledges |
| 11. Escalate to the disclosure committee within 24 hours (POL-03 4.7) | Group CISO | Committee convened |

**Clinical safety watch.** The Ambulance chief medical officer reviews response times every 4 hours while in manual mode. If manual mode passes the 2-hour MTD at a center (P05 BP-BD01), that center asks its counties to route new calls to mutual-aid providers, and the other centers take overflow where radio coverage allows.

## 5. Analysis (RS.AN)
1. **Scope by system and by owner.** Use CAD database audit records (AU-3) and storage access logs to list what was read and copied. Map CAD records to Ambulance Services or to each client agency partition, and claim files to Urgent Care, Ambulance Services, or each billing client.
2. **Individuals by state.** For each covered entity and each client, count affected individuals by state of residence. These drive HHS, media, state, and consumer reporting agency notices.
3. **Overlap.** People transported by the Ambulance division and treated at an Urgent Care clinic appear in both populations. Each covered entity still owes its own notice; coordinated letters must name both.
4. **Premise notes.** Tell the county at once that the copied database included the premise notes it sent. If its CJIS Systems Agency determines they are CJI, follow the CJIS row in the matrix.
5. **Four-factor assessment (164.402)** for each covered entity: nature and extent of the PHI, who obtained it, whether it was actually acquired or viewed, and the extent the risk has been mitigated. With confirmed exfiltration by a criminal group, expect a breach finding.
6. **Integrity of dispatch data.** Compare the restored CAD data with paper incident cards for the outage period before it is used for county response-time reports (P05 BP-AM07).
7. **Root cause:** the vendor VPN and standing accounts, the shared management subnet, and the lack of east-west monitoring. Feed these to P01 GR-02 and GR-05.

## 6. Containment and eradication (RS.MI)
1. Rotate every credential in the legacy account and remove all local cloud users.
2. Rebuild CAD and integration servers from clean images in a **new landing-zone account**, not the legacy account (accelerates POAM-012).
3. Restore vendor access only through PAM with named accounts (accelerates POAM-003).
4. Rebuild the file transfer servers in a separate BDS account; purge claim files older than 14 days (POL-04 4.8).
5. Confirm with forensics that no persistence remains in SYS-G1, the landing zone, or division accounts before reconnecting.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (34 rows).** Counsel approves every notice except the operational outage calls in section 4. The matrix has four layers:
1. **Operational notices (minutes):** 14 client agency duty officers and county PSAP supervisors, under contracts, within 15 minutes and immediately.
2. **Business associate chain inside the group:** corporate notifies BDS as its subcontractor; BDS notifies Ambulance Services (CAD data) and Urgent Care (claim files) under 164.410 and the intercompany BAAs (5 business days).
3. **Each covered entity's own duties:** Ambulance Services and Urgent Care are separate covered entities (no affiliated covered entity designation, P03), so there are **two** HHS reports and two sets of letters and media notices.
4. **Outward duties:** BDS notifies 9 dispatch clients and 23 billing clients whose PHI was taken (72 hours for clients with negotiated terms, 10 calendar days under the standard BAA, never later than 60 days) and sends security incident reports to the others; the group decides SEC materiality; state breach laws apply in each state where affected individuals reside.

| When (from SOC discovery, Day 0) | Action | Owner |
|---|---|---|
| Minute 0 to 15 | Manual dispatch; calls to client duty officers and county PSAP supervisors | Center supervisors; Ambulance contract compliance director |
| Day 0 | Insurer, counsel, forensics engaged; internal 164.410 notices on the bridge | Group Chief Risk Officer; incident commander |
| Day 0 to 1 | Voluntary report to FBI or IC3 and CISA (supports the OFAC mitigating factor if payment is considered); tell the county about the premise notes | Group CISO; BDS security and compliance lead |
| Within 24 hours | Written outage reports to client agencies and counties under their contracts; disclosure committee convened | BDS; Ambulance contract compliance director; Group General Counsel |
| Within 72 hours of discovery | BDS notice to affected billing clients with 72-hour BAA terms | BDS security and compliance lead |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 5 business days | BDS notices to Ambulance Services and Urgent Care (intercompany BAA); security incident reports to unaffected clients | BDS security and compliance lead |
| Within 10 calendar days of discovery | BDS notice to affected clients on the standard BAA | BDS security and compliance lead |
| Within 10 days of determination (Florida third-party agent duty, 501.171(6)) | BDS and corporate to the divisions and to Florida clients | Group General Counsel |
| Within 30 days of determination | Florida individual notice (or HIPAA notice with a copy to the Department of Legal Affairs under the deemed-compliance path); Department notice (500 or more Floridians); consumer reporting agencies (more than 1,000). Apply each other state's law the same way | Each covered entity's Privacy Officer with counsel |
| Within 60 days of discovery | HIPAA individual notices; HHS notice (500 or more, contemporaneous); media in each state with more than 500 affected residents | Ambulance Services and Urgent Care Privacy Officers |
| Confirm before use | State EMS office notices (**unverified** in this sample) | Ambulance Services chief operating officer |

**Plan to the shortest clock.** In this scenario the order is: operational outage calls, 24-hour written outage reports, 72-hour billing client notices, SEC (if material), intercompany and standard client BAA notices, Florida third-party agent notices, Florida 30-day notices, then the HIPAA 60-day outer limit.

**Materiality factors for the disclosure committee:** number of people affected across two covered entities and 32 clients; effect on emergency operations and any patient harm during manual dispatch; county agreement penalties and client contract exposure; regulatory exposure (OCR, state attorneys general, state EMS offices); cost of notification, recovery, and rebuilding; and loss of clients. Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

**Ransom decision:** board risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not remove any notice duty when data was taken, and a decryptor is not trusted for the CAD; the CAD is rebuilt from clean images either way.

**CIRCIA:** not in effect (final rule not published as of 2026-09-25). If a final rule is in force at the time of an incident, add the 72-hour incident and 24-hour ransom payment reports to CISA.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA order (P05 section 7):
1. SYS-G1 identity and break-glass access confirmed clean (BP-G01)
2. A new landing-zone account for the DPCP in provider A, inspected by the hub (BP-G03)
3. WAN to the 4 centers confirmed (BP-G04)
4. CAD database restored from the latest clean provider B copy to the new account; CAD servers rebuilt from clean images (BP-BD01). The 1-hour RTO **cannot be met** in this scenario without the provider B standby; plan for 2 to 4 days of manual dispatch
5. Incident and unit data entered from paper cards, then 911 response tracking resumed (BP-AM01)
6. County CAD-to-CAD interfaces reconnected one at a time with field filters (BP-BD02); the premise notes field stays off
7. SOC visibility over the new account (BP-G02)
8. File transfer servers rebuilt in a separate BDS account; claims resume (BP-BD03)
9. AI triage module stays off until the Group AI council re-approves (BP-BD06)

Tell client agencies, counties, crews, and billing clients when each service returns (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.11).
- Update P01 (GR-01, GR-02, GR-03, GR-05, AMB-001, BDS-001, BDS-003), the POA&M (POAM-003, POAM-004, POAM-011 to POAM-013), the notification matrix, and this runbook.
- Rebuild county response-time reports for the outage period from paper records and tell each county how they were built.
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain all incident records for 6 years (POL-01 4.11).
