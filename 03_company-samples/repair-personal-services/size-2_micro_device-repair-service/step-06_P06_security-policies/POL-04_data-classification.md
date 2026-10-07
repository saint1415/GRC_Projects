# Data Classification and Handling Policy (with Customer Device Handling)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Shop Manager (Security and Privacy Lead); Senior Technician for sections 4.4 and 4.7 |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, AC-3, AC-6, MP-2, MP-6, MP-7, SC-28, CP-9, CP-4, SI-12, AU-6, SA-9 |
| CSF 2.0 | ID.AM-01, ID.AM-05, ID.AM-07, ID.AM-08, PR.AA-05, PR.DS-01, PR.DS-10, PR.DS-11, DE.CM-03 |
| Regulatory drivers | N81-R01 (15 U.S.C. 45(a)(1), 45(n)); N81-R02 (Fla. Stat. 501.171(2), (8)); N81-R03 (PCI DSS v4.0.1 3.1.1, 3.2.1, 3.3.1.2, 9.1.1, 9.4.1, 9.4.6, 9.5.1-9.5.1.2); N81-R04 (16 CFR 682.3); N81-BM (NIST SP 800-88 Rev. 2) |

## 1. Purpose
Sort shop and customer information by how much harm its loss or disclosure would cause, set simple handling rules for each level, and set the rules for handling customer devices, card data, retention, and wiping.

## 2. Scope
All workforce members and all information in any form: in SYS-01, email, the bench workstations and bench storage, backups, paper, and every customer device in the shop's custody, including recycling drop-offs.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Shop Manager | Owns this policy; keeps the inventory (4.2); checks card data handling (4.5) and retention (4.6) |
| Senior Technician | Applies the customer device access standard at the bench (4.4); runs sanitization (4.7) and keeps its records |
| MSP | Encryption, backup, restore tests, and network separation, as directed by the Shop Manager |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 **Levels.** Shop and customer information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer device content (photos, messages, health, location, saved passwords); device passcodes; account passwords; card numbers; background check reports; staff passwords and MFA codes | Only where this policy allows; encrypted at rest and in transit; minimum necessary; never in personal accounts, unapproved AI tools, or open ticket notes |
| **Internal** | Customer names and contact details, tickets and repair history, invoices, business account bank details, HR and payroll files, security documents | Workforce and approved vendors only; encrypted in transit |
| **Public** | Price list, opening hours, website | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-05)

4.2 **Inventory.** The Shop Manager keeps a one-page inventory of every shop device (with payment terminal make, model, serial number, and location), every SaaS service, and every place customer information is kept, and updates it when anything changes. (CM-8; ID.AM-01; ID.AM-07; PCI DSS 9.5.1.1)

4.3 **Passcodes and account passwords.** Staff must not ask for a customer's email or cloud account password. If an account sign-in is needed (for example to turn off activation lock), the customer types it in at the counter. A device passcode may be collected only when testing requires it, and only in the SYS-01 restricted passcode field, never in ticket notes or on the paper tag. The field is cleared when the device is released. (AC-3; SI-12; PR.AA-05; Fla. Stat. 501.171(2))

4.4 **Customer device access standard.** While a customer device is in the shop's custody:
- A technician may open only what the repair test checklist for that repair needs (for example, the camera app to test the camera, a sample sound to test the speaker), and must close it straight after.
- Technicians must not open, read, copy, photograph, or forward photos, messages, email, documents, health data, location history, or accounts, except for a data transfer or recovery job the customer ordered in writing, and then only to copy the data, not to view it beyond spot checks the customer agreed to.
- Data transfers and recoveries run only on the data transfer station under the technician's named account, in camera view. Copies go only to the bench storage or a company-issued encrypted USB drive.
- Customer data copies must never go to a personal device, personal account, or unapproved AI tool.
This is the line between good-faith access and a breach under Fla. Stat. 501.171(1)(a). (AC-6; MP-7; PR.DS-10; 15 U.S.C. 45(n))

4.5 **Card data.** Card numbers may be entered only into the P2PE payment terminals. For phone payments, the Counter Associate keys the number directly into a terminal while the customer is on the line. Card numbers and security codes must never be written on paper, typed into SYS-01, email, or chat, or stored anywhere else. If a card number is found anywhere else, it must be reported to the Shop Manager and destroyed (paper in the cross-cut shredder; electronic records deleted and the deletion recorded). Payment terminals must be inspected weekly for tampering (seals, casing, cables, serial number against the inventory), the result logged, and the spare terminal kept locked away. (SI-12; PE-3; MP-6; PCI DSS 3.1.1, 3.2.1, 3.3.1.2, 9.1.1, 9.4.1, 9.4.6, 9.5.1-9.5.1.2)

4.6 **Retention.**

| Information | Kept for | Then |
|---|---|---|
| Customer data copies on the bench storage or USB drives | 30 days after the customer collects the device or receives the data | Deleted; excluded from backups after 30 days |
| Restricted passcode field in SYS-01 | Until the device is released | Cleared at release |
| Paper intake forms | 2 years | Shredded |
| SYS-01 customer and ticket records | While the customer is active, and at most 5 years after the last repair | Deleted or anonymized in SYS-01 |
| AI assistant transcripts (at the vendor) | 30 days, once the vendor terms allow it (P10) | Deleted by the vendor |
| Background check reports | Until the hiring decision is made; the screening vendor's portal copy only after that | Printed copies shredded |

The Shop Manager checks the bench storage and SYS-01 against this table each month. (SI-12; ID.AM-08; Fla. Stat. 501.171(8))

4.7 **Sanitization and disposal (NIST SP 800-88 Rev. 2).** Every recycling drop-off device, retired shop computer, bench storage drive, and USB drive must be sanitized before it leaves the shop or is reused:
- Choose the method by media type and next use, following SP 800-88 Rev. 2 section 3: **Clear** for reuse inside the shop; **Purge** (including cryptographic erase on encrypted phones and drives that support it) before devices leave the shop; **Destroy** when the device cannot be purged or does not power on.
- **Verify** each device after sanitization (SP 800-88 Rev. 2, 4.5.1), for example by checking that the device boots to setup with no accounts and no user data.
- **Record** each device: make, model, serial number or IMEI, method, tool, date, technician, and verification result, using the sample certificate of sanitization in Appendix C as the model.
- The recycler's certificate must list serial numbers, not only the pickup.
- Paper with Restricted information and printed background reports go in the cross-cut shredder. (MP-6; ID.AM-08; Fla. Stat. 501.171(8); 16 CFR 682.3)

4.8 **AI tools.** Customer information may be entered only into AI tools on the approved list. Today the approved list has one entry: the SYS-01 AI assistant (AI-001), approved with the conditions in P10. Public or personal AI chatbots must never receive customer information, device photos showing personal content, or passcodes. (SA-9; PL-4)

4.9 **Monitoring customer data access.** The Shop Manager reviews SYS-01 exports, bulk ticket views, and after-hours sign-ins each month, and the bench session logs once EDR is in place, and records the review on a checklist. (AU-6; DE.CM-03)

4.10 **Encryption and backups.** Restricted information must be encrypted wherever it is stored, including the counter PCs, laptops, bench PCs, and bench storage. Backups must be immutable for their retention period, and the MSP must restore a sample every quarter and give the Shop Manager a written result. (SC-28; CP-9; CP-4; PR.DS-01; PR.DS-11)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Viewing or copying customer device content outside 4.4 is serious misconduct and is handled as a possible breach under POL-03. Compliance is checked through the monthly review (4.9), the weekly terminal log, the sanitization records, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may allow card data outside the P2PE terminals.

## 7. Related documents
POL-02; POL-03; repair test checklists; inventory; sanitization record and certificate template; terminal inspection log; P04 cloud control map; P10 AI risk assessment; NIST SP 800-88 Rev. 2
