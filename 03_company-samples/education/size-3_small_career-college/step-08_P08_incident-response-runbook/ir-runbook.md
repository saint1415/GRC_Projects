# Incident Response Runbook: Ransomware with Student Record Exposure

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (private career college) |
| Tier / Vertical | Small / Educational Services |
| Incident type | Ransomware with exfiltration of student financial aid and education records (double extortion), starting from a phishing email to a financial aid staff member |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy. Together they are the written incident response plan required by 16 CFR 314.4(h) |
| Runbook owner | IT Director (Qualified Individual) |
| Approved | 2026-08-21 by the Campus President |
| Last tested | Not yet. First tabletop exercise due 2026-11-30 (POAM-016, POAM-017) |

**Where this plan meets 16 CFR 314.4(h):**

| Element | Where |
|---|---|
| (h)(1) Goals | POL-03 section 1 |
| (h)(2) Internal response processes | Sections 2 to 5 and 7 below |
| (h)(3) Roles, responsibilities, decision authority | POL-03 section 3; section 0 below |
| (h)(4) External and internal communications | Section 6 and `notification-matrix.csv` |
| (h)(5) Remediation of weaknesses | Section 8 (feeds the POA&M) |
| (h)(6) Documentation and reporting | Section 3 step 7 (incident log); section 6 |
| (h)(7) Evaluation and revision | Section 8 |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Director (Qualified Individual) | Senior IT technician, then the Campus President | Incident line (cell), then the out-of-band group chat on personal phones |
| Executive lead and communications | Campus President | Director of Institutional Effectiveness | Cell |
| Board | Board chair (majority owner), told the same day | Other Board members | Cell |
| Technical response | IT technicians (2) | Managed detection provider once contracted (POAM-004); forensic firm through the insurer's panel | Cell; provider 24x7 line |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Via the insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| FSA reporting and servicer liaison | Director of Financial Aid | Designated financial aid staff member | Cell |
| Education records and FERPA disclosure record | Registrar | Designated registrar staff member | Cell |
| Refunds and payments | Business Office Manager | Designated business office staff member | Cell |
| Academic continuity (LMS, classes, labs) | Dean of Academic Affairs | Program directors | Cell |
| SaaS vendors (SIS, FAMS, LMS, identity provider, email) | Vendor security or support lines | Account managers | Numbers in the incident binder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email and chat are compromised. Coordinate by phone and use the printed contact list in the incident binders in the IT office and the Campus President's office (POL-03 4.9).

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binders hold this runbook, the contact list, the notification matrix, the FSA breach intake instructions, and the latest SIS export of student and parent mailing and email addresses. **Due 2026-09-30 (POAM-016)**
- [ ] Immutable backups in a separate account and region, with a restore test within the last 90 days (CP-9, CP-4). **Gap until POAM-006 and POAM-007 close**
- [ ] Endpoint detection and response and 24x7 alerting (SI-3, SI-4). **Gap until POAM-004 and POAM-005 close.** Until then, antivirus alerts must be checked daily by an IT technician
- [ ] Two break-glass administrator accounts, sealed and tested (POL-02 4.7)
- [ ] Forensic firm and breach counsel confirmed through the insurer's panel (POAM-017)
- [ ] Servicer and SaaS contracts require notice to the college within 72 hours (POAM-002)
- [ ] Data map of where customer information and education records live (POAM-026). It speeds up the count of affected consumers
- [ ] 6 pre-imaged spare laptops and a clean install package for the Department-provided SAIG software (P05)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A financial aid staff member reports opening an attachment or link (for example, a fake "verification document" or "ISIR correction") or approving an unexpected MFA prompt | Staff report (POL-03 4.2) | IT disconnects the laptop from the network, resets the password, revokes sessions, removes unknown MFA devices, and reviews sign-ins. Escalate if there is any sign of other hosts or accounts being used |
| Antivirus detection on a financial aid or business office endpoint | Antivirus console (checked daily until EDR) | Treat as a possible first stage. Isolate and investigate the host |
| New MFA device, impossible travel, or sign-in from an unusual country on a staff account | Identity provider sign-in review | Revoke sessions; confirm with the user by phone |
| Bulk export from the SIS or FAMS, or a large read of the aid export folder | SIS and FAMS audit trail; file server logs (POAM-010) | Suspend the account; open an incident |
| Large outbound transfer from the cloud tenant or campus | Firewall and cloud logs (egress alerting from 2026-12-31) | Block the destination; open an incident |
| Backup jobs fail or backups are deleted | Backup reports | Treat as an attack on recovery. Declare the incident |
| Files renamed with an unknown extension, or a ransom note | Staff report; file server | Call the incident line. **Do not power off.** Disconnect the network |
| Extortion email to the Campus President, staff, or students, or a leak-site post naming the college | Email; law enforcement; FSA | Declare the incident; preserve the message |
| The servicer or a SaaS vendor reports an incident affecting college data | Vendor notice | Open an incident; get the vendor's facts in writing |

**Declare a ransomware incident when** encryption or a ransom note is confirmed on any college system, or an extortion claim names college data. The IT Director declares and calls the Campus President.

**Record these dates in the incident log. They start the legal clocks:**
- **Discovery (FTC):** the first day the event was known to any employee, officer, or other agent of the college other than the person committing the breach (16 CFR 314.4(j)(2)). The staff member's phishing report can be that day.
- **Determination (Florida):** the day the college determined a breach occurred, or had reason to believe one occurred (Fla. Stat. 501.171(3)-(4)).
- **Suspected breach (FSA):** report immediately. Do not wait for confirmation.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Isolate affected endpoints (cable out, Wi-Fi off). Leave them powered on for memory evidence | Staff, with IT on the phone | Devices offline |
| 2. Cut the site-to-site VPN to the cloud tenant and restrict cloud network rules to the IT admin range if the file server, reporting database, or integration server may be affected | IT Director | Tunnel down; rules changed |
| 3. Protect the backups: remove delete rights from all but one break-glass account and take a snapshot of the vault configuration | IT Director | Vault locked down |
| 4. Revoke all sessions in the identity provider; reset the passwords of the affected user and all administrators; disable the integration service account | IT technicians | Sessions revoked; integration paused |
| 5. Call the cyber insurer's breach hotline. Engage counsel and forensics through the insurer. Tell the Board chair | Campus President | Claim number issued; chair informed |
| 6. Hold outgoing refund payment files and freeze student bank detail changes until their integrity is confirmed | Business Office Manager | No payment file released |
| 7. Start the incident log in the ticketing system (or on paper if it is down): timeline, actions, who, when, and the dates in section 2 | IT Director | Log open (POL-03 4.3) |

## 4. Analysis (RS.AN)
1. **Scope.** Which endpoints, cloud workloads, and accounts are affected? Check antivirus, identity provider sign-ins, cloud audit logs, firewall logs, and the SIS and FAMS audit trails. Ask the SIS, FAMS, and LMS vendors to check for access with the stolen credentials or sessions.
2. **Initial access.** Identify the phishing email, the user, the credential or session taken, and the first compromised host. Search all mailboxes for the same message and remove it.
3. **Preserve evidence.** Forensics images affected hosts and exports logs **before they roll over**. Identity provider and cloud logs keep only 30 to 90 days by default (P02 AU-11). Keep a chain-of-custody record for every image and export.
4. **Exfiltration.** Determine what was taken: look for archive tools, transfers to cloud storage, and firewall and cloud egress. Check the aid export folder on the file server and the reporting database first. They hold the most concentrated customer information.
5. **Who and what is affected.** Build the affected-person list from the files and tables taken. For each person, record:
   - consumer type (student, former student, parent borrower);
   - data elements (SSN, ISIR data, bank details, grades, immunization records);
   - state of residence;
   - whether the data was encrypted and whether the key was also taken.

   This list drives every count in section 6: 500 consumers for the FTC, 500 Florida residents for the Department, and more than 1,000 people for the consumer reporting agencies.
6. **Backups.** Confirm the backup vault is intact and clean before any restore. SaaS data (SIS, FAMS, LMS) is recovered by the vendors (P05); get each vendor's integrity statement.
7. **Determinations.** The Qualified Individual and counsel document whether a notification event occurred under 16 CFR 314.2(m). Unauthorized access to unencrypted customer information is presumed to be acquisition unless there is reliable evidence it was not. They also document whether a Florida breach occurred (POL-03 4.4).

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure (IP addresses, domains) at the campus firewall and in the cloud network rules.
2. Disable compromised accounts. Rotate the integration service account secret and every vendor API key, and move them into the key management service (POAM-012).
3. If a SAIG workstation or a Department system account may be involved, stop transmissions from it and follow FSA's instructions for resetting SAIG and Department system credentials.
4. Rebuild affected endpoints and cloud virtual machines from clean images and patch them before reconnecting. **Do not decrypt and reuse them.**
5. Have the servicer confirm that its 6 FAMS administrator accounts are reset and protected by MFA before they reconnect (POAM-001).
6. Confirm with forensics that persistence mechanisms are removed before recovery starts.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice before it goes out. The Campus President approves all external messages.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Campus President and Board chair informed; insurer notified; counsel engaged | IT Director; Campus President |
| Immediately on suspicion (day 0) | **FSA breach report** through the Cybersecurity Breach Intake Form and CPSSAIG@ed.gov, then updates as facts develop | Director of Financial Aid |
| Day 0-2 | Voluntary report to the FBI (field office or IC3) and CISA | IT Director |
| Day 0-2 | Staff briefing script: what happened, how to work during the outage, and not to discuss the incident outside the college | Campus President |
| Day 0-3 | Holding message to students on the text alert service and the website if services are down (no details on data until counsel approves) | Campus President |
| As soon as facts allow | Written determinations: notification event, discovery date, number of consumers, Florida breach determination date (POL-03 4.4) | Qualified Individual with counsel |
| **No later than 30 days after discovery** (sooner if possible) | **FTC notice** on the ftc.gov form if 500 or more consumers are involved. Include any written law enforcement delay determination | Qualified Individual with counsel |
| **No later than 30 days after determination** | **Florida notices:** each affected Florida resident by mail or email, and the Department of Legal Affairs if 500 or more Floridians are affected. The consumer reporting agencies get notice without unreasonable delay if more than 1,000 people are notified | Campus President and counsel |
| With the Florida notices | Notices to former students and parent borrowers in other states, under each state's law | Counsel |
| Within 14 days of the individual notices | Registrar records the unauthorized disclosure in each affected student's FERPA disclosure record (34 CFR 99.32) | Registrar |
| Next annual report (October) | The event and management's response go into the Qualified Individual's written report to the Board (314.4(i)(2)) | Qualified Individual |

**Plan to the earliest clock.** FSA must hear immediately. The FTC's 30 days run from **discovery**, which is often the day a staff member reports the phishing click, and that can be well before the Florida 30 days start at **determination**. There is no federal rule that requires this college to notify students individually. That is why the Florida notice goes directly to residents rather than through the deemed-compliance path in 501.171(4)(g).

**Law enforcement delay.** A written request from law enforcement can delay the Florida individual notices (501.171(4)(b)). It does **not** remove the FTC notice. The FTC notice still goes in on time and includes the determination (314.4(j)(1)(vi)).

**Ransom decision.** Requires the Board chair, counsel, the insurer, and an OFAC sanctions check (POL-03 4.6). Paying does not remove any notification duty if data was taken.

**Not in effect:** CIRCIA reporting to CISA (72 hours, or 24 hours after a ransom payment) is only proposed. It is voluntary until a final rule is published.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 6):
1. Identity provider and administrator access (break-glass accounts if needed). Target 1 hour.
2. Clean endpoints for the registrar, financial aid, and business office from the 6 pre-imaged spares. Target 4 hours.
3. SIS access (vendor-hosted). Confirm the vendor's integrity statement and that all sessions were revoked. Target 8 hours. Registrar uses printed rosters and a paper add/drop log meanwhile.
4. LMS access (vendor-hosted). Target 8 hours. Faculty extend deadlines for online students.
5. Email suite. Target 4 hours after identity is restored.
6. FAMS access and a clean SAIG workstation with the Department-provided software, coordinated with FSA. Target 24 hours.
7. Integration server and file server. Restore from a verified clean backup. **Do not restore the old standing aid exports** (POAM-003). If the backups were destroyed, rebuild the integration from the vendor connectors and re-key urgent data by hand between the SIS and FAMS. Target 24 hours.
8. Campus network and internet. Target 24 hours.
9. Admissions CRM. Target 24 hours.
10. Reporting database. Rebuild from SIS exports **without** ISIR fields (POAM-025). Target 72 hours.
11. Payroll. Target 72 hours.

**Refund deadline.** Title IV credit balances must still be paid no later than 14 days after they occur (34 CFR 668.164(h)(2)). Before releasing held refunds, the Business Office Manager checks every bank detail change made during the incident window with the student by phone. If the SIS is down, urgent refunds are calculated from FAMS award letters and paid by check (P05 BP-04).

**Validate before reconnecting:** the host is clean, credentials are rotated, and the system is patched. Tell staff and students when each service is back (RC.CO). Keep the manual workarounds running until each process meets its RTO.

## 8. Post-incident (ID.IM)
- Hold a lessons-learned meeting within 14 days of recovery. POL-03 4.8 requires documentation within 30 days of closing the incident.
- **Remediation requirements (314.4(h)(5)):** record every weakness the incident exposed as a POA&M item with an owner and date (P07). Update the risk register, especially R-001, R-002, R-013, and R-019 (P01).
- **Evaluate and revise (314.4(h)(7)):** update this runbook, POL-03, and the notification matrix, and retrain staff on what the phishing email looked like (AT-2).
- Report the event and the response to the Board in the next written report (314.4(i)(2)).
- Keep all incident records, notices, and determinations for at least 5 years. This covers the 5-year retention of any Florida no-harm determination (501.171(4)(c)).
