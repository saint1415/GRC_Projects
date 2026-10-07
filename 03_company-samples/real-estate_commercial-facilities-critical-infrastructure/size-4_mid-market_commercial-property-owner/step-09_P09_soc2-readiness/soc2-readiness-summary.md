# SOC 2 Readiness Summary: Cris Santos Company | Commercial Facilities | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial office and retail property owner-operator) |
| Tier / Vertical | Mid-Market / Commercial Facilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report delivered by 2027-12-31 as the JV management agreement requires |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-15 by the vCISO and the GRC Analyst, using P02, P05, P06, and P07 evidence |

## 1. Why SOC 2 for this organization
A property owner is usually **not** a SOC 2 service organization: it leases space to tenants rather than providing services to other businesses. That changes for the joint venture:
- An institutional investor and the company own Tower 3, Tower 4, Retail 5, and Mixed-Use 2 through a JV.
- The company is the JV's property manager. It runs leasing, tenant services, building operations (BAS, access control, video, the SCC), and accounting for the JV properties on its own systems.
- The JV management agreement (amended 2026-05) requires a SOC 2 Type 2 report on those **property management and building operations services**, covering Security, Availability, and Confidentiality, by 2027-12-31. It also requires a SOC 1 report on rent billing and accounting, which the CFO is preparing separately with the property management system vendor's SOC 1 as a key input.

For those services, the company is a service organization and the JV is its user entity, so a SOC 2 Type 2 report is the right assurance tool.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in recovery, access reviews, OT monitoring, remote access, and vendor oversight. Starting the observation period before those are fixed would produce exceptions or a qualified opinion. The plan is to remediate through 2027 Q1 and run a 6-month observation period from 2027-04-01.

**Alternatives considered:**
- **Type 1 first (point in time, 2027-03-31):** offered to the JV partner as an interim report. The partner accepted this plan with quarterly status updates.
- **A security questionnaire or the P07 internal audit report:** not acceptable to the JV partner's investment committee, which requires an independent CPA examination.
- **ISO/IEC 27001 certification:** not requested by the partner, and it would not replace the SOC 2 requirement in the agreement.

**Service auditor independence.** The SOC 2 examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so that the P07 work does not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Property management and building operations services provided to the JV for its 4 properties |
| Infrastructure | BAACS components serving the JV properties (Platform A at Tower 3, Tower 4, and Mixed-Use 2; Platform B at Retail 5), the access control and video platform, the SCC at Tower 1, the SD-WAN, and the cloud landing zone (P04) |
| Software | Access control and video platform, BAS Platforms A and B, property management and accounting system, identity provider, tenant experience app, visitor management |
| People | Security operations, engineering, property management, IT and security teams, the MSSP, the vCISO |
| Data | JV tenant and tenant employee data, credential records, video, leases, building drawings, JV reports |
| Procedures | POL-01 to POL-05, the standards index, and the P08 runbooks |
| Subservice organizations (carve-out) | Access control and video platform vendor, cloud provider, identity provider, MSSP, property management system vendor. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls listed in the company's system description |

Retail 5 is on BAS Platform B, so the Platform B gaps (Integrator B access, backups, unsupported servers) are inside the SOC 2 scope. That is one more reason the Platform B work in the P03 roadmap comes first.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 17 | 5 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **12** | **20** | **6** | **23** |

**Ready (12):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2;
- monitoring of controls: CC4.1, CC4.2;
- control design: CC5.1;
- access registration and transmission: CC6.2, CC6.7;
- capacity: A1.1.

**Not ready (6):**
- CC6.3: access reviews, termination gaps, and stale tenant credentials;
- CC6.6: Integrator B's always-on remote access and the Park 2 internet exposure;
- CC7.2: no OT or access platform administrator monitoring;
- CC7.5 and A1.3: recovery is not documented or tested;
- CC9.2: vendor management.

Each maps to a P07 POA&M item. Most Partially ready criteria depend on the same three projects: Platform B remediation (gateway, backups, upgrade), OT visibility (inventory and logging), and the standards set (P06).

**N/A (23).** Processing Integrity was not requested; rent billing and accounting are covered by the separate SOC 1. Privacy was not requested; personal information is governed by POL-04 and Fla. Stat. 501.171, and the Privacy category can be added later if the JV partner asks.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.6 (Integrator B on the gateway; Park 2 closed), CC6.3 (termination workflow, first quarterly reviews, tenant recertification), CC6.5 and C1.2 (retention), CC7.3 (decision log), CC3.3, CC9.1 (contingency plan) | Gateway session records; external scan reports; review sign-offs; tenant recertification reports; purge logs; decision log; contingency plan approval |
| 2027 Q1 | CC1.2, CC1.4, CC2.1, CC2.3, CC3.4, CC5.3, CC6.4, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.2, A1.2, A1.3, C1.1 | Quarterly audit committee minutes; training records; OT inventory; SIEM source list with OT; standards; tabletop reports; restore test records; OT change tickets; signed vendor addenda and Tier 1 reviews; management's system description |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to the JV partner | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence (quarterly reviews and recertifications, monthly scans, quarterly restore tests, gateway approvals, vendor reviews) |
| 2027 Q2 | CC5.2, CC6.1, CC6.8 (segmentation and Platform B upgrade at Retail 5 finish by 2027-06-30, inside the observation period) | Firewall rule reviews; EDR coverage reports |

**Risk to the timeline.** CC6.1, CC5.2, and CC6.8 depend on the Platform B upgrade and the segmentation of Retail 5, which finish during the observation period. The service auditor may report exceptions for the first months. Two options are on the table for the COO: move the Retail 5 work to the front of the Platform B schedule (preferred, decided by 2026-12-31), or describe Retail 5's Platform B controls as a carved-out area for the first report.

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee and the JV partner.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 14 Common/Inherited and 22 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of the vendor risk standard (STD-05).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Privileged or remote access to building systems, personal information at scale (more than 10,000 people), or support for a High-criticality BIA process | SOC 2 Type 2 (or, where none exists, a security questionnaire plus company-side compensating controls) and a bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited access or data, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No access and no data | Contract terms only | At contract renewal |

Of the 41 vendors with access or data, 12 are Tier 1 and 17 are Tier 2. The CSV holds the first 9 Tier 1 reviews (September 2026) and 1 Tier 2 example. The remaining 3 Tier 1 reviews (SD-WAN provider, payroll provider, energy optimization vendor) are due by 2027-03-31 (POAM-016).

**Key findings:**
1. **Access control and video platform vendor (VEN-02):** unqualified Type 2, but its stated RTO of 8 hours **does not meet the BIA** (RTO 2 hours for administration). Confidentiality is not in the report scope, and the analytics features (AI-001, AI-002) were released after the period. Three of the complementary user entity controls are open company gaps: administrator count, audit log review, and retention.
2. **BAS Integrator B (VEN-07):** no report, no contract security terms, an always-on tool, and the only copies of controller programs. It is the single most urgent vendor action.
3. **Tenant experience app vendor (VEN-08):** **qualified** opinion on change management. Because the app issues mobile credentials, a bad change could issue or fail to revoke credentials. Reassess in 6 months.
4. **Visitor management vendor (VEN-09):** only a Type 1 report and no breach notice terms, while it holds the largest personal information store (about 610,000 records).
5. **Integrators without SOC 2 reports (VEN-06, VEN-07):** small integrators rarely have one. The company compensates with its own controls (gateway, approval, recording) and requires questionnaires and contract terms instead.
