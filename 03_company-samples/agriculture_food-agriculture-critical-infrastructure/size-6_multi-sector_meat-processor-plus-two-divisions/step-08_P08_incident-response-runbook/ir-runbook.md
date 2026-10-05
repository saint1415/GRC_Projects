# Incident Response Runbook: Ransomware Halting Processing Lines and Cold-Chain Monitoring Across Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Food and Agriculture |
| Incident type | Ransomware with data theft that enters through the corporate directory (a shared service), halts processing lines at two plants, stops cold-chain alerting for plants, DCs, trailers, and stores, disrupts DC automation and store back offices, and steals employee data |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; food safety decisions owned by the Group Chief Food Safety and Quality Officer; notifications owned by the Group General Counsel |
| Approved | 2026-09-15 by the Group CISO, the Group Chief Food Safety and Quality Officer, and the Group General Counsel |
| Last tested | IT playbooks tested quarterly. **The cross-division notification matrix and the product hold steps have not been exercised** (scenario gap 6); the first cross-division tabletop is due 2026-12-15 (POAM-011) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** an attacker phishes a Food Distribution IT administrator with an adversary-in-the-middle page, steals a session token, and from that administrator's workstation harvests the password of one of the 34 privileged directory service accounts outside PAM (P07 AC-2 finding; POAM-012). That account has domain administrator rights.
- **Dwell:** over 5 days the attacker copies HR payroll exports (names and Social Security numbers of about 45,000 current and 18,000 former employees; about 26,000 live in Florida) and a reporting-server extract of 1.1 million loyalty members' names, emails, phones, and addresses (no passwords, no card data).
- **Impact (Day 0, Saturday 02:00):** ransomware is pushed through group policy to every server joined to the corporate domain: corporate file servers, back-office servers in 120 stores, DC automation servers at five DCs, the **cold-chain alert integration server** in the colocation data center, and **SCADA, historian, and MES servers at Plants 2 and 5** (which are on the corporate domain and have no EDR). Plants 1, 3, 4, and 6 run a separate OT domain behind an OT DMZ and are not encrypted. POS lanes sit in the segmented CDE and are not domain-joined; forensics must confirm they were not reached.
- **What stops:** lines at Plants 2 and 5; temperature **alerts** for all 6 plants, 5 DCs, 900 trailers, and 120 stores (sensors and gateways keep recording and buffer readings for 24 hours, and Plants 1, 3, 4, and 6 still see historian alarms in their control rooms); automated freezer retrieval at DC-1 and DC-3; store ordering and time clocks. An extortion note names "Cris Santos Company" and claims employee and customer data.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Food safety lead (all divisions) | Group Chief Food Safety and Quality Officer | Division VP FSQA | Food safety bridge |
| Plant OT leads (safe state, containment, recovery) | Plant controls engineers at Plants 2 and 5; Division controls engineering manager | Group's standard integrator (on site only) | Plant radios and cell |
| Refrigeration and ammonia safety | Plant and DC refrigeration managers | Refrigeration contractors (on site) | Site PSM emergency response plans |
| DC and fleet lead | Division food safety manager (Distribution) with the fleet director | DC general managers | Division bridge |
| Store operations lead | Retail store operations VP | Retail food safety director | Division bridge |
| Payment card lead | Grocery Retail payments security manager | QSA contact | Division bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division counsel | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group CFO | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker controls the corporate directory and can read email and chat. Use the crisis line, managed mobile devices, and plant radios. The printed binder in each plant control room, DC office, and the corporate command center holds contacts, this runbook, the notification matrix, manual CCP and temperature log forms, and signed formulation sheets.

## 2. Preparation checks (Identify / Protect)
- [x] Separate OT domain and OT DMZ at Plants 1, 3, 4, and 6 (they stay up in this scenario)
- [x] Immutable cloud backups in provider B with a separate backup identity (CP-9; P07 satisfied)
- [x] Historian alarms in control rooms at four plants as a fallback for cold storage monitoring
- [ ] OT servers at Plants 2 and 5 and DC automation off the corporate domain (**gap until POAM-001 and POAM-018 close**)
- [ ] All privileged service accounts vaulted in PAM (**gap until POAM-012 closes**)
- [ ] Offline, tested OT backups at Plants 2 and 5 (**gap until POAM-009 closes**)
- [ ] Second, tested node for the cold-chain alert integration server and local fallback alarms at DCs (**gap until POAM-005 closes**)
- [ ] Notification matrix exercised with product hold, card, and materiality decisions (**gap until POAM-011 closes**)
- [x] Forensic retainer with OT capability confirmed through the insurer's panel
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note or encrypted files on any server | EDR, staff reports, plant operators | Declare Severity 1; open the bridge. In OT, **do not power off** SCADA, historians, or MES; disconnect the network cable |
| Cold-chain alerts stop arriving, or the dashboard shows "integration offline" | Site on-call staff; SOC | Start manual temperature logs at every site at once; call the bridge |
| HMIs show "communication lost" or MES will not load formulations | Plant operators | Line supervisor calls the plant controls engineer and the bridge |
| Mass group policy changes or new domain administrator activity | SIEM; SYS-G1 alerts | Disable the account; start triage |
| Setpoint or formulation values that nobody approved | Operators, FSQA | Treat as possible tampering: stop the step; call FSQA and the bridge |
| Extortion email or leak-site post naming the group | Email, threat intelligence, law enforcement | Declare Severity 1; preserve the message |

**Severity 1** (group scale, POL-03 4.2): confirmed encryption or exfiltration in a shared service, or any incident that stops production or temperature monitoring in more than one site.

**Record the times that drive clocks** (POL-03 4.4): discovery; for each plant, DC, and store, the time of the last trusted temperature or CCP record and the start of manual monitoring; and later, the date of each food safety and breach determination.

## 4. First hours: make product and people safe (RS.MA, RS.MI)
**Order matters.** People, then product, then evidence and systems.

| Step | Who | Done when |
|---|---|---|
| 1. Confirm refrigeration is running on local controllers and ammonia detection is normal at every plant and DC-1 and DC-3. If a controller shows tampering, switch to manual operation under PSM procedures | Plant and DC refrigeration managers | Every engine room reports stable |
| 2. Start manual temperature logs (at least hourly; every 2 hours for store cases) at every plant cooler and freezer, DC room, and store case; drivers check reefer displays at each stop | Site on-call roles; fleet dispatch | First manual entries recorded at every site |
| 3. Put Plants 2 and 5 lines in a safe state: finish intact smokehouse cycles on local controllers or abort and hold; stop dosing and injection; close CIP valves manually | Plant operations managers with the plant controls engineers | Every line stopped or finishing a verified cycle |
| 4. **Hold product** (POL-03 4.3): at Plants 2 and 5, everything made, cooked, chilled, or stored since the last trusted CCP record and anything dosed since the last verified formulation; at DCs and stores, nothing is held unless manual readings or buffered gateway data show an excursion | Plant FSQA managers; Division food safety manager (Distribution); retail food safety director | Hold tags and hold lists by site |
| 5. Isolate: disable the compromised service account and the administrator identity; cut the colocation-to-plant links for Plants 2 and 5; keep Plants 1, 3, 4, and 6 OT domains isolated from the corporate domain; leave encrypted hosts powered on for memory evidence | Group identity director; Group OT security director | Accounts disabled; links down; photos of cable positions |
| 6. Confirm the provider B vault and the OT backups at Plants 1, 3, 4, and 6 are intact and unreachable from the compromised identities | Group infrastructure director; Division controls engineering manager | Integrity reports |
| 7. Call the cyber insurer; engage breach counsel and an OT-capable forensic firm through the panel | Group Chief Risk Officer | Claim number issued |
| 8. Brief FSIS inspection program personnel at Plants 2 and 5 (and at the other plants about the alert outage) that manual monitoring and holds are in place | Plant FSQA managers | Briefing times recorded |
| 9. Escalate to the disclosure committee within 24 hours (POL-03 4.6) | Group CISO | Committee convened |

## 5. Analysis (RS.AN)
1. **Scope.** Which servers, accounts, and sites are affected? Check EDR, SYS-G1 sign-ins, group policy history, firewall and VPN logs, and cloud audit logs. WMS and DC automation logs are kept only 30 days (POAM-019); pull them now.
2. **Did the attacker touch the process?** With the plant controls engineers, compare PLC programs at Plants 2 and 5 with the best available copies (the 2024 integrator backups, since the plant backups were on domain storage) and every formulation in MES with the signed masters. Check CIP logic and dosing skids. **Any unexplained difference is treated as possible intentional adulteration**: the product stays on hold, and for Plant 6, a food defense corrective action and reanalysis decision follow (21 CFR 121.145, 121.157(b)(3)).
3. **Temperature evidence by site.** Pull buffered gateway readings, historian alarms, and manual logs for every site to show whether any excursion occurred during the alert outage. Telematics data for trailers is pulled from the vendor portal.
4. **Card data.** Forensics confirms whether the attacker reached the CDE from the store back-office servers. Until confirmed, treat as suspected (Grocery Retail supplement).
5. **Personal information by state.** Count affected employees (current and former) by state of residence. Counsel decides, state by state, whether the loyalty extract (names and contact details only) is personal information; under Florida's definition it is not (501.171(1)(g)1.).
6. **Root cause:** the phishing path, the unvaulted service account, and the domain trust into OT at Plants 2 and 5. Feed to P01 GR-01, GR-02, and GR-12.

## 6. Containment and eradication (RS.MI)
1. Rebuild the directory from offline system-state backups in an isolated environment; reset every privileged and service account; reset the Kerberos ticket-granting account twice.
2. Rebuild corporate, store back-office, DC automation, and Plants 2 and 5 OT servers from clean media. **Do not decrypt and reuse them.**
3. **Do not rejoin Plants 2 and 5 OT servers to the corporate domain.** Rebuild them in the OT domain behind a temporary DMZ (accelerates POAM-001).
4. Reload PLC programs at Plants 2 and 5 from verified copies if any comparison in section 5 step 2 failed or could not be completed.
5. Keep the integrator VPN and the Plant 5 modem disconnected; vendors work on site under escort (POAM-002).
6. Confirm with forensics that persistence is removed before reconnecting any site.

## 7. Food safety decisions and reporting (RS.CO)
**Food safety decisions come first and run on their own clock.** The FSIS and FDA 24-hour clocks start at *determination*, not discovery, but determination must be made with reasonable speed. Do not wait for IT recovery.

**Product on hold.** Each plant FSQA manager documents the unforeseen-deviation review (9 CFR 417.3(b)): segregate and hold, determine acceptability from manual records, chart recorders, buffered data, and product testing, and dispose of anything that cannot be shown safe. Plant product may not ship until its records are complete (9 CFR 417.5(c)). At DCs, any loss of temperature control that may affect safety triggers corrective action and evaluation of affected food (21 CFR 117.206(a)(3)); loads whose in-transit data is missing are treated as a possible material temperature failure and are not sold until a qualified individual decides (21 CFR 1.908(a)(6)).

**Follow `notification-matrix.csv` (28 rows).** Counsel approves every external notice except FSIS and FDA food notices, which FSQA makes with counsel informed. The matrix has three layers:
1. **Food safety duties by site:** FSIS 24-hour notice per plant (9 CFR 418.2) if adulterated or misbranded product entered commerce; Reportable Food Registry within 24 hours for Plant 6 and the DCs if a reportable food is determined (21 U.S.C. 350f(d)); receiver communication for in-transit failures (21 CFR 1.908(a)(6)).
2. **Personal information duties:** each employing entity notifies affected employees under the law of each state where they reside (Florida worked example: individuals within 30 days of determination, the Department of Legal Affairs within 30 days for 500 or more Floridians, consumer reporting agencies for more than 1,000).
3. **Group and contractual duties:** SEC materiality (Form 8-K Item 1.05); acquirer and card brands if card compromise is suspected (contract; timing not verified); 3PL customers within 72 hours of discovery (contract); supply customers per agreement; insurer.

| When (from SOC discovery, Day 0) | Action | Owner |
|---|---|---|
| Hour 0-2 | Insurer, counsel, and forensics engaged; manual monitoring and holds in place; FSIS personnel briefed | Group Chief Risk Officer; plant FSQA managers |
| Day 0-1 | Decide for each plant whether any **already-shipped** product may be adulterated or misbranded (for example, Plants 2 and 5 product shipped Friday after an unexplained formulation change). If so, notify the FSIS District Office **within 24 hours** of that determination and start the recall procedure (9 CFR 418.2, 418.3) | Plant FSQA managers with the Group Chief Food Safety and Quality Officer |
| Day 0-1 | Same question for FDA-regulated food from Plant 6 and the DCs: Reportable Food Registry within 24 hours of a reportable food determination (21 U.S.C. 350f(d)) | Plant 6 FSQA manager; Division food safety manager (Distribution) |
| Day 0-1 | Tell receivers of any load with a possible material temperature failure not to sell it until a qualified individual decides (21 CFR 1.908(a)(6)) | Fleet director with the Division food safety manager (Distribution) |
| Day 0-1 | Voluntary report to FBI or IC3 and CISA (supports OFAC mitigation if payment is considered) | Group CISO |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts (POL-03 4.6) | Group General Counsel |
| As the acquirer contract requires | Acquirer notice if CDE compromise is suspected; forensic investigator if required (timing not verified) | Grocery Retail payments security manager |
| Within 72 hours of discovery | 3PL customer notices (contract term) | 3PL services director |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 10 days (inbound) | Any third-party agent holding employee data must tell the group of its own breach (Fla. Stat. 501.171(6)) | Vendors, to the Group General Counsel |
| Within 30 days of determination | Florida individual notices; Department of Legal Affairs notice (500 or more Floridians); consumer reporting agencies (more than 1,000). Apply each other state's law the same way | Each employing entity with the Group General Counsel |
| Not in effect | CIRCIA reports to CISA (72 hours; 24 hours for a ransom payment) would apply if the final rule keeps the proposed size criterion | Group CISO (tracked) |

**Plan to the shortest clock.** In this scenario the order is: FSIS and RFR food determinations (24 hours from determination), disclosure committee (24 hours from declaration), 3PL customers (72 hours from discovery), SEC (4 business days from materiality), then state breach notices (Florida 30 days from determination).

**Materiality factors for the disclosure committee:** production lost at two plants and the cost of held and destroyed product; DC and store disruption; any recall; the number of employees affected and regulator exposure in several states; 3PL and supply customer contracts; cost of recovery; and reputational effect of a food company's incident. Materiality is decided without unreasonable delay; the 4-business-day clock starts at the determination.

**Ransom decision:** board risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not make held product safe or remove any notice duty.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7):
1. Directory rebuilt clean, break-glass access confirmed (BP-G01)
2. Colocation, hub, and WAN links (BP-G03), keeping Plants 2 and 5 isolated
3. Cold-chain alert integration rebuilt from code on a clean host, then alerts tested site by site (BP-G04); manual logs continue until each site confirms alerts
4. SOC visibility (BP-G02)
5. to 8. Refrigeration control, plant cold storage, DC storage, and store case monitoring confirmed
9. Store back-office servers (checkout continued on lanes)
10. to 14. Plants 2 and 5: SCADA and historians rebuilt in the OT domain, MES restored, **every formulation compared with the signed master** before any dosing; DC automation and picking
15. onward: ERP integrations, food safety records entry of manual logs, traceability, store replenishment, online ordering, 3PL portal updates, payroll, loyalty.

**Validate before restart** (POL-03 4.11): each line at Plants 2 and 5 restarts only after the plant controls engineer confirms PLC programs and formulations match approved versions, the plant FSQA manager signs a restart checklist, labels and lot codes are verified, and the first batch is verified against critical limits. Tell staff, customers, 3PL brands, and FSIS personnel when normal monitoring resumes (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10).
- Update P01 (GR-01, GR-02, GR-03, GR-12, MT-001, MT-004, FD-001, RT-007), the POA&M (POAM-001, POAM-005, POAM-009, POAM-011, POAM-012), the notification matrix, and this runbook.
- Reassess HACCP plans at Plants 2 and 5 if the deviation was unforeseen (9 CFR 417.3(b)(4)); reanalyze the Plant 6 food defense plan if tampering was found or could not be ruled out.
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain incident records for at least 6 years (POL-01 4.11), and product hold and disposition records with the HACCP records.
