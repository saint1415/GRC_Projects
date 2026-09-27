# Incident Response Runbook: Supplier Compromise Introducing Tampered or Counterfeit Products

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (IT hardware and software wholesale distributor) |
| Tier / Vertical | Small / Wholesale Trade |
| Incident type | A supplier is compromised or dishonest, and tampered, counterfeit, or covered (Section 889) products enter inventory or ship to customers. Includes supplier email compromise used to redirect payments or push substitute products |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); supply chain practices from NIST SP 800-161 Rev. 1 |
| Policy basis | POL-03 Incident Response Policy; POL-01 4.11 to 4.14 (supply chain) |
| Runbook owner | IT Manager (cyber side) with the Purchasing and Supplier Manager (product side) |
| Approved | 2026-08-31 by the Chief Operating Officer |
| Last tested | Not yet. First tabletop exercise due 2026-11-30 (POAM-008) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead (overall) | Chief Operating Officer | IT Manager | Cell, then the out-of-band group chat on personal phones |
| Product lead (stock, suppliers, authentication) | Purchasing and Supplier Manager | Warehouse and Logistics Manager | Cell |
| Cyber lead (mailboxes, ERP, lab network) | IT Manager | Systems Administrator; MSP incident team | Incident line; MSP 24x7 line |
| Reporting lead (DoD, primes, contracting officers) | Government Contracts Manager | Controller (second medium assurance certificate holder) | Cell |
| Payments | Controller | Chief Operating Officer | Cell; bank fraud desk number in the incident binder |
| Legal counsel | Outside counsel (insurer panel for cyber matters; government contracts counsel for DFARS and FAR questions) | n/a | Via insurer hotline; counsel's direct line |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder. Call before hiring any incident vendor |
| Customers | Sales Operations Manager (resellers); Government Contracts Manager (primes) | Chief Operating Officer | Account contact lists |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** If a supplier's or the company's mailbox may be compromised, do not use email to discuss the incident or to confirm anything with the supplier. Use phone numbers already on file in the ERP, never numbers from a suspicious message.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder in the Chief Operating Officer's office and the lab: this runbook, contacts, the notification matrix, and the supplier phone list
- [ ] Two DoD-approved medium assurance certificates (Government Contracts Manager and Controller) and a tested DIBNet sign-in. **Gap until POAM-007 closes (2026-10-15)**
- [ ] Quarantine cage area marked in the warehouse, with a "HOLD - DO NOT SHIP" status in the ERP and WMS
- [ ] Receiving inspection and OEM serial validation in use (SR-10). **Gap until POAM-011 closes**
- [ ] Every SKU has a manufacturer of record, with a hard block on covered manufacturers for federal orders. **Gap until POAM-012 closes**
- [ ] Serial numbers recorded per DoD shipment and per Prime B job (for tracing)
- [ ] Call-back verification of bank-detail changes in force (POL-05 4.6; R-003)
- [ ] Log retention long enough to investigate (1 year). **Gap until POAM-018 closes**

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A supplier asks to change bank details, or sends an invoice from a new domain or with new payment instructions | Controller, buyers | Do not pay. Call back on the number in the ERP. Report to the IT Manager (POL-03 4.2) |
| OEM serial validation fails, or the OEM says a serial was never sold into that channel | Receiving, buyers, OEM | Quarantine the lot; open a product incident |
| Resealed boxes, mismatched labels, wrong weight, missing holograms, or odd firmware versions | Receiving, lab technicians | Quarantine; photograph; do not power on in the lab |
| Firmware hash or signature does not match the OEM's published value | Lab technicians | Stop the job; isolate the device from the lab network; call the IT Manager |
| A SKU matches a covered manufacturer, including a rebranded or white-label unit | Government Contracts Manager, screening list | Block the SKU on all orders; start the Section 889 assessment in section 6 |
| A supplier tells the company its systems were compromised | Supplier | Open an incident; freeze payments and purchase orders to that supplier |
| A customer reports a device behaving oddly (unexpected outbound connections, failed updates) | Customer service, primes | Open an incident; pull the serial history |

**Declare a supplier compromise incident when** any of these is confirmed: products in stock or shipped are suspected counterfeit, tampered, or covered; or a supplier's mailbox or systems are being used to send instructions to the company.

**Record the time of discovery and the time of identification.** DFARS 252.204-7012 counts 72 hours from discovery of a cyber incident. FAR 52.204-25(d) counts 1 business day from identification of covered equipment.

## 3. First four hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Stop ship: put every open order line with the affected SKUs, lots, or supplier on hold in the ERP and WMS | Warehouse and Logistics Manager | No affected item can be picked |
| 2. Quarantine affected stock in the marked area; photograph packaging and labels; keep everything | Receiving | Stock counted and tagged |
| 3. Freeze payments, open purchase orders, and bank-detail changes for the supplier; call the bank fraud desk if a payment already went out | Controller | Bank confirms hold or recall attempt |
| 4. Call the cyber insurer's hotline; engage counsel through the insurer and government contracts counsel | Chief Operating Officer | Claim number issued |
| 5. If a company mailbox may be involved: reset the password, revoke sessions and mailbox rules, and pull sign-in logs before they roll over | IT Manager | Sessions revoked; logs exported |
| 6. Pull the shipment history: which customers received the affected SKUs, lots, or serials, and **whether any went on a DoD order** | Sales Operations Manager; Government Contracts Manager | List of affected shipments |
| 7. Start the incident log: timeline, actions, who, and when | IT Manager | Log open |

## 4. Analysis (RS.AN)
1. **Product scope.** List every affected supplier, SKU, lot, serial number, purchase order, receipt, and shipment. Check whether the same broker supplied other SKUs.
2. **Authenticity.** Send serials and photos to the OEM for validation. For items bound for DoD jobs, arrange inspection, testing, and authentication by the OEM or an independent test lab (DFARS 252.246-7008(b)(3)(ii)(B)).
3. **Covered equipment.** Check the true manufacturer of every affected SKU against the FAR 52.204-25 covered manufacturers, including rebranded units. Record who decided and why.
4. **Cyber scope.** Decide whether any company system was affected:
   - Was a company mailbox, ERP account, or portal account used by the attacker?
   - Was a suspect device powered on or connected on the lab network, where CUI is handled?
   - Did the supplier's compromise expose company data (pricing, bank details, employee or reseller contact information)?
5. **Preserve evidence.** Keep the emails with full headers, the devices, the packaging, and exported logs. If the lab network or CUI systems are involved, image the affected systems; DFARS 252.204-7012(e) requires keeping images and monitoring data for at least 90 days after a DIBNet report.

## 5. Containment and eradication (RS.MI)
1. Suspend the supplier on the approved supplier list. Buy replacements only from the OEM or authorized sources.
2. Block the affected SKUs on all orders until the Purchasing and Supplier Manager and Government Contracts Manager release them in writing.
3. Keep suspect items. Do not return them to the supplier or scrap them until the prime or contracting officer gives disposition instructions (POL-03 4.4).
4. For a compromised company account: remove attacker mailbox rules, reset MFA methods, and check for new forwarding rules and OAuth app grants.
5. For a suspect device that touched the lab network: isolate the lab workstation, rebuild it from the standard image, and check the CUI share access logs.
6. Warn other buyers and the Controller about the supplier's lookalike domains and phone numbers.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** The Government Contracts Manager owns every DoD and prime notice. Counsel confirms each notice before it goes out.

**Which clocks start:**
| What was found | Clock | Owner |
|---|---|---|
| A company system or the CUI in it was affected by the incident | DIBNet report within 72 hours of discovery; DoD incident report number to Prime B as soon as practicable; preserve images for 90 days | Government Contracts Manager; IT Manager |
| Covered telecommunications or video surveillance equipment identified in a system during performance of a DoD subcontract | Report within 1 business day of identification; further information within 10 business days (DoD: DIBNet) | Government Contracts Manager |
| A Prime B job used electronic parts from outside the authorized sourcing order, or parts that cannot be confirmed as new | Prompt written notice to the contracting officer through Prime B | Government Contracts Manager |
| Suspect counterfeit items bought for a Government delivery, and a prime has flowed down FAR 52.246-26 | Contracting officer notice and GIDEP report within 60 days | Government Contracts Manager |
| Personal information exposed (for example a compromised mailbox with employee records) | Florida individual notice within 30 days of determination; Department of Legal Affairs if 500 or more; other states' laws for residents elsewhere | Chief Operating Officer and counsel |
| Only a supplier's own systems were compromised and no company system, CUI, or covered equipment is involved | No regulatory clock. Notify the insurer; consider a voluntary IC3 report; notify affected customers under their contracts | Chief Operating Officer |

**Customers.** Tell affected resellers and primes in writing which serials they received, what is known, and what to do (hold, return, or replace). Scripts are approved by counsel. Do not speculate about the supplier's fault in writing.

**Plan to the shortest clock.** The 1-business-day Section 889 report can fall due before the facts are complete. File what is known on time and follow up within 10 business days.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05), adjusted for this incident:
1. Order capture and fulfillment for unaffected SKUs (BP-01, BP-02): lift holds that do not involve the affected supplier or lots.
2. Replacement stock from the OEM or authorized sources for affected orders, DoD orders first.
3. Prime B jobs (BP-06): restart only with authenticated, authorized-source stock and verified firmware.
4. Supplier payments (BP-08): resume for the supplier only after bank details are confirmed by call-back and the supplier shows its systems are clean.
5. Return, credit, or destroy suspect stock only after disposition instructions, keeping records of each serial.

Tell customers when replacement shipments go out (RC.CO). Keep holds on affected SKUs until the Purchasing and Supplier Manager closes the product incident.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-003, R-035), the POA&M (P07), the C-SCRM plan, and this runbook.
- Re-assess the supplier under the broker assessment before any future purchase.
- Retain all incident documentation for 6 years (POL-01 4.15).

## 9. Worked example: white-label video SKUs (August 2026)
On 2026-08-06 control assessment testing (P07, SR-05[02]) found 3 IP camera and video recorder SKUs from one broker whose OEM of record was blank. The broker's catalog listed them as rebranded units of a manufacturer named in FAR 52.204-25. Applying this runbook:
- **Sections 2 and 3:** declared a product incident; blocked the 3 SKUs on all orders and quarantined 46 units on 2026-08-07; froze open purchase orders with the broker.
- **Section 4:** shipment history showed 19 units sold to 4 commercial resellers in 2026 and none on any DoD order. No company system used the products.
- **Section 6:** counsel confirmed that no FAR 52.204-25(d) report was due, because no covered equipment was provided or used under a federal contract. The 4 resellers were told in writing which serials they received and that the units are rebranded products of a covered manufacturer, so they can decide on their own federal sales.
- **Section 8:** the broker is suspended pending the review due 2026-09-30 (POAM-012), and R-035 was added to the risk register.
