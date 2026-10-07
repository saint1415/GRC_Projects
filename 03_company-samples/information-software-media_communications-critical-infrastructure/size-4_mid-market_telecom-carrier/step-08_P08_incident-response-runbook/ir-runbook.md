# Incident Response Runbook: Network Intrusion Exposing CPNI

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional broadband and wired telecommunications carrier) |
| Tier / Vertical | Mid-Market / Communications |
| Incident type | Network intrusion exposing customer proprietary network information (CPNI): exploitation of an internet edge router, movement through the network management plane using shared element credentials, and theft of call detail records (CDRs) from the mediation archive, with possible probing of the lawful-intercept system |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-ransomware-outage.md` (ransomware that disrupts operations); `notification-matrix.csv`; BIA (P05); NOC outage and storm plan; CALEA SSI policies |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. Tabletop with the NOC, regulatory affairs, customer operations, counsel, and the MDR scheduled 2026-11-19 (POAM-012) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers so that technical, service, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, CTO, General Counsel, vCISO, Vice President of Regulatory Affairs, Vice President of Network Operations, Director of Customer Operations, Director of Business Services, HR Director, outside breach counsel | Customer and public statements, regulatory notices, contract notices, ransom or extortion decisions (recommendation to the CEO), resources |
| **Incident response team (IRT)** | Incident commander: Security Manager. Director of Network Engineering (network containment lead), IT Director, security analysts, MDR, forensic firm (through counsel), network equipment vendors' incident teams | Containment, investigation, eradication, recovery sequence |
| **Network service command** | NOC Director (lead), Vice President of Network Operations, on-call engineers | Service impact of every containment step, PSAP and NORS clocks, failover to CO-4 |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Incident bridge on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Network containment | Director of Network Engineering | NOC Director | NOC hotline |
| Service impact and PSAP/NORS | NOC Director (24x7) | Vice President of Network Operations | NOC hotline |
| CPNI breach determination and law enforcement notice | Vice President of Regulatory Affairs | General Counsel | Out-of-band group |
| CALEA compromise reports | Vice President of Network Operations (CALEA senior officer) | Vice President of Regulatory Affairs | Cell; TTP 24x7 line |
| Legal | General Counsel; breach counsel (insurer panel); telecommunications regulatory counsel | n/a | Out-of-band group; insurer hotline |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MDR incident response team | Through counsel |
| Monitoring and first response | MDR 24x7 | n/a | MDR hotline |
| Communications | Director of Customer Operations (customers); Marketing Director (media) | Outside crisis PR through counsel | Out-of-band group |
| Board, lenders, and sponsor | CEO informs the audit committee chair and the sponsor's operating partner; CFO informs the lenders' agent | COO | Phone |
| Law enforcement | FBI field office; USSS (through the FCC reporting facility for CPNI breaches) | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read email, chat, the management network, and possibly VoIP calls on company lines. Coordinate on personal mobile phones and the printed contact list in the incident binders at CO-1 and CO-4.

**Legal privilege protocol.** Counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel." Keep facts (timeline, logs) separate from legal conclusions. Do not speculate in writing.

## 1. Preparation checks (Identify / Protect)
- [ ] Incident binders at CO-1 and CO-4: this runbook, the ransomware runbook, contacts, the notification matrix, PSAP and 988 contact lists, and a business-day calendar (POAM-012)
- [ ] FCC CPNI breach reporting facility access set up and tested (POAM-012)
- [ ] Network element syslog and TACACS+ accounting in the SIEM with 1-year retention (POAM-005). **Gap until it closes: local retention is 90 days, so export logs on day 0**
- [ ] CDR archive object-level read logging (POAM-005). **Gap: without it, the company must assume the whole 36-month archive was exposed**
- [ ] Sealed break-glass console credentials at CO-1 and CO-4, tested quarterly (POL-02 4.9)
- [x] Nightly element configuration backups with a copy at CO-4; isolated write-once cloud backups (P07 CP-9 satisfied)
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-17
- [ ] PSAP contacts confirmed within the last 12 months for every area, including POP-served areas (POAM-021)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Unknown account, configuration change, or reboot on an edge router, SBC, OLT, or switch outside a maintenance window | NOC configuration-diff report; element manager alarms; TACACS+ accounting (once in the SIEM) | NOC opens a security ticket and calls the incident commander |
| Logins to network elements from a host that is not a jump host | TACACS+ accounting; MDR alert (after POAM-005) | Block the source; open a security ticket |
| Mediation service account used from a new source, or large reads from the CDR archive | Cloud audit logs; egress alert (after POAM-005) | Disable the key; open a security ticket |
| Large outbound transfer from CO-1, the POPs, or the cloud to an unknown destination | Edge firewall; cloud flow logs | Block the destination; open a security ticket |
| Vendor, CISA, FBI, or FCC advisory naming an exploited router or SBC flaw that matches company equipment | Advisory tracker (SI-5) | Treat as a possible compromise; hunt on affected devices |
| Law enforcement contact about the company's network or data | FBI, USSS, or another agency | Route to the Vice President of Regulatory Affairs and the incident commander at once |
| Customer reports of calls or texts quoting their call history | Care center | Route to the Vice President of Regulatory Affairs |

**Severity 1 (declare immediately):** confirmed unauthorized actor on a network element, voice core, management plane, or SYS-10; or evidence that CDRs or other CPNI may have left the company.

**Record two times in the incident log (POL-03 4.3):**
1. **Discovery:** when anyone at the company first knew of the suspected intrusion. This starts the PSAP and NORS clocks if service is affected.
2. **Reasonable determination of a CPNI breach:** when the Vice President of Regulatory Affairs, with counsel, concludes that a person intentionally gained access to, used, or disclosed CPNI without or beyond authorization (47 CFR 64.2011(e)). This starts the 7-business-day law enforcement clock and the Florida 30-day clock. Do not wait for forensics to finish; evidence that an unauthorized account read the archive is enough.

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | Open the incident bridge on personal phones; declare severity 1; start the incident log | Incident commander | Log open |
| 0-15 min | **Service first.** Assess whether any voice, 911, broadband, or business circuit is affected, or will be affected by containment (POL-03 4.5) | NOC Director | Decision recorded |
| 0-30 min | If any 911 calling is affected or may be: notify affected PSAPs within 30 minutes and start the NORS clock (section 6) | NOC Director | PSAPs called and emailed |
| 0-60 min | Call the cyber insurer hotline before engaging vendors; counsel engaged; counsel engages forensics; call telecommunications regulatory counsel | Chief Operating Officer | Claim number; counsel on the bridge |
| 0-60 min | **Preserve evidence before it rolls over:** export syslog (90-day retention), TACACS+ accounting, jump host and VPN logs, cloud audit logs, and SBC and router logs to write-once storage; snapshot configurations of affected devices | Director of Network Engineering; IT Director | Exports hashed and stored |
| 0-2 h | Isolate the compromised edge router's management interface; shift traffic to the redundant edge where possible. Isolate affected SBCs; VoIP fails to the CO-4 node | Director of Network Engineering with the NOC | Isolation done without unplanned service loss |
| 0-2 h | Disable and rotate the mediation service account keys; block attacker infrastructure at edges and the cloud firewall | IT Director | Keys revoked |
| 0-2 h | Cut routes from POP corporate VLANs to the management network; administer only from a clean jump host with break-glass credentials; disable vendor VPN access | Director of Network Engineering | Routes removed; vendor access off |
| 1-2 h | **Lawful intercept check.** Could SYS-10 or intercept records have been reached? If it cannot be ruled out, the CALEA senior officer starts section 6 CALEA steps | Vice President of Network Operations | Decision recorded |
| 1-2 h | Convene the CMT; first situation report (service status, scope, decisions needed) | CMT chair | CMT meeting held |
| 2-4 h | Staff briefing script: "we are investigating a network security issue"; no discussion with customers or media; report anything unusual | Director of Customer Operations with HR | Script sent by text and posted at sites |
| 2-4 h | CEO informs the audit committee chair and the sponsor; CFO assesses lender notice terms | CEO; CFO | Notices given |

## 4. Analysis (RS.AN)
1. **Initial access:** confirm the router or SBC flaw used, the time of first access, and any other exposed edge devices. Compare running images against vendor hashes.
2. **Movement:** trace from the edge through the management plane (shared local accounts on access elements and SBCs; vendor VPN account; POP reachability) to the mediation collector and CDR archive. Use TACACS+ accounting, jump host logs, element login histories, and cloud audit logs.
3. **What CPNI was taken:** determine which CDRs (date range, lines) were read or copied, and whether the BSS, SYS-18, the portal, or the data warehouse was reached. **If object-level read logs are not available, treat the whole 36-month archive as exposed:** about 74,000 voice lines on about 61,000 accounts, including hosted voice customers' call records.
4. **Personal information for state law:** determine whether Florida-defined personal information was involved (for example, portal credentials, SSN digits, or account numbers with access codes). CDRs with names and telephone numbers alone may not meet Florida's definition; counsel decides. Identify affected customers who live in other states (about 8% of residential accounts are seasonal residents).
5. **Lawful intercept:** determine whether SYS-10, its management path, or intercept records were accessed. Only the 4 CALEA-authorized employees work on SYS-10; forensics may observe but may not view intercept content.
6. **Business Services:** check whether the hosted voice cluster or SD-WAN orchestrator credentials were exposed; Business Services contracts require 24-hour notice of a confirmed incident.
7. **Persistence:** look for new accounts, modified configurations, implants on routers and SBCs, changed TACACS+ or SNMP settings, and new VPN profiles.

## 5. Containment and eradication (RS.MI)
1. Patch or replace the exploited edge router and any device with a matching advisory; verify running images against vendor hashes. Where firmware integrity cannot be verified, replace the device.
2. Rotate every shared element password, SNMP string, TACACS+ key, VPN pre-shared key, vendor credential, and service account secret. Assume all were exposed (POAM-002).
3. Rebuild the mediation collector from a clean image; restore the archive only from a backup that predates first access and passes integrity checks.
4. Restrict the mediation service account to read-only CDR pulls and move its secret to the secrets manager before reconnecting.
5. Apply deny-by-default rules between POP corporate and management zones (POAM-018) before restoring normal administration.
6. Forensics confirms that persistence is removed before recovery begins.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice. The current 47 CFR 64.2011 is the rule in force; the 2023 amendments are not yet effective (P03 section 1.3). Recheck the Federal Register for an FCC effective-date notice at the start of every incident.

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is there a CPNI breach under 64.2011(e)? Date and basis of the reasonable determination | Vice President of Regulatory Affairs with counsel | Incident log |
| D2 | Is there an extraordinarily urgent need to notify customers sooner (64.2011(b)(2))? | Vice President of Regulatory Affairs with counsel, after consulting the investigating agency | Incident log |
| D3 | Was SYS-10 or intercept information compromised (1.20003(c))? | CALEA senior officer | CALEA record |
| D4 | Is Florida-defined personal information involved? How many Floridians? Which other states? | General Counsel with breach counsel | Affected-customer list by state |
| D5 | Contract notices due (Business Services, enterprise accounts, lenders)? | General Counsel and CFO | Contract register |
| D6 | Extortion or ransom demand? | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner | Citation |
|---|---|---|---|
| Within 30 minutes of discovering an outage that potentially affects a PSAP or 988 facility | Telephone and electronic notice to the designated contacts; first follow-up within 2 hours | NOC Director | 47 CFR 4.9(h), (i) |
| Within 120 minutes (wireline) or 240 minutes (VoIP, PSAP affected) of discovering a qualifying outage | NORS notification; initial report within 72 hours (wireline); final report within 30 days | NOC Director; Vice President of Network Operations approves | 47 CFR 4.9(f), (g) |
| Hour 0-1 | Insurer notified; counsel engaged | Chief Operating Officer | Contract |
| Day 0-2 | Voluntary report to the FBI and CISA (CIRCIA is not yet in effect) | Security Manager through counsel | Voluntary |
| Within a reasonable time of discovering a compromise of SYS-10 or intercept information | Report to the affected law enforcement agencies | Vice President of Network Operations | 47 CFR 1.20003(c) |
| As soon as known | Reasonable determination of a CPNI breach documented with its date and basis | Vice President of Regulatory Affairs with counsel | 47 CFR 64.2011(e) |
| **Internal target 2 business days; legal limit 7 business days after reasonable determination** | Electronic notice to the USSS and FBI through the FCC reporting facility; flag any extraordinarily urgent need | Vice President of Regulatory Affairs | 47 CFR 64.2011(b) |
| Within 24 hours of confirming a security incident affecting them | Business Services customers notified under their contracts, without disclosing a CPNI breach before the hold ends unless the agency agrees | Director of Business Services with counsel | Contracts |
| Until 7 full business days after the law enforcement notice | **No customer or public notice of the CPNI breach**, notwithstanding contrary state law, unless the investigating agency agrees or directs otherwise | Chief Operating Officer; Director of Customer Operations | 47 CFR 64.2011(a), (b)(1)-(3) |
| After the hold ends | Notice to each customer whose CPNI was breached; enterprise and government accounts through their representatives | Vice President of Regulatory Affairs with counsel | 47 CFR 64.2011(c) |
| No later than 30 days after determination | Florida individual notice if Florida-defined personal information is involved (or the FCC-rule notice plus a copy to the Department of Legal Affairs, if counsel confirms the deemed-compliance path); Department notice if 500 or more Floridians; consumer reporting agencies if more than 1,000 | General Counsel with breach counsel | Fla. Stat. 501.171(3)-(5) |
| Per each state's law | Notices for affected residents of other states | General Counsel with breach counsel | State statutes |
| Throughout | CPNI breach record kept at least 2 years | Security Manager | 47 CFR 64.2011(d) |

**How the CPNI and Florida clocks fit together (worked example, no holidays).** Reasonable determination on a Monday (day 0). The law enforcement notice goes in on Wednesday (business day 2; the legal limit would be business day 7, the following Wednesday). The hold runs 7 full business days: Thursday through the next Friday. Customer notices may go out on the Monday after, calendar day 14, inside Florida's 30 days. **If the investigating agency directs a delay** (up to 30 days, extendable, under 64.2011(b)(3)), get the direction in writing: Florida also allows delay on a law enforcement agency's written request (501.171(4)(b)).

**Extortion or ransom demand (POL-03 4.8):** requires the CEO, counsel, the insurer, an OFAC sanctions check, and a report to law enforcement. Paying does not remove any notice duty.

**Communications.**
- Customers: after the hold, a notice letter, a call-center script, and an FAQ; the chatbot switched to a scripted answer that routes to agents.
- PSAPs and the state NG911 provider: direct calls from the NOC Director for any service effect.
- Media: holding statement approved by counsel; no technical details or attribution.
- Staff: daily text or phone briefings on the out-of-band channel.

**Next annual CPNI certification:** the filing due March 1 must include a summary of customer complaints about unauthorized release of CPNI, and its statement on operating procedures must be accurate in light of the incident (47 CFR 64.2009(e)).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Validate each step before the next: credentials rotated, devices patched, monitoring in place, forensics sign-off.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | NOC monitoring (CO-1 or CO-4) | 0.5 h | NOC sees alarms for every 911-tagged circuit |
| 2 | Voice core, SBCs, and 911 trunks | 1 h | Test calls, including 911 test calls arranged with the PSAPs |
| 3 | Management plane: clean jump host, TACACS+ with rotated keys, configurations verified against the CO-4 copy | 1 h | Only named accounts work |
| 4 | Core, edge, and access elements, rebuilt from verified configurations where tampering is suspected | 2 h | Hash and configuration checks |
| 5 | Identity provider (verify administrator accounts and MFA registrations) | 1 h | Sessions revoked; privileged credentials rotated |
| 6 | Lawful-intercept mediation, re-provisioned from the TTP's order records by the authorized employees | 4 h | TTP confirms active orders |
| 7 | BSS and contact center (vendor-hosted; confirm no compromise through the API gateway) | 8 h | Vendor statement; API keys rotated |
| 8 | OSS (restore from backup if touched) | 8 to 24 h | Restore validated |
| 9 | Mediation and rating (before switch CDR buffers overflow) | 72 h | CDR counts reconcile with the switches |
| 10 | Portal, app, and chatbot (chatbot in outage-message mode until API scope is confirmed) | 24 h | Gateway allow-list verified |

Tell customers, PSAPs, and Business Services customers when service is fully restored (RC.CO), and file the final NORS report within 30 days.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.11).
- Update the risk register (P01: R-001, R-002, R-005, R-009, R-051), the POA&M (P07), this runbook, CPNI training, and the CALEA SSI policies if SYS-10 was involved.
- Keep the CPNI breach record at least 2 years (47 CFR 64.2011(d)) and all incident documentation at least 3 years (POL-01 4.13).
- If the incident changed 911 diversity or monitoring, record it for the one-time 911 reliability certification (47 CFR 9.20(a)(2)(ii); notification matrix).
