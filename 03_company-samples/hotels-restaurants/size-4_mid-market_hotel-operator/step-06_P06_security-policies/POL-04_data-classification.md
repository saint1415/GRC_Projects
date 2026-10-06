# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | General Counsel |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, SC-8, SC-28, SI-12, MP-4, MP-6, SA-9, CM-8, SR-10 |
| CSF 2.0 | ID.AM-05, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, GV.SC-05 |
| PCI DSS v4.0.1 | 3.2, 3.3.1, 3.4.1, 4.2, 9.4, 9.5.1, 12.10.7 |
| Other drivers | Fla. Stat. 509.101(2) and 501.171(8); 16 CFR 682.3; 15 U.S.C. 1681c(g) |
| Supporting standards | STD-04 Payment device and card data handling (including the retention schedule); STD-08 Encryption |

## 1. Purpose
Classify company information so that the most sensitive data (card data, ID numbers, biometric data) is kept only where it must be, for only as long as it must be, and protected everywhere it goes.

## 2. Scope
All information the company creates, receives, or holds, on any system or on paper, including information held for the franchisor and (from 2027) for hotel owners.

## 3. Classes
| Class | Examples | Handling summary |
|---|---|---|
| **Restricted** | Card numbers and any security code; government ID numbers and ID scans; biometric data (finger templates); passwords and keys | Only in approved systems (SYS-01 vault, P2PE devices, payment gateways, HR vendor); never in email, chat, text, files, recordings, or paper; encrypted; access by approved role only |
| **Confidential** | Guest profiles, stay history, guest register, call recordings, CCTV video, employee records, background checks, contracts, non-public rates and occupancy | Approved systems only; shared with vendors only under contract; retention schedule applies |
| **Internal** | Procedures, schedules, internal reports | Company systems only |
| **Public** | Published rates (with total price), website content | Approved for release |

## 4. Policy statements
4.1 Every system and data store must be classified by its highest class of data and recorded in the inventory. (RA-2; ID.AM-05)
4.2 Card data must only be stored in the SYS-01 vault, the franchisor's vault, or the payment providers' systems. It must never be stored in email, chat, text messages, files, call recordings, or on paper, and sensitive authentication data (security codes, track data, PINs) must never be kept after authorization. (SI-12; MP-4; PCI DSS 3.2, 3.3.1)
4.3 Card numbers must be masked when displayed (first 6 and last 4 digits at most) except for roles with the approved display permission. Printed receipts show no more than the last 4 digits and no expiration date. (AC-3; PCI DSS 3.4.1; 15 U.S.C. 1681c(g))
4.4 Card numbers received through any other channel (an emailed form, a chat or text message, a spoken number captured by a recording) must be deleted promptly, the sender directed to a payment link, and the event reported under POL-03 4.11. (IR-4; SI-12; PCI DSS 12.10.7)
4.5 Restricted and Confidential data must be encrypted in transit outside company networks and at rest on laptops, removable media, and cloud storage, as STD-08 requires. (SC-8; SC-28; PCI DSS 4.2)
4.6 **Retention schedule (STD-04).** The guest register is kept at least 2 years (Fla. Stat. 509.101(2)) and then for no more than 3 more years; ID scans are deleted 30 days after check-out; call recordings are kept 90 days; CCTV 30 days unless held for an incident; guest marketing profiles are deleted after 3 years without a stay or contact. Records past their retention period must be destroyed. (SI-12; Fla. Stat. 501.171(8))
4.7 Paper and media must be destroyed by cross-cut shredding or certified wiping, with certificates from disposal vendors. Background-check reports are destroyed the same way. (MP-6; PCI DSS 9.4.6, 9.4.7; 16 CFR 682.3)
4.8 Restricted or Confidential data must not be entered into any AI tool that is not on the approved-tools list, and approved tools may receive it only under contract terms that forbid training on company data and set retention (P10). (SA-9; PL-4)
4.9 Guest data may be shared with a vendor or the franchisor only under a contract that states the purpose, and only the minimum needed (for example, the revenue-management system receives aggregated data without guest names). (SA-9; GV.SC-05)
4.10 Every payment device must be on the device list with its serial number and location, inspected for tampering at least weekly (or at the frequency set by a targeted risk analysis), and replaced only through the approved channel. (CM-8; SR-10; PCI DSS 9.5.1)

## 5. Compliance and enforcement
Quarterly data discovery scans of mailboxes and file shares check 4.2. P07 and the QSA-supported assessment test 4.2, 4.3, 4.7, and 4.10. Violations are handled under POL-01 4.15.

## 6. Exceptions
None for statement 4.2. Others under POL-01 4.7.

## 7. Related documents
POL-01; POL-03; POL-05; STD-04; STD-08; P03 rows G-010, G-067, G-069, G-100; P10
