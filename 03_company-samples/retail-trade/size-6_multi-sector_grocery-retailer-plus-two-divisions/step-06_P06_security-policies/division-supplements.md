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
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, payment page rule (POL-01 4.13), card data stays in the CDE | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, tag management standard, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards (for example, PIN pad inspections, OT vendor access, the FTC notice and Reg Z steps) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Grocery Retail | v2026 | 2026-06-15 (to the 2026 draft group policies) | Aligned; update for POL-01 4.13 (payment pages) due by 2026-12-30 (90 days after the effective date) | Add payment page ownership per page |
| Grocery Wholesale | v2026 | 2026-06-30 | Aligned, but the OT vendor access standard still allows always-on connections where a vendor contract requires them, which POL-02 4.10 now prohibits | Remove the contract exception by 2026-12-31 (POAM-014) |
| Financial Services | v2024 | 2024-04 | **Drifted** (scenario gap 11); conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-017) |

## 3. What each supplement adds
### 3.1 Grocery Retail supplement (Level 1 merchant; authorized SNAP retailer)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Payment pages | Each payment page (web checkout, app web view) has a named page owner who approves every script; the tag container for payment pages is separate from "all pages" containers | POL-01 4.13 | PCI DSS 6.4.3, 11.6.1 |
| PIN pads | Devices inspected at a frequency set by targeted risk analysis (daily at self-checkout from 2026-11); device list reconciled with the processor monthly; tampered devices bagged as evidence | POL-05 4.4 | PCI DSS 9.5.1 |
| Store back office | MFA for every store manager account, including the 46 acquired stores by 2026-11-15 | POL-02 4.3 | PCI DSS 8.4.2 |
| Rewards Card at checkout | The Rewards Card field follows the Financial Services protection standard until the isolated frame replaces it | POL-04 4.4 | 16 CFR 314.4(c)(2) |
| EBT | EBT skimming handled with the same playbooks as card skimming; state EBT processor contacts in the matrix | POL-03 4.1 | 7 CFR 278.1 (authorization) |
| Receipts | Receipt template tested in every POS release (last 4 digits, no expiration date) | POL-01 4.1 | 15 U.S.C. 1681c(g) |
| Affiliate data | CDP audiences built from Rewards Card data apply opt-outs daily and record the 12 CFR 1022.21(c) exception used | POL-04 4.5 | 12 CFR 1022.21 |

### 3.2 Grocery Wholesale supplement (distribution and Retailer Services Portal)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| OT vendor access | Vendor access only through group PAM, enabled per work order, recorded | POL-02 4.10 | NIST CSF 2.0 benchmark (PR.AA-05) |
| OT segmentation and inventory | Industrial demilitarized zone at each distribution center; OT asset inventory kept current | POL-01 4.6 | NIST CSF 2.0 benchmark (ID.AM-01, PR.IR-01) |
| Portal users | Named users per independent grocer; MFA required from 2027-03-31 | POL-02 4.11 | FTC Act Section 5 (portal terms) |
| Portal payment page | No shared tag container on the invoice payment page; tamper detection to the SOC | POL-01 4.13 | PCI DSS 6.4.3, 11.6.1; SAQ A eligibility |
| Customer notices | Notice to affected independent grocers within 72 hours of confirming an incident (supply agreement) | POL-03 4.5 | Supply agreements |
| Records | Traceability and shipment records retrievable within 24 hours, drilled quarterly | POL-04 4.6 | 21 CFR 1.361; 21 CFR 1.1455(c) |

### 3.3 Financial Services supplement (non-bank card issuer and lender)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Qualified Individual | The Financial Services CISO reports in writing to the Financial Services board at least annually, covering service providers, testing, and events | POL-01 4.2 | 16 CFR 314.4(a), (i) |
| Service providers | Safeguards-based review of the card processing platform each year, including complementary user entity controls in its SOC reports; group services treated as affiliate service providers | POL-01 4.8 | 16 CFR 314.4(f) |
| FTC notice | Notification event decision by the Qualified Individual; FTC notice within 30 days of discovery when 500 or more consumers are involved | POL-03 4.6 | 16 CFR 314.4(j) |
| Card compromise | Block and reissue; unauthorized charges handled as billing errors; $0 cardholder liability per the cardholder agreement | POL-03 4.6 | 12 CFR 1026.12(b), 1026.13 |
| Identity theft | Red Flags program updated each year for current fraud patterns | POL-01 4.3 | 16 CFR 681.1(d) |
| Credit models | Reason codes validated after every model change; fairness tests before release | POL-01 4.12 | 12 CFR 1002.9(b)(2) |
| Retention | Customer information disposed of within two years of last use unless needed | POL-04 4.8 | 16 CFR 314.4(c)(6) |

## 4. Financial Services drift: conflicts with 2026 group policy
The 2024 Financial Services standards were written before the 2026 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 FS-007; P07 PL-01a.01(b)).

| Topic | Financial Services standard (2024) | Group policy (2026) | Effect |
|---|---|---|---|
| Incident notices | Lists state breach laws only | FTC notice within 30 days; group matrix (POL-03 4.6) | 16 CFR 314.4(j) notice could be missed (FS-008) |
| Service provider review | SOC 1 report review only | Safeguards-based review each year (POL-01 4.8) | Card platform oversight incomplete (FS-003) |
| Affiliate data | Intercompany agreement only | Opt-outs to every audience system within 1 business day (POL-04 4.5) | Scenario gap 5 (FS-006) |
| AI and models | Model risk committee for credit only | AI inventory and Group AI Standard (POL-01 4.12) | Generative AI assistant not reviewed by the model committee (FS-015) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Scenario gap 9 (POAM-018) |
| Retention | Keep closed accounts indefinitely | Dispose within two years of last use unless needed (POL-04 4.8) | FS-009 |

**Why the drift happened.** The 2024 move of Financial Services security under the Group CISO left the supplement without a named owner or review date. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Grocery Retail, Grocery Wholesale) and on re-issue (Financial Services).
