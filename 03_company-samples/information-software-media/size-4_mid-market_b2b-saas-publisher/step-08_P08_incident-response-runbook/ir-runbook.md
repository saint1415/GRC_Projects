# Incident Response Runbook: Cloud Credential Compromise Exposing Customer Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed B2B SaaS publisher of a multi-tenant customer service platform) |
| Tier / Vertical | Mid-Market / Information |
| Incident type | Cloud credential compromise exposing customer data: the long-lived key used by the data warehouse loader leaks from a contractor job configuration and is used to download customer attachments from production and to read the warehouse export staging bucket, which until 2026-10-31 also holds healthcare cell subject lines |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-platform-outage.md` (regional failure or destructive attack); `notification-matrix.csv`; BIA (P05); risk register (P01 R-001, R-002, R-004, R-010) |
| Runbook owner | Director of Security (incident commander) |
| Approved | 2026-09-29 by the Chief Technology Officer |
| Last tested | Not yet. Executive tabletop with outside counsel scheduled 2026-11-10, including a healthcare cell variant (POAM-014, POAM-020) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so technical, business, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Technology Officer. CEO, CFO, General Counsel, Director of Security, VP Platform Engineering, VP Customer Support, Chief Revenue Officer, VP People, outside breach counsel | External statements, customer notices, concessions, extortion response (recommendation to the CEO), resources |
| **Incident response team (IRT)** | Incident commander: Director of Security. VP Platform Engineering (technical lead), security engineers, detection engineer, MDR provider, forensic firm (through counsel), cloud provider support | Containment, investigation, eradication, recovery sequence |
| **Customer and legal cell** | General Counsel (chair), Associate General Counsel, Privacy, VP Customer Support, GRC Manager | Breach determinations, notice content and timing, covered entity and bank customer notices, decision log |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security | VP Platform Engineering | On-call page, then the out-of-band bridge on personal phones |
| Technical lead | VP Platform Engineering | Senior site reliability engineer on call | On-call page |
| CMT chair | Chief Technology Officer | Chief Executive Officer | Out-of-band group |
| Breach and notice decisions | General Counsel | Associate General Counsel, Privacy | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel) | Outside privacy counsel on retainer | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MDR provider incident response team | Through counsel |
| Customer notices | VP Customer Support (sends approved text) | Chief Revenue Officer (top accounts) | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | CFO | Phone |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume the attacker may see company chat, tickets, or email if the compromise spreads to workforce accounts. The CMT and IRT use a pre-provisioned messaging group on personal phones and the incident binder kept in the secrets vault and printed by the Director of Security and the CTO.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions. Do not speculate in tickets or chat.

## 1. Preparation checks (Identify / Protect)
- [ ] No long-lived cloud access keys exist; pipelines and the loader use federated short-lived credentials (IA-5). **Gap until POAM-002 closes (2026-10-31)**
- [ ] Object-level access logging on attachment storage and the export staging bucket; database audit logs (AU-2, AU-12). **Gap until POAM-004 closes (healthcare cell 2026-10-31; production 2026-12-31)**
- [ ] Detections for bulk object reads, unusual-source key use, and snapshot sharing, routed to the MDR provider (SI-4). **Gap until POAM-004 closes (2026-11-30)**
- [x] Cloud audit logs kept 1 year in the write-once log archive (AU-9; P07)
- [ ] Healthcare cell subject lines no longer exported (POAM-015, 2026-10-31)
- [ ] Security contacts on file for at least 95% of customers, with the 38 customers on 24-hour terms, the 46 covered entities, and the 9 banks flagged (POAM-014)
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-29
- [ ] Customer notice templates approved by counsel (initial notice, update, final report; covered entity version with 164.410(c) content)
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-20)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| API calls with a workload key from an address outside the expected ranges (cloud provider B or CI) | Provider threat detection; custom rule (after POAM-004) | MDR pages the incident commander within 30 minutes |
| Bulk reads of attachments or the export staging bucket | Object-level logs and alert (after POAM-004) | Page on-call; candidate severity 1 |
| A cloud key found in a public repository, paste site, or build log | Secret scanning; the cloud provider's exposed-key notice; bug bounty report | Treat the key as compromised; go to section 3 |
| New identities, keys, roles, or resources in an account; logging settings changed | Posture management; guardrail alerts | Investigate; declare if unexplained |
| A customer reports seeing data that is not theirs, or data for sale; an extortion email | Support; security mailbox; threat intelligence; FBI | Preserve the message; declare |

**Severity 1 (declare immediately):** a credential confirmed used from an unknown source against customer data stores, or customer data confirmed or reasonably believed to have been read or copied by an unauthorized party.

**Record two times in the incident log (POL-03 4.3):**
- **Discovery:** when any employee, officer, or agent first knew, or by reasonable diligence would have known. For healthcare cell data, this starts the business associate clock (45 CFR 164.410(a)(2)) and the 10-business-day BAA term.
- **Confirmation:** when the company confirmed a security incident affecting customer data. This starts the 24-hour and 48-hour DPA clocks. Florida's 10-day third-party agent clock runs from "determination of the breach or reason to believe the breach occurred" (Fla. Stat. 501.171(6)(a)).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | **Deactivate (do not delete)** the compromised key and every other long-lived key; pause the warehouse loader and CI deployments | Technical lead | Keys inactive; jobs paused |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log with discovery and confirmation times | Incident commander | Log open |
| 0-60 min | Call the insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | Chief Financial Officer | Claim number; counsel on the call |
| 0-60 min | Export cloud audit logs, object-level logs where enabled, and identity logs to the evidence account with hashes recorded (POL-03 4.9) | Technical lead with the detection engineer | Export hashes in the log |
| 0-2 h | Look for persistence: new identities, keys, roles, trust relationships, compute, snapshot shares, logging changes. Remove only after evidence capture | Security engineers | Findings logged |
| 0-2 h | Block attacker addresses at the WAF and in account policy; revoke sessions for any workforce identity linked to the leak (the contractor account) | Security engineers; Director of IT | Blocks in place |
| 1-2 h | Convene the CMT; first situation report (what was reachable, what is known to be taken, clocks running) | CMT chair | CMT meeting held |
| 2-4 h | Start the customer clock sheet: list of tenants whose attachments the key could read, the 38 customers on 24-hour terms, covered entities, banks | Customer and legal cell | Clock sheet open |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **What the key could reach.** The loader key reads every Standard and Enterprise attachment in production and the export staging bucket in the data analytics account. It cannot reach the healthcare cell's own storage or database. The healthcare subject lines in the staging bucket are the one path to PHI until POAM-015 closes.
2. **What the key did.** From the archived control-plane logs, list every action by the key: first unknown-source use, list and read calls, any writes, deletes, or new credentials. Compare source addresses with cloud provider B's published ranges.
3. **Which objects were read.** Object-level logging is off in production until POAM-004 closes, so the company cannot see which attachments were read. **Assume every object the key could read during the exposure window was taken** unless forensics can narrow it (for example from egress volume or the attacker's own leak samples). This decision drives notice scope and must be recorded in the decision log.
4. **Data elements.** Attachments can hold anything end consumers sent: images, invoices, order documents, identity documents, and in a few tenants, documents that would be personal information under state breach laws (for example a driver's license image or a financial account statement). Build the **affected tenants list**, and for each tenant the data types found by sampling, so counsel can decide which laws are triggered.
5. **Healthcare data.** If the staging bucket was read, the healthcare subject lines of the 46 covered entities may be PHI. This is presumed a breach unless the company demonstrates a low probability of compromise using the four factors in 45 CFR 164.402 (decision D1). Record which covered entities' rows were in the bucket.
6. **Integrity.** If the key had write access anywhere, compare objects against versions to confirm nothing was altered.
7. **Bank customers.** Determine whether any of the 9 banks' tenants were in scope. A confidentiality incident does not by itself trigger the 4-hour rule in 12 CFR 53.4, which is about disruption of covered services, but the banks' contracts require notice of security incidents (notification matrix).

## 5. Containment and eradication (RS.MI)
1. Delete the compromised key after evidence capture. Move the loader to workload identity federation with a metadata-only role (the POAM-002 design). Do not issue new long-lived keys.
2. Rotate every secret the contractor job or CI could read: third-party API keys (SMS, email, model provider), database credentials, webhook signing keys.
3. Remove the contractor job; review the contractor's repositories with secret scanning; revoke the contractor accounts involved.
4. Enable object-level logging in every customer data store immediately, even before POAM-004's full design, so further access is visible.
5. Ask the cloud provider's abuse team to act on any destination account the attacker used.
6. Forensics confirms no persistence remains before jobs and deployments resume.

## 6. Legal, regulatory, and customer communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every legal notice before it goes out. The General Counsel keeps the **decision log** (POL-03 4.5).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | For healthcare cell rows: is this a breach of unsecured PHI? Presumed yes unless the four-factor assessment shows a low probability of compromise. Encrypted data with uncompromised keys is not unsecured PHI, but the attacker read the data through an authorized key, so encryption at rest does not help | General Counsel with counsel | Decision log with the four factors |
| D2 | Discovery time (business associate and BAA clocks), confirmation time (DPA clocks), determination time (Florida third-party agent clock) | General Counsel | Decision log |
| D3 | Scope: which tenants; whether all readable objects are treated as taken; which covered entities; which banks; which customers have Florida or California residents in scope | Customer and legal cell | Affected tenants list |
| D4 | Has law enforcement asked for a delay? A written request delays notice for the period stated; an oral request must be documented and lasts no longer than 30 days unless confirmed in writing (45 CFR 164.412) | Counsel | Decision log |
| D5 | Does any data the company **owns** (customer administrator contacts, employee data) meet a state definition of personal information, making the company a covered entity under state law for that data? | Counsel | Decision log |
| D6 | Extortion demand response | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | Chief Financial Officer |
| As soon as the incident is confirmed | Short initial notice to affected customers when facts are thin, then updates. California example: a service provider must notify the data owner "immediately following discovery" when California residents' personal information was, or is reasonably believed to have been, acquired (Cal. Civ. Code 1798.82(b)) | VP Customer Support with counsel |
| Day 0-2 | Voluntary report to the FBI (IC3 or field office) and CISA through counsel | Incident commander |
| Within 24 hours of confirmation | DPA notice to the 38 Enterprise customers with 24-hour terms | VP Customer Support |
| Within 48 hours of confirmation | DPA notice to all other affected customers: what happened, data involved, actions taken, contact for questions | VP Customer Support |
| No later than 10 days after determination | Florida third-party agent notice to each customer with affected Florida residents' personal information, with the details the customer needs for its own notices (Fla. Stat. 501.171(6)(a)) | General Counsel |
| Within 10 business days of discovery (BAA); no later than 60 calendar days by law | Notice to each affected covered entity, including, to the extent possible, the identification of each individual and the other information the covered entity needs for its notices (45 CFR 164.410(b)-(c)) | Associate General Counsel, Privacy |
| As each state requires | Customers decide on their own notices to end consumers; the company provides the data they need. Counsel checks each state where affected individuals reside | General Counsel |
| Within 30 days of determination, only for company-owned data | Florida individual notice, and Department of Legal Affairs notice if 500 or more Floridians, or a documented "no harm" determination (Fla. Stat. 501.171(4)(c)) | General Counsel |
| At least every 72 hours until closure | Status updates to affected customers; final report within 30 days | Incident commander |

**Why the customer clocks come first.** The company is a service provider for almost all of this data. Its first legal duties run to its customers (DPA, BAA, Florida third-party agent, California service provider), and those clocks are the shortest. The customers then own the notices to end consumers and patients.

**Public statements.** Review the trust center before any statement. Do not repeat the claims that staff access is always logged or that AI providers never retain data (P03 G-033, G-034) unless they are true at that time.

**Extortion demand (POL-03 4.8).** Needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis); and a report to law enforcement. Paying does not remove any notice duty and does not guarantee deletion. The default position, approved by the CEO, is not to pay.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). This incident usually does not take the platform down; recovery means restoring trust in credentials and data paths.
1. Identity provider and administrator access verified clean (BP-15)
2. Production services confirmed unaffected; any altered object restored from versions (BP-01 to BP-04)
3. Healthcare cell confirmed unaffected; export permanently stopped (BP-05)
4. Monitoring with the new detections, verified by a repeat of the P07 simulated download (BP-09)
5. CI/CD resumed with federated credentials only (BP-10)
6. Warehouse loader resumed with the metadata-only role (BP-17)

**Validate before resuming jobs:** no long-lived keys remain, all rotated secrets are in the secrets manager, and the bulk-read alert fires on a test. Tell customers when their data paths are verified (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closure; written report within 30 days (POL-03 4.11).
- Update the risk register (P01 R-001, R-002, R-004, R-010), the POA&M (P07), the SOC 2 incident log (P09, CC7.4 and CC7.5), and this runbook.
- Review the trust center and questionnaire library against what the incident showed (POL-01 4.11).
- Retain the decision log, notices, and evidence for 6 years (POL-01 4.14; 45 CFR 164.414(b)). Keep any Florida "no harm" determination for at least 5 years (Fla. Stat. 501.171(4)(c)).
