# Incident Response Runbook: Exploited Vulnerability in a Fielded Connected Device

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed connected medical device manufacturer) |
| Tier / Vertical | Mid-Market / Manufacturing (NAICS 334510) |
| Incident type | A vulnerability in a fielded IP-4 pump or VM-7 monitor (or the CCC as a related system) is exploited, or credibly exploitable, in a way that could affect patient safety, device settings, or PHI in the CCC |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy (statements 4.3 to 4.7) |
| Regulatory basis | FD&C Act 524B(b)(1)-(2) (N31-33-R05); 21 CFR 803.50, 803.53, 803.56, 806.10, 806.20, 820.35(a); FDA postmarket cybersecurity guidance (December 2016, nonbinding); HIPAA 164.402-164.414 for the CCC (N62-R03); state third-party agent notice laws (Florida example: Fla. Stat. 501.171(6)) |
| Companion documents | `ir-runbook-plant-ransomware.md` (second incident type); `notification-matrix.csv`; BIA (P05); PSIRT, complaint, MDR, and correction and removal procedures (eQMS) |
| Runbook owner | Product Security Manager (incident commander), with the VP QA/RA for regulatory decisions |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Live use for R-049 since 2026-08-19 (section 9). Combined tabletop with outside counsel scheduled 2026-11-12 (POAM-013) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so technical, regulatory and legal, and business decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, VP QA/RA, VP Engineering, Chief Medical Officer, vCISO, Compliance and Privacy Officer, Director of Customer Support and Field Service, Director of Marketing and Communications | Customer advisories, field actions, product holds, external statements, resources, ransom (recommendation to the CEO) |
| **PSIRT and incident response team** | Incident commander: Product Security Manager. Product security engineers, VP Engineering's fix lead, Director of Cloud Operations, Security Manager, MSSP, independent device security lab | Reproduction, analysis, containment, fix, CCC actions |
| **Regulatory and legal cell** | VP QA/RA (chair), Regulatory Affairs Manager, Quality Manager (complaints), General Counsel, outside FDA regulatory counsel, breach counsel through the insurer, Compliance and Privacy Officer | Complaint, MDR, 806 decisions; enforcement-discretion conditions; breach decisions; privilege |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Product Security Manager | VP Engineering | Incident line, then the out-of-band group on company phones |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| FDA reporting decisions | VP QA/RA | Regulatory Affairs Manager | Cell |
| Patient safety assessment | Chief Medical Officer | Director of Clinical Affairs | Cell |
| Breach decisions and notices to hospitals | Compliance and Privacy Officer | General Counsel | Cell |
| Legal lead and privilege | General Counsel | Outside FDA regulatory counsel | Cell |
| CCC technical lead | Director of Cloud Operations | Site reliability on-call | On-call rotation |
| Hospital communications and field actions | Director of Customer Support and Field Service | COO | Support line; contacts from the BAA terms register |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card in the incident binder |
| External coordination | ISAO; CISA for coordinated disclosure (voluntary); FBI field office if criminal activity | n/a | Numbers in the incident binder |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |

**Out-of-band first** if the corporate environment may also be compromised. Keep the reporter's identity and vulnerability details Restricted until the agreed disclosure date (POL-04 4.5).

**Privilege protocol.** The General Counsel decides at declaration whether outside counsel will direct the investigation. If so, label analysis "Privileged and confidential, prepared at the direction of counsel", keep facts separate from legal conclusions, and do not speculate in email or chat. FDA-required records (complaint, MDR, 806 files) are ordinary business records and are never withheld as privileged.

## 1. Preparation checks (Identify / Protect)
- [x] CVD policy published; 3-business-day acknowledgment (13 of 14 in 2026)
- [x] Active ISAO membership; advisory sharing tested
- [x] Machine-readable SBOM for every VM-7, IP-4, AI-001, and CCC version in the field
- [ ] VM-5 SBOM (POAM-019, due 2026-11-30)
- [x] Out-of-cycle release procedure with an expedited verification path
- [x] HSM-backed signing with two approvers
- [ ] HSM key recovery exercised (POAM-008, due 2026-12-31)
- [ ] BAA terms register with each hospital's security incident notice term (POAM-013, due 2026-11-30). **Until then, the Compliance and Privacy Officer pulls the BAAs of affected hospitals on day 0**
- [x] Customer advisory template; hospital clinical engineering, biomed, privacy, and CISO contacts in the CRM
- [x] Lab units of every VM-7 and IP-4 firmware version in the field
- [ ] Day-50 checkpoint and 806.10 fallback in the PSIRT procedure (POAM-020, due 2026-10-31)
- [x] Printed incident binder: this runbook, `notification-matrix.csv`, contacts, the advisory template

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Hospital reports pump settings, calibration, or alarm limits changed without a clinician doing it | Support call or ticket (BP-14) | Open an eQMS complaint and a PSIRT ticket; call the incident line |
| Researcher, ISAO, or supplier reports a vulnerability, with or without exploit code | security@, CVD form, ISAO bulletin, supplier notice | Acknowledge within 3 business days; triage the same day if exploitation is claimed |
| CISA advisory or KEV entry matching a component in a fielded SBOM | Daily SBOM matching (POAM-007) | Assess exploitability in the device context |
| CCC telemetry: settings pushed outside the normal workflow, unusual service sessions, certificate errors across many units, drug library hash mismatch | CCC alerts | Director of Cloud Operations preserves logs and calls the incident line |
| Control assessment, penetration test, or internal finding on shipped units | P07, test reports | Declare; record the date learned |
| Public disclosure or media report naming a product | Monitoring; customers | Declare immediately |
| Returned unit with modified firmware or configuration | Line 4 depot | Quarantine the unit; chain of custody |

**Severity (one scale for corporate and product incidents, POL-03 4.4):**
- **SEV-1:** exploitation in the field with possible patient harm; tampering with the update, signing, or provisioning path; or confirmed PHI exfiltration from the CCC. Activate the CMT within 2 hours.
- **SEV-2:** uncontrolled risk with no evidence of exploitation. CMT informed within 1 business day.
- **SEV-3:** controlled risk, handled as a routine update.

**Record these dates in the incident log, because each starts a different clock:**
| Date | Why it matters |
|---|---|
| Date the company **learned of the vulnerability** | FDA postmarket guidance: customer communication within 30 days and fix within 60 days for uncontrolled risk |
| Date any employee **became aware** of an MDR-reportable event | 21 CFR 803.3 and 803.50 (30 calendar days); 803.53 (5 work days when remedial action is needed) |
| Date a correction or removal was **initiated** | 21 CFR 806.10(b): 10 working days, unless the enforcement-discretion conditions are all met |
| Date a PHI breach was **discovered** | 45 CFR 164.410(a)(2): first day known to any employee, officer, or agent other than the person committing it (60-day limit) |
| Date the breach was **determined**, or there was reason to believe it occurred | State third-party agent notice laws (Florida: 10 days, Fla. Stat. 501.171(6)(a)); BAA terms |

## 3. First 24 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-1 h | Open the incident log and the eQMS complaint record; assign severity; record the dates in section 2 | Product Security Manager | Log and complaint open |
| 0-2 h | SEV-1: convene the CMT; CEO informs the audit committee chair and PE sponsor | COO | CMT meeting held |
| 0-4 h | Export CCC audit, application, gateway, and update service logs to protected storage | Director of Cloud Operations | Export hash recorded |
| 0-4 h | If the update, signing, or provisioning path may be involved: **pause firmware distribution**, freeze signing, and stop device certificate issuance at the plant | VP Engineering; Product Security Manager | Paused and confirmed |
| 0-8 h | Reproduce on lab units of each affected firmware version, using units from production lots | Fix lead with the device lab | Reproduced, or reasons it cannot be |
| 0-8 h | Identify affected units, versions, and hospitals from the MES, ERP (UDI and serial by customer), and CCC inventory | Director of Cloud Operations; Director of Supply Chain | Affected-unit list |
| 0-12 h | Patient safety assessment: what could an attacker do to infusions, alarms, or monitoring, and how likely is it? Initial controlled or uncontrolled risk call | Chief Medical Officer with the Product Security Manager | Decision documented in the risk file |
| 0-24 h | Insurer hotline if PHI, extortion, or likely third-party claims are involved; General Counsel engages outside counsel | CFO; General Counsel | Claim number; counsel engaged |
| 0-24 h | SEV-1: call clinical engineering at affected hospitals with interim steps (section 5) before the written advisory | Director of Customer Support and Field Service | Calls logged |
| 0-24 h | Hold affected finished goods and stop shipment of affected versions | Plant Manager; Quality Manager | Hold in the ERP |

## 4. Analysis (RS.AN)
1. **Exploitability and harm.** Rate exploitability (attack path: hospital network, physical access, or internet; skill; exploit availability) and severity of patient harm, using the matrix in the PSIRT procedure. Decide **controlled or uncontrolled risk** to safety and essential performance, as FDA's postmarket guidance describes. Record the decision and rationale in the design risk management file.
2. **Scope.** Which firmware versions, which hospitals, how many units? Is VM-5 affected? Is the CCC a path in (for example through the pump programming or update services)?
3. **Exploitation evidence.** Look for settings changes outside the clinical workflow, unexpected service sessions, calibration or drug library hash mismatches, certificate errors, and returned units with changed configuration. Image returned units with chain of custody.
4. **Root cause in production.** If the weakness came from manufacturing (station script, factory mode, certificate issuance), check the MES and station change logs, open a CAPA, and decide which lots are affected.
5. **PHI.** Determine whether PHI **held in the CCC** was accessed, acquired, used, or disclosed. This drives the business associate duties. Data in a device's local buffer is under hospital control; if it may have been exposed, tell the hospital so it can make its own breach decision.
6. **Signing and provisioning.** Confirm the signing keys and the provisioning issuing key were not used outside recorded releases and issuance runs. If misuse is possible, treat as SEV-1 and plan key rotation with the fix.

**Regulatory decision points (regulatory and legal cell; documented in the eQMS with dates):**
| # | Question | If yes | Citation |
|---|---|---|---|
| D1 | Does the report allege the device failed to meet specifications? | Complaint record and investigation | 21 CFR 820.35(a) |
| D2 | Does information reasonably suggest a death or serious injury, or a malfunction likely to cause one if it recurred? | MDR within 30 calendar days; 5 work days if remedial action is needed to prevent an unreasonable risk of substantial harm to the public health | 21 CFR 803.50; 803.53 |
| D3 | Is the risk **controlled**? | Routine cybersecurity update; keep the correction record with the controlled-risk justification | FDA postmarket guidance (2016) section VII.A; 21 CFR 806.20 |
| D4 | Is the risk **uncontrolled**? | Correction: report under 806.10 within 10 working days of initiating it, **unless all four** enforcement-discretion conditions are met: no known serious adverse events or deaths; customers told within 30 days with compensating controls; validated fix distributed within 60 days; active ISAO member sharing the communication | 21 CFR 806.10; FDA postmarket guidance (2016) section VII.B |
| D5 | Are affected units still in company finished goods? | Rework them; if no portion of the lot has been released, the rework may be stock recovery, which is exempt from 806 reporting (806.1(b)(4); 806.2(m)); otherwise it is part of the correction | 21 CFR 806.1; 806.2 |
| D6 | Was PHI in the CCC breached (four-factor assessment)? | Notify each affected hospital by the shortest clock: BAA term, state third-party agent law, or 164.410 (no later than 60 days after discovery) | 45 CFR 164.402; 164.410 |
| D7 | Does the fix change the device in a way that needs a new 510(k)? | Regulatory assessment before release; a new submission is also subject to 524B | FDA premarket guidance section VII.D; P03 G-045 |
| D8 | Has law enforcement asked for a delay of PHI notices? | Delay as stated in writing; up to 30 days if oral and documented | 45 CFR 164.412 |

## 5. Containment and eradication (RS.MI)
**Interim compensating controls (hospitals apply them; the company writes them):**
1. Restrict the device VLAN so the vulnerable interface is reachable only from clinical engineering hosts, and block the affected port at the wireless controller or firewall.
2. Where the CCC supports it, push a configuration that disables the vulnerable interface on affected units.
3. Use CCC reports (calibration and drug library hashes, settings change history) to check affected units each shift until the fix is installed.
4. Increase clinical checks (infusion settings at each bag change; alarm limits each shift) where the patient safety assessment calls for it.

**Company-side containment:**
1. Block attacker infrastructure at the CCC edge. Revoke certificates of units known to be compromised.
2. Keep the update service paused if the update path was involved, and rotate keys before any release.
3. Fix the production root cause (station script, factory state check at final test) and verify on the line before releasing held goods.

**Eradication (out-of-cycle fix, 524B(b)(2)(B)):**
1. Fix, then verify: regression tests plus a security test of the fix by someone who did not write it, on units built on the production line.
2. Sign with two approvers in the HSM (POL-02 4.7).
3. Release in stages: lab units, one pilot hospital, then all affected hospitals.
4. Field service installs by USB where a hospital cannot use the update service.
5. **Day-50 checkpoint:** the VP QA/RA confirms the fix will be distributed by day 60. If not, the 806.10 report is prepared (POL-03 4.6).

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms each external notice. The VP QA/RA confirms every FDA filing. The Compliance and Privacy Officer keeps the breach decision log.

| When | Action | Owner |
|---|---|---|
| Day 0 | Log the dates in section 2; insurer notified if PHI, extortion, or claims are involved | Incident commander; CFO |
| Day 0-3 | Acknowledge the reporter (CVD) and agree a disclosure timeline | Product Security Manager |
| Day 0-5 | MDR decision (D2); 5-work-day report if remedial action is needed to prevent an unreasonable risk of substantial harm | VP QA/RA |
| Shortest of BAA term, state law, and 60 days | Notice to each affected hospital if PHI in the CCC was breached (Florida hospitals: no later than 10 days after determination) | Compliance and Privacy Officer with counsel |
| Within 30 days of learning of an uncontrolled risk | Customer advisory: the vulnerability and impact, that work is underway, compensating controls, and when a fix is expected; copy to the ISAO | COO approves; Director of Customer Support and Field Service sends |
| Within 10 working days of initiating a correction | 806.10 report, unless all enforcement-discretion conditions are met (then keep the record with the justification) | VP QA/RA |
| Within 30 days of becoming aware (if reportable) | MDR (803.50); supplemental reports within 30 days of new information (803.56) | VP QA/RA |
| Day 50 | Checkpoint on the 60-day fix date | VP QA/RA |
| Within 60 days of learning of an uncontrolled risk | Validated fix distributed; follow up with hospitals that have not installed it | VP Engineering; Director of Customer Support and Field Service |
| Agreed disclosure date | Public advisory crediting the reporter; optionally coordinated through CISA | Product Security Manager |

**Plan to the shortest clock.** For a CCC breach, a 5-business-day BAA term or a state agent law (Florida: 10 days) comes before the HIPAA 60-day limit. For an uncontrolled device risk, the 30-day customer communication comes before the 60-day fix.

**Communications.** Hospitals hear first, by phone to clinical engineering, before any public statement. Media statements go through counsel and the Director of Marketing and Communications, with no technical exploit details before the fix. Sales and field staff get a script and route questions to support.

**No ransom** is paid without the CEO, the General Counsel, the insurer, an OFAC sanctions check, and a report to law enforcement (POL-03 4.9).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. **BP-01 and BP-02 (CCC monitoring and pump programming):** if the CCC was affected, redeploy from infrastructure code, restore the database to a clean point in time, and verify tenant separation before reconnecting hospitals (RTO 2 and 4 hours).
2. **BP-05, BP-06, BP-14 (intake, regulatory, support):** keep open throughout.
3. **BP-07 then BP-04 (signing, then distribution):** release the validated fix; watch adoption through the CCC until at least 95% of affected units run it, then contact the remaining hospitals by name.
4. **BP-11 or BP-10 (the affected line):** release held lots only after the production fix is verified.

**Validate before closing:** fix installed on lab units of each affected version; no new indicators for 14 days; compensating controls withdrawn only after the fix is installed. Tell hospitals when the incident is closed (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons learned within 14 days of closure; written report within 30 days (POL-03 4.12). CAPA in the eQMS.
- Update the threat model, security risk assessment, design risk management file, SBOM, and customer security documentation.
- Update the risk register (P01), the POA&M (P07), and this runbook.
- Record time from identification to patch and from patch to field deployment (P03 G-033 metrics).
- Keep incident, CVD, and regulatory records at least 6 years; keep correction records not reported to FDA for 2 years beyond the expected life of the device (806.20(c)).

## 9. Worked example: IP-4 factory service mode left enabled (R-049)
Found during the P07 device lab test. This runbook's first live use.

| Date | Day | Step |
|---|---|---|
| 2026-08-19 | 0 | Lab finds the factory service mode enabled on all 10 sampled IP-4 pumps, reachable over the wireless interface with one factory credential. **Date the company learned of the vulnerability.** Declared SEV-2: uncontrolled risk to essential performance (an attacker on the hospital network could change calibration or infusion parameters); no evidence of exploitation |
| 2026-08-20 | 1 | MES and ERP records trace the cause to a 2026-03-02 Line 3 final test script change that dropped the lock step: 1,140 pumps shipped to 37 hospitals, plus 86 units in finished goods |
| 2026-08-21 | 2 | Script fixed and verified on the line; finished goods held and reworked; CAPA opened. CMO safety assessment documented. **MDR decision: not reportable** (no death, injury, or malfunction in use; no complaints linked), documented by the VP QA/RA. **D5:** portions of the affected lots had shipped, so the rework of held units is treated as part of the correction, not stock recovery. **D6:** PHI in the CCC is not involved, so no business associate notice is due |
| 2026-08-24 | 5 | Phone calls to clinical engineering at the 37 hospitals with interim steps: block the factory service port at the wireless controller; check the CCC calibration hash report each shift |
| 2026-09-11 | 23 | Written customer advisory with compensating controls and the planned fix date; copy shared with the ISAO the same day |
| 2026-10-08 (target) | 50 | Day-50 checkpoint on the fix date |
| 2026-10-16 (target) | 58 | Out-of-cycle IP-4 firmware released: factory mode disabled at first clinical boot and enabled only with a signed service token (POAM-001) |
| 2026-12-31 (target) | | 95% of affected pumps updated; remaining hospitals visited by field service |

**806 decision.** The company is an active ISAO member, there are no known serious adverse events or deaths, the customer communication went out on day 23, and the fix is scheduled for day 58. All four enforcement-discretion conditions in FDA's postmarket guidance are being met, so the VP QA/RA, with outside FDA regulatory counsel, recorded the justification in the eQMS instead of filing an 806.10 report. If the fix slips past day 60, or a serious adverse event is linked to the issue, the 806.10 report is due within 10 working days of initiating the correction.

**Why it matters for section 524B.** The flaw came from a production system, not from the device design. That is why P03 rates the SPDF gap (G-005) and the station validation gap (G-013) High, and why POAM-002 brings station software under design change control.
