# Incident Response Runbook: Ransomware with PHI Exfiltration

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-specialty medical group; FL, GA, AL, SC) |
| Tier / Vertical | Enterprise / Health Care and Social Assistance |
| Incident type | Ransomware with PHI exfiltration (double extortion), including the SEC materiality assessment and a multi-state breach notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure |
| Runbook owner | Director of Security Operations (HIPAA Security Officer), with the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise tabletop 2026-03-19 (technical and clinical response; **the disclosure committee did not take part**). Next: full tabletop with the disclosure committee on 2026-11-12 (POAM-014) |
| Notification matrix | `notification-matrix.csv` (32 obligations: 8 HIPAA, 4 generic state, 6 Florida worked example, 4 SEC, plus OFAC, law enforcement, CIRCIA status, and contractual rows) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Chief Medical Information Officer | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Breach and privacy decisions | Chief Privacy Officer (HIPAA Privacy Officer) | Chief Compliance Officer | Direct mobile |
| Outside breach counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | MSSP incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Clinical operations | Chief Operating Officer; Chief Medical Information Officer; Laboratory Director; Vice President, ASC Operations | Regional medical directors | Crisis line |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (for investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and the identity platform may be compromised. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder at each regional office.

## 1. Preparation checks (Identify / Protect)
- [ ] Immutable backups in separate accounts, restore-tested within the last 90 days for tier-1 systems (CP-9, CP-4)
- [ ] EDR on all endpoints and servers, **including AQ-06 to AQ-08 (gap until POAM-013 closes)**
- [ ] SIEM receives logs from all ePHI systems, **except the AQ-07 and AQ-08 EHRs (gap until POAM-005 closes)**; logs retained 1 year online and 6 years in the archive (AU-11)
- [ ] Break-glass accounts sealed and tested this quarter (POL-02 4.11)
- [ ] Downtime kits and the EHR read-only downtime service verified at clinics, the lab, imaging, and ASCs (P05)
- [ ] Materiality playbook and 8-K templates current, disclosure committee roster current (**gap until POAM-014 closes**)
- [ ] Outside counsel, forensics, and insurer contacts confirmed this quarter
- [ ] State breach law matrix from outside counsel updated in the last 12 months

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renames or encryption | EDR, staff report, backup job failures | SOC opens a severity-1 case; isolate hosts through EDR; page the incident commander |
| Large or unusual outbound transfer (cloud storage, warehouse export) | Egress monitoring, DLP, cloud threat detection | Block destination; preserve logs; open a case |
| Privileged account misuse or new admin accounts | PAM, identity platform, SIEM | Revoke sessions; disable the account; open a case |
| Suspicious activity from an AQ-06 to AQ-08 network or legacy directory | Network detection, VPN logs, local IT report | Treat as severity 1 until scoped; cut the site VPN if activity reaches enterprise systems |
| Extortion message or leak-site post naming the group | Email, threat intelligence, law enforcement, media | Declare; preserve; do not engage without counsel |
| Vendor reports a ransomware event affecting group PHI | Vendor notice (BAA) | Open a vendor incident case; start the third-party track in section 7 |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any production system, or an extortion claim names group data.

**Record two times, separately:**
1. **Discovery time** (HIPAA): the first day the breach was known, or by reasonable diligence would have been known, to any workforce member or agent (45 CFR 164.404(a)(2)). This starts the 60-day HIPAA clock.
2. **Materiality determination time** (SEC): recorded later by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Isolate affected hosts through EDR; do not power them off (preserve memory) | SOC | Hosts network-contained |
| 2. Block attacker infrastructure; if activity crosses from an AQ site, cut that site's VPN | SOC; Network Engineering | Blocks confirmed |
| 3. Revoke sessions and rotate credentials for privileged and service accounts involved; use break-glass accounts if SSO is affected | Identity team | Revocations logged |
| 4. Confirm backup accounts are untouched (immutability locks, no recent deletions) | Cloud Platform Engineering | Backup integrity confirmed |
| 5. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 6. COO activates the crisis management team; clinics, the lab, imaging, and ASCs switch to downtime procedures as systems are affected; ASCs activate their emergency plans (42 CFR 416.54) | COO; site leaders | Downtime running; ASC activation documented |
| 7. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** hosts, cloud accounts, identities, and data stores affected. Use EDR, SIEM, cloud audit logs, PAM records, and network detection. For AQ-07 and AQ-08, collect EHR logs locally, because they are not in the SIEM.
2. **Initial access:** phishing, stolen credentials, edge device exploit, vendor remote tool, or an acquired-practice network. Check AQ VPN paths first while POAM-016 is open.
3. **Evidence:** forensics images hosts and exports logs before they roll over; chain of custody is kept in the evidence register; hashes recorded for each artifact.
4. **Exfiltration:** determine what data left, from which systems, for which patients and clients. Sources: egress logs, cloud storage access logs, warehouse query logs, the attacker's claims and samples. **This drives section 7.**
5. **Integrity:** for the LIS and EHR, confirm no clinical data was altered (compare to backups; check result audit trails). If integrity cannot be confirmed, the Laboratory Director decides whether to hold result release and issue corrected reports (42 CFR 493.1291(k)).
6. **Business impact:** Finance and the BIA owners estimate daily impact using P05 values (for example, about $8.5 million per business day if clinical care is disrupted enterprise-wide; about $9.2 million per day of deferred collections if claims stop). These estimates feed section 6.

## 5. Containment and eradication (RS.MI)
1. Contain by segment: isolate affected accounts, subscriptions, sites, or AQ networks.
2. Disable compromised accounts; reset all privileged credentials and service account secrets; rotate interface and API keys (interface engines, clearinghouses, lab clients).
3. Rebuild from known-good images; never decrypt and reuse encrypted hosts.
4. Patch the initial access path before reconnecting.
5. Forensics confirms persistence is removed before recovery starts in each zone.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 and 5 | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date and time, and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align timing and content of patient, client, media, and investor communications with the filing; brief the audit committee and the board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost or deferred revenue from P05 values; recovery and forensic costs; ransom demand; expected notification, credit monitoring, and legal costs; insurance coverage and retention; effect on liquidity and covenants |
| Operational | Tier-1 services down and for how long; number of sites, patients, and clients affected; ASC and lab disruption |
| Data | Number of patients and states; data types (PHI, SSNs, lab results, Part 2 records); whether data was published |
| Patient safety | Any harm or near miss linked to the incident; result integrity concerns |
| Legal and regulatory | Expected OCR, state attorney general, CMS, or CLIA inquiries; litigation exposure; contract breaches with SL-1 and SL-2 clients |
| Reputation and strategy | Media coverage; client or payer loss; effect on acquisitions |

**Worked example of the clocks (fictional dates):** ransomware discovered Tuesday 2027-02-02 at 08:10 (HIPAA discovery). The committee convenes Wednesday 2027-02-03 and determines materiality on Thursday 2027-02-04 at 16:00. The Form 8-K is due by Wednesday 2027-02-10 (4 business days: February 5, 8, 9, and 10). Forensics confirms PHI was taken on Friday 2027-02-19; Florida's 30-day clocks (individuals and the Department of Legal Affairs) run from that determination to 2027-03-21. The HIPAA 60-day outer limit runs from discovery to 2027-04-03, so the Florida date comes first and sets the plan. Counsel must also decide whether a "reason to believe a breach occurred" arose earlier (for example, when the extortion message claimed data theft), which would move the Florida dates forward.

## 7. Multi-state breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Four-factor breach risk assessment (45 CFR 164.402): nature and extent of PHI, who received it, whether it was actually acquired or viewed, and mitigation. Ransomware with exfiltration is treated as a breach unless the assessment shows a low probability of compromise | Chief Privacy Officer | Signed assessment |
| 7.2 | Build the affected population from forensic results: each individual, data elements, and **state of residence** (from registration address). Separate three groups: (a) the group's own patients and workforce; (b) SL-1 client practices' patients (the group is their business associate); (c) SL-2 lab client patients (the lab is their testing provider) | Chief Privacy Officer; data team | Affected-individual file with state counts |
| 7.3 | **Business associate duty (SL-1):** notify each affected client covered entity within the BAA term (10 days), and no later than 60 days after discovery (164.410), with the identity of each individual. Clients decide their own notices unless they delegate to the group | Vice President, Digital Health | Client notices sent |
| 7.4 | Apply HIPAA: individual notices within 60 days of discovery; HHS contemporaneously if 500 or more; media in every state or jurisdiction with more than 500 affected residents; substitute notice where contact information is missing | Chief Privacy Officer | HIPAA notice plan |
| 7.5 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, content rules, and whether HIPAA-compliant notice satisfies the state law. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 7.6 | **Florida worked example:** individual notice within 30 days of determining the breach; Department of Legal Affairs notice within 30 days if 500 or more Floridians (15 more days on written good cause); consumer reporting agencies if more than 1,000 are notified at once; HIPAA notice is deemed compliant if a copy is timely provided to the Department | General Counsel | Florida filings |
| 7.7 | **Plan to the shortest clock** across HIPAA, every state, and the SEC. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 7.8 | Honor any law enforcement delay request under 164.412 and the matching state provisions; document it | General Counsel | Delay record |
| 7.9 | Engage the mail vendor, call center (toll-free number for 90 days if substitute notice is used), and credit monitoring provider | Chief Privacy Officer | Vendors active |
| 7.10 | Notify contractual parties: SL-2 lab clients, payers and Medicaid managed care plans, and the insurer, per contract | Contract owners | Contract notices logged |
| 7.11 | Track inbound vendor notices (164.410; state third-party agent laws such as Fla. Stat. 501.171(6)) if the incident started at a vendor | Director of Third-Party Risk Management | Vendor notices logged |

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.7). Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove notification or disclosure duties.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Identity platform and break-glass access
2. Network core, SD-WAN, DNS, colocation links
3. Security tooling (EDR console, SIEM) for validation
4. EHR access and interface engines (vendor-hosted EHR: obtain the vendor's integrity statement)
5. LIS and instrument middleware: restore, then the Laboratory Director validates results against controls before release
6. ASC clinical systems and device networks
7. E-prescribing connectivity and telephony
8. PACS and RIS
9. Patient-app platform and outreach portal (tell SL-1 and SL-2 clients the restoration status)
10. AQ-07 and AQ-08 legacy EHRs
11. HIE interfaces, ERP and payroll, data warehouse
12. Clearinghouse connectivity and the claims backlog (fallback to the secondary clearinghouse and payer portals if the primary is affected)

**Validate before reconnecting:** EDR clean, credentials rotated, patched, logging to the SIEM. Keep downtime procedures until each process meets its RTO. Tell patients, clients, and staff when services return (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.10).
- Update the risk register (P01: R-001, R-002, R-003, R-017), the POA&M (P07), this runbook, and the materiality playbook.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including the materiality determination minutes and breach assessments, for at least 6 years (POL-01 4.11).
