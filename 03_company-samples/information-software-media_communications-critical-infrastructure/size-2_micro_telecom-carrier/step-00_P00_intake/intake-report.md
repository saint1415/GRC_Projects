# Intake Report: Cris Santos Company | Communications | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural fiber broadband and voice carrier, one Florida town) |
| Intake window | 2026-07-06 to 2026-07-17 |
| Collected by | Office Manager (security and compliance lead), with the Network Operations Lead and the MSP lead technician |
| Approved | Owner and General Manager, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-20. It covers the organization, the systems that hold or reach CPNI and customer PII, the network that carries subscriber traffic, the suppliers that touch them, and the rules that may bind the company. For a 7-person carrier the systems of record are the vendor admin consoles (BSS, voice platform, productivity suite), the network devices and the EMS in the hut, the MSP's reports, the payroll service, the contracts folders and the FCC filing records. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, the walkthrough, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-009 | Payroll service; BSS, voice platform and productivity suite admin consoles; OLT and EMS logins | 2026-06-30 to 2026-07-08 |
| Network and hut | EV-010 to EV-016 | Edge router; Network Operations Lead's version records and server notes; EMS; monitoring service | 2026-07-08 to 2026-07-10 |
| Office IT | EV-017 to EV-022 | MSP device, encryption and antivirus consoles; MSP monthly report; firewall management; backup console; MSP tickets | 2026-06-30 to 2026-07-08 |
| Customers and CPNI | EV-023 to EV-027 | BSS reporting; shared drive scripts; AI assistant settings and terms; mailbox; website | 2026-06-30 to 2026-07-10 |
| Documents, filings and records | EV-028 to EV-033 | Document request; HR files; FCC filing confirmations; CALEA SSI filing; consultant change emails | 2026-02-24 to 2026-07-13 |
| Suppliers and contracts | EV-034 to EV-039 | Contracts folders; BSS vendor portal; accounting system; insurance policy | 2026-03-31 to 2026-07-10 |
| Facilities, outages and company records | EV-040 to EV-045 | Hut key list and generator service record; NORS account and trouble tickets; accounting system; company files and FCC license search; designation letter; mailbox | 2025-12-31 to 2026-07-15 |
| AI tools | EV-025, EV-046 | AI assistant settings and terms; staff meeting | 2026-07-07 to 2026-07-14 |

## 3. Observations by area
**Users and access.** Payroll lists 7 employees and 1 termination in 2026, a Field Technician whose last day was in March 2026 (EV-001). The BSS has named staff accounts for all 7 employees with MFA required; both Customer Service Representatives hold the supervisor role, which can export the full customer list (EV-002). One BSS API key, used by the provisioning link from the hut, holds the full administrator role (EV-003). Customers reset portal passwords with the account number and last name, the portal locks after 5 failures, and the only customer notice turned on is the default email for a portal password change (EV-004). BSS audit logging is on; the account-view and export reports show no runs in 2025 or 2026 (EV-005). The voice platform portal has 4 named logins and 1 shared "support" login, all administrators, with MFA available and not enabled and CDR export open to every login; CDRs are kept 18 months (EV-006). The provider keeps portal sign-in and export logs 90 days (EV-007). The productivity suite enforces MFA for all accounts, and exported customer reports sit in the general shared-drive folder (EV-008). The 2 OLTs and the EMS have one local administrator login, used by the Network Operations Lead, both Field Technicians and the consultant (EV-009).

**Network and hut.** The edge router filters inbound traffic to the management addresses, lets the EMS web page be reached from the internet, and runs the remote-administration VPN with one shared consultant login and a password only. Management, server and subscriber networks share one routed segment (EV-010). Router firmware is 2 years older than the vendor's current release, with open advisories from 2024 and 2025, and OLT firmware is one major release behind (EV-011). OLT administration uses Telnet, SNMP runs version 2c with community strings last changed in 2018, and device logs stay in local buffers of about 14 days (EV-012). The EMS lists the 2 OLTs and about 1,420 ONTs (EV-013) and saves OLT and router configurations nightly to the hut server, with no other storage location and no restore entries (EV-014). The 2 hut servers have no malware protection and unencrypted disks, and are updated during the consultant's visits (EV-015). The monitoring service checks availability and pages the on-call technician; it has no rules for sign-ins, configuration changes or exports. Middle-mile peak use is about 40% and OLT ports about 60% (EV-016).

**Office IT.** The MSP manages 4 desktops, 3 laptops and 3 tablets. Staff have no local administrator rights; laptops lock after 10 minutes; the front counter desktop is excluded from the screen lock; tablets use a 4-digit passcode (EV-017). The 3 laptops are encrypted and the 4 desktops are not; antivirus runs on the 7 office computers, with alerts in business hours (EV-018). The MSP patches office computers monthly and updates the office firewall quarterly; its listed services do not include vulnerability scanning or the hut (EV-019). The office firewall exposes no services and guest Wi-Fi is separate (EV-020). The cloud backup copies the productivity suite nightly with 30 days of versions; network configurations are not in it (EV-021). MSP tickets record a wipe for each reused office computer (EV-022).

**Customers and CPNI.** The BSS holds about 1,420 accounts at Florida addresses, about 440 telephone numbers on about 390 voice accounts, and driver license numbers on about 1,050 accounts. The phone account PIN is set on about 30% of voice accounts, and the account screen has no field for CPNI approval status (EV-023). The call script verifies callers by name and service address; the sign-up script offers the PIN as optional (EV-024). The AI assistant was turned on 2026-05-04 with vendor defaults: guest verification by account number and service address, personalized offers, and email address changes in chat. Its terms allow the vendor to use de-identified chat data to improve its models (EV-025). Marketing emails offer voice plans to voice customers and do not ask for CPNI approval (EV-026).

**Documents, filings and records.** The document request returned no written CPNI procedures, incident response plan, CPNI breach procedure, outage or DIRS procedure, contingency plan, inventory of network devices, SaaS services or CPNI locations, or vendor review records (EV-028). The handbook's discipline section does not mention CPNI (EV-029). Training records hold vendor OLT certificates and no security or CPNI training (EV-030). CPNI certifications were filed by March 1 each year, the latest on 2026-02-24; the statement is the consultant's template and says call detail is released only after a password (EV-031). The 2017 CALEA SSI filing names a technician who is not on the current payroll roster as the 24x7 contact and has not been amended (EV-032). Network changes are announced by email with no written approval or record (EV-033).

**Suppliers and contracts.** The TTP contract has CALEA confidentiality terms; the voice platform contract states 99.99% availability and has no CPNI or incident notice terms (EV-034). The middle-mile contract covers one circuit with a 4-hour repair target; the MSP contract has a 4-business-hour response and no recovery commitment; the consultant works under a best-effort retainer letter; only the TTP contract has CPNI or incident notice terms; there are no federal contracts (EV-035). The BSS vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31, with an RTO of 8 hours and an RPO of 1 hour (EV-036). The 6 dedicated circuit contracts carry a 99.9% monthly commitment (EV-037). Accounts payable lists the suppliers in the vendor register and no AI tool subscription (EV-038). A cyber liability policy with a 24x7 breach hotline and panel vendors is in force (EV-039).

**Facilities, outages and company records.** Hut keys are held by the General Manager, the Network Operations Lead and the 2 Field Technicians; the generator has about 72 hours of fuel at full load (EV-040). The NORS login was created in 2018 and has no filings; a 2025 middle-mile cut lasted 2 hours 40 minutes; the outage contact list has no entry for the county 911 center; there is no DIRS account (EV-041). FY2025 revenue was about $1.1 million, about $92,000 is billed a month, and the cash reserve covers about 45 days (EV-042). The company is a privately held Florida LLC with no wireless, broadcast or cable landing license (EV-043). The Office Manager was designated security and compliance lead on 2026-07-15 (EV-044). The community bank branch's questionnaire is due 2026-09-30 (EV-045).

**AI tools.** The AI assistant is a BSS add-on offered free for six months, with no payment line (EV-025, EV-038). The monitoring service includes a learned alert threshold feature (EV-016). Staff say they sometimes use public generative AI chatbots to draft emails, scripts or troubleshooting notes. No approved-tools list was found (EV-046).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they paste | Office Manager | 2026-07-14 | Not established at intake; P10 treats it as unknown |
| Whether the learned alert thresholds use any customer data | Monitoring service vendor, through the Network Operations Lead | 2026-07-10 | Not answered at intake; carried in P10 (AI-002, vendor confirmation due 2026-10-31) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001), revenue and billing (EV-042), customer and circuit counts (EV-023, EV-037), vendor terms (EV-034 to EV-036), backup schedule (EV-014), capacity and power (EV-016, EV-040), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-002 to EV-021 |
| P04 Cloud mapping | SaaS components (EV-002 to EV-008, EV-021, EV-025, EV-038) and provider assurance (EV-036) |
| P01 Risk register | Likelihood inputs from the configuration exports, the version records (EV-011), the outage records (EV-041) and the filings (EV-031, EV-032) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The scripts (EV-024), the handbook (EV-029) and the document request response (EV-028) |
| P07 Control assessment | Populations to test against (EV-001, EV-002, EV-006, EV-009, EV-017) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the insurance policy (EV-039) |
| P09 SOC 2 | The bank questionnaire (EV-045) and vendor assurance on file (EV-036) |
| P10 AI governance | AI tools found (EV-016, EV-025, EV-038, EV-046) |
