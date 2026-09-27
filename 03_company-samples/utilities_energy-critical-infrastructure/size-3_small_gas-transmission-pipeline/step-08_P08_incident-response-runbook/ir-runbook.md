# Incident Response Runbook: Ransomware on Business IT Forcing a Precautionary Pipeline Shutdown

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (intrastate natural gas transmission pipeline operator) |
| Tier / Vertical | Small / Energy |
| Incident type | Ransomware on business IT (email, file shares, nominations and measurement access, ERP) that leads leadership to consider or order a precautionary pipeline shutdown because OT integrity cannot be confirmed |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT response guidance from NIST SP 800-82 Rev. 3 (sections 3.3.8, 3.3.9, 6.4, 6.5) |
| Policy basis | POL-03 Incident Response Policy; emergency plan (49 CFR 192.615); manual operation plan (192.631(c)(3)) |
| Runbook owner | IT Manager, with the Gas Control Manager for all OT and operations steps |
| Approved | 2026-09-24 by the President |
| Last tested | Not yet. First tabletop, with controllers, due 2027-03-31 (POAM-005) |

**The lesson this runbook is built on.** Ransomware on business IT does not by itself make the pipeline unsafe. The BIA (P05) shows gas control can run with no business IT at all. A shutdown is justified only when the company **cannot trust or cannot see its OT**, or cannot staff safe manual operation. This runbook makes that decision explicit, fast, and owned, so a shutdown is neither ordered out of uncertainty nor delayed when it is needed.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (cyber) | IT Manager | President | Incident line (cell), then the out-of-band group on personal phones |
| Operations lead | Gas Control Manager | VP Operations | Gas Control Center direct line; radio |
| Controller on duty | Gas controller on shift | Gas Control Manager (qualified relief) | Console phone; radio |
| OT technical lead | SCADA Engineer | SCADA integrator (only after its access path is confirmed clean) | Cell |
| Shutdown decision | President | Majority owner | Cell |
| Regulatory notices | Pipeline Safety and Compliance Manager | VP Operations | Cell |
| Customer and upstream pipeline notices | Commercial Manager | VP Operations | Cell; customer contact list in the incident binder |
| Business IT response | MSP incident team | IR retainer firm with OT experience (engaged through the insurer's panel) | MSP 24x7 line |
| Legal and insurance | Outside counsel (insurer panel); cyber insurer | Finance Manager | Insurer breach hotline |
| Law enforcement and CISA | FBI field office; CISA Central (844-729-2472) | | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and the business phone system are compromised. Use personal phones, radio, and the printed contact list in the incident binder at the Gas Control Center, Compressor Station 1, and both field offices.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at 4 sites: this runbook, the decision tree, contacts, the notification matrix, and the manual operation plan
- [ ] IT/OT isolation procedure posted at the Gas Control Center, with the Gas Control Manager's authority to close the DMZ (POL-03 4.5). **Gap until POAM-006 closes**
- [ ] Offline SCADA backup less than 30 days old, stored at Compressor Station 1 (CP-9). **Gap until POAM-003 closes**
- [ ] OT monitoring sensor live, so the company can show OT traffic is normal (SI-4). **Gap until POAM-007 closes. Until then, the OT integrity check in section 4 relies on manual checks and takes longer**
- [ ] Integrator remote access disabled by default (AC-17). **Gap until POAM-002 closes**
- [ ] Manual operation plan tested this calendar year (192.631(c)(3))
- [ ] Pre-drafted customer, upstream pipeline, and employee notices in the binder
- [ ] IR retainer and insurer panel confirmed

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or files renamed with an unknown extension, on a business endpoint or server | Staff report; EDR alert | Call the incident line. **Do not power off.** Unplug the network cable or turn off Wi-Fi |
| MSP reports mass encryption or EDR tamper alerts | MSP | IT Manager opens the incident and calls the Gas Control Manager |
| Nominations portal, measurement application, or email unreachable with no provider outage | Staff; status pages | Treat as possible ransomware until ruled out |
| Anything unusual on an HMI or SCADA host: unexpected pop-ups, slow displays, values that disagree with field readings, commands the controller did not issue | Controller | **Controller follows the CRM and emergency procedures first**, then calls the Gas Control Manager and SCADA Engineer. Severity 1 |
| Extortion email or leak-site post naming the company | Email; law enforcement | Declare the incident; preserve the message |

**Declare a ransomware incident when** encryption or a ransom note is confirmed on any system. **Severity 1** if any OT component is affected or suspected; otherwise **Severity 2** (POL-03 4.3).
**Record the time of discovery** for every clock in the notification matrix.

## 3. First hour (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| T+0 to 15 min | 1. Tell the controller on duty and the Gas Control Manager. **Close the IT/OT DMZ connections** (historian push and jump host) at the OT firewall. Do not wait for proof that OT is affected | IT Manager; Gas Control Manager (authority) | OT firewall shows no sessions to the DMZ |
| T+0 to 15 min | 2. Disable integrator remote access and the MSP's cloud administrator access to the backup account | SCADA Engineer; IT Manager | Accounts disabled |
| T+0 to 30 min | 3. Controller confirms SCADA is responsive and values match expectations (line pack, pressures at key points). Controller keeps operating | Controller on duty | Status reported to the Gas Control Manager |
| T+0 to 30 min | 4. Isolate affected business endpoints (EDR network isolation); leave them powered on for memory capture | MSP | Endpoints isolated |
| T+15 to 45 min | 5. Call the cyber insurer's hotline; engage counsel and the IR retainer | President or Finance Manager | Claim number issued |
| T+30 to 60 min | 6. Put field technicians on standby to staff the compressor station, receipt interconnect, and the 4 largest M&R stations for manual operation | Field Operations Manager | Crews dispatched or on standby |
| T+60 min | 7. **Decision point 1** (section 4) | Gas Control Manager recommends; President decides | Decision recorded in the incident log |
| Ongoing | 8. Start the incident log: timeline, actions, who, and when | IT Manager | Log open (paper if needed) |

## 4. The operate-or-shut-down decision (RS.AN, RS.MI)
The Gas Control Manager recommends and the President decides, except where 192.615(a)(6) requires a controller or field supervisor to act at once for safety (POL-03 4.4 and 4.6).

**Decision point 1 (T+60 min): Is OT trustworthy right now?**

| Question | How to check | If yes | If no or unknown |
|---|---|---|---|
| Is the DMZ closed and holding? | OT firewall session table | Continue | Close again; escalate to Severity 1 |
| Do SCADA values agree with the field? | Field technicians read local gauges at 3 or more sites and compare by radio | Continue | Move to **manual operation**; see below |
| Are HMIs and SCADA hosts behaving normally? | SCADA Engineer checks running processes, recent logins, and changes against the build sheet (no active scanning) | Continue | Fail over to the backup control room if it is not affected; otherwise manual operation |
| Is any business IT system needed to operate safely in the next 24 hours? | BIA (P05): no. Nominations and email have manual workarounds | Continue | Not expected |

**Outcomes:**
- **A. Isolate and operate (the default).** All four answers are yes. Keep the DMZ closed. Run nominations by phone and spreadsheet (P05 BP-04) and billing on estimates (BP-07). Recheck every 4 hours.
- **B. Manual operation.** SCADA values cannot be trusted but the pipeline can be run safely by field crews. Follow the manual operation plan. Consider reducing pressure to widen safety margins. The 8-hour MTD for BP-01 (P05) sets the next decision point.
- **C. Controlled precautionary shutdown or curtailment.** Choose this when manual operation cannot be staffed safely beyond the MTD, when there is evidence that someone other than the controller is sending commands to field devices, or when the Gas Control Manager judges that neither SCADA nor manual operation can keep the pipeline within its operating limits. Follow the O&M manual shutdown procedures (192.605(b)(5)) and the emergency plan. Before closing any delivery, coordinate with each LDC and the power plant, because a supply loss to homes creates its own safety risk.

**Decision point 2 (T+4 h, then every 4 h):** reassess with the IR retainer's findings. A shutdown ordered under outcome C is lifted only under section 7.

**What does not justify a shutdown on its own:** the loss of billing, measurement publishing, email, or the ERP. These are business processes with MTDs of 24 to 120 hours (P05).

## 5. Analysis, containment, and eradication (RS.AN, RS.MI)
1. **Scope (IR retainer and MSP):** find the affected endpoints, servers, cloud workloads, and accounts from EDR, identity provider sign-in logs, cloud audit logs, and firewall logs.
2. **Initial access:** identify the phishing email, stolen credential, or exposed service, and the first host compromised.
3. **Preserve evidence:** capture memory on affected hosts before powering off, and label the affected equipment. Export logs before they roll over (firewall logs keep only 30 days; POAM-017). Maintain chain of custody.
4. **Check the paths into OT (SCADA Engineer with the IR retainer):**
   - the jump host (image it before any cleanup);
   - the historian replica;
   - integrator and SCADA Engineer credentials;
   - the patch staging server.

   Assume the shared administrator password is compromised and change it from a clean OT workstation.
5. **Exfiltration:** determine whether employee personal information (HR and payroll files) or Restricted OT information (network drawings, SCADA configurations) was taken. This drives the Florida breach decision and the threat assessment.
6. **Contain and eradicate:**
   - block attacker infrastructure at the business firewall and in the cloud network rules;
   - disable compromised accounts and rotate service credentials, including the cloud-to-DMZ push credentials;
   - rebuild affected business endpoints and cloud VMs from clean images. **Do not decrypt and reuse them.**
7. **Confirm with the IR retainer** that persistence is removed before reconnecting anything to the DMZ.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms any breach notice. The Pipeline Safety and Compliance Manager owns pipeline notices.

| When | Action | Owner |
|---|---|---|
| Within 1 hour of confirmed discovery of an incident under 49 CFR 191.3 | **NRC telephonic notice (191.5).** If the pipeline is shut down or curtailed because of the cyber event, decide within the first hour of the shutdown whether it is "significant in the judgment of the operator" (191.3 paragraph (3)). Default: report | Pipeline Safety and Compliance Manager |
| At the earliest practicable moment, only if gas was released | FPSC telephonic notice (Rule 25-12.084); otherwise a courtesy call to FPSC gas safety staff | Pipeline Safety and Compliance Manager |
| Before any curtailment, then every 4 hours | Customers (2 LDCs, power plant, 6 industrial plants) and the upstream interstate pipeline | Commercial Manager |
| If an emergency exists | 9-1-1 centers and county emergency managers (192.615(a)(8)) | VP Operations |
| Day 0 | Insurer notified; counsel engaged | President |
| Within 72 hours (voluntary) | CISA report (cisa.gov/report). FBI contact. Supports OFAC mitigation if payment is considered | IT Manager |
| Within 48 hours of confirmed discovery | Revise or confirm the NRC notice (191.5(c)) | Pipeline Safety and Compliance Manager |
| Within 30 days of determination | Florida notice to affected employees if personal information was accessed (Fla. Stat. 501.171) | HR Manager and counsel |
| Within 30 days of detection | PHMSA Form F 7100.2 if a 191.5 notice was made (191.15) | Pipeline Safety and Compliance Manager |
| Day 0 to 2 | Staff briefing script: what happened, what to use, do not discuss outside the company | President |

**Ransom decision:** requires the majority owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not restore trust in OT; the section 7 checks still apply.

**Not required, and why:** TSA reporting (not designated), NERC CIP-008 (not registered), DOE OE-417 (not electric), and CIRCIA (not in effect). See the matrix.

## 7. Recovery and restart (RC.RP, RC.CO)
**Restore business IT in BIA priority order (P05):**
1. Emergency communications
2. SCADA (if affected) and telecommunications
3. Compressor station control
4. Nominations and email
5. Measurement application
6. Field records
7. Leak analytics
8. ERP and billing
9. Payroll

**Before reopening the DMZ:**
- The IR retainer confirms business IT is clean.
- The jump host is rebuilt, and integrator access is re-enabled only through named accounts with MFA.
- The historian replica is rebuilt from a clean image.
- The Gas Control Manager signs off.

**If SCADA hosts must be rebuilt:**
1. Restore from the offline backup, scanning it and comparing its hash before use (POL-04 4.5).
2. Verify configuration against the build sheet.
3. Perform point-to-point checks on any display or point that changed (192.631(c)(2)).
4. Run a failover test before relying on the backup host.

**Restarting after a shutdown:**
1. Follow the O&M manual start-up procedures (192.605(b)(5)) and coordinate with the upstream pipeline and each customer.
2. Controllers confirm SCADA values against field readings at every delivery point before returning to remote control.
3. The President approves the restart on the Gas Control Manager's recommendation.

**Leak analytics** is restored last, and only after revalidation (P10), because its input data passed through the affected DMZ.

Tell staff, customers, and the upstream pipeline as each service returns (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days).
- Review control room actions under 192.631(g) and add lessons to controller training.
- Update the risk register (P01 R-001, R-002, R-004, R-012), the POA&M (P07), this runbook, and the emergency plan annex.
- Retain incident records for at least 3 years (POL-01 4.11), and longer where PHMSA or FPSC records rules require.
