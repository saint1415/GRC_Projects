# Scenario facts: Cris Santos Company | Manufacturing | Sole Proprietorship

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute or regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-machinist files Schedule C) |
| Business | Owner-operated CNC machine shop (NAICS 332710, Machine Shops). Makes small lots (1 to 200 pieces) of precision parts to customer drawings: stainless steel and titanium components for surgical instruments, aluminum brackets and fittings, and shop fixtures |
| Location | Florida. One leased 1,800-square-foot bay in a light-industrial building, with a small office corner. The owner holds the keys; the landlord keeps a master key. Monitored intrusion alarm (EV-011, EV-012) |
| Equipment | One 3-axis vertical machining center (VMC) with a 2012 controller on an embedded operating system that no longer receives updates; its network port receives programs from the laptop. One CNC turning center that loads programs from a USB stick. An inspection bench with calibrated hand gauges and a height gauge (EV-013) |
| Workforce | The owner-machinist only (0 employees). Uses contracted services instead of staff |
| Revenue | About $180,000 a year in receipts (fictional; 2025 Schedule C, EV-006). SBA-small (standard for NAICS 332710: 500 employees; 13 CFR 121.201) |
| Customers | About 12 active business customers and no consumers. **Three Florida medical device manufacturers (OEMs)**, about 65% of receipts. **One aerospace and defense supplier**, about 20%. **About eight local commercial and industrial customers** (marine, food equipment repair, prototypes), about 15% (EV-005) |
| Medical OEM relationship | The shop makes components that the OEMs build into finished devices. The QMSR (21 CFR Part 820, effective 2026-02-02, 89 FR 7496; it incorporates ISO 13485 by reference) binds the OEMs. It does not apply to manufacturers of components or parts (21 CFR 820.1(a)(2)); the OEMs control the shop through their purchasing controls and contracts. Two OEMs have signed supplier quality agreements (SQAs); the third uses PO quality clauses. All three have NDAs. Terms the shop must meet: first article inspection reports, certificates of conformance, material traceability to the heat lot, quality records kept 10 years, prior written approval of process changes to released parts (including CNC program changes), and notice within 5 business days of any unauthorized access to OEM confidential information (EV-015) |
| Defense customer relationship | The aerospace customer is a tier-2 machined-assembly supplier on a DoD prime contract. Since 2025-03 its POs have flowed down FAR 52.204-21 and FAR 52.204-25. In a supplier letter dated 2026-06-15 it told the shop that its new DoD subcontract carries DFARS 252.204-7021 at CMMC Level 1 (Self), and that the shop must hold a Final Level 1 (Self) status with an affirmation in SPRS before the next PO award, expected in December 2026. The customer states in writing that its drawings contain Federal contract information (FCI) but no CUI and no ITAR-controlled technical data, and it does not flow down DFARS 252.204-7012. Its PO terms require notice of any cyber incident affecting its information within 72 hours (EV-016, EV-017) |
| Applicability summary | FD&C Act section 524B: **does not apply** (the shop is not a device manufacturer and submits no premarket submissions). QMSR: not directly (820.1(a)(2)); reaches the shop by contract. FAR 52.204-21 and CMMC Level 1 (Self): **apply by flowdown** to the aerospace work. DFARS 252.204-7012, CMMC Level 2, ITAR registration, and EAR licensing: not today, with the triggers recorded in P03. HIPAA: not applicable (no PHI). Recorded in the intake [obligations register](step-00_P00_intake/obligations-register.csv) |
| Regulatory driver IDs | **N31-33-R02** (CMMC; its Level 1 requirements are the 15 FAR 52.204-21 requirements, 32 CFR 170.14(c)) is the main driver. FAR 52.204-21 is also cited as **C-DIB-R04** from the Defense Industrial Base vertical (verified). N31-33-R03 (ITAR) and N31-33-R04 (EAR) drive the controlled-data intake rule. N31-33-R05 (524B) is recorded as not applicable. Customer contract terms are cited as "OEM SQA" and "Aerospace PO terms". The benchmark is NIST CSF 2.0 with the Small Business Quick-Start Guide (NIST SP 1300, February 2024) |
| State law approach | Florida law is cited only where unavoidable (the Fla. Stat. 501.171 applicability check in P08) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): HIPAA (no PHI); payment card standards (the few card payments go through the accounting SaaS's hosted payment page); SEC disclosure rules (not a registrant); CIRCIA (proposed rule only) |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-machinist | Every role: owner, estimator, CAM programmer, machinist, inspector, quality contact for customers, security lead, CMMC affirming official (32 CFR 170.22), risk acceptor, and incident lead |
| On-call IT technician (independent contractor) | Hourly help with the laptop, router, and machine network link. Remote-support tool on the laptop. Signed the shop's NDA on 2026-08-07, before the self-assessment. **No standing written security terms before that date** (EV-022) |
| Outside bookkeeper (CPA firm) | Monthly bookkeeping and tax returns. Own named login to the accounting SaaS with the accountant role (EV-004, EV-023) |
| Outside processors | A heat treater, a passivation and anodizing shop (both approved by the customers as special processors), and a calibration lab (EV-021) |
| Machine tool service technician (equipment dealer) | Annual preventive maintenance on the VMC. Plugs a service laptop into the controller (EV-024) |
| Customer quality auditors | Visit for supplier audits (two OEM audits in the past 12 months; EV-025) |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds FCI or customer drawings? | Notes |
|---|---|---|---|---|
| SYS-01 | Business productivity suite (email, calendar, cloud file storage) | SaaS, business plan | Yes | Customer drawings, CAM files, NC programs, inspection reports, quotes. The laptop syncs the Jobs folder. MFA on with text-message codes. Deleted files and prior versions kept 30 days by the plan. **Sharing links default to "anyone with the link" and never expire** (EV-001, EV-002) |
| SYS-02 | Accounting and invoicing SaaS | SaaS | No (simple transactional information only) | Invoices, payments, bank feed. Owner (administrator) and bookkeeper accounts. **No MFA on the owner's account** (EV-004) |
| SYS-03 | Shop laptop | Owner device | Yes | CAD/CAM software (desktop license with an online license check), synced Jobs folder, and a shared folder the VMC reads programs from. Built-in full-disk encryption on; built-in antivirus; automatic OS updates. **The owner uses one administrator account for everything.** The IT technician's remote-support tool is installed with unattended access on (EV-008) |
| SYS-04 | Mobile phone | Personal device used for business | Yes (email; setup photos) | Email app, MFA text codes, photos of setups and finished parts, customer texts (EV-009) |
| SYS-05 | CNC machine controllers (OT) | Shop floor | Yes (NC programs derived from customer drawings) | VMC controller on the shop network; turning center by USB stick only. **Programs edited at a controller leave no record** (EV-013, EV-014) |
| SYS-06 | Shop network | Internet provider's router with Wi-Fi | Yes (in transit) | **One flat network** for the laptop, phone, VMC, alarm panel, and visitors. Wi-Fi password posted on the office wall (EV-010, EV-011) |
| SYS-07 | Customer portals | Customer-owned SaaS | Yes (customer-controlled) | Aerospace customer's secure file-exchange portal (named account; the customer enforces MFA). Two OEM supplier portals (POs, first article uploads, corrective action requests) (EV-018) |
| SYS-08 | Consumer generative AI assistant | Vendor SaaS (free consumer plan) | Yes (pasted drawing notes; one uploaded OEM drawing) | Used since 2026-03 for quotes, emails, GD&T explanations, and G-code snippets (EV-029, EV-035). See P10 |
| SYS-09 | Shop website | Website-builder SaaS | Should hold none | Contact page and a photo gallery of past work (EV-028) |

**SSP system (P02):** the *Shop Business Systems (SBS)*: SYS-01 to SYS-06 and SYS-09 (the core SaaS stack for email, files, and accounting, plus the laptop, phone, shop network, website, and the CNC controllers as connected specialized assets), with the customer portals (SYS-07) and the AI assistant (SYS-08) treated as external services.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. For a one-person machine shop the sources are the SaaS admin consoles, the accounting reports, bank and card statements, the inbox, the signed agreements folder, the customer portals, the laptop and phone settings, the router app, the machine controller and the Jobs folder, the insurance agent's portal, and a walk-through of the bay.
- **Which rules and contract terms apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against FAR 52.204-21, CMMC Level 1, the OEM contract terms and the CSF 2.0 benchmark** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 SSP | Shop Business Systems (SBS), short form |
| P03 regulation | FAR 52.204-21 and CMMC Level 1 (Self) (32 CFR Part 170), which reach the shop by flowdown from the aerospace customer; NIST CSF 2.0 (with SP 1300) as the benchmark for the whole business. Section 524B and the QMSR are recorded as not applicable, with reasons |
| P05 BIA | 5 business functions (BP-01 to BP-05) |
| P07 assessment | 10 controls tied to the FAR 52.204-21 requirements and the High risks |
| P08 incident | Ransomware on the shop laptop that encrypts the synced Jobs folder and the VMC program share, with theft of customer drawings (OEM confidential and aerospace FCI) |
| P09 SOC 2 | Security criteria only. The owner's self-check, used to answer customer supplier security questionnaires, plus a review of the productivity suite provider's SOC 2 report. A SOC 2 report for the shop is not sought |
| P10 AI | The consumer generative AI assistant (SYS-08) |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-15 | Aerospace customer's supplier letter on CMMC Level 1 (Self) (EV-017) |
| 2026-08-03 to 2026-08-07 | Intake: the owner collects SaaS admin exports, accounting reports, statements, agreements and customer terms, device, router and controller settings, the program records, and the bay walk-through; inventories; obligations register |
| 2026-08-10 to 2026-08-14 | Self-assessment with the on-call IT technician (under NDA since 2026-08-07): BIA, risk assessment, gap analysis, and control assessment; tests on 2026-08-12 |
| 2026-08-13 | Productivity suite provider's SOC 2 report received and reviewed (EV-030; P09) |
| 2026-08-17 to 2026-09-03 | POL-01 drafted from the risks, the gaps and the test results. No written policy existed during the assessment |
| 2026-08-19 | AI use assessment |
| 2026-09-04 | Deliverables and POL-01 adopted by the owner-machinist |
| 2026-11-30 | Target: CMMC Level 1 self-assessment complete, results and affirmation entered in SPRS |
| December 2026 (expected) | Next aerospace PO award |
| 2027-02 (planned) | Follow-up check: operating effectiveness of the controls POL-01 introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Website photo | In 2026-04 the owner posted a gallery photo of a finished aerospace part, with the customer's part number visible, on the shop website. Found in P07 on 2026-08-12 and removed that day (EV-AC-22) | P01, P03, P07 |
| Router | The router's admin password was the default printed on its label (found in P07 on 2026-08-12; EV-SC-7) | P03, P04, P07 |
| Remote-support tool | Unattended access on the IT technician's remote-support tool was turned off on 2026-08-12 during the assessment (EV-AC-17) | P01, P07 |
| Payment redirection attempt | In 2026-05 an OEM's accounts payable clerk received a spoofed email asking for payment to "new bank details". The OEM called to check and nothing was paid (EV-027) | P01, P08 |
| AI assistant use | About 40 chats since 2026-03, including one uploaded OEM drawing PDF (2026-05) and pasted notes from two aerospace drawings. No aerospace drawing file was uploaded. The consumer plan's default setting allows chats to be used to improve the vendor's models (EV-029, EV-035, EV-036) | P01, P10 |
| Productivity suite assurance | The productivity suite provider publishes a SOC 2 Type 2 report to business customers through its trust portal. The owner downloaded and read it on 2026-08-13 (EV-003, EV-030) | P02, P09 |
| Program storage | Released programs for OEM parts are kept in the Jobs folder and in VMC controller memory. About 180 released programs exist across the three OEMs (EV-014) | P05, P07 |
| Program mismatch | In the P07 test on 2026-08-12, 2 of 10 OEM programs in VMC memory differed from the Jobs folder copy (feed-rate and offset edits made at the controller and not recorded). The parts made with them passed inspection. The owner reviews both with the OEM quality contact by 2026-09-15 (EV-SI-7) | P01, P07, P09 |
| VMC share | The laptop folder the VMC reads programs from accepted connections from any device on the shop Wi-Fi with no password (P07 test, 2026-08-12; EV-SC-7) | P03, P04, P07 |
| Open sharing links | 27 "anyone with the link" shares were open on 2026-08-11, including 4 aerospace drawing packages sent to the anodizer (EV-034) | P03, P04, P07 |
| Old media | The retired laptop (about to be traded in) and 6 used USB sticks were in the office drawer on 2026-08-11 (EV-MP-6) | P03, P07 |
| Bookkeeper MFA | The bookkeeper signs in to the accounting SaaS through the CPA firm's own account with MFA (EV-004) | P04 |
| AI G-code and customer notice | About 12 G-code snippets were generated or edited with the AI assistant; 3 were used on the machines after the owner edited them (EV-035). The owner told the affected OEM and the aerospace customer in writing on 2026-08-20 what drawing content had been shared and that it was deleted; neither asked for more | P10 |
