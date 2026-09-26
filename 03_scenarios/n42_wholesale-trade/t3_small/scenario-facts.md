# Scenario facts: Cris Santos Company | Wholesale Trade | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was read from eCFR (current as of 2026-09-23).

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; the majority owner is also the Chief Executive Officer) |
| Business | IT hardware and software wholesale distributor (NAICS 423430): network switches, routers and wireless equipment, video surveillance and collaboration equipment, servers, storage, peripherals, and software licenses |
| Location | Florida. One site: headquarters offices and a 60,000 sq ft distribution center in the same building, including a caged **configuration lab** where technicians stage and configure equipment before shipment |
| Workforce | 62 employees: 8 management and administration, 14 sales and account management, 6 purchasing and supplier management, 22 warehouse and logistics, 6 configuration technicians, 4 customer service, 2 IT |
| Revenue | $54 million a year (fictional), about $216,000 per shipping day over 250 shipping days. The SBA size standard for NAICS 423430 is 250 employees (13 CFR 121.201), so the company is SBA-small |
| Customers | About 380 active commercial reseller accounts in Florida, Georgia, and Alabama (about 84% of revenue). Three DoD prime contractors buy from the company under subcontract purchase orders (about 16% of revenue, $8.6 million) |
| Suppliers | 47 active suppliers: 35 authorized sources (original equipment manufacturer (OEM) programs and OEM-authorized distributors) and 12 independent brokers (gray market) used for hard-to-find items, about 6% of purchase spend |
| Federal Contract Information (FCI) order stream | Orders under Prime A and Prime C subcontracts that include custom kitting and asset labeling. The purchase orders contain FAR 52.204-21, FAR 52.204-25, and, since 2026-01, DFARS 252.204-7021 at CMMC Level 1 (Self). Orders exclusively for commercially available off-the-shelf (COTS) items carry neither FAR 52.204-21 (see its paragraph (c)) nor a CMMC requirement (32 CFR 170.3(c)) |
| Controlled Unclassified Information (CUI) order stream | Prime B subcontract (awarded 2024-06) to stage and configure network switches and video equipment for DoD installations, using CUI-marked configuration documents (network drawings, IP addressing plans, device configuration templates). The subcontract contains DFARS 252.204-7012, 252.204-7019/-7020, 252.246-7008, and FAR 52.204-25. Prime B has notified the company that the option period starting **2027-04-01** will require CMMC Status of **Level 2 (C3PAO)**, flowed down under 32 CFR 170.23(a)(3) |
| SPRS status | NIST SP 800-171 Basic Assessment posted 2024-03-15 with a self-reported score of 96 out of 110, with no supporting worksheet. CMMC Level 1 (Self) result and affirmation entered 2026-01-20 without a documented self-assessment |
| Not in scope | SEC disclosure rules (the company is private). CCPA/CPRA: the company has no California customers, suppliers, or operations (counsel confirmed 2026-06; revisit before onboarding California resellers). CTPAT: the company buys from U.S. distributors and is not an importer of record, so it has not joined the voluntary program. Payment cards: reseller card payments go through the portal vendor's hosted payment page, outside company systems |
| State law approach | Florida law is cited only where unavoidable (breach notification, Fla. Stat. 501.171, for employee and reseller-contact personal information). Otherwise the samples stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Chief Executive Officer (majority owner) | Accepts High and Very High risks. **CMMC Affirming Official** (32 CFR 170.22) |
| Chief Operating Officer | Executive owner of the security program; system owner of the SSP system; accepts risk up to Moderate; signs policies |
| IT Manager | Runs IT and security (part-time security and compliance duties); maintains the SSP, risk register, and POA&M |
| Systems Administrator | ERP, WMS, identity provider, file server, and endpoint administration |
| Government Contracts Manager | Flowdown clauses, Section 889 representations, SPRS entries, reports to primes, contracting officers, and DIBNet |
| Purchasing and Supplier Manager | Supplier onboarding and vetting, approved supplier list, purchase orders; supply chain risk lead |
| Warehouse and Logistics Manager | Receiving, inventory holds, shipping, dock and warehouse physical security |
| Configuration Lab Lead | Day-to-day custodian of CUI in the configuration lab |
| Controller | Supplier master data, payments, and bank-detail changes |
| Sales Operations Manager | Business owner of the reseller ordering portal and the demand forecasting tool |
| HR Manager | Screening, onboarding, terminations, training records |
| Managed service provider (MSP) | After-hours help desk, server patching, and backup monitoring. It holds administrator credentials, so it is an External Service Provider that handles Security Protection Data (32 CFR 170.19(c)(2)) |

## 3. Systems

| ID | System | Hosting | FCI / CUI | CMMC Level 2 asset category (32 CFR 170.19(c)) | Notes |
|---|---|---|---|---|---|
| SYS-01 | ERP: order management, purchasing, inventory, finance | Vendor SaaS | FCI; **CUI found** (14 DoD sales orders had CUI attachments) | CUI Asset | Vendor has a SOC 2 Type 2 report. No FedRAMP authorization, and FedRAMP Moderate equivalency is not documented |
| SYS-02 | Warehouse management system (WMS) with 40 handheld scanners | Company-managed servers in the cloud tenant (SYS-07); handhelds on warehouse Wi-Fi | FCI (DoD ship-to and order data) | Contractor Risk Managed Asset | Handhelds sign in with 6 shared zone accounts; **no MFA**; handheld operating system is past vendor support |
| SYS-03 | Reseller ordering portal (B2B e-commerce) | Vendor SaaS | None by design (commercial orders only) | Out of scope for CUI if the ERP sync excludes DoD orders (to be confirmed); in scope for SOC 2 (P09) | About 1,100 reseller users; MFA optional for resellers; syncs catalog, pricing, orders, and invoices with SYS-01 |
| SYS-04 | EDI service (value-added network) | Vendor SaaS | FCI in DoD purchase orders from Prime A and Prime C | Contractor Risk Managed Asset | Purchase orders, advance ship notices, and invoices with 22 suppliers and 18 large resellers |
| SYS-05 | Identity provider (single sign-on and MFA) | SaaS | Identities only | Security Protection Asset | **MFA enforced for email, ERP, remote access VPN, and the cloud console.** Not integrated with the WMS or handhelds |
| SYS-06 | Productivity suite (email, chat, personal file storage) | Vendor SaaS (commercial tier) | FCI in email | Contractor Risk Managed Asset | Supplier and customer email; target of supplier email compromise |
| SYS-07 | Cloud tenant (IaaS) | Public cloud provider, commercial region (vendor-agnostic) | **CUI** (file server) and FCI (WMS) | CUI Asset | Hosts the WMS servers, the company **file server with general shares**, and the backup vault. The services in use are listed as FedRAMP Moderate authorized (checked by the IT Manager on 2026-07-15) |
| SYS-08 | Office, warehouse, and lab network | On-premises | CUI in transit | CUI Asset | One firewall; corporate, scanner, and guest Wi-Fi; the configuration lab bench network is on the corporate VLAN (flat) |
| SYS-09 | Endpoints | On-premises | CUI (6 lab workstations); FCI | CUI Asset | 58 Windows laptops and desktops, 6 lab workstations, 12 label and shipping printers |
| SYS-10 | Warehouse physical security | On-premises | None | Security Protection Asset (lab cage) | Badge readers on 4 exterior doors and the lab cage, 24 cameras with a network video recorder, intrusion alarm |
| SYS-11 | Shipping and carrier label service | Vendor SaaS | FCI (ship-to addresses) | Contractor Risk Managed Asset | Rates, labels, tracking |
| SYS-12 | Demand forecasting and automated reordering add-on | Vendor SaaS connected to SYS-01 | Order history (includes DoD orders) | Contractor Risk Managed Asset | Machine learning forecasts and suggested purchase orders; pilot since 2026-03 (see P10) |
| SYS-13 | MSP remote monitoring and management tool | MSP SaaS | Security Protection Data | Security Protection Asset (External Service Provider) | Agent on all Windows endpoints and servers |

**SSP system (P02):** the *Order-to-Fulfillment Platform (OFP)*: SYS-01 ERP, SYS-02 WMS, SYS-03 reseller portal, and the components that support the CUI order stream (SYS-05, SYS-07, SYS-08, SYS-09, SYS-10 lab cage, SYS-13), scoped as the CMMC Level 2 assessment scope under 32 CFR 170.19(c).

## 4. Current security posture: partially compliant

**In place today:**
- MFA through the identity provider for email, ERP, remote access VPN, and the cloud console
- Unique named accounts in the ERP, the identity provider, and the file server
- A next-generation firewall with no inbound services except the VPN
- Next-generation antivirus on Windows endpoints and servers (no 24x7 monitoring)
- Automatic operating system patching on Windows endpoints; the MSP patches servers monthly
- Nightly backups of the WMS database and file server to a backup vault in the same cloud account
- Badge access on exterior doors and the lab cage, cameras, and an alarm
- Supplier onboarding checks: tax form, credit check, and bank letter
- An approved supplier list kept as a spreadsheet by the Purchasing and Supplier Manager
- Annual security awareness video at hire and each January
- A 2024 SSP template that was never completed
- Cyber insurance with a carrier breach hotline

**Missing or weak, found in the 2026 assessments:**
1. CUI configuration documents (about 140 since 2024-06) sit in a general file share that all 62 employees can read. 14 ERP sales orders carry CUI attachments, and the ERP vendor's FedRAMP Moderate equivalency (DFARS 252.204-7012(b)(2)(ii)(D)) is not documented.
2. Supplier vetting is informal. There is no written supply chain risk management (C-SCRM) plan. The 12 brokers were never assessed for authenticity controls, and the DFARS 252.246-7008 sourcing order (authorized sources first) is not documented on purchase orders.
3. No Section 889 screening automation. The Government Contracts Manager checks manufacturer names by hand only when a prime asks. 1,260 of about 14,000 active SKUs (9%) have no manufacturer of record in the ERP item master.
4. Receiving does not inspect for authenticity or tampering: no OEM serial-number checks, seal checks, or firmware verification.
5. No MFA on the WMS. Handhelds use 6 shared zone accounts.
6. Backups have never been restore-tested and share the production cloud account and administrator roles.
7. No audit log review. Cloud, identity, and ERP logs use default retention (30 to 90 days).
8. No written incident response plan. The company has no DoD-approved medium assurance certificate, which DFARS 252.204-7012(c)(3) requires in order to report through DIBNet.
9. Supplier bank-detail changes are accepted by email with no call-back. A near miss in May 2026 almost sent $86,000 to a fraudulent account after a broker's mailbox was compromised.
10. The 2024 SPRS score of 96 and the 2026-01 CMMC Level 1 (Self) affirmation were entered without documented assessments.
11. The configuration lab bench network is on the flat corporate VLAN. Lab workstations have internet access and unrestricted USB storage. File server encryption is provider-managed, and FIPS validation of the encryption modules has not been confirmed.
12. No vulnerability scanning.
13. Two critical product lines are single-source: a ruggedized switch line (one authorized distributor) and an encrypted video line (one OEM program).
14. The handheld scanner operating system is past vendor support.
15. Truck drivers and visitors enter the dock without escort, and badge logs are kept only 30 days.
16. Training is an annual video only: no CUI handling, social engineering, or anti-counterfeit training.
17. Found during P07 testing: 3 IP camera and video recorder SKUs in the ERP item master, bought from one broker, are white-label products whose OEM of record is blank. The broker's catalog lists them as rebranded units of a manufacturer named in FAR 52.204-25. None had shipped on a DoD order.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 | Primary: NIST SP 800-171 Rev. 2 (110 requirements) as required by DFARS 252.204-7012 and assessed under CMMC Level 2, scoped to the CUI order stream. Secondary: the 15 FAR 52.204-21 requirements (CMMC Level 1) for the FCI stream, plus a short supply chain clause check (FAR 52.204-25, DFARS 252.246-7008) |
| P08 incident | Supplier compromise introducing tampered or counterfeit products into distribution, including supplier email compromise and possible covered telecommunications equipment |
| P09 SOC 2 | Readiness self-assessment for the reseller ordering portal requested by two large reseller customers (Security and Availability), plus a review of the portal vendor's SOC 2 Type 2 report |
| P10 AI | Demand forecasting and automated reordering (AI-001), plus general-purpose generative AI use by staff (AI-002) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only for shared responsibility |
| Supply chain practice | NIST SP 800-161 Rev. 1 (upd1) C-SCRM practices (source register SRC-800-161), applied through SP 800-53 SR controls |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork (contracted independent assessor) |
| 2026-08-31 | Deliverables approved by the Chief Operating Officer; High risks and the budget approved by the Chief Executive Officer |
| 2026-11-10 | CMMC Phase 2 begins (32 CFR 170.3(e)(2)) |
| 2027-02 | Planned CMMC Level 2 (C3PAO) certification assessment |
| 2027-04-01 | Prime B option period starts (requires CMMC Level 2 (C3PAO)) |

## 7. Facts added during the build (fictional; used across P01-P10)

| Topic | Added fact |
|---|---|
| Volumes | About 650 order lines and 220 shipments per shipping day; about 14,000 active SKUs; about 1,100 reseller portal users |
| DoD shipments | About 35 DoD shipments per month; about 6 configured-equipment jobs per month for Prime B |
| Gross margin | About 11% ($24,000 gross profit per shipping day) |
| Near miss | 2026-05-12: a broker's mailbox was compromised and sent a bank-change request and an invoice for $86,000; the Controller's bank flagged the new account as a mule account before the payment released |
| Cyber insurance | $3 million limit, $50,000 retention; the carrier requires a call to its hotline before incident vendors are engaged |
| Budget | 2026 Q4 and 2027 Q1 security and compliance budget of $118,000 approved by the Chief Executive Officer on 2026-08-31 |
