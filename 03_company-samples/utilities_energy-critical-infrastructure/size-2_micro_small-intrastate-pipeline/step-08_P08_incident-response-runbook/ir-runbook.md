# Incident Response Runbook: Ransomware on Office IT Forcing a Precautionary Pipeline Shut-in

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (small intrastate natural gas transmission pipeline operator) |
| Tier / Vertical | Micro / Energy |
| Incident type | Ransomware on the office network that reaches the gas control desk workstations, so controllers lose their main SCADA screens and cannot be sure SCADA is trustworthy, and the Owner must decide whether to keep operating, run the line manually, or shut it in |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT response guidance from NIST SP 800-82 Rev. 3 (sections 3.3.8, 3.3.9, 6.4, 6.5) |
| Policy basis | POL-03 Incident Response Policy; emergency plan (49 CFR 192.615); abnormal operation procedures (192.605(c)) |
| Runbook owner | Office Manager (cyber incident lead), with the Operations Manager for every operations step |
| Approved | 2026-09-15 by the Owner |
| Last tested | Not yet. First tabletop with the MSP, the SCADA vendor, and the municipal gas system due 2026-11-30 (POAM-009) |

**The lesson this runbook is built on.** Ransomware in the office does not, by itself, make the pipeline unsafe. Gas keeps flowing, and the mechanical regulators at each delivery station keep holding pressure without SCADA (P05). What the company loses is its **view**: the gas control desk sits on the office network, so when the office goes down, the controllers' main screens go with it. The fastest safe answer is usually to get a trusted view back, not to shut the line in. A shut-in cuts gas to a municipal system serving about 9,000 homes and businesses, and relighting them creates its own safety risk. This runbook makes the choice explicit, fast, and owned.

## 0. Roles and notification chain (Govern)
Seven people run the company. The MSP handles office IT, the SCADA vendor handles the SCADA platform, and the cyber insurer supplies breach counsel and forensics.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Cyber incident lead | Office Manager | Operations Manager | Cell phone (numbers on the printed contact card) |
| Operations lead | Operations Manager | On-call controller | Cell phone; on-call phone |
| Controller on duty | Operations Manager (business hours) or on-call controller | The other 2 controllers | On-call phone |
| Decision maker (shut-in, money, ransom, statements) | Owner | Operations Manager | Cell phone |
| Office IT response | MSP incident line (24x7 emergency number in the MSP contract) | MSP lead technician's cell | Phone only |
| SCADA platform response | SCADA vendor 24x7 support line | Vendor account manager | Phone; number on the contact card |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel firms | n/a | Assigned by the insurer on the first call |
| Municipal gas system | Its gas operations on-call | Its utility director | Numbers in the binder |
| Upstream interstate pipeline | Its gas control desk (24x7) | Its scheduling desk | Numbers in the binder |
| Law enforcement and CISA | FBI field office; CISA Central (844-729-2472) | IC3 | Numbers in the binder |

**Notification chain in the first hour:** staff member → Operations Manager or on-call controller (anything touching SCADA) and Office Manager → MSP incident line and Owner (at the same time) → SCADA vendor support line → insurer hotline (Owner) → counsel and forensics (through the insurer). The municipal gas system's gas operations on-call is told as soon as manual operation or a shut-in is being considered.

**Out-of-band first.** Assume email and the office network are compromised. Coordinate by personal cell phone and text, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at the office, in each field truck, and at the Owner's and Operations Manager's homes: this runbook, the decision table, contacts, the notification matrix, and the manual operation call list
- [ ] Clean spare SCADA laptop, kept off the network in the office safe with a charged phone hotspot. **Gap until set up by 2026-10-31 (P01 R-001)**
- [ ] Gas control desk on its own network segment with no email (CM-7, SC-7). **Gap until POAM-004 closes**
- [ ] MFA on every SCADA account and a sealed break-glass credential (IA-2(1)). **Gap until POAM-002 closes**
- [ ] SCADA configuration export and RTU program copies less than 90 days old in the office safe (CP-9). **Gap until POAM-007 closes**
- [ ] MSP-managed EDR with alert monitoring (SI-4). **Gap until POAM-004 closes (2026-12-31)**
- [ ] Manual operation call list: who goes to the receipt station and the municipal gate station, with keys and gauges in each truck
- [ ] Insurer hotline number and policy number checked each renewal

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Files will not open, names changed, or a ransom note appears on any office computer | Staff | **Unplug the network cable or turn off Wi-Fi. Do not turn the computer off.** Call the Office Manager |
| Anything odd on the gas control desk: pop-ups, frozen or slow displays, values that disagree with the field, a valve that moved without a command | Controller | **Controller follows the emergency plan and abnormal operation procedures first.** Then calls the Operations Manager. Severity 1 |
| SCADA sign-in or command the controller does not recognize | SCADA audit log or sign-in alert | Disable the account (POL-03 4.4); call the SCADA vendor; Severity 1 |
| MSP reports mass encryption or antivirus tampering | MSP | Office Manager opens the incident and calls the Operations Manager |
| Email or call claiming to hold company data or to control the pipeline | Extortion message | Do not reply. Save it. Declare an incident; treat a claim about the pipeline as Severity 1 |

**Declare a ransomware incident** when encryption or a ransom note is confirmed on any device. **Severity 1** if the gas control desk, a controller laptop, the SCADA tenant, or a field device is affected or suspected; otherwise **Severity 2**.

**Write down the discovery time.** It starts every clock in the notification matrix, including the one-hour NRC clock if the event becomes a reportable incident.

## 3. First hour (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| T+0 to 10 min | 1. **Disconnect the gas control desk from the office network** (unplug both workstations). Do not wait for proof that SCADA is affected | Controller on duty (authority under POL-03 4.4) | Desk offline |
| T+0 to 15 min | 2. Restore a trusted SCADA view: the controller signs in from the clean spare laptop on its hotspot (until it exists, from a controller laptop that was off the office network) | Controller on duty | SCADA visible on a clean device |
| T+0 to 30 min | 3. Controller checks SCADA values against expectations (receipt pressure, delivery pressures, flows) and calls the upstream interstate pipeline's gas control to compare receipt readings | Controller on duty | Status reported to the Operations Manager |
| T+0 to 30 min | 4. Call the MSP incident line: isolate affected office computers, leave them on for evidence, suspend the suite backup job so it cannot copy encrypted files over good versions | Office Manager; MSP | MSP confirms isolation |
| T+15 to 30 min | 5. Call the SCADA vendor: ask for the tenant sign-in and command log for the last 72 hours; reset passwords for every SCADA account from the clean device; disable the shared desk login if it still exists | Operations Manager | Vendor case open; passwords reset |
| T+15 to 45 min | 6. Call the insurer's hotline; counsel and forensics assigned | Owner | Claim number issued |
| T+30 to 60 min | 7. Put field staff on standby with the manual operation call list: one pair to the receipt station, one to the municipal gate station | Operations Manager | Crews on standby or dispatched |
| T+60 min | 8. **Decision point 1** (section 4) | Operations Manager recommends; Owner decides | Decision recorded in the incident log |
| Ongoing | 9. Incident log: timeline, actions, who, when (paper if needed) | Office Manager | Log open |

## 4. The operate-or-shut-in decision (RS.AN, RS.MI)
The Operations Manager recommends and the Owner decides (POL-03 4.5). Nothing here delays an immediate safety action under 192.615(a)(6), which any controller takes when needed.

**Decision point 1 (T+60 min): can we see and trust the pipeline right now?**

| Question | How to check | If yes | If no or unknown |
|---|---|---|---|
| Is the gas control desk off the office network and SCADA visible on a clean device? | Steps 1 and 2 | Continue | Move to **manual operation** (outcome B) |
| Do SCADA values agree with the field? | Upstream receipt reading by phone; field readings at the receipt station and the municipal gate station when crews arrive | Continue | Manual operation (B) |
| Has anyone other than our controllers signed in to SCADA or sent a command? | SCADA vendor's log for the last 72 hours | Continue | Disable accounts; manual operation (B); consider shut-in (C) |
| Does any office system matter for safe operation in the next 24 hours? | BIA (P05): no. Nominations and email have phone workarounds | Continue | Not expected |

**Outcomes:**
- **A. Isolate and operate (the default).** All answers are yes. Keep the desk off the network. Run SCADA from the clean device. Confirm nominations by phone with the interstate pipeline's scheduling desk (P05 BP-03). Recheck every 4 hours.
- **B. Manual operation.** SCADA cannot be trusted but field staff can run the line safely. Crews at the receipt station and the municipal gate station read local gauges and report by phone every 30 minutes; RCVs are operated by hand at the site (192.605(c)). The 8-hour MTD for gas control (P05) sets the next decision point, because 4 field-qualified people can cover about one shift.
- **C. Controlled precautionary shut-in or curtailment.** Choose this only when: there is evidence that someone other than our controllers is commanding field devices; or manual operation cannot be staffed past the MTD and SCADA is still untrusted; or the Operations Manager judges the line cannot be kept within its operating limits. Before closing the receipt flow control valve or any RCV, call the municipal gas system so it can protect its customers and plan relights, and call the upstream interstate pipeline. Follow the O&M shutdown procedure (192.605(b)(5)) and the emergency plan.

**Decision point 2 (T+4 h, then every 4 h):** reassess with forensics, the MSP, and the SCADA vendor. A shut-in under outcome C is lifted only under section 7.

**What does not justify a shut-in on its own:** loss of email, the shared drive, accounting, or billing. These have MTDs of 24 to 120 hours (P05).

## 5. Analysis, containment, and eradication (RS.AN, RS.MI)
1. **Scope (forensics and the MSP):** find the affected computers and accounts from antivirus or EDR logs, suite sign-in and file logs, and firewall logs.
2. **Initial access:** identify the phishing email, stolen password, or other entry point and the first computer affected. Search all mailboxes for the same message and remove it.
3. **Preserve evidence:** forensics images affected computers before they are wiped and exports suite and firewall logs before they age out (firewall logs keep only 30 days). Keep a chain-of-custody record.
4. **Check every path to SCADA (Operations Manager with forensics and the SCADA vendor):**
   - the gas control desk workstations (image before rebuilding);
   - each controller laptop (MSP checks, then a password reset from a clean device);
   - the SCADA tenant sign-in and command log and the configuration history (compare with the last export in the safe);
   - the MSP's RMM tool (did the attacker use it?);
   - the gateways (any change in routing or passwords).
5. **Data theft:** did HR or payroll files leave the company? This drives the Florida breach decision. Did network details or SCADA configurations leave? This raises the threat level for the pipeline.
6. **Contain and eradicate:** block attacker senders and addresses in the suite and at the firewall; disable compromised accounts; wipe and rebuild affected computers from the MSP's standard image. **Do not decrypt and reuse them.** If the MSP's tools may be the entry point, the forensics firm leads eradication and the MSP shows its own investigation results (P01 R-004).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel reviews every breach notice. The Operations Manager owns pipeline notices.

| When | Action | Owner |
|---|---|---|
| Before any curtailment, then every 4 hours | Municipal gas system, the two industrial plants, and the upstream interstate pipeline | Operations Manager; Gas Scheduler for updates |
| No later than 1 hour after confirmed discovery of an incident under 49 CFR 191.3 | **NRC telephonic notice (191.5).** If the line is shut in or curtailed because of the cyber event, decide within the first hour of the shut-in whether it is "significant in the judgment of the operator" (191.3, paragraph (3) of the incident definition). Default: report | Operations Manager |
| At the earliest practicable moment, only if gas was released | FPSC telephonic notice (Rule 25-12.084); otherwise a courtesy call to FPSC gas safety staff | Operations Manager |
| If an emergency exists | 9-1-1 center, the city fire department, and the county emergency manager (192.615(a)(8)) | Operations Manager |
| Day 0 | Insurer notified; counsel engaged | Owner |
| Within 72 hours (voluntary) | CISA report (cisa.gov/report) and FBI contact; full and timely reporting is an OFAC mitigating factor if a payment is ever considered | Office Manager with counsel |
| Within 48 hours of confirmed discovery | Revise or confirm the NRC notice (191.5(c)) | Operations Manager |
| Within 30 days of determination | Florida notice to affected employees and former employees if their personal information was accessed (Fla. Stat. 501.171) | Office Manager with counsel |
| Within 30 days of detection | PHMSA Form F 7100.2 if a 191.5 notice was made (191.15) | Operations Manager |
| Day 0 to 1 | Staff briefing: what happened, which devices to use, do not discuss outside the company, send questions to the Owner | Owner |

**Ransom decision:** only the Owner, with counsel and the insurer and after an OFAC sanctions check (POL-03 4.9). Paying does not make SCADA trustworthy again; the section 7 checks still apply.

**Not required, and why:** TSA reporting (not designated), NERC CIP-008 (not registered), DOE-417 (not electric), and CIRCIA (not in effect). See the matrix.

## 7. Recovery and restart (RC.RP, RC.CO)
**Restore in BIA priority order (P05):**
1. Emergency communications
2. Trusted SCADA view and control from a clean device; telemetry checked
3. Nominations and email
4. Measurement data
5. Records and maps
6. Billing
7. Payroll
8. Leak-detection alerts, only after revalidation (P10)

**Before reconnecting the gas control desk:**
- Both workstations rebuilt as dedicated SCADA desks with no email, on their own segment if that work is done (POAM-004), and forensics confirms the office is clean.
- Every SCADA password reset from a clean device, MFA on (if not yet in place, enable it now), and the shared login removed.
- SCADA configuration compared with the last export in the safe; any difference explained by the vendor or the Operations Manager.
- The Operations Manager signs off.

**Restarting after a shut-in:**
1. Follow the O&M start-up procedure (192.605(b)(5)) and coordinate with the upstream pipeline and the municipal gas system, which manages its own customer relights.
2. Controllers confirm SCADA values against field readings at the receipt station and each delivery station before returning to remote control.
3. The Owner approves the restart on the Operations Manager's recommendation.

Tell staff, customers, and the upstream pipeline as each service returns (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery with the MSP, the SCADA vendor, and counsel; written summary within 30 days (POL-03 4.12).
- Update the risk register (P01 R-001, R-002, R-004, R-005), the POA&M (P07), this runbook, and the cyber annex to the emergency plan.
- Keep the incident log, decisions, notices, and the forensic report for at least 3 years (POL-02 A.7), and longer where PHMSA or FPSC rules require.
