# Incident Response Runbook: Supplier Compromise Introducing Tampered or Counterfeit Products

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (IT hardware and software reseller) |
| Tier / Vertical | Micro / Wholesale Trade |
| Incident type | A supplier (usually a broker) is compromised or dishonest, and tampered, counterfeit, or covered (Section 889) products enter stock or ship to customers. Includes a supplier mailbox compromise used to redirect payments or push substitute products |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); supply chain practices from NIST SP 800-161 Rev. 1 |
| Policy basis | POL-03 Incident Response Policy; POL-02 A.8 to A.11 (supplier rules) |
| Runbook owner | Operations Manager, with the Purchasing and Inventory Coordinator for the product side |
| Approved | 2026-08-31 by the Owner |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 |

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. The Owner leads, the Operations Manager coordinates and keeps the log, the MSP does the technical work, and the cyber insurer supplies counsel and forensics for anything that touches company systems.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead (decisions, money, Government reports) | Owner | Operations Manager | Cell phone (numbers on the printed contact card) |
| Coordinator and incident log | Operations Manager | Federal Account Manager | Cell phone |
| Product lead (stop-ship, quarantine, supplier, OEM checks) | Purchasing and Inventory Coordinator | Setup and Receiving Technician | Cell phone |
| Government reports (DIBNet, contracting officers, Federal Prime) | Owner | Federal Account Manager | DIBNet accounts (POAM-007); contracting officer contacts in the binder |
| Payments | Bookkeeper | Owner | Cell phone; bank fraud desk number in the binder |
| Technical response | MSP incident line (24x7 number in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Policy card in the binder. Call before hiring any incident vendor |
| Counsel | Insurer panel counsel (cyber and privacy); government contracts counsel (FAR and DFARS questions) | n/a | Through the hotline; counsel's direct line |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Notification chain in the first hour:** staff member → Operations Manager → Owner and Purchasing and Inventory Coordinator (at the same time) → MSP incident line if any company account, device, or the setup bench may be involved → insurer breach hotline (Owner) if company systems or payments are involved → government contracts counsel if any DoD order is involved.

**Out-of-band first.** If a supplier's or the company's mailbox may be compromised, do not use email to discuss the incident or confirm anything with the supplier. Use phone numbers already in the ERP, never numbers in a suspicious message.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder in the Owner's office: this runbook, the contact card, the notification matrix, contracting officer and Federal Prime contacts, and the supplier phone list
- [ ] DIBNet accounts for the Owner and the Federal Account Manager, tested. **Gap until POAM-007 closes (2026-10-15)**
- [ ] A marked quarantine shelf in the stockroom and a "HOLD - DO NOT SHIP" status in the ERP
- [ ] Every SKU has a manufacturer of record, with a block on covered manufacturers for DoD quotes. **Gap until POAM-012 closes**
- [ ] Receiving checklist and OEM serial validation for non-authorized items. **Gap until POAM-013 closes**
- [ ] Serial numbers recorded in the ERP for every unit shipped (in place)
- [ ] Bank-detail call-back rule in force (POL-02 A.11)
- [ ] Spare laptop kept powered off for the reporting kit (P05 recovery priority 1)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A supplier asks to change bank details, or sends an invoice from a new domain or with new payment instructions | Bookkeeper, buyer | Do not pay. Call back on the number in the ERP. Report to the Operations Manager (POL-03 4.2) |
| Resealed boxes, mismatched labels, wrong weight, missing holograms, or an unexpected firmware version | Receiving, setup bench | Put the lot on hold; photograph; do not power it on at the bench |
| The OEM says a serial number was never sold into this channel, or the serial is a duplicate | Buyer, OEM | Quarantine the lot; open a product incident |
| A SKU's true manufacturer is on the covered list, including a rebranded or white-label unit | Federal Account Manager, screening list | Block the SKU on all quotes; go to section 6 for the clocks |
| A supplier says its systems or mailbox were compromised | Supplier | Open an incident; freeze payments and open purchase orders to that supplier |
| A customer reports a device behaving oddly (unexpected connections, failed updates, wrong firmware) | Account managers | Open an incident; pull the serial history from the ERP |

**Declare a supplier compromise incident when** any of these is confirmed: products in stock, at the bench, or already shipped are suspected counterfeit, tampered, or covered; or a supplier's mailbox or systems are being used to send instructions to the company.

**Write down two times.** The time of **discovery** (first report to the Operations Manager) and the time of **identification** of any covered item. The Section 889 report runs from identification and is due within 1 business day.

## 3. First four hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Stop ship: put every open order line with the affected SKUs, lots, serials, or supplier on hold in the ERP; cancel open drop-ship orders with that supplier | Purchasing and Inventory Coordinator | No affected item can ship |
| 2. Quarantine stock on the marked shelf; photograph packaging, labels, and serials; keep everything | Setup and Receiving Technician | Stock counted and tagged |
| 3. Freeze payments, open purchase orders, and bank-detail changes for the supplier; call the bank fraud desk if a payment already went out | Bookkeeper | Bank confirms the hold or a recall attempt |
| 4. Pull the shipment history from the ERP: which customers received the affected serials, and **whether any went on a DoD order** | Federal Account Manager | List of affected shipments |
| 5. If a company mailbox, account, or the setup bench may be involved: call the MSP incident line and the insurer's hotline; reset passwords, revoke sessions, remove mail forwarding rules, and export sign-in logs before they roll over | Owner; MSP | Sessions revoked; logs exported |
| 6. If a DoD order is involved: call government contracts counsel | Owner | Counsel engaged |
| 7. Start the incident log: timeline, actions, who, and when | Operations Manager | Log open |

## 4. Analysis (RS.AN)
1. **Product scope.** List every affected supplier, SKU, lot, serial, purchase order, receipt, and shipment. Check what else the same supplier sold the company in the last 12 months.
2. **Authenticity.** Send serials and photos to the OEM through the company's partner program. For anything bound for a DoD order, the company is responsible for inspection, testing, and authentication (DFARS 252.246-7008(b)(3)(ii)(B)); the OEM or an independent test lab does the work.
3. **Covered equipment.** Check the true manufacturer of each affected SKU against the FAR 52.204-25 covered list, including rebranded units. Record who decided and why.
4. **Company systems.** Decide whether any company system was affected:
   - Was a company mailbox, ERP account, or supplier portal login used by the attacker?
   - Was a suspect device powered on or connected at the setup bench, and did the bench then configure other customer devices?
   - Did the supplier's compromise expose company data (pricing, bank details, customer contacts)?
5. **Preserve evidence.** Keep the emails with full headers, the devices, the packaging, and the exported logs. If the setup bench was involved, the MSP images it before rebuilding.

## 5. Containment and eradication (RS.MI)
1. Suspend the supplier on the supplier list. Buy replacements only from the OEM or authorized distributors.
2. Keep affected SKUs blocked until the Purchasing and Inventory Coordinator and the Owner release them in writing.
3. Keep suspect items. Do not return them to the supplier or scrap them until the Owner releases them, or, for DoD orders, until the contracting officer or the Federal Prime gives disposition instructions (POL-03 4.4).
4. For a compromised company account: remove attacker mail rules and app consents, reset MFA methods, and check for new forwarding rules.
5. For a suspect device that touched the setup bench: disconnect the bench, rebuild it from the MSP's standard image, and re-check every device it configured since the suspect device arrived.
6. Warn the Bookkeeper and buyers about the supplier's lookalike domains and phone numbers.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** The Owner makes every Government report, with the Federal Account Manager as backup. Counsel reviews each one where time allows; review never delays a deadline.

**Which clocks start:**
| What was found | Clock | Owner |
|---|---|---|
| Covered telecommunications or video surveillance equipment identified in a system during performance of a DoD order | Report at DIBNet within **1 business day** of identification; further information within 10 business days (FAR 52.204-25(d)) | Owner |
| A Kaspersky covered article provided under an order that includes FAR 52.204-23 | Report within **3 business days** of identification; further information within 10 business days (FAR 52.204-23(c)) | Owner |
| A DoD order item came from outside the sourcing order, or cannot be confirmed new | **Prompt** written notice to the contracting officer, or to the Federal Prime for its orders (DFARS 252.246-7008(b)(3)(ii)(A)) | Owner |
| Counterfeit or suspect items on an order that includes FAR 52.246-26 | Contracting officer notice and GIDEP report within 60 days (none of the current orders includes the clause) | Owner |
| Personal information exposed (for example a compromised mailbox with employee records or customer portal credentials) | Florida individual notice no later than 30 days after determination; other states' laws for residents elsewhere | Owner with counsel |
| Only a supplier's own systems were compromised, and no company system, DoD order, or covered equipment is involved | No legal clock. Notify the insurer if a payment was attempted; voluntary IC3 report; notify affected customers under their contracts | Owner |

**Plan to the shortest clock.** The 1-business-day Section 889 report can fall due before the facts are complete. File what is known on time, then complete it within 10 business days.

**Customers.** Tell affected customers in writing which serials they received, what is known, and what to do (hold, return, or replace). Counsel approves the wording. Do not speculate in writing about the supplier's fault.

**No CUI here.** The DFARS 252.204-7012 72-hour cyber incident report does not apply, because the company holds no covered defense information (P03 G-027). If an incident ever involves CUI, stop and call counsel: that would mean CUI entered company systems against POL-04 4.4.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05), adjusted for this incident:
1. Reporting kit (BP-03): clean spare laptop, binder, DIBNet access.
2. Quoting and order entry (BP-01) and purchasing (BP-02) for unaffected SKUs: lift holds that do not involve the affected supplier or lots.
3. Replacement stock from the OEM or authorized distributors for affected orders, DoD orders first.
4. Setup bench (BP-04): restart only after a rebuild if a suspect device touched it, and only with authenticated stock.
5. Supplier payments (BP-06): resume for the supplier only after bank details are confirmed by call-back and the supplier shows its systems are clean.
6. Return, credit, or destroy suspect stock only after disposition instructions, keeping the serial records.

Tell customers when replacement shipments go out (RC.CO). Keep holds in place until the Purchasing and Inventory Coordinator closes the product incident.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP if it was involved. Written summary within 30 days (POL-03 4.11).
- Update the risk register (P01, especially R-001, R-002, R-003, R-019, R-024), the POA&M (P07), the C-SCRM plan, and this runbook.
- Re-assess the supplier under the broker approval checklist before any future purchase.
- Keep all incident records for 6 years (POL-02 A.12).

## 9. Worked examples: 2026 events run through this runbook
**April 2026 payment diversion (supplier mailbox lookalike).** On 2026-04-14 an email from a lookalike domain of a broker asked for new bank details, and the Bookkeeper paid $12,600 to the new account. Under this runbook:
- **Section 2:** the bank-change request is a trigger; the call-back to the number in the ERP would have stopped the payment.
- **Section 3:** freeze payments to the broker and call the bank fraud desk at once. In April the bank recalled the payment and returned it on 2026-04-20.
- **Section 6:** no company system was compromised and no DoD order was involved, so there was no legal clock. The runbook now calls for a voluntary IC3 report and an insurer notice; neither was made in April.

**August 2026 covered camera recorder (company's own equipment).** On 2026-08-11 the P07 assessor found that the stockroom camera recorder and cameras are white-label units of a manufacturer named in the FAR 52.204-25 covered definition (P07 POAM-005). Under this runbook:
- **Section 2:** record the identification time (2026-08-11).
- **Section 5:** devices disconnected 2026-08-12 and replaced 2026-08-20.
- **Section 6:** the equipment was used in the company's own stockroom, not provided on any order. Whether a 52.204-25(d) report is due, and whether the 52.204-26 representation must be corrected, are legal questions; counsel's decision is due 2026-09-30 (R-024). The runbook's rule for any future case on a DoD order is to file within 1 business day and let counsel's review follow.
