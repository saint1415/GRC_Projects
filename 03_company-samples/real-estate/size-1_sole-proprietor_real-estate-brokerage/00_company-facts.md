# Scenario facts: Cris Santos Company | Real Estate and Rental and Leasing | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the broker-owner holds a Florida real estate broker license and files Schedule C) |
| Business | Residential real estate brokerage (NAICS 531210): buyer and seller representation for single-family homes and condominiums, plus tenant placement (leasing only) for a few individual landlords. **No** property management, closing, title, or mortgage services |
| Location | Florida. Home office in the owner's residence; no storefront. Client meetings happen at listed properties or by video call |
| Workforce | The broker-owner only (0 employees). No affiliated sales associates. Uses contracted services instead of staff |
| Volume | About 20 closed sales sides a year (about 12 buyer sides, 8 listing sides) and about 10 tenant placements a year (about 35 rental applications screened) |
| Revenue | About $180,000 a year (fictional): about $162,000 in commissions and about $18,000 in leasing fees, or about $3,500 a week. SBA-small (standard $15.0 million, NAICS 531210) |
| Escrow | One **sales escrow account** at a Florida bank. The brokerage holds the earnest money deposit in about 6 sales a year (about $90,000 a year) and, for leases, the first month's rent and security deposit until move-in (about $50,000 a year), then remits to the landlord. Title companies or closing attorneys hold every other deposit and close every sale |
| Clients and records | About 260 client files since 2019 (buyers, sellers, tenants, landlords). Files hold driver license images, proof-of-funds bank statements, pre-approval letters, rental applications, and tenant screening reports. About 30% of buyers live outside Florida (relocating or seasonal) |
| Primary regulation (decision) | **FTC Safeguards Rule, 16 CFR Part 314 (N53-R01): does not apply.** The business is not a "financial institution": residential brokerage is excluded from the "finder" activity because it requires a real estate broker license (16 CFR 314.2(h)(2)(xiii); 12 CFR 225.86(d)(1)(iii)(D)); tenant placement is brokerage, not nonoperating leasing; and the owner provides no settlement services and arranges no loans. The rule's elements (314.3-314.4) are used as a **benchmark** for "reasonable measures". Full reasoning in P03 section 1 |
| Binding rules | Florida broker escrow duties (Fla. Stat. 475.25(1)(d)1. and (1)(k); Fla. Admin. Code ch. 61J2-14 and r. 61J2-10.032), Fla. Stat. 501.171 (reasonable measures, breach notice, disposal), FTC Act Section 5 (N53-R02), and FCRA duties for tenant screening reports (15 U.S.C. 1681m(a); 16 CFR 682.3) |
| Contrast worth noting | The Small sample in this vertical is covered by the Safeguards Rule because its in-house Closing Services division provides real estate settlement services. The test is the activity, not the size: if this owner ever acted as closing agent, the rule would apply (with the 314.6 exceptions for fewer than 5,000 consumers) |
| Not in scope | FinCEN residential real estate reporting rule (31 CFR 1031.320): vacated by the U.S. District Court for the Eastern District of Texas on 2026-03-19, appeal pending (FinCEN page rechecked 2026-10-06); brokers are not in its reporting cascade in any case. CCPA/CPRA (N53-R03): no California business; receipts far below the threshold. PCI DSS (N53-R04): no payment cards accepted; applicants pay screening fees directly to the screening service. SEC disclosure (N53-R05): not a public company |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: broker escrow (Fla. Stat. 475.25; ch. 61J2-14), breach notice and disposal (Fla. Stat. 501.171), and wire recall (Fla. Stat. 670.211, in P08) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Broker-owner | Every role: owner, licensed broker and only escrow account signatory, security lead (benchmark "Qualified Individual"), privacy contact, risk acceptor, incident lead |
| Freelance transaction coordinator | Independent contractor paid per file (about 20 files a year). Has a named account in the transaction platform. **Signs in to the owner's mailbox with the owner's password** to send documents, and the owner forwards the text-message sign-in code. Works from the coordinator's own laptop. No written confidentiality or security terms |
| Outside bookkeeper | Prepares the monthly escrow reconciliation from bank statements the owner saves to a shared folder; the owner reviews, signs, and dates it (r. 61J2-14.012(2)). No online banking access. Engagement letter has a confidentiality clause but no security or breach notice terms |
| On-call IT technician | Hourly help with the laptop and home network. Signed a confidentiality and data-handling agreement on 2026-08-14, before the self-assessment. No standing access |
| Title companies and closing attorneys | Close every sale and hold most deposits. Independent parties, not the brokerage's service providers |

## 3. Systems
| ID | System | Hosting | Holds client personal information? | Notes |
|---|---|---|---|---|
| SYS-01 | Transaction management platform (contracts, disclosures, document storage, deadlines, client document sharing) | Vendor SaaS | Yes | System of record for transactions. Owner (broker administrator) and transaction coordinator accounts. MFA available but **off**. Vendor SOC 2 Type 2 report reviewed (P09) |
| SYS-02 | Business email and file storage (productivity suite with the brokerage's own domain) | Vendor SaaS | Yes | Main BEC target. MFA by **text-message code**. Coordinator uses the owner's credentials. External auto-forwarding allowed; no alerts; no DMARC policy on the domain |
| SYS-03 | E-signature service | Vendor SaaS | Yes | Password only |
| SYS-04 | MLS, showing scheduling, and electronic lockbox apps | Provided by the MLS and the local association | Limited (buyer names, showing times) | Lockbox app on the phone opens listed homes |
| SYS-05 | Online banking for the sales escrow account and the operating account | Bank-hosted | Yes (account data) | Owner is the only user. Text-message code at sign-in and for each outgoing wire |
| SYS-06 | Accounting SaaS | Vendor SaaS | Limited | Operating books. Bookkeeper has an accountant login. Password only. The escrow ledger is a spreadsheet in SYS-02 |
| SYS-07 | Laptop | Owner device | Yes (downloads, synced files) | Full-disk encryption on; automatic updates; built-in antivirus. **A family member sometimes uses it under the owner's login** |
| SYS-08 | Mobile phone | Personal device | Yes (texts, photos) | Passcode on. Receives the text-message codes. Holds texted photos of driver licenses and pre-approval letters |
| SYS-09 | Home office network | ISP-provided router | Yes (in transit) | Default router admin password; firmware not updated since 2023; one Wi-Fi network shared with family and smart-home devices |
| SYS-10 | Online tenant screening service with an automated applicant score and recommendation | Vendor SaaS | Yes (consumer reports) | Applicants enter their own data and pay the fee. AI-001 in P10 |
| SYS-11 | Generative AI writing assistant (consumer plan) | Vendor SaaS | Sometimes (pasted client details) | Used for listing descriptions and client emails. AI-002 in P10 |

**SSP system (P02):** the *Transaction Management and Closing Communications System (TMCC)*: SYS-01 to SYS-09, with SYS-10 and SYS-11 as external services.

## 4. Current security posture: early (few formal controls)
**In place today:**
- Business-grade email plan with the brokerage's own domain, and the provider's spam and phishing filtering
- MFA by text-message code on email and online banking
- Laptop full-disk encryption (on by default), automatic OS updates, and built-in antivirus
- Sales escrow account at a Florida bank with the broker as signatory; monthly reconciliations prepared by the bookkeeper and signed by the broker (r. 61J2-14.012(2))
- A wire fraud warning line in the owner's email signature
- The SaaS vendors' own backups
- Paper shredded at home with a cross-cut shredder

**Missing:**
1. No written security program, risk assessment, or policies (Fla. Stat. 501.171(2) "reasonable measures" are undocumented).
2. The transaction coordinator signs in to the owner's mailbox with the owner's password, and the owner forwards the text-message code.
3. MFA is off on the transaction platform, e-signature service, and accounting SaaS. Email MFA uses text-message codes only.
4. No wire verification rule. Wire instructions for the escrow account go to buyers as PDF attachments by email, and the owner disburses escrow funds on emailed instructions without a callback. Clients are never told how instructions will (and will not) arrive.
5. No review of email sign-in history or forwarding rules; external auto-forwarding is allowed; no DMARC policy on the domain.
6. Client personal information (driver license images, bank statements, rental applications, screening reports) is kept indefinitely in email, files, and the phone. No retention or disposal rule for electronic records (Fla. Stat. 501.171(8); 16 CFR 682.3).
7. A family member uses the laptop under the owner's login.
8. The home router has its default admin password and old firmware; one network for work, family, and smart-home devices.
9. No incident plan, no contact list, and no bank fraud desk number on file.
10. No written security or breach notice terms with the transaction coordinator or the bookkeeper (Fla. Stat. 501.171(6)).
11. No independent backup of email or transaction files.
12. Tenant screening recommendations are passed to landlords as the decision; no adverse action notice is sent for conditional approvals (a higher deposit).
13. No security training for the owner or the coordinator.
14. Client details were pasted into a consumer generative AI tool.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 incident | Business email compromise targeting closing funds: the owner's mailbox is taken over, and a buyer is sent altered closing wire instructions that appear to come from the title company. Variant: a buyer's earnest money deposit for the brokerage's escrow account is diverted |
| P09 SOC 2 | Security criteria only, as the owner's self-check, plus a review of the transaction platform vendor's SOC 2 Type 2 report. Landlord clients and the professional liability insurer accept a self-attestation |
| P10 AI | AI-001: the tenant screening service's automated recommendation (the registry's "automated tenant and buyer screening"). **Adapted:** the owner does no automated buyer screening; buyers' pre-approval letters are read by the owner. AI-002: the generative AI writing assistant, inventoried with a short screen |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-08-17 to 2026-08-21 | Self-assessment with the on-call IT technician (tests on 2026-08-20) |
| 2026-09-15 | Deliverables adopted by the broker-owner |
| 2026-10-06 | FinCEN rule and HUD disparate impact rule status rechecked before publication |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| May 2026 near miss | On 2026-05-12 a buyer client received an email from a look-alike of the title company's domain with "updated" wire instructions. The buyer phoned the owner before sending money, and the title company confirmed the email was fake. Nothing was documented and no rule changed | P01, P03, P08 |
| Coordinator access | The coordinator has a named transaction platform account that can see every file, and has used the owner's mailbox credentials since 2024. The coordinator's laptop is personal and its security is unknown | P01, P02, P04, P07 |
| Escrow disbursements | The owner wires the held deposit to the title company before closing, or remits rent and security deposits to landlords, on instructions received by email, about 16 outgoing payments a year | P01, P03, P05, P08 |
| Professional liability insurance | Errors and omissions policy in force. Whether it covers funds transfer fraud or social engineering losses is unconfirmed; no standalone cyber policy (owner action in P08) | P01, P08 |
| Platform vendor assurance | The transaction platform vendor provided its SOC 2 Type 2 report (Security and Availability) under a nondisclosure agreement; reviewed 2026-08-19 | P02, P09 |
| Old phone | The owner traded in the previous phone in 2025 without a documented wipe | P03, P07 |
| Website statement | The brokerage website's privacy page says client information is protected with "bank-level security" | P03 |
| Generative AI use | Between March and August 2026 the owner pasted parts of about 6 client emails (names, budgets, and one buyer's pre-approval amount) into the consumer writing assistant to draft replies | P01, P10 |
