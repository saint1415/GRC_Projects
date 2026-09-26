# SOC 2 Readiness Summary: Cris Santos Company | Wholesale Trade | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (IT hardware and software wholesale distributor) |
| Tier / Vertical | Small / Wholesale Trade |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Target report | None now: readiness self-assessment. A SOC 2 Type 1 of the reseller portal service will be considered for 2027-Q3 once the Not ready items close |
| Part A | Company readiness self-assessment for the reseller ordering portal (`soc2-readiness.csv`) |
| Part B | Portal vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager with the Sales Operations Manager |

## 1. Why SOC 2 for this organization
A wholesale distributor is not usually thought of as a SOC 2 service organization. The reseller ordering portal changes that for one service: about 1,100 users at reseller customers rely on it to see their contract pricing, place orders, and download invoices, so the company's controls over the portal affect their operations.

**A. Customer assurance request.** Two of the company's largest reseller customers asked in 2026-06 for evidence of security and availability controls over the portal, using the Trust Services Criteria as the yardstick. The company will answer with this readiness self-assessment, the portal vendor's SOC 2 Type 2 report (under its sharing terms), and a remediation plan, **not** a CPA-issued SOC 2 report.

Why not a formal SOC 2 audit now:
- A Type 2 audit needs controls that have operated over a period, typically 6 to 12 months. Most company-side portal controls were defined in August 2026.
- The resellers asked for evidence, not a report.
- The security budget for 2026 Q4 and 2027 Q1 is committed to CMMC Level 2, which is a condition of DoD revenue.

Other options considered:
- **A security questionnaire:** both resellers accepted the TSC-based format instead.
- **CMMC Level 2 certification (2027):** it will cover the CUI enclave, not the portal, which is deliberately kept out of the CUI scope. It does not answer the resellers' question.

**B. Third-party risk management.** The portal is vendor SaaS. The vendor's SOC 2 Type 2 report is the evidence for the portal's infrastructure and application controls (inherited in P02 and P04). The company reviews it every year (SA-9, CC9.2).

## 2. System description (scope)
- **Service:** the reseller ordering portal (SYS-03): catalog, contract pricing, ordering, order status, and invoices, with a two-way sync to the ERP (SYS-01).
- **Infrastructure and software:** the vendor-hosted portal; the company's portal configuration (roles, pricing rules, sync mapping); the ERP integration; company endpoints and identity provider used by the 5 portal administrators.
- **People:** the Sales Operations Manager (business owner), 5 portal administrators, 4 customer service staff, the IT Manager, and the portal vendor.
- **Data:** reseller user accounts, contract pricing, orders, and invoices. Card payments use the vendor's hosted payment page, outside company systems. DoD orders are excluded from the portal by the ERP sync rule (to be confirmed by 2026-10-31, P01 R-018).
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 19 | 4 | 0 |
| Availability (A1, 3) | 0 | 2 | 1 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles and reporting lines are set
- CC3.1 to CC3.3: objectives, risk assessment, and fraud risk (reseller account takeover and payment fraud are in P01)
- CC4.2: deficiencies are tracked in the POA&M
- CC6.4 to CC6.8: physical protection (vendor), disposal, boundary protection, encryption in transit, and malware protection

**Not ready:**
- CC2.3: no security contact or commitments published to resellers
- CC7.1 and CC7.2: no vulnerability scanning or monitoring of portal sign-ins
- CC8.1: portal pricing rules and sync mapping change with no approval or log
- A1.3: recovery never tested

**Most important partial item:** CC6.1. MFA is optional for reseller users. The vendor's report makes enforcing MFA a customer responsibility, so this is the company's gap, not the vendor's (R-017).

## 4. Findings from the portal vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-06-30. One exception: 2 of 40 sampled production changes lacked documented approval, remediated in 2026-04.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour, with 99.9% monthly uptime, **meet the company's BIA** for BP-03 (RTO 8 h, RPO 1 h).
- **Controls the company must run.** The report lists complementary user entity controls: enforce MFA for customer users, provision and remove users, review user access, protect API credentials for integrations, review portal audit logs, and report incidents to the vendor. Three are open gaps at the company: reseller MFA (CC6.1), user access review (CC6.2), and log review (CC7.2). **The vendor's controls protect resellers only once those gaps are closed.**
- **Follow-ups:**
  - Obtain a bridge letter through 2026-09-30.
  - Obtain the hosting provider's SOC 2 summary (carved-out subservice organization).
  - Negotiate a 72-hour security incident notice at renewal.

## 5. Remediation plan and evidence calendar
Criteria are grouped by the target dates in `soc2-readiness.csv`.

| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.1, CC1.2, CC1.4, CC1.5, CC2.2, CC2.3, CC3.4, CC4.1, CC5.3, CC6.1, CC6.3, CC7.1, CC7.3 to CC7.5, CC8.1, CC9.1, CC9.2, A1.1, A1.2 | Policy acknowledgments, oversight minutes, reseller security statement, reseller MFA enforcement report, change log, scan reports, triage tickets, tabletop report, contingency plan, vendor review file, capacity note to the vendor, portal configuration exports |
| 2027 Q1 | CC2.1, CC5.1, CC5.2, CC6.2, CC7.2, A1.3 | Log review records, reseller user attestations, closed POA&M items, portal outage exercise report |
| 2027 Q2 | All in-scope criteria | Updated self-assessment with 3 to 6 months of operating evidence, as the base for a possible Type 1 |

**Response to the two resellers:** send this summary, the readiness checklist, the portal vendor's report under its sharing terms, and the relevant POA&M items. Commit to an updated self-assessment in April 2027.
