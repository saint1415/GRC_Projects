# Intake Report: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (diversified precision-agriculture crop farm, about 640 acres in two Florida blocks) |
| Intake window | 2026-06-29 to 2026-07-10 (off-season; no H-2A workers on site) |
| Collected by | Operations and Technology Manager (security lead), with the Irrigation Technician and the Office and HR Manager |
| Approved | Majority owner and General Manager, 2026-08-31 |

## 1. Purpose and scope
Intake collected the farm's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that run the farm or hold personal and regulated records (Produce Safety records, H-2A earnings records, worker and customer personal information, operator location history), the OT in the pump house and fields, the suppliers that touch them, and the rules that may bind the farm. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets the CSF 2.0 benchmark or a binding record rule is decided in P03 (the regulatory analysis) and P07 (the control assessment).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-005 | Identity provider; payroll provider and personnel library; SYS-01 admin console; account request emails | 2026-06-30 to 2026-07-01 |
| Irrigation and OT | EV-006, EV-011 to EV-016 | SYS-01 irrigation settings; remote access tool console; integrator agreement, handover pack and email; walk-throughs of both blocks | 2024-03-01 to 2026-07-09 |
| Devices and network | EV-007 to EV-010 | MSP endpoint console; mobile management; antivirus console; MSP firewall and switch management | 2026-06-30 to 2026-07-01 |
| Documents and records | EV-017 to EV-021 | Owner's files; business plan; training records; HR files | 2024-01-01 to 2026-07-06 |
| Cloud, backups and logs | EV-022 to EV-024 | Cloud provider console; backup service; identity provider, SYS-01 and cloud logging settings | 2026-06-30 to 2026-07-02 |
| Suppliers and contracts | EV-025 to EV-033 | Accounting SaaS; contracts folder; vendor portals and terms; insurance policy | 2024-03-01 to 2026-07-06 |
| Program, sales and food safety records | EV-034 to EV-040, EV-046 | Processor portal; food safety audit report; program documents; receipts report; payroll and tally; Office library; SYS-01 reports; e-commerce console | 2025-12-31 to 2026-07-06 |
| Incidents, payments, facilities and AI tools | EV-041 to EV-045 | MSP tickets; bank portal; alarm service; key list; staff survey and identity provider app list | 2026-06-30 to 2026-07-07 |

## 3. Observations by area
**Users and access.** The identity provider has 11 active named accounts, each with MFA registered. One belongs to a person on the 2025-26 season departure list, and 2 cloud administrators have standing access (EV-001). MFA is required for email, files, the cloud console and the SYS-01 web console. Number matching applies to administrators only, and no sign-in alert rules are set (EV-002). HR lists 15 employees, 4 of them H-2A seasonal workers, and 4 departures in the 2025-26 season (EV-003). SYS-01 has named manager, operator and crew accounts, plus 2 generic crew lead logins used on the harvest tablets. Three active SYS-01 accounts belong to people on the departure list, 11 disabled accounts from earlier seasons are retained, the mobile app signs in with a password only, and no record export has ever been run (EV-004). Accounts are created from manager emails; 6 such emails cover the 2025-26 season (EV-005).

**Irrigation and OT.** SYS-01 can alert on irrigation schedule and setpoint changes, but those alerts are switched off. The freeze temperature alert reaches the Irrigation Technician through SYS-01 and the pivot cellular links (EV-006). The integrator's remote access tool on the HMI allows unattended access at all times through one shared account without MFA, and the farm holds no administrator account in it (EV-011). The 2024 integrator agreement has no security, remote access, change or incident terms (EV-012). The commissioning pack records the HMI build and PLC firmware as installed in 2024 and one HMI operator account, with no later update records (EV-013). The integrator states that the PLC program and HMI project files are on its field engineer's laptop only (EV-014). Every well pump, fertigation pump and pivot panel has a Hand-Off-Auto switch. The shop holds one spare VFD and no spare PLC CPU. About 145 OT and IoT devices were counted, and the pivot and well panels in the fields are unlocked (EV-015, EV-016).

**Devices and network.** The MSP console lists 8 laptops and 3 desktops, patched monthly with built-in antivirus. Disk encryption is reported on the 8 laptops and not on the 3 desktops. The data hub VM is enrolled, the HMI is not, and no endpoint detection and response agent is installed (EV-007). The 11 tablets and phones are in basic mobile management with no encryption or PIN requirement (EV-008). Antivirus alerts go to a shared mailbox with no named recipient, and it holds unread alerts (EV-009). The office, the packing shed access point and the pump house share one internal network with no internal firewall rules. No inbound services are published; the only remote path is the HMI tool's outbound connection. Headquarters has one fiber circuit (EV-010).

**Documents and records.** The request for a risk assessment, written security policies, a written security lead designation, an incident response plan, a contingency or manual irrigation procedure, an OT or personal data inventory, access or log review records and a retention schedule returned none (EV-017). The 2026 business plan has no cybersecurity section (EV-018). Training records show food safety training at hire in English and Spanish, and no security training in either language (EV-019). The HR checklist has no step to create or remove system access (EV-020). The handbook has a code of conduct and no information security section (EV-021).

**Cloud, backups and logs.** The cloud tenant holds the data hub VM, imagery storage and the backup vault in one account and one region. The imagery bucket is private, and the data hub accepts collector traffic only from the farm's public IP address, on a listener without TLS (EV-022). Daily backups completed from April to June 2026. Immutability is off, the same 2 administrators can delete recovery points, and no restore was run (EV-023). Log retention is 30 days (identity provider), 90 days (cloud) and 1 year (SYS-01), with no export, review schedule or alerts (EV-024).

**Suppliers and contracts.** Payments went to 18 technology and service suppliers, including the agronomy analytics vendor from October 2025 (EV-025). The MSP contract covers about 10 hours a month and lists no vulnerability scanning or security monitoring (EV-026). The distributor agreement requires notice within 24 hours of events that could affect product safety, traceability or volumes, and the acquirer requires an annual self-assessment questionnaire (EV-027). No farm breach contact is named in the payroll or e-commerce accounts (EV-028). The yield pilot runs on click-through terms that let the vendor use farm imagery and yields to improve its models (EV-029). Dealer technicians have standing access to the telematics account, which keeps operator location history with no limit (EV-030). The FMIS vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 and states an RTO of 8 hours and an RPO of 1 hour; the 2025 report on file has no review notes (EV-031). The cloud provider's SOC 2 report is on file (EV-032). The 2025 cyber policy has a breach hotline and panel counsel and forensics (EV-033).

**Program, sales and food safety records.** The February 2026 self-assessment questionnaire records point-to-point encrypted terminals and a hosted payment page (EV-034). The March 2026 third-party food safety (Good Agricultural Practices) audit was passed and does not cover cybersecurity (EV-035). Program files hold FSA, crop insurance, NRCS, water permit and H-2A documents, with no FDA food facility registration and no federal procurement contracts (EV-036). 2025 receipts were $1.5 million, most of it across about 200 in-season days, with produce sales well above $25,000 in each of the last 3 years (EV-037). Piece-rate pay comes from SYS-01 tally entered under the 2 crew lead logins (EV-038). The Office library holds personnel and H-2A files and is shared with all office and management accounts (EV-039). The Food Safety and Packing Lead signed the required records weekly from January to June 2026 (EV-040). The online store has about 2,400 customer accounts with no retention setting (EV-046).

**Incidents, payments, facilities and AI tools.** The farm keeps no incident log. The MSP closed 9 security-related tickets in 12 months, with no incident numbers (EV-041). The bank requires the majority owner's approval for a new payee (EV-042). The office and pump house alarm is armed after hours. Cooler alerts go by text to one on-call phone over the headquarters internet circuit (EV-043). Keys are issued from a key list (EV-044). The yield pilot and the SYS-01 irrigation recommendations are in use, and office staff report using public chatbots. No approved AI tools list was found (EV-045).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of office staff using public chatbots, and what they paste | Majority owner and General Manager | 2026-07-08 | Not established at intake; P10 treats it as unknown |
| Remote access tool session history for 2026 | Irrigation integrator | 2026-07-03 | Not provided at intake; examined during the control assessment (EV-MA-4) |
| Security questionnaire or assurance report from the MSP and the integrator | MSP technician; irrigation integrator | 2026-07-06 | Not provided; questionnaires due by 2027-03-31 (P02 SR-6) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003), receipts and season length (EV-037), backup schedule (EV-023), PLC program copies (EV-014), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-016 and EV-022 to EV-024 |
| P04 Cloud mapping | Cloud and SaaS components (EV-022, EV-025) and provider assurance (EV-031, EV-032) |
| P01 Risk register | Likelihood inputs from the ticket history (EV-041), configuration exports, the walk-throughs and the supplier terms |
| P03 Regulatory analysis | The obligations register (which rules apply) and every observation above, compared with CSF 2.0 and the record rules |
| P06 Policies | The handbook (EV-021) and the document request result (EV-017) |
| P07 Control assessment | Populations to sample from (EV-001, EV-003, EV-004, EV-005, EV-007) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the insurance policy (EV-033) |
| P09 SOC 2 | Vendor assurance on file (EV-031, EV-032) |
| P10 AI governance | AI tools found (EV-025, EV-029, EV-045) |
