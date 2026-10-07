# SOC 2 Readiness Summary: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (radioactive and hazardous waste processor) |
| Tier / Vertical | Small / Nuclear Reactors, Materials, and Waste |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. This is a **self-benchmark**, not preparation for a CPA-issued SOC 2 report |
| Part A | Security-only self-benchmark (`soc2-readiness.csv`) |
| Part B | Waste tracking vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager |

## 1. Why SOC 2 (or an alternative) for this organization
**The company is not a SOC 2 service organization in the usual sense.** SOC 2 reports on the controls of a system that a service organization operates for its customers, where those controls matter to the customers' own security or compliance. The company's service is physical: it receives, treats, stores, and ships radioactive and hazardous waste. Customers do not use a company system to process their own data. The records the company produces for them (certificates of processing, manifests) are covered by the waste tracking vendor's platform and by regulation.

**How customers actually get assurance.** Generators rely on:
- the company's Florida radioactive materials license and its inspection history;
- its RCRA permit;
- its DOT compliance;
- for the reactor customers, supplier audits under their own programs.

The vertical overlay lists no SOC 2 alternative for this business, and none was found that fits better.

**Why the TSC are still used here:**
- **A. Customer questionnaire.** One reactor customer's 2026 supplier security questionnaire asked for evidence of security controls. The General Manager chose to answer with a TSC Security self-benchmark and the POA&M (P07) rather than a custom narrative. The benchmark is honest about status and gives a structure the customer's reviewers recognize. No CPA report is planned: it would cost more than the request needs, and the controls were mostly defined in August 2026, so a Type 2 period could not start until 2027 anyway.
- **B. Third-party risk management.** The waste tracking vendor holds the company's system of record for manifests and containers. Its SOC 2 Type 2 report is the evidence for the controls P02 and P04 mark as inherited. The company reviews it every year (POL-01 4.9, SA-9).

**Categories.** Only Security is in scope. Availability, Confidentiality, Processing Integrity, and Privacy are marked N/A with reasons in the CSV. The company makes no system commitments to customers in those areas, and confidentiality of Part 37 information is assessed against Part 37 itself in P03.

## 2. System description (scope)
- **Services:** waste receiving, processing, storage, and shipment for about 450 generator accounts, plus disused sealed source recovery.
- **Infrastructure and software:** the Business Operations and Records Platform (SSP, P02), including the physical security systems while they share the business network. Plant OT is covered by P03 section C, not by this benchmark.
- **People:** 60 workforce members, the MSP, and the security system and controls vendors.
- **Data:** customer waste profiles and manifests, Part 37 security-related information, background investigation records, and financial data.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 16 | 7 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.1 and CC1.3: ethics, sanctions, and designated roles
- CC2.3: external commitments
- CC3.1 and CC3.2: objectives and risk assessment
- CC4.2: deficiencies tracked
- CC5.1: controls selected from the risk assessment
- CC6.2: account authorization
- CC6.4: physical access (the Part 37 security zone)
- CC6.5: disposal

**Not ready:**
- CC6.1: security-related information readable by 23 users
- CC6.3: late removals and excess access
- CC3.4: changes not assessed (the predictive maintenance gateway)
- CC7.1 and CC7.2: no vulnerability management or monitoring beyond endpoints
- CC7.5: unproven recovery
- CC8.1: no change management

## 4. Findings from the waste tracking vendor report (Part B)
- **Opinion:** Type 2, unqualified. One late quarterly access review at the vendor, remediated.
- **Availability:** the vendor's stated RTO of 8 hours and RPO of 1 hour **meet the BIA** for waste receiving (BP-03: RTO 8 h, RPO 4 h).
- **Controls the company must run.** The report lists complementary user entity controls: user and role administration, MFA through the customer's identity provider, periodic access reviews, and protection of exported reports. Periodic access review is an open company gap (POAM-006). **The vendor's controls protect the company's records only once that gap is closed.**
- **Follow-ups:**
  - Obtain the e-signature subservice provider's assurance summary.
  - Confirm that the manifest change history can be exported at contract end, to support RCRA record retention (40 CFR 264.74).
  - Negotiate 24-hour incident notice at renewal.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q3-Q4 | CC6.1, CC6.3, CC6.7, CC2.2, CC7.3-7.4 | Restricted library membership and access log reviews, termination checklists, policy acknowledgments, tabletop report |
| 2027 Q1 | CC6.6, CC7.1, CC7.5, CC8.1, CC9.2 | Security VLAN change records, scan reports, restore test records, change log, vendor addenda |
| 2027 Q2 | CC7.2, CC3.3, CC1.2 | Log monitoring alerts and tickets, fraud scenarios in the risk update, oversight meeting minutes |

**Response to the reactor customer:** send this summary, the readiness checklist, and the POA&M (P07), with a commitment to an updated self-benchmark in April 2027. Part 37 security-related information is **not** shared with the customer. The responses describe the controls without revealing the security plan (POL-04 4.1).
