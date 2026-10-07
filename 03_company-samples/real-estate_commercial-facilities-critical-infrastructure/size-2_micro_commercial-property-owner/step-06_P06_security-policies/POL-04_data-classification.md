# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Property Manager (security and privacy lead) |
| Approved by | Managing Member, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes |
| Implements (SP 800-53 Rev. 5) | RA-2, CM-8, MP-6, SC-28, CP-9, CP-4, SA-9, SI-12, PE-3 |
| CSF 2.0 | ID.AM-01, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| Benchmark and obligations | CISA CPG 2.0 goals 2.A, 3.K, 3.O, 3.P (voluntary); PCI DSS v4.0.1 3.1.1, 3.2.1, 3.3.1.2, 9.1.1, 9.4.1, 9.4.6, 9.5.1 to 9.5.1.3; Fla. Stat. 501.171(2) and (8); 16 CFR 682.3(a); 15 U.S.C. 45(a) |

## 1. Purpose
Sort company information by how much harm its loss, change, or disclosure would cause, and set simple handling rules for each level, including for building system data, video, and card data.

## 2. Scope
All employees and contractors, and all company information in any form: in the SaaS systems, the access control and video platform, the BAS, on devices, on paper, and in any vendor's system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Property Manager | Owns this policy; keeps the device and data inventory; approves new tools and features (with POL-02 A.9) |
| Building Engineer | Keeps BAS backups and controller program copies; inventory of building devices |
| Bookkeeper | Card terminal inspections and card data rules |
| Tenant Services and Leasing Coordinator | Applicant and guarantor files: storage, retention, and disposal |
| MSP | Encryption, backup, restore tests, and device wiping, as directed by the Property Manager |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Company information has three levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Social Security numbers, driver license copies, credit reports, and financial statements of applicants and guarantors; employee payroll data; tenant bank details; passwords and MFA codes; any face templates or other biometric data; BAS and door system passwords and network diagrams | Only in approved locations (4.3); encrypted at rest and in transit; only staff who need it; never in personal accounts or public AI tools |
| **Confidential** | Credential holder lists, badge photos, and door access history; video; lease terms; floor plans and BAS graphics; contracts; security documents | Staff and approved vendors only; encrypted in transit; shared outside the company only with Property Manager approval or a legal request |
| **Public** | Building address and hours, marketing brochures, available space listings | No restriction |

When unsure, treat information as Restricted. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted wherever it is stored, on every device that holds it, and whenever it is sent outside company systems. Applications and guarantor documents must not be sent or received by plain email; applicants upload them through the property management system's secure upload or a suite link restricted to named people. (SC-28; PR.DS-01; PR.DS-02; CPG 3.K)

4.3 Restricted information may be kept only in: the property management system, the payroll service, the tenant screening service, the restricted leasing folder in the shared drive (access limited to the Tenant Services and Leasing Coordinator and the Managing Member, and excluded from desktop sync), and the cloud backup. (AC-3; Fla. Stat. 501.171(2))

4.4 The Property Manager and Building Engineer must keep one inventory of every device and service: office computers, tablets, the BAS workstation, supervisory and field controllers, door controllers, cameras, network devices, and the card terminal (make, model, location, serial number, firmware), plus every place Restricted information is stored. It is updated when anything is added, moved, or removed. (CM-8; ID.AM-01; CPG 2.A; PCI DSS 9.5.1.1)

4.5 Before any new vendor, app, device, or platform feature receives company information, it must be approved under POL-02 A.9, its agreement must include the security addendum (POL-02 A.5), and it must be added to the inventory. (SA-9; GV.SC-05)

4.6 **AI and analytics features.** Video analytics, face matching, and any other AI feature may be used only if it is on the approved list kept by the Property Manager and approved by the Managing Member after a P10 assessment. Today the list has one entry: person detection alerts on the Property B rear corridor and parking cameras after hours (AI-002). Face match (AI-001) is not approved until the P10 conditions are met. Public or personal AI chatbots must never receive Restricted or Confidential information. (CM-7; SA-9; 15 U.S.C. 45(a))

4.7 **Backups.** The BAS workstation and the shared drive must be backed up nightly, with versions kept at least 90 days in storage that cannot be changed or deleted within that period, behind a console that requires MFA. The controls contractor must give the Building Engineer a copy of every field controller and supervisory controller program after each change, kept in the backup. Every quarter the MSP must restore a sample of the shared drive and restore the BAS workstation image to the spare laptop, with the Building Engineer checking that the BAS front end opens, and give the Property Manager a written result. (CP-9; CP-4; PR.DS-11; CPG 3.O)

4.8 **Retention and disposal.** Applications and screening reports of applicants who do not sign a lease are kept 1 year and then destroyed. Guarantor documents are kept until 1 year after the lease and any guaranty end. Video is kept 30 days unless the Property Manager places it on hold for an incident, claim, or legal request. Paper with Restricted information is cross-cut shredded; electronic copies are deleted and the trash emptied; devices are wiped or destroyed by a vendor that gives a certificate. The Tenant Services and Leasing Coordinator keeps a disposal record. (MP-6; SI-12; ID.AM-08; Fla. Stat. 501.171(8); 16 CFR 682.3(a))

4.9 **Card data.** Card data may be handled only on the P2PE terminal. Staff must never write card numbers or security codes on paper or type them into a computer, email, or the property management system; phone orders are keyed directly into the terminal during the call. The Bookkeeper inspects the terminal weekly against the P2PE Instruction Manual checklist and records the result, and the 3 staff who use the terminal are trained to spot tampering at hire and yearly. Any card data found on paper or in email must be reported (POL-03) and destroyed. (PE-3; MP-6; PCI DSS 3.1.1, 3.2.1, 3.3.1.2, 9.1.1, 9.4.1, 9.4.6, 9.5.1 to 9.5.1.3)

4.10 **Video and access history requests.** Footage and door history are released outside the company only to law enforcement with a written request, to the company's insurer or counsel, or to a tenant about its own premises or staff with the Property Manager's approval. Each release is logged. (AC-3; PR.DS-01)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Compliance is checked through the monthly MSP report (encryption and backup status), quarterly restore results, the weekly terminal checklist, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.10.

## 7. Related documents
POL-02; POL-03; device and data inventory; P04 cloud control map; P10 AI risk assessment; P2PE Instruction Manual (PIM) for the terminal
