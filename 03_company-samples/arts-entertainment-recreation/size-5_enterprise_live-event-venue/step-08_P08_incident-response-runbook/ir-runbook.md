# Incident Response Runbook: Ticketing Platform Breach Exposing Customer and Card Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded live entertainment company; 36 venues in 8 states; in-house ticketing platform for own events and about 340 client venues) |
| Tier / Vertical | Enterprise / Arts, Entertainment, and Recreation |
| Incident type | Ticketing platform breach: an e-skimming script on checkout pages (own brand or client templates) capturing card data, combined with a patron data export from the data warehouse using a stolen service account credential. Includes the **SEC materiality assessment**, card brand duties as merchant and as service provider, client notifications, and multi-state breach notification |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State and Client Notification Procedure; PRC-03.4 Card Data Found in Unexpected Places Procedure |
| Runbook owner | Director of Security Operations, with the Director of Payments and PCI Compliance (section 7) and the General Counsel (section 6) |
| Approved | Executive risk committee, 2026-09-10 (service provider and client notification path added under POAM-008) |
| Last tested | Enterprise tabletop 2025-10-21 (ransomware; **no card breach scenario; disclosure committee not tested on a service-provider incident**). Next: full tabletop with the disclosure committee on 2026-11-12 using this runbook (POAM-008) |
| Notification matrix | `notification-matrix.csv` (30 obligations: 9 card brand and contractual, 4 SEC, 8 state (1 generic plus 7 Florida worked example), and law enforcement, insurance, OFAC, SL-2, CIRCIA status, and 4 not-applicable rows) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO | Chief Technology Officer | Out-of-band group on company mobile phones |
| Payments and card brand lead | Director of Payments and PCI Compliance | Director of Payments Engineering | Direct mobile; acquirer merchant risk line |
| Client communications (SL-1) | President, Ticketing | Vice President, Client Success | Client security contact list (verified quarterly) |
| Crisis management team chair | Chief Operating Officer | President, Venue Operations | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Committee roster in the sealed incident binder |
| Breach and privacy decisions | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Outside breach counsel and forensics | Retained firms through counsel and the insurer panel. If Visa requires a PFI, a PCI Forensic Investigator that has not served the company (including as QSA) in the last 3 years | MSSP incident team | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | U.S. Secret Service field office (card data) or FBI | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, and the identity platform may be watched. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder.

## 1. Preparation checks (Identify / Protect)
- [ ] Payment page script inventory, integrity hashes, and tamper detection live on own-brand checkout **and all client templates (gap until POAM-002 closes)**
- [ ] Client security contact list verified this quarter; client notice templates ready (POAM-008)
- [ ] Acquirer merchant risk contact, processor contacts, and the tokenization provider's incident line in the binder
- [ ] Data warehouse service accounts on key-pair authentication with network policies and export alerts (**gap until POAM-005 closes**)
- [ ] Log retention: 1 year, 90 days searchable; edge provider and checkout logs in the SIEM (AU-11)
- [ ] Materiality playbook and Form 8-K templates current; disclosure committee roster current (POAM-008)
- [ ] Outside counsel's state breach law matrix updated in the last 12 months
- [ ] Forensic firm list screened for PFI eligibility (no QSA or other services in the last 3 years)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Payment page change or tamper alert (new or modified script, changed header) | Payment page change detection; content security policy reports | SOC opens a severity-1 case; capture the page and script; page the incident commander and the payments lead |
| Common point of purchase notice | Acquirer, processor, or a client's acquirer | **Declare at once.** Card brand clocks start at suspicion |
| Unusual data warehouse export (volume, new source address, service account at odd hours) | Warehouse query logs; SIEM | Disable the service account; preserve query history; open a case |
| Client reports fraud complaints or a changed checkout | Client security contact | Treat as severity 1 until scoped |
| Extortion message or leak-site post naming the company or a client | Email, threat intelligence, law enforcement, media | Declare; preserve; do not engage without counsel |
| Tag vendor or other vendor reports a compromise | Vendor notice (contract; Fla. Stat. 501.171(6) for agents) | Open a vendor incident case; check which templates load its scripts |

**Declare a severity-1 ticketing platform breach when** an unauthorized script or change is confirmed on any checkout page, card data is confirmed at risk, or a patron or client data export is confirmed.

**Record four times, separately:**
1. **Suspicion time** (card brands and contracts): the acquirer's 24-hour clock, Visa's 3-calendar-day clock, and the 72-hour client notice clock all start here.
2. **Determination time** (state law): the determination of a breach or reason to believe a breach occurred starts Florida's 30-day clocks and the 10-day third-party agent clock (Fla. Stat. 501.171(3), (4), (6)).
3. **Window of exposure** (card brands): when it is determined, Visa's 3-day clock for at-risk account numbers starts.
4. **Materiality determination time** (SEC): recorded by the disclosure committee (section 6). This starts the 4-business-day Form 8-K clock.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Do not delete the malicious script yet.** Capture the page, the script, and the tag container configuration with hashes; then block the script at the content security policy and the edge, and remove the tag container from checkout | SOC; Platform Engineering | Script blocked; evidence hashed |
| 2. If the checkout cannot be confirmed clean within 1 hour, switch affected templates to the hardened checkout (no client tag containers) or pause sales on those templates | President, Ticketing; Director of Platform Engineering | Clean checkout confirmed |
| 3. Disable the compromised warehouse service account; rotate all warehouse service credentials and client API keys used near the event | Director of Data Engineering; Identity team | Revocations logged |
| 4. Ask the edge provider, cloud providers, the tag vendor, and the warehouse provider to preserve logs and images (Visa WTDIC Section A.7) | Incident commander | Preservation requests sent |
| 5. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 6. Director of Payments and PCI Compliance notifies the acquirer (24 hours) and agrees how the Visa notice and at-risk account upload will be made | Director of Payments and PCI Compliance | Acquirer case number recorded |
| 7. Start the incident log (timeline, decisions, who, when; times in UTC) and the evidence register | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Window of exposure.** When the script first appeared and when it was blocked, for each template (edge logs, template change history, earlier captures, content security policy reports). Every checkout on an affected template in that window is at risk.
2. **Card data at risk.** The payment service and processors list the card numbers authorized on affected templates in the window, split by merchant (the company's own merchant account versus each client's merchant account). Skimmed data likely includes the security code, so it is personal information under Fla. Stat. 501.171(1)(g)1.a.(III).
3. **Patron data at risk.** From warehouse query history: which tables, fields, and rows were exported, and for which patrons. Patron contact and order data alone is usually not "personal information" under Florida's definition, but other states' definitions differ, and the warehouse holds approximate app check-in locations for about 2.3 million patrons; counsel must decide whether those are "information regarding an individual's geolocation" (501.171(1)(g)1.a.(VII)).
4. **Initial access.** For the script: tag vendor compromise, a stolen client user session, or a template change by a company account. For the export: where the service account password was stored (contractor laptops, per POAM-005). Check client user and workforce sign-in logs for the same actor.
5. **Integrity.** Check for changed prices, fees, bot defense settings, ticket transfers, and refunds made with stolen sessions (AI-001 and AI-002 settings are in scope).
6. **Business impact.** Finance and the BIA owners estimate impact with P05 values (for example about $2.0 million a day if client checkouts must pause, and about $4.9 million a day if the payment service stops). These estimates feed section 6.
7. **PAN in unexpected places.** If analysis finds card data anywhere outside the payment service, follow PRC-03.4 (PCI DSS 12.10.7).

## 5. Containment and eradication (RS.MI)
1. Keep the hardened checkout on every affected template until script authorization and tamper detection are live for that template (POAM-002).
2. Remove the compromised vendor's scripts from every page, not only checkout; suspend the vendor pending review.
3. Reset sessions for client users of affected clients; require MFA before they sign in again.
4. Rotate warehouse, API, and integration credentials; add network policies to all service accounts.
5. Confirm with forensics that no persistence remains in template configuration, the tag manager, or service accounts before closing containment.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5 and does not wait for the investigation to finish. The materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors. **It applies whether the incident hit the company's own checkout or client checkouts the company runs as a service provider.**

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 and 5 | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date and time and the reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay | General Counsel | Filing confirmation |
| 6.8 | Align the timing and content of client, patron, media, card brand, and investor communications with the filing; brief the audit committee and board risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; identify information not yet determined in the filing and amend when it becomes available (SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee (amendment tracking owner: General Counsel's disclosure team) | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost sales while checkouts are paused (P05 values); forensic, PFI, and notification costs; card brand assessments and fraud liability; client service credits and contract claims; insurance coverage and retention |
| Operational | Checkouts paused, on-sales rescheduled, client sales affected, gate entry or venue operations affected |
| Data | Number of cards and patrons, states of residence, data types (card data with security codes, contact data, geolocation), whether data was published or sold |
| Clients and partners | Number of client venues affected; client terminations; artist and promoter relations; Visa Global Registry listing and the next service provider ROC |
| Legal and regulatory | Card brand investigations; FTC or state attorney general inquiries (data security, fee and ticket practices); litigation exposure |
| Reputation and strategy | National media; patron trust in on-sales; effect on the ticketing service line's growth |

**Worked example of the clocks (fictional dates):** a payment page tamper alert fires on 37 client templates on Tuesday 2027-03-02 at 09:40, and the SOC confirms skimming code at 11:15. Suspicion at 09:40 starts the clocks: acquirer notice by Wednesday 2027-03-03 09:40; Visa notice by Friday 2027-03-05; client notices by Friday 2027-03-05 09:40 (72-hour contract term). On Wednesday 2027-03-03, analysis finds that a warehouse service account exported 9.2 million patron records on 2027-02-20. The committee convenes that day and determines materiality on Thursday 2027-03-04 at 16:00, so the Form 8-K is due by Wednesday 2027-03-10 (4 business days: March 5, 8, 9, and 10). Florida's 30-day clocks (individuals and the Department of Legal Affairs) run from the 2027-03-02 determination that skimmed card data with security codes was at risk, to Thursday 2027-04-01; individual notice may get 15 more days only on written good cause, and the Department notice gets none. For client checkouts, the company's 10-day third-party agent notice to each client (by 2027-03-12) is overtaken by the 72-hour contract term. Counsel must also decide each other state's deadlines from the same facts.

## 7. Card brand, client, and multi-state notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each legal obligation before notices go out. Card brand rules are applied through the acquirer; they are not law, but missing them brings non-compliance assessments.

| Step | Action | Owner | Output |
|---|---|---|---|
| 7.1 | **Merchant role:** notify the acquirer within 24 hours of suspicion; make sure Visa is notified within 3 calendar days (WTDIC Section A.1) and receives the incident report within 3 calendar days after that (A.2), with PCI DSS status documents | Director of Payments and PCI Compliance | Acquirer and Visa case numbers |
| 7.2 | **Service provider role:** Visa's Section A applies to service providers too. Notify Visa about the service provider environment, and notify each affected client merchant within 72 hours so it can notify its own acquirer. Offer clients the at-risk card list for their merchant accounts | Director of Payments and PCI Compliance; President, Ticketing | Client notices logged |
| 7.3 | Upload at-risk account numbers within 3 calendar days of determining the window of exposure, through the acquirer or processors, split by merchant account (A.4) | Director of Payments Engineering | Upload confirmation |
| 7.4 | If Visa requires a PFI: contract within 5 business days, initial report within 5 business days of signing, final report within 10 business days of completion (A.5). The company's QSA firm is not eligible | Director of Payments and PCI Compliance; General Counsel | PFI engagement |
| 7.5 | Build the affected population: each individual, data elements, and **state of residence** (billing or account address). Separate (a) the company's own patrons (company is the covered entity), (b) client checkout buyers (client is the covered entity; company is the third-party agent), and (c) the warehouse export | Chief Privacy Officer; data team | Affected-individual file with state counts |
| 7.6 | Apply **each state's law** for every state with affected residents, using counsel's matrix: individual timelines, attorney general or regulator notices, consumer reporting agency thresholds, content rules, and third-party agent duties. Record the earliest deadline for each state | Outside counsel; General Counsel | State deadline table |
| 7.7 | **Florida worked example:** individuals within 30 days of determination (15 more days on written good cause); Department of Legal Affairs within 30 days if 500 or more Floridians (no extension); consumer reporting agencies if more than 1,000 are notified at once; as third-party agent, notify client venues within 10 days and give them what they need, or give the notices on their behalf if they ask (501.171(6)) | General Counsel | Florida filings |
| 7.8 | **Plan to the shortest clock** across card brands, contracts, every state, and the SEC. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 7.9 | Honor any law enforcement delay request (Fla. Stat. 501.171(4)(b) and matching state provisions); document it | General Counsel | Delay record |
| 7.10 | Engage the mail and email vendor, call center, and credit or card monitoring services where appropriate | Chief Privacy Officer | Vendors active |
| 7.11 | Notify the insurer, SL-2 owners if their systems or data are involved, and other contractual parties | Contract owners | Contract notices logged |

**Extortion demand:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.9). Report to law enforcement; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove notification or disclosure duties.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), keeping on-sales paused until checkout integrity is proven:
1. Hardened checkout on all affected templates; script allow-list and tamper detection verified on each before it reopens
2. Payment service health confirmed with processors; reconcile authorizations during the window
3. Client console access restored with MFA for affected clients
4. Warehouse access restored only for service accounts with key-pair authentication and network policies
5. Rescheduled on-sales announced with the artist and client, with bot protection on (AI-002)
6. Patron and client communications: what happened, what to watch for, and how to reach the call center (RC.CO)

**Validate before reopening:** no unauthorized scripts on any template, credentials rotated, monitoring alerts tested, and forensics sign-off on containment.

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- Update the risk register (P01: R-001, R-003, R-005, R-018, R-020, R-064), the POA&M (P07), this runbook, the materiality playbook, and the client responsibility matrix (PCI DSS 12.9).
- Expect the acquirer and Visa to ask for evidence of remediation and possibly an early PCI DSS validation; budget for it.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including materiality minutes, card brand correspondence, and breach assessments, as counsel directs, and no less than POL-01 4.11 requires.
