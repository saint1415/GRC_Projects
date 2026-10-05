# Scenario facts: Cris Santos Company | Construction | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship operating under the owner's trade name; the owner files Schedule C) |
| Business | Commercial and institutional building general contractor (NAICS 236220). Small renovations and tenant build-outs: offices, a dental suite, a church fellowship hall, and one federal clinic renovation. The owner estimates, manages, and supervises every job and **subcontracts all trade work** |
| Location | Florida. A **home office** in the owner's residence, a rented **self-storage unit** for tools and materials, one pickup truck, and 2 to 4 active jobsites at a time (no jobsite trailers) |
| Workforce | The owner only (0 employees). Uses contracted services and trade subcontractors instead of staff |
| Revenue | About $180,000 in annual receipts (fictional). Under the SBA standard of $45.0 million for NAICS 236220 (13 CFR 121.201), so SBA-small |
| Billing and payments | Monthly progress payment applications (pay apps) with a schedule of values on larger jobs, invoices on small ones, about $15,000 billed in a typical month. Private clients pay by ACH or check. The federal agency pays by electronic funds transfer to the bank account in the company's SAM registration (FAR 52.232-33(b)). The owner pays about 14 trade subcontractors and 6 suppliers a year by ACH from the bank portal or by check. On the federal job the owner must pay subcontractors within 7 days of receiving payment (FAR 52.232-27(c)(1)) |
| Federal work (about 35% of 2026 receipts) | **FC-1:** a firm-fixed-price contract with the Department of Veterans Affairs (civilian agency) to renovate a staff break room and two offices at a community-based outpatient clinic in Florida, about $68,000, awarded 2026-03-09 under a small business set-aside, performance through 2026-11. It includes FAR 52.204-21, 52.204-23, 52.204-25, 52.222-8, 52.232-27, and 52.232-33. Construction wage rate requirements apply, so the owner collects and submits subcontractors' weekly certified payrolls (FAR 52.222-8(b)(1)) |
| Federal pipeline | A larger prime contractor has asked the owner to perform interior renovation work (about $45,000) under the prime's **DoD task order** at an Army Reserve Center in Florida, expected to be awarded 2026-12. The prime's task order includes DFARS 252.204-7021 at **CMMC Level 1 (Self)**, and the prime will require the owner to hold a current Final Level 1 (Self) status with an affirmation in SPRS **before the subcontract is awarded** (32 CFR 170.23(a)(1); DFARS 252.204-7021(d)(4) and (f)(2)). No CUI is expected |
| Private work (about 65%) | A dental office tenant build-out (about $52,000), a church fellowship hall renovation (about $35,000), and small retail repairs |
| Insurance | General liability and tool coverage only. **No cyber insurance and no funds transfer fraud or social engineering coverage** (confirmed with the insurance agent on 2026-07-14) |
| Not in scope | CUI, NIST SP 800-171, and DFARS 252.204-7012 (no DoD contract today and no CUI expected; see P03). HIPAA (the dental office build-out gives the owner no patient information). PCI DSS (no card payments). SEC rules (not a public company) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171, which covers sole proprietorships). The samples otherwise stay federal |

## 2. People and contracted services (role titles only)

| Role | Duties |
|---|---|
| Owner | Every role: business owner, estimator, project manager, superintendent, billing and payables, **security lead**, risk acceptor, incident commander, SAM Entity Administrator, and designated **CMMC Affirming Official** (32 CFR 170.22(a)(1)) |
| Outside bookkeeper | Independent contractor, about 6 hours a month: reconciles the bank and accounting records, prepares 1099s. **Signs in to the accounting SaaS with the owner's own username and password** (no separate account). Engagement letter has no security or confidentiality terms |
| On-call IT technician | Independent local technician, paid by the hour. Set up the laptop and home router. No standing remote access. Helped with the July 2026 self-assessment under a short written engagement with a confidentiality clause (signed 2026-07-13) |
| Tax preparer | CPA firm; prepares the annual return from the accounting SaaS export |
| Insurance agent | General liability and tools. No cyber product placed |
| Trade subcontractors | About 14 used in 2026 (electrical, plumbing, HVAC, drywall, painting, flooring, doors and hardware). 8 are themselves sole proprietors and gave the owner W-9 forms with their Social Security numbers. 6 are working on FC-1 and receive VA drawings through the project management portal |

## 3. Systems

| ID | System | Hosting | Holds FCI? | Notes |
|---|---|---|---|---|
| SYS-01 | Construction project management and pay application SaaS (small-contractor plan): drawings, RFIs, submittals, daily logs, photos, schedule of values, pay apps, and a portal for subcontractors and client representatives | Vendor SaaS | Yes (FC-1 drawings, submittals, daily logs, pay apps) | System of record for every job. Owner is the only administrator. 23 external portal users, 9 of them from jobs closed in 2025. MFA available but **off**. Vendor has a SOC 2 Type 2 report (reviewed in P09) |
| SYS-02 | Accounting SaaS (small business plan) | Vendor SaaS | No (simple transactional information only) | Invoices, bills, vendor records with bank details, ACH bill pay, bank feed, 1099 tracking with W-9 files attached. **One login, shared with the outside bookkeeper**; password only |
| SYS-03 | Business email and file storage (small business productivity plan, 1 licensed user, company domain) | SaaS | Yes | Channel for pay apps, lien waivers, subcontractor invoices, and payment correspondence. 2-step verification by **text message code**. The domain publishes SPF only (no DKIM or DMARC) |
| SYS-04 | Laptop (owner-owned) | Home office and field | Yes | Built-in full-disk encryption **on** (default at purchase). Built-in antivirus and automatic updates on. **One login with administrator rights, also used by family members** |
| SYS-05 | Smartphone (owner's personal phone used for business) | Field | Yes (email, jobsite photos) | Passcode and biometric unlock; encrypted by default. Holds the email text codes, the bank app, and the authenticator for the government sign-in service. Jobsite photos sync to the owner's **personal consumer cloud photo account** |
| SYS-06 | Home office network: internet service provider gateway plus an owner-bought Wi-Fi router | Home office | Yes (in transit) | Shared with family phones, a game console, a smart TV, and doorbell camera. Router firmware never updated. A carrier-branded mobile hotspot was used at jobsites until 2026-07-16 (see section 4) |
| SYS-07 | Business online banking (ACH, wires, mobile deposit) | Bank-hosted | No | Single user (the owner). The bank requires app approval for each new payee and each ACH batch, with a $30,000 daily ACH limit. No positive pay |
| SYS-08 | Federal portals: SAM.gov (entity registration with EFT bank information), the federal invoicing portal used for FC-1, and SPRS (no access yet) | Government-operated | n/a | Company accounts only. The government sign-in service enforces MFA. The owner is the SAM Entity Administrator |
| SYS-09 | AI estimating and bid assistant (individual subscription) | Vendor SaaS | Yes (uploaded FC-1 change-order drawings) | Takeoff from uploaded drawings, pricing suggestions, and proposal drafting. Used since 2026-03. "Use my content to improve the service" was on until 2026-07-17 (see P10) |

Paper: current plan sets ride in the truck; signed subcontracts, lien waivers, and certified payroll copies sit in a file cabinet in the home office.

**SSP system (P02):** the *Project Management and Payment Application System (PMPAS)*: SYS-01 to SYS-06, and their interfaces to SYS-07, SYS-08, and SYS-09. The PMPAS boundary is also the proposed CMMC Level 1 assessment scope (32 CFR 170.19(b)).

## 4. Current security posture: early (basic hygiene, big gaps)

**In place today:**
- Laptop full-disk encryption (on by default at purchase), built-in antivirus with real-time scanning, and automatic operating system updates
- Phone passcode, biometric unlock, and automatic updates
- Text-message 2-step verification on the business email account (turned on in 2024)
- Bank app approval for every new payee and ACH batch; $30,000 daily ACH limit
- SAM.gov through the government sign-in service, which enforces MFA
- The SaaS vendors host, patch, and back up their own platforms
- Written subcontracts on every job (standard form)
- Old plan sets and bid documents shredded at a community shredding event twice a year

**Missing:**
1. No documented FCI scope, asset inventory, or system security plan. No CMMC Level 1 self-assessment has been performed, and the owner has no SPRS access. Final Level 1 (Self) with an affirmation is required before the DoD subcontract can be awarded (32 CFR 170.15(b)).
2. Bank-detail changes from subcontractors and clients are accepted by email with no call-back to a known number. Clients have never been told how the company will (and will not) change its remittance details. In March 2026 a spoofed email "from" the electrical subcontractor asked for a bank change; it was caught only because the real subcontractor phoned that day about another matter.
3. Email 2-step verification uses text-message codes, which do not resist phishing. The project management and accounting SaaS use passwords only. The email domain has no DKIM or DMARC record, and nobody watches for lookalike domains.
4. The outside bookkeeper signs in to the accounting SaaS with the owner's credentials.
5. The laptop has one login with administrator rights that family members also use.
6. The home office network is shared with family and smart-home devices. Router firmware has never been updated.
7. No documented Section 889 "reasonable inquiry" (FAR 52.204-25(a)). The SAM representations were renewed in January 2026 without one.
8. FCI sits on external systems the owner does not control: jobsite photos sync to a personal consumer cloud account, FC-1 change-order drawings were uploaded to the AI bid assistant while model-improvement use was on, and subcontractors send files through free file-transfer links.
9. Subcontracts on FC-1 do not include the substance of FAR 52.204-21 or 52.204-25, as their flowdown paragraphs require. The portal's default subcontractor role shows each subcontractor the whole project folder, including other subcontractors' pricing.
10. No backup of the laptop (estimates, scanned lien waivers, W-9 forms) and no independent export of SYS-01 project records.
11. No incident plan, no contact list, and no cyber insurance.
12. The owner is a single point of failure. Every second factor is on one phone, and nobody else can pay subcontractors, submit pay apps, or reach the federal portals.
13. The laptop replaced in February 2026 sits in a drawer, not wiped. The previous phone was traded in at a carrier store in 2025 with no wipe record.
14. No security training. In April 2026 a jobsite photo posted to the company's social media page showed an FC-1 floor plan taped to a wall (removed 2026-07-15).
15. Subcontractors' W-9 forms with Social Security numbers are kept as email attachments and in the accounting SaaS.

**Found during the gap analysis (2026-07-16):** the carrier-branded mobile hotspot the owner used to connect the laptop at jobsites, including FC-1, is labeled as produced by a telecommunications manufacturer named in FAR 52.204-25(a). The owner stopped using it that day, switched to phone tethering, reported to the FC-1 Contracting Officer on 2026-07-17 (within one business day, FAR 52.204-25(d)(2)(i)), and filed the 10-business-day follow-up on 2026-07-29 (FAR 52.204-25(d)(2)(ii)).

**Found during P07 testing (2026-07-21):** the home Wi-Fi router still used the manufacturer's default administrator password, with remote administration from the internet turned on. The owner changed the password and turned off remote administration the same day.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P03 regulation | FAR 52.204-21 (15 basic safeguarding requirements, 17 rows), verified through CMMC Level 1 (Self) under 32 CFR Part 170 for the DoD subcontract, plus FAR 52.204-25 (Section 889) as the secondary regulation. DFARS 252.204-7012 is analyzed for applicability only |
| P08 incident | Business email compromise redirecting progress payments (registry default kept, because it is the owner's largest risk): the owner's mailbox is taken over and used to send a private client false remittance instructions for a pay app, with two variants (a spoofed subcontractor bank change and a SAM EFT change) |
| P09 SOC 2 | The company is not a service organization. Security criteria (CC series) only, as the owner's self-check, plus a review of the project management SaaS vendor's SOC 2 Type 2 report |
| P10 AI | AI estimating and bid assistant (registry default kept): one individual subscription the owner uses for takeoff, pricing suggestions, and proposal drafting |
| Cloud | SaaS only. No IaaS. Services are described by category |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-17 | Self-assessment fieldwork: BIA, risk assessment, and gap analysis (IT technician on site 2026-07-15 and 2026-07-16) |
| 2026-07-16 | Section 889 inquiry finds the covered mobile hotspot; use stopped the same day |
| 2026-07-17 | Section 889 report to the FC-1 Contracting Officer |
| 2026-07-20 to 2026-07-22 | Control assessment (tests on 2026-07-21 with the IT technician) |
| 2026-07-29 | Section 889 10-business-day follow-up report |
| 2026-08-24 | AI use assessment (P10) |
| 2026-08-31 | Deliverables adopted by the owner |
| 2026-11-30 | Target date for Final Level 1 (Self) and the SPRS affirmation, ahead of the DoD subcontract award |
