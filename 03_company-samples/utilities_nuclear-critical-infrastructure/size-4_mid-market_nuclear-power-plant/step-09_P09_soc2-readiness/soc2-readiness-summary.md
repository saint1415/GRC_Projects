# SOC 2 Readiness Summary: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed owner and operator of a single-unit nuclear generating station) |
| Tier / Vertical | Mid-Market / Nuclear Reactors, Materials, and Waste |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1) |
| System | Generation data and settlement reporting (GDSR) service for the PPA buyers |
| Target report | SOC 2 **Type 2**, first observation period 2027-04-01 to 2027-12-31 (9 months), report by 2028-03-15; calendar-year periods after that. Interim Type 1 report as of 2027-03-31 |
| Part A | Company readiness assessment (`soc2-readiness.csv`, 61 criteria) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`, 10 reviews) |
| Prepared | 2026-09-15 by the Compliance and GRC Lead and the IT Security Manager with the Energy Marketing and Settlements Manager, using P02, P04, P05, and P07 evidence; approved 2026-09-17 by the Site Vice President |

## 1. Why SOC 2 for this organization
A nuclear generating station is not usually a SOC 2 service organization. Its product is electricity, and its main assurance comes from regulators: NRC inspection of the CSP and the security program, Nuclear Oversight's 73.55(m) reviews, and NERC compliance monitoring. None of those gives a power buyer assurance about the **data** the company sends it.

That changes with **PPA-2**. The buyer is a large technology company's energy subsidiary. It buys 40% of the output and the associated clean energy attributes, and it relies on the company's data for its own clean energy claims and settlement:
- **Daily:** hourly net generation and attribute quantities for the prior day, delivered to the buyer's data portal by 10:00.
- **Monthly:** settlement statements to both buyers (PPA-1 and PPA-2).

The PPA-2 data exhibit requires an **annual SOC 2 Type 2 report** on this service, covering Security, Availability, Processing Integrity, and Confidentiality, starting with calendar 2027. For the GDSR service, the company is a service organization and SOC 2 is the right tool. **Processing Integrity matters most:** an error in hourly generation or attribute data flows straight into the buyer's settlement and its public claims.

**Why Type 2, and why not from January 2027.** A Type 2 report tests whether controls operated over a period. Today the service runs on informal controls: analysts edit meter-data scripts directly, manual adjustments are not logged or reviewed, GDSR has never been restored from backup, and its logs do not reach the SIEM (gap 12; P01 R-026, R-028). An observation period that started before those fixes would produce exceptions. The buyer accepted this plan in writing on 2026-09-10:
- remediation through 2027 Q1;
- an **interim Type 1 report as of 2027-03-31**;
- a first Type 2 period of **2027-04-01 to 2027-12-31**, then calendar-year periods;
- quarterly status updates to the buyer.

**Alternatives considered:**
- **Agreed-upon procedures on the monthly settlement data:** cheaper, but gives findings, not an opinion, and the buyer's audit committee asked for SOC 2.
- **SOC 1:** the settlement amounts affect the buyer's financial reporting, so SOC 1 would also be relevant. The buyer asked for SOC 2 because its main concern is data integrity and security, not only financial statement assertions. Management will revisit if a buyer asks for SOC 1.
- **Regulatory and industry assurance:** NRC inspection, 73.55(m) reviews, and NERC audits cover plant safety, security, and reliability, not the buyer's data. The vertical overlay lists no SOC 2 alternative for this business.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so the P07 work does not create an independence question.

**What stays out.** The report describes the GDSR service only. No SGI, no SRI, and no CDA information is in the system or in the system description. The CSP, the plant systems, and the NERC dispatch network are outside the system boundary; the description says only that plant data reaches the business network through a one-way device.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Daily hourly net generation and attribute data to the PPA-2 buyer; monthly settlement statements to both buyers |
| Infrastructure | Cloud workloads account (GDSR virtual machines and database), shared services account (network hub, site-to-cloud VPN), identity and security account, recovery account (backup vault) (P04); settlements analysts' workstations on the business network |
| Software | GDSR application, database, and meter-data scripts; cloud identity provider and privileged access broker; EDR and SIEM |
| Data sources | Settlement-quality hourly revenue meter data downloaded daily from the interconnecting transmission owner's meter data portal (there is no connection between the dispatch network and GDSR); historian replica data (SYS-09) used for validation and for estimates when meter data is late |
| People | Energy Marketing and Settlements Manager and 3 settlements analysts; 2 IT application developers; IT infrastructure and security staff; the MSSP |
| Data | Hourly generation and attribute quantities, settlement statements, buyer contact data (Confidential under POL-04). No personal information beyond business contacts |
| Procedures | POL-01 to POL-05, the standards index, the P08 runbooks, and the GDSR operating procedures (due 2027-01-31) |
| Subservice organizations (carve-out) | Public cloud provider (VEN-01), cloud identity provider (VEN-02), MSSP (VEN-03). Their controls are covered by their SOC 2 reports and listed as complementary subservice organization controls |
| Outside the system | The transmission owner's meter data portal and the buyer's data portal (external parties); the plant historian and the one-way device (CSP scope) |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 15 | 13 | 5 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Processing Integrity (PI1, 5) | 0 | 4 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **17** | **19** | **7** | **18** |

**Ready (17):**
- governance and risk: CC1.1, CC1.2, CC1.3, CC1.5, CC3.1, CC3.2;
- monitoring and control selection: CC4.1, CC4.2, CC5.1;
- access, physical, disposal, transmission, and malware: CC6.2, CC6.4, CC6.5, CC6.7, CC6.8;
- continuity and capacity: CC9.1, A1.1, A1.2.

**Not ready (7):**
- CC6.3: GDSR roles never reviewed; transfers keep prior roles (POAM-001);
- CC7.1: GDSR virtual machines not scanned (POAM-015);
- CC7.2: GDSR logs not in the SIEM (POAM-005);
- CC7.5 and A1.3: GDSR never restored or failover-tested (POAM-010);
- CC8.1: scripts edited directly in production (POAM-007);
- PI1.3: manual adjustments not logged or reviewed (R-026).

Each Not ready item maps to a P07 POA&M item; all are tracked together under POAM-022. The 19 Partially ready criteria mostly depend on written GDSR procedures and processing specifications, standards still in draft (P06), and the vendor reviews in Part B.

**The company's strengths carry over.** The governance, risk assessment, independent assessment, physical protection, endpoint protection, and encryption controls built for the Station and the business network are Ready. The gaps are in the GDSR service itself, which grew as an analyst tool and never went through IT's controls.

**Mapping to other work.** Evidence is reused from P02 (control statements), P04 (cloud responsibilities), P05 (BP-11 recovery objectives), P06 (policies), P07 (test results), and P08 (incident procedures, including the PPA-2 48-hour notice). The `related_sp800_53` column links each criterion to SP 800-53 controls; this mapping is the author's.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC3.3, CC3.4, CC6.3, CC7.1, CC7.2, CC7.3, CC7.4, CC8.1, PI1.3, CC2.1 | Adjustment log with second reviewer; pull requests and pipeline deployments for scripts; first quarterly GDSR access review; monthly scans of GDSR virtual machines; SIEM alerts on GDSR logs; tabletop report with the GDSR inject; data flow diagram |
| 2027 Q1 | CC1.4, CC2.2, CC2.3, CC5.2, CC5.3, CC6.1, CC6.6, CC7.5, CC9.2, A1.3, PI1.1, PI1.2, PI1.4, PI1.5, C1.1, C1.2 | Training records; GDSR operating procedures and processing specification; system description and assertion; configuration baselines; named database administrator accounts; restore test record (by 2027-02-15); vendor reviews; input completeness checks; pre-delivery checks; immutable delivered-file copies; labels and retention rule |
| 2027-03-31 | Type 1 report (design) as an interim deliverable to the PPA-2 buyer | Management's system description and assertion |
| 2027-04-01 to 2027-12-31 | First Type 2 observation period | All recurring control evidence (daily delivery checks, adjustment reviews, quarterly access reviews, monthly scans, restore test, vendor reviews) |

**Cost and ownership.** About $240,000 across 2027 for readiness work, the Type 1 and Type 2 examinations, and tooling (POAM-022). The Energy Marketing and Settlements Manager owns readiness; the Compliance and GRC Lead runs the evidence calendar.

**Status reporting.** Monthly to the Site Vice President, quarterly to the audit committee and the PPA-2 buyer. Risk R-028 stays Moderate until the Type 1 report is issued.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 16 Common/Inherited and 17 Hybrid statements; P04 Provider and Shared rows). The program in `vendor-soc2-review.csv` makes that reliance evidence-based. It is the core of the vendor risk standard (STD-03, due 2026-12-31).

**Tiering approach (STD-03):**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Network access, Restricted data, or support for a High-criticality BIA process | SOC 2 Type 2 (or an equivalent independent assessment) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Confidential data, no network access | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | Neither | Contract terms only | At contract renewal |

**CDA suppliers are not in this program.** Suppliers of CDAs and their services stay under the CSP supply chain procedures run by engineering procurement and the CST. This program covers business IT, cloud, and data vendors.

Of about 210 vendors with network or data access, 24 are Tier 1. The CSV holds the first 9 Tier 1 reviews and 1 Tier 2 example. Four of the 9 Tier 1 vendors reviewed have no current SOC 2 report or equivalent (VEN-04, VEN-06, VEN-07, VEN-08); the other 5 of the 9 without current assurance found in P07 are among the 15 Tier 1 reviews still to do, all due by 2027-03-31 (POAM-016).

**Key findings:**
1. **ERO callout service (VEN-06):** its last SOC 2 report ended 2025-03-31, so it is not current. Its 99.9% availability commitment does not show it can support a 1-hour MTD for BP-08 without the printed call tree. This supports the second callout path (POAM-019) and P01 R-007 as High.
2. **WMS vendor (VEN-04) and predictive maintenance vendor (VEN-07):** no SOC 2 reports, no incident notice terms, and shared VPN support accounts (POAM-003). Both are Tier 1 because of network access. Security addenda are required at renewal or before any pilot expansion (P10).
3. **MSSP (VEN-03):** unqualified, with 3 of 40 high-severity escalations late. Log source coverage is the company's own complementary control and is incomplete (POAM-005). The CST must be added to the escalation list for boundary events (R-037).
4. **Personal information vendors (VEN-05, VEN-08):** neither contract meets the 10-day breach notice in Fla. Stat. 501.171(6). Amendments are due 2027-03-31 (G-081). The background screening vendor has only a Type 1 report.
5. **Cloud provider, identity provider, productivity suite (VEN-01, VEN-02, VEN-09):** unqualified reports. Their protection depends on company controls that are still open: cloud scanning (POAM-015), phishing-resistant MFA for administrators (POAM-002), and SRI labels and DLP (POAM-020).
