# Scenario facts: Cris Santos Company | Health Care | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given.

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
| HIPAA status | **Covered entity.** A health care provider that transmits claims electronically through a clearinghouse (45 CFR 160.103) |
| Not in scope | 42 CFR Part 2: the practice does not run a federally assisted substance use disorder program. Group health plan requirements (45 CFR 164.314(b)): the practice does not administer a group health plan. Payment card data: card terminals are a vendor-hosted, point-to-point encrypted service outside the ePHI systems |
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

## 4. Current security posture: partially compliant

**In place today:**
- MFA for email, the EHR, and the cloud console
- Unique user IDs in the EHR
- A BAA with the EHR vendor, clearinghouse, MSP, and reference lab
- Automatic OS patching on endpoints
- Antivirus (signature-based)
- Badge access at Clinic A
- A paper shredding vendor
- New-hire HIPAA training
- Full-disk encryption on laptops, but not on desktops
- Daily backups of SYS-04 workloads, stored in the same cloud region
- The EHR vendor's own backups

**Missing or weak, found in the 2026 assessments:**
1. No documented security risk analysis since 2021 (Required, 164.308(a)(1)(ii)(A)).
2. Security policies are a 2019 template, never adopted or reviewed.
3. No review of audit logs or EHR access reports.
4. No written incident response plan. Incidents are handled ad hoc.
5. No contingency plan, downtime procedure, or backup restore test. Backups sit in the same region and account as production.
6. The X-ray modality workstation uses a shared login and runs an unsupported operating system version.
7. Desktop workstations are unencrypted.
8. No BAAs with the cloud fax or telehealth vendors. The AI scribe vendor's BAA is still under legal review.
9. Accounts of departing staff are disabled within about 5 business days, with no same-day process.
10. No vulnerability scanning. Signature antivirus only (no endpoint detection and response).
11. Training happens only at hire. There are no periodic security reminders or phishing exercises.
12. Clinic B uses keyed locks, and no log is kept of who holds the keys.
13. Hard drives are destroyed without certificates of destruction.
14. Clinical staff have no approved-tools list for generative AI.
15. Four networked vital-sign monitors still use the manufacturer's default admin password (found during P07 testing).

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
| 2026-07-13 to 2026-07-24 | Security risk analysis and gap analysis fieldwork |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork |
| 2026-08-31 | Deliverables approved by the Practice Administrator |
