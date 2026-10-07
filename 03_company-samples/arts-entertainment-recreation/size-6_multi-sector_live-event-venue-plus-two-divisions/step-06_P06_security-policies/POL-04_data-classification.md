# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, SI-12, MP-6, SC-28, PT-2, PT-3, PT-5, AC-21 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, GV.OC-03 |
| PCI DSS v4.0.1 | Requirements 3.1 to 3.4, 9.4 |
| Division supplements | Hotels and Restaurants: identity documents and card authorization forms. Ticketing and Streaming: client data. Live Venues: CCTV and face templates |

## 1. Purpose
Classify group data so that each type gets protection matched to its harm if disclosed, and so that data is used only for its registered purposes.

## 2. Scope
All data the group creates, receives, stores, or transmits, in any form, including data the ticketing platform processes for clients.

## 3. Classification levels
| Level | Examples | Handling |
|---|---|---|
| **Restricted: card data** | Full card numbers, security codes, track data | Only in the CDE or validated P2PE devices; never in email, chat, tickets, or paper; security codes never stored after authorization |
| **Restricted: sensitive personal data** | Identity document numbers, face templates, email with password, precise geolocation | Encrypted; access by named role; purpose registered; retention limit set |
| **Confidential: client data** | Client tenants' patron and order data | Processed only for the client under its agreement; never pooled across clients without contract permission |
| **Confidential** | Patron, guest, and subscriber contact and order data; employee data; contracts | Encrypted at rest; role-based access |
| **Internal** | Policies, schedules, internal reports | Workforce only |
| **Public** | Event listings, published prices, press releases | Approved for release |

## 4. Policy statements
4.1 Every dataset in group systems must have an owner, a classification, and a registered purpose in the data catalog. (RA-2; PT-2; ID.AM-05)

4.2 Card data must be handled only as the Restricted card data row allows. Card numbers received outside the CDE (for example in email or on paper) must be destroyed within 1 business day and the sender asked to use a payment link. (SI-12; MP-6; PCI DSS 3.2, 3.3)

4.3 **Minimization.** A feed from a division system to a group platform must carry only the data elements its registered purposes need. Identity document numbers must not leave the system that collected them. (PT-2; PT-3; AC-21)

4.4 **Client data.** Client tenants' data may be used for another client or for group purposes only where the client's agreement permits it, and only in aggregated form where the agreement says so. (PT-2; GV.OC-03)

4.5 Restricted data must be encrypted in transit and at rest with keys under group control. (SC-28; PR.DS-01; PR.DS-02)

4.6 **Privacy notices.** Each division's privacy notice must describe the data it collects (including tags on its web pages and bot detection signals), its purposes, and its sharing, and must be reviewed whenever a new data use is registered. (PT-5)

4.7 **Retention.** Each dataset follows the group retention schedule. Defaults: patron accounts deleted after 5 years of inactivity; CCTV video 30 days unless held for an investigation; face templates deleted within 24 hours of the event or on withdrawal of consent, whichever is sooner; bot detection evidence for blocked sessions and cancelled orders 12 months. (SI-12)

4.8 Media and paper with Restricted or Confidential data must be destroyed by cross-cut shredding or NIST SP 800-88 sanitization, including consumer report information under 16 CFR 682.3. (MP-6; PCI DSS 9.4.6, 9.4.7)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through data discovery scans, catalog reviews, and the P07 assessment.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may permit storage of security codes or sharing of client data beyond its agreement.

## 7. Related documents
POL-01; POL-05; group retention schedule; `division-supplements.md`.
