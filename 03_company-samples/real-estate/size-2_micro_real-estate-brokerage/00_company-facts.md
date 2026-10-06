# Scenario facts: Cris Santos Company | Real Estate and Rental and Leasing | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute or rule, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (Florida limited liability company; registered Florida real estate brokerage) |
| Business | Residential real estate brokerage (NAICS 531210) with two lines: (1) residential sales brokerage (buyer and seller representation for single-family homes and condominiums) and (2) residential property management and leasing for individual owners. **No** closing, settlement, title, or mortgage services: title companies or closing attorneys close every sale, and agents give buyers a list of unaffiliated lenders |
| Location | Florida. One leased storefront office suite in a coastal county; no branch |
| Workforce | 7 employees: Broker-owner, Office Manager, 2 Transaction Coordinators, Property Manager (licensed sales associate), Leasing Assistant, Bookkeeper |
| Affiliated sales associates | About 22 licensed sales associates who are **independent contractors**, not employees. They work under the Broker-owner's license and use company email and the transaction platform from their **own laptops and phones** |
| Revenue | About $1.1 million in annual receipts (fictional): about $780,000 brokerage company dollar after agent splits and about $320,000 in property management and leasing fees. About $4,400 per business day. SBA-small (standard $15.0 million for NAICS 531210) |
| Sales volume | About 190 closed transaction sides a year. The brokerage holds the earnest money deposit in its **sales escrow account** in about 55 transactions a year (about $1.4 million a year in deposits) and wires each deposit to the title company or closing attorney before closing. Title companies or attorneys hold every other deposit |
| Property management | About 85 rental homes for about 60 owners. Rents and security deposits are held in the **property management escrow account**. Owner distributions go out monthly by ACH (about 60 a month). About 280 rental applications a year are screened through the property management platform |
| Clients and records | About 2,300 people in electronic client files since 2021 (buyers, sellers, owners, tenants, applicants). Files hold driver license images, proof-of-funds bank statements, pre-approval letters, rental applications, and tenant screening reports. Paper files from 2016 to 2020 are boxed in a storage closet. About 25% of buyers live outside Florida |
| Primary regulation (decision) | **FTC Safeguards Rule, 16 CFR Part 314 (N53-R01): does not apply; used as the benchmark.** The company is not a "financial institution": brokerage is excluded from the "finder" activity because it requires a real estate broker license (16 CFR 314.2(h)(2)(xiii); 12 CFR 225.86(d)(1)(iii)(D)); property management leases are operating, not nonoperating, leases (12 CFR 225.28(b)(3)); and the company provides no settlement services (314.2(h)(2)(x)) and brokers no loans (314.2(h)(2)(xi)). Moving escrow funds is incidental to the licensed brokerage service, not a money transfer business offered to consumers (314.2(h)(2)(vi)); this point is a judgment, recorded in P03. If the company ever became covered, it holds information on fewer than 5,000 consumers, so 314.6 would except it from 314.4(b)(1), (d)(2), (h), and (i). Full reasoning in P03 section 1 |
| Binding rules | Fla. Stat. 501.171 (reasonable measures, breach notice, third-party agents, disposal); Florida broker escrow duties (Fla. Stat. 475.25(1)(d)1. and (1)(k); Fla. Admin. Code ch. 61J2-14 and r. 61J2-10.032); broker records retention (Fla. Stat. 475.5015, 5 years); FTC Act Section 5 (N53-R02); FCRA duties for tenant screening reports (15 U.S.C. 1681m(a); disposal rule 16 CFR 682.3); Fair Housing Act (42 U.S.C. 3604) for tenant screening (P10) |
| Contrast worth noting | The Small sample in this vertical is covered by the Safeguards Rule because its in-house Closing Services division provides settlement services. The test is the activity, not the size or headcount |
| Not in scope | FinCEN residential real estate reporting rule (31 CFR 1031.320): vacated by the U.S. District Court for the Eastern District of Texas on 2026-03-19, appeal pending (FinCEN page rechecked 2026-10-06); brokers are not in its reporting cascade in any case. CCPA/CPRA (N53-R03): no California business; receipts far below the threshold. PCI DSS (N53-R04): tenants pay rent by card or ACH only on the property management platform's hosted payment page, and the company stores no card data (noted, not assessed). SEC disclosure (N53-R05): privately held |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: broker escrow and records (Fla. Stat. 475.25, 475.5015; ch. 61J2-14), breach notice and disposal (Fla. Stat. 501.171), and wire recall (Fla. Stat. 670.211, in P08) |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Broker-owner | Broker of Record and managing member. Signatory on all escrow accounts (r. 61J2-14.010(1)) and the **approver** for every outgoing wire and ACH batch from the escrow accounts. Signs the monthly escrow reconciliations (r. 61J2-14.012(2)). Approves policies and spending; accepts Moderate risks; approves treatment plans for High risks |
| Office Manager | **Security and compliance lead** (the benchmark "Qualified Individual"; designated in writing by the Broker-owner on 2026-07-24). Privacy contact. Requests and removes accounts, keeps the vendor list, is the MSP's contact, and **initiates** outgoing escrow wires in online banking. Incident lead |
| Bookkeeper | Keeps the sales escrow ledger and the property management escrow ledger; prepares the monthly reconciliations; **initiates** owner distribution ACH batches; commission disbursements and payroll |
| Transaction Coordinators (2) | Run contract-to-close files in the transaction platform; send deposit instructions to buyers; request written deposit verification from title companies (r. 61J2-14.008(2)(b)) |
| Property Manager | Owns property management operations, owner and tenant communications, and tenant screening (P10 AI-001). Processes owner bank account changes |
| Leasing Assistant | Processes rental applications and showings; sends screening invitations |
| Contractor sales associates (about 22) | Independent contractors. Must deliver deposits to the broker by the end of the next business day (r. 61J2-14.009). Bound by the independent contractor agreement's confidentiality clause; no security terms |
| Managed service provider (MSP) | Help desk, patching, antivirus, firewall and Wi-Fi, laptop encryption, and administration of the email backup. A third-party agent under Fla. Stat. 501.171(1)(h) for the systems it maintains |

## 3. Systems
| ID | System | Hosting | Holds client personal information? | Notes |
|---|---|---|---|---|
| SYS-01 | Transaction management platform (contracts, disclosures, compliance review, document storage, deadlines, client document sharing) | Vendor SaaS | Yes | System of record for sales transactions. Used by 7 employees and about 22 contractor agents. MFA enforced for employees only. Office-wide visibility: every agent can open every file. Vendor SOC 2 Type 2 report reviewed (P09) |
| SYS-02 | Productivity suite (email, shared files, calendar) on the brokerage's own domain | Vendor SaaS | Yes | 29 mailboxes (7 employees, 22 agents). **Main BEC target.** MFA (authenticator app) for employees; agents password only. Legacy sign-in protocols enabled. DMARC policy set to monitor only. External auto-forwarding allowed. One shared global administrator account used by the Office Manager and the MSP, without MFA |
| SYS-03 | E-signature service | Vendor SaaS | Yes | Integrated with SYS-01. Password only |
| SYS-04 | Commercial online banking: sales escrow account, property management escrow account, operating account | Bank-hosted | Yes (account data) | Dual control for wires and ACH batches (Office Manager or Bookkeeper initiates; Broker-owner approves). Text-message codes at sign-in and approval. Positive pay not used |
| SYS-05 | Property management platform: owner and tenant portals, online rent payments (hosted payment page), property management escrow ledger, owner distributions, integrated tenant screening | Vendor SaaS | Yes (consumer reports, bank data) | Used by the Property Manager, Leasing Assistant, Bookkeeper, and Office Manager. Text-message MFA. AI-001 in P10 |
| SYS-06 | Accounting SaaS | Vendor SaaS | Limited | Operating books, commission disbursements, payroll export. The sales escrow ledger is a spreadsheet in SYS-02 |
| SYS-07 | Endpoints | MSP-managed | Yes (cached and scanned files) | 9 company devices: 7 laptops (one per employee) and 2 desktops (front desk, scanning workstation). Laptops encrypted; desktops not. Contractor agents use personal devices that are not managed |
| SYS-08 | Office network | On-premises, MSP-managed | Yes (in transit) | Small-business firewall, staff Wi-Fi, separate guest Wi-Fi, multifunction printer and scanner. One internet line |
| SYS-09 | SaaS-to-SaaS backup of the productivity suite | Backup vendor (cloud workload), MSP-operated | Yes | Nightly copy of the 7 employee mailboxes and shared files, 30 days of versions. Contractor agent mailboxes and SYS-01 are not backed up. Never restore-tested |
| SYS-10 | Generative AI writing assistant (consumer plans) | Vendor SaaS | Sometimes (pasted client details) | Used by staff and agents for listing descriptions and client emails. AI-002 in P10 |

**SSP system (P02):** the *Transaction Management and Closing Communications System (TMCC)*: SYS-01, SYS-02, SYS-03, SYS-07, SYS-08, and SYS-09, with interfaces to SYS-04 (online banking) and SYS-05 (property management platform).

## 4. Current security posture: early to partial
**In place today:**
- MFA (authenticator app) for all 7 employees on email and the transaction platform; text-message MFA on online banking and the property management platform
- Dual control in online banking for every outgoing wire and ACH batch from the escrow accounts (initiator and Broker-owner approver)
- Monthly reconciliations of both escrow accounts, prepared by the Bookkeeper and signed by the Broker-owner (r. 61J2-14.012(2))
- MSP patching, antivirus, firewall, and laptop encryption
- A wire fraud warning in every buyer's contract packet and in the employees' email signatures
- Rent card and ACH payments taken only on the platform's hosted payment page
- The SaaS vendors' own backups, plus the SaaS-to-SaaS backup of employee mailboxes
- Guest Wi-Fi separated from staff Wi-Fi
- A locked shred bin emptied by a shredding vendor

**Missing:**
1. No written security program or risk assessment, and the Safeguards Rule question had never been analyzed. Fla. Stat. 501.171(2) "reasonable measures" were undocumented.
2. The 22 contractor agents sign in to email and the transaction platform with a password only. Legacy sign-in protocols are enabled, and the domain's DMARC policy is monitor only.
3. One shared global administrator account for the productivity suite, used by the Office Manager and the MSP, has no MFA.
4. No wire verification rule. Transaction Coordinators email deposit wire instructions to buyers as PDF attachments; outgoing escrow wires to title companies are set up from emailed instructions without a callback; owner payout bank changes are accepted by email.
5. No review of mailbox sign-ins or forwarding rules, and no alerts; external auto-forwarding is allowed.
6. Departing contractor agents keep access for up to two weeks after they leave; there is no offboarding checklist.
7. The email backup covers employee mailboxes only and has never been restore-tested; agent mailboxes and transaction platform files have no independent backup.
8. No incident response plan. A May 2026 near miss (a spoofed title company email to a buyer) was handled ad hoc and not recorded.
9. No retention or disposal schedule for electronic records; screening reports and ID images are kept indefinitely; paper files from 2016 to 2020 sit in an unlocked storage closet.
10. No vendor inventory and no security or breach notice terms in the MSP contract or the agent agreements; the screening provider has never been reviewed.
11. Security training is a one-time video at hire for employees; contractor agents receive none; no phishing exercises.
12. The two office desktops are unencrypted; the scanning workstation keeps local copies of scanned IDs and bank statements.
13. Tenant screening recommendations are used as the decision; no adverse action notice is sent for conditional approvals (a higher deposit).
14. Client details have been pasted into consumer generative AI tools.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 incident | Business email compromise targeting closing funds. **Variant A:** a contractor agent's mailbox (password only) is taken over and a buyer is sent altered closing wire instructions that appear to come from the title company. **Variant B:** a spoofed owner email changes a property owner's payout bank account and diverts a monthly distribution from the property management escrow account. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Confidentiality. The company is not a service organization; the readiness check answers a relocation management company's security questionnaire for its broker network. Also a review of the transaction platform vendor's SOC 2 Type 2 report |
| P10 AI | AI-001: tenant screening recommendations in the property management platform (the registry's "automated tenant and buyer screening"). **Adapted:** the brokerage does no automated buyer screening; buyers' pre-approval letters are read by agents. AI-002: the generative AI writing assistant, with a short screen |
| Cloud | SaaS plus one cloud workload: the SaaS-to-SaaS email backup (SYS-09), operated by the MSP. Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-27 to 2026-08-07 | Risk assessment and gap analysis by the Office Manager with the MSP lead technician |
| 2026-08-17 to 2026-08-19 | Control assessment by an independent consultant (on site 2026-08-18) |
| 2026-09-14 | Deliverables approved by the Broker-owner |
| 2026-10-06 | FinCEN rule and HUD disparate impact proposals rechecked before publication |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| May 2026 near miss | On 2026-05-19 a buyer received an email from a look-alike of the title company's domain with "updated" closing wire instructions. The buyer called the Transaction Coordinator before sending money, and the title company confirmed the email was fake. Nothing was recorded and no rule changed | P01, P03, P08 |
| Cyber insurance | The company holds a cyber liability policy with a 24x7 breach hotline, panel breach counsel and forensics, and a social engineering (funds transfer fraud) endorsement with a $100,000 sublimit. The policy requires prompt notice and use of panel vendors. Errors and omissions coverage is a separate policy | P01, P08 |
| MSP contract | Covers help desk, patching, antivirus, firewall, Wi-Fi, laptop encryption, and backup administration, with an 8-business-hour response time, no recovery time commitment, and no incident notice clause | P05, P07 |
| Shared administrator | The MSP set up the shared global administrator account in 2023 and both the MSP lead technician and the Office Manager know its password | P01, P02, P07 |
| Forwarding rules | P07 testing on 2026-08-18 found 3 contractor agent mailboxes with rules forwarding all mail to personal webmail accounts. The rules were removed on 2026-08-19 | P01, P07 |
| Departed agent | During P03 fieldwork (2026-07-30), an agent who had moved to another brokerage on 2026-07-17 still had active email and transaction platform accounts. Disabled the same day; sign-in logs showed two sign-ins after departure, both to the agent's own files | P01, P03, P07 |
| Escrow bank | All three accounts are at one Florida bank with a business relationship manager. The bank's fraud desk number had not been recorded anywhere before 2026-08 | P05, P08 |
| Office security | Keyed suite entry with an after-hours alarm. Keys held by the Broker-owner, Office Manager, and Property Manager. The storage closet with paper files has no lock. A cleaning crew enters after hours | P01, P03 |
| Hurricane exposure | The office is in a coastal county; it closed for 3 days in 2024 for a storm. Staff worked from home on laptops | P01, P05 |
| Relocation questionnaire | A relocation management company sent its broker network security questionnaire in July 2026; the response is due 2026-10-15 | P09 |
| Platform vendor assurance | The transaction platform vendor provided its SOC 2 Type 2 report (Security, Availability, Confidentiality; 12 months ending 2026-05-31) under a nondisclosure agreement; reviewed 2026-08-19. It states RTO 4 hours and RPO 1 hour | P02, P05, P09 |
| Screening volumes | In the 12 months to 2026-07-31: 276 applications screened; 171 accepted, 58 accepted with conditions (higher deposit), 47 declined. Leasing staff changed 4 recommendations | P10 |
| Assessor | The P07 assessor is an independent security consultant on a fixed fee, not involved in the risk assessment or the gap analysis and operating no control | P07 |
| Finances and payroll | A cash reserve covers about 45 days of expenses; payroll runs biweekly through an outside payroll service fed from the accounting SaaS | P05 |
| BP-03 owner | One of the two Transaction Coordinators is the senior coordinator and owns contract-to-close workflows and deposit verification requests | P03, P05 |
| MSP operations | Monthly operating system and browser updates, critical updates within 14 days, quarterly firewall firmware updates; firewall alerts go to the MSP | P02, P04, P07 |
| Retired devices | Two laptops were replaced in 2025 and returned to the reseller with no wipe record | P02, P03 |
| Website statement | The brokerage website's privacy page says client documents are "kept secure and confidential" | P03 |
| P03 samples | 15 sales escrow deposits (all placed within 3 business days; 1 reached the broker on the second business day); 20 transaction files with title-held deposits (4 without a written verification request); 12 months of reconciliations for both escrow accounts (2 small differences, both explained) | P03 |
| Agent departures | Of the last 4 agents who left, 2 were disabled more than 5 business days after leaving | P07 |
| Scanning workstation | Held 340 scanned IDs and bank statements in a local folder when tested on 2026-08-18 | P07 |
| Generative AI use | Between March and August 2026, client names, budgets, and one buyer's pre-approval amount were pasted into consumer AI tools in about 9 email drafts | P01, P10 |
| Screening criteria and results | Thresholds set in 2023: income at least 3 times rent, a minimum score band, any eviction filing in 7 years, any criminal record in 10 years. Of 47 declines, 19 were driven by eviction filings (7 dismissed), 9 by criminal records more than 7 years old, 14 by credit score, and 5 by income. A 20-file accuracy check found 2 name-only mismatches and 3 dismissed filings counted | P10 |
| Relocation network data | The relocation company would send transferees' names, contact details, and relocation budgets | P09 |
