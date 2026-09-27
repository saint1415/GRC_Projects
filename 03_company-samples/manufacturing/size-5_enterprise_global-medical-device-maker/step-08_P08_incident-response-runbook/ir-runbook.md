# Incident Response Runbook: Exploited Vulnerability in a Fielded Connected Device

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded connected medical device manufacturer) |
| Tier / Vertical | Enterprise / Manufacturing (NAICS 334510) |
| Incident type | A vulnerability in a fielded device or related system (VM-700, VM-500, DG-10, IV-300, CR-100, US-20, HB-40, the DDC update service, or the build and signing path) is exploited, or credibly exploitable, in a way that could affect patient safety, device settings, or data. Includes the **SEC materiality assessment and Form 8-K Item 1.05** step, FDA reporting, business associate notice to customers, and the disclosure committee |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Product Security Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Breach and Regulatory Notification Procedure; STD-03.4 Coordinated Vulnerability Disclosure Standard |
| Regulatory basis | FD&C Act 524B(b)(1)-(2) (N31-33-R05); 21 CFR 803, 806, 820.35; FDA postmarket cybersecurity guidance (December 2016, nonbinding); HIPAA 164.410 and 164.314(a) for the DDC and RCM (N62-R01, N62-R03); 16 CFR 318 for the consumer app (N62-R06); SEC Form 8-K Item 1.05 and 17 CFR 229.106; state breach laws (Florida worked example) |
| Runbook owner | VP Product Security (incident commander for product security incidents), with the CQRO for the FDA steps and the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | PSIRT technical tabletop 2026-05-21 (no disclosure committee). Enterprise ransomware tabletop with the disclosure committee 2025-11. **First fielded-device tabletop with the disclosure committee: 2026-11-19 (POAM-014)** |
| Notification matrix | `notification-matrix.csv` (41 obligations: 11 FDA and product, 5 HIPAA business associate, 6 FTC rule, 3 generic state, 4 Florida worked example, 4 SEC, and 8 other rows for company policy, OFAC, law enforcement, CIRCIA status, insurance, customer contracts, and two federal contract rules that do not apply) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (product security) | VP Product Security | PSIRT lead on duty | PSIRT bridge (out-of-band conferencing on company phones) |
| Enterprise incident lead (if company systems are involved) | Director of Security Operations | SOC manager on duty | SOC bridge |
| Executive incident lead | CISO | CTO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Chief Medical Officer | Crisis line |
| Patient safety assessment | Chief Medical Officer with clinical affairs | Medical safety physician on call | Crisis line |
| FDA reporting decisions (MDR, 806) | CQRO | Vice President, Regulatory Affairs | Direct mobile |
| Firmware fix and release | CTO; Director of Build and Release Engineering | Product line engineering director | Release on-call |
| DDC and update service | Vice President, Digital Health | DDC site reliability lead | DDC on-call |
| Breach decisions and notices (HIPAA business associate, FTC rule) | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Chief Accounting Officer, CISO, VP Product Security, CQRO, Chief Privacy Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Customer communications | Vice President, Field Service (hospital clinical engineering contacts); Vice President, Corporate Communications (media) | Regional service directors | Crisis line |
| Outside counsel and forensics | Retained FDA regulatory counsel; breach counsel and forensics through the insurer panel | MSSP incident team | Retainer hotlines |
| External coordination | ISAO; CISA (coordinated advisory, voluntary); FBI field office | n/a | Numbers in the incident binder |

**Out-of-band first** if company systems may also be compromised. Keep the reporter's identity and vulnerability details Restricted until the agreed disclosure date (POL-04 4.5).

## 1. Preparation checks (Identify / Protect)
- [ ] CVD policy published; intake alerts the PSIRT; 3-business-day acknowledgment (STD-03.4)
- [ ] ISAO membership active (needed for FDA's enforcement-discretion path in section 5)
- [ ] Current machine-readable SBOM for every firmware version in the field; **legacy VM-500 and IV-300 1.x images under binary analysis until POAM-005 closes**
- [ ] Out-of-cycle release path tested this quarter; secondary HSM failover tested (**gap until POAM-012 closes**)
- [ ] IV-300 1.x signing moved into the HSM service (**gap until POAM-001 closes; until then a legacy signing uses the video-recorded two-custodian procedure**)
- [ ] Customer advisory templates approved in advance by the CQRO and counsel (POAM-015)
- [ ] Materiality playbook includes the fielded-device scenario and product factors (**gap until POAM-014 closes**)
- [ ] BAA terms register current, with each customer's security incident notice deadline (**gap until POAM-022 closes**)
- [ ] FTC rule procedure and templates for the consumer app (**gap until POAM-021 closes**)
- [ ] Lab units of every fielded firmware version for reproduction; forensic kits for returned devices
- [ ] Printed incident binder: this runbook, `notification-matrix.csv`, contacts, templates

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Hospital reports settings changed without a clinician doing it, or unexpected device reboots | Field service, customer support | Open an eQMS complaint and a PSIRT case; call the PSIRT bridge |
| Researcher, ISAO, or CISA reports a vulnerability, with or without exploit code | CVD intake; ISAO bulletin; CISA advisory | Acknowledge within 3 business days; triage the same day if exploitation is claimed |
| KEV entry matches a component in a fielded SBOM | SBOM service | PSIRT assesses exploitability in the device context |
| DDC telemetry anomalies: settings pushed outside the portal, gateway management sign-ins from outside clinical networks, certificate errors from many units | DDC alerts; SOC | Preserve logs; open SOC and PSIRT cases |
| Signing or release anomaly (signing outside a release window, image hash mismatch) | SIEM; artifact repository integrity job | **Stop all releases**; treat as severity 1 |
| Public disclosure, extortion claim, or media report naming a company device | Monitoring; customers; media | Declare immediately |
| Returned unit shows modified firmware or configuration | Service depot | Quarantine; chain of custody |

**Severity (STD-03.1):**
- **SEV-1:** exploitation in the field with possible patient harm; tampering with the update or signing path; or PHI or consumer health data accessed at scale.
- **SEV-2:** uncontrolled risk with no evidence of exploitation.
- **SEV-3:** controlled risk (routine update).

**Every SEV-1 goes to the General Counsel within 24 hours and to the disclosure committee within 48 hours (POL-03 4.7).** The VP Product Security briefs the CISO, who briefs the General Counsel.

**Record these times in the incident log, because each starts a different clock:**
| Time | Why it matters |
|---|---|
| Company **learned of the vulnerability** | FDA postmarket guidance: customer communication within 30 days and fix within 60 days for uncontrolled risk |
| Any employee **became aware** of an MDR-reportable event | 21 CFR 803.50 (30 calendar days) or 803.53 (5 work days) |
| A correction or removal was **initiated** | 21 CFR 806.10 (10 working days) |
| A PHI breach was **discovered** | 45 CFR 164.410(a)(2): 60-day outer limit; BAA terms may be shorter |
| A breach was **determined**, or there was reason to believe it occurred | State agent notice (Florida worked example: 10 days, Fla. Stat. 501.171(6)(a)) |
| A consumer app breach was **discovered** | 16 CFR 318.3(c) and 318.4: 60 days |
| **Materiality determination** | SEC Form 8-K Item 1.05: 4 business days |

## 3. First 24 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the incident log, the PSIRT case, and the eQMS complaint; assign severity | VP Product Security | Records open |
| 2. Export DDC ingestion, gateway, and update service logs to protected storage; preserve SIEM data | DDC site reliability; SOC | Export hashes recorded |
| 3. Reproduce the vulnerability on lab units of each affected firmware version | Product line engineering | Reproduced, or reasons it cannot be |
| 4. Identify affected units and customers from ERP serial and UDI records and DDC inventory (firmware version by site) | DDC analytics; supply chain | Affected-unit list |
| 5. Initial patient safety assessment: what could an attacker change (alarms, infusion parameters, ECG data), and how likely is harm? Initial controlled or uncontrolled risk call | Chief Medical Officer with the VP Product Security | Documented call |
| 6. If the update or signing path may be involved, **pause the update service and all signing**; check HSM audit logs and the legacy workstation log | Director of Build and Release Engineering | Pause confirmed |
| 7. CISO briefs the General Counsel (SEV-1); the General Counsel engages outside counsel; the insurer is notified | CISO; General Counsel | Brief logged; claim number |
| 8. SEV-1: call clinical engineering contacts at affected hospitals with interim steps (section 5) before the written advisory | Vice President, Field Service | Calls logged |
| 9. COO activates the crisis management team if more than one product line, more than 20 customers, or a plant is affected | COO | Team active |

## 4. Analysis (RS.AN)
1. **Exploitability and harm.** Rate exploitability (attack path: internet-reachable gateway, hospital network access, physical access) and severity of patient harm. Decide **controlled or uncontrolled risk** to safety and essential performance, as FDA's postmarket guidance describes. Record the decision in the product risk management file.
2. **Scope.** Which products, firmware versions, customers, and units? Is a legacy product affected (VM-500, IV-300 first-generation module)? Is the DDC or the update service a path in?
3. **Exploitation evidence.** Settings changes not made through the portal; unusual gateway management sessions; certificate errors; returned units with changed configuration. Forensic images with chain of custody.
4. **Data.** Did anyone access, acquire, use, or disclose PHI **held by the company** for customers (DDC, RCM, a DG-10 gateway cache), or consumer health data in the app? This drives section 7. Data on a device under a hospital's control is the hospital's to assess; the company gives the hospital what it needs.
5. **Signing and build path.** Confirm no key was used outside a recorded release and every fielded image matches the artifact repository. If not, treat as a supply chain compromise: rotate keys, rebuild from known-good sources, and plan re-signing of affected releases.
6. **Business impact** for section 6: affected customers and units, field service visits, service credits (P05 BP-01 and BP-02 values), expected field action cost, and revenue at risk.

**Regulatory decision points (CQRO, documented in the eQMS):**
| Question | If yes | Citation |
|---|---|---|
| Does a report allege a device failed to meet specifications? | Complaint record and investigation | 21 CFR 820.35(a) |
| Does information reasonably suggest a death or serious injury, or a malfunction likely to cause one if it recurred? | MDR within 30 calendar days; 5 work days if remedial action is needed to prevent an unreasonable risk of substantial harm | 21 CFR 803.50; 803.53 |
| Is the risk **controlled**? | Routine update; keep the 806.20 record with the justification | FDA postmarket guidance (2016); 21 CFR 806.20 |
| Is the risk **uncontrolled**? | Correction reported under 806.10 within 10 working days of initiating it (no separate report if it was required and submitted under Part 803, per 806.10(f)), **unless all four** enforcement-discretion conditions are met: no known serious adverse events or deaths; customers told within 30 days; fix within 60 days; active ISAO member sharing the communication | 21 CFR 806.10; FDA postmarket guidance section VII.B |
| Does the fix change a device in a way that needs a new 510(k)? | Regulatory assessment before release; a new submission is subject to 524B | P03 G-031 |

## 5. Containment and eradication (RS.MI)
**Interim compensating controls (customers apply them; the company writes them):**
1. Restrict gateway and device management interfaces to the clinical engineering network; block them from any other network.
2. Where the DDC supports it, push a setting that disables the vulnerable interface on affected units.
3. Increase clinical checks of alarm limits or infusion settings on affected units until the fix is installed.

**Company-side containment:**
1. Block attacker infrastructure at the DDC edge; revoke certificates of units known to be compromised.
2. Rotate credentials the attacker may hold (gateway service credentials, IV-300 per-hospital keys for affected hospitals).
3. Keep the update service paused if the update path was involved, until keys are rotated and images re-verified.

**Eradication (out-of-cycle fix, 524B(b)(2)(B)):**
1. Fix the flaw; regression tests plus a security test of the fix by someone who did not write it.
2. Sign through the HSM service with two approvers who check the build provenance (PRC-01.4).
3. Staged release: lab units, one pilot customer, then all customers. Field service installs legacy fixes by USB.
4. Monitor adoption through DDC telemetry and call customers that have not installed the fix.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

**First question for counsel.** Item 106 defines a cybersecurity incident as an unauthorized occurrence on or conducted through a registrant's information systems (17 CFR 229.106(a)). When the DDC, the update service, the signing path, or other company systems are involved, the event plainly is one. When the exploitation happens only on devices in customers' networks, outside counsel advises whether the event falls within the definition. The committee still assesses the event's effect on the company either way, because it may need disclosure elsewhere in the company's reports.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every SEV-1 (enterprise or PSIRT) within 24 hours of declaration (POL-03 4.7) | CISO with the VP Product Security | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 and 5, including the CQRO's view of FDA actions and the Chief Medical Officer's safety assessment | Committee | Worksheet completed |
| 6.5 | **Materiality determination** recorded with the date and time and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would help attackers exploit unpatched devices | General Counsel; CFO; outside securities counsel; VP Product Security for technical accuracy | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align the timing and content of customer advisories, FDA communications, the public CVD advisory, media, and investor messages with the filing; brief the audit committee and board risk and technology committee chairs before filing | Corporate Communications; Investor Relations; CQRO; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers for a fielded-device incident |
|---|---|
| Quantitative | Field action cost (service visits, module swaps, replacements); service credits (P05 BP-01, BP-02); revenue at risk from affected product lines; forensic, legal, and notification costs; insurance coverage and retention |
| Patient safety | Any harm or near miss linked to the incident; MDRs filed; whether the risk is controlled or uncontrolled |
| Regulatory | Expected FDA actions (inspection, recall classification, warning letter); FTC inquiry for consumer data; OCR inquiry through customers; state attorney general interest |
| Scope | Number of customers, units, and product lines; legacy versus current products; whether company systems (DDC, update service, signing path) were involved |
| Data | PHI or consumer health data accessed; number of individuals and states |
| Reputation and strategy | Customer contract losses; health system procurement reactions; media coverage; effect on pending submissions (for example, AI-001) |

## 7. Notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms each obligation before notices go out. Plan to the shortest clock.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | FDA track: complaint records; MDR decision (5-work-day and 30-day checks); 806 decision when the correction is initiated; 806.20 record if not reportable | CQRO | eQMS records; FDA submissions |
| 7.2 | Customer advisory within 30 days of learning of an uncontrolled risk (sooner for SEV-1): the vulnerability and impact, interim controls, and the fix plan; copy to the ISAO | VP Product Security; CQRO approves | Advisory sent |
| 7.3 | Business associate track: four-factor assessment (164.402) for PHI the company holds; notice to each affected customer within its BAA term, the state agent deadline (Florida: 10 days after determination), and no later than 60 days after discovery (164.410), with the identity of each individual | Chief Privacy Officer | Customer notices |
| 7.4 | Consumer app track (if app data is involved): determine whether a breach of security occurred under 16 CFR 318.2; notify individuals, the FTC (contemporaneously if 500 or more), and media (500 or more residents of a state) within 60 days of discovery; apply state laws for company-owned data (Florida worked example: 30 days to individuals; Department of Legal Affairs if 500 or more; consumer reporting agencies if more than 1,000) | Chief Privacy Officer | Notices; FTC notice or annual log entry |
| 7.5 | Honor any law enforcement delay request (164.412; 318.4(d); state provisions); document it | General Counsel | Delay record |
| 7.6 | Public advisory on the agreed disclosure date, crediting the reporter; optionally coordinated through CISA | VP Product Security | Public advisory |
| 7.7 | Contract notices to SL-1 and SL-2 customers and the insurer | Contract owners | Notices logged |

**No ransom or extortion payment** is made without the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.10). Paying does not remove any notification or disclosure duty.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7) if company systems were affected:
1. Identity platform and break-glass access
2. Network and data center connectivity; security tooling for validation
3. RCM platform (BP-02) and DDC remote monitoring (BP-01)
4. PSIRT intake, eQMS, and field service channels (BP-05, BP-06, BP-11)
5. HSM signing service, build farm, and artifact repository (BP-04), with keys rotated if the path was involved
6. DDC update service (BP-03), reopened only for re-verified images
7. Plant MES and stations (BP-07 to BP-09) if programming stations or plant image caches were involved

**Validate before closing:** fixed firmware on lab units of each affected version; adoption at or above 95% of affected units, with named follow-up for the rest; no new indicators for 14 days; compensating controls withdrawn only after the fix is installed. Tell customers when the incident is closed (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closure; written report within 30 days (POL-03 4.13). Open a CAPA in the eQMS.
- Update the threat model, the security risk assessment, the product risk management file, and the SBOM.
- Update the risk register (P01: R-001, R-007, R-008, R-017), the POA&M (P07), this runbook, and the materiality playbook.
- Record time from identification to patch and from patch to field deployment (P03 G-026 metrics).
- The disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Keep incident, CVD, and breach records at least 6 years (POL-01 4.11), and 806.20 records 2 years beyond the expected life of the device.

## 10. Worked example: exploited DG-10 gateway management interface (fictional dates)
| Date | Step and clock |
|---|---|
| Tue 2027-03-02 | ISAO bulletin: an authentication bypass in the DG-10 management interface is being exploited at hospitals that exposed the interface outside their clinical networks; attackers changed VM-700 alarm limits through the gateway. **Company learns of the vulnerability; employees become aware of a possibly reportable malfunction.** PSIRT declares SEV-1; update service paused; CISO briefs the General Counsel |
| Wed 2027-03-03 | Disclosure committee convenes (within 48 hours); trading blackout issued. Interim advisory by phone to 140 hospitals whose gateways telemetry flags as exposed (R-007) |
| Thu 2027-03-04 | DDC pushes a setting that disables the gateway management interface on affected units. **Correction initiated.** CQRO decides a 5-day MDR is needed because remedial action is required to prevent an unreasonable risk of substantial harm |
| Fri 2027-03-05 | Forensics shows gateway PHI caches were read at 3 hospitals. **Breach discovered and determined** (business associate) |
| Mon 2027-03-08 | Committee determines the incident is **material** (field action across 140 hospitals, patient safety exposure, expected FDA follow-up, and health system contract risk) |
| Tue 2027-03-09 | **5-work-day MDR due** (803.53) |
| Fri 2027-03-12 | **Form 8-K Item 1.05 due** (4 business days after 2027-03-08: March 9, 10, 11, and 12) |
| Mon 2027-03-15 | **Florida agent notice due** to the affected Florida hospitals (10 days after the 2027-03-05 determination); the company plans to send all customer notices by 2027-03-10 to meet the shortest BAA term (5 days) |
| Thu 2027-03-18 | 806.10 report would be due (10 working days after 2027-03-04). The 5-day MDR filed on 2027-03-09 reported the correction, so no separate 806.10 report is required (806.10(f)); the CQRO documents that reasoning in the eQMS |
| Thu 2027-04-01 | Written customer advisory deadline under the postmarket guidance (30 days); the company sent it on 2027-03-05 |
| Sat 2027-05-01 | Fix distribution deadline under the postmarket guidance (60 days); target release 2027-03-26 |
| Tue 2027-05-04 | HIPAA 60-day outer limit for business associate notice (already met) |

**Why the shortest clock wins:** the BAA terms and the Florida agent notice come long before the HIPAA 60-day limit, and the 5-day MDR and the 4-business-day 8-K come before any of the notice deadlines. The incident log records each clock separately so none is missed.
