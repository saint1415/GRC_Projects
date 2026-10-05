# Incident Response Runbook: Ransomware on Dispatch and Train Control Back-Office Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company of 64 freight railroads in 27 states) |
| Tier / Vertical | Enterprise / Transportation Systems |
| Incident type | Ransomware affecting the CAD, the PTC back office, CTC office systems, and supporting IT (TMS, crew system), possibly with data theft, including TSA and CISA reporting, the SEC materiality assessment, and a multi-state breach workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); NIST SP 800-82 Rev. 3 for OT |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 RSSM Location Request Fallback; PRC-03.5 Manual Dispatch and CTC Local Control. This runbook is part of the Cybersecurity Incident Response Plan required by SD 1580-21-01E Sec. II.D |
| Runbook owner | Director of Security Operations, with the Vice President, Network Operations for section 3 and the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-08 |
| Last tested | CIRP exercise 2026-03-18 (isolation and backup integrity objectives; **the disclosure committee did not take part**). Next: full tabletop with the disclosure committee on 2026-11-18 (POAM-010) |
| Notification matrix | `notification-matrix.csv` (32 obligations: 7 TSA and CISA, 3 FRA, 1 maritime, 5 SEC and disclosure, 4 generic state, 4 Florida worked example, plus OFAC, law enforcement, CIRCIA status, insurance, customer and partner contracts, and 2 FAR rows that do not apply today) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead; primary Cybersecurity Coordinator | CISO | Director of OT Security (alternate Cybersecurity Coordinator) | Out-of-band group on company mobile phones |
| Operations incident lead | Vice President, Network Operations | Director, Network Operations Center (alternate Security Coordinator) | NOC supervisor desk; satellite phone at both NOCs |
| Train control lead | Director of Train Control Systems | PTC Back Office Manager | Train control 24/7 desk |
| TSA Security Coordinator | Assistant Vice President, Rail Security | Director, Network Operations Center | NOC 24/7 line |
| Crisis management team chair | Chief Operating Officer | Chief Safety Officer | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Risk Officer, Chief Safety Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| Outside counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | MSSP incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Customers and partners | Vice President, Technology Services (SL-1, SL-2); Vice President, Network Operations (Class I and passenger operators) | Account managers | Customer contact lists in the binder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, the identity provider, and VoIP may be compromised. Use company mobile phones, the out-of-band conferencing service, the railroad radio system, satellite phones, and the printed incident binder at both NOCs and each regional office. The binder is SSI and is kept sealed.

## 1. Preparation checks (Identify / Protect)
- [ ] Immutable backups in separate accounts and the weekly offline copy in DC-2, restore-tested within the last 90 days for CAD and PTC databases (CP-9, CP-4)
- [ ] Offline copies of CAD and PTC software, configurations, and territory tables in the DC-2 vault (CP-9(3))
- [ ] Printed bulletins, track warrant forms, and timetable special instructions current at every dispatch desk; signal maintainers' local control instructions current (PRC-03.5). **Manual CTC operations proven at only 2 of 11 signaled railroads (gap until POAM-020 closes)**
- [ ] RSSM location extract on the NOC standby laptop no older than 4 hours. **Procedure untested with the TMS down (gap until POAM-019 closes)**
- [ ] EDR on all endpoints and servers, **except AQ-04 to AQ-06 (gap until POAM-018 closes)**
- [ ] SIEM receives logs from all Critical Cyber Systems, **except CTC code servers, gateway devices, and PTC message brokers (gap until POAM-007 closes; they keep 90 days locally)**
- [ ] PTC back office failover runbook current; **failover is manual and took 9.5 hours in the last test (gap until POAM-006 closes)**
- [ ] Break-glass accounts for the identity platform and OT directory sealed and tested this quarter (POL-02 4.12)
- [ ] Materiality playbook, 8-K templates, and CISA report template (with the SD statement field) current; disclosure committee roster current (**gap until POAM-010 closes**)
- [ ] Coordinator contacts filed with TSA and current (SD 1580-21-01E Sec. II.B.1.d-e; 1570.201(e))
- [ ] Outside counsel, forensics, insurer, and state breach law matrix confirmed in the last quarter

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file encryption, or backup job failures on CAD, PTC, CTC, or business servers | EDR, SIEM, administrators, backup alerts | SOC opens a severity-1 case; network-contain hosts through EDR; page the incident commander and the NOC supervisor |
| CAD consoles freeze, territory tables fail checksum, or authority records are inconsistent | Dispatchers; SI-7 integrity alerts | NOC supervisor declares a dispatch emergency (section 3.1); SOC treats as severity 1 until ruled out |
| PTC back office stops sending messages or initialization fails across trains | Train control desk; Class I or passenger operator calls | Train control lead starts 236.1029(b) procedures; SOC investigates |
| Privileged account misuse, new administrator accounts, or activity across the directory trust | PAM, identity platform, SIEM | Revoke sessions; disable the account; open a case |
| Suspicious activity from an AQ-04 to AQ-06 site or the crossing monitor vendor network | OT network detection, VPN logs, local IT | Treat as severity 1 until scoped; cut the site VPN or vendor connection if activity reaches enterprise or OT zones |
| Extortion message or leak-site post naming the company | Email, threat intelligence, law enforcement, media | Declare; preserve; do not engage without counsel |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any production system, or an extortion claim names company data.

**Record three times, separately:**
1. **Identification time** (TSA/CISA): when the company identifies a cybersecurity incident, including one still under investigation (SD 1580-21-01E Sec. IV.C). This starts the 72-hour CISA clock (company target 24 hours), the 24-hour TSA clock under 1570.203, and the 12-hour TSOC recommendation.
2. **Materiality determination time** (SEC): recorded later by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.
3. **Breach determination time** (state law): when counsel determines, or has reason to believe, that personal information was acquired (section 7). This starts state clocks such as Florida's 30 days.

## 3. First 4 hours (RS.MA, RS.MI): keep trains safe, then contain
### 3.1 Operations (NOC and train control)
| Step | Who | Done when |
|---|---|---|
| 1. If CAD integrity or availability is in doubt, the NOC supervisor instructs trains and roadway work groups on affected territory to stop at the next safe location and report their position, per operating rules; no new authority is issued from an affected CAD | NOC supervisor | Every train and work group on affected territory accounted for |
| 2. Rebuild the picture of authorities in effect from the DC-2 standby (if confirmed clean), printed bulletins, and radio roll call; then issue paper track warrants with radio repeat-back. Priority: PIH trains, passenger host segments on CR-07 to CR-09, trains blocking crossings | Vice President, Network Operations | Manual dispatch running |
| 3. CTC territory: signal maintainers take local control of interlockings as dispatched; vital field logic continues to protect routes | Signal maintainers; NOC | Local control in place at each affected control point |
| 4. PTC back office lost: host territory runs under 236.1029(b) (for example, absolute blocks where PTC is the only way mandatory directives are delivered; reduced speeds, 30 mph for PIH trains where no block signal system is in use); report each failure or cut-out to the host's designated officer (236.1029(b)(4)); hold tenant trains at Class I interchanges | Train control lead; NOC | Restrictions issued; Class I and passenger operators notified |
| 5. Crew calling: switch to printed crew boards and manual calls if the crew system or telephony is affected | Vice President, Crew Management | Calls going out |
| 6. Pull the latest RSSM location extract and printed list so a TSA request can be answered within 30 minutes (1580.203(d)) | Director, Network Operations Center | Extract or printed list at the NOC desk |

### 3.2 Security
| Step | Who | Done when |
|---|---|---|
| 1. Isolate IT from OT: shut the industrial DMZ brokers and block the 7 managed access points (pre-approved, SD 1580/82-2022-01E Sec. III.D.4); the NOC operations zone keeps running inside | Director of OT Security | Boundary blocks confirmed |
| 2. Network-contain affected hosts through EDR; do not power them off (preserve memory) | SOC | Hosts contained |
| 3. Cut AQ site VPNs and vendor connections if they are involved; block attacker infrastructure | SOC; Network Engineering | Blocks confirmed |
| 4. Revoke sessions and rotate privileged and service credentials involved; use break-glass accounts if the identity provider is affected; the OT directory runs independently | Identity team; Director of OT Security | Revocations logged |
| 5. Confirm backup accounts and the DC-2 offline vault are untouched | Director of Data Center Operations | Backup integrity confirmed |
| 6. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Engagement letters; claim number |
| 7. COO activates the crisis management team | COO | Crisis team running |
| 8. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open |

### 3.3 Reports in the first hours (from `notification-matrix.csv`)
- **TSA TSOC** by telephone (1-866-655-7023) within 12 hours of discovery, as IC Surface-2025-01 recommends (voluntary; company practice).
- **CISA** report under SD 1580-21-01E Sec. II.C for the Covered Railroads, stating that it is made to satisfy the SD: company target 24 hours, deadline 72 hours after identification. Include the affected rail systems, earliest known compromise, detection date, indicators, impact on operations, and planned responses such as reverting to manual train control (Sec. II.C.4). Send supplements within 24 hours of new information.
- **TSA under 1570.203** within 24 hours of initial discovery for any company railroad not covered by the CISA report.
- **Class I and passenger operators** by the NOC dispatcher line at once; **SL-1 and SL-2 customers** within 24 hours.
- **National Response Center** only if a 225.9 accident occurs during degraded operations.
- **33 CFR 6.16-1** report if a port facility served by the 2 port switching railroads is involved or endangered.

## 4. Analysis (RS.AN)
1. **Scope:** hosts, zones, identities, cloud accounts, and data stores affected. Use EDR, SIEM, OT network detection, PAM records, and cloud audit logs. For CTC code servers and PTC message brokers, collect local logs at once because they are not in the SIEM.
2. **Initial access:** phishing, stolen credentials, edge device exploit, vendor access, the corporate-to-OT directory trust, or an acquired railroad network. Check the directory trust and AQ VPN paths first while POAM-005 and POAM-018 are open.
3. **Evidence:** forensics images hosts and exports logs before they roll over; chain of custody in the evidence register; hashes recorded. Evidence that is SSI goes to the SSI library.
4. **Integrity:** confirm territory tables, authority records, PTC configuration, and keys are unaltered (compare with the DC-2 vault and checksums). PTC keys suspected of compromise are revoked under the key management procedure (236.1033(b)(3)).
5. **Exfiltration:** determine what data left: SSI (CIP, zone designs), employee personal information (crew system, HR), customer data (SL-1, SL-2, TMS). **This drives sections 6 and 7.**
6. **Business impact:** Finance and BIA owners estimate impact with P05 values: about $13.2 million of revenue per day; dispatch on paper defers or loses about $7.2 million per day (BP-01); PTC loss puts about $2.6 million per day at risk (BP-02). These estimates feed section 6.

## 5. Containment and eradication (RS.MI)
1. Contain by zone: affected IT segments, cloud accounts, AQ networks, and OT enclaves separately.
2. Disable compromised accounts; reset all privileged credentials, service accounts, and API keys (TMS integrations, EDI gateways, PTC administration).
3. Rebuild from known-good images and vendor-certified media from the DC-2 vault; never decrypt and reuse encrypted hosts. PTC software is reinstalled only from certified versions (236.1023).
4. Close the initial access path before reconnecting.
5. Forensics confirms persistence is removed before recovery starts in each zone; the Director of OT Security approves each OT reconnection.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.5) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 3 to 5, including what has already been reported to CISA and TSA | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date and time and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation, and never include SSI | General Counsel; CFO; outside securities counsel; Assistant Vice President, Rail Security (SSI review) | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align timing and content of employee, customer, partner, media, and investor communications with the filing; brief the chairs of the audit committee and the board safety, security, and risk committee before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed (SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost or deferred revenue from P05 values; recovery and forensic costs; ransom demand; customer credits under SL-1 and SL-2 contracts; notification and legal costs; insurance coverage and retention |
| Operational | Railroads and route miles on manual dispatch and for how long; PTC host segments restricted; interchange refused by Class I partners; customer plants without service |
| Safety | Any accident, near miss, or unprotected crossing linked to the incident; PIH trains affected |
| Data | SSI taken or published; number of employees and states affected; customer data |
| Legal and regulatory | TSA inspection or enforcement, FRA inquiries, state attorney general inquiries, litigation exposure, contract breaches |
| Reputation and strategy | National media; Class I or passenger partner escalation; loss of SL-1 or SL-2 customers; effect on acquisitions |

**Worked example of the clocks (fictional dates):** ransomware is identified on CAD and PTC back office servers on Tuesday 2027-02-09 at 04:40.
- TSA TSOC call by 16:40 the same day (12-hour recommendation).
- CISA report by Wednesday 2027-02-10 at 04:40 (company target), no later than Friday 2027-02-12 at 04:40 (72 hours); the same report, stating it satisfies the SD, covers 1570.203 for the Covered Railroads, and a TSA report for the other railroads is due by 2027-02-10 at 04:40.
- The disclosure committee convenes Wednesday 2027-02-10 and determines materiality on Thursday 2027-02-11 at 17:00. Monday 2027-02-15 is a federal holiday (Washington's Birthday), so the 4 business days are February 12, 16, 17, and 18, and the Form 8-K is due by **Thursday 2027-02-18**.
- Forensics confirms on Friday 2027-02-19 that HR files with employee personal information were taken. Florida's 30-day clocks for individuals and, if 500 or more Floridians are affected, the Department of Legal Affairs run to **2027-03-21**. Counsel must also decide whether a "reason to believe" arose earlier (for example, when the extortion message claimed data theft), which would move the Florida dates forward. Each other state's deadline is added to the master calendar.

## 7. Multi-state breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Decide whether personal information was acquired, using forensic results and each state's definition of a breach | General Counsel with outside counsel | Breach determination memo |
| 7.2 | Build the affected population: each individual, data elements, and **state of residence** (from HR address records). Separate employees and former employees, customers' contacts, and SL-1 and SL-2 customers' data | General Counsel; HR data team | Affected-individual file with state counts |
| 7.3 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, and content rules. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 7.4 | **Florida worked example:** individual notice no later than 30 days after determining the breach or having reason to believe one occurred (up to 15 more days on written good cause to the Department, for the individual notice only); Department of Legal Affairs notice within 30 days if 500 or more Floridians; consumer reporting agencies without unreasonable delay if more than 1,000 are notified at once | General Counsel | Florida filings |
| 7.5 | **Plan to the shortest clock** across states, the SEC, and contracts. Publish one master calendar | General Counsel | Master calendar |
| 7.6 | Honor any law enforcement delay request where a state law allows it, and document it | General Counsel | Delay record |
| 7.7 | Engage the mail vendor, call center, and credit monitoring provider | Chief Human Resources Officer | Vendors active |
| 7.8 | If SSI was taken, inform TSA promptly (1520.9(c)); SSI is never described in public notices | Assistant Vice President, Rail Security | TSA notice logged |
| 7.9 | Notify contract parties: SL-1 and SL-2 customers, Class I and passenger operators, and the insurer, per contract | Contract owners | Contract notices logged |
| 7.10 | Track inbound vendor notices if the incident started at a vendor (state third-party agent laws such as Fla. Stat. 501.171(6)) | Director of Third-Party Risk Management | Vendor notices logged |

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.7). Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove any reporting, notification, or disclosure duty. CIRCIA ransom payment reporting is not in effect (final rule not published as of 2026-09-25).

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Identity platform, OT directory, and break-glass access
2. NOC operations zone network, industrial DMZ, radio and backhaul, DNS
3. Security tooling (EDR console, SIEM) for clean-room validation
4. CAD (and SL-2 dispatch tenants): restore, then dispatchers verify territory tables and reconcile every authority issued on paper before returning to CAD
5. CTC code servers and wayside monitoring: signal engineering verifies indications against field conditions before releasing local control
6. RSSM location data for TSA (offline extract stays ready throughout)
7. PTC back office (company and SL-1 tenants): reinstall certified software, re-key if keys were exposed, test with the Class I and passenger back offices, then lift 236.1029(b) restrictions segment by segment
8. Crew system and crew calling telephony
9. TMS and interchange EDI
10. Legacy dispatch at AQ-04 to AQ-06
11. Safety reporting, customer portal, rail services systems
12. Mechanical and engineering applications
13. ERP, revenue accounting, payroll, and HR

**Validate before reconnecting:** EDR clean, credentials rotated, patched, logging to the SIEM, Director of OT Security sign-off for each OT reconnection. Keep manual procedures until each process meets its RTO. Tell crews, customers, Class I and passenger partners, and employees when services return (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- Update the risk register (P01: R-001, R-004, R-013, R-014, R-017), the POA&M (P07), this runbook, the CIRP, and the materiality playbook.
- Decide with the CISO whether lessons require a CIP amendment (SD 1580/82-2022-01E Sec. VI.B.1) and include the results in the next Cybersecurity Assessment Plan report.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including the materiality minutes, CISA and TSA reports, and breach determinations, for at least 7 years (POL-01 4.11); SSI records stay in the SSI library.
