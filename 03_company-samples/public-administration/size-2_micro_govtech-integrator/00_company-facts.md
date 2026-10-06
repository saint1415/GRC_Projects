# Scenario facts: Cris Santos Company | Public Administration | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious, and so are its agency customers and its prime contractor. This scenario is independent of the other sizes. Where a fact comes from a regulation, policy, or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (a privately held GovTech systems integrator; not a government entity) |
| Business | GovTech systems integrator (NAICS 541512, Computer Systems Design Services). It configures, hosts, and supports case management applications for Florida local agencies on a government-community low-code case management platform that it licenses from a platform vendor (about 65% of receipts), builds and runs the data interfaces that feed those applications (about 20%), and provides one integration consultant to a prime integrator on a state revenue agency project (about 15%) |
| Location | Florida. One small leased **office suite** (6 desks, locked network closet) and hybrid work from staff homes in Florida. All work, including all support and administration of agency data, is performed in the United States |
| Workforce | 7 employees: the owner (managing member and principal architect), an Operations Manager, a Lead Platform Engineer, 2 Platform Developers, an Integration Consultant, and an Implementation and Support Analyst (hired April 2026) |
| Revenue | About $1.1 million a year (fictional), about $4,400 per business day. SBA-small (standard $34.0 million for NAICS 541512, 13 CFR 121.201) |
| Customers | 4 Florida local agency customers that use hosted applications, plus 1 subcontract (table below). About 38,000 people have records in the hosted applications |
| Regulatory status | **Private contractor, not a government entity.** Agency rules reach the company **through contracts**: the FBI CJIS Security Policy through the CJIS Security Addendum in the sheriff's contract (28 CFR 20.33(a)(7)); NIST SP 800-53 Rev. 5 Moderate through the county and city contracts; IRS Publication 1075 through the Exhibit 7 safeguarding language the prime contractor flowed down unchanged (Pub. 1075 Exhibit 7, I(9)-(11)). Two Florida statutes apply directly: Fla. Stat. 501.171, as a "third-party agent" (501.171(1)(h), (2), (6)), and Fla. Stat. 119.0701, as a contractor acting on behalf of public agencies (public records duties written into each contract) |
| Not in scope | HIPAA: no customer has designated the company a business associate, and the county assistance program is not a health plan or health care provider. Medicaid and SNAP rules (42 CFR 431.300-431.307; 7 CFR 272.1(c)): the county program in AC-02 is county-funded and is not SNAP, TANF, or Medicaid. Driver's Privacy Protection Act: no data from motor vehicle records (driver license numbers in city complaint files come from the complainants). Election systems: none. Federal contracts (FAR 52.204-21, 52.204-25): none. SLCGP: no grant funds pay for the company's services. CIRCIA: proposed rule only. Rule 60GG-2, F.A.C.: binds state agencies; the revenue agency applies it to the prime, and the company's subcontract carries only the Pub. 1075 terms |
| State law approach | Florida law is cited where a Florida duty is unavoidable (Fla. Stat. 501.171 and 119.0701 directly; Fla. Stat. 282.3185, 282.3186, and 282.318, which bind the customers). Individuals in agency records may live in other states; those are handled generically ("each state where affected individuals reside") |

**Agency customers and the subcontract (fictional)**

| ID | Customer | Use of the company's services | Regulated data | How requirements reach the company | Share of receipts |
|---|---|---|---|---|---|
| AC-01 | A Florida county sheriff's office (pretrial services unit) | Hosted pretrial supervision application, in production since 2024, used by about 30 pretrial officers and staff. A nightly file of new bookings and criminal history summaries arrives from the sheriff's jail management system through the integration server (SYS-02) | **Criminal justice information (CJI)**, including criminal history record information (CHRI). About 4,800 supervision case records | Contract incorporating the CJIS Security Addendum (28 CFR 20.33(a)(7)); CJIS Security Policy v6.1 (06/25/2026); recovery time 24 hours and recovery point 4 hours; 99.5% monthly availability | About 30% |
| AC-02 | A Florida county human services department | Hosted application for the county-funded Emergency Assistance Program (one-time rent and utility payments for residents in crisis), in production since 2024, used by 9 county caseworkers. The AI pre-screening pilot (SYS-09) runs here | Applicant and household data, Social Security numbers, income documents, landlord and utility account details. About 7,500 applicant households | Contract requiring the hosted service to meet the NIST SP 800-53 Rev. 5 Moderate baseline; county program rule that a complete application receives a decision within 5 business days; recovery time 24 hours and recovery point 4 hours | About 22% |
| AC-03 | A Florida city (about 60,000 residents) | Hosted code enforcement and constituent request application, in production since 2025 | Names, addresses, phone numbers, some driver license numbers supplied by complainants. About 18,000 records | Contract modeled on the county contract (SP 800-53 Moderate by reference); recovery time 72 hours and recovery point 24 hours | About 8% |
| AC-04 | A second Florida city (about 22,000 residents) | Same application as AC-03, in production since 2025 | Same data types. About 8,000 records | Same as AC-03 | About 5% |
| SC-01 | A prime integrator's contract with a Florida state revenue agency (tax system modernization) | The Integration Consultant validates data conversion inside the agency's virtual desktop (SYS-10), with the Lead Platform Engineer as named backup. Runs through 2027-06-30 | **Federal tax information (FTI)**, visible only inside the agency's virtual desktop. No company system is authorized to store FTI | Subcontract carrying Pub. 1075 Exhibit 7 language unchanged; IRS approval of the subcontract obtained through the agency's notification to the IRS Office of Safeguards, which names the company (Exhibit 7, I(8); sec. 2.E.6); agency background investigations for both named staff (sec. 2.C.3); agency CISO approval of the specific company laptops that connect (Pub. 1075 sec. 4, AC-20 IRS-defined requirement) | About 15% |

Implementation and integration project work for these customers makes up the remaining receipts (about 20%, counted in the shares above for the customer each project serves).

## 2. People and contracted services (role titles only)
| Role | Security and compliance duties |
|---|---|
| Owner (managing member and principal architect) | Accepts risk; approves policies, spending, and agency security attestations; signs contracts. Also holds a platform administrator account (overlap noted in P02) |
| Operations Manager | Designated **Security and Compliance Officer** in writing on 2026-07-20 (part time, alongside finance, HR, and contracts). Maintains the risk register, policies, and SSP; tracks every agency security term; sends notices to agencies and the prime; manages screening paperwork with AC-01 and the prime |
| Lead Platform Engineer | Technical security lead. Administers the platform tenant (SYS-01) and the integration server (SYS-02); named FTI backup on SC-01 |
| Platform Developers (2) | Configure the agency applications in the developer sandbox and promote changes to production |
| Integration Consultant | SC-01 FTI work inside the agency virtual desktop; builds and maintains interface scripts |
| Implementation and Support Analyst | Agency user support (helpdesk), training, and data migration support |
| Managed service provider (MSP) | Laptops (patching, antivirus, encryption, remote management), productivity suite administration, office firewall and Wi-Fi, and suite backup. Monthly fixed-fee contract with a 4-business-hour response time |
| Platform vendor | Operates the low-code case management platform (SaaS/PaaS) that hosts SYS-01 and the AI add-on used by SYS-09 |
| Cyber insurer | Cyber liability policy ($1 million limit) with a 24x7 breach hotline and panel breach counsel and forensics |
| Agency and prime contacts (customer roles) | AC-01 local agency security officer (LASO); AC-02 department IT security liaison and program manager; AC-03 and AC-04 city IT managers; SC-01 prime's security officer and the revenue agency's disclosure officer |

## 3. Systems
| ID | System | Hosting | Holds agency data? | Notes |
|---|---|---|---|---|
| SYS-01 | Hosted Case Management tenant (4 agency workspaces plus a developer sandbox) | Platform vendor SaaS/PaaS (government-community cloud, U.S. regions) | Yes (CJI, assistance applicant data, constituent data) | The platform is FedRAMP Moderate authorized and listed as GovRAMP verified (both checked on the public listings in June 2026). The company configures applications, roles, workflows, and integrations; the vendor runs everything below the application. AC-01 users federate with the sheriff's identity provider (sheriff-enforced MFA). AC-02, AC-03, and AC-04 users have platform-local accounts; MFA is on for AC-02 and AC-03 but **not for AC-04** |
| SYS-02 | Integration server and export storage (the company's single cloud workload) | Government-community IaaS region: one Linux virtual machine and one object storage bucket | Yes (CHRI files in transit and in a working folder; nightly exports of all 4 workspaces) | Pulls the sheriff's nightly file from the sheriff's secure file transfer drop, transforms it, and loads it through the platform API. Also exports all 4 workspaces each night to the bucket (30 days kept). Administered over SSH with keys held by the Lead Platform Engineer and the owner |
| SYS-03 | Productivity suite (email, files, chat, video) | SaaS | Incidental (implementation files, email attachments) | Business plan; MFA by authenticator push for all staff. Its identity service also signs staff in to SYS-04 and SYS-05. MSP-administered |
| SYS-04 | Helpdesk and ticketing | SaaS | Yes (screenshots attached by agency users) | Agency users open tickets by email. Sheriff users sometimes attach screenshots showing CJI |
| SYS-05 | Source code repository | SaaS | No (scripts and exported application configuration) | Holds the SYS-02 interface scripts and exported platform configurations |
| SYS-06 | Laptops (8: 7 assigned, 1 spare) | Company-owned, MSP-managed | Cached (downloads, email attachments, SSH keys) | Built-in full-disk encryption, next-generation antivirus, monthly patching, and the MSP's remote management agent |
| SYS-07 | Office network | On-premises | In transit only | Small-business firewall, staff Wi-Fi, separate guest Wi-Fi. No servers in the office |
| SYS-08 | MSP remote monitoring and management platform | MSP-operated SaaS (external) | No, but it can run commands on every laptop | Outside the company's control; covered by the MSP contract |
| SYS-09 | AI eligibility pre-screening (pilot) | Platform vendor's generative AI add-on, configured in the AC-02 workspace | Yes (AC-02 applicant documents and data) | Pilot since 2026-06-01 for 6 of the 9 AC-02 caseworkers (see P10) |
| SYS-10 | Revenue agency virtual desktop (SC-01) | Agency-operated (external) | Yes (FTI, inside the agency environment only) | Reached from 2 company laptops with agency-issued accounts and agency MFA. Clipboard and file transfer to the laptop are blocked by agency policy, except text paste into the session |

The platform vendor and the IaaS provider are described by service category only (vendor-agnostic).

**SSP system (P02):** the *Hosted Case Management Service (HCMS)*: SYS-01, SYS-02, and SYS-09, with the services and devices that administer and support them (SYS-03 identity, SYS-04, SYS-05, and the administrator laptops in SYS-06). SYS-08 and SYS-10 are external systems outside the boundary.

## 4. Current security posture: early to partial
**In place today:**
- MFA for every workforce account in the productivity suite (authenticator push) and the platform (authenticator app codes)
- A FedRAMP Moderate authorized platform in U.S. regions, with vendor-managed encryption at rest and in transit, vendor backups, and vendor patching of the platform
- Sheriff users sign in through the sheriff's identity provider with sheriff-enforced MFA
- MSP-managed laptops with full-disk encryption, next-generation antivirus, monthly patching, and remote management
- State and national fingerprint-based record checks and signed CJIS Security Addendum certification pages for 4 staff (owner, Lead Platform Engineer, 2 Platform Developers), held by AC-01; CJIS security awareness training through the sheriff's online program for the same 4
- Agency background investigations for the 2 SC-01 staff, and the revenue agency's disclosure awareness training and signed confidentiality statement for the Integration Consultant (current)
- Office firewall with guest Wi-Fi separated from staff Wi-Fi
- Signed contracts with security terms for every customer and for SC-01
- Cyber liability insurance with a breach hotline and panel vendors

**Missing or weak, found in the 2026 assessments:**
1. No risk assessment, no SSP, and no written security policies. Security was described only in 2024 proposal answers.
2. 5 staff can reach CJI in the AC-01 workspace, but only 4 have fingerprint-based checks and signed Security Addendum certifications. The Implementation and Support Analyst (hired April 2026) holds the platform support role, which can read every workspace.
3. Platform audit logs are kept 90 days (platform default) and integration server logs 14 days. Nobody reviews them. The CJIS Security Policy requires at least 1 year (AU-11).
4. Company-side backups are a nightly export to a bucket in the same cloud account as the integration server, not immutable, and never restore-tested. The platform vendor restores a whole tenant on request within 48 hours (vendor service description). The 24-hour recovery time and 4-hour recovery point in the AC-01 and AC-02 contracts are unproven for an attacker or administrator deletion.
5. No incident response plan, and the agency clocks are not written down: 1 hour for suspected CJI incidents (CJIS IR-6), immediate notice to the prime and the revenue agency so the agency can report to TIGTA and the IRS Office of Safeguards within 24 hours (Pub. 1075 sec. 1.8), 12-hour ransomware reports by Florida counties and cities (Fla. Stat. 282.3185(5)), and 10 days under Fla. Stat. 501.171(6)(a).
6. The integration server is administered with SSH keys only (no MFA). Its operating system patches are applied by hand and were 3 months behind. Each nightly CHRI file stays 30 days in a working folder protected only by the provider's default disk encryption.
7. The SFTP connection that pulls the sheriff's file uses the server's default cryptographic library, and no one has confirmed it runs a FIPS 140-3 certified module. The CJIS Security Policy stops accepting FIPS 140-2 certificates after 2026-09-21 (SC-13).
8. AC-04 platform-local accounts sign in with a password only; MFA is available but was never enabled for that workspace.
9. FTI spillage: on 2026-07-29 the data inventory found a defect log in the shared drive with 14 taxpayer identification numbers typed in from the agency virtual desktop in May 2026 (see section 7).
10. The Lead Platform Engineer's annual FTI recertification has been overdue since June 2026, and in June the engineer connected twice to the agency virtual desktop from a laptop that is not on the agency CISO's approved device list.
11. Sheriff users attach screenshots showing CJI to helpdesk tickets (SYS-04). The helpdesk vendor was never reviewed and has no CJIS Security Addendum.
12. MSP technicians can run commands on laptops that cache CJI and hold the SSH keys to SYS-02, but they have no fingerprint-based checks, and the MSP contract has no security incident notice term.
13. The AI pre-screening pilot started on 2026-06-01 without an AI risk assessment, bias testing, a written human-review rule, or notice to applicants, and the add-on's place inside or outside the platform's FedRAMP authorization was not checked (see P10).
14. No vendor reviews of any kind: the platform vendor's FedRAMP package and SOC 2 report, the helpdesk vendor, the MSP, and the AI add-on.
15. No security awareness training or phishing exercises beyond the agencies' own required courses.

## 5. Scenario choices
| Deliverable | Scenario choice |
|---|---|
| Primary system | The registry default fits: the **Hosted Case Management Service**, a case management system hosted for local agencies. At this size it is built on a licensed low-code platform rather than on the company's own cloud tenant, so most infrastructure controls are inherited from the platform vendor |
| P03 regulation | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline, required by the AC-02, AC-03, and AC-04 contracts, with CJIS Security Policy v6.1 (AC-01) and IRS Pub. 1075 (SC-01) overlay rows |
| P08 incident | Ransomware at the company that reaches agency data: a phishing email gives an attacker the Lead Platform Engineer's laptop and sessions; the attacker encrypts the integration server and its export bucket, pulls CJI from the AC-01 workspace, and could reach the revenue agency's virtual desktop from a connected laptop. Adapted from the registry default ("ransomware affecting agency systems holding CJI and FTI"): the company hosts CJI but never stores FTI, so the FTI risk runs through its access to the agency's system, and the MSP and insurer are in the notification chain |
| P09 SOC 2 | The company **is** a service organization. AC-02's renewal questionnaire (due 2026-10-30) asks for a SOC 2 report, GovRAMP verification, or a self-assessment against the Trust Services Criteria with a remediation plan. Readiness self-assessment against Security plus Confidentiality, and a review of the platform vendor's SOC 2 Type 2 report |
| P10 AI | The registry default, adapted: **AI pre-screening for a county-funded emergency assistance program** (SYS-09). The platform's AI add-on reads documents and suggests "likely eligible", "likely ineligible", or "needs information" to AC-02 caseworkers, who decide. Federal SNAP, TANF, and Medicaid rules do not apply because the county funds the program |
| Cloud | SaaS (the platform and the business SaaS) plus one cloud workload (SYS-02). Vendor-agnostic; AWS, Azure, and Google Cloud equivalents named only in the P04 equivalents table |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-27 to 2026-08-07 | BIA, risk assessment, and gap analysis fieldwork (Operations Manager with the Lead Platform Engineer and the MSP lead technician) |
| 2026-08-17 to 2026-08-19 | Control assessment by an independent consultant |
| 2026-08-31 | Deliverables approved by the owner |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Platform vendor terms | 99.9% monthly availability; continuous backup (platform recovery point 1 hour); 14 days of restore points; full-tenant restore on customer request within 48 hours (no record-level restore); tenant audit logs kept 90 days; customers told within 72 hours of a confirmed security incident | P02, P04, P05, P09 |
| Platform vendor evidence | SOC 2 Type 2 report, 12 months ending 2026-03-31, Security, Availability, and Confidentiality, unqualified, 1 exception (1 of 40 sampled changes lacked documented approval), IaaS hosting carved out; reviewed 2026-08-21. August 2026 letters: platform endpoints use FIPS 140-3 certified modules; the AI add-on and its model subprocessor are outside the FedRAMP authorization and the SOC 2 report | P02, P04, P09, P10 |
| Platform settings at fieldwork | Lockout after 10 failed sign-ins in 30 minutes; idle session 60 minutes and 12-hour absolute limit; passwords of 12 characters or more with a breached-password check. Laptops lock after 15 minutes idle | P02, P03, P06 |
| Platform roles | Administrator (owner, Lead Platform Engineer); developer (both Platform Developers; can promote to production and read production data); support (Implementation and Support Analyst; read every workspace until narrowed to exclude AC-01 on 2026-08-12) | P01, P02, P07 |
| Agency users | About 30 at AC-01, 9 at AC-02, 20 at AC-03, and 15 at AC-04. P07 found 2 AC-03 accounts unused for more than 120 days (disabled 2026-08-19); the city had not reported 2 departures | P02, P05, P07 |
| Sheriff file drop | Keeps 7 days of files. The SFTP credential is a 10-character password unchanged since 2024; P07 found it in plain text in an interface script visible to all 5 repository users; sheriff IT rotated it on 2026-08-20 | P01, P05, P07 |
| SYS-02 details | Built by hand in 2024; default cloud image user disabled; no malware protection; SSH keys held by the owner and the Lead Platform Engineer without passphrases; 2 high-rated security updates pending at fieldwork, all pending updates applied 2026-08-21. A security group rule allowing SSH from any address was added in May 2026 for remote work and removed on 2026-08-18 when P07 found it | P01, P04, P07 |
| FTI spill | A defect log in the suite held 14 taxpayer identification numbers typed in by the Integration Consultant from the agency virtual desktop in May 2026. Found by the data inventory on 2026-07-29; reported by phone about 3 hours later to the prime's security officer and the revenue agency's disclosure officer. The agency could not rule out FTI within 24 hours and reported to TIGTA and the IRS Office of Safeguards on 2026-07-30. File purged 2026-07-30 under the agency's direction with a written record; the MSP purged suite backup copies on 2026-08-05. The agency's review is open | P01, P03, P07, P09 |
| SC-01 devices and staff | The 2 laptops on the agency CISO's approved list are the Integration Consultant's laptop and the spare. The Lead Platform Engineer's annual recertification was due in June 2026; his 2 June connections were from his own assigned laptop. He was suspended from SC-01 on 2026-08-12; the company disclosed the connections to the prime and the agency on 2026-08-14 | P01, P03, P07 |
| Helpdesk and AC-01 disclosures | A sample of 40 sheriff tickets found 3 with CJI screenshots. The AC-01 LASO was told on 2026-08-14 about the screenshots and the unscreened support role | P01, P04 |
| Laptops | P07 found 3 of the 8 laptops using 128-bit full-disk encryption (the operating system default when they were set up). The MSP tests updates on the spare laptop first. One laptop was reissued to the Support Analyst in April 2026 with no wipe record | P03, P04, P07 |
| MSP details | Daily SaaS-to-SaaS backup of the suite kept 30 days. Evidence requested 2026-08-10; patch, antivirus, encryption, MFA, and backup reports received 2026-08-14; technician list, console MFA evidence, and remote session logs not received by fieldwork end | P05, P07 |
| Contract terms | AC-01 and AC-02: 99.5% monthly availability with service credits. Every agency contract has the Fla. Stat. 119.0701 public records clause naming the agency's records custodian. The AC-02 Emergency Assistance Program pays one-time rent or utility amounts to households with income at or below the county's published limit; a complete application gets a decision within 5 business days, and a denial notice states the reason and the county's appeal process. AC-02 staff send a weekly payment request file from the platform to the county payment system | P02, P05, P10 |
| AC-02 and AI pilot | AC-02 confirmed in writing in August 2026 that its human services department receives federal financial assistance for other programs, and agreed in writing on 2026-08-28 to the P10 decision. About 640 applications were processed with suggestions in June and July 2026; caseworkers accepted about 93% of suggestions. County quality control re-worked 120 applications blind, 2026-08-10 to 2026-08-14 (results in P10). The vendor's AI case-note summary feature is off in every workspace (confirmed 2026-08-19) | P10 |
| Office | Keyed entry with an alarm monitored by the landlord; locked network closet; keys held by the owner and the Operations Manager; one internet line; staff Wi-Fi password shared and unchanged since 2024; one office printer for business documents only | P03, P05 |
| Finances | Payroll runs biweekly through an outside payroll service; accounting is SaaS. SC-01 bills about $3,200 a week. The owner approved a 2026 Q4 security budget of about $4,800 one-time and $5,300 a year | P01, P05 |
| Assessor and criteria | The P07 assessor is an independent security consultant on a fixed fee, not involved in P01 or P03. The assessor tested against the draft SSP and draft policies of 2026-08-14; 4 of 6 staff interviewed did not know the 1-hour reporting rule | P07 |
| Data inventory | The Operations Manager ran the first data inventory on 2026-07-29 (it found the FTI spill) | P01, P02, P03 |
