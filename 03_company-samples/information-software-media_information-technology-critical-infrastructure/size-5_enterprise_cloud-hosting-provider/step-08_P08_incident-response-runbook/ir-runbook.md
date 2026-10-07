# Incident Response Runbook: Compromise of Provider Tooling Affecting Downstream Customers

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded public cloud and managed infrastructure provider) |
| Tier / Vertical | Enterprise / Information Technology |
| Incident type | An attacker uses a stolen engineer session to push a malicious guest-agent release through the fleet automation service (SYS-09) to enrolled customer VMs and SL-3 servers, with the SEC materiality assessment and the FedRAMP, bank, DFARS, HIPAA, and multi-state customer notification workflows |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Customer, Bank, and Multi-State Notification Procedure; PRC-03.4 FedRAMP Incident Reporting Procedure |
| Runbook owner | Director of Security Operations, with the General Counsel for sections 6 and 7 and the Director of FedRAMP Compliance for section 7.1 |
| Approved | Executive risk committee, 2026-09-08 |
| Last tested | Technical tabletop on a fleet automation compromise, 2026-05-20 (SOC and engineering only). Next: full tabletop with the disclosure committee on 2026-11-18 (POAM-011) |
| Related risks | P01 R-001 (Very High), R-018, R-013, R-016, R-027 |
| Notification matrix | `notification-matrix.csv` (29 obligations: 5 FedRAMP, 2 bank, 3 DFARS, 1 HIPAA, 1 customer contract, 5 state (Florida worked example), 3 SEC, plus SLA reporting, law enforcement, CIRCIA status, OFAC, 3 FAR clauses, insurance, and inbound supplier notice) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge on the out-of-band conferencing service |
| Executive incident lead | CISO | Chief Technology Officer | Out-of-band group on company mobile phones |
| Technical lead, release path | Vice President, Software Supply Chain | Vice President, Platform Engineering | Out-of-band group |
| Crisis management team chair | Chief Technology Officer | Chief Operating Officer | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | Chief Financial Officer, Controller, CISO, Chief Risk Officer, Chief Privacy Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| FedRAMP reporting | Director of FedRAMP Compliance | FedRAMP on-call reporter in the SOC | FedRAMP Security Inbox and the out-of-band group |
| Government customers | Senior Vice President, Government Cloud | Director of Government Cloud Engineering | Agency contact list in the G1 partition |
| Banks, health care, and all other customers | Senior Vice President, Customer Support | Vice President, Customer Success | Customer notice platform; status page |
| SL-3 managed customers | Senior Vice President, Managed Infrastructure Services | AQ-1 integration lead | Managed services hotline |
| Privacy and breach decisions | Chief Privacy Officer | Deputy General Counsel | Direct mobile |
| Outside counsel and forensics | Retained firms (engaged through counsel and the insurer panel) | Second forensics firm on retainer | Retainer hotline |
| Law enforcement and CISA | FBI field office | CISA | Numbers in the incident binder |

**Out-of-band first.** The attacker used a real engineer session, so assume the engineer's identity, chat, and email may be watched. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder. Do not discuss the response in engineering chat channels.

## 1. Preparation checks (Identify / Protect)
- [ ] Fleet automation **global freeze** (kill switch) tested this quarter; two people can trigger it without the release pipeline (STD-01.9)
- [ ] Guest-agent **denylist** mechanism tested: enrolled agents refuse a release by hash within 10 minutes
- [ ] Two-person release approval from separate teams with signed approvals (**gap until POAM-001 closes on 2026-12-15**; interim SOC review of each release under EXC-2026-034)
- [ ] Enrollment records show which customer VMs and SL-3 servers run each agent version (needed to scope customers)
- [ ] Clean-build environment and offline signing ceremony procedure ready (HSM quorum holders reachable)
- [ ] FedRAMP Initial Incident Report template pre-filled from the SOC case (**15-minute Class D capability gap until POAM-010 closes**)
- [ ] Bank-designated contacts current (**188 of 210 until POAM-023 closes**); fallback CEO and CIO contacts on file for all 210
- [ ] Materiality worksheet includes multi-tenant factors and AQ-1 lines (**gap until POAM-011 closes**)
- [ ] Customer notice templates (general, bank, DIB, HIPAA, agency) approved by counsel
- [ ] Status page on Cloud provider X reachable with credentials outside the company identity platform

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Guest-agent release outside the release calendar, or approved outside normal hours | Fleet automation audit log; SOC detection on release anomalies | Trigger the global freeze; open a severity-1 case; page the incident commander |
| Integrity or behavior anomaly in ring 0 or ring 1 VMs after a release (new outbound connections, credential access, new processes) | EDR on company test VMs; network telemetry; customer reports | Freeze; denylist the release hash; open a case |
| Engineer session used from a new device or location, or token reuse | Workforce identity platform; PAM; SIEM | Revoke sessions; disable the account; check the account's recent releases |
| Customer or agency reports suspicious guest-agent behavior | Support case; agency SOC; DIB customer | Treat as severity 1 until scoped |
| Threat intelligence or law enforcement reports a campaign against cloud provider tooling | CISA; FBI; information sharing groups | Review recent releases; raise monitoring |
| Signing service issues signatures outside expected volume or provenance | HSM audit log; signing service alerts | Freeze; suspend the signing role; key ceremony team on call |

**Declare a severity-1 provider tooling incident when** a release is confirmed or suspected to contain unauthorized code, or a release path identity is confirmed compromised.

**Record four times, separately:**
1. **Discovery time:** the first time any workforce member knew or should have known (HIPAA 164.410 clock; DFARS "discovery").
2. **FedRAMP reportability decision time:** when the incident is identified as a FedRAMP Reportable Incident (IEC clocks start).
3. **Bank determination time:** when the incident commander determines covered services to banks were, or are reasonably likely to be, materially disrupted for four or more hours.
4. **Materiality determination time** (SEC): recorded by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Global freeze** of fleet automation: stop every rollout in every channel and region, including G1 | Vice President, Software Supply Chain (or any two release officers) | Freeze confirmed in all regions |
| 2. **Denylist** the malicious release hash so enrolled agents refuse it; order agents that installed it to stop the payload where the agent can do so safely | Software supply chain engineering | Denylist acknowledged by agents |
| 3. Revoke all sessions and tokens of the compromised engineer and of everyone who can approve channel releases; require re-enrollment of hardware keys in person | Director of Identity and Access Management | Revocations logged |
| 4. Suspend the release signing role for the guest-agent channel; HSM quorum holders confirm no key export occurred; do not destroy keys (evidence) | Director of Key Management and PKI | Signing role suspended |
| 5. Build the **affected population** from enrollment records: customer accounts, VMs, regions, G1 agencies, DIB customers, banks, health care customers, and SL-3 servers that received the release | SOC; data team | Population file v1 |
| 6. CISO briefs the Chief Executive Officer and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Engagement letters; claim number |
| 7. FedRAMP reportability decision; if reportable, Initial Incident Report to all affected parties within 1 hour (Class C, PAIN 3 to 5) | Director of FedRAMP Compliance | Report sent and logged |
| 8. Status page updated within 15 minutes of confirmed customer impact; first customer advisory with indicators of compromise and safe actions (for example, disabling the agent) | Senior Vice President, Customer Support | Status page and advisory live |
| 9. Start the incident log and the evidence register; place DFARS 90-day holds on G1 logs and images if DIB customers are affected | Incident commander | Log open; holds placed |

## 4. Analysis (RS.AN)
1. **How did the attacker get the session?** Check the engineer's endpoint (EDR), the identity platform (device, location, token use), and PAM. Look for token theft from a browser on a managed laptop, a compromised developer tool, or social engineering of the help desk.
2. **What did the release do?** Reverse-engineer the payload in an isolated lab. Determine whether it read customer data, created persistence, opened outbound connections, or changed configurations. This drives the breach analysis in section 7.
3. **Who received it?** Rings 0 and 1 first (company test VMs and 1% of enrolled VMs), then any wider rollout before the freeze. Separate: commercial tenants by region; G1 agencies; DIB customers; banks; HIPAA customers; SL-3 servers (fleet automation, not the AQ-1 RMM tool).
4. **What else did the identity touch?** Every action by the compromised identity in the previous 90 days: other releases, host channel, repositories, signing requests.
5. **Evidence:** forensics images the engineer's laptop, exports release, signing, and approval logs, and keeps chain of custody in the evidence register with hashes. For DIB customers, preserve images and monitoring data for at least 90 days from the DFARS report (252.204-7012(e)).
6. **Business impact:** Finance estimates SLA credits, response cost, and lost usage using P05 values (for example, $24.7 million per day if R1 customers' workloads stop; SL-3 managed services about $1.1 million per day). These estimates feed section 6.

## 5. Containment, eradication, and recovery of the release path (RS.MI, RC.RP)
1. Keep the freeze until the release path is rebuilt: new approval workflow with two approvers from separate teams and signed approvals (POAM-001 items done early if needed), and an automated halt on integrity alerts.
2. Rotate credentials for all release-path identities; reissue hardware keys in person.
3. Rebuild the build runners for the guest-agent channel from clean images; verify provenance for the last 90 days of releases.
4. Decide with the CISO whether to re-key the guest-agent signing key. If yes, run an offline key ceremony with HSM quorum and push the new trust anchor through the host channel first.
5. Publish a **clean agent release** through the rebuilt path, staged by ring, with customer opt-in for regulated customers (agencies, banks) where they prefer to apply it themselves.
6. For SL-3 servers: managed services engineers remediate each server under the customer's maintenance window or emergency approval, and record the work for the customer.
7. Restore in BIA priority order (P05 section 7): identity and keys; control planes and status communications; security tooling; G1 (agency-coordinated); fleet automation for host security patches only; SL-3 jobs; normal releases last.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 12 hours of declaration (POL-03 4.7) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 24 hours of declaration and meets at least daily until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 and 5 | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date, time, and reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Leave out technical details that would help attackers or impede response | General Counsel; Chief Financial Officer; outside securities counsel | Draft approved by the Chief Executive Officer and Chief Financial Officer |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay. Agencies or law enforcement may ask for one in a G1 incident; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align timing and content of the 8-K, customer advisories, agency reports, bank notices, the status page, and investor messages; brief the audit committee and the risk and technology committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed. Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | What the committee considers for a multi-tenant incident |
|---|---|
| Quantitative | SLA credits by region and service; response and forensic cost; lost usage; expected customer churn (contract renewal pipeline at risk); cost of the clean release and SL-3 remediation; insurance coverage and retention |
| Customers affected | Number of customers and VMs that received the release; how many are agencies, DIB, banks, health care; any customer whose own operations stopped |
| Data | Whether customer data was read or taken, from how many customers, and what types (federal data, CUI, PHI, personal information) |
| Federal certification | Likelihood of FedRAMP corrective action or loss of FR-1 or FR-2; effect on the Class D upgrade and the sponsoring agency's plans |
| Legal and regulatory | Agency, bank regulator, DoD, HHS, and state inquiries; contract breaches; litigation exposure |
| Reputation and strategy | Media and analyst coverage; trust in the guest agent across the customer base; effect on sales and the AQ-1 integration |

**Worked example of the clocks (fictional dates):**
- **Tuesday 2027-02-02, 06:40:** severity 1 declared after ring-1 anomalies; discovery time recorded as 06:25 (first SOC analyst alert).
- **06:55:** FedRAMP Reportable Incident identified (PAIN 5 by default). Initial Incident Report due by **07:55** (Class C, 1 hour). If SL-2 were already Class D, it would be due by 07:10 (15 minutes).
- **11:30:** incident commander determines that SL-3 bank customers' managed services are likely disrupted for four or more hours while servers are remediated. Bank notices go out **as soon as possible**, at 12:15.
- **Customer contract notice:** incident confirmed 09:00 Tuesday, so customer notices are due by **Friday 2027-02-05, 09:00** (72 hours). DIB customers' DoD reports are due within 72 hours of discovery, by **Friday 2027-02-05, 06:25**, and the company supports them before then.
- **Thursday 2027-02-04, 17:00:** disclosure committee determines the incident is material. Form 8-K due by **Wednesday 2027-02-10** (4 business days: February 5, 8, 9, and 10).
- **Monday 2027-02-08:** forensics confirms the payload read files on some customer VMs that hold personal information. Florida third-party agent notices to those customers are due by **Thursday 2027-02-18** (10 days). HIPAA business associate notices: the BAA's 72 hours from confirmation applies, inside the 60-day outer limit from discovery (2027-04-03).

## 7. Notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out. One master calendar tracks every clock.

### 7.1 FedRAMP and government customers
| Step | Action | Owner |
|---|---|---|
| 7.1.1 | Decide reportability (IEC-CSO-EFR); PAIN 5 by default until estimated (IEC-CSO-DPR, IEC-CSO-EFI) | Director of FedRAMP Compliance |
| 7.1.2 | Initial Incident Report to all affected parties within the class timeframe; include the FedRAMP ID (CDS-CSO-FID) | Director of FedRAMP Compliance |
| 7.1.3 | Ongoing Incident Reports every 6 hours (Class C, PAIN 3 to 5), including when there is no new information | FedRAMP on-call reporter |
| 7.1.4 | Agency calls with each affected agency SOC; agencies run their own reporting to CISA | Senior Vice President, Government Cloud |
| 7.1.5 | Final Incident Report within 6 hours of resolution and recovery (Class C, PAIN 3 to 5); lessons learned go into the next Ongoing Certification Report (CCM-OCR-AVL) | Director of FedRAMP Compliance |

### 7.2 Banks (12 CFR 53.4; 225.303; 304.24)
| Step | Action | Owner |
|---|---|---|
| 7.2.1 | Incident commander records the four-hour determination (or that the incident is reasonably likely to cause it) | Incident commander |
| 7.2.2 | Notify at least one bank-designated contact at each affected bank as soon as possible; where no contact was provided, notify the CEO and CIO or two people of comparable responsibility | Senior Vice President, Customer Support |
| 7.2.3 | Give banks enough facts for their own 36-hour regulator notice (12 CFR 53.3 and parallels) and follow-up updates | Senior Vice President, Customer Support |

### 7.3 DIB customers (DFARS 252.204-7012 flow-down)
| Step | Action | Owner |
|---|---|---|
| 7.3.1 | Notify each affected DIB customer with the facts needed for its 72-hour DoD report; report through DIBNet where the DFARS addendum requires it | Director of FedRAMP Compliance |
| 7.3.2 | Submit malicious software as DoD directs (7012(d)); keep the 90-day media preservation hold (7012(e)); route DoD requests for access through the General Counsel (7012(f), (g)) | Director of Security Operations |

### 7.4 HIPAA customers and personal information (business associate and third-party agent)
| Step | Action | Owner |
|---|---|---|
| 7.4.1 | Determine whether PHI in HIPAA-eligible services was accessed; four-factor assessment support for each covered entity (164.402) | Chief Privacy Officer |
| 7.4.2 | Notify each affected covered entity within the BAA term (72 hours from confirmation) and no later than 60 days after discovery (164.410), with the identity of each affected individual when known | Chief Privacy Officer |
| 7.4.3 | For customers' personal information: notify each customer (the data owner) under each state's service provider rule. **Florida worked example:** within 10 days after determining the breach (Fla. Stat. 501.171(6)). Customers decide their own notices to individuals and regulators | Chief Privacy Officer |
| 7.4.4 | If the company's own personal information was affected (for example, the engineer's or other staff records), apply each state's law for residents. **Florida worked example:** individuals within 30 days (15-day extension on good cause, individual notice only); Department of Legal Affairs within 30 days if 500 or more Floridians; consumer reporting agencies if more than 1,000 | General Counsel |

### 7.5 All other customers
- Customer advisory within 72 hours of confirmation to each affected customer's security contact, with indicators of compromise, affected resources, and safe actions; then updates at least daily (customer agreement).
- Status page and its machine-readable feed updated for service impact (CDS-CSO-AVR). SLA credits computed after the month ends.

### 7.6 Law enforcement, CISA, and extortion
- Report to the FBI and CISA as early as practical (voluntary). CIRCIA is not in force (no final rule as of 2026-09-25).
- If an extortion demand follows: no payment without the Chief Executive Officer, the General Counsel, the insurer, and an OFAC sanctions check. Paying does not remove any notification or disclosure duty.

## 8. Recovery and customer trust (RC.RP, RC.CO)
1. Release path back in service only after the CISO and the Vice President, Software Supply Chain sign the readiness checklist: rebuilt runners, new approval workflow, signed approvals, automated halt, credential rotation, provenance verified.
2. Host security patches resume first; guest-agent releases resume only after the clean release reaches all affected VMs.
3. Agencies decide when their tenants re-enable the agent; the Senior Vice President, Government Cloud tracks each agency's decision.
4. Publish a post-incident report for customers (through the trust center for agencies) once counsel approves.

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days.
- Update the risk register (P01: R-001, R-027, R-026, R-018), the POA&M (P07), this runbook, STD-01.9, and the materiality worksheet.
- Evaluate whether the response changes require significant change notices to agencies (SCN-CSO-EVA).
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain incident records, materiality minutes, and notices for at least 6 years (POL-01 4.16), and DFARS media for at least 90 days from the report.
