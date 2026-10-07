# Business Impact Analysis: Cris Santos Company | Retail Trade | Sole Proprietorship

**Organization:** Cris Santos Company (corner grocery with online and phone ordering) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner, 2026-08-11, with the outside IT helper | **Adopted:** Owner, 2026-09-04

## 1. Overview and purpose
This one-page BIA lists the five business functions the store depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the incident response plan that PCI DSS v4.0.1 Requirement 12.10 expects (N44-45-R01).

## 2. Business description
One owner runs a 1,500-square-foot neighborhood grocery in Florida, open Monday to Saturday, with an unpaid family member at the register about 8 hours a week. Sales are about $180,000 a year, or about $580 per open day. About 60% of sales are by card and about 20% by SNAP EBT, both on one countertop terminal. About 7 online orders and 6 phone orders a week are delivered by the owner. Everything runs on SaaS tools, one tablet, a personal laptop and phone, and an ISP router. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $580 in sales per open day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $2,500 (about a week of gross margin and fees) | $500 to $2,500 | Less than $500 |
| Operations | The store cannot sell to card or EBT customers | Orders or deliveries delayed; shelves partly empty | Administrative delay only |
| Regulatory | Card data compromise or reportable breach; SNAP or merchant agreement issue | Missed filing or PCI deadline | Internal policy deviation |
| Safety | Spoiled food sold or neighbors without access to food | Perishables pulled; delivery customers wait | None |
| Reputation | Neighbors stop shopping here; online reviews about card fraud | Complaints from regular customers | None outside the store |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 In-store sales and checkout | High | 24 h | 4 h | 24 h |
| BP-02 Online and phone orders, pickup and delivery | Moderate | 72 h | 24 h | 24 h |
| BP-03 Purchasing and receiving | Moderate | 72 h | 48 h | 24 h |
| BP-04 Bookkeeping, banking, and taxes | Low | 168 h | 120 h | 24 h |
| BP-05 Customer communications and promotions | Low | 120 h | 72 h | 24 h |

**What drives the values:** the terminal drives BP-01. Without it, about 80% of customers (card and SNAP EBT) cannot pay, so the store loses most of a day's sales after a few hours. The 4-hour RTO is what the processor's replacement-terminal service and a phone hotspot can meet. Perishable deliveries on Tuesday and Friday drive BP-03. The 24-hour RPO for BP-01 and BP-03 is met by the POS app vendor's cloud sync. The 24-hour RPO for BP-04 and BP-05 is **not supported today** for files on the laptop (customer exports, spreadsheets), which have no backup (P01 R-012).

**Single-person dependency (the key finding).** The owner is the only person who can open the store, order stock, drive deliveries, and sign in to any system. The family member can run the register for a few hours but knows no passwords other than the shared POS PIN. The merchant portal's second factor is on the owner's one phone. If the owner is ill, injured, or without the phone, BP-01 to BP-03 all exceed their MTD within three days, and nobody else can reach the processor, the distributor, or online customers. Actions (P01 R-010, due 2026-12-31):
1. Give the family member a separate POS login (not the owner's PIN) and a one-page "open, sell, close" sheet.
2. Store recovery codes for email, the online store, and the merchant portal, plus a one-page emergency contact sheet, in a sealed envelope at the owner's home safe, with a copy held by a trusted relative.
3. Put a "temporarily closed" notice template and the online store's "pause orders" steps on the same sheet.
4. Ask the processor and the distributor how a designated person can act on the account if the owner is incapacitated, and record the answers.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-02 Payment processor services | Countertop terminal (card and EBT), hosted payment page, merchant portal | BP-01, BP-02, BP-04 |
| SYS-03 POS and inventory app | Item scanning, prices, sales totals; vendor backups | BP-01, BP-03 |
| SYS-06 Store network | Internet for the terminal and tablet; phone hotspot is the fallback | BP-01, BP-02 |
| SYS-01 Online store | Catalog, customer accounts, orders | BP-02, BP-05 |
| SYS-05 Laptop and phone | Store administration, merchant portal second factor, texts with customers | BP-02 to BP-05 |
| SYS-04 Email and files | Order notices, invoices, statements (no backup) | BP-02 to BP-05 |
| SYS-07 Accounting SaaS | Books, bank feed | BP-04 |
| Third parties | Processor, POS app vendor, website builder, ISP, distributor, tax preparer | All |
| People | Owner; family member at the register only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and second factor | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Internet in the store | 1 h | Phone hotspot for the tablet; ask the processor whether the terminal can use it |
| 3 | Card and EBT terminal | 4 h | Processor's replacement-terminal service; cash only with a paper tally meanwhile |
| 4 | POS app on the tablet | 4 h | Printed price list; ring sales by hand and enter them later |
| 5 | Online store and phone orders | 24 h | Pause online ordering; take phone orders and key card details only while the customer is on the line |
| 6 | Distributor portal ordering | 48 h | Phone the sales representative |
| 7 | Email, files, accounting | 72 h | Vendor and bank portals; paper copies |
