# Incident Response Runbook: Intrusion into the Batch Control System

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical maker) |
| Tier / Vertical | Micro / Chemical |
| Incident type | Intrusion into the batch control system through the integrator's shared portal login. The attacker raises the hydrogen peroxide dose in a T-1 recipe and widens the T-1 high-temperature alarm, then runs ransomware on the HMI PC, which spreads toward the office over the flat network |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Operations Manager (incident commander), with the Office Manager (Security Coordinator) for the cyber track |
| Approved | 2026-08-31 by the Owner and President |
| Last tested | Not yet. First tabletop with the MSP and the integrator due 2026-11-30 (POAM-012). The next emergency drill with the county fire department will include a cyber case (P01 R-014) |

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. Two tracks run at once: the **safety track** (blend room, release reporting) led by the Operations Manager, and the **cyber track** (MSP, insurer, integrator) run by the Office Manager. The Owner decides anything that costs money or goes outside the company.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (safety and blend room) | Operations Manager | Owner and President | Cell phone (printed contact card) |
| Cyber incident coordinator and incident log | Office Manager | Owner and President | Cell phone |
| Decision maker (money, ransom, closing the site, customers, media) | Owner and President | Operations Manager | Cell phone |
| Release reporting | Operations Manager | Owner and President | Printed call list at the blend room exit, the loading dock, and in the Operations Manager's truck (POAM-012) |
| Technical response, office systems | MSP 24x7 emergency line (in the MSP contract) | MSP lead technician's cell | Phone only |
| Technical response, PLC, HMI, gateway | Integrator lead engineer, **on site only** once the remote path is cut | Integrator office line | Phone. No 24-hour response commitment yet (POAM-013) |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Policy card in the incident binder |
| Breach counsel and forensics | Insurer panel counsel; forensic firm engaged by counsel (ask for one with OT experience) | n/a | Assigned on the first hotline call |
| Emergency responders | 911 (county fire rescue) | n/a | Any phone |
| Law enforcement and CISA | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Notification chain in the first hour:** whoever sees it → Operations Manager (safety) and Office Manager (cyber) → 911 if there is any fire, release, or runaway reaction → MSP emergency line and the Owner → insurer breach hotline (Owner or Office Manager) → counsel and forensics through the insurer → integrator, to come on site.

**Out-of-band first.** Assume the office network, email, and office phones are compromised or down. Use personal cell phones, the printed contact card, and the incident binder. Do not discuss the incident by company email.

## 1. Preparation checks (Identify / Protect)
- [ ] Incident binder in the blend room, at the loading dock, and in the office: this runbook, the notification matrix, the release call list with RQs in gallons, the contact card, and blank incident log sheets. **Gap until POAM-012 closes (2026-09-30)**
- [ ] Gateway powered off except for sessions the Operations Manager opens and watches (from 2026-09-01). Named portal accounts with MFA (POAM-001, POAM-002, due 2026-10-31)
- [ ] Owner's paper formulation binder up to date (quarterly). It is the reference for checking recipes after an intrusion
- [ ] Offline copy of the PLC program, HMI project, and recipes, less than 7 days old, with checksums, and a restore test on the spare panel PC within the last 90 days (CP-9, CP-4). **Gap until POAM-004 and POAM-005 close (2026-11-30 and 2026-12-15)**
- [ ] HMI PC on its own firewall segment, so ransomware cannot spread between the office and the blend room (SC-7). **Gap until POAM-006 closes (2026-12-31)**
- [ ] Spare panel PC on the shelf, with HMI software installation media from the integrator
- [ ] Insurer hotline number and policy number checked at each renewal; the integrator and MSP contracts include 24-hour incident notice and a response commitment (POAM-013)
- [ ] Hardwired emergency stop and T-1 high-temperature cutout function-tested at the annual walkthrough

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A dose, setpoint, or alarm limit on the HMI does not match the signed batch ticket | Blend Operator at batch start; Owner's signature on the ticket (POL-02 A.11) | **Do not start the batch.** Call the Operations Manager |
| T-1 temperature rising faster than normal, bubbling or foaming, or the hardwired high-temperature cutout trips with no clear cause | Operator; field thermometer; cutout | Emergency stop. Close the peroxide tote valve. If it keeps heating, evacuate and call 911 (section 3) |
| Mouse moving, screens changing, or a remote session banner on the HMI with no one at it | Operator | Do not touch the HMI. Photograph the screen. Call the Operations Manager |
| Portal alert of a new session that the Operations Manager did not open (once POAM-001 closes); gateway lights showing traffic while it should be off | Operations Manager's phone; control panel | Unplug the gateway's power. Declare an incident |
| Ransom note, locked HMI screen, or office files that will not open | Operator; office staff | Unplug the network cable. **Do not power off.** Call the Office Manager |
| QC finds active content or pH out of specification on a peroxide product | QC Technician | Hold the lot. Compare the batch ticket with the HMI recipe |
| Antivirus alert that is not cleared automatically | MSP console | MSP isolates the device and calls the Office Manager |

**Declare a batch control system incident** when any unexplained change to a recipe, setpoint, alarm limit, or PLC logic is confirmed, when a remote session is seen that the Operations Manager did not open, or when ransomware appears on the HMI PC or any office computer.

**Record the time of discovery** in the incident log. Release reporting clocks run from knowledge of the release, not from the cyber declaration. Florida's 30-day breach clock runs from the determination of a breach of employee personal information (Fla. Stat. 501.171(4)(a)).

## 3. First hour: safe state first (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Safe state.** Press the emergency stop. Turn off the T-1 heater and hot-water skid. Close the hydrogen peroxide and sodium hydroxide tote valves by hand. Hold any partial batch. Read T-1 temperature on the field thermometer, not the HMI | Blend Operator, then the Operations Manager | Pumps and heater off; temperature stable or falling on the field reading |
| 2. **Runaway or release check.** If T-1 keeps heating, foams, or vents vapor, or anything has spilled outside containment: evacuate the building, call 911, and start the release notices in section 6. Hydrogen peroxide decomposition gives off heat and oxygen; do not approach the tank | Operations Manager | Everyone out and counted; 911 called |
| 3. **Cut the remote path.** Unplug the gateway's power in the control panel. The Office Manager asks the integrator to disable the shared portal login | Operations Manager; Office Manager | Gateway dark; portal login disabled |
| 4. **Isolate the HMI PC and the office.** Pull the HMI PC's network cable (leave it powered on). The MSP disconnects the office network from the internet at the firewall and isolates any computer showing ransomware | Operations Manager; MSP | No path between the HMI, the office, and the internet |
| 5. **Call the insurer's breach hotline** before hiring any outside firm. If anyone was hurt or there was a release, also tell the general liability and pollution carriers (POL-03 4.6) | Owner or Office Manager | Claim number; counsel assigned |
| 6. **Call the integrator** to come on site. No remote work on the PLC or HMI | Operations Manager | Arrival time agreed |
| 7. **Start the incident log** on paper: timeline, decisions, who did what, and when | Office Manager | Log open |

**Shipping can continue** from finished goods on the shelf if the office has been checked by the MSP, using handwritten bills of lading from the shipping binder (P05 BP-04). Do not ship any lot made during the suspected intrusion window (section 4).

## 4. Analysis (RS.AN)
Led by the forensic firm through counsel, with the integrator for the PLC and HMI and the MSP for the office.
1. **What changed in the process.** The Owner and the Operations Manager compare all 85 HMI recipes, every setpoint, and every alarm limit with the Owner's paper formulation binder and the last signed batch tickets. List every difference. The HMI audit trail is off today, so the change cannot be tied to an account until POAM-009 closes.
2. **When it started.** Export the portal session log for the last 90 days before anyone changes the portal. Look for sessions outside business hours or from unfamiliar locations. July 2026 already showed 9 after-hours sessions (P07).
3. **Which lots are affected.** Every batch made since the earliest suspicious session or the earliest recipe difference is suspect. The QC Technician retests retained samples. Lots that fail are held, and the Owner decides on recall and customer notice. A product made with the wrong peroxide content may no longer match its SDS or its shipping description.
4. **Scope.** Did the attacker reach the office? The MSP checks the antivirus console, firewall logs, and the productivity suite sign-in log. Did the attacker use the MSP's remote tool? The MSP shows its own logs.
5. **Preserve evidence (chain of custody).**
   - Forensics images the HMI PC's disk and memory before it is rebuilt.
   - Export the portal session log, gateway logs, firewall logs, and suite sign-in logs before they age out.
   - Photograph the HMI screens, the control panel, and the batch tickets.
   - Seal the company USB stick and the newest recipe export. They may hold the attacker's changes.
6. **Data taken.** Check for theft of recipes and formulations (trade secrets) and of employee personal information from the office. Theft of employee personal information drives the Florida rows of the notification matrix.
7. **Backups.** Before any restore, confirm the offline copy predates the first sign of intrusion, and that the backup console was not accessed by the attacker.

## 5. Containment and eradication (RS.MI)
1. The gateway stays unplugged until named portal accounts with MFA, session approval, and session alerts are in place (POL-02 B.8). Until then, the integrator works on site only.
2. The integrator disables the shared portal login and switches off the AI write-back option and the AI feature itself (P10).
3. Change every shared or administrator password from a clean device: HMI, PLC, gateway, portal, firewall, Wi-Fi, door code.
4. Disable the HMI PC's remote desktop service permanently.
5. **Build a clean HMI on the spare panel PC** from vendor media. Do not decrypt or reuse the infected disk. Load the HMI project from the newest verified copy.
6. The integrator compares the running PLC program with its 2023 copy, or with the newer checksummed copy once POAM-004 closes. Every difference is explained or reversed. Reload the PLC program if any difference is unexplained.
7. The MSP wipes and rebuilds any infected office computer, and confirms there is no persistence in the suite, the firewall, or its own remote tool before the office reconnects to the internet.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Release notices never wait for the cyber investigation. Counsel confirms every other notice before it goes out.

| When | Action | Owner |
|---|---|---|
| At once | 911 for any fire, release, or runaway reaction | Whoever sees it, then the Operations Manager |
| Immediately, if a release reaches an RQ (sodium hypochlorite 100 lb, about 80 gal of 12.5% solution; sodium hydroxide 1,000 lb, about 157 gal of 50% solution; phosphoric acid 5,000 lb) | National Response Center (40 CFR 302.6). LEPC and SERC too if people outside the site could be exposed (40 CFR 355.40-355.43) | Operations Manager |
| Within 8 or 24 hours | OSHA, if a worker dies (8 h) or is hospitalized, or suffers an amputation or loss of an eye (24 h) (29 CFR 1904.39). The 10-employee exemption does not cover this | Owner |
| Within 12 hours and 30 days | DOT telephone and written reports, only if the incident involved packaged product in transportation while in the company's possession (49 CFR 171.15, 171.16) | Operations Manager |
| Hour 1 | Insurer notified; counsel and forensics engaged | Owner or Office Manager |
| Within 24 hours (company target) | Voluntary report to CISA and the FBI after telling counsel (POL-03 4.8). It helps with support and is a mitigating factor if a ransom payment is ever considered | Office Manager |
| As soon as practicable | Written follow-up to the LEPC and SERC after any immediate EPCRA notice (355.40(b)) | Operations Manager |
| Day 0 to 1 | Staff briefing: what happened, what not to touch, no talk outside the company, send questions to the Owner | Operations Manager |
| Day 1 to 3 | Customers with open orders: delivery impact. Customers who received suspect lots: hold and return instructions | Owner |
| Within 30 days of determination | Florida notice to affected employees if their personal information was breached (Fla. Stat. 501.171(4)(a)) | Office Manager with counsel |

**Not required:**
- CFATS reporting: authority terminated in July 2023 and not reauthorized as of 2026-10-05; the facility was never tiered.
- CIRCIA: proposed only.
- USCG MTSA reporting: not an MTSA facility.
- FAR 52.204-25: no federal contracts.

**Inbound notices.** The payroll service must tell the company within 10 days of determining a breach of employee personal information (501.171(6)(a)). The MSP and integrator have no incident notice term yet; it is added at renewal (POAM-013).

**Ransom decision:** only the Owner, with counsel and the insurer's advice and after an OFAC sanctions check (POL-03 4.7). Recovery never depends on paying: the HMI is rebuilt on the spare panel PC, not decrypted.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 6). **Safety gates come before speed.**
1. Emergency notification (BP-07): cell phones and the printed call list, already in use
2. Safe state of T-1 and T-2: kept until step 7
3. Internet, office network, and clean computers for shipping (SYS-04, SYS-05), after the MSP confirms the office is clean
4. Hazmat shipping (BP-04) through the accounting service, with SYS-07 sign-ins checked. Handwritten bills of lading until then
5. Order entry and invoicing (BP-03)
6. Clean HMI on the spare panel PC, verified PLC program, and recipes reconciled line by line with the paper binder (SYS-01, SYS-02)
7. **Blending restart (BP-01).** The Owner and the Operations Manager approve it after a pre-start check that confirms:
   - every recipe, setpoint, and alarm limit matches the paper binder and is signed off by the Owner
   - the hardwired high-temperature cutout and emergency stop are function-tested
   - all passwords are changed and the gateway stays unplugged
   - non-peroxide recipes run first; peroxide recipes resume only after one clean day
8. Packaging and labels (BP-02) and QC (BP-05), then formulation and SDS files (BP-06), purchasing (BP-08), and payroll and bookkeeping (BP-09)
9. **The integrator portal and the AI feature come last.** The gateway is reconnected only after POAM-001 is complete. The AI feature stays off until the P10 conditions are met again

**Realistic timing today:** with no tested offline backup, rebuilding the HMI and checking 85 recipes by hand could take 1 to 2 weeks (P05 key finding). Simple non-peroxide products can be made with the portable mixer meanwhile. After POAM-004 and POAM-005 close, the target is the 24-hour RTO for BP-01.

**Recovery communications:** tell staff, customers with held orders, the insurer, and the LEPC (if it was notified of a release) when each function is back.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of the blending restart, with the MSP, the integrator, and counsel. Written summary within 30 days (POL-03 4.12).
- Update the risk register (P01, especially R-001, R-002, R-005, R-006, R-007, and R-010), the POA&M (P07), the SSP (P02), the emergency action plan, and this runbook.
- Re-check the SSP categorization (P02 section 6) if the incident showed a worse credible outcome than serious injury in the blend room.
- Keep the incident log, evidence records, notices, and the forensic report for at least 5 years (POL-02 A.7). Keep any DOT incident report 2 years (171.16(b)(3)).
