# Scenario facts: Cris Santos Company | Health Care | Micro

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC |
| Business | Primary care office with two physicians (NAICS 621111) |
| Location | Florida. One office suite |
| Workforce | 7 employees: 2 physicians (one is the owner), 2 medical assistants, 1 front desk coordinator, 1 billing specialist, 1 office manager |
| Patients | About 3,500 active patients; about 40 visits per clinic day |
| Revenue | About $1.1 million a year (fictional). SBA-small (standard $16.0 million) |
| Payers | Medicare, Florida Medicaid, and commercial plans. Section 1557 applies (Medicaid is federal financial assistance) |
| HIPAA status | **Covered entity**, determined in the intake obligations register (N62-R01): claims are sent electronically through the EHR's clearinghouse (EV-019) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): 42 CFR Part 2, the FTC Health Breach Notification Rule, and CMS emergency preparedness conditions do not apply. Group health plan requirements are excluded in the gap analysis (P03). Payment cards: vendor-hosted terminal |
| State law approach | Florida law cited only where unavoidable |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Owner physician | Accepts risk; approves policies and spending |
| Office Manager | HIPAA **Privacy Officer and Security Officer** (combined; designated in writing in 2026) |
| Billing Specialist | Clearinghouse relationship; revenue cycle |
| Managed service provider (MSP) | IT support, patching, antivirus, firewall. A business associate (BAA on file) |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | EHR/PM with portal, e-prescribing, and clearinghouse | Vendor SaaS | Yes | BAA on file; MFA enforced |
| SYS-02 | Business productivity suite (email, files) | SaaS | Yes | Business plan; BAA available but **not accepted in the admin console** |
| SYS-03 | 10 workstations and laptops, 2 tablets | MSP-managed | Yes (cached) | Laptops encrypted; desktops not |
| SYS-04 | Office network: small-business firewall, Wi-Fi | On-premises | In transit | Guest Wi-Fi separated; MSP-managed |
| SYS-05 | Cloud file-sync backup of the shared drive | SaaS | Yes | Set up by the MSP; never restore-tested |
| SYS-06 | Cloud fax | SaaS | Yes | BAA on file |
| SYS-07 | ECG machine and spirometer | On-premises | Yes | Connected to one workstation via USB |
| SYS-08 | AI scribe | Vendor SaaS | Yes | One physician piloting; BAA under review |

**SSP system (P02):** the *Office Clinical Platform*: SYS-01 to SYS-07.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). For a 7-person office the systems of record are the vendor admin consoles, the payroll service, the MSP's reports, the contracts folder, and a walk-through. Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the HIPAA Security Rule** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 incident | Ransomware with PHI exfiltration via a phishing email; the MSP is in the notification chain; the insurer's panel counsel is engaged |
| P09 SOC 2 | Security plus Availability. The readiness check is used to answer security questionnaires from a local hospital's referral network; also a review of the EHR vendor's SOC 2 report |
| P10 AI | AI scribe pilot (one physician) |
| Cloud | SaaS plus one cloud workload: the file-sync backup (SaaS-hosted). Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-17 | Intake: evidence requests, exports from the vendor consoles, the payroll service and the MSP, the contracts folder, a walk-through, inventories, obligations register |
| 2026-07-20 to 2026-07-31 | BIA interviews, risk analysis and gap analysis with the MSP |
| 2026-08-03 to 2026-08-07 | Policies drafted from the gaps |
| 2026-08-10 to 2026-08-12 | Control assessment (independent consultant): operating tests of controls already in place; design review of the draft policies |
| 2026-08-31 | Deliverables and policies approved by the owner physician |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added in Phase 2 because the deliverables needed them. They do not change sections 1-6. Facts drawn from the practice's records cite the evidence register ID they rest on.

| Topic | Added fact | Used in |
|---|---|---|
| Physicians | The owner physician and one **associate physician**. The associate physician runs the AI scribe pilot (started 2026-06-01) (EV-001; EV-023) | P01, P10 |
| Endpoints | SYS-03 is 6 desktops (2 front desk, 1 billing, 2 clinical stations, 1 procedure-room workstation connected to SYS-07) and 4 laptops (both physicians, office manager, billing). The 2 tablets are used by the physicians in exam rooms; they are MSP-managed with a passcode and built-in device encryption (EV-009; EV-011; EV-033) | P01, P02, P04, P07 |
| Shared drive | The "shared drive" is the practice's shared folder in the productivity suite (SYS-02). It is synced to the desktops by the suite's sync client. SYS-05 copies it nightly and keeps 30 days of versions (the default). SYS-05 is administered with one MSP administrator account (EV-006; EV-015) | P01, P04, P05, P08 |
| Backup vendor | The SYS-05 subscription is held by the MSP and resold to the practice, so the backup vendor is the MSP's subcontractor. The MSP BAA requires subcontractor BAAs; flow-down has not been verified (EV-015; EV-017; EV-022) | P03, P04, P07 |
| Clearinghouse and lab | The clearinghouse is contracted through the EHR vendor as its subcontractor. Reference laboratory orders and results flow through the EHR vendor's lab interface (EV-019) | P02, P05 |
| Internet | One business internet line; no failover (EV-032) | P01, P05 |
| Cyber insurance | The practice holds a cyber liability policy with a 24x7 breach hotline and panel vendors (breach counsel, forensics). The policy requires prompt notice and use of panel vendors (EV-028) | P08 |
| Former MA account | Found active on 2026-07-21 during the risk analysis, 3 months after termination, and disabled that day. The EHR and email sign-in logs showed no use after the termination date (EV-042) | P01, P03, P07 |
| Referral network | A local hospital's referral network sent a security questionnaire in July 2026; the response is due 2026-09-30 (EV-029) | P09 |
| Assessor | The P07 assessor is an independent HIPAA security consultant, not involved in the risk analysis or in operating any control | P07 |
| ECG workstation patching | P07 testing found that the MSP had excluded the procedure-room workstation (SYS-07 host) from patching since April 2026, at the device vendor's request, without telling the practice (EV-SI-2) | P01, P07 |
| Productivity suite BAA | The Office Manager accepted the productivity suite BAA in the admin console on 2026-08-14, after the fieldwork found the gap (EV-048) | P01, P03, P07 |
| MSP contract | Covers help desk, patching, antivirus, firewall, Wi-Fi, and backup administration, with a 4-business-hour response time and no recovery time commitment (EV-018) | P05, P07 |
| Office security | Keyed suite entry with an after-hours alarm; keys held by the Office Manager and both physicians; locked network closet (EV-033; EV-034) | P02, P03 |
| Finances and payroll | A cash reserve covers about 30 days of expenses; payroll runs biweekly through an outside payroll service (EV-030; EV-001) | P01, P05 |
| Past events | A staff phone was lost in 2025 and a fax was misdirected; both were handled informally with no record. Two desktops were retired in 2025 with no disposal record (EV-035; EV-016) | P03, P09 |
