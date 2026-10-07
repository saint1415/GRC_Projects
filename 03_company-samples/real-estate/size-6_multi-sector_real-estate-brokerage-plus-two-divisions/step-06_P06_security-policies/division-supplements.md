# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-17 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for every individual, payee verification for every payment, portal-only wire instructions, one severity scale | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, payee verification standard, retention schedule, Group AI Standard (P10) | Group CISO; Group Treasurer for payee verification |
| **Division supplement** | Regulator-specific and system-specific standards (for example, broker escrow procedures, Title trust fund disbursement, AVM quality control, smart-home handover) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Residential Brokerage | v2025 | 2025-10 | Aligned to the 2025 policies; must add the 2026 changes (agent MFA with no exceptions, payee verification for refunds, payouts, and commissions) by 2026-12-30 (90 days after the effective date) | Update and attest |
| Mortgage and Title | v2025 (Home Loans annex and Title annex) | 2025-11 | Aligned; the Title annex already exceeds group policy on wire controls. Must add per-institution FTC counting and AVM testing duties | Update and attest by 2026-12-30 |
| Homebuilding | **None** | Never | **Missing** (scenario gap 5). Homebuilding staff work from group policy alone, and several group requirements have never been applied (section 4) | Issue by 2026-12-31 (POAM-014) |

## 3. What each supplement adds
### 3.1 Residential Brokerage supplement (focus division; not a financial institution itself, but runs the TMCC for Title)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Contractor agent lifecycle | Managing brokers report departures the same day; license transfer feed disables accounts; agents without MFA or training lose access | POL-02 4.3, 4.5; POL-05 4.3 | 16 CFR 314.4(c)(1), (c)(5), (e)(1) |
| Instructions to buyers | Agents never forward or type deposit or closing wire instructions; they send the portal link and the wire fraud warning | POL-04 4.3; POL-05 4.6 | 16 CFR 314.3(b); Fla. Stat. 475.25(1)(k) (worked example) |
| Escrow refunds and payouts | Every escrow refund, owner payout change, and commission account change goes through SYS-G5 payee verification with a callback to the number in the file | POL-01 4.9 | Fla. Stat. 475.25(1)(d)1. (worked example) |
| Deposit verification | When Title or another company holds the deposit, the verification task in SYS-B1 is blocking | POL-01 4.9 | Fla. Admin. Code r. 61J2-14.008(2)(b) (worked example) |
| Escrow disputes | A diverted or disputed deposit triggers the escrow dispute notice in the P08 matrix | POL-03 4.5 | Fla. Stat. 475.25(1)(d)1.; r. 61J2-10.032 (worked example) |
| SYS-B1 visibility | Transaction-team visibility; Title documents visible only to the transaction's agents | POL-02 4.2 | 16 CFR 314.4(c)(1)(ii) |
| Tenant screening | Every decline and conditional approval gets an FCRA adverse action notice; criminal and eviction records get individualized review | POL-01 4.14 | 15 U.S.C. 1681m(a); 42 U.S.C. 3604 |
| Advertising | Fair housing check on every AI-drafted listing description | POL-05 4.9 | 42 U.S.C. 3604(c) |

### 3.2 Mortgage and Title supplement (two financial institutions; Title is also an insurance licensee)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Qualified Individual oversight | The President, Mortgage and the President, Title each meet the Qualified Individual quarterly, with minutes | POL-01 4.2 | 16 CFR 314.4(a)(2) |
| Disbursement (Title annex) | Payoffs verified through lender portals or by callback to the lender's published number; seller proceeds changes need the seller's confirmation in the portal plus a callback; second reviewer for every published instruction | POL-01 4.9 | Fla. Stat. 626.8473(4) (worked example) |
| Seller identity (Title annex) | Enhanced identity verification for vacant property and remote sellers | POL-02 4.11 | 16 CFR 314.3(b) |
| FTC notice (both annexes) | Each institution counts its own consumers in every incident | POL-03 4.4 | 16 CFR 314.4(j) |
| Insurance regulator notices (Title annex) | List of states that have enacted a version of NAIC Model #668, with deadlines and contacts, kept in the matrix | POL-03 4.5 | N52-R07 |
| AVM and pre-qualification (Home Loans annex) | AVM random sample testing each quarter; nondiscrimination review; pre-qualification reason statements | POL-01 4.14 | 12 CFR 1026.42(i)(3); 12 CFR 1002.9 |
| SAR routing (Home Loans annex) | Loan-related fraud cases go to the BSA officer within 1 business day | POL-03 4.7 | 31 CFR 1029.320 |
| Vendor access | Title production vendor support only through group PAM | POL-02 4.10 | 16 CFR 314.4(f)(2) |

### 3.3 Homebuilding supplement (to be issued; required content)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Trade partner bank changes | Changes only through the trade partner portal, verified by callback through SYS-G5, with a 10-day hold; vendor master maintenance separated from purchasing | POL-01 4.9 | FTC Act Section 5; group policy |
| Smart-home handover | Builder roles removed and device passcodes reset before closing; handover checklist signed by the buyer | POL-02 4.11 | 15 U.S.C. 45(a) |
| Identity and email | All users on SYS-G1 and SYS-G4 by 2027-03-31; number-matching MFA on the legacy tenant until then | POL-02 4.3 | 15 U.S.C. 45(a) |
| Sales center networks | Cameras and access control on separate network zones | POL-04 | 15 U.S.C. 45(a) |
| Buyer deposits | Escrow unless waived in writing; daily reconciliation | POL-04 | Fla. Stat. 501.1375 (worked example) |
| Referrals | Signed affiliated business disclosure before a buyer is referred; only opted-in buyers sent to Home Loans | POL-04 4.4 | 12 CFR 1024.15(b)(1) |

## 4. Homebuilding without a supplement: where practice differs from group policy
Without a supplement, Homebuilding staff follow the practices they had before the group policies existed. Where they conflict, **group policy governs now** (POL-01 4.5), but the conflicts are real risks (P01 HB-001 to HB-004; P07 Homebuilding sample).

| Topic | Homebuilding practice today | Group policy (2026) | Effect |
|---|---|---|---|
| Trade partner bank changes | Accepted by email; one approver | Out-of-band verification through SYS-G5; two approvers (POL-01 4.9) | Two losses totaling $1.1 million (HB-001) |
| MFA | SMS codes on the legacy tenant | MFA for every individual; phishing-resistant for privileged roles (POL-02 4.3) | Phishing exposure (HB-002) |
| Smart-home roles | Builder keeps administrator access after closing | Removed at closing (POL-02 4.11) | Unauthorized home access risk (HB-003, HB-004) |
| Vendor master | Purchasing staff edit bank details | Separation of duties (POL-01 4.9) | Insider fraud path (HB-006) |
| Common control inheritance | Not documented | Documented and confirmed yearly (POL-01 4.6) | Cannot show controls operate (POAM-014) |
| Retention | Electronic buyer files kept indefinitely | Group retention schedule (POL-04 4.8) | Larger breach scope |

**Why this happened.** Homebuilding joined the group's shared services later than the other divisions and kept its own directory and email tenant during a migration that is still under way. No one owned a supplement. **Fix:** POL-01 4.5 now requires a supplement for every division, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations under the 2026 policies are due 2026-12-30 (Brokerage, Mortgage and Title) and on issue (Homebuilding).
