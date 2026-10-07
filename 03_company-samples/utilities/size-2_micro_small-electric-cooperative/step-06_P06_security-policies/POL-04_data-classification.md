# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Electric Cooperative, Inc. |
| Policy ID | POL-04 |
| Owner | Office and Finance Manager (Security Coordinator) |
| Approved by | General Manager, 2026-08-31; adopted by the Board of Trustees, 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Yearly (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, SI-12, PL-4 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05 |
| Drivers | Fla. Stat. 501.171(2) and (8); 7 CFR 1730.20 (records of cyber condition), 1730.27(c)(7), 1730.28(c)(4) |

## 1. Purpose
Sort cooperative information by how much harm its loss, change, or disclosure would cause, and set simple handling rules for each level.

## 2. Scope
All staff and all cooperative information in any form: in SCADA, the AMI head-end, the business suite, email and the shared drive, the backup vault, on devices, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office and Finance Manager (Security Coordinator) | Owns this policy; keeps the information inventory; approves new tools |
| Line Superintendent | Keeps the OT inventory and the settings library; owns settings backups and restore tests |
| MSP | Office encryption, vault administration, restore tests, and device wiping, as directed |
| All staff | Handle information according to its level |

## 4. Policy statements
4.1 Cooperative information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Member Social Security numbers, bank account numbers, the medical-needs list; passwords, MFA codes, and device passwords; SCADA point lists, recloser, regulator, and RTU settings, network and modem details; the security sections of the VRA and ERP | Only in approved systems (4.3); encrypted at rest and in transit; shared only with those who need it; never in personal accounts or public AI tools |
| **Internal** | Member names, addresses, phone numbers, and usage data; payroll and HR files; contracts; circuit maps; outage records; security documents not listed above | Staff and approved vendors only; encrypted in transit |
| **Public** | Rates, outage map as published, newsletters, Board meeting notices | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, on every laptop, workstation, tablet, and phone that holds it, and whenever it is sent outside the cooperative's systems. Settings files and network details may be sent to a vendor only through the vendor's support portal or an encrypted link, never as a plain email attachment. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 Restricted information may be kept only in: the business suite, SCADA, the AMI head-end, the productivity suite (email and the shared drive, in folders limited by group), the backup vault, the cooperative's password manager, and the Line Superintendent's encrypted laptop (settings files). Social Security numbers belong in the CIS only. (AC-3)

4.4 The Security Coordinator and the Line Superintendent must keep a one-sheet inventory of every device (including each RTU, recloser and regulator control, gateway, modem, and collector with its model and firmware version), every SaaS service, and every place Restricted information is stored, and update it after any change. (CM-8; ID.AM-01; ID.AM-07; 7 CFR 1730.27(c)(7))

4.5 Before any new vendor, add-on, app, or device receives Restricted information or connects to SCADA or AMI, the Security Coordinator must approve it, the vendor terms in POL-02 A.5 must be in place, and it must be added to the inventory. Trials and free tools are included. (SA-9; GV.SC-05)

4.6 **AI tools.** Restricted or Internal information may be entered only into AI tools on the approved list. Today the list has one entry: the AMI vendor's peak-forecasting add-on, for aggregated interval data, after the data-use addendum is signed and under the P10 conditions (human approval of every load-control event). Public or personal generative AI chatbots must never receive member data, SCADA screens, settings, or network details. (SA-9; PL-4)

4.7 **Backups.** The shared drive must be copied nightly and the CIS export weekly to the vault. Recloser, regulator, and RTU settings and the SCADA point database must be copied to the vault after every change, and at least monthly. Vault copies must be kept at least 90 days in storage that cannot be changed or deleted within that period, and the vault administrator login must use MFA. Every quarter the Line Superintendent must restore one device's settings to the spare recloser control and the MSP must restore a sample of files, each with a written result. (CP-9; CP-4; PR.DS-11; 7 CFR 1730.28(c)(4))

4.8 **Disposal.** Devices and media that held Restricted information, including replaced recloser controls, modems, and meters with stored settings, must be wiped or reset to factory settings before reuse or disposal, or destroyed by a vendor that provides a certificate. Paper with Restricted information goes in the locked shred bin. The Security Coordinator keeps each record. (MP-6; ID.AM-08; Fla. Stat. 501.171(8))

4.9 **Retention.** Membership applications, including scans, must be kept only as long as the cooperative's records retention schedule requires (for example, while the member's deposit decision may be reviewed) and then destroyed under 4.8. Scans of applications from former members past that period must be deleted by 2026-12-31. Security records follow POL-02 A.7. (SI-12; Fla. Stat. 501.171(8))

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report, the quarterly restore results, the inventory review at each risk register update, and the yearly assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.9.

## 7. Related documents
POL-02; POL-03; the information and OT inventory; the settings library; P04 cloud control map; P10 AI risk assessment; records retention schedule
