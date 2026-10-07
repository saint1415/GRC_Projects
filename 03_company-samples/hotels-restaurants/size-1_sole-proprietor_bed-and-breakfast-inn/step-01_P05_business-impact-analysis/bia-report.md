# Business Impact Analysis: Cris Santos Company | Accommodation and Food Services | Sole Proprietorship

**Organization:** Cris Santos Company (six-room bed-and-breakfast inn) | **Tier:** Sole Proprietorship (owner-innkeeper only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-innkeeper, 2026-07-22, with the on-call IT consultant (under a confidentiality agreement since 2026-07-17) | **Adopted:** Owner-innkeeper, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the inn depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the incident response plan's business recovery content that PCI DSS v4.0.1 Requirement 12.10 expects (N72-R01).

## 2. Business description
One owner runs a six-room bed-and-breakfast inn in a restored historic house in a small Florida coastal town and lives on site. There are about 600 stays a year. Reservations, payments, guest messages, and door codes all run through the innkeeping software (SYS-01) and the payment facilitator (SYS-02), with two OTA portals feeding bookings. Everything else runs on one laptop and one phone, a consumer email account, an accounting SaaS, and a single router that also serves guest Wi-Fi. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue: about $490 a day on average and up to about $930 a night when all six rooms are full.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $2,500 (about three full peak nights, or relocation of several guests) | $500 to $2,500 | Less than $500 |
| Operations | Guests cannot be checked in or let into rooms, or rooms are double sold | Bookings or messages delayed; manual workarounds needed | Administrative delay only |
| Regulatory and contractual | Reportable breach; card data compromise reported to the payment facilitator | Missed PCI validation or tax deadline | Internal policy deviation |
| Safety | A guest cannot enter or lock a room at night, or a stranger can | Delayed but safe service | None |
| Reputation | OTA ranking penalty or a run of public reviews about a security problem | A few guest complaints or reviews | None outside the inn |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Reservations and distribution | High | 24 h | 8 h | 1 h |
| BP-02 Guest arrival, stay, and room access | High | 8 h | 4 h | 1 h |
| BP-03 Payments and deposits | Moderate | 72 h | 24 h | 24 h |
| BP-04 Guest communications | Moderate | 24 h | 8 h | 24 h |
| BP-05 Bookkeeping, taxes, and administration | Low | 120 h | 72 h | 24 h |

**What drives the values:** guest safety drives BP-02, because door codes come from reservation data and guests must be able to enter and lock their rooms at any hour. Double selling through the OTAs drives BP-01. Payments (BP-03) tolerate three days because most deposits are already captured and balances can be taken at departure. The 1-hour RPO for BP-01 and BP-02 depends on the innkeeping vendor's backups (RTO 4 hours and RPO 1 hour in its SOC 2 system description; reviewed in P09). The 24-hour RPO for BP-05 is **not supported today** for laptop files, which have no backup (P01 R-015).

**Single-person dependency (the key finding).** The owner is the only person who knows every password, the only one who receives the sign-in codes on the phone, and the only one who deals with vendors, the payment facilitator, and the OTAs. The relief innkeeper can keep the inn running today only because the owner shares logins, which is itself a security gap (P01 R-005). If the owner is ill, evacuating for a hurricane, or without the phone, BP-01, BP-02, and BP-04 exceed their MTD within a day. Actions (P01 R-010, due 2026-12-31):
1. Give the relief innkeeper a **named account** with front desk rights in the innkeeping software and OTA-2, so continuity no longer depends on shared passwords.
2. Store recovery codes for the innkeeping software, email, OTAs, and payment facilitator, plus a one-page emergency access sheet, in a sealed envelope held by the owner's attorney.
3. Agree in writing with a nearby inn to take relocated guests if the inn must close.
4. Ask the innkeeping vendor and the payment facilitator how a designated person can get account access if the owner is incapacitated, and record the answers.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Innkeeping software (vendor SaaS) | Calendar, profiles, register, booking engine, channel manager, messaging, door codes; vendor backups | BP-01, BP-02, BP-03, BP-04 |
| SYS-08 Mobile phone | Sign-in codes; payment app and reader; OTA apps; calls and texts | BP-01, BP-02, BP-03, BP-04 |
| SYS-10 Smart door locks | Per-reservation codes; master code; mechanical override keys | BP-02 |
| SYS-02 Payment facilitator | Card processing and vault; mobile reader | BP-03 |
| SYS-03 OTA portals | Bookings and guest messages from two OTAs | BP-01, BP-04 |
| SYS-09 Inn network | Internet for the owner and guests; phone hotspot is the fallback | BP-01, BP-02, BP-04 |
| SYS-07 Laptop | Main work device; the phone is the spare | BP-01, BP-03, BP-05 |
| SYS-04 Email and files; SYS-05 accounting | Correspondence, documents (no backup), books | BP-04, BP-05 |
| People | Owner-innkeeper; relief innkeeper; cleaning service; bookkeeper | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and sign-in codes | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Room access for guests on site | 1 h | Mechanical override keys from the lockbox; new codes set in the lock app from the phone |
| 3 | Internet in the house | 1 h | Phone hotspot |
| 4 | SYS-01 innkeeping software access | 4 h (vendor-hosted) | Printed 14-day arrivals list; close availability in the OTA portals |
| 5 | A clean work device | 8 h | Phone; laptop reinstalled by the IT consultant |
| 6 | SYS-02 payments | 24 h | Take balances at departure |
| 7 | SYS-04 email and files; SYS-05 accounting | 72 h | Vendor portals; paper copies |
