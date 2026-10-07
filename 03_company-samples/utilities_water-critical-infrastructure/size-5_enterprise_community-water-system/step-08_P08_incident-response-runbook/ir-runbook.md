# Incident Response Runbook: Remote-Access Compromise of a Treatment-Plant HMI

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded parent of state-regulated water utilities; 126 community water systems in FL, GA, NC, TN) |
| Tier / Vertical | Enterprise / Water and Wastewater Systems |
| Incident type | An attacker uses a remote access path (vendor tool, VPN, or stolen gateway credentials) to control an operator HMI at any of the company's 214 treatment plants, with the public health response, Tier 1 public notice, an SEC materiality assessment and Form 8-K Item 1.05 step, and the crisis management and disclosure committee workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 (sec. 6.4 and 6.5) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Tier 1 Public Notice Procedure; each covered system's ERP (42 U.S.C. 300i-2(b)(2)) |
| Runbook owner | Director of Security Operations, with the Director of OT Security for sections 3 to 5 and 8, the Senior Vice President, Water Quality and Environmental Compliance for section 6, and the General Counsel for section 7 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | GCR OT tabletop 2026-03-19 (technical and operations response; **the disclosure committee did not take part**). Next: disclosure committee tabletop with this scenario on 2026-11-12 (POAM-014) |
| Notification matrix | `notification-matrix.csv` (36 obligations: 8 public notification and SDWA reporting, 2 release reporting, 5 SEC and company disclosure controls, 9 state breach rows (4 generic, 5 Florida worked example), OFAC, law enforcement, voluntary federal reporting, CIRCIA status, mutual aid, 4 contractual, and 3 not-applicable rows) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Plant and process safety (first actions) | ROCC shift supervisor (or plant chief operator at AQ-04 to AQ-06) | Plant superintendent | Plant radio and phone |
| Incident commander (cyber) | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| OT incident lead | Director of OT Security | Regional SCADA manager (GCR SCADA Manager for GCR) | OT on-call line |
| Operations lead | Regional vice president of operations for the affected system | Chief Operating Officer | Crisis line |
| Water quality and public notice | Regional water quality manager with the state utility president | Senior Vice President, Water Quality and Environmental Compliance | Direct mobile |
| Release reporting | Director of Environmental Health and Safety | Plant superintendent (RMP plants) | Direct mobile |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Vice President, Resilience and Emergency Management | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises. The Chief Operating Officer joins from 2026-10-31 (POAM-014) | Designated alternates | Committee roster in the sealed incident binder |
| Customer data and privacy | Chief Privacy Officer | Deputy General Counsel | Direct mobile |
| Outside counsel, OT incident response firm, forensics | Retained firms (engaged through counsel and the insurer panel) | MSSP incident team | Retainer hotline |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement and federal partners | FBI field office | CISA; EPA; water-sector information sharing center | Numbers in the incident binder |

**Out-of-band first.** Assume the gateway, email, chat, and the identity platform may be compromised. Use plant radios, company mobile phones, the out-of-band conferencing service, and the printed incident binder kept in every control room.

## 1. Preparation checks (Identify / Protect)
- [ ] Every plant has written manual-mode procedures for each chemical and has drilled them in the last 6 months (**gap at AQ-04 to AQ-06 until POAM-001 closes**)
- [ ] Hardwired chemical feed limits and analyzer alarms tested at the last drill (SC-24)
- [ ] Offline known-good PLC logic, HMI projects, and SCADA images current after the last change (CP-9; **6 of 40 sampled GCR controllers were stale, POAM-016**; **AQ-04 to AQ-06 backups held only by former integrators, POAM-001**)
- [ ] OT remote access gateway the only remote path (**29 systems still on legacy tools or site VPNs, POAM-001**)
- [ ] OT DMZ isolation procedure tested this year at each ROCC (the "pull the conduit" step)
- [ ] Control room break-glass accounts sealed and tested this quarter (POL-02 4.9)
- [ ] Public notice templates (Tier 1, boil water, do not drink) and offline customer contact exports current in each regional ERP binder (**AQ-04 to AQ-06 gap, POAM-021**)
- [ ] Materiality playbook and 8-K templates current, disclosure committee roster current (**OT scenario gap until POAM-014 closes**)
- [ ] Outside counsel, OT incident response firm, forensics, and insurer contacts confirmed this quarter

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Operator sees the HMI cursor move, screens change, or a setpoint, pump, or valve change nobody on shift made | Operator report | Operator takes the action in section 3 step 1 immediately; shift supervisor calls the SOC |
| Analyzer alarm (chlorine residual, pH, turbidity) without a process explanation | SCADA alarm; hardwired alarm panel | Treat as possible tampering until ruled out; grab sample |
| Remote session outside an approved window, or a vendor tool connecting without a ticket | Gateway, OT monitoring, firewall logs, SOC | SOC terminates the session and calls the shift supervisor |
| PLC program download or mode change without a change ticket | OT monitoring (31 monitored systems) | SOC calls the shift supervisor; plant checks key switch position |
| New device or unusual protocol on an OT network | OT monitoring | SOC triages; OT on-call reviews |
| Threat intelligence or federal partner warning about an active campaign against water HMIs | Water-sector information sharing center, CISA, FBI | Hunt across all systems; check remote access paths at legacy systems first |

**Declare a severity-1 OT incident when** any unauthorized command or setpoint change is confirmed on an HMI, PLC, or SCADA server, or unauthorized remote access to an OT network is confirmed.

**Record three times, separately:**
1. **Time the system learned of the situation** (public notification): when the shift supervisor or water quality manager knew of a failure or significant interruption in a key treatment process or of unsafe water. This starts the 24-hour Tier 1 notice and primacy agency consultation clocks (40 CFR 141.202(b)).
2. **Release knowledge time** (if any hazardous substance was released at or above its reportable quantity): starts the immediate notice duties (40 CFR 302.6; 40 CFR 355.40).
3. **Materiality determination time** (SEC): recorded later by the disclosure committee (section 7). This starts the 4-business-day Form 8-K clock.

## 3. First hour: protect the public and the plant (RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Take local control.** Move affected processes (chemical feed, filters, high-service pumps, wells) to manual (local) control. Do not wait for approval (POL-03 4.3). Confirm hardwired limits held | Operator; shift supervisor | Process stable in manual; feed rates verified at the pump |
| 2. **Verify water quality.** Grab samples at the plant outlet and nearest distribution points for chlorine residual, pH, and turbidity; repeat every hour until stable | Plant operators; laboratory | Results logged with times |
| 3. **Cut the remote path.** Terminate the remote session; disable the vendor tool or VPN account; if activity continues or the path is unknown, isolate the plant OT network at the OT DMZ (or unplug the site VPN at legacy systems) | SOC; OT on-call; Network Engineering | Path closed; isolation logged |
| 4. **Do not power off or reimage** HMIs, engineering workstations, or SCADA servers; photograph screens; preserve them for forensics | OT on-call | Devices preserved |
| 5. **Alert other plants.** ROCCs check all systems supervised through the same vendor, integrator, or remote tool; legacy systems AQ-04 to AQ-06 first | SOC; ROCC supervisors | Checks logged |
| 6. **Brief and escalate.** CISO briefs the COO and General Counsel; the General Counsel engages outside counsel, who retains the OT incident response firm under privilege; the insurer is notified; the COO decides whether to activate the crisis management team and the system's ERP | CISO; General Counsel; COO | Engagement letters; ERP activation recorded |
| 7. **Start the logs:** incident log (timeline, decisions, who, when), evidence register, and water quality log | Incident commander; water quality manager | Logs open |

## 4. Analysis (RS.AN)
1. **What changed in the process:** compare HMI event journals, PLC logic, and setpoints with the offline known-good versions; list every command the attacker issued and its effect. The plant runs manually until this is done.
2. **Initial access:** vendor remote desktop tool, site VPN, stolen gateway credentials, or an internet-exposed device. At legacy systems, check the vendor tool's own logs and the site VPN logs, because they are not in the SIEM.
3. **Spread:** did the attacker reach the regional WAN, the OT DMZ, other plants, the historian replica in the cloud, or IT systems (CIS, email)? Use firewall, VPN, identity, and OT monitoring logs. If customer systems were reached, start section 7A.
4. **Evidence:** the OT firm images engineering workstations and HMIs; chain of custody in the evidence register; hashes for each artifact. Keep evidence for law enforcement (tampering with a public water system is a federal crime, 42 U.S.C. 300i-1).
5. **Public health impact:** the water quality manager decides whether unsafe water reached customers, whether treatment was significantly interrupted, and whether pressure or storage losses create a risk (P05 BP-01, BP-02). This drives section 6.
6. **Business impact:** Finance and the BIA owners estimate cost using P05 values (for example, about $4.6 million per day for a loss of treatment with a boil water notice at a large plant; service credits for SL-1 clients). These estimates feed section 7.

## 5. Containment and eradication (RS.MI)
1. Keep affected plants in manual operation and isolated until section 4 steps 1 to 3 are complete.
2. Remove the access path permanently: uninstall vendor tools, disable site VPN accounts, revoke and reissue gateway credentials for the vendor and every user who used the path.
3. Reset all OT domain and local HMI passwords at the affected system; rotate PLC and device credentials where firmware supports it.
4. Restore PLC logic and HMI projects from offline known-good copies; never trust running logic until it matches the approved version (CM-3; SI-7).
5. The OT firm confirms persistence is removed before reconnection to supervisory control.

## 6. Public health and regulatory notifications (RS.CO)
**Follow `notification-matrix.csv`.** These duties do not wait for the cyber investigation.

| Step | Action | Owner | Clock |
|---|---|---|---|
| 6.1 | Decide whether the situation requires a Tier 1 notice: a waterborne emergency, such as "a failure or significant interruption in key water treatment processes" (40 CFR 141.202(a) Table 1 item (7)), or a situation the primacy agency determines has significant potential for serious adverse health effects. Decide within 2 hours (POL-03 4.4) | Regional water quality manager with the state utility president | Decision logged |
| 6.2 | Initiate consultation with the primacy agency | Regional water quality manager | No later than 24 hours after learning of the situation (141.202(b)(2)) |
| 6.3 | Issue the Tier 1 notice (boil water or do not drink) with the ten required elements (141.205(a)), using a form and manner reasonably calculated to reach all persons served: broadcast media, posting, hand delivery, or another approved method (141.202(c)). Use the offline contact export if the CIS or mass notification service is unavailable | Regional water quality manager; Vice President, Corporate Communications | No later than 24 hours after learning (141.202(b)(1)) |
| 6.4 | Follow any repeat-notice or other direction from the consultation (141.202(b)(3)) | Regional water quality manager | As directed |
| 6.5 | Report any failure to comply with a drinking water regulation, including missed monitoring during the incident | Compliance reporting team | Within 48 hours (141.31(b)) |
| 6.6 | Certify public notice compliance to the primacy agency with a representative copy of each notice | Compliance reporting team | Within 10 days of completing notification (141.31(d)(1)) |
| 6.7 | If a hazardous substance was released at or above its reportable quantity (for example, chlorine gas at an RMP plant): notify the National Response Center, and the community emergency coordinator for each affected LEPC and each affected SERC, then send the written follow-up | Director of Environmental Health and Safety | Immediately (302.6(a); 355.40, 355.42) |
| 6.8 | Report to the FBI and share with CISA, EPA, and the water-sector information sharing center through counsel (voluntary today) | CISO; General Counsel | As soon as practical |
| 6.9 | Notify SL-1 municipal clients if the same vendor, tool, or monitoring platform reaches their systems; notify the insurer and affected vendors per contract | Vice President, Contract Services; contract owners | Per contract |

## 7. SEC materiality assessment and disclosure (disclosure committee)
This step runs in parallel with sections 4 to 6. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 7.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.6) | CISO | Brief logged |
| 7.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision. The COO (or delegate) reports the operational and public health picture | General Counsel | Minutes started |
| 7.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 7.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 to 6 | Committee | Worksheet completed |
| 7.5 | **Materiality determination** made and recorded with the date and time and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 7.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details (for example, which plants lack monitoring or which remote paths remain) that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 7.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 7.8 | Align timing and content of the public notice, customer, media, municipal client, regulator, and investor communications with the filing; brief the audit committee and the safety, environmental, and risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 7.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Response and recovery costs; lost or deferred revenue from P05 values; customer credits and bottled water; service credits to SL-1 clients; expected fines and legal costs; insurance coverage and retention |
| Operational | Plants and systems affected and for how long in manual operation; whether other systems share the access path; mutual aid needed |
| Public health and safety | Whether unsafe water reached customers; Tier 1, boil water, or do not drink notices and the population covered; any illness reports; any chemical release |
| Legal and regulatory | Primacy agency enforcement, EPA inquiries, public utility commission proceedings, effect on rate cases; litigation exposure |
| Reputation and strategy | National media; municipal client loss (SL-1, SL-2); effect on pending acquisitions and on customer trust in tap water |
| Pattern | Evidence of a broader campaign (for example, a nation-state actor across several systems), even if each event alone is small |

**Planning scenario with worked clocks (fictional dates, used for the 2026-11-12 tabletop):**
- **Tuesday 2026-10-20, 02:15.** At an AQ-05 plant (legacy SCADA), the night operator sees the HMI cursor move and the sodium hypochlorite feed setpoint rise. The hardwired stroke limit caps the pump, and the high chlorine residual alarm sounds. The operator moves feed to manual at 02:22. The vendor remote desktop agent is disabled at 02:31.
- **02:50.** To flush the high-residual clearwell, the plant is taken offline for about 5 hours. Storage draws down and pressure falls low in one pressure zone (about 6,400 people). The regional water quality manager determines at **04:10** that this is a significant interruption in key treatment processes (the "learned" time for the Tier 1 clocks).
- **08:30.** Primacy agency consultation; the agency directs a precautionary boil water notice for the affected zone. The notice is issued by broadcast media, posting, and door hangers at **11:45**, well inside the 24-hour limit (04:10 Wednesday). The 10-day certification (141.31(d)(1)) runs from completion of notification.
- **Wednesday 2026-10-21.** The disclosure committee convenes. Facts: one small system, no illness reported, notice for 6,400 people, recovery cost under $1 million. Determination at 16:00: **not yet material**; review again on Friday.
- **Friday 2026-10-23, 15:00.** Forensics finds the same actor's tools on the remote access paths of two other legacy systems, and national media report a campaign against water utilities naming the company. The committee determines the incident is **material** on qualitative grounds. The Form 8-K is due by **Thursday 2026-10-29** (4 business days: October 26, 27, 28, and 29).
- No customer personal information was reached, so state breach laws are not triggered. Had the CIS been reached, each state's clock would run from that determination (Florida: 30 days, section 7A below).

### 7A. Customer data track (only if customer systems were reached)
| Step | Action | Owner |
|---|---|---|
| 7A.1 | Determine whether customer personal information was accessed or acquired; record the determination date | Chief Privacy Officer |
| 7A.2 | Build the affected population with **state of residence** for company customers and separately for SL-2 client tenants (the company is the client's third-party agent) | Chief Privacy Officer; data team |
| 7A.3 | Apply each state's law using counsel's state matrix; plan to the shortest clock | Outside counsel; General Counsel |
| 7A.4 | **Florida worked example:** individuals no later than 30 days after the determination (15 more days on written good cause applies to this individual notice only); Department of Legal Affairs within 30 days if 500 or more Florida residents; nationwide consumer reporting agencies if more than 1,000 are notified at once (Fla. Stat. 501.171(3)-(5)) | General Counsel |
| 7A.5 | **SL-2 clients:** as their third-party agent, notify each affected municipal client as soon as possible and within the contract term (10 days in the standard SL-2 contract); Fla. Stat. 501.171(6) sets the same 10-day limit for third-party agents of covered entities under that statute | Vice President, Utility Billing Services |

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.9). Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove notification or disclosure duties.

## 8. Recovery (RC.RP, RC.CO)
Recover in BIA priority order (P05 section 7). Manual operation continues until each step is validated:
1. Water quality confirmed stable in manual operation; notices lifted only with primacy agency agreement
2. Identity: reset OT domain and HMI credentials; break-glass accounts resealed
3. Network: OT DMZ rules reviewed; the legacy access path removed; at AQ-04 to AQ-06, interim firewall rules in place of the site VPN
4. Security tooling: OT monitoring sensor placed at the affected plant if it had none
5. PLC logic and HMI projects restored from offline known-good copies and compared with approved versions; any difference is investigated before automatic control resumes
6. SCADA servers and HMIs rebuilt from known-good images (8-hour RTO at ROCC-supervised systems; no tested media at AQ-04 to AQ-06, so the integrator rebuilds under OT firm supervision)
7. Supervisory control restored one process at a time, with operators watching locally
8. Historian replication and AI-001 resumed last; AI-001 alerts ignored until the model is checked against the incident period
9. Tell customers, municipal clients, the primacy agency, and staff when service and supervisory control return (RC.CO)

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- Update the risk register (P01: R-001, R-003, R-007, R-011), the POA&M (P07), this runbook, the materiality playbook, and the RRA and ERP of every affected system (the ERP must incorporate RRA revisions, 42 U.S.C. 300i-2(b)).
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain incident records, materiality minutes, and notice files for at least 5 years; public notices and certifications at least 3 years (40 CFR 141.33(e)).
