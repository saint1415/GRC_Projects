# Incident Response Runbook: Ransomware Disrupting Production of Grid Equipment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded power and distribution transformer manufacturer; 7 plants in FL, GA, TN, TX, NC, and OH) |
| Tier / Vertical | Enterprise / Critical Manufacturing |
| Incident type | Ransomware that encrypts enterprise IT (ERP and APS, MES application tier, file and PLM services, field laptops) and reaches plant OT at one or more plants, stopping production of grid equipment, with possible theft of employee personal information and designs. Includes the SEC materiality assessment, the crisis management team, utility addendum notices, and multi-state employee breach notification |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 section 6.4 |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Plant Safe-State and Manual Operations Procedure |
| Runbook owner | Director of Security Operations (incident commander), with the Director of OT Security for the OT sections and the General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-08 |
| Last tested | Enterprise tabletop 2026-03-24 (IT ransomware with an employee data breach; the OT-capable response firm took part; **no OT production scenario, and the disclosure committee exercised only the data breach case**). Next: OT ransomware tabletop with the full disclosure committee, plant managers, and two plant OEMs on 2026-11-18 (POAM-011) |
| Notification matrix | `notification-matrix.csv` (34 obligations: 6 utility addendum, 3 service line and customer contract, 4 federal contract, 5 SEC and disclosure, 4 generic state, 5 Florida worked example, plus OFAC, law enforcement, CIRCIA status, DFARS and Form DOE-417 non-applicability, insurance, and inbound supplier notice) |
| Risks addressed | P01 R-001 (Very High), R-002, R-003, R-011, R-016, R-018, R-031 |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company mobile phones) |
| OT incident lead | Director of OT Security, with the Vice President, Manufacturing Engineering | OT security engineer on call (after POAM-005, 24x7) | OT bridge; plant radio |
| Plant safety and restart decisions | Plant manager at each affected plant | Shift superintendent on duty | Plant radio; crisis line |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | COO | CIO | Crisis line |
| Crisis management team members | CIO, CISO, General Counsel, Chief Human Resources Officer, Vice President, Corporate Communications, Vice President, Manufacturing Engineering, affected plant managers | Designated alternates | Roster in the sealed incident binder |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Chief Accounting Officer, COO, CISO, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Contract and regulatory notices | Chief Compliance Officer (obligations register) | Director of Federal Programs (federal clauses) | Direct mobile; printed register in the binder |
| Product security and utility coordination | Director of Product Security (PSIRT) | Chief Technology Officer | PSIRT on-call line |
| Field access and STRS dispatch | Vice President, Spares and Services | Field service manager on duty | Crisis line |
| FMS subscribers | Vice President, Digital Services | FMS operations lead | Crisis line |
| Employee breach decisions | Chief Human Resources Officer with outside counsel | General Counsel | Direct mobile |
| Outside breach counsel, forensics, OT-capable response firm | Insurer panel firms, engaged through counsel | MSSP incident team | Carrier hotline; retainer numbers in the binder |
| Cyber insurer | Carrier breach hotline (called before any vendor is engaged) | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and the identity platform may be compromised. Use company mobile phones, the out-of-band conferencing service, and the printed incident binders kept at every plant office, the SOC, and the HQ crisis room.

## 1. Preparation checks (Identify / Protect)
- [ ] Immutable backups in separate backup accounts, restore-tested within the last 90 days for tier-1 systems; weekly offline copy at DC-2 (CP-9, CP-4)
- [ ] ERP failover can meet the 8-hour RTO. **Gap: 11 hours demonstrated until POAM-006 closes (2027-01-31)**
- [ ] Controller program backups automated at P1 to P6 and restore-tested at every plant. **Gap: tested at P1 and P5 only; AQ-01 manual (POAM-007)**
- [ ] Documented, tested isolation points: IT/OT boundary firewalls and OT DMZs at P1 to P6, the OT remote access gateway, the cloud interconnects, the historian replicas. **Gap at AQ-01: dual-homed MES, two-way trust, 5 cellular routers (POAM-004, POAM-008)**
- [ ] EDR on all IT endpoints and servers; SIEM receives logs from all tier-1 systems. **Gap: P3 and P4 MES logs and all AQ-01 systems (POAM-005)**
- [ ] OT alerts reach an engineer 24x7. **Gap until POAM-005 milestone 2026-11-15**
- [ ] Break-glass accounts sealed and tested this quarter (POL-02 4.11)
- [ ] Plant safe-state procedures (PRC-03.4) posted at every drying oven, vacuum oil system, and test laboratory; printed 5-day schedules refreshed daily during hurricane season
- [ ] Known-good TMU firmware images and their hashes held offline by the Director of Product Security; code signing key recovery procedure tested
- [ ] Obligations register printed monthly into the binders, with each utility's 24-hour or 48-hour term marked. **Gap: single 48-hour clock in templates until POAM-016 closes (2026-11-30)**
- [ ] Materiality playbook with the production-loss calculator (P05 values) and 8-K templates current; disclosure committee roster current. **Gap: calculator due 2026-10-31 (POAM-011)**
- [ ] Outside counsel, forensics, OT-capable firm, and insurer contacts confirmed this quarter; state breach law matrix from outside counsel updated in the last 12 months

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renames or encryption on servers, kiosks, or laptops | EDR; staff report; backup job failures | SOC opens a severity-1 case; isolate hosts through EDR; page the incident commander and the OT incident lead |
| HMI locked, showing a ransom note, or setpoints and recipes changing on their own | Operator; shift superintendent; OT monitoring | Operator steps back and calls the shift superintendent, who calls the plant manager and the OT on-call engineer. **Do not touch the controls** |
| MES kiosks stop across a bay, or work orders stop arriving | Shift superintendent; MES monitoring | Call the SOC; switch to paper travelers |
| New administrator accounts, backup deletions, or changes to immutability settings in a cloud account | Cloud audit logs; backup alerts; PAM | Revoke sessions; disable the account; open a severity-1 case |
| Unexpected session through the OT gateway, an OEM tool, or an AQ-01 cellular router | Gateway logs; OT monitoring; plant controls staff | OT lead terminates the session, powers off the AQ-01 router, and opens a case |
| Suspicious activity from the AQ-01 network or legacy directory | EDR; SD-WAN firewall logs; local IT | Treat as severity 1 until scoped; cut the AQ-01 SD-WAN tunnel and the domain trust if activity reaches enterprise systems |
| Extortion message or leak-site post naming the company | Email; threat intelligence; law enforcement; media | Declare; preserve; do not engage without counsel |
| A Tier 1 supplier reports an incident (TMU contract manufacturer, EDI provider, MSSP) | Supplier notice | Open a supplier incident case; start the inbound track in section 7 |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any production system, any plant controller or HMI shows unauthorized changes, or an extortion claim names company data. The incident commander declares; the OT incident lead declares for plant events.

**Record four times, separately, in the incident log:**
1. **Declaration time.** Starts the internal clocks: General Counsel brief within 24 hours and disclosure committee within 48 hours (POL-03 4.5).
2. **Confirmation that the incident relates to products or services supplied to utilities** (TMU firmware or configuration software, the code signing key or pipeline, field laptops or field access, FMS or STRS data). Starts the 24-hour (27 addenda) and 48-hour (61 addenda) utility notice clocks. The incident commander records it with the General Counsel.
3. **Determination of a breach of personal information** (or reason to believe one occurred). Starts the state clocks, including Florida's 30 days.
4. **Materiality determination time** (SEC), recorded later by the disclosure committee (section 6). Starts the 4-business-day Form 8-K clock.

## 3. First 4 hours: safety, isolation, and calls (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Safe state at every affected plant** (PRC-03.4). The plant manager decides for each area: drying ovens and vacuum oil processing continue under local PLC control with an operator at the panel if running normally, otherwise follow the safe-shutdown procedure; high-voltage test laboratories stop and de-energize; winding, core cutting, and robotic welding lines stop at the end of the current operation; crane lifts complete and park. Responders never override process safety systems (POL-03 4.4) | Plant managers; controls engineers; operators | Every area in a known safe state, logged with times |
| 2. **Isolate IT from OT.** Close the IT/OT boundary firewalls at all plants (deny all, including at plants not yet affected, unless the OT lead confirms the plant is clean and needs a named flow); disable the OT remote access gateway; cut the historian replica feeds to the enterprise data platform | Director of OT Security; Director of Network Engineering | No path between enterprise IT and any plant OT zone |
| 3. **Isolate AQ-01.** Cut the AQ-01 SD-WAN tunnel; disable the two-way domain trust; unplug the office interface of the dual-homed MES; power off the 5 OEM cellular routers | Vice President, Integration Management Office; OT lead | AQ-01 cut off from the enterprise and the internet |
| 4. **Contain IT.** Isolate affected hosts through EDR (do not power off, to keep memory); block attacker infrastructure; suspend the MSSP's and IT vendors' remote access | SOC; Network Engineering | Hosts contained; blocks confirmed |
| 5. **Protect identity and backups.** Revoke sessions and rotate credentials for privileged and service accounts involved; use break-glass accounts if SSO is affected; confirm backup accounts are untouched (immutability locks, no recent deletions) | Director of Identity and Access Management; Director of Cloud Platform Engineering | Revocations logged; backup integrity confirmed |
| 6. **Calls.** The CFO's team calls the carrier hotline (before any vendor is engaged); the CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics and the OT-capable firm under privilege | CFO; CISO; General Counsel | Claim number and engagement letters |
| 7. **Crisis management team.** The COO activates it; plants switch to paper travelers and printed schedules; new work order release is held; storm-restoration commitments are listed for the customer track | COO; plant managers; Vice President, Spares and Services | Manual operations running; storm order list ready |
| 8. **Start the incident log** (timeline, decisions, who, when; the four times in section 2) and the evidence register | Incident commander | Log open (paper if needed) |

## 4. Analysis (RS.AN)
1. **Scope.** Hosts, cloud accounts, identities, data stores, MES instances, and plant zones affected. Sources: EDR, SIEM, cloud audit logs, PAM records, OT monitoring sensors at P1 to P6, and a walk-down of every HMI and engineering workstation. For P3 and P4 MES and all AQ-01 systems, collect logs locally because they are not in the SIEM (POAM-005). Export identity and cloud logs before they roll over.
2. **Controllers.** Did the attacker reach PLCs, drives, or safety systems, or only HMIs and engineering workstations? Controls engineering compares controller programs and recipes with the automated backups (P1 to P6) or the latest manual copies (AQ-01). **No controller is trusted until checked.**
3. **Initial access.** Phishing, stolen credentials, an edge device exploit (R-048), a vendor remote tool or OEM path (R-008), the AQ-01 trust or routers (R-003, R-007), or a supplier. Check the AQ-01 paths first while POAM-004 is open.
4. **Evidence.** Forensics images hosts, uploads HMI and controller programs, and exports firewall, gateway, and router logs before any wipe; chain of custody in the evidence register; hashes recorded for each artifact (POL-03 4.12).
5. **Exfiltration.** What left, from which systems: employee and applicant personal information (HR, payroll, applicant tracking), transformer designs and customer substation drawings, FCI, utility asset health data (FMS), or STRS member data. Sources: egress logs, cloud storage access logs, data platform query logs, the attacker's claims and samples. **This drives section 7.**
6. **Products and customers.** Were the build pipeline, the code signing service, the download portal, or the TMU configuration software touched? Were field laptops or saved utility credentials exposed? **This decides whether the incident is "related to the products or services supplied" under the addenda (section 2, time 2).**
7. **Product integrity.** Were test data in the TDMS or local test stations altered, or were winding or core line recipes changed? The Corporate Director of Quality holds certified test reports for affected units until integrity is confirmed (R-039).
8. **Business impact.** Finance and the BIA owners estimate impact with P05 values and the production-loss calculator: shipments per production day by plant (P1 about $4.6M, P2 $3.9M, P3 $3.4M, P4 $2.0M, P5 $2.0M, AQ-01 $0.8M; P6 parts buffer about 5 production days), liquidated damages on late power transformers (typically 0.5% of contract value per week, capped at 10%), storm-restoration orders at risk, and recovery costs. These estimates feed section 6.

## 5. Containment and eradication (RS.MI)
1. Contain by segment: affected accounts, cloud accounts, plants, and the AQ-01 network.
2. Disable compromised accounts; reset all privileged credentials and service account secrets; rotate integration, EDI, and API keys; rotate shared HMI and test station passwords (POAM-012 list).
3. **Rebuild, do not decrypt and reuse.** IT servers and kiosks from standard images; cloud workloads from clean templates; HMIs and engineering workstations from OEM media with OEM support, then load verified project files. Unsupported operating systems (148 assets) may need OEM media or replacement units (R-006).
4. Patch or close the initial access path before reconnecting. At AQ-01, the MES comes back single-homed on the plant side only (POAM-004 design).
5. If the pipeline or signing key may be compromised: revoke the key in the hardware security module, freeze releases and downloads, and rebuild from the offline known-good images (addendum sec. 5).
6. Forensics and the OT-capable firm confirm that persistence is removed from IT, cloud, and OT before recovery starts in each zone.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.5). Any plant production stop caused by a cyber event is severity 1 | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below), with the production-loss calculator run on the facts from sections 4 and 5 | Committee; CFO | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date and time and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer (for example, the expected restart date of a plant) | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align the timing and content of utility, customer, employee, media, and investor communications with the filing; brief the audit committee and the board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Deferred or lost shipments from the P05 values (about $16.7 million of shipments per production day if every plant stops; $10.0 million if P1, P3, and P4 stop); liquidated damages on late power transformers; storm-restoration orders lost to competitors; recovery, forensic, and legal costs; ransom demand; insurance ($100 million tower, $10 million retention); effect on quarterly guidance, liquidity, and covenants |
| Operational | Plants down and expected restart dates; whether drying cycles on large power transformers must restart (2 to 5 days lost each); MES and ERP recovery against RTO; STRS dispatch and FMS advisory commitments |
| Customers and grid | Utilities with delayed units or storm orders; whether supplied firmware, the signing key, or field access was affected; addendum notices sent; any effect on utility operations |
| Data | Employee and applicant records taken and states affected; designs, customer drawings, FCI, or utility asset data taken or published |
| Safety | Any injury, near miss, or unsafe state linked to the incident |
| Legal and regulatory | Contract breach and liquidated damages exposure; state attorney general inquiries; federal contracting officer actions; litigation exposure |
| Reputation and strategy | Media coverage; utility or STRS member loss; analyst reaction; effect on the AQ-01 integration and future acquisitions |

**Worked example of the clocks (fictional dates):**
- **Monday 2027-02-01, 03:40:** severity 1 declared after MES kiosks at P1 and P3 and the ERP are encrypted; P1, P3, and P4 move to safe states and stop. The General Counsel is briefed at 07:00; the disclosure committee convenes at 16:00 the same day and issues the blackout.
- **Tuesday 2027-02-02, 10:00:** forensics confirms that 140 field laptops with the TMU configuration software and utility site credentials were encrypted. The incident is related to services supplied. Notices are due to the 27 utilities with 24-hour terms by **Wednesday 2027-02-03, 10:00** and to the 61 with 48-hour terms by **Thursday 2027-02-04, 10:00**. Access-revocation notices for the exposed field credentials are due within 1 business day, by the end of **Wednesday 2027-02-03**.
- **Wednesday 2027-02-03, 17:00:** with three plants expected to be down for about 6 production days (about $60 million of shipments deferred, plus liquidated damages on 14 late power transformers), the committee determines the incident is material. The Form 8-K is due by **Tuesday 2027-02-09** (4 business days: February 4, 5, 8, and 9).
- **Friday 2027-02-12:** forensics confirms that HR records of 3,100 current and former employees were taken (about 2,400 Florida residents). Florida's 30-day clocks (individuals and, because 500 or more Floridians are affected, the Department of Legal Affairs) run to **Sunday 2027-03-14**; counsel plans to the earlier business day. Other states' deadlines come from counsel's matrix. Counsel must also decide whether "reason to believe a breach occurred" arose earlier (for example, when the extortion message claimed HR data), which would move the dates forward.

## 7. Notifications: utilities, customers, government, and employees (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel or the General Counsel confirms each external notice before it goes out. The Chief Compliance Officer keeps one master calendar of every clock.

**7A. Utility addenda (88 utilities) and service line customers**
| Step | Action | Owner | Output |
|---|---|---|---|
| 7A.1 | Decide early whether the incident relates to supplied products or services (section 4 step 6). If in doubt, the General Counsel decides within 12 hours of the question being raised, so the 24-hour clock is not lost | General Counsel; incident commander | Decision logged (section 2, time 2) |
| 7A.2 | Pull each affected utility's term from the obligations register (24 or 48 hours) and use the matching template. **Until POAM-016 closes, check each addendum: the register still shows 48 hours for some 24-hour utilities, and the 12 AQ-01 contracts are not loaded** | Chief Compliance Officer | Notice list with deadlines |
| 7A.3 | Send incident notices to each utility's designated security contact by the method in its addendum | Chief Compliance Officer | Notices sent and logged |
| 7A.4 | Send access-revocation notices within 1 business day for every field representative whose credentials may be exposed or whose access should end | Vice President, Spares and Services | Notices logged against the 1-business-day clock |
| 7A.5 | Coordinate response with affected utilities: indicators, affected firmware versions, trusted releases, recovery steps (addendum sec. 2; P03 G-129) | Director of Product Security | Coordination log |
| 7A.6 | If a vulnerability in supplied firmware or software is found, disclose it within 30 days (escalate at day 20) | Director of Product Security | Advisory issued |
| 7A.7 | FMS subscribers and STRS members: data incident notice within 72 hours of confirmation; outage notices immediately; keep the 24-hour STRS dispatch decision through the manual dispatch line and high-severity FMS advisories by phone | Vice President, Digital Services; Vice President, Spares and Services | Notices and dispatch log |
| 7A.8 | Delivery-impact and force majeure notices to customers with delayed units, storm-restoration units first; if a hurricane watch covers a customer's service area, give realistic ship dates for its reserved storm units within 24 hours (business commitment) | COO; General Counsel | Customer notices logged |

**7B. Federal contracts (11 civilian contracts)**
- No cyber incident report is required under FAR 52.204-21; tell contracting officers about any delivery schedule impact under the contract terms.
- During rebuild, buy replacement equipment only from approved sources. If covered telecommunications or video surveillance equipment is identified, report within 1 business day (FAR 52.204-25(d)); a Kaspersky covered article within 3 business days (FAR 52.204-23(c)); a FASCSA-covered article within 3 business days (FAR 52.204-30(c)(4)); each with further information within 10 business days.
- No DFARS report (no DoD contracts) and no Form DOE-417 (the company is not an entity named in its instructions).

**7C. Multi-state employee breach notification**
| Step | Action | Owner | Output |
|---|---|---|---|
| 7C.1 | Build the affected population from forensic results: each individual, data elements, and **state of residence** (from HR address records). Separate employees, former employees, applicants, and dependents | Chief Human Resources Officer; data team | Affected-individual file with state counts |
| 7C.2 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: definitions of personal information, individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, and content rules. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 7C.3 | **Florida worked example:** individual notice within 30 days of determining the breach (15 more days only on written good cause to the Department); Department of Legal Affairs notice within 30 days if 500 or more Floridians; consumer reporting agencies if more than 1,000 are notified at once; a no-notice determination must be documented, kept 5 years, and sent to the Department within 30 days | General Counsel | Florida filings |
| 7C.4 | Honor any written law enforcement delay request under the state provisions; document it | General Counsel | Delay record |
| 7C.5 | **Plan to the shortest clock** across every state, the utility addenda, and the SEC. Publish one master calendar | Chief Compliance Officer | Master calendar |
| 7C.6 | Engage the mail vendor, call center, and credit monitoring provider through the insurer panel | Chief Human Resources Officer | Vendors active |
| 7C.7 | Track inbound vendor notices (payroll, benefits, applicant tracking) under state third-party agent laws such as Fla. Stat. 501.171(6) and Tier 1 supplier terms (72 hours) | Director of Third-Party Risk Management | Vendor notices logged |

**7D. Voluntary and other reports**
- Report to the FBI (field office or IC3) and CISA within 24 hours of declaration. This supports OFAC mitigation and sector threat sharing, and is the path CIRCIA would formalize. **No CIRCIA report is required**: the rule is proposed only.
- **Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.8). Paying does not remove any notice or disclosure duty.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first. **No plant equipment restarts until controls engineering has verified its programs and settings and the plant manager approves (POL-03 4.4).**
1. **Plant safe states and supervision:** drying ovens and vacuum oil processing at P2, P4, and P5 under verified programs, HMI supervision within 4 hours (BP-05)
2. Identity platform and break-glass access (1 hour)
3. Network core, SD-WAN, DNS; IT/OT boundary firewalls rebuilt deny-by-default and held closed (2 hours)
4. Security tooling (EDR console, SIEM, OT sensors) for validation (2 hours)
5. MES application tier and kiosks at P1 to P6, plant by plant after OT validation (4 hours; BP-03). Re-enter paper traveler confirmations
6. FMS on Cloud provider B (4 hours; BP-12), if affected
7. Obligations register and out-of-band communications (4 hours; BP-18)
8. ERP, APS, and integration platform (8-hour target; 11 hours demonstrated until POAM-006 closes). Reconcile orders, receipts, and shipments made on paper
9. STRS portal and spare registry (8 hours; BP-13); field service tools and crew dispatch (8 hours; BP-11)
10. Winding and core line HMIs at P1 and P3 (12 hours; BP-04); manual recipe entry from printed winding sheets with an engineering double-check until then
11. TDMS and test stations (24 hours; BP-07). The Corporate Director of Quality checks raw test data against station records before any certified test report is signed; retest where integrity is in doubt
12. Shipping, export screening, and EDI (24 hours; BP-10, BP-09). **No export ships without a screening record** (POL-04 4.5)
13. Firmware build pipeline and download portal (24 hours; BP-14), only after the signing key is confirmed safe or replaced; re-verify every release hash
14. AQ-01 legacy ERP and MES (24-hour target, untested; BP-17), MES single-homed
15. PLM and engineering compute cluster (48 hours; BP-08); payroll and timekeeping (48 hours; BP-15)
16. P6 component production systems and financial close (72 hours; BP-06, BP-16)

**Validate before reconnecting:** EDR clean, credentials rotated, patched, logging to the SIEM, and the OT-capable firm agrees each plant network is clean. Keep manual procedures until each process meets its RTO.

**Communicate restoration (RC.CO):** tell plants by shift, utilities and customers when production and deliveries resume (final addendum update to utilities that received notices), contracting officers, FMS subscribers and STRS members, and investors through the disclosure committee if an amended 8-K is needed.

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.11), including OEMs and affected utilities where they took part.
- Update the risk register (P01: R-001, R-002, R-003, R-011, R-016, R-031), the POA&M (P07), the BIA recovery times (P05), this runbook, and the materiality playbook.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain incident records, materiality minutes, notices, and evidence for at least 7 years (POL-01 4.12); export records for 5 years (15 CFR 762.6); DOE certification records as required by 10 CFR 429.71.
