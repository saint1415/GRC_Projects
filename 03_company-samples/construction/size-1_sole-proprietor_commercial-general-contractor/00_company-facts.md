# Scenario facts: Cris Santos Company | Construction | Sole Proprietorship

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship operating under the owner's trade name; the owner files Schedule C) |
| Business | Commercial and institutional building general contractor (NAICS 236220). Small renovations and tenant build-outs: offices, a dental suite, a church fellowship hall, and one federal clinic renovation. The owner estimates, manages, and supervises every job and **subcontracts all trade work** |
| Location | Florida. A **home office** in the owner's residence, a rented **self-storage unit** for tools and materials, one pickup truck, and 2 to 4 active jobsites at a time (no jobsite trailers) |
| Workforce | The owner only (0 employees). Uses contracted services and trade subcontractors instead of staff |
| Revenue | About $180,000 in annual receipts (fictional; EV-006). Under the SBA standard of $45.0 million for NAICS 236220 (13 CFR 121.201), so SBA-small |
| Billing and payments | Monthly progress payment applications (pay apps) with a schedule of values on larger jobs, invoices on small ones, about $15,000 billed in a typical month. Private clients pay by ACH or check. The federal agency pays by electronic funds transfer to the bank account in the company's SAM registration (FAR 52.232-33(b)). The owner pays about 14 trade subcontractors and 6 suppliers a year by ACH from the bank portal or by check. On the federal job the owner must pay subcontractors within 7 days of receiving payment (FAR 52.232-27(c)(1)) (EV-005, EV-012) |
| Federal work (about 35% of 2026 receipts) | **FC-1:** a firm-fixed-price contract with the Department of Veterans Affairs (civilian agency) to renovate a staff break room and two offices at a community-based outpatient clinic in Florida, about $68,000, awarded 2026-03-09 under a small business set-aside, performance through 2026-11. It includes FAR 52.204-21, 52.204-23, 52.204-25, 52.222-8, 52.232-27, and 52.232-33. Construction wage rate requirements apply, so the owner collects and submits subcontractors' weekly certified payrolls (FAR 52.222-8(b)(1)) (EV-012) |
| Federal pipeline | A larger prime contractor has asked the owner to perform interior renovation work (about $45,000) under the prime's **DoD task order** at an Army Reserve Center in Florida, expected to be awarded 2026-12. The prime's task order includes DFARS 252.204-7021 at **CMMC Level 1 (Self)**, and the prime will require the owner to hold a current Final Level 1 (Self) status with an affirmation in SPRS **before the subcontract is awarded** (32 CFR 170.23(a)(1); DFARS 252.204-7021(d)(4) and (f)(2)). No CUI is expected (EV-013) |
| Private work (about 65%) | A dental office tenant build-out (about $52,000), a church fellowship hall renovation (about $35,000), and small retail repairs |
| Insurance | General liability and tool coverage only. **No cyber insurance and no funds transfer fraud or social engineering coverage** (EV-025; confirmed with the insurance agent on 2026-07-14, EV-031) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): CUI, NIST SP 800-171, and DFARS 252.204-7012 (no DoD contract today and no CUI expected; see P03). HIPAA (the dental office build-out gives the owner no patient information). PCI DSS (no card payments). SEC rules (not a public company) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171, which covers sole proprietorships). The samples otherwise stay federal |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People and contracted services (role titles only)

| Role | Duties |
|---|---|
| Owner | Every role: business owner, estimator, project manager, superintendent, billing and payables, **security lead**, risk acceptor, incident commander, SAM Entity Administrator, and designated **CMMC Affirming Official** (32 CFR 170.22(a)(1)) |
| Outside bookkeeper | Independent contractor, about 6 hours a month: reconciles the bank and accounting records, prepares 1099s. **Signs in to the accounting SaaS with the owner's own username and password** (no separate account; EV-004). Engagement letter has no security or confidentiality terms (EV-026) |
| On-call IT technician | Independent local technician, paid by the hour. Set up the laptop and home router. No standing remote access. Helped with the July 2026 self-assessment under a short written engagement with a confidentiality clause (signed 2026-07-13) |
| Tax preparer | CPA firm; prepares the annual return from the accounting SaaS export |
| Insurance agent | General liability and tools. No cyber product placed |
| Trade subcontractors | About 14 used in 2026 (electrical, plumbing, HVAC, drywall, painting, flooring, doors and hardware). 8 are themselves sole proprietors and gave the owner W-9 forms with their Social Security numbers (EV-004, EV-009). 6 are working on FC-1 and receive VA drawings through the project management portal (EV-001, EV-011) |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds FCI? | Notes |
|---|---|---|---|---|
| SYS-01 | Construction project management and pay application SaaS (small-contractor plan): drawings, RFIs, submittals, daily logs, photos, schedule of values, pay apps, and a portal for subcontractors and client representatives | Vendor SaaS | Yes (FC-1 drawings, submittals, daily logs, pay apps) | System of record for every job. Owner is the only administrator. 23 external portal users, 9 of them from jobs closed in 2025. MFA available but **off** (EV-001, EV-002, EV-035). Vendor has a SOC 2 Type 2 report (EV-003; reviewed in P09) |
| SYS-02 | Accounting SaaS (small business plan) | Vendor SaaS | No (simple transactional information only) | Invoices, bills, vendor records with bank details, ACH bill pay, bank feed, 1099 tracking with W-9 files attached. **One login, shared with the outside bookkeeper**; password only (EV-004) |
| SYS-03 | Business email and file storage (small business productivity plan, 1 licensed user, company domain) | SaaS | Yes | Channel for pay apps, lien waivers, subcontractor invoices, and payment correspondence. 2-step verification by **text message code**. The domain publishes SPF only (no DKIM or DMARC) (EV-007, EV-008) |
| SYS-04 | Laptop (owner-owned) | Home office and field | Yes | Built-in full-disk encryption **on** (default at purchase). Built-in antivirus and automatic updates on. **One login with administrator rights, also used by family members** (EV-018) |
| SYS-05 | Smartphone (owner's personal phone used for business) | Field | Yes (email, jobsite photos) | Passcode and biometric unlock; encrypted by default. Holds the email text codes, the bank app, and the authenticator for the government sign-in service. Jobsite photos sync to the owner's **personal consumer cloud photo account** (EV-019) |
| SYS-06 | Home office network: internet service provider gateway plus an owner-bought Wi-Fi router | Home office | Yes (in transit) | Shared with family phones, a game console, a smart TV, and doorbell camera. Router firmware never updated (EV-020). A carrier-branded mobile hotspot was used at jobsites until 2026-07-16 (EV-017, EV-039) |
| SYS-07 | Business online banking (ACH, wires, mobile deposit) | Bank-hosted | No | Single user (the owner). The bank requires app approval for each new payee and each ACH batch, with a $30,000 daily ACH limit. No positive pay (EV-015) |
| SYS-08 | Federal portals: SAM.gov (entity registration with EFT bank information), the federal invoicing portal used for FC-1, and SPRS (no access yet) | Government-operated | n/a | Company accounts only. The government sign-in service enforces MFA. The owner is the SAM Entity Administrator (EV-014) |
| SYS-09 | AI estimating and bid assistant (individual subscription) | Vendor SaaS | Yes (uploaded FC-1 change-order drawings) | Takeoff from uploaded drawings, pricing suggestions, and proposal drafting. Used since 2026-03. "Use my content to improve the service" was on until 2026-07-17 (EV-021; see P10) |

Paper: current plan sets ride in the truck; signed subcontracts, lien waivers, and certified payroll copies sit in a file cabinet in the home office (EV-037).

**SSP system (P02):** the *Project Management and Payment Application System (PMPAS)*: SYS-01 to SYS-06, and their interfaces to SYS-07, SYS-08, and SYS-09. The PMPAS boundary is also the proposed CMMC Level 1 assessment scope (32 CFR 170.19(b)).

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. For a one-person general contractor the sources are the vendors' admin consoles, SAM.gov, bank and card statements, the inbox, the signed agreements file cabinet, the device settings screens, the router app, and the carrier and insurance agent portals.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against FAR 52.204-21, CMMC Level 1 and FAR 52.204-25** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

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
| 2026-07-06 to 2026-07-10 | Intake: the owner collects SaaS and banking settings and reports, SAM records, statements, contracts and agreements, device and router settings, the AI tool account and terms, and insurance records; inventories; obligations register. The insurance agent's answer arrived 2026-07-14 |
| 2026-07-13 to 2026-07-17 | Self-assessment fieldwork: BIA, risk assessment, and gap analysis (IT technician on site 2026-07-15 and 2026-07-16) |
| 2026-07-16 | Section 889 inquiry finds the covered mobile hotspot; use stopped the same day |
| 2026-07-17 | Section 889 report to the FC-1 Contracting Officer |
| 2026-07-17 | POL-01 draft rules written from the gap analysis, before the control tests; reviewed as drafts for design only in P07 |
| 2026-07-20 to 2026-07-22 | Control assessment (tests on 2026-07-21 with the IT technician) |
| 2026-07-23 to 2026-08-28 | POL-01 completed from the gaps and the test results |
| 2026-07-29 | Section 889 10-business-day follow-up report |
| 2026-08-24 | AI use assessment (P10) |
| 2026-08-31 | Deliverables and POL-01 adopted by the owner (POL-01 effective 2026-09-01) |
| 2026-11-30 | Target date for Final Level 1 (Self) and the SPRS affirmation, ahead of the DoD subcontract award |
| 2027-01 (planned) | Follow-up check: operating effectiveness of the controls POL-01 introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Accounting password history | The shared accounting password dates from 2023. A previous bookkeeper, whose engagement ended in 2024, also knew it; it was never changed (EV-004, EV-026) | P07, P09 |
| Company website | The website runs on a website-builder SaaS, holds no FCI, and has no connection to the home network or the SaaS tenants, so FAR 52.204-21(b)(1)(xi) is not applicable (EV-024) | P02, P03, P07 |
| Household devices | A game console, a smart TV, and a doorbell camera share the home network. The doorbell camera is household equipment and is not used for company work (EV-020, EV-037) | P03, P07 |
| Keys and codes | A spare storage-unit padlock key lent to a subcontractor in 2025 was never returned. Jobsite lockbox codes were reused across jobs (EV-034, EV-037) | P03 |
| Project management vendor assurance | The vendor's SOC 2 Type 2 report (Security and Availability, 12 months ending 2026-03-31, unqualified, no exceptions) and a bridge letter through 2026-06-30 were reviewed by the owner on 2026-07-16 (report and letter: EV-003) | P02, P04, P09 |
| AI tool use | The AI bid assistant has been used for about 20 bids and change orders since March 2026. FC-1 change-order drawings were uploaded in June 2026. A back-test on 3 completed jobs was run for P10 (EV-021, EV-043) | P10 |
| FC-1 submittals | FC-1 submittals (exhaust fans, lighting, door hardware, finishes) include no telecommunications, camera, or network equipment. The DoD subcontract scope includes a wireless door-access upgrade (EV-040, EV-013) | P03 |
| Covered hotspot | The Section 889 inquiry during the gap analysis (2026-07-16) found that the carrier-branded mobile hotspot the owner used to connect the laptop at jobsites, including FC-1, is labeled as produced by a telecommunications manufacturer named in FAR 52.204-25(a). The owner stopped using it that day, switched to phone tethering, reported to the FC-1 Contracting Officer on 2026-07-17 (within one business day, FAR 52.204-25(d)(2)(i)), and filed the 10-business-day follow-up on 2026-07-29 (FAR 52.204-25(d)(2)(ii)) (EV-039, EV-041, EV-042) | P01, P02, P03, P07, P08 |
| Router default password | P07 testing on 2026-07-21 found the home Wi-Fi router still used the manufacturer's default administrator password, with remote administration from the internet turned on. The owner changed the password and turned off remote administration the same day (EV-IA-5, EV-SC-7) | P01, P03, P07 |
