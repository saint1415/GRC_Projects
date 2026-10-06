# Incident Response Runbook: Customer Device Data Exposure and Point-of-Sale Compromise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded national electronics and device repair chain; 1,120 stores in 44 states and DC) |
| Tier / Vertical | Enterprise / Other Services (except Public Administration) |
| Incident type | A combined incident at the acquired chain (AC) stores, through either or both branches: **(A) customer device data exposure:** theft of AC legacy ticket data that holds device passcodes and account passwords, or a workforce member copying content from customer devices; **(B) point-of-sale compromise:** memory-scraping malware on AC legacy POS PCs that captures card data in clear text. Includes the **SEC materiality assessment** and a multi-state notification workflow |
| Why this incident | P01 R-001 (Very High) and R-007 (High) share one entry path: the flat AC store networks reached through the legacy managed service provider's remote tool (R-004). The same playbook also covers core stores, where Branch B is far less likely because of P2PE |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Card Compromise Procedure |
| Runbook owner | Director of Security Operations, with the General Counsel for sections 6 and 7 and the Vice President, Payments for the card brand steps |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Technical exercise 2026-03 (STPP export by a phished account; **no card compromise, and the disclosure committee did not take part**). Next: full tabletop with the disclosure committee on 2026-11-12 (POAM-008) |
| Notification matrix | `notification-matrix.csv` (25 obligations: 6 contractual, 1 HIPAA business associate, 1 generic state, 6 Florida worked example, 4 SEC, OFAC, law enforcement, and 5 rows recording why other rules do not apply) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Senior Vice President, Store Operations | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Payments and card brands | Vice President, Payments (acquirer, processor, PFI coordination) | PCI Program Manager | Acquirer merchant risk contact in the binder |
| AC stores | Vice President, Integration Management Office | AC regional directors | Crisis line |
| Breach and privacy decisions | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Manufacturers and clients | Vice President, Manufacturer Programs; Vice President, Claims Fulfillment (SL-1); Vice President, Enterprise Services (SL-2) | Their deputies | Program and client contacts in the binder |
| Outside breach counsel and forensics | Retained firms (engaged through counsel and the insurer panel); a PCI Forensic Investigator if the acquirer requires one | MSSP incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline (CFO) | Broker | Policy card in the binder |
| Workforce matters (Branch A insider cases) | Chief Human Resources Officer with the Vice President, Asset Protection | General Counsel | Direct mobile |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3; U.S. Secret Service field office (card fraud) | Local police (insider theft) | Numbers in the binder |

**Out-of-band first.** Assume the AC legacy directory, email, and the legacy remote tool may be compromised. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder at each regional office and AC district office.
**Quiet first for insider cases.** Do not confront a workforce member or tell other staff until HR and counsel agree on the approach. Preserve evidence first.

## 1. Preparation checks (Identify / Protect)
- [ ] Contact lists include AC district managers and the AC legacy managed service provider (**gap until POAM-008 closes**)
- [ ] AC store managers briefed on the 24-hour acquirer and manufacturer notice terms (**gap until POAM-008 closes**)
- [ ] SIEM receives AC POS and legacy ticketing logs (**gap until POAM-012 closes**); until then, AC logs must be collected locally at each store
- [ ] EDR on AC POS PCs (**gap until POAM-001 interim controls close**)
- [ ] PFI shortlist and retainer confirmed with the acquirer; outside counsel, forensics, and insurer contacts confirmed this quarter
- [ ] Materiality playbook and 8-K templates current; disclosure committee roster current
- [ ] State breach law matrix from outside counsel updated in the last 12 months; BAA abstracts for SL-2 health care clients (**11 missing until POAM-022 closes**)
- [ ] Notice templates for customers, the Florida Department of Legal Affairs, manufacturers, and clients drafted with counsel

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Branch | Action |
|---|---|---|---|
| Acquirer or processor notice of a possible compromise (common point of purchase) | Vice President, Payments | B | Declare at once; the 24-hour acquirer clock may already be running |
| EDR or MSSP alert for memory-scraping or credential-dumping tools on a POS PC | MSSP, EDR (core and, after interim controls, AC) | B | Isolate the host through EDR; do not power it off; open a severity-1 case |
| Unusual sessions of the legacy remote support tool or new admin accounts at AC stores | MSSP VPN monitoring; AC managed service provider | A, B | Disable the tool account; cut the store's VPN to headquarters if activity spreads |
| Bulk export from the AC legacy ticketing service or the STPP; sign-in from an unknown location | Vendor alert; STPP bulk export alert (SI-4(12)) | A | Disable the account; preserve the vendor's logs; open a case |
| Customer reports account takeover after a repair, or that someone accessed their photos or messages | Contact center; store; social media | A | Log it; secure the ticket history and bench workstation; route to the SOC |
| Extortion message or leak-site post naming the company | Email, threat intelligence, law enforcement, media | A, B | Declare; preserve; do not engage without counsel |
| A vendor reports an incident affecting company data | Vendor notice (Fla. Stat. 501.171(6); contract) | A | Open a vendor incident case; start the third-party track in section 7 |

**Declare a severity-1 incident when** card data compromise is suspected at any store, customer credentials or passcodes may have left the company, or an extortion claim names company data.

**Record four times, separately:**
1. **Suspicion time** (contracts): starts the 24-hour acquirer and manufacturer clocks.
2. **Discovery time** (HIPAA business associate duty): the first day the breach was known, or by reasonable diligence would have been known, to any workforce member or agent, if SL-2 ePHI is involved (45 CFR 164.410(a)(2)).
3. **Determination time** (state law): the determination of a breach or reason to believe a breach occurred, which starts the Florida 30-day clocks (Fla. Stat. 501.171(3)(a), (4)(a)); counsel records it for each state.
4. **Materiality determination time** (SEC): recorded by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Isolate affected POS PCs and servers through EDR or by unplugging the network cable only; do not power them off or reimage (preserve memory for the PFI) | SOC; AC managed service provider under direction | Hosts contained |
| 2. Disable the legacy remote support tool for all AC stores; cut AC site VPNs to headquarters except the processor path; block attacker infrastructure | Director of Network Engineering | Blocks confirmed |
| 3. Reset AC legacy directory and legacy ticketing credentials; revoke sessions; enforce MFA where the vendor supports it | Director of Identity and Access Management | Revocations logged |
| 4. Switch affected AC stores to standalone legacy PIN pads or deferred payment; **do not** move them to core stores' P2PE until the PFI agrees | Vice President, Payments; Vice President, Integration Management Office | Payment mode confirmed |
| 5. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the CFO notifies the insurer | CISO; General Counsel; CFO | Claim number and engagement letters |
| 6. Start the contract clocks: acquirer notice (Branch B) and manufacturer notice (Branch A, for program customers) within 24 hours of suspicion | Vice President, Payments; Vice President, Manufacturer Programs | Notices sent or scheduled |
| 7. COO activates the crisis management team; affected stores use paper intake and release (P05 BP-16 workaround) | COO | Downtime procedures running |
| 8. Start the incident log (timeline, decisions, who, when) and the evidence register | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Scope, Branch B:** which AC stores, POS PCs, and dates; malware family and exfiltration path; number of cards captured. The PFI, if the acquirer requires one, leads card scope; the company's forensic firm leads everything else, and the two share findings through counsel.
2. **Scope, Branch A:** which tickets were exported or viewed (legacy vendor logs; request the detailed export now, because retention is short); how many held device passcodes, account passwords, or email and password pairs; which customers' devices were in custody at affected stores. For insider cases, which devices the person handled and whether copies were made.
3. **Entry path:** check the legacy remote support tool first while POAM-002 is open, then phishing of AC staff, then edge devices.
4. **Spread:** confirm the attacker did not reach core stores, the STPP, or SL-1 and SL-2 systems (SIEM, cloud audit logs, PAM). If SL-1 or SL-2 client data is affected, start the client tracks in section 7 at once.
5. **Personal information test** for each affected individual and state, with Florida as the worked example (501.171(1)(g)): email or user name with a password; name with a card number and any required security or access code; name with medical, biometric, or geolocation information (for example data on devices in custody). Device passcodes alone are not listed in the Florida statute, but they unlock everything else on a device; counsel decides.
6. **Good-faith test** (501.171(1)(a)) for insider cases: access during a documented repair test is good faith; browsing or copying is not.
7. **Business impact:** Finance estimates impact with P05 values (for example about $850,000 a day if all AC stores stop trading; card brand and PFI costs; notification and call center costs; possible loss of Manufacturer C authorization at AC stores). These estimates feed section 6.

## 5. Containment and eradication (RS.MI)
1. Contain by store: isolate affected AC stores from each other and from headquarters; keep only the processor path, through new firewall rules, if the PFI agrees.
2. Remove the legacy remote tool permanently (POAM-002); replace with PAM-brokered support.
3. Rebuild affected POS PCs from clean media or replace them; never reuse an infected PC. Deploy EDR before reconnecting.
4. Purge passcodes and passwords from the legacy ticketing service so the same data cannot be taken twice (POAM-004).
5. Where account passwords were exposed, contact affected customers promptly to change them, even before formal notice, as counsel advises.
6. Bring forward the P2PE conversion for affected stores if the acquirer and PFI agree (POAM-001).
7. Forensics confirms persistence is removed before recovery starts at each store.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 and 5, including the PFI's preliminary findings and any acquirer statements | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date and time, and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align timing and content of customer, manufacturer, client, media, and investor communications with the filing; brief the audit committee and the risk and technology committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost revenue at affected stores (P05 BP-16 about $850,000 a day for all AC stores); forensic and PFI costs; possible card brand assessments; notification, call center, and credit monitoring costs; insurance coverage and retention |
| Operational | Stores closed or on paper; whether the conversion schedule slips; effect on core stores |
| Data | Number of cards captured; number of customers with passcodes, account passwords, or email and password pairs exposed; states affected; whether data was published or sold |
| Legal, regulatory, and contractual | Acquirer and card brand actions, including any effect on validation; state attorney general inquiries; FTC exposure; manufacturer program status; SL-1 and SL-2 client contract breaches |
| Reputation and strategy | Media coverage; customer trust in leaving devices with the company; effect on the integration and future acquisitions |

**Worked example of the clocks (fictional dates):** on Monday 2027-01-11 at 08:30 the acquirer reports a common point of purchase pointing to 9 AC stores (suspicion; the company confirms receipt and sends its own notice the same day). Forensics finds memory-scraping malware on POS PCs at 23 AC stores and, on Wednesday 2027-01-13 at 14:00, evidence that about 410,000 legacy tickets were exported, about 21,000 with account passwords. The Manufacturer C notice is due by Thursday 2027-01-14 at 14:00 (24 hours from suspicion of a customer data incident). The committee determines materiality on Thursday 2027-01-14 at 17:00. **Monday 2027-01-18 is a federal holiday (Martin Luther King Jr. Day), so it is not a business day:** the Form 8-K is due by Thursday 2027-01-21 (business days January 15, 19, 20, and 21). Counsel records 2027-01-13 as the date the company had reason to believe a breach of email and password pairs occurred, so the Florida 30-day clocks for individuals and the Department run to Friday 2027-02-12. Other states' deadlines come from counsel's state matrix; the earliest one sets the plan.

## 7. Notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each legal obligation before notices go out.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | Contract notices within 24 hours of suspicion: acquirer (card data) and each manufacturer whose program customers or devices are involved; insurer | Vice President, Payments; Vice President, Manufacturer Programs; CFO | Notices logged with time sent |
| 7.2 | Follow acquirer and card brand instructions: engage a PFI if required, preserve and provide evidence, report on scope and containment | Vice President, Payments | PFI engagement; status reports |
| 7.3 | Build the affected population from forensic results: each individual, data elements, and **state of residence** (from the ticket address or store location). Separate: (a) the company's own customers and workforce; (b) SL-1 clients' customers; (c) SL-2 client records, including the 38 health care clients | Chief Privacy Officer; data team | Affected-individual file with state counts |
| 7.4 | **Client duties:** SL-1 clients within 48 hours of confirmation; SL-2 clients within 72 hours; as a third-party agent under state law, notify each client that is a covered entity no later than 10 days after determining the breach, with the information it needs (Florida worked example: 501.171(6)) | Vice President, Claims Fulfillment; Vice President, Enterprise Services | Client notices sent |
| 7.5 | **Business associate duty (SL-2 health care clients only):** notify each covered entity without unreasonable delay and no later than 60 days after discovery, or the shorter BAA term, with each affected individual where possible (45 CFR 164.410). The clients make the HIPAA notices to individuals, HHS, and media | Vice President, Enterprise Services; Chief Privacy Officer | BA notices sent |
| 7.6 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, content rules. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 7.7 | **Florida worked example:** individual notice within 30 days of the determination (15 more days on written good cause given to the Department); Department of Legal Affairs notice within 30 days if 500 or more Floridians (no extension); consumer reporting agencies if more than 1,000 are notified at once; a written no-notice determination kept 5 years and sent to the Department within 30 days if harm is not likely | General Counsel | Florida filings |
| 7.8 | **Plan to the shortest clock** across contracts, every state, HIPAA business associate duties, and the SEC. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 7.9 | Honor any law enforcement delay request in writing (Florida worked example: 501.171(4)(b)); document it | General Counsel | Delay record |
| 7.10 | Engage the mail vendor, a call center, and credit monitoring; prepare store and contact center scripts so staff give one consistent answer | Chief Privacy Officer; Vice President, Contact Center | Vendors active; scripts issued |
| 7.11 | Track inbound vendor notices (state third-party agent laws; contracts) if the incident started at a vendor such as the legacy managed service provider or the legacy ticketing vendor | Director of Third-Party Risk Management | Vendor notices logged |

**Extortion:** a demand to delete or not publish stolen ticket data requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.7). Report to the FBI or CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove notification or disclosure duties.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean state first:
1. Identity: new credentials for AC staff; break-glass access verified
2. Network: AC stores segmented; legacy remote tool removed; site VPNs limited to the processor path
3. Security tooling: EDR on AC POS PCs and bench PCs; local log collection until SIEM onboarding
4. Payments: rebuilt or replaced POS PCs only after PFI agreement; or early P2PE conversion
5. AC legacy ticketing access with named accounts and MFA, after the passcode purge
6. Manufacturer portal access with named accounts
7. Customer communications channels (contact center scripts, status messages)

**Validate before normal trading at each store:** EDR clean, credentials rotated, remote tool removed, legacy ticketing purged, PIN pads inspected and on the inventory, and the acquirer informed. Keep paper procedures until each store meets its RTO. Tell customers, manufacturers, and clients when service is normal (RC.CO-03); public statements come only from Corporate Communications after counsel approves (RC.CO-04).

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.10).
- Update the risk register (P01: R-001, R-004, R-007, R-009, R-013), the POA&M (P07), this runbook, and the materiality playbook.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Sanctions decisions for insider cases under POL-01 4.7, documented by HR, with manufacturer notice where a program requires it.
- Retain all records, including materiality determination minutes, breach determinations, and any no-notice determinations, for at least 6 years (POL-01 4.11).
