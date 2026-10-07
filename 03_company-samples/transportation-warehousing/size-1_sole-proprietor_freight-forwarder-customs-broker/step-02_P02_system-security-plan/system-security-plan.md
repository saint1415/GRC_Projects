# System Security Plan (short form): Core Brokerage SaaS Stack

**Organization:** Cris Santos Company (freight forwarder and customs broker) | **Tier:** Sole Proprietorship | **Vertical:** Transportation and Warehousing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-14

## 1. System Name and Identifier
Core Brokerage SaaS Stack (**CBSS**), identifier CSC-SYS-001.

## 2. System Overview
The CBSS is everything the owner uses to run a one-person customs brokerage and ocean forwarding business: preparing and transmitting import entries, Importer Security Filings, and export information to CBP; booking cargo; paying duties and freight; billing; and keeping the records 19 CFR Part 111 requires. Components are SYS-01 to SYS-04, SYS-06 to SYS-08, and SYS-10 in `../00_company-facts.md` section 3: the customs and forwarding software (SaaS), a business email and file suite, an accounting SaaS, online banking, a laptop and printer-scanner, a personal phone, the home network, and paper records. There is no server and no IaaS. Most safeguards for the data inside each service are **inherited from the SaaS vendors**; the owner is responsible for identities, data handling, devices, the home network, and vendor terms (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| Source | Requirement | Citation |
|---|---|---|
| CBP | Customs broker records, confidentiality, availability, breach notice, supervision | 19 CFR 111.21, 111.23 to 111.28 |
| CBP | Methods for storage of records (scanned records) | 19 CFR 163.5 |
| FMC | Ocean freight forwarder records | 46 CFR 515.33 |
| Census Bureau | Export information records | 15 CFR 30.10 |
| State | Reasonable security; disposal; breach notice | Fla. Stat. 501.171(2), (3), (4), (8) |
| N48-49-R05 | CTPAT (voluntary). Not a partner; answers CTPAT clients' security questionnaires | CBP program |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: the USCG maritime cyber rule (N48-49-R01, 33 CFR Part 101 Subpart F), because the business has no vessel or facility security plan, and the TSA indirect air carrier rule (49 CFR Part 1548), because it arranges no air transportation. Reasons are in P03.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-09-14.
### 4.2 System Authorization Decision
No formal authorization applies to a private business. Equivalent decision: the owner accepted continued operation on 2026-09-14, on condition that the High risks in P01 (R-001, R-002, R-003) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: independent backup of the records archive (2026-10-31); separate business Wi-Fi network (2026-12-31); business plan for the AI assistant with no-training terms, or stop using it with client data (P10, 2026-10-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security officer, risk acceptor, recordkeeping lead (111.21(d)), CBP point of contact (111.3(b)) | Owner (licensed customs broker) | Every role (POL-01 section 3) |
| Technical support | On-call IT consultant | Laptop, printer, and network help on request; no standing access |
| Bookkeeping | Contract bookkeeper | Monthly reconciliation in the accounting SaaS (own account from 2026-09-30) |
| Service providers | Customs software vendor, email and file suite provider, accounting SaaS provider, bank | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Customs entry and trade records (client invoices, importer of record numbers, POAs, entry data) | Moderate | Moderate | Moderate | Confidential under 111.24 and include six Social Security numbers; a wrong entry costs clients duty and penalties; filings cannot wait more than a day (P05 MTD 24 h) |
| Financial transactions (duty payments, freight wires, client ledgers) | Moderate | Moderate | Low | A changed payee sends client money to a criminal; payments can wait two days (P05 MTD 48 h) |
| **CBSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 26 controls that carry the record and confidentiality duties of a one-person brokerage (`control-implementation.csv`). Other Moderate controls are either inherited from the SaaS vendors (evidence: the customs software vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal system.

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts and settings in the customs software, email and file suite, accounting SaaS, and online banking; the laptop, printer-scanner, and phone; the home network as used for business; and the paper records in the locked cabinet.
- **Outside (external services and interconnections):** the vendors' platforms, CBP's electronic systems and portals (SYS-05), the consumer AI assistant (SYS-09), carriers' and agents' systems, and the internet provider's network.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| CBP (through the customs software) | Entries, entry summaries, ISF, EEI, releases and holds | Vendor's CBP-approved connection; the broker's license and permit |
| Clients (importers and exporters) | Invoices, POAs, entry copies, duty and freight bills | Terms of service and POA. **No written authorization for service providers (gap, 111.24)** |
| Ocean carriers and overseas agents | Bookings, bills of lading, arrival notices, payment instructions | Carrier terms; **documents also exchanged in a consumer messaging app (gap)** |
| Bank | Duty payments to CBP; freight wires | Business account agreement |
| Contract bookkeeper | Client ledgers and invoices | Engagement letter with a confidentiality clause; **shared login (gap)** |
| Consumer AI assistant | Invoice lines and some whole invoices | **Consumer terms only; training allowed (gap, P10)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Customs and forwarding software tenant (SYS-01) | SaaS | Owner |
| Email and file suite (SYS-02) | SaaS (business plan) | Owner |
| Accounting SaaS (SYS-03) | SaaS | Owner |
| Online banking (SYS-04) | Bank portal | Owner |
| Laptop and printer-scanner (SYS-06); 2019 laptop (not wiped) | Endpoints | Owner |
| Mobile phone (SYS-07) | Personal endpoint | Owner |
| Home network and router (SYS-08) | Shared home network | Owner (router from the internet provider) |
| Paper records (SYS-10) | Locked cabinet | Owner |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 26 controls:
- Implemented: 10
- Partially implemented: 14
- Planned: 2

Inheritance: 3 fully inherited from vendors (AC-3, AU-2, SI-8), 10 hybrid (the vendor operates the mechanism, the owner configures or uses it correctly), and 13 the owner's alone.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; vendor terms and client authorization (SA-9, gap); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); retention schedule (SI-12, gap) |
| Protect | MFA on customs software and bank (IA-2(1)); email MFA bypass (IA-2(2), gap); disk encryption (SC-28); call-back for payment changes (AT-2(3), gap) |
| Detect | Vendor logging (AU-2, inherited); monthly sign-in review (AU-6, planned) |
| Respond | Ransomware runbook with the CBP 72-hour notice (IR-8, IR-6) |
| Recover | Customs software vendor backups (CP-9, inherited); independent archive backup (CP-9, gap); backup broker (CP-2, gap) |

### 10.2 Control assessment status
Self-assessed 2026-08-17 to 2026-08-21 with the IT consultant (tests on 2026-08-20). See P07.

## 11. Digital Identity Acceptance Statement
The customs software requires a password and an authenticator app code, which suits remote access to confidential client records at a Moderate categorization. Email and the bank use text-message codes, which are weaker; the owner moves email to the authenticator app when the app password is removed (2026-09-30). The accounting SaaS uses a password only until MFA is turned on (2026-09-30). The CBP portals use CBP's own sign-in, outside this boundary.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **ACE:** CBP's Automated Commercial Environment (trade processing system)
- **EEI:** Electronic Export Information
- **ISF:** Importer Security Filing (19 CFR Part 149)
- **MFA:** multi-factor authentication
- **POA:** customs power of attorney
- **CBSS:** Core Brokerage SaaS Stack

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-14 | Initial short-form plan | Owner |
