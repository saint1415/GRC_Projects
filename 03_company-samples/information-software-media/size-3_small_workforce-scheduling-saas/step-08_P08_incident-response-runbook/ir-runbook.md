# Incident Response Runbook: Cloud Credential Compromise Exposing Customer Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher) |
| Tier / Vertical | Small / Information |
| Incident type | Cloud credential compromise exposing customer data: a leaked long-lived CI/CD cloud access key is used to read payroll export files and copy a database snapshot |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Related risk and POA&M | P01 R-001 (High), R-031; P07 POAM-005 to POAM-008, POAM-015, POAM-016 |
| Runbook owner | IT Manager (security and compliance lead) |
| Approved | 2026-09-22 by the Chief Executive Officer |
| Last tested | Not yet. First tabletop exercise 2026-11-18 (POAM-015) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | CTO | On-call page, then the out-of-band incident bridge on personal phones |
| Technical lead | Platform Engineering Lead | Senior on-call engineer (one of the 6 with production access) | On-call page |
| Notification decisions | COO (privacy lead) | CTO | Mobile phone |
| Legal counsel | Outside privacy counsel (retainer) | Breach counsel from the insurer's panel | Counsel's emergency line (in the contact sheet) |
| Cyber insurer | Carrier breach hotline | n/a | Policy number and hotline in the contact sheet |
| Forensics | Firm on the insurer's panel (retainer due 2026-11-30, POAM-015) | n/a | Through the insurer or counsel |
| Customer communications | Customer Support Manager | Director of Product | Mobile phone; sends only approved text |
| Executive approval | Chief Executive Officer | CTO | Mobile phone |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the contact sheet |

**Out-of-band first.** Assume the attacker may be able to read company chat or tickets if the compromise spreads. Use the out-of-band incident bridge and the contact sheet kept in the secrets vault and printed by the IT Manager and CTO.

## 1. Preparation checks (Identify / Protect)
- [ ] No long-lived static cloud access keys exist; CI uses short-lived federated credentials (IA-5). **Gap until POAM-005 closes (2026-10-16)**
- [ ] Provider threat detection and alerts for unusual API calls, bulk object reads, and snapshot copy or share are on (SI-4). **Gap until POAM-007 closes**
- [ ] Object-level access logging on the payroll export bucket and database audit logging are on (AU-2). **Gap until POAM-006 closes**
- [ ] Cloud audit logs are archived for 1 year in a separate log account (AU-11). **Gap until POAM-008 closes.** Until then, export logs at once in step 3.2: the default history is 90 days
- [ ] Backups are in a separate account with write-once retention (CP-9). **Gap until POAM-014 closes**
- [ ] Security contact list for every customer, with the 3 customers on 48-hour notice flagged (IR-6). **Gap until POAM-016 closes (2026-10-31)**
- [ ] Customer notice templates approved by counsel (initial notice, update, final report)
- [ ] Forensic retainer and insurer panel confirmed (POAM-015)
- [ ] This runbook, the notification matrix, and the contact sheet stored outside the production account

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Alert: API calls with a CI key from an address outside the CI service's ranges | Provider threat detection (after POAM-007) | Page on-call; open a SEV-1 candidate ticket |
| Alert: bulk reads from the payroll export bucket, or a snapshot copied or shared to an unknown account | Custom alerts (after POAM-007) | Page on-call; open a SEV-1 candidate ticket |
| Secret-scanning alert: a cloud key found in a public repository, paste site, or build log | Source hosting secret scanning; cloud provider's exposed-key notice | Treat the key as compromised; go to section 3 |
| Unexpected cloud cost spike or new resources in an unused region | Billing alert; provider inventory | Check whether a key is being misused |
| A customer, researcher, or journalist reports company data for sale or a data-theft extortion demand arrives | Support, security contact mailbox, email | Preserve the message; declare the incident |

**Declare a SEV-1 incident when** a cloud credential is confirmed used from an unknown source, or customer data is confirmed or reasonably believed to have been read or copied by an unauthorized party.
**Record two times in the incident log:** the time of discovery (when anyone at the company first knew or had reason to believe) and the time of confirmation. The DPA's 72-hour and 48-hour customer clocks run from confirmation. Florida's 10-day third-party-agent clock runs from "determination of the breach or reason to believe the breach occurred" (Fla. Stat. 501.171(6)(a)). California's service-provider duty is "immediately following discovery" (Cal. Civ. Code 1798.82(b)).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Deactivate (do not delete) the compromised key and every other long-lived key in the account. Pause CI/CD deployments | Technical lead | Keys inactive; pipelines paused |
| 2. Export cloud audit logs for the full default history (90 days) and the logging SaaS logs to a separate evidence location with restricted access | Technical lead | Export hash recorded in the incident log |
| 3. Revoke any snapshot sharing, and list every snapshot copy or share made in the last 90 days | Technical lead | Sharing list attached to the ticket |
| 4. Look for persistence: new identities, keys, roles, trust relationships, compute resources, or changes to logging settings. Remove only after evidence is captured | Technical lead | Findings logged |
| 5. Call the cyber insurer's hotline and outside privacy counsel. Engage forensics through them | COO | Claim number issued; counsel engaged |
| 6. Start the incident log and the customer notice clock sheet (section 6) | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Timeline of the key.** Using the exported audit logs, list every action by the compromised key: first unknown-source use, reads, copies, snapshot shares, writes, and deletes. Compare source addresses with the CI service's published ranges.
2. **Payroll export files.** Object-level access logs are off today (POAM-006), so the company cannot see which files were read. **Assume every file the key could read during the exposure window was taken** unless forensics shows otherwise. Files go back to 2022 because there is no lifecycle rule (POAM-018), which widens the scope.
3. **Database snapshot.** A copied snapshot contains every tenant: about 310 current customers, the 14 former customers whose data was not deleted, about 140,000 worker profiles, and customer administrator accounts.
4. **Data elements.** Worker names, work email, mobile phone, employee ID, job role, work location, availability, schedules, time punches, pay rates, preferred language, and salted, hashed passwords. No Social Security numbers, health data, geolocation, or payment card data.
5. **Integrity.** The key had write access. Compare payroll export files and database tables against object versions and point-in-time recovery to confirm nothing was altered. Altered exports could cause wrong pay.
6. **Breach determination.** Counsel decides, state by state, whether the data elements meet each law's definition of personal information. Under the Florida and California definitions, a name counts only when combined with listed elements such as a government ID number, a financial account number with its access code, or medical, health insurance, or biometric data (and geolocation in Florida). The platform holds none of these. The deciding question is usually whether a user name or email address with a salted, hashed password "would permit access to an online account" (Fla. Stat. 501.171(1)(g)1.b.; Cal. Civ. Code 1798.82(h)(2)). The contractual notice to customers is required either way.

## 5. Containment and eradication (RS.MI)
1. Delete the compromised keys after evidence capture. Replace CI access with short-lived federated credentials scoped per pipeline job (the POAM-005 design). Do not issue new static keys.
2. Rotate every secret the CI service could read: third-party API keys (SMS, email, model provider), database credentials, and signing keys.
3. Force a password reset for all platform accounts whose hashes were in the snapshot, starting with customer administrators, and revoke all sessions.
4. Block the attacker's source addresses at the web application firewall and in account policy. Ask the cloud provider's abuse team to act on any account that received a shared snapshot.
5. Rebuild the CI runners and redeploy production from reviewed code and freshly built images. Confirm with forensics that no persistence remains.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside privacy counsel confirms every legal notice before it goes out. The Chief Executive Officer approves all external statements.

| Clock (from) | Action | Owner |
|---|---|---|
| Hour 0 (discovery) | Insurer and counsel engaged; incident log started | COO |
| Immediately after discovery | California: notify each customer whose California workers' personal information was acquired (Cal. Civ. Code 1798.82(b)). In practice, send a short initial notice to all affected customers as soon as the incident is confirmed | COO and Customer Support Manager |
| Day 0 to 2 | Voluntary report to the FBI (IC3 or field office) and CISA. This also serves as the law enforcement consultation Florida requires before a "no harm" determination (501.171(4)(c)) | Incident commander |
| Within 48 hours of confirmation | DPA notice to the 3 enterprise customers with 48-hour terms | Customer Support Manager |
| Within 72 hours of confirmation | DPA notice to all other affected customers: what happened, data involved, actions taken, contact for questions | Customer Support Manager |
| No later than 10 days after determination | Florida third-party-agent notice to each customer with affected Florida residents' personal information, with the details the customer needs for its own notices (501.171(6)(a)) | COO |
| No later than 30 days after determination | Only for data the company owns (for example, customer administrator credentials): Florida individual notice and, if 500 or more Floridians, Department of Legal Affairs notice, or a documented "no harm" determination sent to the Department within 30 days | COO and counsel |
| As each state requires | Other states: support customers' resident notices; counsel checks each state where affected workers reside | COO and counsel |
| Ongoing | Status updates to customers at least every 72 hours until closure; final incident report within 30 days | Incident commander |

**Plan to the shortest clock.** The 48-hour contract clock and the California "immediately" duty come first. Send a short initial notice when the facts are thin, then update. The DPA says the company notifies customers; customers decide on their own notices to workers, and the company provides the data they need.

**Public statements.** Review the website security page before any public statement. After this incident, the claim that "every access is logged" (P03 G-032) must not be repeated unless it is true.

**Extortion demand:** requires the Chief Executive Officer, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove any notice duty.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Responder access through the identity provider (sealed emergency cloud accounts if needed)
2. Managed database: if integrity checks fail, restore to the last verified point in time
3. Application tier and punch ingestion: redeploy from reviewed code with new credentials
4. Status page and monitoring, with customer updates
5. Schedule views and payroll exports: re-generate any export file that fails integrity checks and tell the affected customers before their payroll cut-off
6. Notification delivery with rotated SMS and email keys
7. Support tooling
8. CI/CD with federated credentials only
9. Corporate SaaS
10. AI assistant with a rotated model provider key

**Validate before resuming deployments:** no static keys remain, threat detection and bulk-read alerts are on, and all rotated secrets are in the secrets manager. Tell customers when services and exports are verified (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closure; documented within 30 days (POL-03 4.9).
- Update the risk register (P01, especially R-001, R-031, R-009, R-010), the POA&M (P07), the SOC 2 incident log (P09, CC7.4 and CC7.5), and this runbook.
- Review the website security page and questionnaire library against what the incident showed (POL-01 4.10).
- Keep all incident records, notices, and "no harm" determinations for at least 5 years (Fla. Stat. 501.171(4)(c) sets 5 years for the determination).
