# Incident Response Runbook: Ransomware on Farm-Management and Irrigation Control Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded diversified precision-agriculture crop farm; FL, GA, SC, NC) |
| Tier / Vertical | Enterprise / Agriculture, Forestry, Fishing and Hunting |
| Incident type | Ransomware on the farm management and irrigation control systems during the strawberry freeze season, with theft of payroll and H-2A worker files (double extortion). Includes the OT safe-state step, the SEC materiality assessment, and the multi-state breach notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); NIST SP 800-82 Rev. 3 sections 6.4 and 6.5 for OT response and recovery |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Manual Irrigation and Freeze-Protection Procedure; PRC-03.4 Multi-State Breach Notification Procedure |
| Runbook owner | Director of Security Operations, with the Director of OT Security for sections 3 and 8 and the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise tabletop 2026-03-24 (IT ransomware; **no OT outage, and the disclosure committee did not take part**). Next: full tabletop with an OT outage and the disclosure committee on 2026-11-17 (POAM-012); cyber outage injection in the November freeze drills (POAM-022) |
| Notification matrix | `notification-matrix.csv` (32 obligations: 3 customer and client contract, 4 generic state, 6 Florida worked example, 6 SEC and insider trading, 5 operational records duties that continue during an outage, plus OFAC, law enforcement, CIRCIA status, cyber insurance, acquirer, Reportable Food Registry, FAA Part 107, and federal contract rows) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| OT incident lead | Director of OT Security | SCADA Engineering Manager | OT bridge; control center radio net |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Vice President, Irrigation and Water Resources | Crisis line |
| Field safety and manual operations | Regional Farm Directors (6) and Irrigation Control Center Managers (6) | Freeze crew leads | Control center radio net; satellite phones at each control center |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Chief Operating Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Breach and privacy decisions | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Food safety and traceability | Chief Food Safety and Quality Officer | Traceability Program Manager | Direct mobile |
| Workforce and H-2A | Chief Human Resources Officer; Director of H-2A and Labor Compliance | HR business partners | Direct mobile |
| Outside breach counsel and forensics (IT and OT) | Retained firms (engaged through counsel and the insurer panel) | MSSP incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Customers and growers | Vice President, Sales and Customer Operations; Vice President, Grower Services; Vice President, Digital Agronomy | Account managers | Customer contact sheet in the binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (for investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, the identity platform, and the FMIS may be unavailable or watched. Use company mobile phones, the out-of-band conferencing service, the control center radio net, and the printed incident binder at each regional office and control center.

## 1. Preparation checks (Identify / Protect)
- [ ] Immutable cloud backups in separate accounts, restore-tested within the last 90 days for tier-1 systems (CP-9, CP-4)
- [ ] SCADA configuration and PLC program library replicated hourly to DC-2, with offline copies; **SCADA master restore within the 6-hour RTO not yet shown (POAM-011)**
- [ ] AQ-01 farm servers in the enterprise backup service (**gap until POAM-017 closes**)
- [ ] EDR on all supported endpoints and servers; **31 legacy HMIs without EDR (POAM-014)**
- [ ] SIEM receives logs from all tier-1 systems, **except AQ-01 farm servers and the AQ-02 pivot cloud service (POAM-005)**
- [ ] OT vendors only through the OT remote access gateway, **except INT-4, INT-5, and 2 packing line vendors (POAM-004) and the AQ-02 pivot cloud service (POAM-002)**
- [ ] Break-glass accounts for the identity platform, cloud, and SCADA masters sealed and tested this quarter (POL-02 4.12)
- [ ] Regional manual irrigation and freeze-protection procedures (PRC-03.3) printed at each control center and freeze station; freeze crews rostered for every forecast freeze night; standalone alarm dialers tested
- [ ] Packing site downtime kits: pre-printed lot label stock, paper lot logs, and paper receiving logs at all 17 packing sites
- [ ] Paper tally cards and Produce Safety forms at every farm office; monthly FMIS exports by region
- [ ] Materiality playbook and Form 8-K templates current, disclosure committee roster current (**gap until POAM-012 closes**)
- [ ] Outside counsel, IT and OT forensics, and insurer contacts confirmed this quarter; state breach law matrix from outside counsel updated in the last 12 months

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renames or encryption on IT or OT hosts (SCADA servers, HMIs, historian) | EDR, operators, backup job failures | SOC opens a severity-1 case; isolate IT hosts through EDR; call the OT incident lead before touching any OT host |
| HMIs frozen or showing a ransom screen; SCADA loses communication with pump stations | Control center operators | Operators call the OT bridge; start section 3 safe-state steps at once |
| Unscheduled pump, pivot, or fertigation command, setpoint, or recipe change; PLC download outside a change window | OT monitoring, SCADA alarms, operators | Treat as severity 1 until scoped; stop fertigation and chemigation injection in the affected region |
| Remote session from an integrator tool outside the gateway (INT-4, INT-5) or unusual activity in the AQ-02 pivot cloud service | OT monitoring, firewall logs, R6 control center log review | Block the path at the OT firewall; call the integrator or vendor through known numbers |
| Large or unusual outbound transfer (payroll exports, file shares, warehouse) | Egress monitoring, DLP, cloud threat detection | Block destination; preserve logs; open a case |
| Suspicious activity from an AQ-01 farm office or legacy directory | Network detection, VPN logs, local IT report | Treat as severity 1 until scoped; cut the AQ-01 site links to enterprise systems |
| Extortion message or leak-site post naming the company or its workers | Email, threat intelligence, law enforcement, media | Declare; preserve; do not engage without counsel |
| Vendor reports ransomware affecting company systems or data (FMIS vendor, payroll provider, cold-chain monitoring SaaS) | Vendor notice | Open a vendor incident case; start the third-party track in section 7 |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any production IT or OT system, SCADA loses control of any region, or an extortion claim names company or worker data.

**Record three times, separately:**
1. **Declaration time:** starts the internal clocks (General Counsel brief within 4 hours, disclosure committee within 24 hours; POL-03 4.5) and the **24-hour customer notice** clock if the event could affect product safety, lot traceability, or committed volumes.
2. **Breach determination time** (state law): when the company determines a breach of personal information occurred, or has reason to believe one occurred. This starts the Florida 30-day clocks and similar clocks in other states.
3. **Materiality determination time** (SEC): recorded later by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.

## 3. First 4 hours: people and crops first, then containment (RS.MA, RS.MI)
**Safe state comes before containment in OT.** The aim is to keep water moving by hand where it is needed, keep chemicals out of the water, and keep workers safe, then isolate.

| Step | Who | Done when |
|---|---|---|
| 1. **OT safe state.** In every affected region: stop all fertigation and chemigation injection (injection pumps off at the skid, interlocks left in place); switch affected pump stations and pivots to local (Hand) control at the panel; take drip zones to their fail-safe state. Never bypass an interlock to restore service | Irrigation Control Center Managers; field technicians | Each region reports "safe state" on the radio net |
| 2. **Freeze night (December to February).** If a freeze is forecast, the Regional Farm Directors in R1, R3, and R4 activate the freeze-night staffing plan: two-person crews start freeze pump stations by hand from thermometer readings and standalone alarm dialers (PRC-03.3). Do not wait for SCADA | Regional Farm Directors; freeze crew leads | Crews at every freeze station before the trigger temperature |
| 3. Isolate affected IT hosts through EDR (do not power them off; preserve memory). For OT hosts, the OT incident lead decides: disconnect the control center from the OT DMZ at the OT firewall; isolate SCADA servers by network, not by shutdown, unless forensics and the SCADA Engineering Manager agree | SOC; Director of OT Security | Hosts and zones contained |
| 4. Cut external OT paths: block INT-4 and INT-5 tools and all non-gateway vendor access at the OT firewalls; disable the AQ-02 pivot cloud accounts and run AQ-02 pivots by hand; suspend all gateway sessions except approved responders | Director of OT Security; Director of Network Engineering | Blocks confirmed |
| 5. Revoke sessions and rotate credentials for privileged and service accounts involved; use break-glass accounts if SSO is affected | Director of Identity and Access Management | Revocations logged |
| 6. Confirm backups are untouched: cloud immutability locks; SCADA configuration and PLC program library offline copies at DC-2; packing site database replicas | Director of Cloud Platform Engineering; SCADA Engineering Manager | Backup integrity confirmed |
| 7. CISO briefs the CEO and the General Counsel within 4 hours; the General Counsel engages outside counsel, who retains IT and OT forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 8. COO activates the crisis management team. Packing sites switch to manual mode with pre-printed lot labels and paper lot logs; coolers to hourly manual temperature checks; harvest crews to paper tally; shipping to phone and email orders for the top 20 customers | COO; Vice President, Packing and Cold Chain; Regional Farm Directors | Downtime procedures running at every site |
| 9. Customer and grower track: if product safety, lot traceability, or committed volumes could be affected, notify retail and foodservice customers within 24 hours of declaration (contract); notify SL-2 growers whose lots are affected | Vice President, Sales and Customer Operations; Vice President, Grower Services | Notices logged |
| 10. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** IT hosts, OT hosts (SCADA masters, historian, HMIs, engineering workstations), cloud accounts, identities, and data stores affected. Use EDR, SIEM, OT monitoring, cloud audit logs, PAM and gateway records. For AQ-01 servers and the AQ-02 pivot service, collect logs locally, because they are not in the SIEM.
2. **Initial access:** phishing, stolen credentials, edge device exploit (including legacy AQ-01 firewalls), an integrator remote tool, or the AQ-02 pivot service. Check INT-4 and INT-5 paths and AQ-01 links first while POAM-004 and POAM-013 are open.
3. **Command integrity (OT):** before any region goes back to automatic control, the SCADA Engineering Manager compares every PLC program in the region with the approved library, checks setpoint and recipe limits, and has technicians re-verify fertigation interlocks on site. Stations without a trusted library copy (INT-4 and INT-5 stations until POAM-019 closes) are reloaded from the integrator's signed archive or rebuilt, and stay in manual until verified.
4. **Records integrity:** confirm Produce Safety, application, tally, and traceability records were not altered (FMIS audit trail, vendor integrity statement, comparison with exports). If integrity cannot be confirmed for a period, the Chief Food Safety and Quality Officer decides on lot holds and customer notices; the Director of H-2A and Labor Compliance rebuilds tally from paper cards for earnings statements.
5. **Evidence:** forensics images hosts and exports logs before they roll over; chain of custody is kept in the evidence register; hashes recorded for each artifact. OT forensics captures HMI and historian data without changing PLC state.
6. **Exfiltration:** determine what data left, from which systems, for which workers, growers, and customers. Sources: egress logs, file share and cloud storage access logs, warehouse query logs, the attacker's claims and samples. **This drives section 7.**
7. **Business impact:** Finance and the BIA owners estimate impact using P05 values: for example, up to $40 million for one unprotected freeze night on the 9,400 freeze-protected acres; about $11.0 million per day if packing stops in peak season; about $6.5 million per day of irrigation outage in a hot week. These estimates feed section 6.

## 5. Containment and eradication (RS.MI)
1. Contain by zone: isolate affected cloud accounts, sites, control centers, or the AQ-01 network. Keep each region's OT zone isolated from the OT DMZ until section 4 step 3 is complete for that region.
2. Disable compromised accounts; reset all privileged credentials, OT service account secrets, gateway credentials, and API keys (FMIS integration, EDI, payroll).
3. Rebuild IT and SCADA servers from known-good images; never decrypt and reuse encrypted hosts. Reimage HMIs and engineering workstations from the golden images before reconnecting.
4. Close the initial access path before reconnecting (for example, move INT-4 and INT-5 onto the gateway, or end the AQ-02 pivot cloud path).
5. Forensics confirms persistence is removed before recovery starts in each zone.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery of the incident (Instruction 1 to Item 1.05), from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors. Item 106 defines information systems to include physical infrastructure controlled by them, so an OT outage is in scope (17 CFR 229.106(a)).

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 4 hours of declaration (POL-03 4.5) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 24 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives (POL-05 4.9) | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 3 to 5, including the crop and harvest impact from the Regional Farm Directors | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date and time, and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer (for example, a freeze night lost, or a major customer suspending orders) | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination** (General Instruction B.1). Only a written U.S. Attorney General determination that disclosure poses a substantial risk to national security or public safety allows delay (Item 1.05(c)); any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | If required information is not determined or unavailable at filing, say so in the filing and file an amendment within 4 business days after it is determined or becomes available (Instruction 2 to Item 1.05) | General Counsel | Open-items list tracked |
| 6.9 | Align timing and content of worker, grower, customer, media, and investor communications with the filing; brief the audit committee and the board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.10 | Keep reassessing as facts change. Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Crop loss (freeze nights unprotected, heat stress days), lost or delayed packing and shipments from P05 values, customer penalties for missed ship windows, recovery and forensic costs, ransom demand, notification and credit monitoring costs, insurance coverage and retention, effect on liquidity and covenants |
| Operational | Regions and processes down and for how long; freeze protection or irrigation under manual control; packing sites in manual mode; harvest windows missed |
| Safety | Any worker injury, chemical exposure, or water source contamination linked to the incident; interlock or command integrity concerns |
| Data | Number of workers, growers, and customers affected and their states; data types (Social Security, passport, visa, bank account numbers); whether data was published |
| Food safety and traceability | Lots whose traceability or Produce Safety records cannot be confirmed; customer lot holds or rejections |
| Legal and regulatory | Expected state attorney general inquiries; Department of Labor questions on H-2A earnings statements; customer contract breaches with SL-1 and SL-2 clients; litigation exposure |
| Reputation and strategy | Media coverage; loss of a major retail customer; effect on grower services growth and acquisitions |

**Worked example of the clocks (fictional dates):** ransomware is discovered on Tuesday 2027-01-12 at 02:40, during a forecast freeze night in R1 and R3. Freeze crews start stations by hand from 03:00. The customer notice is due by 02:40 on Wednesday 2027-01-13. The committee convenes on Wednesday 2027-01-13 and determines materiality on Thursday 2027-01-14 at 17:00. The Form 8-K is due by **Thursday 2027-01-21**: the 4 business days are January 15, 19, 20, and 21, because Monday 2027-01-18 is a federal holiday when the SEC is closed. Forensics confirms on Monday 2027-01-25 that payroll and H-2A worker files were taken; the Florida 30-day clocks (individuals and the Department of Legal Affairs) run from that determination to **Wednesday 2027-02-24**. Counsel must also decide whether a "reason to believe a breach occurred" arose earlier, for example when the extortion note on 2027-01-12 claimed data theft, which would move the Florida dates forward to 2027-02-11.

## 7. Multi-state breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Breach determination: decide whether personal information (Social Security, passport, visa, and bank account numbers; names with those numbers; credentials) was accessed or acquired without authorization. Ransomware with confirmed exfiltration of payroll or H-2A files is treated as a breach unless forensics shows the files were not taken | Chief Privacy Officer; outside counsel | Signed determination with date and time |
| 7.2 | Build the affected population from forensic results: each individual, data elements, and **state of residence**. Separate groups: (a) year-round employees; (b) seasonal and H-2A workers, whose payroll address may be company housing in one state while the H-2A permanent address is in the home country (20 CFR 655.122(j)(1)); (c) contract growers (SL-1 and SL-2 client data); (d) produce box subscribers (Florida and Georgia; card data is with the processor) | Chief Privacy Officer; data team; Director of H-2A and Labor Compliance | Affected-individual file with counts by state and a list of workers with only a foreign address |
| 7.3 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, content rules, and law enforcement delays. Counsel decides how to treat H-2A workers with only a foreign permanent address (the company's practice is to notify them directly in English and Spanish, with the same content, even where no state law requires it) | Outside counsel; General Counsel | State deadline table |
| 7.4 | **Florida worked example:** individual notice no later than 30 days after the determination (15 more days only with good cause given in writing to the Department within 30 days); Department of Legal Affairs notice no later than 30 days if 500 or more Floridians are affected (no extension); consumer reporting agencies without unreasonable delay if more than 1,000 are notified at once | General Counsel | Florida filings |
| 7.5 | **Plan to the shortest clock** across every state, the customer contracts, and the SEC. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 7.6 | Honor any written law enforcement delay request under each state's law (Florida: 501.171(4)(b)); document it | General Counsel | Delay record |
| 7.7 | Engage the mail vendor, a bilingual call center, and the credit monitoring provider; deliver notices to seasonal workers through crew leads and company housing as well as by mail | Chief Privacy Officer; Chief Human Resources Officer | Vendors active |
| 7.8 | Notify contractual parties: retail and foodservice customers (24 hours), SL-1 and SL-2 growers per their agreements, the acquirer if the e-commerce vendor is involved, and the insurer | Contract owners | Contract notices logged |
| 7.9 | Track inbound vendor notices (state third-party agent laws such as Fla. Stat. 501.171(6)) if the incident started at a vendor (FMIS vendor, payroll provider) | Director of Third-Party Risk Management | Vendor notices logged |

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.8). Report to the FBI or CISA; OFAC's 2021 advisory treats full and timely reporting to law enforcement as a mitigating factor. Paying does not remove notification or disclosure duties, and it never shortens the OT verification in section 4 step 3.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Manual irrigation and freeze crews keep running (people first, not systems)
2. Identity platform and break-glass access
3. Network core, SD-WAN, OT DMZ firewalls, DNS
4. Security tooling (EDR console, SIEM, OT monitoring) for validation
5. Packing site systems, label printing, and the cold-chain alarm path
6. EDI, order management, and transport management
7. SCADA masters and regional control center HMIs, one region at a time, **only after section 4 step 3 verification** (RTO 6 hours; 9.5 hours demonstrated, POAM-011). Fertigation and chemigation stay off until interlocks are re-verified on site
8. FMIS access, tally, and Produce Safety records (vendor-hosted: obtain the vendor's integrity statement)
9. Traceability data service and SL-2 hub data
10. Drying controls and telematics
11. AQ-01 and AQ-02 systems (AQ-02 pivots stay in manual until the cloud service is secured or replaced)
12. SL-1 grower data platform (tell SL-1 clients the restoration status)
13. ERP and payroll (repeat the prior payroll if needed so H-2A earnings statements go out each payday)
14. Data warehouse, AI services, imagery pipeline, produce box

**Validate before reconnecting:** EDR clean (or allowlisting for legacy HMIs), credentials rotated, initial access closed, logging to the SIEM, PLC logic and interlocks verified. Keep manual procedures until each process meets its RTO. Tell workers, growers, and customers when services return (RC.CO).

**Records duties during the outage:** H-2A earnings statements still go out each payday (20 CFR 655.122(k)); Worker Protection Standard application information is still displayed within 24 hours of an application (40 CFR 170.311(b)(5)), from paper logs if needed; Produce Safety records must still be produced within 24 hours of an FDA request (21 CFR 112.166(a)).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.11).
- Update the risk register (P01: R-001, R-002, R-004, R-005, R-007, R-012, R-017), the POA&M (P07), this runbook, the regional freeze procedures, and the materiality playbook.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including the materiality determination minutes and breach determinations, for at least 6 years (POL-01 4.11).
