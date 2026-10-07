# Incident Response Runbook: Cloud Credential Compromise Exposing Customer Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded B2B SaaS software publisher; about 9,800 business customers; customers' consumers in every state) |
| Tier / Vertical | Enterprise / Information |
| Incident type | Cloud credential compromise exposing customer data: a long-lived AQ-01 CI access key leaks through a publicly readable build log and is used, through the cross-account role, to copy the shared export of Operations Cloud transcripts and case exports; the attacker then probes the OCP integration API. Includes the SEC materiality assessment, customer DPA notices, bank service provider notice, and a multi-state notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State and Customer Notification Procedure; PRC-03.4 Bank Service Provider and FedRAMP Notification Procedure |
| Related risks and POA&M | P01 R-001 (Very High), R-002, R-003, R-017, R-018, R-019, R-058; P07 POAM-001 to POAM-003, POAM-012, POAM-019 |
| Runbook owner | Director of Security Operations, with the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | 2025-10-21 tabletop (ransomware; disclosure committee took part). Next: disclosure committee tabletop on this scenario, 2026-11-12 (POAM-012) |
| Notification matrix | `notification-matrix.csv` (27 obligations: 4 customer contract, 5 Florida worked example, 4 SEC and disclosure, plus bank service provider, FedRAMP, generic state, OFAC, law enforcement, CIRCIA status, and not-applicable checks) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO | CTO | Out-of-band group on company mobile phones |
| Technical leads | Director of Cloud Platform Engineering (cloud); Vice President, Platform Engineering (OCP); General Manager, Conversational AI (AQ-01) | On-call principal engineers | On-call paging |
| Crisis management team chair | Chief Technology Officer | Chief Customer Officer | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Privacy and breach decisions | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Customer and bank notices | Chief Customer Officer | Vice President, Customer Support | Direct mobile |
| Government Edition and FedRAMP | General Manager, Government Edition | Director of FedRAMP Compliance | Direct mobile |
| Outside breach counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | Second forensics firm on retainer | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read chat and tickets if identity is affected. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder.

## 1. Preparation checks (Identify / Protect)
- [ ] No long-lived static cloud keys in OCP or AQ-01 pipelines (IA-5). **Gap until POAM-002 closes (2027-01-31)**
- [ ] AQ-01 organization under landing zone guardrails; no public storage (CM-6). **Gap until POAM-019 closes (2026-11-15)**
- [ ] AQ-01 cloud audit logs in the archive and SIEM; bulk-read alerts on the shared export (AU-6, SI-4). **Gap until POAM-003 closes (2026-12-15)**
- [ ] AQ-01 export minimized and scoped per customer under an interconnection agreement (CA-3). **Gap until POAM-001 closes (2026-12-15)**
- [ ] Contract obligations register live, with 24-hour and non-standard terms flagged (IR-6). **Gap until POAM-012 closes (2026-11-30)**
- [ ] Bank-designated points of contact on file for all banking customers (96 of 140 today)
- [ ] Materiality playbook, 8-K template, and disclosure committee roster current; new members briefed
- [ ] Customer notice templates (initial, update, final) approved by counsel
- [ ] Outside counsel, forensics, and insurer contacts confirmed this quarter
- [ ] State breach law matrix from outside counsel updated in the last 12 months (current matrix dated 2025-03; refresh due 2026-12-31)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Cloud key used from an address outside the CI service ranges | Cloud threat detection (enterprise orgs; AQ-01 after POAM-003) | Page on-call; open a severity-1 candidate case |
| Bulk read or copy from the shared export bucket, or a new principal reading it | Export detections (after POAM-003); provider storage access logs | Block the principal; preserve logs; open a case |
| Secret-scanning alert or cloud provider exposed-key notice; key found in a public build log or repository | Secret scanning; provider notice; researcher report | Treat the key as compromised; go to section 3 |
| Unusual calls to the OCP integration API from AQ-01 credentials | API gateway anomaly detection; WAF | Revoke the integration tokens; open a case |
| Extortion message, leak-site post, or journalist inquiry about customer data | Security mailbox; threat intelligence; communications | Preserve; declare; do not engage without counsel |
| Customer or sub-processor reports suspicious access | Support; vendor notice | Open a case; start the vendor track in section 7 |

**Declare a severity-1 incident when** a cloud credential is confirmed used from an unknown source against any account that holds customer data, or customer data is confirmed or reasonably believed to have been read or copied by an unauthorized party.

**Record three times, separately, in the incident log:**
1. **Discovery time:** when anyone at the company first knew or had reason to believe that customer data might be affected.
2. **Confirmation time:** when the company confirmed customer data was affected. The DPA 24-hour, 48-hour, and 72-hour clocks run from here (some 24-hour contracts run from suspicion; check the register). Florida's 10-day third-party agent clock runs from "determination of the breach of security or reason to believe the breach occurred" (501.171(6)(a)), which counsel may place earlier.
3. **Materiality determination time:** recorded later by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.

A fourth time applies to banking customers: when the company determines that covered services are, or are reasonably likely to be, disrupted or degraded for 4 or more hours (12 CFR 53.4). Containment that suspends exports or integrations for banking customers can meet this trigger even if no bank data was taken.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Deactivate (do not delete) the leaked key and every long-lived key in the AQ-01 organization; pause AQ-01 pipelines | Technical lead (AQ-01) | Keys inactive; pipelines paused |
| 2. Remove the AQ-01 integration role's trust and suspend the nightly export; revoke OCP integration API tokens issued to AQ-01 | Director of Cloud Platform Engineering; Vice President, Platform Engineering | Trust removed; export suspended; tokens revoked |
| 3. Export cloud audit logs and storage access logs from the AQ-01 organization for the full available history (default 90 days) to the log archive; record hashes | SOC | Export hashes in the evidence register |
| 4. Look for persistence in both clouds: new identities, keys, roles, trust policies, compute, or changes to logging. Capture evidence before removing anything | SOC with forensics | Findings logged |
| 5. Confirm OCP backups, key service, and the Government Edition boundary are untouched | Director of Cloud Platform Engineering; General Manager, Government Edition | Integrity confirmed and logged |
| 6. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 7. Start the incident log, the evidence register, and the clock sheet (section 7.1); open the customer impact list | Incident commander; Chief Customer Officer | Log and clock sheet open |
| 8. Tell support leaders and account teams what they may say (holding statement only) | Vice President, Corporate Communications | Holding statement issued internally |

## 4. Analysis (RS.AN)
1. **Key timeline.** Using the exported logs, list every action by the leaked key and the integration role: first unknown-source use, reads, copies, list operations, writes, and attempts against the OCP API. Compare source addresses with the CI service's published ranges.
2. **What was in the bucket.** The export holds nightly transcripts and case exports for up to 1,150 shared customers. **Until POAM-001 closes, assume every prefix the role could read was taken** unless storage access logs prove otherwise. Map each object to its tenant from the prefix.
3. **Data elements.** End-consumer names, email addresses, phone numbers, message content, case notes, and agent notes. Free text can contain anything consumers typed, including account numbers or health information. Sample the taken objects with automated detection to estimate which sensitive elements appear, by tenant and by state of residence where known.
4. **Pivot attempts.** Review OCP API gateway logs for AQ-01 tokens: which endpoints, which tenants, and whether any request succeeded beyond the integration scope. Confirm tenant isolation held (P02 AC-3, SC-4).
5. **Integrity.** Confirm nothing was written back into the OCP through the integration path; compare recent integration writes against AQ-01's expected behavior.
6. **Business impact.** Finance and BIA owners estimate impact using P05 values (for example, service credits and response cost if exports and integrations stay suspended; BP-17 is about $1.3 million per day, BP-07 about $1.6 million per day). These estimates feed section 6.
7. **Customer impact list.** For each affected tenant: customer, segment (banking, health care, public sector, other), contract notice terms from the register, states of residence of affected consumers where known, and whether the tenant also uses the Government Edition (it should not; confirm).

## 5. Containment and eradication (RS.MI)
1. Delete compromised keys after evidence capture. Replace AQ-01 CI access with short-lived federated credentials (POAM-002 design). Do not issue new static keys.
2. Rotate every secret AQ-01 pipelines could read, including OCP integration credentials, model provider keys, and notification service keys.
3. Rebuild AQ-01 CI runners and redeploy AQ-01 services from reviewed code.
4. Resume the export only in the minimized, per-customer form, with an interconnection agreement and the bucket inside the landing zone (POAM-001); this may take days, so tell affected customers and banking customers when integrations will return.
5. Apply landing zone guardrails to the AQ-01 organization (POAM-019) before reconnecting it.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 and 5 | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date, time, and reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align the timing and content of customer, bank, agency, media, and investor communications with the filing; brief the audit committee and cybersecurity and risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Service credits and lost revenue from P05 values; recovery and forensic costs; expected notification support, legal, and customer remediation costs; contract penalties; insurance coverage and retention |
| Customers | Number and size of affected customers; banking, public sector, and health care customers; Enterprise customers with renewal dates in the next two quarters; expected churn |
| Data | Number of consumers and states; sensitive elements found in free text; whether data was published or used for extortion |
| Trust and statements | Whether the incident contradicts public statements (trust page, SOC 2 system description); expected effect on SOC 2 and ISO/IEC 27001 reports |
| Legal and regulatory | Expected FTC, state attorney general, or CPPA inquiries; bank customers' examiners; agency customers; litigation exposure |
| Reputation and strategy | Media coverage; analyst reaction; effect on the AQ-01 integration and future acquisitions |

**Worked example of the clocks (fictional dates):** an exposed-key notice arrives Tuesday 2027-02-02 at 08:10 (discovery). At 10:30 the export and AQ-01 integrations are suspended for the 1,150 shared customers, including 18 banking customers; at 14:30 the company determines the disruption of those banks' integrations is reasonably likely to last 4 hours or more, so bank notices go out that afternoon. On Wednesday 2027-02-03 at 14:00 forensics confirms the key read the export (confirmation and, per counsel, determination of the breach). Customer notices are due by Thursday 2027-02-04 at 14:00 for the 24-hour contracts, Friday 2027-02-05 at 14:00 for the standard 48-hour DPA, and Saturday 2027-02-06 at 14:00 for legacy 72-hour contracts. The Florida 10-day third-party agent notice is due by Saturday 2027-02-13. The disclosure committee determines materiality on Friday 2027-02-05 at 16:00, so the Form 8-K is due by Thursday 2027-02-11 (4 business days: February 8, 9, 10, and 11). The 48-hour customer notice therefore goes out before the 8-K; section 6.8 aligns the wording.

## 7. Notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each legal obligation before notices go out; the Chief Customer Officer sends customer notices only with approved text.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Build the clock sheet: confirmation time, each affected customer's contract clock from the obligations register, the bank trigger time, and the materiality determination time. Plan to the shortest clock | Incident commander; General Counsel | Clock sheet |
| 7.2 | **Banking customers:** if the 4-hour trigger is met, notify each affected bank's designated point of contact as soon as possible; where no contact is on file, notify the bank's CEO and CIO or two individuals of comparable responsibility (12 CFR 53.4(a)(2)) | Chief Customer Officer | Bank notices logged |
| 7.3 | **Customer notices:** initial notice within the contract clock even when facts are thin (what happened, data possibly involved, actions taken, contact); updates at least every 72 hours; final report within 30 days. Customers decide on notices to their own consumers; the company provides the data they need | Chief Customer Officer | Notices and update log |
| 7.4 | **Florida worked example (third-party agent):** for customers with affected Florida residents, notify within 10 days of determination with all information the customer needs for its own notices under 501.171(3) and (4) | Chief Privacy Officer | Florida agent notices |
| 7.5 | **Each state where affected individuals reside:** counsel checks each state's service provider duty and definition of personal information against the data elements found in the taken objects; the company supports customers' resident notices | Outside counsel; General Counsel | State duty table |
| 7.6 | **Company-owned data:** if company-owned personal information is involved (for example, marketing contacts), apply the company's own duties: Florida individuals and Department within 30 days (Department notice if 500 or more), consumer reporting agencies if more than 1,000, or a written no-harm determination after consulting law enforcement | Chief Privacy Officer | Company-owned data notices or determination |
| 7.7 | **Government Edition:** confirm and document that the Government Edition and federal customer data were not affected. If they were, start the FedRAMP reportable incident communications and agency contract notices at once | General Manager, Government Edition | Confirmation memo or FedRAMP reports |
| 7.8 | Honor any law enforcement delay request and document it | General Counsel | Delay record |
| 7.9 | Inform the SOC 2 service auditor and the ISO/IEC 27001 certification body per engagement terms | Director of Trust and Assurance | Auditor notice |
| 7.10 | **Public statements:** review the trust page and AI pages before any public statement (P03 G-032 to G-034); never repeat a claim the incident showed to be untrue | General Counsel | Reviewed statement |

**Extortion demand:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.7). Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove any notice or disclosure duty.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), validating each step:
1. Identity platform, break-glass accounts, and security tooling (confirm no persistence in either cloud)
2. Customer identity service, API gateway, DNS, and CDN (normally unaffected in this scenario)
3. OCP cells: confirm integrity and tenant isolation; no restore needed unless writes were found
4. Government Edition: confirm unaffected
5. Customer support tools (with the holding statement and customer updates)
6. Customer exports and integrations: only the minimized, per-customer export, inside the landing zone (POAM-001)
7. Conversational AI service: reconnect AQ-01 only after guardrails, key removal, and log onboarding (POAM-002, POAM-003, POAM-019)
8. Data Cloud pipelines (confirm the export path was not used for Data Cloud)
9. Software factory: resume AQ-01 pipelines with federated credentials only

**Validate before reconnecting:** no static keys remain in AQ-01, bulk-read and export detections are live, all rotated secrets are in the secrets manager, and logs from AQ-01 reach the SIEM. Tell customers and banking customers when integrations are verified (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.11).
- Update the risk register (P01: R-001, R-002, R-003, R-017, R-018, R-019, R-058), the POA&M (P07), this runbook, the materiality playbook, and the contract obligations register.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Review the trust page, questionnaire library, and SOC 2 system description against what the incident showed (POL-01 4.13).
- Keep all records, including the materiality determination minutes, customer and bank notices, and any Florida no-harm determination, for at least 7 years (POL-01 4.11; Florida requires at least 5 years for a no-harm determination).
