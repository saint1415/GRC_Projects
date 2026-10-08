# Scenario facts: Cris Santos Company | Health Care | Small

All 11 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC |
| Business | Multi-specialty physician practice (NAICS 621111): primary care, cardiology, orthopedics |
| Location | Florida. Two clinics: **Clinic A** (main clinic, administration, on-site X-ray) and **Clinic B** (satellite clinic, about 15 miles away) |
| Workforce | 60 employees: 12 providers (8 physicians, 4 advanced practice providers), 22 clinical staff, 18 front desk and billing staff, 8 management and administration |
| Patients | About 18,000 active patients; about 240 visits per clinic day |
| Revenue | $9.6 million a year (fictional). Under the SBA standard of $16.0 million for NAICS 621111, so SBA-small |
| Payers | Medicare, Florida Medicaid, and commercial plans. Medicaid is federal financial assistance, so Section 1557 of the Affordable Care Act applies (45 CFR Part 92) |
| HIPAA status | **Covered entity**, determined in the intake obligations register (N62-R01): the clearinghouse agreement covers standard electronic transactions (EV-024) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): 42 CFR Part 2, the FTC Health Breach Notification Rule, CMS emergency preparedness conditions, and group health plan requirements do not apply. Payment card data: card terminals are a vendor-hosted, point-to-point encrypted service outside the ePHI systems |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Practice Administrator | Executive owner of the program; accepts risk up to Moderate; signs policies |
| Medical Director | HIPAA **Privacy Officer**; clinical lead for downtime and AI decisions |
| IT Manager | HIPAA **Security Officer** (45 CFR 164.308(a)(2)); runs IT with a contracted managed service provider |
| Billing Manager | Owns the revenue cycle process and the clearinghouse relationship |
| Clinic Managers (2) | Facility access, workstation areas, local downtime procedures |
| HR and Payroll Specialist | Onboarding, terminations, workforce clearance |
| Managed service provider (MSP) | Help desk, patching, after-hours backup monitoring. A business associate |
| Majority owner (Cris Santos) | Accepts High and Very High risks |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Electronic health record and practice management (EHR/PM) with patient portal and e-prescribing | Vendor SaaS | Yes | System of record. The vendor is a business associate with a SOC 2 Type 2 report |
| SYS-02 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects SYS-01, SYS-03, and the cloud tenant |
| SYS-03 | Productivity suite (email, files, chat) | SaaS | Yes (incidental) | Staff email PHI to referring offices |
| SYS-04 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts three practice-managed workloads: the imaging archive (X-ray images), the interface engine (lab and clearinghouse interfaces), and the backup vault |
| SYS-05 | Clinic networks (Clinic A and Clinic B) | On-premises | Yes (in transit) | Firewalls, switches, Wi-Fi; site-to-site VPN to SYS-04 |
| SYS-06 | Endpoints | On-premises | Yes (cached) | 70 Windows workstations and laptops, 12 tablets |
| SYS-07 | Medical devices | On-premises | Yes | X-ray unit and modality workstation (Clinic A), 6 ECG carts, networked vital-sign monitors |
| SYS-08 | Clearinghouse | Vendor SaaS | Yes | Business associate; claims and remittance |
| SYS-09 | Reference laboratory interface | Vendor | Yes | Orders and results via SYS-04 interface engine |
| SYS-10 | Cloud fax and telehealth video | Vendor SaaS | Yes | **No business associate agreement on file** for either (see gaps) |
| SYS-11 | Ambient clinical documentation (AI scribe) | Vendor SaaS | Yes | Pilot with 3 providers since June 2026 (see P10) |

**SSP system (P02):** the *Clinical and Revenue Cycle Platform (CRCP)*: SYS-01, SYS-02, SYS-04, SYS-05, SYS-06, SYS-07, and their interfaces to SYS-08 and SYS-09.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the HIPAA Security Rule** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 incident | Ransomware with exfiltration of PHI, starting from a phishing email |
| P09 SOC 2 | (a) Readiness self-assessment requested by a regional health system before the practice joins its clinically integrated network; (b) review of the EHR vendor's SOC 2 Type 2 report |
| P10 AI | Ambient clinical documentation (AI scribe) pilot |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, exports, walk-throughs, inventories, obligations register |
| 2026-07-13 to 2026-07-24 | BIA interviews, security risk analysis and gap analysis fieldwork |
| 2026-07-27 to 2026-07-31 | Policies drafted from the gaps |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork: operating tests of controls already in place; design review of the draft policies |
| 2026-08-31 | Deliverables and policies approved by the Practice Administrator |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |
