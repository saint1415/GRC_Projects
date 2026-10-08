# Scenario facts: Cris Santos Company | Manufacturing | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute or regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-machinist files Schedule C) |
| Business | Owner-operated CNC machine shop (NAICS 332710, Machine Shops). Makes small lots (1 to 200 pieces) of precision parts to customer drawings: stainless steel and titanium components for surgical instruments, aluminum brackets and fittings, and shop fixtures |
| Location | Florida. One leased 1,800-square-foot bay in a light-industrial building, with a small office corner. The owner holds the keys; the landlord keeps a master key. Monitored intrusion alarm |
| Equipment | One 3-axis vertical machining center (VMC) with a 2012 controller on an embedded operating system that no longer receives updates; its network port receives programs from the laptop. One CNC turning center that loads programs from a USB stick. An inspection bench with calibrated hand gauges and a height gauge |
| Workforce | The owner-machinist only (0 employees). Uses contracted services instead of staff |
| Revenue | About $180,000 a year in receipts (fictional). SBA-small (standard for NAICS 332710: 500 employees; 13 CFR 121.201) |
| Customers | About 12 active business customers and no consumers. **Three Florida medical device manufacturers (OEMs)**, about 65% of receipts. **One aerospace and defense supplier**, about 20%. **About eight local commercial and industrial customers** (marine, food equipment repair, prototypes), about 15% |
| Medical OEM relationship | The shop makes components that the OEMs build into finished devices. The QMSR (21 CFR Part 820, effective 2026-02-02, 89 FR 7496; it incorporates ISO 13485 by reference) binds the OEMs. It does not apply to manufacturers of components or parts (21 CFR 820.1(a)(2)); the OEMs control the shop through their purchasing controls and contracts. Two OEMs have signed supplier quality agreements (SQAs); the third uses PO quality clauses. All three have NDAs. Terms the shop must meet: first article inspection reports, certificates of conformance, material traceability to the heat lot, quality records kept 10 years, prior written approval of process changes to released parts (including CNC program changes), and notice within 5 business days of any unauthorized access to OEM confidential information |
| Defense customer relationship | The aerospace customer is a tier-2 machined-assembly supplier on a DoD prime contract. Since 2025-03 its POs have flowed down FAR 52.204-21 and FAR 52.204-25. In a supplier letter dated 2026-06-15 it told the shop that its new DoD subcontract carries DFARS 252.204-7021 at CMMC Level 1 (Self), and that the shop must hold a Final Level 1 (Self) status with an affirmation in SPRS before the next PO award, expected in December 2026. The customer states in writing that its drawings contain Federal contract information (FCI) but no CUI and no ITAR-controlled technical data, and it does not flow down DFARS 252.204-7012. Its PO terms require notice of any cyber incident affecting its information within 72 hours |
| Applicability summary | FD&C Act section 524B: **does not apply** (the shop is not a device manufacturer and submits no premarket submissions). QMSR: not directly (820.1(a)(2)); reaches the shop by contract. FAR 52.204-21 and CMMC Level 1 (Self): **apply by flowdown** to the aerospace work. DFARS 252.204-7012, CMMC Level 2, ITAR registration, and EAR licensing: not today, with the triggers recorded in P03. HIPAA: not applicable (no PHI) |
| Regulatory driver IDs | **N31-33-R02** (CMMC; its Level 1 requirements are the 15 FAR 52.204-21 requirements, 32 CFR 170.14(c)) is the main driver. FAR 52.204-21 is also cited as **C-DIB-R04** from the Defense Industrial Base vertical (verified). N31-33-R03 (ITAR) and N31-33-R04 (EAR) drive the controlled-data intake rule. N31-33-R05 (524B) is recorded as not applicable. Customer contract terms are cited as "OEM SQA" and "Aerospace PO terms". The benchmark is NIST CSF 2.0 with the Small Business Quick-Start Guide (NIST SP 1300, February 2024) |
| State law approach | Florida law is cited only where unavoidable (the Fla. Stat. 501.171 applicability check in P08) |
| Not in scope | HIPAA (no PHI); payment card standards (the few card payments go through the accounting SaaS's hosted payment page); SEC disclosure rules (not a registrant); CIRCIA (proposed rule only) |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-machinist | Every role: owner, estimator, CAM programmer, machinist, inspector, quality contact for customers, security lead, CMMC affirming official (32 CFR 170.22), risk acceptor, and incident lead |
| On-call IT technician (independent contractor) | Hourly help with the laptop, router, and machine network link. Remote-support tool on the laptop. Signed the shop's NDA on 2026-08-07, before the self-assessment. **No standing written security terms before that date** |
| Outside bookkeeper (CPA firm) | Monthly bookkeeping and tax returns. Own named login to the accounting SaaS with the accountant role |
| Outside processors | A heat treater, a passivation and anodizing shop (both approved by the customers as special processors), and a calibration lab |
| Machine tool service technician (equipment dealer) | Annual preventive maintenance on the VMC. Plugs a service laptop into the controller |
| Customer quality auditors | Visit for supplier audits (two OEM audits in the past 12 months) |

## 3. Systems
| ID | System | Hosting | Holds FCI or customer drawings? | Notes |
|---|---|---|---|---|
| SYS-01 | Business productivity suite (email, calendar, cloud file storage) | SaaS, business plan | Yes | Customer drawings, CAM files, NC programs, inspection reports, quotes. The laptop syncs the Jobs folder. MFA on with text-message codes. Deleted files and prior versions kept 30 days by the plan. **Sharing links default to "anyone with the link" and never expire** |
| SYS-02 | Accounting and invoicing SaaS | SaaS | No (simple transactional information only) | Invoices, payments, bank feed. Owner (administrator) and bookkeeper accounts. **No MFA on the owner's account** |
| SYS-03 | Shop laptop | Owner device | Yes | CAD/CAM software (desktop license with an online license check), synced Jobs folder, and a shared folder the VMC reads programs from. Built-in full-disk encryption on; built-in antivirus; automatic OS updates. **The owner uses one administrator account for everything.** The IT technician's remote-support tool is installed with unattended access on |
| SYS-04 | Mobile phone | Personal device used for business | Yes (email; setup photos) | Email app, MFA text codes, photos of setups and finished parts, customer texts |
| SYS-05 | CNC machine controllers (OT) | Shop floor | Yes (NC programs derived from customer drawings) | VMC controller on the shop network; turning center by USB stick only. **Programs edited at a controller leave no record** |
| SYS-06 | Shop network | Internet provider's router with Wi-Fi | Yes (in transit) | **One flat network** for the laptop, phone, VMC, alarm panel, and visitors. Wi-Fi password posted on the office wall |
| SYS-07 | Customer portals | Customer-owned SaaS | Yes (customer-controlled) | Aerospace customer's secure file-exchange portal (named account; the customer enforces MFA). Two OEM supplier portals (POs, first article uploads, corrective action requests) |
| SYS-08 | Consumer generative AI assistant | Vendor SaaS (free consumer plan) | Yes (pasted drawing notes; one uploaded OEM drawing) | Used since 2026-03 for quotes, emails, GD&T explanations, and G-code snippets. See P10 |
| SYS-09 | Shop website | Website-builder SaaS | Should hold none | Contact page and a photo gallery of past work |

**SSP system (P02):** the *Shop Business Systems (SBS)*: SYS-01 to SYS-06 and SYS-09 (the core SaaS stack for email, files, and accounting, plus the laptop, phone, shop network, website, and the CNC controllers as connected specialized assets), with the customer portals (SYS-07) and the AI assistant (SYS-08) treated as external services.

## 4. Current security posture: informal (basic hygiene, big gaps)
**In place today:**
- Business email and file plan (not a personal account), with MFA by text-message code
- Built-in full-disk encryption on the laptop (on by default when bought in 2025)
- Automatic OS updates and built-in antivirus on the laptop; automatic updates on the phone
- File version history (30 days) on the cloud file storage
- NDAs with all four main customers; SQAs with two OEMs
- Locked bay with a monitored alarm; paper travelers and inspection records in a locked cabinet
- The aerospace customer's portal enforces MFA on the shop's account
- The customer states in writing that no CUI or ITAR data is provided

**Missing:**
1. No written security policy, risk assessment, or incident plan.
2. FAR 52.204-21 has been on the aerospace POs since 2025-03 but was never reviewed. No CMMC Level 1 self-assessment, no CAGE code, and no SPRS entry; the customer's deadline is the December 2026 award.
3. The owner uses one administrator account on the laptop for everything.
4. No MFA on the accounting SaaS.
5. The shop network is flat: the laptop, the VMC (unsupported controller software), the alarm panel, and visitors share it. The router admin password was never changed.
6. No backup independent of sync. Ransomware on the laptop would sync encrypted files to the cloud; a version restore has never been tried.
7. Drawings go to outside processors through open, non-expiring sharing links or email. Aerospace drawings (FCI) were emailed to the anodizer with no flowdown.
8. No visitor log and no escort rule (auditors, the service technician, delivery drivers).
9. USB sticks move programs to the turning center with no scanning rule; the service technician connects his own laptop to the VMC.
10. The laptop replaced in 2025 sits in a drawer with old job files; no sanitization.
11. No change control or integrity check for released CNC programs on OEM parts.
12. A consumer generative AI assistant was used with customer drawing content and for G-code.
13. No security training.
14. No cyber insurance (general liability policy only).
15. The owner holds every credential; no emergency access sheet.

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
| 2026-06-15 | Aerospace customer's supplier letter on CMMC Level 1 (Self) |
| 2026-08-10 to 2026-08-14 | Self-assessment with the on-call IT technician (under NDA since 2026-08-07); tests on 2026-08-12 |
| 2026-08-19 | AI use assessment |
| 2026-09-04 | Deliverables adopted by the owner-machinist |
| 2026-11-30 | Target: CMMC Level 1 self-assessment complete, results and affirmation entered in SPRS |
| December 2026 (expected) | Next aerospace PO award |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Website photo | In 2026-04 the owner posted a gallery photo of a finished aerospace part, with the customer's part number visible, on the shop website. Found in P07 on 2026-08-12 and removed that day | P01, P03, P07 |
| Router | The router's admin password was the default printed on its label (found in P07 on 2026-08-12) | P03, P04, P07 |
| Remote-support tool | Unattended access on the IT technician's remote-support tool was turned off on 2026-08-12 during the assessment | P01, P07 |
| Payment redirection attempt | In 2026-05 an OEM's accounts payable clerk received a spoofed email asking for payment to "new bank details". The OEM called to check and nothing was paid | P01, P08 |
| AI assistant use | About 40 chats since 2026-03, including one uploaded OEM drawing PDF (2026-05) and pasted notes from two aerospace drawings. No aerospace drawing file was uploaded. The consumer plan's default setting allows chats to be used to improve the vendor's models | P01, P10 |
| Productivity suite assurance | The productivity suite provider publishes a SOC 2 Type 2 report to business customers through its trust portal. The owner downloaded and read it on 2026-08-13 | P02, P09 |
| Program storage | Released programs for OEM parts are kept in the Jobs folder and in VMC controller memory. About 180 released programs exist across the three OEMs | P05, P07 |
| Program mismatch | In the P07 test on 2026-08-12, 2 of 10 OEM programs in VMC memory differed from the Jobs folder copy (feed-rate and offset edits made at the controller and not recorded). The parts made with them passed inspection. The owner reviews both with the OEM quality contact by 2026-09-15 | P01, P07, P09 |
| VMC share | The laptop folder the VMC reads programs from accepted connections from any device on the shop Wi-Fi with no password (P07 test, 2026-08-12) | P03, P04, P07 |
| Open sharing links | 27 "anyone with the link" shares were open on 2026-08-11, including 4 aerospace drawing packages sent to the anodizer | P03, P04, P07 |
| Old media | The retired laptop (about to be traded in) and 6 used USB sticks were in the office drawer on 2026-08-11 | P03, P07 |
| Bookkeeper MFA | The bookkeeper signs in to the accounting SaaS through the CPA firm's own account with MFA | P04 |
| AI G-code and customer notice | About 12 G-code snippets were generated or edited with the AI assistant; 3 were used on the machines after the owner edited them. The owner told the affected OEM and the aerospace customer in writing on 2026-08-20 what drawing content had been shared and that it was deleted; neither asked for more | P10 |
