# Incident Response Runbook: Ransomware Disrupting the Terminal Operating Platform

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-port marine cargo terminal operator; 8 terminals in FL, GA, SC and TX; 5 COTP zones) |
| Tier / Vertical | Enterprise / Transportation and Warehousing |
| Incident type | Ransomware that encrypts ETOP TOS environments and gate servers at several terminals and the SL-2 client environments, with possible theft of truck driver and employee personal information, possible spread toward OT, and an SEC materiality assessment |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Coast Guard and MTSA Reporting Procedure; PRC-03.5 Manual Terminal Operations Procedure. This runbook is part of the Cyber Incident Response Plan required by 33 CFR 101.650(g)(2) |
| Runbook owner | Director of Security Operations, with the Director of Maritime Cybersecurity (CySO) for section 3 and the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise tabletop 2026-03-19 (ransomware on ETOP; **did not include the disclosure committee, notification to several COTPs, or the SL-2 clients**). Next: full tabletop with the disclosure committee, the CySO, the FSOs and two SL-2 clients on 2026-11-18 (POAM-010) |
| Notification matrix | `notification-matrix.csv` (32 obligations: 6 Coast Guard and MTSA, 2 SL-2 and vendor, 5 SEC and insider trading, 3 generic state, 6 Florida worked example, OFAC, CIRCIA status, 3 not-applicable checks, and 5 contractual rows) |
| Handling | SSI once contacts, network details and FSP references are added (POL-04 4.2) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Coast Guard reporting and Subpart F records | Director of Maritime Cybersecurity (CySO) | Terminal OT Security Lead (alternate CySO) of the affected terminal | CySO line through the SOC, 24x7 |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Vice President, Terminal Technology | Crisis line |
| Terminal operations and manual working | Terminal General Managers | Shift superintendents | Terminal radio nets and crisis line |
| OT safety and OEMs | Director of OT Engineering | Terminal maintenance managers | OT on-call; OEM 24x7 service lines |
| Maritime security and MTSA reports | Vice President, Maritime Security; FSOs | Security supervisors on duty | Security control rooms |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Risk Officer, COO, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| SL-2 client notification | Vice President, Terminal Technology | Client success lead | Client CySO and FSO contacts in the binder |
| Outside breach counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | Second forensic firm on the panel | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (for investor messages) | Direct mobile |
| Port partners and carriers | Chief Commercial Officer; Terminal General Managers | Customer service leads | Printed partner contact sheets |

**Out-of-band first.** Assume email, chat and the identity platform may be compromised. Use company mobile phones, the out-of-band conferencing service, terminal radio nets and the printed incident binder in each terminal security control room and at headquarters.

## 1. Preparation checks (Identify / Protect)
- [ ] Immutable backups in separate accounts, restore-tested within the last 90 days for tier-1 systems (CP-9, CP-4); **ETOP parallel restore and failover of all 11 environments not yet proven (POAM-005)**
- [ ] EDR on all endpoints and servers, **including T-08 (gap until POAM-012 closes)**
- [ ] SIEM receives logs from all critical IT and OT, **except T-07 gate and OT and all of T-08 (gap until POAM-008 closes)**; until then export local logs in the first hour
- [ ] OEM remote tools off between approved sessions, **except the 2 OEM tunnels (gap until POAM-002 closes)**: cut them at the terminal firewall at declaration
- [ ] Break-glass accounts sealed and tested this quarter (POL-02 4.12)
- [ ] Printed dangerous cargo location list at every security control room at each shift change; manual gate kits and release lists at every gate complex (P05)
- [ ] Materiality playbook and 8-K templates current; disclosure committee roster current (**gap until POAM-010 closes**)
- [ ] COTP, FBI and CISA contacts for all 5 COTP zones in every binder; CySO and alternates' 24x7 numbers tested this quarter
- [ ] SL-2 client CySO and FSO contacts current; **client notice term still 24 hours (gap until POAM-011 closes)**
- [ ] Outside counsel, forensics and insurer contacts confirmed this quarter; state breach law matrix from outside counsel updated in the last 12 months

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file renames or encryption on a TOS server, gate server or workstation | EDR, gate staff, planners, backup job failures | SOC opens a severity-1 case; isolate hosts through EDR; page the incident commander and the CySO line |
| ETOP environments stop accepting transactions at more than one terminal | Planners, gate supervisors, cloud monitoring | Platform team checks for encryption or unknown admin activity; treat as severity 1 until ruled out |
| Privileged account misuse or new admin accounts in the cloud or PAM | PAM, identity platform, cloud threat detection | Revoke sessions; disable the account; open a case |
| Suspicious activity from T-08 or over an OEM tunnel | Network detection, T-08 local IT, OT monitoring (T-01 to T-05) | Treat as severity 1 until scoped; cut the T-08 site link or the tunnel if activity reaches enterprise systems or OT |
| HMI shows changed settings, or cranes, ASCs or RTGs behave unexpectedly | Equipment operators, OT engineers | **Stop the equipment in a safe state (POL-03 4.10)**; call OT Engineering and the CySO line |
| Extortion message or leak-site post naming the company or a client | Email, threat intelligence, law enforcement, media | Declare; preserve; do not engage without counsel |
| A vendor, SL-2 client or port partner reports a ransomware event affecting shared systems | Vendor or client notice | Open a case; start the third-party track (section 7) |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any ETOP or terminal system, or an extortion claim names company or client data. The incident commander declares it.

**Record three times, separately:**
1. **Evidence time** (Coast Guard): when the first evidence of an actual or threatened cyber incident was seen. 33 CFR 6.16-1 requires an **immediate** report; do not wait for certainty.
2. **Breach determination time** (state law): when the company determines a breach of personal information occurred, or has reason to believe one did. Florida's 30-day clocks run from this time.
3. **Materiality determination time** (SEC): recorded later by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.

## 3. First hour (RS.MA, RS.MI, RS.CO)
| Step | Who | Done when |
|---|---|---|
| 1. **Safety first.** Stop crane, ASC and RTG moves that depend on TOS data if integrity is in doubt; hold hazardous cargo work; the FSOs confirm the printed dangerous cargo list is at every security control room | Terminal General Managers; Director of OT Engineering; FSOs | Equipment in a safe state; list confirmed |
| 2. Isolate affected hosts through EDR (do not power them off); cut the 2 OEM tunnels and the T-08 site link; block IT-to-OT flows at the OT firewalls except the equipment interface once verified | SOC; Network Engineering; OT Engineering | Containment confirmed |
| 3. **Report under 33 CFR 6.16-1** to the COTP of every affected zone, the FBI and CISA. Give what is known now and update later. Use one fact sheet so every zone hears the same thing | CySO (alternate CySO if unreachable) | Reference numbers recorded for each zone |
| 4. **Notify affected SL-2 clients** by phone (CySO and FSO of each client) so they can make their own 6.16-1 reports; follow with written notice | Vice President, Terminal Technology | Each client acknowledged; time logged |
| 5. Revoke sessions and rotate credentials for privileged, service and integration accounts involved; use break-glass accounts if SSO is affected | Identity team | Revocations logged |
| 6. Confirm backup accounts are untouched (immutability locks, no recent deletions) and identify the last clean restore point per environment | Cloud Platform Engineering | Backup integrity confirmed |
| 7. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 8. COO activates the crisis management team; affected terminals switch to manual working (PRC-03.5): manual gate on reduced lanes for confirmed releases only, radio dispatch, paper tally; automated releases suspended until holds are refreshed | COO; Terminal General Managers | Manual working running at each affected terminal |
| 9. Tell carriers with vessels due, port authorities, port community systems and the customs data exchange that EDI and automated gates are suspended and that messages after the declaration time are not trusted until verified | Chief Commercial Officer; Terminal General Managers | Partners called from printed lists |
| 10. Start the incident log (timeline, decisions, reports made, who, when) and the evidence register; this is also the Subpart F incident record (101.640) | Incident commander; CySO | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** environments, terminals, cloud accounts, identities, gate servers and data stores affected. Use EDR, SIEM, cloud audit logs, PAM records and network detection. For T-07 gates and OT and for T-08, collect logs locally first, because they are not in the SIEM.
2. **Initial access:** phishing, stolen credentials, an edge device exploit, a vendor or OEM remote tool, an SL-2 client account, or the T-08 site link. Check the OEM tunnels and T-08 first while POAM-002 and POAM-001 are open.
3. **Evidence:** forensics images hosts and exports logs before they roll over; chain of custody is kept in the evidence register; hashes recorded for each artifact; cloud snapshots of affected disks kept in the forensic account.
4. **OT check:** with the OEMs, compare controller programs and HMI settings at each affected terminal with the program vault (T-01 to T-06) or OEM copies (T-07, T-08). **No crane or automated block returns to TOS-directed work until OT Engineering signs off.**
5. **Exfiltration:** determine what data left, from which systems, and whose: truck driver profiles with driver license numbers (SL-1 and the gate module), employee records, TWIC card identifiers in gate and PACS records, SSI (FSP extracts, network maps, Plan drafts), customers' cargo and customs data, and SL-2 clients' data. **This drives section 7.**
6. **Integrity:** confirm no hold, release or hazardous cargo data was altered; compare restored data with the customs data exchange, carrier bay plans and yard checks.
7. **Security impact:** each FSO decides whether an FSP security measure was circumvented (breach of security) and whether the disruption could become a TSI (33 CFR 101.305).
8. **Business impact:** Finance and the BIA owners estimate impact using P05 values (for example, about $5.8 million per day if vessel work at the container terminals runs manually, about $2.4 million per day for the gates, and SL-2 service credits). These estimates feed section 6.

## 5. Containment and eradication (RS.MI)
1. Contain by environment and terminal: isolate affected spokes, gate zones and the T-08 link; keep unaffected terminals running on ETOP if forensics confirms isolation.
2. Disable compromised accounts; reset privileged credentials and service secrets; rotate EDI partner credentials, API keys (customs data exchange, port community systems, SL-1, AI-001) and the TOS vendor support credentials.
3. Rebuild TOS servers and gate servers from known-good images; never decrypt and reuse encrypted hosts.
4. Close the initial access path before reconnecting (for example, onboard the OEM to the gateway or disable the T-08 link).
5. Forensics confirms persistence is removed before recovery starts in each environment.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 3 to 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors. Coast Guard reporting under 6.16-1 never waits for this step.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.5) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision. The CySO attends to report what was told to each COTP | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 and 5 | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date, time and reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation, and keep SSI out of the filing | General Counsel; CFO; outside securities counsel; CySO for SSI review | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align the timing and content of carrier, SL-1 and SL-2 customer, port authority, media and investor communications with the filing and with what was reported to the COTPs; brief the audit committee and board risk committee chairs before filing | Communications; Investor Relations; General Counsel; CySO | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost or deferred revenue from P05 values; recovery and forensic costs; ransom demand; SL-2 service credits; notification and legal costs; insurance coverage and retention; effect on liquidity and covenants |
| Operational | Terminals and berths down and for how long; vessel calls diverted or delayed; gate volumes; the T-01 automated yard; number of SL-2 clients affected |
| Safety | Any injury, near miss or hazardous cargo event linked to the incident; OT integrity concerns |
| Data | Number of drivers, employees and states affected; data types (driver license numbers, TWIC identifiers, SSI, customers' cargo data); whether data was published |
| Legal and regulatory | Coast Guard actions (for example a COTP order or a finding against the FSP or Cybersecurity Plan); state attorney general inquiries; CBP questions on release integrity; litigation exposure; breach of carrier, concession or SL-2 agreements |
| Reputation and strategy | Media coverage; carriers moving services to other terminals; port authority concession reviews; effect on future acquisitions and SL-2 sales |

**Worked example of the clocks (fictional dates):** ransomware is discovered at T-01, T-03 and T-04 and in the C-02 client environment on Tuesday 2027-02-02 at 08:10. The CySO reports to the COTPs of the 2 affected zones, the FBI and CISA by 08:55, and the C-02 client is told by 09:05 so it can report to its own COTP. The disclosure committee convenes Wednesday 2027-02-03 and determines materiality on Thursday 2027-02-04 at 16:00, so the Form 8-K is due by Wednesday 2027-02-10 (4 business days: February 5, 8, 9 and 10). Forensics confirms on Friday 2027-02-19 that driver profiles with driver license numbers were taken. Florida's 30-day clocks (individuals and, if 500 or more Floridians, the Department of Legal Affairs) run from that determination to Sunday 2027-03-21, so the plan is to mail by Friday 2027-03-19. Counsel must also decide whether a "reason to believe a breach occurred" arose earlier (for example, when the extortion message claimed driver data), which would move the Florida dates forward. Each other state's clock is set from counsel's matrix (section 7).

## 7. Multi-state breach notification and third-party workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each personal information obligation before notices go out. Coast Guard reporting does not wait for counsel.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Decide whether personal information was acquired or accessed, using forensic results; document the decision and the time of determination | General Counsel with outside counsel | Signed breach determination |
| 7.2 | Build the affected population: each individual, data elements, and **state of residence** (from driver registration, HR and hiring hall records). Separate: (a) truck drivers on SL-1 and in the gate module; (b) employees; (c) longshore workers in gate and PACS records; (d) SL-2 clients' users and records | General Counsel; data team | Affected-individual file with state counts |
| 7.3 | **SL-2 clients:** give each client the facts it needs about its own environment and data, without delay, for its own Coast Guard reports and any notices it owes; agree who sends notices to the client's individuals | Vice President, Terminal Technology | Client packages sent |
| 7.4 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds and content rules. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 7.5 | **Florida worked example:** individual notice no later than 30 days after determination (15 more days only on written good cause to the Department, and only for the individual notice); Department of Legal Affairs notice within 30 days if 500 or more Floridians; consumer reporting agencies if more than 1,000 are notified at once; a written law enforcement request can delay individual notices; a documented no-harm determination after consulting law enforcement can remove the individual notice but must be sent to the Department within 30 days | General Counsel | Florida filings |
| 7.6 | **Plan to the shortest clock** across every state and the SEC. Publish one master calendar | General Counsel | Master calendar |
| 7.7 | Honor any law enforcement delay request and document it | General Counsel | Delay record |
| 7.8 | Engage the mail vendor, call center and credit monitoring provider | General Counsel | Vendors active |
| 7.9 | Tell carriers whose cargo data was taken, port authorities and the customs data exchange, per contract | Chief Commercial Officer | Contract notices logged |
| 7.10 | Track inbound vendor notices (101.650(f)(2); state third-party agent laws such as Fla. Stat. 501.171(6)) if the incident started at a vendor | Director of Third-Party Risk Management | Vendor notices logged |
| 7.11 | If SSI was taken, the CySO tells the affected COTPs and records it in the incident record | CySO | COTP update logged |

**Ransom decision:** requires the CEO, the General Counsel and the insurer, plus an OFAC sanctions check (POL-03 4.9). Paying does not remove any reporting, notice or disclosure duty. **CIRCIA is not in effect** (final rule not published as of 2026-09-25), so there is no 72-hour or 24-hour CIRCIA report today; recheck when the final rule is published.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Identity platform and break-glass access
2. Network core, SD-WAN, DNS, colocation links; OT kept isolated
3. PACS, TWIC readers and the dangerous cargo location list
4. Security tooling (EDR console, SIEM) for validation
5. ETOP environments for T-01 to T-07, in the order of vessels due at berth
6. SL-2 client environments C-01 to C-04 (clients confirm their own readiness before go-live)
7. EDI hub and customs data exchange feed; **refresh every hold before any automated release**
8. Gate automation (OCR, kiosks, gate servers)
9. SL-1 platform and appointments
10. OT reconnection to the TOS, only after controller verification and OT Engineering sign-off
11. T-08 legacy TOS and gate
12. Labor ordering, planning tools, AI-001 (only after a security review), ERP, payroll and billing

**Validate before reconnecting:** EDR clean, credentials rotated, patched, logging to the SIEM, restored inventory reconciled with yard checks and carrier bay plans, moves made during manual working keyed in, and hazardous cargo locations confirmed by the FSO. Keep manual procedures until each process meets its RTO. Tell staff, the COTPs, SL-2 clients, carriers and port partners when each service is back (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.13).
- Update the risk register (P01: R-001, R-002, R-008, R-012, R-013), the POA&M (P07), this runbook, the materiality playbook and, where needed, the Cybersecurity Plans (101.650(g)(3)).
- The disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Keep all records, including the 6.16-1 report references, the materiality determination minutes and breach determinations, for at least 2 years (101.640; 105.225), and longer where the records schedule or a state law requires (for example, 5 years for a Florida no-notice determination).
- Add the incident to the next annual cyber training and the next drill and exercise (101.635).
