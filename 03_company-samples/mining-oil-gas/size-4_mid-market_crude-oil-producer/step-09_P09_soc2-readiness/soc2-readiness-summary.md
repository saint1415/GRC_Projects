# SOC 2 Readiness Summary: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed independent crude oil producer with a Panhandle gathering system) |
| Tier / Vertical | Mid-Market / Mining, Quarrying, and Oil and Gas Extraction |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1) |
| Service in scope | Crude oil gathering and custody transfer measurement services provided to the 5 shippers on the Panhandle gathering system |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-16 by the Security Manager and the GRC Analyst with the Measurement Supervisor, using P02, P05, P06, and P07 evidence |

## 1. Why SOC 2 for this organization
A crude oil producer is not usually a service organization. Its gathering system makes it one:
- The company gathers crude for **5 third-party shippers** (about 1,400 barrels per day), measures it at **6 LACT units**, and publishes **daily volume statements** on the shipper portal. Shippers nominate, sell, and pay royalties on those numbers, so the company's controls affect their financial reporting and operations.
- The **largest shipper asked for a SOC 2 Type 2 report** on gathering and measurement services, covering Security, Availability, Processing Integrity, and Confidentiality (gap 11 in `../00_company-facts.md`).
- The gathering agreements are silent on security and incident notice (gap 8), so a SOC 2 report plus the agreement amendments is how the company will show its commitments.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated over a period. P07 found that the controls this service depends on most (change control over pump station setpoints and flow computers, the vendor modem at the Central Facility, the BCC path around the OT DMZ, and SCADA recovery) are not yet in place. Starting the observation period now would produce exceptions or a qualified opinion. The plan is to remediate through 2027 Q1 and observe from 2027-04-01. The risk appetite sets that date as the target for the measurement integrity risks (P01 R-007, R-021, and R-051 at Low by 2027-04-01).

**Alternatives considered:**
- **Type 1 first (point in time):** offered to the shipper; it accepted quarterly written status updates instead, so the company saves the cost of a Type 1.
- **Security questionnaire only:** the shipper's audit committee asked for independent assurance.
- **SOC 1:** joint interest billing and revenue distribution affect the 22 partners' financial reporting, so a SOC 1 is a later option. It is not in scope now because no partner has asked for one.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is neither the co-sourced internal audit firm (which performed P07) nor the external financial statement auditor. Budget: $240,000 across 2027 (P01 section 4).

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Crude oil gathering on the 92-mile Panhandle system, custody transfer measurement at the Panhandle Central Facility, daily shipper volume statements, and monthly shipper invoicing |
| Infrastructure | OCC SCADA servers and HMIs for the gathering system; the BCC as alternate control site; the gathering pump station PLC; 6 LACT units with flow computers; the OT DMZ; the OT data account (measurement data service, historian replica) and the business workloads account (shipper portal, volume integration service); the backup account (P02, P04) |
| Software | SCADA software; measurement data service; shipper portal; volume integration service; production accounting tenant (shipper invoicing) |
| People | Production Controllers (14), gathering operators and measurement staff (26), the Measurement Supervisor, the Pipeline Compliance Manager, the OCC and BCC staff, IT and security staff, the SCADA and Automation Manager's team |
| Data | Shipper volumes, crude quality, LACT tickets, meter proving records, statements, and invoices (Confidential under POL-04) |
| Procedures | POL-01 to POL-05, the standards index, the P08 runbooks, the pipeline emergency procedures, and the measurement procedures |
| Subservice organizations (carve-out) | Cloud provider, identity provider, production accounting vendor, MDR provider, flow computer vendor, and SCADA integrator. Their controls are covered by their own reports or by the company's oversight (Part B), and the complementary subservice organization controls are listed in the system description |
| Excluded | South Florida and Alabama field operations and truck custody transfer (no shipper service there), royalty owner and employee personal information, and corporate business systems not used by the service |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 18 | 4 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 1 | 3 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **13** | **24** | **6** | **18** |

Privacy is not in scope because the service processes shipper business data, not personal information of consumers.

**Ready (13):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2, CC3.3;
- monitoring and control design: CC4.1, CC4.2, CC5.1;
- malware protection: CC6.8 (P07 SI-3 fully satisfied);
- capacity: A1.1;
- stored measurement data: PI1.5 (ticket hashing and write-once backups).

**Not ready (6):**
- CC6.6: the flow computer vendor's modem at the Central Facility and the BCC path around the OT DMZ (POAM-002, POAM-003);
- CC7.5 and A1.3: SCADA image restore and BCC failover never tested (POAM-004, POAM-005);
- CC8.1: pump station setpoint and flow computer changes not under change control (POAM-007, POAM-008);
- CC9.2: the flow computer vendor, the SCADA integrator, and the compressor packager never assessed (POAM-012);
- PI1.4: statements published without reconciliation, with a single portal administrator (POAM-021).

Each Not ready criterion maps to a P07 POA&M item. Most Partially ready criteria depend on issuing the OT standards (P06) and on the measurement controls in POAM-007 and POAM-021.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments for BP-04 and BP-05), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a mapping between the Trust Services Criteria and SP 800-53 (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC3.4, CC6.2, CC6.3, CC6.4, CC6.7, CC7.3, CC7.4, A1.2, and the vendor path in CC6.6 | Vendor modem removal record; termination checklist; second portal administrator and first shipper access review; tabletop reports; headquarters offline image log |
| 2027 Q1 | CC1.2, CC1.4, CC2.1, CC2.3, CC5.2, CC5.3, CC6.1, CC6.5, CC6.6, CC7.1, CC7.2, CC7.5, CC8.1, CC9.2, C1.1, C1.2, PI1.1 to PI1.4 | OT DMZ at the BCC; STD-02, STD-04, STD-07 issued; setpoint and flow computer change records with second review; nightly configuration capture; daily reconciliation before publishing; image restore test record; OT vendor assessments; signed agreement amendments; system description |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence: quarterly access reviews, monthly proving, daily reconciliations, CAB records, restore tests, failover tests, vendor reviews |
| 2027 Q2 | CC9.1, A1.3 | First full BCC failover test (2027-04-30); 24x7 OT alert coverage (2027-06-30) |

**Status reporting.** The Security Manager reports readiness monthly to the COO and quarterly to the audit committee, and sends a quarterly written status update to the largest shipper.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 11 Common/Inherited and 24 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of the supply chain and vendor risk standard (STD-03). Until 2026 the company reviewed SOC 2 reports for 4 SaaS vendors each year. In 2026 it added the cloud provider and the MDR provider, and it started OT vendor assessments, because OT vendors have no SOC 2 reports.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | SCADA network access, Restricted data at scale, or support for a High-criticality BIA process | SOC 2 Type 2 plus bridge letter (review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability against the BIA, incident terms); for OT vendors without a SOC 2, an OT vendor assessment | Annually |
| **Tier 2** | Limited data or access; supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No data and no system access | Contract terms only | At contract renewal |

Of the 64 vendors with system or data access, about 14 are Tier 1 and about 25 are Tier 2 under this approach (final tiering due 2026-12-31, POAM-012). The CSV holds 10 reviews: 6 vendors with SOC 2 reports, the 3 OT vendors that need OT assessments, and the telematics vendor.

**Key findings:**
1. **Production accounting vendor:** unqualified Type 2 including Processing Integrity. Its RTO of 24 hours and RPO of 1 hour **meet the BIA** for allocations and revenue distribution (P05 finding 5). The company's complementary controls (dual payment approval, call-back on bank changes) operate.
2. **Cloud provider:** unqualified Type 2 for the services in use. It is the most important carve-out for the company's own SOC 2, and the shared responsibility split is mapped in P04.
3. **MDR provider:** unqualified Type 2 (Security only) with one exception for late escalations (2 of 40 samples). OT is excluded from the contract, which is the company's own gap (POAM-009).
4. **OT vendors (SCADA integrator, compressor packager, flow computer vendor):** no SOC 2 reports and never assessed. The packager and flow computer vendor paths caused the P07 stop-and-notify finding and the CC6.6 Not ready rating. All three assessments are due by 2027-03-31.
5. **HR and payroll vendor:** unqualified Type 2. The AI candidate-screening feature (AI-004) is confirmed off, and a feature-change alert is requested so that it cannot be switched on without review (P10).
