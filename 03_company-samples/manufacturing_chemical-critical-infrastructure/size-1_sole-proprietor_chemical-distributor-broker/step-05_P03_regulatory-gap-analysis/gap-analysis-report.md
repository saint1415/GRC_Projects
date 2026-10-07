# Regulatory Gap Analysis: Cris Santos Company | Chemical | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (specialty chemical distributor, broker) |
| Tier / Vertical | Sole Proprietorship / Chemical (NAICS 424690) |
| Primary regulation (binding) | DOT Hazardous Materials Regulations: transportation security plan (49 CFR 172.800-172.804) and training (172.702-172.704), with the registration, shipping paper, and emergency response information duties that run through the SaaS stack (107.601-107.620; 172.201; 172.204; 172.602; 172.604) |
| Benchmark (voluntary) | CFATS risk-based performance standards 6 CFR 27.230(a)(5), (a)(6), (a)(8), (a)(15)-(16) (C-CHEMICAL-R01) |
| State law | Fla. Stat. 501.171 (driver identity data and customer records) |
| Assessment dates | 2026-09-08 to 2026-09-11 (self-assessment); G-011 updated 2026-09-14 after the ERI provider call |
| Assessor | Owner, with the on-call IT technician. Evidence is self-attested, checked on screen where possible |
| Regulatory status checked | 2026-09-25 to 2026-10-02 (eCFR point-in-time 2026-09-23, Federal Register, Florida Legislature statutes site) |
| Adopted | 2026-10-05 |

## 1. Applicability
**Why not CFATS RBPS 8 as the primary regulation.** The vertical registry names CFATS RBPS 8 (a voluntary benchmark) as the default. It cannot be the primary rule here. CFATS reaches a "chemical facility", an establishment that possesses a chemical of interest (6 CFR 27.105). A drop-ship broker possesses nothing, and CFATS authority lapsed on 2023-07-28 in any case. The rule that binds this business today is the DOT HMR. RBPS items are kept as a short voluntary benchmark (G-030 to G-033), because the theft and diversion thinking behind them fits a seller of 50% hydrogen peroxide.

**1. DOT HMR: applies.**
- **Offeror.** The owner determines the hazard class, prepares the shipping paper, and provides emergency response information for every drop shipment. Those are pre-transportation functions (171.1(b)(1), (7), (8)), so the business is an offeror (171.8). The supplier is also an offeror for filling, marking, labeling, placarding, and loading. "There may be more than one offeror," and each is responsible for the functions it performs (171.2(b)).
- **Training.** The owner is treated as a self-employed hazmat employee of a hazmat employer that causes hazmat to be transported (171.8). This is an **author interpretation** of the self-employed wording in 171.8, applied conservatively. The training rules in 172.702 and 172.704 follow.
- **Security plan: required.** 172.800(b)(10) covers "a large bulk quantity of a Division 5.1 material in Packing Groups I and II", and "large bulk quantity" means more than 3,000 liters in a single packaging such as a cargo tank. The business offers about 6 cargo tank loads a year of UN2014, hydrogen peroxide 50%, Division 5.1, PG II, at about 15,140 L each. Totes (about 1,041 L) would not trigger the plan on their own. The Class 8 products are not listed, because Class 8 appears only for PG I in large bulk (172.800(b)(16)).
- **Registration: required.** Bulk packagings of 13,248 L (3,500 gal) or more and placarded quantities (107.601(a)(4), (a)(6)).
- **There is no size exemption.** The only exception in 172.800(c) is for certain farmers.

**2. Not applicable, with reasons (5 rows).**
- **CFATS** (G-002): the business has no facility, and the authority is lapsed.
- **EPA RMP** (G-003): "stationary source" excludes transportation, including storage incident to transportation (40 CFR 68.3). The business holds no inventory, and **OSHA PSM** also needs a process and employees.
- **USCG MTSA cyber rule** (G-004): the business has no MTSA facility (33 CFR 101.605).
- **CIRCIA** (G-005): it is only proposed. As proposed, the business would be far below the SBA standard of 175 employees.
- **172.804** (G-029): the option to use another plan is not used.

**3. Florida: applies.** Fla. Stat. 501.171(1)(b) names a sole proprietorship as a covered entity. About 140 driver names with license numbers sit in email, so 501.171(2) (reasonable security), (3) to (6) (breach notice), and (8) (disposal) apply.

**Also checked, not applicable:** DEA listed chemicals. The product line excludes 21 CFR 1310.02 chemicals; hydrochloric acid, sulfuric acid, and potassium permanganate are listed there, and the owner declined to add the two acids.

## 2. Method
1. **Requirements.** HMR rows follow the regulation's own section and paragraph structure (public-domain CFR text, short quotes). CFATS benchmark rows use the 27.230(a) paragraph text. Florida rows follow the statute's subsections.
2. **Crosswalk.** Every CSF 2.0 and SP 800-53 mapping is an **author mapping**. No official NIST mapping exists for 49 CFR, 6 CFR Part 27, or Fla. Stat. 501.171.
3. **Evidence.** Self-attested. Where possible it was checked on screen with the IT technician: a sample of 10 BOLs from 2026, the ERI product list, training and registration certificates, email security settings, and the 2026 near-miss messages.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gaps are rated with the P01 scale.

## 3. Results summary
| Source | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| HMR applicability (Part 171) | 0 | 1 | 0 | 0 | 1 |
| Other regimes checked (CFATS, RMP, MTSA, CIRCIA) | 0 | 0 | 0 | 4 | 4 |
| HMR registration (Part 107 Subpart G) | 1 | 1 | 0 | 0 | 2 |
| HMR shipping papers and ERI (Part 172 Subparts C and G) | 3 | 3 | 0 | 0 | 6 |
| HMR training (Part 172 Subpart H) | 0 | 4 | 2 | 0 | 6 |
| HMR security plan (Part 172 Subpart I) | 0 | 2 | 7 | 1 | 10 |
| CFATS RBPS voluntary benchmark | 0 | 2 | 2 | 0 | 4 |
| Fla. Stat. 501.171 | 0 | 2 | 1 | 0 | 3 |
| **Total** | **4** | **15** | **12** | **5** | **36** |

Of the 27 gaps (Partially met or Not met), **6 are High**, 13 are Moderate, and 8 are Low.

**Reading the results.** The paperwork the business handles every day is mostly sound: registration, the ERI contract, the shipper's certification, and the emergency response information are Met. The failures are in two places. First, the **security plan never existed** (7 of the 12 Not met rows). Second, the **email account** sits where theft and diversion, cyber, and the plan's unauthorized-access element meet (G-023, G-031, G-032). Fixing email MFA and writing the call-back rules into the plan addresses all three.

## 4. Action list (half page)
In order. The first four cost nothing and take under a day.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Adopt HSP-01 hazmat transportation security plan with its risk assessment, designated official, and duties; no bulk hydrogen peroxide release until it is in use | G-020, G-021, G-022, G-025, G-026, G-027 | High | 2026-10-05 (done) |
| 2 | Email MFA, unique passphrase, password manager | G-032, G-034 | High | 2026-10-15 |
| 3 | Pickup number only via portal or phone; call-back on any change; supplier hold-release instruction; know-your-customer steps for hydrogen peroxide | G-023, G-031 | High | 2026-10-31 |
| 4 | Recurrent HMR course with test, plus a social engineering and payment-fraud module | G-014, G-015, G-016, G-018 | High | 2026-10-31 |
| 5 | Locked product description sheet; new-product checklist with ERI confirmation; no AI-drafted hazmat descriptions | G-008, G-011 | Moderate | 2026-10-31 |
| 6 | Record and report suspicious orders; P08 notification matrix | G-033, G-035 | Moderate | 2026-10-31 |
| 7 | In-depth security training on HSP-01 with a written test | G-017 | Moderate | 2026-11-30 |
| 8 | Backup of the email and file suite; complete BOL, registration, and training records | G-007, G-013, G-019, G-028 | Moderate | 2026-11-30 |
| 9 | Approved bulk carrier list, delivery confirmation, overdue-load escalation | G-024, G-030 | Moderate | 2026-11-30 |
| 10 | Driver data minimization and purge; electronic disposal and device wipe | G-034, G-036 | Moderate | 2026-12-31 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
None of these is treated as a current obligation.
- **HM-215R international harmonization NPRM** (91 FR 5996, 2026-02-10; comments closed 2026-04-13). It proposes changes to proper shipping names, hazard classes, packing groups, and special provisions. No final rule had been published by 2026-10-02. Whether it changes any of the five product entries was not checked. When a final rule is published, recheck the product description sheet (G-008).
- **CIRCIA final rule** (proposed 6 CFR Part 226). Not published as of 2026-10-02. As proposed, the business would not be covered.
- **CFATS reauthorization.** Not enacted. Even if it is, the business has no facility to register.
- **Recent final HMR amendments.** PHMSA published several final rules on 2026-08-04, for example 91 FR 49301 (107.620 recordkeeping) and 91 FR 49332 (the farmer exception amount in 172.800(c)). The eCFR text used here (point-in-time 2026-09-23) already includes them.
