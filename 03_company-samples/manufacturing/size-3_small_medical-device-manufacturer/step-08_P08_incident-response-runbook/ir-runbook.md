# Incident Response Runbook: Exploited Vulnerability in a Fielded PM-2 Monitor

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (connected medical device manufacturer) |
| Tier / Vertical | Small / Manufacturing (NAICS 334510) |
| Incident type | A vulnerability in a fielded PM-2 monitor is exploited, or credibly exploitable, in a way that could affect patient safety, device settings, or PHI in the device cloud |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy (product security incidents) |
| Regulatory basis | FD&C Act 524B(b)(1)-(2) (N31-33-R05); 21 CFR 803, 806, 820.35; FDA postmarket cybersecurity guidance (December 2016, nonbinding); HIPAA 164.410 for the device cloud (N62-R03); Fla. Stat. 501.171(6) |
| Runbook owner | Product Security Lead, with the VP QA/RA for the regulatory steps |
| Approved | 2026-09-04 by the COO |
| Last tested | Not yet. First tabletop exercise due 2026-11-30 (POAM-015). The R-032 response (section 9) is the first live use |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Product Security Lead | VP Engineering | Incident line (cell), then the out-of-band group chat on company phones |
| Device cloud technical lead | Cloud Operations Lead | IT Manager | Cloud on-call rotation |
| Firmware fix lead | VP Engineering | Senior firmware engineer | Cell |
| Patient safety assessment | Clinical Affairs Manager (registered nurse) | Contracted physician medical advisor | Cell |
| FDA reporting decisions (MDR, 806) | VP QA/RA | Quality manager | Cell |
| Breach decisions and notices to hospitals | Compliance Manager (Privacy Officer) | VP QA/RA | Cell |
| Hospital communications | Customer Support Manager | COO | Support line; hospital clinical engineering and privacy contacts from the BAA terms register |
| Executive decisions and advisories | COO | CEO (High risks) | Cell |
| Legal counsel | Outside FDA regulatory counsel; breach counsel through the cyber insurer | n/a | Numbers in the incident binder |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| External coordination | ISAO (after POAM-004); CISA for coordinated disclosure (voluntary); FBI field office if criminal activity | n/a | Numbers in the incident binder |

**Out-of-band first** if the corporate environment may also be compromised. Keep the reporter's identity and the vulnerability details Confidential until the agreed disclosure date (POL-04 4.5).

## 1. Preparation checks (Identify / Protect)
- [ ] CVD policy published; security@ queue alerts the Product Security Lead; 3-business-day acknowledgment (POL-03 4.4). **Gap until POAM-004 closes (2026-10-31)**
- [ ] ISAO membership active. **Gap until POAM-004 closes.** Without it, the FDA enforcement-discretion path in section 6 is not available
- [ ] Current machine-readable SBOM for each PM-2 and PM-1 firmware version in the field (POAM-007)
- [ ] Out-of-cycle release procedure approved (POAM-005)
- [ ] Signing key in an HSM with two-person approval (POAM-003). Until then, confirm the build server is not involved before signing any fix
- [ ] Device cloud logs kept 1 year (POAM-009). **Until then, export logs at declaration, because they roll over after 30 days**
- [ ] Customer advisory template and hospital contact list (clinical engineering, privacy officer, CISO) in the eQMS
- [ ] BAA terms register with each hospital's security incident notice deadline (POAM-016)
- [ ] Lab units of every PM-2 and PM-1 firmware version in the field, for reproduction
- [ ] Printed incident binder: this runbook, `notification-matrix.csv`, contacts, the advisory template

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Hospital reports alarm limits or settings changed without a clinician doing it | Support call or ticket (BP-03) | Open an eQMS complaint and a product security ticket; call the incident line |
| Researcher or ISAO reports a vulnerability, with or without exploit code | security@, CVD form, ISAO bulletin | Product Security Lead acknowledges within 3 business days; triage the same day if exploitation is claimed |
| CISA advisory, or a CISA KEV entry for a component in the PM-2 or PM-1 SBOM | Vulnerability monitoring (POAM-006) | Match the SBOM; assess exploitability in the device context |
| Device cloud telemetry shows settings pushed from outside the portal, repeated maintenance sign-ins, or certificate errors from many units | Device cloud alerts (POAM-010) | Cloud Operations Lead preserves logs and calls the incident line |
| Public disclosure or media report naming PM-2 | Monitoring, customers | Declare immediately |
| Returned unit shows modified firmware or configuration | Line 3 service (BP-07) | Quarantine the unit; chain of custody |

**Declare a product security incident when** any of these is true:
- exploitation of a PM-2 or PM-1 vulnerability is confirmed or credibly reported in the field;
- a vulnerability with a working exploit could affect alarms, monitoring, or other essential performance;
- the device cloud or the update path (update service, signing key) may have been tampered with.

**Severity:**
- **SEV-1:** exploitation in the field with possible patient harm, or tampering with the update path.
- **SEV-2:** uncontrolled risk with no evidence of exploitation.
- **SEV-3:** controlled risk (handled as a routine update).

**Record these dates in the incident log, because each starts a different clock:**
| Date | Why it matters |
|---|---|
| Date the company **learned of the vulnerability** | FDA postmarket guidance: customer communication within 30 days and fix within 60 days for uncontrolled risk |
| Date any employee **became aware** of an MDR-reportable event | 21 CFR 803.3 and 803.50 (30 days) or 803.53 (5 work days) |
| Date a PHI breach was **discovered** | 45 CFR 164.410(a)(2): the first day known to any employee, officer, or agent other than the person committing it (60-day limit) |
| Date the breach was **determined**, or there was reason to believe it occurred | Fla. Stat. 501.171(6)(a): 10-day notice to the hospital |
| Date a correction or removal was **initiated** | 21 CFR 806.10(b): 10 working days |

## 3. First 24 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the incident log and the eQMS complaint record; assign severity | Product Security Lead | Log and complaint open |
| 2. Export device cloud audit, application, and ingestion logs to protected storage. Do not wait for the 30-day rollover | Cloud Operations Lead | Export hash recorded |
| 3. Reproduce the vulnerability on a lab unit with the affected firmware version | Firmware fix lead | Reproduced, or reasons it cannot be |
| 4. Identify affected units and hospitals from the ERP serial and UDI records and device cloud inventory (firmware version by hospital) | Cloud Operations Lead | Affected-unit list |
| 5. Patient safety assessment: what could an attacker do to alarms or monitoring, and how likely is it? | Clinical Affairs Manager with the Product Security Lead | Initial controlled or uncontrolled risk call documented |
| 6. Notify the COO, VP QA/RA, and Compliance Manager; brief the CEO if SEV-1 | Incident commander | Briefing held |
| 7. If the update path may be compromised, **stop firmware distribution** from the update service | Cloud Operations Lead | Update service paused |
| 8. SEV-1: call hospital clinical engineering contacts with interim steps (see section 5) before the written advisory | Customer Support Manager | Calls logged |

## 4. Analysis (RS.AN)
1. **Exploitability and harm.** Rate exploitability (for example with CVSS and the attack path: hospital network access, physical access, or internet) and the severity of patient harm if exploited. Decide **controlled or uncontrolled risk** to safety and essential performance, as FDA's postmarket guidance describes. Record the decision in the design risk management file.
2. **Scope.** Which firmware versions, which hospitals, how many units? Is PM-1 affected? Is the device cloud a path in (for example, settings pushed through the update or settings service)?
3. **Exploitation evidence.** Look for settings changes not made through the portal, unusual maintenance sessions, certificate errors, and returned units with changed configuration. Image returned units and keep chain of custody (evidence bag, log of each person who handled the unit).
4. **PHI.** Determine whether PHI **held in the device cloud** was accessed, acquired, used, or disclosed. This drives the business associate duties. Data in a monitor's 72-hour local buffer is under the hospital's control: if it was exposed, tell the hospital so it can make its own breach decision.
5. **Signing key and build pipeline.** Confirm the key was not used outside a recorded release. If misuse is possible, treat it as SEV-1 and plan a key rotation with the fix.

**Regulatory decision points (VP QA/RA and Compliance Manager, documented in the eQMS):**
| Question | If yes | Citation |
|---|---|---|
| Does a hospital report allege the device failed to meet specifications? | Complaint record and investigation | 21 CFR 820.35(a) |
| Does information reasonably suggest a death or serious injury, or a malfunction likely to cause one if it recurred? | MDR within 30 calendar days; 5 work days if remedial action is needed to prevent an unreasonable risk of substantial harm | 21 CFR 803.50; 803.53 |
| Is the risk **controlled**? | Routine cybersecurity update; keep the 806.20 record with the justification | FDA postmarket guidance (2016); 21 CFR 806.20 |
| Is the risk **uncontrolled**? | Correction: report under 806.10 within 10 working days of initiating it, **unless all four** enforcement-discretion conditions are met (no known serious adverse events or deaths; customers told within 30 days; fix within 60 days; active ISAO member sharing the communication) | 21 CFR 806.10; FDA postmarket guidance (2016), section VII.B |
| Was PHI in the device cloud breached (four-factor assessment, 164.402)? | Notify each affected hospital within 10 days of determination (Florida) and no later than 60 days after discovery (HIPAA), or sooner under the BAA | 45 CFR 164.410; Fla. Stat. 501.171(6)(a) |
| Does the fix change the device in a way that needs a new 510(k)? | Regulatory assessment before release; a new 510(k) is also subject to 524B | 21 CFR 807.81(a)(3); P03 G-027 |

## 5. Containment and eradication (RS.MI)
**Interim compensating controls (hospitals apply them; the company writes them):**
1. Restrict the monitors' VLAN so the vulnerable interface is reachable only from the clinical engineering network.
2. Where the device cloud supports it, push a setting that disables the vulnerable interface (for example, the maintenance web interface) on affected units.
3. Increase clinical checks of alarm limits on affected units until the fix is installed.

**Company-side containment:**
1. Block attacker infrastructure at the device cloud edge. Revoke the certificates of any PM-2 unit known to be compromised.
2. Rotate PM-1 per-hospital keys for affected hospitals (POAM-018).
3. If the update path was involved, keep the update service paused and rotate the signing key before any release.

**Eradication (out-of-cycle fix, 524B(b)(2)(B)):**
1. Fix the flaw, then run verification: regression tests plus a security test of the fix by someone who did not write it.
2. Sign with two-person approval (POL-02 4.7).
3. Release in stages: lab units, then one pilot hospital, then all hospitals.
4. Field service installs PM-1 fixes by USB.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms each notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Day 0 | Log the dates in section 2; insurer notified if PHI or extortion is involved | Incident commander; COO |
| Day 0-3 | Acknowledge the reporter (CVD) and agree a disclosure timeline | Product Security Lead |
| Day 0-5 | MDR decision; 5-work-day report if remedial action is needed to prevent an unreasonable risk of substantial harm | VP QA/RA |
| Within 10 days of determining a device cloud breach | Notice to each affected hospital (Fla. Stat. 501.171(6)(a)); also meets 164.410 if made within 60 days of discovery. Check BAAs for shorter terms | Compliance Manager |
| Within 30 days of learning of an uncontrolled risk | Customer advisory: the vulnerability and impact, that work is underway, compensating controls, and when a fix is expected. Copy to the ISAO | COO approves; Customer Support Manager sends |
| Within 10 working days of initiating a correction | 806.10 report, unless all enforcement-discretion conditions are met (then keep the 806.20 record) | VP QA/RA |
| Within 30 days of becoming aware (if reportable) | MDR (803.50); supplemental reports within 30 days of new information (803.56) | VP QA/RA |
| Within 60 days of learning of an uncontrolled risk | Validated fix distributed; follow up with hospitals that have not installed it | VP Engineering; Customer Support Manager |
| Agreed disclosure date | Public advisory, credit to the reporter; optionally coordinated through CISA | Product Security Lead |

**Plan to the shortest clock.** For a device cloud breach, the Florida 10-day agent notice comes before the HIPAA 60-day limit. For an uncontrolled device risk, the 30-day customer communication comes before the 60-day fix.

**No ransom** is paid without the CEO, counsel, the insurer, and an OFAC sanctions check (POL-03 4.8).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. **BP-01 remote monitoring:** if the device cloud was affected, redeploy services from infrastructure code, restore the database to a clean point in time, and verify tenant separation before reconnecting hospitals (RTO 2 hours).
2. **BP-10 vulnerability intake and BP-03 support:** keep intake and hospital lines open throughout.
3. **BP-06 regulatory reporting:** eQMS records current; reports filed on time.
4. **BP-02 firmware distribution** (RTO 24 hours) with **BP-08 build and signing:** release the validated fix; watch adoption through telemetry until at least 95% of affected units run it, then contact the remaining hospitals.

**Validate before closing:** fixed firmware installed on lab units of each affected version; no new indicators for 14 days; compensating controls withdrawn only after the fix is installed. Tell hospitals when the incident is closed (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closure (POL-03 4.10 requires documentation within 30 days). Open a CAPA in the eQMS.
- Update the PM-2 threat model, the security risk assessment, the design risk management file, and the SBOM.
- Update the risk register (P01, especially R-001, R-003, R-004, R-032), the POA&M (P07), and this runbook.
- Record time from identification to patch and from patch to field deployment (P03 G-019 metrics).
- Keep incident and CVD records at least 6 years (POL-01 4.11). Keep 806.20 records for 2 years beyond the expected life of the device.

## 9. Worked example: shared PM-2 service password (R-032)
This runbook's first live use, in progress when it was approved.

| Date | Step |
|---|---|
| 2026-08-12 | P07 lab test finds one service password on every PM-2 unit. **Date the company learned of the vulnerability.** Declared SEV-2: uncontrolled risk, no evidence of exploitation |
| 2026-08-13 | Patient safety assessment: an attacker on the hospital network with the service manual could change alarm limits. No complaints or adverse events linked to it. **MDR decision: not reportable at this time**, documented in the eQMS |
| 2026-09-11 (target) | Customer advisory to all 40 hospitals: restrict the maintenance interface to the clinical engineering network, and check alarm limits each shift (day 30) |
| 2026-10-11 (target) | Out-of-cycle firmware with unique per-device service credentials released (day 60; POAM-002) |

**806 decision:** the company is **not yet an active ISAO member** (POAM-004), so one of the four enforcement-discretion conditions cannot be met. The VP QA/RA will report the correction under 21 CFR 806.10 within 10 working days of initiating it. PHI in the device cloud is not involved, so no business associate notice is due.
