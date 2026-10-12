# Intake Report: Cris Santos Company | Financial Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (merchant payment processor; one Florida office, platform in one public cloud tenant) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager (Information Security Lead and Qualified Individual), with the Compliance and Risk Manager |
| Approved | COO, 2026-08-31 |

## 1. Purpose and scope
Intake collected the processor's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that store, process or transmit account data and customer information (the cardholder data environment and the systems connected to it), the service providers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, exports, samples, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07). Only the QSA's Report on Compliance can conclude on PCI DSS compliance.

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-011 | Identity provider; HR information system; IT help desk tickets; HR files; cloud provider console; merchant portal admin console | 2025-01-01 to 2026-07-06 |
| Devices, network and cloud configuration | EV-012 to EV-025 | Endpoint and EDR consoles; office network documentation; bastion; load balancer and terminal gateway settings; WAF and content delivery consoles; cloud asset inventory; repository and pipeline; scan and penetration test reports | 2025-10-15 to 2026-07-07 |
| Logging and monitoring | EV-026 to EV-029 | SIEM service console; IT help desk ticket | 2026-06-30 to 2026-07-01 |
| Data protection, keys and AI model | EV-030 to EV-035 | Managed database; payment HSM service; compliance shared drive; data warehouse console; fraud team files | 2023-01-01 to 2026-07-06 |
| Merchant support | EV-036, EV-037 | Ticketing SaaS; support procedures | 2026-06-30 to 2026-07-06 |
| Governance and program documents | EV-038 to EV-046 | Company intranet; compliance shared drive; HR information system; document request list; learning management system | 2023-01-01 to 2026-07-08 |
| Suppliers, contracts and registrations | EV-047 to EV-058 | Accounting system; compliance shared drive; provider portals; contracts folder; QSA report; corporate records | 2025-12-01 to 2026-07-06 |
| Facilities and disposal | EV-059, EV-060 | Company intranet; IT help desk tickets | 2026-06-30 to 2026-07-06 |
| Business volume | EV-061 to EV-063 | Accounting system; platform reporting; settlement and funding reports | 2025-12-31 to 2026-06-30 |
| Email, AI tools and backups | EV-064 to EV-066 | Productivity suite admin console; staff survey and identity provider app list; managed database backup settings | 2026-07-01 to 2026-07-07 |

## 3. Observations by area
**Users and access.** 60 active named workforce accounts, each with MFA registered. The 9 cloud and CDE administrators use phishing-resistant hardware keys and the other 51 users use push approval (EV-001). Single sign-on with MFA is required for the cloud console, the bastion, the pipeline and the SaaS applications; push approval without number matching is allowed for non-administrators (EV-002). HR lists 60 employees, all at the Florida office, an April 2026 reorganization, and 11 separations in the 12 months to June 2026, including the security engineer in April 2026 (EV-003). Contractor accounts have no end-date field, and contractor departures do not appear in IT tickets (EV-004). Each of the 11 termination tickets disabled single sign-on on the last working day; the ticket template and the HR checklist have no step for repository tokens, API keys or SaaS local accounts (EV-005, EV-006). 10 of 10 sampled personnel files show a background check before hire (EV-007). Cloud IAM policies deny by default; the last recorded workforce access review is dated 2025-10, and there is no review record for service or application accounts (EV-008). The merchant portal has 11,500 user accounts, and 14% have MFA enabled (EV-009). Portal sign-in is by password, with an 8-character minimum, no expiry and no risk-based analysis; a funding bank account change asks only for the password (EV-010). Card numbers are masked to first six and last four digits, and internal support roles can view full transaction details for all merchants (EV-011).

**Devices, network and cloud configuration.** EDR, full-disk encryption and a host firewall run on all 72 laptops (EV-012). Laptops share one office network segment and sync company file shares (EV-013). The bastion requires single sign-on and a hardware key, records sessions, and is the only administrative path configured into the CDE subnets (EV-014). TLS 1.2 is the minimum on public endpoints and the terminal gateway, and SSL and early TLS were disabled in 2023. The certificate inventory (v2025) does not list the cloud load balancers or the card network links (EV-015). A web application firewall in blocking mode sits in front of the API gateway, portal and hosted payment page (EV-016), and the content delivery service provides DDoS protection (EV-017). Runtime protection covers container hosts; no network intrusion detection is configured inside the CDE or on egress, and DNS queries are not logged (EV-018). The PCI DSS scope document and data-flow diagrams date from 2025 and show the former hosting; the last scope confirmation is dated 2025-10 (EV-019). The cloud asset inventory shows the platform in 3 zones of one region, with snapshot copies only in the second region; the cut-over to the cloud tenant is dated 2026-03-14 (EV-020). Pull requests need one approval to deploy, including to the CDE, and static analysis runs on each one. Dependency scanning covers only the API gateway repository, builds are not signed, and personal access tokens can be created with no expiry (EV-023). Quarterly internal and ASV scans ran from Q3 2025 to Q2 2026, and the Q2 2026 ASV scan passed after a rescan (EV-024). The last penetration and segmentation tests ran in January 2026 on the former hosting (EV-025).

**Logging and monitoring.** The SIEM collects CDE, bastion, identity provider and cloud control-plane logs and keeps them 12 months, with 3 months immediately available (EV-026). Alerts go to a shared mailbox and a chat channel and are opened in business hours; 17 alerts raised on June weekends were first opened the following Monday (EV-028). Two new cloud subnets sent no logs for 9 days in May 2026, and no alert rule exists for a silent log source, a stopped EDR agent or a disabled WAF rule (EV-029).

**Data protection, keys and AI model.** PAN in the token vault is encrypted with AES-256 under keys held in the payment HSM service (EV-030). The last key ceremony, on 2026-03-10, used two custodians (EV-031). The key management procedures and cryptographic architecture date from 2023 and describe the former hosting provider's HSMs (EV-032). The retention schedule sets no period for merchant onboarding files or support tickets (EV-033). The data warehouse extract job is designed to carry tokens only, and warehouse access is limited to 11 people (EV-034). The fraud model's quarterly training extract lists cardholder name and full billing address alongside tokens and features, and no decline-rate, segment or fairness reports were provided (EV-035).

**Merchant support.** Ticketing and the shared support inbox have no masking or card-number detection, the support procedures have no step for card numbers received, and the Merchant Support Manager states that merchants paste card numbers into tickets and email (EV-036). Eight merchant requests for PCI DSS responsibility information in 2026 were answered with an AOC copy or a free-text reply that differs by agent (EV-037).

**Governance and program documents.** The policies date from 2023, were last reviewed in June 2025, and predate the April 2026 reorganization; the acceptable use policy has no generative AI content (EV-038). Two standards still name the departed security engineer as owner (EV-039). The incident response plan dates from 2023, describes the former hosting, and has no card brand, sponsor bank, FTC or state notice steps and no procedure for card numbers found outside the CDE (EV-040). The last tabletop exercise was in 2024 (EV-041). The contact list has no sponsor bank designated points of contact (EV-042). Quarterly reviews of security procedures stop after 2026-Q1 (EV-043). The security engineer role has been vacant since April 2026, and there is no written Qualified Individual designation (EV-044). The document request returned no written executive assignment of PCI DSS responsibility, no written report to the owner, no targeted risk analyses, no scope confirmation after March 2026, no script or software component inventory, no recovery runbook, failover test or restore test records, no responsibility matrices, and no AI tools inventory (EV-045). 58 of 60 staff completed the 2026 awareness course, which has a phishing module and no generative AI content (EV-046).

**Suppliers, contracts and registrations.** Payments in the 12 months to June 2026 went to the providers listed in the vendor register (EV-047). The service provider list names 6 providers; current AOCs are on file for 4, none for the content delivery service or the fraud analytics vendor, and no responsibility matrix is on file (EV-048). The cloud provider's SOC 2 Type 2 report covers the 12 months ending 2026-03-31, its AOC is dated 2026-02-15, and a bridge letter runs to 2026-06-30 (EV-049). The fraud model license has no use limits or deletion terms for the training extract (EV-051). The sponsor agreement makes the settlement and funding services examinable under 12 U.S.C. 1867(c) and requires notice of a suspected account data compromise within 24 hours (EV-052). A letter of intent with an FDIC-supervised state nonmember bank has no services under it yet (EV-054). The 2025 AOC is marked Compliant, dated 2025-12-01 (EV-056). A cyber insurance policy with an incident response panel is in force (EV-057). The company holds no New York license and no SEC registration (EV-058).

**Facilities and disposal.** The office has badge access and holds no CDE hardware (EV-059). Laptops are wiped before reuse (EV-060).

**Business volume.** FY2025 receipts were $28.2 million, about $77,000 a day (EV-061). The platform processed about 95 million transactions (about $6.8 billion) in the 12 months to June 2026 for about 4,200 merchants in 41 states (EV-062). Funding files are reconciled to settlement before transmission (EV-063).

**Email, AI tools and backups.** Email filtering checks sender authentication and rewrites links (EV-064). Staff report pasting transaction details into public generative AI chatbots, and no enterprise AI tool appears in the identity provider app list (EV-065). The managed database keeps point-in-time recovery and copies daily snapshots to a second region; no restore job is recorded since the 2026-03-14 cut-over (EV-066).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they paste | IT Manager (staff survey follow-up) | 2026-07-08 | Not established at intake; P10 treats it as unknown |
| Current AOCs from the content delivery service and the fraud analytics vendor | Compliance and Risk Manager | 2026-07-06 | Not provided; carried into the P01 risk register (R-016) |
| Sponsor bank designated points of contact for 12 CFR 53.4 notices | Compliance and Risk Manager | 2026-07-06 | Not recorded; carried into the P01 risk register (R-015) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003), receipts and volume (EV-061, EV-062), contract commitments (EV-052, EV-055), backup settings (EV-066), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-034 |
| P04 Cloud mapping | Cloud and SaaS components (EV-020, EV-047) and provider assurance (EV-048, EV-049) |
| P01 Risk register | Likelihood inputs from the configuration exports, the alert and log records (EV-028, EV-029), the document request (EV-045) and the interviews |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with PCI DSS, the Safeguards Rule and 12 CFR 53.4 |
| P06 Policies | The 2023 policies and standards (EV-038, EV-039) and the 2023 incident response plan (EV-040) |
| P07 Control assessment | Populations to sample from (EV-001, EV-005, EV-009, EV-020) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register and EV-042 |
| P09 SOC 2 | Provider assurance on file (EV-048, EV-049) and the sponsor bank's request context (EV-052) |
| P10 AI governance | AI uses found (EV-035, EV-065) |
