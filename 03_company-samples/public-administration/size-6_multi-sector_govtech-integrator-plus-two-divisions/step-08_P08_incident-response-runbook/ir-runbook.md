# Incident Response Runbook: Ransomware Across Divisions Affecting Agency Systems Holding CJI and FTI

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Public Administration (focus division: GovTech Integration) |
| Incident type | Ransomware with data theft that starts in the acquired consulting firm's estate (IT Consulting), crosses into corporate shared services with a stolen group cloud platform engineer session, and encrypts and steals data in the ACMP CJI cluster and two FTI tenants (GovTech), plus CUI on the acquired firm's file shares |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Systems | SYS-D1 ACMP (the P02 SSP system); SYS-G1, SYS-G2, SYS-G3; the acquired firm's VPN, identity provider, endpoints, and file shares (part of SYS-D4) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-15 by the Group CISO and the Group General Counsel, with the board risk committee review of P01 and P07 |
| Last tested | Technical playbooks are tested quarterly. **The cross-division notification matrix has never been exercised** (scenario gap 5); the first cross-division tabletop with agency security contacts and the disclosure committee is due 2026-12-15 (POAM-004) |

**Why this incident.** It joins the group's top risks in one event: the only Very High risk (P01 IC-001, the acquired firm's VPN and directory trust), ransomware through shared services (GR-01, GT-001), theft of FTI and CJI (GT-002), recovery at scale (GR-07, GT-003), and a cross-division notice failure (GR-03). Its notice clocks run from 1 hour to 60 days across agencies, DoD, the SEC, and state law.

**Whose clocks.** Most clocks for the agency data belong to the **agencies**: the criminal justice agencies' CJIS reporting, the revenue agencies' 24-hour TIGTA and IRS reports, and Florida agencies' 12-hour ransomware reports. The group's job is to tell each agency fast enough and give it the facts it must report. The group's **own** legal clocks are the third-party agent notices under state law (Florida: 10 days, Fla. Stat. 501.171(6)(a)), the DoD report within 72 hours (DFARS 252.204-7012(c)), the TIGTA contact that Pub. 1075 sec. 1.8.2 places on anyone who discovers a possible FTI disclosure, and the SEC filing if the incident is material. All obligations are in `notification-matrix.csv` (42 rows).

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry (IT Consulting).** An acquired-firm consultant on a DoD program enters a password and SMS code on a phishing page that relays them in real time. The attacker signs in to the acquired firm's VPN, which still accepts SMS codes (P07 AC-17 finding; POAM-018).
- **Lateral movement.** The acquired estate has no group EDR and its VPN is invisible to the SIEM (P07 SI-3, SI-4 findings). The attacker reaches a migration server used by group cloud platform engineers to move accounts across the directory trust, and steals the session token of an engineer who is holding a just-in-time elevation to the ACMP production accounts in provider A.
- **Persistence (GovTech).** Inside the elevation window the attacker creates a new access key for one of the 41 ACMP service accounts that are managed outside identity governance (P07 AC-2 finding; POAM-005). The key outlives the elevation.
- **Dwell (5 days).** Using that service account, the attacker reads the CJI cluster tables of 64 criminal justice agencies in 4 states (31 in Florida) and the data of two FTI tenants: the Florida revenue agency and one other state's revenue agency. No alert fires (P07 SI-04c.01). In the acquired estate it copies CUI from file shares used by 4 DoD programs.
- **Impact (Day 0).** The attacker encrypts the CJI cluster's database volumes and document storage and the two FTI tenants' document storage, deletes the snapshots and point-in-time recovery settings it can reach in provider A, and encrypts the acquired firm's file servers. Extortion email goes to the group and to 3 agencies.
- **What did not happen.** The immutable vault in provider B has a separate identity and a deletion lock, so it is intact. The constituent services cluster, the IEP, the MVSP, the RMS, the Civic Suite, Grants Management, and the CUI enclave were not reached.
- **Forensic estimate at Day 4:** about 1.3 million CJI case records (about 1.1 million individuals, about 520,000 of them Florida residents; about 410,000 records include criminal history record information); about 2.1 million taxpayer case records from the Florida revenue agency and 0.9 million from the other state's agency (FTI and state tax data); about 2,300 files of CUI from 4 DoD programs (the division is prime contractor on 2 and subcontractor on 2).

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC, identity, and cloud platform teams; ACMP platform director | Forensic firm on retainer (insurer panel) | SOC bridge |
| Agency notice desk (BP-G05) | Group public sector compliance director | GovTech division CISO | Printed agency contact list; phones |
| Notifications and legal | Group General Counsel with outside breach counsel | Division general counsels | Out-of-band bridge |
| GovTech liaison | GovTech division CISO | ACMP platform director | Division bridge |
| IT Consulting liaison and DoD reports | IT Consulting federal contracts compliance officer (medium assurance certificate holder) | IT Consulting security and compliance lead | Division bridge |
| Government Software Products liaison | Software security and compliance lead | Software division RMS general manager | Division bridge |
| HIPAA business associate decisions | GovTech HIPAA Security Official; IT Consulting security and compliance lead | Group Chief Privacy Officer | Division bridges |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email, chat, and the ticketing system and may hold identity sessions. Use the crisis line and managed mobile devices. The printed binder in each division's command center holds this runbook, the notification matrix, and agency, CSA, revenue agency, DoD, and customer contacts. **Never put CJI, FTI, CUI, or PHI in the incident log, email, or tickets** (POL-03 4.3); use counts and identifiers.

## 2. Preparation checks (Identify / Protect)
- [x] Immutable vault in provider B with a separate backup identity and deletion lock (CP-9; P07 satisfied)
- [x] 24x7 SOC with EDR on all group-managed endpoints and cloud workloads (SI-3, SI-4)
- [x] Phishing-resistant MFA and just-in-time elevation for administrators (IA-2(1), AC-6(5); P07 satisfied)
- [ ] Phishing-resistant MFA on the acquired firm's VPN and group EDR on acquired endpoints (**gap until POAM-018 closes**: VPN 2026-10-31, EDR 2026-12-31)
- [ ] Acquired VPN, directory trust, and bulk-read alerts in the SIEM (**gap until POAM-007 closes**, 2026-12-31)
- [ ] All ACMP service accounts in identity governance (**gap until POAM-005 closes**, 2026-12-31)
- [ ] Parallel restore automation so the CJI cluster and FTI tenants can meet the 8-hour RTO (**gap until POAM-011 closes**, 2027-03-31)
- [ ] Group notification matrix complete with every LASO, CSO, disclosure officer, BAA, and DoD contact, and exercised (**gap until POAM-003 and POAM-004 close**)
- [ ] At least 6 medium assurance certificate holders in two locations for DoD reports (IT Consulting supplement; only 2 today, P03 IC-G15)
- [x] Forensic retainer and insurer panel confirmed; disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Database volumes, snapshots, or point-in-time recovery settings deleted or changed outside a change ticket | Cloud audit log alerts; backup job failures | Declare Severity 1; open the bridge |
| Key policy changed or a key disabled or scheduled for deletion, including an FTI tenant's customer-managed key | Cloud audit log alerts | Same. Treat as ransomware until proven otherwise |
| Mass rewrite of objects in document storage; ransom note files | Storage metrics; agency users report errors | Same |
| New access key created for a service account, or a service account reading more rows than its baseline | Cloud audit logs; SIEM (bulk-read rule, once POAM-007 closes) | Disable the key and account; start triage |
| Session used from a new device or network, or a session token reused after the elevation window | SYS-G1 risk signals; PAM logs | Revoke all sessions of that identity; open an incident |
| Encryption on acquired firm file servers or laptops | Acquired firm help desk (must forward to the SOC at once); users | Declare; isolate the acquired VPN |
| Extortion email or leak-site post naming the group, a division, or an agency | Email; agencies; threat intelligence; law enforcement | Declare Severity 1; preserve the message |

**Severity 1** (group scale, POL-03 4.2): confirmed encryption or exfiltration in a shared service or in any system holding CJI, FTI, CUI, or PHI, or any incident that reaches more than one division.

**Record the discovery time (T0)** in the offline incident log. In a cross-division event, the earliest discovery by any group workforce member is T0 for every division. No clock is planned from a later date. Clocks that start at T0:
- the 1-hour internal report and the group's 1-hour notice to LASOs, CSAs, and revenue agency disclosure officers (CJISSECPOL v6.1 IR-6; POL-03 4.4);
- the 24-hour TIGTA and Office of Safeguards reports, which must not wait for an internal investigation (Pub. 1075 sec. 1.8.2-1.8.4);
- the 72-hour DoD report (DFARS 252.204-7012(c));
- the 12-hour Florida agency ransomware reports, which run from **each agency's** discovery. In practice that is when the group tells them, so the group tells them within the first hour.

Clocks that start later: the 10-day third-party agent notice runs from determination of a breach "or reason to believe the breach occurred" (Fla. Stat. 501.171(6)(a)), which in a data-theft case can be Day 0; the Form 8-K clock runs from the materiality determination.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the offline incident log; record T0 and the trigger; open the out-of-band bridge with all three division liaisons | Incident commander | Log open; liaisons on the bridge |
| 2. **Cut the entry path:** disable the acquired firm's VPN and the directory trust; revoke every session of the compromised consultant and the platform engineer; disable the new access key and the service account | Group identity director; IT Consulting security lead | VPN down; trust disabled; sessions revoked |
| 3. **Protect what is left:** apply an account-wide deny on deleting or changing snapshots, database instances, keys, and logging in the ACMP accounts; confirm the provider B vault and its deletion lock are intact and unreachable from the compromised identities | Group cloud platform director | Deny rule active; vault integrity report |
| 4. **Scope the stolen session:** check which accounts the engineer's elevation covered. In this scenario it covered ACMP production accounts only, not the RMS, Civic Suite, Grants Management, IEP, MVSP, or the enclave. Record the evidence; it decides which customers receive a suspected-incident notice | Group SOC director | Scope note signed by the incident commander |
| 5. **Stop spread into agency systems:** suspend the 11 state message switch links, the revenue agency file transfers, and agency API links at the ACMP integration gateway; block egress from ACMP containers | ACMP platform director | Interfaces down; egress blocked |
| 6. **Tell the agencies (suspected incident) within 1 hour:** LASOs of all 212 CJI cluster agencies, the 11 CSOs, and the disclosure officers of all 7 revenue agencies. Say what is known, what is not, and when the next update comes | Agency notice desk | Each contact reached by phone; time logged; written follow-up through the agreed secure channel |
| 7. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 8. Put CJI and FTI tenants in maintenance mode; keep the constituent services cluster running if forensics confirms it is untouched | ACMP platform director; GovTech customer support director | Status page updated |
| 9. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.7) | Group CISO | Committee convened |

**Do not** power off or delete attacker resources yet, and do not restore into the compromised accounts. Evidence and a clean rebuild come first. Do not pay or negotiate (section 7.4).

## 5. Analysis (RS.AN)
1. **Entry and path.** Reconstruct the path from the acquired VPN through the migration server to the engineer's session and the service account key. Image the migration server, the consultant's laptop, and the acquired file servers.
2. **Scope by tenant and agency.** Use ACMP database and storage access logs to list every table and object the service account read. Map each to its tenant and agency. Count records and individuals by agency and by state of residence, and the data elements involved (CHRI, FTI, Social Security numbers, driver license numbers). These counts drive every notice.
3. **Rule out the other tenants.** For the 5 revenue agencies not affected, show from key usage logs, database logs, and vault logs that their tenants, keys, and backups were not touched. Give each agency the evidence before its 24-hour mark, so it can decide its own reporting (Pub. 1075 sec. 1.8.2). In this scenario the evidence is ready at hour 20.
4. **Covered defense information.** Run the DFARS 252.204-7012(c)(1)(i) review: identify compromised computers, servers, specific data, and user accounts on the acquired estate and on any group system reached through the trust. List the DoD programs and contract numbers involved.
5. **PHI and FCI checks.** Scan the acquired file shares for PHI from the 19 IT Consulting health clients and for federal contract information from the civilian contracts. In this scenario none is found by Day 4.
6. **Evidence.** Keep chain of custody: who collected what, when, with hashes. Store evidence in a separate forensic account limited to the forensic firm and named SOC staff. Keep DoD-related images and packet capture at least 90 days from the DoD report (DFARS 252.204-7012(e)); keep all incident records 7 years (POL-01 4.12).
7. **Agency fact sheets.** Keep one fact sheet per affected agency (section 7.2), updated at least every 12 hours.

## 6. Containment and eradication (RS.MI)
1. Remove all attacker persistence: access keys, roles, federation changes, functions, scheduled jobs, and network rules. Compare every ACMP account against the infrastructure-as-code baseline.
2. Rotate every ACMP secret, service account credential, and agency interface credential (accelerates POAM-005 and POAM-006). Coordinate customer-managed key actions with each revenue agency.
3. Bind PAM elevations to the device that requested them, and shorten elevation windows for production accounts (P01 GT-001 treatment).
4. Keep the acquired VPN and directory trust off. Bring acquired staff back through group identity with phishing-resistant MFA on group-managed devices only (accelerates POAM-018). Move the recovered CUI into the enclave, not back to the shares (POAM-020).
5. Rebuild the ACMP CJI cluster and FTI tenant environments from code in clean accounts. Forensics confirms that no persistence remains in SYS-G1, the landing zones, or division accounts before reconnecting anything.

## 7. Reporting and communication (RS.CO)
### 7.1 Notice timeline
**Follow `notification-matrix.csv`.** Counsel approves every external notice. The matrix has six layers: internal reporting; GovTech's notices to agencies and the agencies' own duties; IT Consulting's DoD and federal duties; HIPAA business associate duties; Software division duties; and group duties (SEC, OFAC, law enforcement, insurer, CIRCIA tracking).

| When (from T0) | Action | Owner |
|---|---|---|
| T0 + 1 hour | Phone notice of a suspected incident to the LASOs of all 212 CJI cluster agencies, the 11 CSOs, and the disclosure officers of all 7 revenue agencies | Agency notice desk |
| T0 + 1 hour | Insurer breach hotline; status page for ACMP users | Group Chief Risk Officer; GovTech customer support director |
| T0 + 4 hours | Written fact sheet to every affected agency (section 7.2), so Florida agencies can file within their 12 hours and revenue agencies within their 24 hours | Agency notice desk |
| Agency T0 + 12 hours | The Florida revenue agency reports to the Cybersecurity Operations Center and the FDLE Cybercrime Office (Fla. Stat. 282.318(3)(c)9.c.(I)); Florida county and municipal criminal justice agencies in the CJI cluster report under Fla. Stat. 282.3185(5)(b), and any Florida state-level agency among them under 282.318 | Agencies, with group facts |
| T0 + 24 hours | The 2 affected revenue agencies report to TIGTA and the IRS Office of Safeguards (Pub. 1075 sec. 1.8.2-1.8.4). The group contacts TIGTA directly in coordination with them and confirms each report was made. The other 5 agencies receive the evidence that their tenants were not touched | Revenue agencies; Group General Counsel |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts (POL-03 4.7); voluntary report to the FBI or IC3 and CISA, coordinated with the agencies | Group General Counsel; Group CISO |
| As each state CSA requires | Each criminal justice agency reports the security violation to its CSO and the Director, FBI (Security Addendum sec. 4.01) | Agencies, with group facts |
| T0 + 72 hours | DoD report through DIBNet with a medium assurance certificate (DFARS 252.204-7012(c)); then the report number to the 2 prime contractors as soon as practicable (252.204-7012(m)(2)(ii)); malware to DC3 when isolated (252.204-7012(d)) | IT Consulting federal contracts compliance officer |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| No later than 10 days after determining a breach | Written third-party agent notice to the Florida revenue agency and the 31 Florida criminal justice agencies with confirmed data theft, with all information each needs for its own notices (Fla. Stat. 501.171(6)(a)). Apply each other state's service-provider notice law the same way | Group General Counsel |
| Agency: 30 days after determination | Florida individual notices; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 (Fla. Stat. 501.171(3)-(5)). The group can send notices on an agency's behalf if asked (501.171(6)(b)). Agencies in other states follow their own state's law | Agencies |
| Agency: 1 week after remediation | After-action report by each Florida county or municipal agency to the Florida Digital Service (Fla. Stat. 282.3185(6)) | Agencies, with group input |

**Plan to the shortest clock.** In this scenario the order is: CJI notices (1 hour), Florida agency ransomware reports (12 hours, agency side), TIGTA and IRS reports (24 hours, agency side), the DoD report (72 hours), the SEC filing (4 business days after a materiality decision), the third-party agent notices (10 days), then the agencies' 30-day individual notices. A group that waits for its own investigation leaves the agencies in breach.

**Not triggered, and recorded as such.** HIPAA business associate notices (IEP not reached; no PHI on the acquired shares), RMS agency notices (the stolen session had no RMS rights), FedRAMP and GovRAMP incident communications, Medicaid and SNAP contract notices, and DPPA-related notices. Each "not triggered" decision is written in the incident log with its evidence and rechecked if the scope changes.

### 7.2 Fact sheet for agency reports
Florida agency reports and the IRS data incident report ask for specific facts (Fla. Stat. 282.318(3)(c)9.b.; Pub. 1075 sec. 1.8.3). Keep one fact sheet per agency, with no CJI or FTI in it:
- summary of facts; date and time the incident occurred and was discovered; how it was discovered
- the date of the most recent backup, where it is, whether it was affected, and that it is cloud-based
- types of data and data elements involved; potential number of records (a range if unknown)
- systems involved and where (cloud account, U.S. region); whether any group employee was involved
- estimated fiscal impact to the agency, if known; details of any ransom demand
- the group's point of contact and the time of the next update

### 7.3 SEC materiality (disclosure committee)
Factors: the number of agencies and states affected and the type of data (CJI and FTI); the possibility that CSAs or the FBI suspend CJI access, or revenue agencies void contracts (Pub. 1075 Exhibit 7 I(13)); DoD program effects and CMMC timing; contract credits for missing the 8-hour RTO on about 214 tenants; response and notification costs; and effects across divisions (GovTech is about 45% of group revenue). Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

The IT Consulting president, as CMMC Affirming Official, must not make or renew a CMMC affirmation that does not reflect the post-incident state of the systems in scope (32 CFR 170.22).

### 7.4 Ransom decision
- Florida state agencies, counties, and municipalities **may not pay or otherwise comply with a ransom demand** (Fla. Stat. 282.3186). The data belongs to the agencies. The group will not negotiate over agency data without each affected agency's agreement (POL-03 4.8).
- Any payment by the group, for any part of the incident, requires board risk committee approval, counsel, the insurer, consultation with every affected agency and the DoD contracting officers concerned, and an OFAC sanctions check.
- Paying does not remove any notice duty when data was taken.

### 7.5 Other communications
- Agency users: status page updates at least every 4 hours while tenants are down.
- Media: only the Group communications lead speaks, after the affected agencies have seen the statement. The 2 affected revenue agencies share any media release about FTI with the Office of Safeguards before release (Pub. 1075 sec. 1.8.5), so the group sends them its drafts first.
- Staff: one script from the incident commander for all divisions; no posts or outside discussion.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7):
| Priority | Resource | Target |
|---|---|---|
| 1 | SYS-G1 identity and break-glass access (BP-G01) | 1 hour |
| 2 | Clean landing-zone accounts, network rules, and keys (BP-G03) | 2 hours |
| 3 | Agency notice desk (BP-G05), on printed contacts if needed | 1 hour |
| 4 | SOC visibility, with the acquired estate and trust logs added (BP-G02) | 4 hours |
| 5 | Vault access and restore tooling (BP-G04) | 4 hours |
| 6 | ACMP CJI cluster: supervision and court case management (BP-GT01) | 8 hours (contract RTO) |
| 7 | Agency data interfaces, after each CSA and agency approves reconnection (BP-GT04) | 8 hours |
| 8 | The 2 FTI tenants (BP-GT02) | 8 hours (contract RTO) |
| 9 | Acquired firm users on group identity and devices; CUI into the enclave (BP-IC01, BP-IC02) | 24 to 48 hours |

**Warning (current state).** The vault is intact, but the parallel restore automation is not built (POAM-011). The 2026 test restored 12 tenants in 6 hours. With today's tooling the platform team estimates 15 to 18 hours for the about 214 tenants affected here (212 CJI cluster tenants and 2 FTI tenants), against an 8-hour RTO. Tell the agencies early so they can run their manual workarounds (printed supervision rosters; revenue agencies' own tax systems; P05 section 4), and restore the CJI cluster in order of agency size and public safety need, agreed with the CSAs.

**Before restoring an FTI tenant from the vault**, confirm that the agency's IRS notification covers the vault. One of the 2 affected agencies is among the 2 whose notifications predate the vault (P03 PB-16; POAM-027). Tell that agency before the restore so it can file its update.

**Validate before reconnecting:**
- Forensics confirms the environment is clean, and all secrets and keys are rotated.
- Record counts and checksums match the last known good figures for each tenant.
- CJI paths use FIPS 140-3 certified modules (SC-13; met for the ACMP).
- Each agency's security contact approves reconnection of its interface; each CSA confirms whether it must approve message switch reconnection first.

Tell agency users when each tenant is back (RC.CO). Agencies keep their manual workarounds until their process is back within its RTO.

## 9. Post-incident (ID.IM)
- Lessons-learned review within 14 days of recovery, documented within 30 days (POL-03 4.11). Invite the security contacts of the affected agencies and CSAs.
- Post-incident review of the incident procedures, with fixes made as soon as reasonably possible and training on the changes for all staff with FTI access (Pub. 1075 sec. 1.8.4); refresher training within 30 days for staff involved (CJISSECPOL v6.1 AT-2).
- Update the registers (P01: GR-01, GR-03, GR-05, GR-07, IC-001, GT-001, GT-002, GT-003), the POA&M (P07: POAM-003 to POAM-007, POAM-011, POAM-018, POAM-020), the BIA (P05), the notification matrix, and this runbook.
- Update the SPRS score and the CUI enclave assessment for the post-incident state before any CMMC affirmation (POAM-024).
- Provide each Florida local agency's after-action input within 1 week of remediation (Fla. Stat. 282.3185(6)).
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain the incident log, evidence, and notices for 7 years (POL-01 4.12).
