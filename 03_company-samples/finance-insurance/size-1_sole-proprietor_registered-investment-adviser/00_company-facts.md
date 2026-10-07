# Scenario facts: Cris Santos Company | Finance and Insurance | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute or regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-adviser files Schedule C and is the adviser's only associated person) |
| Business | Fee-only investment adviser (NAICS 523940): discretionary portfolio management for individuals and families, plus financial planning for the same clients. No commissions, no insurance sales, no lending |
| Location | Florida. A home office in the owner's house is the principal office and place of business |
| Workforce | The owner-adviser only (0 employees). Uses contracted services instead of staff |
| Clients | About 70 client households: about 120 individual clients and about 140 accounts. Records on about 40 former individual clients are also kept, so customer information covers about 160 consumers. All clients are individuals using the service for personal and family purposes. Five households have moved to other states; the rest live in Florida |
| Assets under management | About $19 million (fictional), all discretionary, all held at one qualified custodian |
| Revenue | About $180,000 a year in advisory fees (fictional), billed quarterly in arrears and deducted from client accounts by the custodian on the adviser's instruction. About $720 per business day. SBA-small (standard $47.0 million, NAICS 523940) |
| Custody of assets | Client cash and securities are held by one qualified custodian (a national broker-dealer). The adviser can trade, deduct fees, and submit money movement requests; it never holds client funds or securities |
| Registration | **Registered with the Florida Office of Financial Regulation (OFR)**, not the SEC. Advisers Act section 203A(a)(1) (15 U.S.C. 80b-3a(a)(1)) bars an adviser regulated by the state of its principal office from SEC registration unless it has at least $25 million under management or advises a registered investment company. At $19 million the adviser must register with Florida (Fla. Stat. 517.12(3)). Rule 203A-1 (17 CFR 275.203A-1) sets the mid-sized adviser threshold: SEC registration is optional from $100 million to under $110 million |
| Primary security rule | **FTC Safeguards Rule, 16 CFR Part 314 (GLBA section 501(b)).** 16 CFR 314.1(b) names "investment advisors that are not required to register with the Securities and Exchange Commission" among the financial institutions under FTC jurisdiction, and GLBA section 505(a)(5) and (a)(7) (15 U.S.C. 6805) give the SEC only advisers registered with it. The small-entity exceptions of 16 CFR 314.6 apply (fewer than 5,000 consumers) |
| Contrast worth noting | If assets under management grew past the Rule 203A-1 threshold and the adviser registered with the SEC, **SEC Regulation S-P** (17 CFR 248.30, as amended in 2024) and **Regulation S-ID** (17 CFR 248.201) would apply instead: 248.30(d)(3) defines a covered institution as an investment adviser "registered with the Commission", and S-ID applies to advisers "registered or required to be registered" under the Advisers Act. The test is registration status, not headcount |
| Not in scope | Interagency Guidelines (12 CFR 30 App. B and parallels): not a bank. NYDFS Part 500: not New York licensed. NAIC Model #668: no insurance license. Form 8-K Item 1.05: not an SEC registrant. FinCEN investment adviser AML/SAR rule: covers SEC-registered and exempt reporting advisers, and its effective date was delayed to 2028-01-01 (FR Doc. 2025-24184). Payment cards: none accepted |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: registration and books and records (Fla. Stat. 517.12, 517.121), data security, disposal, and breach notice (Fla. Stat. 501.171), and recording consent (Fla. Stat. 934.03). Clients in other states are handled generically ("each state where affected individuals reside") |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-adviser | Every role: owner, investment adviser representative, chief compliance function, **Qualified Individual** under 16 CFR 314.4(a), risk acceptor, incident lead |
| Qualified custodian (national broker-dealer) | Holds client assets; provides the advisor portal; runs its own fraud checks on money movement; provides a SOC 1 Type 2 report on request |
| On-call IT consultant | Hourly help with the laptop, router, and SaaS settings. No standing access. A written services agreement with confidentiality and security terms was signed on 2026-07-10 (none before) |
| Outsourced compliance consultant | Helps with Form ADV updates and an annual compliance review. Receives a sample of client files each year. **Engagement letter has no security or confidentiality terms for client data** |
| Outside CPA | Prepares the owner's tax return. Sees business income only, no client data |

## 3. Systems
| ID | System | Hosting | Holds customer information? | Notes |
|---|---|---|---|---|
| SYS-01 | Custodian advisor portal (trading, fee instructions, account opening, money movement requests, statements) | Custodian-hosted | Yes | Client account records of record. The custodian enforces MFA (authenticator app on the owner's phone) |
| SYS-02 | Portfolio management, rebalancing, performance reporting, and fee billing platform | Vendor SaaS (daily custodian data feed) | Yes | **MFA available but off.** Vendor provides a SOC 2 Type 2 report |
| SYS-03 | Client relationship management (CRM) system | Vendor SaaS | Yes (SSNs, dates of birth, ID images, meeting notes) | **MFA available but off.** Onboarding documents are uploaded here |
| SYS-04 | Business email, calendar, and file storage suite | SaaS (business plan) | Yes (statements, tax returns, onboarding forms in email and shared folders) | **MFA off.** Password reused on two other sites. File version history kept 30 days. Vendor terms include a data protection addendum |
| SYS-05 | Financial planning software | Vendor SaaS | Yes (net worth, income, account aggregation) | The vendor enforces MFA |
| SYS-06 | E-signature service | Vendor SaaS | Yes (signed advisory agreements and custodian forms) | Signing links sent to the client's email on file |
| SYS-07 | Laptop, mobile phone, and USB backup drive | Owner devices | Yes (synced files, downloads, backup copy) | Laptop full-disk encryption on. **USB drive not encrypted**; it holds a full copy of the client folders, updated weekly, kept in a desk drawer. Phone holds the MFA app |
| SYS-08 | Home office network | Internet provider's router in the home | Yes (in transit) | **Router admin password never changed**; one network shared with family devices and smart-home devices. A family member sometimes uses the laptop under the owner's account |
| SYS-09 | Generative AI assistant | Consumer plan (web and phone app) | Yes (pasted statements and notes) | Used since 2026-05 to summarize client statements and draft review letters; **consumer terms allow the vendor to use chats to improve its models**; see P10 |
| SYS-10 | Accounting SaaS | Vendor SaaS | Limited (client names and fee amounts) | Business books only |

**SSP system (P02):** the *Advisory Practice Systems Profile*: SYS-01 to SYS-10 as one boundary, the owner's core SaaS stack (email, files, CRM, portfolio and billing records) plus the devices and home network used to reach it.

## 4. Current security posture: informal (basic hygiene, big gaps)
**In place today:**
- MFA on the custodian portal and the financial planning software (enforced by those vendors)
- Full-disk encryption on the laptop (turned on at setup); passcode on the phone
- Automatic operating system updates and built-in antivirus on the laptop and phone
- A business-plan email and file suite (not a consumer account) with the vendor's data protection addendum
- A compliance manual and Form ADV prepared with the compliance consultant, including a privacy notice delivered to clients each year and one generic paragraph on information security
- The custodian's own review of third-party wire requests and a signed letter of authorization for each one
- A cross-cut shredder in the home office

**Missing:**
1. No MFA on email and files, the CRM, the portfolio and billing platform, the e-signature service, or the accounting SaaS (16 CFR 314.4(c)(5)). The email password is reused on other sites.
2. No callback rule. Money movement requests that arrive by email or text are acted on by sending the custodian's form for e-signature to the client's email address, without a phone call to a known number.
3. No information security program beyond one generic paragraph, and no written designation of a Qualified Individual (314.3(a); 314.4(a)).
4. No risk assessment ever performed (314.4(b)).
5. Customer information is spread across email attachments, the CRM, shared folders, the laptop, and the USB drive, with no inventory of where it is (314.4(c)(2)).
6. The USB backup drive is not encrypted, and the cloud files have no independent backup beyond 30-day version history (314.4(c)(3); Fla. Stat. 517.121).
7. No review of sign-in history, mailbox forwarding rules, or platform activity (314.4(c)(8)).
8. Service providers are not overseen: no review of their safeguards, and the compliance consultant's engagement letter has no security terms. The IT consultant had none until 2026-07-10 (314.4(f)).
9. No incident response plan and no contact list. Florida's 30-day breach notice clock is unknown to the owner (Fla. Stat. 501.171(4)).
10. The home network is shared with family and smart-home devices, the router has its default admin password, and a family member sometimes uses the laptop.
11. Client statements with account numbers were pasted into a consumer generative AI assistant whose terms allow model training (314.4(f); P10).
12. No security training beyond continuing education on compliance topics; nothing on business email compromise.
13. No retention or disposal schedule. Records on former clients back to 2015 are kept everywhere (314.4(c)(6)).
14. Single-person dependency: no written arrangement for another adviser or a trusted person to act if the owner is incapacitated, and the custodian portal's second factor is on one phone.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 incident | Business email compromise and a fraudulent wire: a request to wire money from a client's custodial account to a "title company" arrives from the client's real email address, which an attacker controls. The owner sends the custodian's wire form for e-signature to that same address, and the attacker signs it. The runbook also checks whether the owner's own mailbox (no MFA) was the source |
| P09 SOC 2 | The adviser is not a service organization and would not obtain a SOC 2 report. Security criteria only: (A) the owner's self-check and (B) a review of the portfolio and billing platform vendor's SOC 2 Type 2 report |
| P10 AI | The consumer generative AI assistant (SYS-09) used to summarize client statements and draft review letters. The generated brief names an "AI credit underwriting model", which does not fit a one-person adviser that makes no credit decisions; the tier scope is "one third-party AI tool the owner uses" |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-10 | IT consultant signs a services agreement with confidentiality and security terms |
| 2026-07-13 to 2026-07-17 | Self-assessment with the IT consultant (BIA 2026-07-14; control tests 2026-07-15; vendor SOC 2 review 2026-07-16; risk register 2026-07-17) |
| 2026-08-24 | AI use assessment completed |
| 2026-08-31 | Deliverables adopted by the owner-adviser |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Near miss | On 2026-06-18 a request to wire $36,000 to a new bank account arrived from a client's real email address. The owner sent the custodian's wire form for e-signature; the custodian's own call to the client stopped it. The owner had not called the client | P01, P08 |
| Form ADV and privacy notice promise | The privacy notice tells clients the adviser maintains "physical, electronic, and procedural safeguards" for their information | P03, P06 |
| Mailbox rule found | During the 2026-07-15 test, the mailbox had one forwarding rule the owner did not recognize, sending messages containing "wire" to an outside address. It was deleted that day; the sign-in history kept by the plan (30 days) showed no foreign sign-ins. Treated as a possible past compromise that could not be confirmed. Counsel reviewed it on 2026-08-20 and concluded no notice was required on the facts known | P01, P07, P08 |
| Portfolio platform assurance | The portfolio and billing platform vendor provided its SOC 2 Type 2 report (Security and Availability) under a nondisclosure agreement. Reviewed on 2026-07-16 | P02, P09 |
| Cyber insurance | No cyber insurance. The adviser's errors and omissions policy may have a social engineering or cyber endorsement; not confirmed (owner action in P08) | P01, P08 |
| AI assistant use | Used about 3 times a week from 2026-05-04 to 2026-07-15; statements for about 25 client households were pasted in, some with full account numbers. Paused on 2026-07-15 | P01, P10 |
| AI letter accuracy | A review of the chat history found no SSNs. The owner re-checked 5 review letters sent in June 2026 and found one return shown as 6.4% instead of 6.1%; a correction was sent to that client | P01, P10 |
| Meeting tool AI summary | The video meeting service offers an AI meeting summary feature. It is turned off and has never been used | P10 |
