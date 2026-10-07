# Business Impact Analysis: Cris Santos Company | Chemical | Sole Proprietorship

**Organization:** Cris Santos Company (specialty chemical distributor, broker) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner, 2026-09-09, with the on-call IT technician | **Adopted:** Owner, 2026-10-05

## 1. Overview and purpose
This one-page BIA lists the five business functions the brokerage depends on, how long each can be down, and how much data it can lose. It feeds:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the en route and communications measures in the hazmat transportation security plan (HSP-01, P06), because a shipment that cannot be supported in transit is a security and safety problem, not only a business one;
- the recovery order in the incident runbook (P08).

## 2. Business description
One person runs a drop-ship chemical brokerage from a home office in Florida. The business sells hydrogen peroxide 50%, sodium hypochlorite, sodium hydroxide, ferric chloride, and non-hazardous polymers to about 40 industrial customers. Carriers pick up at five suppliers' plants and terminals and deliver to the customer. The business never holds chemicals. Its work is information: orders, pickup authorizations, bills of lading, emergency response information, and payments, all carried by the SaaS stack (SYS-01 to SYS-08). See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts. One bulk hydrogen peroxide load is worth about $15,000.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (a diverted load or misdirected payment) | $1,000 to $5,000 (carrier detention, a lost tote order) | Less than $1,000 |
| Operations | No load can be released or supported in transit | Loads delayed one or two days | Administrative delay only |
| Regulatory | HMR violation on a shipment (no security plan, wrong shipping paper, unmonitored emergency number) or a breach notice duty | Missing record that must be recreated | Internal policy deviation |
| Safety | Hazmat reaches the wrong party, or responders lack emergency information at a spill | A customer's water treatment or sanitation runs short | None |
| Reputation | A producer ends its distribution agreement | Customer complaint | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Order intake and customer verification | High | 48 h | 24 h | 24 h |
| BP-02 Shipment arrangement and hazmat shipping papers | High | 24 h | 8 h | 4 h |
| BP-03 In-transit support and emergency response information | High | 4 h | 1 h | 4 h |
| BP-04 Billing, collections, and supplier payments | Moderate | 120 h | 72 h | 24 h |
| BP-05 Records and compliance administration | Low | 168 h | 120 h | 24 h |

**What drives the values:** safety and the HMR drive BP-02 and BP-03. The 24-hour emergency number is the ERI provider's, so the owner's own 1-hour RTO for BP-03 is about the phone, not the emergency line. BP-01 is High because of what happens when it fails *wrongly* rather than slowly: an order or ship-to change accepted from an impostor can divert an explosive precursor. Integrity, not downtime, drives BP-04. The 4-hour and 24-hour RPOs depend on SYS-01, which **has no backup today** (P01 R-007).

**Single-person dependency (the key finding).** The owner is the only person who can take an order, release a load, change a pickup, answer a carrier, or reach the email, bank, and portals. All MFA codes go to one phone. If the owner is ill, travelling without coverage, or loses the phone while loads are on the road, BP-02 and BP-03 pass their MTD in hours. Actions (P01 R-011, due 2026-12-31):
1. Written standing instruction to each supplier's shipping office: release only against a pickup number issued by the owner, and hold all releases if the owner cannot be reached by phone (also in HSP-01).
2. A reciprocal coverage arrangement with another independent distributor to answer customers and carriers for up to two weeks (no system access; phone and printed load list only).
3. Recovery codes for email, accounting, and bank, plus a one-page access sheet, in a sealed envelope held by the business attorney.
4. A printed list of loads in transit, updated each evening there is a load on the road.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-06 Mobile phone | Carrier, supplier, and ERI provider calls; MFA codes; texts with drivers | BP-01, BP-02, BP-03, BP-04 |
| SYS-01 Email and file suite | Orders, pickup authorizations, BOLs, workbook, SDS library (no backup) | BP-01, BP-02, BP-03, BP-05 |
| SYS-05 Laptop | Main work device (shared with family today) | BP-01, BP-02, BP-04, BP-05 |
| SYS-07 Home network | Internet for the office; phone hotspot is the fallback | All |
| SYS-04 Partner portals | Supplier order portals, carrier bookings and tracking, ERI product list | BP-01, BP-02, BP-03 |
| SYS-02 and SYS-03 | Accounting SaaS and bank portal | BP-04 |
| Contracted services | ERI provider (24-hour line), carriers, suppliers' shipping offices, accountant, IT technician | BP-02, BP-03, BP-04 |
| People | Owner only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Phone and phone number (carrier and ERI provider contact point) | 1 h | Replacement phone from the carrier; printed contact list; ERI provider covers emergencies |
| 2 | Control of the email account | 2 h | Recovery codes in the sealed envelope; provider account recovery; call suppliers to hold releases meanwhile |
| 3 | A clean device | 4 h | Phone for email and portals; laptop rebuilt by the IT technician |
| 4 | Order and shipment workbook and BOL files | 8 h | Rebuild open loads from supplier and carrier portals; printed load list |
| 5 | Partner portals | 8 h | Phone bookings with carrier dispatch |
| 6 | Accounting SaaS and bank portal | 72 h | Bank branch; hold all outgoing payments until access is confirmed clean |
| 7 | Records archive (BOL history, certificates) | 120 h | Request copies from suppliers, carriers, PHMSA, and the training provider |
