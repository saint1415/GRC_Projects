# Incident Response Runbook: POS and Reservation System Compromise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded hotel franchisor, manager, and owner: 750 hotels in 33 states and DC; 110 company-operated) |
| Tier / Vertical | Enterprise / Accommodation and Food Services |
| Incident type | Compromise of point-of-sale and reservation systems through a vendor remote access tool: an attacker uses the legacy POS vendor's remote tool to reach legacy POS servers, pushes memory-scraping malware to outlet workstations, and steals hotel staff sessions to export reservations and display virtual card numbers in the brand PMS. Includes the **SEC materiality assessment and Form 8-K Item 1.05** step, the card brand and acquirer track (as merchant and as service provider), franchisee and owner notices, and a multi-state breach notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); PCI DSS v4.0.1 Requirement 12.10 (incident response plan) |
| Policy basis | POL-03 Incident Response Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Franchise Incident Coordination Procedure; STD-03.2 Breach and Card Brand Notification Standard |
| Runbook owner | Director of Security Operations, with the Director of Payments and PCI Compliance for section 6 and the General Counsel for sections 7 and 8 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Enterprise tabletop 2026-03-24 (technical response and card brand track; **the disclosure committee did not take part**, and no scenario started at a franchised hotel). Next: full tabletop with the disclosure committee, including the franchise track, on 2026-11-12 (POAM-014); exercise with 3 franchisees by 2027-01-31 (R-060) |
| Notification matrix | `notification-matrix.csv` (35 obligations: 9 card brand and payments, 4 franchise, owner, and client contract rows, 4 generic state, 7 Florida worked example, 6 SEC and securities, plus OFAC, law enforcement, CIRCIA status, insurance, and federal contract rows) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Executive incident lead | CISO | CIO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Executive Vice President, Hotel Operations | Crisis line |
| Card brand and acquirer lead | Director of Payments and PCI Compliance | Payments Platform Engineering Manager | Acquirer risk lines and Visa contacts in the sealed incident binder |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| Breach and privacy decisions | Chief Privacy Officer | Deputy General Counsel | Direct mobile |
| Franchise coordination | Director of Franchise Technology Compliance | Vice President, Franchise Technology Services | Franchise incident line; franchisee contact list in the franchise portal (printed copy in the binder) |
| Owner relations (managed hotels) | Executive Vice President, Hotel Operations | Regional vice presidents of operations | Owner contact list in the binder |
| Outside breach counsel, forensics, and PFI | Retained firms engaged through counsel; a PCI Forensic Investigator from the PCI SSC list if a card brand requires one | MSSP incident team | Retainer hotlines |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the binder |
| Hotel operations | Executive Vice President, Hotel Operations; hotel general managers | Hotel managers on duty | Crisis line; hotel phone tree |
| Vendors | Legacy POS vendor, cloud POS vendor, PMS vendor, payment gateway, P2PE solution provider | Account managers | Numbers in the binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | U.S. Secret Service field office (named in the Visa WTDIC) | FBI field office or IC3 | Numbers in the binder |

**Out-of-band first.** Assume email, chat, and hotel back office PCs may be compromised. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder at headquarters, the regional offices, and every company-operated hotel.

## 1. Preparation checks (Identify / Protect)
- [ ] All vendor remote access through the PAM vendor gateway. **Gap until POAM-005 closes:** 5 vendors still use their own tools at 37 hotels; at 11 of them the tools were found enabled outside approved windows
- [ ] EDR on all hotel endpoints. **Gap until POAM-001 closes:** legacy POS workstations at 41 hotels have no EDR
- [ ] SIEM receives logs from all PPP components. **Gap until POAM-011 closes:** legacy POS servers and the 9 resorts' seller systems log locally only; logs retained 12 months online (AU-11)
- [ ] Immutable backups of the vault and PPP configuration restore-tested within the last 90 days (CP-9, CP-4)
- [ ] Break-glass accounts sealed and tested this quarter
- [ ] Current payment device lists and legacy POS server lists for every hotel (**gap until POAM-013 closes**)
- [ ] Materiality playbook, 8-K templates, and disclosure committee roster current (**gap until POAM-014 closes**)
- [ ] Card brand contacts, acquirer contract notice terms, and the PCI SSC PFI list in the binder; the current QSA firm is **not** eligible as PFI (Visa WTDIC A.5.3)
- [ ] Franchisee, owner, and SL-2 client contact lists exported from the franchise portal this quarter
- [ ] Outside counsel's state breach law matrix updated in the last 12 months
- [ ] Downtime procedures at hotels: paper checks and room charges at outlets, P2PE front desk terminals, printed PMS downtime reports (P05)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Vendor remote tool session at a hotel outside an approved window, or from an unusual source | Hotel firewall logs; SOC network detection; hotel staff report | Block the tool at that hotel's firewall; open a severity-1 case; check the other 36 hotels |
| New service, scheduled task, or unsigned binary on a legacy POS server or workstation | Local POS reports; vendor alerts; FIM on cloud components | Isolate the POS segment (do not power off); open a case |
| Acquirer or card brand reports the company or a managed hotel as a common point of purchase | Acquirer letter or call to the Director of Payments and PCI Compliance | Declare. **Record the time as the start of the Visa 3-day clock** |
| Bulk reservation export, unusual card display, or detokenization spike from one PMS account | PMS audit logs; tokenization service alerts; SOC analytics | Revoke the account's sessions; open a case |
| Stolen PMS session token or sign-in from a new device and country | Identity platform; SOC | Revoke sessions; force re-authentication for the hotel |
| A franchisee reports a suspected compromise under BS-TECH-06 | Franchise incident line | Open a franchise-track case (section 8.4); assess brand system exposure within 4 hours |
| Card data offered for sale or a leak-site post naming the brand | Threat intelligence; law enforcement; media | Declare; preserve; do not engage without counsel |

**Declare a severity-1 card compromise** when there is evidence sufficient to raise a reasonable suspicion that card data, or a payment system the company operates for itself, for owners, or for franchisees, was accessed without authorization. Visa's clock starts at suspicion, not at confirmation (WTDIC A.1.1).

**Record four times separately in the incident log:**
1. **Suspicion time** (card brands): evidence sufficient to raise a reasonable suspicion of a compromise. Starts the Visa 3-day notification clock.
2. **Determination time** (state law): when the company determines a breach occurred or has reason to believe one occurred. Starts Florida's 30-day clocks and similar state clocks. Counsel records this decision.
3. **Third-party agent determination** (franchisees and SL-2 clients): when the company determines a breach of a system it maintains for them. Starts the Florida 10-day agent notice (501.171(6)(a)) where counsel concludes the company acted as their third-party agent.
4. **Materiality determination time** (SEC): recorded by the disclosure committee (section 7). Starts the 4-business-day Form 8-K clock.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Block the vendor remote tool at the hotel firewalls of all 37 hotels where vendors use their own tools; disable standing vendor accounts | Director of Network Engineering; SOC | Blocks confirmed |
| 2. Isolate affected legacy POS segments at the network level. **Do not power off, reboot, or sign in to compromised servers or workstations with administrator credentials** (Visa WTDIC A.7.1.1, A.7.1.2) | Network Engineering with the POS Operations Manager | Segments isolated; devices labeled |
| 3. Move affected outlets to the fallback: paper checks and room charges; no keyed card entry; no card numbers on paper. Cloud POS outlets keep trading if P2PE device integrity is confirmed | Hotel general managers; Vice President, Food and Beverage | Fallback running |
| 4. Revoke PMS sessions for affected hotels; force re-authentication; remove the full card display permission tenant-wide except the payments team; rotate the PMS payment interface credentials | PMS Tenant Administration Manager; Payments Platform Engineering Manager | Revocations logged |
| 5. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Engagement letters; claim number |
| 6. Director of Payments and PCI Compliance notifies the acquirer (contract term; section 6) and opens the card brand log | Director of Payments and PCI Compliance | Acquirer case number |
| 7. Ask the legacy POS vendor, PMS vendor, gateway, and cloud providers to preserve logs and images (WTDIC A.7.1.6) | Director of Security Operations | Written requests sent |
| 8. COO activates the crisis management team; hotels switch to downtime procedures as systems are isolated | Chief Operating Officer | Crisis team convened |
| 9. Start the incident log (timeline in UTC, decisions, who, when) and the evidence register | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Initial access:** confirm how the vendor tool was used: stolen vendor credentials, a compromise of the vendor itself, or a tool left enabled outside a window. Ask the vendor for its own logs and whether other customers are affected (it may be the common source).
2. **Scope:** hotels, legacy POS servers and workstations, back office PCs at the 9 hotels where POS shares a segment with them, PMS accounts, and any route toward the managed network hubs or the CRS integration tier. Collect legacy POS logs locally at each hotel, because they are not in the SIEM (POAM-011).
3. **Window of exposure:** first and last date card data could have been captured at each outlet, and the date range of PMS exports. Needed for Visa (WTDIC A.4.1) and for state notices.
4. **Card data at risk:** card numbers captured from legacy POS memory (track data), virtual card numbers displayed in the PMS, and card numbers in group sales and events mailboxes if those were reachable (POAM-006). Confirm that the vault, tokenization service, and P2PE devices were not affected; if they were, the service provider track widens to all franchisees and SL-2 clients.
5. **Guest data at risk:** reservation exports (names, contact details, stay history) and **identity document numbers** captured at check-in. This drives the state law analysis in section 8.
6. **Whose data:** split the affected population by hotel type, because duties differ: (a) owned and leased hotels (company is the merchant and the business that holds the data); (b) managed hotels (owners' merchant accounts, company operates the systems); (c) franchised hotels (franchisee is the merchant; company operates the PMS tenant and the CRS); (d) SL-2 distribution clients.
7. **Evidence:** forensic images, memory captures, firewall and PMS logs, the vendor tool's logs; chain of custody in the evidence register; hashes recorded. If a PFI is required, give it full access (WTDIC A.5.1.2).
8. **Business impact:** Finance estimates impact using P05 values (for example, about $0.9 million a day if food and beverage outlets fall back to manual operation across many hotels; about $3.1 million a day if tokenization or payment authorization stops). These feed section 7.

## 5. Containment and eradication (RS.MI)
1. Keep the vendor tools blocked at all 37 hotels; restore vendor support only through the PAM vendor gateway (this finishes POAM-005 early).
2. Rebuild affected legacy POS workstations and servers from vendor media under change control; do not clean and reuse them. Where replacement hardware for the cloud POS is ready, cut the outlet over instead of rebuilding (POAM-001).
3. Change every credential the attacker could have reached: legacy POS service accounts and any remaining vendor defaults (POAM-010), PMS accounts at affected hotels, back office domain accounts at the 9 hotels, and interface credentials (POS to PMS, PMS to lock).
4. Isolate legacy POS from back office PCs at the 9 hotels before reconnecting.
5. Confirm with forensics (or the PFI) that persistence is removed before each hotel is reconnected. Keep the gateway informed so it can watch for unusual authorization patterns.

## 6. Card brand, acquirer, and service provider track (RS.CO)
The company is both a **merchant** (owned and leased hotels) and a **service provider** (the CRS card vault, PMS tenant, and managed network it operates for franchisees and SL-2 clients). Managed hotels use their owners' merchant accounts, so their acquirers must be told through the owners.

| When | Action | Owner |
|---|---|---|
| Immediately on suspicion | Notify the acquirer of the company's merchant accounts (WTDIC A.3.1; acquirer agreement term, fictional: within 24 hours) and the gateway | Director of Payments and PCI Compliance |
| Same day | Notify owners of affected managed hotels so their acquirers are told (management agreement term, fictional: within 24 hours); the company prepares the notice for them | Executive Vice President, Hotel Operations |
| Within 3 calendar days of suspicion | Ensure the compromise is reported to Visa (WTDIC A.1.1), normally through the acquirer; American Express within 72 hours of discovery (DSOP Section 3); Mastercard and Discover per the acquirer's instructions | Director of Payments and PCI Compliance |
| Within 3 calendar days of notifying Visa | Incident report to Visa and the acquirer (WTDIC A.2.1, Attachment A), with containment steps and dates | Director of Payments and PCI Compliance; Director of Security Operations |
| Within 3 calendar days of discovering compromised accounts, a Visa request, or a window of exposure | At-risk account numbers to Visa through the acquirer (WTDIC A.4.1) | Director of Payments and PCI Compliance |
| Within 5 business days of a Visa PFI notice | Contract a PFI and tell Visa and the acquirer its name and lead investigator (A.5.1.1); preliminary report within 5 business days of contracting (A.5.1.3); final report within 10 business days of completing the investigation (A.5.1.4). The PFI must not have provided QSA or other services to the company in the past 3 years (A.5.3), which rules out the current QSA firm and the 2025 QSA firm | Director of Payments and PCI Compliance; General Counsel |
| If Visa requires an independent investigation instead | Contract a qualified investigator within 5 business days (A.6.1.1) | Director of Payments and PCI Compliance |
| If brand systems the company operates for franchisees are in scope | Notify affected franchisees and SL-2 clients so they can tell their own acquirers; give them the facts they need (section 8.4) | Director of Franchise Technology Compliance |

**Card brand reporting and legal notice run in parallel.** Neither replaces the other. The Visa clock will expire long before any state clock.

## 7. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 to 6. It does not wait for forensics to finish: the materiality determination must be made **without unreasonable delay after discovery** (Instruction 1 to Item 1.05), from the perspective of a reasonable investor, weighing quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 7.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4). Franchise-track incidents that touch brand systems are briefed the same way | CISO | Brief logged |
| 7.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 7.3 | **Special trading blackout** for committee members, responders with knowledge, and executives (POL-05 4.10) | General Counsel | Blackout notice sent |
| 7.4 | Committee reviews the materiality worksheet (below) with facts from sections 4 to 6 | Committee | Worksheet completed |
| 7.5 | **Materiality determination** recorded with the date, time, and reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 7.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations (Item 1.05(a)). Technical details about the response or vulnerabilities need not be disclosed (Instruction 4) | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 7.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination of a substantial risk to national security or public safety allows delay (Item 1.05(c)); any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 7.8 | If information required by Item 1.05(a) is not determined or not available at filing, say so in the filing and file an **amendment within 4 business days** after it is determined or becomes available (Instruction 2) | General Counsel | Amendment log |
| 7.9 | Align timing and content of guest, franchisee, owner, media, and investor communications with the filing; brief the audit committee and risk committee chairs before filing | Vice President, Corporate Communications; Vice President, Investor Relations; General Counsel | Messages approved |
| 7.10 | Reassess as facts change; carry lessons into the next Item 106 disclosure (17 CFR 229.106) | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Card brand assessments and fraud cost recovery claims; forensic, PFI, and legal costs; notification and call center costs; lost outlet and room revenue from P05 values; service credits to franchisees and owners; insurance coverage and retention |
| Operational | Hotels and outlets on fallback and for how long; whether the vault, CRS, or PMS tenant was affected (system-wide) or only legacy POS at some hotels |
| Data | Number of cards and guests; states of residence; identity document numbers; whether data was sold or published |
| Franchise and owners | Whether franchised hotels' guests or merchants are affected through brand systems; owner claims under management agreements; franchisee claims |
| Legal and regulatory | Expected FTC inquiry (the *Wyndham* pattern), state attorney general inquiries, card brand non-compliance assessments, litigation |
| Reputation and strategy | Media coverage; loyalty member trust; franchise sales and owner relationships |

**Worked example of the clocks (fictional dates):**
- **Monday 2027-02-08, 11:00.** The SOC declares a severity-1 incident after finding a legacy POS vendor tool session at 02:10 at one hotel and a new service on its POS server. This is the **suspicion time**. Visa must have the notice by **Thursday 2027-02-11**. The acquirer and the gateway are called the same day.
- **Tuesday 2027-02-09.** Visa is notified through the acquirer. The incident report is due by **Friday 2027-02-12**.
- **Wednesday 2027-02-10.** The disclosure committee convenes (within 48 hours).
- **Friday 2027-02-12, 15:00.** Forensics confirms memory-scraping malware at legacy outlets in 23 hotels and PMS exports with identity document numbers at 4 hotels. Counsel records the **determination** that a breach occurred, and the committee determines the incident is **material**. Monday 2027-02-15 is a federal holiday (Washington's Birthday), so the four business days are February 16, 17, 18, and 19: the **Form 8-K is due by Friday 2027-02-19**.
- **Florida.** Individual notices and the Department of Legal Affairs notice (if 500 or more Floridians) are due no later than 30 days after the determination: **Sunday 2027-03-14**. Counsel also decides whether "reason to believe a breach occurred" arose on 2027-02-08, which would move the date to 2027-03-10. Plan to the earlier date.
- **Franchisees.** If counsel concludes the company maintained the affected PMS data as a third-party agent for 2 franchised hotels, their notice is due no later than 10 days after the determination: **Monday 2027-02-22** (Fla. Stat. 501.171(6)(a)); the company's franchise agreements set a shorter contract term.

## 8. Breach notification workflow (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms each obligation before notices go out.

### 8.1 Steps
| Step | Action | Owner | Output |
|---|---|---|---|
| 8.1.1 | Breach assessment for each data set (POL-03 4.7): what was accessed or acquired, whose data, which states, and whether it meets each state's definition of personal information | Chief Privacy Officer with outside counsel | Signed assessment |
| 8.1.2 | Build the affected population from forensic results: each individual, data elements, and **state of residence** from the reservation or profile address. Separate the four groups in section 4 step 6 | Chief Privacy Officer; data team | Affected-individual file with state counts by group |
| 8.1.3 | Apply **each state's law** for every state with affected residents, using counsel's state matrix: individual deadlines, attorney general or regulator notices, consumer reporting agency thresholds, content rules, and substitute notice rules. Record the earliest deadline per state | Outside counsel; General Counsel | State deadline table |
| 8.1.4 | **Plan to the shortest clock** across card brands, every state, contracts, and the SEC. Publish one master calendar | Chief Privacy Officer | Master calendar |
| 8.1.5 | Honor any written law enforcement delay request and document it (Florida worked example: 501.171(4)(b)) | General Counsel | Delay record |
| 8.1.6 | Engage the mail vendor, call center, and any identity protection service; prepare the website notice if substitute notice is used | Chief Privacy Officer | Vendors active |
| 8.1.7 | Retain all breach records, including any no-harm determination (Florida: at least 5 years, 501.171(4)(c)) | Chief Privacy Officer | Records filed |

### 8.2 Florida worked example (Fla. Stat. 501.171)
- **Is it a breach of personal information?** Personal information includes a name with a driver license, passport, or similar identity document number (501.171(1)(g)1.a.(II)), and a name with a card number **in combination with any required security code** (1.a.(III)). The PMS exports with identity document numbers qualify. Whether track data scraped from POS memory meets the card-number element is a question for counsel; treat it as qualifying unless counsel decides otherwise.
- **Individuals:** as expeditiously as practicable and no later than 30 days after the determination of a breach or reason to believe a breach occurred (501.171(4)(a)). Notice must include the date or estimated date range, a description of the information, and a contact (501.171(4)(e)).
- **Department of Legal Affairs:** if 500 or more individuals in Florida are affected, no later than 30 days after the determination (501.171(3)(a)). The 15-day good-cause extension in 501.171(3)(a) applies only to the notice to individuals.
- **Consumer reporting agencies:** if more than 1,000 individuals are notified at one time, without unreasonable delay (501.171(5)).
- **Substitute notice:** allowed if direct notice would cost more than $250,000, if more than 500,000 people are affected, or if there is no mailing or email address; it requires a conspicuous website notice and print and broadcast media notice (501.171(4)(f)).
- **No federal regulator shortcut:** the deemed-compliance path in 501.171(4)(g) depends on a primary or functional federal regulator's notice rules; no such rule applies to the company's guest data, so Florida notices are given directly.

### 8.3 Other states
Most guests do not live in Florida. For each state of residence, apply that state's law: definitions of personal information, deadlines, attorney general or regulator notices, and consumer reporting agency thresholds differ. Counsel's matrix is the source; this runbook does not restate other states' rules.

### 8.4 Franchisees, owners, and SL-2 clients
| Situation | What the company does | Owner |
|---|---|---|
| Brand systems the company operates (PMS tenant, CRS, managed network) exposed franchisees' guest or card data | Notify each affected franchisee and SL-2 client with the facts they need for their own notices; where counsel concludes the company is their third-party agent, notify within the state deadline (Florida worked example: no later than 10 days after determination, 501.171(6)(a)) and offer to send notices on their behalf (501.171(6)(b)) | Director of Franchise Technology Compliance; General Counsel |
| Managed hotels' systems (operated by the company under management agreements) | Notify owners under the management agreement term; the company normally sends guest notices for the owners | Executive Vice President, Hotel Operations; Chief Privacy Officer |
| The incident starts at a franchised hotel's own systems (franchisee network or terminals) | The franchisee is the merchant and gives its own card brand and legal notices. The company checks whether brand systems were reached through the franchisee (stolen PMS sessions, managed network), briefs the CISO and General Counsel so the disclosure committee hears of it (gap G-100), and coordinates messages under PRC-03.4 | Director of Franchise Technology Compliance |
| A vendor (legacy POS vendor, PMS vendor) is the source | Track the vendor's own notice to the company (Florida worked example: 10 days, 501.171(6)(a); contracts: 72 hours or 24 hours); the company still gives its own notices | Director of Third-Party Risk Management |

**Ransom or extortion:** no payment without approval from the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.8). Report to the U.S. Secret Service or FBI. Paying does not remove card brand, state, or SEC duties.

## 9. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), validating each step:
1. Identity platform and break-glass access
2. Network hubs, SD-WAN, DNS, and cloud connectivity (verify no attacker route from hotel segments to the CRS integration tier)
3. Security tooling (EDR console, SIEM) for clean-room validation
4. Tokenization service, card vault, and gateway connectivity (if touched: key rotation and token review with the gateway)
5. CRS, booking engine, and channel connections
6. Door lock servers and key encoders (rotate the PMS-to-lock interface credential)
7. PMS tenant access for affected hotels with re-enrolled MFA; card display permission restored only to approved roles
8. Contact center and tone-masking service
9. POS: cloud POS outlets first; legacy POS outlets hotel by hotel after rebuild and forensic clearance, or cut over to cloud POS with P2PE
10. Franchise technology services help desk and SL-2 client access, with status updates to franchisees and clients
11. Resorts on the seller's systems (coordinate with the seller under the transition services agreement)
12. Loyalty platform, website, and app; then the remaining Moderate and Low processes

**Validate before reconnecting:** no persistence, credentials changed, systems patched, logs flowing to the SIEM (or collected locally with SOC review), and the acquirer's agreement before the affected outlets accept cards again. Tell guests, franchisees, owners, and staff when services return (RC.CO).

## 10. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days of closing (POL-03 4.11).
- Update the risk register (P01: R-001, R-003, R-005, R-006, R-015, R-060), the POA&M (P07), this runbook, and the materiality playbook.
- Expect card brand non-compliance assessments, a new PCI DSS validation possibly required by the acquirer, and a possible FTC inquiry; keep the evidence binder from P03 section 7 current.
- The disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all records, including materiality minutes, breach assessments, and card brand correspondence, for at least 7 years (POL-01 4.11).
