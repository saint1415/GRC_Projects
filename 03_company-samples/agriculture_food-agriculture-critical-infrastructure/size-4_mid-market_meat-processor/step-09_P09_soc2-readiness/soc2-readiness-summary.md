# SOC 2 Readiness Summary: Cris Santos Company | Food and Agriculture | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed meat processor with two USDA-inspected plants) |
| Tier / Vertical | Mid-Market / Food and Agriculture |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| System | Customer Traceability and EDI Services (CTES): the customer traceability portal, the EDI gateway, and the traceability database in the workloads account (P04) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report by 2027-12-31 as the customer contract requires |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-28 by the vCISO and the GRC Analyst, using P02, P04, P05, and P07 evidence and the intake records of the customer agreement and the CTES (EV-051, EV-052); approved by the Chief Financial Officer (executive sponsor) 2026-09-15 |

## 1. Why SOC 2 for a meat processor
A meat processor is usually **not** a SOC 2 service organization. It sells food, not services. That changed when the company built the Customer Traceability and EDI Services:
- 38 customer organizations use the portal for lot lookups, certificates of analysis, and recall notices (P05 BP-11).
- About 1,900 EDI purchase orders and advance ship notices a week pass through the EDI gateway (P05 BP-10).
- The largest grocery chain (about 22% of sales) now relies on those services to run its own traceability and receiving. Its 2026 supply agreement requires a SOC 2 Type 2 report on them by 2027-12-31, covering Security, Availability, and Processing Integrity (P03 G-081).

For those services, the company is a service organization, and SOC 2 is the right assurance tool. **Processing Integrity** matters here more than in most SOC 2 reports, because a wrong lot record or certificate can send a recall to the wrong stores.

**Why not the plants.** The PPCM (P02) is not part of the CTES system. Customers do not use it, and its assurance comes from FSIS inspection, the HACCP program, and this library's P07 assessment. The CTES system description will name the PPCM only as the source of lot and laboratory data.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated over a period. P07 and this assessment found gaps in access reviews, vulnerability management, recovery testing, and vendor oversight. Starting the observation period now would produce exceptions. The plan is to remediate through 2027 Q1, issue a Type 1 report on 2027-03-31 as an interim deliverable, then observe from 2027-04-01.

**Alternatives considered:**
- **Security questionnaire only:** what other customers accept today; not acceptable under the new agreement.
- **ISO/IEC 27001 certification:** broader and slower; the customer named SOC 2.
- **A GFSI scheme audit:** covers food safety, not these IT services.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so the P07 work does not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Customer lot lookups, certificates of analysis, recall notices, EDI purchase orders, advance ship notices, and invoices |
| Infrastructure | Workloads account (portal, EDI gateway, traceability database), shared services and backup accounts (P04) |
| Software | Portal application (developed in house), EDI gateway and partner maps, integration service from the ERP and WMS |
| People | IT team (portal developers, EDI analysts, infrastructure), customer service (8), FSQA for certificate data, Security Manager and MSSP |
| Data | Lot and shipment data, certificates of analysis, customer user accounts, EDI documents with pricing |
| Procedures | POL-01 to POL-05, the standards index, the P08 runbooks |
| Subservice organizations (carve-out) | Cloud provider, EDI network provider, ERP vendor, WMS vendor, identity provider, MSSP. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls in the system description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 12 | 16 | 5 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 0 | 0 | 2 |
| Processing Integrity (PI1, 5) | 1 | 3 | 1 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **14** | **20** | **7** | **20** |

**Ready (14):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC3.1, CC3.2;
- monitoring and control design: CC4.1, CC4.2, CC5.1;
- physical, disposal, and transmission: CC6.4, CC6.5, CC6.7;
- event evaluation: CC7.3 (MSSP escalation tested at 22 minutes in P07);
- capacity: A1.1;
- EDI input validation: PI1.2.

**Not ready (7):**
- CC2.3: no system description or standard customer service commitments;
- CC6.3: annual access reviews and late terminations (P07);
- CC7.1: 11 overdue Critical and High vulnerabilities (P07);
- CC7.5 and A1.3: the traceability database and EDI gateway have never been restore-tested;
- CC9.2: no ongoing review of subservice organizations; the EDI network provider's report not yet received;
- PI1.5: EDI documents kept 90 days only; certificate versions not retained.

Each maps to a P07 POA&M item or to POAM-022 (SOC 2 readiness). The Partially ready criteria mostly depend on standards being issued (P06), portal logs reaching the SIEM, and processing reconciliation between the ERP and the portal.

**Mapping to other work.** Evidence is reused from P02 (control statements), P04 (landing zone controls), P05 (availability objectives for BP-10 and BP-11), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to SP 800-53 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.4, CC2.1, CC2.2, CC3.4, CC6.2, CC6.3, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, A1.3, PI1.5 | Role-based training records; partner reconciliation; policy acknowledgments; quarterly access reviews; upload scanning logs; closed vulnerability tickets; SIEM source list; restore test records; EDI change tickets; retention settings |
| 2027 Q1 | CC1.2, CC2.3, CC3.3, CC5.2, CC5.3, CC6.1, CC6.6, CC9.1, CC9.2, A1.2, PI1.1, PI1.3, PI1.4 | Audit committee minutes; system description and service schedule; privileged access logs; penetration test report; EDI failover procedure; subservice reviews; reconciliation reports; certificate audit trail |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to the customer | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly scans, restore tests, reconciliations, vendor reviews) |

**Status reporting.** The vCISO reports readiness monthly to the CFO and quarterly to the audit committee and the customer.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendors for many controls (P02: 30 Hybrid and 4 Common/Inherited). The program in `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of STD-07.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Access to OT or to the PPCM, hosting of food safety or CTES data, or support for a High-criticality BIA process | SOC 2 Type 2 (or an equivalent independent assessment, or for OT integrators a questionnaire plus on-site review) and a bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability against the BIA, and incident terms | Annually |
| **Tier 2** | Limited data, no OT or privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No data and no system access | Contract terms only | At contract renewal |

Of the 26 vendors with OT, cloud, or data access, 12 are Tier 1, 8 are Tier 2, and 6 are Tier 3. The CSV holds the first 9 Tier 1 reviews and 1 Tier 2 example. The remaining 3 Tier 1 reviews (the Plant 2 integrator and the two refrigeration contractors) are due by 2027-03-31 (POAM-015).

**Key findings:**
1. **Cloud, ERP, WMS, identity provider, and MSSP:** unqualified Type 2 reports. Their recovery commitments meet the BIA. Their controls only protect the company once the company's own complementary controls close: quarterly access reviews (POAM-001), restore tests (POAM-010), and log onboarding (POAM-006).
2. **Cold-chain monitoring vendor:** no SOC 2 report, no recovery commitment, no incident terms, and vendor administrators can edit customer alert rules. The BIA's 1-hour RTO for monitoring cannot be confirmed, so the manual temperature log is the real control (P05 finding 6; P01 R-024).
3. **EDI network provider:** report requested but not received. It is a carve-out subservice organization in the CTES description, so the report is needed before the observation period.
4. **AI vision vendor and Plant 1 integrator:** no SOC 2 (normal for these vendors). The questionnaires and the on-site review found always-on remote tools, unmanaged laptops, and shared credentials, which match the P07 findings (POAM-004, POAM-021).
