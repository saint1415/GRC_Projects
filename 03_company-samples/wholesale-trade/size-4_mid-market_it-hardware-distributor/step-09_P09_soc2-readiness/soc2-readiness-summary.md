# SOC 2 Readiness Summary: Cris Santos Company | Wholesale Trade | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed IT hardware and software wholesale distributor) |
| Tier / Vertical | Mid-Market / Wholesale Trade |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1), Processing Integrity (PI1) |
| Target report | SOC 2 **Type 2** on the Partner Commerce Platform, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30 |
| Part A | Company readiness assessment (`soc2-readiness.csv`, 61 criteria) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`, 8 reviews) |
| Prepared | 2026-09-15 by the vCISO and the Security Manager with the Vice President of Sales Operations, using P02, P05, and P07 evidence |

## 1. Why SOC 2 for this organization
A distributor is not usually seen as a SOC 2 service organization. The **Partner Commerce Platform** changes that: about 9,600 users at 4,200 reseller accounts see contract pricing, place orders, and receive invoices through the portal, 60 large resellers submit orders through the order API, and 140 trading partners exchange EDI documents. About 80% of order lines arrive this way, so the company's controls over the platform affect its customers' own operations and financial reporting.

**Customer demand.** Three national resellers asked in 2026-05 for a SOC 2 Type 2 report on the platform. One made it a condition of its 2028 contract renewal. They asked for Security and Availability; the company added **Confidentiality** (contract pricing is the most sensitive data the platform holds) and **Processing Integrity** (resellers rely on order, pricing, and ship notice accuracy).

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 and this assessment found gaps in reseller authentication, privileged access, monitoring, recovery testing, and vendor oversight. Starting the observation period before they close would produce exceptions. The plan is to remediate through 2027 Q1 and observe from 2027-04-01.

**Alternatives considered:**
- **Type 1 first:** offered for 2027-03-31 as an interim report; the 3 resellers accepted this plan with quarterly status updates.
- **CMMC Level 2 certification (2027):** covers the enclave and the FIL, which are deliberately outside the platform. It does not answer the resellers' question.
- **Security questionnaires only:** acceptable to smaller resellers, but not to the 3 national resellers. The vertical overlay names no other assurance alternative for wholesale trade.
- **Privacy category:** out of scope. The platform serves businesses; the only personal information is reseller user contact details, covered under Security and Confidentiality.

**Service auditor independence.** The examination will be performed by a CPA firm that is not the co-sourced internal audit firm, so the P07 work does not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Reseller ordering, contract pricing, order status, invoices, the order API, and EDI order and ship notice exchange |
| Infrastructure | The portal and EDI tenants (vendor SaaS), integration services in the workloads account, the ERP order and pricing modules, the WMS ship confirmation interface, the identity provider, and the landing zone controls in P04 |
| Software | Portal and API (vendor), API gateway and middleware (company), ERP (vendor), WMS (company-managed) |
| People | Vice President of Sales Operations (platform owner), 6 platform administrators, the EDI team, customer service, IT and security, the MSSP |
| Data | Reseller users, contract pricing, orders, ship notices, invoices. Card payments use the portal vendor's hosted payment page, outside the company's systems. Federal orders are excluded from the portal by the ERP sync rule |
| Procedures | POL-01 to POL-05, the standards index, and the P08 runbooks |
| Subservice organizations (carve-out) | Portal vendor, ERP vendor, EDI provider, cloud provider, identity provider, MSSP. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls listed in the system description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 14 | 14 | 5 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **17** | **20** | **6** | **18** |

**Ready (17):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2, CC5.1;
- monitoring of controls: CC4.1, CC4.2;
- access and transmission: CC6.2, CC6.5, CC6.7, CC6.8;
- event evaluation: CC7.3;
- capacity and processing: A1.1, PI1.2, PI1.5.

**Not ready (6):**
- CC6.1: reseller MFA is optional, and credential stuffing took over 11 reseller accounts in 2026-04 (POAM-026);
- CC6.3: standing ERP administrators and annual reviews (POAM-002, POAM-003);
- CC7.2: portal, ERP, and API logs are not monitored (POAM-007);
- CC7.5 and A1.3: integration services and order-queue replay have never been restore-tested (POAM-011);
- CC9.2: 9 of 22 Tier 1 vendor reviews are overdue (POAM-019).

Each Not ready criterion maps to a P07 POA&M item. The Partially ready criteria mostly depend on standards being issued (P06), a written system description, and daily processing reconciliations.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.3 (system description), CC3.3, CC3.4, CC6.4, CC7.2 (portal and ERP logs), CC8.1, CC9.1, C1.1, PI1.1, PI1.3, PI1.4, CC1.4 | System description draft; ship-to alerts; vendor release reviews; badge reconciliations; SIEM use cases; second-reviewer change tickets; daily reconciliation sign-offs |
| 2027 Q1 | CC6.1 (reseller MFA), CC6.3, CC5.2, CC5.3, CC6.6, CC7.1, CC7.4, CC7.5, CC9.2, A1.3, CC2.1, C1.2, CC1.2 | MFA enforcement report; quarterly reviews; access broker logs; tabletop reports; restore tests; vendor reviews; standards |
| 2027-03-31 | Type 1 (design) report as an interim deliverable | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence (quarterly reviews, monthly scans, daily reconciliations, restore tests, vendor reviews) |
| 2027 Q2 | A1.2 (ERP recovery terms at renewal) | Amended ERP contract |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee and the 3 resellers.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 8 Common/Inherited and 30 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based and is the core of STD-03.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Holds CUI, FCI at scale, or contract pricing; privileged access to company systems; or supports a High-criticality BIA process | SOC 2 Type 2 (or FedRAMP authorization for CUI services) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No company data and no system access | Contract terms only | At renewal |

Of about 180 vendors with system or data access, 22 are Tier 1. 13 Tier 1 reviews were current at fieldwork; the CSV holds the 7 Tier 1 reviews completed in 2026-09 (including 3 that had been overdue) and 1 Tier 2 example. The remaining 6 overdue Tier 1 reviews are due by 2027-03-31 (POAM-019).

**Key findings:**
1. **Portal vendor:** unqualified Type 2 with one change-approval exception; its RTO of 4 hours and RPO of 1 hour **meet the BIA**. The company's own CUEC (reseller MFA) is the gap that matters.
2. **ERP vendor:** unqualified Type 2, but the contract RTO of 24 hours **does not meet** the 6-hour BIA need for order management, and the ERP must never hold CUI (no FedRAMP equivalency).
3. **MSSP:** missed the 30-minute escalation in 2 of 40 samples; the company has no customer responsibility matrix for it as an External Service Provider.
4. **TMS vendor:** only a Type 1 report and no recovery commitment, which supports keeping R-016 open.
5. **Forecasting platform:** acceptable report, but the company sends it FCI without FAR 52.204-21 terms; the feed filter is due 2026-10-15 (P10).
