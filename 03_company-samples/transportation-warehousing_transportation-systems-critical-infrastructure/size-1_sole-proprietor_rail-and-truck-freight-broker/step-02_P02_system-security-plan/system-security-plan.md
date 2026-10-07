# System Security Plan (short form): Freight Brokerage SaaS Stack

**Organization:** Cris Santos Company (freight broker arranging truck and rail shipments) | **Tier:** Sole Proprietorship | **Vertical:** Transportation Systems
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-08

## 1. System Name and Identifier
Freight Brokerage SaaS Stack (**FBSS**), identifier CSC-SYS-001.

## 2. System Overview
The FBSS is everything the owner uses to book about 1,100 truckloads and coordinate about 260 rail carloads a year: quoting, finding and checking carriers, rate confirmations, tracking loads in transit, billing shippers, paying carriers, and keeping the transaction records FMCSA requires. One person, the owner, uses and runs it. Components are SYS-01 to SYS-09 in `../00_company-facts.md` section 3: the TMS, the email and file suite, the accounting SaaS, the bank portal, the load board and carrier monitoring service, the tracking app, one laptop, one phone with a cloud business line, and the home network. There is no server and no IaaS. Most application safeguards are **inherited from the SaaS providers**; the owner is responsible for identities, data handling, devices, payment decisions, and vendor terms (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-TRANSPORTATION-S09 | FMCSA broker registration and financial security | 49 U.S.C. 13901, 13904; 49 CFR 387.307; 49 CFR part 366 |
| C-TRANSPORTATION-S10 | FMCSA brokers of property: records and conduct | 49 CFR 371.3 (records kept 3 years; parties' right to review), 371.7, 371.13 |
| C-TRANSPORTATION-S07 | Security of confidential personal information (Florida) | Fla. Stat. 501.171(2) reasonable measures, (3)-(6) notice, (8) disposal |
| C-TRANSPORTATION-CT | Contract terms | Master broker-shipper agreement (72-hour incident notice); railroad portal terms of use |
| Internal | Information Security Policy | POL-01 (P06) |

**Not applicable:** the TSA rail cybersecurity directives (C-TRANSPORTATION-R01) and 49 CFR parts 1570 and 1580, because a broker is not a railroad carrier or rail hazmat shipper (1580.1(a)); TSA pipeline, aviation, and maritime rules (R02 to R05). **Tracked only:** CIRCIA (R07) and the TSA surface cyber NPRM (R06), both proposed. Reasons are in P03.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-09-08.
### 4.2 System Authorization Decision
No formal authorization applies to a private brokerage. Equivalent decision: the owner accepted continued operation on 2026-09-08, on condition that the High risks in P01 (R-001 to R-004) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: authenticator-app MFA on the TMS, accounting SaaS, and load board (2026-09-30); a password manager (2026-09-30); a separate network for business devices (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, risk acceptor, incident lead | Owner | Every role (POL-01 section 3) |
| Accounting user | Contract bookkeeper | Monthly reconciliation through an own login; no payment rights |
| Technical support | On-call IT consultant | Laptop, email setup, and home network help on request; no standing access |
| Service providers | TMS vendor, email and file suite provider, accounting SaaS provider, bank, load board, carrier monitoring service, tracking app provider | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Shipment and transaction records (loads, rate confirmations, BOLs and PODs, 49 CFR 371.3 records) | Moderate | Moderate | Moderate | Pickup numbers and high-value loads help cargo thieves; a wrong record misbills or misdirects freight; loads in transit cannot be watched without it (P05 BP-02 MTD 8 h) |
| Carrier and driver personal information (W-9s with Social Security numbers, driver license copies, driver location) | Moderate | Low | Low | Disclosure triggers Fla. Stat. 501.171 notice duties and identity theft risk |
| Payment information (carrier bank details, ACH) | Moderate | Moderate | Moderate | A changed bank detail diverts a carrier payment; carriers left unpaid can claim against the surety bond |
| Shipper commercial data (rates, contracts, rail shipping instructions) | Moderate | Moderate | Low | Contractual confidentiality; wrong shipping instructions misroute rail cars |
| **FBSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

These ratings use the FIPS 199 levels as a planning aid; the business has no federal information.

**Baseline:** SP 800-53B Moderate, tailored to 24 controls that a one-person brokerage can run (`control-implementation.csv`). Other Moderate controls are inherited from the SaaS providers (evidence: the TMS vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal program.

## 7. Authorization Boundary Description
- **Inside:** the owner's TMS, email and file suite, accounting, bank, load board, carrier monitoring, and tracking app accounts and their settings; the laptop and phone; the business phone line; the home network as used for business.
- **Outside (external services and interfaces):** the providers' platforms; the railroad customer portals (SYS-10, operated by the railroads); the FMCSA registration system (SYS-11); motor carriers' and shippers' email systems.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Shippers | Tenders, rate quotes, invoices, rail shipping instructions | Master broker-shipper agreement with the largest shipper; standard terms with the rest |
| Motor carriers | Rate confirmations, BOLs and PODs, W-9s, bank details, insurance certificates | Broker-carrier agreement (2021 industry form; waiver clause under review, P03) |
| Drivers | Location during a load (tracking app link); texts and calls | Tracking app consent screen |
| Railroads (SYS-10) | Car orders, shipping instructions, car tracing | Portal terms of use; **one shared login (gap)** |
| FMCSA (SYS-11) | Registration record and account | FMCSA registration system terms |
| Surety and process agent companies | Bond and BOC-3 filings; claim notices | Surety bond (BMC-84); blanket designation |
| Bookkeeper | Accounting records | Engagement letter with confidentiality clause |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| TMS tenant (SYS-01) | SaaS | Owner |
| Email and file suite tenant (SYS-02) | SaaS | Owner |
| Accounting SaaS (SYS-03) | SaaS | Owner |
| Business bank portal (SYS-04) | Bank service | Owner |
| Load board and carrier monitoring accounts (SYS-05) | SaaS | Owner |
| Tracking app account (SYS-06) | SaaS | Owner |
| Laptop (SYS-07) | Endpoint | Owner |
| Phone and business line (SYS-08) | Personal endpoint; VoIP SaaS | Owner |
| Home network (SYS-09) | ISP router | Owner |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 24 controls:
- Implemented: 6
- Partially implemented: 14
- Planned: 4

Inheritance: 1 fully inherited (AU-2, from the TMS and email providers), 12 hybrid (a provider runs the mechanism and the owner configures or uses it correctly), and 11 the owner's alone (AC-19, AT-2, AT-2(3), AU-6, CP-2, IA-5, IR-8, MP-6, RA-3, SA-9, SI-12).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; vendor oversight (SA-9); carrier vetting as supplier review (SR-6, author mapping); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05) |
| Protect | MFA (IA-2(1), IA-2(2), gaps); laptop encryption (SC-28); sharing settings (AC-3); payment call-back (AT-2(3), planned) |
| Detect | Provider logging (AU-2, inherited); monthly log and bank change review (AU-6, planned) |
| Respond | Ransomware runbook (IR-8) |
| Recover | TMS vendor backups and twice-daily in-transit list (CP-9); backup broker agreement (CP-2, planned) |

### 10.2 Control assessment status
Self-assessed 2026-08-10 to 2026-08-14 with the IT consultant; tests on 2026-08-13. See P07.

## 11. Digital Identity Acceptance Statement
The bank requires a password and a hardware token, which fits the payment risk. The email suite uses a password and a text-message code; text codes can be stolen by moving the phone number, so the owner adds an authenticator app and a hardware security key and sets a port-out PIN with the mobile carrier (2026-09-30). The TMS, accounting SaaS, and load board use a password only until MFA is turned on (2026-09-30). The railroad portals and the FMCSA registration system are outside this boundary; the owner protects those credentials under POL-01 section 7.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and TMS vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **BOL / POD:** bill of lading / proof of delivery
- **FBSS:** Freight Brokerage SaaS Stack
- **MFA:** multi-factor authentication
- **RSSM:** rail security-sensitive materials (49 CFR 1580.3)
- **TMS:** transportation management system

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-08 | Initial short-form plan | Owner |
