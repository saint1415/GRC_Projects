# Scenario facts: Cris Santos Company | Wholesale Trade | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was read from eCFR (current as of 2026-09-23) and the Florida Statutes website.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; the owner is the managing member) |
| Business | IT hardware and software reseller (NAICS 423430): laptops, desktops, monitors, docking stations, network switches and wireless access points, printers, peripherals, and software licenses. For some customers it also does pre-delivery setup: asset tagging, basic configuration from a customer-provided settings list, and delivery to named buildings and rooms |
| Location | Florida. One leased flex unit: a small office and a 2,000 sq ft stockroom with a setup bench |
| Workforce | 7 employees (5 full-time, 2 part-time): Owner, Operations Manager, Federal Account Manager, Commercial Account Manager, Purchasing and Inventory Coordinator, Setup and Receiving Technician (part-time), Bookkeeper (part-time) |
| Revenue | About $1.1 million a year (fictional), about $4,400 per business day over 250 business days. Gross margin about 21% (about $920 of gross profit per business day). The SBA size standard for NAICS 423430 is 250 employees (13 CFR 121.201), so the company is SBA-small |
| Customers | About 85 active commercial accounts (small businesses, professional offices, private schools) in Florida, about 78% of revenue. About 22% of revenue (about $240,000) is for DoD end users: direct purchase orders from two DoD contracting offices that support Florida installations, and orders from one larger federal IT reseller (the **Federal Prime**) that holds DoD contracts |
| DoD orders (last 12 months) | 34 orders. 15 were for commercially available off-the-shelf (COTS) products only. 19 included setup services (asset tagging and pre-delivery configuration), so they are not COTS-only |
| Federal Contract Information (FCI) | The 19 setup orders carry FAR 52.204-21. Customers send equipment lists with government asset tag numbers, user names, building and room assignments, and delivery windows on the installation. That information is FCI as defined in 52.204-21(a): not intended for public release and provided by the Government under a contract to deliver a product or service. Simple transactional information, such as what is needed to process payments, is excluded from the definition |
| Clauses in the setup orders | FAR 52.204-21, FAR 52.204-25, DFARS 252.246-7008, and the standard DFARS 252.204-7012, 252.204-7019, and 252.204-7020 (prescribed for all DoD solicitations and contracts except those solely for COTS items, DFARS 204.7304). Since 2026-02, setup RFQs also carry DFARS 252.204-7021 at **CMMC Level 1 (Self)**. The Federal Prime flows down 52.204-21, 52.204-25, 252.246-7008, and CMMC Level 1 (Self). Under DoD Class Deviation 2026-O0025, Revision 3, contracting officers remove CMMC requirements from existing contracts by modification before the next option period or at the next scheduled administrative modification; new RFQs may still require Level 1 (Self) |
| COTS-only orders | Carry FAR 52.204-25 but not FAR 52.204-21 (FAR 4.1902 excludes COTS acquisitions) and no CMMC requirement (32 CFR 170.3(c) excludes procurements exclusively for COTS items) |
| Controlled Unclassified Information (CUI) | **None.** No CUI-marked document has been received, and no order identifies covered defense information. The company's policy is to refuse CUI (POL-04). If a customer ever sends CUI, the company stops and reassesses (DFARS 252.204-7012 and NIST SP 800-171 would then apply) |
| SAM and SPRS | Registered in SAM with a CAGE code. Annual representations, including FAR 52.204-26, completed by the Owner on 2026-01-15 ("does not provide" and "does not use" covered telecommunications equipment or services). A **CMMC Level 1 (Self)** result of MET and an affirmation were entered in SPRS by the Owner on 2026-03-02, based on a checklist, with no documented self-assessment |
| Suppliers | 16 active suppliers: 2 national IT distributors that are authorized for most product lines (about 78% of purchase spend), 5 OEM partner programs for licenses and direct shipments (about 9%), 5 specialty authorized distributors (about 6%), and 4 independent brokers (gray market) for end-of-life and hard-to-find items (about 7%) |
| Item master | About 2,300 active SKUs in the ERP. 310 (13%) have no manufacturer of record, mostly broker items and accessories |
| Not in scope | SEC disclosure rules (private company). CCPA/CPRA (no California business; revenue far below the threshold). CTPAT (not an importer of record). DFARS 252.204-7012 safeguarding and NIST SP 800-171 (no covered defense information; see P03). Trade Agreements Act: the company holds no GSA schedule contract, and none of its 2026 DoD purchase orders includes the Trade Agreements clause, so it was not analyzed. Payment cards: customers pay through the payment processor's hosted page linked from ERP invoices, outside company systems |
| State law approach | Florida law cited only where unavoidable (Fla. Stat. 501.171 for employee records and customer-contact personal information) |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Owner (managing member) | Accepts risk; approves policies and spending; **CMMC Affirming Official** (32 CFR 170.22); signs SAM representations; leads federal sales with the Federal Account Manager |
| Operations Manager | **Security and compliance lead** (designated in writing on 2026-07-06). Runs the MSP relationship; maintains the SSP, risk register, and POA&M; also office administration and HR |
| Federal Account Manager | DoD quotes and orders; reads the clauses in each purchase order; Section 889 check on federal quotes |
| Commercial Account Manager | Commercial customers and customer portal users |
| Purchasing and Inventory Coordinator | Buyer; supplier onboarding and the supplier list; stock levels; uses the ERP reorder feature (P10) |
| Setup and Receiving Technician (part-time) | Receiving, setup bench, asset tagging, shipping |
| Bookkeeper (part-time) | Invoices, collections, supplier payments, and supplier bank-detail changes |
| Managed service provider (MSP) | Help desk, patching, endpoint protection, firewall and Wi-Fi, backup administration. Holds administrator credentials |
| Outside help (as needed) | Government contracts counsel; the cyber insurer's breach hotline and panel vendors |

## 3. Systems
| ID | System | Hosting | FCI? | Notes |
|---|---|---|---|---|
| SYS-01 | ERP for small distributors: quotes, sales orders, purchasing, inventory with serial-number tracking, accounting, and a customer ordering portal (about 60 customer users) | Vendor SaaS | Yes (DoD orders and attached equipment lists) | MFA for all staff users; vendor SOC 2 Type 2 report available (P09). Includes the AI reorder feature (SYS-10) |
| SYS-02 | Productivity suite: email, shared files, chat | Vendor SaaS (business tier) | Yes | MFA for all users; the "Orders" shared folder is open to all 7 staff |
| SYS-03 | Endpoints: 7 staff laptops, 1 spare laptop, 1 setup bench desktop, 2 USB barcode scanners, 1 label printer | MSP-managed | Yes (downloads) | Laptops encrypted; bench desktop not encrypted and uses a shared local administrator account |
| SYS-04 | Office and stockroom network: small-business firewall, staff Wi-Fi, guest Wi-Fi, one business internet line | On-premises, MSP-managed | In transit | Guest Wi-Fi separated; the setup bench and cameras are on the staff network |
| SYS-05 | SaaS-to-SaaS backup of the productivity suite | SaaS, operated by the MSP | Yes | Nightly; 30 days of versions; never restore-tested |
| SYS-06 | Supplier portals: 2 national distributor portals, OEM partner and license portals | Supplier SaaS (external) | Ship-to details on drop-ship orders | One distributor portal login shared by 3 staff; portal MFA available but off |
| SYS-07 | Online business banking and the payment processor's hosted payment page | Bank and processor SaaS (external) | No | Supplier payments; bank-detail changes made by the Bookkeeper |
| SYS-08 | MSP remote monitoring and management (RMM) tool | MSP SaaS | No (administrative access) | Agent on all 9 computers |
| SYS-09 | Stockroom physical security: keyed doors, intrusion alarm, 4 IP cameras with a network video recorder (bought 2019 from a broker) | On-premises | No | Alarm code shared by all staff and never changed |
| SYS-10 | AI reorder feature in the ERP: demand forecasts and suggested or auto-submitted purchase orders to the 2 national distributors | Part of SYS-01; the ERP vendor uses a third-party AI service as a subprocessor | Order history includes DoD orders | Turned on 2026-05; auto-submit on for accessory orders under $500 (P10) |

**SSP system (P02):** the *Reseller Operations Platform (ROP)*: SYS-01 to SYS-05, which process, store, or transmit FCI and form the CMMC Level 1 assessment scope (32 CFR 170.19(b)(1)), plus the supporting MSP tool (SYS-08) and stockroom security devices (SYS-09).

## 4. Current security posture: early to partial
**In place today:**
- MFA on the productivity suite and the ERP for all staff
- Unique named accounts in the ERP and the suite
- MSP-managed endpoint protection with real-time and weekly scans, and monthly patching, on all 9 computers
- Laptops encrypted with built-in full-disk encryption
- Firewall that blocks unsolicited inbound traffic; guest Wi-Fi separated
- Nightly backup of the suite (SYS-05)
- Serial numbers recorded in the ERP for every unit received and shipped
- Supplier list kept in a spreadsheet; most purchases from authorized distributors
- SAM registration current
- Cyber insurance with a 24x7 breach hotline (since 2025)
- Keyed stockroom doors, an intrusion alarm, and cameras

**Missing or weak:**
1. The CMMC Level 1 (Self) MET result and affirmation entered in SPRS on 2026-03-02 rest on no documented self-assessment or evidence.
2. FCI is not contained. Customer equipment lists arrive by email, are saved in a shared folder all 7 staff can open, and copies sit in download folders on laptops and the setup bench.
3. No Section 889 screening process. The Federal Account Manager checks brand names from memory, and 310 of about 2,300 active SKUs (13%) have no manufacturer of record.
4. Brokers are used without any assessment, and the sourcing order in DFARS 252.246-7008(b) (original manufacturer or authorized suppliers first) is not written down.
5. Receiving does not check for authenticity or tampering: no seal checks, OEM serial validation, or firmware check at the setup bench.
6. Supplier bank-detail changes are accepted by email with no call-back. In April 2026 a $12,600 payment went to a fraudster after an email from a broker lookalike domain; the bank recovered it after 6 days.
7. One distributor portal login is shared by 3 staff, and the carrier shipping account is shared by everyone. The portal offers MFA but it is off.
8. The suite backup has never been restore-tested, and the MSP's backup console login has no MFA.
9. No incident response plan. Staff do not know the 1-business-day Section 889 report.
10. No audit log review; logs use default retention.
11. Offboarding is informal. The former setup technician (left 2025-11) still had an active ERP account until 2026-07-15, and the shared distributor portal password was never changed.
12. No security training beyond occasional MSP phishing warnings.
13. The setup bench desktop has a shared local administrator account, no encryption, unrestricted USB storage, and sits on the staff network while it configures customer devices.
14. Couriers and customer visitors enter the stockroom unescorted. There is no visitor log, and the alarm code is shared and has never changed.
15. No vulnerability scanning.
16. No adopted policies. An MSP-supplied policy template was never adopted.
17. Two laptops retired in 2025 went to an e-waste drop-off with no wipe record.
18. The AI reorder feature auto-submits accessory purchase orders under $500 with no human review (P10).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Primary: the 15 FAR 52.204-21 basic safeguarding requirements for the FCI order stream, assessed as the CMMC Level 1 (Self) requirements (32 CFR 170.14(c)(2) and 170.15). Secondary: Section 889 (FAR 52.204-25 and 52.204-26), DFARS 252.246-7008 sourcing, CMMC status and affirmation (DFARS 252.204-7021; 32 CFR 170.15, 170.22), Fla. Stat. 501.171(2) and (8), and an applicability check of DFARS 252.204-7012, -7019, and -7020 |
| Registry default changed (P03) | The vertical default is NIST SP 800-171 Rev. 2 via CMMC Level 2 and DFARS 252.204-7012. It is not the primary rule here because the company holds no covered defense information, so it has no covered contractor information system (252.204-7012(a)) and is not required to implement SP 800-171 (252.204-7019(b)). The FCI rules are the ones that bind at this size |
| Registry default adapted (P02) | Primary system "Order management, warehouse, and reseller portal (ERP)" becomes one SaaS ERP with an inventory module and a customer ordering portal (SYS-01). A 7-person reseller has no separate warehouse management system |
| P08 incident | Supplier compromise introducing tampered or counterfeit products into distribution, including a broker email compromise and possible covered (Section 889) equipment. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Confidentiality. A readiness self-assessment used to answer the Federal Prime's annual supplier security questionnaire, plus a review of the ERP vendor's SOC 2 Type 2 report |
| P10 AI | Demand forecasting and automated reordering, as the AI reorder feature built into the ERP (SYS-10). Adapted from the registry default because at this size the feature comes inside the ERP rather than as a separate tool |
| Cloud | SaaS plus one cloud workload: the SaaS-to-SaaS backup of the suite (SYS-05). Vendor-agnostic |
| Supply chain practice | NIST SP 800-161 Rev. 1 (upd1) as the benchmark (source register SRC-800-161), applied through SP 800-53 SR controls. It is guidance, not a legal requirement for this company |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | BIA, risk assessment, and gap analysis with the MSP lead technician |
| 2026-08-10 to 2026-08-12 | Control assessment by an independent consultant (on site 2026-08-11) |
| 2026-08-31 | Deliverables approved by the Owner |
| 2026-11-10 | Planned start of CMMC Phase 2 (32 CFR 170.3(e)(2)); suspended by the DoD (Department of War) CIO memorandum of 2026-07-13 (DoD Class Deviation 2026-O0025, Revision 3). Requiring activities may still require Level 1 (Self) |

## 7. Facts added while building the deliverables
| Topic | Added fact | Used in |
|---|---|---|
| Former technician account | Found active in the ERP on 2026-07-15 during the risk assessment and disabled that day. The ERP sign-in log showed no use after the termination date. The shared distributor portal password was changed on 2026-07-16 | P01, P03, P07 |
| Payment fraud | 2026-04-14: an email from a lookalike domain of a broker asked for new bank details; the Bookkeeper changed them and paid $12,600. The bank recalled the payment and returned it on 2026-04-20. No report was filed | P01, P08 |
| Cyber insurance | $1 million limit, $10,000 retention. The policy requires a call to the 24x7 breach hotline before any incident vendor is hired, and use of panel counsel and forensics | P08 |
| MSP contract | Help desk, patching, endpoint protection, firewall, Wi-Fi, and backup administration, with a 4-business-hour response time and no recovery time commitment. Incident response is billed hourly | P05, P08 |
| ERP vendor | SOC 2 Type 2 report, 12 months ending 2026-03-31, unqualified; states 99.9% monthly availability, RTO 4 hours, RPO 1 hour. The AI reorder feature sends order history to a third-party AI service listed as a subprocessor | P05, P09, P10 |
| Cash | A cash reserve covers about 45 days of expenses. Payroll runs every two weeks through an outside payroll service | P05 |
| Internet | One business internet line; no failover. Staff can work from home on laptops | P01, P05 |
| Camera recorder (P07) | On 2026-08-11 the assessor found that the stockroom camera recorder and its 4 cameras are white-label units of a manufacturer named in paragraph (2) of the "covered telecommunications equipment or services" definition in FAR 52.204-25. They were disconnected on 2026-08-12 and replaced with cameras from a non-covered manufacturer on 2026-08-20. Counsel is reviewing the 52.204-26 representation and whether any report is due | P01, P03, P07, P08 |
| Federal Prime questionnaire | The Federal Prime sent its annual supplier security questionnaire in July 2026; the response is due 2026-09-30 | P09 |
| Budget | The Owner approved a 2026 Q4 security budget of about $8,800 one-time and $3,150 a year on 2026-08-31 (itemized in P01) | P01 |
| Assessor | The P07 assessor is an independent consultant who did not take part in the risk assessment or gap analysis and operates no control | P07 |
| Carrier account (P07) | The shared carrier shipping password was unchanged after the former technician left; P07 testing on 2026-08-11 confirmed it still worked. The carrier log showed no use after his last day. Changed 2026-08-12 | P07 |
| DoD broker items | 3 of the 34 DoD orders included broker-sourced docking stations, delivered with no notice to the contracting officer | P03 |
| AI reorder feature (P10) | Results 2026-05-01 to 2026-08-21: A-class WAPE 27% overall, 38% for networking; 46 orders auto-submitted ($14,900), 7 of them excess ($380 restocking fees); 12 of 410 suggested lines named a broker; fill rate 89% for small commercial accounts vs 95% for large accounts and 94% for DoD orders. Auto-submit turned off on 2026-08-25 | P01, P10 |
