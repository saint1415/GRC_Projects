# Incident Response Runbook 1: Ransomware on Business IT Forcing a Precautionary Pipeline Shutdown Decision

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed interstate natural gas transmission pipeline operator) |
| Tier / Vertical | Mid-Market / Energy |
| Incident type | Ransomware on business IT (email, file shares, ERP and gas accounting, measurement access, identity provider at risk) that leads leadership to consider a precautionary shutdown or curtailment of the pipeline because OT integrity cannot be confirmed quickly |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy (4.1 to 4.12); STD-02 and STD-07; TSA Cybersecurity Incident Response Plan (SD Pipeline-2021-02G Section III.F; C-ENERGY-R03); emergency plan (49 CFR 192.615); manual operation plan (192.631(c)(3); C-ENERGY-R04) |
| Companion documents | `ir-runbook-ot-vendor-compromise.md` (runbook 2); `notification-matrix.csv`; BIA (P05); risk register (P01 R-001, R-004, R-010, R-037, R-041, R-050) |
| Runbook owner | Security Manager (incident commander and Cybersecurity Coordinator), with the Director of Gas Control for every OT and operations step |
| Approved | 2026-09-17 by the Chief Operating Officer. To be adopted into the TSA Cybersecurity Incident Response Plan by 2026-12-31 (POAM-008) |
| Last tested | Annual TSA exercise on 2025-11-18 (containment and backup integrity objectives), before this decision tree existed. The 2026 exercise on 2026-11-17 uses this runbook, with the CEO and the board chair in the executive session (POAM-008) |

**What this runbook is built on.** The BIA (P05 finding 1) shows that gas control, compressor operation, and emergency communication run without any business IT system. Ransomware on business IT does not by itself make the pipeline unsafe. A precautionary shutdown costs about $252,000 a day in firm reservation revenue at risk, cuts supply to 9 LDCs serving about 1.3 million homes and businesses and to 7 power plants, and in winter is a public safety event in its own right. A shutdown is justified only when the company **cannot trust or cannot see its OT**, or **cannot staff safe manual operation**. This runbook makes that decision explicit, timed, and owned (P01 R-001 and R-010).

## 0. Governance, roles, and contacts (Govern)
| Team | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, VP Operations, VP Commercial, Director of Gas Control, Director of Pipeline Safety and Compliance, Director of Regulatory Affairs, Director of Corporate Communications, HR Director, vCISO | Operate-or-shut-down (COO), shipper and public communication, ransom recommendation to the CEO, spending, contract notices |
| **Incident response team (IRT)** | Incident commander: Security Manager. OT Security Engineers, security analysts, IT Director (business IT recovery lead), SCADA and OT Engineering Manager (OT technical lead), MSSP, incident response retainer (through counsel) | Containment, investigation, eradication, recovery sequence |
| **Operations command** | Director of Gas Control (operations lead), shift supervisor on duty, controllers, VP Operations, Area Managers, Compressor Station Supervisors | Safety actions, IT/OT isolation, manual operation, field staffing |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander and Cybersecurity Coordinator (SD 01G II.B) | Security Manager | OT Security Engineer (alternate Coordinator); IT Director (second alternate) | Published 24x7 rota (POAM-020); out-of-band group on personal phones |
| Operations lead; isolation authority (POL-03 4.5) | Director of Gas Control | Shift supervisor on duty | GCC direct line; radio |
| Shutdown decision (POL-03 4.6) | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Pipeline safety notices (Part 191) | Director of Pipeline Safety and Compliance | VP Operations | Out-of-band group |
| Shipper, interconnect, and lateral owner notices | VP Commercial (shippers, lateral owners); shift supervisor (first 30-minute lateral notice) | Director of Gas Control | Contact lists in the incident binder |
| FERC postings | Director of Regulatory Affairs | VP Commercial | Out-of-band group |
| Legal and privilege | General Counsel; breach counsel from the insurer panel | Outside regulatory counsel | Out-of-band group |
| Cyber insurer | Carrier hotline ($20 million limit, $500,000 retention). **Call before engaging any incident vendor** | CFO | Policy card in the binder |
| Forensics and recovery support | Incident response retainer with OT experience, engaged by counsel | MSSP incident team | Through counsel |
| Monitoring and business IT containment | MSSP 24x7 operations center. May isolate business endpoints, **never OT devices** | n/a | MSSP hotline |
| Communications | Director of Corporate Communications | Outside crisis firm (through counsel) | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor | COO | Phone |
| Law enforcement and CISA | FBI field office; CISA Central (cisa.gov/report or 844-729-2472) | n/a | Numbers in the binder |

**Out-of-band first.** Assume email, chat, and the business phone system are compromised, and that the identity provider may be. Use personal phones, radio, satellite phones, and the printed call tree in the incident binder at the GCC, the BCC, each compressor station, and each area office.

**Legal privilege protocol.** The General Counsel engages the retainer through breach counsel. Analysis is labeled "Privileged and confidential, prepared at the direction of counsel". Facts (timeline, logs, actions) stay separate from conclusions. Reports to CISA and TSA are SSI under the directive and are stored in the SSI repository (STD-10).

## 1. Preparation checks (Identify / Protect)
- [x] IT/OT segmentation with firewall pairs and a DMZ at the GCC and BCC; separate OT domain with no trust to the business domain (SC-7; P07 inbound test blocked)
- [x] Immutable cloud backups for business workloads (35-day write-once) and monthly offline SCADA backups at the BCC (CP-9)
- [x] BCC failover tested 2025-11-04 (192.631(c)(4))
- [x] Manual operation communication plan tested 2025-10-21 (192.631(c)(3))
- [ ] Isolation procedure performed live, with time to isolate measured (SD 02G III.D.4). **Gap until POAM-010 closes (live drill by 2026-12-31)**
- [ ] OT monitoring at all 5 compressor stations, so the company can show OT traffic is normal. **Gap at Compressor Stations 2, 4, and 5 until POAM-014 closes. Until then, the OT integrity check in section 4 takes longer at those stations**
- [ ] PLC logic backups with hashes at every station, and a tested full SCADA rebuild. **Gap until POAM-009 closes**
- [ ] OT memory capture kit, vendor approved. **Gap until POAM-010 closes**
- [x] Incident binder at every staffed site: this runbook, runbook 2, the decision tree, the call tree, the notification matrix, the manual operation plan, and pre-drafted shipper and lateral owner notices
- [ ] Out-of-band messaging group and Coordinator rota tested quarterly (first test 2026-10-15; POAM-020)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or files renamed with an unknown extension, on a business endpoint or server | Staff report; EDR alert | Call the security incident line. **Do not power off.** Disconnect the network cable or turn off Wi-Fi |
| Mass encryption, EDR tamper, or backup deletion alerts | MSSP | MSSP isolates affected business endpoints and calls the Security Manager |
| Identity provider administrator activity that no one requested | SIEM; identity provider alerts | Treat as Severity 1: the identity provider controls remote access to OT (CCS-8) |
| Email, file shares, ERP, or measurement access unavailable with no provider outage | Staff; IT | Treat as possible ransomware until ruled out |
| Anything unusual on an HMI, SCADA server, or station control: unexpected pop-ups, slow displays, values that disagree with field readings, commands no one issued | Controller; station technician | **Controller follows the control room management and emergency procedures first.** Then the shift supervisor calls the Director of Gas Control and the Security Manager. Severity 1. Switch to runbook 2 if OT itself appears compromised |
| Extortion email or leak-site post naming the company | Email; law enforcement; MSSP threat intelligence | Declare an incident; preserve the message |

**Declare a ransomware incident** when encryption or a ransom note is confirmed on any company system. **Severity 1** if any OT component is affected or suspected, or the identity provider is compromised; otherwise **Severity 2** (POL-03 4.3).

**Record the time of identification in the incident log.** It starts the 72-hour CISA clock under SD 01G Section II.C.3. Other clocks start at different points (see `notification-matrix.csv`, column `clock_starts`).

## 3. First hour (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| T+0 to 15 min | 1. Tell the shift supervisor. **Close the IT/OT DMZ connections** at the GCC and BCC OT firewalls (historian replica push, patch staging, remote access gateway). Do not wait for proof that OT is affected (POL-03 4.5) | Director of Gas Control or shift supervisor (authority); OT Security Engineer (execution) | Firewall session tables show no IT-to-OT sessions; time recorded |
| T+0 to 15 min | 2. Disable all vendor accounts on the remote access gateway, and confirm the OEM modem at Compressor Station 4 is still disconnected (POAM-003) | OT Security Engineer | Accounts disabled; station confirms |
| T+0 to 30 min | 3. Controllers confirm SCADA is responsive and values match expectations (line pack, key pressures, compressor status). Controllers keep operating | Controllers; shift supervisor | Status to the Director of Gas Control |
| T+0 to 30 min | 4. MSSP isolates affected business endpoints with EDR; leave them powered on for memory capture | MSSP | Endpoints isolated |
| T+15 to 30 min | 5. If SCADA monitoring of either operated lateral is lost or degraded, **notify the lateral owner within 30 minutes** (OSA; P01 R-041) | Shift supervisor | Call logged with time |
| T+15 to 45 min | 6. Call the insurer hotline; General Counsel engages breach counsel and the retainer | CFO; General Counsel | Claim number issued |
| T+30 to 60 min | 7. Put field crews on standby for manual operation: all 5 compressor stations, the 4 receipt interconnects, and the largest delivery points by area (about 180 field staff per shift at full manual operation) | VP Operations; Area Managers | Crews on standby or dispatched |
| T+30 to 60 min | 8. Convene the CMT on the out-of-band bridge | COO | CMT convened; decision log opened |
| T+60 min | 9. **Decision point 1** (section 4) | Director of Gas Control recommends; COO decides | Decision recorded with reasons |
| Ongoing | 10. Incident log: timeline, actions, who, when (paper if needed) | Security analyst assigned by the incident commander | Log open |

## 4. The operate-or-shut-down decision (RS.AN, RS.MI)
The Director of Gas Control recommends and the COO decides. Nothing here limits a controller or field supervisor who must act at once for safety, including emergency shutdown, valve shut-off, or pressure reduction under the emergency plan (192.615(a)(6); POL-03 4.4 and 4.6).

**Decision point 1 (T+60 min): Is OT trustworthy and visible right now?**

| Question | How to check | If yes | If no or unknown |
|---|---|---|---|
| Is the DMZ closed and holding? | OT firewall session tables at the GCC and BCC | Continue | Close again; Severity 1 |
| Is there any sign of the attacker in OT? | OT sensor alerts at the GCC, BCC, and Compressor Stations 1 and 3 (MSSP and OT Security Engineers); gateway logs for the last 30 days | Continue | Go to runbook 2 |
| Do SCADA values agree with the field? | Field technicians read local gauges at 3 or more sites per area and compare by radio, starting with Compressor Stations 2, 4, and 5 (no sensors) | Continue | Move to **outcome B** |
| Are SCADA servers and HMIs behaving normally? | SCADA and OT Engineering Manager checks processes, recent logons, and changes against the baseline (no active scanning) | Continue | Fail over to the BCC if it is clean; otherwise **outcome B** |
| Is the identity provider clean? | IT Director and MSSP review administrator activity | Continue | Keep the gateway closed; OT runs without remote access |
| Is any business IT system needed to operate safely in the next 24 hours? | BIA (P05): no. Nominations, postings, and billing have manual workarounds | Continue | Not expected |

**Outcomes:**
- **A. Isolate and operate (the default).** All answers are yes. Keep the DMZ closed. Run nominations by phone and email to the scheduling spreadsheet (BP-05), post critical notices manually (BP-08), and bill on estimates (BP-09). Recheck every 4 hours.
- **B. Isolate and operate manually or from the BCC.** SCADA values or hosts at one control center or one area cannot be trusted, but the pipeline can be run safely by field crews or from the BCC. Follow the manual operation plan. Consider reducing pressure to widen safety margins. The 8-hour MTD for gas control (BP-01) sets the next decision point.
- **C. Controlled precautionary curtailment or shutdown.** Choose this only when at least one of these is true:
  1. there is evidence that someone other than a controller is sending commands to field devices or station controls, and it cannot be stopped by isolation;
  2. manual operation cannot be staffed safely beyond the 8-hour MTD, especially on Class 3 segments;
  3. neither SCADA nor manual operation can keep the pipeline within its operating limits, in the Director of Gas Control's judgment.

  Prefer the smallest action that removes the hazard: one segment, one station, or reduced pressure, before a system shutdown. Follow the O&M manual shutdown procedures (192.605) and the emergency plan. **Before closing any delivery, coordinate with each affected LDC and power plant**, because loss of supply to homes creates its own safety risk.

**Decision point 2 (T+4 h, then every 4 h):** reassess with the retainer's findings. The CMT records each decision, the facts relied on, and who decided.

**What does not justify a shutdown on its own:** loss of email, file shares, the ERP and gas accounting, payroll, or the measurement application. These processes have MTDs of 72 to 120 hours, and measurement data is safe in the flow computers for about 35 days (P05).

## 5. Analysis, containment, and eradication (RS.AN, RS.MI)
1. **Scope (retainer and MSSP):** affected endpoints, servers, cloud accounts, and identities, from EDR, identity provider sign-in logs, cloud audit logs, and firewall logs. Check all 5 cloud accounts, starting with the backup and log archive account.
2. **Initial access:** the phishing email, stolen credential, or exposed service, and the first host compromised.
3. **Preserve evidence (SD 02G III.F.1.b):** capture memory on affected hosts before powering off; label affected equipment; export logs before they roll over (OT logs are kept only 90 days until POAM-005 closes); keep chain of custody.
4. **Check every path into OT (SCADA and OT Engineering Manager with the retainer):** the remote access gateway and its session recordings; the historian replicas; the patch and anti-malware staging server; the OT analytics cloud account; vendor accounts. Image the staging server and gateway before any cleanup. Assume any credential typed on a business endpoint is compromised and reset OT credentials from a clean OT workstation.
5. **Exfiltration:** determine whether employee personal information (HR and payroll files; P01 R-037), shipper contract data, SSI (TSA plans and assessment results), or Restricted OT information (network diagrams, SCADA configurations, CEII) was taken. Each drives a different notice (section 6).
6. **Contain and eradicate:** block attacker infrastructure at the business firewalls and cloud network rules; disable compromised accounts and rotate service credentials, including the DMZ-to-cloud push credentials; rebuild affected endpoints and servers from clean images. **Do not decrypt and reuse them.**
7. **Confirm with the retainer** that persistence is removed before anything is reconnected to the DMZ.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** The General Counsel confirms any breach notice. The Director of Pipeline Safety and Compliance owns Part 191 notices. The General Counsel keeps the **decision log**.

| # | Decision | Owner | Record |
|---|---|---|---|
| D1 | Is this a cybersecurity incident under SD 01G (unauthorized access, malicious software, denial of service, or potential operational disruption)? Ransomware on business IT: **yes** | Security Manager | Decision log; CISA report |
| D2 | If the pipeline or a segment is shut down or curtailed, is the event "significant in the judgment of the operator" (49 CFR 191.3, paragraph (3))? Default for a cyber-caused shutdown: **report** | Director of Pipeline Safety and Compliance | Decision log; NRC report number |
| D3 | Is the shutdown force majeure under the tariff (drives reservation charge credits)? | General Counsel with the VP Commercial | Legal memo |
| D4 | Was personal information acquired? Affected individuals by state, including Florida residents (thresholds: 500 for the Department of Legal Affairs, more than 1,000 for consumer reporting agencies) | General Counsel with the HR Director | Affected individuals list |
| D5 | Has law enforcement asked for a delay in breach notices? | General Counsel | Decision log |
| D6 | Ransom decision | CEO and board chair, on the CMT's recommendation | See below |

**Timeline:**
| When | Action | Owner |
|---|---|---|
| Within 30 min of losing lateral monitoring | Lateral owner notice (OSA) | Shift supervisor |
| Within 1 h of confirmed discovery of an incident (191.3) | **NRC telephonic notice** (49 CFR 191.5). For a shutdown, decide D2 in the first hour | Director of Pipeline Safety and Compliance |
| At once, if an emergency exists | 9-1-1 centers and officials along the route (192.615(a)(8)) | VP Operations |
| Before any curtailment, then every 4 h | Affected shippers, the upstream interconnecting pipelines, and the 5 power plant customers that are NERC-registered (so they can make their own reports) | VP Commercial |
| As soon as an outage or capacity reduction is known | Post service outages or reductions in capacity on the Informational Postings site (18 CFR 284.13(d)(1)); manual posting if the site is affected | Director of Regulatory Affairs |
| Day 0 | Insurer hotline before vendors; audit committee chair and PE sponsor informed | CFO; CEO |
| As soon as practicable, no later than 72 h after identification | **CISA report** (SD 01G II.C), stating that it is made to satisfy the Security Directive. Supplemental information within 24 hours of it becoming available. TSA's Information Circular IC Surface-2025-01 recommends earlier notice to TSA for significant incidents | Cybersecurity Coordinator |
| Day 0 to 1 | FBI field office; supports OFAC mitigation if a payment is considered | Security Manager through counsel |
| Within 48 h of confirmed discovery | Revise or confirm the NRC notice (191.5(c)) | Director of Pipeline Safety and Compliance |
| Within 30 days of detection | PHMSA Form F 7100.2 if a 191.5 notice was made (191.15(a)(1)) | Director of Pipeline Safety and Compliance |
| Within 30 days of determination | Florida notice to affected individuals (Fla. Stat. 501.171(4)) and to the Department of Legal Affairs if 500 or more Florida residents (501.171(3)); each other state where affected individuals reside under its own law | General Counsel; HR Director |

**Ransom decision (POL-03 4.10).** Needs an **OFAC sanctions check** on the threat actor and any wallet, General Counsel and insurer review, and approval by the CEO and the board chair. OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis, and full and timely reporting to law enforcement or CISA is a mitigating factor. The default position is **not to pay** while backups are intact. Paying does not restore trust in OT; the section 7 checks still apply. A payment would also be reportable to CISA within 24 hours if the proposed CIRCIA rule were finalized as proposed (not in effect; see the matrix).

**Communications.**
- **Staff:** short briefing script on day 0 (what happened, what to use, what not to discuss), repeated at each shift change.
- **Shippers and the public:** facts only; no speculation about the attacker or OT. Holding statement approved by the General Counsel and the COO.
- **Media:** only the Director of Corporate Communications speaks.
- **Regulators:** PHMSA, CISA, and TSA contacts go through the named owners above, never through operations staff.

## 7. Recovery and restart (RC.RP, RC.CO)
**Restore in BIA priority order (P05 section 8):**
1. Emergency communications (15 minutes)
2. Clean SCADA at the GCC or BCC with telecommunications (1 hour)
3. Lateral monitoring for the OSA customers (1 hour)
4. Compressor station control (4 hours)
5. MSSP monitoring, OT sensors, and the Coordinator channel (4 hours)
6. Identity provider and the customer activities website (4 hours)
7. Informational Postings and critical notices (12 hours)
8. Physical security systems (8 hours)
9. GIS and emergency maps (24 hours)
10. Field work management and compliance records (48 hours)
11. Leak-detection model, after its input path is clean and the model is revalidated (P10)
12. Measurement application (48 hours)
13. ERP and gas accounting, payroll and HR, and supply chain (72 hours)

**Before reopening the DMZ:**
- the retainer confirms business IT and the identity provider are clean;
- the historian replicas, the staging server, and the remote access gateway are rebuilt from clean images;
- vendor access is re-enabled one vendor at a time, with named accounts and MFA;
- the Director of Gas Control signs off.

**If SCADA hosts must be rebuilt (STD-07):**
1. Restore from the offline backup at the BCC, scanning it and comparing its hash before use (SD 02G III.F.1.c).
2. Verify configuration against the baseline.
3. Perform point-to-point verification on any display or point that changed (192.631(c)(2)).
4. Fail over and back before relying on the rebuilt host.

**Restarting after a curtailment or shutdown:**
1. Follow the O&M manual start-up procedures and coordinate with the upstream interconnecting pipelines and each affected shipper.
2. Controllers confirm SCADA values against field readings at every affected station and delivery point before returning to remote control.
3. The COO approves the restart on the Director of Gas Control's recommendation.

Tell staff, shippers, lateral owners, and the upstream pipelines as each service returns, and update the Informational Postings.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- Review control room actions under 192.631(g) (operating experience) and add lessons to controller training (192.631(h)).
- File a Cybersecurity Implementation Plan amendment if the incident leads to a permanent change (SD 02G Section VI).
- Update the risk register (P01 R-001, R-004, R-010, R-037, R-041), the POA&M (P07), this runbook, the TSA incident response plan, and the emergency plan cyber annex.
- Report the results to the audit committee at its next meeting.
- Keep incident records for at least 5 years (POL-01 4.13), or longer where a PHMSA records rule requires.
