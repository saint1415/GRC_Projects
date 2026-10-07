# Incident Response Runbook: Cloud Credential Compromise Exposing Customer Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher) |
| Tier / Vertical | Micro / Information |
| Incident type | Cloud credential compromise exposing customer data: the long-lived CI/CD cloud key is stolen from the contract developer's personal laptop by information-stealing malware and used to download the document bucket (including W-9s with Social Security numbers) and copy a database snapshot to an outside account |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Related risk and POA&M | P01 R-001 (Very High), R-003, R-009; P07 POAM-004, POAM-005, POAM-009, POAM-011, POAM-014 |
| Runbook owner | CTO (security and compliance lead) |
| Approved | 2026-09-15 by the Chief Executive Officer |
| Last tested | Not yet. First tabletop with the MSP on 2026-11-12 (POAM-009) |

## 0. Roles and notification chain (Govern)
The company has 7 people. The CTO and the Senior Software Engineer do the cloud work; the MSP handles the laptops and the productivity suite; the cyber insurer supplies breach counsel and forensics. The CTO runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander and technical lead | CTO | Senior Software Engineer | Mobile phone (numbers on the contact sheet) |
| Evidence capture in the cloud account | Senior Software Engineer | CTO | Mobile phone |
| Notice decisions and clocks | Operations and Finance Manager (privacy lead) | Chief Executive Officer | Mobile phone |
| Executive approval (statements, spending, extortion) | Chief Executive Officer | CTO | Mobile phone |
| Customer communications | Customer Success Manager | Account Executive | Sends only approved text |
| Laptops and productivity suite | MSP incident line (number in the MSP contract) | MSP lead technician's mobile | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance broker | Policy number and hotline on the contact sheet |
| Breach counsel and forensics | Insurer panel counsel; panel forensic firm | Outside counsel (DPA author) | Assigned by the insurer on the first call |
| Contract developer | Contract developer's mobile | n/a | Phone |
| Law enforcement | FBI field office or IC3 | CISA | Numbers on the contact sheet |

**Notification chain in the first hour:** whoever notices → CTO → Senior Software Engineer, Chief Executive Officer, and Operations and Finance Manager (at the same time) → insurer hotline (Operations and Finance Manager) → panel counsel and forensics (through the insurer) → MSP incident line (CTO) to check laptops and the suite.

**Out-of-band first.** Assume the attacker may also hold suite or repository sessions. Coordinate on personal phones by call and text, using the printed contact sheet kept by the CTO and the Chief Executive Officer and a copy in the password manager.

## 1. Preparation checks (Identify / Protect)
- [ ] No long-lived cloud access keys exist; CI uses short-lived federated credentials (IA-5). **Gap until POAM-004 closes (2026-10-15)**
- [ ] No company data or keys on the contractor's personal laptop; contractor on a company laptop (SA-3(2), PS-7). **Extracts deleted 2026-08-28; laptop and terms due with POAM-014**
- [ ] Object read logging on the document bucket, database audit logging, and provider threat detection with alerts (AU-2, SI-4). **Gap until POAM-005 closes (2026-11-30)**
- [ ] Cloud logs archived 1 year in a separate account (AU-11). **Gap until POAM-005 closes.** Until then, export logs at once in step 3.2: the default history is 90 days
- [ ] Backups in a separate account with write-once retention (CP-9). **Gap until POAM-007 closes**
- [ ] Customer security contact list, with the 2 anchor customers flagged (IR-6). **Gap until the POAM-009 contact list milestone (2026-10-31)**
- [ ] Customer notice templates approved by counsel (initial notice, update, final report, Florida third-party-agent notice)
- [ ] This runbook, the notification matrix, and the contact sheet stored outside the production account and the suite

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Cloud provider email saying an access key was found exposed, or the key used from an unusual location | Provider notice; threat detection (after POAM-005) | Treat the key as compromised; go to section 3 |
| Sudden data transfer charges or an unexpected bill increase | Billing alert | Check for bulk downloads from the document bucket and snapshot copies |
| Snapshot shared or copied to an unknown account; new keys or users created | Management event log; alerts (after POAM-005) | Declare an incident |
| The contractor or an employee reports malware, a strange browser sign-in, or a stolen laptop | Staff or contractor report (POL-03 4.2) | Assume every secret on that device is stolen |
| Email or message claiming to hold customer documents, or vendors' tax IDs seen for sale | Support desk, security contact, a customer | Do not reply. Preserve the message. Declare an incident |

**Declare a SEV-1 incident when** any cloud credential is confirmed used by someone other than the company, or customer data is confirmed or reasonably believed to have been read or copied by an unauthorized party.

**Record two times in the incident log:** the time of **discovery** (when anyone at the company first knew or had reason to believe) and the time of **confirmation**. The DPA's 72-hour clock runs from confirmation. Florida's 10-day third-party-agent clock runs from "the determination of the breach of security or reason to believe the breach occurred" (Fla. Stat. 501.171(6)(a)). Other states' maintainer duties are often "immediately" after discovery, so plan to the earliest clock.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Deactivate (do not delete) the compromised key and every other long-lived key in the account. Pause CI/CD deployments | CTO | Keys inactive; pipeline paused |
| 2. Export the management event log (full 90 days) and any application logs from the error tracking service (14 days) to a restricted evidence folder outside the production account | Senior Software Engineer | Export hash recorded in the incident log |
| 3. Revoke any snapshot sharing and list every snapshot copy or share in the last 90 days | Senior Software Engineer | Sharing list attached to the log |
| 4. Look for persistence: new users, keys, roles, trust relationships, compute resources, or logging changes. Remove only after evidence is captured | CTO | Findings logged |
| 5. Call the insurer's breach hotline and give the claim details; counsel and forensics assigned | Operations and Finance Manager | Claim number issued |
| 6. Tell the contractor to disconnect the personal laptop from the internet and keep it powered on for forensics; call the MSP to check company laptops and suite sign-ins for the same malware or stolen sessions | CTO | Contractor device isolated; MSP check under way |
| 7. Start the incident log and the notice clock sheet (section 6) | CTO; Operations and Finance Manager | Log open |

## 4. Analysis (RS.AN)
Led by the panel forensic firm through breach counsel, with the CTO and Senior Software Engineer supplying access and logs.
1. **Timeline of the key.** From the exported event log, list every action by the key: first use from an unknown address, listings, snapshot copies or shares, writes, and deletes. Compare source addresses with the CI service's published ranges.
2. **Documents.** Object read logging is off today (POAM-005), so the company cannot see which files were downloaded. **Assume every document the key could read during the exposure window was taken** (about 165,000 files across all 45 customers, and the 2 former customers whose data was not deleted) unless forensics proves otherwise, for example from data transfer volumes.
3. **Database snapshot.** A copied snapshot holds every tenant: vendor records and contacts, extracted fields (including full TINs until POAM-012 closes), and customer user accounts with hashed passwords.
4. **Data elements and who is affected.** For each customer, produce counts by state of individuals whose name and Social Security number were exposed (W-9s of sole proprietors), plus vendor contact counts. In Florida, a name with a Social Security number is personal information (501.171(1)(g)1.a.(I)). Counsel checks each other state's definition.
5. **Integrity.** The key had write rights. Compare bucket contents and database records with the last pre-incident snapshot to confirm nothing was changed. A changed certificate or status could let an uninsured vendor on a site.
6. **Contractor's laptop.** Forensics identifies the malware and what else it took (browser sessions, the email delivery API key, repository tokens). Every secret found there is treated as stolen.
7. **Breach determination.** Counsel decides, state by state and customer by customer, whether a breach of personal information occurred. The DPA notice to customers is required either way.

## 5. Containment and eradication (RS.MI)
1. Delete the compromised key after evidence capture. Replace CI access with short-lived federated credentials scoped to deployment (the POAM-004 design). Do not issue new static keys.
2. Rotate every secret the CI service or the contractor's laptop could read: the database password, the email delivery and model provider API keys, repository tokens, and any vault entries the contractor could open, including the root account password.
3. Force a password reset and session revocation for all customer users, starting with customer administrators, and for all staff in the suite and repository (MSP for the suite).
4. Block the attacker's source addresses in account policy. Ask the cloud provider's abuse team to act on any account that received a shared snapshot.
5. Remove the contractor's access until the contractor works on a company-issued, MSP-managed laptop (POAM-014).
6. Redeploy production from reviewed code with the new credentials. Confirm with forensics that no persistence remains.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every legal notice before it goes out. The Chief Executive Officer approves all external statements (POL-03 4.8). Do not say "no data was accessed": without object read logs the company cannot prove it.

| Clock (from) | Action | Owner |
|---|---|---|
| Hour 0 (discovery) | Insurer and counsel engaged; incident log started; MSP checking laptops and the suite | Operations and Finance Manager; CTO |
| Day 0 to 2 | Voluntary report to the FBI (IC3 or field office) and CISA. It also serves as the law enforcement consultation Florida requires before any written "no harm" determination (501.171(4)(c)) | CTO with counsel |
| As soon as confirmed | Short initial notice to every affected customer's security contact; this also starts the support the customers need for their own notices | Customer Success Manager with approved text |
| Within 72 hours of confirmation | DPA notice to all affected customers: what happened, data involved, actions taken, contact for questions | Customer Success Manager |
| No later than 10 days after determination | Florida third-party-agent notice to each customer with affected Florida individuals, with all the information the customer needs for its own notices (501.171(6)(a)): per-customer lists of affected individuals by state, data elements, dates, and a contact | Operations and Finance Manager |
| As each state requires | Other states: counsel confirms each state's maintainer duty; customers give resident notices for their vendors; the company sends notices for a customer only on that customer's written request (501.171(6)(b)) | Operations and Finance Manager and counsel |
| No later than 30 days after determination | Company-owned data only (customer user credentials, if counsel finds hashed passwords are not "secured"): Florida individual notice, or a written "no harm" determination sent to the Department of Legal Affairs; Department notice if 500 or more Floridians | Operations and Finance Manager and counsel |
| Every 72 hours until closure | Status updates to customers; final incident report within 30 days of closure | CTO |
| Before any public statement | Review the website security page and questionnaire answer library against the facts (P03 G-032, G-040) | Chief Executive Officer |

**Plan to the shortest clock.** For this company, the 72-hour DPA clock comes first, and the Florida 10-day clock comes next. Customers face their own 30-day Florida deadline from their determination, so the faster the company gives them complete lists, the more time they have.

**Extortion demand:** only the Chief Executive Officer can decide, with counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove any notice duty.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Responder access: suite identity and cloud console accounts checked and passwords rotated; the sealed emergency account if needed
2. Managed database: if integrity checks fail, restore to the last verified point in time
3. Application tier and document bucket: redeploy from reviewed code with new credentials; restore any altered documents from versions (once versioning is on, POAM-007)
4. Status page and monitoring, with customer updates
5. Email delivery with a rotated API key; re-run expiry reminders
6. Support desk
7. CI/CD with federated credentials only
8. Compliance reports
9. Corporate SaaS and billing

**Validate before resuming deployments:** no long-lived keys remain, threat detection and bulk-download alerts are on, all rotated secrets are in the secrets manager, and the contractor has no access from a personal device. Tell customers when the platform and their data are verified (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closure, with the MSP, counsel, and the contractor. Written summary within 30 days (POL-03 4.12).
- Update the risk register (P01, especially R-001, R-003, R-009, R-024), the POA&M (P07), and this runbook.
- Review every public statement and the questionnaire answer library against what the incident showed (POL-02 A.4).
- Keep the incident log, notices, and any "no harm" determination for at least 5 years (Fla. Stat. 501.171(4)(c) sets 5 years for the determination).
