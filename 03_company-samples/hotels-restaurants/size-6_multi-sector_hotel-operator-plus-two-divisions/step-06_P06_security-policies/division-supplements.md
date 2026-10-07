# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-10 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA, one severity scale, vendor access through PAM, card data only as tokens, purpose tags | Board risk committee or Group CISO |
| Group standards | Hardening, logging, cloud guardrails, payments standard, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards (owner obligations for managed hotels, ride control, COPPA, Safeguards Rule, Red Flags) | Division president, after Group CISO alignment review; for Vacation Ownership also the finance subsidiary board |
| Division procedures | Downtime procedures, terminal inspection checklists, park operations runbooks | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Hotels | v2026 | 2026-06-20 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after effective date) | Confirm alignment |
| Attractions | v2025 | 2025-09 | Aligned on payments, but **does not cover ride and show control networks** or the COPPA program (scenario gaps 7 and 4) | Add the rows marked "new" in section 3.2 by 2026-12-31 (POAM-016, POAM-025) |
| Vacation Ownership | None; division follows its pre-acquisition **2023 standards** | Never aligned | **Drifted** (scenario gap 7); conflicts in section 4 | Issue a supplement mapped to 16 CFR 314.4 by 2026-11-30 (POAM-024) |

## 3. What each supplement adds
### 3.1 Hotels supplement (merchant and service provider; manager of 58 hotels)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Owner responsibility matrix | Give every owner the service provider AOC and the responsibility matrix each year, and on request | POL-01 4.9 | PCI DSS 12.9.1, 12.9.2 |
| Management agreements | New and renewed agreements include security responsibilities, incident notice duties, cost allocation, and interconnection terms | POL-01 4.9 | N72-R02; Fla. Stat. 501.171(6) |
| Card display rights | Full card display only for the night audit and accounting roles listed; reviewed every 6 months | POL-02 4.2 | PCI DSS 3.4, 7.2 |
| Legacy POS | Local accounts listed and certified; vendor access only through PAM; segment monitoring until replacement | POL-02 4.1, 4.10 | PCI DSS 8.2, 8.4 |
| Building systems | Lock servers, IPTV, and building controllers in the hardening scan; vendor defaults changed before go-live | POL-02 4.10 | PCI DSS 2.2; *FTC v. Wyndham* practices |
| Key issuance | Photo ID or verified mobile key before issuing a room key; never by phone | POL-02 4.12 | N72-R02 |
| Terminal inspections | At least weekly at front desks and outlets, as the targeted risk analysis sets; device list from the terminal management service only | POL-05 4.5 | PCI DSS 9.5 |
| Guest register | PMS register kept at least 2 years at Florida hotels; identity document numbers removed 30 days after checkout | POL-04 4.6 | Fla. Stat. 509.101(2) |
| Pricing | Total price first in all channels, including the chatbot; emergency-declaration price cap in the revenue-management system | POL-05 4.6; POL-01 4.13 | 16 CFR 464.2; Fla. Stat. 501.160 |

### 3.2 Attractions supplement (merchant; operator of the kids' club; ride operator)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Ride and show control (**new**) | Ride control networks isolated; maintenance through a one-way path with PAM and ride engineering approval per session; no dual-homed jump hosts; rides closed until engineers verify controls after any suspected compromise | POL-02 4.10; POL-03 4.8 | Safety; N71-R05 |
| Children's information security program (**new**) | Written program with a named coordinator, annual risk assessment, safeguards, testing, and annual evaluation | POL-01 4.2 | 16 CFR 312.8(b) |
| Parental consent (**new**) | Card-transaction or other listed consent method; separate consent for any disclosure to a third party; no email-plus while the club discloses | POL-04 4.5 | 16 CFR 312.5(a)(2), (b)(2)(viii) |
| Children's data retention (**new**) | Profiles deleted 12 months after last activity; policy published in the online notice | POL-04 4.6 | 16 CFR 312.10, 312.4(d) |
| Biometric gate data | Templates deleted 30 days after pass expiry; annual vendor assurance; treated as biometric data under Fla. Stat. 501.171 | POL-04 4.6; POL-01 4.8 | Fla. Stat. 501.171(1)(g)1.a.(VI), (8) |
| Payment pages | No payment page goes live outside the main ticket store without a script inventory and tamper monitoring | POL-04 4.3 | PCI DSS 6.4.3, 11.6.1 |
| Seasonal staff | Accounts disabled at the end of the last scheduled shift | POL-02 4.5 | PCI DSS 8.2 |

### 3.3 Vacation Ownership supplement (merchant; finance subsidiary under the Safeguards Rule; managing entity of timeshare plans)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Qualified Individual | Board designation; senior officer oversight; monthly progress report during remediation; annual written report | POL-01 4.2, 4.10 | 16 CFR 314.4(a), (i) |
| MFA | MFA for every individual on every system; any equivalent approved in writing by the Qualified Individual | POL-02 4.3 | 314.4(c)(5) |
| Encryption | Customer information encrypted at rest and in transit; compensating controls only with written approval | POL-04 4.2 | 314.4(c)(3) |
| Testing | Annual penetration test of all systems with customer information, including the legacy data center; vulnerability scans at least every 6 months (quarterly in practice) | POL-01 4.10 | 314.4(d)(2) |
| Service providers | Risk-tiered assessments; contract safeguards before data is shared | POL-01 4.8 | 314.4(f) |
| FTC notice | Notification event decision with counsel; FTC notice within 30 days of discovery if 500 or more consumers | POL-03 4.6 | 314.4(j) |
| Identity theft | Red Flags program updated for gallery tablets and synthetic identity; gallery staff trained | POL-05 4.4 | 16 CFR 681.1(d), (e) |
| Credit decisions | Adverse action reasons specific to the principal factors; model reason codes reviewed monthly | POL-01 4.13 | 12 CFR 1002.9(b)(2) |
| Inventory reservations | Records supporting each reservation decision kept 5 years; produced to the state division with a confidentiality affidavit | POL-04 4.6 | Fla. Stat. 721.13(12)(c); 721.071 |

## 4. Vacation Ownership drift: conflicts with 2026 group policy
The 2023 standards were written before the acquisition. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 VO-16; P07 PL-01a.01(b)).

| Topic | Vacation Ownership standard (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| MFA | Required for administrators only | MFA for all access (POL-02 4.3) | 340 users without MFA (POAM-020) |
| Encryption at rest | Databases only | All Restricted data (POL-04 4.2) | Loan archive unencrypted (POAM-021) |
| Log review | Division staff weekly | SOC continuous monitoring (POL-01 4.6; group logging standard) | Legacy data center outside the SIEM (POAM-006) |
| Incident severity | Division 3-level scale | One group scale (POL-03 4.2) | Inconsistent escalation (P07 IR-04d.[01]) |
| FTC notice | Not addressed (written before 314.4(j) took effect on 2024-05-13) | FTC notice step (POL-03 4.6) | POAM-023 |
| Vendor reviews | At contract signing only | Risk-tiered reassessment (POL-01 4.8) | 12 of 31 providers unassessed (POAM-022) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Gap 7 (POAM-027) |

**Why the drift happened.** The 2024 integration plan moved finance, HR, and sales systems first and left security policy for "phase 2," which had no owner or date. **Fix:** POL-01 4.5 now requires an acquired business to adopt group policy or an aligned supplement within 6 months of closing, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Hotels, Attractions) and on issue (Vacation Ownership). The Qualified Individual's attestation is included in the annual report to the finance subsidiary board.
