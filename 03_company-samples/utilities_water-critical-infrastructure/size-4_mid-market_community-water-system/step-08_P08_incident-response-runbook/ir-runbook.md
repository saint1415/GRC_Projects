# Incident Response Runbook: Remote-Access Compromise of a Treatment-Plant HMI

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed investor-owned water utility; 11 community water systems, 273,900 people served) |
| Tier / Vertical | Mid-Market / Water and Wastewater Systems |
| Incident type | An unauthorized person uses a remote access path to operate an HMI or engineering workstation in the IWOS. Primary scenario: Integrator B's remote desktop agent on the Ridge engineering workstation is used to raise or stop the **sodium hypochlorite feed** at WTP-G1 or the unstaffed WTP-G2. The same steps apply to the Lakes on-call VPN, a hijacked gateway session, or an exposed small-system modem |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions, with OT response guidance from NIST SP 800-82 Rev. 3 (sections 6.4 and 6.5) |
| Policy basis | POL-03 Incident Response Policy (statements 4.1 to 4.7); ERP for each covered system (42 U.S.C. 300i-2(b)(2)) |
| Companion documents | `ir-runbook-ransomware.md` (business IT ransomware with customer data theft); `notification-matrix.csv`; BIA recovery priorities (P05 section 8); plant manual-mode procedures (STD-06) |
| Runbook owner | Security Manager (incident commander), with the Director of Water Operations for every process decision |
| Approved | 2026-09-15 by the Chief Operating Officer. Becomes the cybersecurity annex of the Ridge ERP when it is certified (target 2026-12-04), and of the Lakes and Regional ERPs at their next revision |
| Last tested | Not yet. First OT tabletop with the ROC, Ridge staff, Integrator B, and the MSSP on 2026-11-17 (POAM-011) |

**The rule that overrides everything else: keep the water safe first, then investigate.** Any operator may take any process safety action at any time without waiting for IT, management, or forensics (POL-03 statement 4.1).

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so that process, technical, and legal decisions each have one owner.

| Tier | Members | Decides |
|---|---|---|
| **Process safety command** | Chief Operator or ROC operator on duty (first hour); then the Director of Water Operations with the Plant Manager (Ridge) | Operating mode, chemical feed, sampling, plant isolation. Has authority over everyone else on process questions |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director, OT security analyst, SCADA and Controls Engineering Manager, MSSP, forensic firm (through counsel), Integrator A (trusted support) | Containment, investigation, eradication, safe reconnection |
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, General Counsel, CFO, vCISO, Director of Water Operations, Water Quality and Compliance Manager, Emergency Management and Resilience Manager, Communications Manager, Director of Utility Services, Director of Customer Service; breach counsel | Public notice, external statements, regulator and law enforcement contact, resources, mutual aid, client communications |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Process safety lead (first 60 minutes) | ROC operator on duty, then the Ridge Chief Operator or on-call operator | ROC Supervisor | ROC phone; radio; plant phone |
| Operating mode decisions | Director of Water Operations | Plant Manager (Ridge) | Out-of-band group on personal phones |
| Incident commander | Security Manager | IT Director | Incident line, then the out-of-band group |
| OT technical response | SCADA and Controls Engineering Manager and OT security analyst | Integrator A under a recorded gateway session (not Integrator B until cleared) | Cell; Integrator A 24x7 line |
| Public notice and state reporting | Water Quality and Compliance Manager | Laboratory Manager | Cell |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Legal counsel | General Counsel; breach counsel and forensics through the insurer panel | Outside counsel | Insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card in the ERP binder |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | FBI field office (and IC3) | CISA | Numbers in the ERP binder |
| Primacy agency | State drinking water program after-hours line | Regional office | Public notice SOP contact sheet |
| Mutual aid | State WARN coordinator | Neighboring utilities | ERP binder |

**Out-of-band first.** Assume the attacker can see business email, chat, and the SCADA network. Coordinate on personal phones and the printed ERP binder at the ROC, each plant control room, and the Director of Water Operations' vehicle.

**Legal privilege protocol.** Counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs, sample results) separate from legal conclusions. Operational and public health records (sample results, operator logs, notices) are never withheld for privilege reasons.

## 1. Preparation checks (Identify / Protect)
- [x] Hardwired stroke limits and analyzer alarms verified at all 4 major plants (P07 SC-24, fully satisfied)
- [x] Regional remote access only through the gateway with MFA, approval, and recording (AC-17)
- [ ] **Ridge agent removed and Lakes VPN retired; all remote paths through the gateway** (POAM-001, due 2026-10-31). Until then, an operator must be present for any agent session (stop-and-notify rule from P07)
- [ ] Offline, encrypted copies of Ridge and Lakes PLC logic and HMI projects in two locations (CP-9). **Gap until POAM-009 closes (2026-12-31).** Interim: Integrator B project files received by 2026-11-15, verified before use
- [ ] Written manual-mode procedure for each chemical feed at WTP-G1, WTP-G2, and WTP-L1; Ridge drill (POAM-024, procedures 2026-11-06, drill 2026-11-20)
- [ ] MSSP OT playbooks and direct escalation to the ROC within 15 minutes (POAM-008, 2026-11-30)
- [ ] Labeled disconnect points and a containment card at each plant (POAM-011, 2026-10-31)
- [ ] Offline customer and media contact exports for all 11 systems and the wholesale city, less than 31 days old (POAM-019, 2026-11-30)
- [x] Insurer panel counsel and forensic firm with OT experience confirmed for 2026
- [x] Tier 1 public notice and boil water templates for each system (Spanish content missing at Lakes and Ridge until 2026-12-04)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| The HMI cursor moves or screens change when no one is using them; a remote session indicator appears | Operator at WTP-G1; ROC operator watching the Ridge read-only view | **Go to section 3 now.** Then call the incident line |
| A hypochlorite feed setpoint, pump speed, or mode changed that no one on shift changed | HMI event list; ROC alarm; operator rounds | Section 3. Treat as an incident until the change is explained |
| Chlorine residual high or low alarm (hardwired) with no process cause | Hardwired alarm panel; ROC | Section 3; confirm with a grab sample |
| A remote session or VPN login outside an approved window | Gateway alert; VPN log; MSSP | ROC Supervisor ends the session; incident line |
| OT sensor alert at a Regional plant showing traffic from the Ridge or Lakes tunnel | MSSP (escalation to the ROC within 15 minutes after POAM-008) | Incident commander triages with the OT security analyst; block the tunnel if unexplained (section 3 step 4) |
| Integrator B reports its own compromise, or CISA, the FBI, or the water-sector ISAC warns about the remote tool | Phone; advisory | IT Director blocks the tool at the firewall; declare if any session occurred in the exposure window |

**Declare an HMI compromise incident (severity 1) when** any control action on the IWOS cannot be traced to an authorized person, or an unapproved remote session reached an HMI or engineering workstation.

**Record the time the company learned of the situation** in the incident log (POL-03 statement 4.3). The 24-hour Tier 1 notice and primacy agency consultation clocks run from when the system learns of the violation or situation (40 CFR 141.202(b)).

## 3. First 60 minutes: process safety and containment (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Put the affected hypochlorite feed, and any process that looks changed, in **local/manual** control at the pump panel. Return the dose to the normal rate. The hardwired stroke limit caps the pump in the meantime. **WTP-G2 is unstaffed and the ROC's Ridge view is read-only:** the ROC operator calls the on-call operator (about 35 minutes away) and the Ridge Chief Operator. If the residual is out of range at the plant outlet, the on-call operator stops the WTP-G2 high-service pumps on arrival, so that storage and WTP-G1 carry demand | Operator on duty; on-call operator for WTP-G2 | Feed on local control at the normal rate, or the plant isolated from distribution |
| 2. Take grab samples for free chlorine at the plant outlet and the first customer location; repeat every 30 minutes until stable. If continuous monitoring is unreliable, grab samples at least every 4 hours are the regulatory minimum (40 CFR 141.403(b)(3)(i)(A)); this runbook requires every 30 minutes during the incident | Operator; laboratory | Two results in range, 30 minutes apart |
| 3. **Cut every remote path into Ridge:** unplug the engineering workstation's network cable (do not power it off); IT Director blocks the agent's relay at the firewall and disables the site-to-site VPN at the ROC end | Chief Operator (Ridge); IT Director | No remote session possible (confirmed on the firewall) |
| 4. **Protect the Regional System:** block the Ridge and Lakes tunnels at the ROC firewall until the IRT confirms they are clean; check the Regional gateway for active sessions and end them | IT Director; ROC Supervisor | Tunnels blocked; no unexpected sessions |
| 5. Decide the Ridge operating mode: (a) SCADA islanded with operators watching every change, or (b) full manual operation. **If PLC or HMI integrity is in doubt, choose manual.** Staff WTP-G2 continuously until normal operation returns | Director of Water Operations | Mode recorded in the incident log |
| 6. Check whether off-spec water reached distribution: clearwell and tank levels, time off-spec, flows, and residuals at the first customer | Water Quality and Compliance Manager; Plant Manager (Ridge) | Yes or no, with evidence |
| 7. Call the cyber insurer hotline; counsel engaged; counsel engages forensics | Chief Operating Officer | Claim number issued |
| 8. Convene the CMT (out-of-band); first situation report | CMT chair | CMT meeting held |
| 9. Start the incident log: timeline, actions, who, and when; photograph HMI screens and panel states | Incident commander | Log open |

If off-spec water may have reached customers, the Water Quality and Compliance Manager starts the Tier 1 decision (section 6) **at the same time**, not after the investigation.

## 4. Analysis (RS.AN)
1. **Scope:** which HMIs, servers, PLCs, and accounts were touched. Sources: HMI event and alarm history (Ridge records show "operator" only, because logins are shared), the agent's connection history (request the vendor relay logs through Integrator B and through counsel), Ridge VPN logs, ROC firewall logs (export now), and the engineering workstation.
2. **Initial access:** which path and which credential. Check Integrator B's agent password, whether it was reused elsewhere, and whether Integrator B itself was compromised (P01 R-013).
3. **PLC integrity:** compare the running logic in every Ridge PLC with a known-good copy. Until POAM-009 closes, the only copy is Integrator B's, which must itself be verified against the commissioning documentation before use. Check PLC key switch positions.
4. **Lateral movement:** did the attacker reach Ridge's other plant, the tunnel to the ROC, the Regional network, the historian, or the business network? If business systems were reached, also follow `ir-runbook-ransomware.md` section 4 for customer data.
5. **Preserve evidence:** forensics images the engineering workstation and affected HMIs before rebuild, where this does not delay safety actions. Keep chain of custody (who collected, when, hash, storage).
6. **Other sites:** check Lakes and the small systems for the same tool or credentials. Integrator B also supports Lakes.

## 5. Containment and eradication (RS.MI)
1. Keep all remote paths into Ridge closed until the gateway path is in place. Integrator B works only on site, observed, until counsel and the IRT clear it.
2. Change every credential the attacker could have seen: HMI and engineering logins, SCADA server administrator accounts, PLC passwords, VPN accounts, and Integrator B accounts.
3. Remove the agent. Rebuild the engineering workstation and any affected HMI from known-good media. **Do not clean and reuse them.** The Ridge server's unsupported operating system makes rebuild, not repair, the only option (P01 R-016).
4. Reload PLC logic from the verified known-good copy if any difference is found. Set key switches to RUN.
5. Forensics confirms no persistence on the historian, the tunnel endpoints, or the business network before anything is reconnected.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every legally required notice. The Water Quality and Compliance Manager owns the public health clocks; the General Counsel keeps the decision log (POL-03 statement 4.5).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is this a failure or significant interruption in key treatment processes, or another waterborne emergency (Tier 1, 40 CFR 141.202(a) Table 1 item (7))? | Water Quality and Compliance Manager with the COO, after consulting the primacy agency | Decision log; sample results |
| D2 | Did residual fall below the state minimum for more than 4 hours (141.405(a)(1))? Was any required monitoring missed (141.31(b))? | Water Quality and Compliance Manager | Decision log; residual records |
| D3 | Did the event affect water sold to the wholesale city (Regional only) or a municipal client's monitoring? | Director of Water Operations; Director of Utility Services | Decision log |
| D4 | Was customer or client personal information accessed? | General Counsel with forensics | If yes, follow the ransomware runbook section 6 |
| D5 | Ransom or extortion demand? | CEO, on CMT recommendation (POL-03 statement 4.8) | Decision log; OFAC check |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer notified; counsel engaged | Chief Operating Officer |
| Hour 0-4 | Tier 1 decision (D1). If yes, draft from the template, including the Spanish statement | Water Quality and Compliance Manager with the COO |
| No later than 24 h after learning of the situation | If Tier 1: deliver the notice to all persons served (broadcast media, posting, hand delivery, or another approved method), using the offline contact export; start consultation with the primacy agency | Water Quality and Compliance Manager; Director of Customer Service; Communications Manager |
| As soon as the incident is declared | Report to the FBI (tampering, 42 U.S.C. 300i-1) | Security Manager through counsel |
| Within 24 h of declaration | Voluntary report to CISA and the water-sector ISAC | Security Manager |
| Within 24 h | Notify municipal clients if their monitoring or data were affected (contract) | Director of Utility Services |
| By the end of the next business day | If residual stayed below the state minimum for more than 4 hours: notify the State (141.405(a)(1)) | Water Quality and Compliance Manager |
| Within 48 h | If a drinking water regulation was violated, including missed monitoring: report to the State (141.31(b)) | Water Quality and Compliance Manager |
| Within 10 days of completing notices | Public notice certification with copies to the primacy agency (141.31(d)(1)) | Water Quality and Compliance Manager |
| Day 0-2 | CEO informs the audit committee chair and the PE sponsor's operating partner | Chief Executive Officer |

**The shortest clock is public health, not data.** For this incident type, the 24-hour Tier 1 notice and primacy agency consultation will almost always come due before any data breach clock. If business systems are also down, use the offline contact export, broadcast media, and door hangers.

**CIRCIA is not in effect.** No final rule had been published as of 2026-10-05. If it is finalized as proposed, the company would be covered (it exceeds the SBA size standard and owns community water systems serving more than 3,300 people), and a 72-hour CISA report would be added to this table.

**Communications.**
- Customers: Tier 1 or boil water notice if required; otherwise no public statement about a contained event without CMT approval. Holding statement approved by counsel: no technical details or attribution.
- Primacy agency: early courtesy call for any confirmed tampering, even without a Tier 1 trigger.
- Staff: briefing by the Director of Water Operations; nothing discussed outside the company.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 8). SCADA comes back **after** safe water, sampling, and public notice are stable.
1. Manual control at WTP-G1 and WTP-G2 with extra staffing (WARN mutual aid if beyond 24 hours) (BIA RTO 2 h)
2. Booster stations and tank levels on local control (2 h)
3. Public notice capability, if a notice is needed (4 h)
4. Compliance and process sampling every 4 hours or more often at plant outlets and distribution sites (4-8 h)
5. Client alarm monitoring confirmed unaffected at the ROC (2 h)
6. Ridge SCADA rebuilt from known-good media and verified clean, then reconnected **one process at a time**, with an operator watching each loop in manual before switching it back to automatic (24 h target; not yet demonstrated, P01 R-008)
7. Tunnel to the ROC re-enabled with named-flow rules only, after forensics sign-off
8. Historian and analytics; AI-001 and AI-002 stay off for Ridge data until the replica is verified (P10)

**Validate before returning to automatic control:** credentials changed; PLC logic verified against a known-good copy; remote paths closed or behind the gateway; 24 hours of stable manual-to-automatic operation on the first process. Tell customers when any notice is lifted, through the same channels as the notice (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, including Integrator A or B as relevant and the primacy agency contact if a notice was issued; written report within 30 days (POL-03 statement 4.13).
- Update the risk register (P01 R-001, R-003, R-008, R-013, R-016, R-019), the POA&M (P07), the RRA addendum, and the Ridge ERP. A real incident is a reason to revise the ERP and to check whether the RRA needs revision.
- Retain incident records and decision logs for at least 5 years (POL-01 statement 4.14), and public notices and certifications for 3 years (40 CFR 141.33(e)).
