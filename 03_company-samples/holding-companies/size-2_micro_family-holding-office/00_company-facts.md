# Scenario facts: Cris Santos Company | Management of Companies and Enterprises | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (the Santos family's holding company and single-family office; manager-managed Florida LLC) |
| Business | Holding company that owns and oversees three family operating companies and acts as the single-family office for the Santos family (NAICS 551112, Offices of Other Holding Companies). It does three things: (1) **subsidiary oversight**: board seats, monthly review of each subsidiary's financial package, second approval of large subsidiary payments, intercompany loans, and consolidated reporting for the family and the subsidiaries' bank lender; (2) **investment management** of the family's securities portfolio and private investments, for family clients only; (3) **family administration**: bill pay, household payroll, tax document coordination with an outside CPA firm, insurance, and estate records |
| Operating subsidiaries | Each is 100% owned by the holding company and has its own management, accounting system, and IT provider. **CSC Hospitality, LLC** ("Hospitality"): two full-service restaurants (NAICS 722511), about 90 employees. **CSC Marine Supply, LLC** ("Marine Supply"): distributor of marine parts and supplies to boatyards and marinas (NAICS 423860), about 28 employees. **CSC Commercial Properties, LLC** ("Properties"): owns three small commercial buildings leased to businesses (NAICS 531120), no employees, run by an outside property management firm |
| Family clients | 11 family members across three generations (the Principal and spouse, three adult children and two of their spouses, two adult grandchildren, two minor grandchildren) and 10 family entities: **CSC Family Investments, LLC** (the family's pooled investment vehicle), 6 irrevocable trusts, 2 revocable trusts, and the family's private foundation. All are family clients under 17 CFR 275.202(a)(11)(G)-1(d)(4) |
| Assets advised | About $310 million (fictional) in securities held at two custodians, plus interests in 14 private funds and direct deals. The office does not have custody: assets sit at the custodians in the clients' names |
| Location | Florida. One office suite, separate from the subsidiaries' sites. Two family households in Florida; one adult child lives in another state |
| Workforce | 7 employees: Family Office Director, Controller, Investment Director, Investment Analyst, Senior Accountant (bill pay and payroll), Executive Assistant to the Principal, and Office Manager. The Principal is the majority owner and Chair of the Board of Managers, not an employee |
| Receipts | About $1.1 million a year (fictional): management fees from the three subsidiaries ($640,000) and service fees charged at cost to family members and family entities under written service agreements ($460,000). SBA counts the receipts of a concern and its affiliates (13 CFR 121.103(a)(6); 121.104(d)(1)); combined with the subsidiaries (about $21.4 million: Hospitality $9.8 million, Marine Supply $10.1 million, Properties $1.5 million) the total is far below the $45.5 million standard for NAICS 551112 |
| Ownership and control | **Privately held.** The Principal (Cris Santos) owns 51%; the Santos Family Trust (an irrevocable trust whose only current beneficiaries are family members) owns 49%. The Board of Managers is the Principal (Chair), the Principal's spouse, and the eldest adult child. No securities are registered with the SEC |
| Advisers Act status | **Family office exclusion.** The office gives investment advice only to family clients, is wholly owned by family clients, is exclusively controlled by family members, and does not hold itself out to the public as an investment adviser, so it is not an "investment adviser" under the Advisers Act (17 CFR 275.202(a)(11)(G)-1(a)-(b)). Outside counsel confirmed this in 2024 and again on 2026-08-12. If it took a non-family client, it would lose the exclusion |
| Safeguards Rule status | **Treated as a financial institution** under 16 CFR Part 314 (conservative position, concurred in by outside counsel on 2026-08-12). Providing investment advisory services is a financial activity (314.2(h)(2)(xii)), 314.1(b) names "investment advisors that are not required to register with the Securities and Exchange Commission" and "other financial advisors", and family members obtain advisory services for a fee under written agreements (a customer relationship, 314.2(e)(2)(i)(G)). No FTC statement specific to single-family offices was found. Customer information concerns 11 individuals, far fewer than 5,000 consumers, so **314.4(b)(1), (d)(2), (h), and (i) do not apply** (314.6) |
| Florida breach law status | The office is a **covered entity** under Fla. Stat. 501.171(1)(b): it maintains personal information of family members, household employees, and its own employees. Where it maintains personal information for a subsidiary, it is that subsidiary's **third-party agent** (501.171(1)(h)) |
| Group health plan | Fully insured small-group plan for the 7 employees, administered by the insurer. Because an entity other than the employer administers it, it is a group health plan (45 CFR 160.103, paragraph (2)). The office receives only enrollment information, so 45 CFR 164.530(k) relief applies and the 164.314(b) plan-document security terms are not triggered (exception for disclosures under 164.504(f)(1)(ii)-(iii)) |
| Not in scope | SEC Regulation S-K Item 106, Form 8-K Item 1.05, and SOX section 404 (not a registrant or issuer). Federal Reserve Regulation Y Subpart N and 12 CFR Part 225 Appendix F (owns no bank). Florida Digital Bill of Rights (a controller must exceed $1 billion in global gross annual revenue and meet one of three further tests in Fla. Stat. 501.702). Payment cards: Hospitality and Marine Supply take cards through their processors' terminals; the office handles no card data. Each subsidiary's own compliance (for example Hospitality's PCI DSS duties) is its own and is not assessed here, except for the office's oversight of it |
| State law approach | Florida law is cited only where unavoidable (breach notice, data security, and disposal under Fla. Stat. 501.171). For the adult child outside Florida, the law of that state applies; it is treated generically |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Board of Managers (Principal as Chair, Principal's spouse, eldest adult child) | Governing body of the office. Accepts High and Very High risks. Receives the Family Office Director's annual written security report (adopted voluntarily; 314.4(i) does not apply under 314.6) |
| Principal (majority owner) | Chairs the Board of Managers; approves policies and the security budget; decides any ransom question |
| Family Office Director | Runs the office. **Qualified Individual** under 16 CFR 314.4(a), designated in writing on 2026-08-14 (none before). Security and privacy lead, incident lead, owner of most risks. Accepts Moderate risks |
| Controller | Multi-entity accounting and consolidation (SYS-01); releases payments; second approver on subsidiary bank portals; backup incident lead |
| Investment Director | Investment decisions and custodian relationships; owner of the investment reporting platform (SYS-06). A key employee under 275.202(a)(11)(G)-1(d)(8) |
| Investment Analyst | Administers SYS-06 and its custodian data feeds; prepares quarterly family reports |
| Senior Accountant | Family bill pay (SYS-03) and household and office payroll (SYS-04) |
| Executive Assistant to the Principal | Family calendars and travel; uploads documents to the family document vault (SYS-07) |
| Office Manager | Office administration; coordinates the MSP; administrator of the productivity suite (SYS-02); onboarding and offboarding; vendor contracts |
| Subsidiary Presidents (3; employees of the subsidiaries) | Run their companies and their own IT; send monthly financial packages; hold guest accounts in the office's board site |
| Managed service provider (MSP) | Help desk, device management, patching, antivirus, firewall and Wi-Fi, and administration of the legacy partnership accounting server (SYS-11). Holds one shared global administrator account in SYS-02 |
| Outside counsel; outside CPA firm | Counsel: Advisers Act and Safeguards Rule questions, breach counsel through the insurer. CPA firm: prepares family and entity tax returns from documents shared through SYS-07 |

## 3. Systems
| ID | System | Hosting | Sensitive data | Notes |
|---|---|---|---|---|
| SYS-01 | Multi-entity cloud accounting and consolidation system | Vendor SaaS | Ledgers for the office and the 10 family entities; consolidation of the three subsidiaries' monthly trial balances; vendor and payee bank details | The office's "ERP". Vendor SOC 2 Type 2 report on file, not reviewed |
| SYS-02 | Productivity suite with identity (email, files, chat, single sign-on, MFA), one tenant | SaaS | All categories. Three file sites: **Family** (tax returns, estate plans, IDs, insurance, medical bills; all 7 staff have access), **Subsidiaries** (board packs and monthly financial packages; 9 subsidiary guests), **Office** | Identity for 7 staff and 9 guest accounts. Push MFA without number matching. Includes the AI assistant add-on (SYS-10) |
| SYS-03 | Bill pay platform | Vendor SaaS | Family members' bank account numbers, payees, invoices, medical bills | About 140 family payments a month from family members' own accounts |
| SYS-04 | Payroll and HR service | Vendor SaaS | SSNs, bank accounts, pay data for 7 office employees and 5 household employees | Household employees work for family members; the office runs their payroll as the family's agent |
| SYS-05 | Bank and custodian portals | Bank- and custodian-hosted | Account access for the office, the family entities, and family members (delegated access); approver roles on the subsidiaries' accounts | Bank-enforced dual approval for wires and ACH batches. The office is second approver on subsidiary payments over $25,000 (about 30 a month). Hardware tokens from the banks |
| SYS-06 | Investment reporting and aggregation platform | Vendor SaaS | Positions, transactions, and account numbers for every family account (read-only custodian data feeds) | Vendor SOC 2 Type 2 report on file, not reviewed |
| SYS-07 | Family document vault and client portal | Vendor SaaS | Estate plans, tax returns, passports and driver licenses, insurance policies, health care directives | Family members reach their own folders with SMS codes. The CPA firm and counsel receive documents by share link |
| SYS-08 | Endpoints | MSP-managed | Cached data of all types | 8 laptops (7 staff, 1 spare), 1 conference-room PC, 1 multifunction printer and scanner. Staff use personal phones for email and MFA, with no mobile management |
| SYS-09 | Office network | On-premises, MSP-managed | In transit | Small-business firewall, staff Wi-Fi, separate guest Wi-Fi, one internet line |
| SYS-10 | Generative AI assistant (add-on to SYS-02) | SaaS | Whatever the user can reach in SYS-02 | Pilot with 4 users since 2026-06-15 (Family Office Director, Controller, Investment Director, Executive Assistant). See P10 |
| SYS-11 | Legacy partnership accounting server | One virtual machine in a public cloud provider's IaaS (vendor-agnostic); MSP-administered | Capital accounts and K-1 allocations for CSC Family Investments, LLC; partners' SSNs | The office's only cloud workload. Daily snapshots in the same cloud account. Remote desktop open to the internet, limited to the office's IP address |

**SSP system (P02):** the *Family Office Shared Services Platform*: SYS-01 to SYS-11, with interfaces to the custodians, the subsidiaries' own systems, the outside CPA firm, and the MSP.

## 4. Current security posture: early to partial
**In place today:**
- MFA (authenticator app push) on the productivity suite, accounting system, bill pay platform, payroll service, and investment platform; bank hardware tokens on bank and custodian portals
- Bank-enforced dual approval for wires and ACH batches on office, family entity, and subsidiary accounts
- MSP-managed laptops with full-disk encryption, antivirus, and automatic patching
- Firewall with a separate guest Wi-Fi network
- Per-family-member folders in the document vault (SYS-07)
- A cyber insurance policy with a breach hotline
- A yearly security awareness video for staff (since 2024)
- SOC 2 Type 2 reports received from the accounting system and investment platform vendors

**Missing:**
1. No written information security program and no adopted policies. No Qualified Individual was designated before 2026-08-14.
2. No risk assessment has ever been done (the 2026 work is the first).
3. Payment instructions from family members, subsidiaries, and vendors arrive by email. The callback habit is unwritten and unrecorded. In March 2026 a spoofed email that looked like it came from an adult child asked for a $48,000 wire to a new account; the Senior Accountant caught it only because the amount was unusual. It was not logged as an incident.
4. Push MFA without number matching. Two family members use SMS codes for the vault, and the Principal's spouse signs in to the vault with the Principal's account.
5. Every staff member can open every family folder in the Family site, including tax returns, estate plans, and medical bills. Found when the AI assistant pilot surfaced a trust distribution memo to the Executive Assistant on 2026-07-22.
6. No review of sign-in or mailbox logs and no alerts for new inbox rules or forwarding. Logs are kept only for the license default.
7. No independent backup of the productivity suite. SYS-11 snapshots sit in the same cloud account and have never been restore-tested.
8. The MSP's shared global administrator account in SYS-02 has MFA registered to the MSP help desk phone; the MSP contract has no security terms.
9. No incident response plan. Only the Family Office Director knows the insurer's hotline number.
10. Guest accounts are never reviewed. A former Marine Supply controller who left in February 2026 still had access to the Subsidiaries site in August 2026.
11. No retention schedule. Family tax returns and ID copies go back to 2009, and household employees' new-hire forms are kept for former employees indefinitely.
12. No vulnerability scanning. SYS-11's remote desktop port is open to the internet (limited by IP address only), and its operating system reaches end of vendor support in October 2026.
13. No list of service providers with access to family information, and the two SOC 2 reports were never reviewed.
14. The AI assistant pilot started without an approved-use rule or a data-access review. An adult grandchild pasted a custodian statement into a free public chatbot in July 2026.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 benchmark | NIST CSF 2.0 Organizational Profile for the office and its oversight of the subsidiaries (voluntary; built with NIST SP 1301). Secondary and binding: the FTC Safeguards Rule (16 CFR Part 314) as narrowed by the 314.6 exception. Applicability gate: the Advisers Act family office exclusion conditions. At Micro size there are no separate subsidiary profiles: each subsidiary runs its own IT, and the office's part is oversight |
| P08 incident | Compromise of the shared productivity and identity tenant affecting the subsidiaries and the family: adversary-in-the-middle phishing of the Controller, mailbox takeover, a payment redirection attempt against a subsidiary and a family vendor, and access to the Family and Subsidiaries sites. The registry default ("compromise of shared services affecting subsidiaries") fits once "shared services" is read as the office's one tenant, which the subsidiaries reach as guests and through payment approvals |
| P09 SOC 2 | Security plus Confidentiality, as a readiness self-assessment used to answer a custodian's due diligence questionnaire and to report to the Board of Managers; plus a review of the investment reporting platform vendor's SOC 2 Type 2 report. Confidentiality fits better than Availability because the family's main concern is exposure of its information |
| P10 AI | Generative AI assistant add-on in the office's tenant (4-user pilot). The registry default ("enterprise generative AI assistant across subsidiaries") is narrowed: at this size the assistant is licensed only to office staff, but it reaches subsidiary board packs and family files in the same tenant |
| Primary system | The registry default ("shared corporate services platform, ERP and identity") is kept as the Family Office Shared Services Platform: the accounting system plays the ERP role and the productivity suite is the identity provider |
| Cloud | SaaS plus one cloud workload: the legacy partnership accounting server (SYS-11) in IaaS. Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-08-03 to 2026-08-14 | BIA, risk assessment, CSF profile, and Safeguards Rule gap analysis (Family Office Director with the MSP lead technician; counsel reviewed applicability on 2026-08-12) |
| 2026-08-31 to 2026-09-02 | Control assessment (independent consultant) |
| 2026-09-18 | Deliverables approved by the Principal; High-risk treatment plans approved by the Board of Managers |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Payment thresholds | Banks: dual approval on every wire and ACH batch. Callback required for every new payee, bank-detail change, and wire over $10,000 (POL-02 B.10). Bill pay platform dual approval for payee changes and payments over $5,000, turned on 2026-09-04 after P07 found it off | P01, P06, P07, P08 |
| Business calendar | Subsidiary monthly packages are due on business day 10; the subsidiaries' lender requires a quarterly covenant certificate 45 days after quarter end; private fund capital calls give about 10 business days' notice; household and office payroll is biweekly | P05 |
| Records held by others | Outside counsel holds the originals of estate plans and health care directives. The office safe holds bank tokens and original documents. Paper goes to a locked shredding bin emptied monthly by a shredding service | P02, P05, P09 |
| Office security | Keyed suite with an after-hours alarm; keys held by the Office Manager, Family Office Director, and Controller; locked file room; safe. Staff Wi-Fi password unchanged since 2023 | P02 |
| SYS-11 details | Daily snapshots kept 14 days in the same cloud account; remote desktop limited to the office IP address; local administrator signs in with a password only (P07 test 2026-09-01); port to be closed by 2026-10-15 | P02, P04, P05, P07 |
| MSP contract | Covers help desk, device management, patching, antivirus, firewall and Wi-Fi, and SYS-11 administration, with a 4-business-hour response time, no recovery time commitment, and no security terms. Evidence requested 2026-08-24; technician and subcontractor lists not received by fieldwork end | P05, P07 |
| Cyber insurance | Policy with a breach hotline and panel vendors (breach counsel, forensics); prompt notice through the hotline before hiring outside firms. Social engineering fraud coverage requires documented verification of payment changes | P01, P08 |
| Departures and transfers | One employee left in 2025 (replaced): SYS-02 disabled 2 days later, bank token returned 3 weeks later, exit interview held, laptop and keys collected. In 2025 the Executive Assistant moved off bill pay duties and SYS-03 access was removed the same day | P07 |
| Guests | 9 subsidiary guest accounts against 8 current subsidiary contacts. The former Marine Supply controller's guest account was removed 2026-08-14; the sign-in log showed no use after February 2026 | P01, P07 |
| Fixes during the work | Staff profile describing advisory services corrected 2026-08-13; separate vault account for the Principal's spouse 2026-08-20; printer firmware updated and conference PC set to a kiosk account 2026-08-21; 37 non-expiring vault share links (oldest from 2023) disabled 2026-09-02 | P01, P03, P07 |
| AI pilot | Paused by the Family Office Director on 2026-07-23, the day after the trust memo surfaced. In July one AI-drafted letter went to a family member without review. Test of 24 prompts run 2026-09-04. On restart, 3 users only (the Executive Assistant's license is not renewed) | P02, P10 |
| Draft runbook | The P08 runbook existed as draft version 0.9 dated 2026-08-28 when P07 fieldwork began; approved 2026-09-18 | P07, P08 |
| Assessor | The P07 assessor is an independent security consultant on a fixed fee, not involved in the risk or gap analysis and operating no control | P07 |
| Custodian questionnaire | One custodian sent a due diligence questionnaire in August 2026 about the office's delegated account access; response due 2026-10-30 | P09 |
| Investment platform report | SOC 2 Type 2, Security, Availability, and Confidentiality, 12 months ending 2026-06-30, unqualified, one exception; hosting provider carved out; reviewed 2026-09-10 | P09 |
| Governance documents | Family governance charter (2024) states the office's purpose. The Qualified Individual is a finance professional with no security training. The Board of Managers received the first written security report on 2026-09-18 | P03, P06, P09 |
| Budget | 2026 Q4 security budget approved 2026-09-18: about $7,900 one-time and $6,700 a year | P01 |
| People whose data the office holds | Fewer than 100 individuals in all: 11 family members, 12 current office and household employees, former employees, and contacts in family records | P08 |
| Storm plan | One-page storm checklist: laptops and tokens go home, contact card, Principal as backup bank approver | P01 |
