# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Policy ID | POL-04 |
| Owner | Group CISO, with the fleet security director for the regulated categories |
| Approved by | Group CISO; noted by the board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-3, MP-4, MP-6, AC-3, AC-21, SC-8, SC-28, SI-12 |
| CSF 2.0 | ID.AM-05, ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10 |
| Regulatory drivers | C-NUCLEAR-S01 (73.22); C-NUCLEAR-S02 (73.56(m), (o)); C-NUCLEAR-S06 (37.43(d), 37.31); C-NUCLEAR-R04 (CIP-011-3); C-NUCLEAR-S09 (810.2); C-NUCLEAR-S11 |

## 1. Purpose
Tell every worker which information is restricted by regulation, where it may live, and how it is marked and handled.

## 2. Scope
All group information in any form, and information held for customers and clients.

## 3. Classification levels
| Level | Examples | Where it may be stored or processed |
|---|---|---|
| **Regulated: Safeguards Information** | Security plans, CDA lists that the SGI program determines are SGI, alarm layouts, response details (73.22(a)) | **Only** SGI stand-alone systems and locked containers (73.22(c), (g)). Never on SYS-G1 to SYS-G3, the WMS, email, or a networked printer or scanner |
| **Regulated: CSP program information** | CSPs, CDA inventories, CDA assessments | The CST program network. Never in the WMS or group cloud |
| **Cyber security sensitive** | CDA identifiers, firmware versions, and network details in work packages; one-way device and kiosk configurations | The restricted CDA module of the WMS and approved engineering repositories, readable only by approved roles |
| **Regulated: access authorization and Part 37** | 73.56 files; Part 37 security plan, procedures, and approved lists; background reports | Program-owned restricted repositories only (73.56(m); 37.43(d); 37.31) |
| **Regulated: other** | BES Cyber System Information (CIP-011-3); Part 810 controlled technology; FCI under DOE contracts; dose records | The repository each program approves |
| **Confidential** | Personal information, customer data, contracts, financials | Approved group systems with encryption |
| **Internal** | Procedures, schedules not otherwise restricted | Group systems |
| **Public** | Approved publications | Anywhere |

## 4. Policy statements
4.1 Every information owner must classify information at creation. The SGI program owner makes SGI determinations; the fleet cyber security program manager decides what is cyber security sensitive. (RA-2; ID.AM-05)

4.2 SGI must be marked as 73.22(d) requires. Cyber security sensitive information must carry the WMS "cyber security sensitive" label once it is available (due 2026-12-31). (MP-3; PR.DS-01)

4.3 **Reproduction.** SGI may be copied only on equipment the SGI program has evaluated under 73.22(e). Networked printers, scanners, and multifunction devices are never evaluated for SGI. (MP-6; CM-6)

4.4 Uploads to the WMS and engineering collaboration systems must be scanned automatically for SGI markings. Any SGI found on a networked system is a reportable internal event to the SGI program owner and is removed and sanitized under 73.22(g)(4). (SI-4; MP-6)

4.5 External transmittals of work packages and drawings must be screened for cyber security sensitive content before release. (AC-21; PR.DS-02)

4.6 Confidential and regulated information must be encrypted in transit and at rest on group systems. (SC-8; SC-28; PR.DS-01; PR.DS-02)

4.7 Records must be kept for the longest period any applicable rule requires (for example 73.54(h); 73.56(o); 37.43(d)(8); 264.73; 20.2106) and then destroyed by a method that prevents reconstruction. (SI-12; MP-6)

4.8 Data held for customers (dose records) and clients (engineering data) must stay in the division system built for it and be returned or destroyed as each contract requires. (AC-3; MP-6)

## 5. Compliance and enforcement
Checked by SGI program audits, P07 testing, and the automated marking scan reports.

## 6. Exceptions
None for the regulated levels. Others under POL-01 4.12.

## 7. Related documents
POL-01; POL-02; SGI program procedures; CSP implementing procedures; Part 37 information protection procedure; CIP-011-3 program.
