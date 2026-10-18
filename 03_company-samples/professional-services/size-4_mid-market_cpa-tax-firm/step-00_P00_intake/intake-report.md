# Intake Report: Cris Santos Company | Professional, Scientific, and Technical Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed CPA, tax, and advisory firm with 6 Florida offices, and its attest affiliate Cris Santos Assurance, LLP) |
| Intake window | 2026-06-15 to 2026-07-02 |
| Collected by | GRC Manager and GRC Analyst, with the Director of Information Security (Qualified Individual) and the Privacy Officer |
| Approved | Chief Operating Officer, 2026-09-22 |

## 1. Purpose and scope
Intake collected the Company's own records before any assessment work began on 2026-07-06. It covers both entities under the one security program, the systems that hold or reach customer information, tax return information and the ePHI of health care clients, the service providers that touch them, and the rules that may bind the Company. At this size the sources are systems of record: the identity provider and privileged access broker, the HR system, the endpoint, EDR and mobile device consoles, the cloud organization console, the SIEM and MSSP portal, the vulnerability scanner, SaaS discovery, the tax software, portal, DMS and CAS platform admin consoles, the ERP accounts payable vendor master, the contract register and BAA tracker, prior risk assessments and board materials, and the incident queue. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, samples, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-012 | Identity provider; HR system; privileged access broker and admin consoles; service desk; DMS, tax software, CAS platform and workpaper admin consoles | 2026-01-30 to 2026-07-01 |
| Devices and network | EV-013 to EV-020 | Endpoint management and EDR consoles; MDM; print management; SD-WAN and firewalls; vulnerability scanner; penetration test report; vendor access list | 2025-11-21 to 2026-06-30 |
| Cloud, backups, monitoring and SaaS | EV-021 to EV-028 | Cloud organization console; backup service; DR records; SIEM and MSSP portal; mail and gateway settings; portal admin console; SaaS discovery | 2026-06-24 to 2026-07-01 |
| Programs and documents | EV-029 to EV-039 | Intranet policy library and GRC folder; DMS reporting; executive and corporate secretary files; incident queue; LMS; HR files | 2024-03-01 to 2026-06-30 |
| Entity, IRS and clients | EV-040 to EV-042 | General Counsel's files; IRS e-Services and tax operations files; tax software client list | 2026-06-24 to 2026-07-01 |
| Suppliers and contracts | EV-043 to EV-052 | ERP accounts payable; contract register and vendor files; vendor portals; BAA tracker; consent records; insurance file | 2025-12-01 to 2026-06-30 |
| Facilities and media | EV-053 to EV-055 | Walk-throughs at Offices 1, 4 and 6; badge system; destruction certificates and lease files | 2026-06-23 to 2026-06-30 |
| Business volume | EV-056, EV-057 | ERP general ledger; tax software, portal, DMS and CAS platform reports | 2025-12-31 to 2026-06-30 |
| AI tools and change | EV-058 to EV-060 | Applicant tracking system; AI tool discovery summary; change system | 2026-06-30 to 2026-07-01 |

## 3. Observations by area
**Users and access.** The identity provider holds unique, MFA-registered accounts for all 600 employees on the HR roster, plus seasonal staff, interns, contractors and about 30 offshore vendor staff (EV-001). Conditional access requires push MFA with number matching on every federated system and blocks legacy authentication. Mailbox access from an unmanaged device needs MFA only, and offshore vendor staff reach the desktop gateway from approved address ranges with no device check (EV-002). No phishing-resistant method is registered for any user (EV-003). HR recorded 96 terminations, 58 transfers and 131 seasonal end dates in the 12 months (EV-004). The HR feed manages identity provider accounts, and 412 accounts were created; local accounts in the payroll and bill-pay services sit outside the feed (EV-005). The last access review was the annual campaign in January 2026 (EV-006). There are 41 privileged accounts; 14 IT staff hold standing administrator rights on daily accounts, break-glass accounts exist for the cloud organization only, and 9 service accounts have non-expiring passwords (EV-007). The service desk verifies reset callers with an employee ID and the manager's name (EV-008). A tax practice group opens every tax client folder in the DMS, and PHI from health care engagements sits in general folders (EV-009). The tax software audit log shows the AI drafting feature turned on in 2026-03 and used on about 2,100 returns, with no change ticket; its activity logs are kept 90 days (EV-010). The payroll and bill-pay services use local accounts with SMS codes (EV-011). Workpaper engagement folders can be opened by all assurance staff, and the enclave is limited to 22 named analysts (EV-012).

**Devices and network.** The endpoint console lists 640 laptops, 110 desktops, 26 multifunction printers and 18 high-volume scanners (776 managed endpoints and devices), with disk encryption on all laptops and desktops and EDR on every managed endpoint and server. Unapproved remote access tools appear on 7 laptops, and 12 scanning stations share one local administrator password (EV-013). About 520 phones are enrolled in mobile device management (EV-014). 8 older printers store scans on unencrypted drives, and pull printing runs at Offices 1-3 only (EV-015). Office 1 has dual ISPs and Offices 2-6 one each. The virtual desktop subnet has a route to all DMS shares, and no alert watches egress volume (EV-016). Scans run quarterly, monthly for internet-facing services since 2026-06, with 40 Critical findings in Q1-Q2 2026 (EV-017). The 2025-11 penetration test scope does not list the portal configuration, the virtual desktop pool or the CAS tenant (EV-018). A benchmark scan of 12 cloud servers found 31 deviations (EV-019). Two software vendors reach the DMS servers with their own remote tools, outside the broker (EV-020).

**Cloud, backups, monitoring and SaaS.** The 5-account landing zone has guardrails, posture detection, a 7-year locked log archive and Company-managed keys; the enclave holds no PHI yet (EV-021). Daily backups of the DMS, the workpaper server and file services go to a write-once vault in a separate account and region (EV-022). The 2025 DMS restore met its 12-hour RTO. There is no restore record for the workpaper server, no exercise of the CAS repeat-payroll fallback, and no procedure for a tax software vendor outage near a deadline (EV-023). The SIEM does not receive tax software, portal, DMS or CAS platform activity, and no rule watches bulk downloads (EV-024). The MSSP suppressed inbox-rule alerts from 2026-02-02 to 2026-04-20 and reported token-theft and help desk impersonation attempts in 2026; its contract has no BAA (EV-025). No mail rule encrypts or blocks outbound tax attachments (EV-026). Client MFA on the portal is optional, with 58% of individual clients enrolled (EV-027). SaaS discovery found 41 unapproved applications, 6 holding client data, and public chatbot use by 9 staff with client names and notice text (EV-028).

**Programs and documents.** The 2024 WISP has POL-01 to POL-05 and five 2024 standards, and no configuration, logging, vendor risk, AI or offshore standard; the 2024 incident response plan has no IRS reporting or refund-diversion steps (EV-029). The 2024 retention schedule has no recorded disposal run, and the DMS holds files of about 95,000 former-client consumers older than 7 years (EV-030). The Qualified Individual was designated in writing on 2024-03-01 (EV-031). Risk assessments were completed in July 2024 and July 2025 (34 risks), with no ePHI-specific analysis (EV-032). The 2025-10 board report has no section on service provider oversight or penetration test results (EV-033). The incident queue holds 31 incidents for 2025 and 2026 (EV-034). The 2025 ransomware tabletop listed 7 actions (EV-035). The June 2026 phishing click rate was 6.1%, and 96% of staff signed the annual acknowledgment (EV-036). Staff sign a confidentiality agreement citing sections 7216 and 6713 at hire (EV-037), and no written notice is on file for contractor staff with access (EV-038). The security team is 4 people (EV-039).

**Entity, IRS and clients.** The Attest Firm is a separately licensed CPA partnership using Company staff and systems under an administrative services agreement, is not PCAOB-registered and audits no issuers (EV-040). The Company is an ERO with 6 EFINs and about 300 PTIN holders (EV-041). It holds records on about 205,000 consumers and about 90,000 other individuals (EV-042).

**Suppliers and contracts.** About 85 service providers hold or can reach customer information (EV-043). 31 of their contracts have no security terms, reviews happen only at onboarding, and there is no BAA with the MSSP (EV-044). SOC 2 reports for the tax software vendor (RTO 8 hours, RPO 1 hour), the cloud, identity and productivity providers and the accounting service are on file; the offshore vendor has an ISO/IEC 27001 certificate and no SOC 2 (EV-045). The tax software service was degraded for about 3 hours on 2026-04-14 (EV-046). The offshore contract sets no time for reporting vendor staff turnover (EV-047). A 2025 amendment states U.S.-only processing and no training for the AI sub-processor, with no independent assurance (EV-048). BAAs are on file for all 44 health care clients, and 11 set notice terms of 5 to 10 business days (EV-049). Offshore and release consents state no duration, and releases are not blocked when a consent is missing (EV-050). The CAS agreement sets a 72-hour incident notice (EV-051). The cyber policy has a $15 million limit and a $500,000 retention (EV-052).

**Facilities and media.** Walk-throughs at Offices 1, 4 and 6 found badge readers at all three, key-only network closets at Offices 4 and 6 with no key log, open print trays at Offices 4 and 6, and unmasked SSNs on scanned images viewed on an offshore desktop (EV-053). Badge access covers all 6 offices (EV-054). Lease returns of printers and scanners have no sanitization certificate step (EV-055).

**Business volume.** Revenue was $100.0 million in FY2025 over about 250 business days, with about 50% of tax receipts billed from February 1 to April 15 (EV-056). On a peak day the Company completes about 1,700 individual and 300 business returns and about 2,900 transmissions; CAS runs about 40 payrolls a business day (EV-057).

**AI tools and change.** The applicant tracking module screened about 6,800 applicants in 2026 (EV-058). Six AI uses were found, each turned on by a practice leader or department with no review record (EV-059). Infrastructure changes go through the change board, and no tickets record SaaS tenant setting changes (EV-060).

**Reconciliation across sources.**
- **Workforce.** The 600 employees on the HR roster each have an identity provider account (EV-001, EV-004).
- **Endpoints.** The endpoint console count (776 managed endpoints and devices, plus about 520 phones) matches the SSP boundary (EV-013, EV-014).
- **Vendors.** About 85 service providers in accounts payable and the contract register; the named vendors and a summary row in [`vendor-register.csv`](vendor-register.csv) cover them (EV-043, EV-044).
- **AI tools.** The 6 AI uses in [`asset-inventory.csv`](asset-inventory.csv) come from SaaS discovery, accounts payable and system settings; public chatbot use beyond the 9 staff found was not established (EV-028, EV-059).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots beyond the 9 found, and what they enter | Director of Information Security with the practice leaders | 2026-07-01 | Not established at intake; P10 treats it as unknown |
| Identity, location and independent assurance of the tax software's AI sub-processor | National Tax Practice Leader with the tax software vendor | 2026-06-26 | Not received; carried into P09 (VEN-01) and the P10 conditions |
| Current SOC reports and bridge letters for the payroll, portal, MSSP and bill-pay providers | GRC Manager | 2026-06-26 | Obtained for the P09 vendor review in 2026-09 (EV-071), except the bill-pay bridge letter |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Business units and owners (EV-004), revenue and volumes (EV-056, EV-057), vendor recovery commitments (EV-045), backup design and restore records (EV-022, EV-023), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-028 |
| P04 Cloud mapping | Landing zone components (EV-016, EV-021, EV-022) and provider assurance (EV-045) |
| P01 Risk register | Likelihood inputs from the incident queue (EV-034), scan results (EV-017), phishing results (EV-036), MSSP reports (EV-025), configuration exports and the walk-throughs |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements; sample populations (EV-004, EV-034, EV-043, EV-047, EV-049, EV-050, EV-055) |
| P06 Policies | The 2024 WISP, policies and standards (EV-029) and the retention schedule (EV-030) |
| P07 Control assessment | Populations to sample from: 131 seasonal accounts, 96 terminations and 58 transfers (EV-004), 412 new accounts (EV-005), 41 privileged accounts (EV-007), about 5,500 offshore returns (EV-047), about 1,900 releases (EV-050), about 85 contracts (EV-044), 40 Critical findings (EV-017), 31 incidents (EV-034), 64 destruction certificates (EV-055) |
| P08 IR runbooks | Notification duties from the obligations register; insurer terms (EV-052); BAA and CAS notice terms (EV-049, EV-051); contacts from the vendor register |
| P09 SOC 2 | CAS agreements (EV-051) and vendor assurance on file (EV-045) |
| P10 AI governance | AI tools found (EV-028, EV-058, EV-059) and their contract terms (EV-048) |
