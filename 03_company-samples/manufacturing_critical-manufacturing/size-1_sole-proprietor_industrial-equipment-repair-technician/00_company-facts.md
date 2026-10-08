# Scenario facts: Cris Santos Company | Critical Manufacturing | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company, its customers, and their plants are fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, standard, or contract term, the citation is given. Regulatory text was re-checked on 2026-10-05 (eCFR version 2026-09-23 for 13 CFR 121.201; the CIRCIA NPRM text, 89 FR 23644; the CIP-013-2 and CIP-013-3 PDFs published by NERC; the NIST SP 800-82 Rev. 3 PDF).

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-technician files Schedule C) |
| Business | Owner-operated industrial equipment repair and maintenance service (NAICS 811310, Commercial and Industrial Machinery and Equipment (except Automotive and Electronic) Repair and Maintenance). Troubleshoots, repairs, and maintains the electrical controls of production machinery at manufacturing plants: PLC-controlled coil winding machines, vacuum drying ovens, oil processing and filling rigs, CNC core cutting lines, and the variable frequency drives and motors that run them. Also commissions and repairs transformer cooling and monitoring control cabinets at utility substations as a subcontractor to one transformer manufacturer |
| Why this business at this size | Size substitution: a sole proprietor does not manufacture power transformers. The vertical's link is the customer base. About 80% of receipts come from plants that build grid equipment (distribution transformers, power transformers, switchgear), and the owner holds the control programs that keep their production lines running |
| Location | Florida. Home-based: a home office with a locked file cabinet, and a service van that carries tools, test instruments, and spare parts. All repair work is done on site at customer plants or substations |
| Equipment | One rugged service laptop; one phone; test instruments (insulation resistance tester, power quality analyzer, thermal camera, multimeters); a field connection kit (programming cables, adapters, USB sticks, a small switch); a wireless vibration sensor kit (AI-001 trial) |
| Workforce | The owner-technician only (0 employees). Uses contracted services instead of staff |
| Revenue | About $180,000 a year in receipts (fictional), about $800 per working day. SBA-small (standard for NAICS 811310: $12.5 million in average annual receipts; 13 CFR 121.201) |
| Customers | About 10 active business customers and no consumers. **Customer A**, a Florida distribution transformer manufacturer: about 35% of receipts from plant service plus about 10% from substation field work it subcontracts, 45% in all. **Customer B**, a small power transformer manufacturer: about 20%. **Customer C**, a switchgear and panelboard manufacturer: about 15%. **About seven local plants** (packaging, plastics, metal fabrication, a food processor): about 20% |
| Customer A contract | Service agreement renewed 2025-09-30 for two years, with a **Contractor Cyber Security Exhibit** (cited as "Customer A exhibit S1" to "S8"): S1 use Customer A information only for the services and disclose none to a third party, including cloud and AI services other than the contractor's own email and file storage, without written consent; S2 remote access only through Customer A's remote access gateway (named account, MFA, per-session approval), and no contractor-installed remote access devices; S3 scan the service laptop and removable media at the plant's media scanning station before connecting to plant equipment; S4 notify Customer A within 24 hours of discovering a cyber incident that affects or could affect Customer A's systems or information, or a device used on Customer A equipment, and coordinate the response; S5 verify the hash value Customer A provides before loading any firmware or software onto Customer A or utility equipment; S6 at utility sites, follow the utility's access rules, use only utility-controlled remote access, and tell Customer A within 1 business day when anyone working for the contractor should no longer have utility site access; S7 return or securely delete Customer A information at the end of the agreement or on request; S8 carry cyber liability insurance of at least $1 million from the 2027-09-30 renewal. These deadlines are contract terms, not regulations |
| Utility flow-down | Customer A told the owner in writing (2025-09-30) that its substation work falls under the Supplier Cyber Security Addenda in its utility contracts, which follow NERC CIP-013-2 Requirement R1 Part 1.2, and that exhibit S4, S5, and S6 flow down those addendum topics (R1.2.1 and 1.2.2 incident notice and coordination; R1.2.5 software integrity; R1.2.6 vendor remote access; R1.2.3 access no longer needed). Inside substations the owner works escorted by utility staff and has no unescorted physical or electronic access to utility systems |
| Other customer terms | Customers B and C: mutual NDAs (protect confidential information with reasonable care, use it only for the services, and give prompt written notice of any unauthorized disclosure). The seven local plants: no written security terms |
| NERC status | **Not a NERC-registered entity.** CIP-013-2 applies to the Responsible Entities in its section 4.1 (for example Transmission Owners and Generator Owners), not to their vendors. It reaches the owner only through Customer A's exhibit |
| Federal work | None. No federal contracts or subcontracts, no FAR or DFARS clauses in any PO, no federal contract information (FCI) and no CUI. Customer A confirmed in writing (2025-09-30) that the service work involves none |
| Exports | None. No service work outside the United States and no shipments abroad |
| Sensitive data | Customer machine programs: PLC logic, HMI projects, drive parameter files, CNC cutting programs, and coil winding recipes (customer trade secrets; winding recipes reflect transformer designs); customer electrical schematics, network address lists, and machine passwords; substation cabinet drawings and monitoring unit configuration and firmware files from Customer A field work; vibration data; business records (quotes, invoices, customer remittance details, the owner's tax records). Personal information is minimal: business contact names, work emails, and phone numbers of customer staff, and the owner's own records |
| Not in scope | NERC CIP as a direct obligation (not registered). FAR 52.204-21, 52.204-23, 52.204-25, DFARS 252.204-7012, and CMMC (no federal or DoD work; C-CRITICAL-MFG-R04). ICTS connected vehicles rule (no vehicle products; C-CRITICAL-MFG-R02). EAR licensing (no exports; C-CRITICAL-MFG-R03). CIRCIA (proposed only, and as proposed it would not reach this business; C-CRITICAL-MFG-R01; see P03). SEC rules (not a registrant). HIPAA (no such data). Payment card standards (customers pay by bank transfer or check) |
| Regulatory driver IDs | The vertical IDs C-CRITICAL-MFG-R01 to R04 are recorded once each in P03 as applicability rows (none binds today). The benchmark, NIST CSF 2.0 with SP 800-82 Rev. 3, is voluntary, so rows driven only by it read "None binding; CSF 2.0 benchmark (P03 G-###)". Binding duties are contract terms, cited as "Customer A exhibit S#" (with "CIP-013-2 R1.2.x flow-down" where it applies) and "Customer B and C NDAs" |
| State law approach | Florida law is cited only where unavoidable (the Fla. Stat. 501.171 applicability check in P08) |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-technician | Every role: owner, estimator, field technician, programmer, security lead, contract compliance, incident lead, and risk acceptor |
| On-call IT consultant (independent contractor) | Hourly help with the laptop, the virtual machine, and the home router. Uses a remote-support tool in sessions the owner starts and watches. Signed the owner's NDA on 2026-08-20, before the self-assessment |
| Outside bookkeeper (CPA firm) | Monthly bookkeeping and tax returns. Own named login to the accounting SaaS with the accountant role and MFA through the firm's account |
| Customer A plant controls engineer | Approves each remote session through Customer A's gateway; runs the plant's media scanning station; Customer A's contact for exhibit S4 notices |
| Customer B maintenance supervisor | Asked for the cellular remote access router in 2024; calls the owner for breakdowns on nights and weekends |
| OEM technical support lines | PLC, drive, and oven control makers' support desks. Sometimes ask the owner to email program files for diagnosis |

## 3. Systems
| ID | System | Hosting | Holds customer programs or confidential data? | Notes |
|---|---|---|---|---|
| SYS-01 | Business productivity suite (email, calendar, cloud file storage) | SaaS, business plan | Yes | Holds the synced **Customer Machine Library**, customer drawings and manuals, quotes, and a spreadsheet of customer machine passwords. MFA on with an authenticator app on the phone. Deleted files and prior versions kept 30 days |
| SYS-02 | Accounting and invoicing SaaS | SaaS | Business records | Quotes, invoices, payments, bank feed, customer remittance details. Owner (administrator) and bookkeeper accounts. **No MFA on the owner's account** |
| SYS-03 | Service laptop | Owner device | Yes | One laptop for everything: email, web, quotes, and connecting to customer machines. Engineering software from 5 automation makers. The Customer Machine Library: about 70 machines at 10 customer sites, about 2,400 files, synced to SYS-01. Built-in full-disk encryption on; built-in antivirus; automatic OS updates. **The owner uses one administrator account for everything.** One legacy engineering package for older winding machine controllers runs in a virtual machine with an operating system that no longer gets updates |
| SYS-04 | Mobile phone | Personal device used for business | Yes (photos, email) | Email, calls and texts with customer maintenance staff, photos of nameplates, wiring, and HMI screens, the MFA authenticator app, and the hotspot used on site. Passcode, encryption, and remote wipe on |
| SYS-05 | Field connection kit | Owner equipment | Yes (programs on USB sticks) | 8 USB sticks (not encrypted), programming cables and adapters, a small unmanaged switch. Older machines at Customer B and two local plants load programs only from a USB stick |
| SYS-06 | Cellular remote access router at Customer B | Owner device on Customer B's vacuum drying oven control panel; managed through the router maker's cloud portal | Reaches the oven PLC and HMI | Bought and installed by the owner in 2024-11 at the maintenance supervisor's request, for night and weekend support. **Always on; the cloud portal account is the owner's, with a password only; no approval by Customer B for each session; never approved in writing by Customer B's plant management** |
| SYS-07 | Customer A remote access gateway account | Customer A owned and operated | Reaches Customer A machines | Named account, MFA, per-session approval by the plant controls engineer, sessions recorded by Customer A. Outside the boundary |
| SYS-08 | Vibration analytics SaaS with AI fault diagnosis | Vendor SaaS, trial since 2026-05-04 | Yes (vibration data, machine and plant names) | Wireless sensors on customer motors, a phone app, and a web dashboard that predicts bearing and alignment faults. See P10 |
| SYS-09 | Home office network | Internet provider's router with Wi-Fi | In transit | **Shared with household devices** (family laptops, smart TV, game console). No separate network for the business laptop |

**SSP system (P02):** the *Field Service Business Systems (FSBS)*: SYS-01 to SYS-06, SYS-08, and SYS-09 (the core SaaS stack for email, files, client and billing records, plus the service laptop, phone, field connection kit, the remote access router at Customer B, the vibration analytics trial, and the home network); Customer A's gateway (SYS-07) and the customers' plant and substation systems are outside the boundary.

## 4. Current security posture: informal (basic hygiene, big gaps)
**In place today:**
- Business email and file plan (not a personal account), with MFA by authenticator app
- Built-in full-disk encryption on the laptop; passcode, encryption, and remote wipe on the phone
- Automatic OS updates and built-in antivirus on the laptop
- File version history (30 days) on the cloud file storage
- NDAs with Customers A, B, and C; Customer A's security exhibit signed 2025-09-30
- Remote work for Customer A goes only through Customer A's gateway (MFA, per-session approval)
- Programs are saved to the library at the end of every visit, with the date in the file name
- Van locked and alarmed; the laptop is not left in the van overnight
- The bookkeeper uses a separate named login with MFA

**Missing:**
1. No written security policy, risk assessment, incident plan, or list of contract obligations. Customer A's exhibit was signed but never turned into steps.
2. One laptop does everything. Email and web browsing run on the same administrator account that connects to customer PLC networks.
3. The Customer Machine Library has no backup independent of sync. Ransomware would sync encrypted files to the cloud. A restore has never been tried, and there is no hash or record showing which program version is current.
4. The cellular remote access router at Customer B is always on, reached through a password-only cloud portal account, with no per-session approval by Customer B and no written approval from its plant management.
5. No MFA on the accounting SaaS or the router maker's cloud portal.
6. USB sticks and the laptop are not scanned before connecting to plant equipment. At Customer A the scanning station was skipped on about 6 night breakdown calls in the last 12 months (exhibit S3).
7. The legacy engineering virtual machine runs an unsupported operating system, is never updated, and is bridged to whatever network the laptop is on.
8. About 140 customer machine passwords (PLC, HMI, drive, and plant Wi-Fi, for 10 sites) are kept in an unprotected spreadsheet in cloud storage.
9. Monitoring unit firmware was loaded on 4 substation cabinets in 2026 without checking the hash values Customer A provides (exhibit S5).
10. The home office network is shared with household devices.
11. Vibration data and machine details from Customer A's plant were uploaded to the AI vibration analytics trial without reading its terms or getting Customer A's written consent (exhibit S1).
12. No security training.
13. No cyber insurance (general liability policy only). Customer A requires $1 million of cyber liability coverage from the 2027-09-30 renewal (exhibit S8).
14. The owner holds every credential and is the only person who can reach the library. No emergency access sheet and no referral arrangement for breakdown calls.
15. The old laptop (replaced in 2025) still holds a copy of the library and sits in a drawer, not wiped.

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
| 2026-08-20 | IT consultant signs the owner's NDA |
| 2026-08-24 to 2026-08-28 | Self-assessment with the IT consultant (tests on 2026-08-26 at the home office and 2026-08-27 at Customer B, with its maintenance supervisor present) |
| 2026-09-02 | AI use assessment |
| 2026-09-11 | Deliverables adopted by the owner-technician |

## 7. Facts added while building the deliverables (Phase 5)
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Sharing links | Three "anyone with the link" sharing links to customer program folders, made for OEM support desks in 2025 and 2026, were still active. Found in the P04 mapping on 2026-08-25 and removed that day; default sharing set to named people only. Program files had also been emailed to OEM support desks without recording customer consent | P03, P04, P09 |
| Router at Customer B | The router's local admin page accepted the factory default password (P07 test on 2026-08-27, with Customer B's maintenance supervisor present; changed that day). On 2026-09-03 Customer B agreed that the router stays powered off except for sessions it approves by phone, until its plant management decides between a Customer B owned gateway and removal | P01, P02, P04, P07 |
| Test restore | Restoring one machine folder (40 files) from version history on 2026-08-26 worked only one file at a time; a full-library restore would take days | P02, P04, P07, P09 |
| Virtual machine | In the 2026-08-26 test the legacy engineering virtual machine reached the home network and the internet through its bridged adapter | P07 |
| Antivirus test | The built-in antivirus detected and quarantined a standard test file within seconds (2026-08-26) | P07 |
| Phone photos | Equipment photos taken on the phone sync to the owner's personal photo cloud | P02, P04 |
| USB sticks | All 8 sticks are the owner's; the owner does not use sticks handed over by plant staff | P07 |
| Equipment list | An equipment list exists for insurance (laptop, phone, instruments), but it leaves out the USB sticks, the router, and the old laptop | P02, P03 |
| Suite provider assurance | The productivity suite provider's SOC 2 Type 2 report (Security, Availability, Confidentiality; period ending 2026-06-30; unqualified; one remediated exception) was reviewed on 2026-08-26 | P02, P09 |
| Exhibit lapses | Customer A has not raised the S1, S3, or S5 lapses. The owner will tell Customer A about the 4 unverified firmware loads by 2026-09-30 | P03, P07 |
| AI-001 trial | Sensors on 6 motors at Customer A (winding line and drying oven vacuum pumps) and 4 motors at one local plant. 3 alerts in the trial: 2 confirmed by handheld readings, 1 false positive. The vendor's paid business plan offers a data addendum that bars training on customer data and deletes data within 30 days of a request. Customer A uploads were stopped (sensors paused) on 2026-09-02 | P04, P10 |
| AI-002 | The owner uses a consumer generative AI assistant on the phone to draft emails and quotes and to look up published fault code meanings; no customer files pasted (self-review) | P10 |
| Cost estimates | Encrypted backup drives about $250; 10 encrypted USB sticks about $150; password manager about $40 a year; business Wi-Fi on the existing router at no cost | P01, P07 |
