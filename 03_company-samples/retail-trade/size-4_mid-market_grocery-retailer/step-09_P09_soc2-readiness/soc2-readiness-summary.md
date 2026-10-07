# SOC 2 Readiness Summary: Cris Santos Company | Retail Trade | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional grocery retailer: 5 supermarkets, online ordering, a distribution center) |
| Tier / Vertical | Mid-Market / Retail Trade |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service in scope | **Supplier Offers and Retail Media service** (supplier-funded digital offers, sponsored placements, redemption reporting, and supplier billing) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1), Processing Integrity (PI1) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30, ahead of the suppliers' 2027-12-31 deadline |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor assurance review program: SOC 2 reports and PCI DSS AOCs (`vendor-assurance-review.csv`) |
| Prepared | 2026-09-04 by the vCISO and the Security Manager, using P02, P05, P06, and P07 evidence (fieldwork 2026-08-24 to 2026-09-04) |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Why SOC 2 for this organization
A grocery retailer sells to consumers, so it is usually **not** a SOC 2 service organization, and for card data its assurance is PCI DSS validation (P03). That changes for one part of the business:
- About 140 consumer goods suppliers fund digital coupons and sponsored placements. The company targets offers to loyalty members, reports redemptions through the supplier reporting portal, and bills suppliers about $3.1 million a year (P05 BP-10).
- Suppliers rely on the company's controls for three things: their confidential campaign and sales data stays separate from competitors' data, redemption figures and invoices are accurate, and the service is available when campaigns run.
- Two national suppliers' agreements (fictional) require a SOC 2 Type 2 report on the service by 2027-12-31, covering Security, Availability, Confidentiality, and Processing Integrity.

For this service the company is a service organization, so a SOC 2 Type 2 report is the right assurance tool. **It does not replace PCI DSS validation.** The store CDE and the checkout pages stay under the SAQ D and the QSA.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in access reviews, data transfers, recovery testing, and vendor oversight that would produce exceptions if the observation period started now. The plan is to remediate through 2027 Q1, then run a 6-month observation period from 2027-04-01.

**Alternatives considered:**
- **Type 1 first (point in time):** offered to the two suppliers as an interim report as of 2027-03-31. Both accepted the plan with quarterly status updates.
- **Supplier security questionnaires only:** acceptable to smaller suppliers but not to the two national suppliers' audit teams.
- **Privacy category:** not requested by the suppliers. Consumer privacy is handled under the FTC Act program (P03 G-069 to G-074) and P10, so the 18 Privacy criteria are marked N/A.

**Service auditor independence.** The SOC 2 examination will be performed by an independent CPA firm that is neither the co-sourced internal audit firm (P07) nor the QSA firm.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Supplier offer setup, targeting, redemption processing, supplier reporting, and supplier billing |
| Infrastructure | Cloud landing zone (P04): workloads account (loyalty and CDP database, data warehouse, supplier reporting portal, integration platform), shared services, identity and security, and backup accounts |
| Software | Pricing and offers engine (vendor SaaS), supplier reporting portal (company-built), data warehouse, ERP finance module for invoicing |
| People | Retail media team (4), e-commerce and analytics staff, IT and security team, MSSP, vCISO |
| Data | Supplier campaign and sales data (Confidential); pseudonymized member purchase data; redemption and billing records |
| Procedures | POL-01 to POL-05, the standards index, and the P08 runbooks |
| Out of scope | Store CDE and checkout pages (PCI DSS); store operations; the DC |
| Subservice organizations (carve-out) | Cloud provider, pricing and offers engine vendor, identity provider, MSSP, ERP vendor. Their controls are covered by their own SOC 2 reports (Part B) and the complementary subservice organization controls listed in the system description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 12 | 17 | 4 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 1 | 3 | 1 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **15** | **22** | **6** | **18** |

**Ready (15):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2;
- monitoring and control design: CC4.1, CC4.2, CC5.1;
- physical access, malware, and event evaluation: CC6.4, CC6.8, CC7.3;
- capacity and backup infrastructure: A1.1, A1.2;
- stored data: PI1.5.

**Not ready (6):**
- CC6.3: access reviews are semiannual, and a shared analyst account runs the weekly export;
- CC6.7: member-level data leaves by email, and supplier data was shared without approval;
- CC7.5 and A1.3: the service's cloud workloads have never been restored in a test;
- CC9.2: the offers engine vendor has no data use or security terms;
- PI1.3: redemptions are not reconciled to supplier invoices.

Each maps to a P07 POA&M item (POAM-001, POAM-003, POAM-008, POAM-012, POAM-018, POAM-023) or to P01 R-031. The Partially ready criteria mostly depend on standards being issued (P06), supplier-facing documentation, and processing integrity checks that do not exist yet.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments for BP-09 and BP-10), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.1, CC3.3, CC3.4, CC6.2, CC6.5, CC6.6, CC6.7, CC8.1, CC9.1, CC9.2, C1.1, PI1.1 | Data flow map; redemption fraud analysis; supplier user approvals; deletion certificates from the agency; portal penetration test report; governed transfer logs; change tickets for portal and offers engine; contingency plan; vendor amendments; separation test; documented processing objectives |
| 2027 Q1 | CC1.2, CC1.4, CC2.3, CC5.2, CC5.3, CC6.1, CC6.3, CC7.1, CC7.2, CC7.4, CC7.5, A1.3, C1.2, PI1.2, PI1.3, PI1.4 | Audit committee minutes; training records; supplier security schedule; standards; key rotation records; quarterly access reviews; scan and egress alert reports; tabletop reports; restore test records; offboarding checklist; campaign second checks; daily reconciliation reports |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to the two suppliers | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly scans, restore tests, daily reconciliations, vendor reviews) |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee and the two suppliers.

## 5. Vendor assurance review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 15 Common/Inherited and 29 Hybrid). PCI DSS Requirement 12.8 also requires a list of TPSPs, written acknowledgments, and an annual check of their compliance status. The program in `vendor-assurance-review.csv` covers both needs and is the core of STD-03.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Card data or CDE access (TPSP), customer data at scale (more than 10,000 people), privileged access, or support for a High-criticality BIA process or the supplier service | PCI DSS AOC for TPSPs; SOC 2 Type 2 (or equivalent) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited customer or employee data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No data and no system access | Contract terms only | At contract renewal |

Of about 85 vendors with data or system access, 16 are Tier 1 and about 30 are Tier 2 under this approach. The CSV holds the first 10 Tier 1 reviews. The remaining 6 Tier 1 reviews are due by 2027-03-31 (POAM-012).

**Key findings:**
1. **POS vendor:** only a SOC 2 Type 1 report and an expired PCI DSS AOC, while it holds standing access to the CDE. It is the riskiest vendor in the program (P01 R-006). A current AOC is due by 2026-10-31; otherwise the QSA will assess the vendor's services as part of the company's own SAQ D.
2. **SD-WAN provider:** AOC expired 2026-01-31. Together with the POS vendor and the tag management service, these are the 3 expired AOCs found in P03 (G-063).
3. **Pricing and offers engine vendor:** unqualified Type 2, Security only. It is a subservice organization for the SOC 2 scope, so the company needs Availability in its next report and data use, no-training, and deletion terms (P10 AI-001).
4. **ERP vendor:** unqualified Type 2, but its stated RTO of 24 hours **does not meet the BIA** for pricing (12 hours).
5. **E-commerce platform vendor:** unqualified Type 2 and a current AOC, but the report states plainly that checkout scripts and admin MFA are customer responsibilities. **The vendor's controls only protect the checkout once POAM-003 and POAM-013 close.**
6. **Marketing agency:** no independent assurance and no contract terms, yet it could publish checkout tags. The fix is to remove that right rather than to seek a report from a 2-person agency.
