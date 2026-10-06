# Incident Response Runbook: Compromise of Shared Services Affecting Subsidiaries

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company with four operating subsidiaries; six states) |
| Tier / Vertical | Enterprise / Management of Companies and Enterprises |
| Incident type | Compromise of shared services affecting subsidiaries: help desk social engineering leads to takeover of a GBS identity administrator, a fraudulent payment attempt through the payment hub, theft of payroll and Finance customer data, and ransomware staged on shared virtualization. Includes the SEC materiality assessment and a multi-entity, multi-state notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State and Regulatory Notification Procedure; PRC-03.4 Payment Fraud Response and Bank Recall Procedure |
| Runbook owner | Director of Security Operations, with the General Counsel for sections 6 and 7 and the Treasurer for section 3.2 |
| Approved | Executive risk committee, 2026-09-14 |
| Last tested | Group tabletop 2026-03-19 (payment fraud scenario; **the disclosure committee did not take part**). Next: full tabletop of this runbook with the disclosure committee, the BISOs, and the outsourced service desk provider on 2026-11-19 (POAM-011) |
| Notification matrix | `notification-matrix.csv` (35 obligations: 8 SEC and disclosure, 4 Finance and FTC, 4 group health plan, 4 multi-state and GBS-as-agent, 5 Florida worked example, and 10 other rows for OFAC, law enforcement, contracts, and regimes that do not apply) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Identity recovery lead | Director of Identity and Access Management | Senior directory engineer | Out-of-band group |
| Payment fraud lead | Treasurer | Assistant Treasurer | Treasury out-of-band line; bank fraud desks |
| Crisis management team chair | CFO | Vice President, Global Business Services | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Chief Accounting Officer, CISO, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| Subsidiary leads | The four subsidiary Presidents and their BISOs | Subsidiary operations leaders | Crisis line |
| Finance notification decisions | Finance Information Security Officer (Qualified Individual) | Finance President | Direct mobile |
| Privacy and plan PHI | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Outside breach counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | Managed security service provider incident team | Retainer hotline |
| Outsourced service desk provider | Provider's security lead (24x7 line in the contract) | Provider account executive | Incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages, Regulation FD) | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** In this incident the attacker may control the identity platform, email, and chat. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder at each GBS and subsidiary headquarters. Do not discuss the response in the productivity suite until the identity platform is confirmed clean (P01 R-063).

## 1. Preparation checks (Identify / Protect)
- [ ] Credential resets for privileged and treasury users done only by the internal IAM team; verified identity proofing live at the outsourced service desk (**gap until POAM-001 closes**)
- [ ] Phishing-resistant MFA on all privileged accounts (**62% today; POAM-002**)
- [ ] Sealed break-glass accounts and the isolated recovery forest tested this quarter (POL-02 4.11)
- [ ] Immutable backups of the directory, ERP, payment hub, and virtualization layer, restore-tested within 90 days (CP-9)
- [ ] SIEM receives identity, PAM, payment hub, and virtualization logs; **AQ directories and integration platform administration logs are missing until POAM-009 closes**
- [ ] Bank fraud desk contacts and recall procedures for all 6 banks current (PRC-03.4)
- [ ] Materiality playbook, 8-K templates, and disclosure committee roster current (**gap until POAM-011 closes**)
- [ ] Outside counsel, forensics, insurer, and service desk provider security contacts confirmed this quarter
- [ ] Counsel's state law matrix updated in the last 12 months (**last update 2025-02; P03 G-064**)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| MFA method added or reset for a privileged account, followed by sign-in from a new device or location | Identity threat detection; SIEM | Revoke sessions; disable the account; call the account owner on the number in the HRIS; open a severity-1 case |
| Mass privileged group changes, new domain administrators, or new federation trusts | Directory monitoring; PAM | Revert; disable the actor; declare |
| New payee, bank-detail change, or payment released outside normal hours or patterns | Payment hub alerts; bank anomaly alerts; positive pay | Treasurer pauses hub release; call the bank fraud desk; open a case |
| Mass access to file sites, the data warehouse, or HRIS exports; large outbound transfers | DLP; database activity monitoring; cloud egress alerts | Block destination; preserve logs; open a case |
| Encryption or mass changes on virtualization hosts; backup job deletions | EDR; hypervisor logs; backup alerts | Isolate hosts; protect backup accounts; declare |
| Service desk provider reports an unusual reset request or its own compromise | Provider notice (contract) | Freeze provider reset rights immediately; open a vendor incident case |
| A subsidiary, plant, or vendor reports something unusual | BISO; plant manager; contract owner | SOC within 1 hour (POL-03 4.2); treat as severity 1 until scoped if identity or payments are involved |

**Declare a severity-1 shared-services incident when** a GBS privileged identity is confirmed compromised, a fraudulent payment is attempted through the hub, or encryption appears on shared virtualization.

**Record the clock-start times separately in the incident log.** Each starts a different legal clock:
1. **Discovery for Finance (FTC):** the first day the event is known to any employee, officer, or agent of Finance, including GBS staff who run Finance services (16 CFR 314.4(j)(2)). Starts the 30-day FTC clock.
2. **Determination of breach (state law):** the date the group determines a breach occurred, or has reason to believe one occurred (Fla. Stat. 501.171(4)(a) worked example). Starts the 30-day Florida clocks.
3. **Discovery for the group health plan (HIPAA):** only if plan PHI is involved (45 CFR 164.404(a)(2)). Starts the 60-day clock.
4. **Materiality determination (SEC):** recorded later by the disclosure committee (section 6). Starts the four-business-day Form 8-K clock.

## 3. First 4 hours (RS.MA, RS.MI)
### 3.1 Identity containment
| Step | Who | Done when |
|---|---|---|
| 1. Freeze all credential and MFA resets at the outsourced service desk; route every reset to the internal IAM team by phone callback | Identity recovery lead | Provider confirms freeze in writing |
| 2. Disable the compromised administrator account; revoke all its sessions and tokens in the identity provider and PAM | Identity team | Revocations logged |
| 3. Review privileged group changes, federation trusts, application consents, and PAM vault access in the last 30 days; revert unauthorized changes | Identity team; SOC | Change list reviewed |
| 4. Rotate credentials for all privileged accounts and the service accounts the attacker could reach; rotate the directory's ticket-signing key twice, following the directory vendor's guidance | Identity team | Rotation logged |
| 5. If the identity platform cannot be trusted, switch to break-glass accounts and the isolated recovery forest | Identity recovery lead | Clean admin path established |

### 3.2 Payment containment
| Step | Who | Done when |
|---|---|---|
| 6. Pause payment release in the hub; allow only payroll, taxes, and debt service through bank portals with dual approval and callbacks (PRC-03.4) | Treasurer | Pause confirmed |
| 7. Call each bank's fraud desk; request recall of any suspicious wire or ACH; freeze changes to payee lists | Treasurer | Recall reference numbers |
| 8. Freeze vendor master and direct-deposit changes in the ERP and HRIS | Vice President, Global Business Services; Chief Human Resources Officer | Change freeze set |

### 3.3 Containment of systems and escalation
| Step | Who | Done when |
|---|---|---|
| 9. Isolate affected virtualization hosts through EDR and the hypervisor management network; do not power them off (preserve memory) | SOC; infrastructure team | Hosts contained |
| 10. Confirm backup accounts are untouched (immutability locks, no recent deletions) | Director of Cloud Platform Engineering | Backup integrity confirmed |
| 11. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number; engagement letters |
| 12. CFO activates the crisis management team; subsidiary Presidents switch to downtime procedures as systems are affected (P05: branch phone dispatch, paper tickets, bank portals for priority payments, local controller programs at plants) | CFO; subsidiary Presidents | Downtime running |
| 13. Tell the Finance Information Security Officer the same day; tell the Chief Privacy Officer if HR or plan data could be involved | CISO | Notices logged |
| 14. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** identities, hosts, cloud accounts, SaaS tenants, and data stores affected, by subsidiary. Use identity provider and directory logs, PAM records, EDR, SIEM, cloud audit logs, payment hub logs, and bank records. For AQ-01 and AQ-02, collect directory logs locally, because they are not in the SIEM.
2. **Initial access:** reconstruct the service desk interaction (call recording, ticket, verification steps). Check for other recent resets with the same pattern.
3. **Evidence:** forensics images hosts and exports logs before they roll over; chain of custody in the evidence register; hashes recorded for each artifact.
4. **Data access and exfiltration:** determine what data left, from which systems, for which entities and people. Sort the affected people by **who is the covered entity**: each subsidiary for its own customers and employees; Finance for its borrowers and applicants; the group health plan for plan PHI; the holding company for its own employees.
5. **Payment integrity:** reconcile the payment hub against bank confirmations for the whole exposure window; confirm no vendor master or payee changes remain.
6. **Financial reporting integrity:** the Chief Accounting Officer confirms no unauthorized journal entries or consolidation changes in the exposure window (input to the disclosure controls evaluation, Rule 13a-15(b)).
7. **Business impact:** subsidiary Presidents and Finance estimate daily impact using P05 values (for example, about $5.7 million per day if Building Products order-to-cash stops, about $2.6 million for Home Services dispatch, about $4.9 million for a plant). These estimates feed section 6.
8. **Related incidents:** the SOC checks the last 90 days of incidents across all subsidiaries for related occurrences (same actor, same technique, same vendor). Related occurrences are treated as one cybersecurity incident for materiality (229.106(a); Item 1.05, Instruction 3).

## 5. Containment and eradication (RS.MI)
1. Contain by boundary: isolate compromised accounts, virtualization clusters, cloud accounts, AQ site VPNs, and any subsidiary network segment the attacker reached.
2. Remove attacker persistence in the identity platform: rogue administrators, federation trusts, application consents, MFA methods, PAM vault entries, and scheduled tasks on domain controllers.
3. Rebuild affected virtualization hosts and servers from known-good images; never decrypt and reuse encrypted hosts.
4. Fix the initial access path before restoring normal resets: the service desk stays frozen until verified identity proofing is in place for every reset (POAM-001).
5. Forensics confirms persistence is removed before recovery starts in each zone.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery (Item 1.05, Instruction 1), from the perspective of a reasonable investor, considering quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, executives, and subsidiary Presidents | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 and 5, **for the group as a whole**, including related incidents across subsidiaries | Committee | Worksheet completed |
| 6.5 | **Materiality determination** recorded with the date, time, and reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft the Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing, and the material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation (Instruction 4). State any information not yet determined | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within four business days after the determination** (General Instruction B.1). Only a written U.S. Attorney General determination allows delay (Item 1.05(c)); any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align investor, lender, dealer, customer, employee, and media communications with the filing. Investor relations follows Regulation FD: no material nonpublic incident information to analysts or investors before public disclosure (17 CFR 243.100). Brief the audit committee and risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Track open information items and file a Form 8-K/A within four business days after each is determined or becomes available (Instruction 2); feed the incident into the quarterly disclosure controls evaluation (Rule 13a-15(b)) and the next Item 106 disclosure | General Counsel (corporate secretary tracks) | Tracker current |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost or deferred receipts by subsidiary from P05 values; fraudulent payments not recovered; recovery, forensic, notification, and legal costs; insurance coverage and retention; effect on liquidity, covenants, and the securitization |
| Operational | Shared services down and for how long; how many subsidiaries, branches, and plants stopped; payroll or supplier payment delays |
| Data | Number of people by covered entity and state; data types (SSNs, bank accounts, Finance credit data, plan PHI); whether data was published |
| Financial reporting | Any effect on ledger or consolidation integrity; effect on the quarter's close and on ICFR conclusions |
| Legal and regulatory | Expected FTC, HHS, state attorney general, or state lender regulator inquiries; litigation exposure; dealer and customer contract claims |
| Reputation and strategy | Media coverage; dealer, customer, or lender reaction; effect on pending acquisitions |

**Worked example of the clocks (fictional dates).** At 06:40 on Tuesday 2027-01-12, the SOC sees a new MFA method on a GBS identity administrator account, followed by privileged changes. GBS staff run Finance's identity services, so this is also Finance's discovery for the FTC clock. The committee convenes Wednesday 2027-01-13 and determines materiality on Thursday 2027-01-14 at 17:00. Monday 2027-01-18 is a federal holiday when the SEC is closed, so the four business days are January 15, 19, 20, and 21: **the Form 8-K is due Thursday 2027-01-21.** Forensics confirms on Friday 2027-01-22 that payroll data and Finance customer data were taken. The Florida 30-day clocks run from that determination to 2027-02-21. The FTC notice for Finance is due no later than 2027-02-11 (30 days after discovery). Counsel must also decide whether "reason to believe a breach occurred" arose on 2027-01-12, when staging of HR exports was first seen; if so, the Florida dates move to 2027-02-11 too. **Plan to the earliest date: 2027-02-11.** If plan PHI was involved, the plan's HIPAA outer limit is 2027-03-13 (60 days after discovery).

## 7. Multi-entity and multi-state notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out. The key holding-company question is **who owes each notice**: the holding company, each subsidiary, Finance, or the group health plan.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Build the affected-person file from forensic results: each person, data elements, **covered entity** (holding company, Building Products, Home Services, Manufacturing, Finance, or the plan), and **state of residence** | Chief Privacy Officer; data team | Affected-person file with counts by entity and state |
| 7.2 | **GBS as third-party agent:** notify each affected subsidiary's President and BISO the same day (POL-03 4.6); the statutory limit is 10 days after determination (Fla. Stat. 501.171(6)(a) worked example). GBS may send individual notices on the subsidiaries' behalf (501.171(6)(b)) | CISO | Subsidiary notices logged |
| 7.3 | **Finance and the FTC:** if Finance customer information of at least 500 consumers was acquired without authorization (access is presumed to be acquisition unless reliable evidence shows otherwise), the Finance Information Security Officer files the FTC notice as soon as possible and no later than 30 days after discovery (16 CFR 314.4(j)). Report the event in the next Qualified Individual report (314.4(i)) | Finance Information Security Officer | FTC confirmation |
| 7.4 | **Group health plan:** if plan PHI was involved, report the security incident to the plan (164.314(b)(2)(iv)); the plan runs the 164.402 four-factor assessment and, if a breach, gives HIPAA notices (individuals within 60 days of discovery; HHS; media where more than 500 residents of a state) | Chief Privacy Officer for the plan | Plan breach file |
| 7.5 | Apply **each state's law** for every state with affected residents, using counsel's matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, content rules. Record the earliest deadline for each state and each covered entity | Outside counsel; General Counsel | State deadline table |
| 7.6 | **Florida worked example:** individual notice within 30 days of determination (up to 15 more days on written good cause to the Department); Department of Legal Affairs within 30 days if 500 or more Floridians (no extension); consumer reporting agencies if more than 1,000 are notified at once; a federal regulator notice counts for Florida only if a copy is timely provided to the Department (the plan's HIPAA notice can; Finance's FTC notice does not replace individual notice) | General Counsel | Florida filings |
| 7.7 | **Plan to the shortest clock** across the SEC, the FTC, HIPAA, and every state. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 7.8 | Honor any law enforcement delay request (FTC 314.4(j)(1)(vi); state provisions such as 501.171(4)(b)) and document it | General Counsel | Delay record |
| 7.9 | Contract notices: banks (immediately for fraud), cyber insurer, lenders and the securitization trustee, SL-1 dealers and SL-2 customers (72 hours under their agreements), and state lender regulators per counsel's matrix | Contract owners | Contract notices logged |
| 7.10 | Engage the mail vendor, call center, and credit monitoring provider | Chief Privacy Officer | Vendors active |

**Ransom or extortion decision:** requires the CEO and the General Counsel, notice to the insurer, and a documented OFAC sanctions check (POL-03 4.7). Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove any notification or disclosure duty.

**Not applicable here:** Federal Reserve notification (the group is not a bank holding company) and CIRCIA (proposed only). Both rows stay in the matrix so responders do not lose time checking.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Identity platform from the isolated recovery forest or verified backups; break-glass access
2. Network core, SD-WAN, DNS, and data center connectivity
3. Security tooling (EDR console, SIEM) for validation
4. Field-service dispatch and contact center routing (Home Services)
5. Loan platform and SL-1 dealer portal (Finance)
6. Payment hub and treasury management: reconcile with every bank before release resumes; first releases with Treasurer callback
7. MES and plant connections to the integration platform, plant by plant
8. Distribution system (Building Products)
9. Productivity suite and SL-2 platform (after identity is confirmed clean)
10. Group ERP and integration platform: Chief Accounting Officer validates ledger integrity before posting resumes
11. E-commerce portal
12. HRIS and payroll (repeat the prior pay file if the cycle is at risk)
13. AQ-01 and AQ-02 legacy systems
14. Consolidation and close
15. Board portal and data rooms

**Validate before reconnecting:** EDR clean, credentials rotated, patched, logging to the SIEM. Keep downtime procedures until each process meets its RTO. Tell subsidiaries, dealers, customers, and employees when services return (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.10).
- Update the risk register (P01: R-001, R-002, R-004, R-013, R-046), the POA&M (P07), this runbook, and the materiality playbook.
- The disclosure committee reviews the incident's effect on the next Item 106 disclosure and the quarterly disclosure controls evaluation.
- Reassess the outsourced service desk provider (POAM-012) and record the event in Finance's Qualified Individual report.
- Retain all records, including materiality determination minutes, breach assessments, and FTC and state filings, for at least 7 years (POL-01 4.11).
