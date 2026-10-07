# Incident Response Runbook: Network Intrusion Exposing CPNI

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (regional broadband and wired telecommunications carrier) |
| Tier / Vertical | Small / Communications |
| Incident type | Network intrusion exposing customer proprietary network information (CPNI): exploitation of the unsupported CO-1 session border controller (SBC), movement through the network management plane, and theft of call detail records (CDRs) from the mediation system |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager (security and compliance lead) |
| Approved | 2026-09-04 by the COO |
| Last tested | Not yet. First tabletop exercise due 2026-11-30 (POAM-013) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | Vice President of Network Operations | Incident bridge (conference line on personal phones), then the out-of-band group chat |
| Network containment and service protection | NOC Manager (24x7) | Network Engineering Manager | NOC hotline |
| Technical response | Managed detection provider (once live, POAM-005) | Forensic firm through the insurer's panel | Provider 24x7 line |
| CPNI breach determination and law enforcement notice | Regulatory Affairs Manager (privacy lead) | COO | Cell |
| CALEA compromise reports | Vice President of Network Operations (CALEA senior officer) | Regulatory Affairs Manager | Cell; TTP 24x7 line |
| Legal counsel | Outside telecommunications regulatory counsel (retainer) and breach counsel (insurer panel) | n/a | Cell; insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Executive decisions | COO | Chief Executive Officer | Cell |
| Customer communications | Director of Customer Operations | Marketing Manager | Cell |
| Law enforcement | FBI field office; USSS field office (through the FCC reporting facility for CPNI breaches) | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read email, chat, and the management network. Coordinate on personal phones and the printed contact list in the incident binder at CO-1 and CO-2. Do not discuss the incident on company email until the IT Manager clears it.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at CO-1 and CO-2: this runbook, contacts, the notification matrix, PSAP and 988 contact lists, and the business-day calendar
- [ ] Account with the FCC CPNI breach reporting facility set up and tested (POAM-012)
- [ ] Managed detection with 24x7 alerting and 1-year log retention (POAM-005). **Gap until it closes: syslog is kept only 30 days, so export logs on day 0**
- [ ] Object-level read logging on the CDR archive (P04 finding 3). **Gap: without it, the company cannot tell which CDRs were read and must assume the whole archive was exposed**
- [ ] Sealed break-glass console credentials at CO-1 and CO-2 (POAM-003)
- [ ] Offline, encrypted copy of device configurations at CO-2 and immutable cloud backups (POAM-008)
- [ ] Forensic retainer and insurer panel confirmed (POAM-013)
- [ ] PSAP contacts confirmed within the last 12 months (47 CFR 4.9(h)(1); P03 G-045)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Unknown account, configuration change, or reboot on an SBC, router, or OLT outside a maintenance window | NOC configuration-diff report; element manager alarms | NOC opens a security ticket and calls the IT Manager |
| Logins to network elements from a host that is not a jump host | TACACS+ accounting; managed detection alert | Block the source; open a security ticket |
| Mediation service account used from a new source, or large reads from the CDR archive | Cloud audit logs; managed detection alert | Disable the key; open a security ticket |
| Large outbound transfer from CO-1 or the cloud tenant to an unknown destination | Edge firewall; cloud flow logs | Block the destination; open a security ticket |
| Vendor or government advisory naming an exploited SBC or router flaw that matches company equipment | Vendor, CISA, FBI, or FCC notice | Treat as a possible compromise; hunt on affected devices |
| Law enforcement contact about the company's network or data | FBI, USSS, or another agency | Route to the Regulatory Affairs Manager and IT Manager at once |

**Declare a CPNI intrusion incident when** an unauthorized actor is confirmed on a voice core, management plane, or mediation component, or when evidence shows CDRs or other CPNI may have left the company.

**Record two times in the incident log:**
1. **Discovery:** when anyone at the company first knew of the suspected intrusion. This starts the outage clocks if service is affected.
2. **Reasonable determination of a CPNI breach:** when the Regulatory Affairs Manager, with counsel, concludes that a person intentionally gained access to, used, or disclosed CPNI without or beyond authorization (47 CFR 64.2011(e)). This starts the 7-business-day law enforcement clock and the Florida 30-day clock. Do not delay the determination to finish forensics. Evidence that the archive was read by an unauthorized account is enough.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the incident bridge on personal phones; start the incident log (timeline, actions, who, when) | IT Manager | Log open |
| 2. **Check service impact first.** Is any voice, 911, or broadband service affected, or will containment affect it? | NOC Manager | Decision recorded |
| 3. Isolate the CO-1 SBC's management interface and, if needed, take the SBC out of service. VoIP fails over to the CO-2 SBC | Network Engineering Manager with NOC | CO-1 SBC isolated; calls completing through CO-2 |
| 4. If any 911 calling is affected for 30 minutes or more, or may be: start the PSAP clock (30 minutes) and the NORS clock (120 minutes wireline) in section 6 | NOC Manager | PSAPs called and emailed |
| 5. Disable the mediation service account's keys and rotate them; block the attacker's known IPs at the edge and in the cloud network rules | IT Manager | Keys revoked |
| 6. Cut the route from the corporate network to the management network; administer only from a clean jump host with break-glass credentials | Network Engineering Manager | Route removed |
| 7. **Preserve evidence before it rolls over:** export syslog (30-day retention), TACACS+ accounting, cloud audit logs, VPN logs, and SBC logs to write-once storage; take configuration snapshots of affected devices | IT Manager and NOC | Exports hashed and stored |
| 8. Call the cyber insurer's breach hotline; engage breach counsel and forensics through the insurer; call telecommunications regulatory counsel | COO | Claim number issued |
| 9. Ask: could the lawful-intercept system (SYS-10) or intercept records have been reached? If it cannot be ruled out, the CALEA senior officer starts section 6 CALEA steps | Vice President of Network Operations | Decision recorded |

## 4. Analysis (RS.AN)
1. **Initial access:** confirm the SBC flaw used, the time of first access, and any other exposed edge devices (both internet edge routers had open advisories; POAM-002).
2. **Movement:** trace from the SBC through the management network (shared local accounts on OLTs, DSLAMs, cabinet switches, and SBCs; POAM-003) to the mediation collector and CDR archive. Check TACACS+ accounting, jump host logs, and element login histories.
3. **What CPNI was taken:** determine which CDRs (date range, lines) were read or copied, and whether the BSS, portal, or data warehouse was reached. **If object-level read logs are not available, treat the whole 36-month archive as exposed:** about 23,400 voice lines on about 20,900 accounts.
4. **Personal information for state law:** determine whether any Florida-defined personal information was involved (for example, portal user names with passwords or security answers, SSN, or government ID numbers). CDRs with names and telephone numbers alone may not meet Florida's definition; counsel decides. Identify affected customers who live in other states (about 9% of residential accounts are seasonal residents).
5. **Lawful intercept:** determine whether SYS-10, its management path, or intercept records were accessed. Do this through the 3 CALEA-authorized employees only; forensics may not view intercept content.
6. **Persistence:** look for new accounts, modified configurations, implants on SBCs and routers, and changed TACACS+ or SNMP settings (11 cabinet switches had default SNMP strings until POAM-010 closes).

## 5. Containment and eradication (RS.MI)
1. Replace or rebuild the CO-1 SBC on a supported release (the replacement is already ordered; POAM-002). Do not return the old unit to service.
2. Patch both edge routers and any device on a matching advisory; verify running images against vendor hashes.
3. Rotate every shared network element password, SNMP string, TACACS+ key, VPN pre-shared key, and service account credential. Assume all were exposed.
4. Rebuild the mediation collector VM from a clean image; restore the archive only from a backup that predates first access and has integrity checks.
5. Restrict the mediation service account to read-only CDR pulls (POAM-007) before reconnecting.
6. Confirm with forensics that persistence is removed before recovery. Where firmware integrity cannot be verified, replace the device.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice before it goes out. The current 47 CFR 64.2011 is the rule in force; the 2023 amendments are not yet effective (P03 section 1.3). Recheck the Federal Register for an FCC effective-date notice at the start of every incident.

| When | Action | Owner | Citation |
|---|---|---|---|
| Within 30 minutes of discovering an outage that potentially affects a PSAP or 988 facility | Telephone and electronic notice to the designated contacts; first follow-up within 2 hours | NOC Manager | 47 CFR 4.9(h), (i) |
| Within 120 minutes (wireline) or 240 minutes (VoIP, PSAP affected) of discovering a qualifying outage | NORS notification; initial report within 72 hours (wireline); final report within 30 days | NOC Manager; Vice President of Network Operations approves | 47 CFR 4.9(f), (g) |
| Day 0 | Insurer notified; counsel engaged | COO | Contract |
| Day 0-2 | Voluntary report to FBI and CISA (CIRCIA is not yet in effect) | IT Manager | Voluntary |
| Within a reasonable time of discovering a compromise of SYS-10 or intercept information | Report to the affected law enforcement agencies | Vice President of Network Operations | 47 CFR 1.20003(c) |
| As soon as known | Reasonable determination of a CPNI breach documented with its date and basis | Regulatory Affairs Manager with counsel | 47 CFR 64.2011(e) |
| **Internal target 2 business days; legal limit 7 business days after reasonable determination** | Electronic notice to the USSS and FBI through the FCC reporting facility. Flag any extraordinarily urgent need for earlier customer notice | Regulatory Affairs Manager | 47 CFR 64.2011(b) |
| Until 7 full business days after that notice | **No customer or public notice**, notwithstanding contrary state law, unless the investigating agency agrees or directs otherwise. Staff and vendor briefing scripts say "we are investigating a network security issue" only | COO; Director of Customer Operations | 47 CFR 64.2011(a), (b)(1)-(3) |
| After the hold ends | Notice to each customer whose CPNI was breached; enterprise and government accounts through their account representatives | Director of Customer Operations with counsel | 47 CFR 64.2011(c); contracts |
| No later than 30 days after determination | Florida individual notice if Florida-defined personal information is involved (or the FCC-rule notice plus a copy to the Department of Legal Affairs, if counsel confirms the deemed-compliance path); Department notice if 500+ Floridians; consumer reporting agencies if more than 1,000 | Regulatory Affairs Manager with counsel | Fla. Stat. 501.171(3)-(5) |
| Per each state's law | Notices for affected residents of other states | Regulatory Affairs Manager with counsel | State statutes |
| Throughout | Breach record kept for at least 2 years | Regulatory Affairs Manager | 47 CFR 64.2011(d) |

**How the CPNI and Florida clocks fit together (worked example, no holidays).** Reasonable determination on a Monday (day 0). The law enforcement notice goes in on Wednesday (business day 2; the legal limit would be business day 7, the following Wednesday). The hold runs for 7 full business days: Thursday through the next Friday. Customer notices may go out on the Monday after, calendar day 14, well inside Florida's 30 days. **If the investigating agency directs a delay** (up to 30 days, extendable, under 64.2011(b)(3)), get the direction in writing: Florida also allows delay on a law enforcement agency's written request (501.171(4)(b)).

**Ransom or extortion demand:** requires the Chief Executive Officer, counsel, the insurer, and an OFAC sanctions check (POL-03 4.6). Paying does not remove any notice duty.

**Next annual CPNI certification:** the filing due March 1 must include a summary of customer complaints received about unauthorized release of CPNI, and its statement on how operating procedures ensure compliance must be accurate in light of the incident (47 CFR 64.2009(e)).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Voice core and 911 trunks (VoIP on the CO-2 SBC; TDM unaffected unless the softswitch was touched)
2. Management plane: clean jump host, TACACS+ with rotated keys, configuration backups verified against the offline copy
3. Core and access network elements, rebuilt from verified configurations where tampering is suspected
4. Identity provider (verify administrator accounts and MFA registrations)
5. Lawful-intercept mediation, re-provisioned from the TTP's order records by the 3 authorized employees
6. BSS and contact center (vendor-hosted; confirm no compromise through the API gateway)
7. OSS, restored from immutable backup
8. Mediation and rating: must be back within 72 hours, before switch CDR buffers overflow (P05 BP-08)
9. Portal, app, and chatbot (chatbot in outage-message mode until the API scope is reduced)

**Validate before reconnecting:** credentials rotated, devices patched, monitoring in place on the rebuilt components. Tell customers and PSAPs when service is fully restored (RC.CO), and send the final NORS report within 30 days.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 4.8 requires documentation within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-007, R-010, R-011, R-013), the POA&M (P07), this runbook, and CPNI training.
- Keep the CPNI breach record for at least 2 years (47 CFR 64.2011(d)) and all incident documentation for at least 3 years (POL-01 4.10).
