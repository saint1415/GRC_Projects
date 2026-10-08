# Intake Report: Cris Santos Company | Health Care and Social Assistance | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-specialty medical group: 140 clinics, 6 ASCs, 12 imaging centers, 1 central lab; FL, GA, AL, SC) |
| Intake window | 2026-05-04 to 2026-05-29 |
| Collected by | GRC team (second line), with system owners in each business unit, the Integration Management Office and Internal Audit's prior workpapers |
| Approved | CISO and Chief Compliance Officer, 2026-05-29. Obligations register reviewed by the General Counsel's office, with outside securities counsel (EV-060) |

## 1. Purpose and scope
Intake collected the group's own records before the enterprise risk analysis, the BIA and the gap analysis began on 2026-06-01, and before Internal Audit's control assessment fieldwork began on 2026-07-13. It covers the organization (159 sites and the eight acquired practices AQ-01 to AQ-08), the systems that create, receive, maintain or transmit ePHI or support tier-1 processes, the vendors that touch them, and the rules that may bind the group and its two external service lines (SL-1 and SL-2). Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (BIA interviews, risk workshops, gap analysis samples, Internal Audit tests) to the same register, so one list backs every deliverable.

At this size the sources are enterprise systems of record across business units: the identity platform and HR system, the CMDB and clinical engineering asset system, the cloud consoles and SIEM, the third-party risk register and accounts payable vendor master, the contract repository, board and committee records, prior Internal Audit and SOX workpapers, and regulator correspondence.

Each register row names the owning business unit's system of record and owner. The [asset inventory](asset-inventory.csv) reconciles the CMDB with the cloud account inventory, the EDR and endpoint consoles and the clinical engineering system; the [vendor register](vendor-register.csv) reconciles the third-party risk register with the accounts payable vendor master and the contract repository.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Identity and access | EV-001 to EV-008 | Identity platform (SSO, PAM, identity governance); HR system; AQ legacy directories; LIS and outreach portal consoles | 2026-04-30 to 2026-05-06 |
| Endpoints, devices and network | EV-009 to EV-015 | EDR and endpoint consoles; CMDB and clinical engineering system; network management; firewall exports; scanner | 2026-04-24 to 2026-05-04 |
| Cloud, logging, backup and recovery | EV-016 to EV-023 | Cloud consoles and posture management; backup accounts; key management; SIEM; SOC case management; DR records; EHR and AQ EHR contracts | 2026-04-18 to 2026-05-16 |
| Governance, prior assurance and disclosure | EV-024 to EV-031 | GRC platform; ERM register; board portal; Internal Audit and SOX workpapers; General Counsel's office; SEC filing | 2025-07-31 to 2026-05-01 |
| Workforce and privacy records | EV-032, EV-033 | Learning system; Privacy Office tracker | 2026-04-30 |
| Third parties, contracts and service lines | EV-034 to EV-040 | Third-party risk register; AP vendor master; contract repository; revenue cycle reporting; vendor portals; service auditor report | 2025-12-31 to 2026-05-01 |
| Facilities, disposal and ASC preparedness | EV-041 to EV-044 | Physical access system; facilities library; IT asset disposition; ASC document library | 2026-04-30 |
| Business volume and structure | EV-045 to EV-048 | ERP financial reporting; operational reporting; legal entity register; Integration Management Office tracker | 2025-12-31 to 2026-05-01 |
| AI | EV-049 to EV-051 | AI council register; SaaS and feature discovery; AI scribe console | 2026-04-30 to 2026-05-12 |
| Laboratory and integration | EV-052 to EV-055, EV-074 | Change system and LIS audit trail; LIS console; lab document control; integration platform | 2026-02-20 to 2026-05-04 |
| Obligations and regulatory status | EV-057 to EV-062, EV-066 | Compliance office; contract repository; regulatory files; counsel memo; benefits files; records office | 2026-01-01 to 2026-05-15 |
| Other operating records | EV-056, EV-063 to EV-065, EV-067 to EV-073 | Data catalog and DLP; insurance files; patient-app records; telecom inventory; ERM; GRC platform; PACS; productivity suite; ERP; threat intelligence | 2025-11-30 to 2026-05-01 |

## 3. Observations by area
**Identity and access.** About 11,390 workforce accounts are federated through SSO with MFA registered. The about 610 workforce members at AQ-06 to AQ-08 sign in through 3 legacy directories that are not federated and are run by local IT firms, with disable dates entered by hand (EV-001, EV-006). MFA is required for every SSO application, FIDO2 keys for privileged roles, and lockout follows 10 failed attempts (EV-002). Privileged access is just in time through PAM with session recording; there are 22 privileged LIS and database accounts (EV-003). Joiner, mover and leaver events flow from the HR system, and 4 quarterly certification campaigns closed in the last 12 months (EV-004). HR holds about 12,000 employees, with AQ-06 to AQ-08 terminations sent to local IT by email (EV-005). The LIS has about 520 workforce accounts, 14 with the build administrator role (EV-007). The outreach portal has about 3,100 client accounts created by client administrators, outside identity governance (EV-008).

**Endpoints, devices and network.** EDR reports on 96% of about 20,000 endpoints; about 420 endpoints at AQ-07 and AQ-08 have no agent (EV-009). About 310 AQ workstations report no disk encryption (EV-010). The device inventory holds about 7,650 of an estimated 9,000 networked medical devices (about 85%), about 1,100 on unsupported operating systems, including 14 analyzer workstations and 2 middleware servers (EV-011). NAC is enforced at 95 of 159 sites (60%); 14 AQ sites run on legacy site VPNs; 41 sites have a single carrier (EV-012). Each AQ-06 to AQ-08 site network is one flat segment, and the AQ VPN rules let the whole site subnet reach the interface engine subnet. MLLP inside the lab segment runs without TLS (EV-013). Scans run weekly (EV-014). Of 9 instrument platforms, 4 take vendor remote support through the vendor's own always-on tool rather than the PAM gateway (EV-015).

**Cloud, logging, backup and recovery.** Both clouds use account vending, guardrails as code and daily posture scans (EV-016). Backups sit in separate accounts with write-once retention and a weekly copy to DC-2; LIS logs ship every 15 minutes (EV-017). Keys are customer-managed with deletion protection (EV-018). The SIEM does not list the AQ-07 and AQ-08 EHRs or the AQ legacy directories as log sources, and no use case covers result changes after verification (EV-019). The SOC runs 24x7 with MSSP overflow; several AQ cases were opened only after local IT had handled the event (EV-020). The LIS disaster recovery test on 2026-05-16 met its RPO and recovered in 5.5 hours against a 4-hour RTO (EV-021). The EHR vendor's contract states RTO 4 hours and RPO 15 minutes, and its failover test was observed on 2026-04-18 (EV-022). The AQ-07 and AQ-08 EHRs back up nightly to local storage, have no restore test record, and their contracts state a 24-hour RTO (EV-023).

**Governance, prior assurance and disclosure.** The 2025 policy set (POL-01 to POL-05, approved 2025-09) sits in the policy portal with standards, procedures and an exception register (EV-024). The 2025 risk analysis rolled into 8 enterprise risks, and the board approved the risk appetite in 2026-02 (EV-025, EV-026). Internal Audit's 2025 assessment and the FY2025 SOX ITGC testing are on file with their workpapers (EV-027). The Security Officer and Privacy Officer are designated in writing (EV-028). The disclosure committee has 7 members, 3 of whom joined after the 2025 acquisitions, and its minutes record no exercise of the materiality playbook since then (EV-029). The FY2025 10-K includes Item 1C (EV-030). The 2026-03-19 tabletop included an LIS outage (EV-031).

**Workforce and privacy records.** Annual training, role-based modules, monthly phishing simulations and monthly reminders are recorded (EV-032). The Privacy Office keeps sanction cases, four-factor breach assessments, notification dates and privacy monitoring reports; the 2025 small-breach log went to HHS on 2026-02-26 (EV-033).

**Third parties, contracts and service lines.** The vendor register lists about 900 vendors, 320 with PHI, all tiered; 23 contracts inherited through acquisitions have no review record, and the courier and specimen tracking vendor has no SOC report on file (EV-034, EV-035). BAA templates require notice within 10 days (EV-036). The primary clearinghouse carries 70% of claims (about $64.6 million a week); the secondary contract has no surge capacity clause; there is no record of a payer-portal fallback test (EV-037). SOC reports are on file for the EHR vendor, both clouds, both colocation providers, the primary clearinghouse, the ERP vendor and the productivity suite (EV-038). SL-1 issued its 2025 SOC 2 Type 2 report with one exception (EV-039). SL-1 serves about 45 practices under BAAs, and SL-2 about 260 practices, with no SOC 2 report yet (EV-040).

**Facilities, disposal and ASC preparedness.** Badge access, quarterly lab badge reviews and visitor logs are in place (EV-041). Facility security plans cover 145 enterprise sites; none is on file for the 14 AQ-06 to AQ-08 sites (EV-042). Certificates of destruction are on file (EV-043). The 6 ASCs run one program with a facility risk assessment each; the 2026 hazard analysis lists cyberattack and IT outage, and neither the 2025 nor the 2026 exercise used a cyber or IT outage scenario (EV-044).

**Business volume and structure.** Revenue was about $4.8 billion in FY2025, about $13.2 million per calendar day (EV-045). The group sees about 36,000 clinic visits per business day and produces about 26,000 lab results per day (EV-046). It runs 159 sites in 4 states (EV-047). AQ-01 to AQ-05 are integrated; AQ-06 to AQ-08 (about 610 workforce, 14 sites) are not, and the AQ-07 and AQ-08 EHR migrations are due 2026-11-30 and 2027-04-30 (EV-048).

**AI.** The AI council register lists 12 use cases, 9 with completed review (EV-049). Feature discovery found 2 more outside the register: EHR draft replies (AI-006) and resume ranking (AI-012), for 14 in total (EV-050). Bias testing records for the clinical decision support tools cite vendor-supplied data (EV-049). About 650 providers use the AI scribe, and consent documentation completion varies by state (EV-051).

**Laboratory and integration.** LIS test build and autoverification rule changes are approved by laboratory supervisors, while other changes go through the enterprise change advisory board (EV-052). Autoverified results are recorded under a process account (EV-053). The LIS contingency plan v4 sets RTO 4 hours and RPO 15 minutes (EV-054). The AQ-07 and AQ-08 interfaces run on legacy agreements (EV-055). LIS SSP version 1.1 and its criticality analysis are on file (EV-074).

**Obligations.** The group sends its own standard transactions through clearinghouses (EV-058), holds a CLIA certificate and Medicare certification for its 6 ASCs (EV-059), runs no substance use disorder program but holds Part 2 records received with consent (EV-057), and is an SEC registrant (EV-030). The employee health plan is a separate covered entity (EV-061). Counsel's view on each candidate rule is in EV-060; the results are in [`obligations-register.csv`](obligations-register.csv).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| SOC report for the LIS vendor's remote support service | Director of Third-Party Risk Management (from the LIS vendor) | 2026-05-12 | Not received at intake; carried to P07 SA-9 and POAM-015 |
| SOC report or security questionnaire from the courier and specimen tracking vendor | Director of Third-Party Risk Management | 2026-05-12 | Vendor states it has no SOC report; carried to the P01 register (R-037) |
| Inventory of the remaining networked medical devices, including point-of-care device types | Director of Clinical Engineering | 2026-05-06 | About 15% not established at intake; P07 traced devices (CM-8) and POAM-010 tracks discovery |
| BAA status of the 23 contracts inherited through acquisitions | General Counsel's office and Integration Management Office | 2026-05-08 | Review not complete at intake; carried to P03 (G-029) and POAM-022 |
| AI features embedded in vendor products beyond the discovery review | CIO | 2026-05-14 | Not established at intake; P10 treats further embedded features as unknown |
| Incident records kept by the AQ-06 to AQ-08 local IT firms | Vice President, Integration Management Office | 2026-05-08 | Partial; P07 sampled the 6 AQ incidents in SOC case management (IR-4) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-005, EV-047), revenue and volumes (EV-045, EV-046), recovery records (EV-017, EV-021, EV-022, EV-023), dependencies from the asset and vendor registers, and claims routing (EV-037) |
| P02 SSP | The LIS boundary from the asset inventory; prior SSP v1.1 (EV-074); as-found configuration from EV-001 to EV-019, EV-052 to EV-055 |
| P04 Cloud mapping | Cloud components and guardrails (EV-016 to EV-019) and provider assurance (EV-038) |
| P01 Risk register | Likelihood inputs from threat intelligence (EV-073), SOC case history (EV-020), coverage and configuration exports, the prior risk analysis (EV-025) and the risk appetite (EV-026) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The 2025 policy set and exception register (EV-024) |
| P07 Control assessment | Populations to sample from (EV-004, EV-005, EV-007, EV-008, EV-011, EV-014, EV-017, EV-020, EV-052) and prior Internal Audit workpapers (EV-027) |
| P08 IR runbook | Notification duties from the obligations register; disclosure committee records (EV-029); contacts from the vendor register |
| P09 SOC 2 | Vendor assurance on file (EV-038), the SL-1 2025 report (EV-039) and service line agreements (EV-040) |
| P10 AI governance | AI tools found (EV-049, EV-050, EV-051) |
