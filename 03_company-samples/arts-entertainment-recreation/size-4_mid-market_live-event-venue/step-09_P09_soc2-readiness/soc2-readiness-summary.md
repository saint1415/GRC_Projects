# SOC 2 Readiness Summary: Cris Santos Company | Arts, Entertainment, and Recreation | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (live event venue operator with ticketing; private equity-backed; three Florida venues) |
| Tier / Vertical | Mid-Market / Arts, Entertainment, and Recreation |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1), Processing Integrity (PI1) |
| Target reports | SOC 2 **Type 1** as of 2027-06-30, then SOC 2 **Type 2** for the period 2027-07-01 to 2027-12-31 (report expected by 2028-03-31), as the County PAC agreement requires |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 and AOC review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-04 by the vCISO and the GRC Analyst, using P02, P05, P06, and P07 evidence (vendor reviews completed 2026-09-11); accepted by the Chief Operating Officer 2026-09-15 |

## 1. Why SOC 2 for this organization
A venue operator is usually **not** a SOC 2 service organization. It sells tickets and experiences to the public, and its assurance mechanism for card payments is PCI DSS validation (the vertical's assurance alternative, P03). That changes with the County PAC agreement:
- From 2027-07-01 the company operates the county's 2,400-seat performing arts center.
- It will sell County PAC tickets on its own ticketing tenant as merchant of record, hold County PAC patron data, and send the county monthly settlement statements and patron reports.
- The county relies on the company's controls for the security and availability of those services, the confidentiality of its patrons' data, and the accuracy of its remittances. The agreement requires a SOC 2 Type 1 report as of 2027-06-30 and a Type 2 report within 12 months after operations begin.

For those services the company is a service organization, and SOC 2 is the right tool. **Processing Integrity** is in scope because the county's money depends on the settlement calculations (BP-15). **Privacy** is not requested; patron privacy is covered by the FTC Act and Florida analysis in P03.

**SOC 2 does not replace PCI DSS.** The QSA's ROC remains the card data assurance. The SOC 2 system description will refer to the ROC for card data controls, and the evidence is shared: the same access reviews, scans, logs, and change records feed both.

**Why Type 1 first, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in access management, logging, change management, recovery testing, and vendor oversight. Starting the observation period before those are fixed would produce exceptions. The plan is to remediate through 2027 Q1, issue the Type 1 as of 2027-06-30, and run the Type 2 period from the day County PAC operations begin.

**Service auditor independence.** The SOC 2 examination will be performed by an independent CPA firm that is not the co-sourced internal audit firm (P07) and not the QSA, so that neither earlier engagement creates an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Ticket sales, patron data management, and settlement and remittance services for the County PAC; the same TVOP serves the company's own venues |
| Infrastructure | TVOP components (P02): the ticketing tenant configuration, website and tag manager, cloud landing zone, identity provider, networks, endpoints, SIEM |
| Software | Ticketing platform (vendor SaaS), website CMS, patron data platform, settlement application |
| People | Ticketing, finance, and digital staff; the IT and security team; the MSSP; the vCISO; County PAC box office staff (from 2027) |
| Data | County PAC patron records, orders, settlement and remittance data |
| Procedures | POL-01 to POL-05, the standards index, and both P08 runbooks |
| Subservice organizations (carve-out) | Ticketing platform vendor, payment partner, identity provider, cloud provider, MSSP. Their controls are covered by their own SOC 2 reports or PCI DSS AOCs and the complementary subservice organization controls listed in the company's system description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 8 | 18 | 7 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 1 | 4 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **10** | **25** | **8** | **18** |

**Ready (10):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC3.1, CC3.2;
- monitoring of controls: CC4.1, CC4.2;
- control design: CC5.1;
- capacity: A1.1 (the virtual queue and the vendor carried 12,500 tickets in the first hour of the 2026-07-15 on-sale);
- stored processing data: PI1.5.

**Not ready (8):**
- CC2.3: no system description or service commitments for the county; no incident terms with agencies and the tag manager vendor;
- CC3.4: AI features and new tags went live without a change review;
- CC6.3: annual access reviews, transfers keeping roles, departed agency accounts;
- CC7.2: no monitoring of ticketing, tag manager, CMS, or payment partner activity;
- CC7.5 and A1.3: recovery of company workloads untested; manual entry procedures at 1 of 3 venues;
- CC8.1: payment-related settings outside change control;
- CC9.2: no provider responsibility matrix; payment partner AOC from 2024; agencies without security terms.

Each Not ready criterion maps to a P07 POA&M item. The Partially ready criteria mostly depend on the standards being issued (P06) and on the logging work (POAM-007, POAM-008).

**The benchmark tells the same story as the PCI DSS analysis from a different angle:** the company's endpoint and backup controls are strong, and its weak point is how it runs its own edge of the SaaS platforms (accounts, scripts, settings changes, and logs).

**Processing Integrity is the new work.** The company has settled its own shows for years, but the County PAC needs a written settlement specification, automated completeness checks on report imports, a reconciliation from ticketing to settlement to remittance, and a monthly statement format agreed with the county (PI1.1 to PI1.4; P01 R-044).

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies and standards), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each Security, Availability, and Confidentiality criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1, CC6.2, CC6.5, CC6.7, CC6.8, CC7.1, CC8.1, CC5.3, CC2.2 | MFA enforcement reports; agency account approvals; purge records; data loss prevention reports; script inventory and monitoring alerts; scan reports; change tickets for ticketing settings and tag manager publishes; standards and acknowledgments |
| 2027 Q1 | CC1.2, CC1.4, CC2.1, CC2.3, CC3.3, CC3.4, CC5.2, CC6.3, CC6.4, CC6.6, CC7.2, CC7.3, CC7.4, CC7.5, CC9.2, A1.2, A1.3, C1.2 | Quarterly access reviews; SIEM use case alerts; restore test records; tabletop and drill reports; vendor review files and contract amendments; baselines; County system description draft |
| 2027 Q2 | CC9.1, PI1.1, PI1.2, PI1.3, PI1.4, C1.1 | County settlement specification; reconciliation reports from dry runs; County data classification; ticketing vendor renewal terms |
| 2027-06-30 | Type 1 (design) report date | Management's system description and assertion |
| 2027-07-01 to 2027-12-31 | Type 2 observation period | All recurring control evidence (quarterly reviews, scans, restore tests, vendor reviews, monthly County settlements) |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee, and gives the county a quarterly status letter until the Type 1 report is issued.

## 5. Vendor SOC 2 and AOC review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 11 Common/Inherited and 33 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of STD-03.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Card data, content on pages that embed the payment form, more than 10,000 patron records, privileged access to company systems, or support for a High-criticality BIA process | SOC 2 Type 2 (or PCI DSS AOC for card data services, or a questionnaire plus contract terms where no report exists) with a bridge letter; review of opinion, scope, carve-outs, exceptions, customer controls mapped to company controls, availability against the BIA, and incident terms | Annually |
| **Tier 2** | Limited patron data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No patron or card data and no system access | Contract terms only | At contract renewal |

The CSV holds the reviews of 8 Tier 1 providers (the ticketing vendor, the payment partner, the identity provider, the cloud provider, the MSSP, the POS vendor, the tag manager vendor, and the marketing agency) and 1 Tier 2 example (the chatbot vendor). The web agency and the network and security integrator are Tier 1 and are due by 2027-03-31 (POAM-021).

**Key findings:**
1. **Ticketing vendor:** unqualified Type 2 and a Compliant AOC. Its stated RTO of 4 hours and RPO of 15 minutes meet online and box office sales but **not event entry** (BP-01, RTO 0.5 hours), so the manual entry procedure stays the control. Five of the six customer controls the report expects are open gaps at the company (MFA, API credentials, audit log review, content added to pages, prompt user removal). **The vendor's clean report does not protect the company until those close.**
2. **Payment partner:** the AOC on file is from 2024 and too old for the 2026 validation; the 2026 AOC is promised by 2026-10-15. The new keyed-entry P2PE devices must be confirmed as part of the listed solution before go-live.
3. **Tag manager vendor and marketing agency:** the vendor's SOC 2 is clean, but every customer control it expects is open at the company, and the agency has no SOC 2, a shared password list, and no MFA. Together they are the entry point of the first P08 scenario.
4. **MSSP:** unqualified Type 2 with an exception for missed 30-minute escalations in 2 of 40 samples; the SIEM platform is carved out. The MSSP must not act as PFI because of the 3-year independence rule.
5. **POS vendor:** clean report and a listed P2PE solution, but the report does not state offline acceptance rules, which BP-03 depends on (P01 R-019).
