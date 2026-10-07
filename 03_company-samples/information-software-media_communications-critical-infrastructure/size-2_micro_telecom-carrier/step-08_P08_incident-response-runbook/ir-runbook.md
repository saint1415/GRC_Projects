# Incident Response Runbook: Network Intrusion Exposing CPNI

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural fiber broadband and voice carrier) |
| Tier / Vertical | Micro / Communications |
| Incident type | Network intrusion exposing customer proprietary network information (CPNI): exploitation of the out-of-date edge router VPN, access to the hut management network, theft of stored credentials from the hut server, export of call detail records (CDRs) from the hosted voice platform, and reads of customer records through the BSS API key |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Office Manager (security and compliance lead) |
| Approved | 2026-08-31 by the Owner and General Manager |
| Last tested | Not yet. First tabletop with the MSP and the consultant due 2026-11-30 |

## 0. Roles and notification chain (Govern)
The company has 7 people and no security staff. The Network Operations Lead and the consultant handle the network, the MSP handles office IT, and the cyber insurer supplies breach counsel and forensics. The Office Manager runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Office Manager | Owner and General Manager | Cell phone (numbers on the printed contact card) |
| Decision maker (money, service shutdown, extortion) | Owner and General Manager | Office Manager | Cell phone |
| Network containment and outage duties | Network Operations Lead | Field Technician on call, then the consultant | On-call phone |
| Network investigation and rebuild | Network engineering consultant | Insurer panel forensic firm | Cell phone (retainer letter) |
| Office IT response | MSP incident line (24x7 emergency number in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel counsel and forensic firm | n/a | Assigned on the first hotline call |
| Telecom regulatory advice | Telecom regulatory consultant | Breach counsel | Cell phone |
| Voice platform provider | Provider's security contact | Provider support line | Phone; account manager |
| BSS vendor | Vendor support line (security incident option) | Account manager | Phone |
| Law enforcement | USSS and FBI through the FCC CPNI reporting facility (for the formal notice); FBI field office | CISA | Numbers and the facility link in the binder |
| CALEA | Owner and General Manager (senior officer) | Network Operations Lead | CALEA TTP 24x7 line |

**Notification chain in the first hour:** whoever notices → Network Operations Lead (network signs) or Office Manager (account or data signs) → both of them and the Owner and General Manager at once → insurer breach hotline (Owner and General Manager) → breach counsel and forensics (through the insurer) → consultant and MSP as needed. The voice platform provider and the BSS vendor are called as soon as their systems are in scope.

**Out-of-band first.** Assume the attacker can read company email and reach the hut network. Coordinate by phone and text on personal phones, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at the office, in the hut, and at the homes of the Office Manager, Network Operations Lead, and Owner and General Manager: this runbook, contact card, notification matrix, outage checklist, the county 911 center's outage contacts, and a business-day calendar
- [ ] Account on the FCC CPNI breach reporting facility set up and tested (P03 G-030). **Gap until 2026-10-31**
- [ ] MFA on the voice platform portal and the router VPN (POAM-003). **Gap until 2026-09-30**
- [ ] Router firmware current (POAM-012). **Gap until 2026-09-20**
- [ ] Credentials in the password manager, not on the hut server (POAM-004). **Gap until 2026-09-30**
- [ ] Off-site copy of network configurations (POAM-008). **Gap until 2026-10-31**
- [ ] Device logs kept long enough to investigate (R-010). **Gap: logs roll over in about 14 days, so export them on day 0**
- [ ] Sealed break-glass network credential in the General Manager's safe (POL-02 B.13)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| VPN login from an unknown place or at an odd hour; configuration change nobody made | Router log; monitoring service; technician notices | Network Operations Lead checks who was connected; open an incident |
| Large CDR export, or a voice platform sign-in nobody recognizes | Voice platform audit log; provider alert | Office Manager calls the provider; open an incident |
| Unusual BSS API activity (many account reads at once) | BSS audit report; vendor alert | Office Manager calls the BSS vendor; open an incident |
| Customer says someone knew their calling history or a stranger called about their account | Customer call | Log it; check BSS views and voice platform exports for that number |
| Vendor or government advisory naming an exploited flaw in the company's router model | Vendor, CISA, or FBI notice | Treat as a possible compromise; hunt on the router |
| Law enforcement contact about the company's network or data | FBI, USSS, or another agency | Route to the Office Manager and the Owner and General Manager at once |

**Declare a CPNI intrusion incident when** an unauthorized actor is confirmed on the router, the hut network, the voice platform, or the BSS, or when evidence shows CDRs or other customer data may have left the company.

**Record two times in the incident log:**
1. **Discovery:** when anyone at the company first knew of the suspected intrusion. Outage clocks run from discovery if service is affected.
2. **Reasonable determination of a CPNI breach:** when the Office Manager, with counsel, concludes that a person intentionally gained access to, used, or disclosed CPNI without or beyond authorization (47 CFR 64.2011(e)). This starts the 7-business-day law enforcement clock and, for Florida-defined personal information, the Florida 30-day clock. **Do not wait for forensics to finish.** A voice platform export by an account nobody at the company used is enough.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the incident log (timeline, actions, who, when) on paper or a personal device | Office Manager | Log open |
| 2. **Check service impact before touching anything.** Will containment drop broadband, voice, or 911? Prefer actions that do not: disable the VPN service and accounts rather than power off the router | Network Operations Lead | Plan recorded |
| 3. Disable the VPN service on the edge router; block the attacker's source addresses; change the router and OLT administrator passwords from the hut console | Network Operations Lead (on site) | No remote access possible |
| 4. **If service must go down** (for example, the router must be isolated) for 30 minutes or more, start the outage clocks in section 6: 120-minute NORS notification for the 667 OC3-minute test, and a call to the county 911 center if 911 calling is affected | Network Operations Lead | Clocks recorded |
| 5. Voice platform: sign in from a clean device, change every password, remove the shared "support" login, turn on MFA, and download the audit log of sign-ins and exports | Office Manager with the provider | Attacker's sessions ended |
| 6. BSS: ask the vendor to revoke the provisioning API key and issue a new, limited key later; export the API audit log | Office Manager with the BSS vendor | Key revoked |
| 7. **Preserve evidence before it rolls over:** copy router and EMS log buffers (about 14 days), the hut server's system logs, VPN session records, voice platform and BSS audit logs; photograph the hut server screen if needed; do not wipe anything | Network Operations Lead; consultant by phone | Copies saved to an encrypted USB drive and hashed |
| 8. Call the insurer's breach hotline; get counsel and forensics assigned; call the telecom regulatory consultant | Owner and General Manager | Claim number issued |
| 9. Ask: could the attacker have reached anything about lawful intercepts (voice platform intercept settings, TTP equipment, the 2022 record)? If it cannot be ruled out, start the CALEA step in section 6 | Owner and General Manager | Decision recorded |
| 10. Ask the MSP to check office computers and the productivity suite for the same attacker (shared passwords may have been reused) | Office Manager | MSP confirms scope |

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the Network Operations Lead and the consultant supplying access and logs.
1. **Initial access.** Confirm the router flaw used and the first access time. Check whether the attacker also tried the EMS web page (exposed until 2026-08-03).
2. **Movement.** What did the attacker reach in the hut: the hut servers, the EMS, the OLTs? Look for the text file with shared passwords and the BSS API key, and for logins to the OLTs with the shared account.
3. **What CPNI was taken.** From the voice platform audit log: which CDR exports, for which date ranges and numbers. At most this is 18 months of call detail for about 440 numbers on about 390 accounts. **If the log cannot show the scope, treat all of it as exposed.**
4. **Personal information for Florida law.** From the BSS API audit log: which account records were read. If the attacker used the key to read accounts, assume names with driver license numbers for about 1,050 accounts. Counsel decides whether call detail with names alone is Florida-defined personal information.
5. **Lawful intercept.** Determine whether the intercept function or records were reached. Only the Owner and General Manager and the Network Operations Lead handle this; forensics may not view intercept content.
6. **Persistence.** Look for new accounts or changed configurations on the router and OLTs, new VPN users, changed RADIUS or DHCP settings, and scheduled tasks on the hut servers.

## 5. Containment and eradication (RS.MI)
1. Upgrade the router firmware (or replace the router from the vendor's advance replacement) before re-enabling the VPN. Re-enable remote access only with named MFA logins (POAM-002, POAM-003).
2. Rotate every network credential, SNMP string, RADIUS secret, and API key. Assume all were exposed. Move them into the password manager and delete the text file.
3. Rebuild the hut servers from clean media if forensics finds tampering. Restore DHCP and RADIUS first, because subscribers need addresses.
4. Compare OLT and router configurations against the last backup from before first access; where firmware integrity cannot be verified, reload vendor images.
5. Confirm with forensics that no persistence remains before reconnecting remote access.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel reviews every notice before it goes out. The current 47 CFR 64.2011 is the rule in force; the 2023 amendments are not yet effective (P03 section 1.3). Check the Federal Register for an FCC effective-date notice at the start of every incident.

| When | Action | Owner | Citation |
|---|---|---|---|
| Within 30 minutes of discovering an outage that potentially affects the 911 center under 4.5(e) | Telephone and written notice to the county 911 center's designated contacts; first follow-up within 2 hours. As a courtesy, call for any 911 outage over 30 minutes | Network Operations Lead | 47 CFR 4.9(h) |
| Within 120 minutes of discovering a qualifying wireline outage (for example, router isolated 30 minutes or more) | NORS notification; initial report within 72 hours; final report within 30 days | Network Operations Lead; Owner and General Manager approves | 47 CFR 4.9(f) |
| Hour 1 | Insurer notified; counsel and forensics engaged | Owner and General Manager | Contract |
| Day 0-2 | Voluntary report to the FBI and CISA, as counsel advises (CIRCIA is not yet in effect) | Office Manager | Voluntary |
| Within a reasonable time of discovering a compromise of intercept information | Report to the affected law enforcement agencies | Owner and General Manager | 47 CFR 1.20003(c) |
| As soon as known | Reasonable determination of a CPNI breach documented with its date and basis | Office Manager with counsel | 47 CFR 64.2011(e) |
| **Internal target 2 business days; legal limit 7 business days after reasonable determination** | Electronic notice to the USSS and FBI through the FCC reporting facility. Flag any extraordinarily urgent need for earlier customer notice | Office Manager | 47 CFR 64.2011(b) |
| Until 7 full business days after that notice | **No customer or public notice**, notwithstanding contrary state law, unless the investigating agency agrees or directs otherwise. Representatives and the answering service say only "we are investigating a network security issue" | Owner and General Manager; Office Manager | 47 CFR 64.2011(a), (b)(1)-(3) |
| After the hold ends | Notice to each customer whose CPNI was breached; the 6 dedicated-circuit customers by phone from the Owner and General Manager as well | Office Manager with counsel | 47 CFR 64.2011(c); contracts |
| No later than 30 days after determination | Florida notice to affected individuals (driver license numbers); Department of Legal Affairs notice (500 or more Floridians); consumer reporting agencies (more than 1,000) | Office Manager with counsel | Fla. Stat. 501.171(3)-(5) |
| Throughout | CPNI breach record kept at least 2 years | Office Manager | 47 CFR 64.2011(d) |

**How the CPNI and Florida clocks fit together (worked example, no holidays).** Reasonable determination on a Monday (day 0). The law enforcement notice goes in on Wednesday (business day 2; the legal limit would be the following Wednesday). The hold runs for 7 full business days: Thursday through the next Friday. Combined CPNI and Florida notices may go out on the Monday after, calendar day 14, well inside Florida's 30 days. The Department of Legal Affairs and consumer reporting agency notices go out the same day. **If the investigating agency directs a delay** (up to 30 days, extendable, under 64.2011(b)(3)), get it in writing: Florida also allows delay on a law enforcement agency's written request (501.171(4)(b)).

**At this size, one notice set.** About 390 voice accounts and about 1,050 driver license records overlap heavily. Counsel should decide in week 1 whether to send one letter per affected person that meets both the CPNI and the Florida content rules, timed to the end of the federal hold.

**Extortion demand** (for example, a threat to publish call records): only the Owner and General Manager may decide, with counsel and the insurer and after an OFAC sanctions check (POL-03 4.9). Paying does not remove any notice duty.

**Next CPNI certification.** The filing due March 1 must summarize customer complaints about unauthorized release of CPNI, and its statement on how procedures ensure compliance must be accurate in light of the incident (47 CFR 64.2009(e)).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Hut power and edge router: upgraded firmware, new credentials, VPN off until named MFA logins exist
2. OLTs and aggregation switch; DHCP and RADIUS on the hut servers (rebuilt if tampered)
3. Voice: confirm with the platform provider that routing, numbers, and 911 locations are unchanged; place a 911 test call as the provider's procedure allows
4. Monitoring service: confirm alerts and on-call paging
5. Office network and computers: MSP confirms clean
6. BSS and portal: new limited API key; provisioning link reconnected
7. EMS and provisioning: rebuilt or verified; installs resume
8. Billing run and productivity suite (unaffected in the scenario)

**Before reconnecting remote access:** credentials rotated, firmware current, MFA on, and forensics satisfied. Tell customers and the dedicated-circuit customers when service is fully restored (RC.CO), and file the final NORS report within 30 days if one was opened.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP, the consultant, and counsel. Written summary within 30 days (POL-03 4.12).
- Update the risk register (P01, especially R-001, R-002, R-005, R-006, R-010), the POA&M (P07), CPNI training, and this runbook.
- Keep the CPNI breach record for at least 2 years (47 CFR 64.2011(d)) and all incident documentation for at least 3 years (POL-02 A.8).
