# Incident Response Runbook: Ransomware Across Farm OT, the Farm Data Hub, and ERP

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Agriculture, Forestry, Fishing and Hunting |
| Incident type | Ransomware on farm-management and irrigation control systems that enters through the irrigation integrator's remote access at an acquired farm, encrypts ROC SCADA, the farm data hub, and ERP application servers, and steals payroll and H-2A files and Farm Supply grower credit files (double extortion) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT response steps follow NIST SP 800-82 Rev. 3 sections 6.4 and 6.5 |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; OT safety steps owned by the Crop Farming and Food Processing OT security managers; notifications owned by the Group General Counsel |
| Approved | 2026-09-10 by the Group CISO and the Group General Counsel |
| Last tested | IT playbooks tested quarterly. **The multi-regulator notification matrix and the OT steps have never been exercised** (EV-012; P07 EV-C-IR6). First freeze-season tabletop due 2026-12-15 (POAM-010); manual freeze drill due 2026-11-15 (POAM-008) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **When:** a Saturday in mid-January, freeze season. The forecast at ROC-1 is 28 degrees F by 04:00, and overhead freeze protection must start on about 4,200 acres of strawberries at the trigger temperature.
- **Entry (Day -9):** an attacker logs in to the irrigation integrator's always-on remote tool at an acquired farm with the shared account (P01 CF-001), then harvests cached credentials of a farm operations directory domain administrator from the site server (CF-002).
- **Spread:** with domain administrator rights the attacker reaches ROC-1 and ROC-2 SCADA servers and HMIs, then uses the two-way path between ROC SCADA and the farm data hub (CF-004) to reach the corporate cloud network, the ERP application servers, the payroll interface share, and the grower credit file share (FS-005).
- **Impact (Day 0, 01:50):** the attacker encrypts ROC-1 and ROC-2 SCADA servers and HMIs, the farm data hub, and ERP application servers, and posts a leak-site notice naming the group.
- **Data taken (forensic estimate at Day 4):** payroll and H-2A files for about 14,800 Crop Farming workers, including about 8,600 H-2A workers with passport and visa numbers and home-country addresses (about 5,200 Florida residents among the non-H-2A workers); grower credit files for about 12,000 individual growers with Social Security numbers (about 4,100 in Florida). No card data and no Grower Agronomy Portal data.
- **Not affected:** plant OT and ammonia refrigeration (the MES domain has no trust to the farm operations directory, and contractor access is through group PAM), the FMIS tenant (vendor SaaS, confirmed by the vendor), and the immutable backup vault in provider B.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile phones) |
| OT safety lead, farms | Crop Farming OT security manager with the ROC-1 lead | Crop Farming VP Irrigation and Field Technology | ROC radio channel; crisis line |
| OT safety lead, plants | Food Processing plant OT security manager | Plant managers | Crisis line |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC, cloud, and identity teams; OT assessment firm | Forensic firm on retainer (insurer panel) | SOC bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Group Chief Privacy Officer | Out-of-band bridge |
| Food safety decisions | Group VP Food Safety and Quality | Crop Farming Director of Food Safety; Food Processing VP Food Safety and Quality | Division bridge |
| Workers, payroll, H-2A records | Crop Farming labor compliance director with Group HR | Farm office managers | Division bridge |
| Growers and cooperatives | Farm Supply credit director; digital agronomy general manager | Farm Supply security and compliance lead | Division bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads (English and Spanish) | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email and chat. Use the crisis line, radios at ROCs and farms, and the printed binder in each ROC, plant, and division command center (contacts, this runbook, the notification matrix, paper tally cards, paper Produce Safety forms, and the manual freeze procedure).

## 2. Preparation checks (Identify / Protect)
- [x] Immutable backups of the farm data hub, ERP, and traceability in provider B with a separate backup identity (CP-9; P07 satisfied)
- [x] 24x7 SOC with EDR on IT and legacy ROC servers (SI-3, SI-4)
- [x] Plant MES domain has no trust to the farm operations directory; refrigeration contractor only through group PAM
- [ ] Integrator access only through group PAM (**gap until POAM-001 closes, 2026-11-15**; interim: tool switched off outside approved windows)
- [ ] No connection path from the farm data hub into ROC SCADA (**gap until POAM-002 milestone, 2026-11-30**)
- [ ] Farm directory administrators under PAM with MFA (**gap until POAM-003, 2026-12-31**)
- [ ] Manual freeze procedure written and drilled at every ROC-1 farm (**gap until POAM-008 milestone, 2026-11-15**)
- [ ] Division-held PLC programs and immutable offsite ROC backups (**gap until POAM-013, 2026-12-31**)
- [ ] OT monitoring at all farms (**gap until POAM-006, 2027-06-30**)
- [ ] Notification matrix exercised across divisions (**gap until POAM-010, 2026-12-15**)
- [x] Forensic retainer and insurer panel confirmed; disclosure committee charter covers cybersecurity

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| HMI or SCADA screen replaced by a ransom note; HMIs unresponsive | ROC operators | Call the crisis line. **Do not power off.** Start the safe-state steps in section 4 at once |
| A pump, pivot, valve, or fertigation pump starts, stops, or changes rate when nobody scheduled it | ROC operators; irrigation technicians; OT monitoring (9 farms) | Put the equipment in local or Hand control; declare Severity 1 |
| Remote tool session nobody requested | ROC lead; OT monitoring | End the session; disable the tool account; declare |
| Encryption or mass file changes on the hub or ERP servers | EDR; cloud audit logs | Declare Severity 1; isolate the account |
| Extortion note or leak-site post naming the group | Email; threat intelligence; law enforcement | Declare Severity 1; preserve the message |

**Severity 1** (group scale, POL-03 4.2): any confirmed manipulation or encryption of OT, any incident in a shared service, or any incident affecting more than one division.

**Record the clock start times.** Record separately: discovery (Day 0, 01:50), the determination that personal information was accessed (drives state notices), awareness of an event affecting lots or volumes (buyer and customer 24-hour terms), and the materiality determination (Form 8-K). Notice clocks start at different events; none is planned from a later date than the facts support.

## 4. First hours (RS.MA, RS.MI): safety and the crop first
| Step | Who | Done when |
|---|---|---|
| 1. **Freeze protection by hand.** ROC-1 lead calls every ROC-1 farm by radio; freeze crews go to the overhead systems and start each one by hand at the trigger temperature read from field thermometers. Do not trust SCADA or the FMIS until section 6 is complete | ROC-1 lead; farm managers | All ROC-1 freeze blocks running by hand before the trigger temperature |
| 2. **Safe state for everything else.** Pumps and pivots to local or Hand control; **fertigation injection off and valves closed** at every farm on ROC-1 and ROC-2 | Irrigation technicians | Each farm reports to its ROC by radio |
| 3. Disconnect ROC-1 and ROC-2 networks from the WAN and the farm data hub at the ROC firewall; leave encrypted hosts powered on for memory evidence | Crop Farming OT security manager | ROC uplinks down; hosts on |
| 4. Disable the integrator remote tool account and the farm directory administrator accounts; force password resets from a clean device using break-glass accounts | Group identity director | Accounts disabled |
| 5. Isolate the farm data hub and ERP accounts from the hub network in provider A; keep provider B workloads (the portal) running | Group cloud platform director | Isolation rules applied |
| 6. Confirm plant OT and ammonia refrigeration are unaffected: plant OT managers check for unexpected mode or setpoint changes; licensed operators stand by to run refrigeration locally | Food Processing plant OT security manager | Each plant reports clean or not clean |
| 7. Confirm the provider B vault and DR replica are intact and unreachable from compromised identities | Group cloud platform director | Vault integrity report |
| 8. Call the insurer hotline; engage breach counsel and forensics (including OT forensics) through the panel | Group Chief Risk Officer | Claim number issued |
| 9. Start paper operations: tally cards to crew leads, paper Produce Safety forms, signed lot manifests per load, hourly cooler checks | Farm managers; Crop Farming Director of Food Safety | Paper workflows running |
| 10. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.6); inform the Group VP Food Safety and Quality at declaration (POL-03 4.8) | Incident commander | Committee convened; food safety lead on the bridge |

**If a release or an unsafe condition appears at a plant**, the plant's emergency response plan takes over and the release reporting rows of the matrix apply (40 CFR 302.6; 355.40-355.42). Security steps never delay a safety response.

## 5. Analysis (RS.AN)
1. **Initial access and spread:** confirm the remote tool, the directory credentials used, and the path from ROC SCADA to the hub and ERP. Pull remote tool history, directory logs (exported before they roll over), hub flow logs, and cloud audit logs.
2. **OT integrity:** did the attacker change PLC logic, setpoints, schedules, fertigation limits, or freeze triggers before encrypting? Compare programs with division-held approved copies where they exist; at acquired farms, get the integrator's copies and treat them as untrusted until verified. **If any fertigation setting changed, treat the affected blocks as a possible food safety issue** and go to the buyer and Food Processing rows in section 7.
3. **Data taken:** confirm which payroll, H-2A, and credit files left (file access logs, egress). Map each person to a state of residence; H-2A workers to home-country addresses.
4. **Lots affected:** list harvest lots shipped since the earliest possible tampering date from affected farms, so buyers and Food Processing can make their own decisions.
5. **Scope check of other divisions:** Food Processing MES domain, Farm Supply card data environment, and the portal. Confirm with logs, not assumptions.
6. **Preserve evidence** with chain of custody: HMI and server images, PLC programs, remote tool logs, cloud snapshots.

## 6. Containment and eradication (RS.MI)
1. Remove the remote tool from every acquired farm server; integrator access only through group PAM from now on (accelerates POAM-001).
2. Rebuild the farm operations directory or move ROC authentication to a new, PAM-protected directory; rotate every OT credential, modem password, and service account (accelerates POAM-003, POAM-004).
3. Block the hub-to-ROC path permanently; stand up the ROC-1 OT DMZ before reconnecting (accelerates POAM-002).
4. Rebuild SCADA servers and HMIs from clean media; load PLC programs only after their hashes match approved versions.
5. Rebuild ERP application servers from infrastructure code and restore data from the vault.
6. Forensics confirms no persistence in SYS-G1, the landing zone, division accounts, or OT before reconnection.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (34 rows).** Counsel approves every notice. In this scenario the divisions owe different notices to different people, on different clocks:

| When (from Day 0 discovery unless noted) | Action | Owner |
|---|---|---|
| Day 0 | Insurer, counsel, and forensics engaged; FBI or IC3 and CISA informed (voluntary; supports OFAC mitigation) | Group Chief Risk Officer; Group CISO |
| Within 24 hours of awareness | **Buyers** told of the event and the lots that may be affected (Crop Farming buyer agreements); **Food Processing** told the same as an internal customer | Crop Farming Director of Food Safety |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Day 0 to 2 | Crew meetings in Spanish and English: what happened, paper procedures, whom to call | Farm managers with crew leads |
| Each payday | H-2A earnings statements issued on time from paper tally (20 CFR 655.122(k)) | Crop Farming labor compliance director with Group HR |
| On request | Produce Safety records within 24 hours (112.166(a)); H-2A records within 72 hours (655.122(j)(2)); Food Processing records within 24 hours (1.361) | Records owners |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 10 days of the agent's determination | Inbound: any third-party agent (payroll SaaS, H-2A filing agent) must report to the group if its own system was involved | The agents |
| Within 30 days of the determination | State notices to individuals (Florida worked example: 501.171(4)); Department of Legal Affairs if 500 or more Floridians (501.171(3)); consumer reporting agencies if more than 1,000 (501.171(5)). Apply each other state's law the same way. H-2A workers notified at home-country addresses in Spanish and English (group policy) | Group Chief Privacy Officer; Crop Farming and Farm Supply as notifying entities |

**Not triggered in this scenario, and why:** card brands and acquirer (card data environment not involved), cooperative 72-hour notice (no portal data involved; cooperatives still get a courtesy update because their growers' credit files were taken), Reportable Food Registry (no reportable food determination unless the OT integrity analysis finds tampering that may have adulterated shipped product), FAR 52.204-23 and 52.204-25 reports (no covered article or covered telecommunications equipment involved; their clocks are 3 business days and 1 business day of identification, each followed by 10 business days), ammonia release reports (plant OT not affected), and CIRCIA (not in effect).

**Plan to the shortest clock.** In this scenario the order is: buyer and Food Processing notices (24 hours), disclosure committee (24 hours), Form 8-K (4 business days after a materiality determination), then state notices (30 days after determination in Florida). Records requests can arrive at any time and must be met from paper and exports.

**Materiality factors for the disclosure committee:** crop loss if freeze protection failed; number of people affected (about 26,800 across workers and growers) and the sensitivity of passport and Social Security data; effects on supply to buyers and Food Processing customers; recovery and notification cost; regulatory exposure (state attorneys general, DOL, FDA records requests); and reputational effects with growers and cooperatives. Materiality is decided without unreasonable delay; the 4-business-day clock starts at the determination.

**Ransom decision:** board risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove notice duties for data that was taken, and it does not make SCADA or PLC programs trustworthy again.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Freeze protection and irrigation stay by hand until verified (people and crop first)
2. Identity (SYS-G1, break-glass), landing zone, WAN, and SOC visibility (BP-G01 to BP-G04)
3. **ROC-1 SCADA** rebuilt on the new segmented design; return to automatic control **one pump and one pivot at a time** with the ROC-1 lead watching a full cycle; freeze triggers tested before the next freeze night (BP-CF01)
4. Cold chain alarms at farm packing sheds and coolers (BP-CF06)
5. Harvest tally on clean tablets (FMIS unaffected); paper tally keyed and reviewed (BP-CF03)
6. Harvest lot records and the lot feed to Food Processing, with signed manifests reconciled (BP-CF04, BP-FP04)
7. ERP order-to-cash and payroll from the vault (BP-G05, BP-G06)
8. **Fertigation last on each farm**, after a supervised low-rate test and a hash check of the controller program (BP-CF02)
9. Farm data hub from the vault, behind the OT DMZ; credit file share with restricted access (POAM-022)

**Validate before reconnecting:** credentials rotated, systems patched, EDR clean where supported, PLC programs match approved versions, safe-state settings tested. Tell crews, buyers, Food Processing, growers, and the insurer when each process is back (RC.CO).

**End of recovery:** declared by the incident commander when BP-CF01 to BP-CF04 run on automation for 72 hours without anomalies and the paper tally for the incident period has been keyed and reconciled with payroll.

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10).
- Update P01 (GR-01, GR-02, GR-12, CF-001 to CF-004, FS-005), the POA&M (POAM-001 to POAM-008, POAM-010, POAM-013, POAM-022), the notification matrix, and this runbook.
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain incident records for 6 years (POL-01 4.12), and any Florida no-harm determination for at least 5 years (Fla. Stat. 501.171(4)(c)).
