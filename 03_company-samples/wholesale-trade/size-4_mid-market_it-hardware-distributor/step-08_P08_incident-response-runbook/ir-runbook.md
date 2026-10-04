# Incident Response Runbook: Supplier Compromise Introducing Tampered or Counterfeit Products

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed IT hardware and software wholesale distributor) |
| Tier / Vertical | Mid-Market / Wholesale Trade |
| Incident type | A supplier (broker, distributor, or private-label contract manufacturer) is compromised or dishonest, and counterfeit, tampered, or covered (Section 889 or FASCSA) products enter inventory, the FIL, or customer shipments. Includes supplier email compromise used to redirect payments or push substitute products |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions; supply chain practices from NIST SP 800-161 Rev. 1 |
| Policy basis | POL-03 Incident Response Policy; POL-01 4.11 to 4.15 (supply chain) |
| Companion documents | `ir-runbook-ransomware.md`; `notification-matrix.csv` (20 obligations); BIA (P05); C-SCRM plan; procedure QP-14 |
| Runbook owners | Director of Quality and Product Compliance (product side) with the Security Manager (cyber side) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet as a whole. Applied to a real case in 2026-08 (section 10). Tabletop with outside counsel scheduled 2026-11-18 (POAM-015) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so product, cyber, business, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, Vice President of Supply Chain, Vice President of Sales Operations, Director of Federal Programs, Director of Marketing and Communications | Customer and prime communications, recalls, supplier termination, external statements, resources |
| **Product incident team** | Lead: Director of Quality and Product Compliance. Vice President of Supply Chain, Director of Distribution Operations, DC-1 and DC-2 General Managers, Federal Integration Lab Manager, OEM brand protection contacts | Quarantine, authentication, traceability, disposition |
| **Cyber incident team** | Incident commander: Security Manager. Director of Information Technology, security analysts, MSSP, forensic firm (through counsel) | Mailbox and account containment, scope of any company system compromise, evidence |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group on personal phones; printed call tree |
| Product incident lead | Director of Quality and Product Compliance | Vice President of Supply Chain | Out-of-band group |
| Cyber incident commander | Security Manager | Director of Information Technology | Out-of-band group; MSSP hotline |
| Reporting lead (DoD, primes, contracting officers, GIDEP) | Director of Federal Programs | Contracts Compliance Manager (second DIBNet certificate from 2026-10-31) | Out-of-band group |
| Legal | General Counsel; government contracts counsel; breach counsel (insurer panel) | Outside general counsel | Direct; breach counsel through the insurer hotline |
| Payments | Controller | Chief Financial Officer | Bank fraud desk number in the incident binder |
| Customers | Vice President of Sales Operations (resellers); Director of Federal Programs (primes) | Chief Operating Officer | Account contact lists |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card in the binder. Call before hiring any incident vendor |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the binder |

**Out-of-band first.** If a supplier's or the company's mailbox may be compromised, do not use email to discuss the incident or to confirm anything with the supplier. Use phone numbers already in the ERP, never numbers from a suspicious message.

**Legal privilege protocol.** General Counsel engages government contracts counsel and, for cyber matters, breach counsel, who directs any forensic firm. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, serial lists, logs) separate from legal conclusions. Do not speculate in writing about the supplier's fault.

## 1. Preparation checks (Identify / Protect)
- [x] Quarantine cage and "HOLD - DO NOT SHIP" status in the ERP and WMS at DC-1
- [ ] Quarantine cage and authenticity inspection at DC-2. **Gap until POAM-022 closes (2026-11-30)**
- [x] Serial numbers recorded for every DoD shipment and FIL job (traceability, 15 of 15 sampled in P03)
- [ ] Every SKU has a manufacturer of record; screening covers drop-ship orders. **Gap until POAM-021 closes (2026-12-15)**
- [ ] Logged quarterly SAM.gov search for FASCSA orders. **Gap until the first search (2026-10-31)**
- [ ] Two DIBNet medium assurance certificates. **Gap until 2026-10-31 (POAM-015)**
- [ ] Independent test lab agreement for authentication testing. **Gap until 2026-12-31 (POAM-022)**
- [x] Call-back verification of bank-detail changes (POL-05 4.6)
- [x] Printed incident binder at HQ, DC-1, DC-2, and the FIL: this runbook, call tree, notification matrix, supplier phone list

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| OEM serial validation fails, or the OEM says a serial was never sold into the channel | Receiving, Quality, OEM | Quarantine the lot; open a product incident |
| Resealed boxes, mismatched labels, wrong weight, missing holograms, unexpected firmware versions | Receiving, FIL and Integration Center technicians | Quarantine; photograph; do not power on |
| Firmware hash or signature does not match the OEM's published value | FIL technicians | Stop the job; isolate the device; call the product lead and the Security Manager |
| A SKU matches a covered manufacturer (including white-label units) or a FASCSA order | Director of Federal Programs; screening list | Block the SKU on all orders; start section 6 assessment |
| A GIDEP report, OEM bulletin, or industry alert names a part or supplier the company bought from | Quality (weekly GIDEP screening) | Trace receipts; quarantine matches |
| A supplier asks to change bank details, or invoices from a new domain | Controller, buyers | Do not pay. Call back. Report under POL-03 4.2 |
| A supplier says its systems were compromised | Supplier | Open an incident; freeze payments and purchase orders |
| A reseller or prime reports devices behaving oddly | Customer service; primes | Open an incident; pull the serial history |

**Declare a supplier compromise incident when** any of these is confirmed: products in stock, in the FIL, or shipped are suspected counterfeit, tampered, or covered; or a supplier's mailbox or systems are being used to send instructions to the company. The product incident lead declares; the CMT chair is told within 1 hour.

**Record the time of discovery and the time of identification.** DFARS 252.204-7012 counts 72 hours from discovery of a cyber incident. FAR 52.204-25(d) counts 1 business day, and FAR 52.204-23(c) and 52.204-30(c) count 3 business days, from identification.

## 3. First four hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Stop ship: hold every open order line with the affected SKUs, lots, serials, or supplier in the ERP and WMS, at both DCs and for drop-ship orders | Director of Distribution Operations | No affected item can be picked or drop-shipped |
| 2. Quarantine stock in the marked cage; photograph packaging and labels; keep everything | DC General Managers | Stock counted and tagged |
| 3. Stop affected FIL and Integration Center jobs; isolate any powered-on suspect device | Federal Integration Lab Manager | Jobs paused; devices bagged |
| 4. Freeze payments, open purchase orders, and bank-detail changes for the supplier; call the bank if a payment went out | Controller | Bank confirms hold or recall attempt |
| 5. Call the insurer's hotline; General Counsel engages government contracts counsel | Chief Operating Officer; General Counsel | Claim number issued; counsel engaged |
| 6. If a company mailbox may be involved: reset the password, revoke sessions and mailbox rules, export sign-in logs | Security Manager | Sessions revoked; logs exported |
| 7. Pull shipment history: which customers received the items, and **whether any went on a federal order or into a FIL job** | Vice President of Sales Operations; Director of Federal Programs | List of affected shipments |
| 8. Start the incident log: timeline, actions, who, and when | Product incident lead | Log open |

## 4. Analysis (RS.AN)
1. **Product scope.** List every affected supplier, SKU, lot, serial, purchase order, receipt, and shipment. Check other SKUs from the same supplier, including drop-ship orders.
2. **Authenticity.** Send serials and photos to the OEM. For parts bound for DoD jobs, arrange inspection, testing, and authentication by the OEM or an independent test lab (DFARS 252.246-7008(b)(3)(ii)(B)).
3. **Covered equipment.** Check the true manufacturer of every affected SKU against the FAR 52.204-25 covered manufacturers and any applicable FASCSA order, including rebranded units. Record who decided and why.
4. **Cyber scope.** Decide whether any company system was affected: was a company mailbox, ERP account, or portal account used? Was a suspect device powered on or connected in the FIL or the Integration Center? Did the supplier's compromise expose company data?
5. **Preserve evidence.** Keep emails with full headers, devices, packaging, and logs. If the FIL or the enclave is involved, image affected systems; DFARS 252.204-7012(e) requires keeping images and monitoring data for at least 90 days after a DIBNet report.

## 5. Containment and eradication (RS.MI)
1. Suspend the supplier on the approved supplier list. Buy replacements only from the OEM or authorized sources.
2. Block the affected SKUs on all orders until the product lead and the Director of Federal Programs release them in writing.
3. Keep suspect items. Do not return them to the seller or scrap them until they are determined authentic or disposition instructions arrive (DFARS 252.246-7007(c)(6); POL-03 4.4).
4. For a compromised company account: remove attacker mailbox rules, reset MFA methods, and check forwarding rules and app grants.
5. For a suspect device that touched the FIL network: isolate the FIL workstation, rebuild it from the enclave image, and review enclave access logs.
6. Warn buyers and the Controller about the supplier's lookalike domains and phone numbers.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** The Director of Federal Programs owns every DoD, prime, and GIDEP report; counsel confirms each before it goes out. The CMT approves customer and external communications.

| What was found | Clock | Owner |
|---|---|---|
| A company system or the CUI in it was affected | DIBNet report within 72 hours of discovery; incident number to the prime as soon as practicable; preserve images 90 days | Director of Federal Programs; Security Manager |
| Covered telecommunications or video surveillance equipment identified in performance of a federal subcontract | Report within 1 business day of identification (FAR 52.204-25(d)); further information within 10 business days | Director of Federal Programs |
| A Kaspersky Lab covered article provided to the Government | Report within 3 business days (FAR 52.204-23(c)); further information within 10 business days | Director of Federal Programs |
| A product or source subject to an applicable FASCSA order provided or used | Report within 3 business days (FAR 52.204-30(c)(4)); further information within 10 business days | Director of Federal Programs |
| A DoD job used parts from outside the sourcing order, or parts that cannot be confirmed new | Prompt written notice to the contracting officer through the prime (DFARS 252.246-7008(b)(3)(ii)) | Director of Quality and Product Compliance |
| Counterfeit or suspect counterfeit parts purchased by or for DoD | Report to the contracting officer through Prime A and to GIDEP (DFARS 252.246-7007(c)(6)); 60 days if a prime flowed down FAR 52.246-26 | Director of Quality and Product Compliance |
| Personal information exposed (for example a compromised mailbox with employee records) | Each state's law; Florida example: individuals within 30 days of determination, the Department of Legal Affairs within 30 days if 500 or more | General Counsel |
| Only a supplier's own systems were compromised, and no company system, CUI, or covered or counterfeit product is involved | No regulatory clock. Insurer notice; consider a voluntary IC3 report; notify affected customers under their contracts | Chief Operating Officer |

**Customers.** Tell affected resellers and primes in writing which serials they received, what is known, and what to do (hold, return, or replace). Scripts are approved by counsel and the CMT.

**Plan to the shortest clock.** The 1-business-day Section 889 report can fall due before the facts are complete. File what is known on time and follow up within 10 business days.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05), adjusted for this incident:
1. Order capture and fulfillment for unaffected SKUs (BP-01, BP-04): lift holds that do not involve the affected supplier or lots.
2. Replacement stock from the OEM or authorized sources, federal orders first.
3. FIL jobs (BP-10): restart only with authenticated, authorized-source stock and verified firmware.
4. Supplier payments (BP-13): resume for the supplier only after bank details are confirmed by call-back and the supplier shows its systems are clean.
5. Return, credit, or destroy suspect stock only after disposition, keeping records of each serial.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; documentation within 30 days (POL-03 4.11).
- Update the risk register (P01: R-003, R-006, R-007, R-023, R-034, R-051), the POA&M (P07), the C-SCRM plan, QP-14, and this runbook.
- Reassess the supplier before any future purchase.
- Retain all incident documentation for 6 years (POL-01 4.17).

## 9. Crisis management and legal integration
| Decision | Who decides | Input from |
|---|---|---|
| Recall from resellers | CMT chair | Product lead; General Counsel; Vice President of Sales Operations |
| Supplier suspension or termination | Vice President of Supply Chain | General Counsel (contract rights) |
| Whether a report is due under each clause | General Counsel with government contracts counsel | Director of Federal Programs; product lead |
| External statement or reseller bulletin | CMT chair | Director of Marketing and Communications; General Counsel |
| Engaging law enforcement | General Counsel | Security Manager |

## 10. Worked example: uninspected optical transceivers (August 2026)
On 2026-08-13 control assessment testing (P07, SR-10) found that 64 optical transceiver modules bought from broker BRK-17 had been received at DC-2 on 2026-06-18 without inspection, and that the OEM could not validate 23 of the sampled serial numbers. Applying this runbook:
- **Sections 2 and 3:** the Director of Quality and Product Compliance declared a product incident; the remaining 46 units were quarantined at DC-1 the same day, and open purchase orders with BRK-17 were frozen.
- **Section 4:** shipment history showed 18 units sold to 2 commercial resellers and none on a federal order or in a FIL job. No company system used the modules.
- **Section 6:** counsel confirmed that no DoD or GIDEP report under DFARS 252.246-7007(c)(6) was due, because no part was purchased by or for DoD; the decision is logged. The 2 resellers were told in writing which serials they received and asked to hold them for recall.
- **Section 7 and 8:** recall and OEM authentication of all 64 units are due 2026-10-31; BRK-17 is suspended pending review (due 2026-10-31); R-051 was added to the risk register, and POAM-022 was raised to include DC-2 inspection.
