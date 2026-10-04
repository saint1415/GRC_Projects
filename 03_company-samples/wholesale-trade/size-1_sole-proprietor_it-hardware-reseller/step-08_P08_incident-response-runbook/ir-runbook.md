# Incident Response Runbook: Counterfeit or Tampered Products from a Supplier

| Field | Value |
|---|---|
| Organization | Cris Santos Company (IT hardware reseller) |
| Tier / Vertical | Sole Proprietorship / Wholesale Trade |
| Incident type | A marketplace seller, broker, or other supplier is compromised or dishonest, and counterfeit, tampered, or covered (Section 889) products reach stock, customers, or a DoD delivery. Includes a supplier mailbox used to redirect a payment |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours; supply chain steps from NIST SP 800-161 Rev. 1 |
| Policy basis | POL-01 sections 6 and 10 |
| Owner and approver | Owner, 2026-08-31 |
| Last tested | Used for the optics case in section 7 (2026-08-06 to 2026-08-24). Walkthrough with the IT consultant due 2026-09-30 |

Keep a printed copy and the contact sheet in the home office. **If a supplier's mailbox or your own may be compromised, do not use email to confirm anything.** Call numbers already on file, never numbers in a suspicious message.

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Prime's subcontracts manager | Any suspect item on, or staged for, a DoD order (2 business days, BPA); any covered equipment (1 business day, FAR 52.204-25(d)) or Kaspersky article (3 business days, FAR 52.204-23(c)) | Hour 0 to day 1 |
| OEM partner support | Confirm whether serial numbers are genuine; replacement and warranty questions | Hours 0-4 |
| Bank fraud desk | Stop or recall a payment sent on changed instructions | At once |
| Marketplace dispute desk or broker | Hold payment, open a claim, and request the seller's records. Do not accuse in writing | Hours 4-8 |
| Government contracts attorney (identified by referral; engage by phone) | Whether a report is due, wording of notices, customer scripts | Hours 0-8 when the prime or Section 889 is involved |
| On-call IT consultant | Mailbox or account compromise; checking a device that was powered on | As needed |
| Affected customers | Hold, return, or replace | Day 1 |
| FBI IC3 (online report) | Voluntary report of payment fraud or a business email compromise | Day 1 |

Contact numbers are on the printed sheet only, not in this file.

## 2. Declare (Detect)
Declare a supplier compromise incident when any of these happens:
- an OEM serial lookup fails, or the OEM says a serial was never sold into that channel;
- seals, labels, weight, holograms, or packaging do not match a genuine unit, or firmware does not match the OEM's published version or hash;
- a product's true manufacturer turns out to be a covered manufacturer under FAR 52.204-25 (including white-label units);
- a customer reports odd behavior (failed updates, unexpected outbound connections);
- a supplier asks to change bank details or sends new payment instructions, or says its systems were compromised.

**Write down the date and time.** Two clocks count from different moments: FAR 52.204-25(d) counts 1 business day from **identification** of covered equipment, and the BPA counts 2 business days from suspicion that an item delivered to the prime is counterfeit or nonconforming.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. **Stop ship.** Put every open order with the affected SKU, lot, or supplier on hold in SYS-01. Cancel pending drop shipments from that supplier | Nothing affected can ship |
| 2. **Quarantine.** Move affected stock to the quarantine shelf in the locked cabinet. Photograph packaging, labels, and serials. Do not power on suspect devices on the home network | Stock counted and tagged |
| 3. **Freeze money.** Hold payments and open orders to the supplier. If a payment went out on changed instructions, call the bank fraud desk now | Bank confirms hold or recall attempt |
| 4. **Check DoD exposure.** Search SYS-01 and the serial-to-tag spreadsheets: did any affected serial go on, or is any staged for, a prime order? | Yes or no recorded |
| 5. **Start the incident log** on paper: time of discovery, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and authenticate (RS.AN)
1. **Product scope.** List every affected supplier, purchase, SKU, lot, and serial, and every customer that received them (SYS-01 sales history). Check what else the same seller supplied.
2. **Authenticity.** Send serials and photos to OEM partner support. Ask for written confirmation.
3. **Covered equipment.** Confirm the true manufacturer of each affected item against FAR 52.204-25 (and FAR 52.204-23). Record who checked and how.
4. **Account scope.** If payment instructions or emails were involved: with the IT consultant, check the owner's mailbox for forwarding rules and unknown sign-ins, and the SYS-01 sign-in history and payment-detail changes. Export sign-in logs before they roll over.
5. **Preserve evidence.** Keep the items, packaging, emails with full headers, marketplace listing screenshots, and payment records. Nothing is returned, resold, or scrapped until the attorney (and, for DoD items, the prime) agrees.

## 5. Hours 8-24: notify and keep selling (RS.CO, RC.RP)
- **Which notices are due** (from `notification-matrix.csv`):

| Finding | Clock | Notify |
|---|---|---|
| Affected item on, or staged for, a prime order | 2 business days (BPA) | Prime's subcontracts manager |
| Covered telecommunications or video surveillance equipment identified | 1 business day; follow-up within 10 business days | Prime's subcontracts manager (prime reports through DIBNet) |
| Kaspersky covered article identified | 3 business days; follow-up within 10 business days | Prime's subcontracts manager |
| Personal information exposed through a compromised account | 30 days after determination (Florida) | Affected individuals, after counsel's check |
| Only commercial customers affected, no covered equipment, no personal information | No regulatory clock | Customers under their purchase terms; voluntary IC3 report |

- **Plan to the shortest clock.** File what is known on time and follow up; do not wait for complete facts.
- **Customers.** Tell each affected customer in writing which serials they received, that the items may not be genuine, and that a replacement from an authorized source is on its way. Do not speculate about the supplier.
- **Keep selling.** Lift holds on unaffected SKUs. Replace affected items only from the OEM or an authorized distributor. Restart staging for the prime only with authorized-source stock and firmware checked on the bench switch. Recovery order otherwise follows P05.

## 6. After day 1 (ID.IM)
Within 30 days of closing: remove the supplier from the supplier list (POL-01 6.2), claim the refund or chargeback, update P01 (R-001, R-002, R-010), the POA&M (P07), and this runbook, and keep the incident records for 6 years (POL-01 8.6). If a payment was lost, record it for the business's tax records.

## 7. Worked example: cloned optics (August 2026)
On 2026-08-06, P07 testing (SR-11a.[03]) checked 12 serials from 2026 marketplace and broker purchases in the OEM partner portals. 2 optical transceivers from a lot of 8 bought from one marketplace seller on 2026-06-10 returned "not found". Applying this runbook:
- **Sections 2 and 3:** declared at 14:10 on 2026-08-06; the 2 units in stock went to quarantine; the seller was blocked in SYS-01 and no payment was outstanding (paid by card through the marketplace).
- **Section 4:** SYS-01 history showed the other 6 units went to 2 commercial customers (a managed service provider and a law office) in 2026-06 and 2026-07. **None went on a prime order** (DoD orders are bought from distributor A), so no BPA notice was due. The OEM's true manufacturer is not a covered manufacturer, so no FAR 52.204-25 report was due. No account or personal information was involved. The OEM confirmed on 2026-08-20 that both serials are cloned.
- **Section 5:** both customers were called on 2026-08-07 and told in writing on 2026-08-20; replacements from distributor A shipped on 2026-08-24 and the 6 units came back to quarantine. A marketplace claim was opened for the full lot.
- **Section 6:** the seller was removed, POAM-008 tracks the receiving checks, and the owner decided that optics and network devices come only from authorized sources (POL-01 6.1).
