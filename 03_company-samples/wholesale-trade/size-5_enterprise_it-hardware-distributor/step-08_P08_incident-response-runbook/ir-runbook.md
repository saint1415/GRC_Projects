# Incident Response Runbook: Supplier Compromise Introducing Tampered or Counterfeit Products

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded IT hardware and software distributor; DoD prime contractor and subcontractor) |
| Tier / Vertical | Enterprise / Wholesale Trade |
| Incident type | A supplier (OEM partner, authorized distributor, drop-ship partner, broker, or contract manufacturer) is compromised or dishonest, and tampered, counterfeit, or covered (Section 889) products enter the company's stock or drop-ship flows and reach customers. Includes a compromised supplier account in the company's drop-ship portal, EDI, or email used to push substitutions or redirect payments. Adds an **SEC "cybersecurity incident" decision and materiality assessment** with a Form 8-K Item 1.05 step |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); supply chain practices from NIST SP 800-161 Rev. 1 |
| Policy basis | POL-03 Incident Response and Resilience Policy; POL-01 4.13 to 4.16 (supply chain); PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-State Breach Notification Procedure; PRC-03.4 Federal Incident and Covered Equipment Reporting Procedure |
| Runbook owner | Director of Security Operations (cyber track) with the Chief Supply Chain Officer (product track); General Counsel for sections 6 and 7 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Product-recall drill without the cyber and disclosure tracks, 2026-04. Full tabletop with the disclosure committee set for **2026-11-18** (POAM-014) |
| Notification matrix | `notification-matrix.csv` (29 obligations: 9 federal contract, 6 SEC and disclosure, 4 generic state, 4 Florida worked example, plus OFAC, law enforcement, CIRCIA status, insurance, reseller, and OEM rows) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander (cyber track) | Director of Security Operations | SOC manager on duty | SOC bridge (out-of-band conferencing on company phones) |
| Product lead (stock, suppliers, authentication) | Chief Supply Chain Officer | Director, Product Authentication Lab | Out-of-band group on company phones |
| Executive incident lead | CISO | CIO | Out-of-band group |
| Crisis management team chair | Chief Operating Officer | Vice President, Distribution Operations | Crisis line |
| Federal reporting lead (DIBNet, Section 889, Kaspersky, contracting officers, primes) | Director, Government Contracts | Two other medium assurance certificate holders in Federal Solutions | Direct mobile; offline reporting kit at FL-1 |
| CMMC impact | Director, CMMC Program Office; President, Federal Solutions (Affirming Official) | n/a | Direct mobile |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | CFO, Chief Accounting Officer, CISO, Chief Risk Officer, Vice President, Investor Relations; Chief Supply Chain Officer for product events; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| Privacy decisions | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Outside counsel and forensics | Breach counsel, government contracts counsel, and forensics firm (through the insurer panel) | n/a | Retainer hotline |
| Cyber insurer | Carrier hotline (call before engaging incident vendors) | Broker | Policy card in the binder |
| Customers | Vice President, E-commerce (resellers); President, Federal Solutions (DoD customers and primes) | Regional sales vice presidents | Account contact lists |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Out-of-band first.** If a supplier's account or a company mailbox may be compromised, do not use email, the drop-ship portal, or EDI messages to discuss the incident or to confirm anything with the supplier. Use phone numbers already on file in the vendor master, never numbers from a suspicious message.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at FL-1 and each distribution center: this runbook, contacts, the notification matrix, the supplier phone list, and the covered-manufacturer list
- [ ] At least 3 medium assurance certificate holders and a tested DIBNet sign-in on the offline reporting kit (drill 2026-04-15)
- [ ] Quarantine cages marked at every distribution center, with a "HOLD - DO NOT SHIP" status in the ERP and WMS that blocks picking and drop-ship release
- [ ] Serial numbers captured at shipment for network, security, and video products, and for every federal order
- [ ] Drop-ship substitutions screened before acceptance. **Gap until POAM-006 closes (2026-12-31)**
- [ ] Firmware hash library and automated serial validation. **Gap until POAM-005 closes (2027-03-31)**
- [ ] Materiality playbook includes the supplier-compromise decision tree. **Gap until POAM-014 closes (2026-12-15)**
- [ ] Logs from the drop-ship portal, EDI translator, and reseller platform retained 1 year online (AU-11)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Firmware hash or signature does not match the OEM value, or a device makes unexpected outbound connections | Product Authentication Lab; Federal Solutions lab; customer | Isolate the device (do not keep it powered on a production or enclave network); quarantine the lot; open a product incident and a SOC case |
| OEM serial validation fails, or the OEM says a serial was never sold into that channel | Receiving; buyers; OEM | Quarantine the lot; open a product incident |
| A drop-ship partner submits substitutions or ship-from changes that do not match its normal pattern, or from a new user | Drop-ship portal analytics; Government Contracts retro-screen | Hold the affected order lines; call the partner on the number on file |
| A SKU or substitute matches a covered manufacturer, including a rebranded or white-label unit | Section 889 screen; retro-screen; lab | Block the SKU on all federal orders; start the Section 889 clock (section 6) |
| A supplier says its systems or accounts were compromised | Supplier notice (SR-8 terms) | Open an incident; freeze purchase orders, drop-ship releases, and payments to the supplier |
| Bank-detail or ship-to change requests from a supplier or reseller that arrive by email | Controller; sales desk | Do not act; verify by call-back (POL-05 4.7); report to the SOC |
| A reseller reports odd device behavior or a suspected counterfeit | Customer service; RMA | Pull serial history; quarantine returns; open a product incident |

**Declare a severity-1 supplier compromise incident when** tampered, counterfeit, or covered products are confirmed in stock or shipped, or a supplier account in a company system (drop-ship portal, EDI, supplier portal) is confirmed to be used by an attacker.

**Record four times separately in the incident log:**
1. **Discovery of a cyber incident** affecting a covered contractor information system (DFARS 252.204-7012(c): 72 hours).
2. **Identification of covered equipment** (FAR 52.204-25(d): 1 business day) or a Kaspersky covered article (FAR 52.204-23(c): 3 business days).
3. **Determination of a personal information breach** (state laws; Florida 30 days).
4. **Materiality determination** (Form 8-K Item 1.05: 4 business days), recorded later by the disclosure committee.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Stop ship: hold every open order line and drop-ship release with the affected SKUs, lots, serials, or supplier in the ERP and WMS | Vice President, Distribution Operations | No affected item can be picked or released |
| 2. Quarantine affected stock at every distribution center; photograph packaging and labels; keep everything | Receiving leads | Stock counted and tagged |
| 3. Freeze purchase orders, drop-ship releases, payments, and bank-detail changes for the supplier; call the bank fraud desk if a payment went out | Chief Supply Chain Officer; Controller | Holds confirmed |
| 4. Disable the supplier's accounts in the drop-ship portal, supplier portal, and EDI partner profile; revoke API keys and sessions; preserve logs before they roll over | Director of Security Operations | Accounts disabled; logs exported |
| 5. Isolate any suspect device that touched a company network; if it touched the FSCE configuration lab, isolate the lab segment and start the DFARS track | SOC; Director, CMMC Program Office | Devices and segments isolated |
| 6. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number and engagement letters |
| 7. Pull the shipment history: which customers received the affected SKUs, lots, or serials, and **whether any went on a federal order** | Vice President, E-commerce; Director, Government Contracts | Affected shipment list |
| 8. Start the incident log and the evidence register (chain of custody for devices, packaging, emails, and exports) | Incident commander; Director, Product Authentication Lab | Log open |

## 4. Analysis (RS.AN)
1. **Product scope.** Every affected supplier, SKU, lot, serial, purchase order, drop-ship line, receipt, and shipment. Check whether the same supplier or account touched other SKUs in the last 12 months.
2. **Authenticity.** Send serials and photos to the OEM. For federal stock, the Product Authentication Lab or an OEM-approved test lab inspects, tests, and authenticates (DFARS 252.246-7008(b)(3)(ii)).
3. **Covered equipment.** Check the true manufacturer of every affected SKU and substitute against the FAR 52.204-25 covered manufacturers and the Kaspersky list, including rebranded units. Record who decided and when.
4. **Cyber scope.** Decide what happened in company systems:
   - Was a supplier account in the drop-ship portal, supplier portal, or EDI used by the attacker? (This is the key input to the SEC decision in section 6.)
   - Did a suspect device run on a company network, including the FSCE configuration lab?
   - Was company data exposed (pricing, reseller contacts, license registrants, FCI, CUI)?
5. **Business impact.** Finance estimates lost gross profit from held stock and blocked SKUs, recall and replacement costs, customer credits, and contract remedies, using P05 values (for example, about $1.36 million of gross profit per shipping day across the company).
6. **Evidence.** If the FSCE or CUI is involved, image the affected systems and keep monitoring data for at least 90 days after the DIBNet report (DFARS 252.204-7012(e)).

## 5. Containment and eradication (RS.MI)
1. Suspend the supplier on the approved supplier list; buy replacements only from the OEM or authorized sources (POL-01 4.13).
2. Block affected SKUs on all orders until the Chief Supply Chain Officer and the Director, Government Contracts release them in writing.
3. Keep suspect items. Do not return them to the supplier or scrap them until disposition instructions are received from the OEM, the contracting officer, or the prime (POL-01 4.16).
4. Reset any company accounts the attacker touched; remove mailbox rules, OAuth grants, and API keys; check for new forwarding rules.
5. Rebuild any workstation or lab device that connected to a suspect device from the standard image; for the FSCE, follow the enclave playbook and check CUI access logs.
6. Warn buyers, the Controller, and the sales desk about the supplier's lookalike domains and phone numbers.

## 6. SEC decision and materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish.

**Step A: Is it a "cybersecurity incident"?** 17 CFR 229.106(a) defines a cybersecurity incident as an unauthorized occurrence, or a series of related unauthorized occurrences, on or conducted through the registrant's information systems that jeopardizes the confidentiality, integrity, or availability of those systems or information in them. "Information systems" include electronic information resources owned **or used** by the registrant.

| Facts | Committee's working answer (confirmed with outside securities counsel) |
|---|---|
| An attacker used a supplier's account in the company's drop-ship portal, supplier portal, or EDI to submit substitutions or change orders | Likely a cybersecurity incident: the occurrence was conducted through company information systems and affected the integrity of order data |
| Tampered firmware ran on a company network or in the FSCE | Likely a cybersecurity incident |
| Counterfeit products arrived through normal purchasing, with no unauthorized activity in company systems | Likely not a cybersecurity incident; the committee still assesses disclosure under its general disclosure controls (for example, a product recall's effect on results) |
| Only the supplier's own systems were compromised | Likely not a cybersecurity incident for the company, unless company information in the supplier's systems was affected |

**Step B: Materiality.** If it is a cybersecurity incident, the committee determines materiality without unreasonable delay after discovery, from the perspective of a reasonable investor, using quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 6.2 | The disclosure committee (with the Chief Supply Chain Officer) convenes within 48 hours of declaration, records the Step A answer, and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet with facts from sections 4 and 5 | Committee | Worksheet completed |
| 6.5 | **Materiality determination** recorded with the date, time, and reasoning, whether material or not yet material; if not yet material, the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident and its material impact or reasonably likely material impact; leave out technical details that would impede response | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a U.S. Attorney General determination (national security or public safety) allows delay | General Counsel | Filing confirmation |
| 6.8 | Align customer, OEM, DoD, media, and investor messages with the filing; brief the audit committee and risk committee chairs before filing | Communications; Investor Relations; General Counsel | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed. Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples the committee considers |
|---|---|
| Quantitative | Value of affected stock and shipments; recall, replacement, and testing costs; customer credits; lost gross profit from blocked SKUs; contract remedies; insurance coverage and the $5 million retention |
| Federal business | DoD orders affected; Section 889 or DFARS 252.246-7008 reports; risk to CMMC status or contract eligibility; suspension or debarment exposure |
| Operational | Distribution centers and product lines on hold; OEM allocation or authorization at risk |
| Data | Pricing, personal information, FCI, or CUI exposed |
| Safety and mission | Tampered equipment in customer or DoD networks |
| Reputation and strategy | Media coverage; OEM or top-20 reseller reaction |

## 7. Federal, state, and customer notifications (RS.CO)
**Follow `notification-matrix.csv`.** The Director, Government Contracts owns every DoD, contracting officer, and prime notice; the Chief Privacy Officer owns personal information notices. Counsel confirms each notice before it goes out.

| What was found | Clock | Owner |
|---|---|---|
| A cyber incident affected the FSCE or other CUI (for example a tampered device on the configuration lab network) | DIBNet report within 72 hours of discovery; incident report number to the prime as soon as practicable; malware to DC3 as instructed; preserve images 90 days | Director, Government Contracts; Director of Security Operations |
| Covered telecommunications or video surveillance equipment identified in a federal delivery or in company systems during performance | Report within 1 business day of identification; further information within 10 business days of that report | Director, Government Contracts |
| A Kaspersky covered article identified | Report within 3 business days of identification; further information within 10 business days | Director, Government Contracts |
| A FASCSA covered article identified (only where FAR 52.204-30 is in the contract) | Report within 3 business days; further information within 10 business days | Director, Government Contracts |
| An electronic part on a DoD order came from outside the authorized sourcing order or cannot be confirmed new | Prompt written notice to the contracting officer (through the prime for subcontracts) | Director, Government Contracts |
| Suspect counterfeit items bought for a Government delivery, where FAR 52.246-26 is in the contract | Contracting officer notice and GIDEP report within 60 days | Director, Product Authentication Lab |
| Personal information exposed (for example reseller contacts through a compromised portal account) | Each state's law for affected residents; Florida: individuals and (if 500 or more) the Department of Legal Affairs within 30 days of determination | Chief Privacy Officer |
| Products shipped to resellers or customers | Contract notices with serial lists, hold or return instructions | Vice President, E-commerce; President, Federal Solutions |
| Only a supplier's own systems were compromised and no company system, CUI, covered equipment, or personal information is involved | No regulatory clock; insurer, OEM, and customer notices under contracts; voluntary IC3 report | Chief Supply Chain Officer |

**CMMC check.** If the FSCE was affected, the Director, CMMC Program Office assesses whether any SP 800-171 requirement is no longer met. A change in compliance affects whether the CMMC status is "current" (DFARS 252.204-7021(a)), and the Affirming Official must not sign the next affirmation until it is fixed.

**Plan to the shortest clock.** The 1-business-day Section 889 report usually falls due first. File what is known on time and follow up within 10 business days.

**Worked example of the clocks (fictional dates):**
- Monday 2027-03-01: a lab technician finds firmware hash mismatches on switches drop-shipped by an authorized distributor. Product incident opened.
- Wednesday 2027-03-03 09:00: forensics confirms an attacker used the distributor's account in the company's drop-ship portal to submit substitutions, and one tampered switch had been powered on in the FSCE configuration lab on 2027-03-02. **DIBNet report due by Saturday 2027-03-06 09:00** (72 hours from discovery).
- Wednesday 2027-03-03 10:00: the Director, Government Contracts identifies that 12 substituted video recorders shipped on a federal order are rebranded units of a covered manufacturer. **Section 889 report due Thursday 2027-03-04** (1 business day); further information due **Thursday 2027-03-18** (10 business days after the 2027-03-04 report).
- Thursday 2027-03-04: the disclosure committee records that the event is a cybersecurity incident (conducted through the drop-ship portal) and starts the materiality assessment.
- Tuesday 2027-03-09 16:00: the committee determines the incident is material (federal contract exposure and a recall across 3 product lines). **Form 8-K due Monday 2027-03-15** (4 business days: March 10, 11, 12, and 15).
- Friday 2027-03-12: the Chief Privacy Officer determines that reseller contact records were exposed through the compromised account, including 640 Florida residents. **Florida individual and Department of Legal Affairs notices due by Sunday 2027-04-11** (30 days); the team plans to mail by Thursday 2027-04-08. Counsel also checks whether a "reason to believe" a breach arose earlier, which would move the Florida dates forward, and applies each other state's law.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), adjusted for this incident:
1. Order capture and fulfillment for unaffected SKUs and suppliers (BP-01, BP-02): lift holds that do not involve the affected supplier, account, or lots.
2. Replacement stock from the OEM or authorized sources for affected orders, federal orders first (BP-05).
3. Federal configuration jobs (BP-06): restart only with authenticated stock and verified firmware, after the FSCE is confirmed clean.
4. Drop-ship releases (BP-01): resume for the supplier only after its account is re-proofed, its environment is confirmed clean, and substitutions are screened before acceptance.
5. Supplier payments (BP-12): resume only after bank details are confirmed by call-back.
6. Return, credit, or destroy suspect stock only after disposition instructions, keeping records of each serial.

Tell resellers, DoD customers, and OEMs when replacement shipments go out (RC.CO). Keep holds on affected SKUs until the Chief Supply Chain Officer closes the product incident.

## 9. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.11).
- Update the risk register (P01: R-003, R-004, R-005, R-017, R-040), the POA&M (P07), the C-SCRM plan, the materiality playbook, and this runbook.
- Re-assess the supplier under STD-01.8 before any future purchase; consider removal from the approved supplier list.
- Disclosure committee reviews the incident's effect on the next Item 106 disclosure.
- Retain all incident records, including determination minutes and federal reports, for at least 6 years (POL-01 4.11).
