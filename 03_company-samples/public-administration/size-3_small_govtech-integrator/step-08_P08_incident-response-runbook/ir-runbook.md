# Incident Response Runbook: Ransomware in the Production Cloud Tenant (CJI and FTI)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (GovTech systems integrator serving state and local agencies) |
| Tier / Vertical | Small / Public Administration |
| Incident type | Ransomware in the production cloud tenant that encrypts platform databases holding CJI (AC-02) and FTI (AC-01), with data theft, starting from a stolen cloud engineer session token |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| System | Agency Case Management Platform (ACMP), per the SSP (P02) |
| Runbook owner | IT Manager (Information Security Officer) |
| Approved | 2026-08-31 by the Chief Operating Officer |
| Last tested | Not yet. First tabletop with the AC-01 and AC-02 security contacts due 2026-11-30 (POAM-018) |

**Why this incident.** It is the company's only Very High risk (P01 R-001) and its main High data-theft risk (R-002). An attacker who holds a cloud administrator session can reach every tenant, the backups, and the logs at once, because all of them sit in the production account today (P04, P07 POAM-003 and POAM-006).

**Whose clocks.** Most legal clocks in this incident belong to the **agencies**, not the company: the sheriff's CJIS reporting, the revenue agency's 24-hour IRS reporting, and every Florida agency's 12-hour ransomware report. The company's job is to tell each agency fast enough and give it the facts it must report. The company's own legal clock is the 10-day third-party agent notice under Fla. Stat. 501.171(6)(a). All obligations are in `notification-matrix.csv`.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | Chief Operating Officer | Incident line (on-call phone), then the out-of-band group on personal phones |
| Technical lead (cloud) | Cloud Operations Lead | Director of Engineering | On-call phone |
| Detection and forensics | Managed detection and response provider (contract due 2026-10-31, POAM-007); forensic firm from the insurer's panel | Cloud provider's security incident channel | Provider 24x7 line; via insurer hotline |
| Agency notices and breach determinations | Contracts and Compliance Manager | Chief Operating Officer | Cell |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Via insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Executive decisions, ransom | Chief Executive Officer | Chief Operating Officer | Cell |
| Agency operations messaging | Director of Customer Delivery (program managers); Customer Support Manager (status page, agency users) | Chief Operating Officer | Cell |
| Agency security contacts | AC-01 disclosure officer; AC-02 local agency security officer; AC-03 information security manager; IT contacts for AC-04 to AC-11 | Named alternates in each contract | Printed contact list in the incident binder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read company email, chat, and the ticketing system, and may hold identity provider sessions. Coordinate on personal phones and the printed contact list. Keep the incident log in the offline incident binder template until a clean workspace is confirmed. **Never put FTI or CJI in the incident log, email, or tickets** (POL-03 4.3).

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at headquarters and with each on-call engineer: this runbook, the notification matrix, the agency contact list, and the agency report template (section 6.2)
- [ ] Immutable backups in a separate account and second U.S. region, restore-tested within the last 90 days (CP-9, CP-4). **Gap until POAM-003 (2026-12-31) and POAM-004 (2027-03-31) close.** Today the snapshots sit in the production account and an administrator can delete them
- [ ] Audit logs copied to a separate write-once account and kept 7 years (AU-9, AU-11). **Gap until POAM-005 and POAM-006 close.** Today logs roll off after 90 days
- [ ] 24x7 security monitoring of the cloud tenant, identity provider, and laptops (SI-4). **Gap until POAM-007 closes.** Today no one watches after hours
- [ ] Just-in-time administrator access, so a stolen session carries no standing rights (AC-6). **Gap until POAM-012 closes (2027-01-31)**
- [ ] Two sealed break-glass accounts with hardware keys, tested quarterly (POL-02 4.9; P01 R-029, due 2026-11-30)
- [ ] All staff briefed on the 1-hour reporting rule (POL-03 4.2; POAM-015, briefing 2026-09-30)
- [ ] Forensic retainer and breach counsel confirmed through the insurer panel (P03 G-074)
- [ ] Agency contact list checked each quarter against the contracts (Contracts and Compliance Manager)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Database instances, snapshots, or point-in-time recovery settings deleted or changed outside a change ticket | Cloud audit log alert; backup job failure | Cloud Operations Lead opens an incident and calls the incident commander |
| Encryption key policy changed, key disabled, or key scheduled for deletion (including the AC-01 customer-managed key) | Cloud audit log alert | Same. Treat as ransomware until proven otherwise |
| Mass rewrite or deletion of objects in document storage; files with unknown extensions or a ransom note file | Storage metrics; agency users report errors | Same |
| Audit logging disabled or log retention changed | Cloud audit log alert | Same. This is often the attacker's first step |
| A cloud engineer's session used from an unfamiliar network or country, or from two places at once | Identity provider and cloud sign-in logs | Revoke the session at once; open an incident |
| Large outbound transfer from containers or storage | Network flow logs; billing anomaly | Block the destination; open an incident |
| Ransom or extortion email to the company or an agency, or a leak-site post naming the company or a customer | Email; agency; threat intelligence; law enforcement | Declare the incident; preserve the message |

**Declare a ransomware incident when** any production data, backup, or key is encrypted, deleted, or locked by an unauthorized actor; or an unknown actor has used administrator rights in production; or an extortion claim names company or agency data. When in doubt, declare. The first reports to agencies are for **suspected** incidents.

**Record the time of discovery** in the incident log. Clocks that start there:
- the 1-hour CJI report (CJISSECPOL IR-6a);
- the 24-hour FTI report by AC-01, which must not wait for an internal investigation (Pub. 1075 sec. 1.8.4);
- the 12-hour ransomware reports by Florida agencies, which run from **their** discovery. In practice that is when the company tells them, so the company tells them within the first hour.

The 10-day clock under Fla. Stat. 501.171(6)(a) starts at the determination of a breach "or reason to believe the breach occurred," which in a data-theft case can be the same day.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the incident log (offline template). Record discovery time and the trigger | Incident commander | Log open with T0 recorded |
| 2. Revoke the stolen session: disable the engineer's identity provider account, revoke all sessions and tokens for every cloud administrator role, and deactivate the engineer's access keys. Use a break-glass account if the identity provider is in doubt | Cloud Operations Lead | No active administrator sessions except the responders' |
| 3. Protect what is left: apply an account-wide deny rule on deleting or changing snapshots, database instances, keys, and logging; copy the newest intact snapshots and the audit logs to a separate account the attacker never touched | Cloud Operations Lead | Deny rule active; copies confirmed |
| 4. Stop spread into agency systems: suspend the AC-02 message-switch link, the AC-01 file transfer, and the AC-03 eligibility API at the integration gateway. Block all outbound traffic from containers | Cloud Operations Lead | Interfaces down; egress blocked |
| 5. Put the platform in maintenance mode with a neutral status message | Customer Support Manager | Status page updated |
| 6. **Tell the agencies (suspected incident):** AC-02 local agency security officer (CJI) and AC-01 disclosure officer (FTI) first, then AC-03 and the municipal IT contacts. Say what is known, what is not, and when the next update comes | Contracts and Compliance Manager | Each contact reached by phone, call time logged, written follow-up sent through the agreed secure channel |
| 7. Call the cyber insurer's breach hotline; engage counsel and the forensic firm through the panel | Chief Operating Officer | Claim number issued; counsel engaged |
| 8. Brief staff on the out-of-band channel: what happened, who speaks to agencies, and that no one discusses the incident outside the company | Incident commander | Briefing sent |

**Do not** power off or delete attacker resources yet, and do not restore into the compromised account. Evidence and a clean rebuild come first.

## 4. Analysis (RS.AN)
1. **Scope.** Which accounts, roles, and resources did the attacker touch? Review cloud audit logs, identity provider logs, database logs, and storage access logs from the first unusual event. List every tenant whose data sits in an affected database or bucket. The shared cluster holds AC-02, AC-03, and the municipal tenants; the dedicated instance holds AC-01.
2. **Initial access.** Confirm how the session token was stolen (for example, an infostealer on the engineer's laptop or a malicious browser extension). Isolate and image that laptop through the endpoint detection and response tool.
3. **Preserve evidence.** The forensic firm images affected resources and exports logs before the 90-day retention drops them (P01 R-009). Keep chain of custody: who collected what, when, with hashes. Store evidence in the separate account with access limited to the IT Manager and the forensic firm. Keep it 7 years (POL-03 4.6).
4. **Exfiltration.** Determine whether data was copied out: database exports or snapshot sharing, storage reads, and outbound volume by destination. **This drives every breach decision.** For each tenant, record the record counts and data elements involved (FTI; CJI and CHRI; Social Security numbers; driver license numbers) and where affected individuals live.
5. **Backups and keys.** Find the last clean restore point for each database and confirm the snapshots are intact. Confirm the state of the AC-01 customer-managed key with AC-01 before any key action.
6. **Agency facts.** Keep a running fact sheet for the agencies (section 6.2), updated at least every 12 hours.

## 5. Containment and eradication (RS.MI)
1. Remove attacker persistence: new users, roles, access keys, identity federation trusts, functions, scheduled jobs, and changed network rules. Compare against the infrastructure-as-code baseline.
2. Rotate every secret: database credentials, the AC-02 interface key and all other interface credentials, pipeline secrets, and storage keys (POL-02 4.8). Coordinate AC-01 key actions with AC-01.
3. Rebuild the platform from infrastructure code in a **clean account** (P05 recovery priority 3). Build container images from the repository after checking recent commits and pipeline changes for tampering (P01 R-012).
4. Reimage the engineer's laptop and any other laptop that shows the same indicators. Reset that person's credentials and hardware key registration.
5. Forensics confirms that persistence is gone before recovery starts.

## 6. Reporting and communication (RS.CO)
### 6.1 Notice timeline
**Follow `notification-matrix.csv`.** Counsel confirms every external notice. T0 is the recorded discovery time.

| When | Action | Owner |
|---|---|---|
| T0 + 1 hour | Phone notice of a suspected incident to AC-02 (CJISSECPOL IR-6) and AC-01 (Pub. 1075 Exhibit 7 contract), then AC-03 and AC-04 to AC-11 | Contracts and Compliance Manager |
| T0 + 1 hour | Insurer breach hotline | Chief Operating Officer |
| T0 + 4 hours | First written fact sheet to every affected agency (section 6.2), so Florida agencies can file within their 12 hours | Contracts and Compliance Manager |
| Agency T0 + 12 hours | Each state agency (AC-01, AC-03) and each county or city (AC-04 to AC-11) reports the ransomware incident to the Cybersecurity Operations Center and the FDLE Cybercrime Office (Fla. Stat. 282.318(3)(c)9.c.(I); 282.3185(5)(b)) | Agencies, with company facts |
| T0 + 24 hours | AC-01 reports to TIGTA and the IRS Office of Safeguards (Pub. 1075 sec. 1.8.2-1.8.4). The company confirms the report was made, and reports directly if it cannot confirm | AC-01; Contracts and Compliance Manager confirms |
| As the state CSA requires | AC-02 reports the security violation to the CSO and the FBI (Security Addendum 4.01) | AC-02, with company facts |
| Within 48 hours | Voluntary report to the FBI (IC3) and CISA, coordinated with the agencies | IT Manager |
| No later than 10 days after determining a breach | Written third-party agent notice to each affected agency with all information it needs for its own notices (Fla. Stat. 501.171(6)(a)) | Contracts and Compliance Manager and counsel |
| Agency: 30 days after determination | Florida individual notices; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 (Fla. Stat. 501.171(3)-(5)). The company can send notices on an agency's behalf if asked (501.171(6)(b)) | Agencies |
| Agency: 1 week after remediation | After-action report by each county or city to the Florida Digital Service (Fla. Stat. 282.3185(6)) | AC-04 to AC-11, with company input |

**Plan to the shortest clock.** The 1-hour CJI report comes first, and the 12-hour Florida reports run on the agencies' side. A company that waits for its own investigation leaves the agencies in breach.

### 6.2 Fact sheet for agency reports
Florida agency reports and the IRS data incident report ask for specific facts (Fla. Stat. 282.318(3)(c)9.b.; Pub. 1075 sec. 1.8.3). Keep one fact sheet per agency, with no FTI or CJI in it:
- summary of facts; date and time the incident occurred and was discovered; how it was discovered
- the date of the most recent backup, where it is, whether it was affected, and that it is cloud-based
- types of data and data elements involved; potential number of records (a range if unknown)
- systems involved and where (cloud tenant, U.S. region); whether any company employee was involved
- estimated fiscal impact to the agency, if known; details of any ransom demand
- the company's point of contact and the time of the next update

### 6.3 Ransom decision
- Florida state agencies, counties, and municipalities **may not pay or otherwise comply with a ransom demand** (Fla. Stat. 282.3186). The data belongs to the agencies. The company will not negotiate over agency data without each agency's agreement.
- Any payment by the company requires the Chief Executive Officer, counsel, the insurer, consultation with every affected agency, and an OFAC sanctions check (POL-03 4.7).
- Paying does not remove any notice duty if data was taken.

### 6.4 Other communications
- Agency users: status page updates at least every 4 hours while the platform is down (Customer Support Manager).
- Media: only the Chief Operating Officer speaks, after the affected agencies have seen the statement. AC-01 shares any media release about FTI with the Office of Safeguards before release (Pub. 1075 sec. 1.8.5).
- Staff: a script from the incident commander; no posts or outside discussion.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 6). Targets assume the backup redesign is done; until then, see the warning below.

| Priority | Resource | Target |
|---|---|---|
| 1 | Agency communications: printed contact list, phones, status page | 1 hour |
| 2 | Workforce identity and cloud account access (break-glass if needed) | 1 hour |
| 3 | Clean cloud account and network rules from infrastructure code | 3 hours |
| 4 | Database cluster and the AC-01 dedicated database from the last clean point | 6 hours |
| 5 | Application tier and agency sign-in: AC-02, then AC-03, then AC-01 | 8 hours (contract RTO) |
| 6 | Integration gateway, replaying agency files and messages | 8 hours |
| 7 | Municipal tenants | 24 hours |
| 8 | Pipeline, then payroll and finance, then implementation work | 72 hours |
| 9 | AI eligibility assistant (only after P10 conditions are met) | After all others |

**Warning (current state).** If the attacker deleted the snapshots, there is **no other copy** today (R-001, POAM-003). The fallback is to rebuild case data from agency sources: AC-01 resends files, AC-02 re-imports from the message switch, and AC-03 re-syncs from its eligibility system. Case notes, documents, and history entered in the platform would be lost. Tell the agencies this early so they can plan manual work (P05 section 4).

**Validate before reconnecting:**
- Forensics confirms the environment is clean; all secrets are rotated.
- Record counts and checksums match the last known good figures for each tenant.
- TLS on the CJI paths uses FIPS 140-3 certified modules (SC-13; POAM-008).
- Each agency's security contact approves reconnection of its interface. For AC-02, the sheriff confirms whether its CJIS Systems Agency must approve first.

Tell agency users when each tenant is back (RC.CO). Agencies keep their manual workarounds until their process is back within its RTO (P05).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; documented within 30 days (POL-03 4.10). Invite the AC-01 and AC-02 security contacts.
- Post-incident review of the incident procedures, with any fixes made as soon as reasonably possible and training on the changes given immediately to all staff with FTI access (Pub. 1075 sec. 1.8.4).
- Refresher training within 30 days for staff involved in the incident (POL-03 4.9; CJISSECPOL AT-2).
- Update the risk register (P01, especially R-001, R-002, R-007, R-009, R-021), the POA&M (P07), the BIA (P05), and this runbook.
- Provide each municipal customer's after-action input within 1 week of remediation (Fla. Stat. 282.3185(6)).
- Retain the incident log, evidence, and notices for 7 years (POL-01 4.11).
