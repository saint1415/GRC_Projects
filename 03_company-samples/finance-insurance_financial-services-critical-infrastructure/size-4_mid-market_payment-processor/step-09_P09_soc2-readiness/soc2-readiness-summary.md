# SOC 2 Readiness Summary: Cris Santos Company | Financial Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed payment processor serving merchants) |
| Tier / Vertical | Mid-Market / Financial Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Tiered vendor SOC 2 and AOC review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-11 by the vCISO and the Director of Information Security, using P02, P05, P06, and P07 evidence; approved by the COO 2026-09-15 |

## 1. Why SOC 2 for this organization
The company **is a service organization**: it performs authorization, clearing, settlement, and funding services for merchants, ISV partners, and both sponsor banks. Three groups asked for a SOC 2 Type 2 report:
- **Both sponsor banks**, in their 2026 annual due diligence. Each bank oversees its service providers under its own information security guidelines (12 CFR 30 App. B for Bank A; 12 CFR 364 App. B for Bank B) and the examination clause in its sponsor agreement (12 U.S.C. 1867(c)). Both asked specifically about availability and settlement accuracy after the 2026-02-21 DR test.
- **The 5 largest ISV partners**, whose own customers ask about the payments embedded in their software.

**PCI DSS remains the main assurance for card data.** The combined annual ROC and AOC by a QSA, at Visa service provider Level 1, is what the card brands and both banks require for account data. SOC 2 does not replace it. SOC 2 adds what PCI DSS does not report on: availability commitments, processing integrity of clearing, settlement, and funding, and confidentiality of merchant information.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in Cloud B access and monitoring, recovery, and vendor oversight. Starting the observation period before those are fixed would produce exceptions. The plan is to remediate through 2027 Q1, then run a 6-month observation period from 2027-04-01.

**Alternatives considered** (the vertical's assurance options):
- **PCI DSS AOC alone.** Already given to every customer; it does not cover availability or settlement accuracy, which the banks asked about.
- **SOC 1 (controls relevant to user entities' financial reporting).** Relevant if the banks' or large merchants' auditors rely on the company's settlement and funding controls for their financial statements. Bank A's internal audit has asked about it for 2028. Most PI1 controls in this checklist would carry over; the company will decide by 2027-06-30 whether to add a SOC 1 Type 2 for the settlement services.
- **Type 1 first.** Offered to both banks as an interim report as of 2027-03-31. Both accepted the plan with quarterly status updates.

**Service auditor independence.** The SOC 2 examination will be performed by a CPA firm that is neither the co-sourced internal audit firm (P07) nor the QSA firm, so that neither earlier role creates an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Card authorization (both platforms), hosted payment page and hosted payment fields, token vaults and recurring billing, clearing and settlement, merchant funding, reconciliation, chargebacks, merchant and partner portals |
| Infrastructure | The Payment Processing Platform (P02): the Cloud A landing zone (P04), Cloud B, and both colocation cages |
| Software | Authorization switch and gateways, Integrated Payments gateway, settlement and funding engine, managed file transfer, portals, fraud model serving |
| People | 600 employees; key roles in `../00_company-facts.md` section 2; the MSSP |
| Data | Account data (encrypted in both token vaults and the settlement database), transaction and settlement records, funding files, merchant owner information, security logs |
| Procedures | POL-01 to POL-05 and the standards index (P06), both P08 runbooks, settlement and reconciliation procedures |
| Subservice organizations (carve-out) | Cloud A provider (including the payment HSM service), Cloud B provider, both colocation providers, the MSSP, the identity and PAM vendor, the content delivery service. Their controls are covered by their own reports and the complementary subservice organization controls listed in the company's system description |
| External parties (not subservice organizations) | Card networks and both sponsor banks |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 17 | 5 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **15** | **22** | **6** | **18** |

**Why Privacy is out of scope.** The company processes cardholder and merchant owner information to deliver services to merchants and the sponsor banks. Privacy notices, consent, and access requests for cardholders are commitments of merchants and issuers, and no customer asked for the Privacy category.

**Ready (15):**
- governance and risk: CC1.1, CC1.2, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2;
- monitoring: CC4.1, CC4.2;
- control design: CC5.1;
- transmission: CC6.7;
- capacity: A1.1;
- processing integrity: PI1.1 to PI1.3. Daily three-way reconciliation is the company's strongest area, because the card networks and both banks reject bad files.

**Not ready (6):**
- CC3.4: the acquisition and the interconnect change were not assessed;
- CC6.3: standing Cloud B administrator roles and no service account reviews;
- CC6.8: no script integrity on the hosted payment fields; unsupported settlement servers;
- CC7.2: Cloud B is not monitored;
- CC7.5 and A1.3: recovery tests missed their RTOs, and the gateway has never been tested.

Each maps to a P07 POA&M item. These are the same weaknesses as the Very High and High risks in P01, so fixing them for the ROC also fixes them for SOC 2. The Partially ready criteria mostly depend on Cloud B reaching the core platform's level and on the P06 standards being issued.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments and covered services), P06 (policies and standards), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 (before the ROC) | CC2.1, CC3.4, CC6.1, CC6.2, CC6.3, CC6.5, CC6.6, CC6.8 (hosted payment fields), CC7.2, CC7.4, C1.2 | Combined scope confirmation; Cloud B PAM and SIEM onboarding records; access review records; script inventory and tamper alerts; portal MFA settings; archive purge record; tabletop report |
| 2026 Q4 to 2027 Q1 | CC1.4, CC3.3, CC5.2, CC5.3, CC6.4, CC7.1, CC7.3, CC8.1, CC9.2, A1.2, C1.1, PI1.5 | Training records; standards; drift and patch reports; escort sign-offs; change tickets with second approver; AOCs and matrices; recording pause logs; DR key ceremony record |
| 2027 Q1 | CC7.5, CC9.1, A1.3, PI1.4, CC2.3, CC6.8 (server replacement under way) | Automated failover test; settlement DR test with both banks; signed funding files; ISV responsibility matrix |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to both banks and the ISVs | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly scans, restore tests, vendor reviews, reconciliations) |
| 2027 Q2 | CC6.8 (unsupported servers retired by 2027-06-30) | Decommission records |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee and both sponsor banks.

## 5. Vendor SOC 2 and AOC review program (Part B)
The company relies on provider controls for many inherited controls (P02: 5 Common/Inherited and 54 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based. It is the core of STD-07.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Stores, processes, or transmits account data or can affect a CDE (PCI DSS service provider), or supports a High-criticality BIA process | PCI DSS AOC with responsibility matrix (or inclusion in the company's ROC) and, where relevant, SOC 2 Type 2 plus bridge letter; review of opinion, scope, subservice organizations, exceptions, complementary user entity controls mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Confidential data (for example merchant owner NPI) but no account data or CDE influence; supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No Confidential data and no system access | Contract terms only | At renewal |

Of 182 vendors, the 34 PCI DSS service providers are Tier 1, about 50 are Tier 2, and the rest are Tier 3; the 41 acquired vendors are being tiered by 2026-12-31 (POAM-016). The CSV holds the first 8 Tier 1 reviews and 1 Tier 2 example. The remaining Tier 1 reviews are due by 2026-12-31.

**Key findings:**
1. **Complementary user entity controls are where the gaps are.** Every unqualified provider report depends on controls the company must run: IAM, MFA, key policies, network rules, and logging. On Cloud B several of those are open (POAM-002, POAM-003, POAM-006). **The providers' controls protect the company only once those gaps close.**
2. **Recovery is the company's job, not the providers'.** Both cloud providers commit to zone-level resilience and both colocation providers met their facility commitments. The RTO misses in P05 come from the company's own runbooks.
3. **The contact center vendor has no AOC.** Recordings have held card verification codes, which makes the vendor a service provider that can affect account data. Either obtain an AOC or remove card data from recordings by design, then reassess its tier.
4. **The MSSP's SIEM platform is carved out.** The platform provider's own SOC 2 must be obtained, and the MSSP's scope must extend to Cloud B.
5. **Cloud B's responsibility matrix belongs to the acquired company.** It must be re-signed in the company's name before the combined ROC.
