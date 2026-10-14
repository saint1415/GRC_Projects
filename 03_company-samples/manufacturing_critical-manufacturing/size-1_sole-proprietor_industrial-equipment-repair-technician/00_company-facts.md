# Scenario facts: Cris Santos Company | Critical Manufacturing | Sole Proprietorship

All 11 deliverables in this folder use the facts below. The company, its customers, and their plants are fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, standard, or contract term, the citation is given. Regulatory text was re-checked on 2026-10-05 (eCFR version 2026-09-23 for 13 CFR 121.201; the CIRCIA NPRM text, 89 FR 23644; the CIP-013-2 and CIP-013-3 PDFs published by NERC; the NIST SP 800-82 Rev. 3 PDF).

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-technician files Schedule C) |
| Business | Owner-operated industrial equipment repair and maintenance service (NAICS 811310, Commercial and Industrial Machinery and Equipment (except Automotive and Electronic) Repair and Maintenance). Troubleshoots, repairs, and maintains the electrical controls of production machinery at manufacturing plants: PLC-controlled coil winding machines, vacuum drying ovens, oil processing and filling rigs, CNC core cutting lines, and the variable frequency drives and motors that run them. Also commissions and repairs transformer cooling and monitoring control cabinets at utility substations as a subcontractor to one transformer manufacturer |
| Why this business at this size | Size substitution: a sole proprietor does not manufacture power transformers. The vertical's link is the customer base. About 80% of receipts come from plants that build grid equipment (distribution transformers, power transformers, switchgear), and the owner holds the control programs that keep their production lines running |
| Location | Florida. Home-based: a home office with a locked file cabinet, and a service van that carries tools, test instruments, and spare parts. All repair work is done on site at customer plants or substations |
| Equipment | One rugged service laptop; one phone; test instruments (insulation resistance tester, power quality analyzer, thermal camera, multimeters); a field connection kit (programming cables, adapters, USB sticks, a small switch); a wireless vibration sensor kit (AI-001 trial) |
| Workforce | The owner-technician only (0 employees). Uses contracted services instead of staff |
| Revenue | About $180,000 a year in receipts (fictional), about $800 per working day. SBA-small (standard for NAICS 811310: $12.5 million in average annual receipts; 13 CFR 121.201). Receipts and customer mix: EV-026, EV-027 |
| Customers | About 10 active business customers and no consumers. **Customer A**, a Florida distribution transformer manufacturer: about 35% of receipts from plant service plus about 10% from substation field work it subcontracts, 45% in all. **Customer B**, a small power transformer manufacturer: about 20%. **Customer C**, a switchgear and panelboard manufacturer: about 15%. **About seven local plants** (packaging, plastics, metal fabrication, a food processor): about 20% (EV-027) |
| Customer A contract | Service agreement renewed 2025-09-30 for two years, with a **Contractor Cyber Security Exhibit** (cited as "Customer A exhibit S1" to "S8"): S1 use Customer A information only for the services and disclose none to a third party, including cloud and AI services other than the contractor's own email and file storage, without written consent; S2 remote access only through Customer A's remote access gateway (named account, MFA, per-session approval), and no contractor-installed remote access devices; S3 scan the service laptop and removable media at the plant's media scanning station before connecting to plant equipment; S4 notify Customer A within 24 hours of discovering a cyber incident that affects or could affect Customer A's systems or information, or a device used on Customer A equipment, and coordinate the response; S5 verify the hash value Customer A provides before loading any firmware or software onto Customer A or utility equipment; S6 at utility sites, follow the utility's access rules, use only utility-controlled remote access, and tell Customer A within 1 business day when anyone working for the contractor should no longer have utility site access; S7 return or securely delete Customer A information at the end of the agreement or on request; S8 carry cyber liability insurance of at least $1 million from the 2027-09-30 renewal. These deadlines are contract terms, not regulations (EV-014) |
| Utility flow-down | Customer A told the owner in writing (2025-09-30) that its substation work falls under the Supplier Cyber Security Addenda in its utility contracts, which follow NERC CIP-013-2 Requirement R1 Part 1.2, and that exhibit S4, S5, and S6 flow down those addendum topics (R1.2.1 and 1.2.2 incident notice and coordination; R1.2.5 software integrity; R1.2.6 vendor remote access; R1.2.3 access no longer needed). Inside substations the owner works escorted by utility staff and has no unescorted physical or electronic access to utility systems (EV-015) |
| Other customer terms | Customers B and C: mutual NDAs (protect confidential information with reasonable care, use it only for the services, and give prompt written notice of any unauthorized disclosure). The seven local plants: no written security terms (EV-016) |
| NERC status | **Not a NERC-registered entity.** CIP-013-2 applies to the Responsible Entities in its section 4.1 (for example Transmission Owners and Generator Owners), not to their vendors. It reaches the owner only through Customer A's exhibit. Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (CIP-013-2, CUST-A-EXHIBIT) |
| Federal work | None. No federal contracts or subcontracts, no FAR or DFARS clauses in any PO, no federal contract information (FCI) and no CUI. Customer A confirmed in writing (2025-09-30) that the service work involves none (EV-015, EV-028; obligations register) |
| Exports | None. No service work outside the United States and no shipments abroad (EV-028; obligations register C-CRITICAL-MFG-R03) |
| Sensitive data | Customer machine programs: PLC logic, HMI projects, drive parameter files, CNC cutting programs, and coil winding recipes (customer trade secrets; winding recipes reflect transformer designs); customer electrical schematics, network address lists, and machine passwords; substation cabinet drawings and monitoring unit configuration and firmware files from Customer A field work; vibration data; business records (quotes, invoices, customer remittance details, the owner's tax records). Personal information is minimal: business contact names, work emails, and phone numbers of customer staff, and the owner's own records |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): NERC CIP as a direct obligation (not registered). FAR 52.204-21, 52.204-23, 52.204-25, DFARS 252.204-7012, and CMMC (no federal or DoD work; C-CRITICAL-MFG-R04). ICTS connected vehicles rule (no vehicle products; C-CRITICAL-MFG-R02). EAR licensing (no exports; C-CRITICAL-MFG-R03). CIRCIA (proposed only, and as proposed it would not reach this business; C-CRITICAL-MFG-R01; see P03). SEC rules (not a registrant). HIPAA (no such data). Payment card standards (customers pay by bank transfer or check) |
| Regulatory driver IDs | The vertical IDs C-CRITICAL-MFG-R01 to R04 are decided in the intake obligations register and recorded once each in P03 as applicability rows (none binds today). The benchmark, NIST CSF 2.0 with SP 800-82 Rev. 3, is voluntary, so rows driven only by it read "None binding; CSF 2.0 benchmark (P03 G-###)". Binding duties are contract terms, cited as "Customer A exhibit S#" (with "CIP-013-2 R1.2.x flow-down" where it applies) and "Customer B and C NDAs" |
| State law approach | Florida law is cited only where unavoidable (the Fla. Stat. 501.171 applicability check in P08) |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-technician | Every role: owner, estimator, field technician, programmer, security lead, contract compliance, incident lead, and risk acceptor |
| On-call IT consultant (independent contractor) | Hourly help with the laptop, the virtual machine, and the home router. Uses a remote-support tool in sessions the owner starts and watches. Signed the owner's NDA on 2026-08-20, before the self-assessment (EV-031) |
| Outside bookkeeper (CPA firm) | Monthly bookkeeping and tax returns. Own named login to the accounting SaaS with the accountant role and MFA through the firm's account (EV-005, EV-032) |
| Customer A plant controls engineer | Approves each remote session through Customer A's gateway; runs the plant's media scanning station; Customer A's contact for exhibit S4 notices |
| Customer B maintenance supervisor | Asked for the cellular remote access router in 2024 (EV-013); calls the owner for breakdowns on nights and weekends |
| OEM technical support lines | PLC, drive, and oven control makers' support desks. Sometimes ask the owner to email program files for diagnosis |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds customer programs or confidential data? | Notes |
|---|---|---|---|---|
| SYS-01 | Business productivity suite (email, calendar, cloud file storage) | SaaS, business plan | Yes | Holds the synced **Customer Machine Library**, customer drawings and manuals, quotes, and a spreadsheet of customer machine passwords. MFA on with an authenticator app on the phone. Deleted files and prior versions kept 30 days (EV-001 to EV-004) |
| SYS-02 | Accounting and invoicing SaaS | SaaS | Business records | Quotes, invoices, payments, bank feed, customer remittance details. Owner (administrator) and bookkeeper accounts. **No MFA on the owner's account** (EV-005) |
| SYS-03 | Service laptop | Owner device | Yes | One laptop for everything: email, web, quotes, and connecting to customer machines. Engineering software from 5 automation makers. The Customer Machine Library: about 70 machines at 10 customer sites, about 2,400 files, synced to SYS-01. Built-in full-disk encryption on; built-in antivirus; automatic OS updates. **The owner uses one administrator account for everything.** One legacy engineering package for older winding machine controllers runs in a virtual machine with an operating system that no longer gets updates (EV-003, EV-006, EV-007) |
| SYS-04 | Mobile phone | Personal device used for business | Yes (photos, email) | Email, calls and texts with customer maintenance staff, photos of nameplates, wiring, and HMI screens, the MFA authenticator app, and the hotspot used on site. Passcode, encryption, and remote wipe on (EV-008) |
| SYS-05 | Field connection kit | Owner equipment | Yes (programs on USB sticks) | 8 USB sticks (not encrypted), programming cables and adapters, a small unmanaged switch. Older machines at Customer B and two local plants load programs only from a USB stick (EV-009, EV-034) |
| SYS-06 | Cellular remote access router at Customer B | Owner device on Customer B's vacuum drying oven control panel; managed through the router maker's cloud portal | Reaches the oven PLC and HMI | Bought and installed by the owner in 2024-11 at the maintenance supervisor's request, for night and weekend support. **Always on; the cloud portal account is the owner's, with a password only; no approval by Customer B for each session; never approved in writing by Customer B's plant management** (EV-012, EV-013) |
| SYS-07 | Customer A remote access gateway account | Customer A owned and operated | Reaches Customer A machines | Named account, MFA, per-session approval by the plant controls engineer, sessions recorded by Customer A. Outside the boundary (EV-017) |
| SYS-08 | Vibration analytics SaaS with AI fault diagnosis | Vendor SaaS, trial since 2026-05-04 | Yes (vibration data, machine and plant names) | Wireless sensors on customer motors, a phone app, and a web dashboard that predicts bearing and alignment faults. See P10 (EV-029, EV-030) |
| SYS-09 | Home office network | Internet provider's router with Wi-Fi | In transit | **Shared with household devices** (family laptops, smart TV, game console). No separate network for the business laptop (EV-011) |

**SSP system (P02):** the *Field Service Business Systems (FSBS)*: SYS-01 to SYS-06, SYS-08, and SYS-09 (the core SaaS stack for email, files, client and billing records, plus the service laptop, phone, field connection kit, the remote access router at Customer B, the vibration analytics trial, and the home network); Customer A's gateway (SYS-07) and the customers' plant and substation systems are outside the boundary.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. For a one-person repair business the sources are the SaaS admin consoles and portals, the accounting reports, bank and card statements, the inbox, the signed agreements folder, the job tickets, the laptop, phone and field kit themselves, and the insurance agent's portal.
- **Which rules and contract terms apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the CSF 2.0 benchmark and the customer contract terms** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 SSP | Field Service Business Systems (FSBS), short form |
| P03 regulation | Primary: NIST CSF 2.0 with NIST SP 800-82 Rev. 3 as the OT guide (voluntary benchmark; no binding sector cyber rule). Binding by contract: Customer A's Contractor Cyber Security Exhibit (S1 to S8, including the CIP-013-2 R1.2 flow-down terms for substation work) and the Customer B and C NDAs. Applicability rows for CIP-013-2, the four vertical requirements, and the FAR clauses |
| P04 cloud | SaaS tenants only (productivity suite, accounting SaaS, router cloud portal, vibration analytics SaaS), plus the customer-side controls on the laptop, phone, and home network. No IaaS |
| P05 BIA | 5 business functions (BP-01 to BP-05) |
| P07 assessment | 10 controls tied to the High risks and the Customer A exhibit; self-assessment with the IT consultant |
| P08 incident | Ransomware on the service laptop that encrypts the local and synced Customer Machine Library during a breakdown call, so a Customer A coil winding line (distribution transformer production) stays down until its program can be reloaded, with a risk that the infection reaches plant equipment through the laptop or a USB stick. Adapted from the registry default "Ransomware disrupting production of grid equipment": a sole proprietor has no production of its own, so the disruption is to the customer's grid equipment line |
| P09 SOC 2 | Security criteria only. The owner's self-check, used to answer customer supplier security questionnaires, plus a review of the productivity suite provider's SOC 2 report. A SOC 2 report for this business is not sought |
| P10 AI | AI-001, the vibration analytics SaaS with AI fault diagnosis (SYS-08). Adapted from the registry default "Demand forecasting and predictive maintenance": a one-person service business has no demand to forecast with a model; predictive maintenance is the AI use it actually has. AI-002 (a consumer generative AI assistant) is inventoried as restricted |
| Primary system | The registry default "Core business SaaS stack (email, files, client and billing records)" is kept, with the service laptop, phone, and field kit added to the boundary because they hold and move the Customer Machine Library |
| Cloud | SaaS only. Vendor-agnostic; no IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2025-09-30 | Customer A agreement renewed with the Contractor Cyber Security Exhibit |
| 2026-05-04 | AI-001 vibration analytics trial starts |
| 2026-08-17 to 2026-08-21 | Intake: the owner collects SaaS console and portal exports, statements, contracts, job tickets, device and field kit reviews, and the home office and van walk-through; inventories; obligations register |
| 2026-08-20 | IT consultant signs the owner's NDA |
| 2026-08-24 to 2026-08-28 | Self-assessment with the IT consultant: BIA, risk assessment, gap analysis, and control assessment (tests on 2026-08-26 at the home office and 2026-08-27 at Customer B, with its maintenance supervisor present) |
| 2026-08-31 to 2026-09-10 | POL-01 drafted from the gaps and the test results |
| 2026-09-02 | AI use assessment |
| 2026-09-11 | Deliverables and POL-01 adopted by the owner-technician |
| 2027-03 (planned) | Follow-up check: operating effectiveness of the controls POL-01 introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables (Phase 5)
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Sharing links | Three "anyone with the link" sharing links to customer program folders, made for OEM support desks in 2025 and 2026, were still active. Found in the P04 mapping on 2026-08-25 from the sharing report collected at intake (EV-002) and removed that day; default sharing set to named people only. Program files had also been emailed to OEM support desks without recording customer consent (EV-020) | P03, P04, P09 |
| Router at Customer B | The router's local admin page accepted the factory default password (P07 test on 2026-08-27, with Customer B's maintenance supervisor present; changed that day; EV-AC-17). On 2026-09-03 Customer B agreed that the router stays powered off except for sessions it approves by phone, until its plant management decides between a Customer B owned gateway and removal (EV-038) | P01, P02, P04, P07 |
| Test restore | Restoring one machine folder (40 files) from version history on 2026-08-26 worked only one file at a time; a full-library restore would take days (EV-CP-9) | P02, P04, P07, P09 |
| Virtual machine | In the 2026-08-26 test the legacy engineering virtual machine reached the home network and the internet through its bridged adapter (EV-SC-7) | P07 |
| Antivirus test | The built-in antivirus detected and quarantined a standard test file within seconds (2026-08-26; EV-SI-3) | P07 |
| Phone photos | Equipment photos taken on the phone sync to the owner's personal photo cloud (EV-008) | P02, P04 |
| USB sticks | All 8 sticks are the owner's; the owner does not use sticks handed over by plant staff (EV-MP-7) | P07 |
| Equipment list | An equipment list exists for insurance (laptop, phone, instruments), but it leaves out the USB sticks, the router, and the old laptop (EV-024) | P02, P03 |
| Suite provider assurance | The productivity suite provider's SOC 2 Type 2 report (Security, Availability, Confidentiality; period ending 2026-06-30; unqualified; one remediated exception), received at intake (EV-033), was reviewed on 2026-08-26 | P02, P09 |
| Exhibit lapses | Customer A has not raised the S1, S3, or S5 lapses. The owner will tell Customer A about the 4 unverified firmware loads by 2026-09-30 | P03, P07 |
| AI-001 trial | Sensors on 6 motors at Customer A (winding line and drying oven vacuum pumps) and 4 motors at one local plant. 3 alerts in the trial: 2 confirmed by handheld readings, 1 false positive. The vendor's paid business plan offers a data addendum that bars training on customer data and deletes data within 30 days of a request. Customer A uploads were stopped (sensors paused) on 2026-09-02 (EV-029, EV-037) | P04, P10 |
| AI-002 | The owner uses a consumer generative AI assistant on the phone to draft emails and quotes and to look up published fault code meanings; no customer files pasted (self-review, EV-037) | P10 |
| Cost estimates | Encrypted backup drives about $250; 10 encrypted USB sticks about $150; password manager about $40 a year; business Wi-Fi on the existing router at no cost | P01, P07 |
