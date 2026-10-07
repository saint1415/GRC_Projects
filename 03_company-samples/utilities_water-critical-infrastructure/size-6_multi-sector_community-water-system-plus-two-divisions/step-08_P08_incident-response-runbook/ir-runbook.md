# Incident Response Runbook: Remote-Access Compromise of a Treatment-Plant HMI Through the Group OT Gateway

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Water and Wastewater Systems |
| Incident type | An attacker uses a stolen session of a Construction commissioning engineer to pass through the group OT remote access gateway (SYS-G4) and operate an HMI at WTP-A (RS-1), changing the sodium hydroxide (caustic) dose setpoint. The same stolen sign-in reaches Construction project workspaces that hold covered defense information |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 (sections 6.4 and 6.5) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06); the RS-1 ERP (42 U.S.C. 300i-2(b)(2)) |
| Runbook owner | Group CISO; process safety owned by the RS-1 Director of Operations; notifications owned by the Group General Counsel, except public health notices (Water Utility VP of Water Quality and Compliance) |
| Approved | 2026-09-15 by the Group CISO, the Water Utility president, and the Group General Counsel |
| Last tested | The RS-1 OT playbook was tested in a Water Utility tabletop on 2026-02-18. **The cross-division version and the notification matrix have not been exercised** (scenario gap 6); the first cross-division tabletop is due 2026-12-15 (POAM-004) |

**The rule that overrides everything else: keep the water safe first, then investigate.** Operators may take any process safety action at any time without waiting for IT, the SOC, management, counsel, or forensics.

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Times are illustrative.
- **Entry (Day minus 4):** a Construction commissioning engineer on the WTP-A expansion enters credentials on an adversary-in-the-middle phishing page. The attacker steals a session token for the engineer's group sign-in (SYS-G1).
- **Reconnaissance (Days minus 4 to minus 1):** with the token, the attacker browses SYS-C1 and downloads drawing sets from 3 project workspaces, including controlled technical information for a DoD installation water system (CUI that should never have left SYS-C2, P03 CG-001).
- **Impact (Day 0, 02:10):** the attacker opens a SYS-G4 session to a WTP-A engineering workstation. Because of the 2025 commissioning exception, no shift supervisor approval is needed (P07 AC-17b.). From the engineering workstation the attacker raises the caustic dose setpoint to the HMI's configured maximum and suppresses one HMI pH alarm.
- **Detection (02:19 to 02:27):** the anomaly detection model (AI-001) flags a rising pH trend at 02:19; the independent hardwired pH alarm sounds in the ROC at 02:24; the operator puts caustic feed in local control at 02:27. The hardwired stroke limit capped the pump throughout.
- **Effect:** clearwell pH rose above the plant's operating range; water above that range entered one pressure zone of RS-1 for about 40 minutes before high-service pumps were switched to the WTP-B supply.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Process safety lead (first 60 minutes) | ROC shift supervisor | RS-1 Director of Operations | Control room phones; radio |
| Incident commander | Group SOC director | Group OT Security Director | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| OT technical response | RS-1 SCADA engineering lead and technicians | OT-capable forensic firm on the insurer's panel; SCADA integrator (on site, observed) | Bridge; on site |
| Public health decisions and notices | Water Utility VP of Water Quality and Compliance | RS-1 water quality manager | Bridge; primacy agency after-hours line |
| Construction (DFARS, commissioning staff, SYS-C1) | Construction security and compliance lead | Construction CMMC program owner (second certificate holder, POAM-004) | Division bridge |
| Environmental Services (client impact) | Environmental Services remote monitoring general manager | Environmental Services security and compliance lead | Division bridge |
| Legal and notifications | Group General Counsel with outside counsel | Division counsel | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Water Utility communications manager | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline binder |

**Out-of-band first.** Assume the attacker can read corporate email and chat, because a group sign-in was stolen. Use the crisis line, managed mobile devices, and the printed binders at the ROC, the WTP-B backup control room, and each division's command center. Each binder holds this runbook, contacts, the notification matrix, manual-mode procedures, and Tier 1 templates.

## 2. Preparation checks (Identify / Protect)
- [x] Hardwired stroke limits on chemical feed pumps and independent hardwired analyzer alarms at WTP-A, WTP-B, and WTP-C (SA-8; SC-24)
- [x] Offline, verified PLC logic and HMI project backups for WTP-A and WTP-B (CP-9). WTP-C restore untested (**gap until POAM-010 closes**)
- [x] OT sensors at WTP-A, WTP-B, and the ROC feeding the SOC (SI-4). None at WTP-C (**gap until POAM-003**)
- [ ] Per-session approval for **every** gateway user (**gap until POAM-002 closes on 2026-10-31**)
- [ ] Commissioning changes only through RS-1 MOC, so a known-good baseline exists for every PLC (**gap until POAM-008 closes**)
- [ ] No CUI outside the enclave (**gap until POAM-018 closes**)
- [ ] Cross-division matrix complete and exercised, with two DFARS certificate holders and Environmental Services client contacts (**gap until POAM-004 and POAM-023 close**)
- [x] Forensic firm with OT experience confirmed through the insurer's panel
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| HMI screens change or a setpoint, mode, or alarm limit changes that no one on shift changed | Operator; HMI event list | **Go to section 4 now.** Then call the shift supervisor and the SOC |
| Hardwired pH or residual alarm with no process cause | Hardwired alarm panel | Section 4; verify with grab samples |
| AI-001 anomaly alert on pH, residual, turbidity, or flow | AI-001 alert in the ROC | Check SCADA trends and the hardwired panel; treat as a possible incident until explained. AI-001 alone never justifies a control action (P10) |
| A gateway session without an approval record, outside the commissioning schedule, or from an unusual location | SYS-G4 and SIEM alerts | SOC terminates the session and calls the ROC |
| Sign-in token used from a new country or device | SYS-G1 risk signals | Revoke sessions; review the user's gateway and SYS-C1 activity |
| A sister division, integrator, or CISA reports compromise of an account that can reach OT | Phone, email, advisory | Disable the account; declare if any session reached OT in the exposure window |

**Declare Severity 1** (group scale, POL-03 4.2) when any control action on a water system cannot be traced to an authorized person, or when an unapproved session reached OT. In this scenario the incident is declared at 02:35 on Day 0.

**Record when each clock starts** (POL-03 4.3):
- **Water system learns of the situation:** 02:24 on Day 0 (hardwired alarm and operator response). The Tier 1 and consultation clocks run from here (40 CFR 141.202(b)).
- **Construction discovers a cyber incident affecting covered defense information:** when forensics confirms the stolen session downloaded from SYS-C1 workspaces holding CUI (in the exercise, 15:00 on Day 1). The DFARS 72-hour clock runs from here.
- **Materiality determination:** the moment the disclosure committee decides. The 4-business-day Form 8-K clock runs from here, not from discovery.

## 4. First 60 minutes: process safety and containment (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Put caustic feed (and any process that looks changed) in **local/manual** control at the pump panel; return the dose to normal. The hardwired stroke limit caps the pump meanwhile | ROC operator; WTP-A operator | Feed on local control at the normal rate |
| 2. Grab samples at the clearwell and high-service discharge for pH and residual every 30 minutes until stable; sample the affected pressure zone | Operators; RS-1 laboratory | Two results in range, 30 minutes apart |
| 3. **Cut the remote path:** SOC terminates all SYS-G4 sessions and the Group OT Security Director disables the gateway for **all** regional SCADA systems; ROC unplugs the WTP-A engineering workstation's network cable (do not power it off) | SOC; Group OT Security Director; ROC | No remote session possible (confirmed on firewalls) |
| 4. Choose the operating mode: SCADA islanded from the business network with operators watching every change, or full manual. **If PLC or HMI integrity is in doubt, choose manual** | RS-1 Director of Operations | Mode recorded in the incident log |
| 5. Decide whether off-spec water reached distribution: clearwell levels, time off-spec, flows, zone sample results. Switch the affected zone's supply if needed | Water Utility VP of Water Quality and Compliance; RS-1 Director of Operations | Yes or no with evidence; supply action logged |
| 6. Disable the engineer's identity in SYS-G1 and revoke all of their sessions; disable all 34 commissioning gateway accounts | Group identity director | Accounts disabled; sessions revoked |
| 7. Call the cyber insurer's hotline; engage counsel and the OT forensic firm through the panel | Group Chief Risk Officer | Claim number issued |
| 8. Tell Environmental Services that SYS-G4 is down; SYS-E1 data flows are not affected | Incident commander | Environmental Services acknowledges |

If the change could affect public health and cannot be reversed quickly, the VP of Water Quality and Compliance starts the Tier 1 decision (section 7) **at the same time**, not after the investigation.

## 5. Analysis (RS.AN)
1. **OT scope:** which HMIs, engineering workstations, PLCs, and accounts were touched at WTP-A, and whether any other regional SCADA system saw sessions from the same account. Sources: SYS-G4 session recordings and logs, HMI event history, OT sensor data (WTP-A and the ROC), and the engineering workstation image.
2. **PLC integrity:** compare the running logic of every WTP-A PLC with the offline known-good copy (CP-9; SI-7). For PLCs changed by commissioning outside MOC (P07 CM-03b.[01]), the "known-good" copy must be rebuilt from the commissioning package and verified by Water Utility engineers before use.
3. **Identity scope:** everything the stolen session reached through SYS-G1 (SYS-C1 workspaces, email, files). Confirm whether customer or employee personal information was accessed; if so, apply the state breach rows of the matrix.
4. **CUI scope (DFARS 252.204-7012(c)(1)(i)):** identify the compromised covered defense information, the user accounts, and the systems involved, including SYS-C1 and the engineer's laptop.
5. **Other divisions:** list every Environmental Services client site and Water Utility system whose remote support depends on SYS-G4, for client notices and operations planning.
6. **Preserve evidence:** image the WTP-A engineering workstation and affected HMIs before rebuild, where this does not delay safety actions; keep images and monitoring data at least 90 days from any DFARS report (252.204-7012(e)); chain of custody.
7. **Root cause for the registers:** the AiTM phishing path, standing commissioning access without per-session approval, commissioning changes outside MOC, and CUI on SYS-C1 (P01 GR-01, GR-06, WU-001, CN-001, CN-004).

## 6. Containment and eradication (RS.MI)
1. Keep SYS-G4 closed for all users until per-session approval is enforced for everyone and the commissioning exception is removed (accelerates POAM-002). Integrators and commissioning engineers work on site, observed, meanwhile.
2. Rebuild the WTP-A engineering workstation and any affected HMI from known-good images; **do not clean and reuse them**.
3. Reload PLC logic from the verified copy wherever a difference is found; key switches to RUN.
4. Change every credential the attacker could have seen: the engineer's accounts, all commissioning accounts, engineering workstation local accounts (and remove local admin, POAM-012), and any device passwords stored on the workstation.
5. Purge CUI from the 3 SYS-C1 workspaces and the engineer's laptop after evidence is preserved (accelerates POAM-018).
6. Confirm with forensics that no persistence remains in SYS-G1, SYS-G4, the OT DMZ, or the engineer's laptop before reconnecting anything.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (27 rows).** It has four layers:
1. **Public health (Water Utility):** Tier 1 notice and primacy agency consultation within 24 hours; 48-hour violation report if monitoring was missed; certification within 10 days of completing notices; records for 3 years.
2. **Construction (DoD):** DFARS report within 72 hours of discovery, malware to DC3, 90-day preservation, the incident report number to any prime contractor, and an immediate notice from Construction to the Water Utility as the asset owner.
3. **Environmental Services (clients):** notice of the remote-support outage to affected clients (interim 24-hour rule until contract terms exist, POAM-023).
4. **Group:** SEC materiality; FBI (tampering, 42 U.S.C. 300i-1) and CISA; state breach laws only if personal information was accessed; OFAC before any ransom decision; CIRCIA not in effect.

| When | Action | Owner |
|---|---|---|
| Hour 0-1 (by 03:35 on Day 0) | Insurer notified; counsel engaged; FBI called (company rule); Construction notifies the Water Utility on the bridge | Group Chief Risk Officer; Group CISO; Construction security and compliance lead |
| Hour 0-4 | Tier 1 decision: was this a significant interruption in key treatment, and did off-spec water reach distribution? Draft the notice from the template | Water Utility VP of Water Quality and Compliance |
| No later than 24 h after the system learned of the situation (by 02:24 on Day 1) | If Tier 1: notice to all persons served in the affected zone (broadcast media, posting, hand delivery, or approved method) and primacy agency consultation started. **Never held for legal review** | Water Utility VP of Water Quality and Compliance |
| Within 24 h of declaration (by 02:35 on Day 1) | Disclosure committee convened (POL-03 4.7); CISA report (voluntary); Environmental Services client notices of the remote-support outage | Group General Counsel; Group CISO; Environmental Services remote monitoring general manager |
| Within 48 h of a violation | Report to the state if a drinking water regulation was violated, including missed monitoring (40 CFR 141.31(b)) | Water Utility VP of Water Quality and Compliance |
| Within 72 h of discovering the CUI compromise (by 15:00 on Day 4 in the exercise) | DFARS report at DIBNet; malware to DC3 if isolated; incident number to primes | Construction security and compliance lead |
| Within 4 business days of a materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 10 days of completing public notices | Certification with copies of each notice to the primacy agency (40 CFR 141.31(d)(1)) | Water Utility VP of Water Quality and Compliance |
| Within 30 days of determination (only if personal information was accessed) | State breach notices in each state where affected individuals reside (Florida worked example: individuals and, for 500 or more, the Department of Legal Affairs) | Group Chief Privacy Officer with counsel |
| Confirm before use | Each state utility commission's incident rules (**not verified** in this sample) | Water Utility regulatory affairs director |

**Plan to the shortest clock.** Here the order is: process safety, then the 24-hour Tier 1 notice and primacy consultation, then the disclosure committee and client notices within 24 hours of declaration, then the 48-hour violation report, then the DFARS 72-hour report (which runs from a later discovery), then any Form 8-K. Public health always comes first; the data clocks come later.

**Materiality factors for the disclosure committee:** public health impact and the Tier 1 notice; regulators involved (primacy agency, EPA attention, DoD, state utility commission); exposure of DoD covered defense information and the effect on the CMMC affirmation and DoD contract eligibility; the cost of remediation across 58 water systems; client effects in Environmental Services; and reputational effects. The committee decides without unreasonable delay; the 4-business-day clock starts at the determination.

**CIRCIA is not in effect.** If the final rule is published, add the 72-hour CISA report to this table; the group would be covered through the water-sector criterion.

**Ransom decision** (if the incident turns into extortion): board risk committee, counsel, the insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not remove any notice duty.

## 8. Recovery (RC.RP, RC.CO)
Restore in the BIA order (P05). SCADA returns **after** safe water and communications are stable.
1. Safe water: WTP-A on manual or islanded control with extra operators; affected zone flushed and sampled until results are normal (BP-W01, BP-W02)
2. Identity confirmed clean and the engineer's and commissioning accounts rebuilt (BP-G01)
3. Public notice capability and water quality sampling at increased frequency (BP-W05, BP-W04)
4. WTP-A engineering workstation and affected HMIs rebuilt from known-good images; PLC logic verified; each process returned from manual to automatic **one at a time** with an operator watching each loop (BP-W03)
5. SYS-G4 re-enabled for Water Utility operators first, then integrators, then Environmental Services technicians, and **last** for Construction commissioning, only with per-session approval and recording review in place (BP-G05)
6. AI-001 stays advisory and is checked against the incident data before it is trusted again (P10)

**Validate before returning to automatic control:** credentials changed, PLC logic verified, remote paths closed or behind enforced approval, and 24 hours of stable operation on the first loop. Tell customers when any notice is lifted, through the same channels as the notice (RC.CO), and tell Environmental Services clients when remote support resumes.

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery, including Construction, Environmental Services, the integrator, and the primacy agency contact if a notice was issued; documented within 30 days (POL-03 4.11).
- Update P01 (GR-01, GR-03, GR-06, WU-001, WU-003, CN-001, CN-004), the POA&M, the notification matrix, this runbook, and the **RS-1 ERP**. A real incident is a reason to revise the ERP.
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain incident records for at least 6 years (POL-01 4.11), public notices and certifications for 3 years (40 CFR 141.33(e)), and DFARS images and data for at least 90 days from the report.
