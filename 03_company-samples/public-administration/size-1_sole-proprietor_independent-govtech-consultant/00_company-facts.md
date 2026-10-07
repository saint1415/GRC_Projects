# Scenario facts: Cris Santos Company | Public Administration | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious, and so are its agency clients. This scenario is independent of the other sizes. Where a fact comes from a regulation or policy, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner files Schedule C) |
| Business | Independent GovTech consultant (NAICS 541512, Computer Systems Design Services). Configures, builds reports for, and migrates data into case management systems that Florida local agencies license or run themselves. **Hosts no system for any agency** |
| Location | Florida. Home office in a spare room of the owner's residence (lockable door). On site at client offices about one day a week |
| Workforce | The owner-consultant only (0 employees, no subcontractors). Uses an on-call IT technician by the hour |
| Revenue | About $180,000 a year (fictional), about 1,200 billable hours, or about $720 per working day. SBA-small (standard $34.0 million for NAICS 541512, 13 CFR 121.201) |
| Clients | Three Florida agencies plus small subcontracts (table below). Work is billed by milestone or by the hour |
| Regulatory status | **Private contractor, not a government entity.** Agency rules reach the owner **through contracts**: the FBI CJIS Security Policy through the CJIS Security Addendum in the sheriff's contract (28 CFR 20.33(a)(7)); NIST SP 800-53 Rev. 5 Moderate safeguards through the county contract's clause for contractor devices that store county data. One Florida statute applies directly: Fla. Stat. 501.171, as a "third-party agent" that processes personal information for the county and the city (501.171(1)(h), (2), (6)) |
| Not in scope | Federal tax information (FTI): the owner declined a 2026 subcontract that needed it (section 7). HIPAA: no client has designated the owner a business associate and no PHI is handled. Driver's Privacy Protection Act: no motor vehicle records (section 7). Medicaid and SNAP data: none. Election systems: none. Federal contracts (FAR clauses): none. SLCGP: no grant-funded work. CIRCIA: proposed rule only. GovRAMP: the owner offers no cloud service |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (Fla. Stat. 501.171; Fla. Stat. 282.3185 and 282.3186, which bind the county and city clients, not the owner). Individuals in agency records may live in other states; those are handled generically ("each state where affected individuals reside") |

**Agency clients (fictional)**

| ID | Client | Work | Data the owner can reach | How requirements reach the owner | Share of receipts |
|---|---|---|---|---|---|
| CL-01 | A Florida county (Code Enforcement and Building divisions) | Migration of legacy code enforcement and permit records into the county's new vendor-hosted case management SaaS, plus configuration and reports. Phase 1 (code enforcement) accepted 2026-05-29; phase 2 (permits) runs to 2026-12-18 | Names, addresses, and phone numbers of property owners and complainants; driver license numbers for about 2,100 people in complaint and citation files. Migration extracts of about 38,000 records were worked on the owner's laptop | County contract: contractor devices that store county data must meet NIST SP 800-53 Rev. 5 Moderate safeguards, with MFA and encryption; security incidents reported to the county IT security officer within 24 hours; county data deleted within 30 days after each phase is accepted, with written certification | About 45% |
| CL-02 | A Florida city (about 30,000 residents) | Configuration of the city's 311 constituent request system and, since June 2026, the intake workflow for the city-funded utility bill assistance program for income-qualified residents | Names, addresses, and utility account numbers; for assistance applicants, household size and income documents (pay stubs, benefit letters), some showing Social Security numbers. About 1,200 applications a year | City contract: confidentiality, use of city data only for the project, prompt notice of any unauthorized disclosure, return or destruction at contract end | About 20% |
| CL-03 | A Florida county sheriff's office | Report development for the jail management and pretrial case management system that the sheriff runs in its own data center | Criminal justice information (CJI), including criminal history record information (CHRI): booking records, charges, and criminal history summaries | Contract incorporating the CJIS Security Addendum. The owner signed the certification page and passed state and national fingerprint-based record checks in November 2025. Access only through the sheriff's virtual desktop with a sheriff-issued hardware MFA token | About 25% |
| Subcontracts | GovTech integrators (prime contractors) | Training materials and user documentation for agency projects | None (no agency data access) | Subcontract confidentiality terms | About 10% |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-consultant | Every role: owner, security officer, privacy contact named in client contracts, incident handler, and risk acceptor |
| On-call IT technician (local IT services shop) | Hourly help with the laptop, home network, and data recovery. No standing access; remote sessions are started by the owner. Signed a nondisclosure agreement on 2026-08-07 |
| Cyber insurer (endorsement on the professional liability policy) | Breach hotline and panel breach counsel; $100,000 cyber sublimit |
| Agency security contacts (client roles) | CL-01 county IT security officer; CL-02 city IT director and the utility assistance program manager; CL-03 sheriff's local agency security officer (LASO) |

## 3. Systems
| ID | System | Hosting | Holds agency data? | Notes |
|---|---|---|---|---|
| SYS-01 | Business laptop | Owner device | Yes (county extracts, city exports, scripts) | The only work computer. Built-in full-disk encryption on; built-in antivirus; automatic updates. **The owner signs in daily with a local administrator account** |
| SYS-02 | Productivity suite, business plan (email, calendar, cloud file storage with a sync folder, video meetings) | SaaS | Yes (project files, email attachments) | MFA on (authenticator app). File version history and recycle bin kept by the vendor for a limited period |
| SYS-03 | Mobile phone | Owner's personal phone | Incidental (business email) | Passcode and biometric unlock; encrypted. Holds the authenticator app for every MFA prompt except the sheriff's token. **No recovery codes stored anywhere** |
| SYS-04 | Password manager (individual plan) | SaaS | No (credentials only) | MFA on. Holds most passwords |
| SYS-05 | Agency accounts used by the owner (outside the boundary) | Agency systems | Yes | CL-01: county single sign-on into its case management SaaS and secure file transfer (county MFA). CL-02: local accounts in the city's 311 system (**password only**; the city offers no MFA to contractors). CL-03: sheriff's virtual desktop (sheriff-issued hardware token) |
| SYS-06 | Home office network | ISP-supplied router | In transit | **Default router admin password; firmware never updated; one Wi-Fi network shared with family devices** |
| SYS-07 | Business administration SaaS: accounting and invoicing; brochure website on a hosted site builder | SaaS | No | MFA on the accounting service. The website holds no client data |
| SYS-08 | General-purpose generative AI assistant (individual paid plan) | SaaS | Yes, from July 2026 (see P10) | Used for code, report logic, and document drafts. **Used with real city applicant data in a July 2026 proof of concept** |
| SYS-09 | External USB backup drive | Owner device | Yes (full copy of laptop files, including county extracts) | **Unencrypted.** Manual monthly backups; last backup 2026-05-30. Kept in the home office desk drawer |

**SSP system (P02):** the *Consulting Delivery Environment (CDE)*: SYS-01 to SYS-04 and SYS-06 to SYS-09, plus the owner's use of the agency accounts in SYS-05 (the agency systems themselves are outside the boundary).

## 4. Current security posture: informal, basic hygiene with big gaps
**In place today:**
- MFA on the productivity suite, password manager, and accounting service, and on every agency account that offers it (county single sign-on, sheriff hardware token)
- Built-in full-disk encryption on the laptop; the phone is encrypted by its passcode
- Automatic operating system and application updates; built-in antivirus with real-time protection
- A password manager with unique passwords for most accounts
- For CJIS work: state and national fingerprint-based record checks and a signed CJIS Security Addendum certification page (November 2025); CJIS security awareness training through the sheriff's online program (completed 2025-11-18)
- Signed contracts with security terms for all three agency clients
- Professional liability insurance with a cyber endorsement and a breach hotline
- Agency data is moved only through each agency's secure file transfer or the owner's business cloud storage, never by personal email (habit, not written)

**Missing:**
1. No risk assessment, no written security policy, and no record of where agency data is kept.
2. County extracts (about 38,000 records; driver license numbers for about 2,100 people) are still on the laptop, in the cloud sync folder, and on the USB drive, although phase 1 was accepted on 2026-05-29. The county contract required deletion and written certification within 30 days (by 2026-06-28). **Overdue.**
3. The USB backup drive is unencrypted and backups are manual (last 2026-05-30). Project scripts sit in a local repository with no other copy.
4. The owner uses a local administrator account for daily work on the laptop.
5. Home router: default admin password, old firmware, and one flat network shared with family devices.
6. City 311 system: contractor accounts are password only (no MFA option), and the owner's account from a 2024 city project was never disabled.
7. No incident response plan. The agency reporting clocks are not written down anywhere (sheriff: 1 hour; county: 24 hours; city: prompt notice; Fla. Stat. 501.171(6)(a): 10 days).
8. The generative AI assistant was used with real city applicant data (25 applications) in a July 2026 proof of concept. The setting that lets the provider use conversations to improve its models was on, and the city contract does not approve any AI service.
9. No security training beyond the sheriff's CJIS awareness course; the CJIS annual refresher is due by 2026-11-18.
10. Single-person dependency: only the owner can do the work, reach the agencies, or meet the 1-hour CJIS reporting rule. Every MFA prompt except the sheriff's goes to one phone, and no backup arrangement exists.
11. No review of the SaaS providers' security or data-use terms (data location for cloud storage; AI assistant data use).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Primary system | The registry default ("case management system hosted for state and local agencies") does not fit a one-person consultancy that hosts nothing. The SSP covers the owner's **Consulting Delivery Environment**, the devices and SaaS accounts used to reach agency case management systems. The agency systems stay outside the boundary |
| P03 regulation | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline, reached through the county contract, scoped to what the owner controls, with a CJIS Security Policy v6.1 overlay for the sheriff work and two Fla. Stat. 501.171 rows |
| P08 incident | Ransomware on the business laptop (SYS-01) with theft of county extracts, and a risk that the attacker reaches the sheriff's CJI system or the county SaaS through the owner's saved sessions and credentials. Adapted from the registry default ("ransomware affecting agency systems holding CJI and FTI"): the owner holds no FTI, so the FTI clock is listed as not applicable, and the agency systems are at risk through the owner's access rather than hosted by the owner |
| P09 SOC 2 | Security criteria only, as a self-check. The owner is a service provider but runs no system for clients, so no agency asks for a SOC 2 report; agencies use security questionnaires, the CJIS Security Addendum, and the county's annual contractor attestation. Includes a review of the productivity suite provider's SOC 2 report, because that service holds agency files |
| P10 AI | The generative AI assistant (SYS-08) the owner used to pre-screen city utility bill assistance applications for eligibility (AI-001), plus its use for code and drafting with no agency data (AI-002). Adapted from the registry default ("AI eligibility determination for public benefits"): at this size the owner builds no eligibility system; the risk is one third-party tool used on a local benefits program |
| Cloud | SaaS only. No IaaS or PaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-08-10 to 2026-08-14 | Self-assessment (BIA, system profile, SaaS mapping, risk register, gap analysis), with the on-call IT technician under NDA |
| 2026-08-24 to 2026-08-26 | Control tests (P07), with the on-call IT technician |
| 2026-09-15 | Deliverables adopted by the owner-consultant |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Declined FTI work | In March 2026 a GovTech integrator offered a subcontract to test data migration for a state revenue agency. The work needed access to federal tax information, which would have required Pub. 1075 Exhibit 7 contract terms, a 45-day IRS notification by the agency, and a background investigation. The owner declined it | P03, P08 |
| Driver license numbers | The driver license numbers in county complaint and citation files were written down by code officers from residents' own documents, not obtained from state motor vehicle records, so the Driver's Privacy Protection Act does not reach them (the county confirmed this in its data inventory) | P03 |
| AI proof of concept | From 2026-07-27 to 2026-07-31, at the city program manager's verbal request, the owner uploaded 25 real utility bill assistance applications (with income documents; 6 pay stubs showed full Social Security numbers) to the generative AI assistant and asked it to sort them into likely eligible, likely ineligible, or missing documents. The owner recognized the problem during the gap analysis on 2026-08-12, turned off the model-improvement setting, deleted the conversations, and told the city IT director by phone and in writing on 2026-08-13 (within the 10 days of Fla. Stat. 501.171(6)(a)). The city's attorney is deciding whether notice to the 6 residents is required. No eligibility decision used the AI output | P01, P03, P08, P10 |
| CJI found outside the virtual desktop | P07 testing on 2026-08-25 at 10:40 found a spreadsheet with CHRI fields (names, dates of birth, booking numbers, charges) for 140 people on the laptop and in the cloud sync folder. The owner had copied report test output out of the sheriff's virtual desktop on 2026-05-14, which the desktop's clipboard and drive mapping allowed. The owner reported it to the sheriff's LASO at 11:15 the same day, deleted the file from the laptop, the sync folder, and the cloud recycle bin, and confirmed the USB drive did not hold it (the backup job copies only the documents folder, and the file sat in the downloads and sync folders). The sheriff disabled clipboard and drive mapping for contractor desktops on 2026-08-26. The LASO accepted deletion with full-disk encryption as the remediation on 2026-08-27 and handles any report to the CJIS Systems Officer. The fields are not "personal information" under Fla. Stat. 501.171(1)(g) (no Social Security, driver license, or financial account numbers) | P01, P03, P07, P08 |
| Stale city account | The owner's 311 account from a 2024 city project was still enabled on 2026-08-24 (P07). The owner asked the city IT director in writing on 2026-08-24 to disable it and to offer MFA for contractor accounts | P01, P03, P04, P07 |
| Laptop and backup details | The laptop is three years old, bought from the manufacturer's online store. The owner has no spare computer. The USB backup job copies the documents folder only, not the scripts repository or the downloads folder | P05, P07, P08 |
| Cyber endorsement | The cyber endorsement has a $100,000 sublimit and requires a call to the breach hotline before hiring any response vendor | P08 |
| Productivity suite assurance | The productivity suite provider publishes a SOC 2 Type 2 report (Security, Availability, and Confidentiality) to business customers under its trust portal terms. The owner reviewed it on 2026-08-13 | P02, P09 |
| Agency response times | The county contract requires notice of a security incident within 24 hours of discovery; the sheriff's contract applies the CJIS 1-hour rule to the owner; the city contract says "promptly" with no number of hours | P03, P06, P08 |
| Home office | Paper printouts of county reports are kept in a locked file box and shredded with a cross-cut home shredder. No CJI is ever printed | P02, P03 |
| CJIS refresher date | Because the owner was involved in the 2026-08-25 CJI incident, CJISSECPOL v6.1 AT-2 a.2 requires the refresher within 30 days, by 2026-09-24, ahead of the annual date (2026-11-18) in section 4 | P02, P03, P06, P07, P08, P09 |
| Device settings | The laptop locks after 10 minutes idle and the phone after 1 minute. Phone remote locate and erase was turned on 2026-08-12. The laptop's disk recovery key was stored in the productivity suite account (moving to the sealed envelope). Six old browser extensions and several unused applications were found on 2026-08-11 | P02, P03, P04 |
| Website builder MFA | The website builder account offers MFA, but it was off (found in P04 mapping on 2026-08-12, confirmed in P07) | P02, P04, P07 |
| Backup restore test | A test restore of one project folder from the USB drive on 2026-08-26 found 14 files that would not open | P07, P09 |
| Incident log | The owner started an incident log on 2026-08-13 (AI proof of concept); the 2026-08-25 CJI finding is its second entry | P03 |
| AI proof of concept results | Comparing the AI labels with the city's own decisions on the same 25 applications: 19 agreed; 4 eligible households were labeled likely ineligible, 3 of them with handwritten benefit letters or Spanish-language pay stubs. The owner sent the provider a written deletion request (reply due by 2026-09-30) and will pay any resident notice costs the city asks for | P10 |
| Business figures | About $15,000 is invoiced a month; personal savings cover about two months of expenses. County phase 2 load windows are booked weekends with the county and its vendor. The sheriff's IT unit takes about one business day to register a new device for the virtual desktop. The security budget is about $300 a year | P01, P05, P08 |
| Productivity suite report details | The SOC 2 Type 2 report covers a 12-month period ending 2026-03-31 with an unqualified opinion and no exceptions; a bridge letter was requested on 2026-08-13 | P09 |
