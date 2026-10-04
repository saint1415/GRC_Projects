# SOC 2 Readiness Summary: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed diversified precision-agriculture crop farm with a central packinghouse and a Grower Services unit) |
| Tier / Vertical | Mid-Market / Agriculture, Forestry, Fishing and Hunting |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1) |
| Target report | SOC 2 **Type 2** for Grower Services, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30, ahead of the growers' 2027-12-31 request |
| Part A | Company readiness assessment for Grower Services (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-15 by the vCISO and the Security Manager with the Vice President of Grower Services, using P02, P05, P06, and P07 evidence |

## 1. Why SOC 2 for this organization
A crop farm that sells its own produce is not a SOC 2 service organization. **Grower Services** changes that. For about 30 independent contract growers the company packs, grades, cools, ripens, and markets produce, monitors irrigation for 18 of them, and computes and pays a weekly pool settlement of about $900,000 in season. Growers see field data, grades, pack-out, and statements in the grower portal (SYS-12). For those services the company is a service organization, and its controls affect the growers' financial results and their data.

**Who asked, and for what:**
- The **contract growers' association** asked for an independent report on the portal and settlement service, covering security, availability of irrigation alerts, the accuracy of settlements, and the confidentiality of each grower's yields and prices.
- **Two lenders** that finance growers against expected settlement payments asked for the same report, because their collateral depends on settlement accuracy and timing.
- PACA makes the accounting duty concrete: as a growers' agent, the company must keep auditable records of packing and grading results and render accurate, detailed accountings that show how pool costs and prices are computed (7 CFR 46.32(b); P03 G-128). **Processing Integrity** is therefore the category that matters most to these users.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 and this assessment found gaps in change control over settlement code, input reconciliation, access reviews, recovery testing, and vendor oversight of the development firm. Starting the observation period before those are fixed would produce exceptions or a qualified opinion. The plan is to remediate through 2027 Q1 and start a 6-month observation period on 2027-04-01.

**Alternatives considered:**
- **Type 1 first (point in time), as of 2027-03-31:** offered to the association and the lenders as an interim report; both accepted the plan with quarterly status letters.
- **Agreed-upon procedures on settlements only:** cheaper, but gives no opinion on security or availability, and the lenders asked for SOC 2.
- **Security questionnaires:** not acceptable to the lenders.
- **SOC 1:** relevant if growers' auditors rely on settlement controls for financial statement audits. Not requested now; the Processing Integrity work would support a SOC 1 later.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so the internal audit work in P07 does not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Grower irrigation monitoring and agronomy alerts (BP-11); grower pack-out reporting and weekly pool settlement (BP-12), including the grading and receiving inputs to settlement |
| Infrastructure | Grower Services workloads account (portal containers, settlement database, WAF, secrets manager); shared services and identity and security accounts as they support it; backup account (P04); packinghouse receiving and optical graders as settlement inputs |
| Software | Grower portal and settlement service (company-owned code built by the development firm); ERP interface for sales prices; grader software |
| People | Vice President of Grower Services, 4 agronomists, 3 settlement analysts, the Controller, the Packinghouse Manager for grading, IT and security staff, the MSSP, the vCISO |
| Data | Grower business data (yields, grades, prices, settlements), grower bank details, grower soil probe and flow data |
| Procedures | POL-01 to POL-05; STD-03, STD-07, STD-11; the settlement run procedure; P08 runbooks |
| Subservice organizations (carve-out) | Cloud provider, identity provider, MSSP and its SIEM platform, ERP vendor, and the development firm. Their controls are covered by their own reports or contract terms, and the complementary subservice organization controls will be listed in the system description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A | Total |
|---|---|---|---|---|---|
| Security (CC1-CC9) | 10 | 19 | 4 | 0 | 33 |
| Availability (A1) | 2 | 0 | 1 | 0 | 3 |
| Confidentiality (C1) | 0 | 2 | 0 | 0 | 2 |
| Processing Integrity (PI1) | 0 | 3 | 2 | 0 | 5 |
| Privacy (P1-P8) | 0 | 0 | 0 | 18 | 18 |
| **Total** | **12** | **24** | **7** | **18** | **61** |

**Ready (12):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC3.1, CC3.2;
- monitoring and control design: CC4.1, CC4.2, CC5.1;
- physical and transmission: CC6.4, CC6.7;
- availability: A1.1 (capacity) and A1.2 (write-once backups in a separate account, confirmed by the P07 restore test).

**Not ready (7):**
- CC6.3: annual access reviews and standing administrator rights;
- CC7.5 and A1.3: portal and settlement restore never tested;
- CC8.1: the development firm deploys without company approval or regression tests;
- CC9.2: no security terms or assurance from the development firm; 10 Tier 1 vendors not reviewed;
- PI1.2: grader output is not reconciled to packed cases;
- PI1.3: settlement logic changes are not independently reviewed.

Each maps to a P07 POA&M item: POAM-001, POAM-002, POAM-011, POAM-016, POAM-017, and POAM-023. Privacy is N/A because no user entity asked for it; worker and customer privacy is handled by the security and HR programs.

**Mapping to other work.** Evidence is reused from P02 (control statements), P04 (cloud control map), P05 (service commitments: 99.5% monthly alert availability in season and the Tuesday statement and Wednesday payment schedule), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | PI1.2, PI1.4, CC2.1, CC3.3, CC6.2, CC6.5, CC7.3, CC7.4, CC9.1, C1.1, C1.2 | Weekly grade-to-case reconciliations and hand-grade audits; Controller sign-off of each settlement run; bank-change call-back log; grower user verification; tabletop report (2026-11-10); data inventory; export purge log |
| 2027 Q1 | CC1.2, CC1.4, CC2.2, CC2.3, CC3.4, CC5.2, CC5.3, CC6.1, CC6.3, CC6.6, CC6.8, CC7.1, CC7.2, CC7.5, CC8.1, CC9.2, A1.3, PI1.1, PI1.3, PI1.5 | Pipeline approval records and scan results; regression test reports; quarterly access reviews; privileged session logs; restore test record; settlement specification; vendor reviews and signed terms; standards |
| 2027-03-31 | Type 1 report (design) as an interim deliverable to the growers' association and lenders | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence: weekly reconciliations, settlement sign-offs, change approvals, quarterly reviews, monthly scans, quarterly restore tests, vendor reviews |
| 2027-11-30 | Type 2 report issued | Report and bridge letter process |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee, the growers' association, and the two lenders.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 7 Common/Inherited and 33 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of the vendor risk standard (STD-03).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Privileged or OT access to company systems, personal information at scale, or support for a High-criticality BIA process | SOC 2 Type 2 (or an equivalent independent assessment; where none exists, a questionnaire, on-site review, and contract security schedule) plus a bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No data and no system access | Contract terms only | At contract renewal |

Of about 110 vendors, 38 have access to company data or systems. Under this approach **14 are Tier 1**: the FMIS vendor, cloud provider, identity provider, MSSP, productivity suite vendor, ERP and EDI vendor, HR and payroll provider, SCADA integrator, pivot manufacturer, development firm, cold-chain alarm service, refrigeration contractor, equipment dealer (telematics), and SD-WAN service provider. **The 4 Tier 1 reviews completed in 2026** are the FMIS vendor, MSSP, identity provider, and cloud provider (VEN-01 to VEN-04). The CSV also records the status of 4 more Tier 1 vendors (VEN-05 to VEN-08) and 1 Tier 2 example (VEN-09). The remaining 10 Tier 1 reviews are due by 2027-03-31 (POAM-016).

**Key findings:**
1. **FMIS vendor:** unqualified Type 2. Its stated RTO of 8 hours **does not meet the 4-hour harvest RTO** in the BIA (P05 finding 3). Three of the CUECs the company must operate are open gaps: user management on crew tablets (POAM-001), audit trail review (POAM-005), and company-held exports (POAM-022). **The vendor's controls protect the company's records only once those gaps close.**
2. **MSSP:** unqualified Type 2 (Security only), with an exception for missed 30-minute escalations in 2 of 40 samples. The SIEM platform is carved out; its own report must be obtained. Log source coverage is the company's CUEC and excludes OT.
3. **SCADA integrator, pivot manufacturer, and development firm:** no SOC 2 reports exist. These three hold the most dangerous access (R-002, R-014, R-045), so they get questionnaires, on-site review, and contract security schedules now, and the development firm must be described as a subservice organization in the company's own SOC 2.
4. **HR and payroll provider:** report requested; it is a third-party agent under Fla. Stat. 501.171(6), so breach notice terms matter as much as the report.
5. **Agronomy analytics vendor (Tier 2):** its click-through terms allow secondary use of company and grower data; negotiated terms are a P10 condition (R-028).
