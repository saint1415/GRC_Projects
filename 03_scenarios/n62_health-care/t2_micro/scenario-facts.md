# Scenario facts: Cris Santos Company | Health Care | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes.

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
| HIPAA status | **Covered entity.** Claims are sent electronically through the EHR's clearinghouse |
| Not in scope | 42 CFR Part 2; group health plan requirements; payment cards (vendor-hosted terminal) |
| State law approach | Florida law cited only where unavoidable |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Owner physician | Accepts risk; approves policies and spending |
| Office Manager | HIPAA **Privacy Officer and Security Officer** (combined; designated in writing in 2026) |
| Billing Specialist | Clearinghouse relationship; revenue cycle |
| Managed service provider (MSP) | IT support, patching, antivirus, firewall. A business associate (BAA on file) |

## 3. Systems
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

## 4. Current security posture: early to partial
**In place today:**
- MFA on the EHR and email
- MSP patching, antivirus, and firewall
- BAAs with the EHR vendor, MSP, and fax vendor
- Laptop encryption
- Unique EHR logins
- Guest Wi-Fi separation
- New-hire HIPAA video

**Missing:**
1. The last risk analysis was a 2019 consultant checklist; nothing since.
2. Policies are a purchased template, never adopted.
3. The productivity suite BAA has not been accepted.
4. Desktops are unencrypted.
5. The shared-drive backup has never been restore-tested.
6. No audit log review.
7. No incident response plan.
8. Terminations are handled by the office manager "when remembered". One former MA's account was found active after 3 months.
9. No annual training or phishing awareness.
10. The AI scribe pilot started before the BAA was signed.
11. No inventory of devices or where ePHI lives.

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
| 2026-07-20 to 2026-07-31 | Risk analysis and gap analysis with the MSP |
| 2026-08-10 to 2026-08-12 | Control assessment (independent consultant) |
| 2026-08-31 | Deliverables approved by the owner physician |

## 7. Facts added while building the deliverables
These facts were added in Phase 2 because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Physicians | The owner physician and one **associate physician**. The associate physician runs the AI scribe pilot (started 2026-06-01) | P01, P10 |
| Endpoints | SYS-03 is 6 desktops (2 front desk, 1 billing, 2 clinical stations, 1 procedure-room workstation connected to SYS-07) and 4 laptops (both physicians, office manager, billing). The 2 tablets are used by the physicians in exam rooms; they are MSP-managed with a passcode and built-in device encryption | P01, P02, P04, P07 |
| Shared drive | The "shared drive" is the practice's shared folder in the productivity suite (SYS-02). It is synced to the desktops by the suite's sync client. SYS-05 copies it nightly and keeps 30 days of versions (the default). SYS-05 is administered with one MSP administrator account | P01, P04, P05, P08 |
| Backup vendor | The SYS-05 subscription is held by the MSP and resold to the practice, so the backup vendor is the MSP's subcontractor. The MSP BAA requires subcontractor BAAs; flow-down has not been verified | P03, P04, P07 |
| Clearinghouse and lab | The clearinghouse is contracted through the EHR vendor as its subcontractor. Reference laboratory orders and results flow through the EHR vendor's lab interface | P02, P05 |
| Internet | One business internet line; no failover | P01, P05 |
| Cyber insurance | The practice holds a cyber liability policy with a 24x7 breach hotline and panel vendors (breach counsel, forensics). The policy requires prompt notice and use of panel vendors | P08 |
| Former MA account | Found active on 2026-07-21 during the risk analysis, 3 months after termination, and disabled that day. The EHR and email sign-in logs showed no use after the termination date | P01, P03, P07 |
| Referral network | A local hospital's referral network sent a security questionnaire in July 2026; the response is due 2026-09-30 | P09 |
| Assessor | The P07 assessor is an independent HIPAA security consultant, not involved in the risk analysis or in operating any control | P07 |
| ECG workstation patching | P07 testing found that the MSP had excluded the procedure-room workstation (SYS-07 host) from patching since April 2026, at the device vendor's request, without telling the practice | P01, P07 |
| Productivity suite BAA | The Office Manager accepted the productivity suite BAA in the admin console on 2026-08-14, after the fieldwork found the gap | P01, P03, P07 |
