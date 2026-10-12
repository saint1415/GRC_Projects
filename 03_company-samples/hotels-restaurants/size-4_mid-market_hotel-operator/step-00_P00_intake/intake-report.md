# Intake Report: Cris Santos Company | Accommodation and Food Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Florida hotel owner and operator: 2 independent resorts and 4 franchised select-service hotels) |
| Intake window | 2026-06-15 to 2026-07-02 |
| Collected by | GRC Analyst, with the Security Manager and the vCISO |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-06. It covers the organization, the 6 hotels, the central reservations office (CRO) and the corporate office; the systems that store, process or transmit card data and guest data; the franchisor's platform where it touches the company's hotels; the suppliers that touch those systems; and the rules that may bind the company, including its contracts. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, samples, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-009 | Identity provider; HR system; SYS-01 admin console; brand PMS user reports; privileged access broker; HR files | 2026-02-27 to 2026-06-30 |
| Endpoints, networks and remote access | EV-010 to EV-018 | Endpoint and EDR consoles; SD-WAN orchestrator; firewall management; remote access records; asset records; scanning platform; IT service management | 2026-06-22 to 2026-06-30 |
| Cloud, servers, backups and logging | EV-019 to EV-023 | Cloud organization console; backup service; lock and POS server consoles; MSSP portal | 2026-06-26 to 2026-06-30 |
| Program documents and records | EV-024 to EV-028 | Intranet library; GRC folder; audit committee materials; incident tracker; learning management system | 2026-06-22 to 2026-06-30 |
| Payments and PCI DSS | EV-029 to EV-033 | CFO's contract files; acquirer portal; device lists and inspection logs; payment channel interviews | 2025-12-31 to 2026-06-30 |
| Suppliers and contracts | EV-034 to EV-042 | ERP accounts payable; GRC vendor register; vendor and provider portals; contract management system | 2026-03-31 to 2026-06-30 |
| Facilities, disposal and continuity | EV-043 to EV-045 | Badge system and visitor logs; disposal and lease records; hotel operations files | 2026-06-24 to 2026-06-30 |
| Business volume and data holdings | EV-046 to EV-049 | ERP general ledger; SYS-01, brand PMS and CRM reporting; contact center console | 2025-12-31 to 2026-06-30 |
| Email, websites, HR systems, interfaces and AI tools | EV-050 to EV-055 | Productivity suite; booking engine and channel manager; websites; AI tool discovery; HR system; interface register | 2026-06-26 to 2026-06-30 |

## 3. Observations by area
**Users and access.** Every workforce account has MFA registered, and MFA is required for corporate applications, email, cloud consoles, VPN and all 162 SYS-01 users (EV-001, EV-002). HR recorded 600 employees, 212 terminations and 70 transfers in the 12 months to 2026-06-30 (EV-003). Identity provider accounts follow HR events automatically; brand PMS accounts are requested from the franchisor by each General Manager (EV-004). In SYS-01, 46 of 162 users hold the full card display permission, and 96 accounts were created in the 12 months (EV-005). The last SYS-01 access review was in February 2026 (EV-006). The brand PMS lists 64 company accounts, and one night-audit login is shared at 3 of the 4 franchised hotels (EV-007). There are 38 company privileged accounts. The access broker covers the cloud and SYS-01 administration; domain administrators at the resorts and local administrators on the Resort 2 POS and lock servers sit outside it (EV-008). Background checks are run for finance, IT, front office managers and CRO agents (EV-009).

**Endpoints, networks and remote access.** The endpoint console lists 520 PCs and laptops and 180 tablets and phones (EV-010). EDR runs on 470 of the 520 PCs; the other 50, at Hotels 3 to 6, run basic antivirus, and the 38 Resort 2 POS workstations run a legacy agent (EV-011). The resorts separate payment, POS, lock, CCTV and office traffic into VLANs. Each of Hotels 3 to 6 has one staff network behind a brand-managed firewall, and guest Wi-Fi is a separate vendor network everywhere (EV-012). One firewall rule permits directory traffic from the Resort 2 POS VLAN to the corporate domain controllers, and the brand firewalls do not appear in company tools (EV-013). The Resort 2 POS vendor and the lock vendor use always-on remote tools with shared logins and no MFA, and the franchisor's network vendor has standing access to the brand firewalls (EV-014). The Resort 2 POS server and lock server run operating systems out of vendor support (EV-015). Internal scans cover the corporate office, CRO, resorts and cloud but not Hotels 3 to 6, and quarterly ASV scans have passed since Q1 2025 (EV-016). Changes by the POS and lock vendors are not ticketed, and no documented baseline exists for firewalls, POS workstations or lock servers (EV-017). The last segmentation test is from 2024 and covered the resorts only (EV-018).

**Cloud, servers, backups and logging.** The landing zone has 4 accounts with organization guardrails and a write-once log bucket (EV-019). Cloud workloads are backed up daily to a separate backup account in a second region with 35-day write-once retention, and no restore of the data warehouse or CRM ran in the quarter (EV-020). The resort lock servers back up weekly to a local disk; the lock servers and the Resort 2 POS server keep 30 days of logs locally (EV-021). The SIEM receives identity, email, cloud, EDR, VPN and corporate and resort firewall logs, but not the Resort 2 POS server, the lock servers or Hotels 3 to 6 (EV-022). MSSP monthly reports cover alerts on connected sources (EV-023).

**Program documents and records.** The policies were adopted in 2024. Four standards exist from 2024; there is no configuration, logging, vendor, payment device or contingency standard (EV-024). The last risk assessment was in June 2025, and the co-sourced firm audits IT each year (EV-025). The 2024 incident response plan has no card brand, acquirer or franchisor notice steps; a ransomware tabletop was held in November 2025 (EV-026). The incident log includes a suspected skimmer at Hotel 5 in 2026-03, recorded as handled with the franchisor (EV-027). Awareness training reached 96% of employees, and the June 2026 phishing simulation click rate was 6.1% (EV-028).

**Payments and PCI DSS.** The acquirer's letter of 2026-05-18 requires a QSA-supported SAQ D, signed by an officer, for 2026, due 2026-12-31 (EV-029). The 2025 SAQ D was prepared internally and signed by the CFO; its scope section does not list the call recording store or the shared mailboxes (EV-030). The company ran about 1.05 million card transactions under 10 merchant accounts, including about 48,000 card numbers keyed by CRO agents (EV-031). Device lists with serial numbers exist for the 78 P2PE devices at the resorts, not for the 12 brand terminals or the 30 Resort 2 readers; only Resort 1 keeps inspection logs (EV-032). Card data passes in clear through the Resort 2 POS, CRO agents key card numbers on general-purpose PCs, and group sales and catering still receive card forms by email (EV-033).

**Suppliers and contracts.** About 120 vendors were paid in the year (EV-034). Of 31 vendors that handle card or guest data, 9 have no current AOC or SOC 2 report on file, and responsibility matrices exist only for SYS-01 and the resort gateway (EV-035). The SYS-01 vendor's SOC 2 report states RTO 4 hours and RPO 15 minutes; the contract states none (EV-036). The channel manager's AOC is dated 2025-04, and the franchisor has provided a summary letter rather than an AOC (EV-037). Cloud and identity provider reports are on file (EV-038). The franchise agreements require 24-hour notice of a suspected compromise and brand access to the property firewalls, and do not allocate PCI DSS requirements (EV-039). The REIT management agreement signed 2026-06-30 requires a SOC 2 Type 2 report on the hotel management platform within 18 months of 2027-01-01 and incident notice within 48 hours (EV-040). The cyber policy has a $10 million limit and a $250,000 retention (EV-041). The chatbot contract has no retention or masking terms, and the revenue-management contract allows pooling of company data (EV-042).

**Facilities, disposal and continuity.** Resort server rooms use badge readers; no visitor or key logs were provided for Hotels 3 to 6 (EV-043). Shredding certificates are on file, and 2 leased copiers were returned in 2026 (EV-044). The resort hurricane plans include IT steps; the Hotels 3 to 6 plans do not (EV-045).

**Business volume and data holdings.** Revenue was about $100 million in FY2025, about $274,000 a day (EV-046). The hotels host about 147,000 stays and about 400 arrivals a day, and the CRO handles about 900 calls a day (EV-047). SYS-01 holds about 410,000 guest profiles and about 152,000 ID scans created since 2019, and the CRM about 265,000 profiles, with nothing deleted by age (EV-048). CRO recordings are kept 13 months (about 148,000 in the store), and 14 users can play them (EV-049).

**Email, websites, HR systems, interfaces and AI tools.** Six shared mailboxes serve group sales, catering and accounting (EV-050). The booking engine shows the total price with the $40 resort fee and embeds its payment form by iframe on the company's websites (EV-051). The 2023 privacy notice states that the company does not store card data (EV-052). Six AI uses were found; the first five went live with no security, privacy or legal review on record (EV-053). The 14 time clocks store finger templates, and the applicant tracking system declines low-scored applications automatically (EV-054). Four of 11 interface credentials show no change since installation (EV-055).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Brand firewall rule sets and change records for Hotels 3 to 6 | Franchisor's regional IT contact | 2026-06-24 | Not provided; P03 and P07 rely on company-side observation and the franchisor's written answers |
| Franchisor's PCI DSS AOC and business continuity plan | Franchisor, through the General Counsel | 2026-06-24 | Summary letter only (EV-037); continuity plan not provided (EV-039); carried into P01 (R-016) |
| Recovery commitments for SYS-01 in the contract | SYS-01 vendor, through the Chief Operating Officer | 2026-06-24 | None in the contract (EV-036); P05 uses the SOC 2 system description values; carried into P01 (R-014) |
| Current AOC or SOC 2 report from the 9 card and guest-data vendors without one | Each vendor, through the GRC Analyst | 2026-06-30 | Not received by the end of intake; P03 (G-061) and P09 |
| Confirmation of background checks on contracted workers | 2 staffing companies, through the HR Director | 2026-06-24 | Not provided; carried into P01 (R-024) |
| Number of staff using public generative AI sites, and what they enter | Department heads, through the vCISO | 2026-07-02 | Not established at intake; P10 and P01 (R-038) treat it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003), revenue and volumes (EV-046, EV-047), vendor recovery statements (EV-036, EV-039), backup design (EV-020, EV-021), downtime procedures (EV-045), and dependencies from the asset and vendor registers |
| P02 SSP | The boundary from the asset inventory; as-found configuration from EV-001 to EV-023, EV-032, EV-043 and EV-055 |
| P04 Cloud mapping | Cloud components (EV-019, EV-020) and provider and vendor assurance (EV-036 to EV-038) |
| P01 Risk register | Likelihood inputs from the incident log (EV-027), scan results (EV-016), phishing results (EV-028), configuration exports, contracts and the vendor register |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with PCI DSS and the FTC, FACTA and Florida rules |
| P06 Policies | The 2024 policies and standards (EV-024) |
| P07 Control assessment | Populations to sample from (EV-003, EV-005, EV-007, EV-008, EV-016, EV-017, EV-027, EV-032, EV-035) |
| P08 IR runbooks | Notification duties from the obligations register; contacts and notice terms from the vendor register, the franchise agreements (EV-039), the REIT agreement (EV-040) and the cyber policy (EV-041) |
| P09 SOC 2 | The REIT agreement (EV-040) and vendor assurance on file (EV-035 to EV-038) |
| P10 AI governance | AI tools found (EV-053), their contracts (EV-042) and the systems they touch (EV-049, EV-054) |
