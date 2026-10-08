# Incident Response Runbook: Compromise of the Payment Processing Environment Across Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Financial Services |
| Incident type | Compromise of the payment processing environment that starts in Merchant Consulting, takes cardholder data from the processor's dispute platform (SYS-P6), and reaches the Software division's ISV credentials |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel; card brand and bank notices run by the head of bank and network relationships |
| Approved | 2026-09-10 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The multi-regulator notification matrix and a covered-services determination have never been exercised across divisions** (scenario gap 7); the first cross-division tabletop is on 2026-12-15 (POAM-006) |

## Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry (Day -9):** an attacker sends a dispute team lead in Merchant Consulting a fake SYS-M1 sign-in page, relays the SMS code in real time, and takes over the federated session (P01 MC-001). The team lead also kept standing access to the Software division's ISV support console from a 2025 integration project (P07 AC-02j. finding).
- **Collection (Day -9 to Day -1):** at night, in small batches, the attacker uses the SYS-P6 case export permission (held by all dispute analysts, P07 AC-06 finding) to export about 610,000 dispute case files. Card images and cardholder letters in them show full PAN with cardholder names for about 580,000 cards, and expiry dates for about 40% of them. No security codes. SYS-P6 events are not in the SIEM (POAM-004), so nothing alerts.
- **Second path (Day -3):** the attacker reads API credentials for 37 ISVs in the support console and, on Day -1, uses two of them to run card-testing traffic through the gateway.
- **Day 0, 09:20:** the gateway fraud team sees the card-testing spike and revokes the two keys. The SOC links both keys to console views by one consulting account, then finds the night-time exports in SYS-P6's application log. **Severity 1 declared at 10:05.**
- **Forensic estimate at Day 5:** about 580,000 cardholders, issued by banks across the United States; card-present and card-not-present disputes of about 41,000 processor merchants, 1,150 of which are also Merchant Consulting dispute clients; 37 ISVs' credentials exposed. About 46,000 of the cardholders have Florida billing addresses.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC, identity, and cloud platform teams | Forensic firm on retainer; PCI Forensic Investigator (PFI) if a brand requires one, engaged through counsel | SOC bridge |
| Notices and legal | Group General Counsel with outside breach counsel | Division general counsels | Out-of-band bridge |
| Card brand and sponsor bank notices; 4-hour determination | Head of bank and network relationships | Payment Processing division president | Division bridge |
| Settlement and funding decisions | Head of settlement operations | Payment Processing chief technology officer | Division bridge |
| ISV and merchant notices (Software) | Software division client trust and assurance director | Software division CISO | Division bridge |
| Client notices (Merchant Consulting) | Merchant Consulting division president | Dispute services director | Division bridge |
| SEC materiality | Disclosure committee | Group Chief Financial Officer | Committee call |
| Law enforcement | U.S. Secret Service or FBI field office; IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read consulting email (SYS-M1) and may watch group chat. Use the crisis line and managed mobile devices. The printed binder in each division's command center holds contacts (including all four sponsor banks), this runbook, and the notification matrix.

## 1. Preparation checks (Identify / Protect)
- [x] 24x7 SOC with EDR, DNS, and egress monitoring of every CDE (SI-4, SI-3; P07 satisfied)
- [x] Immutable cross-provider backups of SYS-P6 and the settlement database (CP-9; P07 satisfied)
- [x] PFI shortlist, forensic retainer, and insurer panel confirmed
- [x] Disclosure committee charter includes cybersecurity materiality
- [ ] SYS-P6 events in the SIEM with a bulk-export detection (**gap until POAM-004 closes, 2026-11-30**)
- [ ] Case export limited to supervisors (**gap until POAM-003 closes, 2026-10-31**)
- [ ] No SMS codes for CDE access; consulting users on SYS-G1 (**gaps until POAM-002 and POAM-001 close**)
- [ ] Designated contacts for all four sponsor banks and a 4-hour determination procedure for any incident origin (**gap until POAM-005 closes, 2026-10-31**)
- [ ] ISV keys masked in the support console; no standing cross-division access (**gap until POAM-018 closes**)
- [ ] Notification matrix exercised across divisions (**gap until POAM-006 closes, 2026-12-15**)

## 2. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Card-testing spike tied to specific ISV or merchant API keys | Gateway fraud monitoring | Revoke keys; check who viewed or used them; escalate to the SOC |
| Bulk case views or exports, or exports at unusual hours | SYS-P6 events in the SIEM (after POAM-004) | Disable the account; declare if confirmed |
| Sign-in to SYS-M1 or SYS-G1 from a new country or device followed by CDE access | SYS-G1 risk signals; SYS-M1 sign-in logs | Revoke sessions; review activity |
| Common point of purchase alert: a sponsor bank or card brand says fraud traces back to the group's merchants | Sponsor bank; card brand | Declare immediately |
| A merchant, ISV, or consulting client reports misuse of data it believes came from the group | Division liaisons | Treat as a potential compromise; open an incident |

**Declare a payment environment compromise (Severity 1)** when cardholder data in any group CDE is confirmed or reasonably suspected to have been accessed without authorization, wherever the access started.

**Record the time of each clock start** (POL-03 4.3). In this scenario:
- reasonable suspicion of an account data compromise: Day 0, 10:05 (Visa 3-day clock; sponsor agreement 24-hour clock);
- discovery for the FTC: Day 0, 10:05, the first day the event was known to an employee other than the attacker (16 CFR 314.4(j)(2));
- Software division learns ISV credentials were exposed: Day 0, 11:30 (ISV 24-hour clock);
- determination that covered services to Bank D are reasonably likely to be disrupted 4 or more hours: Day 0, 13:40 (section 6.2);
- consulting confirms client data was affected: Day 1, 16:00 (engagement letter 72-hour clock);
- determination of a breach for state law purposes: set by counsel (Day 2 in this scenario).

## 3. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the incident log with every clock start; start the clock table in section 6.1 | Incident commander | Log open |
| 2. Disable the compromised account; revoke all its sessions in SYS-M1 and SYS-G1 | Group identity director | Sessions revoked |
| 3. **Suspend federation from SYS-M1 to SYS-G1** for all users. This cuts 2,400 dispute analysts off from SYS-P6 | Group identity director, approved by the Group CISO | Federation off; dispute deadline triage list started (P01 PP-027) |
| 4. Disable the case export function in SYS-P6 for everyone; snapshot SYS-P6 storage and logs for forensics; legal hold | Payment Processing chief technology officer; SOC | Export disabled; evidence list signed |
| 5. Revoke and reissue all 37 exposed ISV credentials; block card-testing patterns at the gateway | Software division CISO | New keys issued; ISVs told through the out-of-band list |
| 6. **Pause the dispute-to-settlement adjustment interface** until adjustments made since Day -9 are verified (the attacker held a session that could reach it) | Head of settlement operations | Interface paused at 13:10; integrity check started |
| 7. **Covered-services check** (section 6.2): can each sponsor bank's funding file still meet its cutoff? | Incident commander with the head of bank and network relationships | Decision recorded per bank |
| 8. Call the cyber insurer; engage breach counsel, forensics, and a PFI through the panel | Group Chief Risk Officer | Claim number; engagements signed |
| 9. Notify all four sponsor banks of a suspected account data compromise (contract, 24 hours) | Head of bank and network relationships | Notices acknowledged |
| 10. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.7) | Group CISO | Committee convened |

**Keep authorization running.** Nothing in this scenario touched SYS-P1, the token vault, or the HSMs. Stop a component only when forensics or the PFI shows it is affected.

## 4. Analysis (RS.AN)
1. **Initial access.** Confirm the phishing page, the relayed SMS code, and the federated session (SYS-M1 sign-in logs; SYS-G1 federation logs).
2. **What was taken.** From SYS-P6 application logs (AU-3 records the case identifier and record counts), list every exported case file. Extract card numbers, names, and expiry dates from the copies the division still holds; de-duplicate by card. Split by issuer (for the brands' at-risk account lists), by merchant, and by the cardholder's state where known.
3. **Window of exposure.** First export (Day -9) to containment (Day 0). Visa requires at-risk accounts within 3 calendar days of setting the window.
4. **Other access by the same identity.** ISV console views, SYS-P6 adjustment screens, and any other federated application. Confirm no adjustments were changed before restarting the interface.
5. **Exfiltration path.** Egress and DNS logs for the analyst's device and session origin; confirm no SYS-P1 or vault access.
6. **Preserve evidence** with hashes and chain of custody. Give the PFI read-only access. Do not access or alter compromised systems with administrator credentials, and do not reboot them.
7. **Root cause.** SMS-based MFA in SYS-M1, the case export permission, SYS-P6 events outside the SIEM, and standing cross-division console access. Feed these to P01 GR-02, PP-001, MC-001, and SW-003.

## 5. Containment and eradication (RS.MI)
1. Keep SYS-M1 federation off. Issue 400 priority dispute analysts temporary SYS-G1 accounts with hardware keys within 72 hours (accelerates POAM-001 and POAM-002); the rest wait for migration.
2. Remove the case export permission from all non-supervisor roles before re-enabling the function (accelerates POAM-003).
3. Remove standing consulting access to the ISV console; mask ISV keys (accelerates POAM-018).
4. Onboard SYS-P6 events to the SIEM with the bulk-export use case before reopening SYS-P6 to consulting users (accelerates POAM-004).
5. Reset passwords and revoke tokens for every SYS-M1 user; check SYS-M1 mailboxes for forwarding rules the attacker may have set.
6. Confirm with the PFI or forensic firm that no persistence remains in SYS-M1, SYS-G1, or SYS-P6 before declaring eradication complete.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (31 rows).** Counsel approves every legal notice before it goes out. The head of bank and network relationships keeps the card brand and bank clock table; the Group General Counsel keeps the rest.

### 6.1 Notice clock table
| Clock starts | Action | Deadline | Owner |
|---|---|---|---|
| Reasonable suspicion (Day 0, 10:05) | Sponsor banks A to D: suspected account data compromise | Within 24 hours (contract); immediately under Visa's rules | Head of bank and network relationships |
| Reasonable suspicion | Report to Visa through the sponsor banks; American Express within 72 hours of discovery (DSOP Section 3); Mastercard and Discover per their rules | 3 calendar days (Visa); 72 hours (American Express) | Head of bank and network relationships |
| Notice to Visa | Incident report to Visa and the acquiring banks | 3 calendar days after notice | Payment Processing division CISO |
| Window of exposure set | At-risk account numbers to Visa | 3 calendar days | Head of settlement operations |
| Software division learns ISV credentials exposed (Day 0, 11:30) | ISV notices | 24 hours | Software division client trust and assurance director |
| Determination for Bank D (Day 0, 13:40) | 12 CFR 304.24 notice | As soon as possible | Head of bank and network relationships |
| Severity 1 declaration | Disclosure committee convened | Within 24 hours (POL-03 4.7) | Group General Counsel |
| Consulting confirms client data affected (Day 1, 16:00) | Client notices under engagement letters | 72 hours | Merchant Consulting division president |
| Materiality determination | Form 8-K Item 1.05 if material | 4 business days after the determination | Disclosure committee |
| Determination of breach (Day 2) | Third-party agent notices to affected merchants (Florida 501.171(6)(a) and each other state's rule) | Florida outer limit 10 days | Group General Counsel |
| Discovery (Day 0) | FTC notice (580,000 consumers is far above 500) | As soon as possible; no later than 30 days | Group General Counsel |
| Day 0 to 2 | Voluntary report to the U.S. Secret Service or FBI and CISA | As soon as practicable | Group CISO |

**Plan to the shortest clock.** In this scenario the order is: the 24-hour sponsor bank and ISV notices and the Bank D notice on Day 0, the Visa reports by Day 3, client notices by Day 4, merchant third-party agent notices by Day 12, and the FTC by Day 30. Merchants need the group's notice early, because their own state-law clocks start when they learn of the breach.

### 6.2 Bank service provider decision (12 CFR 53.4; 225.303; 304.24)
- **Trigger:** a computer-security incident that has materially disrupted or degraded, or is reasonably likely to materially disrupt or degrade, covered services to a sponsor bank for four or more hours. Covered services here: clearing, settlement, reconciliation, and merchant funding files (sponsor agreements; 12 U.S.C. 1867(c)).
- **Apply it to this scenario.** The card data theft itself did not disrupt covered services. The containment step did: pausing the adjustment interface at 13:10 meant no funding file could be released until adjustments were verified, expected around 21:00.
  - **Bank D** (FDIC, cutoff 17:00): disruption reasonably likely to exceed 4 hours. Determination at 13:40; notice under 304.24 at 14:15. Bank D has no designated contact on file, so the notice went to its CEO and CIO under 304.24(a)(2), the same fallback as 53.4(a)(2). The file was released at 22:05, about 5 hours after cutoff.
  - **Banks A, B, and C** (later cutoffs): delay expected under 4 hours. Determination "not reasonably likely" recorded at 13:40 and reviewed at 18:00; files met their cutoffs. No rule notice; they already had the contract notice from step 9.
- **Record the decision for every bank, either way.** Each bank uses it for its own 36-hour decision under 53.3, 225.302, or 304.23.

### 6.3 FTC notice decision (16 CFR 314.4(j))
- **Is it a notification event?** Card numbers and names were exported in readable form: acquisition of unencrypted customer information without the cardholders' authorization (314.2(m)). Yes.
- **Who counts?** Cardholders are customers of their issuing banks. The rule covers that information in the division's possession (314.1(b)), and the group counts affected cardholders toward the 500 (conservative reading; counsel confirms). About 580,000.
- **Who notifies?** The Payment Processing division (SYS-P6 is its system). The Software division's ISV credentials are not consumer customer information, so it has no FTC notice of its own here.
- **What the notice contains (314.4(j)(1)(i)-(vi)):** the institution's name and contact, the types of information involved, the date or date range, the number of consumers affected, a general description of the event, and whether a law enforcement official has asked in writing for a delay of public notice.
- **Deadline:** as soon as possible and no later than 30 days after discovery (Day 0).

### 6.4 Merchant, client, ISV, and state-law notices
- **Merchants (about 41,000).** For cardholder data the processor is its merchants' third-party agent. It must give each affected merchant the information it needs for its own notices: no later than 10 days after determination under Fla. Stat. 501.171(6)(a), and within whatever each other state requires. The processor may send notices on a merchant's behalf (501.171(6)(b)).
- **Which states' definitions are met** is decided by counsel state by state. Florida counts a card number as personal information only with any required security code, access code, or password (501.171(1)(g)); these records have names and card numbers but no codes, so counsel's working view is that Florida's definition may not be met for most records. Other states' definitions differ, so the generic state row stays active and merchants get notice either way.
- **Consulting clients (1,150 of the merchants).** Engagement letters add a 72-hour client notice; send it with the merchant notice content.
- **ISVs (37).** 24-hour notice under the ISV agreement, with the new keys and the card-testing indicators.
- **SOC 2 user entities.** The Software division tells merchants and ISVs what happened to the ISV console under its SOC 2 commitments; the event goes into the next system description.

### 6.5 SEC materiality and communications
**Materiality factors for the disclosure committee:** number of cardholders and merchants affected; card brand assessments and PFI costs; sponsor bank relationships (four banks, one with a missed cutoff); FTC and state attorney general exposure; ISV and merchant churn; cost of notification and remediation; and effects on operations (limited: authorization never stopped). Materiality is decided without unreasonable delay. The 4-business-day clock for Form 8-K Item 1.05 starts at the determination, not at discovery.

**Communications:** merchants, ISVs, and clients get counsel-approved notices after the sponsor banks are informed; staff briefings say what happened, what not to say, and where to send questions; no public statement without counsel and the disclosure committee.

**Ransom or extortion:** none in this scenario. Any demand goes to the board risk committee, counsel, the insurer, and an OFAC sanctions check (POL-03 4.9). Paying does not remove any notice duty when data was taken.

### 6.6 Earlier event: PAN in the group data platform (2026-05-08 to 2026-06-18)
A Software division gateway debug log field wrote full PANs with expiry dates (no names, no security codes) into the raw log zone of the group data platform (SYS-G4) from 2026-05-08. A weekly PAN discovery scan found it on 2026-06-18; the data was purged on 2026-06-20 after access logs were preserved. About 2.9 million unique PANs were involved. The notice analysis was completed by the Group General Counsel with outside counsel on 2026-06-26:

- **Access.** The raw log zone is limited to 46 data engineers through SYS-G1. Access logs for the whole window show only the automated parsing jobs reading the field. No query selected it and no export occurred.
- **FTC.** The logs are reliable evidence that there was no unauthorized acquisition, which rebuts the presumption in 16 CFR 314.2(m). **Not a notification event**; no FTC notice from the Software division or the processor.
- **State law.** No names or security codes were stored with the PANs, so the data did not meet Florida's definition of personal information (501.171(1)(g)). Counsel checked other states' definitions with the same result. No merchant or individual notice.
- **Card brands and banks.** No reasonable suspicion of unauthorized access to account data, so no brand compromise report was due. No covered service was disrupted, so no bank service provider notice was due. The four sponsor banks and the six unaffiliated processors were informed on 2026-06-24 as a PCI DSS compliance matter, not a compromise.
- **PCI DSS.** Handled under 12.10.7 and disclosed to both QSAs. The PAN block now covers every log source (POAM-024, closed 2026-06-30).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). In this scenario:
1. Identity: SYS-G1 confirmed clean; SYS-M1 federation stays off (BP-G01)
2. Data centers, network, and authorization: never stopped; verify no access to SYS-P1, the vault, or the HSMs (BP-PP01, BP-PP02)
3. SOC visibility: SYS-P6 events onboarded before SYS-P6 reopens (BP-G02)
4. Gateway: new ISV keys in use; card-testing blocks in place (BP-SW01)
5. Settlement and funding: adjustments verified; adjustment interface restarted at 21:00; Bank D file released 22:05; reconcile with each bank the next morning (BP-PP03, BP-PP04)
6. Dispute work: 400 analysts on temporary SYS-G1 accounts within 72 hours; deadline triage list worked by processor chargeback staff meanwhile (BP-PP07, BP-MC01)

**Validate before closing:** the PFI or forensic firm confirms eradication; the SYS-P6 bulk-export detection has been tested; no SMS-based sign-in reaches any CDE; all 37 ISV keys rotated.

## 8. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.13).
- Update P01 (GR-02, GR-03, PP-001, PP-007, MC-001, SW-003), the POA&M (POAM-001 to POAM-006, POAM-018), the notification matrix, and this runbook.
- Give both QSAs the incident report, the PFI report, and remediation evidence. A compromise may require an out-of-cycle assessment at a brand's or sponsor bank's request.
- Include the incident and management's response in the next Qualified Individual report to the board (16 CFR 314.4(i)) and consider it in the Reg S-K Item 106 disclosure.
- Retain all incident records for at least 5 years (POL-01 4.11), or longer if counsel or a brand requires.
