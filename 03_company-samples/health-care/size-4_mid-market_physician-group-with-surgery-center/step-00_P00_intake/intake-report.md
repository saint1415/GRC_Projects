# Intake Report: Cris Santos Company | Health Care and Social Assistance | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed multi-specialty physician group with an ASC and an imaging center, 10 Florida sites) |
| Intake window | 2026-06-15 to 2026-07-02 |
| Collected by | Security Manager and the 2 security analysts, with the vCISO and the Compliance and Privacy Officer |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-06. It covers the organization, the systems that create, receive, maintain or transmit ePHI, the suppliers that touch them, and the rules that may bind the company. At this size the sources are systems of record: the identity provider, the HR system, the endpoint and EDR consoles, the cloud organization console, the SIEM, the accounts payable vendor master, the contract register and BAA register, prior risk analyses and internal audit reports, scan results and the incident log. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, samples, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-008 | Identity provider; HR system; directory, EHR, PACS and cloud admin consoles; HR procedures | 2025-09-01 to 2026-06-30 |
| Devices and network | EV-009 to EV-016 | Endpoint management and EDR consoles; clinical engineering spreadsheet and biomedical service schedule; SD-WAN orchestrator; firewalls; scanner; patch and change records | 2026-06-15 to 2026-06-30 |
| Cloud, backups and monitoring | EV-017 to EV-022 | Cloud organization console; backup service; MSSP portal and SIEM; EHR audit settings; interface documentation | 2026-06-30 |
| Programs and documents | EV-023 to EV-034 | Intranet library; document requests; ASC plan; GRC folder; internal audit; incident tracker; Compliance case files; LMS; HR and Compliance files | 2023-03-01 to 2026-06-30 |
| Suppliers and contracts | EV-035 to EV-044 | ERP accounts payable; Compliance contract database and vendor files; vendor portals; contract register; revenue cycle and certification records; benefits files; executive files | 2026-01-01 to 2026-06-30 |
| Facilities and media | EV-045 to EV-047 | Walk-throughs at 4 sites; badge system; destruction certificates and lease checklist | 2026-06-26 to 2026-06-30 |
| Business volume | EV-048, EV-049 | ERP general ledger; EHR/PM reporting | 2025-12-31 to 2026-06-30 |
| AI tools, email and PACS | EV-050 to EV-052 | Identity provider app list, accounts payable and department survey; email filter; PACS admin console | 2026-06-29 to 2026-06-30 |

## 3. Observations by area
**Users and access.** The identity provider holds active named accounts for all 600 employees on the HR roster, plus contractor, vendor and service accounts, and every active user account has MFA registered (EV-001). Conditional access requires MFA for all users; the allowed methods are push with number matching and one-time codes (EV-002). HR recorded 118 terminations and 64 internal transfers in the 12 months to 2026-06-30 (EV-003). The HR feed disables identity provider accounts on the termination date; on a transfer it changes department and title only, and EHR roles, badges and local directory accounts change through separate tickets (EV-004, EV-008). The last user access review was the annual campaign in January 2026 (EV-005). 41 accounts hold administrator roles across 5 admin planes; just-in-time elevation through the privileged access broker covers the 4 cloud accounts only (EV-006). The EHR has a 48-role catalog, 212 new accounts were created in the 12 months, and bulk export rights sit in several CBO roles (EV-007).

**Devices and network.** The endpoint console lists 750 workstations and laptops (including the 10 downtime report workstations) and 120 tablets, 870 in total, with disk encryption reported on 99.6% (EV-009). EDR reports on 100% of managed endpoints and servers; medical devices and the 2 legacy consoles have no agent (EV-010). The medical device spreadsheet lists about 240 networked devices, while the biomedical service schedule and purchasing records count about 400; the lists were not reconciled (EV-011). Medical devices have their own VLAN at Clinics 1-3, the ASC and the imaging center, and share the workstation VLAN at Clinics 4-8. The ASC and imaging center have dual ISPs; each clinic has one (EV-012). 14 vendors have remote access; PACS and modality vendors use their own tools with standing accounts, and 4 VPNs to referring hospitals run without written interconnection terms (EV-013, EV-040). The C-arm console at the ASC and one MRI console at the imaging center run Windows versions past vendor support (EV-014). Scans run quarterly, with 50 Critical findings in Q1 and Q2 2026; PACS servers and medical devices are outside the scan scope (EV-015). Configuration baselines were provided for workstations and cloud virtual machine images (EV-016).

**Cloud, backups and monitoring.** The landing zone has 4 accounts, with organization guardrails, company-managed keys and control-plane logging in every account (EV-017). Daily backups go to a separate backup account in a second region with 35-day write-once retention and separate administrator credentials. No restore jobs were recorded for the interface engine, PACS or data warehouse, and the ASC pump server is not in backup scope (EV-018). The SIEM receives EHR, identity provider, cloud, firewall and EDR logs; PACS, the interface engine, file services, the data warehouse and medical devices are not connected (EV-019). The MSSP's detection use cases are unchanged since 2024 (EV-020). EHR access review is logged monthly for VIP-flagged patients only (EV-021). Interface engine logs are kept locally, and interface mapping changes have one analyst's review (EV-022).

**Programs and documents.** Five security policies were approved in 2023 with no review record since. Four standards date from 2023, and there is no configuration, logging, vendor risk, medical device or AI standard (EV-023). The request for a contingency plan and restore records for company-managed workloads returned only the clinic downtime procedures and the EHR vendor's disaster recovery summary (EV-024). Each site has a downtime report workstation with an hourly read-only extract. There are no written pump or PACS downtime procedures (EV-025). The ASC emergency preparedness plan (2025 revision) lists fire, hurricane, utility loss and mass casualty as hazards, and no cyber hazard (EV-026). The last risk analysis is dated July 2025, and 6 of its 14 treatment items were open in June 2026 (EV-027). The 2025 internal IT audit was reported to the audit committee (EV-028). The IT Director has been the designated Security Officer since 2023 (EV-029). The 2023 incident response plan has no review record since adoption, and the 2025 tabletop recorded 6 actions (EV-030). The incident log holds 37 incidents for 2025 and 2026 (EV-031). There are 6 privacy incident files and 3 breaches under 500 individuals, reported to HHS on 2026-02-20 (EV-032). Training completion is 96%, reminders are monthly, and the June 2026 phishing click rate was 7.8% (EV-033). 11 sanctions were recorded in 2025 (EV-034).

**Suppliers and contracts.** Accounts payable paid about 900 vendors in the 12 months, including 3 AI vendors (EV-035). Compliance flags 140 vendors with PHI access; BAAs were located for 110 and not for 30. The BAA template dates from 2013, the chatbot vendor has no BAA, and the AI scribe BAA permits de-identified data use (EV-036). Vendors are reviewed at onboarding only. There is no security or privacy review record for 4 AI tools, and the purchasing policy has no BAA check (EV-037). The EHR vendor's SOC 2 Type 2 report (12 months ending 2026-03-31) states RTO 12 hours and RPO 1 hour (EV-038). The identity and cloud providers' SOC 2 reports are on file (EV-039). Modality and copier leases have no media sanitization clause (EV-040). The cyber insurance policy has a $10 million limit and a $250,000 retention, with notice through the carrier hotline first (EV-041). One clearinghouse handles all payers, about $1.9 million in expected collections a week, and the ASC is Medicare-certified (EV-042). The employee health plan is fully insured (EV-043). The hospital joint venture partner requests a SOC 2 Type 2 report (EV-044).

**Facilities and media.** Walk-throughs at Clinic 1 with the CBO, Clinic 5, the ASC and the imaging center (2026-06-23 to 2026-06-26) found badge readers at the ASC, the imaging center and Clinic 1. The Clinic 5 network closet has a keyed lock, and no key log was presented (EV-045). Badge records cover the ASC, the imaging center and Clinics 1-3; Clinics 4-8 closets use keys (EV-046). Drive destruction certificates and reimaging tickets are on file. The lease return checklist does not ask for a sanitization certificate (EV-047).

**Business volume.** Revenue was about $100 million in FY2025: clinics about $60 million, the ASC about $22 million, the imaging center about $12 million and other services about $6 million, over about 250 operating days (EV-048). There are about 110,000 active patients, about 1,900 clinic visits, 28 ASC cases and 160 imaging studies a day (EV-049).

**AI tools, email and PACS.** Five AI tools are in use (EV-050). Four were adopted by departments: the scribe, the imaging triage module, prior-authorization automation and the website chatbot. The EHR alert library came with the EHR. No approved-tools list exists, and staff report using public generative AI sites. Email filtering and an advisory mailbox are in place (EV-051). The PACS vendor support role has standing administrator access (EV-052).

**Reconciliation across sources.**
- **Workforce.** The 600 employees on the HR roster each have an identity provider account (EV-001, EV-003).
- **Endpoints.** The endpoint console count (870) matches the SSP boundary and the P07 sampling population (EV-009).
- **Medical devices.** The two sources differ by about 160 devices (about 240 against about 400). That difference stays an open request (EV-011).
- **Vendors.** About 900 vendors in accounts payable, 140 of them flagged with PHI access, 110 with BAAs located (EV-035, EV-036). The named vendors and a summary row in [`vendor-register.csv`](vendor-register.csv) add up to the 140.
- **AI tools.** Three AI vendors in accounts payable, plus the triage module bought with the PACS and the EHR alert library, give the 5 tools in [`asset-inventory.csv`](asset-inventory.csv). Public chatbot use comes from the survey only (EV-035, EV-050).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Reconcile the medical device spreadsheet (about 240) with the biomedical service schedule and purchasing records (about 400) | IT Director with clinical engineering | 2026-06-29 | Not reconciled at intake; P07 passive capture (EV-CM-8) and POAM-008 carry it |
| What plan information the company receives as health plan sponsor | HR Director and the benefits broker | 2026-06-24 | Answered in P03 fieldwork on 2026-07-22 (EV-064) |
| Subcontractor lists from the MSSP and the EHR vendor | Compliance and Privacy Officer | 2026-07-01 | Not received; requested again in P03 (EV-061) |
| Current SOC 2 reports and bridge letters for Tier 1 vendors (MSSP, clearinghouse, AI scribe vendor) | Compliance and Privacy Officer | 2026-07-01 | Obtained for the P09 vendor review in 2026-09 |
| Number of staff using public generative AI sites, and what they enter | vCISO with department heads | 2026-07-02 | Not established at intake; P01 R-025 and P10 treat it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Business units and owners (EV-003), revenue and volumes (EV-048, EV-049), EHR vendor recovery commitments (EV-038), backup design (EV-018), clearinghouse dependence (EV-042), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-022 |
| P04 Cloud mapping | Landing zone components (EV-017, EV-018) and provider assurance (EV-038, EV-039) |
| P01 Risk register | Likelihood inputs from the incident log (EV-031), scan results (EV-015), phishing results (EV-033), configuration exports, the walk-throughs and the prior analysis (EV-027) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements; sample populations (EV-003, EV-007, EV-018, EV-031, EV-035, EV-036) |
| P06 Policies | The 2023 policies and standards (EV-023) and the ASC plan (EV-026) |
| P07 Control assessment | Populations to sample from: 118 terminations and 64 transfers (EV-003), 212 new EHR accounts (EV-007), 41 privileged accounts (EV-006), about 240 inventoried devices (EV-011), 870 endpoints (EV-009), 110 BAAs and about 900 vendors (EV-035, EV-036), 37 incidents (EV-031), 50 Critical findings (EV-015) |
| P08 IR runbooks | Notification duties from the obligations register; insurer terms (EV-041); clearinghouse and vendor contacts from the vendor register |
| P09 SOC 2 | The partner's request (EV-044) and vendor assurance on file (EV-037 to EV-039) |
| P10 AI governance | AI tools found (EV-035, EV-050) and their agreements (EV-036) |
