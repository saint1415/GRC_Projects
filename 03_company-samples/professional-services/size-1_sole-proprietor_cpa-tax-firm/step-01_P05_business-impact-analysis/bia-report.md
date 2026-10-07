# Business Impact Analysis: Cris Santos Company | Professional, Scientific, and Technical Services | Sole Proprietorship

**Organization:** Cris Santos Company (CPA and tax preparation practice) | **Tier:** Sole Proprietorship (CPA-owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** CPA-owner, 2026-07-27, with the on-call IT consultant (services agreement and IRC 7216 notice since 2026-07-23) | **Adopted:** CPA-owner, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the practice depends on, how long each can be down, and how much data each can lose. It supports:
- the safeguards the FTC Safeguards Rule expects the practice to design from its risks (16 CFR 314.4(b) and (c); N54-R01), including the availability of customer information named in 314.4(b)(1)(ii) (written criteria are not mandatory here because of the 314.6 exception, but the owner keeps them);
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08).

## 2. Business description
One CPA prepares about 380 individual returns and 45 business, trust, and estate returns a year, keeps the books for 12 small businesses, and answers IRS notices for clients, from a home office in Florida. About 60% of the year's fees are earned from February to April. The tax software and client portal (SYS-01, SYS-02) are vendor-hosted. Everything else runs on one laptop, one phone, a printer-scanner, a business email and file suite, and the home network. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual fees: about $1,700 per business day in filing season and about $400 per business day in the rest of the year.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (about three filing-season days, or lost clients) | $1,000 to $5,000 | Less than $1,000 |
| Operations | No return can be prepared or filed | Work slowed; some appointments moved | Administrative delay only |
| Regulatory | Reportable data theft (IRS, FTC, state notices) or client returns filed late because of the firm | A missed IRS e-file or recordkeeping requirement | Internal policy deviation |
| Safety | Not applicable: the practice has no physical safety impact. Client financial harm is rated under Regulatory and Reputation | | |
| Reputation | Loss of clients or referral sources; a complaint to the state board of accountancy | Client complaints | None outside the practice |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Tax return preparation and e-filing | High | 48 h | 24 h | 1 h |
| BP-02 Client document intake, e-signature, and return delivery | High | 48 h | 24 h | 24 h |
| BP-03 Client communications and IRS notice representation | Moderate | 72 h | 24 h | 24 h |
| BP-04 Bookkeeping and payroll support | Moderate | 72 h | 48 h | 24 h |
| BP-05 Billing and practice administration | Low | 168 h | 72 h | 24 h |

**What drives the values:** the filing deadlines drive BP-01 and BP-02. The values above are for filing season; in the last week before April 15 or October 15 the MTD for BP-01 drops to 24 hours, and from May to January it is about a week. Extensions are the safety valve: an extension can be filed for any client who cannot be finished, so a missed deadline costs fees and goodwill rather than client penalties, as long as the owner can still file the extensions. The 1-hour RPO for BP-01 depends on the tax software vendor's backups (its SOC 2 report states an RPO of 1 hour, P09). The 24-hour RPO for email and files is **only partly supported**: the suite keeps 30 days of file versions and nothing else, and laptop files have no backup (P01 R-012).

**Single-person dependency (the key finding).** The CPA-owner is the only preparer, the only signer, the e-file Responsible Official, and the only person who holds the tax software, email, and device credentials. The tax software's second factor is on one phone, and no recovery codes are stored. If the owner is ill, injured, or without the phone in March, every function above passes its MTD at once and nobody can even file extensions. Actions (P01 R-009, due 2026-12-31):
1. Sign a practice continuation agreement with another Florida CPA who can file extensions and contact clients if the owner is incapacitated. Counsel confirms how client information may be shared with that CPA under IRC 7216 (for example, a voluntary consent offered with the engagement letter; it may not be a condition of service under 26 CFR 301.7216-3(a)(1)).
2. Save the tax software and email recovery codes and a one-page emergency access sheet in a sealed envelope held by the owner's attorney (by 2026-09-30).
3. Register a second authenticator for the tax software on a spare device kept in the locked cabinet, if the vendor allows it.
4. Ask the tax software vendor how a designated person can file extensions under the firm's EFIN if the owner is incapacitated, and record the answer.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Tax software (vendor SaaS) | Return preparation, e-file transmission, client records; vendor backups | BP-01, BP-03 |
| SYS-02 Client portal with e-signature | Document upload, Form 8879 signatures, return delivery | BP-02 |
| SYS-06 Mobile phone | Tax software authenticator; client calls and texts | BP-01, BP-02, BP-03 |
| SYS-05 Laptop and printer-scanner | The only workstation; scanning paper drop-offs | BP-01, BP-02, BP-04, BP-05 |
| SYS-07 Home network | Internet for the home office; phone hotspot is the fallback | BP-01 to BP-05 |
| SYS-03 Email and file suite | Client correspondence, attachments, client folders (30-day version history only) | BP-02, BP-03, BP-05 |
| SYS-09 Accounting SaaS | The firm's books; accountant access to clients' accounting files | BP-04, BP-05 |
| SYS-04 Practice management | Billing, engagement letters, payment page | BP-05 |
| Contracted services | Tax software vendor; IT consultant (hourly, no standing access) | BP-01, BP-02 |
| People | CPA-owner only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and tax software second factor | 2 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Internet in the home office | 1 h | Phone hotspot |
| 3 | A clean workstation | 8 h | Reinstall the laptop from clean media with the IT consultant; borrow a clean device only for vendor web access |
| 4 | SYS-01 tax software access | 4 h (vendor-hosted; vendor RTO 4 hours) | File extensions when access returns; Form 4868 on paper if needed |
| 5 | SYS-02 client portal and Form 8879 signatures | 24 h | Forms 8879 by mail, hand delivery, or email (allowed by Pub. 1345) |
| 6 | SYS-03 email and files | 24 h | Phone calls; portal messages; clients re-send documents |
| 7 | SYS-09 accounting SaaS access | 48 h | Clients run payroll from their own service for one cycle |
| 8 | SYS-04 practice management and billing | 72 h | Paper invoices |
