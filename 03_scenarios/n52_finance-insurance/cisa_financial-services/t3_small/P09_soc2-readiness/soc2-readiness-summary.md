# SOC 2 Readiness Summary: Cris Santos Company | Financial Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (payment processor serving merchants) |
| Tier / Vertical | Small / Financial Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1), Processing Integrity (PI1) |
| Target report | SOC 2 Type 1 as of 2027-03-31, then Type 2 for the period 2027-04-01 to 2027-09-30 |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`) |
| Part B | Cloud provider SOC 2 Type 2 report and AOC review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager with the Compliance and Risk Manager; approved by the COO 2026-08-31 |

## 1. Why SOC 2 for this organization
The company **is a service organization**: it performs processing, settlement, and funding services for merchants, software-platform partners, and its sponsor bank. SOC 2 therefore fits its role. Three customers asked for it:
- **The sponsor bank**, in its 2026 annual due diligence. The bank oversees its service providers under its own information security guidelines (12 CFR 30 App. B, III.D) and the examination clause in the sponsor agreement (12 U.S.C. 1867(c)).
- **Two software-platform partners** that embed the hosted payment page and API in their products.

**PCI DSS remains the main assurance for card data.** The annual ROC and AOC by a QSA, at Visa service provider Level 1, is what the card brands and the sponsor bank require for account data. SOC 2 does not replace it. SOC 2 adds what PCI DSS does not report on: availability commitments, processing integrity of settlement and funding, and confidentiality of merchant information.

**Alternatives considered** (the vertical's assurance options):
- **PCI DSS AOC alone.** Already given to every customer. It does not cover availability or settlement accuracy, which the bank and partners asked about.
- **SOC 1 (controls relevant to user entities' financial reporting).** Relevant if the sponsor bank's or merchants' auditors rely on the company's settlement and funding controls for their financial statements. The bank has not asked for one. The company will revisit after the 2027 Type 1 if the bank's auditors request it. Many PI1 controls in this checklist would carry over.

**Why not a Type 2 now:**
- A Type 2 report tests controls that have operated over a period, typically 6 to 12 months.
- Many controls were defined or changed in August 2026.
- The ROC in November 2026 must come first.

The plan is a Type 1 in March 2027 and a 6-month Type 2 ending September 2027.

## 2. System description (scope)
- **Services:** card authorization (card-present and card-not-present), hosted payment page and API, token vault and recurring billing, clearing and settlement, merchant funding, chargebacks, and the merchant portal.
- **Infrastructure and software:** the Payment Processing Platform (SSP, P02) in one public cloud tenant, the payment HSM service, and the supporting SaaS (identity provider, SIEM, repository and pipeline).
- **People:** 60 employees; key roles in `../scenario-facts.md` section 2.
- **Data:** account data (PAN encrypted in the token vault), transaction and settlement records, merchant owner information, and security logs.
- **Procedures:** POL-01 to POL-05 (P06), the P08 runbook, and settlement and reconciliation procedures.
- **Subservice organizations (carved out):**
  - the cloud provider, including the payment HSM service (Part B)
  - the content delivery service
  - the fraud analytics vendor
  - the card networks and sponsor bank, as external parties

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 18 | 5 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |
| **Total (61)** | **14** | **23** | **6** | **18** |

**Why Privacy is out of scope.** The company processes cardholder and merchant owner information to deliver services to merchants and the sponsor bank. Privacy notices, consent, and access requests are commitments made by merchants and issuers, and no customer asked for the Privacy category.

**Ready (selected):**
- CC3.1 and CC3.2: objectives and a written risk assessment (P01)
- CC4.1 and CC4.2: annual QSA assessment, internal assessment, and POA&M
- CC6.4 and CC6.5: physical and media controls, inherited from the cloud provider
- CC6.6: boundary protection
- PI1.1 to PI1.3: processing specifications, input validation, and daily settlement reconciliation. This is the company's strongest area, because the card networks and sponsor bank reject bad files

**Not ready:**
- CC3.4: significant changes were not assessed
- CC6.3: repository tokens and service account privileges
- CC6.8: payment page script integrity
- CC7.2: after-hours and egress monitoring
- CC7.5 and A1.3: no recovery runbook or restore and failover tests

These are the same weaknesses as the High risks in P01 and the High POA&M items in P07. Fixing them for the ROC also fixes them for SOC 2.

## 4. Findings from the cloud provider report and AOC (Part B)
- **Opinion:** Type 2, unqualified. One exception (late access removals for provider staff), remediated by the provider.
- **Scope gap:** the data warehouse service was added after the report period and is not on the provider's AOC. That is acceptable only because the warehouse must never hold PAN. The 2026-08-05 finding (R-031) shows why the PAN block and monthly discovery (POAM-012) matter.
- **Complementary user entity controls.** The report lists controls the company must operate for the provider's controls to work: IAM users and roles, MFA, key policies, network rules, and logging. Two are open gaps at the company: account management (POAM-005) and least privilege for service accounts (POAM-006). **The provider's controls only protect the company once those gaps are closed.**
- **Availability.** The provider commits to zone-level resilience. Regional recovery is the company's own design, and it is not built yet (R-006).
- **Follow-ups:**
  - confirm the payment HSM service's second-region key replication
  - obtain an updated bridge letter before 2026-11-02
  - record the provider's security contact in P08

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q3-Q4 (before the ROC) | CC1.3, CC1.5, CC3.4, CC6.3, CC6.8, CC8.1, CC2.3, CC9.2 | Signed designation and charter, quarterly review records, scope confirmation, access review records, script inventory and tamper alerts, two-approval deployment records, responsibility matrices, AOCs |
| 2026 Q4 | CC7.2, CC7.3, CC7.4, CC1.2, C1.1, C1.2 | Managed detection tickets, DNS detection alerts, tabletop report, Qualified Individual report, PAN discovery results, retention schedule |
| 2027 Q1 | CC7.5, A1.2, A1.3, CC9.1, PI1.4, PI1.5 | Recovery runbook, restore test and reconciliation records, failover test report |
| 2027-03-31 | All in-scope criteria | Type 1 examination by a CPA firm |

**Response to the sponsor bank and partners:** send this summary, the readiness checklist, the 2025 AOC, and the POA&M (P07). Commit to the Type 1 report by 2027-04-30.
