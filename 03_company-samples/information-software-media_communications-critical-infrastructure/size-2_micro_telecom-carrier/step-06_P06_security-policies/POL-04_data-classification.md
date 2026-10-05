# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Office Manager (security and compliance lead) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, PT-3, AC-3, CM-8, MP-6, SC-8, SC-28, CP-9, CP-4, SA-9, PL-4, SI-12 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11, GV.SC-05 |
| Regulatory drivers | C-COMMUNICATIONS-R01: 47 U.S.C. 222; 47 CFR 64.2005, 64.2007, 64.2009(a). C-COMMUNICATIONS-R03: 47 CFR 1.20003, 1.20004. Fla. Stat. 501.171 |

## 1. Purpose
Sort company information by how much harm its loss or disclosure would cause, set simple handling rules for each level, and limit how CPNI may be used.

## 2. Scope
All workforce members of Cris Santos Company, the MSP, the consultant, and vendors, and all company information in any form: in the BSS, the voice platform, the hut servers, network devices, email, the shared drive, on tablets and paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Owns this policy; keeps the inventory of systems and data locations; approves new tools and vendors |
| Network Operations Lead | Network configurations, configuration backups, and device disposal |
| Owner and General Manager | Lawful-intercept information |
| MSP | Encryption, backup, and wiping of office devices, as directed |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | CPNI (call detail records, voice features and plans, voice bill lines); **the whole customer account record**, including broadband data, by company choice; driver license numbers; portal credentials and PINs; lawful-intercept orders and records; network configurations, device passwords, API keys; incident records | Only in approved systems (4.4); encrypted at rest and in transit; need to know; never in personal accounts or public AI tools |
| **Internal** | Contracts, vendor reports, policies, outage tickets without customer details, payroll and HR files | Workforce and approved vendors only; encrypted in transit |
| **Public** | Prices, broadband labels, outage map, website | No restriction |

When unsure, treat information as Restricted. Broadband data is not CPNI under current law, but the company protects it as if it were because it sits in the same account record. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, including hut servers, desktops, laptops, and tablets, and whenever it is sent. Network devices must be managed over encrypted protocols (SSH and SNMP version 3) once the OLT upgrade allows it, and by 2026-12-31 at the latest. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 **Use of CPNI.** CPNI may be used only as 47 CFR 64.2005 allows without approval: to provide and bill the customer's service, to market offerings within the voice service the customer already buys, and to protect against fraud. CPNI must **not** be used to market broadband or any other service, or be shared with anyone for marketing, unless the company first adopts the approval, notice, record, and supervisory review rules of 64.2007 to 64.2009 in an approved update to this policy. Until then, every account is treated as having **no CPNI approval**, and any tool or AI feature that would use CPNI for offers must stay turned off. (PT-3; AC-3; 64.2005; 64.2007(b); 64.2009(a))

4.4 Restricted information may be kept only in: the BSS, the voice platform, the hut servers, network devices, the productivity suite (in folders limited to the people who need it), the password manager, the cloud backup, and the locked lawful-intercept cabinet. Exported customer lists or CDR files must be deleted within 30 days of the task they were made for. (AC-3; PR.DS-01)

4.5 The Office Manager must keep a one-page inventory of every device, every SaaS service, and every place Restricted information is stored, and update it when anything is added or removed. (CM-8; ID.AM-01; ID.AM-07)

4.6 Before any new vendor, app, or device receives Restricted information, the Office Manager must approve it, the contract must meet POL-02 A.5, and it must be added to the inventory and the third-party CPNI access register. (SA-9; GV.SC-05; 64.2009(c))

4.7 **AI tools.** Restricted information may be entered only into AI tools on the approved list. Today the list has one entry: the BSS vendor's portal assistant, for signed-in customers only, under the P10 conditions. Public or personal AI chatbots must never receive Restricted information. (SA-9; PL-4)

4.8 **Collect less.** The company stops recording driver license numbers in the BSS on 2026-10-01. Identity is checked by looking at the license, and only "ID checked" and the date are recorded. Stored driver license numbers must be purged by 2026-11-30. (SI-12; PR.DS-01)

4.9 **Backups.** Network configurations must be backed up nightly to the hut server and copied, encrypted, to the cloud backup, with at least 90 days of versions. The Network Operations Lead must restore an OLT and a router configuration to the spare chassis twice a year and record the result. (CP-9; CP-4; PR.DS-11)

4.10 **Disposal.** Office devices must be wiped by the MSP or destroyed with a certificate. Returned ONTs and replaced OLT cards and router parts must be reset to factory settings before reuse or scrap, and the Network Operations Lead keeps a disposal log. Paper with Restricted information goes in the locked shred bin. (MP-6; ID.AM-08)

4.11 **Lawful-intercept information.** Court orders, intercept records, and anything that reveals that an intercept exists are seen only by the Owner and General Manager and, when technically needed, the Network Operations Lead. They are kept in the locked cabinet and never in email, the shared drive, or the BSS. (AC-3; 1.20003(b); 1.20004)

4.12 **Retention.** Customer account records follow the company's records schedule. CPNI and security records follow POL-02 A.8. Call detail kept by the voice platform is limited to 18 months unless a legal hold applies. (SI-12; GV.PO-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly review (POL-02 B.5), the twice-yearly restore test, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.10. No exception may permit CPNI marketing use without approval.

## 7. Related documents
POL-02; POL-03; inventory of systems and data; third-party CPNI access register; CALEA SSI policies; P04 cloud control map; P10 AI risk assessment
