# Scenario facts: Cris Santos Company | Emergency Services | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (a licensed private ambulance service) |
| Business | Private ambulance (EMS) provider (NAICS 621910 Ambulance Services): basic life support (BLS) and advanced life support (ALS) ground ambulance transport |
| Location | Florida. **Headquarters** (administration, billing, the 24x7 dispatch center, and the fleet garage) and **Station 2** (crew quarters and 3 ambulances, about 12 miles away). Service area: one county with about 400,000 residents, plus interfacility trips to neighboring counties |
| Workforce | 60 employees: 40 field clinicians (26 EMTs, 14 paramedics), 9 dispatchers (emergency medical dispatch certified), 5 billing and compliance staff, 6 management and administration |
| Volume | About 16,000 transports a year (about 44 a day). About 70% are scheduled or unscheduled interfacility and non-emergency transports for hospitals and nursing facilities; about 30% are 911 emergency responses in one county zone |
| Fleet | 9 ambulances (6 BLS, 3 ALS); 5 to 7 staffed at peak |
| Revenue | $13.5 million a year (fictional). Under the SBA standard of $22.5 million for NAICS 621910 (13 CFR 121.201), so SBA-small |
| Payers | Medicare Part B (ambulance supplier), Florida Medicaid, commercial plans, and facility contracts. Medicaid is federal financial assistance, so Section 1557 of the Affordable Care Act applies (45 CFR Part 92) |
| Licenses and county authority | State EMS license for BLS and ALS transport (Fla. Stat. 401.25; Chapter 64J-1, F.A.C.). Certificate of public convenience and necessity from the home county (Fla. Stat. 401.25(2)(d)). A county ambulance service agreement covers 911 response in one zone. A contracted Medical Director (physician), as Fla. Stat. 401.265(1) requires |
| HIPAA status | **Covered entity.** A health care provider that transmits claims electronically in HIPAA standard transactions (45 CFR 160.103). With 60 employees it is not a "small supplier" (fewer than 10 FTEs) under 42 CFR 424.32(d)(1), so Medicare requires it to submit claims electronically |
| County 911 relationship | The county 911 public safety answering point (PSAP), run by the county sheriff's office, answers 911 calls. It sends EMS incidents to the company's CAD over a CAD-to-CAD interface (incident type, address, callback number, and brief notes) and transfers callers to the company's dispatchers. The company has **no access** to state or national criminal justice databases or to law enforcement records systems |
| Not in scope | FBI CJIS Security Policy: the company does not access criminal justice information (see P03). 42 CFR Part 2: not a federally assisted substance use disorder program. Group health plan requirements (45 CFR 164.314(b)): the company does not administer a group health plan. FCC EAS rules: not an EAS participant. Payment cards: patients pay through the billing vendor's hosted payment page, outside company systems |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: EMS records (Fla. Stat. 401.30; Rule 64J-1.014, F.A.C.), call recording (Fla. Stat. 934.03), and breach notification (Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Chief Operating Officer (COO) | Executive owner of the program; accepts risk up to Moderate; signs policies |
| Majority owner | Accepts High and Very High risks; approves the security budget |
| IT Manager | HIPAA **Security Officer** (45 CFR 164.308(a)(2)); runs IT with a contracted managed service provider |
| Billing and Compliance Manager | HIPAA **Privacy Officer**; breach determinations; owns the revenue cycle and the clearinghouse relationship |
| Medical Director (contracted physician) | Clinical oversight of dispatch protocols, patient care protocols, and the AI call triage pilot |
| Communications Center Supervisor | Runs the dispatch center; owns manual (paper and radio) dispatch procedures |
| Operations Manager | Field crews, fleet, Station 2, vehicle equipment |
| Clinical Services Coordinator (paramedic) | ePCR quality review, clinical training, state data reporting |
| HR Manager | Onboarding, terminations, certification tracking, workforce clearance |
| Managed service provider (MSP) | Help desk, patching, cloud tenant administration, after-hours monitoring of backups. A business associate |

## 3. Systems

| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Computer-aided dispatch (CAD): call entry, unit recommendation, unit status, AVL map, CAD-to-CAD interface to the county | Vendor-licensed software run in the company's cloud tenant (SYS-06) | Yes | Mission-critical. Uses local CAD accounts, not the identity provider (see gaps) |
| SYS-02 | Electronic patient care reporting (ePCR) with hospital record delivery and state data export | Vendor SaaS | Yes | System of record for patient care. Business associate with a SOC 2 Type 2 report. Tablets work offline and sync |
| SYS-03 | Billing and revenue cycle platform with clearinghouse | Vendor SaaS | Yes | Business associate. Electronic 837 claims to Medicare, Medicaid, and commercial payers |
| SYS-04 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects SYS-02, SYS-03, SYS-05, and the cloud console. CAD is not federated |
| SYS-05 | Productivity suite (email, files, chat) and cloud fax | SaaS | Yes | Physician certification statements (PCS) and facility face sheets arrive in a shared mailbox |
| SYS-06 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts the CAD application server (virtual machine), the CAD managed database, the integration engine (CAD-to-CAD, CAD-to-ePCR, ePCR-to-billing), the dispatch call recording archive (object storage), and the backup vault |
| SYS-07 | Dispatch center at headquarters | On-premises | Yes (in use) | 5 dispatch consoles and 1 supervisor position; county P25 radio control stations; UPS and standby generator |
| SYS-08 | Hosted phone system with call recording | Vendor SaaS | Yes | Request lines, facility lines, and transferred 911 callers. Recordings copied nightly to SYS-06. **No business associate agreement on file** (see gaps) |
| SYS-09 | Fleet mobile systems | In vehicles | Yes | Per ambulance: a cellular router with GPS for AVL, a mobile data computer (MDC) running the CAD mobile client, 1 to 2 rugged ePCR tablets, and a cardiac monitor that sends 12-lead ECGs to hospitals through the monitor vendor's cloud relay (business associate) |
| SYS-10 | Networks (headquarters and Station 2) | On-premises | Yes (in transit) | Firewalls, switches, Wi-Fi; two ISPs at headquarters; site-to-site VPN to SYS-06 |
| SYS-11 | Endpoints | On-premises and in vehicles | Yes (cached) | 28 office and dispatch workstations and laptops, 22 rugged ePCR tablets, 9 MDCs |
| SYS-12 | AI call triage module | CAD vendor's cloud AI service (SaaS) | Yes | Transcribes calls and suggests a call type and response priority in CAD. **Shadow-mode pilot since 2026-06-15** (see P10) |

External systems the company connects to but does not operate: the county CAD and the county P25 radio system (county-operated), hospital systems that receive ePCR records, and the state EMS data system (EMSTARS).

**SSP system (P02):** the *Dispatch and Patient Care Platform (DPCP)*: SYS-01, SYS-02, SYS-04, SYS-06, SYS-07, SYS-09, SYS-10, SYS-11, and their interfaces to SYS-03, SYS-08, SYS-12, and the county CAD.

## 4. Current security posture: partially compliant

**In place today:**
- MFA through the identity provider for email, the ePCR, the billing platform, and the cloud console
- Unique user IDs in the ePCR and the billing platform
- BAAs with the ePCR vendor, the billing and clearinghouse vendor, the CAD vendor (remote support), the MSP, and the cardiac monitor relay vendor
- Full-disk encryption and remote wipe on ePCR tablets and laptops through device management
- Automatic OS patching on office endpoints
- Antivirus (signature-based)
- Badge access at headquarters, with a separate badge-controlled door on the dispatch room
- UPS and standby generator for the dispatch center; two ISPs at headquarters; county P25 radios in every ambulance and at dispatch
- Background checks, driving record checks, and state EMT and paramedic certification checks at hire
- New-hire HIPAA training
- Daily backups of cloud workloads, stored in the same account and region; point-in-time restore enabled on the CAD database (7 days)
- The ePCR and billing vendors' own backups

**Missing or weak, found in the 2026 assessments:**
1. No documented security risk analysis has ever been completed (Required, 164.308(a)(1)(ii)(A)). A 2023 payer compliance questionnaire is the only prior review.
2. Security policies are a 3-page IT policy from 2020. No HIPAA security policies, sanctions policy, or procedures have been adopted.
3. CAD uses shared position logins at the dispatch consoles and a per-vehicle automatic login on the MDCs. CAD is not federated with the identity provider and has no MFA.
4. No review of audit logs, CAD activity, ePCR access reports, or identity provider sign-ins.
5. No written incident response plan. Incidents are handled ad hoc.
6. No written contingency plan. A manual (paper and radio) dispatch binder exists but has not been drilled since 2023, and there is no alternate dispatch site.
7. Cloud backups (CAD database snapshots, integration engine, call recordings) sit in the same account and region as production, are not immutable, and have never been restore-tested.
8. Dispatch console workstations are excluded from automatic patching because of CAD client compatibility and were last patched 7 months ago. Signature antivirus only (no endpoint detection and response).
9. CAD and ePCR accounts are managed outside the identity provider. Accounts of departing field staff stay active for up to 3 weeks.
10. No vulnerability scanning.
11. Training happens only at hire. There are no periodic security reminders or phishing exercises.
12. Flat network at headquarters: dispatch consoles, office PCs, and the crew lounge Wi-Fi share one segment.
13. No BAA with the hosted phone and call recording vendor. The CAD vendor's AI triage module was enabled under an order form whose data-use terms have not been reviewed.
14. PCS forms and facility paperwork sit in a shared mailbox with no retention schedule. Nothing implements Medicare's 7-year documentation rule (42 CFR 424.516(f)) or the state's 5-year EMS records rule (Rule 64J-1.014, F.A.C.).
15. Three of 9 vehicle cellular routers expose remote web administration to the internet with the manufacturer default password (found during P07 testing).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 incident | Ransomware encrypts the CAD application server and the dispatch consoles, forcing manual dispatch (the registry scenario: computer-aided dispatch outage from ransomware) |
| P09 SOC 2 | The company is not a SOC 2 service organization. (a) Security-only (CC1-CC9) self-benchmark, used to answer the county's contract-renewal security questionnaire; (b) review of the ePCR vendor's SOC 2 Type 2 report |
| P10 AI | AI-assisted emergency call triage (CAD vendor module), shadow-mode pilot |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-31 | Security risk analysis and gap analysis fieldwork |
| 2026-08-10 to 2026-08-14 | Control assessment fieldwork (router finding on 2026-08-12) |
| 2026-08-21 | SOC 2 self-benchmark and ePCR vendor report review completed |
| 2026-08-24 | AI call triage assessment completed |
| 2026-09-04 | Deliverables approved by the COO (the majority owner approved High-risk treatments the same day) |
