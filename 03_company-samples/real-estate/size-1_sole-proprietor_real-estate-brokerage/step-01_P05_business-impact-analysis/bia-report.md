# Business Impact Analysis: Cris Santos Company | Real Estate and Rental and Leasing | Sole Proprietorship

**Organization:** Cris Santos Company (residential real estate brokerage) | **Tier:** Sole Proprietorship (broker-owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Broker-owner, 2026-08-18, with the on-call IT technician (under a confidentiality agreement since 2026-08-14) | **Adopted:** Broker-owner, 2026-09-15

## 1. Overview and purpose
This one-page BIA lists the five business functions the brokerage depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order and the "verified channel first" rule in the incident runbook (P08);
- the escrow duties in Fla. Stat. 475.25(1)(k) and Fla. Admin. Code ch. 61J2-14, which do not pause when a system is down.

## 2. Business description
One licensed broker closes about 20 sales sides and places about 10 tenants a year from a home office in Florida. There are no employees. A freelance transaction coordinator helps with files, an outside bookkeeper prepares the monthly escrow reconciliation, and an on-call IT technician helps with the laptop and home network. Everything runs on SaaS (transaction platform, email and files, e-signature, accounting, tenant screening), bank-hosted online banking for the sales escrow account, one laptop, and a personal phone. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts, or about $3,500 a week. Safety is marked N/A: no function can plausibly cause physical harm (the lockbox app risk is a disclosure and property risk, rated in P01).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $10,000, or any client funds lost (a single diverted closing wire can exceed a year of income) | $2,000 to $10,000 (a lost commission) | Less than $2,000 |
| Operations | A closing cannot fund or a contract deadline is missed | Closings delayed but not lost | Administrative delay only |
| Regulatory | Escrow violation, Florida Real Estate Commission complaint, or reportable breach | Missed documentation or notice step | Internal policy deviation |
| Reputation | Client funds lost; referral sources stop sending business | Client complaints or reviews | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Closing funds and escrow handling | High | 24 h | 4 h | 24 h |
| BP-02 Contract-to-close transaction management | High | 24 h | 8 h | 4 h |
| BP-03 Client communications and marketing | Moderate | 24 h | 8 h | 24 h |
| BP-04 Tenant placement and screening | Low | 120 h | 72 h | 24 h |
| BP-05 Business administration | Low | 120 h | 72 h | 24 h |

**What drives the values:** money movement drives BP-01. The risk is not that the bank is down but that the **channel used to confirm wire instructions** (email and the phone) is untrustworthy or unavailable on a closing day; a 4-hour RTO for a verified phone channel keeps a closing on schedule. Contract deadlines drive BP-02; the 4-hour RPO is supported by the transaction platform vendor's backups (P09). The 24-hour RPO for BP-05 is **not fully supported today**: the escrow ledger spreadsheet and the new security documents sit only in SYS-02 with no independent backup (P01 R-014).

**Single-person dependency (the key finding).** The broker-owner is the only licensee, the only escrow account signatory, the only person who can approve a wire, and the only holder of every credential. The text-message codes for email and banking arrive on one phone. If the owner is ill, injured, or without the phone, BP-01 and BP-02 exceed their MTD at once: deposits cannot be placed or disbursed, and clients with closings that week have no broker. Actions (P01 R-010, due 2026-12-31):
1. Sign a written backup arrangement with a trusted broker at another firm to step in on open transactions with the clients' consent.
2. Store the email, platform, and banking recovery codes and a one-page emergency sheet in a sealed envelope held by the owner's attorney.
3. Ask the escrow bank in writing what it requires if the only signatory is incapacitated, and record the answer.
4. Keep a printed list of open transactions (parties, title company, deadlines, deposit holder) updated weekly.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-08 Mobile phone | Text-message codes for email and banking; calls to clients and title companies; lockbox app | BP-01, BP-02, BP-03 |
| SYS-05 Online banking | Sales escrow and operating accounts | BP-01, BP-05 |
| SYS-02 Email and files | Correspondence, PDFs, escrow ledger spreadsheet (no independent backup) | BP-01 to BP-05 |
| SYS-01 Transaction platform | Contracts, deadlines, document storage; vendor backups | BP-02, BP-04 |
| SYS-07 Laptop | Main work device; the phone is the fallback | BP-01 to BP-05 |
| SYS-09 Home network | Internet for the home office; phone hotspot is the fallback | All |
| SYS-03, SYS-04, SYS-06, SYS-10 | E-signature, MLS and showings, accounting, tenant screening | BP-02 to BP-05 |
| Contracted services | Coordinator, bookkeeper, IT technician | BP-01, BP-02, BP-05 |
| People | Broker-owner only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner identity: phone and sign-in codes | 1 h | Recovery codes in the sealed envelope; replacement phone and SIM from the carrier in person |
| 2 | Verified phone channel to clients and title companies | 1 h | Printed open-transactions list with numbers taken from the contracts, not from emails |
| 3 | SYS-05 Online banking | 4 h | Branch visit for any escrow deposit or disbursement |
| 4 | SYS-02 Email (clean, owner-only access) | 4 h | Phone and the platform's document sharing |
| 5 | SYS-01 Transaction platform | 8 h (vendor-hosted) | PDFs in SYS-02; call the other agent and title company |
| 6 | SYS-07 Laptop | 8 h | Phone for urgent work; IT technician rebuilds the laptop |
| 7 | SYS-10, SYS-06 | 72 h | Hold applications; bookkeeping waits |
