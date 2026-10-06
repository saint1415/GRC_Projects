# System Security Plan: Ticketing and Venue Operations Platform (TVOP)

**Organization:** Cris Santos Company, Inc. (live event venue operator with ticketing; private equity-backed; three Florida venues) | **Tier:** Mid-Market | **Vertical:** Arts, Entertainment, and Recreation
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Ticketing and Venue Operations Platform (**TVOP**), identifier CSC-TVOP-01. The TVOP is the company's major system. It is the set of company-managed components and company configuration of vendor services that sell tickets, take ticket payments, admit attendees, and hold patron data (`../00_company-facts.md` section 3).

## 2. System Overview
The TVOP supports every ticketing, entry, settlement, and patron communication process in the BIA (P05) at the Amphitheater, the Music Hall, and the Club, and from 2027-07-01 at the County Performing Arts Center (County PAC). It serves 600 employees, about 1,400 event-day workers, and about 1.1 million patron accounts, and it carries about 600,000 ticket orders a year under the ticketing merchant account (MID-T).

**Major components:**
| ID | Component (in the boundary) | Hosting and service model |
|---|---|---|
| SYS-01 | The company's tenant configuration in the white-label ticketing platform: 186 venue users, roles, pricing rules (dynamic pricing module), bot mitigation and virtual queue settings, checkout settings, 3 API keys | Vendor SaaS; vendor PCI DSS service provider AOC and SOC 2 Type 2 |
| SYS-02 | MID-T card channels: 26 virtual terminal users and 18 standalone validated P2PE devices at the box offices | Payment partner services; devices on premises |
| SYS-04 | Company website and content management system (CMS), with event pages that embed the ticketing checkout form, and the SaaS tag manager | Cloud workloads account; tag manager SaaS |
| SYS-05 | Cloud landing zone: identity and security, shared services, workloads (CMS, patron data platform, settlement application), and backup accounts | Public cloud IaaS/PaaS, vendor-agnostic (P04) |
| SYS-06 | Identity provider (SSO, MFA, conditional access) | SaaS |
| SYS-08 | Corporate and venue networks on SD-WAN at 4 sites | On premises; SD-WAN managed service |
| SYS-09 | 520 laptops and PCs (including the 26 virtual terminal laptops), 180 ticket scanners, 64 tablets | Company-managed |
| SYS-16 | SIEM and EDR console | MSSP-operated SaaS |

The food, beverage, and merchandise POS (SYS-03) is a separate vendor system under its own merchant account (MID-F) with a validated P2PE solution. It connects to the TVOP only through settlement reports.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the TVOP |
|---|---|---|---|
| N71-R04 | PCI DSS v4.0.1 (contractual, through the merchant agreement). MID-T validates with a **ROC by a QSA** in 2026 (Visa Level 2) | PCI SSC standard; acquirer letter 2026-03-16; Visa *What To Do If Compromised* v10.0 | Primary control requirement; requirement numbers are in the `regulatory_driver` column of `control-implementation.csv` |
| N71-R05 | FTC Act Section 5 (patron data security, privacy statements, pricing claims) and the Rule on Unfair or Deceptive Fees for live-event tickets | 15 U.S.C. 45(a), (n); 16 CFR Part 464 | Reasonable security for patron data; total-price display on every page and email the TVOP publishes |
| Federal | ADA Title III ticketing rules | 28 CFR 36.302(f) | Accessible seating sales through the same channels and stages, and price parity, which the pricing and bot settings in SYS-01 must respect (P10) |
| Federal | BOTS Act. The company is a protected ticket issuer; no compliance duty, but bot block records are evidence | 15 U.S.C. 45c | Retention of bot mitigation records (P10) |
| State | Florida Information Protection Act: reasonable measures (501.171(2)), disposal (501.171(8)), and breach notification | Fla. Stat. 501.171 | Data security, disposal of card data found in the CRM, and P08 notices |
| Card brand | Visa compromise reporting rules, applied through the acquirer | Visa *What To Do If Compromised* v10.0 (2026-06-25) | P08 card compromise clocks |
| Contract | County PAC management agreement (from 2027-07-01) | Contract | SOC 2 Type 1 and Type 2 commitments; 48-hour incident notice (P09) |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-09 | P06 | Policy basis for every control |

Not applicable:
- **Gaming rules in the vertical profile** (N71-R01 to N71-R03): the company has no casino, gaming, or wagering.
- **COPPA** (N71-R06): the website, ticketing pages, and the mobile ticket app are not directed to children, and patron accounts require age 18 or older.
- **SEC cybersecurity disclosure:** the company is privately held.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-15, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** continued operation of the TVOP accepted with conditions, 2026-09-15.
- **Risk acceptors:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01).
- **Conditions:**
  - the scope reduction for the virtual terminal channel and the payment page script controls must be in place before QSA fieldwork starts on 2026-11-02 (P03 section 1.3);
  - the High POA&M items in P07 must meet their milestones;
  - the audit committee receives POA&M status each quarter;
  - re-decision by 2027-09-30, or after a major change such as the County PAC onboarding.
### 4.3 System Operational Status
Operational. Major modifications planned:
- Virtual terminal payments move to standalone validated P2PE devices that accept keyed phone orders (due 2026-10-30), removing the 26 laptops and the corporate segment from the cardholder data environment.
- Payment page script management and change detection on the website (due 2026-10-30).
- County PAC onboarding to the ticketing tenant and settlement application (2027-04 to 2027-06).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the TVOP; accepts Moderate risk; executive sponsor of the security program |
| Risk acceptor for High risk (authorizing official equivalent) | Chief Executive Officer | Accepts High risk; approves the risk appetite; signs the AOCs as executive officer |
| Oversight | Board audit committee | Quarterly cyber risk and PCI DSS status reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SOC 2 program |
| Information Security Officer | Security Manager | Day-to-day control owner; PCI DSS program lead; incident commander |
| GRC | GRC Analyst | Risk register, policies, ROC and SOC 2 evidence files |
| Infrastructure and recovery | IT Director | Identity provider, cloud, networks, endpoints, backups and recovery |
| PCI DSS validation and payments | Chief Financial Officer | Merchant agreement, QSA engagement, AOC preparation |
| Privacy and legal | General Counsel (Privacy Officer) | Privacy notice, breach determinations, County PAC agreement |
| Business owners | Vice President of Ticketing; Vice President of Marketing and Digital; Director of Premium Seating and Group Sales; Vice President of Venue Operations | Ticketing configuration; website, tag manager, and patron data; virtual terminal users; scanners and venue networks |
| Independent assessment | Co-sourced internal audit firm (P07); QSA firm (ROC) | Annual IT audit; PCI DSS ROC |
| Monitoring | MSSP | 24x7 EDR and SIEM monitoring |

**Where roles overlap.** The Security Manager both runs controls and leads the PCI DSS program. The independent checks are the co-sourced internal audit firm (which assessed P07 and does not operate controls) and the QSA, which is a different firm from both the internal auditor and the MSSP.

## 6. System Information Types and System Categorization
Information types are the closest analogs in NIST SP 800-60 Vol. 2 Rev. 1 (written for federal missions). Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payment collection (card data in the virtual terminal channel and on the website pages that embed the checkout form; tokens and truncated numbers elsewhere) | Moderate | Moderate | Moderate | Card data disclosure triggers acquirer, card brand, and state breach duties and could put MID-T at risk; altered payment pages would harm patrons; sales can fall back to vendor-hosted pages (P05 BP-05 MTD 8 hours) |
| Customer services (patron accounts, orders, marketing preferences) | Moderate | Moderate | Moderate | About 1.1 million patron records; entry at the gates depends on accurate order data, but a manual entry procedure limits the effect of an outage (P05 BP-01) |
| Financial management (show settlements, artist payments, County PAC remittances) | Moderate | Moderate | Low | Wrong or redirected payments cause direct losses; settlement can be rebuilt from reports (P05 MTD 24 hours) |
| Personal identity and authentication (workforce identities) | Moderate | Moderate | Low | Account takeover is a lead High risk (P01 R-002, R-007) |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for card brand and breach investigations |
| **TVOP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Why availability is not High.** An outage during doors has a severe effect on operations and could affect attendee safety (P05 BP-01, MTD 1 hour). The plan relies on a **manual entry procedure** and offline scanning, not on IT recovery, to keep that effect at the Moderate level. The procedure is written and drilled only at the Amphitheater. Until the Music Hall and the Club have theirs (P01 R-018, due 2026-11-30), this rating is an assumption that the Vice President of Venue Operations owns.

**Why confidentiality is not High.** A skimming attack during a headliner on-sale could expose tens of thousands of card numbers (P01 R-001). The team kept confidentiality at Moderate because card data is never stored in the TVOP by design (the vendor and payment partner hold it), and the effect on the company, while serious, would not stop its operations. The payment page controls are treated as the most important controls in this plan to compensate.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the company's ticketing tenant configuration, users, roles, settings, and API keys (not the vendor's platform);
- the 26 virtual terminal users and their laptops, and the 18 box office validated P2PE devices;
- the website, CMS, and tag manager configuration;
- all 4 cloud accounts and their workloads (CMS, patron data platform, settlement application, log pipeline, backups);
- the identity provider tenant;
- corporate and venue networks at 4 sites (SD-WAN edges, firewalls, switches, Wi-Fi);
- 520 laptops and PCs, 180 scanners, and 64 tablets;
- the company's SIEM tenant and its use cases.

**Outside the boundary (external services, interconnected):**
- the ticketing vendor's platform, embedded checkout form, and mobile ticket app;
- the payment partner's gateway, virtual terminal service, and card vault;
- the acquirer;
- the POS and its P2PE solution (SYS-03);
- the productivity suite (SYS-07), physical security systems (SYS-10), premium seating CRM (SYS-11), marketing platform (SYS-12), finance and HR (SYS-13), and chatbot (SYS-15);
- the cloud provider's infrastructure and the MSSP's platform.

**PCI DSS scope relationship.** The cardholder data environment today includes the virtual terminal laptops and the corporate segment they share, plus the website systems that serve pages embedding the payment form (they can affect the security of the payment page). The planned move of the virtual terminal channel to validated P2PE devices removes the laptops and the corporate segment from the cardholder data environment. The scope document required by PCI DSS 12.5.2 is owned by the Security Manager (P03 row G-064).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Ticketing vendor platform (SYS-01) | Bidirectional (web, embedded form, API) | Orders, patron records, scan manifests, settlement reports | Ticketing services agreement; vendor AOC 2026-02-20; SOC 2 Type 2; **no breach notice time in the contract (gap)** |
| Payment partner (SYS-02) | Outbound keyed card data from the virtual terminal; inbound authorizations | Card data (MID-T) | Merchant agreement; partner AOC **dated 2024 (gap)** |
| Acquirer | Settlement and chargeback data through the partner | Transaction records | Merchant agreement (24-hour compromise notice term, fictional) |
| POS vendor (SYS-03) | Inbound daily sales reports | Sales totals by show | POS agreement; P2PE listing |
| Tag manager vendor and 31 script sources | Scripts loaded into patrons' browsers on event pages | Page events, device data | Tag manager terms of service only; **no review of script sources (gap)** |
| Marketing platform (SYS-12) | Outbound nightly segments from the patron data platform | Names, emails, preferences, purchase segments | Service terms; data processing addendum |
| Marketing agency | Tag manager publish rights; 4 local ticketing accounts | Campaign data | **No security terms (gap)** |
| Web agency | Deploy access to the CMS through the cloud pipeline | Website code | Statement of work; **no security terms (gap)** |
| MSSP | Inbound logs; remote response actions | Security logs | MSSP contract; SOC 2 Type 2 |
| Bank | Outbound payment files from the settlement application | Artist and vendor payments | Online banking agreement |
| County (from 2027-07-01) | Outbound settlement statements and patron reports | Sales and patron data for County PAC events | County PAC management agreement |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Ticketing tenant configuration, 186 venue users, 3 API keys | SaaS configuration | Ticketing vendor | Vice President of Ticketing |
| Dynamic pricing and bot mitigation settings | SaaS configuration | Ticketing vendor | Vice President of Ticketing |
| Virtual terminal user accounts (26) | Service provider portal | Payment partner | Director of Premium Seating and Group Sales |
| Box office validated P2PE devices (18) | Payment device | Three box offices | Vice President of Ticketing |
| Website CMS servers and database | Virtual machines and managed database | Workloads account | Vice President of Marketing and Digital |
| Tag manager container (31 scripts) | SaaS configuration | Tag manager vendor | Vice President of Marketing and Digital |
| Patron data platform and nightly sync function | Managed database and serverless function | Workloads account | Vice President of Marketing and Digital |
| Settlement application | Application service and managed database | Workloads account | Controller |
| Network hub, cloud firewall, VPN, log pipeline, privileged access broker | Network and management services | Shared services account | IT Director |
| Organization guardrails, posture management, cloud federation | Identity and policy services | Identity and security account | Security Manager |
| Backup vault (write-once, 35 days) | Backup service | Backup account (second region) | IT Director |
| Identity provider tenant | SaaS | Identity vendor | IT Director |
| SD-WAN edges, firewalls, switches, Wi-Fi (4 sites) | Network | HQ and three venues | IT Director |
| Laptops and PCs (520), scanners (180), tablets (64) | Endpoint | All sites | IT Director |
| SIEM tenant and EDR console | SaaS | MSSP | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The TVOP uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 125 controls** in `control-implementation.csv`. These cover every Moderate-baseline control that carries a PCI DSS v4.0.1 requirement for the ROC scope or an FTC Act or Florida reasonable-security duty, plus the controls that treat the High risks in P01.
- **Selected by tailoring (added):** CA-8 from the High baseline, because PCI DSS 11.4 requires internal, external, and segmentation penetration testing; PM-1, PM-2, PM-5, and PM-9 (program management, not in the baseline), because PCI DSS 12.1, 12.4, and 12.5 and the board's oversight need them; PT-5 from the privacy baseline, because the privacy notice must match the website's data practices (FTC Act Section 5).
- **Inherited without separate statements:** physical and environmental controls for the vendor and cloud data centers (for example PE-9 to PE-17) and platform-level SA and SC controls. These are inherited from the ticketing vendor, payment partner, identity vendor, cloud provider, and MSSP, and are evidenced by their PCI DSS AOCs and SOC 2 Type 2 reports, reviewed each year (P09 `vendor-soc2-review.csv`).
- **Deferred:** the remaining Moderate controls with no PCI DSS, FTC, or Florida link and no Moderate-or-higher risk in P01 (for example SA-15 development process, because the company develops only website templates through the web agency). They are recorded as tailoring decisions and reviewed yearly.
- **CSF 2.0 column.** Subcategories come from the NIST CSF 2.0 to SP 800-53 crosswalk in `00_universal-framework/crosswalks/`. Where the crosswalk has no entry for a control (for example AC-11, PS-3, PT-5, SI-8), the CSF column is an author mapping.

**Status of the 125 documented controls:**
| Status | Count |
|---|---|
| Implemented | 42 |
| Partially implemented | 79 |
| Planned | 4 |
| Not applicable | 0 |

The 4 Planned controls are CP-4 (restore testing), IR-3 (incident response testing), SI-7 (payment page integrity), and SR-2 (supply chain risk management plan).

**Inheritance of the 125 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 81 | Company |
| Hybrid | 33 | Ticketing vendor, payment partner, identity vendor, cloud provider, MSSP |
| Common/Inherited | 11 | Identity vendor (for example IA-2(8), IA-11), cloud provider (CP-6), ticketing vendor (AC-12, IA-8), payment partner (SC-13), MSSP (IR-7) |

The Partially implemented statements trace to the 15 known gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 34 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). The QSA performs the PCI DSS ROC from 2026-11-02 to 2026-11-13. Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce.** Employees authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance. For the Moderate categorization and PCI DSS 8.4 this is acceptable for general and administrative access through SSO.
- **Exceptions that do not meet this statement today.** 11 local ticketing accounts and the 9 tag manager publishers sign in with passwords only, and virtual terminal users rely on the payment partner's SMS one-time codes. All local ticketing accounts move to SSO or the vendor's app-based MFA, and the tag manager moves to SSO with MFA, by 2026-10-31 (P01 R-002; P03 8.4). The virtual terminal accounts end when the channel moves to P2PE devices (2026-10-30).
- **Administrators.** Administrators of the identity provider, the ticketing tenant, and the cloud move to phishing-resistant security keys by 2027-03-31 (P01 R-007, R-036).
- **Patrons.** Patrons create accounts on the ticketing vendor's platform under the vendor's sign-in controls. That is governed by the vendor and outside this boundary (P01 R-049 tracks patron account takeover).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks and notification matrix (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **ASV:** Approved Scanning Vendor
- **CDE:** cardholder data environment
- **CMS:** content management system
- **County PAC:** County Performing Arts Center
- **MID-T / MID-F:** the ticketing and the food, beverage, and merchandise merchant accounts
- **MFA:** multi-factor authentication
- **MSSP:** managed security service provider
- **P2PE:** point-to-point encryption (PCI SSC validated solutions)
- **POA&M:** plan of action and milestones
- **QSA:** Qualified Security Assessor
- **ROC:** Report on Compliance
- **TVOP:** Ticketing and Venue Operations Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | GRC Analyst |
| 1.0 | 2026-09-15 | Updated with P07 results; approved by the Chief Operating Officer | Security Manager |
