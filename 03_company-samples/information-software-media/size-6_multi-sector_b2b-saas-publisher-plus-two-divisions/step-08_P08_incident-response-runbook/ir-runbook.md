# Incident Response Runbook: Cloud Credential Compromise Exposing Customer and Payroll Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Information |
| Incident type | Cloud credential compromise exposing customer data: a static cloud key from the consulting data migration toolkit leaks and is used to copy files from the Workforce Cloud Platform (WCP) export bucket, including payroll handoff files owned by the Payments and Payroll division |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-17 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The multi-division notification matrix has not been exercised** (scenario gap 7); the first cross-division tabletop, using this scenario, is on 2026-12-08 (POAM-004) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** a consultant copies migration scripts, including one of the 37 static toolkit keys, to a personal public code repository (against POL-05 4.3). Group secret scanning does not cover personal repositories (P04 finding 3). An automated scanner run by criminals finds the key within hours.
- **Access:** over 3 days the attacker uses the key from cloud-hosted servers to list and download objects from the export bucket. The key can read every tenant prefix (P07 AC-03). No alert fires: the bucket has no read logging and the SOC has no bulk-read detection (P07 AU-12, SI-04).
- **Discovery (Day 0, a Tuesday):** the cloud provider's abuse team emails the group that a key belonging to the group was published in a public repository. The SOC also sees an unusual egress charge from the export bucket account.
- **What could be read:** about 14 months of payroll handoff files for 6,800 embedded-payroll employers (about 1.1 million workers: names, Social Security numbers, bank routing and account numbers, gross pay), and HR exports from 410 Workforce Cloud tenants (about 640,000 workers: names, contact details, job, pay rates, and for some HR core tenants, dates of birth and Social Security numbers). After removing overlaps, about **1.35 million people in all 50 states**, about **118,000 of them Florida residents** (about 95,000 in the handoff files).
- **Why encryption does not help:** the files were encrypted at rest with provider-managed keys, so the storage service decrypted them for any principal with read access, including the stolen key. Counsel treats the data as acquired in unencrypted form. Under 16 CFR 314.2(m), unauthorized access to unencrypted customer information is presumed to be acquisition unless the division has reliable evidence that it was not. Without read logs, there is no such evidence.
- **Follow-on fraud (Day 2):** the payroll anomaly model flags a spike in direct deposit change attempts on workers named in the stolen files (P01 GR-06).

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC and cloud platform teams | Forensic firm on retainer (insurer panel) | SOC bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division general counsels | Out-of-band bridge |
| Cloud Software decisions (customer and bank notices) | Cloud Software division CISO | Cloud Software customer support vice president | Division bridge |
| Payments and Payroll decisions (FTC, sponsor banks, employers) | Payments and Payroll division CISO (Qualified Individual) | Payments and Payroll chief compliance officer | Division bridge |
| Technology Consulting (root cause; other toolkit keys) | Technology Consulting security and compliance lead | Technology Consulting delivery executive | Division bridge |
| SEC materiality | Disclosure committee | Group Chief Financial Officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA (voluntary) | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker may hold other credentials. Use the crisis line and managed mobile devices. The printed binder in each division's command center holds contacts, this runbook, and the notification matrix.

## 2. Preparation checks (Identify / Protect)
- [x] 24x7 SOC with cloud control-plane logs and EDR on WCP workloads (SI-3, SI-4)
- [x] Immutable WCP and payroll engine backups in provider B (CP-9; P07 satisfied)
- [x] Forensic retainer and insurer panel confirmed
- [x] Disclosure committee charter includes cybersecurity materiality
- [ ] No static keys that can read customer exports (**gap until POAM-001 closes**)
- [ ] Object-level read logging and bulk-read alerts on the export bucket (**gap until POAM-003 and POAM-008 close**)
- [ ] Handoff files in a dedicated channel with 7-day retention (**gap until POAM-006 and POAM-007 close**)
- [ ] Notification matrix complete with 48-hour customers, bank-designated contacts, sponsor bank terms, and the FTC notice, and exercised (**gap until POAM-004 closes**)
- [ ] Intercompany agreement naming who notifies whom for handoff data (**gap until POAM-020 closes**)

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Provider or researcher report that a group key is public | Email to the security mailbox; provider abuse notice | **Revoke the key within 1 hour (POL-03 4.9)**, then investigate |
| Secret found by group scanning in any repository or workspace | Secret scanning | Revoke; open an incident |
| Unusual egress volume or cost from a storage account | Cloud billing alerts; network telemetry | Triage as possible exfiltration |
| Key used from a network never seen before | SIEM (after POAM-003) | Disable the key; start triage |
| Spike in direct deposit changes or account takeovers on the self-service app | Payroll anomaly model; WCP fraud signals | Treat as possible downstream use of stolen data |
| Extortion email or leak-site post naming a division | Email; threat intelligence | Declare Severity 1; preserve the message |

**Severity 1** (group scale, POL-03 4.2): confirmed exfiltration of Restricted data (Social Security numbers and bank details), affecting more than one division.

**Record the discovery date for each duty.** Under POL-03 4.4, the clock for every notice starts at the earliest date any group workforce member knew or should have known. For the FTC notice, a notification event is treated as discovered on the first day it is known to any employee, officer, or other agent of the division (16 CFR 314.4(j)(2)); because the SOC and the Cloud Software division act for Payments and Payroll here, **this runbook treats Day 0 as the discovery date for every division.** Counsel may refine this, but no clock is planned from a later date.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Revoke the leaked key and every other toolkit key; disable the consultant's access pending review | Group identity director; consulting security lead | Keys revoked (target: within 1 hour of the report) |
| 2. Block public access paths to the export bucket except from the payroll engine's and customers' known endpoints | Group cloud platform director | Bucket policy changed |
| 3. Suspend the export service and rotate credentials for all 2,100 integrations that read it; tell Payments and Payroll the handoff will be late | Cloud Software integrations director | Integrations re-keyed (actual: 9 hours) |
| 4. Turn on object-level read logging now (it will not show past reads, but it shows any further access) | Group cloud platform director | Logging confirmed |
| 5. Request provider-side access records and preserve control-plane logs, billing records, and the public repository on legal hold | SOC; forensic firm | Evidence list signed |
| 6. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 7. Notify the Payments and Payroll Qualified Individual **on the bridge** within 1 hour (POL-03 4.3) | Incident commander | Acknowledged |
| 8. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.6) | Group CISO | Committee convened |
| 9. Put the payroll anomaly model on heightened review: hold first pay to any bank account changed since Day -3 for workers in the affected employers | Payroll operations director | Rule live |

## 5. Analysis (RS.AN)
1. **Scope by object, not by guess.** Without read logs, scope is "everything the key could read" unless provider records or egress volumes give reliable evidence otherwise. Forensics compares the total egress (about 9 TB) with object sizes per prefix. In this scenario the volume is consistent with near-complete copying, so the group presumes every object under the readable prefixes was taken.
2. **Map objects to data owners.** Handoff files belong to Payments and Payroll (for each employer); HR exports belong to each Cloud Software customer. One person can appear in both.
3. **Individuals by state.** For each data owner, count affected individuals by state of residence. These counts drive state notices, the Florida Department notice (500 or more Floridians per covered entity), and consumer reporting agency notices (more than 1,000).
4. **Data elements by state law.** Names with Social Security numbers are personal information in Florida and generally elsewhere; bank account numbers without access codes may not be, depending on the state. Counsel runs the element test state by state.
5. **Disruption test for banks.** The 9-hour export suspension delayed payroll exports for about 420 bank customers. Counsel determines whether this materially disrupted their covered services for 4 or more hours (12 CFR 53.4). In this scenario, the answer is yes for banks whose payroll ran that night.
6. **Root cause:** the static key, the policy breach (personal repository), the all-tenant read permission, and the missing read logs. Feed these to P01 GR-01 and the POA&M.

## 6. Containment and eradication (RS.MI)
1. Replace toolkit keys with per-project, per-tenant short-lived credentials before any migration resumes (accelerates POAM-001).
2. Move handoff files to the payroll engine's intake now, using the planned design, and delete all handoff files older than 7 days from the export bucket after counsel confirms evidence is preserved (accelerates POAM-006 and POAM-007).
3. Search all public code sites for other group secrets; revoke anything found.
4. Confirm with forensics that the key was not used against any other resource (control-plane logs show list and read calls only on the export bucket).
5. Reset nothing that workers cannot reset themselves; instead, require re-verification for bank changes on affected workers' accounts for 90 days.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (25 rows).** Counsel approves every notice. The matrix has three layers:
1. **Inside the group:** Cloud Software, as custodian, tells Payments and Payroll, as data owner (row 1). Without an intercompany agreement (gap 5), the Group General Counsel decides who sends which customer notices; this runbook sets it now: Cloud Software notifies its customers about HR exports; Payments and Payroll notifies employers about handoff files.
2. **To customers and banks:** DPA notices (48 or 72 hours), bank service provider notices, sponsor bank A (24 hours), and third-party agent notices under state law (Florida: within 10 days of determination, 501.171(6)(a)). Customers and employers are the covered entities for their workers' notices; the group offers to send those notices for them, as Florida allows (501.171(6)(b)), but the covered entity stays responsible.
3. **To regulators and investors:** the FTC notice for Payments and Payroll (16 CFR 314.4(j)), state notices, and the SEC materiality decision.

| When (from Day 0) | Action | Owner |
|---|---|---|
| Hour 1 | Key revoked; Payments and Payroll Qualified Individual on the bridge | Incident commander |
| Day 0 | Insurer, counsel, forensics engaged; voluntary report to FBI or IC3 | Group Chief Risk Officer; Group CISO |
| Day 0, as soon as the disruption is determined | Bank service provider notices to bank-designated contacts (CEO and CIO where no contact exists) | Cloud Software customer support vice president |
| Within 24 hours of determination | Sponsor bank A notice | Payments and Payroll chief compliance officer |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Within 48 hours of confirmation | Notices to the 61 affected customers with 48-hour DPA terms | Cloud Software (Group General Counsel approves) |
| Within 72 hours of confirmation | Notices to all other affected customers; notices to the 6,800 employers (Payments and Payroll uses the same 72-hour standard by policy) | Cloud Software; Payments and Payroll |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 10 days of determination | Florida third-party agent notices to customers and employers, with the information they need; apply each other state's agent rules the same way | Group General Counsel |
| Within 30 days of determination | Florida individual notices (15-day extension only with written good cause to the Department, and only for individual notices); Florida Department of Legal Affairs notice for each covered entity with 500 or more affected Floridians (no extension); consumer reporting agencies (more than 1,000); each other state's individual and regulator notices on its own clock | Customers and employers, or the group as their agent |
| Within 30 days of discovery | FTC notice through the form on ftc.gov (about 1.1 million consumers) | Payments and Payroll (Qualified Individual with counsel) |
| Next annual report | Reg S-K Item 106 description, reflecting any material effects | Group General Counsel |

**Plan to the shortest clock.** In this scenario the order is: bank service provider notices, sponsor bank A, the disclosure committee, 48-hour customers, 72-hour customers and employers, SEC (if material), Florida agent notices, then the 30-day individual, Department, and FTC notices. The FTC notice must not wait for the last state notice.

**Materiality factors for the disclosure committee:** number of people affected (about 1.35 million) and the sensitivity of the data (Social Security numbers and bank details); regulatory exposure (FTC under Part 314 and Section 5, state attorneys general, the CPPA, bank regulators through sponsor banks); customer contracts and churn among about 38,000 customers and 11,500 employers; costs of notification, identity protection, and fraud losses; and effects on the embedded payments strategy. Materiality is decided without unreasonable delay; the 4-business-day clock starts at the determination, not at discovery.

**Extortion:** if the attacker demands payment, the decision belongs to the board risk committee with counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove any notice duty, because the data was already taken.

**Communications to workers and customers:** plain-language notice of what was taken, what the group is doing, and what people should do (watch bank accounts, place fraud alerts, beware of calls asking to "confirm" bank details). Identity protection services are offered where state law requires it and as a matter of group policy for everyone whose Social Security number was in the files.

## 8. Recovery (RC.RP, RC.CO)
The export service is High for availability (P05 BP-SW03: RTO 4 hours) because payroll depends on it. Restore in this order:
1. Identity and landing-zone controls confirmed clean (BP-G01, BP-G03)
2. The new handoff channel into the payroll engine, so payroll can run (BP-SW03, BP-PY01): in this scenario the 9-hour suspension made 1,900 employers' ACH files miss one cutoff; sponsor bank A approved a same-day window the next morning
3. Customer export integrations, re-keyed with short-lived credentials (BP-SW04)
4. Consulting migrations, only after the new toolkit credentials are in place (BP-IC01)

Tell customers, employers, and bank customers when services are restored (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10).
- Update P01 (GR-01, GR-03, GR-06, SW-001, SW-003, IC-003, PY-001), the POA&M (POAM-001, POAM-003, POAM-004, POAM-006 to POAM-008, POAM-020), the notification matrix, and this runbook.
- Correct any public statement the incident proves untrue (POL-01 4.13), and tell the SOC 2 service auditor about the incident for the current period (P09).
- Retain all incident records for 6 years (POL-01 4.11).
