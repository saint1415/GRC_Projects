# Incident Response Runbook: Exploited Vulnerability in Fielded IX-3 Infusion Pumps

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Manufacturing |
| Incident type | A known vulnerability in fielded IX-3 infusion pumps is exploited at hospital customers, with possible patient harm, touching all three divisions |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Regulatory basis | 21 CFR 820.35(a), 803.50, 803.53, 803.56, 806.10, 806.20; FDA postmarket cybersecurity guidance (December 2016, nonbinding); 21 CFR 803.18(d) (Distribution); Form 8-K Item 1.05 (N42-R07); HIPAA 164.410 if the DCC is involved (N62-R03); state breach laws if group-held personal information is involved |
| Runbook owner | Chief Product Security Officer (product incidents); Group CISO (enterprise); notifications owned by the Group General Counsel |
| Approved | 2026-09-15 by the Group CISO, the Chief Product Security Officer, and the Group General Counsel |
| Last tested | PSIRT playbooks tested twice in 2026. **The multi-division notification matrix has not been exercised** (scenario gap 7); the first cross-division tabletop, using this scenario, is due 2026-12-15 (POAM-004) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **The vulnerability:** a flaw in the embedded web server component that IX-3 uses for biomedical maintenance. It is listed in the CISA KEV catalog. Medical Devices fixed it in the 2025 IX-3 security release, but only 58% of IX-3 pumps have it installed, because IX-3 updates go by USB (P07 SI-2; POAM-012).
- **Day 0:** a hospital's clinical engineering team calls support: drug library dose limits changed on 14 IX-3 pumps without any pharmacy change. A nurse had caught one pump running a high-alert infusion above the ordered rate for about 20 minutes; the patient was monitored, and the outcome is under clinical review.
- **Day 0 to 2:** the PSIRT reproduces the attack on a lab unit running old firmware. An ISAO bulletin reports the same component exploited in another vendor's product. Two more hospitals report changed limits.
- **Day 5 estimate:** 61 pumps with unauthorized changes at 3 hospitals in 2 states. About 17,600 IX-3 pumps at about 290 hospitals still run old firmware, including about 1,900 pumps at 31 VA and DoD facilities supplied through Distribution. Distribution holds 1,140 refurbished IX-3 exchange units, 380 with old firmware.
- **What is not involved:** IX-3 does not connect to the DCC, so no DCC PHI is involved. Pump event logs (which include patient identifiers) sit on the pumps and hospital servers, under hospital control.
- **The Testing complication:** the Testing division found the same component flaw in 2025 during an engagement for another client and holds embargoed details in its findings vault. The information barrier (POL-02 4.3) means those details must not be passed to Medical Devices.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander (product) | Chief Product Security Officer | PSIRT manager | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Patient safety assessment | Medical Devices chief medical officer with clinical affairs | Contracted clinical advisors | Division bridge |
| FDA decisions (complaint, MDR, correction) | VP Quality and Regulatory Affairs | Quality director | Division bridge |
| Fix and release | VP Engineering | IX-3 engineering manager | Division bridge |
| Field campaign | Medical Devices field service director | Regional service managers | Division bridge |
| Hospital communications | Medical Devices customer support director | Account executives | Support line and advisory distribution list |
| Holds and distributor duties | Distribution VP quality and regulatory | Distribution VP operations | Division bridge |
| Federal customers | Distribution federal contracts compliance director | Federal sales director | Contracting officer channels |
| Testing barrier guardian | Testing laboratory quality director | Group General Counsel | Division bridge |
| Enterprise IT and SOC support | Group SOC director | Group cloud platform director | SOC bridge |
| Notifications and legal | Group General Counsel with outside FDA and breach counsel | Division counsel | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| External coordination | ISAO; CISA (coordinated disclosure, voluntary); FBI field office or IC3 | n/a | Contacts in the offline incident binder |

**Out-of-band first** if the attacker may also be in corporate systems. The printed binder in each division's command center holds contacts, this runbook, the notification matrix, and the advisory template.

## 2. Preparation checks (Identify / Protect)
- [x] Published CVD policy; PSIRT intake with 2-business-day acknowledgment; active ISAO membership
- [x] Lab units of every IX-3 firmware version in the field, for reproduction
- [x] Customer advisory template and hospital contact lists (clinical engineering, CISO, pharmacy)
- [x] Distribution lot and serial trace for IX-3 exchange units and spare boards
- [ ] **IX-3 signing key under HSM or two-person custody** (gap until POAM-003 closes). Until then, any new IX-3 build is signed under the interim custody procedure with two named custodians present
- [ ] **IX-3 SBOM** (gap until POAM-008 closes). Until then, the PSIRT relies on the supplier's component list and binary analysis
- [ ] **IX-3 adoption tracked per hospital** (gap until POAM-012 closes). Until then, field service records are the source
- [ ] **One severity scale and a complete notification matrix, exercised** (gap until POAM-004 closes)
- [ ] **PSIRT and complaint workflow linked** (gap until POAM-023 closes). Until then, the VP QA/RA opens the complaint record by hand at declaration

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Hospital reports settings or drug library limits changed without authorized action | Support desk (BP-MD09); complaint | Open an eQMS complaint and a PSIRT case; call the incident line |
| ISAO bulletin, CISA advisory, or KEV entry for a component in any IX product | PSIRT monitoring | Match to IX-3 and IX-4 component lists; assess exploitability |
| Researcher report through the CVD channel | PSIRT intake | Acknowledge within 2 business days; triage the same day if exploitation is claimed |
| Distribution or a federal customer reports tampering or odd behavior | Distribution complaint intake | Record in the distributor complaint file (803.18(d)); forward to Medical Devices the same day |
| Returned or exchange unit shows modified configuration | Depot at Plant D; Distribution returns | Quarantine; chain of custody; image the unit |

**Severity 1** (group scale, POL-03 4.2): exploitation in the field with possible patient harm, or any sign the update path or a signing key is involved. This scenario is Severity 1 from Day 0.

**Record these dates in the incident log** (POL-03 4.3), because each starts a different clock:
| Date | Why it matters |
|---|---|
| Date the group **learned of the vulnerability or exploit** | FDA postmarket guidance: customer communication within 30 days and fix within 60 days for uncontrolled risk |
| Date any employee **became aware** of an MDR-reportable event | 803.50 (30 calendar days); 803.53 (5 work days) |
| Date a **correction was initiated** | 806.10 (10 working days) |
| Date of the **materiality determination** | Form 8-K Item 1.05 (4 business days) |
| Date any **PHI breach was discovered** (only if the DCC or other group-held PHI is involved) | 164.410 (60 days; BAA terms of 15 or 5 days) |

## 4. First 24 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the PSIRT case, the eQMS complaint, and the incident log; declare Severity 1 | Chief Product Security Officer; VP QA/RA | Records open |
| 2. Call clinical engineering at the reporting hospitals: isolate IX-3 pumps' maintenance interface on their networks, verify drug library limits on every IX-3 pump, and prefer IX-4 or other pumps for high-alert infusions until verified | Customer support director with the CPSO | Calls logged |
| 3. Patient safety assessment of the over-infusion event and of the worst credible misuse | Chief medical officer with clinical affairs | Initial assessment documented |
| 4. Reproduce on lab units; confirm the 2025 security release blocks the attack | VP Engineering | Reproduction report |
| 5. Confirm firmware integrity on returned units (hashes against the release repository) and that no Plant D signing activity occurred outside recorded builds | VP Engineering; Group SOC | Integrity report |
| 6. **Distribution hold:** quarantine the 380 exchange units with old firmware; stop shipping IX-3 spares until reflashed | Distribution VP quality and regulatory | Hold confirmed at all distribution centers |
| 7. **Testing barrier:** remind the Testing cybersecurity practice lead in writing that client findings on the same component may not be shared; any coordination goes through the client and the CVD channel | Testing laboratory quality director | Acknowledgment on file |
| 8. Notify the Group CISO and Group General Counsel; escalate to the disclosure committee within 24 hours (POL-03 4.7) | Incident commander | Committee convened |
| 9. Call the cyber insurer; engage outside FDA counsel | Group Chief Risk Officer | Claim number; counsel engaged |

## 5. Analysis (RS.AN)
1. **Controlled or uncontrolled risk.** With confirmed exploitation and an infusion above the ordered rate, treat the risk to essential performance as **uncontrolled** unless clinical and engineering analysis shows otherwise. Record the decision in the IX-3 risk management file.
2. **Scope.** Which firmware versions, which hospitals, how many units? Use field service records and Distribution's sales and lot data. IX-4, PM-7, and US-2 do not use the component (confirm against their SBOMs).
3. **Exploitation evidence.** Settings changes without pharmacy action; maintenance sessions from unexpected addresses in hospital network logs (ask hospitals); returned units with changed configuration. Image returned units and keep chain of custody.
4. **Personal information.** IX-3 pumps store event logs with patient identifiers under hospital control. Tell hospitals exactly what the pump stores so they can make their own breach decisions. Confirm that no group-held PHI (DCC) or personal information was involved; if any is, open the business associate and state-law rows of the matrix.
5. **Root cause.** Old firmware still in the field (58% adoption), maintenance interface reachable on hospital networks, and USB-only updates. Feed these to P01 GR-02, MD-001, and MD-011.

**Regulatory decision points (VP QA/RA with counsel, documented in the eQMS):**
| Question | If yes | Citation |
|---|---|---|
| Does a hospital allege the device failed to meet specifications? | Complaint record and investigation | 21 CFR 820.35(a) |
| Does information reasonably suggest a death or serious injury, or a malfunction likely to cause one if it recurred? | MDR within 30 calendar days | 21 CFR 803.50 |
| Is remedial action needed to prevent an unreasonable risk of substantial harm to the public health? | 5-day report | 21 CFR 803.53 |
| Is the field update campaign a correction to reduce a risk to health? | Report under 806.10 within 10 working days of initiating it, **unless** all enforcement-discretion conditions in FDA's postmarket guidance are met (no known serious adverse events or deaths; customers told within 30 days; fix within 60 days; active ISAO participation). If the over-infusion is confirmed as a serious injury, the first condition fails and the report is due | 21 CFR 806.10; FDA postmarket guidance (2016), section VII.B |
| Does any new hardening change (for example, disabling the web server by default) need a new submission? | Regulatory assessment before release; a new submission would bring in section 524B | 21 CFR 807.81(a)(3); P03 G-032 |

## 6. Containment and eradication (RS.MI)
**Interim compensating controls (hospitals apply them; the company writes them):**
1. Restrict the IX-3 maintenance interface to the clinical engineering network, or block it at the hospital firewall.
2. Verify drug library limits on every IX-3 pump each shift until the update is installed.
3. Prefer other pumps for high-alert infusions where available.

**Company-side containment:**
1. Reflash the 380 exchange units in Distribution's stock before release.
2. Put IX-3 depot repairs at Plant D on hold until each unit is updated.
3. Keep the Plant D build server under interim two-person custody (POAM-003) for any new IX-3 build.

**Eradication:**
1. **Field campaign:** field engineers and Distribution service partners install the 2025 security release on every IX-3 pump still on old firmware, highest-risk hospitals first (those with confirmed exploitation, then federal facilities and hospitals without network isolation). Track adoption per hospital (POAM-012).
2. **Hardening release** (if approved under section 5): disable the web server by default; signed under interim custody; verified by an **outside laboratory**, not the Testing division, until independence statements are in place (POAM-011).

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (31 rows).** Counsel approves every notice. The matrix has three layers:
1. **FDA duties of the manufacturer (Medical Devices):** complaint record, MDR (30-day, possibly 5-day), supplemental reports, and the 806 decision.
2. **Customer and partner duties:** the hospital advisory, ISAO sharing, coordinated disclosure, Distribution's complaint files and hold, courtesy notices to federal customers through contracting officers, and Testing's client confidentiality (which here means saying nothing about the other client's findings).
3. **Group and conditional duties:** SEC materiality; business associate and state breach notices only if group-held PHI or personal information is involved; DFARS and FAR 52.204-25 rows checked and not triggered.

| When (from Day 0) | Action | Owner |
|---|---|---|
| Day 0 | Complaint record opened; interim calls to affected hospitals; insurer and counsel engaged | VP QA/RA; customer support director; Group Chief Risk Officer |
| Day 0-1 | Distribution hold on exchange units; Testing barrier reminder | Distribution VP quality and regulatory; Testing laboratory quality director |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts (POL-03 4.7) | Group General Counsel |
| Day 0-2 | Voluntary report to FBI or IC3 and CISA; ISAO notified | Group CISO with the CPSO |
| Within 5 work days of becoming aware of the need for remedial action | 5-day MDR if the VP QA/RA decides remedial action is needed to prevent an unreasonable risk of substantial harm | VP QA/RA |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Day 7 (target; no later than day 30) | Written advisory to all hospitals with IX-3, including federal facilities: the vulnerability, impact, compensating controls, and the update plan; copy to the ISAO | Customer support director; CPSO; counsel |
| Within 10 working days of initiating the correction | 806.10 report (unless every enforcement-discretion condition is met) | VP QA/RA |
| Within 30 calendar days of awareness | MDR (803.50); supplemental reports within 30 days of new information (803.56) | VP QA/RA |
| Within 60 days of learning of the exploit | Update installed or scheduled at every affected hospital, with follow-up for those that have not installed it | Field service director |
| Agreed disclosure date | Public advisory; coordinated through CISA if used | CPSO |

**Plan to the shortest clock.** In this scenario the order is: interim calls and holds (Day 0-1), disclosure committee (24 hours), the 5-day MDR decision, the SEC filing if material (4 business days after the determination), the 10-working-day 806 report, the 30-day MDR and advisory deadline, then the 60-day fix target.

**Materiality factors for the disclosure committee:** patient harm and FDA action (MDRs, a correction report, possible inspection); number of hospitals and pumps affected; cost of the field campaign and trade-ins; effect on IX-4 sales and hospital contracts; federal customer relationships; and whether the incident shows a wider weakness in legacy products. Materiality is decided without unreasonable delay; the 4-business-day clock starts at the determination, not at Day 0.

**No ransom** is paid without the board risk committee, counsel, the insurer, and an OFAC sanctions check (POL-03 4.8).

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. **BP-MD05 PSIRT intake and BP-MD09 hospital support:** keep both open throughout (RTO 4 and 8 hours).
2. **BP-DS04 recall, hold, and complaint handling:** hold in place within 4 hours; customer lists within 24 hours.
3. **BP-MD04 build and signing:** only if a hardening release is needed, under interim two-person custody.
4. **BP-MD08 field service:** the campaign runs until adoption reaches at least 95% of affected pumps; remaining hospitals get direct outreach.
5. **BP-MD06 complaint, MDR, and correction records:** current at every milestone.

**Validate before closing:** updated firmware on every pump at the 3 hospitals with confirmed exploitation; no new reports for 30 days; compensating controls withdrawn only after the update is installed. Tell hospitals and federal customers when the incident is closed (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of closure; documented within 30 days (POL-03 4.11). Open a CAPA in the QMS.
- Update the IX-3 risk management file and threat model, the P01 registers (GR-02, MD-001, MD-011, DS-004), the POA&M (POAM-003, POAM-008, POAM-012, POAM-020), the notification matrix, and this runbook.
- Record time from identification to patch and from patch to field deployment for IX-3 (P03 G-026).
- Consider the Reg S-K Item 106 description for the next annual report.
- Keep incident, CVD, and MDR records for at least 6 years (POL-01 4.12), and 806.20 records for 2 years beyond the expected life of the device.
