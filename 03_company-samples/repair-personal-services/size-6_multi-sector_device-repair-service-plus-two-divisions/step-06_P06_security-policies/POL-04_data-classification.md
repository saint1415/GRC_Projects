# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, PT-2, PT-3, AC-3, AC-6, AC-21, MP-4, MP-6, MP-7, SC-8, SC-28, CP-9, SI-12 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory drivers | N81-R01 (15 U.S.C. 45(a)(1), 45(n)); N81-R02 (Fla. Stat. 501.171(2), (8)); N81-R03 and N44-45-R01 (PCI DSS v4.0.1 Req. 3, 9.4); N81-R04 (16 CFR 682.3); N54-R06 (45 CFR 164.310(d); 164.312(a)(2)(iv)); NIST SP 800-88 Rev. 2 (method) |
| Division supplements | Device Repair: passcode handling, bench access, data recovery, sanitization. Electronics Retail: trade-in records. IT Support: customer credentials and ePHI |

## 1. Purpose
Classify group information by sensitivity and set handling rules, especially for the things a repair and support group holds that other businesses do not: customers' devices, their passcodes, and their content.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, and all customer devices and storage media in the group's custody, including trade-in and recycling devices.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes, purposes, retention, and the customer data access standard |
| Device Repair chief operating officer | Owns bench handling, the sanitization standard, and device custody |
| Data owners | Classify data and approve access and sharing |
| All workforce | Handle information and devices according to their class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (cardholder data, customer passcodes and account credentials, customer device content, ePHI, managed customers' credentials, background check reports, keys), **Confidential**, **Internal**, or **Public**. Every customer device in custody is treated as holding Restricted information. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest and in transit with approved algorithms and group-managed keys. (SC-28; SC-8; PR.DS-01; PR.DS-02; 164.312(a)(2)(iv))

4.3 **Passcodes.** Collect a device passcode only when the repair cannot be done without it, record it only in the STPP passcode vault (never in notes, chat, email, or on paper tags), and purge it 7 days after release. **Do not collect account passwords.** When a repair needs an account sign-in, the customer enters it on the device at the counter. (PT-2; PT-3; SC-28(1); SI-12; Fla. Stat. 501.171(1)(g)1.b.)

4.4 **Card data.** Payment card numbers must be entered only into P2PE terminals or the processor's hosted payment fields. Workforce members must never write, type, or record a card number or card code anywhere else. Any found must be destroyed at once and reported. (SI-12; MP-4; PCI DSS 3.2.1, 3.3.1.2, 9.4)

4.5 **Retention.** Tickets: 7 years. Passcode vault: 7 days after release. Recovered customer data: 30 days after delivery, then deleted, including download links. Data transfer caches on benches: wiped at session end. Chat transcripts: 90 days, with passcode patterns redacted before storage. Trade-in identity records: the period counsel confirms. (SI-12; Fla. Stat. 501.171(8))

4.6 **Customer data access standard.** Technicians may open only the device functions a repair or test needs, using approved test applications where available. Browsing, copying, or photographing customer content (photos, messages, files, health or location data) is prohibited unless the customer asked for a data service and the ticket records it. Bench sessions must be logged, and USB storage must be blocked except for approved data transfer stations. Every technician must sign this standard. (AC-6; MP-7; PS-6; PR.DS-10; 15 U.S.C. 45(n); Manufacturer A agreement)

4.7 **Sanitization.** Devices and media leaving the group's custody for resale, recycling, or disposal must be sanitized under the group sanitization standard based on **NIST SP 800-88 Rev. 2** (clear, purge, or destroy by media type, with IEEE 2883 for technique), verified (SP 800-88 Rev. 2 section 4.5.1), and recorded on a per-device certificate based on Appendix C, by serial number. Drop-off devices must be recorded by serial number at intake. (MP-6; ID.AM-08; Fla. Stat. 501.171(8); 164.310(d)(2)(i)-(ii))

4.8 Background check reports must be kept only in the HR system and printed copies shredded. (MP-6; 16 CFR 682.3)

4.9 Backups of Restricted information must be immutable, held with a different provider or account from production, and restore-tested at least quarterly for High-criticality systems. (CP-9; PR.DS-11; 164.308(a)(7)(ii)(A))

4.10 Restricted information must not be sent to any AI service unless the service is approved under the Group AI Standard with terms that prohibit training on group or customer data and limit retention. Free-text ticket notes must not be sent to AI services. (SA-9; AC-21; AC-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-3, AC-6, MP-6, MP-7, PT-3, SI-12), quarterly data discovery scans, and sanitization verification records.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may permit card data outside P2PE terminals or hosted payment fields.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP for the STPP; group sanitization standard (2026); Group AI Standard (P10).
